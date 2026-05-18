Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper derives a parametric family of reverse SDEs (Theorem 1) for Lévy-Itô diffusion models (LIMs) that exactly preserve marginal densities, bridging a gap with conventional Gaussian diffusion models where both the reverse SDE and ODE are exact. The proposed SDE-E sampling algorithm, controlled by a noise parameter η_t, is evaluated on CIFAR10 image generation (up to ~3.5 FID improvement at small NFE over the approximate SDE-A and ODE baselines) and shown to maintain sample diversity. The paper also demonstrates that LIMs can be applied to text-to-speech, showing improvements on rare speakers in an imbalanced multi-speaker dataset.

## Strengths

1. **Theoretical derivation of exact reverse SDEs (Theorem 1).** The paper provides a parametric family of reverse SDEs (Equation 11) whose solutions match the forward process's marginal densities, relying only on the fractional score function. This addresses a genuine gap in the original LIM paper where the reverse SDE (Equation 9) was approximate due to an omitted intractable term. The derivation is the paper's core intellectual contribution.

2. **Consistent FID improvement at small NFE across multiple α values.** On CIFAR10, SDE-E achieves up to ~3.5 FID improvement over SDE-A and ODE when NFE=20 (Euler-Maruyama), with consistent trends across α=1.8, 1.5, and 1.2 (Table 1). The improvement diminishes gracefully as NFE increases and numerical error shrinks, which is internally consistent with the paper's motivating argument.

3. **Diversity preserved while improving quality.** Coverage metrics (Table 2) show that SDE-E generally maintains or improves sample diversity relative to SDE-A and ODE, particularly at small NFE. This is important because naive gains in FID can come at the cost of diversity, and the paper explicitly verifies this does not happen.

4. **Demonstration of LIM applicability to TTS for imbalanced data.** Table 5 shows that a Lévy-Itô TTS model (α=1.8) achieves lower word error rates on rare speakers compared to a Gaussian baseline, suggesting that LIMs' heavy-tailed noise advantage transfers to speech domains. This opens a new application direction for LIMs.

5. **Motivating analysis of the failure of approximate SDE at small NFE.** Figure 3 provides a simple Monte-Carlo simulation showing that finite-variation processes can have comparable sample-path variation to infinite-variation processes when step sizes are large, explaining why dropping the finite-variation term \(d\bar{Z}_t\) in the original SDE-A may cause significant error at small NFE.

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameter η selected using test-set FID, compromising the reported improvements.** The paper states (line 226) that η_t was "chosen as showing the best performance in terms of FID on CIFAR10 test set containing 10k images," and Figure 4 plots FID computed on the test set. The baselines (SDE-A, ODE) have no comparable free parameter to tune, so the comparison is asymmetric: the proposed method receives oracle-level η selection on the evaluation set, while baselines do not benefit from any test-set tuning. The reported FID improvements (up to 3.5 points) could be partially or fully an artifact of this data snooping. A proper validation split (or cross-validation) is needed to establish that the gains are real. This is the most significant weakness in the paper and undermines trust in the empirical claims.

### Minor

1. **No proof sketch or intuition for Theorem 1 in the main text.** The theorem is stated compactly (lines 128–134) with only a brief reference to "certain regularity assumptions" and a pointer to the literature. For a paper whose central contribution is this theoretical development, the main text provides no sense of how the drift modification \(-(1+\eta_t)\sigma_t^\alpha S_t^{(\alpha)}\) and diffusion coefficient \(\sigma_t\eta_t^{1/\alpha}\) work together to yield exact marginals. While full proofs belong in an appendix, a short sketch (e.g., showing how the fractional Fokker-Planck equation of the reverse SDE matches the forward) would greatly improve readability and allow readers to assess the result's plausibility without reading the appendix.

2. **TTS experiments are preliminary and lack key details.** The TTS results (Table 5) test only α=1.8 on a single dataset, report no confidence intervals or significance tests, and do not evaluate the proposed SDE-E sampling algorithm in the speech domain. The paper's third contribution (line 20) is specifically about training a LIM for TTS, which is accomplished, but the experiments are too thin to be convincing on their own. In particular, without error bars or multiple α values, it is unclear how robust the observed improvements for rare speakers are.

3. **No standard deviations for imbalanced CIFAR10 experiments.** Table 3 reports average FID over 5 runs but omits standard deviations. Given that the differences between methods are small (~1.5 FID), error bars are essential to assess whether the observed differences are meaningful.

