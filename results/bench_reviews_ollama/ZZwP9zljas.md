Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper studies how random edge-dropping algorithms (DropEdge, DropNode, DropAgg, DropGNN) affect over-squashing in message-passing neural networks. The key theoretical contribution (Lemma 3.1/Theorem 3.1) provides a closed-form expression for the expected propagation matrix under DropEdge, showing that expected sensitivity between distant nodes decreases monotonically with dropping probability — meaning these methods shrink the effective receptive field. This is extended to nonlinear MPNNs (ReLU-GCNs, source-only and source-and-target message functions) and to DropEdge variants. Experiments on homophilic (Cora, CiteSeer) and heterophilic (Chameleon, Squirrel, TwitchDE) datasets show that dropping probability correlates positively with accuracy on homophilic datasets but negatively on heterophilic ones, consistent with the theory.

## Strengths

- **Clean theoretical result (Lemma 3.1):** The closed-form expression for the expected propagation matrix under DropEdge correctly accounts for the non-trivial correlation between random degree and random adjacency entries under asymmetric normalization. This is a legitimate and non-obvious technical contribution that directly supports the paper's central claim. The extensions to nonlinear MPNNs via existing sensitivity bounds (Sections 3.2) are straightforward but show the conclusion holds broadly.

- **Practical and important finding:** The paper flags a real and underappreciated tension — methods designed to alleviate over-smoothing can exacerbate over-squashing by shrinking the receptive field. This is a genuinely valuable observation for the GNN community, where DropEdge is widely used with little scrutiny of its long-range effects.

- **Ruling out underfitting (Figure 3):** The paper demonstrates that training accuracy on heterophilic datasets *increases* with dropping probability while test accuracy decreases. This is a strong experimental control that eliminates underfitting as an alternative explanation and supports the overfitting-to-short-range-signals narrative.

- **Experiments with GAT beyond theoretical assumptions:** Including GAT (which violates the theoretical assumptions) alongside GCN shows the phenomenon is not an artifact of one architecture, broadening practical relevance.

## Weaknesses

### Fatal
None.

### Major

- **Equating heterophily with long-range task dependence is not validated.** The entire experimental argument treats heterophilic datasets as proxies for "long-range tasks" (Section 4.1, line 178: "Since DropEdge-variants increase a node's sensitivity to its immediate neighbors and reduces its sensitivity to distant nodes, we expect it to improve performance on homophilic datasets but harm performance on heterophilic ones"). However, heterophily means nearby nodes have dissimilar labels — this does not strictly imply the task requires propagating information over long distances. Recent work shows heterophilic tasks can sometimes be solved with sufficiently expressive local aggregations. The paper acknowledges this mapping is heuristic ("identifying whether a task requires modeling LRIs can be challenging"), but never validates that these datasets actually benefit from deeper models or wider receptive fields — e.g., by showing that baseline GNNs without dropping improve with depth on these datasets. Without such validation, the empirical results could reflect disruption of local structural patterns that heterophilic methods rely on, rather than specifically the loss of long-range communication. This weakens but does not invalidate the paper's central claim, since the theoretical prediction (sensitivity reduction) is independently verified and the empirical trends are consistent with the theory.

- **The "overfitting to short-range signals" mechanism is inferred rather than directly verified.** Section 4.3 shows training accuracy increasing while test accuracy decreases with q, which demonstrates overfitting in the standard sense. The paper attributes this to overfitting specifically to "short-range artifacts," but no probe or perturbation study directly confirms what the model is overfitting to. While the interpretation is natural given the theory (reduced sensitivity → reliance on local information → overfitting to local patterns), it remains an inference rather than an empirical finding. A measurement of effective receptive fields under different dropping probabilities would substantially strengthen this claim.

### Minor

- **DropNode behavior contradicts the theoretical prediction, limiting the framework's generality.** The theory predicts DropNode does *not* reduce sensitivity between distant nodes in expectation (Eq. 3.4), yet Table 2 shows negative correlation between dropping probability and test accuracy for *every* dataset–model combination, including homophilic ones. The paper acknowledges this discrepancy (line 205: "our analysis did not account for the effects on the learning trajectory"), which is transparent, but it means the sensitivity-based theoretical framework cannot explain 25% of the methods studied. This limits the generality of the framework without invalidating the core DropEdge results.

- **Theoretical results are restricted to asymmetric normalization.** The closed-form results in Lemma 3.1 assume $\hat{A} = \hat{A}^{\text{asym}}$, while the symmetric normalization $\hat{A}^{\text{sym}}$ (the more common GCN formulation) is validated only empirically (Figures 4–5). This is a genuine scope limitation of the theoretical contribution.

