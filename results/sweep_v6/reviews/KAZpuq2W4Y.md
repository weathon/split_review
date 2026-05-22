## Summary

This paper proposes HOMIL (Higher-Order Multi-Instance Learning), a framework for whole-slide image classification that augments standard attention-based MIL (ABMIL) with second-order moments (a covariance matrix computed over cluster features) to capture feature variability beyond the mean. It further employs DBSCAN-based adaptive clustering to group locally similar patches, reducing computational cost while preserving diagnostic signal. Experiments on CAMELYON16 and TCGA-NSCLC show modest accuracy improvements over strong baselines, and ablation studies confirm that both the second-order module and clustering contribute to performance.

## Strengths

- **Well-motivated integration of second-order moments into MIL.** The idea that ABMIL is effectively computing a first-order moment, and that covariance information captures complementary feature variability, is clearly reasoned (Section 3.2). The ablation study (Table 3) directly measures the contribution of second-order moments: removing them drops ACC by 1.00% (96.98 → 95.98) and AUC by 0.72%, confirming they add value beyond first-order aggregation.

- **Adaptive DBSCAN clustering is a practical and well-justified design.** The paper convincingly argues that density-based clustering naturally aligns with WSI pathology (large clusters for abundant normal tissue, small clusters for rare regions). The ablation shows removing clustering increases runtime by 71% (310→530s) while also hurting accuracy (ACC −1.26%), demonstrating that clustering contributes to both efficiency and performance.

- **Consistent improvements across two standard WSI benchmarks.** HOMIL achieves the best ACC, AUC, and F1 on both CAMELYON16 (96.98%, 99.23%, 96.54%) and TCGA-NSCLC (93.24%, 97.41%, 92.93%) against nine strong baselines, including ABMIL, CLAM, TransMIL, MambaMIL, and HMIL, under a unified codebase and patient-level 5-fold cross-validation.

- **Computational efficiency advantage for practical deployment.** On CAMELYON16, HOMIL's total 5-fold runtime (310s) is lower than ABMIL (455s) and dramatically lower than TransMIL (5175s), MambaMIL (7200s), and HMIL (10800s), while achieving the best accuracy — a practically relevant combination.

## Weaknesses

### Fatal
None.

### Major

1. **Improvements over strong baselines are modest with overlapping standard errors, and no statistical significance is reported.** On CAMELYON16, HOMIL ACC is 96.98±2.43 vs. ABMIL 94.72±2.18 and MambaMIL 96.48±1.37; on TCGA-NSCLC, HOMIL ACC is 93.24±2.47 vs. HMIL 92.89±1.45. Standard errors overlap substantially across nearly every comparison, and the paper reports no paired significance tests (e.g., McNemar, paired t-test). The text claims "significantly improves state-of-the-art" (Abstract) but the evidence does not establish statistical significance — the gains are consistent in sign but small in magnitude. Since the paper's central contribution is improved classification performance, this gap weakens the headline claim.

2. **Missing critical baselines that would isolate the contribution of second-order moments.** The paper does not compare against any simple second-order/covariance-pooling baseline — e.g., appending per-feature variance or the diagonal of the covariance matrix to the ABMIL representation, bilinear pooling on patch features, or a method that flattens the covariance matrix and projects it via an MLP. Without such comparisons, the reader cannot tell whether the improvement comes from the specific second-order formulation (clustering + Conv1D vectorization + fusion) or simply from having more feature dimensions. Relatedly, there is no comparison to existing covariance pooling approaches from the broader vision literature (e.g., DeepO2P, bilinear CNNs, GCP).

3. **The paper overclaims on "attention-weighted covariance matrix" — the term is imprecisely used.** The paper states repeatedly (Section 4.1, Section 4.3.3) that the second-order aggregation computes an "attention-weighted covariance matrix." However, the actual formula (line 156) is an unweighted sum: $\mathbf{C} = \sum_{k=1}^K \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top$, with no attention weight $a_k$ multiplying each outer product. The centering term $\mathbf{v}^{(1)}$ *is* attention-weighted, which makes the covariance centered by an attention-weighted mean — a meaningful but more modest modification. Calling it "attention-weighted covariance" without qualification is imprecise and may mislead readers about the nature of the innovation.

### Minor

1. **The covariance vectorization via 1D convolutions is introduced without justification or comparison to alternatives.** Section 4.3.3 compresses the $d\times d$ covariance matrix to a $d$-vector via row-wise 1D convolutions with multiple kernels and nested max-pooling, but the paper gives no rationale for this specific architecture. Why 1D convolutions rather than flattening+projection, bilinear pooling, or spectral decomposition? The ablation only removes the entire second-order module, so the vectorization design is never isolated or validated. It is plausibly an information bottleneck rather than an enrichment.

2. **No comparison to second-order or covariance-based methods from the MIL/pathology literature.** While the paper positions itself as introducing second-order moments to MIL, it does not discuss or compare against any prior work on covariance pooling in MIL or set-learning contexts. This weakens the novelty claim: the contribution may be the application of second-order moments to WSI-MIL specifically, but this should be clearly scoped and the unique challenges addressed.

3. **The fusion weight analysis (Figure 2b) suggests first-order dominates, raising questions about second-order's importance.** The fusion weight $\alpha^{(1)}$ stabilizes around 0.6 while $\alpha^{(2)}$ settles around 0.4. While the paper correctly notes this indicates second-order still contributes, the analysis is from a single run and does not examine whether simpler alternatives (e.g., fixed equal weighting) perform similarly.

