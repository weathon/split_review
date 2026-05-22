# #!/usr/bin/env bash
# # Run the multi-agent reviewer on the DeepReview-13k test split.
# # Edit the values below to switch models / output paths.
# # final run
# set -e
# cd "$(dirname "$0")/.."

# export ANTHROPIC_API_KEY=""
# export OPENAI_DEFAULT_MODEL="glm-5.1"
# export HARSH_MODEL="deepseek-v4-pro"
# export MERGER_MODEL="deepseek-v4-pro"
# export NEUTRAL_MODEL="deepseek-v4-pro"
# export OUTPUT_CSV="2026_pro_deepreview_cal.csv"
# export MERGE_LOG="2026_pro_deepreview_cal.log" 
# export CONCURRENCY=50
# export MAX_PAPERS=400
# export CALIBRATION_SET="deepreview"
# # export CALIBRATION_SET="2026"
# export REVIEWS_DIR="2026_pro_deepreview_cal"

# ollama serve & 


# python code/main.py --n_samples 2000 --benchmark ~/review_agent/iclr2026_new --seed $(cksum <<< '384758' | cut -f 1 -d ' ')
# # use some test as training
# # python code/main.py --n_samples 2000 --benchmark datasets/deepreview_13k_train/ --no_cal --include_cal_papers --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
# # python code/main.py --n_samples 500 --benchmark datasets/deepreview_13k_test --seed $(cksum <<< '2343' | cut -f 1 -d ' ')

# # --no_cal --include_cal_papers

#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
# final run


#!/usr/bin/env bash
# Run the multi-agent reviewer on the DeepReview-13k test split.
# Edit the values below to switch models / output paths.
# final run
set -e
cd "$(dirname "$0")/.."

export ANTHROPIC_API_KEY=""
export OPENAI_DEFAULT_MODEL="glm-5.1"
export HARSH_MODEL="deepseek-v4-flash"
export MERGER_MODEL="deepseek-v4-flash"
export NEUTRAL_MODEL="deepseek-v4-flash"
export SWEEP_NAME="final_deepreview_cal"
export OUTPUT_CSV="${SWEEP_NAME}/scores.csv"
export MERGE_LOG="${SWEEP_NAME}/merge.log" 
export CONCURRENCY="${CONCURRENCY:-50}"
export MAX_PAPERS="${MAX_PAPERS:-400}"
export CALIBRATION_SET="deepreview"
# export CALIBRATION_SET="deepreview"
export PAPERS_DIR="$HOME/review_agent/iclr2026_new/papers"
export REVIEWS_DIR="${SWEEP_NAME}/reviews"

LOG_FILE="results/${MERGE_LOG}"
mkdir -p "$(dirname "$LOG_FILE")"
{
  echo "============================================================"
  echo "Config @ $(date '+%Y-%m-%dT%H:%M:%S')"
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
} >> "$LOG_FILE"

/home/wg25r/miniconda/envs/neg/bin/python code/main.py --n_samples "$MAX_PAPERS"  --benchmark ~/review_agent/iclr2026_new --seed $(cksum <<< '384758' | cut -f 1 -d ' ')
# use some test as training
# python code/main.py --n_samples 2000 --benchmark datasets/deepreview_13k_train/ --no_cal --include_cal_papers --seed $(cksum <<< '2343' | cut -f 1 -d ' ')
# python code/main.py --n_samples 500 --benchmark datasets/deepreview_13k_test_uniform --seed $(cksum <<< '2343' | cut -f 1 -d ' ')

# --no_cal --include_cal_papers
