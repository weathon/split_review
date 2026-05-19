Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper extends Lévy-Itô diffusion models (LIMs) by deriving a parametric family of reverse SDEs (Theorem 1, Equation 11) whose marginal densities match the forward process exactly, unlike the original approximate reverse SDE from Yoon et al. (2023). The parameter η_t controls the amount of α-stable noise added at inference. The paper demonstrates FID improvements on CIFAR-10 at small numbers of function evaluations (NFE) and provides a first demonstration of LIM-based text-to-speech on an imbalanced dataset.

---

## Strengths

1. **Theoretical derivation of an exact reverse SDE family for LIMs (Theorem 1).** The paper correctly identifies a gap: conventional diffusion models (Song et al., 2021a) have a parametric family of exact reverse SDEs, but LIMs only had an approximate SDE (Equation 9) and an exact ODE (Equation 10). Theorem 1 fills this gap by providing SDE (11), which is exact in marginals and tunable via η_t. The result is non-trivial because the fractional Laplacian is a non-local operator and reverse-time dynamics for jump processes are more complex than for Gaussian diffusions.

2. **Principled justification for why the proposed SDE can outperform the approximate SDE at low NFE.** Figure 3 provides a concrete simulation showing that a finite-variation process (compensated Gamma) has comparable variation to an infinite-variation Lévy process when the number of solver steps is small. This directly supports the paper's core argument: the omitted dZ̄_t term in Equation (9) may not be negligible at coarse discretizations, motivating the exact SDE-E.

3. **Significant and consistent FID improvements across multiple α values and solvers at small NFE.** Table 1 reports gains up to 3.5 FID (e.g., α=1.8, Euler-Maruyama 20 steps: SDE-E 37.6 vs SDE-A 41.1 vs ODE 42.7). The improvement is consistent for α=1.8, 1.5, and 1.2 and for both Euler-Maruyama and Exponential Integrator solvers, and diminishes as NFE increases (as the theory predicts).

4. **Coverage metric confirms diversity is preserved.** Table 2 shows that SDE-E achieves coverage values generally higher than or comparable to the deterministic ODE and the approximate SDE-A, particularly at low NFE where the diversity advantage is most needed (e.g., α=1.8, Euler-Maruyama 20-step: SDE-E 47.5% vs SDE-A 46.0% vs ODE 41.2%).

5. **First application of LIMs to text-to-speech.** While the TTS experiments are preliminary (see weaknesses), the paper represents the first attempt to apply LIMs to speech generation on imbalanced multi-speaker data, demonstrating a potential new application direction.

---

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameter η_t selected on the test set (evaluation protocol violation).** The paper states (lines 226–227): *"with the parameters η_t chosen as showing the best performance in terms of FID on CIFAR10 test set containing 10k images."* Figure 4 likewise plots FID on the test set as a function of η. This is a textbook violation of evaluation protocol: the test set should be used only for final reporting, not hyperparameter selection. Every reported FID value for SDE-E in Tables 1 and 2 is therefore optimistically biased relative to what would be achieved with proper validation.

   **Why this is Major, not Fatal:** The paper is tuning essentially a single scalar parameter η (with smoothing at boundaries), which has very few degrees of freedom for overfitting on a 10k-image test set. The improvement is large (up to 3.5 FID) and consistent across three α values, two solvers, and multiple NFE settings — a pattern unlikely to arise purely from overfitting a single parameter. However, the protocol error is unambiguous and must be corrected: the authors should re-run the evaluation using a held-out validation split for tuning and report FID on the standard test set. Without this fix, the reported numbers cannot be taken at face value.

### Minor

2. **Text-to-speech experiments are cursory and lack detail.** The entire TTS experimental description consists of a single table reference (Table 5, line 245) with no subsection, no description of architecture, training schedule, data splitting, imbalance ratio, or the number of function evaluations used at inference. The claim that *"a well-trained text-to-speech Lévy-Itô model may have advantages over standard diffusion models on highly imbalanced datasets"* (abstract) is appropriately hedged ("may"), but the evidence is too thin to meaningfully evaluate. No confidence intervals or significance tests are reported. This does not undermine the paper's core contribution (the SDE derivation), but it does weaken the third claimed contribution significantly.

3. **No error bars or multiple-seed reporting for any experiment.** FID and coverage are known to vary across training runs and generation seeds. The paper reports single values throughout (except Table 3, which reports averages over 5 runs but no variance). Given the paper's reliance on quantitative comparisons, the absence of confidence intervals makes it impossible to assess whether the reported improvements are statistically significant.

### Trivial
None.

---

