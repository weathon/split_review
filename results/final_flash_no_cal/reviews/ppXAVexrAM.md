Now I have all the information needed to write a thorough consolidated review. Let me produce the final output.

## Summary

This paper introduces ARSS, a decoder-only autoregressive transformer framework for novel view synthesis (NVS) from a single image given a camera trajectory. It employs a video tokenizer (VidTok with FSQ) for temporally consistent tokenization, a camera autoencoder that compresses Plücker raymaps into discrete 3D positional tokens, and a hybrid permutation strategy that randomly shuffles spatial token order while preserving temporal causality. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based baselines. The core novelty is demonstrating that GPT-style causal AR models can perform NVS with camera control — a task previously dominated by diffusion models.

## Strengths

- **First decoder-only AR framework for NVS with camera control.** The paper introduces a GPT-style causal AR model to novel view synthesis, a direction dominated by diffusion models. This is a genuine conceptual contribution, and the system demonstrably works: ARSS achieves competitive or superior metrics against diffusion baselines on several benchmarks (e.g., 19.02 PSNR on RealEstate10K vs. 18.73 for SEVA; best scores on all reported metrics for zero-shot DL3DV). The claim is backed by both quantitative (Table 1) and qualitative (Figures 3–5) evidence.

- **The hybrid token-order permutation strategy is well-motivated and effectively ablated.** Randomly permuting tokens spatially while preserving temporal order adapts the causal transformer's uni-directional attention to the bi-directional nature of visual data. The ablation (Table 2) cleanly demonstrates the advantage over both raster ordering (19.22 vs. 16.29 PSNR) and full spatiotemporal permutation (19.22 vs. 18.76 PSNR), with corresponding visual improvements shown in Figure 7.

- **Video tokenizer substantially improves temporal consistency.** Ablation (Table 3) compares per-frame VQ image tokenization against the FSQ-based video tokenizer (VidTok). The video tokenizer yields a ~62% improvement in FVD (52.56 vs. 137.68) and large gains across all metrics, convincingly validating its role in maintaining temporal coherence across the generated sequence.

- **Strong zero-shot generalization.** On the DL3DV benchmark, which is unseen during training, ARSS achieves the best scores among all compared methods (16.70 PSNR, 0.449 SSIM, 0.347 LPIPS, 84.96 FID, 91.25 FVD). Qualitative results on AI-generated out-of-distribution images (Figure 5) further demonstrate broad domain transferability.

## Weaknesses

### Fatal

None.

### Major

- **Core motivation (causal AR advantages) is not directly tested against the strongest competitor.** The paper motivates AR models by arguing that causal structure enables slower error accumulation, incremental trajectory extension, and online generation. However:
  (1) The error accumulation analysis (Figure 6) omits SEVA — the strongest diffusion baseline that the paper directly competes with. Without SEVA in this comparison, the claim that ARSS degrades slower is unsubstantiated against the most relevant competitor.
  (2) No experiment tests sequences longer than the training length, path extension after partial generation, or conditioning on previously generated views for trajectory modification.
  The paper demonstrates that an AR model *can* do NVS, but does not experimentally validate the stated *advantages* of the AR approach over diffusion alternatives. This weakens the core narrative from "AR is better for NVS because X" to "AR can also do NVS."

- **Camera encoder is not ablated against simpler alternatives.** The camera autoencoder is presented as a central contribution for providing per-token 3D positional guidance. Yet no ablation compares it against simpler alternatives such as 2D spatial positional embeddings within the latent grid, a single global camera embedding prepended to the sequence, or removal of camera tokens entirely. Without this, the reader cannot attribute any performance gain to the specific camera encoder design. Additionally, the weighting coefficients λ₁–λ₄ in the camera loss (Eq. 5) are not specified, leaving the training objective underspecified.

### Minor

- **Performance claims are somewhat overstated.** The abstract states the method is "overall comparable," while the introduction and conclusion claim it "out-performs current state-of-the-art methods." The quantitative results are genuinely mixed: ARSS leads on PSNR and LPIPS across datasets, but SEVA leads on SSIM (0.670 vs. 0.624 on Re10K) and FID (46.98 vs. 47.60 on Re10K, 33.16 vs. 47.76 on ACID). The paper acknowledges these trade-offs in the quantitative results section but still uses "outperforms" in the introduction and conclusion, creating a mismatch.

- **Discrepancy between Table 1 and Table 2.** Table 1 reports "Ours" PSNR = 19.02 on RealEstate10K, while the ablation study (Table 2) reports "Ours" PSNR = 19.22. This 0.2 dB gap is non-negligible and likely stems from different subsets or seeds. The paper should explain this discrepancy.

