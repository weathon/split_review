## Summary

This paper proposes UO-Explainer, a unified framework that provides both model-level and instance-level explanations for GNN node classification by decomposing the classifier's weights and per-node predictions into linear combinations of graphlet-orbit basis vectors. The core idea is to use a pre-defined set of orbits (from graphlets of 2–5 nodes) as human-interpretable explanation units, learning orbit bases from the GNN's own node representations and then decomposing class weights into these bases to reveal which structural patterns drive predictions. The method is evaluated on five synthetic and three real-world datasets against multiple baselines.

## Strengths

1. **Unified framework delivering both model-level and instance-level explanations from a single decomposition.** The paper shows that decomposing class weights into orbit bases (Section 3.2, Eq. 3) directly extends to decomposing per-node prediction values (Section 3.3, Eq. 7), so the same learned orbit bases and class-orbit scores serve both explanation levels. Prior work (D4Explainer, GLGExplainer, GNNExplainer) requires separate mechanisms for each level. This is a principled and clean mathematical unification.

2. **Strong empirical results on non-tautological evaluation tasks.** On BA-Shapes and BA-Community (Table 2), the GNN classifies node positions within a house motif — a task fundamentally different from orbit membership — yet UO-Explainer correctly recovers orbits 56, 57, 58 (the house motif's positions) as the model-level explanation for each class. This demonstrates that the method can discover meaningful structural patterns that the GNN relies on, not just re-identify the training labels.

3. **High instance-level explanation quality across multiple synthetic and real-world datasets.** In Table 3, UO-Explainer achieves the highest Sub-recall across all five synthetic datasets (e.g., 0.998 on BA-Shapes vs. 0.822 for the next-best). On real-world datasets (Table 4), it achieves the best Fidelity on most tasks, and the qualitative Gene dataset case study (Section 5.5) connects the identified genes to known biology with supporting literature citations, demonstrating alignment with domain knowledge.

4. **Greedy selection algorithm addressing the non-uniqueness of overcomplete decomposition with 73 orbits.** When the number of orbits exceeds the embedding dimension, Eq. 4 admits infinitely many solutions. The greedy approach (Section 3.2, Eq. 6, Algorithm 2) iteratively selects the orbit minimizing the residual, providing a concrete technical fix for a genuine mathematical challenge that prior motif-based methods do not address.

5. **Demonstrated extensibility beyond the standard 2–5 node graphlet set.** For Tree-grid and Tree-cycle datasets (Section 5.4, line 208), the paper defines custom graphlets (grids, cycles) and incorporates them. Results in Table 3 show UO-Explainer still achieves top Sub-recall (0.991 and 0.972 respectively), validating that the framework is not brittlely tied to the 73-orbit canonical set.

## Weaknesses

### Fatal
None.

### Major

1. **The model-level evaluation on Random Graph datasets (Table 1) is a sanity check, not a discovery test.** Each task is "classify whether a node belongs to orbit $o_k$" — the ground-truth explanation is the orbit itself. The method learns orbit bases by training logistic regressors to predict orbit membership from node representations, then decomposes the class weight for "belongs to orbit $o_k$" into these bases. Finding that the corresponding orbit basis dominates the decomposition validates that the machinery works correctly, but it does not demonstrate discovery of genuinely unknown structural patterns. The BA-Shapes/BA-Community evaluation (Table 2) is stronger because the classification task (node position in a motif) is different from orbit membership — but the ground-truth structure (the house motif = graphlet $g_{23}$, orbits 56–58) still falls within the pre-defined orbit vocabulary, so even this test does not assess the method's ability to discover structures outside the orbit set. The paper would benefit from an evaluation where the GNN learns a task based on structures that are *not* expressible as any individual orbit in the vocabulary.

2. **The instance-level comparison is confounded by fundamentally different explanation formats.** UO-Explainer returns "a subgraph within the input graph that matches the highest-contributing orbit for the target node" (line 206) — a single, connected, pattern-matched substructure. Baselines return top-$k$ edge masks that are often disconnected. Metrics like Sub-recall (does the *entire* explanation match ground truth?) and Edge-recall (fraction of ground-truth edges captured) inherently favor UO-Explainer's format, because it directly searches for a subgraph matching a pattern, while baselines score edges independently. The paper controls for sparsity but does not control for this structural asymmetry in explanation format. Results on real-world datasets using Fidelity (Table 4) partially mitigate this concern, as Fidelity is less format-dependent, but the primary synthetic results (Table 3) should be interpreted with this caveat. This does not invalidate the method's utility, but the claim of "outperforming" baselines on these metrics conflates explanation quality with explanation format.

### Minor

3. **No computational cost analysis for the pre-processing step.** The paper lists baseline complexities (line 132) and asserts UO-Explainer is "less demanding" than D4Explainer and GNNExplainer, but never computes its own complexity. Enumerating all 0–72 orbits across all nodes requires checking each node against each of the 73 orbits by enumerating induced subgraphs of size 2–5. This pre-processing cost is non-trivial and unanalyzed. For practitioners evaluating scalability, this omission is material.

4. **No variance or significance measures reported.** Tables 1–4 report point estimates without standard deviations or confidence intervals. Given the small number of tasks per dataset (especially in Tables 1–2 where each Table cell is a single task), it is unclear whether UO-Explainer's advantages over baselines are statistically reliable or could vary across random seeds.

5. **The bias term in the prediction decomposition is not attributed to any orbit.** Equation 7 decomposes $z_{v_n,c_m}$ into orbit contributions plus an unattributed bias $b_{c_m}$. This means part of the prediction value is not explained by orbits, which should at least be discussed as a limitation of the decomposition's completeness.

6. **Human-interpretability is asserted rather than empirically demonstrated.** The paper motivates orbits as "human-interpretable units" appealing to prior use in network science, but provides no user study, domain expert evaluation, or systematic evidence that non-expert users can understand or act on explanations of the form "this node is important because it occupies orbit 56 in graphlet 23." The qualitative case study (Section 5.5) validates correctness, not interpretability relative to other explanation formats.

7. **The greedy selection stopping criterion is underspecified.** The paper states selection stops "when the difference between the class weight and the linear combination does not decrease" (line 110). It is unclear whether this means the residual stops decreasing (convergence plateau), begins to increase (overfitting), or reaches zero (exact fit). No sensitivity analysis of the stopping threshold is provided.

### Trivial

8. The "performance degradation is less than 5%" claim (line 189) when comparing the original GNN to the decomposed class-weight model is stated without a supporting table or figure.

## Nice-to-Haves

- **Replace the Random Graph orbit-classification experiment (Table 1) with a diagnostic that tests discovery of structures NOT in the orbit vocabulary.** For instance, train a GNN to classify nodes based on betweenness centrality, clustering coefficient, or community membership, where the ground-truth explanation is not orbit-identification. This would demonstrate that the method genuinely discovers meaningful patterns rather than re-identifying what it already knows.

- **Ablate the orbit basis construction.** What happens if orbit bases are replaced with random directions, one-hot encodings of orbit membership, or mean representations of nodes in each orbit? This would demonstrate that the specific learning procedure matters and results are not driven by arbitrary structure in the representation space.

- **Analyze greedy selection stability.** Report how many orbits are typically selected per class, how sensitive selection is to the stopping threshold, and whether the selected orbits are stable across random seeds or training runs of the underlying GNN.

- **Report failure-case analysis.** The paper notes (line 189) that UO-Explainer fails on tasks 33, 60, 62 with GCN. Which orbits are these? Is there a pattern (e.g., orbits requiring symmetric-position discrimination that GCN with mean pooling cannot handle)?

## Removed Points

The following points from the inputs were removed with justification:

- **Duplicated sentence on lines 187–188:** The original submission's PDF contains a sentence repeated twice ("We pre-train 2 or 3-layer GCN models..."). This is a likely parser artifact from PDF extraction of overlapping text; the original paper likely does not contain this duplication. Per the hard rules, formatting artifacts from parsing should not be treated as author errors.

- **"Self-validating" characterization of Table 1 as a fatal flaw:** The harsh critic labeled the Random Graph model-level evaluation as fundamentally invalidating the paper's core claims. This overstates the problem. The Random Graph evaluation is a sanity check that validates the decomposition mechanics; the paper's core empirical claims are also supported by the BA-Shapes/BA-Community evaluation (Table 2, where the task is NOT orbit classification) and by instance-level results across multiple datasets. The concern is real but downgraded to Major, not Fatal.

- **Framing the instance-level comparison as structurally "biased" in a way that invalidates all results:** The harsh critic suggested the comparison is "not informative" because of format differences. While the format asymmetry is a genuine concern, the paper controls for sparsity, and the real-world results (Table 4) use Fidelity — a metric less affected by format differences. The concern is retained as Major but not treated as invalidating.

- **Criticisms that demand user studies for "human-interpretability" claim:** While the claim is indeed soft, requiring a user study goes beyond the standard practice for GNN explainability papers at top venues. The qualitative evidence provided (literature-cited gene associations) is consistent with community norms. Retained as Minor.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper that goes beyond what the authors themselves articulate. The core tension — between the unified mathematical framework (a genuine strength) and the fundamentally different explanation format that makes direct comparison with edge-mask methods problematic — is already implicitly present in the paper's design choices, though not explicitly discussed by the authors.

## Suggestions

1. Add a diagnostic experiment where the GNN is trained on a structural property NOT capturable by any single orbit (e.g., node degree, clustering coefficient, community membership), and test whether the orbit decomposition still yields meaningful class-level patterns. This would directly address the concern that the current evaluation validates mechanics rather than discovery.

2. Report the wall-clock time and scaling behavior of the orbit enumeration pre-processing step so practitioners can assess practicality for large graphs.

3. Report standard deviations across multiple runs for all experimental results.

4. Acknowledge the bias term's unattributed contribution to the prediction decomposition as a limitation, or extend the decomposition to include it.

5. Discuss at least one failure mode or limitation of the orbit-based approach in the Discussion section.

## Score and Decision

The paper presents a genuinely novel idea — using graphlet orbits as unified, human-defined explanation units for both model- and instance-level GNN explanations — with a clean mathematical formulation. The unified framework is a principled contribution beyond what prior work offers. The empirical results are strong across multiple datasets and the qualitative validation is supportive. The major concerns are (a) that the model-level Random Graph evaluation is a sanity check rather than a discovery test, and (b) that the instance-level comparison format asymmetry makes some metrics favor the proposed method by construction. These are real but not fatal: the BA-Shapes/BA-Community evaluation (Table 2) and the real-world fidelity results (Table 4) provide genuine evidence of effectiveness. The paper would be strengthened by addressing the missing computational cost analysis, statistical reporting, and a diagnostic task outside the orbit vocabulary. Overall, the contributions outweigh the weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>