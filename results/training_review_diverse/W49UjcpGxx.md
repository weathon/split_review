Now I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

FasterCache proposes two training-free techniques for accelerating video diffusion model inference: (1) a dynamic feature reuse strategy that extrapolates cached attention features (using a linear bias from two cached steps) instead of naively copying them, and (2) CFG-Cache, which reuses conditional/unconditional residuals decomposed into low- and high-frequency bands with timestep-adaptive weighting. The method is evaluated on five video diffusion models (Open-Sora 1.2, Open-Sora-Plan, Latte, CogVideoX, Vchitect-2.0), achieving 1.54–1.68× speedup while maintaining VBench scores close to the unaccelerated baseline and substantially outperforming existing cache-based methods Δ-DiT and PAB on perceptual metrics.

## Strengths

- **Novel identification and exploitation of CFG redundancy.** The paper discovers that conditional and unconditional outputs at the *same* timestep are far more similar than features across adjacent timesteps, and that their disparities shift systematically from low-frequency to high-frequency as sampling progresses (Fig. 2-3-1a, Fig. 2-4-1b). This insight directly motivates CFG-Cache, which stores frequency-decomposed residuals and reuses them adaptively — a genuinely new direction in video diffusion acceleration. Table 1 shows that FasterCache with CFG-Cache matches or improves the baseline VBench score (e.g., Vchitect-2.0: 80.80% → 80.84%) while competing methods all degrade.

- **Consistent superiority across five diverse video diffusion models.** The evaluation spans Open-Sora 1.2, Open-Sora-Plan, Latte, CogVideoX, and Vchitect-2.0 — varying in architectures, resolutions, frame counts, and sampling schedulers. FasterCache achieves the highest speedup on every model and simultaneously the best LPIPS/SSIM/PSNR, often by a large margin (e.g., CogVideoX LPIPS: 0.0766 vs. best Δ-DiT 0.3319). This breadth makes the empirical claims robust.

- **Clear ablation isolating each component's contribution.** Tables 3 and 4 decompose the method: dynamic feature reuse recovers ~0.35% VBench over vanilla reuse; CFG-Cache with frequency enhancement adds further quality gains; and the efficiency benefit of combining both components is quantified (26.12s vs. 41.28s baseline). Fig. 5 visually validates the role of low- vs. high-frequency bias compensation.

- **Scalability demonstrated to multi-GPU and varying video sizes.** Table 5 shows that when combined with Dynamic Sequence Parallelism, FasterCache maintains superior speedups as GPUs scale (e.g., 15.28× on 8 A100s for Open-Sora, vs. 11.16× for PAB). Fig. 6 shows stable acceleration across resolutions 320P–720P and frame counts 48–320.

## Weaknesses

### Fatal
None.

### Major
- **Δ-DiT adaptation for video is not described, creating an unfair-comparison concern.** The paper states (line 195): "Notably, Δ-DiT was originally designed as an acceleration method for image synthesis. Here we have adapted it for video synthesis to facilitate comparison." No further detail is given about how the adaptation was performed — how temporal attention layers were handled, whether Δ-DiT hyperparameters were re-tuned for video, or whether the adaptation was applied uniformly across all models. While the paper tests multiple Δ-DiT configurations (different *Nc* values), the reader cannot assess whether these configurations represent a reasonable or optimal adaptation. If Δ-DiT was suboptimally adapted, the claimed superiority of FasterCache could be overstated. This is the most significant weakness and should be addressed by adding a detailed description (even in supplementary) of the adaptation procedure.

### Minor
- **No ablation on the CFG-Cache interval (*n*=5) or starting point (1/3 of steps).** These choices directly control the trade-off between speed and quality, yet the paper provides no sensitivity analysis. The method would be stronger with an ablation showing how VBench score and speedup vary when the cache interval is set to *n*=1, 3, 5, 7, or when the starting point shifts to 1/4 or 1/2 of total steps.

