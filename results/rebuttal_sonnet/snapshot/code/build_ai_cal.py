"""
Build a calibration set whose reviews are AI-generated (from results/fresh_cal/)
but whose scores/decisions are taken from the matching human reviews in
datasets/deepreview_13k_calibration/.

Outputs:
  datasets/ai_review_cal/<paper_id>.md
  datasets/human_review_score_index_ai_cal.pkl
  datasets/human_reviews_embeddings_ai_cal.pkl
"""

import os
import pickle
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import dotenv
import tqdm
from openai import OpenAI

from paths import DATASETS_DIR, RESULTS_DIR

dotenv.load_dotenv()

AI_REVIEWS_DIR = (RESULTS_DIR / "fresh_cal").resolve()
HUMAN_CAL_DIR = (DATASETS_DIR / "deepreview_13k_calibration").resolve()
OUT_DIR = (DATASETS_DIR / "ai_review_cal").resolve()
SCORE_INDEX_PATH = DATASETS_DIR / "human_review_score_index_ai_cal.pkl"
EMBEDDINGS_PATH = DATASETS_DIR / "human_reviews_embeddings_ai_cal.pkl"


_SCORE_HEADER_RE = re.compile(r"^\s{0,3}#{1,6}\s*Score and Decision", re.IGNORECASE)
_FINAL_SCORE_RE = re.compile(r"MY FINAL SCORE", re.IGNORECASE)
_SCORE_TAG_RE = re.compile(r"<score>")


def strip_ai_score(text: str) -> str:
    """Remove the AI's score/decision section from the end of the review."""
    lines = text.splitlines()
    cut = None
    for i, ln in enumerate(lines):
        if _SCORE_HEADER_RE.search(ln) or _FINAL_SCORE_RE.search(ln) or _SCORE_TAG_RE.search(ln):
            cut = i
            break
    if cut is None:
        raise ValueError("no score/decision marker found")
    return "\n".join(lines[:cut]).rstrip() + "\n"


def parse_human_meta(human_path: Path) -> tuple[str, float, list[float]]:
    """Return (decision, avg_score, scores) parsed from a human review file."""
    text = human_path.read_text(errors="replace")
    decision = ""
    scores: list[float] = []
    avg: float | None = None
    for ln in text.splitlines():
        if ln.startswith("- Decision:"):
            decision = ln[len("- Decision:"):].strip()
        elif ln.startswith("- Avg Score:"):
            try:
                avg = float(ln[len("- Avg Score:"):].strip())
            except ValueError:
                pass
        elif ln.startswith("- Scores:"):
            body = ln[len("- Scores:"):].strip()
            for tok in body.split(","):
                tok = tok.strip()
                if not tok:
                    continue
                try:
                    scores.append(float(tok))
                except ValueError:
                    pass
    if not scores:
        raise ValueError(f"no scores parsed from {human_path}")
    if avg is None:
        avg = sum(scores) / len(scores)
    return decision, avg, scores


def build_files() -> dict[str, float]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    score_index: dict[str, float] = {}
    skipped_no_human = 0
    skipped_no_score = 0
    written = 0
    for name in sorted(os.listdir(AI_REVIEWS_DIR)):
        if not name.endswith(".md"):
            continue
        ai_path = AI_REVIEWS_DIR / name
        human_path = HUMAN_CAL_DIR / name
        if not human_path.exists():
            skipped_no_human += 1
            continue
        ai_text = ai_path.read_text(errors="replace")
        try:
            stripped = strip_ai_score(ai_text)
        except ValueError:
            skipped_no_score += 1
            continue
        decision, avg, scores = parse_human_meta(human_path)
        score_str = ", ".join(
            (str(int(s)) if float(s).is_integer() else f"{s:g}") for s in scores
        )
        header = [
            f"- Decision: {decision}",
            f"- Avg Score: {avg:.2f}",
            f"- Scores: {score_str}",
            "",
        ]
        out_text = "\n".join(header) + stripped
        (OUT_DIR / name).write_text(out_text)
        score_index[name] = avg
        written += 1
    with open(SCORE_INDEX_PATH, "wb") as f:
        pickle.dump(score_index, f)
    print(f"Wrote {written} files -> {OUT_DIR}")
    print(f"  no matching human review: {skipped_no_human}")
    print(f"  no AI score marker:       {skipped_no_score}")
    print(f"Score index -> {SCORE_INDEX_PATH} ({len(score_index)} entries)")
    return score_index


def build_embeddings(filenames: list[str]) -> None:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    db: dict[str, list[float]] = {}
    if EMBEDDINGS_PATH.exists():
        with open(EMBEDDINGS_PATH, "rb") as f:
            db = pickle.load(f)
        print(f"  resuming with {len(db)} existing embeddings")

    def embed_one(name: str):
        if name in db:
            return name, db[name]
        content = (OUT_DIR / name).read_text(errors="replace")
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

    todo = [n for n in filenames if n not in db]
    print(f"  {len(todo)} files to embed (of {len(filenames)})")

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
    print(f"Embeddings -> {EMBEDDINGS_PATH} ({len(db)} entries)")


if __name__ == "__main__":
    idx = build_files()
    build_embeddings(sorted(idx.keys()))
    print("Done.")
