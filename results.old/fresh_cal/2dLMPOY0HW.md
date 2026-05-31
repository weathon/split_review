Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper investigates *when* MLP-based methods can match GNNs on node classification through an information-theoretic lens. It proposes a tractable upper bound $H(A|\hat{A})$ to quantify the overlap between node features and graph structure (Theorem 1), demonstrating that datasets with higher feature–structure overlap see MLPs perform competitively. It then introduces InfoMLP, which preprocesses graph-augmented features via diffusion (Eq. 5) and trains an MLP to maximize mutual information between its embeddings and those augmented features using a lightweight decorrelation-based loss (Eq. 7). Experiments on seven medium-sized graphs across transductive, inductive, and cold-start settings show InfoMLP outperforms prior MLP methods on all datasets and matches/exceeds GNNs on most.

## Strengths

1. **Principled information-theoretic analysis of MLP vs. GNN performance.** The paper provides a theoretically grounded upper bound $H(A|X) \leq H(A|\hat{A})$ (Theorem 1) using only $\ell_2$ distances of normalized node features, with a gap analysis (Theorem 2) characterizing when the bound is tight. Figure 2 shows clear alignment between the estimated conditional entropy and observed MLP-vs-GNN performance gaps across datasets — for instance, CS (small entropy → MLP works) vs. Computer (large entropy → MLP struggles). This is the first concrete dataset-level measure explaining *why* MLP success varies across graphs, moving beyond post-hoc intuition.

2. **Strong and consistent empirical results.** In the transductive setting (Table 3), InfoMLP outperforms all prior MLP methods on 7/7 datasets and beats competitive GNNs on 6/7. In the cold-start setting (Table 4), it achieves the best results on all 7 datasets. Results are reported with means and standard deviations over 20 trials. The method also achieves $\text{MLP}_{\text{both}}$ status — same training and testing complexity as a vanilla MLP — verified in Table 1.

3. **Elegant decomposition of the MI maximization objective.** The paper decomposes the intractable $I(Z_{\text{mlp}}; A)$ into (a) a non-parametric preprocessing step (graph diffusion with $K$ chosen via $H(A|X_{\text{aug}})$ minimization) and (b) a training-time MI loss with $\mathcal{O}(ND^2)$ complexity. This design cleanly preserves MLP-level efficiency while incorporating structural information.

