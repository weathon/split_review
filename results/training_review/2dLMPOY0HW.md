Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper studies when and why MLP-structured models can succeed at node classification on graphs, using information theory. It introduces a tractable metric $H(A|\hat{A})$ (conditional entropy of the adjacency matrix given a distance-based estimate from features) to quantify the overlap between node features and graph structure, showing that datasets where this entropy is low correspond to settings where MLPs can approach GNN performance. Based on this analysis, the paper proposes InfoMLP, a method that maximizes mutual information between MLP node embeddings and the graph structure via a two-step decomposition: (1) non-parametric graph diffusion preprocessing to construct an augmented feature matrix that captures structural information, and (2) a feature-decorrelation-based MI maximization objective. InfoMLP achieves vanilla-MLP-level training/testing efficiency while outperforming prior MLP methods across transductive, inductive, and cold-start settings.

## Strengths

1. **Clean information-theoretic framing** — The paper provides a principled perspective (grounded in mutual information between node features and graph structure) to explain when and why MLPs can compete with GNNs. The Venn diagram intuition (Fig. 1) and the tractable entropy metric $H(A|\hat{A})$ (Theorem 1, Fig. 2) offer a conceptually useful tool for understanding dataset-specific MLP-vs-GNN performance gaps.

2. **Elegant method design with practical efficiency** — The two-step decomposition (non-parametric preprocessing via graph diffusion + parametric MI maximization) is well-motivated and allows InfoMLP to maintain vanilla-MLP complexity during both training and testing ($\mathcal{O}(\text{MLP})$), with preprocessing done once ($\mathcal{O}(KEd)$). This is a genuine practical advantage over distillation-based methods that require a GNN teacher during training.

3. **Strong empirical performance, especially in cold-start** — InfoMLP outperforms all prior MLP baselines on all 7 datasets in the transductive setting (Table 3) and achieves the best results on all 7 datasets in the cold-start setting (Table 4), often by large margins (e.g., +3.44% on Photo). The cold-start results are particularly compelling because this is a practically relevant yet underexplored scenario where GNNs fundamentally struggle due to missing test-time graph structure.

4. **Comprehensive evaluation across three settings** — The paper systematically tests transductive, inductive, and cold-start settings on 7 medium-sized graphs, with additional results on large-scale and heterophilic graphs in the appendix. This thoroughness strengthens the empirical contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in the inductive evaluation protocol (potential data leakage)** — The paper does not specify whether the graph diffusion preprocessing (Step 1: computing $X_{\text{aug}} = \sum \gamma_k \tilde{A}^k X$) in the inductive setting is performed on the **full graph** (including validation/test nodes) or only on the **training subgraph**. If the full graph is used, information from test nodes propagates into training node features through multi-hop diffusion, which would constitute data leakage and invalidate the inductive results. The paper states "Inductive/cold start makes no difference for MLP methods" (Table 4 footnote), but this refers only to inference — the preprocessing step still requires the graph structure. The cold-start results are unaffected (test nodes have no edges), and the transductive results are unaffected, but the **inductive** column in Table 4 rests on an unverified protocol. This is a significant reporting gap that must be clarified before the results can be trusted.

### Minor

2. **Qualitative rather than quantitative support for the explanatory metric** — Figure 2 and the associated entropy values provide visual evidence that $H(A|\hat{A})$ correlates with MLP-vs-GNN performance, and the classification into three regimes (small/medium/large entropy) is intuitive. However, no quantitative correlation (e.g., Pearson/Spearman between $H(A|\hat{A})$ and the accuracy gap) is computed, and the regime thresholds are not formally defined. This weakens the claim that the metric "explains" performance variations rather than merely being post-hoc consistent with them.

3. **Incomplete specification of the entropy estimation procedure** — The paper does not describe how $p(\hat{A}_{ij}|A_{ij})$ is estimated for large graphs where computing all $O(N^2)$ pairwise $\ell_2$ distances is infeasible. Specifically, the negative sampling strategy (how many non-edge pairs, how they are sampled) and how Gaussian parameters are fitted are not stated. This makes Figure 2 difficult to reproduce independently.

4. **Ambiguity in $K$ selection criteria** — The paper states that $K$ can be selected by (a) minimizing $H(A|X_{\text{aug}})$ and (b) evaluating performance on the validation set, without clarifying which criterion was used in the reported experiments. These could yield different $K$ values, and the ambiguity makes the experimental protocol incompletely specified.

5. **Incomplete reference for the MI estimator** — The MI maximization loss (Eq. 7, based on feature decorrelation) is cited as "Zhang et al.3" without a full citation or derivation, making it difficult for readers to assess the connection between the decorrelation objective and mutual information maximization.

### Trivial

6. **Minor notation inconsistencies** — The paper sometimes uses $Z_{\text{m1p}}$ (with a numeral "1") and sometimes $Z_{\text{mlp}}$, and there is a typographical artifact ("√of" on line 147). These are parser artifacts or minor inconsistencies that do not affect understanding.

