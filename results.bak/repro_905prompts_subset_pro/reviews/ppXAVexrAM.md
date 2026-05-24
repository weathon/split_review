## Summary

This paper introduces ARSS, the first framework to apply a GPT-style decoder-only causal autoregressive transformer to novel view synthesis from a single image conditioned on a camera trajectory. The method uses a video tokenizer for temporal consistency, a camera autoencoder to convert Plücker raymaps into 3D positional guidance tokens, and a hybrid spatial permutation strategy that shuffles within-frame token orders while preserving inter-frame temporal causality. Results on RealEstate10K, ACID, and zero-shot DL3DV show competitive performance with state-of-the-art diffusion-based methods, particularly in perceptual metrics (LPIPS) and error accumulation over long trajectories.

## Strengths

- **Genuine novelty as the first causal AR model for camera-controlled NVS.** Applying a decoder-only autoregressive transformer with next-token prediction to multi-view synthesis from a single image is a novel architectural contribution that has not been explored before. The paper clearly differentiates its approach from diffusion-based methods that generate all views jointly (Section 1, Section 3.2).

- **Well-motivated hybrid token permutation with strong ablation evidence.** The strategy of permuting spatial token order within each frame while preserving temporal order across frames (Eq. 6) directly addresses the mismatch between uni-directional transformers and bi-directional image data. Table 2 and Figure 7 provide clear evidence: raster order degrades to 16.29 PSNR and full spatial-temporal permutation produces incorrect early-frame geometry, while the proposed hybrid approach achieves 19.22 PSNR with stable quality across frames.

- **Video tokenizer validated as crucial for temporal consistency.** Table 3 shows that replacing the video tokenizer with per-frame VQ tokenization causes FVD to jump from 52.56 to 137.68 (a 62% degradation) and drops PSNR by ~3.5 dB, convincingly demonstrating that temporal compression is essential for multi-view coherence.

- **Competitive perceptual quality and strong error-accumulation behavior.** The method achieves the best LPIPS across all three datasets (0.269, 0.265, 0.347 on Re10K, ACID, DL3DV respectively). Figure 6 shows ARSS maintains the slowest quality degradation over long trajectories compared to all baselines, with flatter PSNR/SSIM/LPIPS curves — a meaningful finding for long-horizon view synthesis.

- **Zero-shot generalization demonstrated.** Results on the DL3DV benchmark (Table 1) and on synthetically styled images (Figure 5) show that ARSS transfers beyond its training distribution without fine-tuning.

## Weaknesses

### Major

- **Overstated performance claims relative to SEVA.** The introduction (line 114) and discussion (line 490) claim the method "out-performs current state-of-the-art methods," but Table 1 tells a more nuanced story: on RealEstate10K, ARSS achieves better PSNR (19.02 vs. 18.73) and LPIPS (0.269 vs. 0.349), but *worse* SSIM (0.624 vs. 0.670) and *worse* FID (47.60 vs. 46.98). On ACID, FID is substantially worse (47.76 vs. 33.16). The paper briefly acknowledges "minor geometric inconsistencies" in Section 4.2 but then reverts to claiming outright superiority. The evidence supports a conclusion of *complementary strengths* (ARSS better for perceptual quality, SEVA better for structural fidelity), not one model outperforming the other. This overclaim undermines credibility.

- **Missing ablation of the camera autoencoder — a central design component.** The camera autoencoder (Section 3.2.2) is presented as a key innovation, producing "3D positional guidance tokens" that are interleaved with every visual token. Yet there is no experiment that isolates its contribution: no run that removes camera tokens, replaces them with raw Plücker coordinates, or substitutes a learned null embedding. Without this ablation, readers cannot judge whether the camera autoencoder actually provides useful 3D structure or whether the transformer learns to ignore it. This is a significant evidential gap for what the paper positions as a core component.

- **The claimed advantage of autoregressive generation over diffusion is not empirically demonstrated.** The paper motivates AR by arguing that diffusion methods "generate target views jointly" and are "less straightforward" for causal extension (Section 1). However, no experiment demonstrates a practical benefit unique to the AR formulation — e.g., extending a generated trajectory by 5 frames without recomputing the first 5, or leveraging KV-caching during incremental generation. The error-accumulation analysis (Figure 6) shows slower degradation, but this does not directly validate the claimed causal-incremental advantage over, say, a sequential diffusion model that conditions on previous frames. The central motivation remains a theoretical claim.

### Minor

- **Camera autoencoder architecture is insufficiently specified for reproducibility.** Section 3.2.2 describes the encoder as "stacked 3D convolutional and downsampling blocks" and the decoder as "symmetric 3D convolutional and upsampling blocks," but gives no concrete numbers for layers, channels, strides, or latent dimensionality. Equation 7 also appears incomplete in the manuscript text. These omissions make the method difficult to reproduce.

