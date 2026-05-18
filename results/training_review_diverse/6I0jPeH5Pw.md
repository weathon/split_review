Here is my consolidated review, with all claims verified against the actual paper.

---

## Summary

This paper proposes a patch-wise preprocessing pipeline (splitting ultra-high-resolution PCB images into 1024×1024 tiles) combined with a YOLOv7 segmentation model to automate ROI segmentation for PCB Automated Optical Inspection (AOI). On a test set of 5 boards with different background colors, the method achieves an average IoU of 0.8889, pixel accuracy of 0.9961, and mAP of 0.8255, outperforming DeepLabv3+, Mask R-CNN, and YOLACT in reported metrics. The paper addresses a genuine industrial need but its evaluation is substantially under-developed for the strength of the claims made.

## Strengths

- **Practical problem with clear motivation.** Automating ROI setting in PCB AOI is a real bottleneck in manufacturing, and the paper correctly identifies that manual ROI specification is time-consuming, error-prone, and labor-intensive (Section 1). The patch-wise strategy is a sensible way to handle images that can reach 25,000×30,000 pixels on standard GPU hardware.

- **Consistent per-board results across diverse board colors.** Table 1 reports per-board metrics for all 5 test boards (blue, green, brown-green, white, black backgrounds) with IoU ≥ 0.86, F1 ≥ 0.92, and pixel accuracy ≥ 0.99 across all five. This provides some evidence that performance does not collapse on specific background colors—a necessary property for industrial deployment.

- **Granular 10-class labeling.** Unlike prior work (Li et al., 2020) that treated all components as a single class, this paper labels lead, pad, chip, resistor, capacitor, diode, IC, connector, LED, and coil separately (Section 3.1). This granularity is meaningful for AOI systems that need different inspection criteria per component type.

- **Honest acknowledgment of limitations.** Section 5 openly discusses the patch-boundary problem for small components (leads and pads at tile edges) and identifies it as an inherent limitation of the fixed-size non-overlapping patch strategy. This transparency is commendable.

- **Manual labeling by experienced AOI operators with quality review** (Section 3.1), increasing confidence in the ground-truth data.

## Weaknesses

### Fatal

None. The approach is reasonable and the core idea is sensible.

### Major

- **No per-class metrics despite defining 10 component classes.** The paper defines 10 distinct classes (leads, pads, chips, resistors, capacitors, diodes, ICs, connectors, LEDs, coils) but reports only aggregate metrics. Per-class IoU, F1, or pixel accuracy is entirely absent. Given that Section 5 explicitly notes difficulties with leads and pads, and the qualitative comparison notes that YOLACT struggles with pad segmentation and DeepLabv3+ confuses chips and diodes, the absence of per-class numbers is a critical gap. Without them, it is impossible to determine whether the aggregate IoU of 0.8889 masks near-zero performance on some classes, or whether all 10 classes are segmented reliably. This is the single most impactful thing the authors could add with their existing data.

- **Baseline comparison is not reproducible and may be unfair.** The paper compares YOLOv7 against DeepLabv3+, Mask R-CNN, and YOLACT in Table 2 and Figure 3, but never states: (i) whether these baselines were trained on the same patch-wise preprocessed data, (ii) whether they were trained from scratch or fine-tuned from pretrained weights, (iii) what hyperparameters, optimizer, or training budget were used, or (iv) how inference was conducted (patch-wise or full-image). If the baselines were not trained on patches, the comparison conflates the preprocessing strategy with model architecture, and the observed YOLOv7 advantage could simply reflect the benefit of patch-wise training rather than model superiority. If they were trained on full-resolution images, the GPU memory constraints would have forced a much smaller batch size or image resize, further confounding the comparison. The paper must disclose the baseline training protocol or the comparison table is uninterpretable.

- **Real-time claim is ambiguous and likely overstated.** The paper reports 10–20 ms inference time for YOLOv7 (Table 2, line 114) without specifying whether this is per patch or per full board. A PCB image of 18,242 × 14,782 pixels (Figure 1) would generate ~250 patches of 1024×1024 (with padding). At 10–20 ms per patch, end-to-end latency for a single board would be 2.5–5 seconds, which is not real-time for a production line. The paper also invokes YOLOv7's general capability of "30 FPS or higher on standard GPU setups" (line 37)—a claim from the original YOLOv7 paper about standard-resolution detection benchmarks, not about this patch-based pipeline. The real-time framing must be grounded in actual per-board end-to-end latency including patch extraction and reconstruction. As it stands, the paper's central "real-time" selling point is unsupported.

### Minor

- **Patch-wise preprocessing design choices are unjustified.** The paper presents patch-wise division (1024×1024, non-overlapping, with black padding) as a "novel preprocessing method" (lines 19, 130), but it is a standard technique that the paper itself acknowledges has been used in prior work (Lam et al., 2018; Gao et al., 2013; Wang et al., 2023b). No ablation is provided for: the choice of 1024×1024 vs. 512×512 or 2048×2048; whether overlapping patches would mitigate the acknowledged boundary problem; or the reconstruction strategy from patches back to full-board segmentation. The claim that the preprocessing is a contribution would be strengthened by even a minimal ablation showing that 1024×1024 is preferable to alternatives.

