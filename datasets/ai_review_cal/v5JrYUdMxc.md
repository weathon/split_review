- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information I need. Let me construct the final review.

## Summary

The paper proposes Fourier123, an image-to-3D pipeline that generates 3D assets from a single image in under 60 seconds. The core technical contribution is hy-FSD (hybrid Fourier Score Distillation), which supervises 3D Gaussians using Zero123 in the spatial domain (for geometric consistency) and Stable Diffusion in the frequency domain via Fourier amplitude (for texture detail). The key insight is that the two diffusion models have complementary strengths — Zero123 produces consistent geometry but over-smooth output, while SD produces rich textures but distorted structures — and using SD's output in the frequency domain (amplitude only) avoids spatial-domain conflicts while providing texture enrichment.

## Strengths

- **Novel and well-motivated hybrid spatial-frequency distillation.** The paper identifies a genuine limitation of prior work (Magic123) — that naively combining SD and Zero123 in the spatial domain leads to conflicts — and proposes a clean solution: use Zero123 spatially and SD in the frequency domain via Fourier amplitude. The frequency analysis in Fig. 1 directly motivates this design by showing that SD's output has richer mid-to-high frequency amplitude than Zero123's, corresponding to finer textures.

- **Strong ablation evidence isolating the design choice.** Tab. 1 compares five score-function variants across two frameworks (DreamFusion/NeRF and DreamGaussian/3DGS). The hy-FSD configuration (2D-FSD & 3D-SDS) substantially outperforms all alternatives — e.g., improving DreamGaussian from 0.5923 (standard 2D+3D SDS used by Magic123) to 0.7546 in CLIP-Similarity. This cleanly attributes the improvement to frequency-domain SD supervision rather than other factors.

- **Substantial quantitative and qualitative gains over strong baselines.** Fourier123 achieves best results across all metrics in Tab. 2 (CLIP-Sim 0.8010 vs. next best 0.7666, User-Qual 3.8333 vs. 3.1292) and Tab. 4 on the GSO subset (PSNR 21.50 vs. 17.22, SSIM 0.865 vs. 0.842, LPIPS 0.111 vs. 0.181). The visual comparisons (Fig. 4) show notably sharper textures and more consistent geometry than competing methods.

- **Plug-and-play generalizability.** The method is demonstrated to work with both NeRF-based (DreamFusion) and 3DGS-based (DreamGaussian) frameworks, and the paper explicitly states hy-FSD can replace existing SDS loss functions (Sec. 4.1.2). This increases the practical impact of the contribution.

- **Efficiency without quality sacrifice.** Fourier123 completes generation in 52 seconds on a single 4090 GPU — 3× faster than DreamGaussian (147s) and orders of magnitude faster than Magic123 (~3000s) — while achieving better metrics.

## Weaknesses

### Fatal
None.

### Major

- **Disconnect between motivation (pixel-space image analysis) and loss implementation (latent-space noise prediction amplitude).** The paper's central motivation (Fig. 1, Sec. 1) analyzes the frequency content of *output images* from SD and Zero123, showing that SD images have richer mid-to-high frequency amplitude. However, the actual 2D-FSD loss (Eq. 7) operates on the amplitude of the *noise prediction* ϵ_θ(z_t,t,y) and the sampled noise ϵ — both in the VAE latent space, not pixel space. The paper provides no argument or evidence that (a) the amplitude of latent-space noise predictions corresponds to image-level texture frequency, or (b) the gradient direction from A(ϵ_θ) - A(ϵ) is meaningfully related to enriching texture. In standard SDS, (ϵ_θ - ϵ) approximates a score function; replacing this with A(ϵ_θ) - A(ϵ) breaks that interpretation without a replacement theory. The method works empirically (the ablation is convincing), but the paper's *explanation* of why it works is incomplete — the bridge between observed pixel-space frequency patterns and the proposed latent-noise-amplitude gradient is missing. This does not invalidate the empirical contribution but is a significant gap in scientific rigor.

### Minor

- **GSO evaluation protocol not fully documented.** The paper reports large improvements on a 100-object GSO subset (PSNR 21.50 vs. 17.22) but does not specify: whether all methods are evaluated from identical camera trajectories, whether the evaluation views are the same views used during optimization for Fourier123 (which could bias results), or how "lateral Ground Truth" is exactly defined. The margins are large and consistent across metrics, which suggests a real effect, but the lack of protocol detail makes independent verification difficult.

- **Hyperparameter consistency in ablation not discussed.** In Tab. 1, hy-FSD replaces only the score function while other settings (learning rates, CFG scales, number of iterations, DDIM steps) are presumably kept constant across ablation variants. The paper does not state whether hyperparameters were re-tuned for each setting. If the non-hy-FSD variants would benefit from different hyperparameters, the comparison may be unfair. This is a standard concern in ablation studies worth clarifying.

