Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

---

## Summary

DreamClean proposes a training-free, unsupervised image restoration method that requires no knowledge of the degradation type. The approach uses DDIM inversion to embed the degraded image into the latent space of a pre-trained diffusion model, then applies a novel Variance Preservation Sampling (VPS) correction to guide latents from low-probability (degraded) regions toward high-probability (clean) regions. The method is demonstrated on linear, noisy linear, non-linear, and weather-based degradations, with quantitative results on noisy super-resolution and multiple non-align JPEG artifacts correction, and qualitative results across many other tasks.

## Strengths

1. **Training-free, degradation-blind restoration without paired data**: DreamClean requires no supervised training on degraded-clean pairs and does not assume a specific form of degradation. Despite this, it achieves competitive or superior results on two benchmarked tasks (noisy SR in Tables 1–2, multiple JPEG artifacts in Tables 3–4) against both supervised methods (FBCNN, QGAC) and unsupervised methods that exploit the degradation model (DDRM, DDNM, DDRM-JPEG). This is a genuine departure from prior work that conditions on paired data or requires knowledge of the degradation model.

2. **Broad qualitative generality across diverse degradation types**: The method is demonstrated on a genuinely wide range of degradation types in a single framework — linear (coloration, super-resolution, deblurring), noisy linear (Poisson noise, noisy SR), non-linear (multiple non-align JPEG artifacts), and complex weather (rain, snow, raindrop) — all via qualitative results in Figure 2. Additionally, integration with Stable Diffusion XL for 1024×1024 severely degraded images (Figure 1) shows the method scales beyond pixel-space diffusion models.

3. **Orthogonality to degradation-aware methods**: When the degradation model is known, DreamClean can exploit it (Section 3.5) to produce more faithful results. This is quantitatively validated for noisy SR (Tables 1–2, Ours* vs. DDRM/DDNM/DPS) and qualitatively for phase retrieval (Figure 7). This demonstrates the method is not a special-case solver but can complement existing degradation-aware approaches.

4. **Empirical validation of the VPS mechanism**: The ablation study (Section 3.6, Table 5, Figure 8) compares VPS against two natural alternatives (plain gradient ascent and vanilla Langevin dynamics) and shows VPS achieves strictly better results. This provides empirical grounding for the specific parameterization in Equation (9), even if a principled derivation is absent.

## Weaknesses

### Fatal
None.

### Major

1. **Theory–algorithm gap undermines claimed theoretical support**. Theorem 2.2 proves that VPS at a *single* timestep τ converges (as M→∞) to the High Probability Set of a clean image x₀. However, the algorithm applies *one* VPS step per timestep (M=1) during the full DDIM reverse process from τ down to t=0 — a fundamentally different regime. Furthermore, the High Probability Set (Definition 2.1) is defined using the *conditional* distribution p_t(x_t|x₀), while VPS uses the *unconditional* score ∇log p_t(y_t^{m-1}). The paper provides no argument for why an unconditional score update should drive latents toward the conditional typical set of a *specific* clean image. The paper explicitly advertises "elegant theoretical guarantees" (abstract, introduction, conclusion) as a pillar of the contribution, yet the logical chain between theorem and algorithm is broken. This does not invalidate the empirical results, but it means the theoretical claims are substantially overstated relative to what is actually proved.

2. **Quantitative evaluation is too narrow to fully support the claimed generality**. The paper's central appeal is handling "various different degradation types at one time" and achieving "superior experimental performance over various challenging tasks" (abstract). Yet quantitative comparisons with baselines are provided for only *two* tasks: noisy super-resolution (Tables 1–2) and multiple non-align JPEG artifacts (Tables 3–4). For deblurring, inpainting, Poisson noise, raindrop, snow, and coloration, only qualitative results are shown. While qualitative evidence is valuable, the claim of superiority over previous methods across many degradation types would be substantially strengthened by quantitative metrics (PSNR/SSIM/LPIPS) and comparisons to competing unsupervised methods (DPS, GDP, DDRM) on at least one or two more degradation types. The paper explicitly scopes its quantitative experiments (line 163) to these two tasks, which is honest, but this creates a mismatch with the breadth of the claims in the abstract and conclusion.

### Minor

