- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the final consolidated review.

---

## Summary

This paper investigates the scaling properties of image classifiers and finds that larger models primarily help with low-confidence ("hard") samples. Based on this observation, the authors propose a simple two-pass inference scheme called Little-Big: a lightweight model processes all samples, and only those with low confidence are forwarded to a larger model. The method is model-agnostic, requires no retraining or architectural modification, and achieves reported MACs reductions of 62–81% while broadly maintaining accuracy across CNNs, ViTs, and hybrid models on ImageNet-1K. The contribution is primarily empirical—demonstrating that confidence-based cascading, a classic idea, works surprisingly well on modern large vision models.

## Strengths

1. **Large and consistent MACs reductions across diverse model families**: The paper reports 81% MACs reduction for EfficientNet-B7-600, 76% for EfficientViT-L3-384, 71% for DeiT3-L-384, and 62% for the 3B-parameter InternImage-G-512, all while maintaining top-1 accuracy (Abstract, Section 4.3, Table 1). These results span CNNs, transformers, and hybrid models, supporting the claim of model agnosticism.

2. **Empirical justification that scaled-up models preferentially help low-confidence samples**: Section 3 decomposes mistakes by the Little model into correctable vs. non-correctable by the Big model. For EfficientNet-B0+B7, B2+B7, B4+B7 pairs, 90% of correctable mistakes fall below confidence thresholds of 0.65, 0.67, and 0.47, directly motivating the two-pass routing algorithm (Figure 3). This analysis is clean and reproducible.

3. **Principled threshold selection with generalization validation**: Section 4.2 describes a simple procedure to select the optimal threshold by setting a tolerable accuracy loss ΔAcc and finding the leftmost intersection on the accuracy-MACs curve. The optimal threshold found on ImageNet-1K generalizes to ImageNet-ReaL and ImageNet-V2 with only 0.04% and 0.07% accuracy loss, and the paper further validates robustness by picking the threshold on V2 (10k samples) and testing on ImageNet-1K. This is a practical, reproducible protocol.

4. **Honest discussion of limitations**: Section 5 acknowledges storage overhead, memory/latency trade-offs, and the fact that speedup depends on the data distribution. The paper also sketches principled extensions to video classification and semantic segmentation, showing the framework is not confined to image classification.

## Weaknesses

### Fatal
None.

### Major

1. **Missing the most informative baseline: a single static model at matched average MACs.** The paper never directly answers the question: *does Little-Big outperform simply picking a smaller static model whose average MACs matches that of the two-pass system?* For example, if a B4+B7 pair achieves 81% MACs reduction while retaining B7's accuracy, then a single model at ~7 GMACs (e.g., B4) should be compared directly. The paper has the individual model accuracy data (Table 1 shows scaling trends) and could construct this comparison without any additional experiments. Without it, the reader cannot distinguish between genuine adaptive-compute benefits and the trivial advantage of having higher effective capacity on hard samples. This is the paper's central practical claim, yet it is not explicitly tested. The paper's argument in Section 4.4 (comparison table) focuses on pruning methods and makes only qualitative claims about adaptive methods, missing the simplest competitor.

2. **No quantitative comparison with adaptive compute baselines.** DynamicViT and A-ViT are discussed in Related Work (Section 2.3) and in the Discussion (Section 5), where the paper asserts they "fail to match the performance of better trained baseline models." However, they are absent from the main comparison table (Table 2). A proper comparison — even using published results from those papers on comparable model families, or a simple re-evaluation — is needed to substantiate the claim that Little-Big offers a better accuracy-MACs trade-off than learned adaptive computation. The paper's dismissal of these methods without quantitative evidence is a significant evidential gap.

3. **No wall-clock latency measurements.** The paper's title promises "Speeding Up" and the central quantity reported is MACs reduction. While MACs are a standard proxy, real-world speedup depends on memory bandwidth, kernel launch overhead, batch size, and the overhead of running two models. The paper acknowledges the latency-vs-memory trade-off in the Limitations paragraph (Section 5) but provides no empirical latency numbers. For a practical deployment paper, this is a notable omission.

### Minor

1. **Hardness analysis (Section 3) is demonstrated only on EfficientNet.** The confidence-decomposition analysis that motivates the method is carried out exclusively on the EfficientNet family (B0/B2/B4 → B7). While the subsequent MACs results include ViTs and hybrid models, the core motivational analysis does not verify that the same pattern holds for non-CNN families. The paper would be stronger with a complementary analysis for, say, a DeiT3 pair.

