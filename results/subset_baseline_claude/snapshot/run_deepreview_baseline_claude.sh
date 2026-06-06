#!/usr/bin/env bash
# Single-agent Claude SDK baseline reviewer: the model gets only the paper
# (via read_file) and a simple review guideline, then produces a review + score.

set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export BASELINE_MODEL="${BASELINE_MODEL:-claude-sonnet-4-6}"
export SWEEP_NAME="${SWEEP_NAME:-subset_baseline_claude}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export MERGE_LOG="${SWEEP_NAME}/merge.log"
export CONCURRENCY="${CONCURRENCY:-5}"
export MAX_PAPERS="${MAX_PAPERS:-400}"
export PAPERS_DIR="${PAPERS_DIR:-/home/wg25r/split_review_opus_repro/datasets/iclr2026_subset/papers}"
# export PAPERS_DIR="${PAPERS_DIR:-$HOME/split_review/datasets/iclr2026_new/papers}"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"

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
  cp scripts/run_deepreview_baseline_claude.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_deepreview_baseline_claude.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "BASELINE_MODEL=$BASELINE_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "MERGE_LOG=$MERGE_LOG"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MAX_PAPERS=$MAX_PAPERS"
  echo "PAPERS_DIR=$PAPERS_DIR"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
} >> "$LOG_FILE"

python code/baseline_claude.py --n_samples "$MAX_PAPERS" --benchmark "$PAPERS_DIR/.." --reviews_dir "$REVIEWS_DIR" --model "$BASELINE_MODEL" --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
