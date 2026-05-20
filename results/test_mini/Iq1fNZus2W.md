Now I have all the verification I need. Let me write the final consolidated review.

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA) to address the computational bottleneck of multi-condition control in Diffusion Transformers (DiTs). PKA decomposes full attention into two specialized modules: Position-Aligned Attention (PAA), which confines spatial condition computation to aligned patches (reducing O(N²) to O(N)), and Keyword-Scoped Attention (KSA), which uses keyword-derived masks to restrict subject-condition attention to salient regions. An early-timestep sampling strategy for training is also proposed. Experiments on FLUX.1 with LoRA fine-tuning demonstrate up to 10× inference speedup and 5.12× VRAM reduction in the attention module while maintaining or improving generation quality across three multi-conditional tasks.

## Strengths

1. **Well-motivated by empirical sparsity analysis.** Figures 2 and 3 provide direct evidence that attention in multi-condition DiTs is highly redundant: spatial conditions exhibit strongly diagonal attention (localized to aligned patches), and subject conditions activate only keyword-relevant image regions. This analysis cleanly motivates the two-module design of PKA and is a genuine empirical contribution.

2. **Impressive and cleanly measured efficiency gains.** Figures 7 and 8 show that PKA achieves a 3.90×–10× inference speedup and 2.46×–5.12× VRAM reduction in the attention module compared to the full-attention baseline, with gains monotonically increasing in the number of conditions. The efficiency results are compelling and directly validate the central claim of eliminating computational waste.

3. **Quality maintained or improved in the main evaluation.** Table 1 reports that PKA achieves the best FID (52.99 vs. 61.03 for UniCombine on Subject-Canny), best CLIP-I (0.945), and best DINOv2 (0.926) scores on the Subject-Canny task, with similar advantages on Subject-Depth and Canny-Depth tasks. This demonstrates that the dramatic efficiency gains do not come at the expense of generation quality.

4. **Ablation confirms PAA efficiency over sliding window alternatives.** Figure 9 shows PAA (13.63s, 237MB) outperforms even the most efficient sliding-window variant (SWA size 1: 14.00s, 276MB) on both latency and VRAM. KSA threshold analysis (Figure 10) further shows tunable efficiency gains with visually graceful quality degradation.

## Weaknesses

### Major

1. **Missing quantitative quality metrics in PAA and KSA ablations.** Figures 9 and 10 report only latency and VRAM for the ablated configurations, without any of the quality metrics used in Table 1 (FID, CLIP-I, DINOv2, F1, MSE). This makes it impossible to verify that the individual modules (PAA vs. full attention, or KSA at various thresholds) do not degrade generation quality. The claim that KSA offers a "graceful trade-off" (line ~308) is supported only by visual inspection, which is inconsistent with the paper's otherwise quantitative approach. Adding the same metrics from Table 1 to these ablations would close this gap.

2. **Early-timestep sampling is claimed as a contribution but validated only qualitatively.** Section 3.3 presents the sampling strategy as a contribution that "accelerates convergence and enhances the final model's control fidelity." However, Figure 11 provides only visual comparisons at different training iterations. No quantitative measures—FID over training iterations, loss curves, or any of the metrics from Table 1 across training checkpoints—are reported for any of the sampling distribution variants (μ=-0.5, μ=0, μ=0.5). Without such evidence, the claimed benefit of this strategy is unsubstantiated.

### Minor

1. **Keyword token identification unspecified.** Section 3.2.2 states the keyword set K "typically contains just 1 to 2 tokens" but does not explain how these tokens are extracted from the text prompt (e.g., noun extraction, parsing heuristic, manual selection). This is needed for reproducibility.

2. **"Norm" in Equation 3 is undefined.** The normalization operation in the mask computation is not specified (softmax, min-max, or other), making the exact mask computation ambiguous.

3. **Training/test set sizes unreported.** The paper states it uses "a subset from the Subject200K dataset" but provides no information about the number of training or test samples used.

4. **Baseline fine-tuning protocol unclear.** The paper reports fine-tuning FLUX.1 with LoRA but does not clarify whether OminiControl2 and UniCombine were used off-the-shelf or also fine-tuned under the same data and LoRA protocol. This affects the fairness interpretation of the comparison.

5. **F1 metric definition for Canny controllability not specified.** Table 1 reports F1 scores for edge conditions, but the paper does not define what constitutes a true/false positive in the edge detection context (e.g., thresholding protocol, edge detection algorithm used on generated images).

6. **KSA mask reuse schedule is underspecified.** Equation 3 computes a mask at step t, and the text states it is "reused" at step t+1. The paper does not clarify whether a new mask is computed at each step or the same mask persists across all subsequent steps, which affects both the actual computation saved and reproducibility.

### Trivial

None.

## Nice-to-Haves

