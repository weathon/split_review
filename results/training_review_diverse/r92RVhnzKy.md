Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper introduces Regformer, a transformer-based method for single image deraining that uses learned spatial masks to separately attend to rain-affected and unaffected regions during attention computation. The model consists of an encoder-decoder architecture built from Region Transformer Blocks (RTBs), each containing a Region Masked Attention (RMA) mechanism and a Mixed Gate Forward Block (MGFB) for multi-scale local feature extraction. Experiments on six public datasets (Rain200L/H, DID, DDN, SPA, AGAN) show consistent PSNR/SSIM improvements over prior methods including Restormer and DRSformer, with ablation studies isolating the contribution of each component.

## Strengths

1. **Consistent state-of-the-art performance across multiple benchmarks.** Regformer achieves the best PSNR/SSIM on all six evaluated datasets, with gains of 0.20–0.28 dB on synthetic rain-streak datasets and up to 0.64 dB on the real-world raindrop dataset (AGAN-Data). The margins are small but consistent across diverse evaluation settings, which is non-trivial for a saturated benchmark.

2. **Well-structured ablation study that isolates the role of each component.** The ablation (Table 3) shows: (a) adding the RTC structure alone without masking (v3) yields only +0.01 dB; (b) adding the region mask mechanism (v4) yields +0.17 dB over the structure-only variant; (c) adding the foreground-only mask (v6) or background-only mask (v7) yields +0.20 dB and +0.17 dB respectively. This confirms that the masking mechanism, not the architectural backbone modifications, drives the performance gain.

3. **Novel combination of region-masked attention with multi-scale local processing.** The MGFB uses depthwise convolutions of different kernel sizes (3×3 and 5×5) within a gated structure, and the ablation shows it adds 0.09 dB on top of the region-masked attention (full Regformer vs. v4), confirming the two components are complementary.

4. **Efficiency–performance trade-off is explicitly demonstrated.** Figure 1(c) plots PSNR against GFLOPs and parameter count, showing Regformer achieves higher PSNR than Restormer and IDT while maintaining competitive computational cost.

## Weaknesses

### Fatal
None.

### Major