- **Ablation tables do not specify the evaluation dataset or split.** Tables 2 and 3 report PSNR/SSIM/LPIPS/FID/FVD for permutation and tokenizer ablations, but nowhere state which dataset or split these numbers are computed on. Without this information, the ablation results are not fully interpretable.

### Trivial

- The abstract says "achieves overall comparable to state-of-the-art" while the introduction says "out-performs current state-of-the-art methods" — internal inconsistency in the paper's own framing.

## Nice-to-Haves

- A direct experiment demonstrating the practical benefit of AR generation over diffusion — e.g., extending a trajectory mid-generation without full recomputation — would strongly strengthen the paper's motivation and contribution.
- Reporting standard deviations or confidence intervals for the main metrics in Table 1 would help readers assess whether the small PSNR margin over SEVA is meaningful.
- Discussing the inference cost and sequence-length overhead introduced by interleaving camera tokens with every visual token would provide useful practical context.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Causal diffusion variants exist" / missing related work discussion** — Removed per rules: I cannot verify the existence or relevance of specific missing related works. The paper cites relevant diffusion-based NVS methods (SEVA, Genwarp, MotionCtrl, ViewCrafter, LVSM, RayZer) and autoregressive visual generation works.
- **"Weak baselines inflate comparative strength"** — The paper includes SEVA and LVSM, the strongest relevant baselines in the field. Including additional weaker baselines (MotionCtrl, Genwarp) is standard practice and does not distort the comparison since SEVA is present.
- **"Equation 7 appears incomplete in the parsed text"** — This is likely a parser artifact and not an author error; the original submission is assumed to be correct. The architectural underspecification concern (Minor weakness above) is retained on its own merits.
- **"Sequence-length overhead from camera tokens not discussed"** — This is a nice-to-have, not a weakness. The paper provides implementation details (17 frames → 5×32×32 latent codes, line 344) and does not hide the token counts.

## Novel Insights

The error-accumulation analysis (Figure 6) reveals an interesting property: the hybrid spatial-only permutation strategy appears to produce not just better absolute quality but *qualitatively different* degradation behavior — ARSS maintains nearly flat quality curves across 16 frames while all baselines show monotonic decline. This suggests the causal autoregressive formulation with shuffled spatial tokens may confer a form of temporal robustness that goes beyond what per-frame metrics capture, and is worth further investigation as a property of AR vs. diffusion generation for sequential visual tasks.

## Suggestions

- Add the camera autoencoder ablation: train a variant without camera tokens (relying only on shuffled visual tokens + learned positional embeddings) and report the performance drop. This directly tests whether the 3D guidance mechanism is doing real work.
- Either demonstrate the unique AR advantage empirically (trajectory extension experiment) or soften the motivation to focus on what is actually shown: that AR models can achieve competitive NVS quality with the benefit of a simpler, next-token-prediction formulation.
- Tone down the "out-performs" language in the introduction and discussion to accurately reflect the trade-off with SEVA. The paper is strong enough without overclaiming.
- Specify the dataset and split used for Tables 2 and 3.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
- CCM-DiT (`15lk4nBXYb`): 3.00 — camera-controlled video generation; clearly weaker than ARSS in both novelty and evaluation breadth.
- GeoGS3D (`I86z54CL2y`): 3.40 — single-view 3D reconstruction; weaker contribution.
- ARVideo (`hWlCc7Iksi`): 3.40 — autoregressive video pretraining; different task, weaker evaluation.
- AR-1-to-3 (`pOcGFvfgjS`): 5.00 — autoregressive multi-view generation but object-only, synthetic data only, limited evaluation. ARSS is clearly stronger (real-scene data, zero-shot, better ablations).
- GST / "Where Am I" (`NuHYh4YKNe`): 6.25 — accepted, novel AR model for spatial localization + view prediction. Comparable novelty to ARSS but with somewhat cleaner evaluation. ARSS is slightly weaker due to missing camera ablation and overclaim.
- LVSM (`QQBPWtvtcn`): 7.67 — well-executed transformer NVS model with thorough experiments. ARSS does not reach this level of evaluation completeness.

**Round 1 bracket: 5.0–7.0.**

**Round 2 (narrowing):**
- BSQ-ViT (`yGnsH3gQ6U`): 5.75 — accepted, novel quantization method for tokenization; has some missing comparisons/ablations like ARSS. ARSS is roughly comparable in quality.
- Pseudo-Generalized DVS (`QuVlUn4T2G`): 6.75 — accepted, first method in its setting but result quality is low; thorough analysis compensates. ARSS has better result quality but less thorough methodological validation.

**Final placement:** ARSS sits between BSQ-ViT (5.75) and GST (6.25), closer to BSQ-ViT. The missing camera autoencoder ablation, overclaimed performance, and unvalidated AR motivation pull the score below GST. The genuine novelty, three-dataset evaluation, strong ablations on permutation and tokenization, and zero-shot generalization keep it above AR-1-to-3. **Score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>