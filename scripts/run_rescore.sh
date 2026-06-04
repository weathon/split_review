#!/usr/bin/env bash
# Re-score papers from a cached merger pipeline log.
# Requires a completed main.py run (the merge.log with cached harsh critic + strength finder outputs).
#
# Required env vars:
#   MERGER_LOG  — path to the pipeline merge.log file
#
# Optional env vars:
#   RESCORE_MODEL  — model to use for re-scoring (default: deepseek-v4-flash)
#   PAPERS_DIR     — override papers directory (remap paths from the log)
#   SWEEP_NAME     — output directory name under results/ (default: rescore)
#   CONCURRENCY    — number of concurrent papers (default: 5)

set -e
cd "$(dirname "$0")/.."

export RESCORE_MODEL="${RESCORE_MODEL:-claude_sdk:claude-sonnet-4-6}"
export SWEEP_NAME="${SWEEP_NAME:-2026_sonnet_rescore}"
export CONCURRENCY="${CONCURRENCY:-5}"
export MERGER_LOG="${MERGER_LOG:-/home/wg25r/split_review_opus_repro/results/2026_sonnet_repro/merge.log}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
export RESCORE_LOG="${SWEEP_NAME}/rescore.log"
export OPENROUTER_PROVIDER="${OPENROUTER_PROVIDER:-deepseek}"

LOG_FILE="results/${RESCORE_LOG}"
mkdir -p "$(dirname "$LOG_FILE")"

# Ensure output directory doesn't overlap with input log directory
MERGER_LOG_DIR="$(cd "$(dirname "$MERGER_LOG")" && pwd)"
OUTPUT_DIR="$(mkdir -p "results/${SWEEP_NAME}" && cd "results/${SWEEP_NAME}" && pwd)"
if [ "$MERGER_LOG_DIR" = "$OUTPUT_DIR" ]; then
  echo "ERROR: Output directory (results/${SWEEP_NAME}) is the same as the input log directory ($MERGER_LOG_DIR). Use a different SWEEP_NAME." >&2
  exit 1
fi

SNAPSHOT_DIR="results/${SWEEP_NAME}/snapshot"
if [ -e "$SNAPSHOT_DIR" ]; then
  if [ "${BYPASS_SNAPSHOT:-0}" = "1" ]; then
    echo "BYPASS_SNAPSHOT=1: $SNAPSHOT_DIR already exists, keeping existing snapshot."
  else
    echo "ERROR: $SNAPSHOT_DIR already exists. Bump SWEEP_NAME, or rerun with BYPASS_SNAPSHOT=1." >&2
    exit 1
  fi
else
  mkdir -p "$SNAPSHOT_DIR"
  cp -r code prompts "$SNAPSHOT_DIR/"
  cp scripts/run_rescore.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_rescore.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "RESCORE_MODEL=$RESCORE_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "MERGER_LOG=$MERGER_LOG"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
  echo "RESCORE_LOG=$RESCORE_LOG"
  echo "OPENROUTER_PROVIDER=$OPENROUTER_PROVIDER"
  [ -n "${PAPERS_DIR:-}" ] && echo "PAPERS_DIR=$PAPERS_DIR"
} >> "$LOG_FILE"

PAPERS_ARG=""
if [ -n "${PAPERS_DIR:-}" ]; then
  PAPERS_ARG="--papers_dir $PAPERS_DIR"
fi

python code/rescore.py "$MERGER_LOG" $PAPERS_ARG
