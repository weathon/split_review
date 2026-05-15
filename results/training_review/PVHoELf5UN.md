Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes a zero-reference framework for joint denoising and enhancement of low-light images. It generates paired sub-images with different illumination and noise levels via neighboring-pixel masking and random gamma correction, then decomposes them into reflectance and illumination guided by DCT-based frequency priors and an implicit degradation encoder with cross-attention transformers. The method is evaluated on LOLv1, LOLv2, SICE, and SIDD, showing competitive results against both supervised and unsupervised baselines.

## Strengths

- **Novel self-supervised sub-image generation strategy**: The combination of neighboring-pixel masking (inspired by Noise2Noise) with random gamma correction to create paired sub-images with different noise levels \*and\* different illumination is a creative solution to the zero-reference training problem. This allows the network to learn denoising and enhancement simultaneously without paired ground truth (Section 3.2, Equations 5–8, Figure 2).

- **DCT-based frequency priors provide structured feature separation**: Using channel-wise 2D DCT to decompose the input into four spectral bands (low-frequency chromaticity/semantics and high-frequency edges/noise) plus an illumination prior is a principled architectural choice. The ablation study (Table 3) confirms that removing these priors degrades performance, validating their utility. The visualizations in Figure 4 help illustrate what each frequency band captures.

- **Competitive performance across multiple real-world benchmarks**: The method achieves strong results on LOLv1, LOLv2, SICE, and SIDD across both full-reference (PSNR/SSIM/LPIPS) and no-reference (BRISQUE/CLIPIQA) metrics. The qualitative comparisons (Figures 5–7) show consistently clean outputs with good color fidelity and noise suppression.

- **Thorough ablation study isolating individual components**: The paper ablates the denoising design (masking + regularization, Table 4), the hybrid priors (illumination, high-pass, low-pass, Table 3), and the LCnet adaptive illumination module (Figure 8), providing clear evidence that the full combination is needed for optimal results.

- **Adaptive illumination correction via LCnet**: The LCnet uses global average pooling with a transformer to predict a per-image correction factor, avoiding fixed or hand-crafted adjustments. The ablation (Figure 8) shows that removing it leads to local overexposure.

## Weaknesses

### Fatal

None.

### Major

- **Flawed theoretical justification undermines the claimed "physical grounding" (Section 3.2, Equations 7–10)**. The derivation requires the approximation `R^(λ-1) ≈ 1` with the justification "when λ is close to 1." However, in practice (Section 4.3, Gamma Enhancement Factor analysis), λ = 1/σ where σ ∈ (1.3, 1.7), giving λ ∈ (0.59, 0.77). For λ = 0.7, λ−1 = −0.3, so `R^(λ-1) = 1/R^0.3`. Since R ∈ (0,1) (normalized pixels), this quantity can be significantly larger than 1 (e.g., for R=0.2, `R^(-0.3) ≈ 1.62`; for R=0.1, `R^(-0.3) ≈ 1.99`). The paper \*does\* partially acknowledge this in Section 4.3 ("At higher values, the enhancement does not conform to the assumption R₁^(λ-1)=1 during framework inference"), yet the core theoretical derivation in Section 3.2 is presented as a clean, principled foundation without caveat. This disconnect means the method's theoretical scaffolding is weaker than claimed — the approach is better understood as a practically motivated heuristic (masking + gamma correction) that works empirically, not one rigorously grounded in physical imaging. This does \*not\* invalidate the empirical results, but it does weaken the central claimed contribution of being "interpretable" and "grounded in physical imaging principles."

- **Claimed "interpretability" is asserted but never defined or evaluated (Title, Abstract, Section 3)**. The paper's title and abstract describe the method as "interpretable," and the introduction criticizes prior methods for lacking interpretability. Yet the paper provides: (a) no definition of what interpretability means in this context, (b) no metric to measure it, (c) no evaluation (e.g., attention visualization, latent space analysis, feature attribution, or user study), and (d) no discussion of which specific components enhance interpretability. The DCT decomposition visualizations (Figure 4) are informative but are simply visualizations of input preprocessing, not analyses of what the network learns or why its decisions are interpretable. Without any evaluation, "interpretable" is an unsubstantiated label rather than a verified property of the method.

### Minor

- **Loss function has at least 7 weighting hyperparameters with no sensitivity analysis**. The overall loss (Equation 18) uses weights ω_R, ω_L, ω_con, ω_enh, plus internal weights ω_reg (Equation 14), ω_exp, and ω_col (Equation 16). No ablation or sensitivity study is provided for any of these hyperparameters. This makes it difficult to assess how robust the method is to their settings or how transferable the configuration is to new datasets.

- **Technically inaccurate description of noise model (Section 3.1.1)**. The paper states "N is modeled as zero-mean Poisson noise" (line 67). Poisson noise is signal-dependent (variance equals mean), so it is not zero-mean additive noise. The subsequent derivations treat N as additive zero-mean noise throughout. While this simplification is common in practice, stating it as a modeling assumption is imprecise and could mislead readers about the noise characteristics being assumed.

