#!/usr/bin/env bash
# Pairwise-score papers from a cached merger pipeline log.
# For each paper: re-run merger with a 5-band bracketing-only calibration
# instruction, then pairwise-compare the merged review against every
# retrieved anchor and fit a Bradley-Terry score.
#
# Required env vars:
#   MERGER_LOG  — path to the pipeline merge.log file
#
# Optional env vars:
#   RESCORE_MODEL        — merger model (default: claude_sdk:claude-sonnet-4-6)
#   PAIRWISE_MODEL       — pairwise judge model (default: deepseek-v4-flash)
#   DATA_DIR             — dataset dir containing ratings.csv (default: iclr2026_new)
#   PAPERS_DIR           — override papers dir (remap paths from the log)
#   SWEEP_NAME           — output directory name under results/ (default: 2026_pairwise)
#   CONCURRENCY          — concurrent papers (default: 4)
#   PAIRWISE_CONCURRENCY — pairwise calls per paper (default: 20)
#   ANCHORS_PER_BAND     — anchors retrieved per band (default: 40)
#   BT_BETA              — Bradley-Terry temperature (default: 1.0)

set -e
cd "$(dirname "$0")/.."

export RESCORE_MODEL="${RESCORE_MODEL:-claude_sdk:claude-sonnet-4-6}"
export PAIRWISE_MODEL="${PAIRWISE_MODEL:-claude_sdk:claude-sonnet-4-6}"
export SWEEP_NAME="${SWEEP_NAME:-2026_pairwise}"
export CONCURRENCY="${CONCURRENCY:-2}"
export PAIRWISE_CONCURRENCY="${PAIRWISE_CONCURRENCY:-2}"
export ANCHORS_PER_BAND="${ANCHORS_PER_BAND:-8}"
export BT_BETA="${BT_BETA:-1.0}"
export MERGER_LOG="${MERGER_LOG:-/home/wg25r/split_review_opus_repro/results/2026_sonnet_repro/merge.log}"
export DATA_DIR="${DATA_DIR:-/home/wg25r/split_review/datasets/iclr2026_new}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
export PAIRWISE_LOG="${SWEEP_NAME}/pairwise.log"
export OPENROUTER_PROVIDER="${OPENROUTER_PROVIDER:-deepseek}"

LOG_FILE="results/${PAIRWISE_LOG}"
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
  cp scripts/run_pairwise_score.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_pairwise_score.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "RESCORE_MODEL=$RESCORE_MODEL"
  echo "PAIRWISE_MODEL=$PAIRWISE_MODEL"
  echo "SWEEP_NAME=$SWEEP_NAME"
  echo "CONCURRENCY=$CONCURRENCY"
  echo "PAIRWISE_CONCURRENCY=$PAIRWISE_CONCURRENCY"
  echo "ANCHORS_PER_BAND=$ANCHORS_PER_BAND"
  echo "BT_BETA=$BT_BETA"
  echo "MERGER_LOG=$MERGER_LOG"
  echo "DATA_DIR=$DATA_DIR"
  echo "OUTPUT_CSV=$OUTPUT_CSV"
  echo "REVIEWS_DIR=$REVIEWS_DIR"
  echo "PAIRWISE_LOG=$PAIRWISE_LOG"
  echo "OPENROUTER_PROVIDER=$OPENROUTER_PROVIDER"
  [ -n "${PAPERS_DIR:-}" ] && echo "PAPERS_DIR=$PAPERS_DIR"
} >> "$LOG_FILE"

PAPERS_ARG=""
if [ -n "${PAPERS_DIR:-}" ]; then
  PAPERS_ARG="--papers_dir $PAPERS_DIR"
fi

python code/pairwise_score.py "$MERGER_LOG" --data_dir "$DATA_DIR" $PAPERS_ARG
