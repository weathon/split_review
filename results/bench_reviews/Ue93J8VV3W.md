Now I have thorough calibration. Let me write the consolidated review.

---

## Summary

This paper introduces TabGraphs, a benchmark of 7 graph datasets (8 tasks) with heterogeneous tabular node features — addressing a real gap between graph ML benchmarks (which overwhelmingly use homogeneous features like bag-of-words) and real-world tabular data. The authors evaluate a broad set of 10+ methods (GBDT, tabular deep learning, standard GNNs with and without PLR embeddings, and specialized methods BGNN/EBBS) and report findings on when and why graph structure helps tabular prediction. Key claims: graph structure is generally beneficial, the best GNN architecture varies by dataset, standard GNNs typically outperform BGNN/EBBS, and PLR embeddings further improve GNNs on tabular features.

## Strengths

- **Addresses a genuine blind spot in graph ML evaluation.** The paper correctly identifies that popular graph benchmarks (OGB, citation networks, etc.) rely on homogeneous features, making it difficult to assess how GNNs transfer to industrial tabular settings where features are heterogeneous. The TabGraphs dataset collection is diverse in domain, size (11K–170K nodes), degree, homophily, and feature types, and includes realistic tasks (fraud detection, CTR prediction, road speed regression). This is well-documented via Table 1 and the per-dataset descriptions in Section 3.

- **Clean experimental design isolates the effect of graph structure.** ResNet and all GNNs are implemented in the same codebase (Section 4: "we simply swap each residual block … with the residual neighborhood aggregation block"). This makes the ResNet↔GNN comparison a direct test of whether neighbor information helps, and the results convincingly show that GNNs outperform ResNet on almost all datasets (Tables 2 and 3).

- **Broad baseline coverage with useful methodological consistency.** The paper includes GBDT (XGBoost, LightGBM, CatBoost), tabular DL (MLP-PLR, TabR), a range of GNNs (GCN, GraphSAGE, GAT, GT plus -sep variants), and specialized methods (BGNN, EBBS). Using TabR's codebase for all neural models ensures consistent implementation, and the inclusion of PLR-augmented GNN variants is a thoughtful extension that bridges tabular and graph deep learning.

- **Actionable specific finding about PLR embeddings.** The result that PLR numerical embeddings significantly improve GNN performance on several datasets (e.g., GCN from 82.83 to 89.52 ROC-AUC on questions-tab) is a concrete, reproducible insight with practical value.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric hyperparameter tuning compromises comparative claims.** Tabular models (GBDT, MLP-PLR, TabR) undergo "extensive hyperparameter search using Optuna" while GNNs are not tuned at all, with the justification that "when augmented with skip-connections and layer normalization, they are not very sensitive to the hyperparameter choice" — given without any supporting sensitivity analysis, ablation, or grid search results (Section 5). The paper's central claims — "best of GNNs always outperform graph-agnostic models," "standard GNNs typically outperform BGNN/EBBS," and architecture rankings — all depend on fair comparisons. Without tuning (or evidence that default configurations are near-optimal), observed differences could partly reflect suboptimal GNN configurations. This is the most significant threat to the paper's conclusions. The authors should at minimum vary learning rate and depth for one GNN per dataset to justify the insensitivity claim, or run a moderate grid for all GNNs.

2. **Benchmark's long-term value depends on uncertain data release.** The paper states it "will make our benchmark and the code public once we finalize legal procedures" (Abstract; Section 7). Two datasets (city-reviews, city-roads) are built from proprietary logs of a "large IT company" (Section 3). While the paper does specify which datasets are proprietary, it offers no fallback plan if these cannot be released (e.g., synthetic versions, detailed feature descriptions, or partial data). For a benchmark paper, this uncertainty weakens the contribution — especially since the proprietary datasets contribute to the diversity claims that underpin the "insights."

3. **Limited scope for a benchmark claiming broad "insights."** The benchmark contains 8 tasks on 7 graphs (2 tasks share a graph). While each dataset is meaningfully diverse, 7 distinct graphs is a small base from which to generalize patterns about when graph structure helps, which GNN architecture to prefer, and whether tabular models can compete. The findings should be treated as preliminary rather than conclusive field-wide insights. The paper acknowledges this implicitly but the framing ("insights for researchers and practitioners") overclaims relative to the evidence base.

### Minor

4. **No statistical significance testing.** Several comparisons in Tables 2 and 3 involve overlapping standard deviations (e.g., on city-reviews, various models score within ~0.5 ROC-AUC of each other). Without significance tests or confidence intervals, it is unclear which "best" model is truly best for a given dataset. Adding paired tests or effect-size measures would strengthen the reliability of rankings.

5. **Graph construction thresholds unvalidated.** The projections from bipartite to monopartite graphs (city-reviews γ=2, hm-products γ=10, avazu-devices γ=1000) use thresholds applied without sensitivity analysis. For a benchmark, showing that conclusions are stable across reasonable threshold ranges would increase confidence that the graphs meaningfully capture underlying relations.

