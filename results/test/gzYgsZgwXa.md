Now I have thoroughly cross-checked all claims against the paper. Let me construct the final consolidated review.

## Summary

This paper addresses the ambiguity of path choices in path-based attribution methods for DNN interpretability. It introduces the **Concentration Principle**, which formalizes the goal of producing concentrated (sparse, aesthetic) attributions by maximizing variance. To efficiently find a path satisfying this principle, the paper proposes **SAMP** (Salient Manipulation Path), a greedy algorithm that selects pixels for manipulation based on gradient projection, along with two auxiliary modules: Infinitesimal Constraint (IC) for maintaining completeness and Momentum Strategy (MS) for escaping local optima. Experiments on MNIST, CIFAR-10, and ImageNet show consistent improvements over 12 baselines on Deletion/Insertion metrics.

## Strengths

1. **Novel formulation of path selection as an optimizable criterion.** The Concentration Principle (Definition 1) is the first explicit criterion for preferring one path over another in path methods, directly addressing the long-standing "which path is better?" question. This is a clear conceptual contribution.

2. **Consistent and substantial quantitative improvements.** Table 1 shows SAMP/SAMP++ outperform all 12 baselines across nearly every Deletion/Insertion metric on three datasets. For example, on ImageNet, SAMP++ achieves Deletion 0.145 (best) vs. 0.167 (GuidedIG, next best) and Insertion 1.116 (best) vs. 0.898 (LIME, next best). The margin is particularly large on Insertion, where the next-best non-SAMP method (LIME) scores 0.898 versus SAMP++ at 1.116.

3. **Validation of auxiliary modules via ablation.** Table 2 demonstrates that MS alone improves SAMP's ImageNet Insertion from 0.984 to 1.088, and the combined SAMP++ (MS+IC) reaches 1.116. The Sensitivity-N check (Figure 4) confirms that IC systematically improves completeness (correlation with Δy), verifying its theoretical purpose even though it does not directly boost Deletion/Insertion scores.

4. **Theoretical insight linking random paths to linear output curves.** Remark 2 observes that the conditional expectation 𝔼(uₖ|u_d=C)=kC/d predicts linear output variation for randomly selected paths, and the paper empirically notes that IG, XRAI, and Grad-CAM produce nearly straight output curves (Figure 1). This consistency between theory and observation strengthens the paper's framing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The Brownian motion theoretical apparatus is overclaimed and adds little.** Assumption 1 treats the unconstrained allocation process as Brownian motion, but the actual algorithm is purely deterministic. The resulting propositions (conditional covariance is negative; attributions become nearly independent in high dimensions) are generic properties of sum-constrained independent increments and do not specifically require Brownian motion. The key algorithmic insight — greedily selecting pixels with the largest |gradient × residual| to maximize step-wise attribution magnitude — can be justified more directly and transparently without this machinery. The theoretical framing suggests a rigor that is not actually delivered.

2. **The primary evaluation (Deletion/Insertion) has partial alignment with the method's design.** SAMP's greedy selection criterion picks pixels whose manipulation produces the largest immediate output change (via first-order approximation). Deletion/Insertion then measures output change when removing/adding pixels in attribution order. These are not identical — SAMP computes a full path integral, not a single ranking — but there is a non-trivial degree of alignment. The paper mentions additional evaluations (μFidelity, pointing game) in the appendix but does not summarize them in the main text, which would have provided a more rounded evaluation. Including at least a brief summary of those results would strengthen confidence in the method.

3. **The momentum strategy's effect on formal guarantees is not discussed.** When MS is applied (line 271), the attribution uses a moving average of gradients (vg^k), not the gradient at the current point. This means SAMP++'s attributions no longer strictly correspond to a path integral of the model's actual gradients along the manipulation path, and the formal completeness/axiomatic guarantees of path methods hold only approximately. The paper does not discuss this trade-off or clarify which guarantees still hold.

4. **The step-size parameter *s* (pixels per step) is not systematically studied.** The paper fixes *s* per dataset (e.g., 224×16 for ImageNet, 10 for MNIST/CIFAR-10) but does not ablate its impact on either computational cost or attribution quality. Since *s* determines the granularity of the manipulation path and the number of forward passes, readers cannot assess the sensitivity of results to this choice.

5. **The Concentration Principle's use of variance is one of many possible concentration measures.** The paper asserts variance as the criterion (Definition 1) but does not discuss alternatives (Gini index, entropy, kurtosis, L1 sparsity) or justify why variance is preferable. While variance is a natural choice given the fixed-sum constraint (Remark 1), a brief discussion of alternatives and their trade-offs would strengthen the formulation.

