## Summary

OGBench is a benchmark for offline goal-conditioned RL comprising 8 environment types, 85 datasets, and tuned implementations of 6 algorithms, designed to systematically probe specific capabilities (stitching, long-horizon reasoning, stochasticity handling, pixel-based control) that prior benchmarks aggregate into single scores. Experiments reveal interpretable strength/weakness profiles across methods—HIQL dominates stitching/long-horizon but collapses on stochastic teleport tasks, CRL is robust to stochasticity but fails at stitching, GCIQL excels at manipulation but struggles in locomotion.

## Strengths

1. **Capability-specific task design reveals differential algorithm performance.** The benchmark is structured so specific tasks isolate individual capabilities (stitching via `stitch` datasets, stochasticity via `teleport` mazes, long-horizon via `giant` mazes). Table results bear this out cleanly: HIQL dominates in stitching and long-horizon locomotion but drops sharply on teleport tasks (e.g., HIQL 18% vs CRL 53% on `antmaze-teleport-navigate`), while CRL is robust to stochasticity but fails on `stitch` datasets (0% on all pointmaze stitch tasks). Prior benchmarks like D4RL lack this diagnostic signal.

2. **Demonstrates that single-goal evaluation can reverse algorithm rankings.** Table "Do not use single-goal evaluation!" directly compares D4RL single-goal evaluation with OGBench's multi-goal evaluation on the same maze layout. GCIQL vs. QRL flips from 64% vs. 37% (single-goal) to 34% vs. 75% (multi-goal). This is concrete evidence that the benchmark's multi-goal design changes which methods appear state-of-the-art.

3. **Reference implementations are well-tuned and often exceed previously reported performance.** Table "vs_prior_work" shows that on D4RL `antmaze-large-diverse-v2`, CRL improves from 54% (original paper) to 79%, GCBC from 20% to 41%, and GCIQL from 30% to 64%. This provides stronger, more reliable baselines for future work.

4. **Controllable dataset generation yields actionable insights about data collection.** The noise ablation study (Figure "Datasets must be noisy enough") shows that removing action noise from expert data collapses performance from 99% to 6% on the simplest cube task. This finding—that coverage matters more than optimality for offline GCRL—is not extractable from fixed, human-collected datasets used in prior benchmarks.

5. **Substantially longer horizon tasks than prior work.** Table 1 quantifies that OGBench tasks require up to ~3000 steps (HumanoidMaze giant) and up to 24 atomic behaviors (Puzzle 4x6), compared to D4RL's ~400 steps and 4 subtasks. This is a concrete advance over existing benchmarks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Evaluation resolution with 5 test-time goals is coarse, especially for stochastic environments.** Each task is evaluated on only five fixed state-goal pairs. While averaging over 8 seeds (4 for pixels) mitigates variance, the small number of binary evaluation episodes per seed limits resolution. In stochastic environments (teleport mazes, powderworld), a method that succeeds on 2/5 goals in one run and 3/5 in another could change apparent rankings due to the coarse grid. The reported standard deviations are often small, which somewhat addresses this, but a bootstrap analysis of ranking stability or an increase to 15-20 goals would strengthen reliability.

2. **The noise-ablation finding is overgeneralized from thin evidence, and the paper does not specify which method produced the results.** The ablation showing that removing action noise collapses performance (Figure noise_abl) is conducted on two tasks (cube-single-noisy, puzzle-3x3-noisy). Critically, the paper never states which algorithm was used for this ablation (lines 966-978). The claim that "datasets *must* be noisy enough" and the extrapolation to real-world data collection go beyond what an unreported single-method, two-task experiment can support. A behavioral cloning method like GCBC might prefer low-noise data. The claim should be qualified, with the method specified, and ideally supported by ablating multiple methods.

3. **Limited validation of reference implementations against prior work.** Table vs_prior_work compares implementations on only two D4RL AntMaze datasets. While this demonstrates reasonable tuning, extending validation to at least one additional environment type (e.g., Fetch or Roboverse tasks) would substantiate the claim that implementations generalize beyond a single environment.

4. **No systematic analysis of failure modes.** The Q&A section discusses *which* methods succeed at which tasks but does not analyze *why* they fail on specific tasks. For instance, why does QRL collapse on `pointmaze-teleport` (4%) while GCIVL gets 45%? The paper speculates about optimistic bias but does not examine whether the quasimetric structure itself is responsible. A few deep-dive failure analyses would increase the benchmark's diagnostic value.

### Trivial
- The paper could quantify the *drop* from `large` to `teleport` per method (a delta table) to make the stochasticity analysis more precise, rather than comparing absolute numbers across different maze types.

## Nice-to-Haves
- Increase the number of test-time goals from 5 to at least 15-20 per task to improve statistical power in stochastic environments.
- Report wall-clock time or GPU-hours per method to help researchers prioritize baselines under compute constraints.
- Provide easier pixel-based variants of visual-humanoidmaze so that at least one method achieves >10%, increasing diagnostic signal for that quadrant of the benchmark.

## Removed Points
These points were raised by reviewers but did not survive filtering:
- **"Pixel-based tasks have limited diagnostic value / violate design principle 2"** — The design principle (line 329-331) requires "at least one task per type" to achieve 20-30% success. State-based HumanoidMaze satisfies this (HIQL at 89%). The paper explicitly acknowledges (line 327-328) that harder variants exist for future-proofing. The transparency about floor results is appropriate, not a flaw.
- **"Non-Markovian datasets not evaluated in main table"** — The paper references an appendix section (sec:additional_datasets) for noisy dataset results. Per review policy, missing appendix content is not a valid critique.
- **"Section 2 should mention how many prior papers used each approach"** — A minor presentation suggestion without substantive weight.
- **"The framing equating offline GCRL with unsupervised pre-training is overextended"** — A subjective framing opinion. The paper is self-aware about this and discusses limitations in the Research Opportunities section.
- **"Missing analysis of training compute costs"** — A nice-to-have, not a weakness.
- **Strength: "Minimal dependencies (MuJoCo-only)"** — While technically true, this is a supporting detail rather than a central contribution.

## Novel Insights

The harsh critic and strength finder converge on the key insight: the paper's most important contribution is not any single algorithm result but the *infrastructure* that enables capability-disentangled evaluation. The single-goal vs. multi-goal ranking reversal table is a particularly clean piece of evidence that validates the benchmark design—it shows concretely that the field's standard evaluation protocol has been producing misleading rankings. The strength finder correctly identifies that the main results table (lines 661-748) is the paper's core evidence: it shows cross-cutting patterns (e.g., HIQL dominates all humanoidmaze tasks but not pointmaze; GCIQL dominates all puzzle tasks but not locomotion) that no prior benchmark can produce. An additional observation not captured by either reviewer: PointMaze being "surprisingly hard" (the paper's own Research Opportunities question) is itself a finding worth future investigation—QRL uniquely succeeds here while collapsing on teleport, which contrasts sharply with AntMaze where QRL is mediocre on navigate and CRL/HIQL dominate.

## Suggestions
- Run the noise ablation on at least one additional method (e.g., CRL or GCBC) to show whether the "noise is critical" result is method-specific or general. At minimum, specify which method was used.
- Add a delta table showing per-method performance drop from `large` to `teleport` for the stochasticity analysis.
- Provide an explicit "recommended evaluation protocol" specifying a minimum number of test-time goals for reliable ranking.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>