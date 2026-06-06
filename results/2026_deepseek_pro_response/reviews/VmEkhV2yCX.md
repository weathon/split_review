Now I have all the anchor comparisons I need. Let me write the final review.

---

## Summary

This paper conducts the first systematic study of how reasoning data — varying in scale, diversity, and quality — should be allocated across the LLM training pipeline (pretraining vs. SFT). Through a fully-crossed experimental design training 8B models from scratch for 1T tokens (4 pretraining conditions × 3 SFT conditions = 12 models, plus RL on a subset), the authors discover an asymmetric principle: diversity and scale of reasoning data matter most during pretraining, while data quality dominates during SFT. They further show that front-loading reasoning into pretraining creates a durable advantage SFT cannot replicate, that high-quality pretraining data can have latent effects revealed only after alignment, and that blindly scaling SFT data volume can actively harm reasoning.

## Strengths

- **Fully-crossed experimental design with clean hypothesis tests**: The paper trains 12 models (4 pretraining × 3 SFT conditions) from scratch, enabling causal attribution. The "catch-up" hypothesis test (Table 4) is particularly clean: doubling SFT epochs for the baseline (M_base + SFT_SHQ at 2× epochs, score 34.01) still fails to match the weakest reasoning-pretrained model (M_SHQ + SFT_SHQ at 37.33), directly demonstrating that SFT cannot substitute for a reasoning-rich pretraining foundation.

- **The asymmetric principle is demonstrated with separable within-phase evidence**: Table 1 isolates the diversity advantage during pretraining (M_LDQ at 64.09 vs M_SHQ at 54.98), while Table 5 isolates the quality advantage during SFT (M_res + SFT_SHQ at 44.99 vs M_res + SFT_LDQ at 31.54). The reversal — diversity dominates early, quality dominates late — emerges from the data rather than being assumed, and provides an actionable heuristic for data allocation.

- **Harmful SFT scaling is demonstrated convincingly**: Table 8 shows that doubling mixed-quality SFT data yields no average improvement (32.84 → 32.99) while specifically harming math by −4.92 points. Meanwhile, adding a small fraction (0.4%) of high-quality samples produces consistent gains. This provides clear evidence that SFT scaling without quality control is counterproductive.

- **The latent effects finding is a genuinely novel empirical observation**: M_LMQ and M_LDQ are nearly tied at pretraining (64.07 vs 64.09 in Table 1), yet after identical SFT with D_SHQ, M_LMQ opens a +4.25 point lead (50.95 vs 46.70 in Table 4). Demonstrating that pretraining data choices can have effects invisible at the pretraining checkpoint but revealed after alignment is an interesting finding.

- **Reasoning ratio sensitivity analysis demonstrates robustness**: Tables 6–7 vary the pretraining reasoning ratio from 10% to 40%, showing monotonic improvement and confirming that the main results at 20% are not artifacts of a specific hyperparameter choice.

- **Broad cross-domain evaluation**: The evaluation spans math (GSM8K, MATH-500, AIME24/25), science (MMLU, MMLU-Pro, GPQA-Diamond), code (HumanEval, MBPP, LiveCodeBench), and instruction-following (IFEval), strengthening the generality of findings.

## Weaknesses

### Fatal

None.

### Major

- **The central "diversity > quality in pretraining" comparison conflates dataset size/repetition with data properties.** The paper compares M_LDQ (pretrained on D_LDQ: 268M diverse, mixed-quality samples) against M_SHQ (pretrained on D_SHQ: 1.2M high-quality samples), both with an 80B reasoning-token budget. This means D_SHQ must be repeated ~60–70× (depending on average sample length) while D_LDQ is seen roughly once. The paper acknowledges repetition (line 93: "When a reasoning dataset is small, it is repeated so that the model still observes the same total volume of reasoning tokens") but never discusses how extreme repetition of a small dataset during pretraining may cause memorization and degradation that confounds the diversity-vs-quality interpretation. M_SHQ's underperformance may reflect overfitting from repetition rather than an intrinsic disadvantage of high-quality data during pretraining. The SFT-stage results (Table 5), where the repetition factor is lower (~4× for D_SHQ), partially mitigate this concern, but the pretraining claim — one of the paper's most prominent findings — rests on a comparison where dataset size and repetition are entangled with the quality/diversity axis.

- **The RL evaluation is too narrow to support the headline claim.** Only 2 of the 12 SFT models are evaluated through RL: M_LMQ + SFT_SHQ and M_base + SFT_SHQ (Table 3). The +18.74% gap is attributed broadly to "front-loading reasoning data into pretraining," but M_LMQ is the union of D_LDQ and D_SHQ — it is the maximal-data condition. Without evaluating M_LDQ + SFT_SHQ + RL and M_SHQ + SFT_SHQ + RL, the paper cannot distinguish whether the RL advantage is driven by reasoning pretraining per se or by the specific composition and scale of M_LMQ's data. This matters because the "19% gain" (rounded from 18.74%) is the paper's most prominently featured number (abstract, introduction, conclusion).

### Minor

- **No variance estimates are reported despite multiple evaluation runs.** The evaluation protocol describes 16 runs for AIME and 4 runs for other benchmarks (line 148), but no standard deviations, confidence intervals, or statistical tests appear in any table. Several claimed effects involve differences of 4–5% (e.g., the +4.25% latent effect, the −4.92% math drop from doubling SFT data), where variance estimates would help assess robustness. Reporting the already-computed standard deviations would cost nothing.

