- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes TabPTM, a pre-training framework for heterogeneous tabular datasets. The key idea is to transform instances from any dataset into a **meta-representation**: a fixed-dimensional vector of distances to K nearest neighbors (per class) and their labels. This meta-representation serves as a shared vocabulary across datasets with incompatible attribute and label spaces, enabling pre-training of a single shared MLP that can then be applied (directly or with fine-tuning) to new datasets. The paper validates on 72 datasets (36 classification + 36 regression) across multiple settings.

## Strengths

1. **Novel and well-motivated solution to a genuine problem**: The meta-representation approach is a creative way to handle the heterogeneity of tabular datasets. The paper clearly motivates why instance-level relationships can serve as a shareable vocabulary, drawing connections to multidimensional scaling and manifold learning. This is a distinct departure from existing approaches that rely on column-name semantics or dataset-specific tokenizers.

2. **Strong empirical scope and thorough ablation**: The paper validates on 72 datasets (18 seen + 18 downstream per task), which is a substantial benchmark. The ablation in **Table 3** is particularly effective: it cleanly isolates the contribution of pre-training by comparing TabPTM (pre-trained) against TabPTM_S (same MLP architecture trained from scratch on the meta-representation) and XGBoost_MR (XGBoost on the meta-representation). TabPTM outperforms both, directly confirming that pre-training encodes transferable knowledge beyond what the meta-representation alone provides.

3. **State-of-the-art or competitive results across benchmarks**: TabPTM achieves the **best average rank** across 18 classification datasets (Table 2) and strong RMSE results on regression (Table 1), outperforming or matching XGBoost, TabR, XTab, and TabPFN — including methods that do not require pre-training. This is a meaningful empirical contribution.

4. **Few-shot generalization evidence**: Figure 4 consistently shows TabPTM outperforming baselines across multiple shot sizes (5, 10, 20, 40) on multiple datasets, supporting the claim that pre-trained knowledge transfers well under data scarcity.

5. **Scalability advantage demonstrated**: Table 1 shows TabPTM runs successfully on datasets where TabR, XTab, and MLP hit OOM errors (HIP dataset), supporting the practical scalability claim vs. methods like TabPFN that require processing the entire training set for each test instance.

## Weaknesses

### Fatal
None.

### Major

1. **Efficiency claims are unsubstantiated with runtime measurements**: The paper's "Remark" section (end of §1) explicitly differentiates TabPTM from TabPFN on efficiency grounds — "more training-efficient," "more testing-efficient," and applicable to "much larger tabular datasets." However, no training time, inference time, or FLOPs measurements are reported anywhere in the paper. The OOM entries in Table 1 partially support the scalability claim, but they do not quantify efficiency. Since efficiency is a stated advantage in the paper's own narrative, the lack of any runtime evidence is a significant gap. *The paper should report pre-training wall-clock time, per-instance inference time on at least a few downstream datasets of varying size, and ideally compare with TabPFN on these metrics.*

### Minor

1. **No variance reporting on main results**: Tables 1 and 2 report averages over 10 random seeds without standard deviations, confidence intervals, or statistical significance tests. While the paper reports average rank across many datasets (which mitigates over-reliance on any single comparison), the reader cannot assess whether individual margins are reliable. **Figure 4** (few-shot) also lacks error bars. For a paper whose headline claim rests on "best average rank," some form of uncertainty quantification (std dev, pairwise significance tests) is needed for reproducibility and reader confidence.

2. **No direct KNN baseline**: The meta-representation is fundamentally built from nearest neighbors, yet the paper does not include a standard KNN classifier (with tuned K and the same MI-weighted distance metric) as a baseline on downstream datasets. Table 3 compares XGBoost_MR and TabPTM_S, but a tuned KNN on original features would be the most natural baseline to assess what the learned MLP adds beyond what a simpler neighborhood-based predictor already achieves.

