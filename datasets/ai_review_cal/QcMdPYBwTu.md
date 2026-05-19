- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 3, 8
Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes SEIGNN, an implicit GNN designed for large graphs. It addresses two scalability bottlenecks of prior implicit GNNs (e.g., IGNN, MGNNI): (1) their reliance on full-batch training, and (2) the large number of iterations needed to solve the fixed-point equation. SEIGNN introduces coarse nodes derived from graph partitioning into mini-batches to preserve long-range information, and a stochastic unbiased solver (based on a Neumann series with Russian roulette estimation) that reduces iteration count. Experiments on six datasets show accuracy improvements over existing implicit and traditional GNNs, along with reduced training time.

---

## Strengths

1. **Empirical evidence that coarse nodes recover accuracy lost by naive mini-batch training.** Table 5 shows that directly applying Cluster-GCN or GraphSAGE mini-batches to an implicit GNN drops accuracy by 2–6% on several datasets, while SEIGNN's coarse-node approach substantially recovers these losses (e.g., 50.41% vs. 47.03% on Reddit). Table 4 confirms that removing coarse nodes degrades accuracy by 1–3% across all tested datasets, and Table 6 shows coarse nodes can even improve other mini-batch methods. Collectively this is strong evidence that the mini-batch design matters and that coarse nodes contribute meaningfully.

2. **Demonstrated scalability beyond prior implicit GNNs.** Table 2 reports that MGNNI runs out-of-memory on ogbn-products (2.5M nodes, 61M edges), while SEIGNN trains successfully and achieves 84.1% accuracy. This directly validates the claim that the mini-batch approach overcomes the memory barrier that prevents full-batch implicit GNNs from scaling to large graphs.

3. **Stochastic solver delivers wall-clock speedup with competitive accuracy.** Table 7 shows the stochastic solver (max 3 iterations, α=0.5) achieving 73.71% accuracy in 130.3 total seconds on ogbn-arxiv, while the original fixed-point solver requires 50 iterations to reach 73.49% accuracy in 503.2 seconds — a ~3.9× speedup with comparable accuracy. Proposition 1 formally establishes unbiasedness, and Table 4 shows replacing the stochastic solver with a truncated Neumann solver causes only a minor accuracy drop.

4. **Analysis of where coarse nodes help most.** Figure 3a/3b provides an insightful breakdown by node degree: the accuracy improvement from coarse nodes is concentrated in the lowest-degree quartile (~12% relative improvement) and negligible on the highest-degree quartile. This gives a concrete mechanism — coarse nodes supply missing global context to nodes that otherwise receive limited information in a sampled subgraph — and strengthens the paper's central claim.

---

## Weaknesses

### Fatal

None.

### Major

1. **No statistical significance reported for main results.** Tables 1 and 2 report only single accuracy/F1 numbers without standard deviations, confidence intervals, or run counts. On benchmark datasets like ogbn-arxiv, published results typically include standard errors (~0.2–0.5%). Without variance estimates, it is impossible to assess whether SEIGNN's gains over baselines are statistically meaningful or simply noise. This is the single biggest weakness in the evaluation.

2. **Missing reproducibility details for key design choices.** Several important hyperparameters and implementation decisions are not specified in the available text: the graph partitioning method used to create coarse nodes, the number of partitions \(k\), the truncation point \(t\) in Algorithm 1, and how mini-batch sizes are chosen. While some of these may appear in the appendix (which the parser strips), \(k\) and \(t\) are first-order parameters that directly control model behavior and should be reported. Without them, independent reproduction is difficult.

### Minor

1. **Evidence for long-range information capture is indirect.** The paper's central motivation is that coarse nodes preserve the ability of implicit GNNs to capture long-range dependencies under mini-batch training. The provided evidence (accuracy drop when coarse nodes removed, larger benefit for low-degree nodes) is consistent with this claim but does not isolate long-range propagation from other benefits of coarse nodes (e.g., increased model capacity or better gradient flow). A controlled experiment on a task with known long-range dependency requirements would strengthen the claim. The existing evidence is reasonable for a conference paper but leaves room for alternative explanations.