## Nice-to-Haves

- **Include a proof sketch of Theorem 1 in the main text.** The theorem is central to the paper's contribution, and a brief sketch showing that the fractional Fokker-Planck equation (2) is preserved under SDE (11) would improve readability and trust. (The full proof is presumably in the appendix, which was stripped during parsing.)
- **Specify the exact functional form of η_t tested.** The paper mentions testing functions that are constant η "most of the time" with smoothing near 0 and T, but does not give the precise parameterization or the set of η values evaluated.
- **Clarify whether the FID scores in Tables 1–2 use the training set or test set as reference.** The text says generated images are compared with 50k CIFAR-10 training set images, but the η selection is described as using the test set. The relationship between these two reference distributions should be clarified.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Proof of Theorem 1 not presented in main text" (Harsh Critic).** The proof is standard to place in an appendix. The instruction disallows penalizing missing appendix content — the appendix exists in the original submission. Moved to Nice-to-Haves as a suggestion for a proof sketch.
- **"Non-sequitur about ODE comparison at lines 268–277" (Harsh Critic).** The paper simply states that the ODE is exact (as proven by Yoon et al., 2023) — this is a factual statement from prior work, not a non-sequitur. The paper later discusses the diversity-vs-exactness trade-off in context.
- **"Missing architecture / implementation details for image experiments" (Harsh Critic).** The paper explicitly states it follows Yoon et al. (2023) precisely, which is standard practice.
- **"Code and model release not mentioned" (Harsh Critic).** Per hard rules, speculating about reproducibility from the absence of a code release statement is removed.
- **Several generic or speculative weaknesses** from the Harsh Critic (e.g., "could the metric be measuring a proxy?", speculation about the appendix). These lack concrete anchors in the paper text.
- **Strength Finder strengths that are generic/superficial** — all listed strengths were concrete and specific, so none were dropped for that reason. However, Strengths 2 (FID improvements) and 5 (η analysis) are qualified by the test-set tuning weakness.

---

## Novel Insights

The reviews surface an interesting meta-point about LIM evaluation: the paper's core innovation (the exact reverse SDE family) is theoretically motivated by the fact that coarse discretizations can make infinite- and finite-variation processes comparable in magnitude (Figure 3). This insight — that a theoretically negligible term becomes practically significant at low NFE — is a useful conceptual contribution that goes beyond the specific SDE derivation. It suggests that other approximate sampling schemes for jump-process-based models may similarly suffer at coarse discretizations in ways that are not immediately obvious from asymptotic theory. The reviews do not raise genuinely novel observations beyond what the paper itself contributes on this front.

---

## Suggestions

1. **Fix the evaluation protocol:** Re-run the image experiments with η_t tuned on a held-out validation split (e.g., 10k images held out from the CIFAR-10 training set) and report FID on the standard test set. If the improvements persist (which they likely will), the claim is credible. Report the optimal η values found and whether they are consistent across validation and test splits.

2. **Strengthen the TTS evaluation:** Add experimental details (architecture, training schedule, NFE used, imbalance ratio), report metrics with confidence intervals across multiple seeds, and compare against a stronger Gaussian baseline of equivalent capacity and training budget.

3. **Add error bars or multiple-seed reporting** to all tables (at least 3 seeds for each configuration).

4. **Include a brief derivation sketch for Theorem 1** in the main text to increase transparency.

---

## Score and Decision

**Overall assessment:** The paper makes a genuine theoretical contribution by deriving an exact parametric family of reverse SDEs for Lévy-Itô diffusion models, filling a clear gap in the literature. The empirical results show promising and consistent improvements at small NFE, and the motivation (finite-variation terms matter at coarse discretizations) is well-supported. However, the evaluation protocol is flawed: hyperparameter selection on the test set undermines the reported FID numbers, and the TTS experiments are too preliminary to constitute a meaningful contribution. The paper is on the right track but requires revision before it meets the bar for acceptance.

**Originality:** Moderate — the SDE family is an adaptation of Song et al. (2021a)'s technique to the LIM setting, which is non-trivial due to the fractional calculus involved but still incremental.

**Quality of claims:** The central theoretical claim (Theorem 1) is well-stated. The empirical claims are plausible but weakened by the test-set tuning issue.

**Soundness of experiments:** The experimental design has a clear protocol flaw (test-set tuning). The underlying data likely supports the conclusions, but the reporting as-is is not trustworthy.

**Clarity:** Well-written and clearly structured. The variation argument (Figure 3) is particularly well-presented.

**Value to community:** Useful for practitioners and researchers working with LIMs or other heavy-tailed diffusion models.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**