2. **"Lossless" claim has a small but real accuracy drop on shifted distributions.** The paper selects the threshold to achieve ΔAcc ≥ 0 on ImageNet-1K, but on ImageNet-V2 the optimal pair loses 0.07% accuracy (Section 4.2). While this is negligible for most practical purposes, it technically violates the strict "lossless" framing. The paper would benefit from testing a more challenging distribution shift (e.g., ImageNet-C, ImageNet-R, or a domain like iNaturalist) to characterize the method's robustness boundaries — or from framing the claim as "near-lossless."

3. **Storage overhead is stated but not quantified.** The Limitations paragraph says "the storage overhead is usually a small fraction of the storage requirement of the Big model" without providing concrete numbers (e.g., "DeiT3-L-384 has 304M params, and the Little model adds 26M, an 8.5% overhead"). Providing these numbers for each pair in Table 1 would help readers assess the practical storage trade-off.

### Trivial
None.

## Nice-to-Haves
- The comparison against pruning methods in Table 2 would be more informative if pruning were applied to the same modern baselines (e.g., DeiT3) rather than to older architectures. Currently, the comparison conflates baseline strength with compression effectiveness.
- A latency benchmark on a modern GPU (e.g., A100) at a few batch sizes would directly support the "speeding up" claim.
- Measuring calibration (confidence–accuracy alignment) for each Little model used in the main results would verify that the routing principle generalizes.

## Removed Points

The following points from the inputs were removed with brief justification:

- *"Section 4.3 Table 1 is not fully visible in the extracted text"* — Parser artifact; not an author error.
- *"The comparison with pruning methods conflates architecture improvements with compression effectiveness"* — The paper's argument is that the best way to get a strong accuracy-MACs trade-off is to use a well-trained modern baseline, and that Little-Big can then speed that baseline up further. This is a reasonable position. The pruning vs. modern-baseline comparison is presented as context, not as a direct apples-to-apples ablation.
- *"The argument that SPViT with distillation failed to outperform DeiT3-S is irrelevant"* — The paper's point is that pruning methods applied to older architectures don't match simply using a better-trained modern model at comparable cost, establishing that the Little-Big starting point (modern baselines) is already stronger. This argument has merit even if a direct pruning-of-modern-model comparison would also be useful.
- *"The paper overstates the distinction from early-exit methods"* — The Discussion (Section 5) explicitly contrasts Little-Big with early exits on the key dimension (separate models vs. integrated exits), which is a genuine architectural distinction.
- *"Memory overhead workaround incurs latency from I/O"* — The paper explicitly acknowledges this trade-off ("keeps both...in memory...to minimize latency"), so this is already addressed.
- *Several generic strength finder claims* (e.g., "this paper addressed an important problem," "the paper is well-written") — removed as generic or sycophantic.
- *Claim about V2 being too small (10k) for generalization testing* — The paper also tests the reverse (picking threshold on V2, testing on ImageNet-1K with 50k samples), which is a stronger generalization test. The criticism is not well-founded.

## Novel Insights

None beyond the paper's own contributions. The key observation — that scaled-up models preferentially help low-confidence samples and that a simple confidence-thresholded cascade exploits this — is the paper's central insight and is well-supported. No reviewer uncovered a novel angle beyond this.

## Suggestions
1. **Add the matched-static-model comparison.** For each Little-Big pair in Table 1, find the smallest single model in the same family whose average MACs matches the Little-Big pair's average MACs, and report its accuracy in a new column. This is the single most important addition.
2. **Add quantitative comparisons with adaptive-compute methods.** Include published results from A-ViT and DynamicViT in Table 2 (or a new table), using the same base model families where possible.
3. **Add latency measurements.** Report wall-clock time for the Big model alone, the Little model alone, and the optimal Little-Big pair at batch sizes 1, 32, and 128 on a modern GPU.
4. **Extend the hardness analysis to at least one ViT family** (e.g., DeiT3-S→DeiT3-L) to confirm the confidence–correctability pattern holds beyond CNNs.
5. **Quantify storage overhead** for each pair in Table 1 (e.g., parameter counts and overhead percentage).
