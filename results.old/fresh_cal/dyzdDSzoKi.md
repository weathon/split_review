Now I have a solid understanding of the paper. Let me compose the final review.

## Summary

The paper proposes the Adaptive Low-level Experts Injection (ALEI) framework for AI-generated image detection, which adaptively integrates multiple sources of low-level information (NPR, DnCNN, NoisePrint) along with RGB input using LoRA experts, cross-low-level attention, a low-level information adapter, and dynamic feature selection. Trained on only four ProGAN categories, ALEI achieves state-of-the-art results across three challenging benchmarks (AIGCDetectBenchmark, GANGenDetectionBenchmark, UniversalFakeDetectBenchmark).

## Strengths

1. **Consistent state-of-the-art results across multiple diverse benchmarks.** Tables 1–3 show that ALEI outperforms prior methods on three testbeds covering both GAN and diffusion models: +3.44% Acc on AIGCDetectBenchmark (Table 1), +2.1% Acc on GANGenDetectionBenchmark (Table 2), and +3.4% Acc on UniversalFakeDetectBenchmark (Table 3). The gains are consistent across different forgery families, not isolated to a single benchmark.

2. **Systematic component ablation validates the design.** Table 5 decomposes the 12.5% absolute accuracy gain (from 74.0% to 86.5%) across LE, CLA, LIIA, and DFS, with each component contributing a meaningful increment. The LIIA alone adds 4.4% over LE+CLA (76.1% → 80.5%), providing quantitative evidence that the low-level information adapter addresses the known problem of low-level feature loss in deep transformers (Zhao et al., 2023).

3. **Diagnostic analysis motivates the multi-expert design.** Section 3.1 evaluates six low-level features across 16 forgery types and reveals that no single feature dominates all forgeries (e.g., NPR excels on GANs while DnCNN/NoisePrint perform better on diffusion models). This data-driven finding provides a clear rationale for the paper's multi-expert, adaptive fusion approach rather than relying on any single low-level cue.

4. **Dynamic feature selection adapts to forgery type empirically.** Figure 4 uses t-SNE to show that different low-level features form distinct separation boundaries for different forgery families (StyleGAN vs. ADM), and the router's selection distribution shifts depending on forgery type, directly supporting the claim that the mechanism dynamically chooses suitable features per image.

## Weaknesses

### Fatal
None.

### Major

1. **No baseline isolating the contribution of low-level features from LoRA fine-tuning.** The paper claims a "collaborative advantage" from combining multiple low-level features, but the ablation baseline ("Late fusion + FC" in Table 5) already uses low-level features + RGB as inputs. The comparison against UnivFD (RGB-only, FC fine-tuning) is confounded because ALEI uses LoRA adapters (substantially more parameters) in addition to low-level features. The paper **does not include a baseline that fine-tunes CLIP with LoRA on RGB images alone (without any low-level input)**. Without this, it is impossible to determine how much of the reported gain comes from the low-level features versus simply from stronger fine-tuning (LoRA vs. FC-only). This directly weakens the paper's central claim that low-level information offers a collaborative advantage.

2. **Feature selection appears to be informed by test data.** The analysis in Section 3 evaluates individual low-level features on AIGCDetectBenchmark and then uses those results (via "Occam's Razor") to drop SRM, LNP, and Bayar, keeping only NPR, DnCNN, and NoisePrint. The paper then reports the main results on **the same benchmark** (Table 1). The paper does not state that a held-out validation set was used for feature selection. While the method also performs well on two other benchmarks (GANGenDetection, UniversalFakeDetect) that were not part of this selection, the AIGCDetectBenchmark results in Table 1 are subject to a data-inflation concern from this design decision. The paper should either confirm that feature selection was done on a separate validation split, or add the "all six features" result to Table 1 to show the selection did not materially affect the comparison.

### Minor

1. **Two-stage training protocol is underspecified.** Section 4.5 describes a two-stage training process (train LoRA experts + low-level encoder first, then load and train fusion module), but does not state whether the LoRA experts are frozen during stage 2. If they are not frozen, what prevents them from unlearning their modality-specific specialization? If they are frozen, the paper should say so explicitly. Similarly, it is not specified whether the ResNet50 blocks used in the low-level information adapter (Section 4.3) are ImageNet-pretrained or randomly initialized.

