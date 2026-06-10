## Summary

The paper proposes iGraphMix, an Input Mixup method for node classification on graphs. To bypass the irregularity (variable-sized neighbor sets) and alignment (no natural ordering of neighbors) problems that prevented prior Mixup approaches from operating on graph inputs, iGraphMix uses masking matrices to randomly sample neighbors from each source node rather than interpolating adjacency matrices directly. The method mixes node features, labels, and edges via a stochastic neighbor-selection mechanism that generates virtual training nodes. Experiments across five datasets and three GNN backbones show average gains of 2.84% over no augmentation and 2.41% over M-Mixup.

## Strengths

- **Principled design that overcomes a real structural barrier.** The paper correctly identifies that irregularity (neighbor sets of varying sizes) and alignment (no natural ordering) prevent naive Input Mixup on graphs, and proposes a masking-matrix sampling scheme (Definition 4.1) that side-steps both issues. Instead of interpolating adjacency matrices—which is ill-defined when two nodes have different numbers of neighbors—iGraphMix randomly samples neighbors from each source node. This design choice is conceptually clean and directly addresses the problem it sets out to solve.

- **Consistent empirical gains across diverse settings.** The method outperforms no augmentation by an average of 2.84% across five datasets (CiteSeer, CORA, PubMed, ogbn-arxiv, Flickr) and three backbone models (GCN, GATv1, GATv2), and outperforms the strongest prior Mixup baseline M-Mixup by 2.41% (Table 1). Gains are largest precisely where regularization matters most: 5.22% improvement when only 40 labeled nodes per class are used, and 6.39% improvement for 8-layer GCNs (suggesting mitigation of over-smoothing). These patterns are internally coherent and strengthen the paper's claims.

- **Empirically validated versatility.** The method can be combined with DropEdge, DropNode, and DropMessage to produce additional improvements (1.86% average gain on CiteSeer, Table 2). This is a direct consequence of operating at the input level rather than on hidden representations, and the paper provides evidence for this claimed advantage.

## Weaknesses

### Fatal

None.

### Major

- **Core theoretical claim is unsupported: the bound depends on an unspecified quantity.** The abstract claims the paper "mathematically prove[s] that training GNNs with iGraphMix leads to better generalization performance compared to that without augmentation." However, Theorem 5.3 introduces a factor $c = Q(\alpha, A, X)$ where $Q$ is described as "the certain function of $(\cdot)$" and is never concretely specified. Since the standard GCN bound (Remark 3.1) is multiplied by $c$, we cannot determine whether $c < 1$ (tighter bound) or $c > 1$ (looser bound) without knowing $Q$. Corollary 5.4 is then conditioned on "appropriate $\alpha$" — but the condition under which "appropriate" holds is never characterized. Lemma 5.2 similarly invokes an unspecified "certain function of the second-order of $W_2$" and uses an undefined $\approx$ relation. This means the central theoretical claim that the paper advertises as a contribution is not actually established. The theoretical framework can still serve as intuition, but the paper should not claim a mathematical proof without specifying the key quantities.

- **No ablation isolating the edge-mixing component.** The method has three distinct operations: feature mixing, label mixing, and edge mixing (random neighbor selection). Standard Input Mixup on node features and labels (ignoring the graph structure) could be applied trivially. There is no experiment that ablates the edge-mixing component to show it contributes independently. Without this, it is unclear whether the gains come from the graph-specific innovation or simply from applying feature+label Mixup to node representations.

### Minor

- **The adjacency mixing operation could be specified with more precision.** Definition 4.1 states $A'$ is "the permuted batch within labeled nodes of $(X, Y, A)$," and the mixing equation is $\tilde{A} = M_{1-\lambda} \circ A + M_\lambda \circ A'$. While the overall idea (sample neighbors from each source node with complementary probabilities) is understandable, the paper does not fully specify how $A'$ is constructed from $A$ during batch training — whether it is the full $n \times n$ matrix with labeled rows/columns permuted, or a submatrix. The operation is implementable, but a concrete step-by-step description (or pseudocode) would remove ambiguity and improve reproducibility.

