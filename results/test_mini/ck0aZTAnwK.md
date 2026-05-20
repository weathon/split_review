Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper studies how to pre-train language models when data is fixed but compute is abundant. It shows that standard data-constrained recipes (epoching + parameter scaling) overfit, and proposes fixing this via heavy regularization — finding that optimal weight decay is ~30× larger than standard practice (0.8–3.2 vs. 0.1). It then proposes evaluating recipes by the **asymptote** of their scaling law (limit as parameter count N→∞ or ensemble size K→∞), and shows that ensembling independently trained models achieves a lower loss asymptote than scaling a single model's parameters. The paper composes both strategies (joint scaling of N and K) and reports a 5.17× data efficiency improvement over the baseline at 200M tokens. Distillation preserves 83% of the ensemble gain in an 8× smaller model, and validation loss improvements transfer to a 9% average improvement on three downstream benchmarks.

---

## Strengths

1. **Concrete practical finding about weight decay for data-constrained pre-training (Section 3).** The paper shows that optimal weight decay ranges from 0.8 to 3.2 (vs. the standard 0.1 from Brown et al., 2020) for models 140× larger than Chinchilla at a fixed data budget. This is a specific, reproducible, and actionable result that directly enables monotonic power-law scaling where prior approaches (Muennighoff et al., 2023) exhibited overfitting. The coordinate descent tuning procedure described in Appendix C.1 is appropriate for this search.

2. **Asymptote evaluation as a framework for comparing recipes under infinite compute (Sections 1, 3).** Instead of comparing recipes at a fixed compute budget (Hoffmann et al., 2022; Snell et al., 2024), the paper proposes evaluating the limit of the scaling law as N→∞ or K→∞. This is a conceptually clean and well-motivated metric that matches the problem setting and departs from prior scaling-law work.

3. **Empirical demonstration that ensembling achieves a lower loss asymptote than parameter scaling, and that composing both yields further gains (Section 4).** At 200M tokens, the regularized recipe asymptote is 3.43, the ensembling asymptote (300M members, K→∞) is 3.34, and the joint scaling asymptote (N,K→∞) is 3.17. Even K=3 ensembles (300M members) outperform the regularized single-model asymptote. The paper also provides a non-extrapolated data efficiency figure: the best five-member 1.4B ensemble achieves 3.75× data efficiency without any asymptotic extrapolation (line 189).

4. **Distillation preserves ensemble gains in smaller models (Section 6).** Distilling an 8-ensemble (300M members) into a 300M student retains 83% of the loss improvement over the regularized 300M model, and the student outperforms the regularized recipe asymptote. This addresses the practical concern that ensembles require large parameter counts at inference.

5. **Validation loss improvements transfer to held-out downstream benchmarks (Section 7).** The paper evaluates on PIQA, SciQ, and ARC Easy after all recipe selection was done, achieving a 9% average improvement. This provides evidence that the validation-loss-driven improvements are not an artifact of overfitting to the validation set.

---

## Weaknesses

### Fatal
None.

### Major

1. **The headline quantitative claims (5.17× data efficiency, specific asymptote values) rely on extrapolation from very few data points without uncertainty quantification.** The parameter scaling law is fit to 4 points (150M, 300M, 600M, 1.4B), the ensemble scaling law to 5 ensemble sizes (K=1–5) at a single member size, and the joint scaling involves nested extrapolation where the inner K→∞ asymptotes themselves are fit from 4–5 points each. The paper acknowledges a sensitivity analysis in Appendix I.1 showing asymptotes vary by at most ±0.02 loss across 3 seeds, but (a) this covers only one specific setting, not the nested joint scaling or the data scaling laws, and (b) ±0.02 in asymptote translates to a much larger range in data efficiency ratios. The 5.17× figure and the precise ordering of asymptotes (3.43 vs. 3.34 vs. 3.17) are presented as crisp numbers but carry substantial, unquantified uncertainty. The paper would be significantly stronger if it reported bootstrap confidence intervals or Bayesian credible intervals on all fitted parameters and derived quantities.

