Now let me do calibration search with the content in hand.**Round 1 bracket: 5–7**

The paper is substantially better than the 3.0 anchors (WL-Tree, chordal sampling) and more comparable to the 4.75–5.75 range. The 8.0 anchors are more theoretically rigorous and tighter. Initial bracket: 5–7.Now let me read one of the closer anchors in full to better calibrate.Now I have enough to write the final review. Let me compile everything.

---

## Summary

Forest-Based Graph Learning (FGL) proposes a novel paradigm where message passing on a graph is reinterpreted as transport over spanning trees (a "forest"), enabling global node-pair interactions in O(n) time. Two main theoretical contributions support the approach: Theorem 1 derives two recursive pass formulas that realize O(n) all-pairs interactions for any aggregator satisfying Combine/Disentangle properties; Theorem 2 shows that increasing the score ratio Δ = p/q monotonically shifts the spanning-tree distribution toward higher-homophily trees, formally connecting estimator quality to sampling quality. Experiments on 9 benchmarks (including homophilous, heterophilous, and large-scale graphs) show FGL achieves the best average rank among 26 baselines while being faster than most.

---

## Strengths

- **Novel spanning-tree aggregation paradigm with linear complexity (Theorem 1):** The derivation of two O(n) recursions (Eqs. 5–6) that achieve all-pairs node interactions is a concrete, formally justified algorithmic contribution. The two-pass (bottom-up S, then top-down H′) is clean and generalizes over linear attention, RNNs, and SSMs.

- **Rigorous theoretical justification for homophily-guided tree sampling (Theorem 2):** The theorem proves monotonicity of the expected tree homophily ratio R(Δ) as Δ increases, with an asymptotically tight upper bound tied to the graph's homophilous connected components. This is a sound and non-trivial result that distinguishes FGL from purely empirical methods.

- **Comprehensive empirical evaluation with strong efficiency:** Table 1 (26 baselines, 9 datasets) and Table 2 (runtime comparison) together establish that FGL achieves state-of-the-art average rank while running 2–5× faster than competitive baselines such as GCNII and DiFFormer. The efficiency advantage is both theoretically grounded and empirically confirmed.

- **Ablation studies confirm component contributions (Table 3 and 4):** Removing the global submodule, local submodule, using uniform sampling, or using a single tree all degrade performance systematically, confirming that both the tree sampling quality and the multi-tree fusion matter. Table 4 further confirms the 2-stage homophily estimator is important.

- **Interpretability evidence empirically aligns with Theorem 2 (Figure 6):** Trees sampled from the homophily-guided distribution show significantly higher homophily ratios than random trees across all four reported datasets (e.g., Cornell: 0.9026 vs. 0.6768), directly validating the theoretical claim that better sampling produces more homophilous trees.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation of the pre-processing step — critical attribution gap.** Section 4.1 describes a preprocessing step that trains a GCN or MLP to generate pseudo-labels and then adds KNN edges in pseudo-label space to augment the graph. This step is applied in every experiment, including all ablations in Table 3. On heterophilous datasets — precisely where FGL's most extraordinary gains occur — this step injects strongly class-discriminative edges before any tree-based reasoning. However, Table 3 only ablates the global submodule, local submodule, sampling strategy, and tree count; no row removes or bypasses the preprocessing. Without a control experiment applying the same preprocessing augmentation to a strong baseline (e.g., SGFormer, GCNII), it is impossible to determine whether the headline gains on Texas (91.89%), Wisconsin (86.27%), and Cornell (83.24%) are driven by the spanning-tree mechanism or by the KNN graph rewiring. Notably, even the "w/o Global Submodule" ablation still uses preprocessing and still achieves 82.88% on Texas — far above all baselines. This makes it plausible that the preprocessing alone, rather than the spanning tree aggregator, is responsible for most of the heterophilous gain. The paper's framing centers the spanning-tree paradigm as the source of the gains; this attribution is undemonstrated.

### Minor

- **Overclaimed interpretation of Figure 5.** The paper states in Section 5 (Interpretability Studies): "Fig. 5 reveals that as the accuracy of homophily estimator increases, model performance consistently improves across all datasets, with perfect estimation (accuracy is 1) leading to perfect classification." However, Figure 5's description confirms that the mean accuracy peaks around p ≈ 0.7–0.8 and then *slightly decreases* before the experiment ends at p = 0.9. The "perfect estimation → perfect classification" claim is not visible in the figure; the x-axis does not reach p = 1.0, and the figure shows a downturn before that point. This specific claim is overstated.

