I now have all the information needed to write the final consolidated review.

## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that enriches the standard attention-weighted first-order representation (ABMIL) with second-order statistics (covariance matrix) and DBSCAN-based adaptive clustering. The key idea is to capture inter-feature variability and correlations across patches, which is missed by mean-based aggregation alone. DBSCAN groups similar patches into variable-size clusters (coarse for abundant normal tissue, fine for rare pathology), reducing computation while preserving diagnostic information.

## Strengths

1. **Principled statistical framing and clean motivation.** The paper explicitly frames ABMIL as a first-order moment estimator (Section 3.1) and motivates second-order statistics as a natural extension to capture feature variability — a conceptually clear and well-articulated contribution. The ablation in Table 3 confirms that adding second-order moments yields consistent gains (ACC +1.00%, F1 +1.60% on CAMELYON16 with clustering held constant).

2. **State-of-the-art performance on two benchmarks with dramatic computational savings.** On CAMELYON16, HOMIL achieves the best ACC (96.98%), AUC (99.23%), and F1 (96.54%) across ten methods while being 17× faster than TransMIL and 23× faster than MambaMIL. On TCGA-NSCLC, it also leads all metrics (ACC 93.24%, AUC 97.41%, F1 92.93%). These results are supported by the unified codebase and consistent 5-fold cross-validation setup.

3. **Computational efficiency from adaptive clustering is validated.** The ablation shows the "w/o CM" variant (no clustering) takes 530s vs 310s for the full model, while also performing worse (ACC 95.72% vs 96.98%). This demonstrates DBSCAN's dual benefit of reducing computation and improving representation quality by grouping redundant patches.

4. **Ablation isolates both components.** Table 3 cleanly separates the effect of clustering (Full vs w/o CM) and second-order moments (Full vs w/o SOM), showing consistent ~1% ACC improvements from each.

## Weaknesses

### Fatal
None.

### Major

1. **Covariance vectorization via 1-D convolution is insufficiently justified.** The core technical device that compresses the d×d covariance matrix to a d-dimensional vector (Section 4.3.3) uses row-wise 1-D convolution (kernel size m=64, T=4 kernels) followed by max-pooling. The paper provides no rationale for this particular design, no ablation comparing it to alternatives (e.g., flattening the upper triangle with a learned projection, using eigenvalues/trace, or a bilinear form), and no sensitivity analysis on the kernel parameters. The paper simply states "To align dimensions with the first-order representation" — but many compression strategies exist, and this specific one is never defended. Given that this is a central component that differentiates the method from prior work, this gap undermines the claim that the framework is principled rather than ad hoc.

2. **Reported improvements are small with no statistical significance testing.** Across both datasets, HOMIL's gains over the strongest baselines are modest, and error bars overlap in several comparisons:
   - CAMELYON16: HOMIL ACC 96.98±2.43 vs MambaMIL 96.48±1.37 
   - TCGA-NSCLC: HOMIL ACC 93.24±2.47 vs HMIL 92.89±1.45, AUC 97.41±1.24 vs Mean Pooling 96.85±0.87
   - No paired significance tests (DeLong for AUC, McNemar for ACC, bootstrapped CIs) are reported. With overlapping standard errors, it is impossible to assess whether the observed differences reflect real improvements or fold-split noise. Given the added complexity of covariance computation and clustering, the paper should quantitatively demonstrate that the gains are statistically robust.

### Minor

3. **Covariance computation is not attention-weighted.** The covariance matrix (Eq. 4) is computed as an unweighted sum Σₖ g̃ₖ g̃ₖᵀ, while the first-order mean v⁽¹⁾ used for centering is attention-weighted. This design choice is defensible (unweighted covariance captures overall variability), but it is inconsistent with the paper's framing of "attention-weighted" second-order statistics and is never discussed.

4. **DBSCAN parameters (65th percentile for ε, minPts=4) are stated without empirical justification.** The paper claims these are robust via an appendix sensitivity analysis, but the main paper only reports "stable performance as long as compression rate > 5%." Given that the paper emphasizes adaptive clustering as a key contribution, an ablation varying these parameters (or at least a summary figure) should be in the main text.

