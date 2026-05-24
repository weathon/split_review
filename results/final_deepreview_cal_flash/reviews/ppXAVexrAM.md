Now I have all the information I need. Let me compile the final review.

## Summary
The paper proposes ARSS, a decoder-only autoregressive transformer for novel view synthesis from a single image with camera control. It introduces three components: (1) a video tokenizer (VidTok with FSQ) to discretize multi-view sequences while preserving temporal consistency, (2) a camera autoencoder that compresses Plücker raymaps into latent tokens as 3D positional guidance, and (3) a hybrid token permutation that shuffles spatial tokens within each frame while maintaining temporal order. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based baselines.

## Strengths
- **First decoder-only AR model for NVS with camera control.** The paper demonstrates that a GPT-style causal next-token prediction paradigm can be adapted to novel view synthesis, a task previously dominated by diffusion models. The related work section (lines 118–122) confirms that prior AR visual generation methods focus on single-image generation, making this a legitimate architectural contribution.
- **Hybrid token permutation is well-motivated and ablated.** The design preserves temporal causality while permuting spatial tokens, and the ablation (Table 2, Figure 7) shows clear quantitative and qualitative advantages over both raster-order (16.29→19.22 PSNR) and full spatiotemporal permutation (18.76→19.22 PSNR). This provides strong evidence for the design choice.
- **Video tokenizer ablation is convincing.** Replacing the video tokenizer with a per-frame VQ image tokenizer degrades FVD by ~62% (52.56→137.68 in Table 3), confirming that temporal coding is critical for multi-view consistency.
- **Competitive or state-of-the-art results across multiple benchmarks.** On RealEstate10K, ARSS achieves the best PSNR (19.02), LPIPS (0.269), and FVD (50.51); on ACID it leads on PSNR (21.93) and LPIPS (0.265); on the zero-shot DL3DV benchmark it scores best across all five metrics (Table 1). The error accumulation analysis (Figure 6) further shows slower degradation over 16-frame trajectories.
- **Zero-shot generalization on out-of-distribution inputs.** Figure 5 shows that ARSS produces geometrically consistent novel views on AI-generated non-photorealistic images (oil paintings, cartoons), demonstrating generalizability beyond the training distribution.

## Weaknesses

### Major
- **Baseline evaluation protocol is not disclosed.** The paper reports quantitative numbers for MotionCtrl, ViewCrafter, RayZer, LVSM, and SEVA in Table 1, but never states how these numbers were obtained — whether from published papers, reproduced from official checkpoints on the same test split, or re-trained identically. This makes it impossible to judge whether the reported improvements reflect genuine method superiority or differences in evaluation protocol (resolution, sequence length, test split, metric computation). This is especially concerning because several baselines (ViewCrafter: 12.67 PSNR, RayZer: 12.97 PSNR) show much lower performance than expected, suggesting evaluation-condition mismatch. The paper must clarify the exact source of every baseline number and ideally demonstrate evaluation under identical conditions.
- **Central causal/extensibility claim is not tested.** The introduction motivates the autoregressive design by arguing that it can "incrementally extend and reuse existing generations when the trajectory changes" and "process observations in a sequential and causal manner." However, every experiment evaluates fixed-length, pre-determined sequences of 17 frames — exactly the training length. No experiment demonstrates generation beyond the training horizon, modified camera paths mid-generation, or any scenario that exploits the causal property. The error accumulation analysis (Figure 6) shows slower degradation over 17 steps, but this does not distinguish a causal advantage from other factors in the method. This is a substantive gap between the paper's framing and its evidence.
- **Factual error in quantitative reporting.** The text in Section 4.2 states that ARSS shows "minor geometric inconsistencies (e.g., -6.6% SSIM, +22% FID)" relative to SEVA. While the SSIM figure is approximately correct (0.624 vs 0.670 ≈ -6.9%), the FID comparison gives +1.3% on RealEstate10K (47.60 vs 46.98) and +44% on ACID (47.76 vs 33.16); no comparison supports +22%. The paper should either correct this figure or explain which comparison the +22% refers to.

### Minor
- **Camera autoencoder is not ablated.** The camera autoencoder is presented as a core contribution, but the ablation study (Section 4.3) only covers token permutation and tokenizer type. There is no comparison against simpler alternatives (e.g., encoding raw camera parameters as embeddings, using sinusoidal positional encodings of Plücker coordinates directly). Without this, it is unclear whether the dedicated autoencoder and its geometry-aware loss are beneficial or merely add complexity.
- **No statistical significance or variance reporting.** The paper reports point estimates without confidence intervals, error bars, or multi-seed runs for any metric. For generative tasks with inherent stochasticity (FID, FVD, LPIPS), this limits the reader's ability to assess result reliability.
- **Missing temporal-only shuffle ablation.** The ablation compares raster order, full spatiotemporal permutation, and the proposed spatial-only permutation. However, a temporal-only shuffle (preserving spatial order within each frame but shuffling frame order) is not tested, making it harder to isolate the effect of temporal causality from the spatiotemporal interaction.
- **Minor errors and inconsistencies.** (a) Figure 6 legend labels one baseline as "L2SM" rather than "LVSM." (b) The camera autoencoder loss description (line 233) has a typo: "d is the momentum term" should read "m is the momentum term." (c) FVD evaluation details (number of clips, frame stride, overlap) are not specified.

