Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces BIRD-INTERACT, a benchmark for evaluating LLMs on multi-turn interactive text-to-SQL tasks. The benchmark's key contributions are: (1) a function-driven user simulator that mitigates ground-truth leakage through a two-stage semantic parsing pipeline (AMB/LOC/UNA actions), (2) two evaluation settings (c-Interact for protocol-guided conversation and a-Interact for agentic exploration), and (3) 900 tasks spanning full CRUD operations with state-dependent sub-tasks. The paper evaluates 7 frontier models and finds very low success rates (GPT-5 achieves 8.67% on c-Interact, 17% on a-Interact), demonstrating the benchmark's difficulty.

## Strengths

- **Function-driven user simulator with rigorous validation.** The two-stage AMB/LOC/UNA approach is validated through both an objective guard dataset (USERSIM-GUARD, Fig. 6) where failure on "unanswerable" questions drops from 67.4% to 2.7%, and a human alignment study (Table 3) showing Pearson r=0.84 (p=0.02) for the proposed simulator vs. r=0.61 (p=0.14, not significant) for the LLM-only baseline. This is the paper's strongest methodological contribution.

- **Expansion to full CRUD operations.** Unlike prior multi-turn benchmarks (CoSQL, SParC) that only cover SELECT queries, BIRD-INTERACT includes DML/DDL tasks — 105 DM tasks in LITE and 190 in FULL — addressing a clear gap in the evaluation landscape.

- **Memory grafting diagnostic experiment (Section 5.2).** The experiment cleanly separates communication skill from SQL generation ability: GPT-5 achieves 14.50% SR on c-Interact but improves to 18.8% (with Qwen-3-Coder's history) and 20.5% (with O3-mini's history) — a relative improvement of 36–49%. This provides replicable evidence that strategic interaction is a distinct capability from SQL writing.

- **Rigorous benchmark construction.** High inter-annotator agreement (93.33%/93.50%), systematic ambiguity injection with three categories (superficial, knowledge, environmental), a principled 5-category taxonomy for follow-up sub-tasks, and executable test cases for functional verification. The budget-constrained evaluation framework ties budgets to annotated ambiguity counts rather than arbitrary caps.

## Weaknesses

### Major

1. **Single-run evaluation with no variance reporting.** The paper explicitly states (Section 5, line 163): "All models use temperature=0...conducting single runs due to cost." For a benchmark intended as a community reference point, this is the most significant limitation. Without confidence intervals or multiple runs, fine-grained comparisons in Table 2 (e.g., GPT-5 at 14.50% vs. Claude-Sonnet-4 at 22.33% on c-Interact priority tasks) cannot be distinguished from run-to-run variation. This concern is amplified in an interactive setting where non-deterministic reasoning traces (o3-mini) and API backend variability can produce variance even at temperature=0. A benchmark that others will use to compare methods should establish the stability of its results.

2. **The "ITS Law" is not supported by the evidence.** The paper defines (line 207): "A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task." Figure 4 shows only Claude-3.7-Sonnet with a modest upward trend (roughly 15% → 25%) that plateaus well below the idealized dotted line; GPT-4o and Qwen-3 show flatter curves; and in a-Interact mode, performance is essentially flat or declining across all four models. Labeling this a "law" substantially overclaims what the data supports. This distracts from an otherwise interesting empirical observation about interaction scaling.

### Minor

3. **Cross-setting comparisons use causal language without controlling for confounds.** The paper states (line 187) "Interaction Mode Emerged as the Decisive Factor for a Successful Outcome" and claims "GPT-5 performs poorly in the constrained, predefined flow...but excels in the *a*-Interact setting." However, c-Interact and a-Interact differ on multiple dimensions simultaneously (action space, budget structure, debugging mechanism, simulator engagement protocol). The observations are valid and interesting as descriptive findings, but the framing implies a level of causal identification the experimental design does not support.

4. **No limitations section.** The paper discusses future work (Section 8) but never acknowledges the benchmark's own boundaries — whether the artificial ambiguity injection methodology may create a "guess the annotation" dynamic, whether the LIVESQLBENCH task sample introduces biases, or what aspects of real interaction the function-driven simulator does not capture. A benchmark that will be used as a community reference should explicitly scope what it does and does not measure.

5. **Memory grafting experiment dataset ambiguity.** The "without memory grafting" baseline for GPT-5 in Figure 5 is 13.8%, while Table 2 reports GPT-5's c-Interact priority SR as 14.50% on the FULL set. The paper does not specify whether the memory grafting experiment was run on LITE or FULL, making the baseline discrepancy difficult to reconcile. This should be clarified.

### Trivial

6. The abstract states 600 tasks "unfold up to 11,796 dynamic interactions" while Table 1 reports 13.64 interactions per task on average. Since 600 × 13.64 = 8,184, the relationship between "up to" and the average should be explained.

## Nice-to-Haves

