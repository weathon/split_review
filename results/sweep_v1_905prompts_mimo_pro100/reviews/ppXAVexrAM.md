Now I have enough data for calibration. Let me synthesize the review.

---

## Summary

ARSS introduces a decoder-only autoregressive framework for novel view synthesis from a single image conditioned on a camera trajectory. It combines three components: a video tokenizer (VidTok) for temporal consistency, a camera autoencoder mapping Plücker raymaps to latent tokens for 3D guidance, and a hybrid spatial-permutation strategy that preserves temporal causality while randomly permuting spatial token order. Evaluated on RealEstate10K, ACID, and zero-shot on DL3DV, the method achieves competitive results against diffusion-based baselines, with strong error accumulation behavior over long camera trajectories.

## Strengths

- **First autoregressive framework for camera-controlled novel view synthesis.** ARSS is the first to apply a GPT-style causal decoder-only transformer to scene-level multi-view NVS with camera conditioning, extending the AR visual generation paradigm to a new and practically important task domain.

- **Well-designed ablation studies validate two of the three core components.** Table 2 (spatial-only permutation achieves PSNR 19.22 vs. 16.29 for raster and 18.76 for full permutation) and Table 3 (video tokenizer reduces FVD from 137.68 to 52.56 over per-frame VQ) provide concrete evidence that the spatial permutation strategy and video tokenizer are effective design choices, with visual support from Figure 7.

- **Error accumulation analysis demonstrates genuine causal advantage.** Figure 6 shows that ARSS maintains higher PSNR/SSIM and lower LPIPS across all frame indices with flatter degradation curves than all baselines, directly supporting the core thesis that causal sequential generation is better suited for long-horizon trajectories than joint generation.

- **Zero-shot generalization to DL3DV demonstrates robustness.** Table 1 shows ARSS achieves 16.70 PSNR and 0.347 LPIPS on DL3DV (zero-shot), outperforming LVSM (15.86, 0.400) and MotionCtrl (14.58, 0.507) across most metrics, suggesting reasonable out-of-distribution generalization.

## Weaknesses

### Fatal

None.

### Major

- **Overclaiming relative to the actual results.** The paper claims to "out-perform current state-of-the-art methods" (line 114, Discussion line 490), but Table 1 tells a more mixed story. On RealEstate10K, ARSS loses to SEVA on SSIM (0.624 vs. 0.670) and FID (47.60 vs. 46.98). On ACID, the FID gap is substantial: 47.76 vs. SEVA's 33.16 (a 44% relative increase). The paper does acknowledge this parenthetically in the quantitative results section ("−6.6% SSIM, +22% FID"), but the abstract, introduction, and discussion continue to frame the results as superiority rather than a trade-off where ARSS leads on pixel-level/perceptual metrics (PSNR, LPIPS) but trails on distributional/structural metrics (SSIM, FID). This framing mismatch between the evidence and the claims is a significant coherence issue that should be resolved.

- **Missing camera autoencoder ablation.** The camera autoencoder is one of the paper's three claimed contributions, yet there is no ablation testing what happens without it. Comparing against (a) no camera tokens, (b) raw Plücker coordinates directly fed as continuous features, or (c) a simple MLP encoding of camera parameters would allow readers to assess whether the autoencoder's design contributes meaningfully or whether any camera encoding would suffice. This is a notable gap given that the other two contributions (video tokenizer and spatial permutation) each have dedicated ablations.

### Minor

- **Training data and resolution confound acknowledged but not resolved.** The Discussion (line 490) admits that "different from the current diffusion-based view synthesis method that mostly finetuned from pre-trained models, our method is trained from scratch using limited public datasets with relatively low resolution." This is an important caveat that partly explains the metric trade-offs (e.g., FID gaps), but it appears only in the final paragraph rather than being foregrounded in the experimental setup. It also creates an internal tension: the paper claims superiority while acknowledging that the comparison is confounded by training conditions.

- **The causal advantage is claimed but only partially demonstrated.** The paper's core motivation is that AR models offer natural causal structure for sequential view generation that diffusion models lack. Figure 6 (error accumulation) provides supporting evidence, but the paper does not demonstrate the primary practical implications: generating variable-length trajectories at test time, conditionally extending trajectories, or incrementally reusing previously generated views. These experiments would directly validate the thesis rather than relying on a single metric.

- **No inference speed or training efficiency analysis.** The paper hints at computational efficiency advantages ("without such requirements" re: training from scratch) but never reports inference time, training time, or FLOPs comparisons with diffusion baselines. Given that one practical argument for AR models is faster or incremental generation, this omission weakens the efficiency case.

- **Low resolution (256×256) relative to contemporary methods.** The 256×256 resolution is acknowledged in the Discussion but is notably lower than what current methods operate at. Combined with the training-from-scratch limitation, it means the results may not fully reflect the approach's ceiling.

### Trivial

- The mathematical notation in Section 3.2.3 (Eqs. 6–8) is dense and the interleaving of π and x tokens with permutation notation P_i(j) is hard to follow. The prose description of the insight is clearer than the equations.

## Nice-to-Haves

