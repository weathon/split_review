Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a geometry-aware adaptive mapping function for unbounded NeRF scenes. The key idea is to use a $p$-norm distance metric to define a manifold whose shape can be adjusted per scene, replacing the fixed cylinder/paraboloid shapes of prior inverted-sphere and contract mappings. The paper also introduces an angular ray parameterization to correct sampling bias in the distorted embedding space. The method is integrated into four NeRF frameworks (DVGO, TensoRF, iNGP, NeRF) and evaluated on three datasets, showing consistent improvements especially when cameras are far from the scene origin.

## Strengths

1. **Novel adaptive mapping via $p$-norm (Sections 4.3, Fig. 1).** The idea of parameterizing the mapping manifold with a $p$-norm distance — enabling scene-dependent shape adjustment — is a genuine generalization of the fixed contract ($p=2$) and inverted-sphere mappings. This directly addresses a real limitation: fixed mappings allocate capacity in the same way regardless of scene geometry.

2. **Angular ray parameterization (Section 4.4, Fig. 4).** The $\theta/\theta_{\max}$ parameterization correctly identifies and addresses a sampling bias that arises when ray origins are far from the scene origin. The toy example in Fig. 4 clearly demonstrates that uniform sampling in normalized-distance space produces uneven coverage, while angular sampling mitigates this.

3. **Consistent empirical improvement across diverse backbones (Table 1).** The method is tested in four different NeRF frameworks spanning MLP-based (NeRF) and voxel-based (DVGO, TensoRF, iNGP) architectures. In the challenging $\times2$ camera-offset scenarios, the improvement over contract mapping is substantial and consistent, with the method often succeeding where the baseline collapses (especially in iNGP).

4. **Automatic $p$ selection from scene point clouds (Section 4.3).** Using the existing COLMAP point cloud to determine $p$ via a RANSAC-like procedure is a practical contribution that makes the method usable without per-scene manual tuning. The approach of maximizing spread in the embedding space is well-motivated.

5. **Geometric unification of existing mappings (Section 4.1, Fig. 2).** The stereographic-projection framework provides a clean conceptual lens for understanding why different mappings produce different manifold shapes (cylinder, paraboloid) and why fixed shapes have limited capacity. This analysis motivates the need for adaptive shape.

## Weaknesses

### Fatal
None.

### Major

1. **The $p$-norm mapping function is not fully specified with a precise vector equation.** Section 4.3 defines the manifold as $X_m = \{ \mathbf{x}_m \mid \|\mathbf{x}_m - Q\|_p = 1 \}$ and states that $m = 1/\|\mathbf{x} - Q\|_p$, but the actual mapping from a 3D unbounded coordinate to a bounded coordinate vector is given only as the garbled "xb = ∥x−Q∥p" — which reads as a scalar, not a vector mapping. Unlike Eqs. 2 and 3 which provide complete, closed-form piecewise functions for the inverted-sphere and contract mappings, the paper's core contribution lacks an explicit equation showing exactly how $\mathbf{x}_b$ is computed from $\mathbf{x}$ (including the inner/outer region handling analogous to the piecewise definitions in existing mappings). While the conceptual idea is communicated, a reader cannot precisely reproduce the mapping from the main text. This is the paper's central technical contribution and must be specified unambiguously.

### Minor

1. **The "state-of-the-art" claim is broader than the evidence supports.** The abstract and conclusion claim SOTA results, but the experimental comparison is against contract mapping (and NeRF+/F2-NeRF) embedded in simplified frameworks — not against the full published mip-NeRF 360 or Zip-NeRF pipelines with their complete multiscale representations, proposal sampling, and distortion loss. A controlled comparison of mapping functions within the same framework is valid and useful, but it supports a claim of "our mapping improves over contract mapping in these frameworks" rather than "state-of-the-art" against all published methods. The paper should either include published numbers from mip-NeRF 360 and Zip-NeRF on the same datasets, or temper the claim.

2. **Ablation study limited to a single scene (Table 2).** The component analysis (mapping function, angular parameterization, automatic $p$) is performed on only the bicycle scene from MIP-360. While the results are informative, a multi-scene ablation would better demonstrate the generalizability of each component's contribution.

3. **RANSAC-based $p$ selection procedure is not validated.** The automatic $p$ selection is described but never compared against alternatives (e.g., grid search over validation views, or fixed $p$ values). It is unclear whether the chosen $p$ is near-optimal or whether the procedure is stable across different COLMAP point clouds (noise levels, point densities). A sensitivity analysis of $p$ vs. final PSNR would strengthen the claim.