3. **No discussion of handling categorical attributes or missing values**: The distance metric (Eq. 7-8) uses Minkowski-style distances with mutual-information weighting. Many real-world tabular datasets contain categorical features (which require special distance treatment) or missing entries. The paper should clarify how these cases are handled in the preprocessing and distance computation pipeline. Without this, reproducibility is diminished.

4. **Overclaiming in framing**: The abstract states "state-of-the-art accuracy in many datasets after fine-tuning" — the evidence supports "best average rank" across datasets, not necessarily SOTA on individual ones. Table 2 shows XGBoost or XTab winning on several individual datasets. The conclusion more appropriately says "competitive performance." The framing in the abstract and introduction should be calibrated to match what the evidence shows (best on average, competitive individually), which is already a strong claim.

### Trivial

- The notation in **Eq. 9** (general function T_Θ taking concatenated meta-representations) vs. **Eq. 10** (per-class MLP implementation) caused confusion for at least one reader. The intent — T_Θ is a general transformation, implemented as applying the same MLP independently to each φ_c — is clear from the text ("we implement T with MLP, i.e., [Eq 10]"), but the notation could be tightened to avoid misinterpretation.
- The few-shot study (Figure 4) covers only 4 datasets; a summary across all 18 downstream datasets would strengthen the claim.

## Nice-to-Haves

- Sensitivity analysis of K (number of neighbors). The paper uses K=128 for classification and K=16 for regression by default; showing how performance varies with K would be informative.
- Quantitative validation of the pilot study (Figure 3), e.g., silhouette score or average intra- vs. inter-class distance in meta-representation space, beyond the qualitative visualization.
- Evaluation on a dataset from a domain completely absent from the pre-training set to test the limits of generalization.
- Wilcoxon signed-rank test or similar pairwise comparison between TabPTM and the strongest baseline on each task.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Inconsistency in Equations 9 vs. 10 (critical/fatal)"** — This is not a genuine inconsistency. Eq. 9 defines T_Θ as a general function producing a score vector; Eq. 10 specifies the implementation as applying the same MLP to each φ_c independently. The paper says "we implement T with MLP, i.e., [Eq 10]". This is standard mathematical writing (general form → specific implementation). The critic's concern about variable C handling is addressed by the per-class application pattern. At worst a minor clarity issue, not a structural problem.

- **"Cannot be reproduced or understood as written"** — The method is clearly described: compute distances from each instance to K nearest neighbors per class, concatenate distances and neighbor labels into a fixed-dimensional meta-representation, then apply a shared MLP per class. The forward pass is unambiguous.

- **"Few-shot padding strategy is a heuristic whose impact is not evaluated"** — This is a standard and well-known technique (padding with the maximum distance). The paper explicitly describes it and cites prior work. It is not a weakness worth elevating.

- **"No discussion of limitations in the conclusion"** — While true, this is a generic critique. The paper's conclusion is short but appropriate for a 6-page conference submission.

- **"Connection to multidimensional scaling is stated rather than argued"** — The connection is a motivation, not a formal claim. The paper provides sufficient intuition for a conference paper.

- **"The paper does not release the dataset split"** — The paper includes an anonymous code link. Dataset splits are a reasonable reproducibility expectation but are standard to include with code release, not a paper weakness per se.

## Novel Insights

None beyond the paper's own contributions. The reviewer comments do not surface any observation about the method or results that the paper itself does not already state or imply.

## Suggestions

1. Add standard deviations to Tables 1-2 and error bars to Figure 4. Report pairwise Wilcoxon signed-rank tests between TabPTM and the strongest baseline on each task.
2. Report pre-training wall-clock time and per-instance inference time on at least 3 downstream datasets of varying size (e.g., 500, 5k, 50k instances) to substantiate the efficiency claims.
3. Add a tuned KNN baseline (with the same MI-weighted distance) on downstream datasets.
4. Clarify how categorical features and missing values are handled in the distance computation (Eq. 7-8).
5. Calibrate abstract / introduction claims from "state-of-the-art in many datasets" to "best average rank across datasets."