- A comparison against a "naive AR" baseline (e.g., raster-scan order with standard VQ-VAE, no camera tokens) would demonstrate that the system's performance comes from the proposed components rather than simply from using an AR model.
- Failure case analysis showing where ARSS struggles would help assess robustness and guide future work.
- Per-scene or per-category breakdowns (indoor vs. outdoor) would clarify where the method excels and where it falls short.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Notation confusion about the moment term in Plücker coordinates (harsh critic).** The harsh critic claimed the paper's definition m = o × d is non-standard. However, in Plücker coordinates, the moment is m = p × d where p is any point on the line — the camera origin o is a valid point on the ray, so the paper's notation is correct. The harsh critic's proposed alternative (m = d × p) is actually the wrong sign convention. This criticism is factually incorrect and is removed.

- **Derivative contribution of spatial permutation (harsh critic).** The harsh critic flagged the spatial permutation as derivative of Pang et al. (2025) and Yu et al. (2024a). The paper explicitly credits these works and positions its contribution as the specific application to multi-view synthesis with camera tokens. Application contributions in a new domain (scene-level NVS) are valid, and the paper is transparent about its building blocks. This is a mild novelty concern, not a weakness.

- **Evaluation protocol concerns about sequence length (harsh critic).** The harsh critic speculated that baselines might use different sequence lengths. The paper uses a standardized protocol (17 frames, first frame conditioning) and there is no concrete evidence that other methods are evaluated differently. This is speculative and is removed.

- **Missing failure cases (harsh critic).** While useful as a suggestion, the absence of failure case analysis is common in NVS papers and does not constitute a substantive weakness for this venue.

- **Missing inference speed analysis (harsh critic).** While useful to have, this is a nice-to-have rather than a core flaw, and is common in NVS papers at this stage.

- **Generic concerns about cherry-picked qualitative figures (harsh critic).** The harsh critic noted qualitative figures are cherry-picked examples. All NVS papers show selected results; this is a general concern, not specific to this paper.

## Novel Insights

The paper provides a genuinely useful empirical observation in Figure 6: the autoregressive model's per-frame quality degrades more slowly along the camera trajectory than all diffusion-based and transformer-based baselines. This is the first concrete evidence that the causal generation structure of AR models produces less error accumulation for sequential view synthesis — a result that supports the broader thesis of using AR models for world-model applications where trajectories may be long and incrementally extended. The observation that spatial-only permutation outperforms both raster and full permutation (Table 2) also offers a practical insight: preserving temporal causality while randomizing spatial order is the right inductive bias for multi-view AR generation.

## Suggestions

1. **Reframe the claims honestly.** Replace "outperforms SOTA" with a clear characterization: ARSS leads on pixel-level and perceptual metrics (PSNR, LPIPS) but trails on distributional and structural metrics (SSIM, FID), and argue why the former matter more for downstream applications like world models or robotics.

2. **Add a camera autoencoder ablation.** Compare against (a) no camera tokens, (b) raw Plücker coordinates as continuous input, and (c) a simple MLP encoding. This would complete the ablation story for all three contributions.

3. **Demonstrate the causal advantage practically.** Show that ARSS can generate variable-length trajectories or condition on previously generated views without retraining — this is the primary claimed advantage and would be the strongest possible evidence.

4. **Foreground the training limitations earlier.** Move the training-from-scratch / low-resolution caveat from the Discussion to the experimental setup, and consider presenting the comparison as a trade-off between training efficiency and final quality.

## Score and Decision

### Anchor Comparison

**Round 1 anchors:**
- AR-1-to-3 (avg 5.0, reject) — AR approach for object-level NVS with fewer datasets and simpler evaluation. ARSS is clearly more comprehensive.
- Where Am I and What Will I See (avg 6.25, accept) — AR framework for joint spatial localization + view prediction. Similar overclaiming concerns; comparable novelty level.
- Zero-shot NVS via Adaptive Modulating (avg 6.0, accept) — Training-free NVS using video diffusion. ARSS has more substantial evaluation and clearer ablations.
- LVSM (avg 7.67, accept) — Transformer-based NVS with 1.5-3.5 dB PSNR improvements and clean narrative. Clearly stronger than ARSS.

**Round 2 anchors:**
- Cameras as Rays (avg 6.5, accept) — Novel camera representation for pose estimation. Comparable contribution level; ARSS addresses a different problem.
- Image and Video Tokenization with BSQ (avg 5.75, accept) — Tokenization-focused work with strong technical contribution. ARSS is comparable in scope.
- MVTokenFlow (avg 6.0, accept) — 4D content generation with multiview consistency. ARSS addresses a different problem but similar contribution level.
- WildFusion (avg 7.0, accept) — 3D-aware latent diffusion in view space. Stronger technical contribution than ARSS.

### Bracketing and Final Score

Round 1 bracket: 5.0–7.0. ARSS is clearly above AR-1-to-3 (5.0) and below LVSM (7.67).

Round 2 narrowing: 5.5–6.5. ARSS is comparable to Zero-shot NVS (6.0) and Where Am I (6.25), with similar strengths (genuine first contribution, good ablations) and similar weaknesses (overclaiming, missing ablations). ARSS's mixed metric results (strong on PSNR/LPIPS, weak on SSIM/FID) and the missing camera ablation keep it from the upper end, but the genuine first-mover contribution for AR-based scene-level NVS and the error accumulation analysis place it firmly in the middle.

Final score: **6.0**. ARSS is a solid first contribution to AR-based novel view synthesis with well-designed ablations for two of three components and a genuinely useful error accumulation analysis. The overclaiming issue and missing camera autoencoder ablation are significant but fixable. The mixed results are understandable given the training-from-scratch constraint and should be honestly presented rather than hidden.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>