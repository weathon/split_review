## Summary

VIPaint proposes a hierarchical variational inference procedure for conditioning pre-trained diffusion models on partial observations, focusing on image inpainting. The method defines a variational posterior over a strategically chosen subset of intermediate diffusion timesteps (SNR ≈ 0.2–0.5), fits it by optimizing a variational lower bound, then samples from the fitted posterior to produce reconstructions. The approach works with both pixel-based (EDM) and latent diffusion models without retraining or fine-tuning.

## Strengths

- **Principled hierarchical variational posterior over intermediate diffusion timesteps (Section 3.1).** Rather than defining the posterior at the noise-free pixel level (as Red-Diff does), VIPaint operates in a mid-noise regime where the denoising function is better behaved. The convex combination between the prior denoising prediction and a learned variational parameter (Eq. 5) is a clean design that allows posterior adaptation without retraining the diffusion model.

- **Evidence of effectiveness with both pixel-based and latent diffusion models.** The paper demonstrates VIPaint on EDM (ImageNet-64) and LDM backbones (ImageNet-256, LSUN-Church), including comparisons against LDM-specific baselines (PSLD, ReSample, DPS). This is a meaningful advance since many prior inpainting methods are designed for pixel-space models only.

- **Efficient optimization (Section 3.3).** VIPaint requires only O(KI) denoising network calls for the optimization phase (e.g., ~150 calls for VIPaint-2 with 50 iterations), which is modest relative to full sequential sampling. The complexity analysis, while incomplete (omits backprop cost), provides a reasonable first-order accounting.

- **Qualitative results are visually compelling.** Figures 6–8 show plausible inpaintings under large masks (~50–80%), where baselines produce visible artifacts or fail to complete images meaningfully. The diversity of outputs shown in Fig. 8 provides some support for the uncertainty-capturing claim.

## Weaknesses

### Fatal
None.

### Major

- **LPIPS is part of VIPaint's optimization objective for LDM experiments, and LPIPS is the primary evaluation metric — creating a circular comparison.** Line 200 explicitly states: "For latent diffusion models specifically for the task of image inpainting, we add the perceptual loss (LPIPS) that was also originally used to train the decoder." Table 1 then reports LPIPS as the quantitative result. VIPaint optimizes what it is measured on for the LDM experiments (ImageNet-256, LSUN-Church), while none of the baselines (ReSample, PSLD, DPS) optimize LPIPS during inference. This systematically favors VIPaint in the comparison. The EDM-based experiments (ImageNet-64, top of Table 1) are **not** affected by this issue because VIPaint uses L1 reconstruction loss there. However, since the LDM experiments constitute a substantial portion of the evidence, the quantitative claims for those settings are compromised. The paper does not acknowledge this circularity or provide any control (e.g., reporting FID, KID, or PSNR as primary metrics in addition to LPIPS).

- **No variance or uncertainty quantification for any quantitative result.** Table 1 reports point estimates only — no standard deviations, standard errors, or confidence intervals. With only ~33 test images per dataset (100 images across 3 datasets, line 300), the reported differences (e.g., VIPaint-2 LPIPS 0.227 vs. CoPaint-TT 0.245 on ImageNet-64 Random Mask) may or may not be statistically significant. The paper provides no basis for the reader to judge. For a submission to a top venue claiming state-of-the-art results, reporting variance is standard practice.

### Minor

- **The variational bound's approximation from skipping intermediate timesteps is not discussed.** VIPaint defines its posterior over only K selected timesteps (K=2 or K=4), explicitly "skipping intermediate noise levels" (Fig. 1 caption). The bound in Eq. 6 includes KL terms only at these selected steps. The paper does not discuss how omitting the skipped transitions affects bound tightness or whether the approximation error decreases with increasing K. This is a methodological gap worth acknowledging.

- **Missing experimental details for reproducibility.** Several key hyperparameters are not reported in the main text: the number of Monte Carlo samples (M), the learning rate and optimizer, and the exact value of β (only stated as "> 1" in Eq. 6). While specific timestep values are given for one configuration (Fig. 1: Tₑ=550, Tₛ=400), the paper relies on an SNR range [0.2, 0.5] (line 162) rather than reporting exact values for each model. These details are necessary for reproducibility of the per-query optimization procedure.

### Trivial
None.

## Nice-to-Haves

- Report FID or KID as an additional metric that VIPaint does not directly optimize, which would strengthen the claim of genuine improvement.
- Include a wall-clock time comparison with baselines (the current complexity analysis measures only forward passes, not the cost of backpropagation through the denoising network in Phase 1).
- Ablate the choice of K beyond K=2 vs. K=4, and study sensitivity to the specific selected timesteps within the SNR [0.2, 0.5] range.
- Report a quantitative diversity metric (e.g., LPIPS between samples, or recall) to substantiate the claim that the hierarchical posterior captures uncertainty rather than collapsing to a single mode.

## Removed Points

- **Super-resolution/deblurring claims unsupported in main paper (Harsh Critic, issue 3).** The paper cross-references Table `\ref{tab:performance_metrics_LIP_}` and Figures `\ref{fig:super-resolution}`, `\ref{fig:gaussian-deblurring}` which are absent from the provided text. Per the review guidelines: the parser strips appendix sections from all papers; these exist in the original submission. This criticism is removed.
- **Missing hyperparameters criticism (partially).** Some details (e.g., learning rate, exact β, M) could be in the stripped appendix. The criticism is retained in weakened form (Minor tier, with acknowledgment that appendix may contain them).
- **"Test set extremely small" — softened.** While 100 images across 3 datasets is modest, it is within the range of common practice in this sub-area. The real issue is the lack of error bars, not the absolute number.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not surface any unexpected connection or broader implication not already articulated in the paper.

## Suggestions

1. **Disentangle evaluation from optimization.** For LDM experiments, either remove the LPIPS term from VIPaint's reconstruction loss (relying only on L1), or report FID/KID/PSNR as the primary metric. This is essential to make the quantitative comparison fair.
2. **Report error bars.** Compute standard errors over images and/or samples per image for all metrics in Table 1. This is especially important given the modest test set size (~33 images per dataset).
3. **Either provide quantitative results for super-resolution/deblurring or temper the generality claims** in the abstract and title.
4. **Acknowledge and discuss the approximation introduced by skipping intermediate timesteps** and how bound tightness depends on K.

## Score and Decision

The paper introduces a genuinely novel methodological idea — hierarchical variational inference over a sparse subset of diffusion timesteps — and demonstrates visually compelling results, especially for large-mask inpainting with both pixel and latent diffusion models. However, the quantitative evaluation has a significant flaw: LPIPS is both optimized (for LDMs) and used as the primary evaluation metric, creating a circularity that undermines the LDM experimental results. The lack of any variance reporting further weakens the quantitative claims. The method's generality to other inverse problems cannot be assessed from the visible text.

The core idea has merit, but the evidence in its current form does not meet the standard for acceptance at a top venue. Substantial revision of the evaluation (disentangling optimization from metrics, adding error bars, providing complete generalization results) would be needed.

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>