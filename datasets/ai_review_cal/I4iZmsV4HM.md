- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8
Now I have a thorough understanding of the paper. Let me also verify the precise wording of the "overstated claim" criticism against the paper text.

The paper's abstract says: "ConcreTizer concretely restores the original 3D point cloud scene." Section 4.3.1 says: "by using the center coordinates of the voxel, we achieve effective restoration within an error range constrained by the voxel size." The paper is transparent about the limitation. The claim is about restoration at voxel resolution, which is appropriate for a method that explicitly converts regression to occupancy classification.

Now let me assemble the final consolidated review.

## Summary
This paper proposes ConcreTizer, the first in-depth study of model inversion attacks on voxel-based 3D point cloud feature extractors. It identifies two key challenges: (1) the semantic ambiguity of zero-padded voxels under regression-based inversion, and (2) the dispersion of non-empty voxels (VoI) through deep layers. The paper addresses these via Voxel Occupancy Classification (VOC), which converts coordinate regression to binary occupancy classification, and Dispersion-Controlled Supervision (DCS), which partitions the feature extractor at downsampling layers to prevent VoI spread. Experiments on KITTI and Waymo with two backbone architectures show large and consistent improvements over a regression baseline and an adapted generative model.

## Strengths

**Core strengths:**

1. **Insightful problem diagnosis (Section 3).** The paper provides a clear, well-illustrated analysis of why prior point-regression attacks fail on voxel-based 3D feature extractors. It identifies two interconnected mechanisms: the semantic ambiguity of zero-padded voxels under MSE regression (which conflates empty voxels with points at the origin), and the VoI dispersion phenomenon where non-empty voxel signals spread into empty regions during downsampling (quantified in Figure 3, right). This analysis directly motivates the paper's design choices.

2. **VOC is a principled solution to the regression ambiguity (Section 4.3.1).** Converting coordinate regression to binary occupancy classification eliminates the fundamental ambiguity that doomed prior approaches. The ablation study (Figure 7) confirms that VOC alone enables meaningful restoration from the 6th layer, while the conventional regression baseline fails completely at all depths (Table 1).

3. **DCS directly addresses VoI dispersion (Section 4.3.2).** Partitioning the feature extractor at downsampling layers and applying intermediate occupancy masking prevents error accumulation from VoI spread. Figure 7 shows that ConcreTizer (VOC + DCS) restores a distribution much closer to the original than VOC alone at the 12th layer. Figure 8 confirms that the optimal number of DCS instances (2–4) aligns with downsampling layers where VoI dispersion peaks, while excessive partitioning (DCS 10) degrades performance — validating the causal logic.

**Supporting strengths:**

4. **Consistent improvement across datasets and backbones.** Table 1 reports ConcreTizer outperforms both baselines on KITTI and Waymo at all layer depths. At the deepest layer, ConcreTizer improves CD by 23.4% and F1 by 12.4% over UltraLiDAR on KITTI. Figure 6 extends this to the VoxelResBackbone architecture.

5. **Restored scenes retain task-level utility.** Table 2 shows that 3D object detectors trained on ConcreTizer-restored scenes achieve 75.4–86.7% of original detection AP on KITTI and 62.6–75.7% on Waymo. Point regression yields unusable results and UltraLiDAR fails on the more complex Waymo scenes, demonstrating that the restored point cloud preserves actionable geometric information.

6. **Systematic privacy-utility tradeoff study (Section 5.6).** The paper evaluates two families of perturbations (point cloud augmentations and region-specific Gaussian noise), revealing that defenses which increase restoration error also degrade detection utility, and that noise affects empty and non-empty regions unevenly due to feature sparsity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Slightly imprecise framing of restoration quality.** The abstract states ConcreTizer "concretely restores the original 3D point cloud scene." The method restores a voxel-resolution occupancy mask with points at voxel centers — Section 4.3.1 explicitly acknowledges "an error range constrained by the voxel size." The paper would benefit from using more precise language (e.g., "restores a voxel-resolution occupancy approximation of the original scene") to avoid implying sub-voxel recovery. This does not diminish the contribution — the restored scenes are demonstrably useful for detection tasks — but precision matters for a privacy-attack paper.

2. **No uncertainty reporting on primary quantitative results.** Table 1 reports average CD, HD, and F1 scores without standard deviations, confidence intervals, or statistical significance tests. Given that ConcreTizer consistently outperforms baselines by large margins across 3769 and 3999 scenes, the main conclusions are robust. Still, adding variance estimates would improve the paper's rigor.

3. **Missing experimental details in the main text.** The paper does not report the train/test split protocol (scene-wise random, by drive, etc.), the number of training scenes, or the numerical voxel size used. While these details may appear in the supplementary material (stripped by the parser), the main text should briefly state them for self-containedness. Voxel size is particularly relevant since it directly bounds the restoration error.

4. **Hyperparameter justification.** Section 5.1 states that only the alpha parameter of focal loss is adjusted (gamma left at default) and the regression loss weight β is set to 1. The paper does not provide reasoning or sensitivity analysis for these choices. This is a minor omission.

### Trivial
- None.

## Nice-to-Haves

- **Occupancy-level evaluation metric.** Adding a metric that directly measures the accuracy of the predicted occupancy mask (e.g., voxel-wise precision/recall) would strengthen the evidence that the attack is effective even at the occupancy level, independent of sub-voxel coordinate recovery. Since the method outputs occupancy scores, this analysis costs almost nothing.

- **Deeper DCS analysis on false positive voxels.** A plot showing the effect of DCS on the distribution of false positive voxels (similar to Figure 3, right) would directly illustrate how DCS suppresses VoI growth and tie the mechanism to metric improvements.

- **Explicit re-implementation of prior work (Hwang et al., 2023).** The paper contrasts its analysis with the negative result of Hwang et al. A direct re-implementation of that specific method under the same training setup (rather than the generic point-regression baseline) would make the comparison more airtight and preempt concerns about mischaracterizing prior work.

- **Comparison with a standard defense (e.g., differential privacy).** The privacy-utility tradeoff section tests only two families of ad-hoc perturbations. Including one established defense from the literature would make the claim that "mitigating ConcreTizer attacks is challenging" better supported.

## Removed Points

These points were raised by reviewers but are removed from the main review with justification:

- **"Unfair baseline comparison with UltraLiDAR."** The paper explicitly states (Section 5.2): "We modified the encoder part of UltraLiDAR to accept voxel features as an input." It also explains why UltraLiDAR was chosen: it is "the only model based on voxel representation, similar to our feature extractor." The paper is transparent about the adaptation and does not claim UltraLiDAR was designed for this task. The comparison is informative and fairly framed. Removed as the paper already addresses this concern.

- **"Defense analysis is preliminary and should compare against literature defenses."** Moved to Nice-to-Haves as a suggestion for strengthening, not a weakness. The paper is transparent about the scope of this section.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface observations about the method or results that the paper itself does not already articulate.

## Suggestions

1. In the abstract and conclusion, qualify "restores the original scene" with phrasing that acknowledges the voxel-resolution nature of the restoration (e.g., "restores a voxel-level occupancy approximation of the original scene").
2. Add standard deviations or confidence intervals to Table 1.
3. Report the train/test split, training set size, and voxel size explicitly in the main experimental setup section.
4. Consider adding a voxel-wise occupancy precision/recall metric to directly measure occupancy prediction accuracy.
