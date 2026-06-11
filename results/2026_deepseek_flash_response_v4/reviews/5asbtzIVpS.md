## Summary

This paper proposes Forest-Based Graph Learning (FGL), a novel paradigm for semi-supervised node classification that reinterprets message passing as transportation over spanning trees. The key insight is that spanning trees are the minimal subgraph achieving global coverage, thereby balancing cost and receptive field. The framework includes: (1) pre-processing that augments the graph via pseudo-labels, (2) a Wilson-sampling-based tree sampler guided by a learned homophily estimator, (3) a linear-time tree aggregator using two recursions that propagate information over each tree, and (4) a tree fuser merging knowledge from multiple trees. The paper provides theoretical analysis (Theorem 2) linking homophily-estimator accuracy to tree-distribution quality, and experiments on 9 benchmarks show strong results (average rank 1.22) with competitive efficiency.

## Strengths

1. **Principled spanning-tree insight (Section 1, Eq. 1, Figure 1).** The paper identifies that both deep local models (many cheap structures) and shallow global models (one expensive structure) suffer because total cost = (cost per structure) × (number of structures). Spanning trees are identified as the minimal subgraph achieving global coverage while keeping both factors low. This clean, fundamental insight directly motivates the entire FGL paradigm.

2. **Theorem 2 establishes a non-trivial asymptotic guarantee (Section 4.6).** The theorem proves monotonicity, a structural upper bound determined by the graph's homophilous connected components, and asymptotic tightness for the relationship between homophily-estimator accuracy and tree-distribution quality. This provides formal justification for the sampling strategy that goes beyond engineering intuition.

3. **Strong empirical results (Table 1).** FGL achieves the best average rank (1.22) across 9 datasets and tops 6 of 9, with large margins on heterophilous benchmarks (e.g., Texas 91.89% vs. next-best 78.92%; Wisconsin 86.27% vs. 80.39%; Cornell 83.24% vs. next-best 76.76%).

4. **Competitive efficiency (Table 2).** Per-epoch running time is the fastest on all five tested datasets (e.g., 0.005s on Cora, 0.020s on Pubmed, 0.246s on ArXiv), validating the linear-complexity claim and demonstrating practical speed advantages over both deep GNNs and Graph Transformers.

5. **Well-structured ablation and analysis (Table 3, Table 4, Figure 6).** The ablation cleanly isolates the contribution of each component: homophily-guided sampling outperforms uniform sampling, multiple trees (a forest) outperform a single tree, and the local and global submodules each contribute. Table 4 and Figure 6 provide mechanistic evidence linking Theorem 2 to observed performance.

6. **Algorithmically clever tree aggregator (Theorem 1, Section 4.3).** The observation that globally merged messages for neighboring tree nodes differ in only one edge direction enables two linear-time recursions. The construction is theoretically general (can accommodate linear RNNs, SSMs, etc.) and concretely implementable as weighted sums.

## Weaknesses

### Major

- **Uneven comparison due to pre-processing (Section 4.1 vs. Table 1 baselines).** The pre-processing step (Section 4.1) constructs an augmented graph Ĝ by adding kNN edges based on pseudo-labels, which increases the homophily ratio. FGL operates on Ĝ, while all 26 baselines are evaluated on the original graph G. This means FGL benefits from a label-informed graph enrichment that the baselines do not receive, making it impossible to fully attribute the reported gains to the forest-based paradigm alone. The ablation (Table 3) shows that even without the tree aggregator (row 1: "w.o. Global Submodule"), the method achieves 82.88% on Texas — already exceeding every baseline except SGFormer (78.92%) — suggesting the pre-processing + local module contribute substantially. A fairer comparison would either (a) apply the same pre-processing to all baselines or (b) evaluate FGL on the original graph to isolate the forest component's contribution.

### Minor

- **The "quadratic node-pair interactions" claim overstates what the tree aggregator does (Abstract, Section 4.3).** The abstract states the tree aggregator "realizes quadratic node-pair interactions." While information from every node does reach every other node via the root through the two recursions, this is a diffusion process on a tree — not independent pairwise interaction modeling as in Graph Transformers. Any connected message-passing scheme with enough depth achieves the same all-pairs reachability. The phrasing could mislead readers into thinking the model matches the expressivity of full pairwise attention at lower cost, which is not demonstrated.

- **Running time comparison scope (Table 2 vs. Section 4.5).** The per-epoch times in Table 2 likely cover only the student training loop, not the one-time costs of pre-training the homophily estimator, Wilson sampling of trees, and pre-processing. While these overheads are relatively small (O((n+m)d) per pre-training epoch), the practical wall-clock comparison would be more complete if reported end-to-end.

### Trivial

None.

## Nice-to-Haves

