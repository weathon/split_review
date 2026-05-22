Now I have thoroughly cross-checked all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper introduces ARSS, the first decoder-only causal autoregressive framework for novel view synthesis (NVS) from a single image with camera control. The method combines a video tokenizer (VidTok) for temporally consistent discrete tokens, a camera autoencoder that maps Plücker ray maps into 3D positional guidance tokens, and a hybrid token-order permutation strategy (spatial shuffle while preserving temporal causality) to adapt uni-directional transformers to bi-directional spatial context. Experiments on RealEstate10K, ACID, and DL3DV show competitive results on several metrics and demonstrate slower error accumulation over long camera trajectories compared to diffusion-based methods.

## Strengths

- **First decoder-only causal AR model for NVS with camera control.** While the individual components (video tokenizer, Plücker ray encoding, spatial token permutation) draw from prior work, their combination for sequential multi-view generation via next-token prediction is genuinely novel and well-motivated by the desire for causal, incremental view synthesis along camera trajectories. The ablation in Table 2 validates that the hybrid permutation strategy (spatial shuffle only) substantially outperforms raster ordering (PSNR 19.22 vs. 16.29) and full spatiotemporal permutation (19.22 vs. 18.76).

- **Competitive quantitative performance on key metrics.** On RealEstate10K, ARSS achieves the best PSNR (19.02), LPIPS (0.269), and FVD (50.51) among all methods including SEVA (18.73 PSNR, 0.349 LPIPS, 57.56 FVD). On ACID, ARSS leads in PSNR (21.93) and LPIPS (0.265). These are not universal wins — SEVA beats ARSS on SSIM and FID — but the method is clearly competitive.

- **Demonstrably slower error accumulation over long trajectories.** The per-frame analysis (Figure 6) shows that ARSS maintains higher PSNR/SSIM and lower LPIPS at every frame index (0–16) with flatter degradation slopes than all baselines. This directly validates the claim that the causal autoregressive structure mitigates drift in sequential view generation — a property that joint-denoising approaches lack.

- **Video tokenizer ablation confirms its importance.** Replacing VidTok with a VQ image tokenizer (Table 3) degrades FVD from 52.56 to 137.68 (−62%) and PSNR from 19.22 to 15.69, providing concrete evidence that temporal-aware tokenization is crucial for consistent multi-view generation.

- **Zero-shot generalization to out-of-distribution inputs.** Results on DL3DV (Table 1) and AI-generated images (Figure 5) demonstrate meaningful generalization beyond the training distribution, a capability not evaluated for several baselines.

## Weaknesses

### Major

- **Unexplained inconsistency between main and ablation results.** Table 1 reports "Ours" on RealEstate10K at PSNR 19.02, SSIM 0.624, LPIPS 0.269, FID 47.60, FVD 50.51. Tables 2 and 3 report "Ours" at PSNR 19.22, SSIM 0.565, LPIPS 0.294, FID 60.11, FVD 52.56. These are substantially different — SSIM drops by ~9.5%, FID increases by ~26% — and **no explanation is given** for which evaluation set, generation length, or inference setting produced each. This makes it impossible to confidently interpret either the main claims or the ablations, and it undermines the paper's reliability. *This is the single most important issue to address in revision.*

- **Overclaimed framing in the introduction.** The abstract appropriately says "overall comparable to state-of-the-art," but the introduction (line ~114) states that results "demonstrate that our method out-performs current state-of-the-art methods." Given that SEVA achieves clearly higher SSIM on both datasets (Re10K: 0.670 vs. 0.624; ACID: 0.664 vs. 0.623) and substantially lower FID on ACID (33.16 vs. 47.76), this claim is not supported. The paper's own Section 4.2 concedes a −6.6% SSIM gap and +22% FID gap. The framing should be brought in line with the evidence.

### Minor

- **Camera autoencoder is not ablated.** The camera tokens are a core component for 3D positional guidance, yet there is no experiment that replaces them with a simpler conditioning mechanism (e.g., a global per-view camera embedding, or no camera conditioning at all). Without this ablation, it is unclear whether the complex camera autoencoder design (3D convolutions, geometric loss in Eq. 5) is necessary, or whether the gains attributed to it come from other design choices. The ablation in Table 2 includes camera tokens as a constant — they should be varied.

- **Figure 6 axis labeling is ambiguous.** The x-axis shows "frame index (0 to 16)" but it is unclear whether frame 0 is the input view or the first generated view. If frame 0 is the input, baselines should show near-perfect metrics there; the reported ~18 PSNR at frame 0 for all methods suggests it may be the first generated view. This should be explicitly clarified.

