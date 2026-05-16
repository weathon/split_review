Now I have all the evidence needed. Let me compose the final consolidated review.

## Summary

The paper introduces Corruption2Self (C2S), a score-based self-supervised MRI denoising framework. Its core theoretical contribution is the Generalized Ambient Denoising Score Matching (GADSM) loss (Theorem 1), which extends denoising score matching to settings where only noisy observations are available and subsumes DSM, ADSM, and Noisier2Noise as special cases. The method incorporates a reparameterization of noise levels for training stability, mentions a detail refinement extension for fine-feature preservation, and supports multi-contrast inputs. Experiments on M4Raw (real noise) and fastMRI (simulated noise) show C2S achieving state-of-the-art results among self-supervised methods and competitive performance with supervised methods trained on multi-repetition-averaged labels.

## Strengths

- **Novel theoretical unification via GADSM loss.** Theorem 1 provides a clean generalization of denoising score matching to the ambient noise setting, with explicit coefficients γ and δ that correctly reduce to DSM, ADSM, and Noisier2Noise as edge cases (Section 3.1, lines 58–68). This is a principled foundation for self-supervised score-based denoising, not an ad-hoc engineering trick.

- **Strong empirical performance on real and simulated MRI data.** On M4Raw (Table 2), C2S outperforms all compared self-supervised methods (Noise2Void, Noise2Self, PUCA, LG-BPN, Noisier2Noise, Recorrupted2Recorrupted) across T1, T2, and FLAIR contrasts, with PSNR gains of 1–4 dB depending on the baseline. On fastMRI (Table 3), it achieves the best or tied-best SSIM at both noise levels (σ=13/255, σ=25/255), demonstrating consistent detail preservation.

- **Reparameterization demonstrably stabilizes training.** Figure 2 and Table 4a show that the reparameterization of noise levels (mapping t→τ for uniform sampling) yields smoother convergence and measurable PSNR/SSIM improvements across all three M4Raw contrasts. The benefit is validated both visually and quantitatively.

- **Multi-contrast extension works and is well-motivated.** Table 6 shows multi-contrast C2S (using T1&T2 or T1&FLAIR as inputs) outperforms single-contrast C2S, BM3D, and Noise2Noise on all target contrasts, with improvements of 0.5–2 dB PSNR. This addresses a clinically relevant scenario where multiple contrasts are routinely available.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Detail refinement extension is mentioned but not described.** The paper repeatedly invokes "detail refinement" as a key contribution (abstract, intro, Section 3.2, conclusion) and Table 1 attributes statistically significant gains of up to +0.49 dB PSNR to it (p<0.05). Yet the mechanism—what it is, how it integrates with the C2S loss, its architectural implications—is never explained in the main text. If this is detailed in a (potentially parser-stripped) appendix, it should still be summarized in the main body given its prominence in the claimed contributions. A reader cannot evaluate, reproduce, or build upon a method whose core component is opaque.

- **Baseline comparison conditions are underspecified.** The paper does not state whether SwinIR, Restormer, PUCA, LG-BPN, etc. were retrained from scratch on the same data splits or used pre-trained weights (and if so, on what data). Training epochs, learning rates, optimizer choices, and data augmentation for each baseline are absent. While some of these details may reside in a stripped appendix, the main text lacks the transparency needed to rule out configuration bias in the comparisons.

- **Blind denoising claim is asserted without direct evidence.** The paper states (line 153) that C2S "effectively functions as a blind denoising model" by using standard noise estimation tools (skimage). However, no experiment compares C2S' performance with estimated vs. ground-truth noise levels, nor evaluates degradation under misestimation. This claim is currently unsupported.

- **Noise-level handling on real data lacks analysis.** For the M4Raw dataset (real noise), the paper does not state the estimated σ_t_data values, how noise estimation was validated, or how sensitive results are to estimation error. The one-sentence claim of robustness (line 153) is not backed by any sensitivity experiment.

### Trivial

