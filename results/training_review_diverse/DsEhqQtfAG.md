Now I have verified all reviewer claims against the actual paper. Let me produce the final consolidated review.

---

## Summary

The paper proposes Decomposed Diffusion Sampling (DDS), a method that replaces the computationally expensive manifold-constrained gradient (MCG) in diffusion-based inverse problem solvers with efficient Conjugate Gradient (CG) iterations on the denoised estimate. The theoretical insight is a conditional proof: if the tangent space at a denoised sample forms a Krylov subspace, then CG updates stay within that tangent space, making MCG unnecessary. The method is applied to large-scale medical imaging (multi-coil MRI and 3D CT), achieving 80–200× inference speedups over prior diffusion solvers while maintaining or improving reconstruction quality.

## Strengths

- **Dramatic and well-documented practical acceleration.** DDS achieves state-of-the-art results with 19–99 NFE on tasks where prior methods require 1000–4000+ NFE. For 4× accelerated multi-coil MRI, DDS (99 NFE) reaches 34.88 dB PSNR vs. Score-MRI (4000 NFE) at 33.25 dB (Table 1). For 8-view CT, DDS (49 NFE) surpasses DiffusionMBIR (4000 NFE) at both PSNR and SSIM (Table 4). Wall-clock times are reported (e.g., ~4.7 sec for 49 NFE MRI; ~25 min vs. ~2 days for CT on a single RTX 3090).

- **Broad experimental validation across challenging real-world tasks.** The paper evaluates on 5 MRI sampling patterns (including non-Cartesian NUFFT), multiple acceleration factors, noisy measurements, and two CT tasks (sparse-view and limited-angle), with both VP and VE diffusion schedules. This goes well beyond typical benchmarks in the DIS literature.

- **Principled handling of noisy measurements without SVD.** The proximal CG formulation (Eq. 17) avoids singular value decomposition, which is non-trivial for medical imaging forward operators. DDS (49 NFE) outperforms DPS (1000 NFE) by >5 dB PSNR on noisy MRI while being ~40× faster (Table 3).

- **Clean conceptual connection between Krylov methods and diffusion geometry.** The observation that MCG is a single-step projected gradient (Proposition 1) and that multi-step CG can replace it under a Krylov subspace condition (Section 3) provides a principled framework for understanding why numerical optimization on the denoised estimate works well.

## Weaknesses

### Fatal
None.

### Major

- **The paper's central theoretical claim rests on an unverified condition that is not argued or tested.** The paper proves that *if* the tangent space at a denoised sample coincides with a Krylov subspace of the forward operator, *then* CG updates stay within that tangent space. However, it provides no evidence — empirical or theoretical — that this Krylov subspace condition holds (or approximately holds) for any of the tested forward operators (MRI Fourier sampling, CT Radon transform) or for natural image manifolds. The paper acknowledges the affine subspace assumption is an approximation (line 229), but the leap from "affine subspace" to "tangent space = Krylov subspace of A" is never justified. Without this, the theoretical framing is a motivating intuition rather than a verified explanation. The method's practical success is well-demonstrated empirically, but the paper should either (a) provide evidence of subspace containment (e.g., measuring how close CG-updated images stay to the estimated tangent space via local PCA or Jacobian analysis), or (b) clearly reframe the theory as an intuitive motivation and present the method as a well-motivated heuristic.

### Minor

- **DPS baseline uses a non-standard sampling variant, and step-size re-tuning is not documented.** The paper uses DDIM sampling for DPS (line 348) rather than its original ancestral (DDPM) sampling. While the authors provide a rationale (isolating the effect of CG vs. MCG by keeping the sampling strategy fixed), DPS's step size γ was originally designed and tuned for ancestral sampling. The paper reports grid search on η for DPS but does not state whether γ was re-tuned for DDIM. If γ was not adjusted, this could disadvantage DPS. Given the large performance gap, the main conclusion is likely robust, but the concern should be addressed.

- **The choice of M=5 CG iterations is disconnected from the theoretical condition.** The theory requires M ≤ *l* where *l* is the (unknown) Krylov subspace dimension matching the tangent space. M=5 is chosen via ablation on a single configuration (uniform 1D ×4, 49 NFE). This empirical approach is standard and the ablation is useful, but the paper would be stronger with a broader sensitivity analysis across tasks and with some attempt to estimate *l* or verify subspace containment.

