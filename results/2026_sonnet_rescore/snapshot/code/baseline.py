import argparse
import csv
import json
import os
import pickle
import random
import re
import statistics
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import dotenv
from openai import OpenAI

from paths import RESULTS_DIR


ROOT = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(ROOT / ".env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

BASELINE_PROMPT = """You are an experienced academic reviewer for ICLR, a top ML venue. Your task is to write one direct review of the paper.

The paper was extracted from PDF by an automated parser. Treat formatting artifacts, broken equations, garbled tables, OCR errors, stripped appendix, and missing references as parser issues, not paper flaws.

Evaluate the paper as a whole: originality, importance of the research question, whether the claims are well supported, soundness of the method and experiments, clarity, and value to the research community. Judge the paper within its own class: method paper, benchmark, dataset, survey, theory paper, empirical study, or position paper may need different standards.

Do not compress every paper into a middle score. If the contribution is genuinely strong, score it high. If a problem invalidates the contribution, score it low. Rank weaknesses by severity rather than count.

Hard rules:
- Do not criticize missing appendix, missing proofs in appendix, or absent references.
- Do not mention missing related work unless the paper itself makes the gap obvious.
- Do not criticize typos, grammar, formatting, OCR artifacts, citation style, or parser damage.
- Do not question whether a cited model, benchmark, dataset, tool, or reference exists.
- Do not invent weaknesses to fill sections.
- Do not reject a paper just because it has minor weaknesses; every paper has some.
- If the paper is inaccessible, empty, or not a paper, return score -100 and decision Error.

Use this output format:

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with concrete evidence
- strength 2 with concrete evidence

## Weaknesses
### Fatal
Errors that invalidate the paper's core claims or results. Most papers have none.

### Major
Issues that weigh against acceptance and should be fully resolved.

### Minor
Issues worth attention but unlikely to change the accept/reject decision.

### Trivial
Small issues that carry no weight in evaluation.

## Nice-to-Haves
- suggestions that would improve the paper but are not core flaws

## Novel Insights
One paragraph synthesizing genuinely novel observations. If no genuinely novel insight emerges beyond the paper's own contributions, write "None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

## Score and Decision
Assign a score based solely on your assessment of the paper's quality after review.

Scoring scale:
1 - strong reject
3 - reject
4 - borderline reject
6 - borderline accept
8 - accept
10 - strong accept

Score round to .5 or .0. Use the full range when warranted. The number of weaknesses listed is not a signal for a bad paper; focus on weakness severity.

At the very end of your response, write exactly these two lines:
MY FINAL SCORE: <score>score</score>
MY FINAL DECISION: <decision>Accept/Reject/Error</decision>

You HAVE TO use the XML tag for scores. 



ICLR Offical Guideline for reference:
Reviewing a submission: step-by-step
Summarized in one sentence, a review aims to determine whether a submission will bring sufficient value to the community and contribute new knowledge. The process can be broken down into the following main reviewer tasks:

 

Read the paper: It’s important to carefully read through the entire paper and to look up any related work and citations that will help you comprehensively evaluate it. Be sure to give yourself sufficient time for this step.
While reading, consider the following:
Objective of the work: What is the goal of the paper? Is it to better address a known application or problem, draw attention to a new application or problem, or to introduce and/or explain a new theoretical finding? A combination of these? Different objectives will require different considerations as to potential value and impact.
Strong points: is the submission clear, technically correct, experimentally rigorous, reproducible, does it present novel findings (e.g. theoretically, algorithmically, etc.)?
Weak points: is it weak in any of the aspects listed in b.?
Be mindful of potential biases and try to be open-minded about the value and interest a paper can hold for the entire ICLR community, even if it may not be very interesting for you.
Answer four key questions for yourself to make a recommendation to Accept or Reject: 
What is the specific question and/or problem tackled by the paper?
Is the approach well motivated, including being well-placed in the literature?
Does the paper support the claims? This includes determining if results, whether theoretical or empirical, are correct and if they are scientifically rigorous.
What is the significance of the work? Does it contribute new knowledge and sufficient value to the community? Note, this does not necessarily require state-of-the-art results. Submissions bring value to the ICLR community when they convincingly demonstrate new, relevant, impactful knowledge (incl., empirical, theoretical, for practitioners, etc).
Write and submit your initial review, organizing it as follows: 
Summarize what the paper claims to contribute. Be positive and constructive.
List strong and weak points of the paper. Be as comprehensive as possible.
Clearly state your initial recommendation (accept or reject) with one or two key reasons for this choice.
Provide supporting arguments for your recommendation.
Ask questions you would like answered by the authors to help you clarify your understanding of the paper and provide the additional evidence you need to be confident in your assessment. 
Provide additional feedback with the aim to improve the paper. Make it clear that these points are here to help, and not necessarily part of your decision assessment.
Complete the CoE report: ICLR has adopted the following Code of Ethics (CoE). When submitting your review, you’ll be asked to complete a CoE report for the paper. The report is a simple form with two questions. The first asks whether there is a potential violation of the CoE. The second is relevant only if there is a potential violation and asks the reviewer to explain why there may be a potential violation. In order to answer these questions, it is therefore important that you read the CoE before starting your reviews.
 
Engage in discussion: During this phase, reviewers, authors and area chairs engage in asynchronous discussion and authors are allowed to revise their submissions to address concerns that arise. It is crucial that you are actively engaged during this phase. Maintain a spirit of openness to changing your initial recommendation (either to a more positive or more negative) rating.
Borderline paper meeting: Similarly to last year, the ACs are encouraged to (virtually) meet and discuss borderline cases with reviewers. ACs will reach out to schedule this meeting. This is to ensure active discussions among reviewers and well-thought-out decisions. ACs will schedule the meeting and facilitate the discussion. For a productive discussion, it is important to familiarize yourself with other reviewers' feedback prior to the meeting. Please note that we will be leveraging information for reviewers who failed to attend this meeting (excluding emergencies). 
Provide final recommendation: Update your review, taking into account the new information collected during the discussion phase and any revisions to the submission. (Note that reviewers can change their reviews after the author response period.)  State your reasoning and what did/didn’t change your recommendation throughout the discussion phase.

"""

REVIEW_USER_PROMPT = """Review the following paper thoroughly.
--- PAPER CONTENT START ---
{paper_content}
--- PAPER CONTENT END ---
"""

csv_lock = threading.Lock()


def load_ground_truth(data_dir: Path):
    csv_file = data_dir / "ratings.csv"
    if not csv_file.exists():
        raise FileNotFoundError(f"No ratings.csv found in {data_dir}")
    rows = []
    with open(csv_file, "r", newline="") as f:
        for row in csv.DictReader(f):
            score_fields = [field for field in row if field.startswith("score_")]
            scores = [float(row[field]) for field in score_fields if row[field].strip()]
            decision = row["decision"].strip()
            gt_binary = row["gt_binary"].strip()
            rows.append({
                "paper_id": row["paper_id"].strip(),
                "title": row["title"].strip(),
                "scores": scores,
                "avg_score": float(row["avg_score"]),
                "decision": decision,
                "gt_binary": gt_binary,
            })
    return rows, data_dir / "papers"


def parse_review(review_text: str):
    score_match = re.search(r"<score>\s*(-?\d+(?:\.\d+)?)\s*</score>", review_text)
    decision_match = re.search(r"<decision>\s*(Accept|Reject|Error)\s*</decision>", review_text)
    if score_match and decision_match:
        return float(score_match.group(1)), decision_match.group(1), 0.0

    extractor_response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "system", "content": "Extract the final numeric score and accept/reject/error decision from a paper review. Respond with exactly: <score>NUMBER</score><decision>Accept|Reject|Error</decision>. No other text."},
            {"role": "user", "content": review_text},
        ],
        temperature=0,
        extra_body={"reasoning": {"enabled": False, "effort": "low"}, "provider": {"only": ["deepseek"]}, "usage": {"include": True}},
    )
    extracted = extractor_response.choices[0].message.content
    if extracted is None or not extracted.strip():
        raise RuntimeError("empty score extractor response")
    score_match = re.search(r"<score>\s*(-?\d+(?:\.\d+)?)\s*</score>", extracted)
    decision_match = re.search(r"<decision>\s*(Accept|Reject|Error)\s*</decision>", extracted)
    if not score_match:
        raise ValueError("missing <score> tag")
    if not decision_match:
        raise ValueError("missing <decision> tag")
    usage = extractor_response.usage
    if usage is None:
        raise RuntimeError("score extractor response missing usage")
    if hasattr(usage, "cost") and usage.cost is not None:
        extractor_cost = float(usage.cost)
    elif hasattr(usage, "model_extra") and usage.model_extra is not None and "cost" in usage.model_extra:
        extractor_cost = float(usage.model_extra["cost"])
    else:
        raise RuntimeError("score extractor response missing usage cost")
    return float(score_match.group(1)), decision_match.group(1), extractor_cost


