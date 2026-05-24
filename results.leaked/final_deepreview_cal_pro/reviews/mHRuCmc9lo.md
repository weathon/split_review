Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper develops a principled minimax framework for robust decision-making with partially calibrated forecasts. Given a forecaster that satisfies $\mathcal{H}$-calibration (a family of moment constraints weaker than full calibration), the authors characterize the optimal robust decision policy via duality (Theorem 3.1). The central insight is a sharp transition: once the calibration test class $\mathcal{H}$ contains the decision-calibration indicators $\{\mathbf{1}_{R_a}\}$, the robust policy collapses to the simple plug-in best response — recovering the trust semantics of full calibration through a much more tractable condition (Theorems 4.1–4.2). The framework is instantiated with practical calibration sources including self-orthogonality from squared-loss training and bin-wise calibration.

## Strengths

- **Dual characterization of the minimax-optimal policy (Theorem 3.1).** The theorem reduces the infinite-dimensional robust decision problem to a pointwise best response against an adversarially shifted belief $q^*(v)$, with multipliers $\lambda^*$ obtained from a finite-dimensional concave maximization. This yields a clean, interpretable, and computationally tractable decision rule.

- **Sharp transition to plug-in best response under decision calibration (Theorems 4.1–4.2).** The proof shows that decision-calibration constraints make the expected utility of $a_{\text{BR}}$ *invariant* to the adversary's choice of $q \in \mathcal{Q}$, so the robust policy collapses to the plug-in rule. This is a crisp and elegant theoretical insight that identifies decision calibration as a natural, tractable target for forecaster design.

- **Practical calibration sources grounded in standard training (Propositions 4.4–4.5).** The self-orthogonality guarantee from squared-loss training with linear heads provides a "free" partial-calibration condition requiring no post-processing. Bin-wise calibration yields a simple closed-form robust policy using only bin-mean estimates. Both are directly actionable.

- **Multi-problem optimality (Corollary 4.3).** A single $\mathcal{H}$-calibrated forecaster that covers the decision-calibration tests for multiple downstream tasks is simultaneously trustworthy for all of them — broadening the practical appeal.

- **Clear exposition and helpful visualizations (Figures 1–2).** The interpolating property schematic and the sharp-transition diagram effectively communicate the paper's conceptual arc.

## Weaknesses

### Major

None.

### Minor

- **Experimental section is underdeveloped relative to the theory.** The experiments (Section 5) use only two regression datasets with point estimates and no error bars. The construction of the adversarial evaluation distributions is described only in general terms — how exactly the worst-case $q^*$ is computed and applied at test time is not specified. No empirical verification is provided that the trained forecaster actually satisfies the assumed self-orthogonality condition (Proposition 4.4), even approximately. These gaps mean the empirical component provides only weak independent evidence for the practical value of the method. This does not undermine the theoretical contributions, which are the paper's primary strength, but the experimental section would benefit from greater detail and rigor.

- **No discussion of finite-sample effects.** The framework replaces population expectations with empirical estimates from the calibration split (Section 5), but the paper does not address how estimation error in the moment constraints or dual variables propagates to the decision rule's regret. A brief treatment or pointer to standard concentration results would make the framework more directly usable in practice.

### Trivial

- **Theorem 3.1 omits explicit technical conditions.** The theorem statement asserts existence of a saddle point but does not list supporting conditions (e.g., compactness of $\mathcal{A}$, Slater-type constraint qualification for strong duality), though these are standard.

- **Unsubstantiated sensitivity claim.** The statement that "qualitative conclusions … remain the same under other reasonable parameter choices" (Section 5.1) is asserted without supporting evidence or even a brief parameter sweep.

## Nice-to-Haves

- A small synthetic experiment showing the sharp transition as $\mathcal{H}$ is systematically enlarged (from empty, to self-orthogonality, to bin-wise, to decision calibration) would directly visualize the theory of Figure 2 and be more informative than the current two-policy comparison.
- A brief summary in the main text of how the results adapt to *approximate* $\mathcal{H}$-calibration (currently deferred entirely to Appendix B) would improve self-containment.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Optimization method not given"** — The paper does mention standard methods (projected subgradient ascent, primal-dual schemes) in the discussion following Theorem 3.1. While the specific method used in experiments is not detailed, this is a minor implementation detail, not a genuine gap.
- **Concerns about missing Appendix B** — The parser strips appendices from all papers. The original submission contains this material; the paper explicitly references it. This is not an author error.
- **Formatting/style nitpicks** — None substantively affect the paper's contribution or clarity.

