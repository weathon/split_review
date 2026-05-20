Now I have everything I need. Let me write the consolidated review.

## Summary

This paper tackles Geodesic Principal Component Analysis (GPCA) in Wasserstein space, proposing two algorithms: (1) an exact method for centered Gaussians via a lift to GL\_d using Bures-Wasserstein geometry, and (2) GPCAGEN, a neural-network-based method for general absolutely continuous measures using Otto's fiber bundle. The Gaussian algorithm is theoretically well-grounded (Propositions 3–5), and GPCAGEN offers a novel parameterization of geodesics via MLPs that avoids input-convex neural networks. The paper provides theoretical quantification of TPCA distortion (Proposition 4) and shows interpretable results on 3D point clouds and images.

## Strengths

1. **Exact GPCA for Gaussians without linearization.** Proposition 3 (Section 3) formulates the GPCA problem as a lifted minimization in GL\_d using Bures-Wasserstein geometry, guaranteeing that recovered components are true geodesics rather than tangent-space approximations. The theoretical development is sound and fills a genuine gap in the literature.

2. **GPCAGEN: neural-network parameterization for general measures.** Algorithm 1 and the associated parameterization of geodesics via MLPs for φ and f (equations 15–17) enable GPCA on arbitrary absolutely continuous distributions without input-convex networks. Using Otto's parameterization to avoid convexity constraints is a clever practical contribution, and the method is validated on real-world 3D point clouds (ModelNet40) and landscape images.

3. **Quantification of TPCA distortion.** Proposition 4 provides an explicit formula for the ratio of true to linearized Bures-Wasserstein distance when covariances share eigenvalues but differ in orientation. This analytical result clarifies when curvature-induced error becomes significant, directly supporting the motivation for exact GPCA.

4. **Theoretical consistency for univariate Gaussians.** Proposition 5 proves that the first GPCA component of univariate Gaussians stays in the Gaussian submanifold, showing the restriction to Gaussians does not discard relevant structure in dimension 1.

5. **Empirical demonstration of GPCA vs. TPCA divergence.** Figure 4 shows a concrete setting (equal eigenvalues, varying orientation) where GPCA improves the cost by up to ~35% over TPCA, illustrating that curvature effects the linearized method misses.

## Weaknesses

### Fatal

None.

### Major

1. **Overstated "exact" claim for GPCAGEN.** The paper states (contributions, page 1) that both methods solve "the exact GPCA problem" and are "exact in the sense that they do not rely on a linearization of the Wasserstein space, and the components are true geodesics that minimize the cost in equation 1." For GPCAGEN, this is misleading: geodesics are parameterized by MLPs (restricting the function class), the objective uses Sinkhorn divergence S\_ε (an approximation to W₂², not W₂² itself), and optimization is stochastic and non-convex. The algorithm does not solve the exact problem (1); it finds an approximate solution within a restricted function class using an approximate cost. This overclaim runs through the abstract, introduction, and discussion. The Gaussian algorithm deserves the "exact" label if interpreted as a problem formulation (not guaranteed global optimality), but the two cases should be sharply distinguished.

2. **Thin experimental evidence that GPCAGEN is practically superior to simpler baselines.** For the Gaussian case, the paper honestly reports that GPCA and TPCA generically differ by less than 1% in cost, and the setting where they differ significantly (equal eigenvalues) is near-degenerate and the paper notes GPCA can yield "undesirable effects... yielding a poor separation." For GPCAGEN on general measures, the only comparison to TPCA is qualitative (mentioning that TPCA produces artifacts on discrete point clouds, Figure 16 in the appendix). No quantitative metric (reconstruction error, explained variance, or downstream task performance) is offered. The paper dismisses a direct numerical comparison as "not meaningful" because the methods operate on different representations, but this is precisely the evidence needed to justify the method's practical value. Without it, the reader cannot assess whether GPCAGEN's increased complexity is warranted.

3. **Missing TPCA comparison on the weather dataset (Gaussian case).** The weather dataset experiment (Section 5.1) shows GPCA results alone with no TPCA baseline. Since this is a real-data Gaussian example, it would be natural to compare both methods and see whether the <1% typical gap holds or whether meaningful differences emerge.

