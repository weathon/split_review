Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a keypoint detection and description framework that fuses rotation-equivariant multi-scale features (via G-CNNs) with global positional information (via a Transformer encoder) and introduces a directional uncertainty weighted descriptor loss. The method is evaluated on rotated variants of HPatches, MegaDepth, and YFCC100M, and achieves state-of-the-art results among learning-based methods on the 3D pose estimation benchmarks (MegaDepth, YFCC100M) under rotated conditions.

## Strengths

- **State-of-the-art rotation-robust descriptor matching on 3D benchmarks**: On rotated-MegaDepth (random rotations), the method achieves AUC@5/10/20 of 0.398/0.601/0.741, outperforming prior learning-based methods including AWDesc (0.347/0.552/0.704), ReF (0.314/0.516/0.680), and RELF. These results are the paper's strongest empirical contribution and provide genuine evidence that the overall system advances the state of the art.

- **Novel directional uncertainty weighted descriptor loss with ablation support**: The proposed L_DUWD explicitly accounts for discrete group sampling bias when aligning rotation-equivariant descriptors. Ablation results (Table 4) show the full fusion strategy outperforms alternative fusion strategies (Ablation1, Ablation2) across MegaDepth variants, e.g., on MegaDepth-Rot90 AUC@5=0.467 vs. 0.447/0.411.

- **Comprehensive evaluation across diverse rotation conditions**: The method is tested on three datasets (HPatches, MegaDepth, YFCC100M) with three rotation variants each (no rotation, 90° multiples, arbitrary angles). It achieves the best or near-best results among learning-based methods in every rotated setting on the 3D datasets, providing broad empirical support.

## Weaknesses

### Major

- **Missing ablation baseline: the contribution of positional information is not isolated.** The ablation study (Table 4, Section 4.4) compares three variants of the fusion architecture, but every variant includes the Transformer/positional encoding branch. There is no comparison against a pure rotation-equivariant backbone (rotation-equivariant FPN + directional loss + standard descriptor loss) without any positional encoding component. The paper's central narrative is that fusing positional information with rotation-equivariant features is beneficial, but this cannot be verified without isolating whether the improvement comes from the fusion or simply from the rotation-equivariant backbone and losses. Adding this baseline would directly test the paper's core claim about the fusion.

