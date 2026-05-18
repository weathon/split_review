I have thoroughly analyzed the paper and the reviewer claims. Let me now produce the final consolidated review.

---

## Summary

This paper introduces the problem of *certified calibration* — provable worst-case bounds on a classifier's calibration under adversarial perturbations, within the randomized smoothing certification framework. The authors contribute: (1) a closed-form, tight upper bound on the Certified Brier Score (CBS); (2) a mixed-integer program (MIP) formulation for the Certified Calibration Error (CCE), solved approximately via ADMM to yield the Approximate CCE (ACCE); (3) a family of calibration attacks (ACE); and (4) Adversarial Calibration Training (ACT), which fine-tunes models using calibration adversaries to improve certified calibration. Experiments on CIFAR-10 and ImageNet demonstrate calibration attacks and ACT-based improvements.

## Strengths

- **Clean theoretical contribution for the Certified Brier Score (CBS):** Theorem 1 provides a simple, closed-form, tight upper bound on the top-label Brier score under adversarial perturbations (Equation 4). This is a genuine theoretical result that does not depend on any approximation and directly enables provable guarantees on Brier score degradation.

- **Well-motivated problem formulation and effective attack demonstration:** The paper convincingly shows (Table 1) that calibration can be severely degraded while accuracy remains unchanged — e.g., a (1,y)-ACE attack increases AdaECE from 3.70% to 47.23% on ImageNet. This motivates the need for certified calibration and is a clear contribution.

- **Novel MIP formulation for CCE with practical ADMM solver:** Reformulating the worst-case ECE under perturbations as a mixed-integer program (Equation 7) is a principled approach to a non-convex, non-differentiable problem. The ADMM solver yields consistently higher bounds than baseline approaches (dECE, Brier-confidence-based bounds), often by ~0.2 in ACCE (Figure 3), demonstrating practical value.

- **Demonstration that ACT can improve certified calibration:** Table 2 and Figure 4 show that ACT fine-tuning (particularly ACCE-ACT) reduces ACCE by up to 9.3 percentage points and CBS by up to 11.4 percentage points at larger radii (R=1.0) on CIFAR-10 while maintaining competitive certified accuracy. The scatter plots in Figure 4 visualize joint improvements in accuracy and calibration.

## Weaknesses

### Fatal
None.

### Major

- **The ACCE approximation is not validated against any gold standard.** The MIP formulation (Section 3.3) is a relaxation of the true CCE, so its global optimum is an upper bound. However, ADMM on the resulting non-convex problem with ~30,000+ binary variables has no optimality guarantee. The paper compares ADMM only against weak baselines (dECE, Brier confidences), showing it outperforms *them*, but provides no evidence that the ADMM solution is close to the MIP optimum. Without validation against a global solver on small subsets, or any reported dual bound/optimality gap, the quality of the ACCE is unknown. This matters because (i) ACCE is used as the primary metric for evaluating certified calibration, and (ii) the ACCE adversary drives ACCE-ACT training — if the adversary is far from worst-case, the training signal may be weak or misdirected.

- **Training evaluation lacks statistical rigor.** Table 2 reports single values for ACCE and CBS under an opaque selection procedure ("models achieving within 3% of the highest certified accuracy..."). No error bars, standard deviations, or run counts are provided. The paper mentions "multiple fine-tunings" but does not specify how many, across how many seeds, or under what hyperparameter settings. Selecting the *best* calibration model within a 3% accuracy band creates cherry-picking risk. Additionally, certified metrics are computed on the per-model subset of test samples certifiable at a given radius — this subset can differ between models, so ACCE/CBS improvements may partly reflect a shift to easier certification sets rather than genuine calibration improvement. These gaps substantially weaken the empirical support for ACT.

- **The ImageNet results are essentially null and underexplained.** The paper acknowledges only "marginal effects (1-2%)" on ImageNet (line 301), attributing this to prior work that "struggles to find consistent effects." However, no analysis is offered for *why* ACT might fail at scale — e.g., fewer certified samples, different certificate behavior, or optimization difficulty. Since a key method (ACCE-ACT) is only clearly demonstrated on CIFAR-10, the claim that ACT is a "generally useful technique" is overstated relative to the evidence.

### Minor

- **The MIP optimization is over confidences z_{n,m} that can differ per bin for the same sample, which is a relaxation of the actual CCE.** The paper should explicitly state that the MIP optimum is an upper bound on the true CCE, and conversely, that a suboptimal ADMM solution could be *lower* than the true CCE, making the ACCE an empirical estimate rather than a formal certificate. The paper calls it "approximate" but the precise status (upper bound vs. empirical estimate) is never clarified.

