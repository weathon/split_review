# Review of "Adaptive Log-Exp Perturbations for Secure AI Image Compression"

## Summary
This paper proposes a luminance-adaptive adversarial perturbation for neural image compression, using the nonlinear function I' = log(exp(I) + n) whose Taylor expansion yields δI = n·exp(-I) — applying more perturbation to dark pixels and less to bright pixels. The motivation is grounded in Weber's Law from visual psychophysics. An attack (maximizing output distortion via high-entropy region targeting) and a defense (learning corrective noise to restore quality) are evaluated on the Kodak dataset using Cheng2020-anchor and TCM compression models.

## Strengths
- **Clean mathematical formulation**: The log-exp function yields a simple, differentiable closed-form perturbation δI = n·exp(-κI) with a single parameter κ. The derivation is straightforward and easily implementable.
- **Non-trivial attack effectiveness on TCM**: The attack degrades decompressed PSNR from 38.66 dB to 22.89 dB (13.77 dB drop) while maintaining PSNR(original, attacked) of 47.21 dB — genuinely small-magnitude perturbations that still disrupt a state-of-the-art hybrid architecture.
- **Defense recovery on TCM**: The corrective-noise defense restores PSNR from 22.89 dB to 37.89 dB, closely approaching the 38.66 dB undefended baseline on a modern Transformer-CNN model.
- **Cross-architecture evaluation**: The method is tested on two structurally distinct architectures (Cheng2020-anchor VAE with residual blocks, TCM Transformer-CNN hybrid), showing the perturbation generalizes beyond a single model family.

## Weaknesses

### Major
- **Weber's Law motivation is contradicted by the paper's own data, leading to the wrong adaptation direction.** The paper claims (line 4, lines 100–102) that because "the human eye is less sensitive to variations in dark areas," more noise should be added there. However, the paper's own Weber's Law examples (lines 60–62) give absolute JND values: at 0.001 mL, δI = 0.0002; at 1 mL, δI = 0.02. The absolute JND is **100× larger in bright regions**, meaning the eye tolerates far more absolute noise in bright areas. The log-exp perturbation applies the opposite pattern (δI ≈ n in dark vs. δI ≈ 0.37n in bright), putting more perturbation where absolute sensitivity is highest. The paper confuses relative sensitivity (δI/I, the Weber ratio) with absolute perturbation tolerance — a category error, since the perturbation operates in absolute pixel space, not proportional space. This undermines the paper's central claim of perceptually motivated imperceptibility. (Verifiable from lines 60–62 and 100–102 of the paper.)

- **No controlled comparison against additive noise with equal perturbation budget.** The paper (line 215) admits "Additive Noise degrades the performance more than Log-Exp Noise" — i.e., it produces a larger PSNR drop in the decompressed output. The log-exp method produces both a weaker attack AND a higher PSNR between original and attacked images. This is a trivial trade-off: any attack with smaller perturbations will be less destructive and less visible. The paper never holds the L2 or L∞ norm of the perturbation equal between methods and then compares the resulting trade-off. Without this control, the experiment cannot isolate whether the luminance-adaptive *distribution* of noise (as opposed to its smaller overall magnitude) provides any benefit. The headline comparison is uninformative.

- **No comparison against any existing adversarial attack methods.** Section 2.1 surveys FGSM, PGD, BIM, C&W, and Wasserstein attacks; Section 2.2 specifically discusses Chen & Ma (2021)'s PGD-based attack on compression models. Yet none of these are used as baselines. The only comparison is against an "Additive Noise" baseline whose noise budget and optimization procedure are not fully described. Without comparisons to known methods from the literature the paper itself cites, the paper cannot demonstrate an advantage over the existing state of the art.

- **No ablation study disentangling the log-exp function from the masking/shrinking procedure.** The attack pipeline on Cheng2020-anchor includes: (1) superpixel-based high-entropy region selection, (2) Gaussian smoothing with σ=21, (3) iterative mask shrinking, and (4) the log-exp perturbation itself. The paper never evaluates "log-exp without mask" vs. "additive noise with the same mask" on comparable settings. The contribution of the luminance-adaptive perturbation cannot be separated from the sophisticated masking procedure. Different procedures are even used across models (masked for Cheng, unmasked for TCM), making cross-model comparisons uninterpretable.