### Minor

4. **No sensitivity analysis for regularization coefficients λ\_I, λ\_O.** The paper sets λ\_I = λ\_O = 1.0 in all experiments, stating this "ensures the algorithm works as expected" (page 8), but provides no ablation. Since the orthogonality and intersection terms compete with the reconstruction loss, sensitivity to these hyperparameters is important for understanding the method's robustness. Details are deferred to the (stripped) appendix, but a brief main-text analysis would strengthen the paper.

5. **No discussion of Sinkhorn entropy parameter ε.** The paper uses Sinkhorn divergence S\_ε as a differentiable proxy for W₂² but does not discuss how ε is chosen, whether it is annealed, or how the approximation error affects the recovered components. For small ε, gradients can be ill-conditioned, and S\_ε is not a metric for finite ε—these limitations should be acknowledged.

6. **The second-component intersection condition is enforced in Diff(Ω) rather than Prob(Ω).** The paper acknowledges this (page 6): enforcing ξ₁(t¹_inter) = ξ₂(t²_inter) in Diff(Ω) is a stricter condition than requiring the projected geodesics to intersect in Prob(Ω), since it forces the representatives to coincide. The computationally cheaper alternative (setting R\* = Id) is a reasonable design choice, but its impact on the recovered components is not analyzed. A synthetic experiment testing whether this biases the second component would be helpful.

7. **t\_min/t\_max estimation is a heuristic.** The bounds are estimated by evaluating Hessian eigenvalues on a finite batch of samples (Algorithm 1, line 5). This does not guarantee the interval is correct for all x, and the paper does not discuss potential failure modes where a point outside the batch violates the positive-definiteness condition during sampling.

8. **No variance reporting for GPCAGEN experiments.** Given the stochastic training (random batches, random initializations, different seeds), reporting results across multiple runs would help assess stability.

### Trivial

None.

## Nice-to-Haves

- A quantitative comparison between GPCAGEN and TPCA on at least one real dataset (even requiring discretizing the GPCAGEN geodesics or interpolating the TPCA components) would substantially strengthen the paper's claims.
- An ablation study restricting f to a simpler parametric form (e.g., quadratic) in GPCAGEN would clarify whether the MLP parameterization is necessary.
- A discussion of computational cost and scaling (training time, memory) for GPCAGEN would aid practical adoption.

## Removed Points

- **Missing optimization details for Gaussian GPCA (Q\_i ∈ SO\_d).** The harsh critic noted that the main text does not specify the optimizer, initialization, or whether alternation is used. These implementation details reside in the appendix (Section D.2), which was stripped by the parser. Per the rules, criticism about missing appendix content is removed.
- **MNIST experiment is synthetic/does not test optimality.** The paper explicitly frames this as "a preliminary experiment on a synthetic dataset with known geodesics to verify that our algorithm... accurately recovers the two first principal components." This is a verification experiment, not a claim of optimality on real data. The criticism misunderstands the experiment's purpose.
- **Several formatting/style nitpicks and grammar complaints.** Removed per the hard formatting rule.
- **Missing related works.** Per the rules, I cannot verify the existence or absence of references.

## Novel Insights

The reviews reveal an interesting tension in the paper's framing: the Gaussian GPCA method is theoretically exact and well-supported, yet its own experiments show it rarely improves over the simpler TPCA in practice. Meanwhile, GPCAGEN (the more broadly applicable method) is the one that relies on approximations, making the "exact" label misplaced. This suggests the paper's genuine contribution is less about practical superiority over TPCA and more about providing a principled, non-linearized formulation of GPCA that becomes necessary in high-curvature regimes—a narrower but defensible contribution. The Otto-parameterization for general measures (avoiding ICNNs) is the paper's strongest practical innovation, but its value would be clearer with direct quantitative comparison against alternatives.

## Suggestions

