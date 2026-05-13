"""
Download WestlakeNLP/DeepReview-13K and produce two on-disk datasets:

  ../deepreview_13k_calibration/  <- from `train` split, mimics ../human_reviews/
      <paper_id>.md  (one markdown file per paper, with `- Scores:` line so
                      build_score_index parses it)
  ../deepreview_13k/               <- from `test` split, mimics ../iclr2025/
      papers/<paper_id>.txt        (raw paper content)
      human_reviews/<paper_id>.md  (formatted human reviews, same shape as
                                    iclr2025/human_reviews/*.md)
      ratings.csv                  (paper_id,title,decision,gt_binary,
                                    avg_score,score_0..score_5)

Then build the calibration pkls in the new/ dir:
  human_review_score_index_deepreview.pkl   {filename: avg_score}
  human_reviews_embeddings_deepreview.pkl   {filename: embedding_vector}

The embedding model + provider matches build_embeddings.ipynb
(google/gemini-embedding-001 via OpenRouter).
"""

import csv
import json
import os
import pickle
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import dotenv
import tqdm
from datasets import load_dataset
from openai import OpenAI

dotenv.load_dotenv()

from paths import DATASETS_DIR
CAL_DIR = (DATASETS_DIR / "deepreview_13k_calibration").resolve()
TEST_DIR = (DATASETS_DIR / "deepreview_13k_test").resolve()
SCORE_INDEX_PATH = DATASETS_DIR / "human_review_score_index_deepreview.pkl"
EMBEDDINGS_PATH = DATASETS_DIR / "human_reviews_embeddings_deepreview.pkl"

REVIEW_FIELDS = [
    "summary",
    "strengths",
    "weaknesses",
    "questions",
    "limitations",
    "soundness",
    "presentation",
    "contribution",
    "rating",
    "confidence",
]


def extract_title(user_content: str) -> str:
    marker = r"\title{"
    if marker in user_content:
        start = user_content.index(marker) + len(marker)
        depth = 1
        i = start
        while i < len(user_content) and depth > 0:
            ch = user_content[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return user_content[start:i].strip().replace("\n", " ")
            i += 1
    return ""


def first_user_content(inputs_json: str) -> str:
    msgs = json.loads(inputs_json)
    for m in msgs:
        if m.get("role") == "user":
            return m.get("content", "")
    return ""


def format_human_reviews_md(reviewer_comments: list[dict]) -> str:
    sections = []
    for i, rc in enumerate(reviewer_comments, start=1):
        content = rc.get("content", {}) or {}
        rating = rc.get("rating", content.get("rating", ""))
        confidence = content.get("confidence", "")
        parts = [f"## Human Reviewer {i}"]
        if rating != "":
            parts.append(f"### Rating\n{rating}")
            parts.append(f"### Rating Number\n{rating}")
        if confidence != "":
            parts.append(f"### Confidence\n{confidence}")
        for field in REVIEW_FIELDS:
            if field in ("rating", "confidence"):
                continue
            v = content.get(field, "")
            if v in ("", None):
                continue
            parts.append(f"### {field.replace('_',' ').title()}\n{v}")
        sections.append("\n\n".join(parts))
    return "\n\n---\n\n".join(sections)


def build_md(title: str, decision: str, scores: list[int], avg: float,
             abstract: str, reviewer_comments: list[dict]) -> str:
    lines = [
        f"# {title}",
        "",
        f"- Decision: {decision}",
        f"- Avg Score: {avg:.2f}",
        f"- Scores: {', '.join(str(s) for s in scores)}",
        "",
        "## Abstract",
        abstract,
        "",
        "## Human Reviews",
        "",
        format_human_reviews_md(reviewer_comments),
    ]
    return "\n".join(lines).strip() + "\n"


def extract_abstract(user_content: str) -> str:
    open_marker = r"\begin{abstract}"
    close_marker = r"\end{abstract}"
    if open_marker in user_content and close_marker in user_content:
        a = user_content.index(open_marker) + len(open_marker)
        b = user_content.index(close_marker)
        return user_content[a:b].strip()
    return ""


def gt_binary_from_decision(decision: str) -> str:
    if not decision:
        return "Reject"
    return "Accept" if "accept" in decision.lower() else "Reject"


def coerce_scores(raw) -> list[int]:
    out: list[int] = []
    if not raw:
        return out
    if isinstance(raw, str):
        raw = json.loads(raw)
    for s in raw:
        try:
            if isinstance(s, str):
                tok = s.split(":", 1)[0].strip()
                out.append(int(tok))
            else:
                out.append(int(s))
        except (ValueError, TypeError):
            continue
    return out


def write_calibration(train_split):
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Writing calibration set to {CAL_DIR} ({len(train_split)} papers)...")
    written = 0
    for ex in tqdm.tqdm(train_split):
        pid = ex["id"]
        scores = coerce_scores(ex["rating"])
        if not scores:
            continue
        avg = sum(scores) / len(scores)
        user_content = first_user_content(ex["inputs"])
        title = extract_title(user_content) or pid
        abstract = extract_abstract(user_content)
        try:
            rc = json.loads(ex["reviewer_comments"]) if ex["reviewer_comments"] else []
        except json.JSONDecodeError:
            rc = []
        md = build_md(title, ex["decision"] or "", scores, avg, abstract, rc)
        (CAL_DIR / f"{pid}.md").write_text(md, encoding="utf-8")
        written += 1
    print(f"  wrote {written} calibration md files")


def write_test(test_split):
    papers_dir = TEST_DIR / "papers"
    reviews_dir = TEST_DIR / "human_reviews"
    papers_dir.mkdir(parents=True, exist_ok=True)
    reviews_dir.mkdir(parents=True, exist_ok=True)
    ratings_path = TEST_DIR / "ratings.csv"

    print(f"Writing test set to {TEST_DIR} ({len(test_split)} papers)...")
    with open(ratings_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "paper_id", "title", "decision", "gt_binary", "avg_score",
            "score_0", "score_1", "score_2", "score_3", "score_4", "score_5",
        ])
        written = 0
        for ex in tqdm.tqdm(test_split):
            pid = ex["id"]
            scores = coerce_scores(ex["rating"])
            if not scores:
                continue
            avg = sum(scores) / len(scores)
            user_content = first_user_content(ex["inputs"])
            title = extract_title(user_content) or pid
            try:
                rc = json.loads(ex["reviewer_comments"]) if ex["reviewer_comments"] else []
            except json.JSONDecodeError:
                rc = []

            (papers_dir / f"{pid}.txt").write_text(user_content, encoding="utf-8")

            review_md_lines = [
                f"# {title}",
                "",
                f"- Decision: {ex['decision'] or ''}",
                f"- Scores: {', '.join(str(s) for s in scores)}",
                "",
                "## Abstract",
                extract_abstract(user_content),
                "",
                "## Human Reviews",
                "",
                format_human_reviews_md(rc),
            ]
            (reviews_dir / f"{pid}.md").write_text(
                "\n".join(review_md_lines).strip() + "\n", encoding="utf-8"
            )

            scores_padded = [str(s) for s in scores] + [""] * (6 - len(scores))
            w.writerow([
                pid, title, ex["decision"] or "", gt_binary_from_decision(ex["decision"] or ""),
                f"{avg:.2f}", *scores_padded[:6],
            ])
            written += 1
    print(f"  wrote {written} test paper+review pairs and ratings.csv")


