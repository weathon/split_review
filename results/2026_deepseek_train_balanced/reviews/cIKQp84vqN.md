## Summary

This paper proposes Adaptive Graduated Non-Convexity (AGNC) for robust point cloud registration. The core idea is to replace the fixed multiplicative scale schedule in GNC with an adaptive scheme that monitors the smallest eigenvalue of the Hessian (λ_min(H) > 0) via binary search to determine the next scale parameter μ. The paper also claims a multi-task knowledge sharing mechanism for collaborative optimization across cost functions at different GNC stages. Experiments on simulated (Stanford repository), indoor (3DMatch, 3DLoMatch), and outdoor (KITTI) datasets show strong registration accuracy, including at extreme 99% outlier rates.

## Strengths

- **Principled adaptive scale reduction guided by Hessian eigenvalue monitoring.** The idea of using λ_min(H) to adaptively set μ_{k+1} (Section 3.2, lines 86–98) is well-motivated and clearly described. The 2D line-fitting example (Fig. 2, Table 1) provides direct empirical evidence: AGNC converges to the global minimum in 8 stages, whereas ζ=4 requires 16 (slow but correct) and ζ=20 needs 6 but falls into a local minimum. This directly demonstrates the advantage over fixed-schedule GNC.

- **Strong empirical results across diverse benchmarks.** AGNC achieves competitive or state-of-the-art results on simulated data (Stanford repository, Fig. 3), indoor scenes (3DMatch, Table 3; 3DLoMatch, Table 4), and outdoor scenes (KITTI, Table 5). On 3DMatch, the paper reports registration recall 0.15 higher than the strongest competitor MAC (line 208). On KITTI, AGNC outperforms all compared methods regardless of descriptor choice (line 217). The method maintains near-zero error even at 99% outlier rates on simulated data.

- **Computationally efficient adaptation.** The Hessian is a 6×6 matrix (line 128), making the binary search for λ_min inexpensive. This practical consideration is explicitly noted and is important for real-world adoption.

## Weaknesses

### Major

- **The multi-task knowledge sharing mechanism — listed as a core contribution — is not actually described.** Section 3.3 (lines 146–153) states the goal: "implement the collaborative optimization of non-convex cost functions at different levels through a multi-task sharing mechanism" and formulates the problem as argmin{f_{μ_k}(z), f_{μ_{k-1}}(z), ..., f_{μ_{k-j}}(z)}. However, **no algorithmic mechanism is specified.** How are multiple cost functions optimized jointly? What information is shared? How does knowledge transfer between μ-levels work? Line 5 of Algorithm 1, which should specify this, is blank. A contribution that is not specified cannot be evaluated or reproduced. If this mechanism is essential to performance (as the ablation suggests), the paper is incomplete without it. If it is inessential, it should not be listed as a separate contribution. Either way, the paper as written effectively has only one described contribution (the adaptive GNC scheme).

- **The ablation study conflates two independent interventions into one condition.** The ablation (Table 6, lines 227–231) tests "no adaptive GNC + no multi-task transfer" as a single combined condition against the full method. This does not allow the reader to attribute performance changes to either component individually. A proper ablation requires at least three conditions: (i) full method, (ii) adaptive GNC without multi-task sharing, (iii) fixed schedule with multi-task sharing. Without this, the claim that both components contribute independently (Contributions, line 18) is unsubstantiated.

### Minor

- **Directly relevant adaptive GNC baselines (GradOpt, ASKER) are only compared in the supplementary material.** The paper identifies these as prior adaptive GNC methods (line 138) but defers all quantitative comparison to Table 2 of the supplementary. For an adaptive-GNC paper, these are the most relevant baselines and should appear in the main paper, or at minimum be summarized with key numbers.

- **The binary search procedure is underspecified.** Line 128 states "We do a binary search with a search interval defined below μ_k" but does not specify the lower bound, termination criterion, or what happens if the monotonicity assumption (λ_min decreases monotonically with μ) is violated. The paper acknowledges this assumption and says "we can further decrease the search interval to make sure this assumption is reliable" — but this is too vague for reproducibility. The search range, tolerance, and fallback strategy should be explicitly stated.

### Trivial

- **The "guarantee" language around Hessian-based scheduling** (lines 94–96) is slightly overstated. The claim that z_{k+1} is "guaranteed to be in the same convergence domain" when the Hessian remains positive definite is standard and cited, but readers may interpret this as a stronger guarantee than intended. The global minimum claim is appropriately hedged ("likely to be"). Consider tightening the phrasing in line 94 to avoid overinterpretation.

## Nice-to-Haves

- **Error bars / confidence intervals** for the 100 Monte Carlo runs on simulated data. This would strengthen the statistical claims.
- **A failure case analysis** (e.g., cases on 3DLoMatch where AGNC ties with SC²-PCR in RR) would build credibility.
- **Testing with additional robust cost functions** (Huber, Cauchy, Welsch) would help substantiate the claim that the scheme is universal.

## Removed Points

The following points were raised by reviewers but are removed as noise:

- **"Only one cost function is tested"** — The paper explicitly states the scheme is universal but instantiates with GM as an example (line 116). Testing additional cost functions is scope creep, not a flaw. The derivation in Eqs. 8–10 is GM-specific but the binary-search principle on λ_min(H) is general.
- **"Outlier generation produces trivial outliers"** — The paper follows TEASER++'s exact setup (line 192). This is a standard protocol in the field, not a flaw unique to this paper.
- **"No error bars / confidence intervals"** — A nice-to-have; many registration papers at top venues do not report error bars for this type of experiment.
- **"No failure case analysis"** — A nice-to-have, not a core weakness.
- **"Ablation study confirms both proposed components contribute independently"** (claimed by the Strength Finder) — Misreading of the paper. The ablation combines both removals into one condition and does not isolate individual components.
- **"Missing related works"** — The paper's related work section (Section 2) is thorough and covers the relevant literature adequately.

## Novel Insights

None beyond the paper's own contributions. The reviews identify that the multi-task sharing mechanism is underspecified and the ablation is poorly designed, but these are gaps in the paper's presentation, not novel observations about the method's potential.

## Suggestions

1. **Specify the multi-task knowledge sharing mechanism.** Provide a full algorithmic description: how are multiple cost functions jointly optimized? What is being shared (parameters, gradients, solutions)? This could be a weighted combination, alternating minimization, an ensemble, or another scheme — but it must be specified. Alternatively, if the adaptive GNC alone is the core contribution, remove the multi-task sharing as a claimed contribution and redesign the ablation accordingly.

2. **Redesign the ablation study** to include at minimum three conditions: (i) full AGNC, (ii) adaptive GNC without multi-task sharing, (iii) fixed GNC schedule with multi-task sharing. This will properly isolate the contribution of each component.

3. **Move the GradOpt and ASKER comparison into the main paper** or at least summarize the key results. These are the most directly relevant baselines for evaluating an adaptive GNC method.

4. **Specify the binary search parameters** — interval bounds, termination criterion, and any fallback if the monotonicity assumption is violated.

5. **Tighten the "guarantee" language** in lines 94–96 to avoid potential overinterpretation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>