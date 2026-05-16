Now I have a comprehensive understanding. Let me write the final review.

## Summary

This paper identifies a novel problem — that strongly connected subgraphs (not just bottlenecks) can restrict information flow in standard GNNs — and formalizes this as a lack of *multi-scale consistency* at both the node level (propagation remains connected across scales) and graph level (features are stable under resolution coarsening). It proposes ResolvNet, a spectral architecture using resolvents of the graph Laplacian, and provides rigorous theoretical guarantees (Theorems 2–4) that ResolvNet approximates propagation on a coarse-grained graph when connectivity scales are well separated. Experiments on node classification benchmarks and molecular property prediction (QM7) show competitive or superior performance, and a hydrogen-deflection experiment demonstrates the claimed stability to resolution changes.

## Strengths

1. **Novel problem identification with rigorous theoretical analysis.** The paper identifies a genuinely counter-intuitive phenomenon — that strongly connected subgraphs, which one might expect to *help* information flow, actually create a disconnection problem in standard GNNs. This is formalized cleanly through spectral decomposition of the graph Laplacian (Section 2.1, Definition 1–2) and supported by an analytical derivation showing how GCN's normalized adjacency degenerates in this setting (Equation 1, Fig. 1).

2. **Theoretical proof of multi-scale consistency (Theorems 2–4).** The central theoretical result (Theorem 2) establishes resolvent convergence: $\|R_z(\Delta) - J^\uparrow R_z(\underline{\Delta}) J^\downarrow\| = \mathcal{O}(\lambda_{\max}(\Delta_{\text{reg.}})/\lambda_1(\Delta_{\text{high}}))$, which is a non-asymptotic bound that is novel in the GNN literature. Theorems 3 and 4 extend this to node-level and graph-level stability, providing the first provable multi-scale consistency guarantees for a GNN architecture.

3. **Empirical demonstration of graph-level stability to resolution change.** The hydrogen-deflection experiment (Fig. 3, Table 3) is the paper's most compelling empirical contribution: as hydrogen atoms are moved toward heavy atoms (increasing scale separation), ResolvNet's graph-level features converge to those on the coarse-grained graph, while all baselines fail to do so. On coarse-grained QM7, ResolvNet achieves MAE 16.23 vs. the next best baseline at 124.53 — a 7.7× improvement — directly verifying Theorem 4.

4. **Strong performance on standard node classification benchmarks.** Table 1 shows ResolvNet achieves top-1 accuracy on 4 out of 8 datasets (MS Academic, Cora, Pubmed, Citeseer) with statistically significant margins over strong baselines like PPNP and BernNet, and is competitive on heterophilic graphs despite its inductive bias toward homophily.

5. **Principle-based architecture design.** Unlike many spectral methods whose filter bases are chosen heuristically, ResolvNet's use of resolvent filters is directly motivated by the convergence theory. The Type-0 vs. Type-I distinction (Theorem 3) provides a principled choice between signal-lifting and signal-projection, a nuance absent in most spectral GNNs.

## Weaknesses

### Fatal
None.

### Major

1. **The decomposition $W = W_{\text{reg.}} + W_{\text{high}}$ is given as a conceptual framework but not operationalized.** The paper provides two illustrative examples (large weights, dense blocks) and a spectral definition, but never specifies how to obtain this decomposition for a real graph in practice. For the QM7 experiments and the hydrogen-deflection experiment, the decomposition is naturally induced by geometry/distance, but this is not made explicit. For standard unweighted benchmarks (Cora, Citeseer, etc.), it is unclear whether a meaningful decomposition even exists, which weakens the connection between the theoretical framework and those experiments. While the paper's theoretical contributions stand independently, the practical applicability of the multi-scale framework is underspecified, which limits reproducibility.

2. **Missing experimental details on the QM7 setup.** The QM7 baseline MAEs (~59–61 for GCN, ChebNet, ARMA) are reported without information about train/val/test splits, hyperparameter tuning procedures, or whether all methods used the same preprocessing and splits. While the paper is comparing general-purpose GNNs (not specialized molecular property predictors), the dramatic gap between ResolvNet (16.52) and the baselines cannot be properly interpreted without knowing whether the baselines were reasonably tuned. The paper states ResolvNet's advantage comes from multi-scale information propagation — but without ablations (e.g., removing node weights, changing the resolvent shift, comparing Type-0 vs. Type-I on QM7), the attribution is speculative.

### Minor

1. **The clique-duplication experiment is too narrow.** The central motivational experiment (Fig. 2, Fig. teaser) only tests GCN on Citeseer. To establish that the strongly-connected-subgraph problem is general, the experiment should be replicated on multiple architectures (GAT, ChebNet, ARMA, etc.) and multiple datasets. As it stands, the paper's motivating claim is supported by a single data point.

2. **Node weights $\mu_i$ for standard (unweighted) node classification benchmarks are not specified.** The paper clearly sets $\mu_i = Z_i$ (atomic charge) for QM7, but for Cora, Citeseer, Pubmed, etc., it never states what $\mu_i$ are. If they are uniform (all 1s), this should be stated explicitly; if derived from degrees or something else, that should be justified. This omission affects reproducibility.

