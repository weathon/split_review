Now I have all the information I need to write the final review. Let me synthesize everything carefully.

---

## Final Consolidated Review

## Summary
ARSS introduces a decoder-only autoregressive (GPT-style) transformer to the task of novel view synthesis from a single image. It tokenizes multi-view image sequences via a video tokenizer, encodes camera trajectories into 3D positional tokens via a learned camera autoencoder, and applies a hybrid permutation strategy (spatial shuffle + fixed temporal order) for next-token prediction. Experiments on RealEstate10K, ACID, and zero-shot on DL3DV show competitive results against diffusion-based NVS methods.

## Strengths
1. **First application of decoder-only autoregressive models to controlled novel view synthesis.** The paper demonstrates that a causal transformer with camera conditioning can generate view-consistent sequences from a single image, opening a new paradigm for NVS that is conceptually distinct from the dominant diffusion-based approaches. The full pipeline (Figure 2) and quantitative results (Table 1) support this claim.

2. **Hybrid token permutation strategy is well-motivated and ablated.** The paper identifies a key tension — unidirectional causal attention vs. bidirectional spatial image context — and proposes shuffling tokens spatially while preserving temporal order. The ablation (Table 2: 19.22 PSNR vs. 16.29 raster, 18.76 full perm.) provides clear evidence that this design choice matters.

3. **Video tokenizer ablation with FVD metric.** The ablation in Table 3 compares VQ image tokenizer vs. video tokenizer and reports FVD (52.56 vs. 137.68, a ~62% improvement), demonstrating that temporal encoding is critical for multi-view consistency. Including FVD as a temporal consistency metric is a methodological strength.

4. **Error accumulation analysis over long trajectories.** Figure 6 shows per-frame metrics across the generated sequence, with ARSS exhibiting flatter degradation curves than baselines. This directly addresses a core challenge for autoregressive multi-view generation.

5. **Zero-shot generalization to out-of-distribution inputs.** Figure 5 shows ARSS generating consistent novel views from AI-generated oil paintings and cartoon images, demonstrating generalization beyond the photorealistic training distribution.

## Weaknesses

### Fatal
None.

### Major

1. **The camera autoencoder, a core claimed contribution, is never directly ablated.** The paper presents the camera autoencoder as necessary for "accurate 3D position in the scene" (Section 3.2.2) and devotes an entire subsection to its design with geometric loss terms (Eq. 5). Yet there is no experiment comparing ARSS with vs. without the camera autoencoder, or against simpler alternatives such as directly embedding camera pose parameters or using sinusoidal positional encodings of Plücker coordinates. Similarly, the geometry losses (ray orthogonality and unit-length regularization) are not validated — do they improve generation quality or are they benign? Without this ablation, the claimed contribution of 3D-aware AR generation via the learned camera encoder is unsubstantiated. This is a significant omission for a component that the paper pitches as one of its three main modules.

2. **Insufficient detail on baseline evaluation protocol.** The paper compares against ViewCrafter, RayZer, MotionCtrl, Genwarp, LVSM, and SEVA, but does not specify the resolution, number of target frames, or camera trajectory configuration used for these baselines. The Implementation Details section (Section 4.1) only describes ARSS's own setup (256×256, 17 frames). Several reported numbers raise plausibility questions — for instance, ViewCrafter at 12.67 PSNR on RealEstate10K and RayZer at 12.97 PSNR are notably lower than what one might expect from these methods. Without a clear description of the evaluation protocol applied to each baseline, the quantitative comparisons in Table 1 lack credibility. The paper should either provide official published numbers for the same datasets or describe the re-implementation protocol in detail (including resolution, frame count, and conditioning).

3. **Quantitative advantage over the strongest competitor (SEVA) is mixed, yet the paper overclaims.** The text acknowledges that SEVA achieves close results, with ARSS better on PSNR (+1.1%) and LPIPS (–21%) but worse on SSIM (–6.6%) and FID (+22%). The paper then claims to "outperform" state-of-the-art methods. A PSNR gain of +1.1% is small, while an FID increase of +22% is substantial. Moreover, SEVA is trained at higher resolution on more data — the paper notes this as context, but the abstract and introduction still use language suggesting clear superiority. The claims should be tempered to reflect a trade-off rather than outright outperformance.

### Minor

1. **Limited training scale and unspecified convergence.** The model is trained for 100K iterations on 8 H100 GPUs. The paper does not report whether the model converged, or whether longer training would close the gap to SEVA. Diffusion-based NVS methods often train for 500K+ iterations. This is a missing detail that makes it difficult to assess whether the reported results reflect the method's full potential.

2. **No study of classifier-free guidance scale.** Appendix A.2 describes CFG implementation with a guidance scale ω, but no ablation or study of different ω values is provided. Since CFG can significantly affect generation quality, this is a gap, albeit a minor one.

### Trivial
None.

