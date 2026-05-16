Now I have all the information needed. Let me produce the consolidated review.

## Summary

InstantIR introduces a diffusion-based blind image restoration (BIR) method that dynamically adjusts generation conditions during inference. The key innovations are: (1) a **Previewer** module — a consistency-distilled one-step generator that produces "instant generative references" from the current diffusion latent conditioned on a compact LQ representation, (2) a **Latent Aggregator** that fuses these previews with the original LQ input to preserve fidelity, and (3) an **adaptive sampling algorithm (AdaRes)** that uses the variance of previews as a signal of input quality to modulate conditioning. The method is built on SDXL and achieves state-of-the-art scores on non-reference perceptual metrics (MANIQA, MUSIQ) across all tested settings, while enabling controllable restoration via text prompts.

## Strengths

- **Novel preview-based dynamic conditioning.** The Previewer mechanism — generating on-the-fly restoration references from the generative prior and using them to iteratively refine the generation condition — is a genuinely novel approach to handling unknown degradation in BIR (Sec. 3.2). The ablation (Table 5b) confirms that removing generative references causes a sharp drop in perceptual metrics (MUSIQ from 64.86 to 42.64), and the ControlNet-style variant ("+Noisy Previews") degrades substantially (MUSIQ 49.23 vs. 66.35), validating that the preview mechanism itself is critical, not just a technical artifact.

- **Consistent state-of-the-art non-reference perceptual quality.** Across all four test settings (Table 1, Scenarios 1 & 2, synthetic and real-world), InstantIR achieves the highest MANIQA and MUSIQ scores, with gains of up to 22% in MANIQA and 8% in MUSIQ over the second-best method. On real-world data at 512², InstantIR scores MANIQA 0.4819 vs. the next best (CoSeR) at 0.3941, and MUSIQ 65.32 vs. 60.51 — substantial margins.

- **Insightful analysis of preview trajectory as a quality indicator.** Figure 3 provides empirical evidence that the L2-distance between previews and denoising means increases monotonically with input quality across four degradation levels. The temporal normalization (Eq. 5) that removes time-step correlation is principled, and this observation is the foundation for the adaptive sampling algorithm.

- **Advantage over ControlNet-style conditioning clearly demonstrated.** The ablation in Table 5a ("+Noisy Previews") shows that simply injecting fresh noise (which makes the pipeline resemble ControlNet) leads to dramatic degradation in perceptual metrics (MUSIQ drops from 66.35 to 49.23), confirming that the previewing mechanism is doing something fundamentally different and more effective.

- **Controllable restoration via text prompts as a bonus capability.** The paper demonstrates (Fig. 5, 6) that InstantIR can perform semantic editing during restoration by toggling the Aggregator at later stages, adding creative restoration as an orthogonal capability beyond standard BIR.

## Weaknesses

### Fatal
None.

### Major

- **Large fidelity gap with insufficient explanation relative to the "reducing hallucinations" claim.** InstantIR's PSNR/SSIM are substantially worse than all baselines — e.g., on real-world 512², PSNR is 21.75 vs. Real-ESRGAN's 27.29 (a 5.5 dB gap), and SSIM is 0.6766 vs. 0.7894. The paper's sole defense is a single sentence citing the well-known PSNR/SSIM-vs-perceptual tradeoff (citing SUPIR and StableSR). However, those cited methods have *much smaller* fidelity gaps than InstantIR, so the analogy is weak. The paper explicitly claims its method "reduc[es] hallucinations" (Sec. 4.3), yet provides no controlled fidelity analysis — no hallucination measurement, no faithfulness metric (e.g., DISTS, correspondence score), and no user study. A method that claims to reduce hallucinations must provide evidence that its outputs are more faithful to the input than competitors', not just that they look better to automated perceptual metrics. Without this evidence, the core motivation is not well supported.

- **The adaptive sampling algorithm (AdaRes) shows near-negligible benefits in the ablation.** Table 5b shows that adding AdaRes on top of generative references yields improvements of CLIPIQA +0.0011, MANIQA +0.0019, MUSIQ +0.08 — all well within metric noise. While AdaRes is conceptually interesting, the paper does not demonstrate that it meaningfully improves results. The hyperparameter η (the step threshold at which δ is set to 0) is never specified or ablated. The algorithm's behavior is validated on only four degradation levels (Fig. 3) without statistical characterization (variance across images, sensitivity to degradation type).

### Minor

- **Evaluation confound in Scenario 2 (1024² setting).** The paper follows SUPIR's protocol: 512-models receive a 512² crop while InstantIR (a 1024-model) sees the full 1024² image. This gives InstantIR substantially more context, which can inflate perceptual metrics. Scenario 1 partially offsets this (InstantIR is tested at off-distribution 512²), but the confound in Scenario 2 is not acknowledged or controlled for.

- **No user study.** For a method that explicitly trades pixel fidelity for perceptual quality, human evaluation is essential to establish that the trade-off is justified. The paper relies entirely on automated non-reference metrics (CLIPIQA, MANIQA, MUSIQ), which have well-documented biases (e.g., favoring smooth, saturated outputs).

- **Inference cost not reported.** The Previewer requires an additional forward pass per DDIM step (30 steps × 1 extra UNet pass). The paper reports training cost (9 days on 8×H800) but provides no inference-time comparison to baselines (e.g., StableSR, CoSeR, SUPIR), making it difficult to assess practical applicability.

