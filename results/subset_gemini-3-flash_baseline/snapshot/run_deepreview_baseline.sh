#!/usr/bin/env bash
# Run the single-call OpenRouter baseline reviewer.

set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export BASELINE_MODEL="${BASELINE_MODEL:-gemini-3-flash-preview}"
export SWEEP_NAME="${SWEEP_NAME:-subset_gemini-3-flash_baseline}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export MERGE_LOG="${SWEEP_NAME}/merge.log"
export CONCURRENCY="${CONCURRENCY:-5}"
export MAX_PAPERS="${MAX_PAPERS:-100}"
export CALIBRATION_SET="deepreview"
export PAPERS_DIR="${PAPERS_DIR:-/home/wg25r/split_review_opus_repro/datasets/iclr2026_subset/papers}"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
export OPENROUTER_PROVIDER="${OPENROUTER_PROVIDER:-google-ai-studio}"

LOG_FILE="results/${MERGE_LOG}"
mkdir -p "$(dirname "$LOG_FILE")"

SNAPSHOT_DIR="results/${SWEEP_NAME}/snapshot"
if [ -e "$SNAPSHOT_DIR" ]; then
  if [ "${BYPASS_SNAPSHOT:-0}" = "1" ]; then
    echo "BYPASS_SNAPSHOT=1: $SNAPSHOT_DIR already exists, keeping the existing snapshot and continuing."
  else
    echo "ERROR: $SNAPSHOT_DIR already exists. Bump SWEEP_NAME, or rerun with BYPASS_SNAPSHOT=1 to keep the existing snapshot and continue." >&2
    exit 1
  fi
else
  mkdir -p "$SNAPSHOT_DIR"
  cp -r code prompts "$SNAPSHOT_DIR/"
  cp scripts/run_deepreview_baseline.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_deepreview_baseline.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "OPENAI_DEFAULT_MODEL=$OPENAI_DEFAULT_MODEL"
  echo "BASELINE_MODEL=$BASELINE_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "MERGE_LOG=$MERGE_LOG"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MAX_PAPERS=$MAX_PAPERS"
  echo "CALIBRATION_SET=$CALIBRATION_SET"
  echo "PAPERS_DIR=$PAPERS_DIR"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
  echo "OPENROUTER_PROVIDER=$OPENROUTER_PROVIDER"
} >> "$LOG_FILE"

python code/baseline.py --n_samples "$MAX_PAPERS" --benchmark "$PAPERS_DIR/.." --reviews_dir "$REVIEWS_DIR" --model "$BASELINE_MODEL" --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