- **The Dilated Feature Extraction (DFE) module is underspecified.** This module is a critical part of the pipeline: it processes the fused features and its output directly forms the final descriptor map (Figures 2/4, ablation formulas in Section 4.4). However, the paper provides no architectural details — number of layers, dilation rates, kernel sizes, whether it uses group-equivariant or standard convolutions, or how the two addition operations in the fusion formula are implemented. Without this information, the method cannot be reproduced. (Note: the paper's Table 4 formulas reference "DFE" but only as a black-box symbol with no architectural specification.)

### Minor

- **The cross-entropy term in L_DUWD is underspecified.** Equation (3) includes `CE(Shift(D_A, O_gt, D_B))`. The paper states that O_gt is the ground-truth relative rotation and Shift circularly shifts descriptors along the rotation-group channels. But it does not specify the target distribution for the cross-entropy loss — is the model classifying the shift index (K=8 classes?)? Is O_gt encoded as a one-hot vector? The loss function as written cannot be implemented from the paper alone.

- **The rotated-HPatches results are weaker than claimed.** On the dataset explicitly designed for planar rotation evaluation, traditional handcrafted keypoints (ORB, BRISK, AKAZE, KAZE) outperform the proposed method (Table 1). The paper acknowledges this and attributes it to planar scenes limiting learning-based advantages, but this is the exact regime where rotation-handling tricks should be most effective (no 3D structure to confound local equivariance). The fact that the method does not beat traditional algorithms on this benchmark, while strongly outperforming them on 3D benchmarks, raises the question of whether the method's advantage on 3D data comes more from the Transformer's global context on non-planar scenes than from improved rotation handling per se. A controlled experiment isolating rotation effects on 3D scenes would clarify this.

- **Detection component is barely described.** The paper claims an "end-to-end framework to simultaneously detect and describe robust keypoints," but the detection head architecture, the resolution of the score map, and how detection interacts with the rotation-equivariant backbone are not specified. The only information given (Section 4.1) is that the loss is weighted binary cross-entropy with ground truth from SuperPoint.

- **Training details are sparse.** The paper reports learning rate (0.001), weight decay (0.05), batch size (12), and epoch count (28), but omits the optimizer type (e.g., Adam vs. SGD), learning rate scheduler, data augmentation strategy, and how negative pairs are sampled for the triplet loss. These details are needed for reproducibility.

### Trivial

- **Runtime comparison is limited.** The runtime analysis (Section 4.5) only compares against AWDesc. Comparisons to ReF and RELF — the most relevant rotation-equivariant baselines — would have been more informative.
- **Origin of attention maps (w_A, w_B) in the CVtri loss is not explicitly stated.** The paper adopts this loss from AWDesc but does not clarify whether these attention maps come from the Transformer encoder in this paper's architecture or are computed separately.

## Nice-to-Haves

- A controlled experiment on rotated-MegaDepth at multiple discrete rotation angles (e.g., 30°, 60°, 90°, 120°, 150°, 180°) would clarify whether the method's advantage is continuous across rotations or only benefits from the discrete group structure at angles aligning with the group sampling (K=8 → 45° increments). This is not a weakness in its absence but would strengthen the rotation robustness analysis.
- Additional runtime comparisons against ReF and RELF would help contextualize the 54% slowdown relative to AWDesc.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Section numbering jump (3.1.2 to 3.3, missing 3.2):** This is likely a parser artifact or minor editing error. The rule for meta-reviewing is to remove formatting/parser artifacts. The original submission likely contains this section.
- **Missing related works (non-rotation-equivariant learning-based keypoint methods):** As per meta-review guidelines, I cannot verify the presence or absence of specific related works without external sources. This criticism is excluded.
- **"Uncertainty weighting" name critique:** The critic argues that L_DUWD does not truly model uncertainty despite its name. This is a stylistic/pedantic point about naming conventions rather than a substantive weakness. The loss still performs as described.
- **Criticism that O_gt cannot be obtained during evaluation:** Not raised by this particular reviewer but the general class of "missing test-time supervision" criticisms was filtered. The paper uses O_gt only during training (for the loss), which is standard.

## Novel Insights

None beyond the paper's own contributions. The reviews are largely convergent: the paper has genuine SOTA results that make a contribution, but the experimental analysis is incomplete in a way that prevents full attribution of those gains, and several architectural components are underspecified to the point of hampering reproducibility.

## Suggestions

1. **Add the missing ablation baseline**: Evaluate the method with the positional branch removed entirely (no Transformer encoder, no positional encoding — use only the rotation-equivariant FPN and the directional loss on fused features). This directly tests whether the fusion is beneficial.
2. **Specify the DFE module completely**: Provide architecture details (layers, dilation rates, kernel sizes, equivariance properties, implementation of the addition operations in the fusion formula).
3. **Clarify the cross-entropy loss term**: Specify the target distribution, number of classes (K=8?), and whether O_gt is a one-hot encoding of the discrete rotation index.
4. **Provide detection architecture details**: Describe the detection head, score map resolution, and its interaction with the rotation-equivariant backbone.
5. **Add training details**: Specify the optimizer type, learning rate scheduler, data augmentation, and negative pair sampling strategy.
6. **Discuss the rotated-HPatches result more thoroughly**: Acknowledge the gap with traditional methods and provide analysis or a controlled experiment that separates rotation effects from global context effects.

## Score and Decision

**Originality:** The fusion of rotation-equivariant features with positional encoding for local descriptors is a reasonable direction, though individual components (G-CNNs, Transformers for positional info) are established. The directional uncertainty weighted loss is a novel contribution. — *Score: 3/5*

**Importance of research question:** Rotation robustness for local features is practically important for robotics, UAVs, and extreme-motion scenarios. The question is timely and well-motivated. — *Score: 4/5*

**Claims support:** The main claim (SOTA rotation-robust performance) is supported by results on 3D benchmarks. However, the attribution claim about the fusion benefit is not fully supported due to the missing ablation. — *Score: 2.5/5*

**Soundness of experiments:** The evaluation is comprehensive across datasets and rotation conditions. The ablation compares fusion strategies but misses the fundamental baseline. Missing optimizer/details slightly weaken the soundness. — *Score: 3/5*

**Clarity of writing:** The paper is generally understandable but has significant gaps in architectural specification (DFE module, detection head) and loss definition (CE target) that affect reproducibility. The writing quality is adequate but needs revision. — *Score: 2.5/5*

**Value to community:** If the reproducibility gaps are addressed, the SOTA results and the loss formulation would be valuable to researchers working on rotation-robust local features. — *Score: 3.5/5*

**Overall assessment:** The paper demonstrates genuine SOTA results on rotation-robust keypoint matching on 3D benchmarks and proposes a novel loss. However, the ablation analysis has a critical gap (no baseline removing positional information entirely), and the method description has significant reproducibility issues (DFE module architecture unspecified, cross-entropy target undefined, detection details missing). These issues are addressable with additional experiments and clarifications, but in its current form the contribution analysis is incomplete and the method cannot be fully reproduced.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>