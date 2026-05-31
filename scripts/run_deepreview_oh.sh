#!/usr/bin/env bash
# Run code_oh (OpenHarness-only port of code/main.py) over the DeepReview-13k
# test split. All three agents (Harsh, Strength Finder, Merger) run via the
# oh_agent_sdk shim → OpenHarness's resolved API client (codex / claude / api-key
# — whichever `oh auth ...` profile is active locally).
#
# Both merger variants (cal + no_cal) run per paper and write to split CSVs +
# review dirs (see code_oh/main.py:_bench_output_paths).

set -e
cd "$(dirname "$0")/.."

export HARSH_MODEL="${HARSH_MODEL:-gpt-5.2}"
export MERGER_MODEL="${MERGER_MODEL:-gpt-5.2}"
export NEUTRAL_MODEL="${NEUTRAL_MODEL:-gpt-5.4-mini}"
export SWEEP_NAME="${SWEEP_NAME:-2026_oh_repro}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
export MERGE_LOG="${SWEEP_NAME}/merge.log"
export CONCURRENCY="${CONCURRENCY:-1}"
export MAX_PAPERS="${MAX_PAPERS:-30}"
export CALIBRATION_SET="${CALIBRATION_SET:-deepreview}"
export PAPERS_DIR="${PAPERS_DIR:-$HOME/split_review/datasets/iclr2026_new/papers}"

LOG_FILE="results/${SWEEP_NAME}/merge.log"
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
  cp -r code_oh oh_agent_sdk prompts "$SNAPSHOT_DIR/"
  cp scripts/run_deepreview_oh.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code_oh oh_agent_sdk prompts scripts/run_deepreview_oh.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "HARSH_MODEL=$HARSH_MODEL"
  echo "MERGER_MODEL=$MERGER_MODEL"
  echo "NEUTRAL_MODEL=$NEUTRAL_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MAX_PAPERS=$MAX_PAPERS"
  echo "CALIBRATION_SET=$CALIBRATION_SET"
  echo "PAPERS_DIR=$PAPERS_DIR"
} >> "$LOG_FILE"

python code_oh/main.py --n_samples "$MAX_PAPERS" --benchmark "$PAPERS_DIR/.." --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