- **The Previewer is trained only on JourneyDB (synthetic data).** While the Aggregator is later trained on diverse texture-rich datasets, the Previewer — which generates the critical references — is distilled only on JourneyDB. The paper provides no analysis of how Previewer quality varies across different input domains (e.g., natural vs. synthetic scenes).

- **DCP text-domain training comparison is qualitative only.** The comparison of DCP trained with vs. without text descriptions (Fig. 5, line 309) is shown only via visual examples with no quantitative evaluation. The paper acknowledges this is due to computational constraints, but it limits the strength of the claimed advantage.

### Trivial
- The ablation table labels are somewhat confusing: "Baseline" in Table 5a appears to be the full method (with Previewer + consistency distillation), while "+Distillation" actually removes the Previewer and uses DDIM denoising predictions instead — this naming is counterintuitive and should be clarified.

## Nice-to-Haves
- **Direct hallucination/fidelity measurement.** A controlled experiment with synthetic degradations and known ground truth, measuring faithfulness (e.g., DISTS, identity preservation score, or semantic correspondence) would directly support the paper's claims about reduced hallucinations.
- **User study** comparing InstantIR's outputs with those of top baselines in terms of both perceptual quality and faithfulness to the input.
- **Failure case analysis** showing examples where InstantIR produces incorrect content, to clarify the limitations of the approach.
- **Ablation of η** and more thorough validation of δ across diverse degradation types with variance bars.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that "the method is essentially replacing content, not restoring it."** This is a speculative interpretation not directly supported by evidence. The qualitative results show plausible outputs that correspond to input content (e.g., four faces recovered in Fig. 4). Removed as unsupported speculation.

- **Criticism that "the paper attributes hallucinations to encoding errors but proposes a method that actually adds generative content rather than correcting encoding."** The paper explicitly proposes to "refine the LQ encodings with generative references" (line 46) — the preview is fused with the LQ input via the Aggregator, which anchors it to the original. The characterization as "adding content rather than correcting" misrepresents the architecture. Removed as a strawman.

- **Criticism that "the Aggregator borrows heavily from prior work without sufficient novelty discussion."** The paper explicitly cites ControlNet (Zhang et al., 2023) as the initialization source and describes its adaptations (removing text cross-attention, SFT fusion). Borrowing architectural components from prior work with clear attribution is standard practice. Removed as a subjective and non-substantive critique.

- **Criticism about "The Previewer's training data (only JourneyDB, synthetic high-quality) raises generalization concerns."** The paper explains that Stage-2 Aggregator training incorporates diverse texture-rich datasets (DIV2K, LSDIR, Flickr2K, FFHQ), partially addressing this concern. Removed as the paper already takes reasonable steps to mitigate this.

## Novel Insights

The most interesting observation that emerges across the reviews is the tension between the paper's motivation and its evidence: InstantIR achieves clearly superior non-reference perceptual metrics, but the fidelity gap (measured by PSNR/SSIM) is substantially larger than other generative BIR methods, while the paper simultaneously claims to "reduce hallucinations." This suggests that the preview-based dynamic conditioning may be optimizing for *perceptual plausibility* (smooth, detailed outputs that score well on automated metrics) rather than *restoration faithfulness* — a distinction that deserves sharper acknowledgment and separate measurement. A second insight is that the adaptive algorithm (AdaRes), while theoretically elegant, contributes vanishingly small empirical gains, raising the question of whether the complexity of the adaptive mechanism is justified, or whether the core contribution is simply the preview-based conditioning itself.

## Suggestions

1. **Add a direct hallucination/faithfulness evaluation.** Use synthetic degradations with known ground truth and report a metric like DISTS, LPIPS, or identity preservation score alongside PSNR/SSIM. Show that InstantIR's outputs are *more* faithful than competitors' under mild degradation, and characterize how faithfulness degrades under severe degradation.
2. **Conduct a user study** comparing InstantIR against CoSeR, StableSR, and SUPIR for both perceptual quality and perceived faithfulness to the input.
3. **Either strengthen the validation of AdaRes** (more degradation levels, variance bars, η ablation, showing statistically significant improvements) or temper the claim about the adaptive algorithm being a key contribution.
4. **Acknowledge the Scenario 2 context confound explicitly** and provide a supplementary experiment where InstantIR is also restricted to 512² crops.
5. **Report inference time and memory** compared to baselines.

## Score and Decision

**Originality:** High. The preview-based dynamic conditioning is a genuinely new approach in BIR.  
**Importance of research question:** High. Handling unknown degradation is a central challenge in BIR.  
**Claims well supported:** Moderate. SOTA non-reference metrics are well supported, but the large PSNR gap and lack of hallucination measurement weaken the core "reducing hallucinations" claim.  
**Soundness of experiments:** Moderate. Ablations partially validate the design, but AdaRes shows negligible benefits, and there is a confound in the high-resolution evaluation.  
**Clarity of writing:** Good. The architecture is clearly described and the pipeline is easy to follow.  
**Value to the research community:** Moderate to High. The preview mechanism is likely to inspire follow-up work.

The paper introduces a genuinely novel approach with convincing perceptual quality improvements. The weaknesses — particularly the large fidelity gap relative to the hallucination-reduction claim, the marginal AdaRes improvement, and the lack of a user study — are real but not fatal. With targeted additional analysis, the contributions would be stronger, but the core ideas are already a meaningful step forward for the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>