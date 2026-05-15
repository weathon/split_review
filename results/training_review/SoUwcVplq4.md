I have thoroughly read the paper. Let me now produce the final consolidated review.

---

## Summary

This paper proposes ComPC, a test-time point cloud completion framework that leverages 2D diffusion priors via 3D Gaussian Splatting (3DGS) without any training requirement. The pipeline consists of three stages: Partial Gaussian Initialization (PGI) to render a reference image from the partial point cloud; Zero-shot Fractal Completion (ZFC) which optimizes newly initialized 3D Gaussians guided by Zero-1-to-3's SDS loss conditioned on the reference image, while preserving observed geometry via a Preservation Constraint; and Point Cloud Extraction (PCE) which extracts surface points from Gaussian centers and resamples them uniformly via Grid Pulling. The key claimed advantages are eliminating the need for manual text prompts (required by SDS-Complete) and reducing completion time from ~1000+ minutes to ~15 minutes per object.

## Strengths

1. **Novel and well-motivated pipeline**: Combining 3D Gaussian Splatting with image-conditioned 2D diffusion priors (Zero-1-to-3) for point cloud completion is original. The paper replaces the slow NeRF-based optimization of SDS-Complete with 3DGS rendering and replaces text prompts with a rendered reference image, both of which are clearly motivated (Section 2.2, lines 36–37).

2. **Dramatic efficiency improvement**: The reported 15-minute completion time on Redwood (RTX A6000) versus up to 1,950 minutes for SDS-Complete (Section 5, line 230) represents a >100× speedup, making test-time completion practically viable.

3. **Elimination of manual text prompts**: Unlike SDS-Complete, the method uses the partial point cloud itself to render a reference image that conditions the diffusion model, removing the need for per-object text descriptions (Section 2.2, line 36). This is a meaningful practical advantage.

4. **Consistent quantitative advantage on Redwood (in-domain and out-domain)**: Table 2 shows the method outperforms all supervised baselines as well as SDS-Complete on both in-domain categories (where supervised methods are expected to be strongest) and out-domain categories, supporting claims of cross-category generalization.

5. **Ablation coverage of core components**: The paper provides ablations for colorization strategies (Table 3), and for ZFC/PCE components including Preservation Constraint, Gaussian Surface Extraction, and Grid Pulling (Table 4, Fig. 8), with both quantitative and qualitative evidence.

## Weaknesses

### Fatal

None.

### Major

- **Synthetic evaluation lacks reproducibility specifications**: The synthetic test data is assembled from non-standard sources (Krishnamurthy & Levoy 1996; DeCarlo et al. 2003; Praun et al. 2000; Lipman et al. 2008) but the paper does not specify the number of test objects, the partiality protocol, how the partial point clouds are generated, or benchmark splits (Section 4, line 177). This makes it impossible for others to reproduce the synthetic results or compare against them. The paper follows SDS-Complete's data selection approach but does not report the exact composition.

- **Grid Pulling's trade-off is acknowledged but not justified**: The ablation (Table 4, and Section 4.4, line 223) shows that Grid Pulling improves EMD substantially but also *degrades* CD ("CD metric experiences a slight decline due to precision loss"). Since the final metric comparisons (Tables 1–2) include Grid Pulling, the reader cannot tell whether the reported advantage over baselines comes from the diffusion-guided optimization or from this learned post-processing. The paper does not justify why EMD improvement is worth the CD degradation, or report metrics without GP on the main comparison tables.

- **Reference viewpoint estimation is foundational but unablated**: The method searches 5,000 camera poses to find the reference viewpoint (Section 3.1, line 60), yet there is no analysis of (a) how many poses suffice for stable results, (b) sensitivity to incorrect viewpoint estimates, or (c) comparison to simpler heuristics. Since the entire completion pipeline depends on this single reference view, its robustness should be characterized.

### Minor

- **Results are averaged over 3 runs but no variance is reported** (Section 4, line 179): Given the method involves stochastic initialization and SDS noise, error bars or standard deviations would strengthen the reliability of the claimed improvements.

