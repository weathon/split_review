Now I have a thorough understanding of the paper. Let me compose my final review.

---

## Summary

This paper proposes Curvature Enhanced Manifold Sampling (CEMS), a data augmentation method for regression that generates synthetic (x,y) pairs by sampling from a second-order approximation of the data manifold. It extends prior first-order manifold sampling (FOMA) by incorporating curvature information via the CAML framework (Li, 2018). The method constructs local neighborhoods in joint input-output space, computes tangent and normal bases via SVD, estimates gradient and Hessian through a differentiable linear solve, and samples new points using a second-order Taylor expansion. Experiments across nine datasets spanning tabular, time series, and image domains show consistent (if modest) improvements over several baselines.

## Strengths

- **Principled extension of first-order manifold sampling to second-order.** The paper correctly identifies that first-order methods (FOMA) struggle with curved manifolds and proposes a clean, theoretically motivated second-order alternative. The sine example (Fig. 1) provides an intuitive visualization of why curvature matters, showing CEMS following the manifold near high-curvature points where first-order approximations deviate.

- **Consistent empirical performance across diverse regression tasks.** Tables 1 and 2 show CEMS achieving best or second-best results on 4/4 in-distribution metrics and 6/9 out-of-distribution metrics across nine datasets, spanning tabular, time series, and image domains. The SkillCraft worst-case improvement of ~8% relative to the second-best method is notable. The method is evaluated against strong baselines including FOMA, C-Mixup, ADA, and standard ERM, using established benchmarks from Yao et al. (2022).

- **Fully differentiable, domain-independent design with reasonable complexity.** The method is architecture-agnostic and operates on the joint (x,y) space without domain-specific assumptions. The complexity analysis shows time complexity O(b²D) under the low intrinsic dimension assumption (d ≪ D), and the ablation study (Table 3) demonstrates that batch-wise basis sharing (CEMS) achieves nearly identical accuracy to per-point computation (CEMSₚ) with much lower SVD overhead.

- **Honest discussion of limitations.** Section 6 forthrightly acknowledges the underdetermined linear system issue when intrinsic dimension is large and the SVD memory costs, and suggests practical mitigations (ridge regression, reduced intrinsic dimension estimates).

## Weaknesses

### Fatal
None.

### Major

- **Limited theoretical novelty relative to claimed scope.** The paper describes its contribution as "providing the fundamental theory and practical tools for approximating and sampling general data manifolds," but the theoretical centerpiece (Theorem 4.1) is a standard Taylor expansion error bound cited from Fowkes et al. (2013). This bound assumes the true function is known and smooth — it does not account for the estimation error of ∇g and H from finite, noisy samples using an underdetermined linear system. The gap between the idealized bound and the actual algorithm's behavior is not analyzed, so the theorem does not directly justify CEMS's practical performance.

- **Missing sensitivity analysis of critical hyperparameters.** The method's behavior depends on three key choices: neighborhood size k (set to a fixed constant independent of d), noise scale σ, and estimated intrinsic dimension d. The paper acknowledges that k should scale as O(d²) for an overdetermined system, but neither analyzes how performance degrades when k is too small nor empirically tests sensitivity to these parameters. Without this analysis, it is not clear whether the observed improvements are robust or fragile to hyperparameter choices.

- **No direct validation that generated samples are functionally meaningful on real data.** The sine example (Fig. 1) convincingly shows that CEMS follows a known 2D manifold with no noise. However, for real datasets, the paper provides no diagnostic evidence (e.g., plots of generated vs. true function values, distance-to-manifold measures) that CEMS-generated (x,y) pairs respect the underlying regression function better than FOMA or simple additive noise. The empirical results serve as indirect validation, but the paper would be strengthened by directly examining the quality of generated samples.

### Minor

- **Marginal improvements without statistical significance testing.** Most RMSE improvements over FOMA are in the 1–5% range (e.g., Airfoil 0.093 vs. 0.097, NO2 0.018 vs. 0.019, Crime Avg 0.044 vs. 0.045). While the pattern is consistent across many datasets, the main text reports only means over three seeds. Standard deviations are deferred to Appendix H (stripped by the parser). No confidence intervals or statistical significance tests are reported. Given the small margins, the possibility that some gains are within the noise of a 3-seed evaluation cannot be ruled out from the main paper alone.

- **No runtime or memory benchmarks.** The paper claims "only a mild computational overhead" but provides no wall-clock time or GPU memory measurements to substantiate this. Given that the method involves per-point least-squares solves and per-batch SVD computations, quantifying overhead would help practitioners assess the practical trade-off.

