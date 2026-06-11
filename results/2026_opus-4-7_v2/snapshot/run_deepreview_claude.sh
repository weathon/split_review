#!/usr/bin/env bash
# Reproduce the 2026_opus 393-paper run (rho=0.677, AUROC=0.825).
# Original run was committed at 8757ca3575 ("2025 finished", May 19 2026).
# Harsh + Merger run on Claude SDK (claude-opus-4-7); Strength Finder runs
# on OpenRouter (deepseek-v4-flash).

set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="claude_sdk:claude-opus-4-7"
export MERGER_MODEL="claude_sdk:claude-opus-4-7"
export NEUTRAL_MODEL="mimo-v2.5-pro"
export SWEEP_NAME="${SWEEP_NAME:-2026_opus-4-7_v2}"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export MERGE_LOG="${SWEEP_NAME}/merge.log"
export CONCURRENCY="${CONCURRENCY:-2}"
export MAX_PAPERS="${MAX_PAPERS:-400}"
export CALIBRATION_SET="deepreview" 
export PAPERS_DIR="${PAPERS_DIR:-$HOME/split_review/datasets/iclr2026_new/papers}"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"
# Lock OpenRouter provider for the Strength Finder (deepseek only) so
# routing variance does not leak into the comparison.
export OPENROUTER_PROVIDER="${OPENROUTER_PROVIDER:-deepseek}"

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
  cp scripts/run_deepreview_claude.sh "$SNAPSHOT_DIR/"
  git rev-parse HEAD > "$SNAPSHOT_DIR/git_commit.txt" 2>/dev/null || echo "not-a-git-repo" > "$SNAPSHOT_DIR/git_commit.txt"
  git status --short > "$SNAPSHOT_DIR/git_status.txt" 2>/dev/null || true
  git diff HEAD -- code prompts scripts/run_deepreview_claude.sh > "$SNAPSHOT_DIR/git_diff.patch" 2>/dev/null || true
fi

{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
  echo "SNAPSHOT=${SNAPSHOT_DIR}"
  echo "GIT_COMMIT=$(cat "$SNAPSHOT_DIR/git_commit.txt")"
  echo "OPENAI_DEFAULT_MODEL=$OPENAI_DEFAULT_MODEL"
  echo "HARSH_MODEL=$HARSH_MODEL"
  echo "MERGER_MODEL=$MERGER_MODEL"
  echo "NEUTRAL_MODEL=$NEUTRAL_MODEL"
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

ollama serve &

python code/main.py --n_samples "$MAX_PAPERS" --benchmark "$PAPERS_DIR/.." --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