- **SDS-Complete comparison is only on Redwood, not on synthetic data** (Section 4, line 179): The paper explains that SDS-Complete only provides code for Redwood processing, which is a practical limitation. However, this means the claim of "outperforms... test-time approaches" on synthetic data rests solely on comparisons with supervised methods (which are at an inherent disadvantage on unseen data distributions).

- **Several design choices are not ablated**: The opacity binarization (Eq. 2) and the single shared scalar scale for Gaussians (Section 3.2) are introduced as modifications to standard 3DGS but their individual contributions are not quantified. The weighting factors \(w_0, w_1, w_2, w_3\) are mentioned but their specific values are not reported.

### Trivial

- The sentence about ShapeNet/KITTI comparisons is truncated due to a parser artifact (line 177–178). This does not affect the paper's content.

## Nice-to-Haves

- A comparison on a standard point cloud completion benchmark (e.g., ShapeNet-55/34 or Completion3D) would help contextualize absolute quality, even if only on a subset, though the paper explains why full-benchmark evaluation is impractical for test-time methods.
- Analysis of failure cases (e.g., thin structures, symmetric objects, heavily occluded scenes) would be valuable — the paper references supplementary material for this.
- Integration with a more recent view-consistent diffusion model (e.g., MVDream, Stable Zero123) is a natural extension that could further improve quality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Supervised methods evaluated OOD is unfair"**: The harsh critic argues that supervised methods are at a disadvantage on unseen domains. However, the paper's central claim is about *generalization*, and evaluating on unseen domains is precisely the correct test for that claim. Moreover, the Redwood "in-domain" results (Table 2) show the method winning even on categories similar to supervised methods' training data. This criticism misunderstands the paper's contribution.

- **"Grid Pulling may overfit to local density patterns"**: Speculative claim not grounded in any evidence from the paper. Removed as not substantiated.

- **"Missing appendix/failure cases"**: The paper references supplementary material for failure cases (Section 5). As per instructions, appendix content is not available in the parsed file. Removed.

- **"Missing related works (SparseDiff, OccInpainting)"**: Rule prohibits mentioning missing related works.

- **"The opaque binarization trick (Eq. 2) could cause rendering artifacts"**: Speculative and not supported by any evidence in the paper or reviews — no experiment or observation backs this up. Removed.

- **"No diffusion prior for the Preservation Constraint weighting"**: The critic questions the weighting factor \(w_2\) but this is a standard loss balancing weight; many papers do not report every weight value. Moved here per Rule 7 on undisclosed hyperparameter nitpicks.

- **Strength Finder strengths about "generalization across unseen categories" and "normal-map colorization superiority"**: These are kept as they are well-supported by paper evidence (Table 2, Table 3).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the synthetic evaluation protocol in detail**: Report the number of test objects per category, the partiality generation method, and the complete list of object sources with splits, so the synthetic results are reproducible.
2. **Report metrics without Grid Pulling in the main comparison tables** (Tables 1–2), alongside the full method, so the reader can attribute the improvement to the diffusion-guided optimization versus the post-processing step.
3. **Add an ablation for the viewpoint estimation**: Compare performance with different numbers of camera poses (e.g., 100, 500, 5000) and a random-viewpoint baseline, to validate the robustness of this critical step.
4. **Include standard deviations** on all quantitative results, given the stochastic nature of the method.
5. **Report the numeric values of all loss weighting factors** (\(w_0, w_1, w_2, w_3\)) and the noise scale \(\sigma_n\) for reproducibility.

## Score and Decision

The paper presents a genuinely novel and well-motivated pipeline with a dramatic practical speedup over the only prior test-time method. The core contribution is real and the experimental evidence is broadly supportive, though the synthetic evaluation is under-specified and the Grid Pulling trade-off conflates the source of improvement. These issues are addressable but as presented, the evidence is stronger for the method's generalization and efficiency than for its absolute superiority over all baselines.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>