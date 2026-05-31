Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces a method for solving video inverse problems (temporal deblurring, spatio-temporal deblurring/super-resolution/inpainting) using **only pre-trained image diffusion models**, completely bypassing the need for video diffusion models. The key ideas are: (1) treating each video frame as a separate batch element in an image diffusion model, (2) using **batch-consistent sampling** (same initialization/re-noising noise across frames) to enforce temporal consistency, and (3) applying multi-step conjugate gradient (CG) optimization on the denoised batch to impose spatio-temporal data consistency. Evaluated on the DAVIS dataset against classical baselines (ADMM-TV, CG) and 2D-diffusion-based solvers (DPS, DiffusionMBIR), the method reports large improvements in PSNR, SSIM, LPIPS, and FVD along with a 50–100× speedup over diffusion baselines.

## Strengths

1. **Novel and effective use of image diffusion models for video inverse problems** — Tables 1 and 2 show that the proposed method consistently and substantially outperforms DPS and DiffusionMBIR (which also use 2D image diffusion models) across all temporal and spatio-temporal degradation tasks. For example, on uniform PSF (k=7), Ours achieves PSNR 43.16 vs. DPS 33.42 and DiffusionMBIR 29.13. This directly supports the paper's core thesis that video diffusion models are not strictly necessary.

2. **Batch-consistent sampling is quantitatively shown to be critical** — The ablation study (Table 3, Figure 7) demonstrates that removing stochasticity control drops PSNR from 39.69 to 30.86 and increases FVD from 0.035 to 0.567. This provides clear evidence that synchronizing noise components across frames (Section 3.2, Algorithm 1) is essential, differentiating this work from prior DIS solvers that treat frames independently.

3. **Dramatic speed advantage over prior diffusion-based video solvers** — Table 1 reports Ours (20 NFE) at 12 seconds vs. DPS (1000 NFE) at 1244 seconds and DiffusionMBIR (1000 NFE) at 611 seconds — a 50–100× speedup. The paper notes speeds exceeding 1 FPS, making the approach practical.

4. **Uses a pre-trained image diffusion model without any fine-tuning or extra networks** — Stated in Section 4 ("The pre-trained unconditional 256×256 image diffusion model from ADM is used directly without fine-tuning and additional networks"), simplifying deployment.

5. **Multi-step CG on the denoised manifold (Eq. 13) improves convergence over single-step gradient descent** — Figure 7 shows CG yields substantially lower inter-batch difference and better reconstruction quality than GD, validating the Krylov-subspace optimization choice.

6. **Single framework handles both temporal-only and combined spatio-temporal degradations** — Tables 1 and 2 cover temporal PSF deblurring plus spatial deblurring, super-resolution, and inpainting with the same method, demonstrating generality.

## Weaknesses

### Fatal
None.

### Major

- **"State-of-the-art" claim is overreaching without comparison to video-diffusion-based methods** — The paper repeatedly claims "state-of-the-art" (Abstract, Introduction, Section 1 contributions) but only compares against methods that also use 2D image diffusion models (DPS, DiffusionMBIR). The paper's motivation is explicitly that training video diffusion models is difficult, and pre-trained video diffusion models exist (Stable Video Diffusion, VideoLDM, etc.). While the core technical contribution — showing image diffusion models can solve video inverse problems — does not strictly require this comparison, the unqualified SOTA claim is unsupported. The authors should either add comparisons to video-diffusion-based inverse solvers or moderate their claim to "state-of-the-art among methods using only image diffusion models."

### Minor

- **Measurement noise level is not reported, and experiments appear noiseless** — The forward model (Eq. 1) includes additive noise **W**, but the experimental setup (lines 301–305) describes generating measurements by convolving kernels with ground truth without mentioning added noise. The very high PSNRs (e.g., 43.16 dB on uniform PSF k=7) are partly explained by noiseless measurements with a known, well-conditioned operator — the CG ablation (Fig. 6) confirms CG alone "nearly solves" the problem. The paper should explicitly state whether noise is added, and if so, at what level; if not, this should be acknowledged and ideally supplemented with results at realistic noise levels to demonstrate robustness.