### Trivial
- The paper could clarify whether the reported Deletion AUC values below 0 (e.g., MNIST Deletion of -0.137 for SAMP++) are meaningful relative to a theoretical floor.

## Nice-to-Haves
- A baseline that computes a single-step attribution by sorting pixels by |∇f(x⁰)⋅(x^T−x⁰)| at the baseline point would help isolate the benefit of the full path-integral computation over a one-shot first-order approximation.
- A table of wall-clock runtimes for SAMP/SAMP++ versus other methods (e.g., IG, GuidedIG, RISE) would help readers assess practical feasibility.
- An ablation of the parameter *s* (pixels per step) on a subset of ImageNet would clarify the sensitivity of results to this design choice.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"No comparison of computational cost"** (from harsh critic's "Missing Parts"): Re-framed into Nice-to-Haves above rather than a weakness, since the paper's primary contribution is methodological, not about efficiency, and the method's complexity is O(d) with d/s forward passes — which is already described.
- **"The choice of baseline is discussed only in a qualitative visualization"**: The paper actually includes an ablation on baseline choices (Section 4.4.2, lines 580-587) showing visual comparisons across four baseline types. The critic's claim is partially incorrect.
- **"The evaluation is insufficient to support the strong claims"** (from critic's Issue 1 framing as fatal): Downgraded from "insufficient" to "minor" because the paper does include additional evaluations (μFidelity, pointing game) in the appendix, and Deletion/Insertion is a standard evaluation protocol used by all compared methods. The alignment concern is valid but does not invalidate the strong empirical results.
- **Concentration Principle under-motivated criticism**: The paper does provide a rationale (Remark 1) with a concrete 3-feature example, and variance is a natural concentration measure for fixed-sum vectors. The critic's concern about negative Δy is academic — the paper's examples and evaluation cover the standard positive-Δy case.
- **Weakness about missing related works**: Removed per instructions; I cannot verify the existence of missing references.
- **"SAMP is almost identical to computing per-pixel scores via a first-order approximation"**: This misreads the method. SAMP recomputes gradients at each step along the path, producing a true path integral — not a single first-order approximation. The difference from IG is the *path shape*, not the path-integral computation itself.
- **Strength "strong theoretical grounding" from Strength Finder**: Removed because it conflicts with the verified weakness that the Brownian motion framework is overclaimed. The method is well-motivated algorithmically but the theoretical grounding is not as strong as claimed.

## Novel Insights

Beyond the paper's own contributions, the key tension the reviews surface is between **optimization-driven path design** and **axiomatic path methods**. SAMP shows that optimizing a secondary criterion (variance) over paths produces better-behaved attributions, but this optimization inherently relaxes the neutral, unbiased- prior that axioms like IG's symmetry impose. This suggests that the interpretability community may need to accept a trade-off: either strong axiomatic guarantees with potentially diffuse attributions (IG) or task-specific concentration with loosened guarantees (SAMP). The paper's hybrid approach — greedily optimizing while constraining step sizes to preserve approximate completeness — is a pragmatic compromise, but the field would benefit from a formal characterization of what is lost and gained when moving from "any path is valid" to "this particular path is better."

## Suggestions

1. **Replace or simplify the Brownian motion derivation** with a direct argument: the greedy selection maximizes each step's contribution to the variance objective, and the high-dimensional independence property follows from the diagonal dominance of the conditional covariance matrix. This would be cleaner and avoid questionable stochastic-process assumptions.

2. **Include a brief summary of the appendix's μFidelity and pointing game results** in the main text (even one sentence with the key numbers) to show that SAMP performs well on evaluations that do not directly mirror the greedy selection criterion.

3. **Add an ablation of the step-size parameter *s*** on a subset of ImageNet, showing how Deletion/Insertion and runtime vary with s.

4. **Clarify the impact of momentum on axiomatic guarantees** — specifically, whether SAMP++ still satisfies completeness (approximately or exactly) and whether the attributions still correspond to any well-defined path integral.

## Score and Decision

**Originality:** 7/10 — The Concentration Principle and its optimization over paths are novel, though the greedy algorithm itself follows naturally from the formulation.

**Importance of research question:** 8/10 — Resolving path-choice ambiguity in attribution methods is a well-recognized problem.

**Claims supported:** 7/10 — The main claim (SAMP produces better attributions on Deletion/Insertion) is well-supported, but the theoretical framing overclaims rigor.

**Soundness of experiments:** 7/10 — Strong on Deletion/Insertion with 12 baselines and three datasets, but overly reliant on one evaluation paradigm in the main text.

**Clarity of writing:** 7/10 — Generally clear but the Brownian motion section is harder to follow than necessary.

**Value to community:** 8/10 — The Concentration Principle and the SAMP algorithm are likely to influence future work on path-based attribution methods.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>