Now I have a good calibration landscape. Let me synthesize the final review.

**Round 1 bracket**: The paper sits clearly above the low-anchor papers (2-3 range) and below the very strong papers (8+). Initial bracket: **5.0–7.0**.

**Round 2 narrowing**: Compared to mid-range anchors:
- NeRP3D (5.33): More thorough experiments, more datasets — our paper is stronger
- "How Well Does GPT-4o Understand Vision" (6.00): Similar systematic benchmark genre — comparable quality
- "Understanding Learning Phases in SSL via Critical Periods" (6.80): Stronger due to novel methodology + findings
- SHED/AnyDepth (4.0-4.5): Our paper is notably stronger

Final score: **6.0** — a well-executed, thorough empirical study with genuine insights, held back mainly by the few-shot emphasis as primary evidence and missing variance estimates, but transparent and appropriately scoped.

---

## Summary

This paper investigates whether monocular depth pre-training is a viable alternative to ImageNet classification or self-supervised pre-training for downstream semantic segmentation. Through extensive controlled experiments spanning multiple architectures (ResNet18/50, DeepLabV3, ViT), supervision types (video, stereo, Lidar), datasets (KITTI, Cityscapes, NYU-V2, ADE20k, PascalVOC), and evaluation regimes (few-shot, full-scale, out-of-domain transfer), the paper demonstrates that depth pre-training consistently improves segmentation performance over ImageNet and several self-supervised baselines, and provides mechanistic explanations for why depth succeeds where optical flow fails.

## Strengths

- **Systematic breadth of controlled experiments.** The paper tests depth pre-training across multiple architectures (ResNet18/50, DeepLabV3, ViT), supervision modalities (video, stereo, Lidar), training-set sizes (Figure 4), and fine-tuning regimes (full vs. frozen encoder). Table 1 shows depth pre-training consistently outperforms both random and ImageNet initialization (e.g., +5.8% mIoU on KITTI with ResNet50). This breadth directly validates the main hypothesis and goes beyond prior mixed results from Taskonomy and related work.

- **Mechanistic explanation for why depth succeeds where optical flow fails.** Section 4.1 and Figure 5 show optical flow pre-training is detrimental (e.g., -2.88 mIoU when fine-tuning all, -9.05 when freezing encoder) while depth helps. The paper argues convincingly that depth forces recognition of rigidity and stable 3D structure, whereas flow captures raw phenomenology without enforcing scene geometry — a novel causal explanation.

- **Out-of-domain transfer with large-scale depth models.** Table 5 shows Depth Anything (initialized from DINO v2) outperforms DINO v2 on ADE20k (+1.6 mIoU fine-tune, +4.6 linear probe), PascalVOC (+1.2, +1.0), and Cityscapes (+2.1, +3.5). This demonstrates that depth pre-training transfers across domains and rebuts the in-domain-only conjecture.

- **Identification of ImageNet frozen-encoder failure.** Figure 3 and Table 1 show freezing an ImageNet-pretrained encoder is *worse* than random initialization (mIoU 33.33 vs 41.24 on KITTI ResNet18). The paper attributes this to object-centric bias removing scene-level information — a concrete, testable insight about pre-training blind spots.

- **Robustness to object-scale analysis.** Figure 4 and the resolution-mismatch experiment demonstrate that depth pre-training is robust to object-scale variation, whereas ImageNet pre-training suffers from fixed-scale bias, identifying a specific mechanism behind the improvement.

## Weaknesses

### Major

- **Few-shot setting as the primary evidence base.** The headline results (Table 1, Figures 2–3) and most ablations use only 16 training images for KITTI semantic segmentation. While the authors are transparent about this and use it to highlight the role of pre-training, the practical claims about depth pre-training being "viable" rest heavily on this extremely low-data regime. Full-scale results on Cityscapes confirm the pattern but show smaller gains (2.76 point mIoU improvement vs. 5.8 on KITTI). The out-of-domain transfer results (Table 5) are more compelling but use a different setup (Depth Anything initialized from DINO v2 vs. DINO v2). The paper would benefit from more explicitly acknowledging this gap in evidential strength between few-shot and full-scale findings.