4. **No analysis of sensitivity to η across independent training runs.** Figure 4 shows FID as a function of η for a single sweep, but the paper does not examine whether the optimal η value is stable across different model training seeds or data splits. Since η is the key hyperparameter of the proposed method, this limits the practical guidance offered to practitioners.

5. **No discussion of computational overhead.** The proposed SDE-E introduces η_t as an extra hyperparameter that requires tuning. The paper does not discuss the cost of this tuning or any adaptive/automatic scheme for setting η_t, which matters for practitioners considering adoption.

### Trivial

1. **Coverage improvements are sometimes marginal.** In Table 2, SDE-E coverage is occasionally within 1–2% of the best baseline, and in rare cases slightly worse (e.g., α=1.2, Exponential Integrator, N=500). The paper honestly reports this, but the diversity advantage is not uniformly strong across all settings.

## Nice-to-Haves

- **Evaluation on a second image dataset** (e.g., CelebA or LSUN) would strengthen the claim that the benefits generalize beyond CIFAR10, especially since the improvements are concentrated at small NFE.
- **A proof sketch in the main text** (a few equations showing how the fractional Fokker-Planck equation of the reverse SDE matches that of the forward process) would make the paper's central theoretical contribution more accessible.
- **An ablation fixing the η selection** via a held-out validation split (e.g., 10k images from training set) and re-reporting the main FID results would resolve the most serious concern.
- **Confidence intervals** for all tables, particularly for the imbalanced CIFAR10 (Table 3) and TTS (Table 5) results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The variation argument is tangential / does not explain why SDE-E is better."** The paper's narrative is coherent: the variation argument motivates *why SDE-A fails* at small NFE (because the dropped finite-variation term matters when step sizes are large), and SDE-E is better simply because it is *exact in marginals* and does not drop any term. This is a clean, two-part argument, not a contradiction. The reviewer's criticism reflects a preference for a different narrative structure, not a flaw.
- **"No comparison with higher-order solvers or DPM-solver-like for Lévy processes."** The paper already compares with the Exponential Integrator (Zhang & Chen, 2023), which is a higher-order solver that reduces numerical error. A DPM-solver analogue for Lévy processes does not exist in the literature and would be a separate paper. This ask is impossible or unreasonable.
- **"The TTS experiments do not use the proposed sampling algorithm."** The paper's third contribution (line 20) is "We train a Lévy-Itô text-to-speech model," not "we evaluate SDE-E on TTS." The TTS section is scoped as a demonstration of LIM applicability to a new domain, which is separate from the sampling algorithm contribution. The absence of SDE-E in TTS is not a flaw of the TTS experiments.
- **Criticism that "the variation argument does not explain why SDE-E with any particular η should be better."** SDE-E's advantage comes from being exact in marginals; the choice of η trades off noise vs. diversity, which is a separate axis from the exactness property. The paper's framing is appropriate.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the authors themselves have not already identified or discussed.

## Suggestions

1. **Fix the experimental methodology:** Hold out a validation split from the CIFAR10 training set (e.g., 10k images) to select η, then re-report results on the test set. This single change would resolve the most serious concern and make the empirical claims credible.
2. **Add a proof sketch in Section 4:** Even 3–4 lines showing how the fractional Fokker-Planck equation of (11) matches that of (1) (using the Fourier multiplier property of the fractional Laplacian) would greatly improve the paper's accessibility without adding bulk.
3. **Add error bars / confidence intervals** to Tables 3 and 5, where the reported gains are small and need variance estimates to be interpretable.
4. **Either strengthen the TTS experiments** (test multiple α values, report variances, optionally evaluate SDE-E) or clearly scope them as a preliminary demonstration of LIM applicability rather than a co-equal contribution.

---

## Score and Decision

The paper's core theoretical contribution (Theorem 1) is genuinely novel and addresses a real gap in the LIM literature. The experimental evaluation, however, is compromised by the undisclosed test-set tuning of the key hyperparameter η — a methodological error that prevents the reader from trusting the reported FID improvements. This is a correctable flaw, but in its current form the empirical evidence does not reliably support the paper's primary performance claims. Additionally, the TTS experiments are too preliminary to constitute a standalone contribution.

**Score:** 5.0 (marginally below the acceptance threshold; could be raised to 6+ with a proper validation split and corrected reporting)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>