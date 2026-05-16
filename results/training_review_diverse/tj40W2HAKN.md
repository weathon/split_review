I now have complete information to write the final consolidated review.

---

## Summary

This paper proposes Node-MoE, a graph neural network that applies different spectral filters to different nodes via a Mixture of Experts framework, motivated by the observation that real-world graphs contain a mixture of homophilic and heterophilic patterns that vary across communities. The authors provide theoretical analysis (using a CSBM model) showing that a global low-pass filter provably incurs significant loss on heterophilic nodes while node-wise filtering can achieve linear separability. Empirically, the method achieves the best average rank (1.29) across 7 benchmark datasets, outperforming 12 baselines including fixed-filter, learnable-filter, and prior MoE-based GNNs.

## Strengths

- **Theoretical motivation for node-wise filtering (Theorem 1):** The paper formally proves that a global low-pass filter incurs a lower-bounded loss on heterophilic nodes while node-wise filtering can achieve linear separability with probability 1−o_d(1) under a mixed CSBM model. This provides clear theoretical justification for why per-node filtering is needed, going beyond heuristic motivation.

- **Consistent empirical superiority across homophilic and heterophilic benchmarks:** Table 1 shows Node-MoE achieves the best average rank (1.29) among 12 methods, outperforming the best single-filter model (ChebNetII, rank 3.86) and the prior MoE-based GNN (GMoE, rank 6.57). The gains are substantial on heterophilic datasets (e.g., Chameleon: +2.50% over ChebNetII, +1.76% over GMoE; Squirrel: +5.19% over ChebNetII).

- **Verification that experts learn distinct, interpretable filters and gating assigns them appropriately:** Figure 3 shows one expert learns a low-pass filter and another a high-pass filter on Chameleon; Figure 4 demonstrates that nodes with lower homophily receive higher weight for the high-pass expert. This provides direct evidence that the learned mechanism aligns with the intended design.

- **Empirical documentation of mixed patterns at community level (Section 2.1, Figures 1-2):** The paper quantifies that even nominally homophilic datasets (Cora, CiteSeer) contain nodes with heterophilic tendencies and vice versa, and that homophily varies dramatically across communities within the same graph. This analysis grounds the problem in real data and goes beyond prior global-homophily assumptions.

- **Gating design validated through ablation:** The ablation study (Figure 5) shows that the proposed graph-structure-aware gating (GIN on composite input) significantly outperforms a simple MLP-based gating, confirming the benefit of leveraging community structure for expert selection.

- **Efficiency via Top-1 gating:** With k=1, Node-MoE achieves nearly identical performance to soft gating (e.g., 89.38% vs 89.28% on Cora), showing the method can be practical with complexity comparable to a single expert model.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theory-method gap between the CSBM analysis and the actual gating mechanism.** Theorem 1 shows that *if* one knew which nodes follow homophilic vs. heterophilic patterns, applying separate filters achieves linear separability. However, the actual method must *infer* these pattern memberships via a learned gating model. The paper acknowledges this challenge ("without ground truth on node patterns") but provides no bound or analysis on whether (or under what conditions) the gating model — which uses GIN on `[X, |AX-X|, |A^2X-X|]` — can approximate the oracle assignment that the theorem assumes. The theorem motivates the *idea* of node-wise filtering but does not directly support the specific gating design, leaving a logical gap between the theoretical motivation and the implemented solution. This weakens, but does not invalidate, the paper's story since the empirical results stand independently.

- **Lack of formal statistical significance testing for key comparisons.** Several performance differences over the second-best method fall within overlapping confidence intervals (e.g., Cora: 89.38±1.26 vs. GloGNN 88.78±1.21; CiteSeer: 77.78±1.36 vs. APPNP 77.42±1.47; Squirrel: 62.31±1.98 vs. LinkX 61.81±1.80). While the average rank (1.29 vs. 3.86 for the next best) is compelling, the paper does not report pairwise significance tests (e.g., paired t-test or Wilcoxon signed-rank across splits). Adding such tests would increase confidence that the improvements are robust rather than split-dependent.

- **The gating model's reliance on community detection via GIN may be imperfect when within-community pattern diversity is high.** Figure 2 shows several communities with intermediate homophily (~0.4–0.6), where nodes within the same community exhibit mixed patterns. The gating model uses GIN (a low-pass GNN) with neighborhood aggregation, which may group nodes by community rather than by individual pattern contrast. The paper argues this is beneficial ("neighboring nodes are likely to receive similar expert selections") but does not analyze the failure case where community and pattern membership diverge. The ablation (GIN gating outperforms MLP gating) partially addresses this concern but does not fully resolve it.

