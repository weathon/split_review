Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me write the consolidated review.

## Summary

This paper introduces InstantIR, a blind image restoration method built on SDXL that dynamically refines generation conditions during the reverse diffusion process. Its core innovation is a "preview-then-aggregate" mechanism: a distilled Previewer decodes the current diffusion latent into a restoration reference on-the-fly, which is then fused with the original LQ encoding by an Aggregator to guide the next diffusion step. The paper additionally proposes an adaptive sampling algorithm (AdaRes) that uses the relative distance between preview and denoising prediction as an indicator of input quality, and demonstrates text-guided creative restoration. The method achieves state-of-the-art MANIQA and MUSIQ scores across multiple benchmarks.

## Strengths

1. **Novel previewing mechanism for iterative condition refinement.** The idea of decoding a restoration preview from the current diffusion latent at each step and using it to re-condition the next step is genuinely novel. Unlike prior works that condition once at the beginning (e.g., ControlNet-style), InstantIR actively realigns with the generative prior throughout the reverse process. This is well-motivated in the paper (Section 3) and supported by qualitative results showing reduced hallucinations — e.g., in Figure 4, InstantIR is the only method that correctly recovers four faces without distortion and avoids the semantic blending seen in SUPIR.

2. **State-of-the-art on non-reference perceptual metrics across all settings.** In Table 1, InstantIR achieves the highest MANIQA and MUSIQ scores in every evaluated configuration — often by substantial margins (e.g., MANIQA 0.4379 vs. next best 0.4152 in Scenario 1 synthetic; 0.4819 vs. 0.3941 on real-world data in the same scenario). This provides credible evidence for the paper's claim of outstanding perceptual quality.

3. **Reasonably thorough ablation isolating component contributions.** Tables 3a and 3b separate the effects of consistency distillation, fresh noise injection, generative references, and AdaRes. The ablation in Table 3b cleanly shows that adding generative references dramatically improves non-reference metrics (MANIQA from 0.2128→0.3747, MUSIQ from 42.64→64.86), supporting the core claim that the previewing mechanism is beneficial.

## Weaknesses

### Fatal
None.

### Major

1. **The PSNR/SSIM gap is large and insufficiently justified.** InstantIR consistently produces the lowest PSNR and near-lowest SSIM among all competitors — e.g., PSNR 21.75 vs. 27.29 (Real-ESRGAN) on real-world data in Scenario 1, a 5.5 dB gap. While the paper briefly notes the "misalignment of PSNR and SSIM scores with visual quality" and the conclusion acknowledges that "excessive generative prior diminishes fidelity," this is not accompanied by any evidence that the perceptual gains justify the fidelity loss. A user study comparing InstantIR outputs against the closest competitor on real-world images is needed to establish that the trade-off is worthwhile. Without it, a skeptical reader can reasonably suspect the method generates attractive but inaccurate images — a known failure mode of heavily generative priors.

2. **The ablation in Table 3a presents an unexplained contradiction.** The "Baseline" (without consistency distillation) achieves strong non-reference metrics (CLIPIQA 0.5433, MANIQA 0.4024, MUSIQ 66.35), while "+Distillation" collapses them (CLIPIQA 0.2453, MANIQA 0.2145, MUSIQ 38.33). The paper states this validates "the necessity of consistency constraints," but the data shows the opposite on the paper's own preferred metrics — the distilled Previewer makes perceptual quality *worse* in this ablation. The paper offers no explanation for this discrepancy, nor for why the full system (which uses distillation) nevertheless achieves SOTA. This may be an artifact of the ablation setup (e.g., the Aggregator being trained for the distilled Previewer but tested without it, or the "Baseline" using a different reference source), but the paper does not clarify. Readers and the text itself (line 313) appear to have a cross-reference error (citing Tab. 3b instead of 3a), suggesting confusion about what is being compared.

3. **The mechanism by which δ modulates generation is architecturally underspecified.** Algorithm 1 passes δ as an argument to the noise predictor ϵ_θ, but the architecture section (Section 3.2) describes only the Aggregator's SFT fusion and residual connections — no mechanism for how a time-varying scalar δ amplifies or suppresses the Aggregator's conditional signals. The paper states that "conditional signals from the Aggregator should be amplified" for high δ, but does not specify where or how this modulation occurs in the network. Without this detail, the claimed contribution of "adaptive restoration" is not concretely grounded, and the algorithm is not reproducible.

### Minor

1. **AdaRes provides only marginal quantitative benefit.** In Table 3b, adding AdaRes on top of generative references improves CLIPIQA from 0.5445→0.5456, MANIQA from 0.3747→0.3766, and MUSIQ from 64.86→64.94. These differences are within measurement noise. The paper should either demonstrate a meaningful effect on a relevant subset (e.g., stratified by degradation severity) or tone down the claim of adaptivity.

