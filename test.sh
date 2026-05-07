#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

PAPER="16.pdf"
# PAPER="/home/wg25r/review_agent/new/ELErARGR5U.md"
LOG="run.log"

export OPENAI_DEFAULT_MODEL="glm-5.1"
# export HARSH_MODEL="gpt-5.5"
# export MERGER_MODEL="gpt-5.5"
# export NEUTRAL_MODEL="gpt-5.5"
# export SUBAGENT_MODEL="gpt-5.5"
export HARSH_MODEL="ollama:glm-5.1:cloud"
export MERGER_MODEL="ollama:glm-5.1:cloud"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
export SUBAGENT_MODEL="ollama:glm-5.1:cloud"
export CONCURRENCY="1"
export PYTHONUNBUFFERED=1

/home/wg25r/miniconda/envs/neg/bin/python -u code/main.py --single_paper "$PAPER" --position 2>&1 | tee "$LOG"