1. Sharply distinguish the Gaussian method as "exact in formulation" from GPCAGEN as "approximate, using a differentiable Sinkhorn proxy and neural network parameterization." Rephrase the abstract and contributions accordingly.
2. Add at least one quantitative comparison between GPCAGEN and TPCA on a real dataset. Even a simple metric like reconstruction error (sum of squared W₂ distances to the learned geodesic) on held-out data for the point cloud experiment would significantly strengthen the paper.
3. Include a brief sensitivity analysis for λ\_I, λ\_O and the Sinkhorn parameter ε in the main text or supplement.
4. Report variance across random seeds for the GPCAGEN experiments.

## Score and Decision

**Round 1 — Bracketing:** The bracketing pass placed the paper in the 3.5–7.5 band (middle anchors). The weak anchors (avg 1.5–3.33) were clearly worse — papers with fatal flaws or very weak experiments. The strong anchors (avg 8.0–8.5) were clearly better — polished papers with strong theory and extensive experiments.

**Round 2 — Narrowing:** Within the (3.5, 7.5) bracket, I retrieved anchors in the 4.5–6.5 range. The most comparable anchors were:
- **SPD Cholesky Metrics** (5S8ruWKe8l.md, avg 5.00, Accept): solid theory with limited baselines and no ablation for key parameters — similar profile to the paper under review.
- **Neural OT Solver** (FJTdyG8jeJ.md, avg 5.00, Accept): theory-heavy with limited (low-dimensional synthetic) experiments — comparable to the paper under review.
- **RISWIE** (JQ0SIA2IA1.md, avg 5.33, Reject): had a central invariance robustness issue that the paper under review does not share.
- **Contact Wasserstein Geodesics** (IaEohEBUgi.md, avg 6.00, Accept): stronger experimental validation across diverse tasks — the paper under review is weaker than this anchor.
- **Mixed-Curvature Tree-Sliced Wasserstein** (e439wJl5sT.md, avg 6.00, Accept): stronger theoretical and experimental package.

The paper under review is most comparable to the SPD Cholesky paper (5.00) and the Neural OT paper (5.00) — both accepted despite experimental limitations — but the overclaim about "exactness" for GPCAGEN is a clearer issue than either of those papers faced. The theoretical contribution is genuine and the method is novel, but the experimental validation does not match the strength of the claims. The paper is clearly above the 3.2–4.5 range (weakly executed papers with fatal flaws) but below the 6.0 range (papers with stronger experimental packages). I place it at **5.0**.

**Calibration anchors summary:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| xCYFRyGI38.md | 3.33 | R1 | Weaker — withdrawn paper, lower quality |
| L0DTflYss0.md | 1.50 | R1 | Much weaker — fatal flaws |
| NshBOtWeK4.md | 3.20 | R1 | Weaker — weak experiments, unclear contributions |
| KAJ9JUCafc.md | 3.33 | R1 | Weaker — less relevant subfield |
| mlRWnMN6vE.md | 4.50 | R1 | Slightly weaker — fatal privacy flaw |
| 5S8ruWKe8l.md | 5.00 | R1/R2 | Similar — comparable theory/experiment gap |
| 4sDszSYKP6.md | 4.00 | R1 | Weaker — more theoretical, less applied contribution |
| NlnDselrtl.md | 6.00 | R1 | Stronger — more polished experiments |
| 248ysaRatx.md | 8.00 | R1 | Much stronger — different subfield |
| nCsF3Bsn2n.md | 8.00 | R1 | Much stronger — different subfield |
| VaS6xcDrTb.md | 8.50 | R1 | Much stronger — different subfield |
| Ahdsg2nkNH.md | 8.00 | R1 | Much stronger — different subfield |
| e439wJl5sT.md | 6.00 | R2 | Stronger — better experiments and theory |
| oyxExc7TEl.md | 5.60 | R2 | Slightly stronger — better evaluation |
| JQ0SIA2IA1.md | 5.33 | R2 | Comparable — but had central robustness flaw |
| FJTdyG8jeJ.md | 5.00 | R2 | Comparable — theory-heavy, experiments light |
| IaEohEBUgi.md | 6.00 | R2 | Stronger — better experiments |
| Og1klGbvlM.md | 5.60 | R2 | Slightly stronger — better experiments |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>