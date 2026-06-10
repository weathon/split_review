Now I have all the calibration data I need. Let me write the final review.

## Summary
ARSS is the first GPT-style decoder-only autoregressive framework for camera-controlled novel view synthesis from a single image, combining a video tokenizer, a geometry-aware camera autoencoder with Plücker ray constraints, and a spatial-permutation strategy that preserves temporal causality. The paper evaluates on RealEstate10K, ACID, and zero-shot DL3DV benchmarks, achieving best PSNR on all three and best LPIPS on two.

## Strengths
- **Competitive quantitative results across three datasets (Table 1):** ARSS achieves the best PSNR on all three benchmarks (RealEstate10K: 19.02, ACID: 21.93, DL3DV: 16.70) and best LPIPS on RealEstate10K (0.269) and DL3DV (0.347). This establishes that autoregressive models can compete with state-of-the-art diffusion-based NVS methods.
- **Well-designed ablation validating spatial permutation (Tables 2–3, Figure 7):** The spatial-permutation/temporal-preservation strategy achieves 19.22 PSNR vs. 16.29 for raster order and 18.76 for full permutation. Figure 7 provides clear qualitative failure modes: raster ordering causes progressive distortion at later frames, while full permutation causes geometric errors from violating temporal causality. This is a clean, convincing demonstration.
- **First causal AR approach to camera-controlled NVS (Section 1, Figure 2):** The paper fills a genuine gap — prior AR visual generation focused only on single-image generation, while NVS methods relied on diffusion. The interleaved visual-camera token architecture with a geometry-aware camera autoencoder provides a principled way to inject 3D geometry into next-token prediction.
- **Significant improvement from video tokenization (Table 3):** Replacing VQ image tokenization with VidTok+FSQ improves FVD from 137.68 to 52.56 (~62%) and PSNR from 15.69 to 19.22, demonstrating that temporal-aware compression is critical for multi-view AR generation.

## Weaknesses

### Fatal
None.

### Major
- **Core causal-generation motivation is never experimentally validated.** The paper's primary motivation is that AR models "impose a strictly causal structure along a camera trajectory" and enable "incrementally extend[ing] and reus[ing] existing generations when the trajectory changes" (line 13). Yet no experiment tests incremental generation, trajectory extension, or reuse. The evaluation uses the same static-scene benchmarks as diffusion methods. Figure 6 (error accumulation per frame) is the closest, but it measures degradation along a fixed trajectory — a property of any sequential generation method (including causal diffusion with KV-caching), not a distinctive advantage of the AR architecture. This leaves the paper's most distinctive claim unsupported.
- **Mixed results against strongest baseline with overclaiming.** Against SEVA (the strongest competitor), ARSS wins on PSNR and LPIPS but loses on SSIM and FID. The FID gap on ACID is 47.76 vs. 33.16 — a 44% relative difference favoring SEVA. Yet line 88 claims "out-performs current state-of-the-art methods" and line 281 repeats "our method outperforms state-of-the-art methods," while the abstract honestly says "comparable." These claims are inconsistent, and the introduction/discussion overstate results. The paper should frame the comparison as "competitive with different trade-offs" rather than "outperforms SOTA."

### Minor
- **Camera autoencoder implementation details unspecified.** The architecture is described only as "stacked 3D convolutional and downsampling blocks" (line 149), and the loss weights λ₁–λ₄ in Eq. 5 are never specified. Given that this is a novel and important component, these details matter for reproducibility.
- **Resolution matching with baselines unclear.** The paper trains and evaluates at 256×256 (line 210) but does not report what resolution baselines were evaluated at, making it unclear whether the comparison is resolution-matched.

### Trivial
None.

## Nice-to-Haves
- An experiment demonstrating incremental trajectory generation or trajectory variation (change direction mid-generation) would directly validate the paper's central thesis and make the contribution far more compelling than metric improvements on static benchmarks.
- Discussion should acknowledge that the causal-generation advantage — the paper's raison d'être — remains unvalidated, and that the current experiments establish feasibility rather than a compelling case for AR over diffusion.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **DL3DV fairness concern** (raised by Harsh Critic): Excluding SEVA, ViewCrafter, and RayZer from DL3DV is standard practice when a benchmark was part of their training data. This actually protects the baseline comparison. The remaining baselines (MotionCtrl, LVSM) are weaker competitors, which limits evidential value but is not a methodological flaw. Per Hard Rules, this is an unfair comparison that favors the baseline, so it is removed.
- **Formatting/style nitpicks** (figure redundancy, acronym redefinition): Parser artifacts, not author errors. Removed per Hard Rules.
- **Missing appendix/proofs**: Stripped by parser. Exist in original submission.

