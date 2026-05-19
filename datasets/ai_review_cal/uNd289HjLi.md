- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces Corruption2Self (C2S), a score-based self-supervised framework for MRI denoising. The core contribution is a Generalized Ambient Denoising Score Matching (GADSM) loss that unifies prior self-supervised frameworks (DSM, ADSM, Noisier2Noise) as special cases, enabling learning from noisy observations without clean labels. Additional contributions include a reparameterization of noise levels for training stability, a detail refinement extension, and an extension to multi-contrast denoising. Evaluated on M4Raw and fastMRI datasets, C2S achieves state-of-the-art results among self-supervised methods.

## Strengths

- **GADSM loss unifies prior self-supervised frameworks** (Section 3.1, Theorem 1). The paper formalizes a loss that subsumes DSM, ADSM, and Noisier2Noise as special cases by setting the target noise level σ_{t_target} appropriately. This is a clean theoretical contribution that clarifies the relationship between these methods within a score-matching perspective.

- **State-of-the-art among self-supervised methods on real and simulated MRI benchmarks** (Tables 2, 3). On M4Raw, C2S achieves 32.59 dB PSNR on T1, 32.28 dB on T2, and 32.43 dB on FLAIR, consistently outperforming Noise2Void, Noise2Self, PUCA, LG-BPN, Noisier2Noise, and Recorrupted2Recorrupted by clear margins. On fastMRI, C2S matches or beats competitors across contrasts and noise levels.

- **Reparameterization demonstrably stabilizes training and accelerates convergence** (Figure 2, Table 4a). The paper shows that mapping noise levels to a reparameterized scale yields smoother training curves, faster PSNR/SSIM improvement, and higher final metrics (e.g., +0.28 dB on T1) compared to the non-reparameterized baseline.

- **Detail refinement extension yields statistically significant improvements** (Table 1). The paper reports significant gains (p<0.05) from this module (e.g., +0.18 dB PSNR on T1 on M4Raw validation), demonstrating that oversmoothing can be mitigated.

- **Ablation studies are informative and well-structured** (Tables 4b, 5). The paper systematically investigates the impact of maximum corruption level T, architecture choices (time conditioning, NVC-MSA), and provides design guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming relative to supervised methods in multi-contrast setting.** The introduction (line 16) states that after extending to multi-contrast, C2S "shows state-of-the-art performance among both self-supervised and supervised methods." However, the multi-contrast comparison (Table 6) includes only BM3D (a classical non-deep method) and Noise2Noise (requires paired noisy measurements, not a standard supervised method trained on clean labels). No modern supervised multi-contrast denoising architectures are included. This claim substantially overreaches its evidence base. The single-contrast claims are more measured (the abstract says "competitive results compared to supervised counterparts"), but the multi-contrast SOTA claim needs to be either removed or supported with a broader set of supervised baselines.

- **Detail refinement module is underspecified.** The detail refinement extension is introduced as a key contribution in the abstract and introduction, credited with statistically significant improvements in Table 1, but the paper provides no description of how it works—no architectural diagram, no loss function, no training procedure. The main text only mentions its existence and that it improves results (lines 4, 10, 102, 113, 169). Given the module's role in addressing the oversmoothing problem that the paper identifies as a core limitation of existing self-supervised methods, this is a significant methodological gap that prevents reproducibility and evaluation.

### Minor

- **No error bars or confidence intervals on main quantitative comparisons.** Tables 2, 3, and 6 report point estimates without variability measures. Only Table 1 (detail refinement) includes significance testing. Since some margins over baselines are modest (e.g., +0.65 dB over Noise2Self on T1), the reader cannot assess whether these differences are significant.

- **Multi-contrast evaluation limited to two baselines.** Table 6 compares only against BM3D and Noise2Noise. The paper would be strengthened by including other multi-contrast MRI denoising approaches from the literature, even if performed by the authors as re-implementations.

- **Gaussian noise assumption not tested in low-SNR regimes where it likely fails.** The method assumes additive Gaussian noise (Section 3). The paper acknowledges VST as a pre-processing option for Rician noise (line 49) and notes the Gaussian assumption "does not appear necessary for empirical performance" (line 41), but does not state whether VST was actually applied in the experiments, nor evaluates on data where the Gaussian approximation is poor. The claim of "superior robustness across varying noise conditions" (conclusion, line 169) is broader than the evidence supports.

### Trivial
None.

## Nice-to-Haves

- Directly compare against supervised methods trained on truly clean references (e.g., 6-repetition averages on M4Raw) to substantiate or qualify the claim of competing with supervised approaches.
- Test on a dataset with explicit Rician noise at low SNR, both with and without VST preprocessing.
- Add the α value used for the weighting function w(τ) = (σ_τ² + σ_tdata²)^α to the main text.

## Removed Points

These points from the reviewers were removed per filtering rules:

1. *"Training details (learning rate, batch size, optimizer, hardware) not reported"* — Removed per instruction: nitpicks about undisclosed hyperparameters and trivial implementation details should be removed. The parser may have stripped an appendix with these details.
2. *"It is unclear whether baselines were re-implemented or adapted from public code, and whether their hyperparameters were tuned"* — Removed per same rule about reproducibility nitpicks.
3. *"Weighting function α value not given"* — Removed per same rule.
4. *"Code availability not mentioned"* — Removed per instruction: missing appendix content likely stripped by parser.
5. *"The claim about being 'among the first to comprehensively analyze...' is arguable"* — Too minor to include, does not affect the paper's core claims.
6. *"The derivation would benefit from intuitive explanation"* — Removed as a subjective presentation preference, not a weakness.
7. *"The detail refinement should be mentioned in Section 3"* — Merged into the Major weakness about underspecified module.
8. *"Connection between ADSM and Noisier2Noise would be helpful earlier"* — Too minor.
9. *"fastMRI label noise not quantified"* — The paper explicitly acknowledges this (line 136: "they still contain inherent noise typical in MRI, albeit with higher SNR"), making the criticism a statement of what the paper already acknowledges.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the multi-contrast claim: either remove the "state-of-the-art among supervised methods" phrasing, or expand Table 6 with modern supervised multi-contrast denoising baselines.
2. Describe the detail refinement module in the main text — at minimum a conceptual description, loss term or architectural modification, and training procedure. Without this, a named contribution of the paper is a black box.
3. Add error bars or statistical significance tests to Tables 2 and 3 so readers can assess whether modest PSNR margins are meaningful.
4. Clarify whether VST was applied in the reported experiments and, if not, add an experiment testing C2S on low-SNR magnitude data with explicit Rician noise.
