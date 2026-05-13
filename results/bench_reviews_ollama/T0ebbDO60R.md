Let me now verify the key claims from the harsh critic against the paper:

1. **The $f_s$ trade-off claim**: The paper says "which can inherently achieve robustness and fidelity in a unified manner" (line 17) and introduces $f_s$ "used to balance the fidelity and robustness" (line 117). It also explicitly acknowledges in Section 3.3: "This leads to a trade-off between the robustness and fidelity, which we will explore in detail in Sec. 4.4" (line 103). So the paper actually acknowledges the trade-off exists, contradicting the framing in the intro/abstract.

2. **Section 4.4 missing**: The paper references "Sec. 4.4" for exploring the trade-off, but no Section 4.4 appears in the paper text. This is a valid concern — likely content fell in the appendix/removed sections.

3. **ZoDiac comparison**: Table 4 caption says "The corresponding results of ZoDiac are those presented in their paper." This is indeed using published numbers rather than reproduction.

4. **Robust-Wide vs SuperMark on VAE attacks**: This requires looking at Table 1 data which is an image, so I can't verify exact numbers, but the paper's own text on line 161 says "SuperMark maintains a high robustness with an accuracy of 89.29%" and doesn't single out individual attack comparisons.

5. **Conclusion claim "superior robustness compared to nearly all existing watermarking methods"**: Line 192. The paper says "nearly all" not "all," so if Robust-Wide outperforms on some attacks, the claim is slightly overstated but technically covers itself with "nearly all."

Now let me synthesize my final review.

## Summary

SuperMark proposes a training-free image watermarking framework that leverages pre-trained diffusion-based super-resolution (SR) models and DDIM Inversion for watermark embedding and extraction. By injecting watermark information into the initial Gaussian noise of the SR model's denoising process and using the SR model's conditional generation to preserve fidelity, the framework eliminates the need for joint encoder-decoder training while achieving strong robustness against both normal distortions and adaptive attacks.

## Strengths

- **Novel and practical architectural insight**: Leveraging a pre-trained conditional diffusion SR model as both embedder and extractor, with watermark information injected into the initial noise and DDIM Inversion for extraction, is a clean and practical idea. It eliminates the need for jointly trained encoder-decoder pairs and per-image optimization (unlike ZoDiac). Section 3.1 lays out the design principles clearly, and Figure 2 makes the pipeline easy to follow.

- **Strong robustness against adaptive attacks**: Table 1 demonstrates an average bit accuracy of 89.29% under adaptive attacks (VAE-based and diffusion-based), substantially higher than most baselines which fall below 55%. This is a practically important result because adaptive attacks are precisely the threat model where most existing methods fail.

- **Modular and transferable framework**: The clean separation between watermark injection methods (Gaussian Shading, Tree-Ring) and SR model backbone is well-motivated. Tables 2–4 effectively demonstrate transferability across datasets, SR models (SD-Upscaler vs. LDM-SR), and watermark injection methods, showing the framework is not tied to a single component.

- **Training-free operation**: Unlike encoder-decoder methods requiring extensive training with carefully designed differentiable distortions, and unlike ZoDiac which requires per-image optimization of initial noise, SuperMark operates without any fine-tuning or optimization, which is a genuine practical advantage.

## Weaknesses

### Fatal
None.

### Major

- **The "inherently achieve robustness and fidelity in a unified manner" claim is contradicted by the method's own formulation**: The introduction (line 17) claims SuperMark can "inherently achieve robustness and fidelity in a unified manner," implying the framework resolves the robustness-fidelity trade-off. However, Equation (2) makes this trade-off explicit: $I_{wm} = I_{ori} + f_s \times I_{res}$, where $f_s$ is a "strength factor used to balance the fidelity and robustness" (line 117). Section 3.3 further acknowledges: "This leads to a trade-off between the robustness and fidelity, which we will explore in detail in Sec. 4.4." The trade-off has simply been relocated from the training objective (in encoder-decoder methods) to an inference-time scaling parameter. The paper promises exploration of this trade-off in Section 4.4, but no such section exists in the submission. Without an $f_s$ ablation, the reader cannot assess whether SuperMark shifts the Pareto frontier or merely selects a different operating point on the same curve. This significantly undermines the core framing claim.

- **Missing distortion parameter specifications**: The experimental setting (line 147) lists distortion categories (JPEG compression, random cropping, Gaussian blur, Gaussian noise, brightness adjustments, VAE-based attacks, diffusion-based attacks) but does not specify the severity parameters (e.g., JPEG quality level, Gaussian noise standard deviation, crop ratio, blur kernel size). These parameters are critical for reproducibility and for assessing whether the tested distortions are sufficiently challenging. The headline "99.46% average accuracy under normal distortions" depends entirely on what parameters were used.

### Minor

