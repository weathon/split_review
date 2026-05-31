Now I have all the information I need. Let me verify the specific claims in the paper against each reviewer point, then produce the final consolidated review.

---

## Summary

This paper proposes X-PlugVid, a framework for adapting pretrained image-based spatial-control plugins (e.g., ControlNet, T2I-Adapter) to video diffusion models without per-plugin retraining. The method trains a single spatial-temporal adapter that bridges the image model (SD v1.5) to video backbones (I2VGen-XL, Hotshot-XL, SVD), augmented by a high-pass filter to remove low-frequency artifacts from the spatial prior and a timestep remapping strategy that injects later-timestep (information-richer) image features into earlier video timesteps. Experiments show compatibility with multiple plugins and backbones, and ablations isolate the contribution of each component.

## Strengths

- **Single adapter achieves universal plugin compatibility across backbones.** Table 1 shows X-PlugVid on I2VGen-XL and Hotshot-XL with both depth and canny ControlNets outperforms prior methods (Control-A-Video, ControlVideo, VideoComposer) on FID and optical flow error. Figure 7 further shows qualitative results with both ControlNet and T2I-Adapter on both backbones, demonstrating the method's generality.

- **Timestep remapping measurably improves guidance.** Table 2's ablation shows timestep remapping alone reduces optical flow error from 0.1380 to 0.0729 (a ~47% reduction). Figure 6 visualizes the effect via PCA denoising trajectories, showing that the remapping allows the adapter to provide meaningful guidance during early denoising steps where synchronized timesteps fail.

- **High-pass filtering of the spatial prior provides a small but consistent quality gain.** Table 2 shows that adding the high-pass filter on top of timestep remapping improves FID from 47.86 to 47.14 and reduces optical flow error from 0.0729 to 0.0710, confirming that removing low-frequency artifacts from the image model's feature maps prevents degradation.

- **Empirical analysis of ControlNet and X-Adapter mechanisms grounds the design decisions.** Section 3.3.1 uses feature-map similarity (Figure 2) and frequency analysis (Figure 3) to motivate why high-frequency injection is necessary and why the image model's raw feature maps contain low-quality components that must be filtered. This analysis is not merely qualitative but directly informs the adapter architecture.

- **Efficient training with modest data requirements.** The adapter is trained on only 100k text-video pairs from Panda70M for 5 epochs (Section 4.1). This supports the paper's central efficiency claim—one trained adapter replaces per-plugin retraining that would require labeled video-condition pairs for each plugin.

- **Generalization to video editing is demonstrated.** Figure 10 shows the same framework applied to video editing, indicating the method is not limited to controllable generation with spatial conditions.

## Weaknesses

### Fatal

None.

### Major

- **No direct temporal video quality metric.** The paper uses FID (per-frame) and optical flow error (condition-alignment). Neither directly measures temporal coherence—flickering, motion smoothness, or frame-to-frame consistency—which is precisely what distinguishes video generation from per-frame image generation. The paper claims "high-quality and consistent" video generation (lines 17, 278) and the temporal adapter is a key contribution, yet the evaluation does not include a standard video-level metric like FVD (Fréchet Video Distance) or a temporal consistency score. The optical flow error only checks whether the generated spatial structure matches the input condition; it does not assess whether the temporal dynamics are realistic. This weakens the evidence for the core claim of producing *consistent* videos. *Evidence: Section 4.3 lines 168-169 list only FID and optical flow error as metrics.*

- **Comparison set is narrow and lacks a simple per-frame baseline.** The paper compares against ControlVideo, Control-A-Video, and VideoComposer. While these are the most directly relevant prior works, the evaluation would be substantially stronger with the inclusion of: (a) a trivial baseline that applies the image ControlNet independently to each frame with no temporal modeling (to isolate the benefit of the temporal adapter), and (b) methods that train video-temporal ControlNets from scratch (as an upper bound). Without these, the claim that the temporal adapter is responsible for the gains (rather than the spatial ControlNet alone) is plausible but not definitively established.

### Minor

- **High-pass filter implementation is underspecified.** Section 3.3.2 defines the filter as \(\mathcal{H}()\) but does not specify the filter type (e.g., ideal, Gaussian, Butterworth), cutoff frequency, kernel size, or whether it is applied in the spatial or frequency domain. This omission makes reproduction dependent on guesswork. *Evidence: lines 95-101 define the operation formally but only say "high-pass filter."*

- **Quantitative results lack confidence intervals or significance tests.** In Table 1, differences between methods are small (e.g., FID 71.05 vs. 71.25). Without error bars across the 2000-sample validation set, it is unclear whether these differences are statistically meaningful. *Evidence: Table 1, lines 167-169 describe the evaluation setup but no error bars are reported.*