3. **VPS parameterization is stated without derivation or principled justification**. The constraint η_l = γ(1-ᾱ_t), η_g = √(γ(2-γ))√(1-ᾱ_t) in Equation (9) is described as "required" but is never derived. The paper says this "will be discussed later in Theorem 2.2," but the theorem asserts convergence under this parameterization — it does not explain where the specific form comes from or what principle it encodes (e.g., variance preservation under a known SDE discretization). The ablation study shows this schedule outperforms two alternatives empirically, which is useful, but the method remains ad-hoc rather than principled. This undercuts the claim of "elegant theoretical supports."

4. **Ablation study is limited in scope**. Only two alternative η_g schedules are tested. There is no ablation on the number of VPS steps per timestep (M), the inverse strength τ, or the step-size parameter γ. These hyperparameters likely affect the faithfulness–realness tradeoff, and their sensitivity is unreported.

5. **Failure case analysis is shallow**. The limitation section (line 234) mentions that DreamClean fails on haze removal with ImageNet-pretrained models and "tends to generate unexpected content," but provides no analysis of *why* VPS struggles here. Understanding the failure modes would strengthen the paper by clarifying the boundaries of the approach.

### Trivial

6. **Computational cost discussion is thin**. NFEs are reported (90 blind, 60 with degradation model), but wall-clock time or memory overhead relative to baselines is not discussed.

## Nice-to-Haves

- An ablation on M, τ, and γ to show sensitivity of the method to its free parameters.
- Quantitative results on at least one additional degradation type (e.g., deblurring with a known kernel or raindrop removal) with comparisons to DPS or GDP.
- A derivation or heuristic justification of Equation (9) connecting it to SDE discretization or variance-preserving dynamics.

## Removed Points

- **Reviewer's claim that "it does not compare DreamClean (with degradation model) against DDRM, DDNM, or DPS on the same tasks"** — This is partially inaccurate. For noisy SR (Section 3.3, Tables 1–2), DreamClean* (with degradation model) IS compared against DDRM, DDNM, and DPS quantitatively. The point stands for phase retrieval (Section 3.5), where only qualitative results are shown, but the blanket statement was too broad.

## Novel Insights

Neither the harsh critic nor strength finder surfaces genuinely novel insights beyond the paper's own contributions. The most interesting observation from cross-referencing the reviews is the tension between the paper's *stated* contribution (elegant theory + broad generality) and its *actual* contribution (empirically effective blind restoration algorithm with an imperfect theoretical framing). This tension — a paper that works better than its theory would predict — could itself be a framing opportunity: the authors might strengthen the paper by presenting VPS as a *practically motivated* correction mechanism with empirical justification, rather than over-claiming theoretical completeness.

## Suggestions

1. **Reconcile the theory with the algorithm.** Either rewrite Theorem 2.2 so its setting matches the procedure (one VPS step per DDIM step across multiple timesteps), or clearly acknowledge that the theorem provides asymptotic motivation for a single-timestep correction while the full algorithm relies on the iterative application of this principle. Most importantly, address the conditional-versus-unconditional score gap — explain why the unconditional score update should drive latents toward the typical set of a clean image (even if not a specific pre-specified one). If the theory cannot be fixed without substantial new analysis, consider reframing the paper to deemphasize the theoretical claims and focus on the empirical and algorithmic contribution.

2. **Add quantitative results on at least 1–2 more degradation types** from the qualitative gallery (e.g., motion deblurring with a known kernel, or raindrop removal) with comparisons to recent unsupervised baselines. This would substantially strengthen the claim of blind generality without requiring an exhaustive benchmark.

3. **Provide a derivation or at least a clear intuition** for the VPS parameterization in Equation (9). Even a heuristic argument connecting it to variance preservation under the diffusion forward process would improve transparency.

4. **Add ablation experiments for key hyperparameters** (M, τ, γ) to help readers understand the method's sensitivity and tradeoffs.

## Score and Decision

**Originality**: 6/10 — The combination of DDIM inversion with a Langevin-like correction is creative, though both components individually are known.  
**Importance of research question**: 8/10 — Blind, training-free restoration is a genuinely important and timely problem.  
**Claims supported**: 4/10 — The theoretical claims are not well supported by the theory presented; the generality claims are only partially supported by quantitative evidence.  
**Soundness of experiments**: 5/10 — The experiments done are sound, but their scope (2 tasks quantitatively) is too narrow for the breadth of claims.  
**Clarity of writing**: 6/10 — The method description is clear, but the theoretical argument is confusing and the mismatch between claims and evidence is apparent.  
**Value to community**: 6/10 — The approach is practically useful, but in its current form the overstated claims reduce credibility.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>