- **500 epochs on 52 training images without data augmentation raises overfitting concerns.** The paper trains for 500 epochs on only 52 images (lines 48–50). While weight decay (5e-4) is used, no data augmentation is mentioned, and no early stopping or validation-based checkpoint selection is described. Given the small dataset size, this training protocol could lead to memorization rather than generalization. The lack of data augmentation is particularly notable since PCB images could plausibly benefit from rotations, flips, or color jitter.

- **Paper calls IoU of 0.8889 "relatively low" (Section 5), which is inconsistent with typical segmentation benchmarks** where 0.89 would be considered strong. This suggests either unusual metric computation or unrealistic expectations. The paper should clarify whether this is macro-averaged IoU across all classes (which would make 0.89 more understandable as a lower value if small classes underperform), or a different averaging scheme.

- **Reconstruction from patches to full-board segmentation is mentioned only in passing.** The paper states results were "recombined into one PCB image" (line 34) but provides no technical details on how overlapping predictions at patch boundaries are handled (or whether they are simply concatenated), how the black padding regions are dealt with, or whether any post-processing is applied. This matters because the boundary problem (Section 5) is a direct consequence of the patch strategy, and the reconstruction method determines how severely it affects the final output.

### Trivial

- The description of YOLOv7's architecture (E-ELAN, FPN, PAN) in Section 2.2 is a generic summary from the original YOLOv7 paper and could be substantially shortened.

## Nice-to-Haves

- Per-class metrics (IoU, F1, pixel accuracy) on the existing test set — this is the single most impactful addition the authors could make.
- A controlled ablation: YOLOv7 trained on full-resolution (resized) images vs. on patches, or at least comparing two patch sizes.
- End-to-end per-board latency figures including patch extraction, inference on all patches, and reconstruction.
- Disclosure of whether baselines used the same patch-wise preprocessing, and if not, a clear rationale.
- Data augmentation (rotations, flips) would likely improve robustness given the small dataset.

## Removed Points

These points were raised in the reviews but are removed or downgraded per the filtering rules:

1. **"Patch-wise preprocessing is presented as a contribution but is standard practice"** — moved from Major to Minor. The paper does present it as novel, which is overclaimed, but this is a framing issue rather than a technical flaw. The real weakness (no ablation/justification) is retained in Minor.
2. **"The loss function (BCEWithLogitsLoss) is unclear vs. standard YOLOv7-seg implementation"** — removed. YOLOv7-seg uses per-class BCE loss (sigmoid-based) for mask prediction; the paper's description is consistent with standard practice. The reviewer's concern about "combination of losses" reflects a knowledge gap about YOLOv7-seg's actual loss design.
3. **"Methodologically sound comparison against three strong baselines"** (Strength Finder Supporting Strength 1) — removed. This conflicts with the verified weakness that the baseline training protocol is undisclosed. Per rules, the weakness wins.
4. **"Components are spread throughout the board... this is true of almost any natural image"** — removed. This is a fair comment on writing style but does not affect the technical contribution.
5. **Qualitative observations not linked to quantitative metrics** — downgraded to trivial. Qualitative comparisons in Figure 3 are inherently qualitative; demanding per-class IoU for each observation is reasonable as a suggestion but not a standalone weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily identify evaluation gaps rather than offering new technical insights about the method itself.

## Suggestions

1. **Add per-class metrics immediately.** With the existing 5 test boards, compute and report IoU, F1, and pixel accuracy for each of the 10 component classes. Include per-class standard deviations across boards. This single addition would address the most serious evaluation gap and would reveal whether specific component types (leads, pads) are genuinely problematic as suggested in Section 5.
2. **Disclose baseline training protocols.** State whether DeepLabv3+, Mask R-CNN, and YOLACT were trained on the same patches or on full images, with what hyperparameters, and what pretrained weights were used. If they were not trained on patches, this must be clearly acknowledged as a confound, and the comparison should be re-run under matched conditions.
3. **Report end-to-end latency for a full board**, including patch generation, inference across all patches, and reconstruction. This is necessary to support any real-time claim.
4. **Abbreviate the generic YOLOv7 architecture description** (Section 2.2) and replace it with task-specific details: which backbone variant was used, the segmentation head architecture, and how the model was adapted for this specific patch-based pipeline.
5. **Add a simple ablation on patch size** (e.g., 512×512 vs. 1024×1024 vs. full-image resized) to empirically defend the preprocessing design choice.

## Score and Decision

The paper addresses a real industrial problem with a sensible approach, but the evaluation is substantially insufficient to support the claimed conclusions. The most critical gaps are: (a) no per-class metrics despite defining 10 component classes, (b) baseline comparison rendered uninterpretable by undisclosed training protocols, and (c) the real-time claim is unsubstantiated (per-patch vs. per-board latency is ambiguous). These are not minor presentational issues—they undermine the paper's central claims. A significant revision with substantially stronger empirical evidence would be needed for this to be publishable.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>