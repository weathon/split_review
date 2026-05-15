#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

PAPER="datasets/deepreview_13k_test/papers/0AYosSFETw.txt"
# PAPER="/home/wg25r/review_agent/new/ELErARGR5U.md"
LOG="run.log"

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="deepseek-v4-pro"
export MERGER_MODEL="deepseek-v4-pro"
export NEUTRAL_MODEL="ollama:glm-5.1:cloud"

# export HARSH_MODEL="ollama:glm-5.1:cloud"
# export MERGER_MODEL="ollama:glm-5.1:cloud"
# export NEUTRAL_MODEL="ollama:glm-5.1:cloud"
# export SUBAGENT_MODEL="ollama:glm-5.1:cloud"
export CONCURRENCY="1"
export PYTHONUNBUFFERED=1

/home/wg25r/miniconda/envs/neg/bin/python -u code/main.py --single_paper "$PAPER" #--no_cal #--position 2>&1 | tee "$LOG"
