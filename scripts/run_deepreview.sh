#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
# final run
set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="deepseek-v4-pro"
export MERGER_MODEL="deepseek-v4-pro"
export NEUTRAL_MODEL="deepseek-v4-pro"
export OUTPUT_CSV="2026_pro_deepreview_cal.csv"
export MERGE_LOG="2026_pro_deepreview_cal.log" 
export CONCURRENCY=50
export MAX_PAPERS=300
export CALIBRATION_SET="deepreview"
# export CALIBRATION_SET="2026"
export REVIEWS_DIR="2026_pro_deepreview_cal"

ollama serve & 


python code/main.py --n_samples 2000 --benchmark ~/review_agent/iclr2026_new --seed $(cksum <<< '384758' | cut -f 1 -d ' ')
# use some test as training
# python code/main.py --n_samples 2000 --benchmark datasets/deepreview_13k_train/ --no_cal --include_cal_papers --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
# python code/main.py --n_samples 500 --benchmark datasets/deepreview_13k_test --seed $(cksum <<< '2343' | cut -f 1 -d ' ')

# --no_cal --include_cal_papers