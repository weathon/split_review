- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8
Now I have all the information needed to write the consolidated review.

---

## Summary

This paper proposes L2C, a framework for few-shot test-time domain adaptation (FSTT-DA) that freezes CLIP and attaches a parallel network (CPNet) to learn dataset-specific visual knowledge via a revert-attention mechanism. It further enhances text features through a greedy prompt ensemble and lightweight refinement, and generates domain prompts that adapt both modalities toward a target domain. Experiments on DomainNet and four WILDS benchmarks show improvements over prior work, particularly with the smaller ViT-B/16 backbone (e.g., +5.1 F1 on iWildCam, +3.1% WC Acc on FMoW).

## Strengths

- **CPNet with revert attention yields large and consistent gains, especially on challenging WILDS benchmarks with smaller backbones.** The method improves over VDPG by +5.1 F1 on iWildCam and +3.1% WC Acc on FMoW using ViT-B/16 (Table 1). Ablations confirm CPNet alone adds +13.1 F1 on iWildCam and +13.8% WC Acc on FMoW over frozen CLIP (Table 3, Index 1 vs. 2).

- **The greedy text ensemble strategy demonstrably improves over standard average ensemble across all benchmarks.** Table 6 shows consistent gains, with larger improvements on the more challenging WILDS benchmarks compared to DomainNet, supporting the paper's motivation about text feature inter-dispersion.

- **Domain-aware fusion (DAF) with a K-V cache and batch-reshaping aggregation is well-ablated.** Tables 4 and 5 systematically show that both components of the domain prompt (queried source knowledge and current domain knowledge) are essential, and that the proposed batch reshaping outperforms simpler mean/max pooling.

- **Efficiency is a practical strength.** CPNet requires only 3 transformer blocks to complement a 12-layer ViT-B/16 on DomainNet, and the text encoder is discarded after preprocessing, keeping overhead minimal (Sec. 4.1, 4.2).

## Weaknesses

### Major

- **No statistical significance or variance reporting for any result.** All experiments report only point estimates. Gains as small as +0.3% (FMoW WC Acc with ViT-L/14) and +0.1% (Camelyon17 with ViT-B/16) cannot be distinguished from within-run variance without multiple seeds, confidence intervals, or error bars. This is especially consequential for the small-margin WILDS results and weakens the paper's comparative claims. The paper does not report multiple runs, standard deviations, or any uncertainty quantification (verified via grep: no occurrence of "standard deviation", "variance", "seeds", or "confidence" in the paper body).

- **The central claim about revert attention learning "complementary" information is unsupported.** The paper states that the revert-attention mechanism (A = 1 − softmax(CP·I)) "ensures CPNet is focused solely on learning information distinctive from CLIP." No empirical analysis is provided to substantiate this claim — e.g., measuring feature similarity, mutual information, or redundancy between CPNet and CLIP outputs. The mechanism is a plausible heuristic, but the paper presents it as a principled guarantee without evidence. The method may work well for other reasons (e.g., the parallel architecture alone), and the stated justification is not backed by data.

### Minor

- **Text-related components show small and inconsistent benefits in ablations.** Per Table 3, text refinement (Index 2→3) and the uniformity loss (Index 5→6) yield marginal improvements on some datasets and small degradations on others (e.g., the paper reports iWildCam F1 decreasing with some components). These fluctuations are within a range that could be noise. While the paper claims these components are beneficial, the evidence is thin and dataset-dependent, making the text pipeline's contribution less convincingly isolated from the larger gains from CPNet and DAF.

- **No discussion of limitations or failure cases.** The paper lacks a limitations section. The method's assumptions (e.g., requiring a support set of 16 unlabeled images per domain, the domain cache being fixed after training) and scenarios where it might struggle are not analyzed.

### Trivial

None.

## Nice-to-Haves

- Providing empirical analysis of what CPNet actually learns relative to CLIP (e.g., feature similarity or redundancy measurements) would directly strengthen the revert-attention motivation.
- Reporting results with at least 3 random seeds would increase confidence in the small-margin improvements.
- A brief discussion of when the method might fail (e.g., very small support sets, streaming one-by-one inference) would be a helpful addition.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing appendix content / pseudocode not present.** Removed because the parser strips images and supplementary sections from all papers; the original submission contains these.
- **Footnote about 0.01% cost not verifiable.** Same reason — appendix stripped by parser.
- **No comparison with prompt-based methods (CoOp, CoCoOp, DTL) in main paper.** The paper text (line 166) explicitly mentions this comparison exists; the results are likely in a table/figure stripped by parsing.
- **Softmax axis underspecified in Eq. 1.** Trivial implementation detail; removed per rule about nitpicks on reproducibility.
- **Greedy ensemble computational overhead.** Too minor a nitpick; the paper clearly describes it as a one-time preprocessing step.
- **"The number of transformer layers in CPNet is dataset-dependent and unspecified."** The paper discusses this in Fig. 4 and the surrounding text (lines 186–187), so this is partially addressed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add standard deviations or confidence intervals to all main results (Tables 1 and 2). Even a brief note showing that key results are stable across 3 runs would substantially increase confidence in the claimed improvements, especially for the small-margin WILDS gains.
- Provide a simple empirical analysis for the revert-attention claim: e.g., comparing cosine similarity between CLIP and CPNet output features with and without revert attention, or showing that removing CPNet increases feature redundancy with CLIP.
- Consider simplifying or downplaying the text pipeline components (text refinement, uniformity loss) if their marginal and inconsistent benefits do not justify the added complexity, or provide a clearer analysis of when they help versus hurt.
