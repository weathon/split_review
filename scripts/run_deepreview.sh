#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
set -e
cd "$(dirname "$0")/.."

export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="ollama:glm-5.1:cloud"
export MERGER_MODEL="ollama:glm-5.1:cloud"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export SUBAGENT_MODEL="ollama:glm-5.1:cloud"
export OUTPUT_CSV="bench_scores_deepreview.csv"
export MERGE_LOG="pipeline_whole_deepreview.log"
export CONCURRENCY=5
export MAX_PAPERS=200

python code/main.py \
  --n_samples 200 \
  --benchmark datasets/deepreview_13k_test/ \
  --seed "$(cksum <<< "$(date +%s)" | cut -f1 -d' ')"
