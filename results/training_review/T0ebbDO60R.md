Now I have all the information I need. Let me carefully synthesize the review, verifying each claim against the paper.

---

## Summary

SuperMark proposes a training-free image watermarking framework that repurposes pretrained diffusion-based Super-Resolution (SR) models. Watermarks are embedded into the initial Gaussian noise fed to the SR model; the denoised SR output is then combined with the original image via a residual addition to produce the watermarked image. For extraction, DDIM inversion is applied to reconstruct the initial noise, from which the watermark is decoded. The framework is modular, accepting different watermark injection methods (Gaussian Shading, Tree-Ring) and different SR models without fine-tuning. Experiments report 99.46% bit accuracy under normal distortions and 89.29% under adaptive attacks, with fidelity comparable to baselines (PSNR 32.49, SSIM 0.93).

## Strengths

- **Training-free, modular design:** SuperMark requires no training and integrates off-the-shelf watermark injection methods (Gaussian Shading, Tree-Ring) and pretrained SR models (SD-Upscaler, LDM-SR). The paper demonstrates this flexibility through transfer experiments across two injection methods (Sec. 4.3, Tables 3–4) and two SR models, all with frozen weights. This is a practical advantage over trained encoder–noise-layer–decoder methods.

- **Strong empirical robustness across diverse attacks:** On the MS-COCO benchmark (Table 1), SuperMark achieves 99.46% average bit accuracy under normal distortions (JPEG, cropping, blur, noise, brightness) and 89.29% under adaptive attacks (Bmshj18, Cheng20, Zhao23, InstructPix2Pix), substantially outperforming all nine baselines on robustness. Under adaptive attacks where most baselines degrade severely (e.g., DwtDctSvd at ~50%, RoSteALS at ~65%), SuperMark maintains 89.29%, supporting the core claim of resilience.

- **Clear motivation and problem identification:** The paper correctly identifies that the standard encoder–noise-layer–decoder architecture creates a tension between robustness and fidelity that joint training cannot resolve (Sec. 1, Fig. 1), and offers an alternative paradigm that decouples these objectives by leveraging pretrained diffusion models.

## Weaknesses

### Fatal
None.

### Major

- **Missing distortion parameters and attack configurations prevent reproducibility and fair comparison.** The paper lists normal distortions (JPEG compression, random cropping, Gaussian blur, Gaussian noise, brightness adjustments) and adaptive attacks (Bmshj18, Cheng20, Zhao23, InstructPix2Pix) but provides no parameter values — no JPEG quality factor, crop ratio or protocol, kernel size, noise variance, compression level for VAE attacks, or editing strength for InstructPix2Pix. Without these, the reported 99.46% and 89.29% bit accuracies cannot be reproduced, compared with baselines run under identical conditions, or assessed for practical significance (e.g., is the cropping a mild center-crop or aggressive random crop?). This is the most significant weakness because it undercuts the paper's primary evidence.

- **ZoDiac comparison (Table 4) is not a controlled evaluation.** The paper states "The corresponding results of ZoDiac are those presented in their paper." This means the comparison likely uses different dataset splits, distortion parameters, or evaluation protocols. The claimed advantage in fidelity (PSNR 29.44 vs. 24.75) and rotation robustness may partly reflect these differing conditions rather than a genuine improvement. A fair comparison requires running ZoDiac's code on the same images and under the same distortion pipeline.