## Nice-to-Haves

- Computing a quantitative correlation (Pearson/Spearman) between $H(A|\hat{A})$ and the GCN-vs-best-MLP accuracy gap across a larger set of datasets would substantially strengthen the explanatory claim.
- An ablation study separating the two components of the MI loss (the MSE invariance term and the decorrelation term) would clarify each component's contribution.
- A comparison with an alternative MI estimator (e.g., InfoNCE) would justify the choice of the decorrelation-based estimator beyond computational complexity.
- Testing whether the $H(A|\hat{A})$ metric can predict MLP feasibility on new datasets (i.e., a forward prediction rather than post-hoc explanation) would turn the analysis into a practically useful tool.

## Removed Points

These points from the reviewers were evaluated and removed with justification:

1. **PMLP omitted from baselines** (Harsh Critic, Section-by-Section Notes) — The paper explicitly discusses PMLP in Section 2 and justifies its exclusion because PMLP uses message passing during testing, which is outside the paper's scope (MLPs that take only $X$ as test-time input). The exclusion is properly scoped and justified.

2. **MI inequality chain is not theoretically grounded** (Harsh Critic, Critical Issue 3) — The reviewer attributed an inequality $I(Z_{\text{mlp}}; A) \geq I(Z_{\text{mlp}}; X_{\text{aug}})$ to the paper, but the paper does not claim this inequality. The paper's approach is a two-step heuristic (find $X_{\text{aug}}$ that captures $A$ information, then maximize $I(Z_{\text{mlp}}; X_{\text{aug}})$) and only claims $I(Z_{\text{mlp}}; X_{\text{aug}}) \geq I(Z_{\text{mlp}}; Z_{\text{aug}})$, which follows correctly from the data processing inequality. The strawman chain is removed.

3. **Missing implementation details (architecture, hyperparameters, training epochs)** (Harsh Critic, Critical Issue 4) — These are standard details that the paper's appendix (truncated by the parser) likely contains. The paper references Section E.1 for additional experiments and ablation studies. Not a valid criticism of the main paper.

4. **Theorem 2 is irrelevant to experiments** (Harsh Critic, Section-by-Section Notes) — Theorem 2 provides a theoretical gap analysis that contextualizes when the upper bound is tight. It is not claimed to be directly computed in experiments. Its role is analytical, not empirical.

5. **Generic complaint about missing statistical significance tests** (Harsh Critic, Section-by-Section Notes on Table 3) — Standard deviations are reported, and the paper's claim "outperforms" refers to mean accuracy, which is standard practice in this field. The margin is small on some datasets, but the paper reports this transparently.

## Novel Insights

The interaction between the harsh critic (who raised valid concerns about experimental protocol) and the strength finder (who identified genuine contributions) reveals that the paper's core methodological contribution (InfoMLP) is solid and empirically validated, while its **explanatory** contribution (the $H(A|\hat{A})$ metric) is plausible but underevidenced. An interesting observation that emerges is that the paper's strengths and weaknesses are largely decoupled: the inductive protocol ambiguity affects only one column of one table, and even if fully resolved, does not touch the transductive or cold-start results where InfoMLP shines. Conversely, even if the explanatory metric were fully quantitatively validated, it would not change the empirical success of InfoMLP. This suggests the paper could be strengthened by either tightening the evaluation protocol description (addressing the inductive concern) or by expanding the metric validation — but only the former is necessary for the method to stand on its own.

## Suggestions

1. **Clarify the inductive preprocessing protocol** — Specify explicitly whether $X_{\text{aug}}$ is computed using only the training subgraph's adjacency matrix or the full graph. If the former, describe how the training subgraph is induced. If the latter, re-run the inductive experiments with proper isolation and report whether results change.

2. **Specify the entropy estimation details** — Describe the negative sampling strategy used for estimating $p(\hat{A}_{ij}|A_{ij}=0)$ on each dataset (number of negative samples, sampling method) and how the Gaussian parameters were fitted.

3. **Disambiguate $K$ selection** — State clearly whether $K$ was selected by minimizing $H(A|X_{\text{aug}})$ or by validation accuracy, and report the selected $K$ values.

4. **Complete the MI estimator reference** — Provide the full citation for the decorrelation-based MI estimator and briefly explain its connection to mutual information lower bounds.

## Score and Decision

The paper makes a genuine contribution: a well-motivated, efficient MLP method for node classification with strong empirical results, particularly in the practically important cold-start setting. The information-theoretic perspective is conceptually valuable. The main weakness — ambiguity about the inductive evaluation protocol — is a reporting gap rather than a fundamental flaw, and the method's two strongest sets of results (transductive and cold-start) are unaffected by it. The minor weaknesses (qualitative-only metric support, underspecified estimation details) are addressable.

**Overall assessment**: The paper's core contributions are sound and clearly demonstrated. The inductive protocol ambiguity must be clarified (preferably with a verification that the results hold under a clean protocol), but this does not invalidate the paper's main claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>