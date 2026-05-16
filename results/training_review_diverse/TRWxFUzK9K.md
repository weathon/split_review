Now I have a complete picture. Let me compose the final consolidated review.

## Summary

This paper proposes a video inverse problem solver that uses only pre-trained 2D image diffusion models, bypassing the significant difficulty of training video diffusion models. The method treats the temporal dimension as a batch dimension for image diffusion models, introduces batch-consistent sampling (synchronizing stochastic noise across frames to maintain temporal coherence), and applies multi-step conjugate gradient (CG) optimization within the denoised spatio-temporal batch at each reverse diffusion step. Experiments on temporal PSF deblurring and combined spatio-temporal degradations (deblur+deblur, SR+deblur, inpainting+deblur) show large quantitative margins over existing diffusion-based baselines with 10–50× speed improvements.

## Strengths

- **First video inverse solver using only 2D image diffusion models without video-specific training.** The paper introduces a novel formulation that treats the temporal dimension as a batch dimension for 2D diffusion models and solves spatio-temporal optimization problems inside the Tweedie-denoised batch. This is concretely realized in Algorithm 1 (Section 3.2) and validated by the fact that a pre-trained ADM image diffusion model is used directly without any fine-tuning or additional networks (Section 4, experimental setup).

- **State-of-the-art quantitative results across multiple spatio-temporal degradations with large margins.** Tables 1 and 2 show that the proposed method outperforms all baselines (DPS, DiffusionMBIR, ADMM-TV) on PSNR, SSIM, LPIPS, and FVD for both temporal degradations (e.g., 43.16 PSNR vs. DPS 33.42 for uniform PSF k=7, Table 1) and spatio-temporal degradations (e.g., 27.77 PSNR vs. next best 22.76 for deblur + temporal PSF, Table 2). The FVD metric, which specifically measures temporal consistency, shows the largest relative improvements (e.g., 0.008 vs. 0.325 for DPS, Table 1).

- **Dramatic computational efficiency (10–50× faster than prior diffusion solvers).** The method uses only 20 NFE for temporal tasks, achieving 12s reconstruction time vs. 611s for DiffusionMBIR and 1244s for DPS (Table 1). The paper explicitly notes that this enables speeds exceeding 1 FPS (Section 4.2), a practical advantage over existing diffusion-based methods.

- **Ablation studies cleanly isolate the contributions of batch-consistent sampling and CG updates.** Figure 7 and Table 3 quantify the effect of removing stochasticity control (PSNR drops from 39.69 to 30.86) and replacing CG with GD, confirming both components are essential. Figure 6 shows that stand-alone CG leaves residual artifacts while the full method produces clean reconstructions, demonstrating the synergy between diffusion prior and CG optimization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "state-of-the-art" claim is not precisely scoped.** The paper compares only against other methods that also use image diffusion models (DPS, DiffusionMBIR) plus classical solvers, which is appropriate given the paper's contribution, but the abstract and introduction claim "state-of-the-art reconstructions" without qualification. Since no video-diffusion-based inverse solvers exist in the literature for these specific setups, the claim is defensible but would benefit from explicit scoping (e.g., "state-of-the-art among video inverse solvers using image diffusion priors").

- **Limited evaluation breadth.** All experiments use only the DAVIS dataset at 256×256 resolution with 16-frame clips. The paper does not test longer-range temporal dependencies (e.g., 32+ frames), higher resolutions, or additional datasets (e.g., GoPro, REDS). While the tested degradations (3 temporal PSFs + 3 spatial degradations) are reasonable, the generalizability of the approach to other video domains and longer sequences is unverified.

- **No discussion of failure cases or limitations.** The paper presents only successful reconstructions. It would be informative to know how the method behaves under very fast motion, large baseline temporal blur (kernel width > 13), scene cuts, or videos with frequent occlusions. Reporting such boundary behavior would increase credibility.

- **η hyperparameter values differ between temporal and spatio-temporal tasks without explanation.** The paper uses η=0.15 for temporal degradation tasks and η=0.8 for spatio-temporal tasks (Section 4, line 350), but provides no intuition or sensitivity analysis for this difference, which affects reproducibility.

