# Task: Prompt Combination Sweep for Split Review

## Context
This is a multi-agent paper review system with multiple prompt versions:
- `prompts/` — current version
- `prompts.bak/` — backup version 1
- `prompts.bak.2/` — backup version 2

All three folders have the same files (one-to-one correspondence), just different versions of each prompt. The system runs via `scripts/run_deepreview.sh` and evaluates via `code/metric.py [csv_path]`.

## Goal
Find the best combination of prompt versions across agents, optimizing for:
1. **Diversity** — reviews should not be a checklist of all common problems, should not list similar problems for every paper, and should not turn every paper into the same form
2. **Validity** — points raised must be substantive, not nitpicky or bad-faith
3. **Accuracy** — scores should correlate with human ground truth (metric.py output)

## Rules
- **NEVER modify anything in `code/`. ** Only touch the active `prompts/` and `scripts/` folder.
- Before doing anything, back up the current prompts: `cp -r prompts/ prompts.bak.sweep_$(date +%s)`
- Each test run uses **100 papers** only. Find how to limit this.
- Save each run's output to a **unique folder** (e.g., `results/sweep_v1/`, `results/sweep_v2/`, ...). Do NOT overwrite existing results.

## Approach 

### Phase 0: Recon
1. List every file in `prompts/`, `prompts.bak/`, and `prompts.bak.2/`. Confirm they correspond 1:1.
2. Diff each file across the three versions. For each prompt file, summarize what's actually different between versions (not just "they differ" — understand HOW they differ in intent, tone, rubric, structure).
3. Read `scripts/run_deepreview.sh` to understand how to control paper count and output path.
4. Run `code/metric.py` on an existing result CSV to get a baseline.

### Phase 1: Run Experiments
For each planned combination:
1. Copy the chosen version of each prompt file into `prompts/`
2. Run the pipeline (100 papers)
3. Save results to unique folder
4. Run metric.py, record the score
5. Log in `results/sweep_log.md`: which version of each file was used, the score, and any observations

### Phase 2: Iterate
After initial experiments:
- If a clear "best base" combination emerges, try targeted tweaks on top of it
- If certain prompt files don't affect scores much, fix them and focus on the ones that do
- Try at least one hybrid version where you merge the best parts of different versions for the same prompt file

### Phase 3: Report
Update `results/sweep_log.md` with:
- Summary table: experiment ID → version combo → score
- Best combination and why
- Which prompt files matter most (sensitivity analysis)
- Any hybrid versions you created and how they performed
- Install the best-performing combination as the new `prompts/`