Now I have a thorough understanding of the paper. Let me synthesize the final review, cross-checking every claim against the paper text.

---

## Summary

X-PlugVid proposes a framework to adapt pretrained image-based spatial-control plugins (e.g., ControlNet, T2I-Adapter) for use with video diffusion models by training a single generic adapter rather than retraining each plugin per video backbone. It introduces a spatial-temporal adapter with a high-pass filter and a timestep remapping strategy. Experiments on I2VGen-XL and Hotshot-XL with depth and canny conditions demonstrate compatibility across plugins and backbones.

## Strengths

- **First framework to train a single generic adapter enabling all spatial-control image plugins on video models without per-plugin retraining** – The paper defines this as a new task (Section 1, Figure 1) and contrasts with prior work that requires per-plugin retraining or lacks transferability. Evidence: the method works with both ControlNet (depth, canny) and T2I-Adapter on two different video backbones (I2VGen-XL and Hotshot-XL) in Figure 7, using one trained adapter.

- **Novel timestep remapping strategy with clear ablation support** – The insight that later timesteps of the image model contain richer information and should be mapped to earlier video timesteps is well-motivated by the denoising trajectory analysis (Figure 6). The ablation in Table 2 (described in Section 4.4) quantitatively shows that remapping with n=2 significantly improves outcomes over synchronous mapping (n=1), and Figure 8 provides visual confirmation. This is a genuine methodological contribution.

- **Mechanistic analysis of ControlNet and X-Adapter that directly drives design choices** – The frequency analysis (Figure 3) showing ControlNet outputs are dominated by high frequencies, and the feature-map similarity analysis (Figure 2), motivate both the high-pass filter (to suppress low-quality low-frequency components from the diffusion prior) and the per-step injection design (to match ControlNet's behavior). The ablation confirms that high-pass filtering improves results.

- **Demonstrated generalization beyond controllable video generation** – Section 5.1 shows the high-pass filter and timestep remapping also improve X-Adapter's image-model upgrade task, and the method applies to video editing (Figure 10). This confirms the contributions are not task-specific.

## Weaknesses

### Fatal
None.

### Major

- **The quantitative comparison against prior methods is confounded by different backbones and does not isolate the proposed method's contribution.** Table 1 compares X-PlugVid (built on I2VGen-XL or Hotshot-XL) against ControlVideo, Control-A-Video, and VideoComposer—methods originally developed for different base models (typically Stable Diffusion). The paper does not reimplement those baselines on the same video backbones or provide a same-backbone baseline (e.g., per-frame ControlNet injection into I2VGen-XL/Hotshot-XL without the proposed temporal adapter). As a result, the reported improvements in FID and optical flow error could be partially driven by the quality of the backbone rather than by the proposed adapter or timestep remapping. The comparison against the original backbones (I2VGen-XL, Hotshot-XL without control) only shows that the method does not degrade native generation—it does not isolate the advantage over alternative control methods on equal footing. This weakens the claim that X-PlugVid "surpasses previous methods."

### Minor

- **The evaluation metrics, while defensible, are not the most standard for video generation, and one metric's interpretation is underspecified.** The paper uses FID (comparing generated videos to original Panda70M videos) and optical flow error (L2 distance between optical flow of input and generated video). The paper correctly uses FID as a distributional metric (not a paired metric as the reviewer incorrectly claimed), but FVD (Frechet Video Distance) is the more standard metric for video generation quality and accounts for temporal structure. The optical flow error, cited from VideoControlNet, is reasonable for measuring spatial control fidelity, but the paper does not discuss its limitations (e.g., penalizing condition-consistent motions that differ from the input video's specific motion). The core claims are not invalidated by these metric choices, but adopting FVD and/or a human evaluation would substantially strengthen the evidence.

- **The high-pass filter and temporal attention module lack architectural specification.** The paper introduces a temporal attention module (Section 3.3.2) to ensure temporal coherence but does not specify its structure (e.g., number of heads, whether it is causal, how frames are aggregated, where it is inserted relative to existing layers). Similarly, the high-pass filter \( \mathcal{H}() \) is invoked in the formulation (Equation 1) but its type (e.g., spatial kernel, Fourier-based, learned or fixed) and parameters are never defined. These omissions are not fatal—these are standard components in the video diffusion literature—but they hamper reproducibility.

