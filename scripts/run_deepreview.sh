#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="deepseek-v4-pro"
export MERGER_MODEL="deepseek-v4-pro"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export OUTPUT_CSV="bench_scores_deepreview_cal_dsor.csv"
export MERGE_LOG="pipeline_whole_deepreview_cal_dsor.log"
export CONCURRENCY=10
export MAX_PAPERS=500
export CALIBRATION_SET="deepreview"

ollama serve &


# python code/main.py --n_samples 500 --benchmark ~/review_agent/iclr2025 --seed $(cksum <<< '384758' | cut -f 1 -d ' ')
python code/main.py --n_samples 2000 --benchmark datasets/deepreview_13k_test/ --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
