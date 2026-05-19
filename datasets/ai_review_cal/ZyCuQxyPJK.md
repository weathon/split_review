- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper introduces NeuroLifting, a method that reparameterizes MAP inference in Markov Random Fields using a Graph Neural Network. The decision variables are relaxed to continuous probability vectors output by a GNN, and the MRF energy function is used directly as a differentiable loss for gradient descent. The method is evaluated on synthetic, UAI 2022 competition, and real-world Physical Cell Identity (PCI) instances, showing competitive or superior results on large-scale MRFs compared to LBP, TRBP, and the exact solver Toulbar2.

## Strengths

- **Strong empirical results on large-scale and dense MRFs** – On synthetic high-order instances with 50k nodes (Table 2), NeuroLifting consistently outperforms Toulbar2 by wide margins (e.g., H_Instances_3: −3601.724 vs. +1423.823). On real-world PCI instances with 929–2000 nodes (Table 5), NeuroLifting achieves the lowest energy in all large cases, whereas LBP/TRBP/Toulbar2 plateau or produce worse solutions. These results demonstrate genuine practical value on problems where exact solvers and classical approximate methods struggle.

- **Principled connection between GNN reparameterization and lifting techniques** – The paper draws an explicit parallel between the GNN's message-passing and the lifting concept from optimization (Section 3.5), offering conceptual justification for why reparameterizing into a higher-dimensional continuous space aids optimization. The loss landscape visualizations (Figure 5) provide supporting evidence: deeper networks produce flatter landscapes with wider low-energy basins and lower converged loss.

- **Empirically validated GNN backbone selection** – The ablation study (Figure 4) compares GraphSAGE, GCN, and GAT across UAI, PCI, and synthetic datasets, showing that GraphSAGE achieves faster convergence and consistently lower loss. This is grounded in the symmetry requirement of MRFs (equal neighbor influence), demonstrating principled design rather than ad-hoc selection.

- **Demonstrated real-world applicability** – The PCI experiments (Table 5) show that NeuroLifting generalizes to a practical engineering domain with commercial relevance, outperforming all baselines on the largest instances.

## Weaknesses

### Fatal
None.

### Major

- **Complexity analysis is incorrect for high-order cliques.** The paper claims the loss computation cost is $O(|\mathcal{V}||\mathcal{X}| + c_{max}|\mathcal{C}||\mathcal{X}|)$ and asserts "linear computational complexity growth" (lines 184–185, abstract). However, the loss function (Eq. 6) requires computing $P_k = \otimes_{i\in C_k} p_i$, a tensor with $|\mathcal{X}|^{c_{max}}$ entries, and taking its inner product with the clique potential $\psi$, also of size $|\mathcal{X}|^{c_{max}}$. The true cost per clique is $O(|\mathcal{X}|^{c_{max}})$, not $O(c_{max}|\mathcal{X}|)$. This means the loss computation is exponential in clique size. While the method may still be practical when clique sizes are small (as in many real-world MRFs), the paper's central scalability claim is unsubstantiated for arbitrary-order high-clique MRFs, and no actual runtimes are reported to compensate for the incorrect analysis. **Impact**: the theoretical justification needs substantial correction; the empirical results remain valid but the framing of "linear complexity" is misleading.

### Minor

- **Claims are somewhat overstated relative to results.** The abstract claims "superior solution quality against all baselines" on large-scale MRFs, but on UAI pairwise instances (Table 3), NeuroLifting is consistently worse than Toulbar2 (which finds optimal solutions on Segmentation instances) and often only marginally better than LBP/TRBP. On UAI high-order instances (Table 4), NeuroLifting wins on only 1 of 5 instances against Toulbar2. On some 50k synthetic instances (Table 1: P_potts_7, P_random_7, P_random_9), LBP matches or very slightly outperforms NeuroLifting. These results are not a problem per se — the paper identifies where the method excels — but the blanket superiority claim should be tempered.