2. **The joint scaling recipe's nested extrapolation rests on a heuristic hyperparameter rule that is not validated.** For the inner limit (K→∞ at fixed N), the paper uses a heuristic of 2× epochs and 0.5× weight decay relative to the optimal regularized hyperparameters, stating that "we cannot fully find locally optimal hyperparameters due to experimental constraints" (lines 147–148). While the paper is transparent about this, the final 5.17× figure depends on this untested assumption. Some analysis (even at one N, showing how the fitted asymptote changes as hyperparameters vary around the heuristic) would help assess sensitivity.

3. **No error bars or run-to-run variance are reported on any point-wise loss or downstream accuracy results.** The paper shows no confidence intervals on the empirical loss values used for fitting, on the downstream benchmark accuracies, or on the derived data efficiency ratios. This is the single biggest empirical weakness. The only exception is the brief mention of a sensitivity analysis in the (stripped) appendix. For a paper making precise quantitative claims about asymptotes and data efficiency multipliers, the absence of uncertainty quantification is a significant gap.

### Minor

1. **Only three downstream benchmarks (PIQA, SciQ, ARC Easy) are used, all of which are small-scale multiple-choice tasks.** At the model scales studied (up to 1.4B parameters), a broader evaluation including tasks like HellaSwag, WinoGrande, or MMLU subsets would strengthen the claim that validation loss improvements generalize to capabilities of interest. The paper's argument that it "did not evaluate on any benchmarks until the end" is a good-faith practice, but the narrow benchmark selection limits the strength of the generalization claim.

2. **The ensemble scaling analysis uses K=1–5 at a single member size (300M) for the main comparison (Figure 4).** While the joint scaling (Section 4.3) and data scaling (Section 5) provide additional evidence across multiple N, the core claim that "ensembling beats parameter scaling at asymptote" rests primarily on one ensemble size sweep. The distillation result (Section 6) partially mitigates this by showing the ensemble benefit persists in a distilled student at a different size.

3. **The claim that the standard recipe's overfitting "contradicts the functional form of the decay-based scaling law in Muennighoff et al. (2023)"** (line 62) is somewhat overstated — Muennighoff et al. acknowledge this overfitting and remove overfit runs. The paper's contribution is fixing it, not discovering it.

### Trivial
None.

---

## Nice-to-Haves

