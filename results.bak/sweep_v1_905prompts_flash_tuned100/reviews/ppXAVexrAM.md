Now I have all the verified information. Let me write the final consolidated review.

## Summary

This paper introduces ARSS, a framework that applies GPT-style decoder-only autoregressive models to novel view synthesis (NVS) from a single image. The method comprises three components: (1) a video tokenizer (VidTok) for temporally consistent discrete tokenization of multi-view sequences, (2) a camera autoencoder that compresses Plücker ray maps into 3D positional tokens, and (3) an autoregressive transformer that performs next-token prediction with a hybrid token ordering strategy (random spatial permutation within each frame while preserving temporal causality). The approach is evaluated on RealEstate10K, ACID, and DL3DV, showing competitive results against diffusion-based NVS methods.

## Strengths

1. **Novel and timely direction.** This is, to the best of the paper's knowledge, the first application of a GPT-style decoder-only autoregressive model to novel view synthesis with camera control. The motivation — that causal AR models naturally support incremental generation along camera trajectories, unlike joint-denoising diffusion methods — is well-articulated and compelling.

2. **Hybrid token permutation ablation convincingly supports the design.** Table 2 shows that spatial-only permutation (proposed) substantially outperforms both raster-order (PSNR 19.22 vs. 16.29) and full spatio-temporal permutation (19.22 vs. 18.76) across all metrics. This directly validates that preserving temporal causality while allowing spatial permutation is key to the method's effectiveness.

3. **Video tokenization ablation quantifies its importance.** Table 3 shows that replacing the video tokenizer with a VQ image tokenizer degrades FVD from 52.56 to 137.68 (62% worse), cleanly demonstrating the need for temporally-aware tokenization for multi-view generation.

4. **Zero-shot generalization demonstrated on out-of-distribution inputs.** Figure 5 shows ARSS generating geometrically consistent novel views from AI-generated images (Betker et al., 2023) that differ substantially from the training distribution, providing evidence that the camera autoencoder generalizes.

5. **Error accumulation analysis shows a real advantage.** Figure 6 demonstrates that ARSS maintains flatter degradation curves across 17 frames compared to baselines, supporting the claim that the autoregressive design avoids rapid quality collapse on long trajectories.

## Weaknesses

### Major

1. **Overclaimed narrative relative to actual results.** The abstract accurately says "overall comparable," but the introduction (line ~114) claims the method "out-performs current state-of-the-art methods." Table 1 tells a mixed story: ARSS beats SEVA on PSNR and LPIPS but is worse on SSIM (Re10K: 0.624 vs. 0.670) and FID (Re10K: 47.60 vs. 46.98); on ACID, ARSS has markedly higher FID than SEVA (47.76 vs. 33.16). The paper's own Section 4.2 acknowledges this ("minor geometric inconsistencies") but the high-level framing is not calibrated to the evidence. The results are competitive, not clearly superior, and the claims should match that tone.

2. **Baseline comparison transparency is inadequate.** The paper reports ViewCrafter at PSNR 12.67 and RayZer at 12.97 on RealEstate10K — values well below even simpler baselines like MotionCtrl (16.17). No details are given about which official implementation/checkpoint was used, what inference hyperparameters were applied, what frame length or resolution was used, or whether any post-processing was performed. The paper must either (a) provide a complete configuration for every baseline (checkpoint ID, inference recipe, frame selection protocol) that explains these numbers, or (b) re-run comparisons under documented conditions. Without this, Table 1's quantitative comparisons cannot be fully trusted.

3. **Missing inference cost analysis.** A major advertised advantage of AR models over diffusion is single-forward-pass generation vs. iterative denoising. The paper does not report inference latency, total generation time per frame, or FLOPs, and does not compare against a diffusion baseline on these terms. This leaves a central motivation unquantified.

4. **Camera autoencoder details are insufficient for reproducibility.** The architecture is described as "stacked 3D convolutional and downsampling blocks" with no specifics on layer count, channel dimensions, training data, or whether the autoencoder is frozen or fine-tuned during AR transformer training. The loss weights λ1–λ4 in Eq. (5) are introduced but never specified. The camera autoencoder versus a simpler baseline (e.g., MLP on pose embeddings) is not ablated, so its contribution is unclear.

### Minor

5. **Figure 6 legend has an error.** The figure caption reads "L2SM" while the text and Table 1 consistently use "LVSM." This appears to be a drafting error. The dataset on which Figure 6 is evaluated is also not specified in the caption.

6. **No error bars or variance reporting.** Table 1 reports point estimates without standard deviations or confidence intervals. Given that several metrics are close between methods (e.g., PSNR 19.02 vs. 18.73 on Re10K), it is difficult to assess whether differences are significant.

7. **Geometric consistency is not directly evaluated.** For NVS, image-space metrics (PSNR/SSIM/LPIPS) do not explicitly penalize 3D geometric violations. Adding a simple geometric check (e.g., depth alignment or reprojection error) would strengthen the paper's claims about 3D consistency.

### Trivial