## Nice-to-Haves
- Comparison with a non-autoregressive transformer baseline (e.g., encoder-decoder with bidirectional attention using the same tokens and camera conditioning) to isolate the value of causal modeling.
- Error accumulation comparison with SEVA's per-frame metrics (Figure 6 only shows ARSS's own curves).
- Ablation of the geometric loss terms in Eq. 5 (each term separately).
- Study of CFG guidance scale (ω) values.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"SEVA's numerical values omitted from Table 1 on RealEstate10K and ACID"** — The table in the paper does include SEVA's values (the paper discusses them in text: "+1.1% PSNR, –21% LPIPS, –6.6% SSIM, +22% FID"). The table was partially garbled by the PDF parser. REMOVED per hard rule on parser artifacts.
- **"Tokenizer ablation shows core improvement is tokenizer, not AR framework"** — This misinterprets the ablation. The comparison of VQ image tokenizer vs. video tokenizer validates a specific design choice within ARSS, not the AR framework itself. Both conditions use the same AR model. REMOVED as strawman.
- **"Raster baseline (16.29 PSNR) is surprisingly low"** — The paper explains this as a consequence of mismatch between unidirectional attention and bidirectional image data, which is a plausible and testable explanation. Speculating that the number should be higher without evidence is not a valid criticism. REMOVED.
- **"Video tokenizer trained on natural video may not generalize to viewpoint change"** — The ablation results (Table 3) directly show that the video tokenizer significantly outperforms the image tokenizer on FVD, demonstrating tangible benefits for temporal consistency across views. REMOVED as factually contradicted by evidence in the paper.
- **"Hybrid permutation is borrowed from RandAR — incremental contribution"** — The paper explicitly cites RandAR and similar works and identifies the novelty as applying and adapting these techniques to multi-view NVS with camera tokens. Building on prior work is standard practice. The camera-conditioned variant with temporal preservation is a non-trivial adaptation.
- **"Motivation for AR vs. diffusion not experimentally demonstrated"** — The paper's motivation (AR enables causal structure along camera paths) is a conceptual argument for why the AR direction is worth exploring. It is not a claim the paper must experimentally prove to justify its contribution; the paper's main claim is that AR works for NVS, not that it is strictly better than diffusion for all settings.

## Novel Insights
The reviews surface a thoughtful tension: the paper's strongest evidence for its design comes from the tokenizer and permutation ablations (which are clean and informative), while its weakest evidence surrounds the camera autoencoder (a core claimed contribution that is never ablated). This asymmetry — good system-level validation but poor component-level validation — suggests the paper would benefit from either providing the missing ablation or repositioning the camera autoencoder as a straightforward engineering choice rather than a claimed contribution. The mixed results against SEVA also underscore that the paper is positioned as a "first of its kind" demonstration rather than a definitive SOTA claim, and the writing should reflect that.

## Suggestions
1. **Add an ablation of the camera autoencoder.** Compare at minimum: (a) camera autoencoder tokens, (b) raw Plücker coordinates concatenated with visual tokens, (c) a simple MLP encoding of camera extrinsics+intrinsics. This is essential to justify the design of Section 3.2.2.
2. **Clarify the baseline evaluation protocol.** State the exact resolution, frame count, conditioning, and any hyperparameter choices used for each baseline. If numbers are from official implementations, cite them precisely.
3. **Temper the claims in the abstract and introduction** to reflect the mixed quantitative trade-off with SEVA rather than claiming clear "outperformance."
4. **Report whether the model converged** at 100K iterations (e.g., plot training loss) and discuss whether longer training would likely change the results.
5. **Report the CFG guidance scale used** and ideally provide a brief study of its effect.

## Score and Decision

**Calibration anchors** (from vector search over human reviews):

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `PZQHihJlfm.md` (ArchonView: AR for object NVS) | 5.00 | Reject | Very similar topic. ArchonView had clearer SOTA claims and scaling-law experiments but some of the same baseline-fairness concerns. ARSS has weaker experimental validation. |
| `pIyADlhQsp.md` (CausNVS: AR diffusion for NVS) | 3.50 | Reject | Similar task. CausNVS was criticized for limited novelty and comparable results. ARSS has a more novel core paradigm (pure AR vs. diffusion) but similar validation gaps. |
| `rJdGst0W8s.md` (ARPG: randomized parallel AR) | 6.50 | Accept | Stronger paper with thorough ablations and clear efficiency gains. ARSS is less experimentally complete. |
| `yx3g4sF70y.md` (SHARP: feed-forward NVS) | 5.00 | Accept | ARSS and SHARP both have missing ablations of core components (camera autoencoder vs. 3DGS necessity). SHARP had clearer SOTA on perceptual metrics; ARSS has mixed results. |
| `1CR1MTIgmq.md` (unfounded claims) | 0.00 | Reject | Not comparable — this is a meta-commentary paper. |
| `OPFE1zPYbU.md` (flawed diffusion analysis) | 1.00 | Reject | Not comparable — fundamentally different paper type. |
| `StshuNpuaO.md` (scaling law) | 5.00 | Reject | Unrelated topic but similar score band. |

The paper makes a genuine contribution (first decoder-only AR for camera-controlled NVS) with some well-executed ablations, but the missing ablation of the camera autoencoder and the insufficiently documented baseline evaluation are significant gaps that prevent acceptance at the current level of rigor. The paper is above causality-challenged papers (avg 3.5) but below rigorously validated papers (avg 5+). 

Comparative assessment: ARSS is slightly *weaker* than ArchonView (5.00) because ArchonView had broader experiments (scaling laws, more datasets) and the camera autoencoder in ARSS is an unablated core component. ARSS is stronger than CausNVS (3.50) because the core idea is more novel and the ablations that *are* present are informative. The best anchor is SHARP (5.00, Accept), which had similar missing-validation issues but clearer SOTA numbers. ARSS's mixed results against SEVA make its contribution less clear-cut.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>