- **Missing standard deviations in the noisy MRI results (Table 3).** The noiseless MRI results (Table 1) report mean ± std, but the noisy results (Table 3) report only means. The CT results (Table 4) indicate std values are deferred to a supplementary table, which is acceptable if present.

- **The η values for DDS vary with NFE (0.15 for 19 NFE, 0.5 for 49, 0.8 for 99) without explanation of how to set this parameter in practice.** This suggests η may be sensitive to sampling aggressiveness, which is relevant for practitioners trying to reproduce the method.

### Trivial

- **Minor formatting inconsistency:** The paper claims to be "step-size-free" (line 316) regarding the CG optimization, but the overall method still requires tuning η and γ. This scope nuance is clear in context but could be clarified to avoid confusion.

## Nice-to-Haves

- An explicit comparison between DDS and DPS with the original ancestral (DDPM) sampling at comparable NFE (even if approximate) would strengthen the baseline fairness argument.
- For the ablation on CG iterations (M), testing across multiple mask patterns and acceleration factors (beyond uniform 1D ×4) would increase confidence in the robustness of M=5.
- A brief discussion or visualization of failure cases (e.g., 2-view CT where DDS still outperforms baselines but performance degrades) would help users understand limitations.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. Criticisms about missing comparisons against non-DIS methods (e.g., compressed sensing with learned dictionaries): The paper's scope is diffusion-based inverse solvers, and it already includes strong CS baselines (TV, ADMM-TV). Demanding coverage of orthogonal literature classes is scope creep.

2. Claim that the paper's theoretical claim is presented as a "given" condition: The paper repeatedly uses "if" and "Suppose" language (line 247, abstract "if the tangent space... forms a Krylov subspace"). The conditionality is transparent. The real weakness is the lack of verification, which is kept in Major.

3. Suggestion that wall-clock times should be tabulated across all methods: The paper reports wall-clock times for DDS (lines 391, 476) and notes the dramatic contrast with prior methods (Score-MRI's 120k NFE, DiffusionMBIR's 2 days). A systematic table would be nice but the data is effectively communicated.

4. Demand for comparison against DDNM in the main MRI table: DDNM is compared in the dedicated ablation (Table 1 in text), which is the appropriate place for a method that the paper argues is conceptually inferior for medical imaging. Its omission from the main table is justifiable.

5. Criticism that the paper "oversells the theoretical guarantee": The paper's language ("we prove that if... then...") is technically accurate as a conditional proof. The issue is the unverified premise, which is already captured in the Major weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate the paper's empirical strengths and identify the gap between its theoretical framing and the evidence provided. No reviewer identified a structural flaw or novel application the authors missed.

## Suggestions

1. Add an experiment that provides empirical evidence about the tangent-space-containment property. For a few representative cases, estimate the tangent space (e.g., via the Jacobian of the denoiser or local PCA) and measure the distance between the CG-updated denoised image and its projection onto that space. This would directly test the paper's motivating assumption.
2. For the DPS baseline, either (a) report results with ancestral (DDPM) sampling and document step-size re-tuning, or (b) more clearly justify why DDIM is the appropriate comparison and state whether γ was re-tuned.
3. Add standard deviations to Table 3 (noisy MRI), and move std values for CT from the appendix into the main table or clearly reference the appendix.
4. Provide guidance on how to set η in practice (e.g., a heuristic or a small ablation).
5. Broaden the ablation on M (CG iterations) to at least one more mask/acceleration combination to support the claim that M=5 is generally robust.

## Score and Decision

**Originality:** Good — the combination of CG with diffusion for the tangent-space property is novel.  
**Importance of research question:** High — accelerating DIS for medical imaging is practically significant.  
**Claims well supported:** Generally yes for empirical claims; the theoretical framing lacks verification of its key premise.  
**Soundness of experiments:** Good breadth and quality, with minor gaps (DPS DDIM variant, missing std).  
**Clarity of writing:** Clear.  
**Value to community:** High — the speed-quality tradeoff is genuinely useful for medical imaging.

The paper makes a strong empirical contribution with a useful practical method. The main weakness is the gap between the theoretical framing and the evidence for its key premise — but this does not invalidate the empirical results, which speak for themselves. The other issues are addressable in revision.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>