6. **BGNN/EBBS comparison is incomplete and uneven.** EBBS is evaluated on regression only (its official implementation does not support classification). BGNN outperforms vanilla GNNs on hm-groups (87.48 vs 86.35 Accuracy) and city-roads. The claim "standard GNNs typically outperform specialized methods" is hedged ("typically") but could be strengthened by: (a) analysis of why BGNN wins on certain datasets and loses on others, or (b) loss curves showing optimization dynamics.

### Trivial
None.

## Nice-to-Haves

- A brief analysis of *when* graph structure does not help (e.g., city-reviews, where GNNs essentially tie with graph-agnostic models) — is the structure uninformative, or are features already sufficient?
- Runtime comparisons would help practitioners choose between GBDT and GNN-based pipelines.
- Qualitative examples from different datasets showing how neighbor relationships relate to targets.

## Removed Points
*These points are flagged to be removed, treat them with caution:*

- **Harsh critic's claim that "the paper does not specify which datasets are proprietary vs. open-source"** — This is factually incorrect. The paper explicitly states which datasets are from open sources (tolokers-tab, questions-tab, amazon-users, hm-products, avazu-devices) and which are from proprietary IT company logs (city-reviews, city-roads) in Section 3.
- **Harsh critic's claim that "if these datasets cannot be legally released, the benchmark is not publicly available and the paper's core contribution…is void"** — Overstated. 5 of 7 datasets are open-source or adapted from open datasets; only 2 are proprietary. The core contribution is not void if proprietary subsets have release delays.
- **Strength Finder's claim that TabGraphs is the "first comprehensive benchmark for graphs with heterogeneous tabular features"** — This is partially accurate but the paper itself discusses RelBench and 4DBInfer in the appendix, acknowledging related efforts. Keeping it as stated but noting this nuance.
- **Harsh critic's "missing appendix" concerns** — Parser-stripped sections; original submission includes them.

## Novel Insights

The most novel signal across the reviews is not a single point but a pattern: the paper's core value is as a *curated testbed* that surfaces tensions between tabular and graph ML methodologies. The finding that PLR embeddings — a simple numerical embedding technique from tabular DL consistently boosts GNN performance on graph-with-tabular-features tasks is the paper's strongest practical contribution. The paper also implicitly highlights an important methodological gap: standard GNN evaluation practices (no hyperparameter tuning, homogeneous features) are poorly aligned with the needs of industrial tabular applications, and bridging this will require benchmarks like TabGraphs as well as more careful experimental standards.

## Suggestions

1. **Run systematic hyperparameter optimization for all GNNs** (at least on a subset of datasets) or provide a controlled sensitivity analysis showing that default configurations are near-optimal. This is the single change that would most strengthen the paper.

2. **Clarify the data release plan.** State explicitly which datasets can be released immediately and which face legal review, and provide a concrete timeline or fallback (e.g., feature statistics, anonymized versions).

3. **Add statistical significance tests** (paired bootstrap or corrected t-tests) for the main comparisons, especially where standard deviations overlap.

4. **Validate threshold choices** for bipartite projections with a brief sensitivity analysis (e.g., show that rankings are stable for γ in [1,5] for city-reviews).

5. **Rephrase "insights" more cautiously.** Acknowledge that the benchmark size (7 graphs) makes findings preliminary and in need of validation on larger collections.

## Score and Decision

**Calibration against anchors (all from the returned batch):**

| Anchor Path | Avg Human Score | Comparison to paper under review |
|---|---|---|
| a6XE2GJHjk (same paper, earlier version) | 4.00 | This version is marginally better — clearer claims, but same fundamental limitations remain |
| Onw93uJCWO (Graph pooling benchmark, 28 datasets) | 4.75 | More comprehensive (28 datasets vs 7) but similar methodological concerns about tuning |
| jy6Lj3JaOf (Multimodal graph benchmark) | 4.50 | Comparable scope, similar benchmark paper, somewhat better coverage |
| rhgIgTSSxW (TabR, accepted) | 5.75 | Has algorithmic novelty this paper lacks; stronger experimental rigor |
| dbniI5RyWH (SEESAW) | 4.50 | Comparable quality; both benchmark papers with useful findings and some limitations |
| 7Jer2DQt9V (Graph OOD pretraining) | 4.50 | Similar tier — useful benchmark but limited novelty in methodology |
| M4RhGr2lAy (Fairness-aware graph benchmark) | 4.40 | Similar tier and reviewer reception |
| 2wwPG1wpsu (LST-Bench) | 2.50 | Much weaker — pure empirical report without meaningful analysis |
| AxYTFpdlvj (Graph Decoding GRDPG) | 2.00 | Weak paper with confused claims |
| anzIzGZuLi (TP-BERTa, accepted, high score) | 7.00 | Stronger paper with algorithmic contribution and better experiments |
| uTqnyF0JNR (IGL-Bench, accepted, high score) | 7.33 | Stronger benchmark with more comprehensive coverage and analysis |

The paper falls in the mid-range of the calibration set. It is substantially better than papers scoring 2.00–3.00 (which have confused claims or minimal analysis) and comparable to mid-tier benchmark papers scoring 4.00–4.75. It is weaker than accepted papers (5.75–7.33) which offer algorithmic novelty or more comprehensive benchmarks.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>