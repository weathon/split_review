Now let me produce the final consolidated review.

## Summary

This paper proposes the Cascaded Learned Bloom Filter (CLBF), a new learned Bloom filter architecture that interleaves multiple machine learning models (weak learners) with trunk and branch Bloom filters in a cascade, culminating in a final PLBF-style arrangement. A dynamic programming algorithm jointly optimizes the number of models (depth D) and the false positive rates of each Trunk Bloom filter, with a tunable hyperparameter λ to trade off between memory efficiency and reject time. Experiments on the Malicious URLs and EMBER datasets show up to 24% memory reduction and up to 14× reject-time reduction compared to PLBF, the prior state-of-the-art.

## Strengths

- **Principled DP optimization for joint model-filter configuration**: The dynamic programming formulation (Equations 4–10) jointly optimizes model depth D and Trunk Bloom filter false positive rates with proven polynomial complexity O(̄DP² + ̄DPK). This goes beyond prior LBFs (sandwiched LBF, PLBF) that optimize only Bloom filter parameters for a fixed model, providing an automated solution to the model-filter size balance problem.

- **Up to 14× reject-time reduction on EMBER with near-Pareto frontier**: In the memory vs. reject-time experiment (Section 4.2, Figure 5), CLBF at ~500kB on EMBER achieves approximately 14× shorter average reject time than PLBF. The CLBF curve forms a near-Pareto frontier where no other LBF configuration simultaneously achieves lower memory and shorter reject time—a clear empirical result.

- **Architecture generalizes existing LBFs**: CLBF with one Trunk and one Final Bloom filter reduces to sandwiched LBF; without Trunk/Branch filters but with multiple Final filters, it reduces to PLBF (Section 3.1). This establishes that CLBF searches a strictly larger design space than either prior architecture, not an ad-hoc structure.

- **Construction overhead is honestly bounded and contextualized**: Section 4.3 reports that CLBF's construction time is 10–41% longer than existing LBFs at the same model size (D=100), and provides a reasonable argument that this overhead is acceptable because LBFs are reconstructed infrequently (e.g., malicious URL sets change slowly).

## Weaknesses

### Major

- **The memory-efficiency claim (24%) rests on an incomplete PLBF comparison that conflates architecture with automatic depth selection.** CLBF selects D between 18–38 on EMBER (Section 4.1, line 150), but PLBF is evaluated only at D ∈ {1, 10, 100}. The paper does not test whether PLBF at the same D values that CLBF selects (e.g., D=30) would achieve comparable memory. If PLBF at D=30 matches CLBF's memory, the advantage would be entirely attributable to automatic D selection—not the cascaded architecture—and the 24% figure would be a comparison against deliberately suboptimal PLBF configurations. The paper presents no ablation that separates the effect of (a) the cascaded architecture from (b) automatic depth selection via DP. This is a critical gap because the paper's core claim is about optimal *balance* achieved by the architecture, not just automated tuning of D.

### Minor

- **Reject-time calculation ignores Bloom filter lookup time, and the paper does not validate this approximation experimentally.** The expected reject time (Equation 3) is computed from ML inference time only, with Bloom filter lookup time set to zero (line 67). CLBF's reject path may involve more Bloom filter lookups than PLBF's (a non-key may traverse multiple TBFs as false positives). The paper acknowledges this is an approximation but provides no wall-clock measurements to validate it. Without measured reject times, the 14× claim is a consequence of the formula's assumptions, not an empirical finding.

- **Key implementation parameters are unspecified, compromising reproducibility.** The DP discretization parameters p and P (line 126) are never given numerical values. The number of Final Bloom filters K is defined (line 47) but never specified. The Bloom filter variant (standard, Cuckoo, Xor, Ribbon) is not stated. These omissions make it impossible to reproduce the results without contacting the authors.

- **Ada-BF is discussed in related work but excluded from experiments without explanation.** The paper states "we have omitted the results of some baselines" (line 144) and explains the omission of sandwiched LBF in the memory-accuracy experiment (line 148). However, Ada-BF (Dai & Shrivastava, 2020), another score-partitioned LBF, is never evaluated or explained as omitted. While PLBF is the stated SOTA, the absence of Ada-BF from the experimental comparison is a gap worth noting.

