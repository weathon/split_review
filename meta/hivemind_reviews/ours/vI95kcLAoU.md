## Summary
The paper proposes Skip-Attention, a method to improve ViT efficiency by replacing Multi-Head Self-Attention (MSA) blocks in certain layers with a lightweight parametric function (depthwise convolution + channel attention). The motivation comes from an empirical analysis showing high correlation in attention maps and MSA features across adjacent ViT layers (cosine similarity up to 0.97, high CKA in layers 2–8). By skipping MSA computation in layers 3–8 and using the parametric function instead, the method achieves modest accuracy gains (0.1–0.4%) alongside 19–25% throughput improvements on ImageNet, with consistently positive results on semantic segmentation, image/video denoising, self-supervised learning, and mobile deployment.

## Strengths
1. **Well-motivated, clean method with thorough empirical grounding.** The paper provides quantitative evidence (CKA analysis, cosine similarity of attention maps) that ViT layers produce highly correlated MSA outputs, directly motivating the skip strategy. This is a stronger empirical foundation than prior attention-reuse work in NLP.

2. **Ablation cleanly isolates the parametric function's contribution.** Table `ablation` (referenced in §4.6) shows that direct feature reuse (identity function) causes a 4.7% accuracy drop, while the full Skip-Attention module outperforms the baseline by ~1.6% (100-epoch setting). This demonstrates the depthwise-convolution-based estimator is essential — not just the act of skipping itself — and acts as a meaningful regularizer.

3. **Consistent speedups across a diverse task set (7 tasks, 4 architectures).** The method is validated on ImageNet classification (ViT-T/S/B), DINO self-supervised learning, ADE20K semantic segmentation, SIDD image denoising (Uformer), and DAVIS video denoising (UniFormer). The consistent pattern of maintained-or-better accuracy with non-trivial throughput gains (19–25% classification, 25% segmentation, 25% denoising, 26% training time reduction in DINO) makes the contribution practically credible.

4. **Real-world mobile latency validation.** On a Snapdragon 8 Gen 1 NPU (Samsung Galaxy S22), Skip-Attention cuts inference time by 19% at 224×224 and 34% at 384×384. This confirms that the FLOP reductions translate to actual speed on low-power hardware, which many efficient-transformer papers do not demonstrate.

5. **Improved attention interpretability as a side benefit.** Without any fine-tuning, Skip-Attention produces segmentation masks on Pascal-VOC12 with substantially higher Jaccard similarity and CorLoc scores than vanilla ViT, and qualitative maps show better object localization in the remaining attention layers (§4.1, Fig. 5).

## Weaknesses
### Fatal
None.

### Major

1. **Loss of global context in skipped layers is not analyzed.** The parametric function uses 5×5 depthwise convolutions, which can only model local spatial relationships, yet these replace the global all-to-all receptive field of self-attention in 6 out of 12 layers (for ViT-T). The paper shows the method *works* on tasks requiring long-range dependencies (segmentation), but never analyzes *how* the model compensates — e.g., whether the remaining attention layers carry the full global burden, whether effective receptive field shrinks, or whether long-range predictions degrade in measurable ways. This gap weakens the paper's core conceptual claim that expensive attention can be replaced without representational loss. Adding effective receptive field analysis or attention-distance variance would meaningfully strengthen the paper.

### Minor

2. **Accuracy gains reported under different training regimes lack explicit side-by-side comparison.** The main results (§4.1, 300-epoch DeiT recipe) report 0.1% gain over baseline ViT-T, while the ablation section (§4.6, 100-epoch training) reports "at least 1.4%" improvement. These are not contradictory — different training schedules produce different baselines — but the paper never states the baseline accuracy for the 100-epoch setting explicitly (it must be inferred: 65.8% from the alternate-config comparison). A single table or sentence showing both baselines would eliminate reader confusion. As written, the discrepancy between 0.1% and "at least 1.4%" erodes trust even though it is fully explainable.

3. **Video denoising experiment uses identity function, undercutting the "parametric function is critical" narrative.** The paper states: "simply adopt a naive Skip-Attention, where we reuse window self-attention matrix, A, of the corresponding encoder block using an Identity function. We empirically observe that reusing attention works better in this task." The paper is honest about this, but if identity function suffices for one task, the claim that the parametric form is "critical" (§3, §4.6) is weakened. This should at least be discussed — why does identity work here but fail (4.7% drop) in classification?

4. **Throughput comparisons against token-pruning methods are not fully controlled.** The paper correctly notes that FLOPs reductions do not always translate to throughput gains and cites prior work on this point. However, it does not state whether baseline throughput numbers (ATS, SPViT, etc.) were measured in the same framework/hardware or taken from prior papers under unknown conditions. This is a standard limitation in efficiency papers, but it means the "state-of-the-art" throughput claim should be read with caution.

### Trivial
None.

## Suggestions
1. **Add a single table showing all baselines.** Report the 100-epoch ViT-T baseline accuracy alongside the 300-epoch one, and show both sets of gains side-by-side. This would resolve the "0.1% vs 1.4%" confusion entirely.

2. **Add an effective receptive field (ERF) analysis** for Skip-Attention vs. vanilla ViT on a task where global context matters (e.g., segmentation). This would directly address the concern about lost long-range reasoning.

3. **Discuss why identity function works for video denoising but fails for classification.** This would strengthen rather than weaken the paper by showing the method's boundaries are understood.

4. **Run at least one token-pruning baseline in the same framework** to verify the throughput advantage is not an artifact of differing implementation maturity. Even one comparison would significantly increase confidence in the efficiency claims.

5. **State the "40% speedup" on ADE20K explicitly in the body** with the specific comparison it refers to, so the contribution list matches the experimental section.

## Score and Decision

The paper presents a simple, empirically grounded, and well-validated method for improving ViT efficiency across diverse tasks and architectures. The core contribution — replacing MSA blocks in correlated layers with a lightweight convolutional parametric function — is clean, the ablations are sound, and the breadth of evaluation is commendable. The main weaknesses (missing analysis of global context loss, under-specified comparison between training settings, and the identity-function tension) are real but addressable and do not invalidate the paper's central claims. The method's consistent pattern of modest accuracy gains with meaningful throughput improvements across 7 tasks is rare in the efficient ViT literature and gives the paper practical value.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