### Trivial

- The figure description (Figure 1 caption) mentions Conv1D applied to instance features ($n \times d$) before clustering, while the text (Section 4.3) describes processing cluster features ($K \times d$) — this inconsistency between the caption and text should be harmonized.
- The paper reports standard errors (SE) but does not clarify whether these are computed over the 5 folds of CV; some readers may expect standard deviations. Clarifying this would help.

## Nice-to-Haves

- A "clustered ABMIL" baseline (mean-pooled cluster features with attention, but no second-order module and no fusion) would cleanly isolate the effect of clustering from the effect of second-order moments — the current "w/o SOM" ablation still uses the fusion mechanism.
- Visualizing the learned covariance matrix for a cancerous vs. normal slide would substantiate the claim that second-order moments capture meaningful feature correlations.
- A sensitivity analysis for the covariance vectorization parameters (kernel dimension $m$, number of kernels $T$) would demonstrate robustness of this design choice.

## Removed Points

- *"The performance improvements may not be statistically significant"* — This is **kept** as a Major weakness because it is valid and verifiable from the paper's own reported numbers.
- *"ABMIL becomes a special case is a trivial claim that overstates the contribution"* — **Removed**. The claim that a more general framework reduces to a special case under specific conditions is a standard and reasonable way to describe a generalization, not overstatement.
- *"The paper's efficiency advantage is from clustering, not higher-order method"* — **Partially removed**; the paper already includes w/o SOM (clustering without second-order) at 217s, which provides this baseline. The remaining point about comparing to clustered ABMIL without the fusion architecture is kept as a nice-to-have.
- *"Missing related work on second-order/covariance-based aggregation in MIL"* — **Removed** per the hard rule against citing missing related works without external verification. The experimental gap (not comparing against covariance methods) is kept as a Minor weakness.
- *"The DBSCAN epsilon parameter choice is arbitrary"* — **Removed**. The choice (65th percentile of nearest neighbor distances) is a standard heuristic for DBSCAN, and the paper notes a sensitivity analysis in the appendix.
- *Generic strengths from Strength Finder* (e.g., "fair and reproducible experimental setup") — **Removed**. The unified codebase and 5-fold CV are standard practice; the remaining strengths are concrete and evidenced.

## Novel Insights

The reviews surface an interesting tension: the paper's core idea — that second-order statistics capture complementary information beyond mean aggregation in MIL — is well-motivated and validated by ablation, yet the actual performance gains over strong baselines are small enough that they could plausibly arise from increased model capacity or random seed variation rather than from the covariance mechanism itself. The missing simple baseline (e.g., ABMIL + concatenated variance diagonal) is the single experiment that would resolve this ambiguity most cleanly. Additionally, the "attention-weighted covariance" terminology imprecision is not merely a nitpick — it reflects a broader pattern where the paper's framing slightly overstates what the method actually implements, which matters when the empirical gains are marginal.

## Suggestions

1. **Add a simple second-order baseline.** At minimum, compare against ABMIL with per-cluster variance/covariance-diagonal features concatenated to the pooled representation. This would isolate whether the value comes from the second-order statistics or from the specific vectorization/fusion architecture.
2. **Report statistical significance.** Add McNemar's test or a paired bootstrap test comparing HOMIL against the best baseline on each dataset, and report whether differences are significant at $p<0.05$.
3. **Correct the "attention-weighted covariance" label.** Either weight the outer products by $a_k$ to truly make it attention-weighted, or clarify that the centering is attention-weighted while the covariance sum itself is unweighted.
4. **Ablate the covariance vectorization.** Compare the proposed Conv1D-based vectorization against simpler alternatives (flatten+linear projection, upper-triangle vectorization) to justify the design choice.

## Score and Decision

**Calibration anchors** (from retrieval):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| MFC Framework (WSI causal MIL) — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6xrDPHhwD3.md` | 6.00 (Accept) | Stronger novelty and more thorough causal motivation; HOMIL is clearer in presentation but weaker in empirical rigor (no significance testing) |
| Covariance Pooling Theory — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/q1t0Lmvhty.md` | 6.00 (Accept) | Deeper theoretical contribution in a related area; HOMIL has stronger practical motivation but less technical depth |
| Vision-Language SA — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/trj2Jq8riA.md` | 5.67 (Accept) | More innovative paradigm (VL + survival) and broader evaluation (5 datasets); HOMIL's contribution is narrower |
| MILCA — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YCdag94iZs.md` | 3.50 (Reject) | HOMIL has clearer writing, better experimental methodology, and a more grounded technical contribution |
| Mamba-HMIL — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0yVP49SDg0.md` | 3.25 (Reject) | HOMIL has better motivation and more thorough ablations; both have modest gains over baselines |
| Pg-GAT — `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MOCEoNsjEx.md` | 3.00 (Reject) | HOMIL has clearer novelty (second-order moments) and stronger empirical validation |

HOMIL has a genuinely novel idea (second-order moments in MIL for WSI) and solid experimental infrastructure (unified codebase, two datasets, ablation study). However, it falls short of the accepted anchors on three fronts: (1) the performance improvements are modest with overlapping error bars and no significance tests; (2) missing critical baselines that would isolate the core contribution; (3) imprecise terminology ("attention-weighted covariance") that overstates the method's novelty. These gaps would need to be addressed for acceptance at ICLR. The paper is stronger than the rejected anchors (scored 3.0–3.5) but clearly below the accepted ones (5.67–6.0).

**Score: 5.0**

**MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>**