- **Tokenization ablation conflates two factors.** The VQ baseline (Table 3) uses a per-frame image tokenizer with VQ, while the "ours" condition uses a video tokenizer with FSQ. This conflates quantization method (VQ vs. FSQ) and tokenization domain (image vs. video). A cleaner ablation would isolate whether the improvement comes from the video-level modeling or the quantization strategy. The conclusion (video tokenizer improves temporal consistency) is still supported by the large FVD gap, but the confound should be noted.

- **Eq. 7 notation is incomplete/unclear.** The training objective is written as `L = CE(f_θ([S, [x21^{P2(1)}, ..., xln^{Pl(n)}]]))` with only one argument to the cross-entropy loss, unlike Eq. 3 which provides both input and target. The intended targets need to be made explicit. Additionally, the notation does not clarify whether the permutation P_i(j) is resampled each training iteration or drawn from a fixed set.

- **Metric computation details for FID/FVD are underspecified.** The paper reports FID and FVD on 17-frame sequences but does not specify whether these are computed per generated sequence, over concatenated frames, or using specific temporal windows.

- **ViewCrafter and RayZer baselines show very low PSNR (~12–13 on Re10K).** These scores are far below all other methods, suggesting these methods may be operating outside their intended use case (e.g., designed for multi-view input rather than single-image input). While this does not undermine ARSS's performance against stronger baselines (SEVA, LVSM), it inflates the relative comparison. The paper should clarify whether these baselines were properly adapted to the single-image setting or consider excluding them.

### Trivial

None.

## Nice-to-Haves

- Include SEVA in the error accumulation analysis (Figure 6) to directly validate the claimed slower degradation of AR models against the strongest diffusion competitor.
- Test the causal advantage directly: generate sequences longer than the training length (e.g., 32 frames) or demonstrate incremental trajectory extension without retraining.
- Report model parameter count, inference wall-clock time per frame, and parallel decoding efficiency — the paper mentions parallel decoding as a benefit but provides no speed measurements.
- Provide a quantitative evaluation of camera autoencoder reconstruction quality (e.g., ray direction error) to assess whether camera tokens preserve accurate geometry.
- Add a failure case analysis identifying which types of view changes (large rotations, disocclusions) cause degradation.
- Clarify the performance narrative in the introduction and conclusion to match the nuanced picture presented in Section 4.2.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"L2SM" typo in Figure 6** — The harsh critic flags "L2SM" as a typo for "LVSM." Removed per formatting/typo rule (parser artifact or minor typo; does not affect the paper's technical content).

2. **Clarification needed about prior AR video models (TATS, VideoPoet)** — The harsh critic suggests the paper should clarify differences from these models. Removed per "missing related works" rule: the paper's related works section already distinguishes prior AR work by noting "none of the methods focus on video or multi-view sequence generation." The external reference to specific models not cited by the paper cannot be verified.

3. **Generic "cannot be independently verified" framing** — Removed per rule prohibiting reproducibility concerns based on doubting that cited entities exist.

## Novel Insights

The most interesting observation from the reviews is that the paper's conceptual contribution (applying causal AR to NVS) and strongest experimental evidence (token-order permutation ablation, zero-shot generalization) are somewhat disconnected from the paper's motivational framing. The permutation ablation cleanly shows *how* to make AR generation work for multi-view data, but the paper's core claim about why AR models are *inherently better* for this task remains experimentally unvalidated. This suggests the paper would be more accurately framed as "an effective AR framework for NVS" rather than "AR is superior for NVS because of causal structure." The zero-shot results on DL3DV, where ARSS outperforms all baselines despite being trained from scratch on smaller datasets, are perhaps the paper's most compelling empirical contribution — they argue for the approach's practical value regardless of the theoretical causal advantages.

## Suggestions

1. **Tone down the "outperforms" claim** in the introduction and conclusion to match the mixed quantitative reality. Frame the contribution as "a competitive AR-based framework" rather than claiming superiority across all metrics.
2. **Add an ablation of the camera encoder** comparing it against: (a) no camera conditioning, (b) a single global camera embedding, and (c) 2D spatial positional embeddings without 3D information. This is the highest-leverage missing experiment.
3. **Include SEVA in the error accumulation analysis** in Figure 6. Also consider a simple experiment generating longer sequences than the training horizon and measuring degradation.
4. **Explain the Table 1 vs. Table 2 PSNR discrepancy** (19.02 vs. 19.22). Note whether different subsets, seeds, or evaluation protocols cause the gap.
5. **Fix Eq. 7** to clearly separate model input and prediction targets, and specify whether permutations are resampled per iteration.
6. **Specify the λ₁–λ₄ values** used in the camera loss (Eq. 5).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>