- **Rounding procedure is underspecified.** The paper states that after network convergence, assignments are obtained by "rounding the probabilities $p(\theta)$ to obtain binary vectors $v$" (line 171), but never specifies the rounding mechanism (argmax? sampling? threshold?). This matters because the gap between the relaxed loss $L(\theta)$ and the true energy $E(v)$ depends on the rounding strategy, and a poorly designed rounding could produce invalid assignments or inflated gaps.

- **No runtime or variance reporting.** The paper does not report wall-clock runtime for NeuroLifting on any instance, making it impossible to assess whether the claimed efficiency trade-off is realized. Nor does it report variance over random seeds or initializations, so it is unclear whether the results are stable. Both are standard reporting practices for empirical ML/optimization papers.

- **Padding strategy lacks empirical validation.** The paper pads energy tensors with the maximum original energy value (Section 3.2) to handle heterogeneous state spaces. While the strategy is intuitively sound (assigning high cost to padded states), the paper never verifies whether the final rounded assignments ever select padded (virtual) states, nor does it ablate the choice of padding value. An ablation on small instances where the optimal solution is known could confirm that the padding does not distort the objective.

### Trivial
None.

## Nice-to-Haves

- **Compare to a simpler gradient-based baseline** — The paper could strengthen the claim that the GNN architecture is essential by comparing to direct optimization of soft assignments (e.g., a parameterized $p_i$ per node without a GNN, or a standard MLP). This would isolate the benefit of the GNN's message-passing structure.
- **Report actual runtimes** for NeuroLifting vs. baselines to substantiate the efficiency claim, especially on the largest 50k-node instances where the complexity analysis is central to the contribution.
- **Validate the padding strategy** on small instances where the exact optimum is known, confirming that the minimizer of the padded loss never selects a padded state and that the reported energy values are comparable to those of solvers operating on the original problem.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing related work discussion (Harsh Critic, multiple locations):** Removed per policy — missing related works should not be cited without external confirmation.
- **"Complexity is linear" as a strength (Strength Finder #1):** Removed because the complexity analysis is shown to be incorrect for high-order cliques, so this claimed strength is not valid as stated.
- **"Generalizable padding scheme" as a standalone strength (Strength Finder #2):** Downgraded — included implicitly in the main review's acknowledgment of the method; the lack of validation prevents it from being a strong stand-alone strength.
- **Formatting-related nitpicks (e.g., bracket placement in Table 1):** Removed per policy as parser artifacts.
- **Speculative concerns about "could be an artifact" (Harsh Critic's padding critique):** The concern about the modified objective is valid as a point of missing validation, but the stronger claim that "the reported performance advantage could be an artifact" is unfounded — there is no evidence in the paper that the padding distorts results, and the method performs comparably on small instances where exact solutions are known.

## Novel Insights

The most interesting observation from the reviews is that the loss landscape visualization (Figure 5) provides concrete evidence linking network depth to optimization difficulty: deeper GNNs produce demonstrably flatter landscapes with wider basins. This connection between the "lifting" metaphor (optimization in higher-dimensional space) and empirical optimization geometry is a genuinely useful insight that goes beyond a simple performance comparison. It suggests that the GNN depth controls a trade-off between representational capacity and optimization smoothness, which could inform architecture design for similar neural-optimization methods.

## Suggestions

1. **Correct the complexity analysis** to replace $O(c_{max}|\mathcal{C}||\mathcal{X}|)$ with $O(|\mathcal{C}||\mathcal{X}|^{c_{max}})$ for the loss computation, acknowledge the exponential dependence on clique size, and report actual runtimes for all datasets to back the scalability claim empirically.
2. **Temper the claims** in the abstract and introduction to match the evidence: replace "superior solution quality against all baselines" with more nuanced framing that acknowledges strong performance on large-scale and dense MRFs.
3. **Specify the rounding procedure** (presumably argmax over the probability vector) and report the gap between $L(\theta)$ and $E(v)$ after rounding.
4. **Add variance estimates** (at least 5 runs) for a subset of instances to establish result stability.
5. **Include a padding validation** on small instances: confirm that the minimizer of the padded loss never selects padded states and that the solution matches the exact optimum.