- **No error bars or variance estimates.** The few-shot results (16 training images) are particularly susceptible to noise from random splits, initialization, and optimization stochasticity. The striking frozen-ImageNet-worse-than-random finding would be substantially more credible with standard deviations over multiple runs. This omission weakens the statistical foundation of several claims.

- **Optical flow experiment is underspecified.** The paper states: "We train optical flow on a siamese network with two shared-weight encoders" but provides no loss function, architecture details, training data, or hyperparameters (Section 4.1, Figure 5). Without these details, it is impossible for readers to assess whether the comparison is fair — do the flow and depth models have matched encoder architectures, training data, and compute budgets? This is the weakest experiment in the paper and needs to be substantiated or reframed as preliminary.

### Minor

- **The information bottleneck formalization (Section 3) is elegant but disconnected from the experiments.** The empirical protocol uses validation error as a proxy without any attempt to estimate mutual information or the Lagrangian terms in Equation~4. This section motivates the study but does not drive the experimental design. It could be shortened without loss.

- **The depth-cropped Cityscapes result (Table 5) raises more questions than it answers.** Training depth on random 256×256 patches improves training accuracy but reduces validation accuracy in the full setting, suggesting overfitting. The paper acknowledges this needs "future research," but as presented, this experiment adds confusion rather than insight.

- **Ambiguous reporting of improvement percentages.** The abstract claims "depth on average improves by 5.8% mIoU and 5.2% pixel accuracy on KITTI" without specifying absolute vs. relative. From Table 1, the improvement over ImageNet on ResNet50 is about 5 points absolute mIoU (44.65→50.92), which is a relative improvement of ~14%. This ambiguity is common but should be clarified.

### Trivial

- None of note.

## Nice-to-Haves

- The frozen-encoder result (ImageNet worse than random) is a standout finding that could be deepened by analyzing the feature space (e.g., measuring effective receptive field or using CKA similarity). Such analysis would sharpen the contribution from "depth works" to "here is *why* it works differently from classification pre-training."
- Reporting ViT-L results under full fine-tuning (both encoder and decoder), which would make the ViT comparison more complete.
- The evidence hierarchy could be reorganized so that out-of-domain transfer results (currently in Section 4.3) appear earlier, since they provide the strongest practical evidence.

## Removed Points

The following points from the inputs were removed with justification:

1. **"Depth pre-training comparison not fair because Depth Anything is initialized from DINO v2"** (removed — the paper explicitly notes this in the table caption and treats it as a strength: it isolates the *additional* value of depth pre-training on top of an already strong representation).

2. **"The formalization section is too dense"** (removed — this is a stylistic preference, not a substantive weakness).

3. **Various generic formatting/style nitpicks** from the harsh critic (removed per instructions — these are not substantive).

4. **Strength Finder generic strengths** (e.g., "the paper addresses an important problem") — removed as superficial or generic.

5. **Strength that mentions "clear presentation"** — removed per instructions when it conflicts with verified weaknesses (the flow experiment is underspecified, which is a presentation gap).

6. **Criticism about "missing related works"** — removed per instructions (cannot verify from external sources).

## Novel Insights

None beyond the paper's own contributions. The reviews mostly confirm and reinforce the paper's own framing rather than providing a genuinely novel reinterpretation. One observation worth noting: the harsh critic's framing of the few-shot vs. full-scale evidence gap is more salient than the paper's own presentation foregrounds — the paper could reorganize its evidence hierarchy to better match where the strongest evidence actually sits (out-of-domain transfer > few-shot KITTI).

## Suggestions

- Add variance estimates (standard deviations over 3-5 runs) to the few-shot KITTI results, especially for the frozen-encoder experiments where the ImageNet-worse-than-random finding is most surprising.
- Substantiate the optical flow experiment by providing full training details (loss function, architecture, dataset, hyperparameters), or reframe it as a preliminary observation with caveats.
- Explicitly clarify in the abstract and introduction that the "5.8% improvement" is in absolute percentage points (or convert to relative percentages).
- Consider moving the out-of-domain transfer results earlier in the paper or giving them more emphasis in the abstract, as they constitute the strongest evidence for the practical value of depth pre-training.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>