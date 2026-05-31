import concurrent.futures
import json
import os
import random
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_ROOT = Path(__file__).resolve().parents[1]

BASELINE_PATH = SCRIPT_ROOT / "outputs/weakness_humanEvaluation.jsonl"
REVIEW_GUIDELINE_PATH = REPO_ROOT / "review/datasets/deepreview_13k_shiyu/reviewGuideline.md"
OUTPUT_DIR = SCRIPT_ROOT / "outputs/2times_7files_metareviews"

MODEL = "z-ai/glm-5.1"
TEMPERATURE = 0.0
PARALLEL = 4
SAMPLE_SIZE = 50
SEED = 0

SOURCES = [
    {
        "name": "consolidated_v1_DeepReviewer_14B_TXT",
        "kind": "v1_json_dir",
        "path": REPO_ROOT / "review/datasets/consolidated_reviews_2025/v1_DeepReviewer_14B_TXT",
    },
    {
        "name": "consolidated_v1_DeepReviewer_7B_TXT",
        "kind": "v1_json_dir",
        "path": REPO_ROOT / "review/datasets/consolidated_reviews_2025/v1_DeepReviewer_7B_TXT",
    },
    {
        "name": "consolidated_v2_API_DeepSeek_PDF",
        "kind": "markdown_dir",
        "path": REPO_ROOT / "review/datasets/consolidated_reviews_2025/v2_API_DeepSeek_PDF",
        "glob": "*_report.md",
        "paper_id_suffix": "_report",
    },
    {
        "name": "consolidated_v2_Local_Qwen_PDF",
        "kind": "markdown_dir",
        "path": REPO_ROOT / "review/datasets/consolidated_reviews_2025/v2_Local_Qwen_PDF",
        "glob": "*_report.md",
        "paper_id_suffix": "_report",
    },
    {
        "name": "test_mini_wo_search",
        "kind": "markdown_dir",
        "path": REPO_ROOT / "review/datasets/results/test_mini_wo_search",
        "glob": "*.md",
        "paper_id_suffix": "",
    },
    {
        "name": "deepreview_reviews_deepseek",
        "kind": "jsonl",
        "path": REPO_ROOT / "review/datasets/deepreview_13k_shiyu/reviews_deepseek.jsonl",
    },
    {
        "name": "deepreview_reviews_qwen3_5_flash_02_23",
        "kind": "jsonl",
        "path": REPO_ROOT / "review/datasets/deepreview_13k_shiyu/reviews_qwen3_5_flash_02_23.jsonl",
    },
]


class Weakness(BaseModel):
    weakness: str
    reliable: int


class WeaknessList(BaseModel):
    items: list[Weakness]


def progress(event, **fields):
    row = {"event": event, **fields}
    print(json.dumps(row, ensure_ascii=False), file=sys.stderr, flush=True)


