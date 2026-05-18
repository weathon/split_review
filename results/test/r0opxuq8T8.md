Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes HERTA, a training algorithm for Unfolded GNNs (specifically TWIRLS) that achieves a nearly-linear time convergence guarantee. The algorithm uses a preconditioner constructed via a new spectral sparsification method for normalized and regularized Laplacians, combined with SDD solvers, to simultaneously address two bottlenecks: per-iteration cost and poor convergence rate due to ill-conditioning. The main theoretical result (Theorem 1) gives a runtime of Õ((m+nd)c(log 1/ε)² + n_λλ²d + d³), which is essentially linear in the input size when the effective Laplacian dimension is not too large.

## Strengths

1. **Nearly-linear time convergence guarantee (Theorem 1)**: The paper proves that HERTA solves the TWIRLS training objective within ε accuracy in time Õ((m+nd)c(log 1/ε)² + n_λλ²d + d³), which is essentially linear in the input size up to log factors. This is a nontrivial theoretical contribution that directly supports the paper's claim of high efficiency with rigorous worst-case guarantee.

2. **Preservation of interpretability**: Unlike sampling-based methods that distort the original objective, HERTA converges to the optimum of the original training problem. Lemma 3 (after preconditioning) formally shows that a solution of the preconditioned problem maps back to a solution of the original problem with the same error rate, maintaining Unfolded GNN interpretability.

3. **New regularized spectral sparsifier (Lemma 3.3/4)**: The paper proposes a spectral sparsification method specifically tailored to normalized and regularized graph Laplacians (Ĵ + λ⁻¹I). It reduces edge count to O(n_λ/ε² log n), which is tighter than standard spectral sparsifiers (O(n/ε² log n)) when n_λ ≪ n. This is a genuine algorithmic contribution that enables the tighter runtime bound.

4. **Addresses both scalability bottlenecks**: The paper identifies two issues (slow iterations from full-graph computation, slow convergence from ill-conditioning) and designs HERTA to tackle both: using SDD solvers for fast inner-loop solving and a preconditioner to reduce outer-loop iterations. Most prior work addresses only the first issue.

5. **Empirical validation of convergence**: Experiments on Cora, Citeseer, Pubmed, and ogbn-arxiv demonstrate that HERTA reaches near-minimum training loss within ≤10 iterations for both MSE and cross-entropy losses, showing faster convergence than standard GD/Adam in terms of iteration count.

## Weaknesses

### Fatal
None.

### Major

1. **No wall-clock time measurements reported.** HERTA's iterations are significantly more expensive than standard gradient descent iterations: each gradient step requires two calls to an SDD solver on the full graph (Algorithm 1, lines 15-16) plus matrix multiplications involving the preconditioner. All experimental plots show loss versus *iterations*, not wall-clock time. A method that converges in 10 iterations but each iteration takes 100× longer than standard GD may not be practically faster. The paper claims to "verify the superiority of HERTA" and that it is "ready to use in practice" — but without wall-clock time, the practical significance of the convergence curves is uninterpretable. This is the single most important missing piece. The theoretical runtime bound (Õ(...)) is interesting, but the experiments as presented cannot distinguish between "converges faster in practice" and "converges in fewer iterations but each iteration is prohibitively slow."

2. **No test accuracy results reported.** For node classification on Cora, Citeseer, Pubmed, and ogbn-arxiv, test accuracy is the standard evaluation metric. The paper reports only training loss convergence. It is possible that HERTA's preconditioner and approximate gradient computation lead to worse generalization, or that faster training loss convergence does not translate to better models. Reporting training loss alone is insufficient to support claims of practical utility. The paper claims HERTA "is ready to use in practice" without providing a single test accuracy number.

### Minor

1. **No comparison against scalable training methods on realistic scales.** The paper motivates HERTA by arguing that sampling methods (ClusterGCN, GraphSAINT, etc.) distort the original objective, yet provides no experimental comparison against these methods on any metric (training time, memory, accuracy). Whether HERTA is competitive with or better than sampling approaches on realistic large graphs remains unknown. This weakens the practical narrative, though it does not invalidate the core theoretical claim (which is about accelerating the original objective).

2. **The claim of "universality" is overstated.** The paper concludes that HERTA "shows the universality of HERTA and verifies that it is ready to use in practice" based on training loss convergence on 4 datasets under MSE and CE loss with two optimizers (GD, Adam). This is a modest empirical validation, not universality. The practical scope (linear encoder f, MSE loss for theory, small-to-medium graphs without wall-clock time) is narrower than the conclusion suggests.

3. **The algorithm's practical complexity is high.** HERTA involves a custom spectral sparsifier (Algorithm 2), multiple SDD solver calls, a Hadamard transform, row subsampling, a matrix inverse square root, and preconditioned gradient iterations. The paper provides no ablation study showing which components are essential or how sensitive performance is to approximation parameters (e.g., the sparsifier accuracy ε). This limits practical adoption, though it does not undermine the theoretical contribution.