- **Most analyses limited to a single dataset.** The layer-depth analysis (Section 6.3, Figure 4a), label-scarcity analysis (Figure 4b), and combination experiments (Section 6.4, Table 2) are all conducted on CiteSeer only. The paper acknowledges this ("The results of GCN on the CiteSeer are presented and analyzed"), but drawing conclusions about over-smoothing mitigation, label-scarcity behavior, and versatility from one dataset limits generalizability. The Beta parameter analysis (Figure 3) covers three datasets, but the pattern is incomplete.

- **No computational cost analysis.** The method generates virtual nodes and edges, which increases effective graph size and density. The paper reports no comparison of training time, memory usage, or convergence speed relative to baselines. For a method whose claimed advantage includes "ease of usability," knowing the practical cost is relevant information.

### Trivial

- The definition of $M_\lambda$ as "the masking matrix with $\lambda$ dropping probability" (Definition 4.1) is slightly confusing given that $M_{1-\lambda}$ is multiplied by $A$ and $M_\lambda$ by $A'$; the text on lines 89–90 clarifies the intent but the notation requires a double-take.

## Nice-to-Haves

- A concrete expression for $Q(\alpha, A, X)$ under the stated assumptions, or alternatively, a clear statement that the bound is structural rather than quantitative.
- Statistical significance tests (e.g., paired t-tests) for the main comparisons, given the modest number of trials (10).

## Removed Points

These points were considered but removed after verification against the paper:

- **Exclusion of GraphMix baseline**: The paper excludes GraphMix (Verma et al., 2021) because it "requires additional modifications to the model, auxiliary loss, and training techniques" — a reasonable justification. M-Mixup, which is included, operates within GNNs directly and is the more directly comparable Manifold Mixup method. The "first Input Mixup" claim is also factually correct since GraphMix is a Manifold Mixup method, not an Input Mixup method. *Reason for removal: not a genuine weakness given the paper's stated scope.*

- **Lack of statistical significance tests**: Reporting means and standard deviations is standard practice in this subfield; formal hypothesis tests are not routinely expected. *Reason for removal: not standard for this paper's genre.*

- **Method "may not be implementable"**: The critic claimed the adjacency operation as described may not be implementable. This is an overstatement; the operation is clearly specified for implementation, though not with full engineering precision. *Reason for removal: factually inaccurate — the method is implementable, though additional precision is welcome (handled under Minor).*

- **"No labeled connections" assumption not verified on all datasets**: While only CiteSeer's 1.71% rate is cited, theoretical assumptions do not need to hold exactly in practice. The paper uses this assumption for the mathematical derivation, not as a requirement for the method. *Reason for removal: standard practice; not a substantive weakness.*

## Novel Insights

The reviews surface one genuinely novel observation that is not foregrounded in the paper itself: the optimal $\alpha$ values for the three datasets examined (CiteSeer: 100, ogbn-arxiv: 10, Flickr: 50) are all large — meaning the method works best when nodes are mixed roughly evenly ($\lambda \approx 0.5$). This suggests the method's primary benefit may come from the stochastic edge sampling (which produces different neighborhood structures each iteration) rather than from feature interpolation per se, since the feature interpolation is essentially always 50/50. The missing ablation would directly test this hypothesis.

## Suggestions

1. **Specify $Q(\alpha, A, X)$ or retract the formal proof claim.** If a concrete expression can be derived under the stated assumptions (no connections between labeled nodes, two-layer binary GCN), present it. If not, remove the claim of mathematical proof from the abstract and Section 1, and re-frame the theoretical section as a structural/intuitive argument about how iGraphMix shapes the weight space.

2. **Add an ablation isolating edge mixing.** Compare (a) full iGraphMix, (b) feature+label Mixup without edge mixing (i.e., standard Input Mixup on node features), and (c) no augmentation. This would directly establish whether the graph-specific edge-sampling component is responsible for the gains.

3. **Add pseudocode for the training loop.** A step-by-step algorithmic description of how batches are selected, how $A'$ is constructed, and how $\tilde{A}$ feeds into the GNN forward pass would resolve the remaining ambiguity in Definition 4.1.

4. **Broaden the single-dataset analyses.** At minimum, extend the label-scarcity and layer-depth experiments to a second dataset (e.g., CORA or PubMed) to support the general claims about over-smoothing mitigation and label efficiency.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>