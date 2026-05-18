# %%
reviews = "../results/training_review_diverse_cal"

# %%


# %%
import pandas as pd
df = pd.read_csv("../results/bench_scores_deepreview_flash_diverse_cal.csv")

# %%
def get_gt(review_filename):
    paper_id = review_filename.split(".")[0]
    row = df[df["paper_id"] == paper_id]
    return row["gt_avg_score"]

# %%
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

# %%
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

# %%
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

# %%
import pickle
emb_path = "../datasets/human_reviews_embeddings_deepreview.pkl"
idx_path = "../datasets/human_review_score_index_deepreview.pkl"

with open(emb_path, "rb") as f:
    review_embeddings = pickle.load(f)

with open(idx_path, "rb") as f:
    review_score_index = pickle.load(f)


# %%
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

import tqdm
with ThreadPoolExecutor(max_workers=50) as executor:
    ds = list(tqdm.tqdm(executor.map(build_sample, os.listdir(reviews)), total=len(os.listdir(reviews))))

# %%
from datasets import Dataset
ds_hf = Dataset.from_list(ds)
ds_hf.push_to_hub("weathon/grpo_dataset")

# %%
