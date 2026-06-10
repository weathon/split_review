## Summary

This paper proposes a kurtosis concentration (KC) loss for diffusion models, which encourages generated images to match the "kurtosis concentration property" of natural images (kurtosis values across DWT subbands should be nearly constant). The loss is computed as the max-minus-min of kurtosis across DWT-filtered versions of the reconstructed image and is added to the task/reconstruction losses. The method is evaluated on three tasks: personalized few-shot fine-tuning (DreamBooth/Custom Diffusion), unconditional generation (DDPM), and super-resolution (Guided Diffusion/k-diffusion), with consistent but modest improvements across metrics.

## Strengths

- **Principled theoretical framing connecting kurtosis minimization to SNR improvement (Lemma 2, Eq. 7–8, Proposition 1):** The paper derives an inverse relationship between projection kurtosis and SNR (Eq. 8), providing a theoretical rationale for why minimizing kurtosis of reconstructed images could lead to better denoising. This goes beyond heuristic perceptual losses and connects the loss to the core denoising mechanism of diffusion models.

- **Consistent empirical improvements across three diverse tasks and against LPIPS baselines (Tables 1–3):** The KC loss improves nearly all metrics (FID, MUSIQ, DINO, CLIP-I/T) across all three task categories. Improvements include: DreamBooth FID 111.76→100.08, Custom Diffusion FID 84.65→75.68, GD super-resolution FID 121.23→103.19, DDPM CelebAHQ FID 199.77→190.59. The inclusion of LPIPS as a perceptual-loss baseline in every table is appropriate and shows that KC loss outperforms this alternative.

- **Real-vs-synthetic detection experiment (Table 5) provides direct evidence of increased naturalness:** A classifier trained to distinguish real from generated images drops from 93.33% accuracy (DreamBooth) to 66.66% (DreamBooth + KC loss), providing behavioral evidence that KC loss makes images statistically harder to distinguish from natural ones.

- **Loss is parameter-simple and model-agnostic:** The KC loss introduces a single extra term added to existing losses with no auxiliary networks, no guidance requirements, and no architecture modifications. It is applied in pixel space for image-space models and via decoder for latent models, demonstrating genuine generality.

## Weaknesses

### Major

- **Data inconsistency between Table 1 and Table 2 undermines credibility:** In Table 1 (motivation), DreamBooth + KC loss is reported with MUSIQ = 68.319, identical to the DreamBooth baseline. In Table 2 (main results), the same configuration achieves MUSIQ = 69.78 — a substantial difference. The paper never acknowledges or explains this discrepancy. This is not a minor rounding issue; these are different experimental outputs for the same method. Without clarification, the reader cannot trust which set of numbers is correct, which casts doubt on the reliability of all reported results.

- **Commented-out section contains substantially different results for the same experiment (lines 448–477):** A commented-out table shows DreamBooth FID = 111.76 and DiffNat FID = 107.93 (a 3.83-point improvement), while the active Table 2 shows DreamBooth FID = 111.76 and DreamBooth + KC loss FID = 100.08 (an 11.68-point improvement — three times larger). Both refer to the same method on the same task. While commented-out sections are draft remnants, the presence of two result sets with the larger improvement selected for publication is a significant concern about result stability.

- **No error bars, confidence intervals, or multiple seeds for any experiment:** Every quantitative result in the paper is a single point with no indication of variance. The reported improvements are often modest (2–5% FID reduction, 1–3 point MUSIQ increase), and without any measure of uncertainty, it is impossible to assess whether these gains are statistically meaningful or within run-to-run variation. This is a serious omission for a paper making quantitative claims at a top venue.

- **Unconditional generation FID scores are implausibly high, suggesting poorly configured baselines:** DDPM achieves FID = 243.43 on Oxford flowers, 202.67 on Celeb-faces, and 199.77 on CelebAHQ. Standard reference implementations of DDPM on comparable datasets typically achieve FIDs well below 100 (often <20 for CelebA). Such high FID values suggest either (a) the DDPM implementation uses very few diffusion steps or very low resolution, (b) the FID computation uses an unreasonably small sample, or (c) there is an error in the evaluation pipeline. If the baseline is poorly configured, the marginal improvements from KC loss (≈2–5%) tell us little about the method's value in realistic settings.

### Minor

- **Loss weighting hyperparameters are unspecified:** The overall loss is given as $L = L_{task} + L_{recon} + L_{KC}$ (line 269) with no weighting coefficients. This makes the method non-reproducible as-is. The relative scale of the KC loss to the other losses must be tuned or at least reported.

