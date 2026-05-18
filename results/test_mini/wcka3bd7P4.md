Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces FROND (FRactional-Order graph Neural Dynamical network), a framework that replaces integer-order derivatives in continuous GNNs with Caputo fractional derivatives of order β>0. This enables non-Markovian (memory-dependent) feature dynamics during information propagation. The paper provides a theoretical analysis showing that F-GRAND-l (the linear diffusion variant) converges to the stationary distribution at a slow algebraic rate Θ(t^{-β}) rather than the exponential rate of integer-order models, which helps mitigate oversmoothing. The framework is demonstrated across multiple base architectures (GRAND, GRAND++, CDE, GREAD, GraphCON) on node and graph classification tasks.

## Strengths

- **Provably slower oversmoothing for the linear diffusion model**: Theorem 4 proves that F-GRAND-l converges to the stationary distribution at rate Θ(t^{-β}) for 0<β<1, whereas GRAND-l converges exponentially O(e^{-rt}). This is a concrete, rigorous mathematical advantage that directly addresses a central limitation of deep GNNs. The proof is properly scoped to the linear case and provides clear mechanistic insight.

- **Non-Markovian random walk interpretation with explicit transition probabilities**: Theorem 2 and Corollary 1 derive a rigorous connection between F-GRAND-l and a random walk whose transition probabilities depend on the full path history via coefficients c_k(β) and b_n(β). This goes beyond prior Markovian interpretations of graph diffusion and provides an intuitive explanation of how memory enters the dynamics.

- **Consistent empirical improvement across multiple base architectures**: F-GRAND variants outperform their integer-order counterparts on nearly all datasets tested (e.g., F-GRAND-l best on 7/10 node-classification datasets; F-CDE beats CDE on 5/6 heterophilic datasets). The framework is applied to five distinct backbones (GRAND, GRAND++, GraphCON, CDE, GREAD), demonstrating generalizability.

- **Empirical validation of oversmoothing mitigation**: Figure 2 shows that F-GRAND-l maintains stable accuracy across 8–128 layers on Cora, Citeseer, and Airport, while GRAND-l's performance degrades sharply. This directly corroborates the theoretical prediction of slower convergence.

- **Parameter-free compatibility**: The framework introduces no additional training parameters to backbone models—β is a tuned hyperparameter—making it a practical drop-in upgrade for existing continuous GNNs.

## Weaknesses

### Major

- **Theory covers only the linear diffusion variant (F-GRAND-l), but the broader narrative sometimes over-claims**: Theorem 4 and the random walk interpretation are explicitly scoped to F-GRAND-l (linear diffusion, Eq. 8). This is a significant limitation because practitioners typically use the nonlinear attention-based F-GRAND-nl, where the attention matrix A(X(t)) is time- and state-dependent. The paper does not provide theoretical guarantees for nonlinear variants. While the oversmoothing experiment uses F-GRAND-l, the abstract, introduction, and conclusion occasionally speak about "mitigating oversmoothing" and "addressing key challenges" in a way that implies FROND broadly—not just its linear subcase. This overreach weakens the claimed contribution.

- **Computational cost of the full-memory solver is not addressed**: The basic predictor solver (Eq. 4) requires evaluating {F(W,X^{(j)})}_{j=0}^{k-1} at every step, yielding O(K²) total cost for K steps. The paper mentions a "short memory principle" in the appendix (stripped) but the main experiments use the basic predictor. It is unclear whether the short memory approximation preserves the oversmoothing benefits, and no wall-clock time or memory benchmarks are reported. Without this analysis, the practical scalability of FROND for deep architectures is uncertain.

### Minor

- **Performance gains on standard benchmarks are modest**: On citation networks (Cora, Citeseer, Pubmed) and coauthor/co-purchase graphs, absolute improvements over GRAND are typically 1–3%, often within overlapping error bars. The paper's stated goal is not state-of-the-art but demonstrating consistent improvement, which it achieves. However, the modest margins mean the practical significance of switching from integer-order to fractional-order on non-fractal datasets is unclear.

- **Fractal motivation is not empirically operationalized**: The introduction motivates FROND by appealing to fractal graph datasets and connections between β and fractal dimension. However, the paper does not measure fractal dimensions of any dataset, nor does it show that optimal β correlates with any structural graph property beyond a qualitative observation about tree-structured data. The fractal motivation remains decorative.

- **Oversmoothing experiment lacks full experimental details in the main paper**: While the experiment clearly uses F-GRAND-l and reports results up to 128 layers, specifics about β values used, numerical step size h, and integration time T for the oversmoothing curves are not stated in the main text (presumably deferred to the stripped appendix). This makes the experiment harder to evaluate from the main paper alone.