### Trivial
- The camera autoencoder training details (data, schedule, whether trained jointly with the transformer) are not provided.
- The y-axis ranges in Figure 6 are partially cropped, making it harder to gauge effect sizes.
- "L2SM" label in Figure 6 should be "LVSM."

## Nice-to-Haves
- A direct experiment testing the claimed causal advantage: generate sequences longer than 17 frames, or switch the camera path mid-generation and show that the model adapts coherently. This would substantially strengthen the paper's core thesis.
- Ablating the camera autoencoder against a simpler baseline (e.g., projecting camera parameters to the transformer dimension and adding them as per-token embeddings).
- Reporting error bars or at least results from multiple seeds for the main metrics.
- Testing on dynamic scenes (the introduction frames ARSS in the context of world models, which often involve dynamic environments).

## Removed Points
- **"ARSS claim of being 'first' is too broad"**: The paper qualifies this by noting prior AR work focuses on single-image generation and states "none of the methods focus on video or multi-view sequence generation." This is sufficiently scoped to the NVS task with camera control. Removed as the paper's claim is appropriately qualified.
- **"Missing related work on autoregressive video generation (VideoGPT, TATS, Phenaki)"**: These methods address unconditional or class-conditional video generation, not view synthesis with camera control. The paper's related work section is focused on the NVS task, and the omission is not a significant gap. Removed as out-of-scope.
- **"Generality: evaluation at 256×256 favors ARSS"**: The paper evaluates all methods (including baselines) at this resolution consistently. If there is a concern, it applies fairly across comparisons, and the paper explicitly states "All the images are in a resolution 256×256" in Implementation Details. Removed because the resolution is consistent across all methods.
- **"ViewCrafter and RayZer numbers seem suspicious"**: This is a concern about potential evaluation-condition mismatch, but the paper does not confirm or deny this. The core issue (baseline protocol transparency) is already merged into a single Major weakness above. The specific suspicion about individual baselines is not independently verifiable from the paper. Subsumed into the baseline transparency weakness.
- **"Camera autoencoder loss description uses 'd' for both ray direction and momentum"**: Verified as a typo ("d is the momentum term" should be "m"), but this belongs in Trivial, not a substantive weakness. Moved to Trivial.
- **"Comparison with autoregressive video baselines"**: As noted, such methods are not designed for NVS and comparing against them would not be informative. The paper includes LVSM (transformer-based) as a relevant non-diffusion baseline. Removed as not a meaningful missing comparison.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Clearly state in Table 1 or a footnote how each baseline's numbers were obtained (cited from the original paper, reproduced from official code, etc.). If reproduced, specify the exact split, resolution, frame count, and metric computation pipeline.
2. Remove or substantially soften the causal/extensibility claims in the introduction, or add an experiment that directly tests them (e.g., generating 30 frames with a model trained on 17, or altering the camera path mid-generation and evaluating coherence).
3. Correct the +22% FID figure in Section 4.2 to match the actual numbers in Table 1.
4. Add an ablation that removes or simplifies the camera autoencoder (e.g., replacing it with a learned embedding of the camera parameters) to validate its contribution.
5. Add error bars or multi-seed results for the main quantitative metrics.
6. Fix the "L2SM" → "LVSM" typo in Figure 6 and the "d" → "m" typo in Section 3.2.2.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:** Three calibration queries for papers topically similar to ARSS (NVS + autoregressive/generative methods):
- Weak band (<3.5): Three anchors avg 2.33–3.40 (papers rejected for fundamental flaws or being off-target).
- Middle band (3.5–7.5): Key anchors — *AR-1-to-3* (5.00, Reject), *Where Am I* (6.25, Accept), *ControlAR* (6.25, Accept), *Zero-shot NVS via Diffusion* (6.00, Accept).
- Strong band (>7.5): *LVSM* (7.67, Accept) — the actual LVSM paper that is a baseline in Table 1.

**Round 1 bracket:** 5.0–6.5.

**Round 2 — Narrowing:** Two targeted queries within the bracket:
- *3D-free meets 3D Priors* (5.00, Reject) — single-image NVS with weaker novelty and evaluation concerns.
- *ControlAR* (6.25, Accept) — controllable AR generation with thorough ablations and controlled experiments.
- *GTA* (6.25, Accept) — geometry-aware attention for NVS, strong evaluation.
- *CameraCtrl* (6.50, Accept) — camera control for video diffusion, well-executed.

**Comparison against anchors:** ARSS is clearly stronger than the 5.0 anchors (AR-1-to-3, 3D-free meets 3D priors) — it evaluates on more benchmarks, has more metrics, and provides ablation studies. It is weaker than the 6.0–6.5 anchors (ControlAR, Zero-shot NVS Diffusion, Where Am I) because those papers have more complete evaluation protocols, better-controlled comparisons, and fewer reporting gaps. The main issues preventing ARSS from reaching the 6.0+ level are the undisclosed baseline evaluation protocol, the untested central claim, and the factual error in the FID percentage. These are addressable but currently weaken the experimental argument.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>