#!/usr/bin/env bash
# Calibrate already-generated nocal reviews (results/original_nocal/reviews/*.md).
# Reads each review, runs the merger's calibration_search logic, writes
# results/original_nocal/calibrated_scores.csv. Resumes automatically.
set -e
cd "$(dirname "$0")/.."

export CAL_MODEL="${CAL_MODEL:-claude-opus-4-7}"
export CONCURRENCY="${CONCURRENCY:-3}"
export CAL_REVIEW_DIR="${CAL_REVIEW_DIR:-results/original_nocal/reviews}"
export POST_HOC_CAL_CSV="${POST_HOC_CAL_CSV:-results/original_nocal/calibrated_scores.csv}"
export POST_HOC_GT_CSV="${POST_HOC_GT_CSV:-$HOME/review_agent/iclr2026_new/ratings.csv}"
# Set CAL_LIMIT=2 for a smoke run over the first 2 reviews.
export CAL_LIMIT="${CAL_LIMIT:-0}"

LOG_FILE="${POST_HOC_CAL_CSV%.csv}.log"
mkdir -p "$(dirname "$LOG_FILE")"
{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "CAL_MODEL=$CAL_MODEL"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "CAL_REVIEW_DIR=$CAL_REVIEW_DIR"
  echo "POST_HOC_CAL_CSV=$POST_HOC_CAL_CSV"
  echo "POST_HOC_GT_CSV=$POST_HOC_GT_CSV"
  echo "CAL_LIMIT=$CAL_LIMIT"
} >> "$LOG_FILE"

/home/wg25r/miniconda/envs/neg/bin/python code/cal_agent.py
