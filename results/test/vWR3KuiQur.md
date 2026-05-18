Now I have all the evidence I need to construct the final review.

---

## Summary

This paper proposes SVDQuant, a 4-bit post-training quantization paradigm for diffusion models that introduces a 16-bit low-rank branch to absorb outliers shifted from activations to weights via smoothing. The co-designed inference engine Nunchaku fuses the low-rank branch kernels into the low-bit kernels, cutting memory-access overhead and enabling measured speedup. The method is validated on UNet (SDXL, SDXL-Turbo) and DiT backbones (PixArt-Σ, FLUX.1) at both INT4 and FP4 precisions, achieving 3.0× speedup over an NF4 weight-only baseline on a 12B FLUX.1 model while largely preserving image quality.

## Strengths

1. **Novel and well-motivated quantization paradigm.** The core idea—first consolidating outliers from activations to weights via smoothing, then absorbing the magnified weight outliers into a 16-bit low-rank branch via SVD—is elegant and clearly explained. The paper demonstrates empirically (Figure "singular values", Figure "distribution") that the residual after this decomposition has substantially reduced magnitude and fewer outliers, enabling effective 4-bit quantization of both weights and activations. The ablation study (Figure "ablation") confirms that smoothing + SVD significantly outperforms smoothing-only and prior low-rank compensation (LoRC) approaches.

2. **Co-designed inference engine that makes the low-rank branch nearly cost-free.** A key practical insight: naively running the low-rank branch separately incurs ~50% overhead due to redundant memory access. By fusing the down-projection with the quantization kernel and the up-projection with the 4-bit computation kernel, Nunchaku reduces the overhead to 5–10%. This systems contribution is critical—without it, the additional branch would negate the quantization speedup. The paper reports a measured 3.0× speedup over the NF4 weight-only baseline on the 12B FLUX.1 model (Figure "efficiency"), demonstrating that the approach delivers real inference acceleration on current hardware.

3. **Broad validation across architectures, model scales, and data types.** The method is evaluated on three distinct model families (SDXL 2.6B UNet, PixArt-Σ 600M DiT, FLUX.1 12B DiT), supports both INT4 and FP4, and consistently outperforms or matches 8-bit baselines (ViDiT-Q, MixDQ, TensorRT). The quality results in Table 1 show that SVDQuant W4A4 models achieve competitive or superior FID, Image Reward, LPIPS, and PSNR relative to W4A8/W8A8 competitors.

4. **Seamless integration with off-the-shelf LoRAs without re-quantization.** The engine's kernel fusion design allows LoRA adapters to be absorbed into the low-rank branch by slightly increasing the rank, avoiding the re-quantization overhead that prior methods require. Visual results across five different LoRA styles are provided.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses identified below are addressable and do not threaten the paper's core claims.

### Minor

1. **Proposition 2's normality assumption is unsubstantiated and the proposition adds little.** The paper assumes the residual R follows a normal distribution to bound quantization error by its Frobenius norm (line 108). This assumption is not justified for the residual after smoothing + SVD, which could have a structured, non-Gaussian distribution. More importantly, the proposition is used only to motivate minimizing ‖R‖_F—which is already justified by the Eckart–Young–Mirsky theorem (line 115). The proposition is not needed for the paper's contribution; the empirical observation that R has smaller magnitude and fewer outliers (Figure "singular values", Figure "distribution") is sufficient and more honest. This does not affect the validity of the experimental results, but the paper would be stronger by dropping or relaxing the normality assumption.

2. **The ablation study is conducted only on PixArt-Σ (600M), not on FLUX.1 (12B).** While computational cost is a reasonable explanation, the paper's headline results are on FLUX.1, and the effectiveness of smoothing + SVD decomposition may behave differently for larger models with different outlier structure. A targeted ablation on a subset of FLUX.1 layers or timesteps would substantially increase confidence that the core mechanism translates to the largest model. Without this, there is a minor gap between the ablation's conclusions and the main results.

3. **Details of the iterative refinement are missing.** Section 4.2 (line 116) mentions "iteratively updating the low-rank branch through decomposing W − Q(R) and adjusting R accordingly for several iterations, and then picking the result with the smallest error," but no specifics are given on the number of iterations, convergence criteria, or how the "smallest error" is measured. This affects reproducibility.