2. **The DINO vs. CLIP choice is asserted without evidence.** The paper states (Section 3.2) that DINO is preferred over CLIP because its self-supervised training "improves robustness of the encoded features," but provides no ablation comparing the two. Given the centrality of this encoding to the entire pipeline, the choice deserves empirical justification.

3. **Text-guided creative restoration is shown only qualitatively.** The paper claims as Contribution 3 the ability to enable "both adaptive and controllable restoration to text prompts," but provides no quantitative evaluation — not even a CLIP score or small user study — for this capability. The qualitative demonstrations in Figure 6b are interesting but insufficient to substantiate the contribution.

### Trivial

- The text at line 313 references "Tab.~\ref{ablation2}" but the discussion is about the consistency distillation ablation, which is Table 3a (labeled `ablation1`), not Table 3b (labeled `ablation2`). The second row of Table 3b does *not* show a drop, confirming the cross-reference is incorrect.

## Nice-to-Haves

- A user study comparing InstantIR against the closest perceptual competitor (e.g., CoSeR or SUPIR) on real-world images would substantially strengthen the paper by arbitrating the PSNR/perceptual metric conflict.
- An ablation comparing DINO vs. CLIP as the DCP encoder would justify the design choice.
- A quantitative evaluation of text-guided restoration (e.g., CLIP score or preference judgment) would substantiate Contribution 3.
- A description — even a single sentence — of how δ modulates the Aggregator's feature injection would resolve the architectural underspecification.

## Removed Points

- **"Only one image example per method"**: The paper shows multiple examples in Figure 4 (with several rows of comparisons). The reviewer's claim is inaccurate. Removed.
- **"Never reports total computational cost"**: The paper reports "9 days on 8 Nvidia H800 GPUs" (line 149), which is approximately 1728 GPU-hours. This is sufficient for a conference paper. Removed.
- **"Previewer architecture underspecified (student architecture, LoRA toggling)"**: The paper specifies LoRA on SDXL (line 147), consistency distillation with explicit loss (Eq. 8), and LoRA toggling ("By toggling the Previewer LoRA, we can seamlessly switch"). These details are adequate for the class of paper. Removed as overclaim.
- **Points that question existence/availability of cited models/datasets**: Removed per hard rules.
- **"Formatting/style nitpicks"**: Removed per hard rules.
- **Generic strengths from Strength Finder without specific evidence**: Removed (conflict with verified weaknesses noted below).

## Novel Insights

The most interesting pattern across the reviews is the tension between the paper's strong perceptual metric results and the contradictory ablation evidence. The Tab 3a finding — that adding consistency distillation to the Previewer collapses non-reference metrics despite the full system's success — is not adequately addressed and may point to an interaction effect between the Previewer and Aggregator that the two-stage training pipeline is designed to manage. The fact that the full system works but the isolated ablation doesn't suggests the Aggregator may be learning to compensate for the Previewer's deficiencies during Stage 2 training, rather than the Previewer producing genuinely better references. If true, this would weaken the paper's narrative about "informative generative references" but does not invalidate the overall approach — the pipeline as a whole demonstrably works. Clarifying this interaction would be the single highest-impact improvement for the paper.

## Suggestions

1. **Resolve the distillation contradiction.** Clearly explain what "Baseline" and "+Distillation" mean in Table 3a, and address why the non-distilled setup gives better perceptual metrics. If the difference is that only the full system's Aggregator is trained for the distilled Previewer, state this explicitly. If the baseline uses a different source of references (e.g., Eq. 7 denoising means), say so clearly.

2. **Specify how δ modulates the Aggregator.** Add one sentence or a diagram showing the architectural mechanism — e.g., a learned linear projection that scales the residual connections from the Aggregator — to make Algorithm 1 reproducible.

3. **Demonstrate when AdaRes matters.** Stratify the AdaRes results by degradation severity to show whether the adaptive mechanism provides meaningful gains on some subset, or acknowledge its effect is modest.

4. **Add a human evaluation.** A small-scale user preference study on real-world images comparing InstantIR against the closest competing method would resolve the credibility concern around the PSNR gap more effectively than additional metric analysis.

## Score and Decision

Given the paper's genuinely novel contribution (previewing mechanism for iterative condition refinement) and its SOTA results on perceptual metrics, but weighed against the unresolved ablation contradiction, the underspecified adaptive mechanism, and the large unarbitrated PSNR gap, the paper is borderline. The core idea is strong and the empirical results on perceptual metrics are credible, but the evaluation has significant gaps that prevent full confidence. The paper would benefit from major revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>