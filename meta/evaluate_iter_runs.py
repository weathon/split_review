import concurrent.futures
import json
import os
import random
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


ROOT = Path(__file__).resolve().parents[1]
GUIDELINE_PATH = ROOT / "meta/weakness_reliability_guideline.md"
OUTPUT_DIR = ROOT / "meta/iter_eval_outputs"

MODEL = "z-ai/glm-5.1"
TEMPERATURE = 0.0
PARALLEL = 8
SAMPLE_SIZE = 30
SEED = 0

SOURCES = [
    {"name": "baseline_v0", "path": ROOT / "results/baseline_v0/reviews"},
    {"name": "iter1_format", "path": ROOT / "results/iter1_format/reviews"},
    {"name": "iter2_addressed", "path": ROOT / "results/iter2_addressed/reviews"},
    {"name": "v905381a_repro", "path": ROOT / "results/v905381a_repro/reviews"},
]


class Weakness(BaseModel):
    weakness: str
    reliable: int


class WeaknessList(BaseModel):
    items: list[Weakness]


def progress(event, **fields):
    print(json.dumps({"event": event, **fields}, ensure_ascii=False), file=sys.stderr, flush=True)


load_dotenv(ROOT / ".env")
api_key = os.environ["OPENROUTER_API_KEY"]

guideline_text = GUIDELINE_PATH.read_text(encoding="utf-8").strip()

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

items_by_source = {}
for source in SOURCES:
    indexed = {}
    for p in sorted(source["path"].glob("*.md")):
        indexed[p.stem] = {"source": source["name"], "paper_id": p.stem, "path": str(p)}
    items_by_source[source["name"]] = indexed

common_ids = sorted(set.intersection(*(set(v) for v in items_by_source.values())))
rng = random.Random(SEED)
sampled_ids = rng.sample(common_ids, min(SAMPLE_SIZE, len(common_ids)))
progress("batch_start", sources=len(SOURCES), sample_size=len(sampled_ids), common=len(common_ids))


def run_item(client, item):
    review_text = Path(item["path"]).read_text(encoding="utf-8")
    progress("sample_start", source=item["source"], paper_id=item["paper_id"])
    user_content = f"""Weakness reliability guideline:
{guideline_text}

Paper id:
{item["paper_id"]}

Unsegmented review to evaluate:
{review_text}

Task:
Extract every weakness claim that the review makes about the paper, then judge whether each weakness is reliable.

For each weakness, return:
- weakness: one specific weakness, flaw, limitation, or criticism of the paper that appears in the review.
- reliable: 1 if this weakness is a well-grounded, paper-specific criticism; 0 if it matches any of the unreliable error patterns in the guideline (Misunderstanding, Neglect, Vague Critique, Out-of-scope, Invalid Criticism, Superficial Review, Unstated statement, Excessive demands, Generic comment).
"""
    completion = client.chat.completions.parse(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert NLP conference meta-reviewer. Use the supplied weakness reliability guideline to judge each weakness raised in a paper review."},
            {"role": "user", "content": user_content},
        ],
        temperature=TEMPERATURE,
        response_format=WeaknessList,
        extra_body={"reasoning": {"effort": "none", "exclude": True}},
    )
    parsed = completion.choices[0].message.parsed
    rows = [{"paper_id": item["paper_id"], "weakness": w.weakness, "reliable": w.reliable, "status": "ok"} for w in parsed.items]
    progress("sample_done", source=item["source"], paper_id=item["paper_id"], n=len(rows))
    return rows


client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={"X-Title": "iter review reliability eval"},
)

for source in SOURCES:
    out_path = OUTPUT_DIR / f"{source['name']}.jsonl"
    done = set()
    if out_path.exists():
        with out_path.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                done.add(json.loads(line)["paper_id"])
    pending = [items_by_source[source["name"]][pid] for pid in sampled_ids if pid not in done]
    with out_path.open("a", encoding="utf-8") as out:
        with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL) as ex:
            futures = {ex.submit(run_item, client, item): item for item in pending}
            for fut in concurrent.futures.as_completed(futures):
                for row in fut.result():
                    out.write(json.dumps(row, ensure_ascii=False) + "\n")
                out.flush()

progress("batch_done", output_dir=str(OUTPUT_DIR))
