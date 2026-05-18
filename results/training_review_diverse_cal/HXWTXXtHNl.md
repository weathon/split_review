Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper proposes Transition-aware weighted Denoising Score Matching (TDSM), a method for training conditional diffusion models under label noise. The core theoretical contribution is Theorem 2, which proves that the noisy-label conditional score is a convex combination of clean-label conditional scores with instance- and time-dependent coefficients. The authors derive a practical estimator for these weights using a time-dependent noisy-label classifier and transition matrix, and prove (Theorem 3) that minimizing the TDSM objective recovers the clean-label conditional score under an invertible transition matrix. Experiments on MNIST, CIFAR-10/100, and Clothing-1M show substantial improvements on conditional generation metrics (CW-FID, CAS, etc.) across symmetric and asymmetric noise settings.

## Strengths

- **First theoretical characterization of noisy-label conditional scores for diffusion models.** Theorem 2 and Proposition 2 establish that the noisy-label conditional score is a convex combination of clean-label scores with instance- and time-dependent coefficients. This is a genuinely novel result that provides the theoretical foundation for the entire approach.

- **Clean-label score recovery guarantee (Theorem 3).** The paper proves that minimizing the TDSM objective under an invertible transition matrix recovers the clean-label conditional score. Theorem 4 further proves that the simpler S-weighted DSM (analogous to GAN-based approaches) cannot recover clean scores, demonstrating why the proposed instance- and time-dependent weighting is necessary rather than merely heuristic.

- **Strong conditional metric gains across diverse settings.** On CIFAR-10 with 40% symmetric noise, CW-FID drops from 30.45 (DSM) to 15.92 (TDSM), and CAS rises from 47.21% to 62.28%. On CIFAR-100 with 40% symmetric noise, CW-FID goes from 100.04 to 93.24 and CAS from 15.41% to 21.17%. These gains are consistent across all datasets, noise types, and noise rates. The ablation study (Table 4) confirms that the instance- and time-dependent weights are indeed necessary — S-DSM underperforms TDSM on most metrics.

- **Practical estimator and training procedure.** The weight estimator in Eq. (8) is derived in closed form, and Algorithm 1 provides a concrete training procedure with memory-saving techniques (detaching non-dominant outputs, skipping negligible weights) that make the method feasible for datasets with many classes. The orthogonal combination with existing label correctors (DISC, VolMinNet) demonstrates practical utility beyond synthetic noise settings.

## Weaknesses

### Major

- **The significant unconditional FID degradation on CIFAR-100 symmetric noise is not analyzed or adequately discussed.** On CIFAR-100 with 40% symmetric noise, unconditional FID jumps from 3.36 (DSM baseline) to 6.85 (TDSM) — roughly a doubling. The 20% symmetric case shows a similar pattern (2.96→4.26). These are not minor fluctuations, and they occur despite TDSM improving most other unconditional metrics (IS, Density). The paper's claim that "our models beat the baseline models in most cases" on unconditional metrics is technically true when aggregating all four metrics, but it obscures a systematic degradation in FID that deserves explanation. The conclusion goes further, claiming TDSM "outperform[s] baseline models in both conditional and unconditional performance" without the "most cases" qualifier. Since the method's main value is in conditional generation, this does not undermine the paper's core contribution, but the trade-off must be honestly characterized. The paper should provide a precision/recall or class-level breakdown to explain *why* FID degrades (e.g., whether it is driven by specific classes with poor weight estimates, or a global smoothing effect from the weighted-sum objective).

- **Sensitivity to the noisy-label classifier is not investigated.** The weight estimator \(\hat{w}\) in Eq. (8) critically depends on the time-dependent noisy-label classifier \(\tilde{\mathbf{h}}_{\boldsymbol{\phi}}\). This classifier is trained on the same noisy data and its accuracy will vary across timesteps — especially under high noise (e.g., 40% symmetric) or many classes (CIFAR-100). Errors in the classifier propagate through the weight estimator and could break the theoretical guarantee of Theorem 3. The paper includes an ablation using an estimated transition matrix (VolMinNet), but the classifier itself remains an unexamined component. A minimal robustness study — e.g., artificially degrading classifier accuracy and measuring the impact on conditional/unconditional metrics — is needed to establish practical reliability. Without this, readers cannot assess whether the method requires near-perfect classifier estimates or is robust to realistic levels of classifier error.

