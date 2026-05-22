#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
# final run
set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="deepseek-v4-flash"
export MERGER_MODEL="deepseek-v4-flash"
export NEUTRAL_MODEL="deepseek-v4-flash"
export OUTPUT_CSV="fresh_cal.csv"
export MERGE_LOG="fresh_cal.log" 
export CONCURRENCY=30
export MAX_PAPERS=3000
export CALIBRATION_SET="2025"
export REVIEWS_DIR="fresh_cal"

ollama serve &

LOG_FILE="results/${MERGE_LOG}"
mkdir -p "$(dirname "$LOG_FILE")"
{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "OPENAI_DEFAULT_MODEL=$OPENAI_DEFAULT_MODEL"
  echo "HARSH_MODEL=$HARSH_MODEL"
  echo "MERGER_MODEL=$MERGER_MODEL"
  echo "NEUTRAL_MODEL=$NEUTRAL_MODEL"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "MERGE_LOG=$MERGE_LOG"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MAX_PAPERS=$MAX_PAPERS"
  echo "CALIBRATION_SET=$CALIBRATION_SET"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
} >> "$LOG_FILE"


# python code/main.py --n_samples 2000 --benchmark ~/review_agent/iclr2026_new --seed $(cksum <<< '384758' | cut -f 1 -d ' ')
# use some test as training
python code/main.py --n_samples 5000 --benchmark datasets/deepreview_13k_train/ --no_cal --include_cal_papers --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
# python code/main.py --n_samples 500 --benchmark datasets/deepreview_13k_test_mini/ --seed $(cksum <<< '2343' | cut -f 1 -d ' ')

# --no_cal --include_cal_papers