
reviews = "../results/test"



import pandas as pd
df = pd.read_csv("../results/test.csv")

def get_gt(review_filename):
    paper_id = review_filename.split(".")[0]
    row = df[df["paper_id"] == paper_id]
    return row["gt_avg_score"]


rl_prompt = """
You will get a review of a paper and a set of retrieved anchor reviews, based on the anchor review, estimate the score of the paper under review. The score should be between 1 and 10, where 1 is the worst and 10 is the best. Round to the nearest .5 or .0. 

Scoring rules:
- Your final score must be positioned relative to the retrieved anchors.
- Do not pick a score first and then justify it. Compare to anchors first, let the comparison set the score.
- The number of weaknesses listed is not a signal for a bad paper — focus on weakness content and anchor scores.
- Score distribution: extreme scores are rare but valid. If the paper truly is exceptional or truly weak, give an extreme score even if most retrieved anchors sit in the middle.
- Do NOT cluster scores around 5, the score should be relative to the retrieval samples. Score a good paper high and a bad paper low. 
- Compare the paper under review with every single anchor paper

Scoring scale:
1 - strong reject
3 - reject
4 - borderline reject
6 - borderline accept
8 - accept
10 - strong accept

Give your analysis first, then put your final score in a XML-style tag <score></score>
"""


from openai import OpenAI
import os
import dotenv
import hashlib
import time

dotenv.load_dotenv("../.env")

or_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)


condense_anchor_cache = "../results/condensed_anchor_cache"
condense_anchor_retries = 3

condense_anchor_prompt = """
Condense this paper's human reviews into one merged anchor review, but preserve evidence.

Rules:
- Merge duplicate points across reviewers, but keep every distinct scoring-relevant point.
- Preserve strength/weakness direction, severity, magnitude, reviewer confidence, and reviewer disagreement.
- Keep concrete named methods, baselines, datasets, tables, figures, equations, examples, and numeric details.
- Put reviewer questions into Weaknesses when they overlap with a criticism, missing experiment, missing comparison, or ablation request.
- If a minority reviewer is more positive or negative, explicitly keep that contrast.
- Shorten wording, not information. Do not turn specific criticisms into vague summaries.
- Only summarize the reviewers. Do not decide whether the paper should be accepted, rejected, improved, or downgraded.
- Do not invent information.
- Do not include the title, abstract, decision, or score header.
- Return only this structure:

## Merged Review

### Summary

### Strengths

### Weaknesses
"""

def condense_anchor_review(review_content):
    os.makedirs(condense_anchor_cache, exist_ok=True)
    cache_key = hashlib.sha256((condense_anchor_prompt + "\n\n" + review_content).encode("utf-8")).hexdigest()
    cache_path = os.path.join(condense_anchor_cache, f"{cache_key}.md")

    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            return f.read()

    score_header = []
    for line in review_content.splitlines():
        if line.startswith("- Decision:") or line.startswith("- Scores:"):
            score_header.append(line)
        if line == "## Abstract":
            break

    if len(score_header) != 2:
        raise ValueError("missing decision/scores header")

    for attempt in range(condense_anchor_retries):
        try:
            print(f"deepseek condense attempt {attempt + 1}/{condense_anchor_retries} for {cache_key[:10]}")
            response = or_client.chat.completions.create(
                model="deepseek/deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": condense_anchor_prompt},
                    {"role": "user", "content": review_content},
                ],
                temperature=0,
                extra_body={"reasoning": {"enabled": True, "effort": "low"}, "provider": {"only": ["deepseek"]}},
            )
            condensed_review = "\n".join(score_header) + "\n\n" + response.choices[0].message.content
            tmp_path = f"{cache_path}.{time.time_ns()}.tmp"
            with open(tmp_path, "w") as f:
                f.write(condensed_review)
            os.replace(tmp_path, cache_path)
            return condensed_review
        except Exception as e:
            print(f"deepseek condense failed for {cache_key[:10]} attempt {attempt + 1}/{condense_anchor_retries}: {e}")
            if attempt == condense_anchor_retries - 1:
                raise
            time.sleep(2)


import pickle
emb_path = "../datasets/human_reviews_embeddings_deepreview.pkl"
idx_path = "../datasets/human_review_score_index_deepreview.pkl"

with open(emb_path, "rb") as f:
    review_embeddings = pickle.load(f)

with open(idx_path, "rb") as f:
    review_score_index = pickle.load(f)



import os
from concurrent.futures import ThreadPoolExecutor
import numpy as np
bin_names = ["very_low", "low", "medium", "high", "very_high"]
thresholds = [2, 4, 6, 8]

bins = {name: [] for name in bin_names}
bins_embeddings = {name: [] for name in bin_names}

for i in review_score_index:
    score = review_score_index[i]
    idx = next((j for j, t in enumerate(thresholds) if score <= t), len(thresholds))
    name = bin_names[idx]
    bins[name].append(i)
    bins_embeddings[name].append(review_embeddings[i])

for name in bin_names:
    bins_embeddings[name] = np.array(bins_embeddings[name])

