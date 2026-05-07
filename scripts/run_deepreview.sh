#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
set -e
cd "$(dirname "$0")/.."

export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="gpt-5.5"
export MERGER_MODEL="ollama:glm-5.1:cloud"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export SUBAGENT_MODEL="ollama:glm-5.1:cloud"
export OUTPUT_CSV="bench_scores_deepreview.csv"
export MERGE_LOG="pipeline_whole_deepreview.log"
export CONCURRENCY=5
export MAX_PAPERS=100

ollama serve &
OLLAMA_PID=$!
trap "kill $OLLAMA_PID 2>/dev/null" EXIT

python code/main.py --n_samples 200 --benchmark datasets/deepreview_13k_test/ --seed $(cksum <<< '45678692954567875456' | cut -f 1 -d ' ')