- **Choice of β requires extensive tuning**: The optimal β varies widely across datasets (0.1 to 0.98). Since β is a hyperparameter requiring grid search jointly with other hyperparameters, this tuning cost is non-trivial. The paper does not discuss practical guidelines for β selection beyond validation-based tuning.

### Trivial

None.

## Nice-to-Haves

- An experiment measuring Dirichlet energy (or mean pairwise cosine similarity) over time for F-GRAND-l with different β values, directly verifying the Θ(t^{-β}) scaling predicted by Theorem 4.
- An ablation comparing full-memory vs. short-memory (with varying window sizes) on a representative dataset, showing that the oversmoothing benefits and accuracy gains are preserved with modest memory windows.
- t-SNE/PCA visualizations of node embeddings at different depths for F-GRAND-l vs. GRAND-l to visually demonstrate the delayed collapse.

## Removed Points

- **Criticism that the oversmoothing experiment likely used F-GRAND-nl**: The paper explicitly states "F-GRAND-l maintains a consistent performance level across all datasets" in Section 4.3. The reviewer misread this section.
- **Criticism about F-CDE identical performance on Questions being "suspicious"**: The optimal β for Questions is 1.0, meaning F-CDE = CDE mathematically. Identical results are expected and correct.
- **Missing appendix content (solver details, model formulations)**: The parser strips these; they exist in the original submission.
- **Pure formatting nitpicks and demands for datasets/results the paper's appendix covers**: Removed per instructions.
- **"No additional training parameters" criticism about hyperparameter search cost**: The claim is technically correct (no learned parameters); hyperparameter tuning is standard in this field.
- **Requirement for comparison with GRU/LSTM-based memory mechanisms**: Outside the paper's stated scope of fractional calculus integration into continuous GNNs.
- **Demand for statistical significance tests on 1-3% margins**: Not standard practice for these benchmarks.

## Novel Insights

None beyond the paper's own contributions. The core insight—that fractional derivatives introduce memory-dependent dynamics that provably slow convergence to stationarity in graph diffusion—is well articulated by the paper itself. The non-Markovian random walk interpretation (Theorem 2) is the most original conceptual contribution, as it makes the abstract fractional calculus concrete through explicit history-dependent transition probabilities.

## Suggestions

1. **Scope the oversmoothing claim precisely to F-GRAND-l** in the abstract and conclusion, and acknowledge that nonlinear variants require separate analysis. An empirical Dirichlet energy comparison for F-GRAND-nl would strengthen the paper considerably.

2. **Add a controlled experiment comparing full-memory vs. short-memory** with different window sizes on one dataset (e.g., Cora), reporting both accuracy and wall-clock time. This is essential for establishing practical viability.

3. **Include a "practical guidelines" section** discussing how β should be selected and noting the relationship between optimal β and dataset properties (even if only qualitative).

4. **Report h (step size) and T (integration time)** explicitly in the oversmoothing section for reproducibility.

## Score and Decision

**Anchor comparison (all retrieved):**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| Residual Connections & Normalization | i8vPRlsrYu.md | 7.00 | Stronger paper: cleaner experiments, more direct practical implications, though similarly limited to linearized analysis. FROND has more novel theory but weaker empirical validation. |
| DMD-GNN | duGygkA3QR.md | 6.60 | Comparable: both connect GNNs to novel mathematical frameworks. DMD paper has broader experiments; FROND has deeper theoretical analysis for the linear case. |
| Fractal-Inspired MPNN | zPoW8CajCN.md | 5.50 | Comparable: both have interesting cross-disciplinary ideas with modest empirical gains. FROND has stronger theory; fractal nodes paper has cleaner experiments. |
| Continuous Spiking Graph ODE | OXKJtrfH5n.md | 4.50 | FROND is stronger: clearer narrative, better-grounded theory, more extensive experiments. |
| GNN as Mean Field Game | mxkm1Pr2PM.md | 5.33 | Comparable: both propose novel mathematical frameworks for GNNs. FROND has more concrete experimental validation. |
| PoincareNorm | jrKPOQBq9i.md | 3.75 | FROND is substantially stronger: more novel idea, better theory, more comprehensive experiments. |
| Graph Reconstructability | 83w0LPowHz.md | 4.00 | FROND is stronger: more impactful contribution, better empirical support. |

**Assessment**: The paper presents a genuinely novel idea—replacing integer-order derivatives with fractional ones in continuous GNNs—and supports it with a clean theoretical analysis for the linear diffusion case. The non-Markovian random walk interpretation is elegant and provides clear mechanistic insight. The experimental validation covers multiple architectures and datasets. However, the contribution is meaningfully constrained by: (1) the theory applying only to the linear variant while the narrative occasionally over-claims, (2) unaddressed computational cost concerns for the full-memory solver, and (3) modest performance gains on standard benchmarks. The paper is a solid contribution that would benefit from sharper scope boundaries and scalability analysis before archival publication.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>