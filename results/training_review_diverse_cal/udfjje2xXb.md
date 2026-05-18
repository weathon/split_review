Now I have verified the relevant content thoroughly. Here is my consolidated final review:

---

## Summary

This paper proposes GKAN (Graph Kolmogorov–Arnold Network), which extends KAN-style learnable spline-based activation functions to graph neural networks. The key idea is to replace fixed activation functions in message-passing GNNs with learnable B-spline functions on edges, resulting in the layer-wise update rule `x_i^(l) = φ(∑ φ(x_j^(l-1)))`. Experiments on node classification, link prediction, and graph classification (three citation datasets + two molecular datasets) show GKAN outperforming GCN, GAT, and GraphSAGE on 7 of 8 tasks. The paper also claims inherent interpretability by visualizing the learned spline values on edges.

## Strengths

- **Novel architecture combining KANs with GNNs**: GKAN is the first work to apply KAN-style learnable spline activations to graph-structured data, providing a clear layer-wise formulation (Eq. 6, Section 2.2). This opens a new direction for combining spline-based representations with message-passing mechanisms.

- **Consistent empirical improvement across tasks**: GKAN achieves the best result on 7 of 8 benchmark comparisons (Table II), with gains of up to 13.9% on MUTAG (85.0 vs. 75.1 for GAT). Results are averaged over 100 runs, and hyperparameters were tuned via grid search (Section 3.2), providing non-trivial evidence of improvement.

- **Transparent reporting of limitations**: The paper explicitly acknowledges memory scaling issues, the lack of edge feature support, and the extreme computational cost (Table III: 2.052s/epoch vs. 0.0016s for GCN), as well as the nuanced statement about interpretability in the Limitations section. This honesty is commendable.

- **Interpretability visualization**: The paper provides a concrete example (Figures 2–3) showing learned spline values on graph edges for a node classification prediction, contrasted with GNNExplainer's post-hoc edge masks. The qualitative comparison illustrates the conceptual difference between inherent vs. post-hoc explanations.

## Weaknesses

### Fatal
None.

### Major

- **Internally contradictory interpretability claim**: The abstract states that GKAN "inherently provides clear insights into the model's decision-making process, eliminating the need for post-hoc explainability techniques" and the contributions list says "GKAN provides inherent interpretability by design." Yet the Limitations section (Section 5.1) explicitly says: "We want to make clear that we do **not claim** that GKAN is interpretable, but that it is **more interpretable** than other models." These are incompatible positions and the paper never resolves this tension. Furthermore, the interpretability evidence is purely qualitative — a single node's normalized edge weights with no comparison to GAT attention weights (which also provide inherent edge importance), no faithfulness metrics, no user study, and no demonstration that the "piecewise polynomials can be easily visualized and understood" (the actual spline functions are never shown). Since interpretability is a central claimed contribution, this undermines the paper's core narrative.

- **Dataset table contains a factual error that undermines trust**: Table I lists PubMed with 3,327 nodes and CiteSeer with 19,717 nodes. These values are **swapped** — the standard Planetoid/PyG datasets have CiteSeer ≈ 3,327 nodes and PubMed ≈ 19,717 nodes (the edge counts and feature dimensions are also swapped correspondingly). A basic factual error about the most widely used GNN benchmarks raises serious questions about whether the correct datasets, splits, and preprocessing were used. The paper also uses 80/10/10 random splits (not the standard Planetoid fixed splits), but does not clarify this contrast or discuss reproducibility implications.

- **Experimental comparison is too narrow to support "outperforms state-of-the-art"**: Only three baselines are included (GCN, GAT, GraphSAGE, all 2017–2018). The paper itself mentions GIN and RGCN in the introduction but does not compare against them, nor against other strong modern baselines (GCNII, APPNP, GatedGCN). The reported gains over GAT on node classification are 1.2–2.8 percentage points, and **no standard deviations, confidence intervals, or significance tests are reported** despite averaging over 100 runs. Without variance estimates, these modest differences could plausibly arise from random variation, especially since the PubMed swap raises doubt about data fidelity.

- **Computational cost is documented but unexplored as a trade-off**: GKAN takes 2.052 seconds per epoch vs. 0.0016 for GCN on Cora — a ~1,280× slowdown. The paper acknowledges this but provides **no analysis** of the accuracy–cost trade-off: how accuracy varies with spline grid size, degree, or hidden dimension; whether cheaper configurations (smaller grid/degree) approach similar accuracy; or whether the cost is justified for the modest gains. Without this analysis, the computational overhead reads as a liability rather than a quantified engineering trade-off.

