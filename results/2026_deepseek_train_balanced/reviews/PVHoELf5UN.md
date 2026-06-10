Now let me produce the final consolidated review.

## Summary

This paper proposes a zero-reference (unsupervised) framework for joint low-light image enhancement and denoising. The method generates paired sub-images via neighboring-pixel masking and gamma correction, uses a DCT-based Frequency-Illumination encoder (FIcoder) to extract multi-band degradation representations, and employs a transformer-based decomposition network with cross-attention to separate reflectance from illumination. The framework is trained end-to-end with a self-supervised loss derived from Retinex theory. Experiments on LOLv1, LOLv2, SICE, and SIDD are reported.

## Strengths

- **Novel DCT-based frequency decomposition with physically motivated band separation.** The FIcoder (Section 3.3) performs channel-wise 2D DCT and uses four explicit masks (low.1, low.2, high.1, high.2) to filter frequency spectra across defined bands, linking each band to a specific visual attribute (chromaticity, semantics, edge contours, noise intensity). This design provides a more interpretable decomposition of degradation modes than prior frequency-domain methods that lack such structured band-to-attribute mappings.

- **Thorough ablation studies systematically validating individual design choices.** Section 4.3 ablates each of the three physical priors (illumination, high-pass, low-pass), the masking mechanism, the regularization term, and the LCnet adaptive module. The ablation of priors (Table 3) shows a ~0.6 dB PSNR drop when illumination prior is removed, and the denoising design ablation (Table 4) demonstrates that both masking and regularization contribute to performance. The gamma enhancement factor is also swept with a clear optimal range identified (Figure 9).

## Weaknesses

### Fatal

None. While the N2N theoretical grounding is problematic (see Major), the method may still yield useful empirical results through other mechanisms (the architecture, the full loss function, the consistency regularization between views). The issue undermines the paper's stated justification but does not invalidate all empirical findings categorically.

### Major

- **1. The theoretical grounding in Noise2Noise is incorrect for the proposed masking procedure.** The paper explicitly grounds its self-supervised denoising in N2N theory (line 79–90), claiming that the neighbor-masked sub-images $\mathcal{D}_1(I)$ and $\mathcal{D}_2(I)$ "share the same ground truth reflectance" (line 122) and thus satisfy N2N's requirement of two independent noisy observations of the same clean signal. This is false. The masking procedure partitions the image into 2×2 blocks and assigns different pixels (adjacent but spatially distinct) to each sub-image. The underlying clean reflectance values $R_1$ and $R_2$ at the corresponding positions in the two sub-images are different because they come from different spatial locations. N2N requires $\mathbb{E}[\text{observation}_1] = \mathbb{E}[\text{observation}_2] = \text{clean signal}$, which holds only when the noise is zero-mean and the clean signal is identical. Here $\mathbb{E}[\mathcal{D}_1(I)] = R_1 \circ L_1 \neq R_2 \circ L_2 = \mathbb{E}[\mathcal{D}_2(I)]$, so the N2N guarantee does not apply. The L2 loss between reflectance maps from different spatial locations will drive the network toward a spatial average rather than true denoising. The paper asserts "they exist within the same scene" as justification (line 122), but same-scene ≠ same-pixel-value. This is a conceptual error in the claimed theoretical foundation.

- **2. On SIDD (a dataset with ground-truth clean images), only no-reference metrics are reported, creating an evidential gap for the denoising claim.** Table 2 reports PSNR/SSIM/LPIPS on SICE and BRISQUE/CLIPIQA on SIDD. SIDD provides paired noisy-clean images; PSNR, SSIM, and LPIPS against the clean ground truth are the standard metrics for evaluating denoising quality. The paper does not explain why these reference metrics are omitted while they are reported for the other three benchmarks. Since the paper's central claim is *joint denoising and enhancement*, the absence of reference-based fidelity metrics on the only dedicated denoising benchmark in the evaluation suite is a decisive gap. No-reference metrics (BRISQUE, CLIPIQA) measure perceptual naturalness, not reconstruction fidelity — they cannot substitute for PSNR/SSIM in supporting a denoising claim.

### Minor