- **Data presentation overclaims relative to results (Section 4.2)**. The paper states its method "outperforms most of the compared unpaired and no-reference methods" and "achieves the best results" across metrics. However, on LOLv1 the method's PSNR (20.08) trails PairLIE (20.69) and NeRCo (20.53); on SICE the PSNR (22.35) trails PairLIE (22.41). The gains over other zero-reference methods (Zero-DCE, EnlightenGAN) are often marginal. The qualitative differences in Figures 5–7 are subtle. The claims should be calibrated to match the data — "competitive with" or "favorable against" would be more accurate than "the best."

- **Undefined term introduced in conclusion (Section 5)**. The conclusion mentions a "Dynamic Discrete Sequence Fusion Transformer" that was never defined or discussed in the main paper. This term does not appear in Sections 1–4, leaving the reader confused about what it refers to.

### Trivial

- The gradient term `∇L₁` in Equation 15 is mentioned but not specified as L1 or L2 norm — this should be clarified.

## Nice-to-Haves

- A hyperparameter sensitivity analysis (varying each loss weight by ±50%) would substantially strengthen reproducibility claims.
- Runtime / FLOPs / parameter count comparisons against baselines would help assess practical utility.
- Visualizing the decomposed reflectance maps `R₁` and `R₂` from the two sub-images (and their difference) would provide direct evidence that the network enforces reflectance consistency.
- An analysis of failure cases (e.g., extreme low-light, saturated highlights) would improve the paper's completeness and help characterize the method's limitations.

## Removed Points

These points from the original reviews were removed with justification:

- **"Unfair comparison against supervised methods"** (Harsh Critic, Point 2, part 1): Per hard rules, criticisms about asymmetry favoring the baseline (supervised methods have an inherent advantage on full-reference metrics) are removed — the paper is attempting a stronger comparison. However, the related sub-point about results not consistently supporting the claimed superiority is retained in Minor Weaknesses above.
- **Missing related works (Noise2Fast, Self2Self, BM3D, DCT denoising)**: Per hard rules, missing related works should not be raised as weaknesses.
- **Claim that paper misstates N2N requires paired images**: The paper correctly describes N2N (lines 79–90) — this criticism misunderstands the paper.
- **Baseline configurations not specified / missing training details**: Minor reproducibility nitpicks; some details may be in the supplementary appendix which the parser strips.
- **"No comparison on runtime"** and similar missing-experiment demands: Moved to Nice-to-Haves or deemed beyond stated scope.
- **Formatting/style nitpicks and typo complaints**: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method or results that the paper itself does not make.

## Suggestions

1. **Revise the theoretical derivation (Section 3.2)**: Either (a) acknowledge explicitly that the Taylor expansion approximation `R^(λ-1) ≈ 1` does not hold for the λ values used and reposition the method as a justified heuristic, or (b) provide an analysis quantifying the approximation error and showing why the method still works despite it. The current framing oversells the theoretical foundation.

2. **Either substantiate or remove the "interpretable" claim**: Provide a concrete definition of interpretability for this context and an evaluation (e.g., visualizing cross-attention maps from REFnet, showing how the FIcoder's implicit representation separates degradation types, comparing feature maps to manual degradation annotations). If no evaluation is added, remove "interpretable" from the title and abstract.

3. **Add a hyperparameter sensitivity study** for the 7+ loss weights, even if only a table showing performance variance when each weight is varied by ±50%.

4. **Calibrate the claims in Section 4.2** to match the data — replace "outperforms... achieving the best results" with more measured language given the mixed quantitative comparisons.

5. **Clarify the unspecified term ("Dynamic Discrete Sequence Fusion Transformer")** in the conclusion or remove it.

6. **Correct the noise model description** (Section 3.1.1) to accurately characterize N as additive zero-mean noise approximating sensor read noise, rather than describing it as "zero-mean Poisson noise."

## Score and Decision

**Originality**: Medium. The combination of masking + gamma correction for sub-image generation is novel, though individual components are known. **Importance of question**: High. Joint zero-reference denoising and enhancement is practically important. **Claims supported**: Below average. The theoretical grounding claim is weakened by the Taylor expansion issue, and interpretability is unevaluated. **Soundness of experiments**: Adequate. Ablation studies are thorough, but hyperparameter sensitivity is missing. **Clarity**: Adequate, with one undefined term in the conclusion. **Value to community**: Moderate — the method works empirically and could be useful, but the overclaimed framing reduces confidence.

The paper presents a method that works well empirically, with genuinely clever engineering choices (masking + gamma correction for self-supervision, DCT-based priors, cross-attention for degradation guidance). However, it overreaches in two critical ways: (1) the theoretical derivation presented as rigorous physical grounding has a clear mathematical gap that the paper itself acknowledges in passing, and (2) the "interpretable" label in the title is entirely unevaluated. These are not fatal — the empirical method stands on its own — but they are significant weaknesses that need to be addressed before the paper's claims are credible.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>