4. **Free Dataset results incomplete.** The Free Dataset results (Table 1, Fig. 7) are reported only for the $\times1$ case. Showing the $\times2$ case for this dataset would complete the picture, especially since the method's advantage is most pronounced for far-offset cameras.

### Trivial
None.

## Nice-to-Haves

- A sensitivity sweep over camera distance multipliers (e.g., 1.5×, 3×) to characterize how the method's advantage grows or saturates.
- A discussion of how $Q$ (the projection center) is chosen and whether it could be learned or adapted per scene.
- A comparison of the angular parameterization against uniform sampling in $p$-norm distance space as an even simpler baseline.

## Removed Points

These points from the input reviews were considered and removed, with justification:

1. **"Section 4.2 is missing / derivation absent"** — The paper references Section 4.2, which is not visible in the parsed text. Per instructions, parser-stripped content is not penalized as an author error. The geometric analysis in Section 4.1, while qualitative, does communicate the conceptual framework. Removed as unverifiable from parsed output.

2. **"Evaluation is biased because camera repositioning favors proposed method"** — The paper explicitly tests this scenario as its target use case. Contract mapping was tested under the same conditions; this is a controlled experiment, not bias. Removed (misunderstands experimental design).

3. **"Missing confidence intervals / variance"** — Single-run evaluation is standard practice for NeRF benchmarks. This is a generic methodological demand not specific to the paper's flaws. Removed.

4. **"Missing related work on adaptive strategies / space subdivision"** — Hard rule: do not cite missing related works without external sources. Removed.

5. **"Reproducibility details minimal / hyperparameters not disclosed"** — The paper states it follows existing configurations and specifies sample doubling. This is standard for the field. Removed per hard rules on reproducibility nitpicks.

6. **"Not yet released code / model"** — Hard rule: remove criticisms questioning existence or availability of cited entities. Removed.

7. **Various formatting nitpicks and parser-artifact complaints** — Removed per hard rules.

## Novel Insights

The harsh critic's observation that the paper's core mapping equation is incompletely specified is a genuine concern that goes beyond a typical "more details needed" comment — it is specifically that the paper defines a manifold (a set) but never gives the vector-valued mapping function that transforms unbounded coordinates into bounded coordinates, which is what implementers actually need. This is a distinct issue from missing supplementary materials. The strength finder correctly identifies that the empirical comparisons across four frameworks are the paper's strongest evidence, but it overstates the ablation's conclusiveness given the single-scene limitation.

## Suggestions

1. **Provide a complete, closed-form equation for the $p$-norm mapping** in a form comparable to Eqs. 2 and 3, including the piecewise definition for inner vs. outer regions and demonstrating that it reduces to the contract mapping when $p=2$ and $Q=0$.

2. **Add published mip-NeRF 360 and Zip-NeRF numbers** to Table 1 for the MIP-360 dataset, or reframe the "SOTA" claim to accurately reflect the comparison scope.

3. **Extend the ablation to at least 2–3 scenes** and include a sensitivity plot of PSNR vs. $p$ to validate the RANSAC procedure.

4. **Report Free Dataset $\times2$ results** and consider adding a camera-distance sweep.

**Evaluation axes:**
- **Originality:** Good — the $p$-norm adaptive mapping is a novel generalization of existing fixed mappings.
- **Importance of question:** High — unbounded scene representation is a key challenge in NeRF research.
- **Claims supported:** Partially — the improvement over contract mapping in the same frameworks is well-supported, but the SOTA label and full derivation are not.
- **Soundness of experiments:** Moderate — the controlled comparison is well-designed but the single-scene ablation and unvalidated $p$ selection weaken it.
- **Clarity of writing:** Moderate — the conceptual exposition is clear, but the central equation is not specified.
- **Value to community:** Moderate to high — a practical, plug-in mapping improvement that works across frameworks would be useful.

## Score and Decision

Based on the review: the paper has a genuine contribution (adaptive $p$-norm mapping with angular parameterization) and provides reasonable empirical support across four frameworks. The main weakness — incomplete specification of the core mapping equation — is serious but correctable; it does not invalidate the overall approach. The SOTA claim is overstated but the underlying comparison is valid. With revisions to clarify the mapping equation and modestly strengthen the evaluation, this paper would make a solid contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>