- **No sensitivity analysis for the hyperparameters α₁, α₂ (both defaulted to 0.2).** The paper states these values "perform well for most models" (line 208), but without any evidence of how quality varies when they are changed. A simple sensitivity curve (e.g., VBench vs. α over [0.05, 0.5]) would substantially increase confidence in the method's robustness.

- **Limited analysis of failure cases.** The limitation section (line 468) mentions degraded results in "complex scenes with substantial video motion" and says this "can be remedied through manual adjustments of hyperparameters." This understates the practical difficulty: users seeking a fully automatic acceleration method cannot tune hyperparameters per prompt. The paper would benefit from quantifying how often degradation occurs (e.g., over a set of high-motion VBench prompts) and whether the degradation is model-dependent.

### Trivial
- **Single visual example (Fig. 4, stars) for the feature degradation claim.** While the paper provides accompanying quantitative MSE evidence, the visual case study is limited. Showing one or two additional examples would strengthen the motivation. This does not affect the validity of the paper's claims.

## Nice-to-Haves
- An ablation comparing the linear extrapolation in Eq. (2) against simpler alternatives (vanilla reuse, second-order extrapolation) to directly quantify whether the linear bias term is the best simple choice.
- Reporting variance (e.g., standard deviation) or per-dimension VBench breakdowns across prompts, since the table reports only single aggregate numbers.
- A brief discussion contextualizing the 1.54–1.68× speedup against orthogonal step-reduction methods (e.g., DPM-Solver, LCM) that can achieve 2–4× by reducing the number of sampling steps, noting these are complementary.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Pioneering" claim too strong / missing prior CFG caching work.** The reviewer asserts prior work exists on CFG caching in image diffusion but provides no specific citations. Without verifiable prior art, this criticism cannot be sustained. The paper's claim is defensible within its stated context (video diffusion with frequency-domain analysis). *Reason: DO NOT mention missing related works (hard rule).*

2. **Ambiguity about what "outputs" means in CFG analysis.** The reviewer asks whether "outputs" refers to attention features or model predictions. The paper is clear: Section 3.1 (Preliminary) defines CFG as computing noise predictions ε_θ(x_t,c) and ε_θ(z_t,∅), and the MSE analysis in Section 3.3 uses the same terminology consistently. *Reason: Criticisms that misunderstand the paper (hard rule).*

3. **LPIPS/SSIM/PSNR should note they measure fidelity to original.** The paper already states (lines 200–201): "LPIPS, PSNR, and SSIM measure the similarity between videos generated by the accelerated sampling method and those from the original model." *Reason: Criticism already addressed in the paper.*

4. **Multi-GPU scaling numbers don't match.** The reviewer claims 243.33/37.13 = 6.55× does not match 8.53×. This is a miscalculation: all speedup factors in Table 5 are relative to the original model's single-GPU latency (316.71s). Indeed, 316.71/37.13 = 8.53×, which is correctly reported. *Reason: Factually wrong (hard rule).*

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core findings (CFG redundancy within timesteps, frequency-domain shift of CFG biases, and the effectiveness of dynamic feature extrapolation) without introducing new observations not already in the paper.

## Suggestions

1. **Describe the Δ-DiT video adaptation in detail.** Even a short paragraph or supplementary section explaining how Δ-DiT's residual caching was applied to temporal attention layers, any hyperparameter changes, and validation that the adaptation produces reasonable results would resolve the main fairness concern.

2. **Add sensitivity ablations for the CFG-Cache interval, starting point, and α₁/α₂.** A small grid search showing the quality–speed Pareto frontier would transform these heuristics into well-characterized design choices and substantially strengthen the paper.

3. **Quantify the high-motion failure mode.** Run FasterCache on a set of prompts known to produce high motion, report how often quality degrades relative to the baseline, and characterize the degradation pattern. This would turn a vague limitation into actionable knowledge for practitioners.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>