- **DreamGaussian runtime discrepancy.** The paper reports DreamGaussian at 147s on a 4090 GPU (Tab. 2). The original DreamGaussian paper reports ~60s for generation. The paper does not explain this discrepancy (different resolution? more iterations? different settings?). Given that runtime is a claimed advantage, clarifying this is important for fair comparison.

- **Latent space vs. pixel space disconnect for DFT not addressed.** The DFT in Eq. 7 is applied to latent-space noise predictions (ϵ_θ and ϵ). The paper's motivation and the well-known amplitude/texture connection are typically understood in pixel space. The effect of applying frequency-domain analysis in the VAE's compressed latent space — where spatial frequencies may not correspond to image-level frequencies in a straightforward way — is not discussed.

- **DDIM step count not specified.** The paper says SD performs "a few steps" of DDIM denoising (Sec. 4.2) but does not give the exact number. This detail matters for reproducibility.

### Trivial

- **User study metrics reported with excessive precision.** User-Cons (4.5251) and User-Qual (3.8333) are reported to four decimal places based on 40 volunteers rating on a 1–5 scale. This precision is unwarranted. Reporting to two decimal places and including confidence intervals or variance would be more appropriate.

## Nice-to-Haves

- **Analysis linking amplitude differences in noise predictions to texture gradients.** A toy experiment or analysis showing that the gradient from A(ϵ_θ) - A(ϵ) aligns with standard SDS gradient for texture-rich content would strengthen the paper's scientific foundation.
- **Ablation on frequency-domain hyperparameters**, such as whether the loss at different frequency bands (low/mid/high) has different effects on the output, or comparing using both amplitude and phase versus amplitude only.
- **Impact of amplitude-only vs. including phase.** The paper correctly notes that phase carries structural information (line 125), but does not ablate whether using phase (from SD) would hurt geometry. This would further validate the design choice.

## Removed Points

These points from the reviews were evaluated and removed with justification:

- *"The 2D-FSD formulation collapses into an empirical black box whose working mechanism is not explained"* — Retained above as a Major weakness, but toned down from "structural flaw" / "fatal" because (a) the paper clearly describes the loss and its intuitive motivation, (b) the ablation study provides strong empirical support, and (c) many methods in this field are heuristic; the contribution is empirical, not theoretical.
- *"Missing appendix content / full version of visual comparisons"* — Removed as a parser artifact. The original submission contains this content.
- *"Quantitative results on GSO not credible"* — Demoted from "not credible" to Minor (documentation gap). The large, consistent margins across three metrics make it unlikely the results are spurious due to biased evaluation, but the protocol should be clarified.
- *"Missing analysis of gradient alignment between 2D-FSD and standard SDS"* — Moved to Nice-to-Haves. This is a suggestion for improvement, not a weakness.
- *"Frequency-domain hyperparameter ablation missing"* — Moved to Nice-to-Haves.
- *"Amplitude vs phase discussion missing"* — The paper DOES discuss this (lines 125–126): "Phase component is related to the content structure of the image and amplitude component means texture features." The remaining concern (lack of ablation) is moved to Nice-to-Haves.
- *Strength: "Ablation proves the key design choice"* — Kept, but weakened slightly to acknowledge the hyperparameter concern noted above.
- *Generic strengths from Strength Finder about "addressing an important problem"* — Removed. These are superficial and not specific to this paper.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's clean high-level motivation (frequency domain avoids spatial conflicts) and its rather opaque low-level implementation (amplitude of latent noise predictions). The reviewers correctly identify that the paper has not built a bridge between these two levels. This gap is not unusual for empirically-driven computer graphics papers, but it means the method's success is surprisingly contingent — small changes to the loss formulation (e.g., using denoised latent amplitude instead of noise amplitude) could either strengthen or break it, and the paper provides no guidance on which details matter. A follow-up study that systematically ablates the components of the Fourier-domain loss (noise vs. denoised latent, latent space vs. pixel space, amplitude vs. phase, different frequency bands) could both validate the current results and produce a more principled understanding.

## Suggestions

1. **Bridge the motivation-implementation gap.** Either reformulate the loss to operate on the amplitude of the *denoised latent* (z_{0|t}) rather than the noise prediction, or provide analysis (e.g., a simple 2D experiment) showing that A(ϵ_θ) - A(ϵ) correlates with image texture enrichment. This would significantly strengthen the paper.
2. **Document the GSO evaluation protocol in full detail.** Specify camera trajectories, whether evaluation views overlap with training views, and the exact rendering pipeline for all methods.
3. **Report variance/confidence intervals** for the GSO metrics and user study, and report user study scores with appropriate precision.
4. **Clarify the DreamGaussian runtime (147s vs. ~60s in the original paper)** and the DDIM step count.
5. **Ablate frequency bands** (low/mid/high) to show that the improvement comes from mid-to-high frequencies, which would directly validate the central claim of Fig. 1.
