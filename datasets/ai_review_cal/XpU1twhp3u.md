- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

---

## Summary

MatchMask proposes a mask-centric generative data augmentation pipeline for label-scarce semantic segmentation. It consists of (1) a Gradient Probe Method that identifies critical layers in pre-trained diffusion models by measuring parameter changes during early fine-tuning, (2) a Layer-Timestep Adaptive Adapter (LT-Adapter) with only 0.7M trainable parameters that enables few-shot semantic image synthesis via layer-adaptive cross-attention fusion and timestep-adaptive LoRA scaling, and (3) a relative filtering strategy that uses majority voting across multiple generated images to suppress artifacts. Experiments on VOC, COCO, and ADE20K show consistent improvements over baselines and existing text-centric augmentation methods, and the MatchMask++ extension integrates with semi-supervised methods like Unimatch to approach fully-supervised performance.

## Strengths

- **Mask-centric generation substantially outperforms text-centric approaches that use orders of magnitude more synthetic data.** The paper shows (Table 2) that MatchMask using ~1–2k synthetic images achieves results far exceeding text-centric methods (DatasetDiffusion, DatasetDM) using 40k images. This directly supports the core claim that mask-conditioned generation produces more informative and better-aligned training pairs for segmentation.

- **The Gradient Probe Method reveals that critical layers are consistent across different datasets.** Figure 3 visualizes importance scores across ADE and VOC, showing that the same small subset of layers (primarily time-embedding and cross-attention layers in high-resolution blocks) are consistently salient. This empirically validates the claim that only a minority of parameters are critical for spatial control and that the finding generalizes.

- **LT-Adapter enables few-shot semantic image synthesis without overfitting.** Figure 2 shows that full fine-tuning (FreestyleNet) diverges rapidly on 200 ADE20K samples, while LT-Adapter maintains low FID and generates diverse images. The parameter count (0.7M) is clearly stated, demonstrating genuine parameter efficiency.

- **The relative filtering strategy outperforms confidence-based filtering.** Table 6 shows that the proposed majority-voting filtering improves results over confidence-based filtering, validating the approach's robustness to confirmation bias in the segmentation model.

- **Integration with existing semi-supervised methods boosts performance and approaches fully-supervised baselines.** Table 5 shows Unimatch improves from 78.3% to 79.6% mIoU on VOC with 366 labels when augmented with MatchMask, nearly matching the fully-supervised 79.9% — a practically significant result.

- **Comprehensive ablation of LT-Adapter components.** Table 7 isolates the contributions of layer-adaptive fusion and timestep-adaptive LoRA scaling, showing that both independently improve DINO similarity and mIoU, and their combination is best.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation of the layer selection itself.** The paper claims the Gradient Probe identifies critical layers that are important for adaptation, but never compares against baselines that would validate this: (a) applying the same LoRA adapter to *all* candidate layers (e.g., all cross-attention projections), or (b) selecting a random subset of layers of the same size. Without this, the reader cannot determine whether the probe genuinely adds value over a simpler default LoRA application. This is the most significant evidential gap — it directly affects the paper's claim about the necessity and utility of the probe.

### Minor

- **Comparison to text-centric methods is not fully controlled.** Table 2 compares MatchMask (which fine-tunes the diffusion model on the few labeled samples) against text-centric methods like DatasetDiffusion and DatasetDM that generate data zero-shot without using those labeled samples. The performance gap could partially reflect the benefit of target-domain fine-tuning rather than the mask-centric paradigm alone. A controlled experiment where a text-centric method is allowed to use the same few labeled samples (e.g., for prompt tuning or model adaptation) would better isolate the effect of mask conditioning. The paper mentions none of this nuance.

- **No error bars or standard deviations reported.** In a few-shot regime with tiny labeled sets (e.g., 92–732 samples on VOC), results can be noisy. Reporting single runs without variance reduces confidence in the measured gains. Standard practice for this setting (semi-supervised segmentation) is to report mean and std over 3+ seeds.