- Reporting confidence intervals on all fitted asymptotes (via bootstrapping or Bayesian methods) would substantially strengthen the paper's quantitative claims. Even if the 5.17× figure has a 95% interval spanning 3×–10×, the qualitative story (ensembling helps) would remain intact while the quantitative overprecision would be corrected.
- Validating the scaling trends at one moderately larger scale (e.g., 3B tokens on a 2.7B model) would provide an out-of-sample check on the extrapolations. Currently, all experiments are between 200M and 1.6B tokens.
- An ablation separating the contribution of regularization tuning from the effect of increased parameter count (e.g., fixing weight decay at 0.1 while scaling N with the regularized recipe's epoch choices) would clarify how much of the gain comes from regularization vs. parameter scaling.

---

## Removed Points

These points were flagged during review but are removed because they are factually incorrect, outside scope, or misread the paper:

- **"Baseline comparison is uncompetitive (no comparison to synthetic data, diffusion LMs, etc.)"** — The paper scopes itself to studying epoching + regularization + ensembling recipes under infinite compute. It does not claim to be the best possible data-constrained method. The paper's baseline tunes epoch count and learning rate at each parameter count (Figure 2 table), making it a reasonable standard-practice baseline. Demanding comparisons to diffusion LMs, energy-based models, or synthetic data methods is outside the paper's stated scope and would be a separate paper.

- **"Limit order (N then K vs. K then N) is not validated"** — The paper explicitly addresses this: "As long as min_H ... monotonically decreases in N and K when fixing the other variable, the value does not depend on the order of the limits" (lines 147–148). Monotonicity, which the paper verifies, guarantees the double limit is well-defined.

- **"Hyperparameter search methodology insufficiently documented"** — The paper states full details are in Appendix C.1. The appendix is stripped by the PDF parser, not missing from the submission.

- **"No training compute costs reported"** — The setting is explicitly "infinite compute." Reporting compute costs is irrelevant to the paper's thesis, which is about the best achievable loss when compute is not a constraint.

- **"Section 2 finding is well-known in prior work"** — The paper is not claiming novelty for the observation that overfitting occurs; the novelty is in fixing it via heavy regularization and then building scaling laws on top of the fix.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add uncertainty quantification.** Report confidence intervals (via bootstrapping or Bayesian fitting) on all fitted asymptotes, exponents, and data efficiency ratios. This is the single improvement that would most strengthen the paper. Even wide intervals preserve the qualitative message while removing the appearance of overprecision.

2. **Validate the scaling trends at one larger scale.** A single experiment at, say, 3B tokens on a 2.7B model would provide an out-of-sample test of the extrapolations — far more convincing than additional sensitivity analysis.

3. **Expand downstream evaluation.** Adding 2–3 more benchmarks (e.g., HellaSwag or WinoGrande) at the largest model sizes would substantially strengthen the generalization claim.

4. **Tone down the precision of the quantitative claims.** Replace phrasings like "5.17× data efficiency" with "approximately 5× data efficiency (with substantial uncertainty)" and present confidence ranges rather than point estimates.

---

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Weak anchors (<3.5): `zCpVdWaIEp` (avg 1.00), `guUUlHPXRw` (avg 2.00), `3iXyRG2nzT` (avg 3.00), `jYrdhGvjVY` (avg 3.33) — None of these are topically close. They are weaker papers in different domains.
- Middle anchors (3.5–7.5): `x54wwB6QvL` (avg 6.00, scale-law data quality), `2FZC0c06jP` (avg 6.50, proxy model reliability), `0BkvUY61MX` (avg 5.33, multilingual scaling laws), `Ym33xJYINV` (avg 6.00, scaling laws for generative evals) — These are the relevant comparison band.
- Strong anchors (>7.5): `oBXfPyi47m` (avg 8.00, RL), `VKGTGGcwl6` (avg 8.00, multi-turn conversation), `qOyF214xmg` (avg 8.00, transduction) — These are different problem domains and clearly stronger papers overall.

**Initial bracket:** 4.0 – 6.0.

**Round 2 — Narrowing:**
- Lower band (3.5–5.5): `nrVbL1CK1A` (avg 4.00, bootstrapped pretraining — rejected, limited scale), `NbdCwOgk4m` (avg 4.00, hyperparameter tuning), `pJcHaD3mvn` (avg 4.00, extrapolating scaling laws — rejected, overclaims), `v3mJ4f4Mnc` (avg 4.40, reasoning scaling laws — rejected).
- Upper band (5.5–7.0): `2FZC0c06jP` (avg 6.50, accepted poster), `Ym33xJYINV` (avg 6.00, accepted poster), `x54wwB6QvL` (avg 6.00, accepted poster), `dSdLqg02tx` (avg 6.00, learning rate scaling laws, accepted poster).

**Comparison to anchors:**
- vs. `nrVbL1CK1A` (4.00, reject): Both study scaling at modest scale. The current paper has a more novel problem framing, a concrete practical finding (weight decay), and distillation results. However, `nrVbL1CK1A` had more extensive experiments (multiple model sizes, multiple domains). The current paper is clearly stronger.
- vs. `pJcHaD3mvn` (4.00, reject): Both involve extrapolation from small models. The current paper has clearer contributions and better presentation. The current paper is stronger.
- vs. `x54wwB6QvL` (6.00, accept): Both propose new scaling frameworks at small scale. The data quality paper had more thorough synthetic experiments (7 quality levels, 2 tasks) but was criticized for unrealistic noise. The current paper has a more real-world experimental setup but fewer data points for its fits and less comprehensive evaluation. Comparable overall, with the current paper slightly weaker on empirical thoroughness.
- vs. `Ym33xJYINV` (6.00, accept): That paper had experiments up to much larger scales with clearer validation. The current paper's experiments are at smaller scale with more speculative extrapolation. The current paper is weaker.

### Final Score

The paper has genuine contributions (weight decay finding, asymptote framework, ensemble comparison, distillation results) but is held back by the gap between its precise quantitative claims and the limited evidence supporting them. The core story — regularization and ensembling improve data-constrained pre-training — is well-supported, but the specific 5.17× figure and the precise asymptote ordering carry unquantified uncertainty that should be explicitly acknowledged. Relative to accepted scaling-law papers in the 6.0 range, this paper's experiments are less extensive and its claims more extrapolative; relative to rejected papers at 4.0, it has clearer novelty and practical findings. I place it at **5.0**.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>