- Run each experiment with at least 3 seeds (or bootstrap confidence intervals) to establish variance estimates. Even 2-3 runs would give the community a sense of result stability.
- Compare models on BIRD-INTERACT vs. static-transcript versions of the same tasks to directly demonstrate that the dynamic setting changes model behavior and rankings.
- Provide a direct comparison showing how the function-driven simulator changes model rankings vs. an LLM-only simulator baseline on the full benchmark.

## Removed Points

- *Memory grafting conflates information quality with communication skill (Harsh Critic)* — Removed. The paper's interpretation is valid: GPT-5 generates good SQL when given good interaction histories, which is precisely evidence that communication (extracting information) is the bottleneck. The experiment isolates SQL generation from interaction skill; the critic's proposed counterfactual (giving GPT-5 the same information through its own history) would be a different experiment testing a different question.

- *Ambiguity injection creates an artificial interaction game (Harsh Critic)* — Removed. This is inherent to any benchmark construction and not a specific flaw of this paper. All benchmarks impose structure to make evaluation tractable; the paper's methodology is transparent about how this is done.

- *GPT-5 numbers in Figure 5 vs Table 2 discrepancy (Harsh Critic)* — Retained as Minor#5 but with corrected analysis: the discrepancy likely reflects LITE vs FULL sets, not an error. The paper should clarify.

- *Missing related works (Harsh Critic)* — Removed per policy (cannot confirm from external sources).

- *Formatting and appendix-related criticisms* — Removed per policy (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Prioritize multi-seed runs for the main results (Table 2).** Even 3 runs with reported mean ± std would substantially increase the benchmark's credibility as a community reference point. This is the single most impactful improvement.

2. **Replace the "ITS Law" with measured language.** The observation that some models improve with more interaction turns is interesting and worth reporting. Drop the "law" framing entirely.

3. **Add a limitations section** that discusses: (a) what the ambiguity injection methodology measures vs. what it doesn't, (b) potential biases from the LIVESQLBENCH task sample, (c) boundaries of the function-driven simulator relative to real human interaction, and (d) the single-run limitation.

4. **Clarify the memory grafting experiment** by stating which dataset (LITE vs. FULL) it was conducted on and reconciling the baseline numbers.

5. **Qualify cross-setting comparisons** as descriptive observations rather than causal conclusions about interaction mode.

## Score and Decision

**Bracketing (Round 1):** I compared the paper against three bands: weak anchors (avg < 3.5 on text-to-SQL benchmarks — irrelevant, those papers are rejected with different flaws), mid-range anchors (3.5–7.5 on interactive benchmarks — MINT at 6.75, MTU-Bench at 5.75, DynaEval at 4.25), and strong anchors (>7.5 on multi-turn benchmarks — Spider 2.0 at 8.0, LiveBench at 7.33). The paper clearly falls in the mid-range: it has solid, well-validated contributions but is weaker than top-tier benchmark papers.

**Narrowing (Round 2):** I narrowed to the 5.5–7.0 range and compared against MINT (6.75), MTU-Bench (5.75). Relative to MINT, BIRD-INTERACT has stronger simulator validation but suffers from a more significant methodological weakness (single-run evaluation) and a clearly overclaimed "ITS Law." Relative to MTU-Bench (5.75), BIRD-INTERACT has a more clearly motivated gap (static transcripts + SELECT-only) and stronger construction validation (inter-annotator agreement, human alignment study). The paper sits between these anchors — closer to MTU-Bench than to MINT in overall rigor, but with contributions that are more impactful than MTU-Bench's.

**Calibration anchors used:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jp3gWrMuIZ.md` (MINT, avg 6.75) — Round 1 & 2. BIRD-INTERACT is weaker on experimental rigor and claim calibration.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/XmProj9cPs.md` (Spider 2.0, avg 8.00) — Round 1. BIRD-INTERACT is substantially weaker than this top-tier benchmark.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sKYHBTAxVa.md` (LiveBench, avg 7.33) — Round 1. BIRD-INTERACT is weaker on experimental design and scope.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/6guG2OlXsr.md` (MTU-Bench, avg 5.75) — Round 2. BIRD-INTERACT is slightly stronger on contribution clarity and validation.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/f7PmO5boQ9.md` (DynaEval, avg 4.25) — Round 1. BIRD-INTERACT is substantially stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CvGqMD5OtX.md` (CHASE-SQL, avg 6.25) — Round 2. Method paper; BIRD-INTERACT is comparable in overall quality.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MKEHCx25xp.md` (WildBench, avg 7.33) — Round 2. BIRD-INTERACT is weaker in experimental depth.

**Final score:** 6.0. The core contributions are real and the benchmark fills a genuine gap. The function-driven simulator is well-validated, the memory grafting experiment is clever, and the CRUD expansion addresses a clear limitation of prior work. However, the single-run evaluation is a significant concern for a community benchmark, and the overclaimed "ITS Law" undermines credibility. With these issues addressed, the paper would be substantially stronger.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>