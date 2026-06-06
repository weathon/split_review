#!/usr/bin/env bash
# Submit a single PDF to DeepReviewer-v2. The agent loop runs on OpenHarness
# via oh_agent_sdk (see deepreview/runner.py). Whichever `oh auth ...` profile
# is bound locally drives the LLM (codex / claude / api-key).
#
# Usage:
#   scripts/run_review.sh <path/to/paper.pdf> [parsed_papers_dir]
#
# The parsed_papers_dir must contain a <pdf_stem>.txt file with page markers
# in the form `{N}-----` separating each page.

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <path/to/paper.pdf> [parsed_papers_dir]" >&2
  exit 2
fi

PDF_PATH="$1"
PARSED_DIR="${2:-${PARSED_PAPERS_DIR:-$HOME/review_agent/iclr2026_new/papers}}"

cd "$(dirname "$0")/.."

export AGENT_MODEL="${AGENT_MODEL:-gpt-5.4}"
export AGENT_MAX_TURNS="${AGENT_MAX_TURNS:-200}"
export AGENT_RESUME_ATTEMPTS="${AGENT_RESUME_ATTEMPTS:-2}"
export PARSED_PAPERS_DIR="$PARSED_DIR"
export PAPER_SEARCH_ENABLED=false
export PAPER_SEARCH_PROVIDER=offline
export MIN_PAPER_SEARCH_CALLS_FOR_PDF_ANNOTATE=0
export MIN_PAPER_SEARCH_CALLS_FOR_FINAL=0
export MIN_DISTINCT_PAPER_QUERIES_FOR_FINAL=0
export FORCE_ENGLISH_OUTPUT=true
export UI_LANGUAGE=en

echo "============================================================"
echo "Submit @ $(date '+%Y-%m-%dT%H:%M:%S')"
echo "PDF=$PDF_PATH"
echo "PARSED_PAPERS_DIR=$PARSED_PAPERS_DIR"
echo "AGENT_MODEL=$AGENT_MODEL"
echo "AGENT_MAX_TURNS=$AGENT_MAX_TURNS"

python main.py submit --pdf "$PDF_PATH" --wait-seconds "${WAIT_SECONDS:-0}"
