Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper presents FasterCache, a training-free method for accelerating video diffusion model inference. It combines two innovations: (1) a dynamic feature reuse strategy that preserves inter-step feature variations (instead of naive caching), and (2) a CFG-Cache mechanism that exploits redundancy between conditional and unconditional outputs by decomposing their differences in the frequency domain and applying adaptive enhancement. The method is evaluated across five recent video diffusion models (Open-Sora, Open-Sora-Plan, Latte, CogVideoX, Vchitect-2.0) and achieves 1.5–1.7× speedup while maintaining competitive visual quality.

## Strengths

- **Dynamic feature reuse is a meaningful improvement over vanilla caching**: The ablation study (Table 2, visual quality) shows that replacing vanilla feature reuse with the dynamic variant raises VBench from 78.34% to 78.69% and reduces LPIPS from 0.0657 to 0.0590, while incurring negligible efficiency overhead (33.25s → 33.50s). The accompanying MSE curves (Fig. 5(a)) empirically demonstrate that the bias term reduces the feature divergence from the original model.

- **Novel frequency-domain analysis of CFG redundancy provides a principled basis for caching**: The observation that conditional–unconditional biases shift from low- to high-frequency components as sampling progresses (Fig. 2-4-1(b)) is genuinely insightful and distinguishes CFG-Cache from naive reuse or simple CFG skipping strategies. The design of frequency-specific adaptive weights follows directly from this analysis.

- **Broad generalization across diverse models, resolutions, and settings**: The method is validated on five video diffusion models with different architectures (DiT variants), resolutions (480P, 512×512), frame counts (16–192), and sampling schedulers, demonstrating consistent speedup (1.54–1.69× at single GPU) without requiring per-model tuning of the core caching schedule. The extension to I2V (DynamiCrafter) and image synthesis (PixArt-sigma) further supports generality.

- **Multi-GPU scaling demonstrates practical deployability**: Table 3 shows that FasterCache combines naturally with DSP parallelism, achieving 15.28× total speedup on 8 GPUs for Open-Sora (vs. 8.89× for the baseline). The parallel scaling efficiency is maintained or slightly improved relative to the baseline, which is relevant for deployment.

## Weaknesses

### Fatal

None.

### Major

- **VBench quality gains over competitive baselines are marginal and lack statistical significance**: Across Table 1, the VBench improvements over PAB (the most relevant training-free competitor) are at most 0.31 percentage points (Open-Sora) and in several cases the method's VBench is slightly below the original full model (Open-Sora 78.79% vs. 78.46%; Latte 77.05% vs. 76.89%; CogVideoX 80.18% vs. 79.83%). No error bars, confidence intervals, or multi-seed results are reported for any metric. While the speedup advantage is clear (1.62× vs. 1.23× on Open-Sora, etc.), the paper's claim to "consistently outperform existing methods in *both* inference speed and video quality" is only partially supported—the quality dimension rests on very narrow margins. Furthermore, PAB is not evaluated on CogVideoX or Vchitect-2.0, making direct comparison incomplete on those models.

- **Heavy reliance on similarity-to-original metrics (LPIPS, SSIM, PSNR) without corroborating absolute quality evidence**: These metrics measure how closely the accelerated output matches the original model's output, not absolute quality. A method that perfectly replicated the original would score perfectly, but this does not validate that the accelerated method produces "high quality" in any absolute sense—only that it preserves the original's outputs. VBench is the single absolute metric, and on that metric the paper's gains are tiny. The visual comparisons (Fig. 3, Fig. 6) are illustrative but subjective. Human evaluation or a broader set of absolute metrics would substantially strengthen the quality claim.

- **Hyperparameter sensitivity is unexplored**: The method introduces at least six tunable parameters (attention reuse interval=2, CFG reuse interval=5, starting step=1/3 total steps, linear slope of \(w(t)\), \(\alpha_1=0.2\), \(\alpha_2=0.2\)). The paper states that default values "perform well for most models" without providing any sensitivity analysis. Without understanding how results vary with these choices, the robustness of the method is unclear, and the risk of implicit cherry-picking cannot be dismissed.

### Minor

- **The dynamic feature reuse formula uses a first-order extrapolation without empirical or theoretical validation of the linearity assumption**: The formula \(F_{t-1} = F_{cache}^t + (F_{cache}^t - F_{cache}^{t+2}) \cdot w(t)\) assumes the feature trajectory is approximately linear over the 3-step window. While the ablation MSE curves (Fig. 5(a)) provide some empirical support that this reduces error relative to vanilla reuse, the paper does not analyze whether a more sophisticated model (e.g., quadratic, or one using more cached timesteps) would perform better. The choice of specifically the backward-looking difference \(F_t - F_{t+2}\) to predict the forward step \(t \to t-1\) is presented without justification for why the trend direction is assumed consistent.

