I have thoroughly verified the paper content against each reviewer claim. Here is my consolidated review.

---

## Summary

This paper introduces Unified Uncertainty Calibration (U2C), a framework that replaces the standard reject-or-classify (RC) recipe for combining aleatoric and epistemic uncertainty. Instead of hard thresholding an epistemic uncertainty score, U2C learns a non-linear calibration function τ_u that fuses the epistemic score as an additional logit in a (c+1)-way softmax, enabling soft, calibrated communication between uncertainty types. The paper provides theoretical lemmas characterizing when U2C outperforms RC in terms of classification error and negative log-likelihood, and evaluates across four ImageNet benchmark families using four epistemic uncertainty estimators.

## Strengths

1. **Principled problem identification and clean solution.** The paper clearly identifies three concrete deficiencies of RC (no communication between uncertainty types, miscalibration from binary accept/reject, inability to correct misspecified uncertainty estimates), and each component of U2C directly remedies one of these deficiencies (Section 4). The idea of learning a non-linear calibration function to fuse an epistemic score as an additional logit is simple and well-motivated.

2. **Comprehensive evaluation across benchmark types and uncertainty estimators.** The experiments cover four ImageNet benchmark types (in-domain, covariate shift, near-OOD, far-OOD) with four diverse uncertainty estimators (MaxLogit, ASH, Mahalanobis, KNN). Table 1 reports both error and ECE, with consistent improvements from U2C over RC across the vast majority of settings. This systematic evaluation directly supports the paper's central claim that U2C outperforms RC.

3. **Theoretical analysis quantifying the regimes of improvement.** Lemma 5.1 expresses the difference in classification errors between RC and U2C as a function of probability mass in regions B and C of the (max-logit, τ(u)) plane, showing U2C excels when OOD mass falls in the high-aleatoric/low-epistemic region B. Lemma 5.2 proves that RC yields infinite NLL on certain regions where U2C does not, due to RC's overconfident binary predictions. These lemmas provide useful geometric intuition.

4. **Honest discussion of limitations.** Section 7 explicitly acknowledges the fundamental challenge of unknown-unknowns (feature myopia) and adversarial examples, citing Goodman (1972) and Hendrycks et al. (2021b). This avoids overclaiming and adds intellectual depth.

## Weaknesses

### Major

- **Unsubstantiated "state-of-the-art" claim.** The abstract claims U2C "yields state-of-the-art performance across a variety of standard ImageNet benchmarks," but the experiments compare only against RC — a single, deliberately simple baseline. While RC is the standard approach the paper targets, "state-of-the-art" implies superiority over a broader literature of abstention, selective classification, and OOD detection methods (e.g., learning-based abstention classifiers, post-hoc OOD detectors, confidence-calibrated classifiers). The paper's experiments convincingly show that U2C improves over RC, but the SOTA claim is unsupported and should be removed or softened to reflect the actual comparison.

### Minor

- **No analysis of sensitivity to the relabeling threshold α.** U2C relabels the top 5% (α=0.95) of validation examples as OOD. The paper provides no ablation or sensitivity analysis for this hyperparameter, and the choice is not justified beyond being "common practice" for RC thresholds. A higher α might corrupt calibration with genuine in-domain examples; a lower α might provide too few negative examples. Without analysis, the robustness of U2C to this choice is unknown.

- **Distribution mismatch between pseudo-OOD and true OOD is unexamined.** The calibration function τ_u is trained on relabeled in-domain examples (the 5% most uncertain by u), but must generalize to genuinely out-domain examples at test time. The paper provides no analysis of whether the distribution of u on relabeled in-domain examples resembles that on true OOD data, nor does it probe this transfer (e.g., by comparing score distributions, varying the relabeling threshold, or testing on OOD examples with varying degrees of similarity to in-domain). The concern is not fatal — many OOD methods implicitly rely on such monotonicity — but the lack of analysis is a gap.

