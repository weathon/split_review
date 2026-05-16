Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes an unsupervised (zero-reference) framework for joint denoising and low-light enhancement. The key idea is to generate paired sub-images from a single low-light input via neighboring-pixel masking (for different noise realizations) and gamma correction (for different illumination levels), then enforce consistency between their reflectance maps under a Retinex decomposition. DCT-based frequency-domain priors and a cross-attention mechanism are used to separate compounding degradations. The method achieves strong quantitative results on LOLv1, LOLv2, SICE, and SIDD benchmarks against state-of-the-art unsupervised methods.

---

## Strengths

- **DCT-based multi-frequency prior encoding in sRGB space.** The paper explicitly decomposes images into five physically interpretable priors (illumination, low-frequency chromaticity/semantics, high-frequency edges/noise) using channel-wise 2D DCT with frequency masks (Section 3.3, Figure 4). This separates compounding degradations rather than handling them sequentially. The ablation in Table 3 confirms that removing any of these priors degrades performance (PSNR drops ~0.6 dB without the illumination prior), providing clear evidence for the design choice.

- **State-of-the-art quantitative results on multiple benchmarks.** The method achieves the best or runner-up scores on PSNR, SSIM, and LPIPS for LOLv1, LOLv2, and SICE (Table 1), and on BRISQUE/CLIPIQA for SIDD (Table 2), outperforming all compared unsupervised baselines (Zero-DCE, SCI, RUAS, EnlightenGAN, NeRCo, PairLIE, etc.). Qualitative comparisons (Figures 5–7) consistently show superior denoising, color fidelity, and illumination handling.

- **Systematic ablation studies.** The paper provides thorough ablations for the denoising design (Table 4, Figure 8 — masking mechanism, regularization term), hybrid priors (Table 3 — illumination, high-pass, low-pass components), LCnet adaptivity (Figure 8), and gamma factor selection (Figure 9). Each ablation clearly demonstrates the necessity of the proposed component.

- **Interpretable illumination correction via LCnet.** Instead of a fixed reference-based adjustment, LCnet learns a one-dimensional scaling factor from illumination features to adaptively correct the illumination map (Section 3.2, Figure 8). The ablation shows this avoids local overexposure that plagues methods using fixed strategies (e.g., PairLIE-like reference adjustment).

---

## Weaknesses

### Fatal
None.

### Major

- **The theoretical derivation for the self-supervised signal uses an approximation that does not hold for the actual training parameters.** The derivation (Section 3.2) relies on the Taylor expansion approximation \(R^{\lambda-1} \approx 1\), stated to require \(\lambda\) close to 1. However, the gamma factors are sampled from \(\lambda = 1/\sigma\) with \(\sigma \in (1.3, 1.7)\), giving \(\lambda \in (0.59, 0.77)\) — substantially less than 1. While the paper later acknowledges this in the ablation (Section 4.3: "the enhancement does not conform to the assumption \(R_{1}^{\lambda-1}=1\) during framework inference"), this admission sits in the ablation section rather than qualifying the main theoretical narrative. The paper claims the framework is "physically sound" and "interpretable" (contributions, abstract), yet a central step in the derivation uses an invalidated approximation. This is a significant overclaim. **Why it matters:** The stated theoretical justification does not match the implementation. The method may work well empirically, but the paper should either (a) constrain \(\lambda\) to values where the approximation is valid (e.g., 0.9–1.1), (b) provide an alternative derivation that does not require this step, or (c) reframe the contribution as an empirically motivated framework rather than a physically grounded one.

### Minor

- **The SIDD evaluation does not include full-reference metrics despite ground truth being available.** The paper reports only no-reference metrics (BRISQUE, CLIPIQA) on SIDD (Table 2), a dataset with clean ground-truth images. While direct PSNR/SSIM against the original clean images is problematic for a joint enhancement+denoising method (because illumination enhancement would shift brightness), the absence of any quantitative denoising-specific evaluation weakens the claim of "superior denoising." A controlled experiment (e.g., evaluating denoising on patches with comparable illumination, or using an aligned protocol) would substantially strengthen the evidence. This gap is partially mitigated by the LOL results (which use full-reference metrics), but SIDD is the primary dataset for realistic noise.

- **Missing key hyperparameters for reproducibility.** The DCT bandwidth threshold \(t\) (Section 3.3) is described only as "manually set" with no value given. All loss weighting factors (\(\omega_R, \omega_L, \omega_{con}, \omega_{enh}, \omega_{exp}, \omega_{col}, \omega_{reg}\) in Eqs. 14, 16–18) are listed symbolically but never assigned numerical values. These details are essential for reproducing the method, especially given the many competing loss terms.