4. **Explicit evaluation of the underexplored cold-start scenario.** The paper formalizes and evaluates a challenging inductive cold-start setting where test nodes have no available connections at inference — a scenario where GNNs are inapplicable yet MLPs can still perform. InfoMLP's strong results here (Table 4) demonstrate practical utility beyond standard benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in cold-start preprocessing protocol.** The cold-start setting is defined such that "connections of validation and testing nodes are not available during the inference stage" (Section 4.1). However, InfoMLP's preprocessing step (Eq. 5: $X_{\text{aug}} = \sum \gamma_k \tilde{A}^k X$) uses the adjacency matrix $A$ and is described as "performed once ahead of training" (Section 3.3). The paper does **not** specify whether this preprocessing uses the full graph (including test nodes' edges) or only the training subgraph in the cold-start setting. If the full graph is used, the MI loss (Eq. 7) during training would involve $Z_{\text{aug}}$ for test nodes computed with their graph connections, which constitutes information leakage. The paper must clarify the protocol used and, if the full graph was used, report results with training-graph-only preprocessing or justify why this is not leakage. The identical results across inductive and cold-start for InfoMLP are *explained* by the table caption ("Inductive/cold start makes no difference for MLP methods"), so the results themselves are not suspicious — but the preprocessing ambiguity is a genuine methodological gap.

2. **Insufficient justification of the MI maximization loss.** The paper claims InfoMLP "explicitly maximizes" $I(Z_{\text{mlp}}; A)$ (contributions, Section 1), but the connection between the actual objective and the target is heuristic. The chain is: maximize $I(Z_{\text{mlp}}; A)$ → maximize $I(Z_{\text{mlp}}; X_{\text{aug}})$ → maximize $I(Z_{\text{mlp}}; Z_{\text{aug}})$. While $I(Z_{\text{mlp}}; X_{\text{aug}}) \geq I(Z_{\text{mlp}}; Z_{\text{aug}})$ (by data processing inequality, since $Z_{\text{aug}} = \text{MLP}_\theta(X_{\text{aug}})$), the initial step from $I(Z_{\text{mlp}}; A)$ to $I(Z_{\text{mlp}}; X_{\text{aug}})$ is not formally justified — the paper asserts that minimizing $H(A|X_{\text{aug}})$ bridges this gap but provides no inequality chain. Furthermore, the loss in Eq. 7 is presented as an MI maximizer "based on feature decorrelation (Zhang et al.)" but the paper gives no explanation of why the MSE + decorrelation terms constitute a valid lower bound on mutual information, or how the specific formulation relates to known MI estimators like InfoNCE. This undercuts the paper's foundational narrative that InfoMLP is an explicit MI maximization method rather than a well-engineered heuristic.

### Minor

3. **Limited empirical validation of the proposed metric.** The correlation between $H(A|\hat{A})$ and MLP-vs-GNN performance is shown on only 5 datasets in Figure 2 and Table 2. While the theoretical bound (Theorem 1) is sound, the paper would benefit from demonstrating that this metric predicts performance gaps across a wider range of graphs (including the other 2 datasets used in experiments and ideally additional datasets beyond these 7). The current evidence, while suggestive, is not strong enough to support the claim of a broadly predictive "tractable metric."

4. **Selection of $K$ not fully specified.** The paper states $K$ is chosen by minimizing $H(A|X_{\text{aug}}(K))$ (Section 3.3), but does not describe the search procedure: how many values of $K$ are tried, what range is explored, what is the computational cost of evaluating $H(A|X_{\text{aug}})$ for each candidate $K$, and how the validation set is used for this selection. The complexity analysis accounts for preprocessing but not the cost of this hyperparameter search.

### Trivial
None.

## Nice-to-Haves

- Ablation isolating the contribution of the MI loss components: compare against (a) cross-entropy only, (b) cross-entropy + MSE only, (c) cross-entropy + decorrelation only. This would make the method's design more transparent.
- Hyperparameter sensitivity analysis for $\alpha$ and $\beta$ on at least one dataset.
- Comparison with a simpler baseline: feeding $X_{\text{aug}}$ (Eq. 5) directly into an MLP *without* the MI loss, to isolate whether the loss adds value beyond the preprocessing.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The citation to Zhang et al. does not appear in the main text."** — Factually wrong. The citation appears at line 141 of the paper (as a superscript 3). Removed.
- **"Table 4 reports identical accuracy... which is suspicious."** — The paper explicitly states in the table caption: "Inductive/cold start makes no difference for MLP methods." The identical results are expected, not suspicious. The underlying preprocessing-concern is retained as a Major weakness above.
- **"Missing appendix content, missing ablations, hyperparameter details, training setup, optimizer, learning rate."** — The parser strips the appendix from all papers. Section E.1 and additional experimental details referenced throughout likely exist in the original submission. Removed per instructions.
- **Generic criticisms lacking concrete anchors** (e.g., "the evaluation lacks rigor," "the bound is heuristic," "could measure proxies") — Removed as they are area-of-concern sweeps without specific identifiable flaws in the paper.
- **"The cold-start setting... InfoMLP's results are identical to inductive — suggesting the setting is not actually cold-start for InfoMLP."** — As noted above, the paper explicitly states this is expected for MLP methods, so there is no inconsistency.
- **Strengths that are generic or conflict with verified weaknesses** (e.g., "this paper addressed an important problem," vague praise about methodology) — Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no fundamentally new observation that is not already present in the paper's own analysis. However, the reviews collectively highlight that the paper's strongest contribution is its information-theoretic framing (the $H(A|\hat{A})$ metric and its alignment with empirical regimes), while the weakest link is the gap between the claimed MI maximization narrative and the actual loss function — a tension the paper itself does not fully resolve.

## Suggestions

1. **Clarify the cold-start preprocessing protocol explicitly.** State whether $X_{\text{aug}}$ is computed using the full graph or only the training subgraph. If the full graph is used, justify this by noting that preprocessing is offline and the model still takes only $X$ at test time; alternatively, report results with training-only preprocessing to eliminate any concern.

2. **Revise the framing around MI maximization.** Either (a) provide a clear justification or inequality chain showing how minimizing $H(A|X_{\text{aug}})$ and maximizing $I(Z_{\text{mlp}}; Z_{\text{aug}})$ connects to $I(Z_{\text{mlp}}; A)$, or (b) honestly reposition the method as "inspired by information-theoretic principles" rather than claiming explicit MI maximization. The loss in Eq. 7 is empirically effective regardless of whether it provably maximizes MI.

3. **Expand empirical validation of the metric** to include more datasets and a direct test of whether choosing $K$ via $H(A|X_{\text{aug}})$ minimization correlates with downstream accuracy.

4. **Describe the $K$ selection procedure** (search range, grid density, computational cost) in detail.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>