def build_score_index():
    print(f"Building score index from {CAL_DIR}...")
    idx: dict[str, float] = {}
    for name in sorted(os.listdir(CAL_DIR)):
        if not name.endswith(".md"):
            continue
        text = (CAL_DIR / name).read_text(errors="replace")
        score_line = next(
            (ln for ln in text.splitlines() if ln.startswith("- Scores:")), None
        )
        if not score_line:
            continue
        body = score_line[len("- Scores:"):].strip()
        scores = []
        for tok in body.split(","):
            tok = tok.strip()
            if not tok:
                continue
            try:
                scores.append(float(tok))
            except ValueError:
                pass
        if not scores:
            continue
        idx[name] = sum(scores) / len(scores)
    with open(SCORE_INDEX_PATH, "wb") as f:
        pickle.dump(idx, f)
    print(f"  score index: {len(idx)} entries -> {SCORE_INDEX_PATH}")


def build_embeddings():
    print(f"Building embeddings from {CAL_DIR}...")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    db: dict[str, list[float]] = {}
    if EMBEDDINGS_PATH.exists():
        with open(EMBEDDINGS_PATH, "rb") as f:
            db = pickle.load(f)
        print(f"  resuming with {len(db)} existing embeddings")

    review_files = sorted(p for p in os.listdir(CAL_DIR) if p.endswith(".md"))

    def embed_one(name: str):
        if name in db:
            return name, db[name]
        path = CAL_DIR / name
        content = path.read_text(errors="replace")
        backoff = 1.0
        while True:
            try:
                resp = client.embeddings.create(
                    model="google/gemini-embedding-001",
                    input=content,
                    encoding_format="float",
                )
                return name, resp.data[0].embedding
            except Exception as e:
                print(f"  embed error {name}: {e}; retry in {backoff:.1f}s")
                time.sleep(backoff + random.uniform(0, 1))
                backoff = min(backoff * 1.5, 30)

    todo = [n for n in review_files if n not in db]
    print(f"  {len(todo)} files to embed (of {len(review_files)})")

    save_every = 500
    done_since_save = 0
    with ThreadPoolExecutor(max_workers=50) as ex:
        futures = {ex.submit(embed_one, n): n for n in todo}
        for fut in tqdm.tqdm(as_completed(futures), total=len(futures)):
            name, vec = fut.result()
            db[name] = vec
            done_since_save += 1
            if done_since_save >= save_every:
                with open(EMBEDDINGS_PATH, "wb") as f:
                    pickle.dump(db, f)
                done_since_save = 0

    with open(EMBEDDINGS_PATH, "wb") as f:
        pickle.dump(db, f)
    print(f"  embeddings: {len(db)} entries -> {EMBEDDINGS_PATH}")


def main():
    print("Loading WestlakeNLP/DeepReview-13K...")
    ds = load_dataset("WestlakeNLP/DeepReview-13K")
    print(ds)

    write_calibration(ds["train"])
    write_test(ds["test"])
    build_score_index()
    build_embeddings()
    print("Done.")


if __name__ == "__main__":
    main()