def review_paper(paper_path: Path, model: str, system_prompt: str):
    paper_content = paper_path.read_text(encoding="utf-8")
    print(json.dumps({"event": "sample_start", "paper_id": paper_path.stem, "path": str(paper_path)}), flush=True)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": REVIEW_USER_PROMPT.format(paper_path=str(paper_path.resolve()), paper_content=paper_content)},
        ],
        temperature=0,
        extra_body={"reasoning": {"enable": True}, "usage": {"include": True}},
    )
    review_text = response.choices[0].message.content
    if review_text is None or not review_text.strip():
        raise RuntimeError(f"{paper_path.stem}: empty model response")
    score, decision, extractor_cost = parse_review(review_text)
    usage = response.usage
    if usage is None:
        raise RuntimeError(f"{paper_path.stem}: OpenRouter response missing usage")
    if hasattr(usage, "cost") and usage.cost is not None:
        cost = float(usage.cost) + extractor_cost
    elif hasattr(usage, "model_extra") and usage.model_extra is not None and "cost" in usage.model_extra:
        cost = float(usage.model_extra["cost"]) + extractor_cost
    else:
        raise RuntimeError(f"{paper_path.stem}: OpenRouter response missing usage cost")
    print(json.dumps({"event": "sample_done", "paper_id": paper_path.stem, "score": score, "decision": decision, "cost": cost}), flush=True)
    return review_text, score, decision, cost


