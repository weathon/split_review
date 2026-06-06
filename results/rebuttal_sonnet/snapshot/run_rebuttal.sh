#!/usr/bin/env bash
# Run the rebuttal + meta-review pipeline over an existing set of reviews.
# Requires a completed main.py run (input reviews in INPUT_REVIEWS_DIR, papers in PAPERS_DIR).

set -e
cd "$(dirname "$0")/.."

export REBUTTAL_MODEL="${REBUTTAL_MODEL:-claude_sdk:claude-sonnet-4-6}"
export SWEEP_NAME="${SWEEP_NAME:-rebuttal_sonnet}"
export CONCURRENCY="${CONCURRENCY:-5}"
export INPUT_REVIEWS_DIR="${INPUT_REVIEWS_DIR:-/home/wg25r/split_review_opus_repro/results/2026_sonnet_repro/reviews}"
export PAPERS_DIR="${PAPERS_DIR:-/home/wg25r/split_review_opus_repro/datasets/iclr2026_new/papers}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
export REBUTTAL_LOG="${SWEEP_NAME}/rebuttal.log"
export MERGE_LOG="${REBUTTAL_LOG}"
export OPENROUTER_PROVIDER="${OPENROUTER_PROVIDER:-deepseek}"

LOG_FILE="results/${REBUTTAL_LOG}"
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
  cp scripts/run_rebuttal.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_rebuttal.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "REBUTTAL_MODEL=$REBUTTAL_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "INPUT_REVIEWS_DIR=$INPUT_REVIEWS_DIR"
  echo "PAPERS_DIR=$PAPERS_DIR"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
  echo "REBUTTAL_LOG=$REBUTTAL_LOG"
  echo "OPENROUTER_PROVIDER=$OPENROUTER_PROVIDER"
} >> "$LOG_FILE"

python code/rebuttal.py --batch "$INPUT_REVIEWS_DIR" "$PAPERS_DIR"
