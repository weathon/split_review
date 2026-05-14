Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a novel attention mechanism that addresses the quadratic computational bottleneck of the "concatenate-and-attend" paradigm in multi-condition Diffusion Transformers. Through analysis of attention patterns, the authors identify that spatial conditions exhibit strong diagonal localization while subject conditions activate sparse, keyword-correlated regions. They design two modules—Position-Aligned Attention (PAA) for one-to-one spatial correspondence and Keyword-Scoped Attention (KSA) for saliency-masked subject attention—along with a condition KV-cache and an early-timestep training strategy. The method achieves up to 10× inference speedup and 5.12× attention-VRAM reduction while maintaining competitive generation quality against OminiControl2 and UniCombine.

## Strengths

- **Strong empirical motivation from attention-pattern analysis**: Figures 2 and 3 provide clear, interpretable evidence that full attention in multi-condition DiTs is highly redundant, and that the redundancy pattern differs fundamentally by condition type (spatial-aligned vs. subject-driven). This directly and convincingly motivates the PAA/KSA decomposition.

- **Impressive and well-benchmarked efficiency gains**: Figures 7–8 demonstrate 3.9–10× inference speedup and 2.46–5.12× VRAM reduction for the attention module compared to the full-attention baseline (UniCombine) across varying numbers of conditions, and the method also outperforms the optimized OminiControl2. These are substantial, practical gains.

- **Well-motivated and simple attention redesign**: The decomposition into PAA (O(N) one-to-one attention for spatial conditions) and KSA (masked attention for subject conditions) is intuitive, cleanly maps onto the observed sparsity patterns, and is architecturally simple to implement.

- **The condition KV-cache is a practical optimization**: Computing Key and Value projections for all condition tokens once and reusing them across denoising steps (Section 3.2, Figure 4a) is a simple but effective idea that compounds the efficiency benefits without any quality impact.

- **Comprehensive multi-condition qualitative results**: Appendix Figures 14–16 demonstrate harmonious integration of 2, 3, and 4 simultaneous conditions, showcasing the scalability of the approach beyond the two-condition main experiments.

## Weaknesses

### Fatal

None.

### Major

- **Ablation studies lack quantitative quality and controllability metrics**: Sections 4.3.1 (PAA) and 4.3.2 (KSA) report only latency and VRAM, plus qualitative visual examples. No FID, SSIM, F1, MSE, or subject-consistency metrics are provided for the PAA vs. full-attention/SWA comparison or for KSA across different mask thresholds. The paper's central claim—that efficiency gains do not degrade quality—is demonstrated for the full system (Table 1) but is not quantitatively validated at the component level. A reader cannot assess the actual quality–efficiency trade-off curve for PAA or KSA individually. This is addressable with additional experiments but represents a significant evidential gap in the current manuscript.

### Minor

- **Subject-consistency metric conflates subject and background preservation**: CLIP-I and DINOv2 are computed between generated images and ground-truth images. In the multi-condition reconstruction setting (where conditions are extracted from the ground truth), this is standard and reasonable. However, as a measure of *subject consistency* specifically, these global similarity metrics do not isolate subject appearance from background/scene similarity. A localized metric (e.g., DINOv2 computed on subject bounding boxes or segmentation masks) would more precisely measure what the paper claims.

- **Early-timestep sampling validation is partial**: The perturbation analysis (Appendix A.2) and SSIM training curves (Figure 13) plausibly support the claim that early timesteps matter more. However, the paper does not report a final-model comparison (all task metrics: FID, controllability, consistency) between the proposed Logit-N(0.5, 1.5) sampling and the standard Logit-N(0, 1). The SSIM training curve alone is suggestive but not sufficient to fully substantiate the claim that early-timestep sampling "enhances the final model's control fidelity."

- **KSA mask stability across timesteps is not empirically validated**: KSA reuses the binary mask computed at timestep t for timestep t+1, citing temporal consistency (Zhou et al., 2025). However, no experiment measuring mask overlap (IoU) between consecutive timesteps or comparison against recomputing the mask at every step is provided. The risk of error accumulation, especially at aggressive thresholds, is unexamined.

### Trivial

- **"Norm" operation in KSA mask generation (Eq. 3) is undefined**: The paper writes M^t = Norm(...) but does not specify what normalization is applied (e.g., min-max, softmax, thresholding). This is a minor clarity issue.

- **Keyword extraction method is not specified**: The paper states "each image caption contains a descriptive keyword" (Section 4.1) and that the keyword set K "typically contains just 1 to 2 tokens," but how keywords are identified from captions is not explained. Similarly, the encoder used for subject condition tokens (SJ) is not explicitly specified beyond references to prior work.

- **The 5.12× VRAM reduction applies to the attention sub-module, not total GPU memory**: The abstract and introduction frame this prominently; while the paper does clarify this in context (e.g., Figures 7–8 labels), a reader skimming the abstract could be misled. The framing is technically correct but could be more precise.

## Nice-to-Haves