5. **No qualitative analysis.** The paper does not visualize cluster assignments, attention maps, or how the covariance captures pathology-relevant structure. Such visualizations would significantly strengthen the claim that adaptive clustering preserves diagnostic information and that second-order statistics capture meaningful feature correlations.

6. **No discussion of limitations.** The paper does not discuss failure cases, scenarios where second-order moments might not help, or sensitivity to extreme compression scenarios (e.g., very few clusters). This omission weakens the paper's stance as presenting a practical method.

### Trivial
None.

## Nice-to-Haves
- A comparison of the covariance vectorization against simpler alternatives (e.g., trace, eigenvalues, flattened upper triangle with MLP) would be illuminating.
- A breakdown of computational time (PCA vs. DBSCAN vs. first-order vs. second-order vs. classifier) would clarify the source of the speed advantage.

## Removed Points
The following points raised by reviewers are removed with justification:

- **"Ablation does not isolate second-order moments":** This is factually incorrect. The ablation (Table 3) directly compares Full model (clusters + both moments) vs w/o SOM (clusters + first-order only), which isolates the contribution of second-order moments while holding clustering constant. Both variants operate on cluster-level features. The reviewer's proposed four conditions are all already present in Table 3. **REMOVED** — factually wrong.

- **"Missing prior work on covariance for WSI/MIL":** Per policy, I do not evaluate missing citations as I cannot verify their existence. **REMOVED** — per instruction.

- **"Code not released" / reproducibility concerns about unreleased artifacts:** The paper's appendix (stripped by parser) may contain code/artifact information. **REMOVED** — per instruction.

- **"Sensitivity analysis should be in main paper not appendix":** The appendix was stripped by the parser. **REMOVED** — per instruction on parser-stripped appendices.

- **"No mention of limitations":** Kept as a minor weakness — this is a fair observation about the paper's own framing, not about missing appendix content. The paper genuinely does not include a limitations paragraph.

- **"Fusion weights interpretation is post-hoc":** Kept as a minor observation — it's valid but not a significant weakness.

- Various formatting/typo concerns, speculation-driven criticisms, and generic area-of-concern sweeps: **REMOVED** per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any genuinely novel observation about the paper that the paper itself does not articulate.

## Suggestions
1. **Justify the covariance vectorization.** Provide an ablation comparing the current 1-D conv + max-pooling approach against at least one alternative: flatten + linear projection, trace, eigenvalue summary, or a learnable bilinear pooling step. Without this, the compression procedure appears ad hoc.
2. **Add statistical significance tests.** Report paired bootstrapped CIs or p-values (e.g., DeLong's test for AUC, McNemar's for ACC) comparing HOMIL against the strongest baseline on each dataset. This is essential given the small margins and overlapping error bars.
3. **Add qualitative results.** Show example cluster assignments on actual WSIs (e.g., coarse clusters on normal tissue, fine clusters on tumor regions) and attention heatmaps. This would substantially strengthen the paper's claims about adaptive granularity.
4. **Include a limitations paragraph.** Discuss failure modes, sensitivity to extreme DBSCAN parameter settings, and scenarios where second-order moments provide little benefit.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison to HOMIL |
|------|-----------|---------------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/MOCEoNsjEx.md (Pg-GAT) | 3.00 | Weaker — insufficient novelty and uncompetitive results. HOMIL has a clearer contribution and stronger empirical results. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/0yVP49SDg0.md (Mamba-HMIL) | 3.25 | Weaker — poorly motivated components, limited novelty. HOMIL's motivation from statistical moments is stronger. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/lo9HMoGNwQ.md (SMIL) | 4.50 | Comparable — both have incremental contributions with modest improvements. HOMIL has clearer ablation but SMIL tested on more datasets. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/6xrDPHhwD3.md (MFC) | 6.00 | Comparable — both propose MIL extensions with modest empirical gains. MFC has a more complex pipeline; HOMIL is conceptually cleaner. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/q1t0Lmvhty.md (Covariance Pooling) | 6.00 | Stronger — provides rigorous theoretical treatment of second-order features, unlike HOMIL's heuristic vectorization. |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>