- **Overclaiming in the conclusion**: The conclusion states "superior robustness compared to nearly all existing watermarking methods." Based on Table 1 (which we can read from the paper's narrative), Robust-Wide appears competitive on some adaptive attack categories. The "nearly all" qualifier makes this technically defensible, but the claim would be more accurate and informative if the paper explicitly acknowledged where Robust-Wide outperforms on specific attack types, providing a more nuanced characterization.

- **Only PSNR/SSIM for fidelity evaluation**: The method replaces part of the original image content with SR-generated content (governed by $f_s$), which can introduce structural changes that PSNR/SSIM may not capture well, particularly for images with fine text, small logos, or high-frequency patterns. Adding a perceptual metric (e.g., LPIPS) and showing some qualitative examples would strengthen the fidelity assessment.

- **ZoDiac comparison under mismatched conditions**: Table 4 uses ZoDiac's published numbers rather than reproducing results under identical conditions. The paper acknowledges this in the table caption ("The corresponding results of ZoDiac are those presented in their paper"). As the most comparable baseline (same noise-embedding strategy, same extraction via DDIM Inversion), a direct same-setting comparison would be more probative, though the current comparison is still informative as a reference point.

## Nice-to-Haves

- Ablation on $S_{low}$ (the low-resolution size) to show how the downscaling factor affects the fidelity-robustness trade-off along this axis.
- Qualitative visual comparisons showing $I_{ori}$, $I_{wm}$, and their difference for diverse image types (natural scenes, faces, text-containing images) to complement the PSNR/SSIM numbers.
- Failure mode analysis showing image categories where $I_{sr}^{\downarrow}$ significantly deviates from $I_{ori}$.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that baselines like CIN at ~50% are "catastrophically low" and "raises the question of whether these baselines were properly configured"**: This is speculation about implementation issues in baselines. The paper compares against open-source methods, and ~50% bit accuracy under adaptive attacks is consistent with claims in prior work that adaptive attacks effectively break most methods. This is not evidence of misconfiguration.

- **Harsh Critic's concern about extraction vulnerability to scaling/cropping attacks that "disrupt the assumed resolution relationship"**: The paper already tests random cropping as one of the normal distortions (line 147), and the results show 99.46% average accuracy under normal distortions. This suggests the framework handles at least the tested crop attacks well. The specific concern about resolution-relationship disruption is speculative and not grounded in a demonstrated failure.

- **Harsh Critic's demand for complete distortion parameters as a "methodological gap"**: While the parameters should ideally be specified, classifying this as a "methodological gap" overstates it. The distortion categories and the fact that they follow standard benchmarking practices from prior works (RoSteALS, ZoDiac) are indicated. This is more of a reproducibility nicety.

- **Strength Finder's claim about "controllable fidelity-robustness trade-off" as a strength**: This conflicts with the verified weakness that the trade-off is actually a weakness (it contradicts the "inherently unified" claim). The existence of $f_s$ is a design feature but cannot be simultaneously claimed as a strength for "controllability" and a weakness for "not resolving the trade-off." The weakness takes precedence since the paper overclaims the trade-off is resolved.

- **Harsh Critic's claim that the paper "overstates the novelty of the insight that watermark embedding/extraction parallels diffusion denoising/noising"**: The paper explicitly cites Tree-Ring and Gaussian Shading as exploiting this for in-generation watermarking (line 67). The contribution is explicitly framed as the *transfer* to post-processing via SR models, not the basic symmetry observation itself. The paper does not overstate this.

- **Harsh Critic's concern about "inference overhead" as a criticism**: The paper itself acknowledges the inference overhead in Section 3.5 (lines 133) and discusses potential solutions (model distillation, consistency models, SinSR). This is adequately addressed.

## Novel Insights

The core tension in this paper is that it makes a genuinely useful contribution — a training-free, modular watermarking framework that achieves impressive robustness against adaptive attacks — but overclaims by asserting it "inherently" resolves the robustness-fidelity trade-off, when $f_s$ explicitly parameterizes that same trade-off. The most honest characterization would be that SuperMark *decouples* robustness from fidelity in a novel way (robustness comes "for free" from DDIM Inversion properties, while fidelity is controlled separately via the SR model quality and $f_s$), which is a meaningful architectural difference from encoder-decoder methods where the two properties are entangled during training. This distinction — between entangled training-time trade-offs and decoupled inference-time control — is the paper's real conceptual contribution, but it gets buried under the stronger claim of having resolved the trade-off entirely.

## Suggestions

- Add an $f_s$ ablation sweep showing PSNR/SSIM and bit accuracy (under key distortions) for several values of $f_s$, ideally as part of the promised-but-missing Section 4.4. This is the single most important addition to validate the core claim.
- Specify the exact distortion parameters (JPEG quality, noise std, crop ratio, blur kernel) used in experiments, either in the main text or in supplementary material.
- Tone down the "inherently achieve robustness and fidelity in a unified manner" framing to more accurately reflect the contribution: e.g., "decouples the robustness-fidelity trade-off by leveraging inherent properties of DDIM Inversion for robustness and SR model conditioning for fidelity."

## Score and Decision

**Originality**: The idea of using a pre-trained diffusion SR model for post-processing watermarking, with watermark injection into initial noise and DDIM Inversion for extraction, is novel and well-motivated. The transfer of in-generation watermarking principles to post-processing is a meaningful contribution.

**Importance of research question**: Robust watermarking against adaptive attacks is a pressing practical concern, and training-free methods are highly desirable.

**Claims support**: The robustness claims are well-supported by experiments. The "inherently unified" robustness-fidelity claim is not supported, as $f_s$ explicitly parameterizes a trade-off, and the promised ablation (Section 4.4) is absent.

**Soundness of experiments**: Strong on robustness evaluation across distortion types, datasets, SR models, and injection methods. Weaker on missing $f_s$ ablation, unspecified distortion parameters, and lack of perceptual quality metrics.

**Clarity**: The pipeline is clearly explained with good figures. The overclaiming in the introduction and conclusion slightly undermines clarity of the actual contribution.

**Value to community**: High — the modular, training-free framework is practically useful and points to clear extension paths.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>