- **Weighting function hyperparameter α is introduced but never specified or ablated** (line 98). Since α controls the relative contribution of different noise levels to the loss, its value (or at least a brief sensitivity check) would help practical adoption.

- **Main results lack error bars.** Tables 2, 3, and 6 report single-run metrics without confidence intervals or standard deviations. Given stochasticity in neural network training and the fact that some reported differences are small (e.g., 30.91 vs. 30.95 dB PSNR on fastMRI PDFS at σ=13/255), readers cannot assess whether gaps are meaningful.

- **Multi-contrast architecture is not specified.** The paper simply states "incorporating additional MRI contrasts as inputs" without describing how contrasts are fused (channel concatenation? attention? separate encoders?). For a U-Net this is likely input-channel stacking, but stating this explicitly would aid reproducibility.

## Nice-to-Haves

- A noise-level sensitivity study on fastMRI (where ground-truth σ is known) misestimating σ_t_data by ±20%, ±50%, etc. would substantiate the robustness claim and guide practitioners.
- An ablation of the weighting parameter α and the choice of loss weighting function w(τ).
- Reporting mean ± std over 3 random seeds for the main tables would strengthen confidence in the reported improvements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing proof/sketch for Theorem 1 "assumed in appendix."** The paper never references an appendix in the parsed text; proofs are standardly deferred to supplementary material, which the parser strips. Removed per instruction that parser-stripped appendix content should not be held against the paper.

- **Strength about detail refinement providing statistically significant gains.** While the empirical numbers in Table 1 are present, the strength is inherently qualified because the method is not described. Rather than list it as a strength the reader cannot evaluate, it is moved here with a note: if the detail refinement is described in the appendix, this can be reinstated as a supporting strength; if not, the corresponding weakness stands.

- **Criticism about "the paper should also cover Y / domain Z."** The reviewer's suggestion to evaluate supervised methods on the same noise level as training labels is a valid deeper analysis but not a required comparison for the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's own framing: GADSM is a legitimate theoretical contribution, the empirical results are solid, but the detail refinement extension—a component credited with significant gains—is absent from the main text, creating a disconnect between claimed contributions and what the reader can evaluate.

## Suggestions

1. **Describe the detail refinement extension in Section 3.2** (or at minimum summarize its key design choices if full details remain in the appendix). A diagram or a short paragraph explaining the mechanism and how it interacts with the GADSM loss would resolve the paper's most significant weakness.
2. **Add a table of training hyperparameters** for both the proposed method and all baselines (epochs, learning rate, optimizer, batch size, data splits, pre-trained vs. from-scratch status). This would greatly increase trust in the comparisons.
3. **Include a brief noise-level sensitivity experiment** (e.g., on fastMRI) showing PSNR/SSIM vs. σ_t_data misestimation, even as a supplementary figure. This is inexpensive and would substantiate the robustness claim.
4. **Remove or soften the "blind denoising model" claim** unless supported by a blind-evaluation experiment, or explicitly qualify it as "blind with respect to noise level via standard estimation tools."

## Score and Decision

**Originality:** Good. The GADSM theoretical framework is novel and cleanly generalizes prior score-matching approaches.  
**Importance of question:** High. Self-supervised MRI denoising is practically important given the difficulty of acquiring clean ground truth.  
**Claims support:** Moderate. The empirical claims are well-supported, but the detail refinement contribution is unverifiable and the blind-denoising claim lacks evidence.  
**Soundness of experiments:** Good overall, with gaps in baseline transparency and sensitivity analysis.  
**Clarity of writing:** Good for the described parts, but the missing detail-refinement description undermines completeness.  
**Value to community:** Moderate to high, assuming the method is fully described and reproducible.

The paper makes a genuine theoretical contribution (GADSM) and demonstrates strong empirical results. The primary weakness—an absent description of the detail refinement extension—is addressable in a revision. The remaining issues (baseline transparency, missing ablations) are common limitations in conference papers of this type and do not individually threaten the core claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>