### Minor

- **The clean-benchmark experiment (Section 3.4) does not cleanly separate regularization from actual noise correction.** The paper applies TDSM to clean-labeled benchmarks using an *assumed* 5% symmetric noise transition matrix and attributes the resulting improvements to "potentially noisy or ambiguous labels" in those datasets. However, treating clean labels as if they came from a 5%-noise process and applying TDSM could yield improvements through beneficial regularization effects unrelated to any real label noise. The qualitative evidence in Figure 6 (showing 15 potentially mislabeled MNIST examples) is suggestive but not conclusive. The paper's claim that "existing benchmark datasets may suffer from noisy labels" is appropriately hedged, but the experimental design does not convincingly isolate the cause of the improvement.

- **The conclusion overclaims on unconditional performance.** Line 430 states TDSM "outperform[s] baseline models in both conditional and unconditional performance," dropping the "most cases" qualifier present in the results section (line 280). On CIFAR-100 symmetric noise, unconditional FID degrades substantially, and unconditional Coverage is also frequently worse. This is a presentation issue that should be corrected.

### Trivial

- None.

## Nice-to-Haves

- Add a brief "Limitations" subsection explicitly stating: (i) the method assumes class-conditional label noise, (ii) it requires a known or estimable transition matrix, (iii) classifier quality affects weight estimates, and (iv) unconditional FID can degrade under high symmetric noise.

- Report the noisy-label classifier accuracy as a function of timestep \(t\) for each noise setting, to give readers a sense of when the estimator is reliable.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"The derivation that W inherits invertibility from S... should be stated explicitly in main text"** — This is a presentation suggestion, not a weakness. The derivation is present and correct in the paper's proofs.

- **"Detaching non-dominant outputs introduces bias... ablation in appendix would ideally cover this"** — The paper already has an ablation study of the skip threshold τ (referenced in Sec. 3.5). The critic's concern is a valid theoretical observation but the paper does address it empirically. Also, this is framed more as speculation about what the appendix should contain, which may reflect a parser limitation.

- **"First study claim should be checked against robust score matching"** — This is a minor phrasing nitpick. The paper claims "first time in the diffusion model" which is plausible and not a substantive weakness.

- **"Injecting synthetic 5% noise on top of existing labels"** (from Weakness 3) — The paper does NOT inject noise on top of existing labels; it applies TDSM with an assumed 5% transition matrix to the original clean labels. The underlying concern (experimental design confound) is valid and retained in Minor weaknesses above, but the specific characterization was inaccurate.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's own framing: the theoretical contribution is genuinely novel, the conditional gains are convincing, but the unconditional behavior is undertreated.

## Suggestions

1. **Diagnose the unconditional FID degradation.** Compute precision and recall (or density/coverage per class) to show whether the FID increase is driven by specific classes with poor weight estimates, or reflects a global smoothing effect from the weighted-sum objective. If localized to high-noise classes, that is informative; if global, discuss the fundamental trade-off explicitly.

2. **Add a classifier sensitivity analysis.** Measure the accuracy of \(\tilde{\mathbf{h}}_{\boldsymbol{\phi}}\) as a function of timestep, then conduct a controlled experiment where classifier outputs are artificially corrupted (e.g., by adding noise or using a deliberately misspecified architecture) to measure the method's robustness.

3. **Correct the unconditional claim in the conclusion.** Replace "outperform baseline models in both conditional and unconditional performance" with language reflecting that conditional metrics improve universally while unconditional metrics improve in most (but not all) settings, with the trade-off discussed.

4. **Strengthen the clean-benchmark experiment.** Either (a) estimate a transition matrix from a held-out clean subset rather than assuming synthetic noise, or (b) explicitly frame the experiment as demonstrating robustness to a mild noise prior, not as evidence that clean benchmarks contain real label noise.

## Score and Decision

The paper makes a genuinely novel theoretical contribution (first characterization of noisy-label conditional scores for diffusion models) and backs it with a practical algorithm that achieves convincing improvements on conditional generation metrics across diverse noise settings. The two major weaknesses — the unexplained unconditional FID degradation and the lack of classifier sensitivity analysis — are real gaps but do not invalidate the core claims (which are about conditional generation). Both are addressable in a revision. I therefore recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>