#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="claude_sdk:claude-opus-4-7"
export MERGER_MODEL="claude_sdk:claude-opus-4-7"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export OUTPUT_CSV="bench_scores_deepreview_cal.csv"
export MERGE_LOG="pipeline_whole_deepreview_cal.log"
export CONCURRENCY=3
export MAX_PAPERS=500

ollama serve &
OLLAMA_PID=$! 
trap "kill $OLLAMA_PID 2>/dev/null" EXIT

# python code/main.py --n_samples 200 --benchmark ~/review_agent/iclr2025 --seed $(cksum <<< '45678692954567875456' | cut -f 1 -d ' ')
python code/main.py --n_samples 2000 --benchmark datasets/deepreview_13k_test/ --seed $(cksum <<< '45678692954567875456' | cut -f 1 -d ' ')
