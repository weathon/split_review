import asyncio
import csv
import os
from pathlib import Path

import dotenv
from openai import AsyncOpenAI

dotenv.load_dotenv()

CSV_PATH = Path("/home/wg25r/split_review/results/fresh_cal.csv")
REVIEWS_DIR = Path("/home/wg25r/split_review/results/fresh_cal")

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


async def extract(review_text: str) -> tuple[float | None, str | None]:
    resp = await client.chat.completions.create(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "system", "content": "Extract the final numeric score and accept/reject decision from a paper review. Respond with exactly: <score>NUMBER</score><decision>Accept|Reject</decision>. No other text."},
            {"role": "user", "content": review_text},
        ],
        extra_body={"reasoning": {"enabled": False}},
    )
    text = resp.choices[0].message.content or ""
    print(f"  extractor raw: {text!r}")
    score = None
    decision = None
    if "<score>" in text:
        try:
            score = float(text.split("<score>")[1].split("</score>")[0].strip())
        except ValueError:
            pass
    if "<decision>" in text:
        decision = text.split("<decision>")[1].split("</decision>")[0].strip()
    return score, decision


async def main():
    with open(CSV_PATH, "r") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = rows[1:]

    targets = [(i, r) for i, r in enumerate(data) if r[1] == "-1" or r[1] == "-1.0"]
    print(f"Found {len(targets)} rows with pred_score=-1")

    for i, row in targets:
        pid = row[0]
        gt_binary = row[5]
        review_path = REVIEWS_DIR / f"{pid}.md"
        if not review_path.exists():
            print(f"[{pid}] missing review at {review_path}, skipping")
            continue
        review_text = review_path.read_text(encoding="utf-8")
        print(f"[{pid}] extracting ...")
        score, decision = await extract(review_text)
        if score is None or decision is None:
            print(f"[{pid}] extractor failed (score={score}, decision={decision}), leaving row alone")
            continue
        match = "YES" if decision == gt_binary else "NO"
        row[1] = str(score)
        row[2] = decision
        row[6] = match
        print(f"[{pid}] score={score} decision={decision} match={match}")

    with open(CSV_PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(data)
    print(f"Wrote {CSV_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
