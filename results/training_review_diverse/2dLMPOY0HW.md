Based on my thorough reading of the paper, I can now produce the consolidated review. I've verified each claim against the actual paper text.

---

## Summary

This paper investigates why MLP-based models sometimes match GNN performance on node classification. It introduces a tractable conditional entropy metric $H(A|X)$ to quantify how much graph structure information is already present in node features, and shows this metric correlates with empirical MLP-GNN performance gaps. Building on this analysis, the paper proposes InfoMLP, which maximizes mutual information between MLP node embeddings and the graph structure via a two-step procedure: (1) non-parametric graph diffusion to construct an augmented feature matrix that captures structural information, and (2) a decorrelation-based loss that aligns original and augmented embeddings. InfoMLP achieves strong results across seven benchmarks in transductive, inductive, and cold-start settings while maintaining vanilla-MLP-level efficiency during training and testing.

## Strengths

- **Novel information-theoretic analysis of the MLP-GNN gap.** The paper introduces $H(A|X)$ as a tractable metric to quantify how much graph structure is predictable from node features. This metric is validated in Figure 2 and Table 2, where datasets with smaller $H(A|\hat{A})$ (CS, Cora, Citeseer, Pubmed) see competitive MLP performance, while datasets with larger overlap (Computer) still lag behind GNNs. This provides a clean, testable explanation for previously unexplained performance variability — a genuine contribution beyond the method itself.

- **Strong empirical performance across diverse settings.** In the transductive setting (Table 3), InfoMLP outperforms all prior MLP baselines (GraphMLP, GLNN, N2N, NOSMOG) on all seven datasets, and surpasses GNNs on six of seven. In the challenging cold-start setting (Table 4), where graph structure is unavailable at inference and GNNs degrade sharply, InfoMLP achieves the best results on all seven datasets. These results convincingly demonstrate practical value.

- **MLP-level efficiency preserved.** InfoMLP's complexity during training and testing is identical to a vanilla MLP ($\mathcal{O}(\mathrm{MLP})$). The graph diffusion preprocessing is non-parametric and executed once, incurring no message-passing overhead at train or test time. This is a clear practical advantage over distillation-based methods (GLNN, NOSMOG) that require a GNN teacher during training, making the comparison fairer for the claimed category.

- **Comprehensive evaluation in under-explored settings.** The paper evaluates in transductive, inductive, and cold-start settings — the latter is particularly underexplored, and InfoMLP's consistent advantage there demonstrates robustness when graph structure is absent at inference.

## Weaknesses

### Fatal
None.

### Major

- **The connection between the two-step optimization and maximizing $I(Z_{\mathrm{mlp}}; A)$ is heuristic, not rigorous.** The paper claims the two-step procedure — (1) constructing $X_{\mathrm{aug}}$ to minimize $H(A|X_{\mathrm{aug}})$ and (2) maximizing $I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}})$ — "allows us to maximize $I(Z_{\mathrm{mlp}}; A)$" (Section 3.3). However, no formal inequality chain or Markov assumption is provided to connect maximizing $I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}})$ to maximizing $I(Z_{\mathrm{mlp}}; A)$. (Note: the specific chain "$I(Z_{\mathrm{mlp}}; A) \geq I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}})$" that the harsh reviewer attributes to the paper does **not** appear in the text — the only explicit inequality is $I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}}) \geq I(Z_{\mathrm{mlp}}; Z_{\mathrm{aug}})$ in Eq. 6.) The overall framing is intuitive and the method works empirically, but the paper overclaims by presenting the procedure as a principled instantiation of MI maximization without the requisite formalism. The method would be more honestly described as "graph-conditional feature alignment."

- **The MI estimator in Eq. (7) is not justified as a valid lower bound on $I(Z_{\mathrm{mlp}}; Z_{\mathrm{aug}})$.** The loss combines MSE between normalized embeddings and a decorrelation penalty on $Z_{\mathrm{mlp}}$'s auto-correlation matrix. The paper cites "Zhang et al. 3" for this being an "MI maximizer based on feature decorrelation," but does not adapt the argument to this setting, derive the bound, or validate that optimizing this loss increases mutual information. In self-supervised learning, similar losses (Barlow Twins, VICReg) serve as *surrogates* for MI maximization under specific assumptions (e.g., invertible transformations, specific augmentations) that do not automatically transfer to the node-classification setting where $Z_{\mathrm{mlp}}$ and $Z_{\mathrm{aug}}$ are computed from the same MLP on $X$ and $X_{\mathrm{aug}}$ respectively. Without a formal connection, calling Eq. (7) an "MI maximizer" is misleading. The paper should either derive the bound, adopt a standard MI estimator (e.g., InfoNCE, accepting its $\mathcal{O}(N^2 D)$ cost on smaller graphs), or characterize the loss as a heuristic regularizer.

### Minor

- **Empirical improvements over strong baselines are modest on several datasets and lack statistical significance testing.** In the transductive setting (Table 3), InfoMLP's margins over GraphMLP/N2N are within one standard deviation on Cora, Citeseer, Pubmed, and Physics (e.g., Cora: 87.02±0.69 vs. GraphMLP 86.85±0.32; Pubmed: 88.72±0.50 vs. N2N 88.58±0.26). No statistical significance tests (e.g., paired bootstrap tests) are reported. Given the additional preprocessing cost and hyperparameter tuning, the paper should demonstrate the gains are robust, not noise. The cold-start setting shows more consistent advantages, which partially mitigates this concern.