- **The timestep remapping assumes both models share the same total timesteps \( T \).** The remapping function \( t_{img} = \lceil t_{vid} / n \rceil \) implicitly assumes the image diffusion model and the video diffusion model use the same total number of timesteps \( T \) and the same noise schedule (e.g., both DDIM with equal steps). If the two backbones use different schedulers (e.g., DDIM vs DDPM, different numbers of steps), the remapping may not be directly applicable. The paper does not discuss this assumption or its implications.

- **The ablation study's quantitative results (Table 2) would benefit from using the same clearly defined metrics as Table 1.** The paper defines FID and optical flow error as evaluation metrics in Section 4.3. The ablation (Section 4.4) should explicitly state that it uses the same metrics rather than leaving the reader to infer this from context.

### Trivial
- The generalization to SVD is mentioned in Section 4.1 ("Notice that we also train our method for SVD") but SVD results are not shown in the quantitative comparisons—only briefly mentioned. Either including them or clarifying their omission would be cleaner.

## Nice-to-Haves
- FVD as an additional evaluation metric to align with video generation community standards.
- A same-backbone baseline (e.g., per-frame ControlNet injection into I2VGen-XL/Hotshot-XL with no temporal adapter) to isolate the benefit of the temporal modeling and timestep remapping.
- A brief discussion of how the timestep remapping generalizes to backbones with different total timesteps or noise schedules.
- Statistical significance or variance estimates for quantitative results (common in the field but helpful given the moderate training set size).

## Removed Points

- *"FID is used as a paired metric"* — REMOVED as factually wrong. FID compares distributions, not paired samples. The paper correctly describes it as measuring distribution distance.
- *"Optical flow error may penalize creative motions" (as a critical issue)* — DOWNGRADED to minor. The concern has some validity but the metric is from prior work (VideoControlNet, cited), and for spatial-control evaluation, faithfulness to the input structure is a reasonable criterion.
- *"ControlNet analysis is purely qualitative"* — REMOVED as a weakness. The paper explicitly uses this analysis as motivation for design choices, not as proven claims. This is standard for the motivational analysis in Section 3.3.1.
- *"The claim that previous works lack flexibility is overstated"* — REMOVED. The paper's characterization of prior work (per-plugin retraining required, difficulty transferring across backbones) is substantially accurate.
- *"Missing statistical significance"* — DOWNGRADED to nice-to-have. Single-run evaluation is standard in this field.
- *"Temporal consistency metric undefined"* — REMOVED. Cannot be verified from the available text; the paper only defines FID and optical flow error as metrics. If the table uses those same metrics for the ablation (which the text surrounding it implies), there is no undefined metric.
- *"Missing appendix/proofs"* — REMOVED per rules about parser-stripped sections.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the comparison issue head-on in a revision**: Add a controlled baseline that applies the image ControlNet per-frame to the same video backbone (I2VGen-XL or Hotshot-XL) with simple feature addition, and compare against X-PlugVid. Even a simple baseline would help isolate the benefit of the temporal adapter and timestep remapping.
2. **Add FVD as an evaluation metric** to align with standard video generation evaluation and to address concerns about FID's sufficiency for video quality assessment.
3. **Specify the high-pass filter type and temporal attention architecture** (number of heads, causal vs. bidirectional, frame aggregation method) either in the main paper or a supplementary document.
4. **Explicitly state in the ablation section** that Table 2 uses the same FID and optical flow error metrics defined in Section 4.3.
5. **Discuss the assumption about shared timesteps \( T \)** and how the method handles models with different schedulers or step counts.

## Score and Decision

The paper addresses a practical and timely problem—reusing the rich ecosystem of image control plugins for video generation without expensive retraining. The core contributions (single-adapter framework, timestep remapping, high-pass filtering) are well-motivated by analysis and validated by ablation studies. The qualitative results convincingly demonstrate compatibility across multiple conditions and backbones. However, the quantitative comparison against prior methods is weakened by different backbone conditions, which undermines the strongest comparative claims. The missing architectural details and the lack of FVD are addressable issues. Overall, the paper has genuine contributions that are reasonably supported, but the evaluation has a notable gap.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>