def build_sample(review):
    with open(os.path.join(reviews, review), 'r') as f:
        review_content = f.read().split("Score and Decision")[0]

    query_embedding = or_client.embeddings.create(
        model="google/gemini-embedding-001",
        input=review_content,
        encoding_format="float",
    )
    query_vector = np.array(query_embedding.data[0].embedding)

    anchor_samples = []
    for name in bin_names:
        if len(bins_embeddings[name]) == 0:
            continue
        similarities = bins_embeddings[name] @ query_vector.T
        top_indices = np.argsort(similarities)[-2:]
        selected = [bins[name][idx] for idx in top_indices]

        for filename in selected:
            if filename == review:
                continue # skip itself
            with open(os.path.join("../datasets/deepreview_13k_train/human_reviews", filename), 'r') as f:
                anchor_review = f.read().split("Score and Decision")[0]
            print(f"condensing anchor {filename}")
            anchor_samples.append(condense_anchor_review(anchor_review))
    try:
        gt = get_gt(review)
        gt = float(gt.values[0])
    except:
        return None

    return {
        "prompt": [
                    {
                        "content": rl_prompt,
                        "role": "system"
                    },
                    {
                        "content": f"Paper review:\n{review_content}\n\nAnchor reviews:\n" + "\n\n".join(anchor_samples),
                        "role": "user"
                    }
                ], 
        "solution": gt,
        "paper_id": review.split(".")[0]
    }

import csv
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

csv_lock = threading.Lock()

gt_index = {}
with open("../results/test.csv", "r", newline="") as f:
    for row in csv.DictReader(f):
        gt_index[row["paper_id"].strip()] = row

csv_path = "../results/deepseek_cal_baseline.csv"
csv_header = [
    "paper_id", "pred_score", "pred_decision", "gt_avg_score", "gt_decision",
    "gt_binary", "match", "cost", "sdk_savings",
    "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
]

logged_paper_ids = set()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    with open(csv_path, "r", newline="") as f:
        for row in csv.DictReader(f):
            logged_paper_ids.add(row["paper_id"])
else:
    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerow(csv_header)
print(f"CSV: {csv_path} ({len(logged_paper_ids)} already logged)")


def safe_build_sample(review):
    try:
        return build_sample(review)
    except Exception as e:
        print(f"build_sample failed for {review}: {type(e).__name__}: {e}")
        return None


review_files = os.listdir(reviews)
with ThreadPoolExecutor(max_workers=50) as executor:
    ds = list(tqdm(executor.map(safe_build_sample, review_files), total=len(review_files), desc="build"))

ds = [s for s in ds if s is not None]
print(f"built {len(ds)} samples")


def cal(sample):
    paper_id = sample["paper_id"]
    if paper_id in logged_paper_ids:
        return None
    messages = sample["prompt"]
    cost = 0.0
    scores = []
    ans = []
    for _ in range(1):
        for attempt in range(5):
            try:
                _response = or_client.chat.completions.create(
                    model="deepseek/deepseek-v4-flash",
                    messages=messages,
                    extra_body={"reasoning": {"enabled": False, "effort": "low"}, "provider": {"only": ["deepseek"]}}
                )
                response = _response.choices[0].message.content
                ans.append(response)
                try:
                    cost += _response.usage.cost_details["upstream_inference_cost"]
                except Exception:
                    pass
                break
            except Exception as e:
                print(f"rollout {paper_id} deepseek attempt {attempt + 1}/5 failed: {e}")
                if attempt == 4:
                    raise

        try:
            parsed_score = float(re.search(r'<score>(.*?)</score>', ans[-1]).group(1))
            scores.append(parsed_score)
            print("Deepseek", paper_id, parsed_score - sample["solution"])
        except Exception:
            pass

    if not scores:
        print(f"  [{paper_id}] no parseable scores — skipping")
        return None

    pred_score = float(np.mean(scores))
    pred_decision = "Accept" if pred_score >= 5 else "Reject"

    gt = gt_index.get(paper_id)
    if gt is None:
        gt_avg_score = f"{sample['solution']:.2f}"
        gt_decision = ""
        gt_binary = ""
        gt_scores_padded = [""] * 7
    else:
        gt_avg_score = f"{float(gt.get('gt_avg_score', sample['solution'])):.2f}"
        gt_decision = gt.get("gt_decision", "").strip()
        gt_binary = gt.get("gt_binary", "").strip()
        gt_scores_padded = [gt.get(f"gt_score_{i}", "") for i in range(7)]

    if gt_binary in ("Accept", "Reject"):
        match_str = "YES" if pred_decision == gt_binary else "NO"
    else:
        match_str = "N/A"

    with csv_lock:
        with open(csv_path, "a", newline="") as f:
            csv.writer(f).writerow([
                paper_id,
                pred_score,
                pred_decision,
                gt_avg_score,
                gt_decision,
                gt_binary,
                match_str,
                f"{cost:.6f}",
                "0.0000",
                *gt_scores_padded,
            ])
        logged_paper_ids.add(paper_id)
    return pred_score


def safe_cal(sample):
    try:
        return cal(sample)
    except Exception as e:
        print(f"cal failed for {sample.get('paper_id')}: {type(e).__name__}: {e}")
        return None


print(f"running cal on {len(ds)} samples ...")
with ThreadPoolExecutor(max_workers=50) as executor:
    list(tqdm(executor.map(safe_cal, ds), total=len(ds), desc="cal"))
print(f"done. final CSV rows: {len(logged_paper_ids)}")


