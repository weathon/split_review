# %%
import os
import re
import csv
from pathlib import Path
from paths import ensure_hf_file, RESULTS_DIR
import pickle
import dotenv
dotenv.load_dotenv()
cal_path = "./datasets/deepreview_13k_calibration"
review_path = "./results/bench_reviews"

CAL_CSV_PATH = Path(os.getenv("POST_HOC_CAL_CSV", str(RESULTS_DIR / "post_hoc_cal_scores.csv")))
CAL_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
GT_CSV_PATH = Path(os.getenv("POST_HOC_GT_CSV", "./datasets/deepreview_13k_test/ratings.csv"))

CAL_CSV_HEADER = [
    "paper_id", "pred_score", "calibrated_score", "pred_decision",
    "gt_avg_score", "gt_decision", "gt_binary", "match", "cost", "sdk_savings",
    "gt_score_0", "gt_score_1", "gt_score_2", "gt_score_3", "gt_score_4", "gt_score_5", "gt_score_6",
]

_gt_index = {}
with open(GT_CSV_PATH, "r", newline="") as _f:
    for _row in csv.DictReader(_f):
        _gt_index[_row["paper_id"].strip()] = _row

if not CAL_CSV_PATH.exists() or CAL_CSV_PATH.stat().st_size == 0:
    with open(CAL_CSV_PATH, "w", newline="") as _f:
        csv.writer(_f).writerow(CAL_CSV_HEADER)
_logged_paper_ids = set()
if CAL_CSV_PATH.exists() and CAL_CSV_PATH.stat().st_size > 0:
    with open(CAL_CSV_PATH, "r", newline="") as _f:
        for _row in csv.DictReader(_f):
            _logged_paper_ids.add(_row["paper_id"])


emb_path = ensure_hf_file("human_reviews_embeddings_deepreview.pkl")
idx_path = ensure_hf_file("human_review_score_index_deepreview.pkl")


with open(emb_path, "rb") as f:
    review_embeddings = pickle.load(f)

with open(idx_path, "rb") as f:
    review_score_index = pickle.load(f)


# %%
os.environ["ANTHROPIC_API_KEY"] = ""

# %%
import numpy as np
reviews = os.listdir(review_path)

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

# %%
from openai import OpenAI
or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

# %%
prompt = """
You are given a paper review and a set of calibration reviews for comparison. For each calibration review, determine how different in strength and weakness the given review is from it. You have to read each review one by one and in full. 
You should NOT based on how the review characterizes the paper or how the review's tone (positive/negative) is. You should only based on the content (strengths and weaknesses) of the review. 
You have to read review one by one, after each one, do a pair-wise comparsion and output the comparsion and reasoning after each review. Use the read tool for one review at a time, do not call parallel read tools. 
Then produce a final estimated score for the given review on this scale:

1 - strong reject
3 - reject
4 - borderline reject
6 - borderline accept
8 - accept
10 - strong accept

Score must be between 1 and 10 in increments of 0.5.

Given Review:
{review_content}
Calibration Reviews (under `/home/wg25r/split_review/datasets/deepreview_13k_calibration`):
{calibration_reviews}


Output the final score in a <score> tag. 

"""

# %%
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock


async def cal_paper(review):
    paper_id = review.rsplit(".", 1)[0]
    if paper_id in _logged_paper_ids:
        print(f"  [{paper_id}] already logged — skipping")
        return

    with open(os.path.join(review_path, review), "r") as f:
        full_review = f.read()
    review_content = full_review.split("<score>")[0].replace("MY FINAL SCORE:", "").strip()

    raw_match = re.search(r"<score>([\d.]+)</score>", full_review)
    if not raw_match:
        raise RuntimeError(f"[{paper_id}] no <score> raw score found in review file")
    raw_score = float(raw_match.group(1))

    decision_match_re = re.search(r"<decision>(.*?)</decision>", full_review, re.DOTALL)
    pred_decision = decision_match_re.group(1).strip() if decision_match_re else "N/A"

    if paper_id not in _gt_index:
        raise RuntimeError(f"[{paper_id}] not found in ground truth {GT_CSV_PATH}")
    gt = _gt_index[paper_id]
    gt_scores = [gt.get(f"score_{i}", "") for i in range(7)]
    gt_binary = gt.get("gt_binary", "").strip()
    match_str = "N/A" if pred_decision in ("", "N/A", None) else ("YES" if pred_decision == gt_binary else "NO")

    query_embedding = or_client.embeddings.create(
        model="google/gemini-embedding-001",
        input=review_content,
        encoding_format="float",
    )
    query_vector = np.array(query_embedding.data[0].embedding)

    selected_names = []
    for name in bin_names:
        if len(bins_embeddings[name]) == 0:
            continue
        similarities = bins_embeddings[name] @ query_vector.T
        top_indices = np.argsort(similarities)[-2:]
        selected_names.extend(bins[name][idx] for idx in top_indices)


    response_text = ""
    async for message in query(
        prompt=prompt.format(
            review_content=review_content,
            calibration_reviews="\n".join(selected_names),
        ),
        options=ClaudeAgentOptions(model="claude-opus-4-7",
                                   allowed_tools=["Read"],
                                   disallowed_tools=["Bash", "Edit"],
                                   permission_mode="dontAsk"),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
                    response_text += block.text

    cal_match = re.search(r"<score>\s*([\d.]+)\s*</score>", response_text)
    if not cal_match:
        raise RuntimeError(f"[{paper_id}] no <score> tag in calibration response")
    calibrated_score = float(cal_match.group(1))

    gt_scores_padded = gt_scores + [""] * (7 - len(gt_scores))
    with open(CAL_CSV_PATH, "a", newline="") as f:
        csv.writer(f).writerow([
            paper_id,
            raw_score,
            calibrated_score,
            pred_decision,
            f"{float(gt.get('avg_score', 0)):.2f}",
            gt.get("decision", "").strip(),
            gt_binary,
            match_str,
            "0.0000",
            "0.0000",
            *gt_scores_padded,
        ])
    _logged_paper_ids.add(paper_id)
    print(f"  [{paper_id}] raw={raw_score} calibrated={calibrated_score} — logged to {CAL_CSV_PATH}")
    

    

# %%
for review in reviews: 
    asyncio.run(cal_paper(review))