- **The "latent effect" interpretation has plausible alternatives.** The paper attributes the +4.25% post-SFT gain of M_LMQ over M_LDQ to a "latent" mechanism where SFT unlocks pretraining benefits (line 215–216). An alternative explanation is that the 1.2M additional high-quality samples in M_LMQ directly improve the model, but the base-model evaluation benchmarks lack sensitivity to detect this improvement — no "unlocking" required. The paper would benefit from acknowledging this alternative.

### Trivial

- Some numeric claims in the abstract are loosely characterized relative to specific tables. The "15% average gain with high quality data" is not cleanly pinned to a single comparison (it approximately matches M_res + SFT_SHQ vs M_base + SFT_SHQ at +15.07%, but this is the joint effect of pretraining and SFT, not SFT data quality alone as the phrasing suggests).

- The optimization framing (Eqs. 1–2) is acknowledged conceptually but the paper runs a grid of experiments rather than solving an optimization problem. This is stylistic rather than substantive.

## Nice-to-Haves

- A control experiment repeating a subset of D_LDQ to the same degree as D_SHQ would isolate the repetition confound from the diversity/quality axis, substantially strengthening the central claim.
- Expanding the RL evaluation to include M_LDQ + SFT_SHQ + RL and M_SHQ + SFT_SHQ + RL would allow cleaner attribution of the RL gain.
- A limitations section acknowledging the single-model-scale (8B), the repetition confound, and the narrow RL evaluation would improve transparency.
- Per-dataset token counts (rather than just sample counts) would let readers compute exact repetition factors.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The improvement on science is minimal in prior work but large here (line 183) relies on comparing M_res+SFT vs M_base+SFT on SCIENCE_SFT AVG, but SCIENCE_SFT AVG includes GPQA-Diamond which was not evaluated at the base-model stage."** REMOVED — The comparison is between two models both evaluated at the SFT stage on the same benchmark set (which includes GPQA), so both are evaluated identically. There is no confound.

- **Harsh Critic: "The optimization framing (Eqs. 1–2) is largely decorative."** REMOVED as a standalone major criticism — this is a stylistic preference, not a methodological flaw. Moved to Trivial.

- **Harsh Critic: "The paper claims it 'refutes the overfitting hypothesis' (line 36) which is an overstatement."** REMOVED as a substantive criticism — the paper provides reasonable evidence against overfitting (GPR_PT AVG is essentially flat across models in Table 1). The word "refutes" may be strong but this is a wording nitpick that does not affect the paper's contribution.

- **Harsh Critic: "The description of D_ALF* ... is somewhat opaque."** REMOVED — D_ALF* is described as D_ALF augmented with D_SHQ, and the Table 8 comparison is sufficiently clear for the ablation's purpose.

- **Strength Finder: "This paper addressed an important problem."** REMOVED — generic and applies to most papers. Not a concrete, verifiable strength.

- **Harsh Critic: missing related works, appendix content, formatting, typos** — All REMOVED per hard rules (missing related works cannot be verified; appendix is stripped by parser; formatting/typos are parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The asymmetric principle (diversity for pretraining, quality for SFT) is the paper's most distinctive takeaway and is supported by within-phase comparisons. The latent-effects finding is also novel, though the interpretation warrants caution as noted in Minor weakness 2.

## Suggestions

- The highest-impact revision would be to explicitly discuss the repetition confound and temper the "diversity > quality in pretraining" claim. Even without new experiments, acknowledging that the comparison conflates dataset size/repetition with quality would substantially improve intellectual honesty. Reporting per-dataset token counts would let readers assess the confound themselves.
- Report standard deviations across the already-computed evaluation runs. This costs nothing and addresses the most common methodological concern.
- For the RL section, either expand the evaluation to additional models or narrow the claim to "M_LMQ (the maximal-data condition) shows compounding RL gains" rather than the broader "front-loading reasoning data" framing.

## Score and Decision

**Round-1 bracket:** Between 5.0 and 7.5, based on comparisons with "Amuro and Char" (4.20, Reject) below and "At Which Training Stage Does Code Data Help LLMs Reasoning?" (7.25, Accept) above.

**Round-2 narrowing:** Compared against "Advancing Mathematical Reasoning" (5.71), "MIND" (6.00), and "What Kind of Pretraining Data" (6.75). The paper is clearly stronger than the 5.71 and 6.00 anchors in experimental rigor and contribution breadth, and comparable to but slightly below the 6.75 anchor given the two major weaknesses. The most similar paper — "At Which Training Stage Does Code Data Help LLMs Reasoning?" (7.25) — has a comparable research question structure; our paper exceeds it in model scale and experimental control, but the repetition confound and narrow RL evaluation pull it below the 7.25 level.

**Anchor summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Amuro and Char | 4.20 | R1 | Our paper substantially stronger in scale, design, and contribution |
| At Which Training Stage (Code) | 7.25 | R1 | Most similar; our paper has better control/scale but the repetition confound makes it slightly weaker |
| Advancing Math Reasoning | 5.71 | R2 | Our paper cleaner and more novel |
| MIND | 6.00 | R2 | Our paper more comprehensive |
| What Kind of Pretraining Data | 6.75 | R2 | Comparable quality; ours more empirical, theirs more mechanistic |

**Final score:** 6.5 — a clear accept. The paper makes a genuine contribution with a substantial experimental investment and novel, actionable findings. The two major weaknesses (repetition confound, narrow RL evaluation) are real but do not invalidate the core contributions; they are addressable limitations that affect the strength of specific claims rather than the paper's overall value.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>