- **Error bars are absent and the justification is weak.** The paper states "there is no randomness involved in our experimental protocol — the splits ImageNet-va and ImageNet-te were computed once and set in stone for all runs." Fixed splits remove one source of randomness, but classifier training involves initialization seeds, SGD stochasticity, and other sources of variance. If the classifier weights are themselves fixed (e.g., a pretrained model used as-is), that should be stated explicitly. Without error bars, it is impossible to assess whether reported improvements (often a few tenths of a percent) are meaningful or within noise.

- **Theory analyzes idealized U2C rather than the learned version.** Lemma 5.1 and Lemma 5.2 compare RC and U2C assuming τ_u is a fixed function characterizing the accept/reject regions (A, B, C, D). The actual U2C procedure learns τ_u on relabeled in-domain data; the theory does not address whether the learned τ_u actually places mass in regions B and C in the way that benefits U2C, nor does it provide guarantees about the learned function. The theoretical results are clean and intuitive, but they describe a hypothetical version of the method.

### Trivial

- The paper claims Section 6 "shows additional experiments on linear U2C ... as well as other neural network architectures, such as ResNet152 and ViT-32-B" (line 192), but these appear in a stripped appendix and cannot be verified in the current text. This is a presentation issue imposed by the PDF extraction, not an author error.

## Nice-to-Haves

- A comparison to a version of U2C with a *linear* τ_u (mentioned in passing but not presented) would strengthen the claim that non-linear calibration matters.
- Reliability diagrams or per-bin calibration plots would clarify the calibration improvement beyond aggregate ECE numbers.
- An analysis of what the learned τ_u looks like (is it approximately linear? does it saturate?) would add practical insight.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic point about insufficient baseline comparisons (Geifman & El-Yaniv 2017, selective classification, etc.)** — Removed in severity. The paper's central claim is that U2C outperforms the *standard* approach (RC), not that it outperforms every alternative in the literature. The experiments support this specific claim. The SOTA overclaim is kept as a Major weakness, but the broader "missing baselines" criticism is scope creep for a methods paper targeting a specific deficiency of one recipe.

- **"Theory doesn't engage with learning theory" criticism** — Weakened/Removed. The paper calls the analysis "clean," not a full learning-theoretic treatment. Two lemmas characterizing decision-rule differences are legitimate theoretical contributions for a methods paper.

- **"Philosophical framing takes space from technical depth"** — Removed. This is a subjective stylistic preference.

- **Points about missing appendix content** (linear U2C results, ResNet152/ViT-32-B experiments) — Removed per instructions: parser strips appendices; these exist in the original submission.

- **Strength Finder's generic strengths** (e.g., "Clear problem formulation and motivation") — Removed as generic; the specific strengths (theoretical quantification, comprehensive evaluation, quadrant-of-knowledge connection) are kept.

## Novel Insights

None beyond the paper's own contributions. The reviews surface genuine concerns (α sensitivity, distribution mismatch, error bars) but raise no novel theoretical or empirical insight that the paper itself does not already contain or directly imply.

## Suggestions

1. **Remove or soften the "state-of-the-art" claim** to "outperforms the standard reject-or-classify recipe" — this is accurate and supported by the data.
2. **Add an ablation on the relabeling threshold α** (e.g., 0.90, 0.95, 0.99) to demonstrate robustness.
3. **Report variability** over at least 3–5 runs with different random seeds, or explicitly state that the classifier weights are frozen/pretrained with fixed seeds and that the only operation is deterministic calibration.
4. **Add a brief analysis of the distribution mismatch**: compare the distribution of u on the relabeled 5% vs. on actual OOD test examples, or show that performance degrades gracefully as one varies the relabeling proportion.

## Score and Decision

**Score: 6.0 / 10** — The paper introduces a clean, well-motivated idea and provides solid empirical evidence that U2C outperforms RC across diverse benchmarks. The weaknesses are primarily around overclaiming (SOTA) and missing ablations/sensitivity analyses. The core contribution is real, and the issues are addressable in a revision. However, the SOTA overclaim and lack of error bars are nontrivial gaps that prevent acceptance at the "strong accept" level.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>