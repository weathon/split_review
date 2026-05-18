I have all the information I need. Let me now construct the final consolidated review.

---

## Summary

This paper proposes BFLP (Bag of Features for Link Prediction), a model that combines handcrafted structural features (Common Neighbors, Jaccard, Salton, Sorensen, Adamic-Adar) with domain (attribute-similarity) features and feeds them into XGBoost for link prediction. The central claim is that this simple feature-engineering pipeline matches or outperforms most GNN-based methods across six standard benchmarks (CORA, CITESEER, PUBMED, PHOTO, COMPUTERS, OGBL-COLLAB), suggesting that current GNNs are not fully leveraging the information available in graph structure and node attributes.

## Strengths

- **Consistently competitive performance across multiple benchmarks.** Tables 3–5 show that BFLP achieves the best or second-best result on 5 out of 6 datasets across multiple metrics (AUC, AP, Hits@20, Hits@50), including surpassing the prior OGBL-COLLAB leader (55.19 vs. 54.63). This directly substantiates the claim that traditional feature engineering can rival state-of-the-art GNNs.

- **Ablation study confirms synergistic benefit of combining feature types.** Table 6 systematically compares structural-only, domain-only, and combined features across four datasets. In every case, the combined set yields higher AUC than either subset alone (e.g., CORA: combined 0.852 vs. structural 0.805 vs. domain 0.788), demonstrating that the fusion of neighborhood-based and attribute-based features is a key mechanism behind the model's effectiveness.

- **Comprehensive coverage of baselines.** The paper evaluates against 13 GNN-based methods (GCN, GraphSAGE, GAT, SEAL, GAE, VGAE, ARGA, ARVGA, MVGRL, DBGAN, LGLP, MSVGAE, CFLP) plus classical embedding techniques (MF, MLP, Node2Vec) across multiple metrics, providing broad evidence that the results are not due to cherry-picked comparison points.

- **Computational efficiency is clearly documented.** End-to-end runtime for the largest dataset (OGBL-COLLAB) is reported as 30 minutes, and the worst-case complexity is given as O(|V|k³), with code provided.¹ Footnote: ¹ The paper states "We provide our code at the link1" — the link itself is not resolved in the extracted text.

## Weaknesses

### Major

- **Baseline comparisons are not controlled.** The paper takes GNN baseline results from Li et al. (2023) and the OGB leaderboard without confirming that they were obtained under identical experimental conditions. The paper uses train/val/test splits from (Zhao et al., 2022) for CORA/CITESEER/PUBMED and (Guo et al., 2022) for PHOTO/COMPUTERS, but it is not verified whether Li et al. (2023) used these same splits. For OGBL-COLLAB the splits are standardized, which mitigates this concern for that dataset, but for the other five datasets the comparison rests on an assumption of compatible experimental setups. Since the paper's central claim is that BFLP "outperforms most GNNs," the lack of a controlled re-evaluation of baselines under matching conditions is a significant gap. The paper would be substantially stronger if even three representative GNNs (e.g., GCN, GAT, SEAL) were re-run under the exact same splits and negative sampling procedure.

- **Domain features are critically underspecified.** The paper defines domain features as "the relevant similarity measure between the node features" (Section 3.2) but never states precisely which similarity functions are used for which datasets. Node feature types vary: bag-of-words (CORA, CITESEER, PUBMED, PHOTO, COMPUTERS) and 128-dimensional averaged word embeddings (OGBL-COLLAB). The paper mentions that features were "adjusted" for OGBL-COLLAB "since [it] is dynamic and weighted" (Section 4.1) without specifying the adjustment. The authors themselves acknowledge this as a limitation (Section 4.2), but the current description is insufficient for replication. Because the ablation study shows domain features contribute substantially in some cases (e.g., CORA: combined 0.852 vs. structural alone 0.805), their exact formulation is critical for interpreting results. At minimum, the precise similarity measure(s) (e.g., cosine similarity, dot product, RBF kernel) and any normalization should be stated per dataset.

### Minor

- **Hyperparameters are tuned separately per metric without variance reporting.** The paper sets different XGBoost hyperparameters for AUC, AP, Hits@20, and Hits@50 (Section 4.1). While different metrics may genuinely benefit from different configurations, this practice risks overfitting to the specific evaluation protocol, especially since no standard deviations or confidence intervals are reported despite running 5 or 10 repetitions. Without variance estimates, readers cannot assess whether the observed performance differences between BFLP and baselines are statistically meaningful.

- **The inductive/versatility claim is unsupported.** The paper describes transductive, inductive, and semi-inductive settings in Section 3.1 and states that BFLP "exhibits a high degree of versatility and can easily adapt to any of these settings." However, all experiments are conducted in the transductive setting only (explicitly noted in Section 4.1). The adaptability claim is thus untested. The paper should either add an inductive experiment (e.g., on a dataset with explicit train/inductive-test splits) or remove the unsupported claim.