4. **No discussion of limitations.** The paper does not honestly discuss scenarios where HERTA might be slower or less applicable (small graphs where overhead dominates, very large λ, non-linear f, large number of classes c). The conclusion claims "ready to use in practice" without acknowledging these boundary conditions.

### Trivial

- The paper uses "universality" in a non-standard sense. Standard usage in ML refers to the ability to approximate any function; here it refers to working with different loss functions and optimizers. This is a language overclaim.

## Nice-to-Haves

- **Wall-clock time comparison** between HERTA and standard GD/Adam on the same datasets, showing time-to-convergence for a given loss threshold. This would directly address the most important experimental gap.
- **Test accuracy comparison** between HERTA-trained models and standard GD/Adam-trained models to verify that faster training convergence does not degrade model quality.
- **Comparison against a representative sampling method** (e.g., ClusterGCN) on a dataset where full-batch training is slow (e.g., ogbn-products), showing wall-clock time and accuracy trade-offs.
- **Ablation study** on the spectral sparsifier: how does convergence degrade if a standard (unregularized) sparsifier is used instead of the new regularized one? How sensitive is convergence to the sparsifier accuracy ε and the preconditioner approximation quality?
- **Empirical measurement of n_λ** for the datasets used, to ground the theoretical condition in practice.

## Removed Points

The following points from the reviewer inputs were removed per rules:

- **"Missing proofs in appendix / preprint-style referencing"**: Per instructions, appendix content is stripped by the parser and exists in the original submission. This criticism is not valid.
- **"Complexity bound contains hidden assumptions about n_λ = O(n/λ²)"**: The paper is fully transparent about this condition. It states explicitly (lines 32-33) that the condition is "not strictly necessary" and "used here to simplify," provides the full theorem without the condition (Theorem 1), and explains the origin of the condition. The reviewer's call for "more transparency" ignores the paper's own discussion.
- **"Theoretical scope is narrow (linear f, MSE loss)"**: The paper clearly states its assumptions (Section 4: "we consider a simple implementation of f which is a linear function") and dedicates a substantial discussion (Section 5.2) to explaining why HERTA works beyond this scope. This is scope clarification, not a weakness.
- **Strengths from Strength Finder that are generic or conflict with verified weaknesses**: The strength "Empirical validation across datasets and losses" is kept but its weight is reduced given the absence of wall-clock time and test accuracy. The strength "Theoretical explanation for cross-entropy effectiveness" is kept as stated.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's strong theoretical contribution (nearly-linear time training guarantee for Unfolded GNNs) and its weak experimental validation. The theory itself appears technically sound — the combination of regularized spectral sparsification with SDD solvers to construct a provably good preconditioner is genuinely novel. However, the paper positions itself as both a theory paper and a practical algorithm paper ("ready to use in practice"), and the experiments do not meet the standards of the latter genre. The single most impactful change would be wall-clock time measurements: if HERTA is actually faster in practice despite per-iteration overhead, the paper becomes much stronger; if not, the theory alone may be better suited to a theory-focused venue. This is a common pattern in theory-heavy ML papers that needs more discipline in separating theoretical contribution from practical claims.

## Suggestions

1. **Add wall-clock time convergence plots** for all datasets and methods. This is the single highest-leverage addition and directly determines whether the practical claims are supported.
2. **Report test accuracy** for all settings. Even if the primary claim is about training convergence, test accuracy reassures readers that the preconditioner does not harm model quality.
3. **Include at least one comparison against a sampling-based method** (e.g., ClusterGCN) on a larger dataset (e.g., ogbn-products or ogbn-papers100M) with wall-clock time. This would substantiate the claim that HERTA addresses the scalability problem practically, not just theoretically.
4. **Tone down the "ready to use in practice" and "universality" claims** in the conclusion, or provide the experimental evidence that would justify them.
5. **Include a brief limitation section** that honestly discusses when HERTA may not be the best choice (small graphs, very large λ, non-linear encoders, large c).

## Score and Decision

The paper's core theoretical contribution — a nearly-linear time training algorithm with convergence guarantees for Unfolded GNNs, enabled by a new regularized spectral sparsifier — is novel and technically interesting. However, the experimental evaluation is fundamentally insufficient to support the paper's practical claims: no wall-clock time, no test accuracy, and no comparison against scalable baselines. The paper is caught between being a theory paper (where the experiments would be adequate to validate the theoretical convergence rate) and a practical algorithm paper (where the experiments fall short).

Given that the theoretical contribution appears sound and novel, the paper has genuine value. However, the experimental gaps are large enough that the paper's claims of practical superiority are unsubstantiated. The paper would benefit from major revisions — specifically wall-clock time and test accuracy — before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>