def run_benchmark(data_dir: str, model: str, n_samples: int, seed: int, balanced: bool, reviews_dir: str):
    data_path = Path(data_dir)
    gt_data, papers_dir = load_ground_truth(data_path)
    available = [row for row in gt_data if (papers_dir / f"{row['paper_id']}.txt").exists()]
    if not available:
        raise RuntimeError(f"No paper txt files found in {papers_dir}")
    calibration_score_index_path = Path("~/review_agent/new/human_review_score_index_2026.pkl").expanduser()
    if not calibration_score_index_path.exists():
        raise FileNotFoundError(f"No 2026 calibration score index found at {calibration_score_index_path}")
    with open(calibration_score_index_path, "rb") as f:
        calibration_score_index = pickle.load(f)
    score_values = [float(score) for score in calibration_score_index.values()]
    if not score_values:
        raise RuntimeError(f"No scores found in {calibration_score_index_path}")
    score_bins = {}
    for score in score_values:
        rounded = round(score)
        if rounded not in score_bins:
            score_bins[rounded] = 0
        score_bins[rounded] += 1
    bin_lines = []
    for rounded in sorted(score_bins):
        pct = score_bins[rounded] / len(score_values) * 100
        bin_lines.append(f"- rounded avg score {rounded}: {score_bins[rounded]} papers ({pct:.1f}%)")
    dataset_stats_prompt = BASELINE_PROMPT + f"""

2026 score distribution:
- Number of papers: {len(score_values)}
- Mean human average score: {statistics.mean(score_values):.2f}
- Median human average score: {statistics.median(score_values):.2f}
- Rounded average-score bin distribution:
{chr(10).join(bin_lines)}

Use the 2026 score distribution above to understand the scale. Do not force the current paper toward the mean or median if its quality warrants a high or low score.
"""
    if balanced:
        random_source = random.Random(seed)
        bins = {}
        for row in available:
            rounded = round(row["avg_score"])
            if rounded not in bins:
                bins[rounded] = []
            bins[rounded].append(row)
        samples = []
        per_bin = max(1, n_samples // len(bins))
        for rounded in sorted(bins):
            random_source.shuffle(bins[rounded])
            samples.extend(bins[rounded][:per_bin])
        random_source.shuffle(samples)
        samples = samples[:n_samples]
    else:
        samples = random.Random(seed).sample(available, min(n_samples, len(available)))

    if "MAX_PAPERS" in os.environ:
        samples = samples[:int(os.environ["MAX_PAPERS"])]

    output_csv = Path(os.environ["OUTPUT_CSV"]) if "OUTPUT_CSV" in os.environ else RESULTS_DIR / "baseline_scores.csv"
    if not output_csv.is_absolute():
        output_csv = RESULTS_DIR / output_csv
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    review_path = Path(reviews_dir)
    if not review_path.is_absolute():
        review_path = RESULTS_DIR / review_path
    review_path.mkdir(parents=True, exist_ok=True)

    finished = set()
    if output_csv.exists() and output_csv.stat().st_size > 0:
        with open(output_csv, "r", newline="") as f:
            for row in csv.DictReader(f):
                finished.add(row["paper_id"])
    else:
        with open(output_csv, "w", newline="") as f:
            csv.writer(f).writerow([
                "paper_id", "pred_score", "pred_decision", "gt_avg_score", "gt_decision", "gt_binary", "match", "cost", "sdk_savings",
                "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
            ])

    skipped_existing = sum(1 for sample in samples if sample["paper_id"] in finished)
    samples = [sample for sample in samples if sample["paper_id"] not in finished]
    print(json.dumps({"event": "batch_start", "n": len(samples), "skipped_existing": skipped_existing, "model": model, "csv": str(output_csv), "reviews_dir": str(review_path)}), flush=True)

    total_cost = 0.0

    def run_sample(sample):
        paper_id = sample["paper_id"]
        paper_path = papers_dir / f"{paper_id}.txt"
        padded_scores = sample["scores"] + [""] * (7 - len(sample["scores"]))
        try:
            review_text, score, decision, cost = review_paper(paper_path, model, dataset_stats_prompt)
            if decision == "Error":
                match = "N/A"
            else:
                match = "YES" if decision == sample["gt_binary"] else "NO"
        except Exception as e:
            score = -100
            decision = "Error"
            match = "N/A"
            cost = 0.0
            review_text = f"# Error\n\n{type(e).__name__}: {e}\n"
            print(json.dumps({"event": "sample_done", "paper_id": paper_id, "status": "error", "error": f"{type(e).__name__}: {e}"}), flush=True)
        with csv_lock:
            with open(output_csv, "a", newline="") as f:
                csv.writer(f).writerow([
                    paper_id,
                    score,
                    decision,
                    f"{sample['avg_score']:.2f}",
                    sample["decision"],
                    sample["gt_binary"],
                    match,
                    f"{cost:.6f}",
                    "0.0000",
                    *padded_scores,
                ])
            (review_path / f"{paper_id}.md").write_text(review_text, encoding="utf-8")
        return cost

    concurrency = int(os.environ["CONCURRENCY"]) if "CONCURRENCY" in os.environ else 1
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        for cost in executor.map(run_sample, samples):
            total_cost += cost

    print(json.dumps({"event": "batch_done", "n": len(samples), "cost": total_cost}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Single-call OpenRouter baseline paper reviewer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--single_paper", type=str)
    group.add_argument("--benchmark", type=str)
    parser.add_argument("--model", type=str, default=os.environ["BASELINE_MODEL"] if "BASELINE_MODEL" in os.environ else "deepseek-v4-flash")
    parser.add_argument("--n_samples", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--balanced", action="store_true")
    parser.add_argument("--reviews_dir", type=str, default="baseline_reviews")
    args = parser.parse_args()

    if args.single_paper:
        review_text, score, decision, cost = review_paper(Path(args.single_paper), args.model, BASELINE_PROMPT)
        print(review_text)
        print(f"\nPredicted score: {score}")
        print(f"Predicted decision: {decision}")
        print(f"OpenRouter cost: ${cost:.6f}")
    elif args.benchmark:
        run_benchmark(args.benchmark, args.model, args.n_samples, args.seed, args.balanced, args.reviews_dir)