- **Hyperparameter choices for baselines (DPS, DiffusionMBIR) are not reported** — The paper specifies its own hyperparameters (l=5, η=0.15/0.8) but does not disclose step sizes, schedules, or tuning procedures for DPS or DiffusionMBIR. The huge gap between Ours (39.69 PSNR) and DPS (20.61 PSNR) on uniform PSF k=13 is suspicious and could partly reflect suboptimal baseline tuning. This omission weakens the reproducibility and fairness of the comparison.

- **Text inconsistency: inpainting masking ratio** — Line 305 states "random masking at a ratio r of 0," but Table 2 (column header) and Figure 5 caption both use r=0.5. This is a clear factual discrepancy in the paper's description of the experimental setup.

### Trivial

- **"DiffusiomMBIR" in Tables 1 and 2** (appears twice) — should be "DiffusionMBIR." (Note: removed per formatting rules; included here as a factual observation since it appears in the original paper content, not a parser artifact.)

## Nice-to-Haves

- **Report per-scene results or error bars** — The current tables show aggregate scores over 338 video samples without variance. Showing standard deviations or worst-case reconstructions would help assess failure modes.
- **Analyze sensitivity to inaccurate forward models** — The method assumes the forward operator **A** is known exactly. A discussion of robustness to model mismatch (e.g., space-varying motion blur) would strengthen the paper.
- **Present raw FVD values** — The FVD scaled by 10⁻³ is explained, but presenting raw values alongside the scaling would avoid confusion.

## Removed Points

These points were raised by reviewers but are removed following the consolidation guidelines. They should be treated with caution:
- **"Missing per-scene results or error bars"** — This is a nice-to-have, not a weakness; moved up.
- **"FVD scaling presentation issue"** — A presentation preference, not a flaw; moved to Nice-to-Haves.
- **"Code not included"** — Reproducibility nitpick; not a valid weakness for a conference submission.
- **"Typo criticism about DiffusiomMBIR"** — Typo/capitalization criticisms are removed per hard rules; mentioned briefly in Trivial for factual completeness.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the method that the paper itself fails to articulate. However, one observation worth noting: the paper's ablations (Figure 7, Table 3) reveal that the CG component does most of the heavy lifting for reconstruction quality (the "CG alone" result nearly solves the inverse problem), while the diffusion prior primarily removes artifacts. This division of labor — physics-based optimization for structure, generative prior for perceptual naturalness — is interesting but already discussed in the paper.

## Suggestions

1. **Moderate the SOTA claim** — Replace unqualified "state-of-the-art" claims with "state-of-the-art among DIS methods using image diffusion models" to accurately reflect the comparison scope.
2. **Add comparisons to video-diffusion-based inverse solvers** — Even on a subset of tasks, this would strengthen the paper significantly.
3. **Clarify noise levels** — State whether measurement noise was added; if not, explicitly note this and ideally add experiments with noise (e.g., σ=0.01).
4. **Report baseline hyperparameters** — Disclose the step sizes, schedules, and tuning procedures used for DPS and DiffusionMBIR to ensure fair comparison.
5. **Fix the masking ratio inconsistency** — Line 305 should read r=0.5 to match Table 2 and Figure 5.

## Score and Decision

**Originality:** Good — the batch-consistent sampling + CG on denoised batches is a clever combination not previously applied to video inverse problems.  
**Importance of research question:** High — video inverse problems with spatio-temporal degradation are underexplored in the DIS literature.  
**Claims support:** Mostly strong, but the unqualified SOTA claim is overreaching.  
**Soundness of experiments:** Solid core results with a convincing ablation study; weakened somewhat by missing noise specification and baseline hyperparameter reporting.  
**Clarity of writing:** Generally clear; one factual error (r=0 vs r=0.5) needs correction.  
**Value to the research community:** High — demonstrates a practical path to video inverse problems without video diffusion models, with large speed improvements.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>