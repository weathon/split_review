Here is my final consolidated review.

---

## Summary

This paper studies when and why MLPs can compete with GNNs in node classification. It proposes (1) a tractable metric based on conditional entropy $H(A|X)$ to quantify how much node features capture graph structure, and (2) InfoMLP, an MLP-structured method that uses graph-diffused features as a target for representation learning via a decorrelation-based objective. The key insight is that on datasets where node features already contain substantial structural information (low $H(A|X)$), properly regularized MLPs can match or exceed GNNs. InfoMLP achieves strong empirical results across transductive, inductive, and cold-start settings while maintaining MLP-level complexity.

## Strengths

- **Novel tractable metric for quantifying feature–structure overlap.** The paper proposes an upper bound $H(A|X) \le H(A|\hat{A})$ using $\ell_2$ distances between normalized features, and estimates it by fitting Gaussian distributions to positive/negative edge distances (Section 3.2, Theorem 1). This metric directly explains observed MLP-vs-GNN performance patterns: e.g., CS has low $H(A|\hat{A})$ and MLP performs well; Computer has high entropy and MLP struggles (Figure 2 vs. Table 2). This is the paper's most distinctive conceptual contribution — it gives the community a practical tool for diagnosing when structure-aware methods are likely to help.

- **Strong empirical performance across multiple challenging settings.** In the transductive setting (Table 3), InfoMLP outperforms all prior MLP-based models on all 7 datasets and beats GNNs on 6/7. In the cold-start setting (Table 4) — where test nodes have no connections and GNNs collapse (e.g., Cora GCN drops from 87.2 to 24.1) — InfoMLP achieves the best accuracy on all 7 datasets. These results are not incremental; the gains are often large.

- **Efficiency: MLP-level complexity at both training and testing.** By moving graph diffusion to a non-learning preprocessing step, InfoMLP avoids message passing during training and inference, unlike distillation-based methods (GLNN, N2N). This is cleanly demonstrated in Table 1's taxonomy. The $\mathcal{O}(ND^2)$ MI objective matches the cost of a linear layer, making the method practical for large graphs.

- **Principled analysis linking feature dimensionality to structure predictability.** The paper notes that the gap between feature dimension $d$ and graph size $N$ directly affects how much $X$ can convey about $A$ (Section 3.2, final paragraph). This explains why high-dimensional features (CS, 6800 dim) capture structure better than low-dimensional ones (Computer, 700 dim), aligning with the entropy estimates in Figure 2.

## Weaknesses

### Major

- **The theoretical framing as "explicit mutual information maximization w.r.t. $A$" is overclaimed.** The paper argues that InfoMLP maximizes $I(Z_{\text{mlp}}; A)$ via two steps: (1) find $X_{\text{aug}}$ that minimizes $H(A|X_{\text{aug}})$, then (2) maximize $I(Z_{\text{mlp}}; X_{\text{aug}})$. The connection is intuitive — if $X_{\text{aug}}$ captures information about $A$, then aligning $Z_{\text{mlp}}$ with $X_{\text{aug}}$ should capture some of that information — but it is not a formal equivalence. The paper provides no bound, data-processing argument, or empirical validation that maximizing $I(Z_{\text{mlp}}; X_{\text{aug}})$ actually increases $I(Z_{\text{mlp}}; A)$. This gap is significant because the paper's main selling point is "direct" MI maximization. The method would be better positioned as *a well-motivated heuristic that uses graph-diffused features as a regularizer* rather than a principled MI maximizer. The empirical results are convincing regardless, but the framing should match what is actually demonstrated.

- **The MI estimator (Eq. 7) is not justified as a lower bound on mutual information.** The objective (MSE between standardized embeddings plus a covariance penalty) is adopted from Zhang et al. and resembles Barlow Twins / VICReg. While the paper cites "well-studied mutual information estimators" (Belghazi et al., 2018; van den Oord et al., 2018), the specific objective in Eq. 7 is not a known variational lower bound on $I(Z_{\text{mlp}}; Z_{\text{aug}})$. No derivation or proof is provided. Given that the paper's framing centers on MI maximization, this is a gap in rigor. The empirical success may equally stem from feature smoothing, contrastive effects, or variance regularization. Either provide a justification that Eq. 7 bounds MI, or weaken the claim (e.g., "a regularization that encourages alignment, which can be seen as a surrogate for MI maximization").

### Minor

- **No direct empirical validation that InfoMLP increases $I(Z_{\text{mlp}}; A)$.** The paper's central hypothesis is that InfoMLP's advantage comes from maximizing MI with the graph structure. Yet the paper never measures $I(Z_{\text{mlp}}; A)$ (e.g., using a simple edge-prediction probe or InfoNCE estimate) for InfoMLP vs. baselines. Without this, the mechanism remains a conjecture, and the strong results could equally be attributed to the specific form of the regularization (smoothing, feature mixing) rather than MI maximization.

