from __future__ import annotations
import csv
import os
import random
import shutil
import sys
import time
from collections import defaultdict
from pathlib import Path

import pandas as pd
import tqdm
from dotenv import load_dotenv

load_dotenv()

SRC = Path("datasets/deepreview_13k_test")
DST = Path("datasets/deepreview_13k_test_uniform")
N = 300
SEED = 42

DST.mkdir(parents=True, exist_ok=True)
(DST / "papers").mkdir(exist_ok=True)
(DST / "human_reviews").mkdir(exist_ok=True)
(DST / "pdf").mkdir(exist_ok=True)

df = pd.read_csv(SRC / "ratings.csv")
print(f"Loaded {len(df)} papers")

rng = random.Random(SEED)
bins = defaultdict(list)
for _, row in df.iterrows():
    bins[round(row["avg_score"])].append(row)
for k in bins:
    rng.shuffle(bins[k])

sorted_bins = sorted(bins.keys())
print(f"{len(sorted_bins)} bins: {sorted_bins}")
for k in sorted_bins:
    print(f"  score~{k}: {len(bins[k])} available")

# Take min(N//nbins, available) per bin, then redistribute deficit greedily
n_bins = len(sorted_bins)
target = N // n_bins
samples = []
deficit = 0
leftovers = {}
for k in sorted_bins:
    take = min(target, len(bins[k]))
    samples.extend(bins[k][:take])
    leftovers[k] = bins[k][take:]
    deficit += target - take

deficit += N - len(samples) - sum(target - min(target, len(bins[k])) for k in sorted_bins)
needed = N - len(samples)
# fill remaining by taking from bins with leftovers, round-robin
while needed > 0:
    progress = False
    for k in sorted_bins:
        if needed == 0:
            break
        if leftovers[k]:
            samples.append(leftovers[k].pop(0))
            needed -= 1
            progress = True
    if not progress:
        break

print(f"Sampled {len(samples)} papers")
sampled_df = pd.DataFrame(samples)
print(sampled_df["avg_score"].round().value_counts().sort_index())

# write ratings.csv
sampled_df.to_csv(DST / "ratings.csv", index=False)

# copy text files and human reviews
for pid in tqdm.tqdm(sampled_df["paper_id"], desc="copy txt/reviews"):
    src_txt = SRC / "papers" / f"{pid}.txt"
    dst_txt = DST / "papers" / f"{pid}.txt"
    if src_txt.exists() and not dst_txt.exists():
        shutil.copy2(src_txt, dst_txt)
    src_rv = SRC / "human_reviews" / f"{pid}.md"
    dst_rv = DST / "human_reviews" / f"{pid}.md"
    if src_rv.exists() and not dst_rv.exists():
        shutil.copy2(src_rv, dst_rv)

# fetch PDFs
import openreview
username = os.environ["OPENREVIEW_USERNAME"]
password = os.environ["OPENREVIEW_PASSWORD"]
client = openreview.api.OpenReviewClient(
    username=username, password=password,
    baseurl="https://api2.openreview.net",
)

pdf_dir = DST / "pdf"
failed = []
for pid in tqdm.tqdm(sampled_df["paper_id"], desc="pdfs"):
    out = pdf_dir / f"{pid}.pdf"
    if out.exists() and out.stat().st_size > 1000:
        continue
    try:
        pdf_bytes = client.get_pdf(pid)
        if len(pdf_bytes) <= 1000:
            print(f"  short pdf for {pid}: {len(pdf_bytes)} bytes")
            failed.append(pid)
            continue
        out.write_bytes(pdf_bytes)
    except Exception as e:
        print(f"  fail {pid}: {e}")
        failed.append(pid)
        continue
    time.sleep(0.3)

print(f"Done. Failed: {len(failed)}")
if failed:
    (DST / "pdf_failed.txt").write_text("\n".join(failed))