8. "Dimension is set to be 1280" (line ~344) — the paper should clarify whether this is the hidden dimension, number of layers, or a different architectural parameter, and provide the number of transformer layers and attention heads used.

## Nice-to-Haves

- An ablation replacing the camera autoencoder with a simple MLP on camera extrinsics/intrinsics would validate the Plücker-based design.
- Error accumulation analysis with a diffusion baseline that generates frames sequentially (rather than jointly like SEVA) would better isolate the causal advantage of the AR approach.
- Discussion of exposure bias (training with ground-truth tokens vs. inference with predicted tokens) and whether it manifests in ARSS would be useful context.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism that ViewCrafter/RayZer numbers are "not credible" based on claimed typical performance (PSNR 18-20).** The assertion depends on external knowledge about what these methods "typically achieve" that is not verifiable from the paper itself. However, the more general concern about inadequate baseline configuration reporting (point 2 in Major) is retained, as it is grounded in what the paper does and does not say on its own pages.

- **Missing related works (VideoGPT, TATS, Phenaki).** Cannot be independently verified as absent or relevant. Per guidelines, do not mention missing related works.

- **Claim that the paper "does not discuss known limitations of AR generation such as exposure bias."** The paper's Discussion section acknowledges tokenizer limitations and training-from-scratch constraints. The exposure bias point is a reasonable suggestion but not a core weakness.

- **Critique of table formatting (red/yellow highlighting).** Style nitpick; this is a presentation choice that does not affect scientific validity.

- **Criticism about SEVA exclusion on DL3DV being confusing.** The paper's footnote states the exclusion reason clearly. The criticism about the direction of the note is a misreading.

- **Request for "average over all frames with standard deviation."** This is subsumed by point 6 above (no error bars) which is retained as Minor.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reconcile the narrative with the evidence: replace all "outperforms" claims with "competitive with" or "comparable to," and explicitly discuss the metric trade-offs (stronger LPIPS, weaker SSIM/FID).
2. Provide a detailed baseline configuration table specifying for each method: official implementation source, checkpoint version, inference hyperparameters (sampling steps, guidance scale, etc.), frame selection protocol, and resolution.
3. Report inference latency and total generation time per frame, and compare against a diffusion baseline under matched settings.
4. Specify λ1–λ4 values, camera autoencoder architecture (layer counts, channel dimensions), and training data for the autoencoder.
5. Add an ablation replacing the camera autoencoder with a simple MLP on pose features.
6. Fix "L2SM" to "LVSM" in Figure 6 and add the dataset name to the caption.

## Score and Decision

### Calibration anchors

**Round 1 — Bracketing** (three queries on AR NVS topics):

| Anchor | Avg Score | Round | Comparison to ARSS |
|--------|-----------|-------|-------------------|
| I86z54CL2y (GeoGS3D) | 3.40 | R1 | Weaker — less complete, less relevant |
| pOcGFvfgjS (AR-1-to-3) | 5.00 | R1 | Most similar topic (AR for NVS), but uses diffusion-based AR with hand-crafted conditioning vs. clean GPT-style decoder-only. ARSS has stronger ablations and real-world benchmarks. |
| KI1zldOFz9 (CamTrol) | 5.80 | R1 | Different approach (training-free camera control), comparable acceptance rate |
| BWuBDdXVnH (ControlAR) | 6.25 | R1 | Stronger execution on a different task (controllable 2D generation), missing fewer details |
| NuHYh4YKNe (GST) | 6.25 | R1 | AR for spatial localization + view prediction, comparable scope but better-documented |
| QQBPWtvtcn (LVSM) | 7.67 | R1 | Much stronger — far more comprehensive experiments and analysis |

**Round 1 bracket:** 5.0 – 6.5

**Round 2 — Narrowing** (targeted queries in (4.5, 6.5) and (4.5, 6.0)):

| Anchor | Avg Score | Round | Comparison to ARSS |
|--------|-----------|-------|-------------------|
| pOcGFvfgjS (AR-1-to-3) | 5.00 | R2 | ARSS is stronger: cleaner architecture, real-world benchmarks, zero-shot evaluation, better ablations |
| KUz8QXAgFV | 5.50 | R2 | Different task (visual representation learning); similar score tier |
| b9dBNNeDd3 | 4.60 | R2 | Different task (set AR for image gen); weaker than ARSS |
| NuHYh4YKNe (GST) | 6.25 | R2 | ARSS is similar in scope but less polished (missing details, overclaims) |

**Final score determination:** ARSS is clearly stronger than AR-1-to-3 (5.0, rejected) — it tackles a harder problem with a cleaner approach and more thorough evaluation. However, it falls short of the quality bar set by ControlAR (6.25, accepted) and GST (6.25, accepted) due to overclaimed narrative, missing baseline reporting, absent inference cost analysis, and insufficient camera autoencoder documentation. I place it between these anchors.

**Score:** 5.5 — a borderline paper with a genuinely novel contribution and reasonable validation, but whose impact is diminished by uncalibrated claims and incomplete reporting that prevent a clear acceptance recommendation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>