2. **Stochastic solver comparison in Table 7 does not control for expected cost.** The comparison pits a deterministic solver at various budgets (max iterations 5, 10, 50) against the stochastic solver with max 3 iterations. Because the stochastic solver continues sampling with probability α=0.5 after each step, its expected number of additional iterations beyond \(t\) is \(1/(1-\alpha) = 2\), making the expected total cost higher than the nominal "max 3." The wall-clock advantage (130s vs. 503s for 50-iteration solver) is large enough that the conclusion likely still holds, but reporting the expected/actual number of solver iterations would make the comparison cleaner.

3. **Missing analysis of stochastic solver variance and trade-offs.** Proposition 1 establishes unbiasedness, but the paper does not analyze estimator variance, its dependence on α and \(t\), or whether variance causes training instability. An empirical report of variance across runs or training loss trajectories would strengthen confidence in the solver.

4. **Coarse node features are not specified.** The paper creates coarse nodes and adds them to the graph but does not state whether these nodes have features (and if so, how they are initialized) or whether they receive trainable embeddings. If coarse nodes add learnable parameters not present in baselines, this could partially explain accuracy improvements without invoking long-range information. This should be clarified.

5. **Linear fixed-point formulation vs. broader implicit GNN scope.** The method is developed for the linear equation \(Z^{*} = \gamma g(W) Z^{*} S + f(X, \mathcal{G})\) (following MGNNI). However, the introduction and related work discuss implicit GNNs broadly, including non-linear variants (e.g., IGNN uses tanh). The paper should explicitly state this linearity assumption and discuss whether the stochastic solver and mini-batch approach extend to non-linear fixed-point equations.

### Trivial

- The reference "Table 5" in the efficiency comparison text (line 223) appears to conflict with "Table 3" in the caption; this should be corrected.

---

## Nice-to-Haves

- **Add standard deviations / error bars** to all main result tables and Figure 2 (this is listed as Major above, but addressing it would significantly strengthen the paper).
- **Report how PPR-based auxiliary node selection behaves on the augmented graph** — coarse nodes have high degree and may dominate PPR scores; a description of whether this biases auxiliary node selection would be helpful.
- **Sensitivity analysis on the number of partitions \(k\)** to guide practitioners on the robustness of this hyperparameter.
- **Memory usage comparison table** (the paper mentions lower GPU memory but the figure is not extractable from the text; a clear table would strengthen the scalability argument).
- **Verify the convergence condition for the stochastic estimator** (the condition \(\sum \gamma^k g(W)^k f(X,\mathcal{G}) S^k / \alpha^{k-t}\) requiring spectral radius \(< \alpha\) is not checked empirically).

---

## Removed Points

- **Criticism that Table 2 omits traditional baselines (GCN, GAT, GraphSAGE) on OGBN datasets:** Table 1 already includes these baselines on four other large datasets, and Table 2 is specifically framed as an implicit-GNN comparison. The paper already shows SEIGNN outperforms traditional GNNs on the datasets where they are compared. This criticism is scope creep.
- **Criticism about the "time per epoch" definition being unclear:** This is a parsing artifact; the figure caption exists in the original.
- **Criticism that missing variance analysis makes the stochastic solver comparison unfair:** The wall-clock comparison is valid and the speedup is large; this concern is addressed in Minor #2 above in a more measured way.
- **Criticism about missing memory usage figure:** The text clearly states "Figure 3, showing that SEIGNN has significantly less GPU memory usage" — the figure exists in the original submission but cannot be rendered from the extracted text. The criticism incorrectly treats this as absent.
- **Strength Finder point about "mini-batch training with coarse nodes is empirically shown to preserve long-range information"** — retained as a strength but with the caveat that evidence is indirect (see Minor #1).
- **Strength Finder point about Figure 3a/3b analysis** — retained as a strength.

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Report mean and standard deviation over at least 5 random seeds** for all main results (Tables 1, 2, 4, 5, 7). This is the most impactful improvement for establishing reliability.
2. **Clarify coarse node features:** explicitly state whether coarse nodes have features (e.g., zero vectors, aggregated partition statistics) or learnable embeddings. If the latter, quantify parameter count difference from baselines.
3. **Specify the graph partitioning method and the number of partitions \(k\)** used in experiments, and add a sensitivity analysis on \(k\) for at least one dataset.
4. **Specify the truncation point \(t\)** used in Algorithm 1 and provide the expected number of stochastic solver iterations alongside the "max 3" setting.
5. **Add a brief discussion** of the linearity assumption and whether the approach extends to non-linear implicit GNNs (e.g., those using activation functions inside the fixed-point equation).