- **Cold-start evaluation protocol for GNN baselines is underspecified.** The paper describes the cold-start setting as "the connections of validation and testing nodes are not available during the inference stage" (Section 4.1). However, it does not clarify how GNN baselines were adapted — e.g., whether they were trained with the full adjacency matrix then deprived of test edges at inference, whether hyperparameters were retuned, or whether the GNN was retrained on only training nodes. This matters because the reported GNN drops are dramatic (e.g., Cora GCN from 87.2 to 24.1). The comparison is plausible but the protocol needs explicit description for reproducibility.

- **The $H(A|X)$ analysis does not directly inform the method's design choices.** The analysis (Section 3.2) convincingly shows that datasets differ in how predictable $A$ is from $X$, and this correlates with MLP performance. However, the specific choices in InfoMLP — uniform-weight graph diffusion (Eq. 5) and the decorrelation-based objective (Eq. 7) — are not derived from or justified by this analysis. The paper would be stronger if it showed, e.g., that the optimal diffusion depth $K$ correlates with $H(A|X)$, or that the improvement of InfoMLP over vanilla MLP correlates with the entropy metric.

### Trivial

- None beyond the presentation issues noted in Removed Points.

## Nice-to-Haves

- An ablation study separating the alignment term ($\ell_2$ loss) from the decorrelation term (covariance penalty) in Eq. 7 to show which drives performance.
- Sensitivity analysis for hyperparameters $\alpha$ and $\beta$ in Eq. 7.
- A direct estimate of $I(Z_{\text{mlp}}; A)$ for InfoMLP vs. baselines using a simple logistic regression edge-predictor probe, to directly validate the mechanism.

## Removed Points

These points were raised in the original reviews but are removed or downgraded for the following reasons:

- **The reviewer's chain-rule argument** (claiming $I(Z_{\text{mlp}}; A) = I(Z_{\text{mlp}}; X_{\text{aug}}) + I(Z_{\text{mlp}}; A | X_{\text{aug}})$) **is factually incorrect**. The chain rule gives $I(Z_{\text{mlp}}; X_{\text{aug}}, A) = I(Z_{\text{mlp}}; X_{\text{aug}}) + I(Z_{\text{mlp}}; A | X_{\text{aug}})$, not $I(Z_{\text{mlp}}; A)$ on the LHS. The underlying concern (incomplete theoretical justification) is valid and kept above, but this specific mathematical argument is wrong and removed. *[Hard Rule 2]*
- **Criticism about missing ablation studies / appendix content** — The paper references "Section E.1" and "extensive ablation studies" in the abstract (line 5). These sections were stripped by the PDF parser, not omitted by the authors. *[Hard Rule: missing appendix]*
- **Request for multi-seed runs / confidence intervals** — 20 random trials are already reported (Section 4.1). *[Hard Rule: parser artifact]*
- **Formatting/style nitpicks** — Any such criticisms are parser artifacts, not author errors. *[Hard Rule 5, 6]*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the theoretical claims.** Replace claims of "direct MI maximization w.r.t. $A$" with honest language: e.g., "we propose a regularization that encourages MLP embeddings to align with graph-diffused features, which serves as a surrogate for capturing structural information." This would not diminish the paper's value — the empirical results and the $H(A|X)$ analysis are contributions on their own.

2. **Empirically validate the mechanism.** Compute an estimate of $I(Z_{\text{mlp}}; A)$ for InfoMLP and key baselines (e.g., using a logistic regression edge-predictor on the embeddings). If InfoMLP indeed yields higher $I(Z_{\text{mlp}}; A)$, this directly supports the framing. If not, discuss what else the method might be doing.

3. **Specify the cold-start protocol for GNNs.** Add 2–3 sentences describing exactly how GCN, GAT, etc. were evaluated in the cold-start setting (e.g., "GNNs were trained on the full training graph including all training-set nodes and edges, then at inference time, test nodes were treated as isolated — no neighborhood was aggregated"). Clarify whether hyperparameters were retuned for the cold-start scenario.

4. **Connect the $H(A|X)$ analysis to the method.** Show that the improvement of InfoMLP over vanilla MLP correlates with $H(A|X)$ across datasets, or that the optimal $K$ (diffusion depth) relates to the entropy metric. This would turn the analysis from a post-hoc explanation into a design principle.

## Score and Decision

**Originality:** Good — the $H(A|X)$ estimation metric is novel, and the analysis of feature-structure overlap is a genuine contribution. The method itself combines existing ideas (graph diffusion + feature decorrelation) in a new way.

**Importance of research question:** High — understanding when MLPs can replace GNNs has significant practical implications for efficiency and deployment in cold-start settings.

**Claims well supported:** Partially — the empirical claims are well supported; the theoretical framing (MI maximization) is overclaimed relative to what is actually demonstrated.

**Soundness of experiments:** Good — comprehensive evaluation across three settings with multiple baselines, 20 random trials, and consistent results. Minor clarity issues in the cold-start protocol.

**Clarity of writing:** Good overall — the paper is well-structured and the information-theoretic concepts are explained clearly. The main weakness is the gap between the stated theoretical ambition and what is actually justified.

**Value to the research community:** Potentially high — the $H(A|X)$ metric could become a standard diagnostic tool for understanding when structural information matters in node classification tasks. InfoMLP is a practical, efficient method with strong results.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>