- **Reproducibility: LoRA rank and architecture details not specified.** The paper does not state the LoRA rank *d*, nor does it describe the architecture of the linear layers that predict the adaptive fusion parameter α and the timestep scaling factor β. These details are needed to reproduce the 0.7M parameter count and the method itself.

- **Sensitivity of the Gradient Probe to hyperparameters is not analyzed.** The probe's importance scores depend on the number of fine-tuning steps, learning rate, and early stopping criterion. The paper states that important layers "stabilize after a few epochs" (Figure 3), but does not analyze how these choices affect the set of selected layers. A layer could have small parameter changes yet still be functionally critical — this limitation of gradient-based importance measures is not discussed.

- **Potential circularity in using the same data for probe and training.** The Gradient Probe fine-tunes the full U-Net on the few labeled samples to identify critical layers, and the LT-Adapter is then trained on those same samples. This means the selection is evaluated only on the data that determined it. The paper partially addresses this by showing cross-dataset consistency (Figure 3), but does not demonstrate that the selected layers would hold up on a held-out subset or that the selection is not an early-training artifact on a tiny dataset. This is not a fatal flaw (splitting the already-tiny labeled set would be impractical), but the paper could strengthen this point with additional analysis.

### Trivial

- No discussion of limitations or potential failure cases (e.g., scenarios where relative filtering might fail, such as when the segmentation model is extremely biased and all K predictions agree on the wrong label).

## Nice-to-Haves

- A brief computational cost comparison between MatchMask (requires 100k iterations of LT-Adapter training on an A100) and zero-shot text-centric generation methods would help practitioners assess the practical trade-offs.
- A comparison or discussion of FreeMask (Yang et al., 2024), which also uses mask-based generation but for the fully-supervised setting, would strengthen the positioning.
- A no-filtering baseline in Table 6 (if not already present — the table is image-embedded and its exact content cannot be verified from the text) would help quantify the absolute benefit of filtering.

## Removed Points

These points were raised in the reviews but removed after verification against the paper:

- *"No no-filtering baseline in Table 6"* — The table is embedded as an image and cannot be verified from the paper text. The paper's discussion mentions comparing "relative filtering" against "confidence-based filtering," but whether a no-filtering row is included cannot be confirmed from the text alone. Removed due to unverifiability.
- *"Missing comparison to FreeMask"* — FreeMask is discussed in Related Work and acknowledged as designed for the fully-supervised setting. Criticizing its absence in a label-scarce paper is scope creep.
- *"Paper does not discuss recent work that mitigates text-centric limitations"* — This is a speculative "missing related work" criticism, which the instructions forbid.
- *"Reproducibility concern about undisclosed hyperparameters / large artifacts"* — The instruction explicitly removes such nitpicks as they are routine for conference submissions.
- *"Missing appendix / references"* — The parser strips appendices; they exist in the original submission.
- *"Garbled table rendering"* — This is a parser artifact, not an author error.

## Novel Insights

The reviews do not surface a genuinely novel insight beyond the paper's own contributions. The Gradient Probe's finding that critical layers are dataset-agnostic and concentrated in high-resolution blocks is itself the most novel observation; the reviews confirm its value but do not add to it.

## Suggestions

1. **Add the missing layer-selection ablation.** Compare: (a) probe-selected layers + LT-Adapter, (b) LoRA applied to all candidate layers (same adapter design), (c) random subset of layers of equal size. This single experiment would directly validate the probe and is the most impactful addition the authors could make.
2. **Add a controlled text-centric baseline** that uses the few labeled samples (e.g., fine-tune SD with BLIP captions on those samples, then generate). This isolates mask conditioning from the benefit of fine-tuning.
3. **Report standard deviations over 3+ random seeds** for the main experiments, especially on VOC and COCO in the few-shot regime.
4. **Specify the LoRA rank d** and describe the architecture of the α/β prediction networks in the main paper or supplement.
5. **Include a brief limitations paragraph** acknowledging potential failure cases (e.g., when the segmentation model is extremely biased, causing relative filtering to also fail).
