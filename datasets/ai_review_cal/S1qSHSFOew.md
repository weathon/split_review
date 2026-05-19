- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 8, 3
Now I have all the information needed to synthesize the review. Let me produce the final consolidated review.

## Summary

The paper proposes Critical Subset Identification (CSI), a framework to improve point cloud recognition robustness against data corruption. CSI has two components: Density-Aware Sampling (DAS), which selects anchor points based on local density rather than farthest-point or random sampling, and Self-Entropy Minimization (SEM), an auxiliary training objective that sharpens attention maps. Evaluated on ModelNet40-C and PointCloud-C, the method combined with PCT achieves error rates of 18.4% and 16.3%, outperforming all compared baselines.

## Strengths

- **DAS consistently improves over standard sampling strategies.** When combined with SEM, DAS (18.4% error) substantially outperforms farthest-point sampling (21.7%) and random sampling (19.6%) on ModelNet40-C (Table 4). The advantage holds across multiple base architectures including CurveNet and PointMLP (Table 5).

- **SEM yields consistent robustness gains across diverse architectures.** Applying SEM to point-level features (rather than global features) improves corruption error by +1.34% on average across PointNet, PointNet++, DGCNN, RSCNN, SimpleView, and CurveNet (Table 3). This demonstrates the method is architecture-agnostic, not tied to a single backbone.

- **Thorough and well-designed ablation studies.** The paper systematically ablates: number of SEM layers (Table 1), SEM loss weight λ (Table 1), alternative density definitions (ℓ₀ vs ℓ₁, ball query vs kNN) (Table 5), kNN parameter in DAS (Table 4), and different sampling strategies (Table 4). These experiments validate the design choices and show clear trends.

- **Clean accuracy is maintained while corruption robustness improves.** PCT+CSI achieves a clean error rate of 7.3% versus PCT's 7.1% — a negligible drop — while improving corruption error by 7.1 percentage points (Table 1). This practical trade-off is important for deployment.

## Weaknesses

### Fatal
None.

### Major

- **The claimed SOTA margin of 5.2% on ModelNet40-C is inconsistent with the paper's own Table 1.** The abstract and conclusion state improvement of 5.2% over "state-of-the-art methods." However, Table 1 shows CurveNet as the best non-CSI baseline at 22.7%, yielding an actual gap of 22.7 − 18.4 = 4.3%, not 5.2%. The 5.2% figure only obtains if comparing against the weaker PointNet++ (23.6%). This is a numerical inaccuracy in a headline claim that appears three times (abstract, introduction, conclusion). While the method genuinely achieves the best results in the table, the stated margin is inflated.

- **Comparisons against pre-training and augmentation methods mentioned in the paper are promised but not shown.** The paper states (Sec. 4.1, line 192): "we also compare with several pre-trained methods OcCo, Point-BERT, and data augmentation PointMixup, RSMix, PointWOLF, and WOLFMix. The result shows that augmentation works well combined with our proposed CSI." No table or numbers for these comparisons appear anywhere in the paper. This is a significant omission — the reader cannot verify the claimed compatibility or evaluate how CSI fares against these prominent approaches.

### Minor

- **No per-corruption breakdown is provided for the main results (Table 1).** The paper states "DAS can greatly help with noise and density corruption types" but only supports this with the augmentation Table 2, which covers a different setting (with PointCutMix-R). For a robustness paper, reporting only the macro-averaged error across 15+7 corruption types masks whether gains are concentrated on easy corruptions or whether any categories see degradation. A per-corruption (or at least per-category) table for the core CSI method is standard practice for these benchmarks and should be provided.

- **The temperature hyperparameter τ in the SEM loss (Eq. 3, line 94) is never reported.** Temperature critically controls the sharpness of the attention distribution and thus the strength of entropy minimization. Without this value, the experiments are not fully reproducible and the sensitivity of the method to this choice is unknown.

- **The claim that CSI identifies "critical subsets" of points is motivated but never directly validated.** The paper asserts that DAS selects "critical" points and SEM sharpens attention toward "critical" correspondences, but provides no direct evidence — such as ablation by removing the identified subset and measuring accuracy drop, comparison with human-annotated critical points, or saliency analysis. The mechanism remains a plausible narrative; the empirical contributions (improved error rates, thorough ablations) stand on their own but without supporting the specific "critical subset" framing.

### Trivial
None.

## Nice-to-Haves

- A per-corruption breakdown table for the main CSI results (Table 1) showing all 15/7 corruption types, ideally grouped by category (density, noise, transformation). This is standard practice for corruption benchmarks.
- An ablation of the τ temperature parameter (e.g., τ ∈ {0.5, 1.0, 2.0}) to show sensitivity.
- An experiment or visualization directly testing whether DAS-selected points and SEM-highlighted correspondences are indeed the most informative for classification (e.g., removing them and measuring accuracy drop).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"SOTA claim is not properly supported because PointASNL and Triangle-Net are excluded from experiments"** — These methods are mentioned in related work but were not evaluated on the ModelNet40-C/PointCloud-C benchmarks in their original publications. The paper's comparison scope (9 representative models retrained under a unified recipe) is standard and reasonable. The paper also notes specific limitations of these methods. This criticism overstates the omission.

- **"Statistical significance should be established"** — Single-run evaluation on these large-scale benchmarks is standard practice in the 3D point cloud robustness literature. Not a necessary addition.

- **"Missing comparison with robustness-specific methods"** — Same as the PointASNL/Triangle-Net point above. The paper explicitly benchmarks against the models evaluated on these benchmarks in the original benchmark papers.

- **Several generic strengths from the Strength Finder** — Removed because they are duplicative (e.g., "comprehensive ablation study" was merged into the concrete ablation strength above) or too generic to be meaningful standing alone.

- **"The comparison with data augmentation is incomplete — only PointCutMix-R tested"** — This is partially addressed below as a Major weakness (promised but missing comparisons with OcCo, Point-BERT, etc.). The specific complaint about only testing PointCutMix-R is valid but is subsumed by the larger issue of missing promised comparisons.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the claimed SOTA margin on ModelNet40-C to reflect the actual best baseline in Table 1 (CurveNet at 22.7%, yielding ~4.3% improvement), or explain what baseline yields 5.2% if it is not shown in the table.
2. Add a supplementary table reporting the per-corruption and per-category breakdown for the main CSI results (Table 1), so readers can assess which corruption types drive the gains.
3. Report the τ value used in SEM, and ideally include a brief ablation.
4. Either provide the promised comparison tables for OcCo, Point-BERT, etc., or remove the unsupported claim about those comparisons.
5. Consider adding a direct validation of the "critical subset" narrative, e.g., a visualization of attention maps before/after SEM, or an ablation that removes DAS-selected points to measure accuracy drop.
