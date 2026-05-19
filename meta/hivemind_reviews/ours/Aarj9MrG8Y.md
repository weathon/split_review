## Summary
This paper identifies a convergence condition (absolute summability of power-series coefficients) and a Lipschitz stability condition for graph filters in GNNs, frames these as a "universal learning principle" for infinite-depth GNNs, and instantiates the principle in APGNN—a model using exponentially decaying aggregation weights with a P-hop filter. Theoretical generalization bounds are derived under a continuous graph setting, and experiments on 8 benchmark datasets report strong results.

## Strengths
- **Theorem 1 provides a clean necessary-and-sufficient condition for convergence of power-series graph filters**: The paper rigorously proves that \(\sum_{k=0}^{\infty}\theta_{k}\tilde{\mathbf{A}}^{k}\) converges uniformly and absolutely iff \(\sum_{k=0}^{\infty}\theta_{k}\) converges absolutely (Section 4.1). This is a precise theoretical criterion that prior work on learnable polynomial filters (DAGNN, GPR-GNN) did not explicitly articulate, and it directly enables principled design of provably convergent deep GNNs.

- **The P-hop filter with exponentially decaying weights is a practical instantiation that follows the principle**: APGNN's design (equation 15) uses \(\theta_{k}=\beta_{k}\alpha^{k}\) with \(|\beta_{k}|\leq 1, 0<\alpha<1\), ensuring \(\|\theta\|_{1}\leq 1/(1-\alpha)\). The truncation error bound \(\|\text{g}_{\beta}^{\infty}(\mathbf{L})-\text{g}_{\beta}^{K}(\mathbf{L})\|_{2}\leq \alpha^{K+1}/(1-\alpha)\) (equation 13) is graph-size-independent and controllable. The P-hop extension (Section 4.3) provides an analysis showing \(K\) can be reduced by increasing \(P\), which the experiments validate.

- **Empirical performance is strong across multiple benchmarks**: Table 1 shows APGNN achieves the highest average accuracy on 6 of 8 datasets and is second on the remaining two, covering both homophilic (Cora, Citeseer, Pubmed) and heterophilic (Cornell, Texas, Wisconsin) settings.

- **Unification of existing GNNs under the proposed framework**: Section 4.2 usefully characterizes which prior methods satisfy (PPNP, GPR-GNN) or violate (DAGNN) the convergence condition as \(K\to\infty\), providing a clear conceptual framework.

## Weaknesses
### Fatal
None.

### Major

- **Missing per-dataset hyperparameter specifications undermine reproducibility**: The paper reports main results in Table 1 without stating which values of \(K\), \(\alpha\), and \(P\) were used for APGNN on each dataset. The parameter studies (Figures 2–3) show that performance varies substantially with these choices (e.g., \(\alpha\) between 0.1 and 0.99 yields accuracy differences of 10+ points; \(K<10\) is suboptimal on Cora/Citeseer/Pubmed). Without this information, the reported results cannot be independently verified or reproduced. Additionally, the phrasing "we also applied our optimal hyperparameters to [the baselines], selecting the maximum value to display" (Section 6.1) is ambiguous — it could mean hyperparameters tuned for APGNN were used on baselines, which would be unfair to the baselines. This needs clarification regardless of intent.

- **Unusually large gains on heterophilic datasets lack explanatory analysis**: On Cornell, APGNN achieves 90.91% vs. 82.70% (GPR-GNN, +8.21pp); on Texas, 88.46% vs. 70.19% (GPR-GNN, +18.27pp); on Wisconsin, 88.46% vs. 79.41% (GPR-GNN, +9.05pp). These margins are far outside typical variance for these small but well-studied datasets. The paper offers no analysis of the learned filter shapes, no ablation of the decay mechanism (e.g., fixing \(\alpha=1\) to disable decay), and no explanation for why exponential decay—which heavily penalizes high-order information—produces such large improvements precisely on heterophilic graphs where distant neighbors often carry useful class information. The mechanism that drives these gains remains unsupported, and without it the results look anomalous.

- **The generalization bound comparison with GPR-GNN is mathematically flawed**: The paper claims (Proposition 1 discussion, line 255) that for GPR-GNN, \(M=1\) and \(L_{M}=K\), then concludes APGNN has "stronger generalization." However, GPR-GNN's constraint is \(\sum\theta_{k}=1\) (equation 11), and the paper acknowledges \(\theta_{k}\) can be negative (line 136: "the learned parameter \(\theta_{k}\) is permitted to have negative values"). Therefore \(\|\theta\|_{1}=\sum|\theta_{k}|\) can be arbitrarily larger than 1 even though the sum equals 1, so \(M=1\) is not a valid bound on \(\|\theta\|_{1}\). Similarly, the Lipschitz constant \(L_{M}=\sum k|\theta_{k}|\) can be much larger than \(K\). This makes the claimed generalization advantage over GPR-GNN unsubstantiated. The comparison with DAGNN is unaffected by this issue.

### Minor

- **The "universal learning principle" framing overstates the novelty of the core mathematical condition**: The two requirements in (6)—absolute summability of coefficients and Lipschitz continuity—are a direct application of the Weierstrass M-test and basic calculus (Lemma 1 → Theorem 1). The paper's real contribution is in *identifying and applying* these conditions to GNN design, not in the conditions themselves. The "principle" framing inflates the novelty unnecessarily.

- **The generalization bound (Theorem 2) depends on uncharacterized constants**: The bound involves constants \(C\) (related to the graph function) and \(c_{\mathcal{X}}\) (a data-dependent constant), and the transition from the continuous graph operator to the discrete empirical graph is not formally justified beyond stating that the same parameters are shared. While the bound provides useful qualitative insight into how APGNN's complexity scales with \(K\), its practical tightness is unclear.

- **The paper does not discuss train/validation/test splits for the heterophilic datasets** (Cornell, Texas, Wisconsin), which is standard practice to ensure results are comparable with prior work.

### Trivial

- None that survive filtering.

## Suggestions
1. **For every dataset in Table 1, report the specific \((K, \alpha, P)\) values used for APGNN** (or the selection procedure, e.g., grid search ranges and validation criterion). This is the single most impactful change for reproducibility.

2. **Clarify the baseline hyperparameter procedure**: Rewrite "we also applied our optimal hyperparameters to them" to specify whether each baseline was tuned independently or whether APGNN's hyperparameters were reused for other methods.

3. **Add an analysis of the heterophilic results**: Show learned filter shapes for Cornell/Texas/Wisconsin, run an ablation with \(\alpha\) fixed to 1 (no decay), and explain how the negative \(\beta_k\) + P-hop mechanism enables the reported gains.

4. **Fix the GPR-GNN bound comparison**: Either compute the actual \(\|\theta\|_1\) and Lipschitz constant for GPR-GNN (or upper-bound them honestly), or remove the explicit comparison and restrict the claim to APGNN's own bound being favorable (which does not depend on comparison).

5. **Report data splits** (train/validation/test ratios) for all datasets, especially the small heterophilic ones.

## Score and Decision

The paper makes a real theoretical contribution—identifying the convergence condition for power-series GNN filters—and instantiates it in a clean, well-motivated model with strong empirical performance. However, the experimental validation has three significant gaps: (1) unreported hyperparameters that prevent reproducibility, (2) unexplained large gains on heterophilic graphs that need mechanistic analysis, and (3) a flawed generalization bound comparison with GPR-GNN that undermines a claimed advantage. These are addressable in revision but weaken the paper as submitted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