1. **The mask generation mechanism is critically underspecified regarding differentiability.** The paper's core novelty hinges on the masks computed via Eq. 2: `R = Binarize(T(I - I'))`. The binarization step produces a hard 0/1 matrix, which is non-differentiable. The paper states that "T signifies the application of dynamic thresholds" but provides no information about how T is determined (learned parameter? hand-tuned? computed from statistics of I−I'?), nor does it describe any mechanism for ensuring gradient flow through the binarization (straight-through estimator, soft relaxation, Gumbel softmax, etc.). Since the mask generation is upstream of the attention computation and the entire region-separation claim depends on it, this gap makes it impossible to assess whether the masks are genuinely learned or produced by a heuristic preprocessing step that is frozen during training. The paper must specify the exact training procedure for the mask or replace hard binarization with a differentiable approximation and justify the choice.

### Minor

2. **The "independent processing" framing modestly overstates what the architecture implements.** The abstract and introduction claim the method "independently processes" rain-affected and unaffected regions. In practice, both RTBs in the decoder take the *same* input feature map and apply complementary masks to the same Q and K (Eq. 3). This is better described as masked attention over shared features with two per-location masks, not independent processing of disjoint feature sets. The outputs are then concatenated and merged by a third RTB. The paper's actual contribution — attention with learned spatial masks that emphasize different regions — is reasonable and well-described in the method section; the framing should be adjusted to match what the architecture does.

3. **Quantitative gains are modest and reported without error bars.** The improvements over Restormer are 0.2–0.5 dB, which is within the range that could arise from training hyperparameters, random seeds, or minor architectural variations. No confidence intervals, standard deviations, or statistical significance tests are reported. While single-run evaluation is common in this subfield, the small margin of improvement relative to a strong baseline makes it important to demonstrate robustness across multiple runs or seeds.

4. **No analysis or visualization of the learned masks is provided.** The paper's central claim is that separating regions via learned masks improves deraining, yet no analysis shows what the masks actually capture: do they consistently highlight rain streaks of different scales and densities? How well do they align with ground-truth rain maps? The paper briefly acknowledges (line 111) that the threshold "cannot completely distinguish the rain region and unaffected region" but provides no failure-case analysis or quantitative evaluation of mask quality. Visualizing and analyzing the learned masks would substantially strengthen the contribution.

### Trivial

5. **The abbreviation "MGFB" is introduced but the expanded form switches between "Mixed Gate Forward Block" (abstract, Section 3.2.2 title) and "Mixed Gate Feed-Forward Block" (a plausible reading) without consistency.** This is a minor clarity issue the authors can fix in revision.

## Nice-to-Haves

- Report mean and standard deviation over at least three independent training runs to establish that the PSNR gains are robust.
- Visualize the learned masks alongside ground-truth rain maps and provide quantitative mask accuracy metrics (e.g., precision/recall against simple baselines like thresholding the difference with the ground-truth clean image).
- Test the method on a challenging real-world dataset beyond SPA-Data (e.g., RaindropCityscapes or an in-the-wild collection) where the region-differentiation hypothesis is most relevant.
- Assess whether the combined improvement could be achieved by simpler mechanisms (e.g., standard gated linear units or spatial attention with learned gating), which would clarify the marginal value of the specific binarized-mask design.
- Discuss the limitations of the mask mechanism more thoroughly, including failure cases where the threshold produces poor separation.

## Removed Points

These points were flagged by reviewers but are removed per protocol with brief justifications:

- **"ForeGround/BackGround terminology switching without clear definition":** Removed — the paper defines these terms in Figure 4 caption and Eq. 2. They are used consistently throughout.
- **"Encoder using full mask is misleadingly described":** Removed — Section 3.1 explicitly states: "Note that we directly use a tensor with all 1 values as a mask at the encoder stage, since we have not yet accessed the restored feature maps" (line 72). The statement in Section 3.2.1 ("At different stages… we employ various masking strategies") is factually correct.
- **"No methods from 2024 or later compared":** Removed per rule — the instruction explicitly prohibits raising missing related works as a weakness. The paper's comparison set (Restormer, DRSformer, IDT, Uformer, etc.) is reasonable for the era the paper is responding to.
- **"The ablation shows components contribute little in isolation":** Removed — this mischaracterizes the ablation. The paper shows that the RTC *structure without masks* (v3) adds only +0.01 dB, but the *mask mechanism itself* (v4 vs v3) adds +0.17 dB, and individual foreground/background masks (v6, v7) add +0.20 dB and +0.17 dB respectively. This actually *supports* the claim that the mask is the key contributor, not the opposite. The MGFB without RMA (v5) is expected to add little since it is designed as a complementary module.
- **"AGAN-Data comparisons are uneven":** Removed — the paper compares against 5 methods for the raindrop task, which is an auxiliary experiment. The primary focus is rain-streak removal, where the comparison set is thorough. The raindrop experiment is a demonstration of generalizability, not a comprehensive benchmark.

## Novel Insights

The most interesting signal from the reviews is that the paper's core contribution — region-masked attention — appears to be genuinely driving the performance gains, despite the individual components (the cascade structure alone, the MGFB alone) having negligible effect. The 0.17 dB jump from v3 to v4 isolates the mask's contribution, and the complementary nature of the foreground-only (+0.20) and background-only (+0.17) variants suggests that both masks are important and their combination in the full model is not redundant. This pattern is consistent with the motivating hypothesis that separate treatment of rain and non-rain regions is beneficial, but the small absolute margins leave open the question of whether a simpler learned-gating mechanism would achieve similar results. The paper would be strengthened by addressing this directly.

## Suggestions

1. **Resolve the mask differentiability issue as the top priority.** Specify whether the dynamic threshold T is learned or computed, and describe how gradients flow through the binarization step (e.g., straight-through estimator, Gumbel softmax, or a soft relaxation during training with hard binarization at inference). If the mask is produced by a differentiable approximation, state this explicitly. If hard binarization is used at training time, provide the gradient approximation method.

2. **Reframe the "independent processing" language** to match the architecture: "masked attention that emphasizes different spatial regions" rather than "independently processing regions." The contribution is still novel and useful without independent-pathway framing.

3. **Add visualizations of the learned masks** alongside input rainy images and ground-truth clean images, with discussion of what the masks capture (or miss) in challenging cases such as low-contrast rain or rain-mimicking textures.

## Score and Decision

**Originality:** 5/10 — The core idea of spatial masking within attention for deraining is reasonably novel, though conceptually the approach of separating regions via masks is incremental relative to existing masked-attention mechanisms in other domains. The MGFB multi-scale design adds modest technical novelty.

**Importance of research question:** 6/10 — Single image deraining is a well-studied but still practically relevant problem. The insight that rain-affected and unaffected regions should be treated differently is intuitively sound.

**Claims well supported:** 5/10 — The quantitative results support the claims but lack error bars. The ablation study is well-structured. The major weakness is the underspecified mask training mechanism, which undermines confidence in whether the claimed region separation is actually learned as described.

**Soundness of experiments:** 6/10 — Evaluation covers six datasets including both synthetic and real-world data. Comparisons include appropriate baselines. The ablation is informative. The lack of multiple-run statistics is the main gap.

**Clarity of writing:** 6/10 — Method description is mostly clear, but the mask generation mechanism is underspecified, and the framing slightly overstates the architectural independence of processing pathways.

**Value to the research community:** 5/10 — The idea of region-aware attention for deraining is worth disseminating, but the marginal gains and unresolved questions about the mask mechanism limit immediate impact. The code release will help.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>