- **No analysis of DDIM inversion accuracy for the modified image pipeline.** The watermarked image is not a direct SR model output — it is a composite: \( I_{wm} = I_{ori} + f_s \times (\text{downscale}(\text{SR}(...)) - I_{ori}) \). Extraction upscales this composite, encodes it, and applies DDIM inversion. The paper does not measure the reconstruction error between the original watermarked noise \( Z_{wm}^T \) and the recovered noise \( Z_{wm}^{'T} \), even under no distortion. While the high bit accuracy suggests the inversion works, this is a critical missing diagnostic. Without it, one cannot distinguish between high-fidelity watermark recovery and a scenario where the extraction is accidentally robust due to redundancy in the injection scheme rather than faithful inversion.

### Minor

- **Only average robustness reported, no per-distortion breakdown (Table 1).** A reader cannot tell whether SuperMark is uniformly strong across all distortions or excels on a few while being merely adequate on others. For instance, DwtDctSvd may be robust to JPEG but weak against adaptive attacks; the averages conceal such profiles. A supplementary table with per-distortion results is needed.

- **Insufficient rationale for the residual addition design (Eq. 2–3).** The paper explains *that* downscaling the original image before SR reduces the size discrepancy, but does not formally justify *why* the residual addition (\( I_{ori} + f_s \times (I_{sr}^\downarrow - I_{ori}) \)) is superior to alternatives (e.g., directly using the downscaled SR output as the watermarked image, or embedding in a different domain). An ablation study comparing pipeline variants would substantiate the design choices.

- **The claim of "inherent robustness of DDIM inversion" is cited from prior work on *in-generation* watermarking (Wen et al., Yang et al.) but not validated for this composite-image setting.** While the empirical results are consistent with robustness, the paper does not verify that DDIM inversion's known robustness properties transfer to inputs that have undergone the downscale–SR–residual–addition pipeline. The discussion in Sec. 3.5 correctly notes that "Inversion accuracy" matters, but no quantitative measurement is provided.

### Trivial
None.

## Nice-to-Haves

- An ablation study varying the strength factor \( f_s \) (currently fixed at 0.4) and low-resolution size \( S_{low} \) (currently 128), with plots of the robustness–fidelity trade-off.
- Inference time comparison with baselines, since SuperMark requires 25 DDIM sampling steps + 25 DDIM inversion steps, which is computationally heavier than feed-forward baselines.
- Visual examples of watermarked images side-by-side with baselines, and failure cases under strong distortions.

## Removed Points

*These points were flagged as invalid or not applicable after verification against the paper.*

- **Criticism that the paper does not "formally demonstrate" the robustness–fidelity disentanglement claim:** The paper presents this as an observation motivating the approach, not a formal theorem. It is a reasonable motivation, not a required proof.
- **Claim that \( f_{sr} = f_{vae} \) is confusing:** The paper's explanation in Sec. 2.2 is clear — the SR model's magnification factor equals the VAE's input-to-latent scaling factor.
- **Criticism that 428–500 images is a small sample:** This sample size is standard for watermarking evaluation benchmarks (consistent with RoSteALS, ZoDiac). No evidence of high variance is provided.
- **Claim that the conclusion "overstates" validation:** This is a subjective style judgment. The paper's claims are broadly supported by the experiments presented (though the missing details weaken them).
- **Criticisms about missing Sec. 4.4 (ablation on \( S_{low} \)):** The paper explicitly references Sec. 4.4 for this analysis ("which we will explore in detail in Sec. 4.4"). This section was likely in the original submission's appendix and stripped by the parser.
- **Strength from Strength Finder about "clear identification of a limitation in prior approaches":** This is generic and conflicts with the verified weakness that the claim is never formally demonstrated. Moved here because it overstates what is essentially a motivational observation.

## Novel Insights

The harsh critic's most penetrating observation is that SuperMark's pipeline is structurally asymmetric: the watermark is embedded into the SR model's noise, but the final watermarked image is a composite (original + scaled residual of the downscaled SR output), not a direct SR output. The extraction must then invert this composite through upscaling, VAE encoding, and DDIM inversion. The paper never verifies that the inversion error in this specific setting is low enough to faithfully recover the watermark — it assumes the 99.46% bit accuracy speaks for itself, but without a direct measurement of \( \|Z_{wm}^T - Z_{wm}^{'T}\| \), one cannot rule out that the watermark survives extraction not because of faithful inversion but because the injection method (e.g., Gaussian Shading) has enough redundancy to tolerate substantial reconstruction noise. This is a genuine gap that should be addressed with a simple diagnostic experiment. Additionally, the ZoDiac comparison problem — using published numbers rather than a controlled re-evaluation — is a common but serious flaw that weakens the paper's strongest comparative claim.

## Suggestions

1. **Report per-distortion robustness and full attack parameters** in a supplementary table. Specify JPEG Q, crop ratio and protocol (center-crop or random), Gaussian blur kernel size and σ, Gaussian noise σ, and the exact model checkpoints and compression levels for adaptive attacks.
2. **Measure and report DDIM inversion reconstruction error** (MSE or PSNR between original and recovered noise latents) under no distortion and under each distortion type. This directly validates the core assumption that the inversion works on the composite image.
3. **Re-run ZoDiac using its official code** under the same image set and distortion pipeline for a fair head-to-head comparison.
4. **Add an ablation study** comparing the full pipeline against variants (e.g., no residual addition, direct downscaling of SR output, varying \( f_s \) and \( S_{low} \)) to justify each design choice.

## Score and Decision

The paper presents a genuinely novel idea with strong empirical results that support its core claims. The training-free, modular design is a clear contribution. However, the evaluation lacks critical experimental details (distortion parameters, per-distortion breakdown), the signature comparison with ZoDiac is uncontrolled, and a key diagnostic (inversion reconstruction error) is missing. These are addressable weaknesses that do not invalidate the core contribution but must be fixed for the paper to be accepted at a venue that values reproducibility and rigorous evaluation. The paper does not suffer from fatal flaws.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>