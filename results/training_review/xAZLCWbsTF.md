Now I have a thorough understanding of the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes replacing the epipolar-based cost volume in self-supervised multi-frame depth estimation with a cross-attention map that the authors show can function as an **asymmetric full cost volume**. The key insight is that cross-attention layers trained via masked image modeling (CroCo-v2) implicitly learn a warping function analogous to explicit epipolar warping. The authors introduce the **CRAFT module** (cross-attention map and feature aggregation) to refine this learned cost volume, used hierarchically in a coarse-to-fine manner. The method eliminates the need for a pose network during inference and demonstrates strong robustness to dynamic objects and image noise on KITTI and Cityscapes.

## Strengths

- **Novel conceptual contribution with mathematical grounding.** The paper clearly draws the connection between cross-attention maps (Eq. 7: \(C_{\text{attn}}(i,j) = \text{softmax}(F_t^Q(i) \cdot F_s^K(j))\)) and full cost volumes (Eq. 6: \(C_{\text{full}}(i,j) = F_t(i) \cdot F_s(j)\)), showing that the cross-attention map can be viewed as an asymmetric variant of a full cost volume. This reframing is original and well-motivated.

- **Strong targeted empirical results on the paper's stated scenarios of interest.** On dynamic objects (Cityscapes, Table 1) and under multiple noise types (KITTI, Table 2), CRAFT consistently and substantially outperforms prior epipolar-based methods (ManyDepth, DualRefine) and even methods that use additional supervision (segmentation networks, optical flow). These experiments directly address genuine weaknesses of epipolar-based cost volumes and provide the paper's most compelling evidence.

- **Eliminates pose network during inference.** Unlike prior multi-frame methods, the proposed architecture requires no separate pose network at test time, reducing computational complexity and removing pose-estimation failure as a source of error.

- **Ablation study validates CRAFT module components.** Table 5 confirms that both the attention aggregation and feature aggregation sub-modules contribute to final depth accuracy, and that the hierarchical CRAFT structure outperforms a DPT head alternative.

## Weaknesses

### Fatal
None.

### Major

- **Missing controlled comparison isolates the cross-attention map from the backbone/pretraining.** The paper's central claim is that the cross-attention map functions as a full cost volume, but every experiment compares the full CRAFT architecture (ViT backbone + CroCo-v2 pretraining + cross-attention cost volume) against prior methods using different backbones (ResNet) and different pretraining. The only ablation (Table 5) compares CRAFT modules against a DPT head — a decoder comparison that does **not** isolate the cost volume type. No experiment holds the ViT backbone and CroCo pretraining constant and varies only the cost volume construction (epipolar vs. cross-attention). Without this baseline, the observed robustness and accuracy gains cannot be unambiguously attributed to the cross-attention map functioning as a cost volume, as opposed to the more powerful backbone and pretraining. This is the paper's most significant weakness and limits the strength of its core claim.

### Minor

- **Abstract overstates performance relative to evidence.** The abstract claims "our approach outperforms traditional methods" without qualification. On the standard KITTI Eigen split (Table 3) and Cityscapes (Table 4), the method is competitive but not dominant across all metrics (e.g., ManyDepth with monocular prior and DualRefine achieve lower AbsRel on KITTI). The conclusion appropriately qualifies the claim with "particularly in environments with dynamic objects and image noise," but the abstract's broader framing is imprecise and could mislead readers.

- **Emergent correspondence claim rests on only qualitative evidence.** Section 4.1.3 argues that the cross-attention map learns geometric warping based on one qualitative visualization (Fig. 3) and a mathematical analogy. No quantitative metric (e.g., recall@k of the attention argmax against ground-truth disparity or optical flow) measures whether the attention map actually captures correct correspondences. This weakens the "emergent correspondence" narrative.

- **"Consistency mask" is ablated but never defined.** Table 5 shows that a "consistency mask" component has a nontrivial effect on all metrics, yet this component is not defined or described anywhere in the main paper text. The reader cannot understand what it is or how it contributes.

- **Reproduction details for Cityscapes baselines are limited.** Table 1 marks baselines as "reproduced from official repository" without specifying training hyperparameters, data splits, or whether methods were retrained on Cityscapes. Since the dynamic-object results are the paper's strongest evidence, these details are important for reproducibility.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment using the same ViT+CroCo backbone with an epipolar-based cost volume (using ground-truth pose to avoid compound confounds) would directly substantiate the core claim.
- A quantitative attention-correspondence benchmark (e.g., recall@k) would strengthen the emergent-correspondence argument.
- Ablation with random backbone initialization (or a non-MIM pretraining) would clarify how much of the correspondence is inherited from CroCo vs. learned from the depth training objective.

## Removed Points

- **"False dichotomy" claim about epipolar cost volumes** — The paper explicitly acknowledges that prior work uses monocular priors and segmentation to handle dynamics (lines 12, 53). It correctly states that epipolar cost volumes require pose during inference, which is factual. This is not a false dichotomy.
- **Architecture details are vague** — The paper states "Further details are provided in Figure 2 and in Section B." The appendix was stripped by the parser, but these details exist in the original submission. Per hard rules, appendix-deferred details are not a valid weakness.
- **Metrics (mDEE, mRR) not defined in main text** — The paper defines mDEE as "a combined metric of AbsRel and δ₁" and mRR as "performance degradation compared to noise-free conditions" in the main text, with detailed equations deferred to the appendix. This is standard practice.
- **Missing/inconsistent table comparisons** — Tables 3-4 include methods with and without monocular priors, with clear notation (ℳ). This is standard practice in the field and does not make interpretation difficult.
- Various formatting/style/completeness nitpicks that stem from parser artifacts, not the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews raise valid concerns about experimental design but do not identify a fundamentally new angle on the problem that the paper itself has missed.

## Suggestions

1. **Add the critical controlled ablation**: Replace the cross-attention cost volume with an epipolar-based cost volume using the same ViT backbone and CroCo-v2 pretraining (with a learned pose network or ground-truth pose). Report the same metrics on KITTI and Cityscapes. This single experiment would either substantiate or refute the paper's central mechanistic claim.
2. **Sharpen the abstract's claims** to match what the data show: the method excels in dynamic and noisy scenarios and is competitive overall, rather than claiming unqualified superiority.
3. **Define the consistency mask** in the main text so readers can understand the ablation.
4. **Add a quantitative evaluation** of cross-attention correspondence accuracy (e.g., percentage of argmax matches within a threshold of the ground-truth epipolar match) to support the emergent-correspondence claim beyond a single qualitative example.

## Score and Decision

The paper presents a genuinely novel idea — using learned cross-attention maps as a full cost volume — with clean mathematical exposition and strong targeted experiments on dynamic objects and noise robustness. These are important practical scenarios where epipolar-based methods genuinely struggle. However, the experimental validation has a critical gap: it never isolates the effect of the cross-attention map from the powerful ViT backbone and CroCo pretraining, leaving the core mechanistic claim incompletely supported. The abstract's framing is also broader than the evidence warrants. These issues are addressable with additional experiments, but in their current form they prevent full confidence in the claimed contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>