4. **The W4A4 vs. W4A8 quality comparison, while credible, would benefit from a controlled ablation.** The paper claims that its W4A4 results outperform ViDiT-Q's and MixDQ's W4A8 results. Because different calibration protocols, group sizes, and quantization granularities may differ across methods, it is not fully clear whether the advantage is solely attributable to SVDQuant's design. The paper partially addresses this by computing ViDiT-Q's similarity metrics from their FP16 results (footnote in Section 5.2), but a controlled comparison where only the bit-width varies (e.g., SVDQuant W4A4 vs. SVDQuant W4A8) on PixArt-Σ would cleanly isolate the method's contribution from bit-width effects.

5. **The offline computational cost of SVD decomposition is not reported.** For a 12B model with many linear layers, the calibration cost (including SVD) could be nontrivial. A brief note on the wall-clock time or GPU-hours required would help practitioners assess practicality.

### Trivial
None.

## Nice-to-Haves

- A direct speedup measurement over the original BF16 model on a desktop 4090 (24 GB, where the model fits without offloading) would complement the existing 3.0× over NF4 and isolate the end-to-end benefit of W4A4 quantization from memory-capacity effects. The paper already reports 3.0× speedup on both desktop and laptop 4090 GPUs over NF4; adding the corresponding BF16 baseline comparison would make the speedup story more complete.
- The paper's "first to achieve measured W4A4 speedup on diffusion models" claim could be stated slightly more guardedly—e.g., "to our knowledge, the first"—which it already does (line 25: "To our knowledge, we are the first…").

## Removed Points

These points were flagged by reviewers but are removed or downgraded based on cross-checking against the paper:

- **Speedup baseline confusion (Harsh Critic point 3 partial):** The reviewer claimed the "3.0× speedup" baseline could be misinterpreted. However, the paper explicitly and repeatedly states "over the 4-bit weight-only quantized baseline" / "over the NF4 weight-only-quantized variant" (abstract line 5, Section 5.2 line 175). The paper also explains that weight-only quantization does not accelerate computation (line 21–22). The reported numbers are unambiguous. The request for a raw BF16 speedup is a useful addition (moved to Nice-to-Haves) but the characterization that the framing is "confusing" is not supported by the paper's text. 
- **"Paper does not report time or compute cost of SVD decomposition"** — Retained as Minor weakness 5 (genuinely useful information for practitioners).
- **"No details given (number of iterations, convergence criteria)"** — Retained as Minor weakness 3.

## Novel Insights

The most interesting insight from the cross-review is that SVDQuant inverts the standard LoRC logic: instead of using a low-rank branch to *compensate for* quantization error after quantization (which fails because quantization errors have a smooth singular spectrum), it uses SVD to *pre-remove* the dominant singular components from the weight *before* quantization, leaving a residual that is both smaller in magnitude and easier to quantize. This distinction—absorbing outliers vs. compensating for errors—is conceptually clean and explains why prior low-rank+quantization approaches underperform. The Nunchaku kernel fusion strategy (fusing down-projection with quantization, up-projection with 4-bit compute) is a pragmatic engineering insight that directly addresses the concern that additional branches negate speedup, and the fact that it naturally handles LoRA adapters is a nice bonus.

## Suggestions

1. Drop the normality assumption from Proposition 2 and restructure it as an empirical observation or a heuristic motivation. The Eckart–Young–Mirsky theorem already guarantees that ‖R‖_F is minimized by SVD truncation, which is sufficient for the paper's purposes.
2. Add a targeted ablation on FLUX.1—even on a subset of attention blocks or a reduced set of timesteps—to verify that the smoothing+SVD mechanism behaves similarly at 12B scale.
3. Report the number of iterations and convergence criterion used for the iterative refinement (Section 4.2).
4. Provide a controlled comparison on PixArt-Σ: SVDQuant W4A4 vs. SVDQuant W4A8, holding all other factors (calibration data, group size, etc.) fixed. This would directly confirm that the quality advantage over baselines' W4A8 comes from the method rather than uncontrolled variables.
5. Briefly report the offline calibration cost (GPU-hours) for SVD decomposition on the 12B model.

## Score and Decision

The paper presents a novel, well-motivated quantization method for diffusion models with a co-designed inference engine that delivers real measured speedup. The experimental evaluation is broad (3 model families, 2 data types, multiple metrics) and the results convincingly support the core claims. The identified weaknesses (unsubstantiated normality assumption, ablation scope limited to PixArt-Σ, missing iterative refinement details, uncontrolled cross-baseline comparison, unreported SVD cost) are minor and addressable. The paper makes a genuine contribution to efficient diffusion model inference.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>