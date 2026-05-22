#!/usr/bin/env bash
# Run the multi-agent reviewer on the ICML 2025 position-paper test split.
# Edit the values below to switch models / output paths.
set -e
cd "$(dirname "$0")/.."

export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="claude_sdk:claude-opus-4-7"
export MERGER_MODEL="claude_sdk:claude-opus-4-7"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export SUBAGENT_MODEL="ollama:glm-5.1:cloud"
export OUTPUT_CSV="bench_scores_position.csv"
export MERGE_LOG="pipeline_whole_position.log"
export CONCURRENCY=5
export MAX_PAPERS=200

ollama serve &
OLLAMA_PID=$!
trap "kill $OLLAMA_PID 2>/dev/null" EXIT

LOG_FILE="results/${MERGE_LOG}"
mkdir -p "$(dirname "$LOG_FILE")"
{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "OPENAI_DEFAULT_MODEL=$OPENAI_DEFAULT_MODEL"
  echo "HARSH_MODEL=$HARSH_MODEL"
  echo "MERGER_MODEL=$MERGER_MODEL"
  echo "NEUTRAL_MODEL=$NEUTRAL_MODEL"
  echo "SUBAGENT_MODEL=$SUBAGENT_MODEL"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "MERGE_LOG=$MERGE_LOG"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MAX_PAPERS=$MAX_PAPERS"
} >> "$LOG_FILE"

python code/main.py --n_samples 200 --benchmark datasets/icml2025_position/ --position --seed $(cksum <<< '🍍position' | cut -f 1 -d ' ')
