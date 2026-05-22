Now I have all the information needed. Let me produce the final consolidated review.

## Summary

ARSS is the first work to apply a decoder-only causal autoregressive (GPT-style) transformer to novel view synthesis from a single image, conditioned on an explicit camera trajectory. The framework combines a video tokenizer for temporally consistent visual tokens, a camera autoencoder that converts Plücker raymaps into 3D positional tokens, and a hybrid permutation strategy that shuffles spatial token order while preserving temporal causality. Experiments on RealEstate10K, ACID, and zero-shot DL3DV demonstrate competitive results against diffusion-based methods.

## Strengths

- **First causal AR model for NVS with explicit camera control.** The paper pioneers the application of decoder-only AR models to novel view synthesis — a genuine gap in the literature. The motivation for causal generation along a camera trajectory (enabling incremental extension and reuse of prior views) is well-articulated, even if not experimentally demonstrated.

- **Hybrid spatial-temporal token permutation.** The strategy of permuting spatial token order within each frame while keeping temporal order fixed is principled, and the ablation (Table 2) shows it dramatically outperforms both full permutation (+2.5% PSNR over full perm.) and raster order (+18% PSNR over raster). Figure 7 visually confirms that alternative strategies produce distorted geometry.

- **Temporal consistency via video tokenizer.** The ablation in Table 3 validates that using a video tokenizer (VidTok) instead of per-frame VQ image tokenization improves FVD by ~62% (52.56 vs. 137.68), a clear quantitative demonstration of the tokenizer's role in maintaining inter-frame coherence.

- **Error accumulation analysis.** Figure 6 shows that ARSS maintains flatter degradation curves over 16-frame trajectories compared to MotionCtrl, RayZer, ViewCrafter, and LVSM. This is a meaningful result supporting the claim that causal generation handles long camera sweeps better than joint-denoising approaches.

- **Zero-shot generalization evidence.** On DL3DV (unseen during training), ARSS achieves the best PSNR (16.70), SSIM (0.449), LPIPS (0.347), and FVD (91.25) among methods evaluated zero-shot. Qualitative results on AI-generated images (Figure 5) further support generalization claims.

## Weaknesses

### Major

- **Overclaimed results relative to evidence.** The Introduction (line 114) and Discussion (line 490) state the method "outperforms current state-of-the-art methods," but Table 1 tells a more nuanced story. ARSS leads on PSNR, LPIPS, and FVD on both RealEstate10K and ACID, but SEVA scores substantially higher on SSIM (+7.4% on Re10K, +6.6% on ACID) and especially FID (+22% on Re10K, +44% on ACID). The paper dismisses these gaps as "minor geometric inconsistencies" (line 419), but a 44% FID gap is not minor. The Abstract more cautiously says "overall comparable," which better reflects the evidence. The paper should either calibrate its claims to "competitive with" or provide a clear framing for when and why the trade-offs occur.

- **Strongest competitor omitted from error accumulation analysis.** Figure 6 includes MotionCtrl, RayZer, ViewCrafter, and LVSM, but excludes SEVA — the single strongest competitor on SSIM and FID. Since the paper's central qualitative argument is that ARSS degrades more slowly over long trajectories, omitting the most relevant comparison undermines this claim. The figure is still informative about the included baselines, but the absence of SEVA is a significant gap.

- **Numerical inconsistency between main results and ablations.** Table 1 reports ARSS achieving PSNR 19.02 / SSIM 0.624 / LPIPS 0.269 / FID 47.60 on Re10K (17-frame sequences, 256×256). Tables 2 and 3 report "ours" achieving PSNR 19.22 / SSIM 0.565 / LPIPS 0.294 / FID 60.11 on the same dataset. All metrics differ substantially, and the paper provides no explanation. The reader cannot determine whether the ablation studies use a different test split, different frame count, or different seed. This ambiguity makes the contribution of each component unquantifiable.

### Minor

- **Camera autoencoder contribution is not ablated.** The paper introduces a camera autoencoder to convert Plücker raymaps into camera tokens with a geometry-constrained loss (Eq. 5), but no ablation study compares the full method against a variant without camera tokens or with simpler conditioning (e.g., raw camera parameters). Without this, the reader cannot assess whether the camera autoencoder meaningfully improves generation quality or whether visual tokens plus the video tokenizer already encode sufficient viewpoint information.

- **Verification of tokenizer causality is deferred.** The paper states that VidTok is used "for temporally causal modeling" (line 344) and describes both causal and non-causal modes (Section 3.1). This is stated but not verified — no analysis, ablation, or reference to a specific causal variant of VidTok is provided. A brief analysis of how the tokenizer's temporal receptive field interacts with the autoregressive mask would strengthen the paper.

- **"Outperforms" vs. "comparable" inconsistency.** The Abstract claims the method is "overall comparable to state-of-the-art" while the Introduction/Discussion claim it "outperforms" SOTA. These are inconsistent framings of the same results.

### Trivial

- None (the formatting issues are parser artifacts, not author errors).

## Nice-to-Haves

