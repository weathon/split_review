- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 6, 5, 5, 3
Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Flow Graph Neural Networks (FlowGNNs), a modification of graph attention that normalizes attention weights across outgoing edges rather than incoming edges. This prevents arbitrary duplication of a node's outgoing messages, reflecting the conservation principle of flow graphs (e.g., power grids, circuits). The authors also propose DAFlowGNN for directed acyclic flow graphs, which combines a reverse pass (standard attention on the reversed DAG) with a forward pass (flow attention), enabling the model to distinguish non-isomorphic DAGs that standard DAGNNs cannot. Experiments on power grid cascading failure analysis and operational amplifier property prediction show that FlowGNN variants match or outperform their standard counterparts, with DAFlowGNN-2 achieving the best results on all three circuit regression targets.

---

## Strengths

**1. Simple, well-motivated architectural modification.** The core idea — normalizing attention across outgoing edges instead of incoming edges — is conceptually clean and directly targets a real limitation of standard attentional GNNs on resource-flow graphs. The paper clearly motivates this by contrasting informational graphs (where message duplication is fine) with flow graphs (where it violates physical conservation). (Sections 1, 3.1, Figure 2)

**2. Concrete expressivity improvement on DAGs.** The illustrative example in Figure 3 convincingly shows that DAFlowGNN can distinguish two non-isomorphic DAGs that produce identical rooted subtrees under standard DAGNN attention. This is a non-trivial theoretical advantage: the flow attention weights differ because outgoing normalization makes them sensitive to the full structure, not just incoming messages. (Section 3.3, Figure 3)

**3. Strong empirical results on circuit benchmarks.** On Ckt-Bench101, DAFlowGNN-2 achieves the lowest RMSE on all three target properties (gain, bandwidth, FoM), outperforming DAGNN-4 which has the same parameter count. DAFlowGNN-1 also outperforms DAGNN-4 on two of three properties. (Section 4.3, Table 3)

**4. Fair experimental design for the DAG comparison.** The paper explicitly notes that one DAFlowGNN layer is twice as expensive as one DAGNN layer and accordingly compares DAFlowGNN-2 to DAGNN-4, controlling for model complexity. (Section 3.2, paragraph 4; Section 4.3)

**5. Thorough reproducibility details.** All results are averaged over multiple random seeds (5 for PowerGraph, 10 for circuits), standard deviations are reported, and hyperparameters, optimizer settings, and early stopping criteria are specified. (Sections 4.2–4.3)

---

## Weaknesses

### Fatal
None.

### Major

**1. Missing ablation: the effect of the two-pass architecture is not separated from the flow attention mechanism in the DAG experiments.**

DAFlowGNN introduces two simultaneous modifications relative to DAGNN: (a) a two-pass architecture (reverse pass then forward pass), and (b) flow attention weights in the forward pass. Because the reverse pass alone provides nodes with access to descendant information — something DAGNN completely lacks — it could independently improve performance regardless of the attention normalization scheme. The paper does not include a baseline that isolates this factor: a two-pass DAGNN that uses standard (incoming-normalized) attention in both passes.

The paper's core claim is that the *flow mechanism* drives the improvement on DAGs, but without this ablation the improvement could be entirely attributable to the architectural addition of the reverse pass. This is partially mitigated by the undirected PowerGraph experiments (where no two-pass structure is needed and FlowGNNs still show gains over standard GNNs) and by the expressivity example in Figure 3 (which specifically demonstrates flow attention's discriminative advantage). However, the DAG circuit experiments are the strongest empirical evidence, and the missing ablation weakens the attribution of those results to the flow mechanism specifically.

### Minor

**1. Overstated conservation claim in the contribution list.** The paper's contribution list states that the flow attention mechanism "ensures the conservation of physical resources as they traverse through the graph" (line 29). This is too strong. The mechanism prevents arbitrary *duplication* of outgoing messages (sum of outgoing attention weights = 1), but it does not enforce Kirchhoff's first law, which requires incoming flow to equal outgoing flow at each non-source/non-target node. The rest of the paper uses more appropriate hedging language ("reflects," "accounts for"), but this one instance overpromises. The mechanism should be described as *discouraging arbitrary duplication consistently with conservation*, not ensuring conservation itself.

**2. "Expressivity of DAFlowGNN" title overpromises.** Section 3.3 presents a single illustrative example (Figure 3) showing that DAFlowGNN can distinguish two specific non-isomorphic DAGs that DAGNN cannot. This is an existence proof, not a general expressivity characterization. The section title suggests a broader theoretical treatment. The content is still a valuable contribution (it cleanly demonstrates the advantage), but should be titled "Illustrative Example" or "Expressivity Advantage" to avoid overpromising.

**3. Power grid improvements are modest and within noise bounds.** On the PowerGraph dataset, FlowGNN variants often match or slightly outperform their standard counterparts, but many comparisons show overlapping standard deviations (Tables 1–2). The paper's own discussion is appropriately cautious ("may be beneficial"), but the evidence in this domain is weak. GIN (a non-attentional GNN) remains a strong or best-performing baseline on several test systems, which somewhat undermines the claim that the flow attention mechanism is critical for flow graph tasks.

### Trivial
None.

---

## Nice-to-Haves

- **Two-pass DAGNN ablation:** Running a two-pass DAGNN with standard (incoming-normalized) attention in both passes on Ckt-Bench101 would cleanly separate the contribution of the flow mechanism from the contribution of the two-pass architecture.
- **Statistical significance testing:** Formal tests (e.g., corrected paired t-tests) would substantiate claims where standard deviations overlap on the PowerGraph results.
- **Full performance distributions:** Boxplots or per-seed results (mentioned by one reviewer) would be more informative than means and stds alone.

---

## Removed Points

These points were identified in the review inputs but are removed for the following reasons:

- **"No comparison to physics-informed regularization":** The paper explicitly notes (line 23) that the physics-informed loss approach is "useful if the target variable is the resource flow itself." The paper's tasks are graph-level classification and regression, not flow prediction. Requesting this comparison is scope creep and not a fair evaluation criterion.
- **"Reproducibility concern — code not yet released":** The paper states code is available at a URL (line 33). Per instructions, any concern about the existence or availability of cited resources is removed.
- **"Conservation claim is fatal / structurally flawed":** Demoted from the harsh critic's framing to Minor weakness #1 above. The paper's language is mostly hedged ("reflects," "accounts for") with one overstated instance in the contribution list. The mechanism does genuinely prevent arbitrary message duplication, which *reflects* conservation even if it does not *enforce* Kirchhoff's law in full.
- **Strength Finder claim #1 reworded:** The Strength Finder stated the mechanism "directly implements Kirchhoff's first law." This is inaccurate and contradicts the weakness assessment above. The mechanism distributes outgoing messages but does not enforce Kirchhoff balance, so this framing is adjusted in the strengths list above.
- **"Missing related works":** Removed per instructions — I cannot verify the existence of missing citations.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself misses.

---

## Suggestions

1. **Add the two-pass DAGNN ablation** on Ckt-Bench101 to isolate the effect of the flow mechanism from the two-pass architecture.
2. **Correct the overstatement** in the contribution list (line 29) to match the more careful language used elsewhere in the paper.
3. **Rename Section 3.3** to "Expressivity Advantage of DAFlowGNN: An Illustrative Example" or similar.
4. **Consider formal significance tests** for the PowerGraph experiments where standard deviations overlap.

---