- **The number of bins M for ECE estimation is not reported.** This is a meaningful hyperparameter that affects both the ACCE values and the training adversary. Without it, the results are not fully reproducible.

- **Computational cost breakdown is missing.** The paper states ACCE-ACT is "3.4% slower than SmoothAdv" but does not provide wall-clock times or a breakdown of where the additional cost is incurred (ADMM iterations vs. forward/backward passes). This makes it hard to assess practical deployability.

### Trivial

- Figure 2 and Figure 3 captions lack sufficient detail for the reader to extract quantitative information independently of the main text.

## Nice-to-Haves

- Validate ACCE by solving the MIP to global optimality on a small subset (e.g., 100 samples, 5 bins) using a commercial solver (Gurobi/CPLEX) and reporting the ratio ADMM/optimal. Alternatively, report a dual bound or LP relaxation gap to bound suboptimality.
- Report mean and standard deviation of ACCE/CBS across multiple fine-tuning runs (3–5 seeds) rather than a single best-within-band value.
- Control for the certification set by computing ACCE/CBS on the *intersection* of samples certifiable for all compared models, or report per-model certification set sizes.
- Provide a brief analysis of why ACT underperforms on ImageNet (e.g., certified sample counts, certificate width distribution, optimization difficulty).

## Removed Points

- *"Missing appendix / proof omitted"* — The parser strips these; they exist in the original submission. Removed per policy.
- *"No code is provided"* — This is a reproducibility nitpick concerning an artifact not required for evaluation. Removed per policy.
- *"AdaECE choice should be justified"* — The paper cites prior work for AdaECE (line 45); equal-count binning is a standard choice and does not require additional justification. Removed.
- *"ACCE is an unvalidated upper bound with unknown tightness"* (as phrased by the reviewer) — The paper clearly labels the ACCE as "approximate" and "empirical." While the *lack of validation* is a real weakness (retained in Major), the framing as an unacknowledged fatal flaw is excessive. Downgraded from potential Fatal to Major.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that changes how it should be interpreted relative to its own framing.

## Suggestions

1. **Validate the ACCE approximation.** On a small CIFAR-10 subset (100–500 samples, M=5 bins), solve the MIP to global optimality and report the ADMM-to-optimal ratio. This single experiment would substantially raise confidence in the entire empirical pipeline.
2. **Add statistical rigor to training results.** Report means and standard deviations over at least 3 random seeds for ACT fine-tuning. Specify the model selection protocol precisely and consider reporting performance on the intersection of certifiable samples across models.
3. **Add a limitations section or paragraph.** Explicitly discuss: (a) the approximate nature of the ACCE, (b) the reliance on randomized smoothing / ℓ₂ perturbations, (c) the lack of ImageNet-scale improvement and plausible reasons, (d) the dependence on the quality of the confidence certificate (C2).
4. **Report the number of bins M used in experiments** and any sensitivity analysis with respect to this choice.
5. **Clarify the theoretical status of the ACCE** — state that the MIP optimum is an upper bound on the true CCE, and that the ADMM solution is an empirical approximation whose gap to the MIP optimum is not quantified.

## Score and Decision

**Originality:** The problem of certified calibration is new and well-motivated. The CBS bound and MIP formulation are novel contributions.

**Importance:** The question of whether calibration can be guaranteed under attack is practically important for safety-critical deployments. The paper identifies a genuine vulnerability.

**Claims support:** Partially supported. The CBS bound is theoretically sound. The ACCE and ACT claims are only weakly supported due to the unvalidated approximation and lack of statistical rigor.

**Soundness:** Moderate. The theory is sound. The experimental design has significant gaps (no ACCE validation, no error bars, uncontrolled certification sets).

**Clarity:** Generally clear, though the paper would benefit from explicitly stating the status of the ACCE as an upper bound vs. empirical estimate.

**Value:** The problem and theoretical framework are valuable. The empirical evidence for ACT is suggestive but not conclusive.

The paper introduces a timely and novel problem with a clean theoretical result (CBS bound). However, the empirical validation has significant gaps: the ACCE approximation is unvalidated against any gold standard, the training results lack statistical rigor and use an opaque selection procedure, and the method only demonstrates clear improvements on CIFAR-10. These issues prevent the paper from providing convincing evidence of its central claims. The ideas merit a second chance with strengthened empirical validation, but the current evidence is insufficient for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>