## Novel Insights

The sharp-transition result (Theorems 4.1–4.2) is the paper's most striking insight: decision calibration — requiring only $|\mathcal{A}|$ moment constraints rather than the exponentially many needed for full calibration — is both necessary and sufficient for the robust policy to collapse to the plug-in best response. This upgrades decision calibration's previously known semantics (no swap regret) to full minimax optimality, and reveals that the space of possible robust policies is not a rich hierarchy but collapses at a specific, tractable threshold. This connection between calibration strength and decision-theoretic trustworthiness is genuinely novel and has practical implications for how forecasters should be designed and post-processed.

## Suggestions

- Expand the experimental section with at minimum: (a) a description of how adversarial distributions are constructed numerically, (b) a measure of how well the trained forecaster satisfies self-orthogonality in practice, and (c) standard errors or confidence intervals for Table 1.
- Add a brief discussion (even a paragraph) on how finite-sample estimation of the moment constraints affects the robust policy's guarantees, pointing to relevant concentration results.
- Include a one-paragraph summary in the main text of the approximate $\mathcal{H}$-calibration results from Appendix B, so the paper is self-contained on this practically important extension.

## Score and Decision

**Round 1 bracketing:** Searched across three bands. Weak anchors (avg 1.50–3.40) are clearly below this paper. Middle anchors (4.67–6.00), such as "Does Calibration Affect Human Actions?" (4.67) and "Addressing Misspecification in SBI" (6.00), have significant methodological or experimental concerns. Strong anchors (all 8.00), including a DRO optimization paper and a resource-allocation theory paper, combine strong theory with thorough experiments. Initial bracket: **6.0–8.0**.

**Round 2 narrowing:** Retrieved anchors at 6.75–7.50. "Provable Uncertainty Decomposition via Higher-Order Calibration" (TId1SHe8JG, 7.50, scores 8/8/8/6) is the closest comparator — a theoretical paper introducing a novel calibration notion with clear guarantees, modest but adequate experiments. Our paper's theory is comparably strong; its experiments are thinner. "Decision-Focused Uncertainty Quantification" (iOMnn1hSBO, 6.80, scores 6/8/8/6/6) has stronger experiments but a less elegant theoretical core.

**Final comparison:** The paper is slightly below TId1SHe8JG (7.50) due to weaker empirical validation, and clearly above iOMnn1hSBO (6.80) in theoretical originality and clarity. It does not reach the 8.00 anchors, which pair strong theory with comprehensive experiments. **Final score: 7.0.**

**Anchor summary (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| WoJzHQIIUk | 1.50 | R1 | Much weaker; rejected minimax BNN paper |
| p79lnC36CO | 2.00 | R1 | Much weaker; calibration diagnosis paper |
| ZBL26FX0FT | 3.00 | R1 | Weaker; selective classification paper |
| lvHHWDJCcr | 3.40 | R1 | Weaker; calibrated metric paper |
| XM7INBbvwT | 4.67 | R1 | Weaker; HCI calibration study with methodological concerns |
| 34xYxTTiM0 | 5.50 | R1 | Weaker; calibration optimization paper |
| X0epAjg0hd | 5.67 | R1–R2 | Weaker; calibration evaluation survey |
| g6fYDGKeyB | 6.00 | R1–R2 | Below; SBI calibration with split reviews |
| uuPkll6i7m | 6.75 | R2 | Slightly below; certified calibration paper |
| dIkpHooa2D | 6.75 | R2 | Slightly below; group DRO in function space |
| iOMnn1hSBO | 6.80 | R2 | Below; decision-focused conformal prediction |
| TId1SHe8JG | 7.50 | R2 | Slightly above; closest comparator — similar theory-forward calibration paper |
| TTrzgEZt9s | 8.00 | R1 | Above; DRO with strong theory + experiments |
| A3YUPeJTNR | 8.00 | R1 | Above; prediction-timing theory with thorough analysis |
| stUKwWBuBm | 8.00 | R1 | Above; MARL through behavioral economics |
| UHPnqSTBPO | 8.00 | R1 | Above; LLM judges with provable guarantees |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>