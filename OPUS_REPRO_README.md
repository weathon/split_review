# 2026_opus reproduction snapshot

This clone preserves the exact source state used to produce the
**2026_opus** baseline (n=393 papers, Spearman ρ=0.677, AUROC=0.825,
Pearson r=0.721). That run beat single-human reviewer correlation and
matched the N-1 human consensus correlation — significantly better than
any of the DeepSeek-based runs in the ablation repo.

## Provenance

- **Commit checked out**: `8757ca3575` ("2025 finished", May 19 2026 20:37 PDT)
  on the `split_review` repo. This is the last commit before the opus run
  started at May 19 23:40 PDT.
- **Models** (from `results/2026_opus/merge.log`):
  - Harsh Critic: `claude_sdk:claude-opus-4-7` (Claude Agent SDK path)
  - Merger: `claude_sdk:claude-opus-4-7` (Claude Agent SDK path)
  - Strength Finder: `deepseek-v4-flash` via OpenRouter (deepseek provider)
- **Per-paper cost**: ~$1.47 (Claude Opus 4.7 on a 5-hour plan)
- **Total cost** for the 393-paper run: ~$580

## Frozen artifacts

`results/2026_opus/`:
- `scores.csv` — 395-line CSV with predicted score / decision per paper
- `reviews/` — 393 individual paper review markdown files
- `merge.log` — full pipeline log with token usage, costs, and merged
  inputs for every paper
- `metrics/` — Spearman/Pearson/AUROC/MAE reports and correlation plots
- `2026_opus_scatter.png` — predicted-vs-true scatter

## Modifications to the frozen state

This clone has *minimal* edits on top of `8757ca3575`, to bring forward
features added later that are useful for replication but not behavior-
changing:

1. **`scripts/run_deepreview_claude.sh`** — adds:
   - `SWEEP_NAME` env var (defaults to `2026_opus_repro`); all output
     paths are derived from it so reruns don't overwrite the frozen
     artifacts in `results/2026_opus/`
   - Snapshot mechanism: every run writes `results/<sweep>/snapshot/`
     with copies of `code/`, `prompts/`, the script itself, and the
     current `git rev-parse HEAD` + `git status` + `git diff HEAD`
   - `BYPASS_SNAPSHOT=1` to skip the snapshot guard when intentionally
     rerunning into an existing sweep
   - `OPENROUTER_PROVIDER` env var (defaults to `deepseek`) so the
     Strength Finder routing is locked

2. **`code/main.py`** — adds:
   - Reads `OPENROUTER_PROVIDER` env var instead of hardcoding
     `"deepseek"`. Default behavior unchanged.

Nothing else in `code/`, `prompts/`, or any other source file is
modified. The pipeline behavior is identical to the original run.

## Reproducing the run

```bash
# Set ANTHROPIC_API_KEY and OPENROUTER_API_KEY_OURS in .env first.
# Pricing: ~$580 for the full 393-paper run on Claude Opus 4.7.

# Tiny smoke test (10 papers):
SWEEP_NAME=opus_smoke MAX_PAPERS=10 bash scripts/run_deepreview_claude.sh

# Full reproduction (393 papers):
SWEEP_NAME=2026_opus_repro2 MAX_PAPERS=400 bash scripts/run_deepreview_claude.sh

# Evaluate against the frozen scores:
python code/metric.py results/2026_opus_repro2/scores.csv
```

## Why this snapshot exists

The DeepSeek-based runs in `split_review_ablation/` consistently come in
~0.04 ρ below the Opus baseline despite using nearly identical prompts.
That gap appears to be an actual model-quality difference (Opus 4.7 vs
DeepSeek v4 Flash), not a regression introduced by prompt or code
edits. This clone exists so we always have a clean reference point for
the result we should be matching, with enough infrastructure to rerun
it on demand if needed.