3. **Hyperparameter values for ResolvNet are not reported.** The number of filter terms $K$, the resolvent shift $z$, network depth, and whether the same hyperparameters were used across all datasets are not stated. Similarly, baseline hyperparameters and tuning procedures are absent.

4. **The coarse-graining experiment (Table 3) is striking but the baselines are evaluated entirely out-of-distribution without retuning.** The paper correctly frames this as testing robustness to resolution shift, and ResolvNet's advantage is genuine. However, the paper would be strengthened by also reporting whether retrained baselines on coarse-grained data show any recovery, to distinguish "inability to handle distribution shift" from "structural property of the architecture."

5. **No discussion of computational cost.** Computing resolvent polynomials involves either inverting $(\Delta - zI)$ (which is $O(N^3)$ in the worst case) or iterative methods. The paper does not discuss practical complexity, limits, or approximations for large graphs.

6. **Figure 3 (feature vector differences) is qualitative only.** No error bars or numerical values at the maximum perturbation are reported.

### Trivial
- The sentence "The fairly involved proof of Theorem 2... by establishing omni-directional transferability" on line 305–310 appears to have a grammatical issue (seems to be missing a main clause).

## Nice-to-Haves
- An ablation study isolating the effect of the resolvent filters (e.g., replacing them with polynomial filters while keeping the architecture identical) would substantially strengthen the causal claim that multi-scale consistency drives the performance gains.
- A discussion of how to detect multi-scale structure in a given graph and validate the condition $\lambda_1(\Delta_{\text{high}}) \gg \lambda_{\max}(\Delta_{\text{reg.}})$ would make the framework more practically useful.
- A comparison of Type-0 vs. Type-I filters on real tasks would validate whether the theoretical distinction matters in practice.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *"The QM7 baselines are essentially random-guess level; even simple kernel methods have reported MAEs around 10–15."* — This evaluates the paper against specialized molecular prediction models (SchNet, DimeNet, etc.) when the paper explicitly states it is comparing against *non-specialized graph neural networks* (line 524–526). The comparison is fair across the methods tested; the paper never claims SOTA on QM7.

2. *"The margins over PPNP and BernNet on node classification are often within one standard error."* — Factually incorrect. For Cora: ResolvNet 84.16±0.26 vs. PPNP 83.77±0.27 (≈1.4σ gap). For Pubmed: 79.29±0.36 vs. PPNP 78.42±0.31 (≈2.3σ gap). The margins are statistically significant.

3. *"The proofs of Theorems 3 and 4 are not provided."* — These are in the appendix, which is stripped by the PDF parser. The rules require removing criticisms about missing appendix content.

4. *"Theorem 1 (approx_theorem) does not add much."* — This is a matter of opinion about a supporting result. It does not threaten any core claim.

5. *"The coarse-graining experiment baselines may not have been tuned for this setting."* — This misunderstands the experiment: models are pre-trained on original data and tested OOD without retraining. That is the intended test of resolution robustness, not a failure to tune.

6. *"The paper's claim that it 'out-performs baselines significantly on many tasks' should be tempered."* — On the homophilic graphs where ResolvNet's inductive bias is designed to help, it achieves top-1 on all four datasets with statistically significant margins. The claim is accurate.

7. *"Missing related work"* — Rule prohibits mentioning missing related works.

## Novel Insights

The reviews surface an important tension in this paper: the theoretical framework requires an explicit decomposition $W = W_{\text{reg.}} + W_{\text{high}}$ that satisfies a spectral gap condition, yet the experiments on standard benchmarks apply ResolvNet without using this decomposition at all. This suggests that ResolvNet's good performance on standard benchmarks may stem from properties of resolvent filters that are *related to* but not necessarily *identical to* the multi-scale consistency property. A natural follow-up would be to characterize what other inductive biases resolvent filters introduce beyond multi-scale consistency — for instance, whether they implicitly implement a form of low-pass filtering with a learnable cutoff determined by $z$, which could explain their strong performance on homophilic graphs independent of multi-scale structure.

## Suggestions
1. Specify how the decomposition $W = W_{\text{reg.}} + W_{\text{high}}$ is obtained in practice (e.g., thresholding edge weights by a quantile) and state whether any decomposition was used for the standard node classification benchmarks.
2. Report train/val/test splits, hyperparameters ($K$, $z$, depth, learning rate), and tuning procedures for all experiments, especially QM7.
3. State node weights $\mu_i$ for all datasets, including unweighted benchmarks.
4. Expand the clique-duplication experiment to include at least 2 additional architectures and 2 additional datasets.
5. Include a brief discussion of computational complexity (cost of computing resolvents, possible approximations).
6. Add error bars or a table to the hydrogen-deflection experiment (Fig. 3).

## Score and Decision

This paper presents a genuinely novel problem, a principled theoretical framework, and a new architecture with rigorous guarantees. The main weakness is not in the core contribution but in the presentation of experiments: several important details (decomposition methodology, node weights for standard benchmarks, hyperparameters, baseline tuning) are omitted, and some experiments are narrower than ideal. These are addressable in a revised version. The theoretical contribution — establishing resolvent convergence as a mechanism for multi-scale consistency in GNNs — is significant and well-supported.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>