- **Theory-implementation gap for Theorem 2.** Theorem 2 assumes known binary edge labels (homophilous = p, heterophilous = q), while the implementation (Eq. 3) uses learned softmax attention coefficients as unsupervised proxies. Table 4 and Fig. 5 provide empirical support that better estimators help, but the formal connection between learned attention scores and the p/q idealization is not established. This makes the theoretical justification informal at the critical bridge between theory and practice.

- **Actor dataset: 22+ point gap vs. Graphormer unexplained.** FGL achieves 39.88% on Actor, while Graphormer achieves 62.70%. This 22-point gap is the largest single-dataset shortfall in Table 1 and is not discussed. Actor is a heterophilous graph, a setting where FGL claims advantages; the failure mode should be analyzed.

### Trivial

- **Complexity claim for Wilson algorithm.** Section 4.2 states "nearly O(n) time per-tree" for the weighted Wilson algorithm. The original O(n) expected-time complexity holds for uniform spanning trees under specific random-walk mixing conditions; for arbitrary edge weights, the expected cover time can differ. The word "nearly" is left without formal qualification.

- **Pre-processing requires prior knowledge of graph type.** Section 4.1 states that a GCN layer is used for homophilous graphs and an MLP for heterophilous graphs, but does not explain how this determination is made in practice, especially for graphs of ambiguous homophily.

---

## Nice-to-Haves

- **Ablation applying preprocessing to strong baselines.** This is the single most impactful addition: run the same pseudo-label-guided KNN edge augmentation on SGFormer and GCNII, then compare against FGL. If FGL still substantially outperforms these augmented baselines, the spanning-tree mechanism is clearly contributing; if the gap narrows dramatically, the paper's claims should be recalibrated accordingly.

- **Formal statement about the gap between Theorem 2 and learned attention scores.** Even an informal bound relating the learned edge scores to the theoretical p/q ratio would strengthen the theory-practice connection.

- **Analysis of Actor failure mode.** Since FGL performs well on other heterophilous graphs (Texas, Wisconsin, Cornell) but poorly on Actor, a brief analysis of why the spanning-tree paradigm succeeds in some heterophilous settings but not others would substantially improve the reader's understanding of the method's scope.

- **Standard deviations in Table 1.** These are currently deferred to an appendix. For small-graph datasets like Texas/Wisconsin/Cornell, variance over 10 seeds is an important signal for whether gains are reliable.

---

## Removed Points

*These points are flagged for removal; treat them with caution as they may reflect reviewer misreading or speculative reasoning.*

- **Split protocol invalidity concern (Harsh Critic, Critical Issue 2).** The reviewer questions whether the reported GCNII numbers (69.19% on Texas) are lower than published values because of split differences, suggesting the splits may be non-standard. However, the paper states all baselines are reproduced by the authors under the same split protocol. Internal consistency of Table 1 is maintained. Cross-paper comparison of absolute numbers is inherently unreliable given differing protocols. This criticism is speculative and cannot be verified without access to the actual re-run implementation. Removed as unverifiable.

- **Claim that GCNII "typically achieves 77–80% on Texas" (Harsh Critic).** This cross-paper comparison presupposes that the external GCNII results used Geom-GCN splits (Pei et al., 2020), while FGL may use a different protocol. Since the authors reproduce all baselines uniformly, this is not a flaw in the paper's comparison. Removed per hard rules.

- **Actor is "quietly absorbed without comment" (Harsh Critic).** While it is true that Actor's gap versus Graphormer is large, the paper does not suppress this: Table 1 shows the numbers clearly. The absence of textual discussion qualifies as a Minor suggestion, not a structural flaw. Retained as Minor above.

- **Generic strength claims from the Strength Finder** ("FGL effectively captures long-range knowledge" without specific evidence beyond the table) were filtered in favor of the specific, grounded strengths listed above.

- **Efficiency comparison excludes pre-training cost (Harsh Critic).** This concern is noted but the pre-processing is a one-time cost (executed before the main training loop, not per epoch). Without direct evidence that Table 2 omits this cost, the criticism is speculative. Demoted and removed.

---

## Novel Insights