- **The neighboring-pixel masking assumption about local homogeneity is not examined.** The method assumes that two sub-images generated from 2×2 pixel patches share the same underlying reflectance and illumination (Section 3.2). The paper describes them as "highly similar" but provides no analysis of when this assumption breaks (e.g., at edges, fine textures, or thin structures) or how it affects detail preservation. A quantitative analysis of structural similarity between sub-images or a test on high-texture crops would ground this assumption.

- **Baseline configuration details are underspecified.** The paper states "all experiments were terminated after 100 training epochs" (Section 4.1) but does not state whether baselines were retrained under identical conditions or if numbers were taken from original papers. For unsupervised methods trained per dataset, convergence behavior across different loss formulations matters, and this detail is needed for a fair comparison.

### Trivial

- The ablation studies in Tables 3 and 4 report only PSNR; including SSIM and LPIPS would strengthen the evidence for perceptual quality preservation.

- The gamma factor ablation (Figure 9) is informative but only tests LOLv1 PSNR; testing on additional datasets and metrics would confirm the trend.

---

## Nice-to-Haves

- An ablation of the DCT bandwidth \(t\) to show sensitivity of results to this hyperparameter.
- A limitations section acknowledging assumptions about local homogeneity and the gamma approximation more prominently.

---

## Removed Points

- *"The claim that prior methods generally fail to differentiate feature layers is plausible but not specifically supported by citations"* — this is a general observation about framing, not a substantive weakness. The point is adequately illustrated by Figure 1.
- *"Tables lack entries for several baseline methods (e.g., MIRNet, Restormer in Table 2 have no values)"* — Tables are embedded as images; cannot verify whether entries are missing or a parser artifact. Not a reliable criticism.
- *"Strength: Physically grounded self-supervised training strategy"* — this strength conflicts with the verified weakness about the Taylor approximation / \(\lambda\) range, so per the meta-review rules the weakness prevails and the strength is removed from the main assessment.
- *"The regularization term L_reg is described only in text; its exact role and why it aligns gradients across scales is unclear"* — the paper does provide the equation (Eq. 14) and text explaining it. The description is adequate for a methods paper.

---

## Novel Insights

The harsh reviewer identifies a genuine tension in the paper: the method works well empirically, but the theoretical narrative overclaims physical interpretability for a step (the Taylor expansion approximation for \(R^{\lambda-1} \approx 1\)) that is used outside its valid regime. This is a recurring pattern in the zero-reference / self-supervised literature — elegant theoretical derivations often rely on approximations that don't hold under the actual training conditions. The paper's own ablation (Figure 9) shows that performance cannot be improved by simply moving \(\lambda\) closer to 1 (where the approximation would be valid), because the images wouldn't have enough illumination diversity. This reveals a genuine trade-off: theoretical correctness and empirical performance pull in opposite directions for this design choice. Acknowledging this trade-off explicitly rather than framing the derivation as physically grounded would strengthen the paper.

---

## Suggestions

1. **Fix the theoretical narrative.** Either confine the training to \(\lambda\) values where \(R^{\lambda-1} \approx 1\) is reasonable, provide an alternative derivation, or reframe the contribution as empirically motivated. The current framing oversells the physical grounding.
2. **Provide all hyperparameter values** (\(t\), all \(\omega\) weights) either in the main paper or supplementary. These are essential for reproducibility.
3. **Add a SIDD experiment with full-reference metrics.** Even an approximate protocol (e.g., evaluating denoising on regions with similar illumination before/after enhancement) would strengthen the denoising claim.
4. **Analyze the masking assumption.** Measure patch-level similarity between the generated sub-images on held-out data to validate the assumption that they share common reflectance/illumination.

---

## Score and Decision

**Originality:** Good. The combination of neighboring-pixel masking with gamma adjustment for zero-reference joint denoising and enhancement, plus DCT-based multi-frequency priors, is novel.  
**Importance:** Good. Real-world low-light joint enhancement+denoising is practically important.  
**Claims supported:** Partially. Empirical claims are well-supported; the "physically grounded" claim is overstated given the approximation issue.  
**Soundness of experiments:** Good overall. Multiple datasets, thorough ablations, but some missing hyperparameters and the SIDD evaluation gap.  
**Clarity:** Adequate. The method is described clearly, but some details (masking spatial arrangement, hyperparameter values) are underspecified.  
**Value to community:** Positive. Provides a practical unsupervised framework and useful design insights (frequency-domain degradation separation, LCnet).

The paper makes a real contribution and the weaknesses are addressable. The theoretical overclaim is the most significant issue but does not invalidate the empirical contribution.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**