- **Only two datasets are evaluated.** While these are standard in the LBF literature (following Vaidya et al., 2021; Sato & Matsui, 2023), the generality of the findings would be strengthened by additional datasets or controlled synthetic experiments varying noise level and class imbalance.

- **The paper does not verify whether the constructed CLBF empirically satisfies its target false positive rate F.** The optimization constrains the "expected" FPR via a per-filter heuristic (min(F g/h, 1)), but no experiment reports measured FPR on test data to confirm the constraint is actually met. This is important because the heuristic's correctness in a multi-level cascade is not self-evident.

### Trivial

- The θ threshold optimization uses a heuristic grid search over α ∈ {0.5, 0.2, 0.1, ..., 0.0001, 0.0} (line 53). The step sizes in this sequence are not fully specified. However, the paper acknowledges this limitation in Section 5.

## Nice-to-Haves

- Adding error bars or multiple-trial statistics would strengthen confidence in quantitative claims, though single-run evaluation is standard in the LBF literature.
- Including a comparison of CLBF against PLBF at the same D (the D that CLBF selects) would cleanly isolate the architectural contribution from the depth-selection contribution.

## Removed Points

The following points from the harsh critic were considered but removed:

- **Criticism about "no ablation studies"** — This is the same underlying concern as the Major weakness above (PLBF comparison at limited D). It has been merged into the first Major weakness rather than listed separately.
- **Criticism about "no statistical measures"** — Single-run evaluation without error bars is the standard reporting practice in the LBF literature (Vaidya et al., 2021; Sato & Matsui, 2023). Demanding confidence intervals where they are not the norm is scope creep. Moved to Nice-to-Haves.
- **"The paper frames model size optimization as a core contribution but what CLBF does is model selection"** — This is a distinction without a difference for the paper's contribution. The paper clearly states that it trains ̄D weak learners and selects the first D ≤ ̄D. This is described transparently; the semantic framing does not affect the technical content.
- **Argument that "the DP does not guarantee the global FPR constraint" in a multi-level cascade** — The paper uses the same min(F g/h, 1) heuristic as PLBF for BBF and FBF FPRs. While the critic speculates this may not satisfy the global constraint, the paper's optimization minimizes memory subject to an *expected* FPR ≤ F, and the heuristic is standard. Without evidence that the heuristic actually fails, this is speculation. The concern about *empirical verification* of the FPR is retained as a minor weakness.
- **Criticism comparing against "fast PLBF" instead of standard PLBF for construction time** — The paper explicitly states that fast PLBF "constructs the same data structure as PLBF more quickly" (line 165), so the comparison is meaningful.
- **"The conclusion overstates the contribution"** — This is a subjective assessment. The paper's claims are bounded by the experimental results presented.
- **Various formatting and presentation nitpicks** — Removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The central insight—that interleaving multiple ML models and Bloom filters in a cascade can be jointly optimized via DP for the model-filter size balance—is the paper's own contribution. The reviews do not surface any additional novel perspectives.

## Suggestions

1. **Add the critical ablation**: Compare CLBF (λ=1) against PLBF at the exact D that CLBF selects (e.g., D=30 on EMBER). If PLBF at D=30 matches CLBF's memory, the contribution is automatic D selection; if CLBF still beats PLBF at the same D, the architecture provides additional benefit. Either result is informative.

2. **Report measured wall-clock reject times** in addition to the formula-based estimate, to validate that ignoring Bloom filter lookup time does not systematically bias the comparison.

3. **Specify p, P, K, and the Bloom filter variant** in the paper (or in the appendix) for reproducibility.

4. **Report empirical false positive rates** on the test set for each experimental configuration to verify that the constructed CLBF meets its target F.

5. **Add at least one additional dataset** or a synthetic experiment to probe which data properties (noise, class imbalance, separation) drive CLBF's advantages over PLBF.

## Score and Decision

Based on my assessment: the paper proposes a genuinely novel architecture with a principled optimization, and the reject-time results are compelling. However, the central memory-efficiency claim (24% reduction) is undermined by a comparison against PLBF at only three depths while CLBF operates at depths the paper itself shows are different. The lack of an ablation isolating architecture from automatic depth selection is a significant gap that must be addressed before the paper's claims can be fully accepted. The paper has clear contributions and potential but needs major experimental strengthening to support its headline claims at a top conference.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>