- The theoretical analysis (Theorem 2) assumes binary edge scores (p for homophilous, q for heterophilous), while the actual method uses continuous attention weights. A discussion of how estimation error in the continuous case affects tree quality would tighten the theory-practice connection.
- The homophily estimator is trained using the same pseudo-labels that are used for graph augmentation. While the two-stage estimator (Table 4) partially mitigates this, a brief discussion of potential label leakage would be helpful.
- The claimed generality of the tree aggregator (accommodating linear RNNs, SSMs, etc.) is asserted but only a weighted-sum variant is implemented. Demonstrating even one alternative variant would strengthen this claim.

## Removed Points

These points were flagged for removal; treat with caution if re-raised:

- *Missing standard deviations / variance reporting*: The paper states standard deviations are in Tab. 10 of the appendix. The appendix was stripped by the parser; these exist in the original submission. **Removed** (parser artifact).
- *Theorem 2 doesn't bridge to practice*: The theorem provides a formal analysis for a simplified (binary) case. This is standard theoretical practice — the paper never claims the binary analysis directly operationalizes, but rather provides intuition and formal guarantees on the relationship between estimation accuracy and tree quality. The critic's framing as a "methodological gap" is overly harsh for what is a clean but abstract theoretical result. **Demoted to Nice-to-Have**.
- *Circular dependency in pseudo-label use*: The two-stage estimator design (Table 4) specifically addresses the concern about label leakage. **Demoted to Nice-to-Have**.
- *Missing related works, formatting/style nitpicks, speculative fatal flaws*: All removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations about the paper that go deeper than what the authors already articulate.

## Suggestions

1. **Isolate the forest contribution through fairer evaluation.** Either (a) apply the same pre-processing (pseudo-label-based edge addition) to all baselines so the comparison isolates the forest-based component, or (b) evaluate FGL on the original graph (with minimal connectivity fixes that don't leverage label information) to show what the forest paradigm contributes independently.

2. **Rephrase "quadratic node-pair interactions."** Use "all-pairs information propagation via linear-time message passing on a tree" to avoid over-claiming about expressivity.

3. **Report end-to-end wall-clock time** including pre-training, sampling, and augmentation, not just per-epoch student training time.

4. **Consider tightening the theory-practice connection** with even an informal discussion of how continuous attention scores relate to the binary-score analysis of Theorem 2.

---

## Calibration Anchors

Round 1 — Bracketing (all queries: "graph neural network spanning trees global receptive field semi-supervised node classification"):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ceNnsnA5gu.md (WL-Tree) | 3.00 | 1 | Much weaker — basic WL analysis, no real empirical gains |
| S3zKrEQpRr.md (Noisy Communication Channels) | 3.00 | 1 | Much weaker — abstract theoretical framing, weak experiments |
| W4q7cwRCwg.md (GloMP-GNN) | 3.00 | 1 | Much weaker — less novel, weaker results |
| aJl5aK9n7e.md (What Improves GT Generalization) | 5.25 | 1,2 | Weaker — highly restrictive assumptions caused reviewer disagreement (scores 1,6,6,8) |
| HgSf6sGIn.md (STExplainer) | 4.75 | 1 | Weaker — explanation method, different task |
| qT1I15Zodx.md (Snowflake Hypothesis) | 4.75 | 1 | Weaker — far from SOTA performance, unclear motivation |
| vst5P4Pve2.md (Towards Global Interaction) | 4.67 | 1 | Weaker — poorly defined concepts, problematic theory |
| P7KIGdgW8S.md (Hölder Stability) | 8.00 | 1 | Stronger — rigorous theory, clean evaluation |
| viftsX50Rt.md (General Graph Random Features) | 8.00 | 1 | Stronger — foundational theory, clean proofs |

Round 2 — Narrowing:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 6MBqQLp17E.md (Linear Transformer Topological Masking) | 7.00 | 2 | Slightly stronger — had a serious theoretical flaw (O(1) sparsity claim incorrect per one reviewer) but still scored higher; comparable novelty level |
| hmv1LpNfXa.md (Polynormer) | 6.00 | 2 | Comparable — similar contribution profile (linear GNN, SOTA results on heterophilic data), but different method family. Polynormer lacks the pre-processing fairness concern but also lacks as novel a paradigm shift |
| 5x88lQ2MsH.md (Bonsai) | 6.00 | 2 | Comparable — solid empirical work with theory, uniformly scored 6 |
| 4v4RcAODj9.md (DUALFormer) | 6.50 | 2 | Similar — dual GCN/attention approach, but less novel paradigm |
| oSdrJyb4UH.md (Monophilic Neighbourhood Transformers) | 6.00 | 2 | Comparable — heterophily-focused method with attention, similar quality |

**Round 1 bracket:** 5.0–7.0.

**Narrowing:** After comparing to Polynormer (6.00), Bonsai (6.00), and DUALFormer (6.50), the paper is strongest among the 6.0-level anchors due to its more novel paradigm (forest-based learning is more transformative than another attention variant), stronger theoretical foundation (Theorem 2), and more striking results on heterophilic benchmarks. However, the pre-processing fairness concern is a real weakness that Polynormer and Bonsai do not share. The paper sits at the upper end of the 6-range but the fairness concern keeps it from reaching 7.0.

**Final score: 6.0**

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>