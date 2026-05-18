I now have a thorough understanding of the paper. Let me construct the final consolidated review, carefully verifying each claim against the paper.

---

## Summary

This paper proposes a computational framework for data-driven gene-gene interaction (GGI) discovery from single-cell transcriptomic data. The framework consists of (1) CelluFormer, a Transformer trained to classify Alzheimer's vs. non-Alzheimer's cells; (2) a two-pass randomized algorithm (WDS) that estimates each cell's minmax kernel density via 0-bit consistent weighted sampling, producing an inverse-minmax-density (IMD) score for diversity-aware sampling; and (3) a weighted estimator that aggregates attention maps from sampled cells to rank gene-gene interactions. The central claim is that sampling just 1% of cells with WDS achieves performance comparable to the full dataset, dramatically improving data efficiency.

## Strengths

1. **Novel two-pass randomized algorithm for minmax kernel density estimation.** Algorithm 1 estimates each cell's minmax density in O(n·nnz(X)) time and O(RB) memory (constant w.r.t. dataset size). Theorem 1 (informal) shows the estimate is unbiased for the minmax density, providing a principled foundation. The connection between 0-bit CWS hash collision probability and minmax similarity is well exploited.

2. **Clear and consistent empirical advantage of WDS over uniform sampling.** Across 6 cell types and 4 sample sizes (1%–10%), WDS achieves higher mean NES and lower MSE than uniform sampling in 23 out of 24 comparisons (Table: Sampling_Res). For example, L6_CT at 1%: WDS NES=1.19 vs. uniform NES=0.85, MSE 0.0000 vs. 0.0207. The improvement is large and consistent, not marginal.

3. **Superiority of the Transformer-based GGI framework over statistical baselines.** CelluFormer achieves the highest NES on 5 of 8 datasets in Table 2 (RQ1), outperforming Pearson, Spearman, CS-CORE, and NID. This validates that attention maps from the proposed model carry meaningful interaction signal.

4. **Formal theoretical grounding.** The paper defines the minmax kernel density, links it to CWS hashing via collision probabilities, and derives an unbiased estimator. This goes beyond heuristic sampling and provides a clear motivation for why IMD-weighted sampling should select diverse cells.

## Weaknesses

### Fatal
None.

### Major

1. **Only uniform sampling as a baseline for the sampling experiments (RQ2/RQ3).** The paper justifies this by saying other methods require "preprocessing time exponential to the dataset size," but there exist many linear-time diversity sampling methods (e.g., k-medoids on gene expression, farthest-point sampling, stratified sampling by cell type or expression level, sampling by distance from centroid). Without comparing against at least one such method, it is impossible to tell whether the improvement comes from the specific minmax diversity notion or simply from non-uniform sampling. This is the most significant gap in the experimental design.

2. **No standard deviations, confidence intervals, or statistical significance tests for the NES values in the sampling experiments.** The paper reports mean NES over 5 runs but does not report standard deviations or run any significance test (e.g., paired t-test, Wilcoxon) between WDS and uniform. Since many NES differences are modest (e.g., L5_ET at 1%: 0.95 vs. 0.90), the reader cannot assess whether these differences are statistically reliable. This is a critical omission for a claim that the method outperforms the baseline.

### Minor

3. **The "1% sampling" claim is overstated for some cell types.** At 1% sampling, WDS NES diverges noticeably from the full-dataset NES for L5_ET (0.95 vs. 1.15) and Pax6 (1.08 vs. 1.25). While the method performs very well at 1% for L6_CT, L6b, and L6_IT_Car3, the abstract's blanket claim ("by sampling a mere 1%... we achieve performance comparable to that of utilizing the entire dataset") should be qualified. At 2% sampling, WDS matches full-data performance across all cell types, so the claim is defensible at 2%.

4. **The connection between minmax gene-expression diversity and attention-map diversity is asserted without evidence.** The paper's logic is: diverse gene-expression profiles → diverse attention maps → better interaction recovery. This is reasonable as a heuristic, but the paper does not directly verify it (e.g., by computing pairwise attention-map similarity across cells selected by WDS vs. uniform sampling and showing WDS selects more diverse attention maps). This would strengthen the causal chain.

5. **The interaction score estimator (Definition 7) has unaddressed statistical complexities.** The estimator uses weights I(x) that are themselves estimated from data (via Algorithm 1), not known a priori. This introduces an additional layer of variance not accounted for. Furthermore, the variance formula is presented for sampling with replacement, but the paper specifies sampling without replacement. These issues do not invalidate the method (the practical results speak for themselves) but the theoretical framing overstates the statistical guarantees.

6. **Model architecture details are missing.** The paper does not state the number of layers, attention heads, hidden dimensions, embedding size, optimizer, learning rate, or training time for CelluFormer. Similarly, the fine-tuning procedure for scGPT and scFoundation is described only as "fine-tuned to classify whether a cell is AD or non-AD" without specifics. This limits reproducibility.