- **The assumption that p₀+q₀ = p₁+q₁ (equal expected degrees) in the CSBM analysis is restrictive** and not discussed. While this is a common simplifying assumption for theoretical tractability, it limits the generality of the result and should be acknowledged.

- **No quantitative bound is provided for the homophilic set's loss under the global filter** — only the heterophilic loss receives a lower bound (part 1 of Theorem 1). The homophilic case is described qualitatively as "near linear separability" without a matching bound.

- **The choice of two hops (|A²X-X|) in the gating input is not explicitly motivated** — the paper does not discuss why two hops is chosen over one or three, or how sensitive the method is to this choice.

### Trivial
None.

## Nice-to-Haves

- A brief computational cost analysis (training/inference time, parameter count) would help practitioners assess the practical overhead of Node-MoE, even though the Top-1 ablation speaks to efficiency.

- A discussion of failure cases (e.g., very high edge homophily where |AX-X| is small for all nodes, making pattern discrimination difficult; or graphs where the number of experts is insufficient to cover all latent patterns) would strengthen the paper's completeness.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper misses related works on node-wise spectral filtering (e.g., wavelet-based adaptive filtering)."** — Rule: do not mention missing related works, as external sources to confirm their existence are unavailable.

- **"Reproducibility details (hyperparameters, optimizer, etc.) are absent from the main text."** — These may exist in an appendix that was stripped by the parser. The rule says to remove weaknesses about missing appendix content.

- **"The toy example in Figure 1 relies on an unrealistic scenario."** — A toy example is intentionally simplified for illustration. This is a generic criticism that does not affect the core contribution.

- **"Theorem 1's statement uses 'near' imprecisely."** — The bound is given quantitatively for the heterophilic loss, and "near" is natural-language summary — this is a formatting/style nitpick.

- **"The theorem applies only to a linear model, not to a full GNN."** — The paper explicitly says "For simplification, we consider a linear model" — this is an acknowledged scope choice, not an oversight.

- **"The load-balancing loss is not described in detail."** — The paper references Shazeer et al. for the standard formulation, which is standard practice.

- **"The paper does not discuss whether GMoE could be extended with learnable filters."** — This is speculative criticism about what the paper *could have* compared, not what it did.

## Novel Insights

None beyond the paper's own contributions. The reviews reinforce the paper's core message — node-wise filtering via MoE is well-motivated and empirically effective — but do not surface fundamentally new observations beyond what the authors already present.

## Suggestions

1. **Tighten the theory-method connection:** Add a brief discussion (even informal) of why the gating features `[X, |AX-X|, |A²X-X|]` can reasonably recover pattern membership under the CSBM model. Even a note that a simple threshold on `|AX-X|` separates homophilic from heterophilic nodes in the CSBM setting would help bridge the gap.

2. **Add statistical significance tests:** Report paired t-test p-values (across the 10 splits) for the comparison with the second-best method on each dataset. This is straightforward and would substantially strengthen confidence in the results.

3. **Analyze gating behavior in mixed-community nodes:** Visualize gating assignments (e.g., via a 2D node embedding colored by gating weight) for communities with intermediate homophily (0.4–0.6) to demonstrate that the gating model makes fine-grained per-node assignments rather than coarse community-level groupings.

## Score and Decision

**Originality:** Good. Node-wise filtering via MoE is a novel synthesis of ideas from spectral graph theory and MoE architectures.  
**Importance of research question:** High. Handling mixed structural patterns is a recognized challenge in graph learning.  
**Claims well-supported:** Mostly yes. The empirical evidence is strong, though the theory-method gap and lack of significance tests are notable.  
**Soundness of experiments:** Solid. Seven datasets, 12 baselines, ablation studies, and behavioral analysis.  
**Clarity of writing:** Clear and well-structured.  
**Value to the community:** Positive. The framework is flexible, achieves strong results, and the behavioral analysis provides useful insights.

The paper makes a genuine contribution. No weakness is fatal or major — the theory-method gap is acknowledged by the authors, the empirical results are strong and independently convincing, and the remaining concerns are addressable in minor revisions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>