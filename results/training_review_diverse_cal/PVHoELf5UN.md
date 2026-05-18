Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes a zero-reference (unsupervised) framework for joint denoising and low-light enhancement. It constructs paired sub-images via neighbor pixel masking and random gamma adjustment to create self-supervised training signals grounded in Retinex theory, uses DCT-based frequency decomposition to extract degradation priors, and employs a cross-attention transformer that integrates these representations for reflectance decomposition with adaptive illumination correction. Experiments on LOLv1, LOLv2, SICE, and SIDD show competitive quantitative results against unsupervised/zero-reference baselines.

## Strengths

- **Strong empirical performance across diverse real-world benchmarks.** Tables 1–2 report best or second-best PSNR, SSIM, LPIPS on LOLv1, LOLv2, SICE, and best BRISQUE/CLIPIQA on SIDD against a range of unsupervised and zero-reference methods. The visual comparisons (Figs. 5–7) show improved color fidelity and noise suppression relative to Zero-DCE, SCI, RUAS, and NeRCo.

- **DCT-based multi-frequency degradation modeling is validated by ablation.** Table 3 shows that removing illumination, low-frequency, or high-frequency priors degrades PSNR/SSIM, confirming that the explicit frequency decomposition provides a measurable benefit over processing in a single domain.

- **Cross-attention mechanism for degradation-guided reflectance extraction is well-designed.** REFnet uses cross-attention with FIcoder outputs (degradation representations), enabling separation of reflectance from illumination and noise. The ablation (Tables 3–4) supports the utility of this design, and the visual results show it mitigates the error-accumulation problem common in sequential multi-stage methods.

- **Ablation on the gamma enhancement factor (Fig. 9).** The paper systematically explores the impact of the gamma factor and empirically selects a range (σ ∈ 1.3–1.7) that balances sufficient illumination difference with acceptable noise behavior, demonstrating careful tuning of the training data generation.

## Weaknesses

### Fatal

None.

### Major

- **The Taylor expansion derivation for the self-supervised signal is mathematically unsound for the gamma values actually used.** The paper derives (Section 3.1.2, Eq. 8) that gamma-corrected noise becomes λN₂ with preserved zero-mean property by claiming R^(λ−1) ≈ 1 "when λ is close to 1." However, λ = 1/σ with σ ∈ (1.3, 1.7) gives λ ∈ (0.588, 0.769), which is substantially less than 1. For these λ values, R^(λ−1) = R^(negative) can be arbitrarily large when reflectance is small (dark pixels). The paper partially acknowledges this in the ablation (line 259: "At higher values [of σ], the enhancement does not conform to the assumption R₁^(λ−1)=1 during framework inference"), yet the main derivation is presented without caveat as a rigorous justification. This weakens the theoretical grounding of the self-supervised training signal. The method evidently works empirically (the ablation in Fig. 9 and Table 4 confirms this), but the mathematical framing overstates the rigor of the derivation.

### Minor

- **The DCT band separation (Section 3.3) is heuristic and the threshold t is not ablated.** The four masks are defined by diagonal cutoffs with a manually set hyperparameter t. Assigning semantic interpretations (chromaticity, semantics, edge contours, noise) to these specific DCT bands is asserted without principled justification or references. The ablation (Table 3) removes entire categories of priors but never tests sensitivity to different values of t. This weakens the claim of "interpretable" decomposition.

- **No sensitivity analysis for the six loss weighting coefficients.** The full loss (Eqs. 14–18) involves ω_R, ω_L, ω_con, ω_enh, ω_reg, plus ω_exp, ω_col within L_enh. No analysis is provided for how these weights were set or how sensitive performance is to their values. Without this, it is unclear whether reported results rely on extensive per-dataset tuning.

- **Scale mismatch between training and inference is acknowledged but not analyzed.** Training uses 1/4-resolution sub-images (256×256 patches from downsampled versions), while inference runs on full-resolution images. The regularization term L_reg (Eq. 15) partially addresses cross-scale gradient alignment, but no experiment compares results when inference is run on downsampled versus full-resolution images to validate whether the scale transfer works as intended.

- **Architecture details are insufficient for reproducibility.** REFnet, LUMnet, and LCnet are described at a high level ("hybrid-prior attention transformer," "cross-attention," "gating module") without specifying dimensions, number of layers, attention heads, or other architectural parameters. This makes it difficult to assess whether the architecture is well-matched to the task or to reproduce the results.

### Trivial

None beyond the minor points above.

## Nice-to-Haves

- An analysis of the noise model assumptions (zero-mean Poisson additive on reflectance) against real low-light noise statistics (read noise, quantization, etc.) would strengthen the claim of physical grounding.
- A systematic sensitivity study of the DCT threshold t would turn a heuristic design choice into a validated component.
- Showing how the implicit degradation representations (C_low_1, C_low_2, C_high_1, C_high_2) respond to controlled degradations (injected noise, blur, color shift) would substantiate the "interpretable" claim with more than visual illustration.

## Removed Points

- **Neighbor2Neighbor citation omission** (from harsh critic). This point is removed per policy: the paper's neighbor masking from 2×2 patches is structurally similar to Huang et al. (2021, Neighbor2Neighbor), which is not cited. The criticism is substantive, but the policy on missing related works precludes its inclusion in the main review. The authors are strongly encouraged to cite and discuss Neighbor2Neighbor, as it directly affects how the novelty of the masking mechanism should be assessed.

## Novel Insights

The reviews reveal a tension that the paper itself does not fully address: the method achieves strong empirical results on four real-world benchmarks despite a theoretical derivation that is mathematically fragile. This suggests that the true engine of the method's success may not be the gamma-expansion formalism (Section 3.1.2) but rather the combination of the pixel-masking strategy (generating two noisy views) with the DCT-based frequency decomposition and cross-attention architecture. The gamma correction may serve primarily as a practical mechanism to create illumination diversity, and the noise transformation argument, while presented as a rigorous deduction, is better understood as an approximate heuristic that happens to work in practice. The paper would benefit from reframing its theoretical claims accordingly, presenting the Taylor expansion as an approximate empirical strategy rather than a rigorous derivation. A controlled study that isolates the contribution of each component (masking, gamma, DCT priors, cross-attention) would clarify which parts are essential and which are supporting.

## Suggestions

1. Reframe the Taylor expansion derivation as an approximation heuristic supported by empirical evidence (the gamma ablation already partially provides this), rather than presenting it as rigorous proof. Explicitly acknowledge the λ range used and explain why the approximation is empirically acceptable despite the mathematical gap.
2. Add an ablation of the DCT threshold t to justify that the chosen value is not critical or to show how performance varies.
3. Provide the loss weighting coefficients (ω_R, ω_L, etc.) either in the paper or supplementary, and ideally include a sensitivity analysis.
4. Include a reproducibility section with architectural details (layer counts, dimensions, attention heads) for REFnet, LUMnet, and LCnet.
5. Add a comparison of full-resolution vs. downsampled inference to validate the scale-transfer regularization.

## Score and Decision

This paper makes a useful empirical contribution — a zero-reference joint denoising and enhancement method backed by competitive results across multiple benchmarks and thoughtful ablation studies. The core weakness is a theoretical derivation that overstates its rigor, and several design choices (DCT thresholds, loss weights, scale transfer) lack thorough validation. However, none of these issues invalidate the empirical contributions. With revision to address the theoretical framing and the missing analyses, the paper would be a solid contribution to the unsupervised low-light enhancement literature.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>