7. **No empirical runtime or memory measurements.** The paper claims efficiency (two passes, constant memory) but does not report wall-clock times or peak memory usage for the WDS preprocessing step vs. alternatives. This would substantiate a core claimed advantage.

8. **Hyperparameters R and B not reported.** The paper states R = O(log|X|) following theoretical analysis but does not give the actual values used in experiments. This is important for reproducibility.

9. **The multi-cell-type training comparison (Table 1) is confounded.** The paper shows CelluFormer (all types, F1=98.12) vs. MLP (individual types, F1=62–95). The statement that "we do not see this gap when we perform training of CelluFormer on a single cell type" is mentioned in text but not shown with numbers. A proper ablation would compare CelluFormer trained on single types vs. all types.

10. **Absolute NES values are modest.** Many NES values are near 1.0–1.2, indicating relatively weak enrichment. For instance, CelluFormer's NES on all neuron data is 1.17, and CS-CORE's is 1.06. The paper does not discuss whether these values correspond to biologically meaningful signal strength.

### Trivial
None.

## Nice-to-Haves
- An analysis of how the quality (classification accuracy) of CelluFormer affects the reliability of the interaction scores.
- A discussion of how to choose R and B beyond the asymptotic statement.
- An investigation into whether smaller sampled subsets sometimes outperforming larger ones (as noted by the authors) can be explained by noise reduction effects.
- Direct validation that cells with high IMD indeed have more diverse attention maps, e.g., by computing pairwise attention-map cosine similarities.

## Removed Points
- **"The variance formula in Definition 7 is dimensionally inconsistent / lacks a 1/|X_s| factor"** — This is factually incorrect. For equal weights, the formula simplifies to Var/k, which has the correct sample-size scaling. The formula is dimensionally consistent.
- **"The theoretical framing is essentially a count-min sketch"** — The paper cites prior work on hash-based KDE and explicitly frames its contribution as an application to single-cell attention aggregation. This is a descriptive observation, not a weakness.
- **"The paper would benefit from acknowledging the prior work it cites more explicitly"** — The related work section (Section 5) already discusses hash-based KDE and LSH methods and clearly differentiates the paper's contribution on weighted (minmax) similarity.

## Novel Insights
The two reviews surface a tension that is broader than this paper: when a method relies on an indirect theoretical connection (here, minmax diversity in expression space → diversity in attention maps), the experimental design must do extra work to validate that link. The harsh critic correctly identifies that the paper skips this step, while the strength finder correctly notes the paper provides formal guarantees on the density estimation itself. The missing piece is an experiment that directly connects the two — e.g., showing that WDS-sampled cells indeed yield lower redundancy in accumulated attention maps. This is a pattern common in ML-for-science papers where the target quantity (interaction scores) is several steps removed from the sampling criterion.

## Suggestions
1. **Add at least one alternative diversity-aware sampling baseline** (e.g., k-medoids sampling on gene expression vectors, or stratified sampling by cell type). This is the single highest-leverage improvement and would distinguish whether the minmax kernel or simply non-uniform sampling drives the gains.
2. **Report standard deviations or bootstrapped confidence intervals** for the NES values across the 5 runs, and run a paired significance test between WDS and uniform.
3. **Temper the "1%" claim** to reflect the actual results — e.g., "sampling 1–2% of cells with WDS achieves NES scores within 0.05–0.10 of the full dataset for most cell types, and within 0.01 for several."
4. **Report actual values of R and B** used in experiments, and include a brief sensitivity analysis.
5. **Provide architecture details** for CelluFormer and fine-tuning details for the foundation model baselines.
6. **Include wall-clock runtime and memory measurements** for the WDS preprocessing step to substantiate efficiency claims.
7. **Either correct the variance formula** to account for sampling without replacement, or reframe it as approximate and acknowledge the added complexity from estimated weights.

## Score and Decision

**Originality:** The combination of CWS-based minmax kernel density estimation with IMD-weighted sampling for attention-based GGI is genuinely novel. **Importance:** The problem of efficient data-driven GGI discovery on massive single-cell datasets is timely and relevant. **Claims support:** The central claim (WDS > uniform) is well supported; the headline "1% comparable" claim is partially supported but overstated. **Soundness:** The algorithm is theoretically grounded, but the experimental evaluation has a significant gap (single baseline) and lacks statistical rigor. **Clarity:** Generally well-written and clear. **Value:** The WDS method and the overall framework have practical utility for the single-cell community.

The paper has a clear contribution and demonstrates meaningful empirical improvements over the de facto default (uniform sampling). However, the experimental evaluation is significantly weakened by having only one baseline for the sampling experiments and by lacking statistical significance testing. These are addressable in a revision but limit confidence in the paper's claims as presented.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>