- **WL expressivity motivation is superficial.** The paper invokes the Weisfeiler-Lehman equivalence result to motivate the investigation, but the proposed method does not engage with expressivity in any formal sense — it simply uses handcrafted structural features that WL-type GNNs are already known to be able to compute. The paper would be more coherent if it framed the contribution as a practical empirical demonstration without claiming validation of a specific theoretical bound.

- **Negative sampling strategy is underspecified for reproducibility.** The paper states that negatives are "randomly selected" (Sections 4.1) but does not specify the sampling distribution (uniform? degree-based? using any bias correction?). Different negative sampling strategies can substantially affect link prediction results and comparability with baselines. This detail should be stated explicitly.

- **Runtime comparison lacks context.** The paper provides BFLP runtime (30 minutes for OGBL-COLLAB, 18 hours for COMPUTERS) but no corresponding runtime for any GNN baseline. The efficiency claim is qualitative without a reference point. Additionally, 18 hours on a CPU is not obviously more efficient than a GPU-trained GNN — a direct comparison would clarify the practical advantage.

### Trivial

- None beyond the points already covered above.

## Nice-to-Haves

- **Analysis of *why* GNNs fail to capture these features.** The ablation study shows that combining structural and domain features helps, but the paper does not analyze whether GNNs are theoretically or empirically unable to capture the same signals. Such analysis could turn the paper from a demonstration into an explanation, but this is beyond the stated scope.
- **Direct comparison with Singh et al. (2021).** The paper notes that another feature-engineering method ranks highly on OGBL-COLLAB but does not compare BFLP against it directly. A side-by-side comparison would strengthen the positioning.
- **Statistical significance tests.** Given the reported repetitions, paired tests (e.g., Wilcoxon signed-rank) comparing BFLP against the best GNN baseline per dataset would give readers a principled way to assess reliability.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- *"The paper does not report whether it re-ran any baselines under identical conditions"* — **Kept** (this is accurate and kept as a Major weakness above).
- *"The ablation study does not analyze why GNNs might fail to capture these same features"* — **Moved to Nice-to-Haves** (scope creep; the paper is an empirical demonstration, not a theoretical analysis).
- *"WL expressivity criticism implies the paper's framing is misleading"* — **Kept** (this is accurate and kept as a Minor weakness).
- *All criticisms related to formatting, missing appendix, or incomplete sections* — **Removed** (these are parser artifacts, not author errors).
- *"Does not compare directly with Singh et al. (2021)"* — **Moved to Nice-to-Haves** (relevant context but not a core weakness of the paper).
- *Strength Finder's claim of "fair comparison"* — **Rephrased to "comprehensive"** (the breadth of baselines is a strength, but "fair" conflicts with the verified uncontrolled-comparison weakness).

## Novel Insights

None beyond the paper's own contributions. The reviews raise standard methodological concerns (uncontrolled comparisons, underspecification, lack of variance) and do not contribute novel analytical perspectives on the paper's core findings.

## Suggestions

1. **Re-run at least 2–3 representative GNN baselines** (e.g., GCN, GAT, SEAL) under the exact same splits, negative sampling procedure, and evaluation protocol used for BFLP. This single change would transform the comparison from uncontrolled to controlled and significantly strengthen the paper.
2. **Report standard deviations** for all metrics across the 5/10 repetitions. Include them in the tables.
3. **Precisely specify the domain similarity measures** used per dataset. Create a small table stating whether cosine similarity, dot product, or another function is applied to node features, including any normalization or the "adjustment" for OGBL-COLLAB.
4. **Either add an inductive experiment or retract the unsupported versatility claim** in Section 3.1.
5. **Report the negative sampling distribution** explicitly (e.g., "uniform random over all non-edges" or "degree-based sampling").
6. **Remove or soften the WL-expressivity framing** if the paper is meant as a purely empirical contribution, or engage with the theory more carefully by explaining whether the features used here circumvent any WL limitations.

## Score and Decision

The paper's core finding — that well-chosen handcrafted features plus XGBoost can match or exceed GNNs on standard link prediction benchmarks — is a timely and valuable empirical contribution in a field where GNNs are often assumed to be dominant. The breadth of datasets, baselines, and the ablation study are genuine strengths. However, the three major weaknesses (uncontrolled comparison, underspecified domain features, and per-metric tuning without variance) directly affect the credibility of the central claim and prevent acceptance in the current form. The issues are fixable, and the paper could be strong after revisions, but the experimental validation as presented is not yet rigorous enough to support the strength of the claims made.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>