- Include SEVA in the error accumulation analysis (Figure 6) for a complete comparison.
- Ablate the camera autoencoder by comparing against simpler camera conditioning or no camera conditioning.
- Report inference speed / compute requirements to substantiate advantages of the AR approach over diffusion.
- Demonstrate the claimed AR advantage of incremental trajectory extension (generate a view, then extend and generate more views from the newly generated frames).
- Report the model's parameter count and layer count for reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"VidTok is non-causal by default"** (Harsh Critic #2). The paper explicitly states "We apply VidTok... for temporally causal modeling" (line 344) and describes both causal and non-causal scenarios in Section 3.1. The critic's assertion that VidTok has no causal variant is speculation about a cited tool — per the hard rules, this is removed.
- **"P_i(j) notation undefined."** The paper defines it inline at line 247: "where x_{ij}^{P_i(j)} represents the j-th randomly shuffled token under i-th frame."
- **"Camera token sequence contradicts Figure 2 caption."** Eq. (6) shows camera tokens π_{ij} appearing immediately before visual tokens x_{ij} in each pair — this is consistent with "inserted before visual tokens."
- **"DL3DV results for SEVA should be reported."** The paper explains these methods were trained on DL3DV, making zero-shot comparison inapplicable. This is a reasonable justification.
- **"Missing related works."** Excluded per rules (no external sources to verify).
- **Formatting/style nitpicks.** Excluded as parser artifacts.
- **Generic demands for more baselines without specific justification.** E.g., "missing modern diffusion baselines like CAT3D, MVDream." These are not standard for this comparison and the paper already compares against 6 methods including SEVA, the most relevant concurrent work.
- **Strength Finder generic strengths** (e.g., "addressed an important problem," "targeted an interesting question") — removed for lacking specific evidence.

## Novel Insights

The harsh critic raises a genuinely interesting point about tokenizer-receptive-field mismatch in autoregressive visual generation paradigms — when a video tokenizer encodes each frame's latent tokens using bidirectional temporal context, the training distribution for tokens (informed by future frames) may differ from the inference distribution (no future frames available). While the paper states it uses causal tokenization, the broader community challenge of ensuring that the tokenizer's temporal receptive field respects the autoregressive model's causal constraint is worth surfacing as an open issue. Beyond this, no truly novel insight emerges from the reviews beyond the paper's own contributions.

## Suggestions

1. **Calibrate the claims.** Replace "outperforms" with "is competitive with" or clearly scope the claims: "ARSS achieves higher PSNR and LPIPS, while SEVA achieves higher SSIM and FID." Acknowledge the trade-off transparently.
2. **Include SEVA in Figure 6.** This is the most important missing experiment.
3. **Explain or fix the PSNR discrepancy.** State whether Tables 2/3 use a different evaluation setup than Table 1, and ensure consistency.
4. **Add a camera autoencoder ablation.** Compare full ARSS against a variant that removes camera tokens or uses simpler conditioning.
5. **Provide tokenizer causality analysis.** Show that the causal mode actually prevents future-frame information leakage during encoding, or acknowledge if this is a limitation.

## Score and Decision

**Anchor comparisons (all from calibration search):**

| Path | Avg Score | Comparison to ARSS |
|------|-----------|-------------------|
| LVSM (`QQBPWtvtcn.md`) | 7.67 | Much stronger: cleaner evaluation, fully justified claims, comprehensive baselines. ARSS is well below. |
| GST / "Where Am I" (`NuHYh4YKNe.md`) | 6.25 | Stronger execution with more thorough ablations, but mixed review reception. ARSS is below. |
| Zero-shot NVS via Video Diffusion (`zDJf7fvdid.md`) | 6.00 | Comparable-level idea, but cleaner framing. ARSS is slightly weaker due to overclaiming. |
| AR-1-to-3 (`pOcGFvfgjS.md`) | 5.00 | Highly similar (autoregressive NVS). Shared weaknesses in evaluation; ARSS has slightly broader evaluation (3 datasets vs. 1) but also has the overclaiming issue. ARSS is comparable or slightly better. |
| Set AR Modeling (`b9dBNNeDd3.md`) | 4.60 | Similar tier of quality — both have interesting ideas undermined by evaluation concerns. Comparable. |
| Exploring AR Design Space (`zfIxlvKq4u.md`) | 4.00 | Slightly weaker; more of a survey/analysis paper with limited novelty. ARSS is modestly stronger. |
| CCM-DiT (`15lk4nBXYb.md`) | 3.00 | Clearly weaker: poor writing, limited evaluation, unclear contributions. ARSS is significantly stronger. |

The paper introduces a genuinely novel framework (first decoder-only AR model for NVS with camera control) with some supporting evidence. However, the evaluation is undermined by overclaimed results relative to the data in Table 1, omission of the strongest competitor from the error accumulation analysis, an unexplained numerical inconsistency between main results and ablations, and a missing ablation for a core claimed component. These issues are significant but not fatal — the core idea has merit and the paper provides partial validation. Relative to the anchors, ARSS sits slightly below AR-1-to-3 (5.00) and above CCM-DiT (3.00).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>