- **The FFT-based frequency decomposition lacks a specified cutoff between low and high frequencies**: Equations 8–9 decompose outputs into low- and high-frequency components using FFT, but the paper never states how the cutoff frequency is determined (e.g., fraction of coefficients retained). This is a critical implementation detail for reproducibility.

- **Adaptation of Δ-DiT for video is not described**: The paper states "we have adapted it for video synthesis to facilitate comparison" (line 195) but provides no details of how this adaptation was performed, making this baseline result unverifiable.

- **Ablation improvements are individually small**: In Table 2 (visual quality), dynamic feature reuse adds +0.35 VBench points over vanilla FR, and the full CFG-Cache (with enhancement) adds +0.27 points over the no-enhancement version. Combined, the full method adds 0.35 points over vanilla FR. These improvements are consistent across metrics but individually small, raising the question of whether simpler alternatives (e.g., tuned reuse intervals) could achieve comparable results.

### Trivial

- The limitation discussion is honest but brief: it acknowledges occasional degradation in high-motion scenes without quantifying how often this occurs or providing a systematic analysis of failure cases.

## Nice-to-Haves

- Reporting VBench with standard deviations over multiple seeds (even 2–3) would greatly increase confidence in the reported quality claims.
- A hyperparameter sensitivity plot (e.g., varying \(\alpha_1, \alpha_2\) over [0.05, 0.5]) for at least one model would demonstrate robustness.
- A systematic breakdown of VBench per-category scores (especially motion-related categories) would clarify when degradation occurs.
- Specifying the FFT cutoff ratio is a simple documentation fix that would improve reproducibility.
- An analytic/comparison table showing PAB results on CogVideoX and Vchitect-2.0 (if feasible to run) would complete the comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The speedup factors at 8 GPUs ... imply algorithm-only speedups of 1.91× and 1.55× respectively, which are larger than the 1.62× and 1.69× at single GPU. This is not explained."* — **Removed: based on a misunderstanding.** The multi-GPU speedups in Table 3 are all relative to the same 1-GPU baseline (original model on 1 GPU), not compounded from the single-GPU algorithmic speedup. The parallel scaling efficiency of FasterCache is 9.42× (from 1 to 8 GPUs, vs. baseline 8.89×), which is consistent and slightly better, not anomalous.

- *"The dynamic reuse formula is 'not interpolation but extrapolation' ... 'conceptually questionable.'"* — **Removed: the paper never claims the formula is interpolation.** The paper describes the approach as using the feature difference as a "bias for approximating the feature variation trend." The reviewer's framing as "interpolation" is a strawman. The underlying concern about linearity assumption is kept as a minor weakness.

- *"The paper should discuss why this similarity is not trivially exploited (e.g., by simply using the conditional output as unconditional) — it does, showing quality degradation."* — **Removed: the paper already addresses this** at line 155 ("A naive approach... leads to a noticeable degradation..."). The reviewer even acknowledges "it does, showing quality degradation."

- *Missing related works.* — **Removed per instruction: external confirmation of missing references is not available.**

- *"Cannot be independently verified" / "not yet released" type comments* — **Removed per instruction: all cited benchmarks, models, and references are assumed to exist.**

- *"The claim to 'pioneering investigation of CFG's potential for acceleration' is overstated"* — **Partially kept as context but the specific frequency-domain analysis is novel.** The reviewer's claim that CFG caching has been explored before (e.g., CFG early stopping) is not supported by specific references, and the paper's contribution is the *frequency analysis*, not merely noticing CFG is expensive. Weakened to a trivial observation rather than a substantive weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add standard deviations or confidence intervals to the main VBench results (Table 1) by running at least 2–3 seeds. If computational cost is prohibitive, at minimum add a statement acknowledging single-run evaluation and the need for caution in interpreting small margins.
2. Add a hyperparameter sensitivity study (e.g., varying \(\alpha_1, \alpha_2\) and the CFG reuse interval) for one representative model and report the resulting VBench/latency trade-off.
3. Specify the FFT cutoff ratio used for the low/high frequency decomposition in CFG-Cache.
4. Briefly describe how Δ-DiT was adapted for video, or cite the implementation if publicly available.
5. Include a per-category breakdown of VBench scores to quantify when and how often degradation occurs in high-motion scenes, directly addressing the paper's acknowledged limitation.
6. Consider including PAB results on CogVideoX and Vchitect-2.0 to complete the comparison table.

## Score and Decision

The paper presents two clean, well-motivated ideas for training-free video diffusion acceleration and validates them across a diverse set of modern models with consistent speedup. The weaknesses are substantive but not fatal: the quality advantage over competitors is thin and lacks statistical validation, and several methodological details are underspecified. These issues are addressable with additional experiments and documentation. The core contributions—dynamic feature reuse and frequency-aware CFG caching—are sound and practically useful.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>