def load_v1_json_review(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    results = data["results"]
    if not results:
        raise ValueError(f"Empty results list in {path}")
    result = results[0]
    review_obj = result["meta_review"] if "meta_review" in result else result
    if not isinstance(review_obj, dict):
        raise ValueError(f"Malformed review object in {path}")
    if not review_obj:
        raw_text = result["raw_text"]
        match = re.search(
            r"(## Reviewer 1\s+.*?### Confidence\s+.+?)(?:\n\s*\*{5,}|\n\s*## Reviewer 2|\Z)",
            raw_text,
            flags=re.DOTALL,
        )
        if match is None:
            match = re.search(
                r"(## Reviewer 1\s+.*?### Weaknesses\s+.*?)(?:\n\s*### Suggestions|\n\s*### Questions|\n\s*### Rating|\n\s*## Reviewer 2|\n\s*\*{5,}|\Z)",
                raw_text,
                flags=re.DOTALL,
            )
        if match is None:
            raise ValueError(f"Missing structured review and complete Reviewer 1 block in {path}")
        return match.group(1).strip()
    fields = [
        ("Summary", "summary"),
        ("Strengths", "strengths"),
        ("Weaknesses", "weaknesses"),
        ("Suggestions", "suggestions"),
        ("Questions", "questions"),
        ("Rating", "rating"),
    ]
    lines = []
    for title, key in fields:
        value = review_obj[key]
        if value is None or str(value).strip() == "":
            raise ValueError(f"Missing {key} in {path}")
        lines.append(f"## {title}\n{value}")
    if "decision" in result and result["decision"] is not None and str(result["decision"]).strip():
        lines.append(f"## Decision\n{result['decision']}")
    return "\n\n".join(lines)


def load_source_items(source):
    path = source["path"]
    kind = source["kind"]
    rows = []
    if kind == "v1_json_dir":
        for review_path in sorted(path.glob("*.txt.json")):
            name = review_path.name
            if not name.endswith(".txt.json"):
                raise ValueError(f"Unexpected v1 filename: {review_path}")
            rows.append({
                "source": source["name"],
                "source_kind": kind,
                "paper_id": name[: -len(".txt.json")],
                "review_path": str(review_path),
            })
        return rows
    if kind == "markdown_dir":
        suffix = source["paper_id_suffix"]
        for review_path in sorted(path.glob(source["glob"])):
            paper_id = review_path.stem
            if suffix and paper_id.endswith(suffix):
                paper_id = paper_id[: -len(suffix)]
            rows.append({
                "source": source["name"],
                "source_kind": kind,
                "paper_id": paper_id,
                "review_path": str(review_path),
            })
        return rows
    if kind == "jsonl":
        with path.open(encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                row = json.loads(line)
                paper_id = row["paper_id"]
                review = row["review"]
                if not isinstance(paper_id, str) or not paper_id.strip():
                    raise ValueError(f"Missing paper_id at {path}:{line_number}")
                if not isinstance(review, str) or not review.strip():
                    raise ValueError(f"Missing review at {path}:{line_number}")
                rows.append({
                    "source": source["name"],
                    "source_kind": kind,
                    "paper_id": paper_id,
                    "review_path": f"{path}:{line_number}",
                    "review": review.strip(),
                })
        return rows
    raise ValueError(f"Unknown source kind: {kind}")


def load_item_review(item):
    if item["source_kind"] == "v1_json_dir":
        return load_v1_json_review(Path(item["review_path"]))
    if item["source_kind"] == "markdown_dir":
        return Path(item["review_path"]).read_text(encoding="utf-8").strip()
    if item["source_kind"] == "jsonl":
        return item["review"]
    raise ValueError(f"Unknown source kind: {item['source_kind']}")


def run_item(client, item, baseline_text, review_guideline):
    review_text = load_item_review(item)
    example_id = f"{item['source']}:{item['paper_id']}"
    progress("sample_start", source=item["source"], paper_id=item["paper_id"])

    user_content = f"""Baseline calibration examples from ReviewCritique:
{baseline_text}

Review guideline:
{review_guideline}

Paper id:
{item["paper_id"]}

Unsegmented review to evaluate:
{review_text}

Task:
Extract every weakness claim that the review makes about the paper, then judge whether each weakness is reliable.

For each weakness, return:
- weakness: one specific weakness, flaw, limitation, or criticism of the paper that appears in the review.
- reliable: 1 if this weakness really exists in the paper or is a reasonable, well-grounded criticism; 0 if this weakness is unsupported, unreasonable, vague, fabricated, out-of-scope, or not justified by the review/paper context.
"""
    completion = client.chat.completions.parse(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """You are an expert NLP conference meta-reviewer. Use the supplied ReviewCritique calibration examples and review guideline to judge the reliability of a whole unsegmented review.""",
            },
            {"role": "user", "content": user_content},
        ],
        temperature=TEMPERATURE,
        response_format=WeaknessList,
        extra_body={"reasoning": {"effort": "none", "exclude": True}},
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise ValueError(f"No parsed response for {example_id}")
    rows = [
        {
            "paper_id": item["paper_id"],
            "weakness": w.weakness,
            "reliable": w.reliable,
            "status": "ok",
        }
        for w in parsed.items
    ]
    progress("sample_done", source=item["source"], paper_id=item["paper_id"], weaknesses=len(rows))
    return rows


load_dotenv(SCRIPT_ROOT / ".env")
api_key = os.environ["OPENROUTER_API_KEY"]

baseline_examples = []
with BASELINE_PATH.open(encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        row = json.loads(line)
        baseline_examples.append({
            "segment_text": row["segment_text"],
            "label": row["baseline_label"],
            "topic_class_2": row["topic_class_2"],
            "human_evaluation": row["human_evaluation"],
        })
if not baseline_examples:
    raise RuntimeError(f"No baseline examples found in {BASELINE_PATH}")
baseline_text = "\n".join(
    f"BASELINE EXAMPLE {idx}\n{json.dumps(example, ensure_ascii=False)}"
    for idx, example in enumerate(baseline_examples, start=1)
)

review_guideline = REVIEW_GUIDELINE_PATH.read_text(encoding="utf-8").strip()

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

items_by_source = {}
for source in SOURCES:
    indexed = {}
    for row in load_source_items(source):
        if row["paper_id"] in indexed:
            raise ValueError(f"Duplicate paper_id {row['paper_id']} in {row['source']}")
        indexed[row["paper_id"]] = row
    items_by_source[source["name"]] = indexed

common_ids = set.intersection(*(set(v) for v in items_by_source.values()))
if len(common_ids) < SAMPLE_SIZE:
    raise RuntimeError(f"Only {len(common_ids)} common paper ids, need {SAMPLE_SIZE}")
rng = random.Random(SEED)
sampled_ids = rng.sample(sorted(common_ids), SAMPLE_SIZE)

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={"X-Title": "Unsegmented review reliability evaluation"},
)

progress("batch_start", sources=len(SOURCES), sample_size=SAMPLE_SIZE)

for source in SOURCES:
    output_path = OUTPUT_DIR / f"{source['name']}.jsonl"
    done_ids = set()
    if output_path.exists():
        with output_path.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                if row["status"] == "ok":
                    done_ids.add(str(row["paper_id"]))
    pending = [items_by_source[source["name"]][pid] for pid in sampled_ids if pid not in done_ids]

    with output_path.open("a", encoding="utf-8") as out:
        with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL) as executor:
            futures = {
                executor.submit(run_item, client, item, baseline_text, review_guideline): item
                for item in pending
            }
            for future in concurrent.futures.as_completed(futures):
                item = futures[future]
                rows = future.result()
                for row in rows:
                    out.write(json.dumps(row, ensure_ascii=False) + "\n")
                out.flush()

progress("batch_done", output_dir=str(OUTPUT_DIR))
