import concurrent.futures
import json
import os
import random
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_ROOT = Path(__file__).resolve().parents[1]

REVIEW_DIR = Path("/home/wg25r/split_review_opus_repro/results/2026_sonnet_repro/reviews")
REVIEW_GLOB = "*.md"
PAPER_ID_SUFFIX = ""
PAPER_DIR = Path("/home/wg25r/review_agent/iclr2026_cspaper_new/papers")
GUIDELINE_PATH = SCRIPT_ROOT / "outputs/weakness_reliability_guideline.md"
OUTPUT_PATH = SCRIPT_ROOT / "outputs/sonnet_with_paper_weaknesses.jsonl"
SAMPLED_IDS_PATH = SCRIPT_ROOT / "outputs/sonnet_subset_ids.json"

MODEL = "z-ai/glm-5.1"
TEMPERATURE = 0.0
PARALLEL = 8
SAMPLE_SIZE = 30
SEED = 0

ERROR_TYPE_TABLE = """| Error Type | Explanation |
|---|---|
| Misunderstanding | The reviewer misinterprets claims or ideas presented in the paper, leading to inaccurate or irrelevant comments. |
| Neglect | The reviewer overlooks important details explicitly stated in the paper, resulting in unwarranted questions or critiques. |
| Vague Critique | The review lacks specificity, claiming missing components without clearly identifying what is missing. |
| Out-of-scope | The reviewer suggests additional methods, experiments, or analyses that are beyond the intended scope of the paper. |
| Invalid Criticism | The reviewer's criticism is considered invalid, especially when suggesting impractical experiments or trivializing results. |
| Superficial Review | The reviewer appears to have only skimmed the paper, providing generic or unsupported comments about the presence or absence of weaknesses. |
| Unstated statement | Statements made in the review are not supported by content in the paper. |
| Excessive demands | if the weaknesses are just asking for excessive things that are not necessary for a good paper. |
| Generic comment | weaknesses are just generic comments that can apply to any paper, without really pointing out the specific problems of the paper. |"""

VALID_ERROR_TYPES = {
    "Misunderstanding", "Neglect", "Vague Critique", "Out-of-scope",
    "Invalid Criticism", "Superficial Review", "Unstated statement",
    "Excessive demands", "Generic comment", "",
}


class Weakness(BaseModel):
    weakness: str
    reliable: int
    error_type: str
    justification: str


class WeaknessList(BaseModel):
    items: list[Weakness]


def progress(event, **fields):
    print(json.dumps({"event": event, **fields}, ensure_ascii=False), file=sys.stderr, flush=True)


def run_item(client, paper_id, review_text, paper_text, guideline):
    progress("sample_start", paper_id=paper_id)
    user_content = f"""Weakness reliability guideline (error type table + human-annotated examples):
{guideline}

Paper id: {paper_id}

=== PAPER TEXT ===
{paper_text}
=== END PAPER TEXT ===

=== REVIEW TO EVALUATE ===
{review_text}
=== END REVIEW ===

Task:
The review is structured with multiple sections (Summary, Strengths, Weaknesses, Nice-to-Haves, Suggestions, etc.). ONLY consider claims that appear under the `## Weaknesses` section (including its `### Fatal`, `### Major`, `### Minor`, `### Trivial` subsections). IGNORE anything under `## Nice-to-Haves`, `## Suggestions`, `## Questions`, `## Removed Points`, `## Novel Insights`, or any other non-Weakness section -- those are not weaknesses by design and should NOT be extracted or judged.

Extract every weakness claim from the `## Weaknesses` section, then judge whether each weakness is reliable BY CHECKING IT AGAINST THE PAPER TEXT ABOVE.

For each weakness, return:
- weakness: one specific weakness, flaw, limitation, or criticism of the paper that appears in the review.
- reliable: 1 if this weakness is genuinely supported by the paper. 0 if it matches one of the error patterns in the guideline.
- error_type: if reliable=0, choose the single best-matching label from {sorted(t for t in VALID_ERROR_TYPES if t)}. If reliable=1, use an empty string.
- justification: 1-2 sentences. If reliable=0, cite the specific paper passage that contradicts the weakness or explain why it is vague/excessive/generic. If reliable=1, point to the gap in the paper that supports the weakness.

Be strict. The paper is available to you -- if the reviewer's claim contradicts something explicitly in the paper, mark it Neglect/Misunderstanding.
"""
    completion = client.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": f"""You are an expert NLP/ML conference meta-reviewer. You will be given a paper and a review of that paper. Your job is to extract each weakness claim in the review and judge whether it is reliable, USING THE PAPER TEXT as ground truth.

Error type table:
{ERROR_TYPE_TABLE}"""},
            {"role": "user", "content": user_content},
        ],
        temperature=TEMPERATURE,
        response_format=WeaknessList,
        extra_body={"reasoning": {"effort": "none", "exclude": True}},
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise ValueError(f"No parsed response for {paper_id}")
    rows = []
    for w in parsed.items:
        et = w.error_type.strip()
        if et not in VALID_ERROR_TYPES:
            raise ValueError(f"Invalid error_type {et!r} for {paper_id}")
        rows.append({
            "paper_id": paper_id,
            "weakness": w.weakness,
            "reliable": w.reliable,
            "error_type": et,
            "justification": w.justification,
            "status": "ok",
        })
    progress("sample_done", paper_id=paper_id, weaknesses=len(rows))
    return rows


load_dotenv(REPO_ROOT / ".env")
api_key = os.environ["OPENROUTER_API_KEY"]
guideline = GUIDELINE_PATH.read_text(encoding="utf-8").strip()

review_paths = {p.stem: p for p in REVIEW_DIR.glob(REVIEW_GLOB)}
paper_paths = {p.stem: p for p in PAPER_DIR.glob("*.txt")}

sampled = sorted(set(review_paths) & set(paper_paths))
print(f"sonnet∩papers: {len(sampled)}", file=sys.stderr)
SAMPLED_IDS_PATH.parent.mkdir(parents=True, exist_ok=True)
SAMPLED_IDS_PATH.write_text(json.dumps(sorted(sampled), indent=2))

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
done_ids = set()
if OUTPUT_PATH.exists():
    with OUTPUT_PATH.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            if row["status"] == "ok":
                done_ids.add(str(row["paper_id"]))
pending = [pid for pid in sampled if pid not in done_ids]

progress("batch_start", sample_size=len(sampled), pending=len(pending), done=len(done_ids))

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={"X-Title": "sonnet weakness reliability evaluation"},
)

with OUTPUT_PATH.open("a", encoding="utf-8") as out:
    with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL) as executor:
        futures = {}
        for pid in pending:
            review_text = review_paths[pid].read_text(encoding="utf-8").strip()
            paper_text = paper_paths[pid].read_text(encoding="utf-8").strip()
            futures[executor.submit(run_item, client, pid, review_text, paper_text, guideline)] = pid
        for future in concurrent.futures.as_completed(futures):
            pid = futures[future]
            try:
                rows = future.result()
            except Exception as e:
                progress("sample_failed", paper_id=pid, error=repr(e))
                continue
            for row in rows:
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
            out.flush()

progress("batch_done", output=str(OUTPUT_PATH))