- **Camera autoencoder training details omitted.** The paper states the camera autoencoder is "pre-trained" but does not specify whether it is frozen during AR training or fine-tuned jointly. This matters for understanding whether the AR model can adapt to camera encoding errors.

### Trivial

- Eq. (5) introduces the momentum term $\mathbf{m} = \mathbf{o} \times \mathbf{d}$. The notation $\mathbf{o}$ for the ray origin is introduced here without prior definition, and the "momentum" terminology is non-standard for Plücker coordinates (where the moment is typically $\mathbf{r} \times \mathbf{d}$ for a point $\mathbf{r}$ on the ray). This does not affect correctness but may confuse readers.

## Nice-to-Haves

- An ablation of the camera autoencoder (replace with global camera embedding or omit camera conditioning) would strengthen the contributions.
- Training at higher resolution (≥512) to match diffusion baselines' operating regime, as acknowledged in the Discussion.
- Reporting why the ablation numbers differ from the main table (dataset split, sequence length, inference configuration) would resolve the most significant concern.
- Visualizing camera token reconstruction quality would build trust in the 3D positional guidance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **RayZer misclassification claim (Harsh Critic):** The critic claims the paper "calls [RayZer] a non-diffusion method but then treats as diffusion-based." In fact, Section 4.1 clearly groups RayZer under "non-diffusion NVS methods" alongside LVSM. The paper is consistent.
- **"No discussion of concurrent work (LlamaGen fine-tuning)":** The paper reviews the relevant AR image generation literature (LlamaGen, VAR, etc.) and correctly identifies the gap. The suggestion to fine-tune LlamaGen for multi-view generation is a nice-to-have, not a missing baseline.
- **Generic baseline fairness concerns about MotionCtrl/LVSM:** The criticism that MotionCtrl is "not specialized for NVS" and that LVSM "is not generative, so comparing FID/FVD is odd" overstates the issue. Table 1 evaluates all methods on the same held-out test sets with standard NVS metrics, which is standard practice. The paper notes LVSM as a feed-forward method.
- **"Missing appendix/proofs":** These are parser artifacts; the original submission includes the appendix.
- **Pure formatting/style nitpicks:** Removed per instructions.

## Novel Insights

The reviews raise one genuinely novel observation beyond the paper's own contributions: the unexplained discrepancy between Table 1 and Tables 2/3 suggests that the ablation experiments may have been run on a different evaluation protocol (e.g., different number of generated frames, different test split, or different random seed for token permutation). If the ablation numbers are the ones that control for evaluation configuration, then the main-table numbers may be inflated relative to a controlled comparison. Conversely, if the main-table numbers are the standard evaluation, then the ablation results are weaker than they appear. Neither scenario is addressed in the paper, and resolving this is the single most important action for the authors.

## Suggestions

1. **Reconcile the numerical discrepancy** between Table 1 and Tables 2/3. Report all quantitative results on the same evaluation protocol (same split, same frame count, same inference settings). If the ablations used a different configuration, explain why and include a corrected comparison.
2. **Tone down the "outperforms" claim** in the introduction to match the evidence. The abstract's "overall comparable" language is appropriate.
3. **Add an ablation of the camera autoencoder** — at minimum, compare against a baseline that replaces camera tokens with a single global camera embedding per view, or removes camera conditioning entirely.
4. **Clarify the Figure 6 x-axis** — state explicitly whether frame 0 is the input view or the first generated view.
5. **State whether the camera autoencoder is frozen** during AR training.

## Score and Decision

**Calibration anchors (all from ICLR reviews):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QQBPWtvtcn.md` (LVSM) | 7.67 | Much stronger results and cleaner execution; ARSS is ~2.5 pts below |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NuHYh4YKNe.md` (GST) | 6.25 | Also autoregressive with camera tokenization; cleaner presentation without the inconsistency issue |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KI1zldOFz9.md` (CamTrol) | 5.80 | Different task; ARSS is roughly comparable in quality of contribution |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pOcGFvfgjS.md` (AR-1-to-3) | 5.00 | Most directly comparable (autoregressive NVS); ARSS is stronger (real datasets, better analysis) |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zfIxlvKq4u.md` (Design Space AR) | 4.00 | ARSS has stronger novelty and clearer contribution |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IqGVIU4rvM.md` (Tokenizer paper) | 2.50 | Fundamentally different league; ARSS is far stronger |

The paper proposes a genuinely novel approach with several well-supported strengths (first AR NVS framework, slower error accumulation, convincing video tokenizer ablation, zero-shot generalization). However, the unexplained inconsistency between main and ablation results (a ~9.5% SSIM gap and +26% FID gap with no explanation) is a significant reliability concern that prevents acceptance in the current form. The contribution is real but the experimental reporting needs a major fix.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>