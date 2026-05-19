- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 5, 5, 8
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper proposes Order-Aware Interactive Segmentation (OIS), which introduces relative depth (order) information into interactive segmentation. OIS constructs order maps from monocular depth estimates and user clicks, then uses order-aware masked cross-attention to guide prompt-image interaction based on depth ordering. It further incorporates object-aware attention that separates foreground and background prompts, and combines dense and sparse prompt fusion for efficiency. Experiments on HQSeg44K and DAVIS show substantial gains over prior methods (7.61 mIoU after one click on HQSeg44K) while achieving 2× faster inference than SegNext.

## Strengths

- **Novel order-aware attention mechanism**: The paper introduces order maps (Eq. 1–2) that encode relative depth between the click location and image regions, and uses them as attention masks (Eq. 3) to guide prompt-image interaction. The ablation (Table 4) shows removing this module increases NoC90 by 1.04 and decreases 5-mIoU by 1.15 on DAVIS, directly proving its contribution.

- **Object-aware attention with explicit foreground-background separation**: Adapting ideas from video object segmentation (Cutie) to interactive segmentation, this module forces positive-click embeddings to attend only to foreground and negative-click embeddings only to background (Eq. 4–5). The ablation confirms its necessity. This is a clear differentiator from SAM-style methods that intermingle both prompt types.

- **Large and consistent gains across datasets**: On HQSeg44K (Table 1), OIS achieves 1-mIoU of 89.40% vs. 81.79% for SegNext (+7.61) and reduces NoC90 by 1 full click. On DAVIS (Table 2), NoC95 improves by over 2 clicks (8.59 vs. 10.73). The consistency across benchmarks rules out overfitting to a single dataset.

- **Effective balance of accuracy and speed**: Table 3 shows OIS achieves 2× faster inference than SegNext (SPC 12ms vs. 32ms, SAT latency 1.40s vs. 2.42s) while simultaneously improving accuracy. This trade-off is achieved by replacing expensive spatial self-attention with efficient sparse cross-attention, enabled by the hybrid dense-sparse prompt integration.

- **Qualitative evidence directly supports the claimed benefits**: Figures 4–6 show OIS correctly segmenting occluded objects (rhinoceros behind a tree), handling blur (fast-moving car), and rejecting false positives from background objects at different depths — cases where SegNext and HQ-SAM fail. The attention visualizations in Figure 6 directly illustrate how order-aware attention suppresses distractors.

## Weaknesses

### Fatal
None.

### Major

- **Baseline evaluation relies on reported numbers rather than a unified protocol**: The paper explicitly states (line 120) that for most metrics (NoC90, NoC95, 5-mIoU), it "directly reference[s] the results as reported in their papers," computing only 1-mIoU and NoF95 using released weights. Different papers may use different image sizes, click sampling strategies, or stopping criteria. While this practice is common in the interactive segmentation literature, it reduces confidence in the exact magnitude of the reported gains. The claimed improvements (e.g., 1-click reduction in NoC90) are within the range that protocol differences could affect, making it difficult to determine how much of the margin is genuine improvement vs. evaluation drift.

- **No control for backbone strength in baseline comparisons**: OIS uses a frozen ViT-Base encoder from DepthAnythingV2 — a large, highly capable pretrained model. SegNext, SimpleClick, and other baselines use different (generally lighter) backbones. The ablation (Table 4) convincingly shows that the proposed modules contribute beyond the encoder (since the encoder is held constant), but this does not quantify how much of the *absolute gain over baselines* is attributable to the stronger encoder versus the proposed innovations. A control experiment replacing OIS's encoder with a backbone comparable to SegNext's would strengthen the attribution of gains.

### Minor

- **Depth model timing is not fully broken down**: The paper states (line 122) that the same frozen encoder is reused for both depth map generation and feature extraction, and that the depth decoder runs once. The per-click (SPC) depth cost is therefore near zero, which is reasonable. However, the presentation (Table 3) would benefit from a full latency breakdown (encoder, depth decoder, segmentation decoder) to clarify what is included, rather than showing 0 ms without explanation. The SAT latency description (line 151) accounts for depth model prediction in the total, which suggests the one-time cost is included — but this is not made explicit.

- **No discussion of depth estimation quality limitations**: The method relies on monocular depth estimates from DepthAnythingV2. Cases where monocular depth is unreliable (transparent objects, reflections, repetitive structures) are not discussed. An honest acknowledgment of this limitation would improve the paper.

### Trivial
None.

## Nice-to-Haves

- A controlled evaluation re-running all baselines under the same evaluation pipeline (same image sizes, click sampling, etc.) would make the comparison unassailable.
- An ablation replacing OIS's encoder with a backbone similar to SegNext's would isolate the contribution of the proposed modules from the encoder advantage.
- Adding an explicit baseline that feeds raw depth as an extra input channel (like MM-SAM but with OIS's architecture) would directly validate the superiority of the order-map formulation over naive depth concatenation.

## Removed Points

- **"Ablation performance drop could be attributed to the strong encoder rather than to order information"**: This criticism misunderstands the ablation design. The encoder is held constant when order-aware attention is removed (Table 4, row 2). Any performance drop is therefore attributable to removing the module, not the encoder. The valid concern about encoder strength applies to *baseline comparisons*, not the ablation.
- **"Claim that current methods fail to incorporate depth information overstates because MM-SAM exists"**: The paper explicitly acknowledges MM-SAM (line 31) and explains why its approach is insufficient ("poor performance...due to insufficient fusion"). This is a reasonable framing.
- **"Missing click simulation details"**: The paper states (line 128) it follows prior works' click sampling strategies. This is standard and sufficient.
- **"Missing learning rate / batch size / augmentation in main text"**: These details may exist in the appendix (stripped by the PDF parser). The main text provides key hyperparameters (Adam, 15 epochs, 2 A100 GPUs, image size 1024).
- **"Number of training clicks (48) seems high"**: This is a design choice without a clear problem. No evidence is provided that this harms performance.
- **Formatting and style nitpicks**: Removed per instructions.

## Novel Insights

The harsh critic correctly identifies that the evaluation protocol (using reported numbers for baselines) weakens confidence in the exact margin of improvement, but this concern applies mainly to the headline claims about *how much* better OIS is, not *whether* it is better. The ablation experiments (Table 4) provide controlled evidence that each proposed module contributes meaningfully. An interesting synthesis not emphasized by either reviewer is that the two attention modules — order-aware and object-aware — address complementary failure modes: the former handles depth-separated objects while the latter handles same-depth objects. This interdependence is a natural strength of the design that makes the whole greater than the sum of its parts. The paper would benefit from an experiment that explicitly demonstrates this complementary behavior on failure cases where only one module suffices and where both are needed.

## Suggestions

1. **Provide a backbone control experiment**: Either (a) re-implement OIS using the backbone architecture of SegNext (ConvNeXt) and report the results, or (b) re-implement SegNext using the DepthAnythingV2 ViT-Base encoder and show that OIS still outperforms it. This would cleanly separate encoder effects from module effects.

2. **Re-run a subset of key baselines under a unified evaluation pipeline** (even if only for the main metrics like NoC90 and 5-mIoU on DAVIS) to verify the gains are not artifacts of protocol differences.

3. **Provide a full latency breakdown** showing encoder forward pass time, depth decoder time, segmentation decoder time, and per-click attention time separately.

4. **Add a discussion of failure cases** where monocular depth estimation is unreliable and acknowledge this as a limitation.