- **Generalization claim in Section 5.1 is unquantified.** The paper states "we implement timestep remapping and high-pass filter upon X-Adapter and achieve better results" for image model upgrade, but provides no quantitative comparison. This reads as a promissory note rather than demonstrated generalization. *Evidence: lines 253-254.*

- **Computational cost is not reported.** The paper argues for efficiency over per-plugin retraining but does not report training time, inference overhead (e.g., additional latency per frame), or the number of added parameters in the adapter. These numbers would concretely substantiate the efficiency claim. *Evidence: Section 4.1 mentions "4 NVIDIA A100 GPUs" and 5 epochs but no training duration.*

- **Failure cases and limitations are underexplored.** Section 5.2 discusses identity/style plugins as future work but does not analyze where the current method fails (e.g., complex motions, extreme viewpoint changes, long videos). Including a failure analysis would improve credibility.

### Trivial

None.

## Nice-to-Haves

- **Broader cross-condition evaluation.** Testing on a condition type not seen during training (e.g., segmentation map, sketch) would strengthen the "universal compatibility" claim beyond the two conditions (depth, canny) tested.
- **Ablation on the number/location of mapping layers beyond encoder vs. decoder.** The paper tests encoder vs. decoder placement but does not ablate the specific configuration used (middle block + first three decoder blocks) vs. alternatives.
- **Analysis of long-range temporal modeling** (e.g., beyond 16 frames) would clarify the limitations of the temporal attention module.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that timestep remapping is "ad hoc" and the n parameter makes the method "fragile":** The paper provides an extensive ablation on n (Table 2, Figure 8, with n=1,2,4,1000), includes qualitative visualization (Figure 9), and explicitly states "n=2 is suitable in most cases." The method is studied, not assumed. The sensitivity is characterized, not hidden.
- **Criticism that the ablation for "where to insert mapping layers" is incomplete:** The paper tests the two main architectural choices (encoder vs. decoder), finds decoder clearly better, and uses that result. A more granular ablation would be nice but is not a deficiency given the clear finding.
- **Criticism about training data scale leading to overfitting:** Speculative. The paper shows generalization across two backbones and two condition types, suggesting the method is not overfit to a specific motion pattern. The validation set being from the same distribution as training is standard practice.
- **Criticism demanding comparison with VideoControlNet (which trains temporal ControlNets from scratch):** VideoControlNet requires per-plugin retraining, which is the opposite paradigm from this paper's contribution. The paper cites it for the metric, which is appropriate.
- **Strength Finder's claim about "state-of-the-art results":** The paper reports improvements over the chosen baselines, but without a broader comparison set and error bars, "state-of-the-art" is not conclusively established. This strength is removed to avoid overclaiming.

## Novel Insights

None beyond the paper's own contributions. The key insight—that the image diffusion model's feature maps at later timesteps contain richer spatial information that can be remapped to earlier video timesteps for better guidance—is the paper's central contribution and is well-supported by analysis. The reviews do not surface any unrecognized insight beyond what the paper already claims.

## Suggestions

1. **Add a temporal video quality metric** such as FVD or a per-video consistency score (e.g., CLIP temporal similarity, warping error) to the main evaluation. This directly tests whether the temporal module and timestep remapping produce coherent videos.
2. **Include a per-frame ControlNet baseline** (applying the spatial ControlNet independently to each frame without temporal modeling). This cleanly isolates the contribution of the temporal adapter.
3. **Report confidence intervals or error bars** on all quantitative results (Table 1, Table 2) to establish significance of the reported gains.
4. **Specify the high-pass filter implementation** (filter type, parameters, domain of application) to aid reproducibility.
5. **Report training time, inference overhead, and parameter count** for the adapter to substantiate the efficiency claim quantitatively.
6. **Include a brief failure analysis** discussing cases where the method struggles (complex motion, extreme viewpoint changes) to improve credibility.

## Score and Decision

**Originality:** Good. The task of reusing image plugins for video models without per-plugin retraining is well-motivated and not previously solved. The timestep remapping is a novel and clever idea grounded in analysis.

**Importance of research question:** High. Reducing the training burden for controllable video generation has practical value given the abundance of image plugins and the scarcity of video-condition data.

**Claims supported:** Moderately. The core claim of compatibility across plugins and backbones is supported. The claim of "high-quality and consistent" video generation is partially supported but weakened by the absence of a temporal video metric and narrow baseline set.

**Soundness of experiments:** Adequate but improvable. Ablations are well-designed and isolate each component. But the evaluation lacks a video-level temporal metric, error bars, and a per-frame baseline, which collectively weaken the experimental rigor.

**Clarity of writing:** Clear. The method is well-structured, the analysis of ControlNet and X-Adapter is accessible, and the figures effectively communicate the ideas.

**Value to community:** Moderate to high. The framework could enable practical reuse of the large ecosystem of image plugins for video generation, which would be valuable to practitioners.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>