### Minor

- **Novelty is incremental**: The contribution is essentially a straightforward application of KAN-style activations to GNN message passing. The update rule `x_i^(l) = φ(∑ φ(x_j^(l-1)))` follows naturally from combining KAN's edge-wise activations with standard sum aggregation. There is no analysis of whether the Kolmogorov–Arnold theorem's theoretical guarantees (decomposition of multivariate functions into sums of univariate functions) are meaningfully preserved under graph-structured message passing. The paper reads as an engineering adaptation rather than a theoretically grounded extension.

- **No ablation on the spline components themselves**: The paper does not compare learnable B-splines against alternative learnable activation functions (e.g., PReLU, Swish with learnable parameters) in the same message-passing framework, making it impossible to attribute the gains specifically to splines rather than the increased parameter count or learnable activations generally.

- **The one failure case is unexplained**: GKAN underperforms GCN on PubMed link prediction (82.3 vs. 90.6), a 8.3-point gap. The paper mentions this but offers no analysis or hypothesis. For a paper claiming general superiority, explaining non-trivial failure cases is important.

### Trivial

- The abstract says "Our experiments on five benchmark datasets demonstrate that GKAN outperforms state-of-the-art GNN models" — but it is compared against only three baselines, and GAT is the only attention-based one. "State-of-the-art" is overclaimed relative to the actual comparison set.

## Nice-to-Haves

- Report standard deviations or confidence intervals for the 100-run averages.
- Include a quantitative interpretability evaluation: compare GKAN's inherent edge weights against GAT attention weights on faithfulness metrics (fidelity, sparsity) or correlation with ground-truth explanations where available.
- Add an ablation study showing accuracy vs. runtime across different spline grid sizes and degrees to characterize the trade-off.
- Include newer baselines (GIN, GCNII, APPNP) for a more competitive comparison.
- Show an actual visualization of the learned spline functions (piecewise polynomials) rather than just the normalized edge weights.

## Removed Points

These points were flagged for removal (treated with caution):

1. "The paper does not discuss prior work on learnable activation functions in GNNs or on spectral splines methods." — Removed per instruction: missing related works cannot be confirmed.
2. "Splines have coefficients, not scalar 'weights'" — Pure terminology nitpick; "weights" is used broadly and understandably.
3. "Hyperparameter inconsistency for link prediction / graph classification" — The paper adequately explains: node classification tuned on Cora, graph classification tuned on MUTAG, link prediction uses separately stated hyperparameters. Not a real inconsistency.
4. Various formatting/style nitpicks — Parser artifacts, not author errors.

## Novel Insights

The most interesting observation from the reviews is the fundamental tension the paper creates for itself: it wants credit for interpretability as a design feature (which requires strong claims in the abstract and contributions) while also wanting to be defensible and honest (which requires the hedging in the Limitations section). The paper never decides which claim it is actually making, and this indecision renders the interpretability contribution ambiguous regardless of which interpretation one adopts. The qualitative visualization is a start, but without quantitative grounding or a resolved stance, the paper falls into a "have your cake and eat it too" trap that weakens both the scientific and the rhetorical contribution.

## Suggestions

1. **Resolve the interpretability stance.** Decide between "inherently interpretable" (then prove it with faithfulness metrics, user studies, or symbolic function recovery) or "more interpretable than baselines" (then quantify the improvement with established XAI metrics and compare against GAT attention weights). The current contradictory framing cannot stand.

2. **Fix the dataset error** (Table I: swap PubMed and CiteSeer statistics) and specify exactly which splits (random 80/10/10 vs. fixed Planetoid) were used for each experiment. Provide the code or exact split indices for reproducibility.

3. **Add a simple ablation**: keep the GKAN message-passing framework but replace spline activations with standard activations (ReLU, PReLU) to isolate the effect of the spline. At minimum, this would clarify the source of the gains.

4. **Include variance estimates.** Since 100-run averages are already computed, reporting standard deviations is nearly zero additional cost and would significantly strengthen the empirical claims.

5. **Add at least 2–3 modern baselines** (GIN, GCNII, APPNP) — these are no harder to run than GCN/GAT given standard libraries, and would make the "outperforms state-of-the-art" claim credible.

## Score and Decision

The paper introduces a novel combination of KANs with GNNs and demonstrates consistent accuracy improvements across multiple tasks. However, the central interpretability claim is internally contradictory and unsupported; the experimental evaluation is too narrow and contains a factual dataset error that undermines trust; and the extreme computational cost is unanalyzed. These issues are addressable but substantial in their current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>