### Trivial
None.

## Nice-to-Haves

- Running depth-sweep experiments (varying L without dropping) on the heterophilic datasets to directly verify that deeper models benefit these datasets, which would validate the "long-range task" proxy.
- Adding established long-range benchmarks (e.g., Long-Range Graph Benchmark, ZINC) alongside heterophilic node classification datasets.
- Computing effective receptive fields (e.g., via gradient attribution) to directly verify that DropEdge-trained models have smaller receptive fields.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Critic claim that the abstract overstates prior evidence for DropEdge.** The critic says "DropEdge's benefits were observed primarily on specific benchmarks, not universally." The abstract states these methods "have successfully addressed the over-smoothing problem" — this is a standard characterization of their purpose and is consistent with their published results. This is not a weakness of the current paper.

- **Critic claim that Section 3.2 is "more synthesis than new analysis."** The extensions to nonlinear MPNNs are straightforward applications of E[Â]^L = E[Â]^L by independence, but the paper does the work of connecting these to DropEdge variants and showing the unified conclusion. This is standard for theoretical papers in this area and the result is still useful.

- **Critic claim that Section 4.3 sets up a "false binary" between over-squashing and underfitting.** The paper *explicitly considers and rules out* underfitting — this is good scientific practice, not a false dichotomy. The section shows that underfitting does not explain the results.

- **No standard deviations/variance reported across 5 runs.** While desirable, this is a minor methodological point and the trends in Figure 2 and the rank correlations in Table 2 are clear enough that variance likely wouldn't change the conclusions.

- **Missing comparison with graph rewiring methods.** This is outside the paper's stated scope — the paper studies the effect of edge-dropping on over-squashing, not whether rewiring can fix the problem.

- **Strength Finder's claim that the paper provides "controlled empirical evidence distinguishing short-range vs. long-range effects."** This is weakened by the major weakness above (heterophily ≠ long-range). Moving to Removed Points since it conflicts with a verified weakness.

## Novel Insights

The paper identifies a real architectural blind spot: widely-used regularization methods designed for one GNN pathology (over-smoothing) can exacerbate another (over-squashing). The theoretical analysis cleanly shows *why* this happens through the propagation matrix — DropEdge increases local sensitivity while reducing sensitivity between distant nodes. The most interesting empirical finding is the DropNode anomaly: it does *not* reduce sensitivity in the theoretical analysis (due to the row/column zeroing structure preserving expected propagation), yet still hurts performance on all datasets including homophilic ones. This suggests the optimization-trajectory effects of random dropping may be more consequential than the sensitivity-reduction effects, at least for DropNode, and points to a deeper question about whether the sensitivity framework fully captures the practical impact of these methods.

## Suggestions

- Validate the heterophily ↔ long-range mapping by running depth-sweep experiments without edge dropping, showing whether deeper models actually improve on Chameleon, Squirrel, and TwitchDE — this would directly confirm that these datasets require long-range information.
- Add a gradient-based effective receptive field visualization comparing models trained with and without DropEdge on heterophilic datasets, which would directly verify the "overfitting to short-range signals" claim.
- Acknowledge the DropNode discrepancy more prominently and discuss what the optimization-trajectory explanation implies for extending the theoretical framework.

## Score and Decision

The paper makes a solid and timely contribution — flagging an important trade-off between over-smoothing and over-squashing solutions, with a clean theoretical result in Lemma 3.1. The experimental results are largely consistent with the theory. The main weakness is the unvalidated mapping from heterophily to long-range task dependence, which weakens the empirical support for the central claim. This is addressable in revision but makes the current evidence partially circumstantial. The DropNode discrepancy further limits the theoretical framework's generality. Overall, this is a worthwhile contribution that would benefit from stronger empirical validation.

**Originality:** Moderate — the theoretical result is a clean but straightforward extension of existing sensitivity analysis to the DropEdge setting; the key insight (edge-dropping hurts over-squashing) is important and novel.

**Importance of research question:** High — DropEdge is widely used; understanding its interaction with over-squashing is practically important.

**Claims well supported:** Partially — the theoretical claims are well supported; the empirical claims have a gap in the heterophily → long-range mapping.

**Soundness of experiments:** Moderate — consistent with theory but limited by the dataset choice and unverified proxy.

**Clarity:** Good — clearly structured with explicit "Message of the Section" summaries.

**Value to community:** High — alerts practitioners to a real risk of a widely-used method.

MY FINAL SCORE: <pineapple>6</pineapple>
MY FINAL DECISION: <orange>Accept</orange>