- **No comparison with classifier-free guidance (CFG):** The paper explicitly frames KC loss as an alternative that "does not require any additional guidance like classifier or classifier-free guidance" (abstract, line 9) and criticizes guidance methods for requiring "external supervision" (line 24). Yet no experiment compares KC loss against CFG. For a paper that positions itself as providing quality improvement without guidance, the absence of this comparison weakens the claim.

- **Theoretical chain from projection kurtosis to subband kurtosis is not formally connected:** Lemma 1 establishes that projection kurtosis (kurtosis of a 1D projection wᵀx) is constant for GSM vectors. The KC loss operates on the kurtosis of entire DWT subbands (2D coefficient arrays), not scalar projections. While the kurtosis concentration property for DWT subbands is empirically documented in prior work (Zhang et al. 2014), the paper presents Lemmas 1–2 and Proposition 1 as a deductive chain directly supporting the KC loss when the connection is actually more of an empirical analogy. The paper should state this explicitly.

- **The noise variance of natural images reported as 3×10⁻⁴⁷ (Table 1) is physically implausible:** Even clean natural images from any sensor have non-zero noise. This value (effectively machine-precision zero) suggests a pipeline issue—perhaps with `skimage.estimate_sigma` on post-processed or synthetic images, or a reporting/formatting error. Since this table is used as motivation for the method, the implausible number weakens the motivating argument.

- **Real-vs-synthetic detection uses a weak forensic classifier and results are asymmetric:** The classifier is a 2-layer MLP on pre-extracted ResNet features, far from state-of-the-art forensic detectors. The effect is dramatic for DreamBooth (93.33% → 66.66%) but negligible for Custom Diffusion (94.16% → 92.5%), and this asymmetry is not discussed.

- **User study evidence is modest:** The preferred-by-50.4% result is from a four-way choice including "None is satisfactory." A 50.4% preference among four options is barely above random (25%), though still positive. Individual pairwise win rates against each baseline would be more informative.

### Trivial

- **"27 Daubechies filter banks" (line 297) is ambiguous:** Daubechies wavelets are specified by order (db1–db10+). It is unclear whether "27" refers to the wavelet order (which would be unusual), the number of filters, the number of decomposition levels, or something else. This should be clarified for reproducibility.

- **Table 1 reports MUSIQ to three decimal places (68.319)** while Table 2 rounds to two (68.31), a minor presentation inconsistency.

## Nice-to-Haves

- An ablation study varying the DWT parameters (wavelet family, decomposition levels, number of subbands) would clarify what drives the improvement and make the loss design choices less arbitrary.
- It would strengthen the paper's claimed mechanism to directly measure noise variance of generated images with and without KC loss across all three tasks (beyond the single noisy estimate in Table 1).
- For the super-resolution task, comparison with diffusion-based SR methods (SR3, SRDiff) would better situate the method in the SR literature.

## Removed Points

The following points from the source reviews were removed with justification:

- **"LPIPS is primarily a metric rather than a training loss"** — LPIPS is widely used as a perceptual loss in the literature; this criticism is inaccurate and removed.
- **"Missing other perceptual losses (VGG, style, CLIP)"** — Scope creep. The paper includes LPIPS as a reasonable perceptual-loss baseline, which is sufficient.
- **Strength about user study being "large-scale"** — 4230 tasks and 1500 questionnaires is reasonable but not exceptional; calling it "large-scale" overstates the evidence given the modest 50.4% preference result. Moved here for calibration.
- **Strength about "addressing an important problem"** — Generic, not specific to this paper. Removed.

## Novel Insights

None beyond the paper's own contributions. The review sources (harsh critic and strength finder) both engage with the paper on its own terms—confirming the theoretical connection and cross-task generality as genuine strengths while identifying data inconsistencies and missing experimental rigor as the primary weaknesses.

## Suggestions

1. **Resolve the Table 1/Table 2 MUSIQ inconsistency** by either correcting the motivation table or acknowledging and explaining the discrepancy. This is the single most damaging issue for credibility.
2. **Add error bars** (multiple seeds + confidence intervals) to every quantitative table, especially given the modest effect sizes.
3. **Specify loss weighting hyperparameters** (λ_KC) and include an ablation on the weight.
4. **Explain or remove the commented-out section** (lines 448–477) and confirm which set of results is correct.
5. **Provide a baseline quality sanity-check** for the DDPM implementation: report the number of diffusion steps, image resolution, and sample size used for FID, and compare against established reference numbers.
6. **Add a comparison with classifier-free guidance** on at least one task to substantiate the claimed advantage.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>