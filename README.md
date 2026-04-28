# Split Review

Multi-agent paper reviewer with calibration retrieval against the DeepReview-13K human-review corpus.

## Layout

```
code/        Python implementation (main.py, tools.py, claude_merger.py, ...)
prompts/     Agent system prompts (markdown)
datasets/    DeepReview-13K calibration + test splits.
             The embeddings/score-index pickles are NOT in git — they are
             auto-downloaded on first use from
             https://huggingface.co/datasets/weathon/paper_embeddings
results/     Benchmark CSVs and scatter plots from prior runs
scripts/     Convenience launchers
```

Path resolution lives in [code/paths.py](code/paths.py). All defaults assume the
layout above; override with `REVIEW_REPO_ROOT`, `REVIEW_PROMPTS_DIR`,
`REVIEW_DATASETS_DIR`, `REVIEW_RESULTS_DIR`.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # then fill in keys
```

The two embedding pickles are downloaded automatically from the HuggingFace
dataset repo `weathon/paper_embeddings` on first run (cached in `datasets/`).
Override with `REVIEW_HF_REPO` if you fork/mirror them.

Required env vars (in `.env`):

- `OPENROUTER_API_KEY` — calibration embeddings & default model traffic
- `OPENAI_API_KEY` — Weave tracing
- `ANTHROPIC_API_KEY` — only if `MERGER_MODEL=claude_sdk:...`

## Run

```bash
./scripts/run_deepreview.sh
```

Or directly:

```bash
python code/main.py \
  --benchmark datasets/deepreview_13k_test/ \
  --n_samples 200 \
  --seed 42
```

Outputs land in `results/` (CSV + per-paper review markdown under
`results/bench_reviews/`).

## Building the calibration artifacts from scratch

The pickles in `datasets/` are prebuilt. To regenerate them from the public
HuggingFace `deepreview/DeepReview-13K` dataset:

```bash
python code/build_deepreview.py
```

## Notes

- `*.pkl` files are tracked via Git LFS (see `.gitattributes`).
- The repo is configured for the DeepReview calibration set only. Older
  ICLR-2025/2026 and NeurIPS position-paper code paths were trimmed.