- A direct end-to-end comparison of the full PKA system against a FLUX model using full attention for all conditions (i.e., "PKA w/o PAA and w/o KSA") would cleanly isolate the overall quality–efficiency trade-off beyond the external baselines.
- Quantitative subject-consistency evaluation using localized metrics (e.g., face similarity, DINOv2 on segmented subject regions) would strengthen the subject-fidelity claims.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Evaluation metric for subject consistency is invalid for the task"** (Harsh Critic Point 1): The critic argued that CLIP-I/DINOv2 against ground-truth is fundamentally invalid because prompts change the scene. However, in the quantitative evaluation (Table 1), conditions (Canny, Depth, Subject) are extracted from the ground-truth image and the model's task is reconstruction—the ground truth IS the target. Global similarity metrics are standard and appropriate in this multi-condition reconstruction setting. While a localized metric would better isolate subject consistency (kept as a Minor weakness above), the metric is not invalid and does not undermine the experimental support.

2. **"Missing baseline: the same FLUX model with full attention"** (Harsh Critic Section-by-Section Notes): The PAA ablation (Section 4.3.1) already compares against "w/o PAA" (full attention), the KSA ablation uses "w/o KSA" (ε=0) as baseline, and the main results compare against UniCombine (full attention). The relevant baselines exist in decomposed form. A unified full-attention FLUX baseline for the complete multi-condition setting would be cleaner but its absence does not constitute a missing critical baseline.

3. **"Table 1 is not present in the review copy; I cannot verify the numbers"** (Harsh Critic): This is a parser artifact. The table exists in the original PDF and the paper describes its contents in detail. Removed as a parser issue, not an author error.

4. **"KSA's reliance on temporal consistency is not analyzed or justified" → elevated to "serious concern about soundness"**: The criticism is valid at a Minor level (kept above), but the harsh critic's framing as a "serious concern about the soundness of the method" is disproportionate. Temporal consistency of latent representations across adjacent denoising steps is a well-established phenomenon in diffusion models (the paper cites Zhou et al., 2025), and the mask reuse is a pragmatic acceleration heuristic that many caching-based DiT papers employ. The lack of empirical validation is a gap but does not threaten the method's soundness.

## Novel Insights

None beyond the paper's own contributions. The core insight—that attention redundancy in multi-condition DiTs is condition-type-specific (spatial alignment vs. keyword-driven sparsity) and can be exploited through different sparse attention strategies—is genuinely novel and well-supported by the attention-map analysis. The decomposition into PAA and KSA follows naturally from this observation and represents a clean design contribution.

## Suggestions

- Add quantitative quality metrics (FID, SSIM, F1, MSE, CLIP-I) to the PAA ablation (Section 4.3.1) and the KSA threshold sweep (Section 4.3.2). This is the single most important improvement to the paper.
- Train one model with standard Logit-N(0,1) sampling and compare against the early-timestep model on all final metrics to fully validate the training strategy.
- Define the "Norm" operation in Equation 3 and clarify how keyword tokens are identified from captions and how subject condition tokens (SJ) are encoded.
- Consider a KSA mask stability experiment (IoU between consecutive timesteps) to strengthen the temporal-reuse justification, or at minimum discuss the expected impact more explicitly.

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Decision | Comparison to paper under review |
|------|-----------|----------|----------------------------------|
| URbsHlTK8c (HyCa) | 7.00 | Accept (Oral) | Stronger: more comprehensive multi-model evaluation, deeper theoretical framing (ODE modeling of feature evolution), similar speedup range. Paper under review has narrower scope and thinner ablation. |
| 0hy9kJ1ULB (MoGA) | 7.00 | Accept (Poster) | Stronger: tackles long video generation at 580k-token scale, learnable token routing, FlashAttention integration. Our paper's contributions are more modest in scale. |
| 3Z3Is6hnOT (Fast-dLLM) | 7.00 | Accept (Poster) | Stronger: addresses KV-cache and parallel decoding for diffusion LLMs with both theoretical analysis and strong empirical results. Different domain but higher evaluation standard. |
| ANKQqRicBM (DiffMoE) | 5.33 | Reject | Comparable: DiffMoE has good ablations but limited qualitative results; our paper has stronger efficiency claims and qualitative results but weaker component-level ablation. |
| eD8IPvNoZB (SLA) | 5.00 | Accept (Poster) | Comparable: SLA proposes sparse-linear attention for DiTs with 20× attention reduction and 2.2× end-to-end speedup. Our paper has better motivation (condition-specific sparsity analysis) and similar/better efficiency numbers, but SLA has more thorough ablation and GPU kernel implementation. |
| 92PM2kSzK1 (D²C) | 3.60 | Reject | Our paper is clearly stronger: better motivation, clearer contributions, stronger results. |
| gT6AmJghJi (DynamicControl) | 2.00 | Reject | Our paper is much stronger: the low-score anchor has fundamentally flawed problem framing and unclear methodology. |

The paper under review sits between SLA (5.0, accepted poster) and DiffMoE (5.33, rejected). Like SLA, it proposes a novel attention sparsification mechanism for DiTs with strong efficiency results. The motivation via attention-pattern analysis is clearer and more compelling than SLA's. However, the ablation studies lack quantitative quality metrics (a gap SLA does not share), which weakens the evidence for the paper's central quality-preservation claim at the component level. The main results (Table 1) do validate the full system comprehensively, and the efficiency gains are substantial and well-measured. The weaknesses are addressable with additional experiments rather than fundamental methodological flaws.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>