- **$K$ in the graph diffusion is selected via validation accuracy (using labels) rather than the unsupervised $H(A|X_{\mathrm{aug}})$ metric.** The paper's analysis (Section 3.2) suggests $H(A|\hat{A})$ is a useful metric for characterizing datasets, but the method itself does not use this metric to guide design: $K$ is selected by evaluating validation performance (which uses labels). The paper would be strengthened by showing that the optimal $K$ according to $H(A|X_{\mathrm{aug}})$ (evaluated without labels) correlates with the best $K$ found via validation accuracy, making the preprocessing step truly unsupervised and deepening the connection between analysis and method.

- **The Gaussian assumption in Theorem 2 is stated without empirical verification.** Theorem 2 assumes that $\ell_2$ distances of positive and negative edges follow Gaussian distributions. This is a strong assumption for real-world graphs, and the paper provides no verification. While the theorem is presented as an analytical result under stated assumptions, the practical relevance would be clearer with empirical validation or a robustness discussion.

### Trivial
None (the notation inconsistencies noted by the harsh reviewer are OCR/parser artifacts, not present in the original submission).

## Nice-to-Haves

- A systematic analysis of when InfoMLP underperforms (e.g., on heterophilic graphs or datasets with very large $N$ relative to $d$) would strengthen practical guidance beyond the brief limitation note in the conclusion.
- Wall-clock time or scaling experiments on larger graphs (e.g., ogbn-arxiv) would confirm the claimed efficiency advantages.
- The paper notes the MI estimator reference; ensuring the citation is specific and complete in the camera-ready version.

## Removed Points

- The harsh reviewer's claim that the paper asserts the inequality chain "$I(Z_{\mathrm{mlp}}; A) \geq I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}})$" — this chain does **not** appear in the paper. The only explicit inequality is $I(Z_{\mathrm{mlp}}; X_{\mathrm{aug}}) \geq I(Z_{\mathrm{mlp}}; Z_{\mathrm{aug}})$ (Eq. 6). The paper's claim about maximizing $I(Z_{\mathrm{mlp}}; A)$ is a qualitative design claim, not a stated bound-chain. The underlying concern (insufficient theoretical rigor) is kept in Major, but the specific inequality accusation is removed as factually incorrect.

- "The paper does not discuss failure cases beyond the note in the conclusion" — the conclusion (Section 5, final paragraph) explicitly discusses the limitation: "when the graph structure is much more important than the features, and the node features cover almost no information of the graph structure, MLPs performance can hardly be improved." This qualifies as discussion of failure cases. The suggestion for a more *systematic* analysis is kept in Nice-to-Haves.

- Notation inconsistency complaints — these are PDF/OCR parser artifacts, not author errors.

## Novel Insights

The most interesting observation emerging from reading the reviews against the paper is the tension between the paper's rhetorical framing ("mutual information maximization") and its actual engineering contribution. The method's success likely comes from a concrete, well-tuned combination of graph-diffused features and a feature-alignment + decorrelation regularizer. The MI framing adds motivational clarity but risks overpromising theoretical rigor. If the paper repositioned its loss as "graph-conditional feature alignment" — an MSE objective that pulls node embeddings toward structure-informed targets plus a diversity penalty — the empirical story would be equally strong and scientifically more honest. This also explains why the method works well in cold-start settings: the alignment objective teaches the MLP to internalize structural patterns during training, which can then be invoked from features alone at test time.

## Suggestions

1. **Reframe the theoretical connection honestly.** Either provide the Markov assumptions and prove that maximizing $I(Z_{\mathrm{mlp}}; Z_{\mathrm{aug}})$ is a lower bound on $I(Z_{\mathrm{mlp}}; A)$, or reposition the method as "graph-conditional feature alignment" and drop the MI maximization language where it is not justified. The empirical results stand on their own either way.

2. **Validate or replace the MI estimator.** Demonstrate empirically that Eq. (7) correlates with estimated MI (using a separate estimator during training) or adopt InfoNCE on smaller graphs. At minimum, characterize the loss explicitly as a heuristic regularizer rather than an MI bound.

3. **Add statistical significance tests** (e.g., paired bootstrap) for the main results in Tables 3 and 4 to establish that gains over GraphMLP and N2N are reliable.

4. **Select $K$ using $H(A|X_{\mathrm{aug}})$ on a held-out edge set** and show this correlates with validation-accuracy-based selection, making the preprocessing step truly unsupervised.

## Score and Decision

The paper makes two real contributions: (1) an information-theoretic analysis that provides a tractable explanation for MLP-GNN performance gaps across datasets, and (2) a practically effective method (InfoMLP) that achieves strong results while maintaining MLP-level efficiency. The empirical evaluation is comprehensive across three settings, and the cold-start results are particularly convincing. The major weaknesses concern the rigor of the theoretical framing — the connection between the two-step optimization and MI maximization is heuristic, and the MI estimator is not justified as a bound. These are real issues that should be addressed, but they do not invalidate the paper's contributions. The method works, the analysis is insightful, and the paper advances understanding of when and why MLPs can succeed on graphs. With honest reframing and additional validation, this would be a strong paper.

**Overall assessment**: The paper has genuine contributions and strong empirical support. The theoretical overclaiming is a fixable issue (suggestion #1 above). I recommend acceptance with a request for revision to address the framing and estimator justification.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>