- **3. The Taylor expansion derivation relies on approximations that are weakest in the regime the method targets.** Equation (6)’s expansion $(R+N)^\lambda \approx R^\lambda + \lambda R^{\lambda-1}N$ requires $|N| \ll R$. In low-light conditions where $R$ is very small (near zero in dark pixels) and noise (modeled as Poisson, with variance proportional to signal) can be of comparable magnitude, this condition is routinely violated. The further approximation $R^{\lambda-1} \approx 1$ (requiring $R \approx 1$ when $\lambda$ is not extremely close to 1) is also rough: for $\lambda=1.5$ and $R=0.1$, $R^{\lambda-1} \approx 0.32$. While the paper acknowledges this at high $\gamma$ values (line 259), the approximations are strained across much of the operating range. The method may still work empirically, but the derivation that motivates the self-supervised signal is mathematically fragile.

- **4. Multiple key hyperparameters are not reported in the main text.** The loss weights $\omega_R, \omega_L, \omega_{\text{con}}, \omega_{\text{enh}}, \omega_{\text{exp}}, \omega_{\text{col}}$ and the DCT bandwidth threshold $t$ are never given numerical values. The optimizer, learning rate schedule, and weight decay are not specified (only initial LR $1\times10^{-5}$ and 100 epochs). Some details may reside in supplementary materials (which are stripped by the parser), but the main text should state or reference these values to make the paper self-contained for review.

- **5. The "interpretable" claim in the title is not substantiated.** The only explicitly interpretable components are the DCT frequency masks (whose mapping to "chromaticity, semantic information, edge contours, and noise intensity" is asserted without verification) and the Retinex decomposition. The learned implicit degradation representation $P$ is never analyzed — whether its internal structure reflects the claimed degradation attributes, whether the cross-attention weights align with degradation structure, or whether interpretability can be verified beyond the design intention.

### Trivial

None.

## Nice-to-Haves

- Include a cascaded baseline (e.g., Noise2Void denoising followed by Zero-DCE enhancement) to directly test the paper's thesis that joint processing outperforms sequential processing.
- Validate the N2N-based training strategy in isolation: on controlled data where the same clean pixel has two independent noisy observations, test whether the masking strategy preserves the N2N property.
- Report variance or confidence intervals over multiple runs for quantitative results.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic point #4: "Tables are unreadable and the quantitative claims cannot be verified."** Removed. The tables are rendered as embedded images extracted from the PDF; the numbers are present and readable in the original PDF submission. This is a parser artifact, not an author error.
- **Strength Finder strength #1: "Physically grounded self-supervised training strategy derived from first principles."** Demoted/removed because it conflicts with verified Weakness #1 (the N2N grounding is incorrect). The training strategy is physically motivated but its claimed N2N-equivalence foundation is unsound.
- **"No comparison with a simple denoiser+enhancer cascade"** moved to Nice-to-Haves rather than a Weakness, as it is a suggestion for strengthening rather than a flaw in what is presented.
- **Various formatting/style nitpicks** (unreadable tables, typo-level issues) removed per parsing-artifact and formatting rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the theoretical framing.** Drop the claim of N2N equivalence and reframe the training strategy as a form of cross-view consistency regularization or self-supervised reflectance constancy instead. This would better match what the loss actually does.
2. **Report PSNR, SSIM, and LPIPS on SIDD.** If the method truly performs joint denoising and enhancement, reference metrics against SIDD ground truth are essential to demonstrate fidelity beyond perceptual naturalness. If SIDD is not suitable for reference-metric evaluation (e.g., because the ground truth is not in the same illumination range), explain this clearly.
3. **Report all loss weights, DCT bandwidth $t$, optimizer configuration, and schedule** either in the main text or in a clearly referenced appendix.
4. **Provide evidence for the interpretability claim** by analyzing the learned representation $P$, showing whether the cross-attention weights correlate with degradation types, or verifying the claimed mapping from DCT bands to semantic attributes.
5. **Tighten the Taylor expansion justification** by either (a) providing empirical evidence that the approximation errors are small, or (b) eliminating the derivation and motivating the loss function directly from the desired invariance property.

## Score and Decision

The paper proposes a genuinely novel architecture (DCT-based FIcoder with explicit band separation, transformer-based Retinex decomposition with cross-attention) and provides thorough ablation studies. However, the core self-supervised training strategy is grounded in a theoretical claim (N2N-based denoising from neighboring-pixel masking) that is mathematically incorrect: adjacent pixels from different spatial locations do not share the same underlying clean signal, violating the N2N guarantee. Additionally, the absence of reference-based metrics on SIDD — the only dedicated denoising benchmark evaluated — leaves a significant evidentiary gap for the denoising component. While the method's empirical results may still hold value, the flawed theoretical foundation and missing evidence on the central claim make the paper unsuitable for acceptance at ICLR in its current form.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>