2. **Cross-low-level attention output reconstruction is ambiguous.** In Eq. 2, the modality features are concatenated and passed through a shared multi-head attention, but the paper does not specify how the per-modality outputs are separated afterward for processing in subsequent blocks. The notation suggests `F_{i+1}` is the concatenated output, yet individual `F_{i+1}^j` are needed per modality for the next block's LoRA expert. This operation should be clarified with an explicit reshaping step or a diagram.

3. **No variance or statistical significance reported.** All tables report point estimates from single runs. Given the pipeline's complexity (multiple LoRA experts, cross-attention, dynamic routing), the results may be sensitive to initialization or hyperparameters. Reporting standard deviations across at least 3 seeds would strengthen confidence in the reported margins.

### Trivial
None.

## Nice-to-Haves

- A parameter/inference time comparison with baselines (UnivFD, NPR) would help assess the practical cost of the additional modules.
- An analysis showing the effect of including all six vs. the selected three low-level features on the main benchmarks (beyond the ablation in Table 4) would fully address the feature-selection concern.

## Removed Points

- **Criticism about missing related works**: I cannot independently verify the completeness of related work coverage.
- **Claim that SOTA comparison is unfair because some baselines use smaller backbones**: The key competing methods (UnivFD, NPR, FAFormer) all use ViT backbones. The broader baseline list includes methods of varying backbone size for context, which is standard practice.
- **Claim that reproducibility is "severely compromised"**: While some details are missing (noted above), the paper does specify architecture choices (ViT-L, LoRA rank=4, α=8, ResNet50 blocks, Adam optimizer, learning rate, batch size, epochs). The missing details are addressable in a rebuttal and do not constitute a fatal reproducibility gap.
- **Criticism about cross-low-level attention not separating features**: This is rephrased as Minor weakness #2 with the specific ambiguity pinpointed.
- **Criticism about statistical significance being a "core flaw"**: Demoted to Minor as single-run evaluation is common in this benchmark setting.
- **Strength Finder's praise about "diagnostic analysis motivates approach" (keep)**: Kept as a legitimate strength; the analysis genuinely uncovers non-trivial behavior.
- **Strength Finder's claim that LIIA "addresses a known transformer limitation"**: Kept as a strength with quantitative evidence from Table 5.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding—that different low-level features specialize in different forgery types and that adaptive fusion outperforms any single feature—is the paper's own contribution rather than a novel synthesis from the reviews.

## Suggestions

1. **Add the critical missing baseline**: Fine-tune CLIP with LoRA on RGB-only images (no low-level features), using the same LoRA rank and training configuration. Include this in Table 5 to directly quantify the value contributed by low-level features.
2. **Clarify the feature selection protocol**: Specify whether the analysis in Section 3 used a held-out validation set. If it did not, add a version of Table 1 that includes a row with all six low-level features to demonstrate that the selection did not overfit to the test set.
3. **Clarify the two-stage training**: State explicitly which parameters are frozen in stage 2 (e.g., "LoRA experts remain fixed during stage 2 to preserve modality-specific knowledge"). Also specify whether the ResNet50 blocks in the low-level adapter are ImageNet-pretrained or randomly initialized.
4. **Clarify Eq. 2**: Add a sentence explaining how the concatenated multi-modality features are split back into per-modality representations for the next transformer block.
5. **Report variance**: Add standard deviations across 3 runs for the main comparison tables and ablation.

## Score and Decision

**Assessment by axis**:
- *Originality*: Moderate. Adaptive fusion of multiple low-level features via LoRA experts and dynamic selection is a reasonable extension of prior work, but each individual component (LoRA, cross-attention fusion, adapter) is known.
- *Importance of research question*: High. Generalizable AI-generated image detection is timely and important.
- *Claims supported*: Partially. The main claim (collaborative advantage of low-level features) lacks the necessary RGB-only+LoRA control baseline. The feature-selection protocol weakens the AIGCDetectBenchmark results.
- *Soundness of experiments*: Adequate but has gaps. The missing baseline and feature-selection concern are addressable. Single-run reporting is a limitation.
- *Clarity of writing*: Generally clear. The method description is reasonable given missing figures. The ambiguity around cross-low-level attention and two-stage training needs tightening.
- *Value to community*: Moderate. If the missing baseline is added and confirms the value of low-level features, the framework and findings would be useful.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>