- **No sensitivity analysis for the number of CG steps (l).** The number of CG steps is fixed at l=5 throughout. Varying l (e.g., 1, 3, 5, 10) would clarify the practical robustness and computational trade-offs of the core CG component.

### Trivial

- The paper's project page is listed in the abstract, but there is no explicit statement about whether code/models will be released, which is helpful for reproducibility.

## Nice-to-Haves

- A comparison to a video diffusion model adapted for inverse problems (e.g., via DPS with a pretrained video diffusion model) could further strengthen the paper's claim that image diffusion models are sufficient. However, this is not a required comparison since: (i) no such video-DIS baselines currently exist in the literature, (ii) training/fine-tuning video diffusion models is precisely what the paper argues is impractical, and (iii) all baselines fairly use image diffusion models. This would be a nice additional validation rather than a missing comparison.

- An equal-NFE comparison (e.g., DPS at 20 NFE) would show the degradation of naive DPS at low steps, though the paper's speed advantage inherently rests on using fewer NFEs, so the current time comparison at operating points is already meaningful.

- Additional temporal consistency metrics beyond FVD (e.g., warping error, per-frame flow consistency) would provide a more granular view of temporal coherence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison to video diffusion model–based inverse solvers" as a major/evidential weakness.** This reflects scope-creep: the paper's contribution is specifically about using image diffusion models (not video diffusion models), and all baselines fairly use image diffusion models. There exist no established video-DIS methods in the literature for these tasks. The paper acknowledges the difficulty of training video diffusion models as its core motivation. The baselines (DPS, DiffusionMBIR) are the correct comparisons within the paper's class.

- **"Narrow experimental scope" complaints about missing motion-compensated spatiotemporal degradations, compression artifacts, etc.** These demand breadth outside the paper's scope. The paper tests temporal PSF convolution (3 variants) + 3 spatial degradations — this is a reasonable coverage for a single paper.

- **Criticism about theoretical justification of linear-subspace argument being "incomplete."** The paper inherits DDS's well-established linear-manifold assumption and applies CG in the spatio-temporal video space. The linearity of the forward operator Ac ensures Krylov subspace methods operate correctly. Experiments validate the approach. The paper's treatment is consistent with the DDS framework it extends.

- **Complaints about missing hyperparameters, implementation details, or "undisclosed" information.** The paper reports all key hyperparameters (η, l, NFE, ADM model used) and provides pseudocode in Algorithm 1.

- **Formatting/style nitpicks** (e.g., FVD scaling notation).

## Novel Insights

The most interesting insight from the reviews is the framing of the "dilemma" (identical vs. independent frames with batch-consistent vs. batch-independent sampling) and how the paper resolves it: batch-consistent sampling ensures temporal coherence by synchronizing stochastic components, while the conditioning signal from the inverse problem (via multi-step CG) injects frame-specific diversity. This two-stage design — synchronize noise, then diversify through data-consistency optimization — is a clean conceptual separation that distinguishes this work from naive multi-frame DPS. The reviews also highlight that the dramatic speed advantage (10-50×) is not merely an implementation artifact but stems from the fundamental design choice of operating on Tweedie-denoi sed manifolds with Krylov subspace methods, avoiding backpropagation entirely.

## Suggestions

1. **Scope the "state-of-the-art" claim more precisely** to reflect that comparison is against other methods using image diffusion priors, since no video-diffusion DIS baselines exist.
2. **Add a brief discussion of failure cases**, e.g., very large temporal kernel widths, fast motion, or scene cuts where temporal consistency may break down.
3. **Provide sensitivity results** for the number of CG steps (l) and a brief justification for the different η settings across task types.
4. **State code/model release intentions** explicitly (e.g., on the project page or in a reproducibility statement).
5. **Consider adding one more dataset** (e.g., REDS or GoPro) to demonstrate generalizability beyond DAVIS.

## Score and Decision

The paper presents a novel, well-motivated, and clearly explained method that achieves impressive results with large quantitative margins and dramatic speed improvements over existing diffusion-based approaches. The weaknesses are minor and addressable — none threaten the core contribution. The method is sound, the ablation studies cleanly validate the design choices, and the practical significance (reaching >1 FPS with image diffusion models) is clear.

**Score: 8.0/10**

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>