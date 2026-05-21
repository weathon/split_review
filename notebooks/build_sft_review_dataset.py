import re
from pathlib import Path

import dotenv
import pandas as pd
from datasets import Dataset, DatasetDict


dotenv.load_dotenv(".env")

csv_path = Path("results/fresh_cal.csv")
review_dir = Path("results/fresh_cal")
repo_id = "weathon/sft_review"
random_state = 7
test_size = 0.1

system_prompt = (
    "Predict the average reviewer score for this paper review. "
    "Return only a single number with one decimal place."
)


def strip_self_prediction(review_text):
    review_text = re.split(r"\n## Score and Decision\b", review_text, maxsplit=1)[0]
    review_text = re.sub(r"(?im)^.*MY FINAL SCORE:.*\n?", "", review_text)
    review_text = re.sub(r"(?im)^.*MY FINAL DECISION:.*\n?", "", review_text)
    return review_text.strip()


df = pd.read_csv(csv_path)
if df["gt_avg_score"].isna().any():
    raise ValueError("gt_avg_score has missing values")

rows = []
for row in df.itertuples(index=False):
    path = review_dir / f"{row.paper_id}.md"
    if not path.exists():
        raise FileNotFoundError(path)

    review_text = strip_self_prediction(path.read_text())
    if not review_text:
        raise ValueError(f"empty stripped review for {row.paper_id}")

    rows.append(
        {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": review_text},
                {"role": "assistant", "content": f"{float(row.gt_avg_score):.1f}"},
            ],
        }
    )

dataset = Dataset.from_list(rows)
splits = dataset.train_test_split(test_size=test_size, seed=random_state)
dataset_dict = DatasetDict({"train": splits["train"], "test": splits["test"]})

print(dataset_dict)
print(dataset_dict["train"][0]["messages"][0])
print(dataset_dict["train"][0]["messages"][2])
dataset_dict.save_to_disk("results/sft_review_hf")
dataset_dict.push_to_hub(repo_id)
print(f"pushed {repo_id}")