The most genuinely novel observation in this paper is the formalization of spanning trees as an *intermediate-level structure* that avoids both the excessive depth of deep local models and the quadratic cost of global transformers. The Combine/Disentangle abstraction (Property I/II) is elegant: it unifies linear attention, RNNs, and SSMs under a single two-pass recursion on trees. Theorem 2's asymptotic tightness result — that the upper bound on homophily ratio is determined by the number of homophilous connected components, not by the graph's size — is a clean graph-theoretic result with practical implications for understanding when the method can succeed.

---

## Suggestions

1. **Add one targeted ablation:** apply identical preprocessing (pseudo-label-guided KNN augmentation) to SGFormer and GCNII, then compare their performance against FGL on Texas, Wisconsin, and Cornell. This single experiment would resolve the paper's most critical open question.
2. **Correct or qualify the Fig. 5 interpretability claim.** Either extend the sweep to p = 1.0 or remove the "perfect estimation → perfect classification" statement, which is not supported by the data as shown.
3. **Briefly analyze the Actor performance gap** (FGL 39.88% vs. Graphormer 62.70%) to delineate the method's scope.
4. **Clarify the complexity claim for Wilson's algorithm** under arbitrary weights, noting any mixing-time assumptions needed for the "nearly O(n)" claim to hold.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| ceNnsnA5gu.md (WL-Tree) | 3.00 | R1 | Much weaker; no empirical contribution |
| VyMW4YZfw7.md (Simplifying GNN) | 3.00 | R1 | Weaker; raises methodological critique without novel method |
| GEZACBPDn7.md (KDGCN) | 5.25 | R1 | Weaker; less theoretical depth, narrower benchmark |
| nFcgay1Yo9.md (Scale-Free GLMs) | 5.75 | R1 | Comparable territory (KNN augmentation + pseudo-labeling); less theoretical |
| aFMiKm9Qcx.md (Central Spanning Tree) | 4.75 | R1 | Different problem (spanning tree optimization); less ML-focused |
| HgSfV6sGIn.md (STExplainer) | 4.75 | R1 | Weaker; explainability tool rather than learning paradigm |
| P7KIGdgW8S.md (Hölder Stability GNNs) | 8.00 | R1 | Stronger; rigorous mathematical theory, tight; different contribution type |
| zBbZ2vdLzH.md (JDR — Joint Denoising/Rewiring) | 8.00 | R1 | Stronger; formally justified rewiring, strong theory, broader experimental scope |
| oSdrJyb4UH.md (Monophilic NT) | 6.00 | R2 | Rejected; FGL clearly stronger (more baselines, more theory, more datasets) |
| 6MBqQLp17E.md (Linear Transformer Topological Masking) | 7.00 | R2 | Accepted at 7.0 but has a fundamental theoretical flaw (O(1) sparsity claim) |
| tGOOP7DGxs.md (Graph Transformers for Large Graphs) | 5.00 | R2 | Rejected; narrower scope, less theoretical rigor than FGL |
| BapOwAzicb.md (HOGT: High-Order GTs) | 5.25 | R2 | Rejected; similar ambition, less theoretical depth, missing scalability |
| rWQDzq3O5c.md (Graph Transformers Dream of Electric Flow) | 5.75 | R2 | Accepted; theoretical analysis of linear transformers; comparable depth but narrower scope |

**Round 1 bracket:** 5–7.

**Round 2 narrowing:** FGL is clearly stronger than the 5.0–5.25 rejected anchors (Graph Transformers for Large Graphs, HOGT). It is comparable to or stronger than the 5.75 accepted anchors (Scale-Free GLMs, Graph Transformers Dream of Electric Flow) given its more comprehensive empirical coverage and clean theory. The 7.0 anchor (Linear Transformer Topological Masking) has a more sophisticated theoretical contribution but is accepted despite a fundamental theoretical flaw — FGL's theory is cleaner but the preprocessing attribution gap is a real empirical shortcoming. The 6.0 rejected anchor (Monophilic NT) lacks the baseline coverage and theoretical depth FGL has. FGL sits above 6.0 in contribution quality but the preprocessing attribution concern — which affects the paper's headline claims — is material. The paper is not ready to accept as-is due to this one missing experiment, but the core contribution is solid.

**Final score: 5.5** — The spanning-tree learning paradigm is a genuine and interesting contribution, the two theorems are sound, and the empirical breadth is impressive. However, the complete entanglement of the preprocessing step with the spanning-tree mechanism in every experiment means the paper's headline attribution is undemonstrated, which is a major issue for a venue like ICLR.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>