- Provide FID/CLIP-I/DINOv2 curves for the early-timestep sampling variants to substantiate the convergence claim.
- Run the PAA/KSA ablations with the quality metrics from Table 1 to confirm no quality degradation at the component level.
- Clarify whether baselines were fine-tuned on the same data; if not, a discussion of why the comparison remains informative.
- Add error bars or confidence intervals to Table 1 (common practice, but useful given the non-standard FID range).
- Report the computational overhead of the mask generation step in KSA.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Abstract speedup phrasing nitpick*: The critic noted the abstract's "inference speedup" could be misread as end-to-end. The body clarifies this is attention-module speedup. This is a minor presentational point, not a substantive weakness.
- *FID value range discussion*: The critic noted FID values of 50–80 are "quite high" but acknowledged this may reflect task difficulty. This is an observation, not a criticism.
- *Future work motivation*: The critic noted the video generation future work is "not well-motivated." This is an opinion about scope, not a concrete weakness.
- *Model capacity caveat (LoRA fine-tuning cost)*: The critic suggest discussing whether fine-tuning is more expensive due to the sampling strategy. This is a reasonable suggestion but not a weakness of the current experiments.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add quality metrics (FID, CLIP-I, DINOv2) to the PAA and KSA ablation tables (Figures 9 and 10) so readers can directly compare the quality implications of each module.
2. Provide a quantitative comparison of the early-timestep sampling strategy—at minimum, a convergence plot (e.g., FID vs. training iterations) for μ=-0.5, μ=0, and μ=0.5.
3. Clarify the KSA mask computation schedule (computed once, recomputed every N steps, or recomputed every step) and, if the mask is reused for multiple steps, measure the mask overlap between consecutive steps to justify temporal consistency.
4. Specify the keyword extraction method, the "Norm" operation in Eq. 3, the dataset size, and the F1 thresholding protocol.

## Calibration Anchors

### Round 1 (bracketing)
**Initial bracket:** 4.0–6.0

| Path | Avg Score | Round | Comparison to Paper |
|------|-----------|-------|---------------------|
| `/home/wg25r/review_agent/human_reviews_2026/eD8IPvNoZB.md` (SLA) | 5.00 | R1 | Most similar conceptually (attention efficiency for DiTs). PKA has a more targeted problem (multi-condition) but weaker ablations. |
| `/home/wg25r/review_agent/human_reviews_2026/xXI2L62A8K.md` (CoReDiT) | 3.33 | R1 | Token pruning for DiTs. PKA has stronger efficiency results (10× vs. 1.33×) and better motivation. PKA is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/jUNmW3s45i.md` (DraftAttention) | 2.50 | R1 | Low-res attention guidance. PKA is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/t9Wx3W2B0x.md` (MixDiffusion) | 3.00 | R1 | Mixing uni-condition models. Different approach, PKA is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/idXIbOfm8d.md` (JET-Diff) | 2.50 | R1 | Irrelevant domain (DTI reconstruction). |
| `/home/wg25r/review_agent/human_reviews_2026/KtocialdxS.md` (LowDiff) | 2.67 | R1 | Low-res cascaded sampling. Irrelevant domain. |
| `/home/wg25r/review_agent/human_reviews_2026/92PM2kSzK1.md` | 3.60 | R1 | Diffusion dataset condensation. Different topic. |
| `/home/wg25r/review_agent/human_reviews_2026/ANKQqRicBM.md` (DiffMoE) | 5.33 | R1 | MoE for DiTs. Different approach, comparable score. |
| `/home/wg25r/review_agent/human_reviews_2026/FetaeuGsEs.md` (Semantic Bottleneck) | 4.50 | R1 | Analysis of conditional embeddings. Different contribution type. |
| `/home/wg25r/review_agent/human_reviews_2026/DDcrkBwzec.md` (ECM) | 4.50 | R1 | Efficient conditional generation for VAR. Different architecture. |

### Round 2 (narrowing)

| Path | Avg Score | Round | Comparison to Paper |
|------|-----------|-------|---------------------|
| `/home/wg25r/review_agent/human_reviews_2026/dwbrZtYP04.md` (SparseD) | 5.00 | R2 | Sparse attention for diffusion language models. Different domain, similar overall quality. PKA has stronger speedup numbers but weaker ablations. Roughly comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/V3eUas3VCL.md` (DiffSparse) | 4.50 | R2 | Learned token sparsity for DiTs. PKA is stronger: better efficiency results and more novel motivation. |
| `/home/wg25r/review_agent/human_reviews_2026/aTVollXaaI.md` (SPRINT) | 5.50 | R2 | Token dropping for DiT training. Different focus (training vs. inference efficiency). SPRINT has more comprehensive experiments. PKA is slightly weaker in experimental completeness. |
| `/home/wg25r/review_agent/human_reviews_2026/oQaRElUdmh.md` (VMoBA) | 5.50 | R2 | Mixture-of-block attention for video diffusion. Different domain. |
| `/home/wg25r/review_agent/human_reviews_2026/NLsUsrOIuh.md` (Compact Attention) | 4.50 | R2 | Structured sparsity for video diffusion. Different domain, rejected despite good scores. |
| `/home/wg25r/review_agent/human_reviews_2026/Xs7DhA88bd.md` | 4.00 | R2 | Diffusion for parallel token generation. Different topic. |

The round-1 bracket placed this paper between 4.0 and 6.0. Round 2 narrowed the comparison: PKA is clearly stronger than DiffSparse (4.50) and comparable to SLA (5.00) and SparseD (5.00), but weaker in experimental completeness than SPRINT (5.50). The paper's core contribution (condition-specific attention decomposition for multi-condition DiTs) is novel and well-motivated, and the efficiency results are strong. However, the missing quantitative metrics in ablations and the unvalidated early-timestep sampling prevent a higher score.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>