## Novel Insights
The paper demonstrates that autoregressive generation can successfully handle camera-controlled multi-view synthesis — a domain previously dominated by diffusion models. The spatial-permutation/temporal-preservation strategy, adapted from prior AR image generation work (Pang et al. 2025, Yu et al. 2024a), is a well-motivated extension to sequential view synthesis. The video tokenizer ablation reveals that temporal-aware compression (FSQ over VQ) is critical for multi-view AR generation, with ~62% FVD improvement. However, the paper does not establish whether the causal AR structure provides practical advantages over sequential-but-non-causal approaches (e.g., causal diffusion with KV-caching), leaving the most distinctive aspect of the contribution unvalidated.

## Suggestions
- Add at least one experiment demonstrating the causal-generation advantage (e.g., trajectory extension, incremental generation, or reuse of existing tokens when the path changes).
- Reconcile claims across sections: the abstract's "comparable" is honest; the introduction and discussion should match this framing and acknowledge the mixed results against SEVA.
- Specify camera autoencoder architecture details (layers, channels) and loss weights (λ₁–λ₄) for reproducibility.
- Report baseline evaluation resolutions to confirm fair comparison.

## Calibration Anchors Retrieved

| Path | Avg Score | Round | Comparison to ARSS |
|------|-----------|-------|--------------------|
| rWIrdAo2xC.md | 2.83 | 1 | Weak anchor. Monocular 3D human rendering, rejected with much weaker results. ARSS clearly stronger. |
| 15lk4nBXYb.md | 3.00 | 1 | Weak anchor. Camera-pose controllable DiT, rejected at uniform 3s. ARSS clearly stronger. |
| MI0UiWeqOl.md | 2.33 | 1 | Weak anchor. Poly-autoregressive modeling, rejected. ARSS clearly stronger. |
| I86z54CL2y.md | 3.40 | 1 | Weak anchor. GeoGS3D single-view 3D, rejected. ARSS clearly stronger. |
| VLuJL8cnGk.md | 5.00 | 1 | Middle anchor. 3D-free meets 3D priors NVS, rejected. Overclaimed SOTA, limited novelty. ARSS has better ablations and more complete evaluation. |
| zDJf7fvdid.md | 6.00 | 1 | Middle anchor. Zero-shot NVS via video diffusion, accepted at uniform 6s. Training-free, but missing PSNR/SSIM comparisons and has flickering artifacts. ARSS is more complete with ablations and broader metrics. |
| FUgrjq2pbB.md | 6.50 | 1 | Middle anchor. MVDream multi-view diffusion, accepted. More focused (3D generation via SDS) with cleaner framing. |
| 3eFMnZ3N4J.md | 7.25 | 1 | Strong anchor. Efficient-3Dim single-image NVS, accepted. Faster training of diffusion model; less novel than ARSS but better validated. |
| QQBPWtvtcn.md | 7.67 | 1 | Strong anchor. LVSM, accepted. Transformer-based NVS with 1.5-3.5 dB PSNR gains. Stronger results and better framing than ARSS. |
| P4o9akekdf.md | 8.00 | 1 | Strong anchor. NoPoSplat sparse unposed images, accepted. Clearly stronger contribution. |
| 6O3Q6AFUTu.md | 8.00 | 1 | Strong anchor. NoiseDiffusion, accepted. Different domain (image interpolation). |
| OlzB6LnXcS.md | 8.00 | 1 | Strong anchor. One step diffusion, accepted. Clearly stronger. |
| pOcGFvfgjS.md | 5.00 | 2 | Narrowing anchor. AR-1-to-3, rejected at uniform 5s. Also AR for NVS but object-level only (Objaverse), less complete evaluation. ARSS clearly stronger with real-world datasets and better ablations. |
| GuQeZWbaGr.md | 5.50 | 2 | Narrowing anchor. AnyView personalized view transfer, rejected. Less relevant but helps bracket. |

**Round 1 bracket:** 5.0–7.67 (clearly above rejected 5.0 papers, below LVSM at 7.67).

**Round 2 narrowing:** The 5.0 anchors (AR-1-to-3, 3D-free meets 3D priors) are clearly weaker than ARSS — both were rejected with overclaiming and incomplete evaluation. The 6.0 anchor (zDJf7fvdid) is comparable but ARSS is more comprehensive. However, ARSS has the overclaiming problem against SEVA and the unvalidated causal motivation that zDJf7fvdid doesn't have (it's a training-free method with a more modest framing). ARSS lands slightly below zDJf7fvdid at 6.0 but above the 5.0 rejected papers.

**Final score: 5.5** — ARSS is a solid first exploration of AR-based NVS with strong ablations and competitive metrics against most baselines. However, the central motivation (causal generation advantage) is unvalidated, and the results against the strongest baseline (SEVA) are mixed with overclaiming. This places it between the clearly-rejected papers at 5.0 and the accepted papers at 6.0+.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>