- **Unclear statement in complexity analysis.** Line 102 states "d ≪ D therefore d ∈ O(D²)," which is mathematically inconsistent (if d ≪ D, d cannot be in O(D²)). The intended conclusion (overall complexity O(b²D)) may still be correct, but the reasoning is garbled. This could be a parser artifact, but as presented it is confusing.

### Trivial
- The Hessian in Eq. 2 is presented in matrix form without clarifying the tensor structure for vector-valued g (normal space dimension D−d). While this notation is standard in manifold learning papers, a brief clarification would improve readability.

## Nice-to-Haves

- A synthetic experiment with known ground-truth function in higher dimensions with controlled noise would directly validate whether CEMS recovers the true function better than baselines.
- A sensitivity study varying k, σ, and d on one or two datasets would help establish the method's robustness.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that the method's core premise is "conceptually unsupported" because regression data with noise does not lie on a low-dimensional manifold.** The manifold hypothesis assumes data lies *near* (not exactly on) a low-dimensional manifold — this is standard and widely accepted in machine learning (Goodfellow, 2016; Belkin & Niyogi, 2003). The paper explicitly operates under this hypothesis. This criticism reflects a misunderstanding of the manifold hypothesis rather than a flaw in the paper.

- **Claim that the observed improvements "might stem from generic regularization effects (e.g., adding noise to inputs) rather than from correctly modeling manifold curvature."** This is speculation unsupported by evidence. CEMS is compared to FOMA (which also operates in tangent space) and outperforms it, suggesting curvature information specifically — not just noise injection — drives improvements.

- **Criticism that the paper does not verify gradient flow through SVD and linear solve.** CEMS uses differentiable SVD (Ionescu et al., 2015) and differentiable least squares, both standard differentiable operations available in PyTorch autograd. Verifying gradient flow through these is not standard practice.

- **Criticism that Eq. 9 is "referenced but not shown in main text."** This is standard for papers with appendices — the equation is defined in Appendix A, which was stripped by the parser. The main text provides a clear description of its construction.

- **Criticism that Ψ and G are "underspecified" and defined only by reference to Eq. 9.** The paper states these contain "{uⱼ}ⱼ₌₁ᵏ and {g(uⱼ)}ⱼ₌₁ᵏ" respectively (line 92), which is sufficient for a main-text description with details deferred to the appendix.

- **"No confidence intervals or significance tests are reported anywhere"** — the paper states standard deviations are in Appendix H (which the parser stripped). Three-seed evaluation is standard in this benchmark line of work (Yao et al., 2022).

- **Criticism that the R metric for DTI/Poverty "is not standard; its relationship to RMSE and its interpretation should be explained"** — R (Pearson correlation) is a standard regression metric in the ML community. The paper clearly states "higher values are preferred" for R.

- **Various formatting nitpicks** (e.g., about the complexity analysis typography, presentation style) — these are parser artifacts or minor issues that do not affect the paper's substance.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself fails to articulate about its own work.

## Suggestions

1. **Add a sensitivity analysis** showing how RMSE varies with k (neighborhood size), σ (noise scale), and estimated d (intrinsic dimension) on at least one dataset (e.g., Airfoil or NO2). This would address the most significant empirical gap and help establish the method's robustness.

2. **Tone down the "fundamental theory" claim** in the abstract and contributions. Present Theorem 4.1 as what it is — a standard Taylor error bound that motivates why second-order approximations can be better — rather than as a novel theoretical contribution. Acknowledge explicitly that the theorem bounds approximation error of the expansion itself, not the additional estimation error from finite-sample Hessian estimation.

3. **Include a direct diagnostic** (e.g., for a low-dimensional real dataset or a synthetic noisy dataset with known ground truth) showing that CEMS-generated points better approximate the true regression function than FOMA-generated or naively noised points.

4. **Report wall-clock time per epoch or per-batch** for CEMS vs. baselines on at least one large dataset (e.g., RCFashionMNIST or PovertyMap) to substantiate the "mild computational overhead" claim.

5. **Fix the complexity analysis statement** at line 102: "d ≪ D therefore d ∈ O(D²)" is mathematically inconsistent and should be corrected.

## Score and Decision

Based on an assessment of originality (reasonable — first second-order approach for regression DA), importance of the research question (moderately important — DA for regression is underexplored), support for claims (moderate — claims are partially supported but would benefit from additional analysis), soundness of experiments (adequate — extensive but lacking sensitivity analysis and significance testing), clarity of writing (good — clear motivation and method description), and value to the community (moderate — useful contribution but incremental):

The paper makes a genuine contribution as a principled extension of first-order manifold sampling to second-order, with clean design and consistent empirical validation across diverse datasets. However, the theoretical novelty is overstated, the empirical gains are modest and unsupported by statistical testing, and key sensitivity analyses are missing. These issues are addressable but weaken the paper in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>