### Minor
- **Evaluation on a severely limited image set with no statistical rigor.** Detailed results on Cheng2020-anchor are shown for a single image (kodim19). Broader Cheng results (Tables 2–3) are reported as images that cannot be read as text; the only numerical discussion in text references averages without variance. For the TCM model, only 3 images are tested. No error bars, confidence intervals, or statistical significance tests are reported anywhere. The imperceptibility claim is never supported by a human evaluation.

- **Defense evaluated against no alternative defenses.** The learned corrective noise is compared only against the undefended baseline. No comparison to simple preprocessing defenses (Gaussian blur, bilateral filtering, JPEG re-compression, adversarial training) is provided, so it is unclear whether the optimization provides value beyond a trivial denoiser.

- **The "second scenario" from the abstract is never formalized or separately evaluated.** The abstract promises two attack scenarios: "one distorts the output ... and another one increases the bit rate ... without visibly affecting quality." The attack formulation (Eq. 5) minimizes decompression PSNR (distortion), not bitrate. No separate experiment with a bitrate-maximization objective is presented, making this a dangling promise rather than an evaluated contribution.

### Trivial
- The claim on line 12 that "larger models are more vulnerable to adversarial attacks" is stated as a generality without evidence specific to model size vs. vulnerability. This is a small unsupported assertion in the introduction and not central to the paper.

## Nice-to-Haves
- A human perceptual evaluation (e.g., two-alternative forced choice) to substantiate the imperceptibility claim, which is the paper's central promise.
- Testing on the full Kodak dataset with per-image breakdowns and confidence intervals.
- An equal-budget ablation where log-exp and uniform additive perturbations are matched on L∞ norm, isolating the effect of noise distribution from noise magnitude.

## Removed Points
The following points from the inputs were removed with justification:
- **"Principled derivation from Weber's Law" (Strength Finder):** While the math is clean, the Weber's Law grounding is erroneous (see Major weakness 1). The mathematical clarity is retained as a strength; the Weber grounding claim is removed.
- **"Controlled comparison against additive noise" (Strength Finder):** The comparison is NOT controlled (different perturbation magnitudes), so this is not a genuine strength.
- **"BPP preservation under attack" (Strength Finder):** Only holds for the masked Cheng experiment (BPP unchanged); TCM shows BPP increase from 0.54 to 0.85. Inconsistent as a claimed strength.
- **"BPP inconsistency between Cheng and TCM":** The paper explains this discrepancy — TCM uses unmasked full-image attack while Cheng uses a masked approach. This is a reasonable explanation.
- **Formatting nitpicks, missing appendix complaints, speculative reproducibility concerns about cited references:** These are either parser artifacts or violations of the rule against questioning cited entities.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Reframe the motivation.** Either drop the Weber's Law claim entirely (the method should stand on empirical results, not a flawed psychophysics argument) or correct the adaptation direction so that noise decays less in bright regions where the absolute JND is substantially larger.
2. **Add controlled experiments.** Match the L∞ bound of log-exp and additive perturbations, then compare both the output-distortion and input-perturbation-visibility metrics. This is the minimum needed to claim any advantage for the luminance-adaptive distribution.
3. **Include at least one existing attack as a baseline.** PGD from Chen & Ma (2021), which the paper itself cites as the key prior work on compression-specific attacks, is the obvious candidate.
4. **Run an ablation with four conditions:** (a) log-exp with mask, (b) log-exp without mask, (c) additive noise with mask, (d) additive noise without mask. This would separate the effect of the noise function from the masking procedure.
5. **Report results on all 24 Kodak images** with per-image statistics and confidence intervals.
6. **Formalize and evaluate the bitrate-increase scenario** with a separate optimization objective if it remains a claimed contribution.

## Score and Decision
**Score:** 4.0/10  
**Decision:** Reject

The paper proposes a mathematically clean perturbation function, but the theoretical motivation from Weber's Law is verifiably inverted relative to the paper's own cited data, and the experimental evaluation has multiple critical gaps: no controlled noise-budget comparison, no baselines from existing attack literature, no ablation study, and evaluation on a handful of images without statistical rigor. The paper cannot support its central claims in its current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>