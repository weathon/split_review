Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper introduces TabGraphs, the first benchmark specifically designed for graph datasets with heterogeneous tabular node features (mixtures of numerical, categorical, and binary attributes). It comprises eight diverse datasets spanning crowdsourcing, e-commerce, navigation, and advertising domains. The paper evaluates a broad set of models — GBDT, tabular deep learning models, standard GNNs, and specialized methods (BGNN, EBBS) — and extracts actionable insights about when and how graph-aware methods outperform graph-agnostic alternatives on tabular-feature graphs.

## Strengths

- **First dedicated benchmark for graphs with heterogeneous tabular features.** This directly addresses a well-documented gap: both BGNN (Ivanov & Prokhorenkova, 2021) and EBBS (Chen et al., 2022) explicitly noted the lack of suitable public datasets, and existing graph benchmarks overwhelmingly use homogeneous bag-of-words or word-embedding features. The eight proposed datasets are genuinely diverse in domain, graph size (11K–170K nodes), average degree, homophily (adjusted homophily from -0.19 to 0.43), clustering coefficients, and feature types (Section 3, Table 1).

- **Broad and systematic evaluation across model families.** The paper implements GNNs (GCN, GraphSAGE, GAT, GT, and their –sep variants) within the same codebase as a ResNet baseline, enabling direct apples-to-apples comparison on whether graph structure helps. It also covers three GBDT implementations (XGBoost, LightGBM, CatBoost), two tabular deep learning models (MLP-PLR, TabR), and two specialized methods (BGNN, EBBS). The use of fixed 50:25:25 splits, 5 independent runs with reported means and standard deviations, and a consistent preprocessing pipeline (quantile transformation for numerical features, one-hot encoding for categorical) is solid practice.

- **Actionable insights that challenge common assumptions.** The paper identifies several practically useful findings: (a) the best GNN architecture varies significantly across datasets (GCN best on tolokers-tab, GraphSAGE on city-roads, GAT on hm-prices), (b) standard GNNs generally outperform the specialized BGNN/EBBS methods designed for tabular-feature graphs, and (c) PLR numerical feature embeddings — borrowed from tabular deep learning — consistently improve GNN performance, sometimes dramatically (e.g., GCN from 82.83 to 89.52 ROC-AUC on questions-tab).

- **Inclusion of underexplored real-world data characteristics.** Several datasets contain unlabeled nodes (a common but understudied scenario in graph ML benchmarks), and the benchmark spans both regression and classification, homophilous and heterophilous graphs, and both weighted and unweighted constructions.

## Weaknesses

### Fatal
None.

### Major
- **Asymmetric hyperparameter tuning undermines the reliability of the headline performance comparisons.** The paper states (line 106-108): *"For GBDT and tabular deep learning models, we conduct an extensive hyperparameter search using Optuna… For GNNs, we found that, when augmented with skip-connections and layer normalization, they are not very sensitive to the hyperparameter choice, thus we did not tune them for graph neural models."* This is a consequential experimental asymmetry: the best graph-agnostic results come from heavily tuned models, while GNN results come from an untuned default configuration. The paper's central comparative claims — that GNNs (especially PLR-augmented) "always outperform" graph-agnostic models, and that standard GNNs beat specialized methods — are built on this mismatch. Crucially, the paper provides no evidence in the main text for the claimed hyperparameter insensitivity; no sensitivity analysis, ablation, or range-search is shown. On datasets where margins are thin (e.g., city-reviews: best PLR-GNN 93.36 vs. best graph-agnostic 93.04 ROC-AUC), proper GNN tuning could shift the relative ranking. The paper would be stronger if it either (a) tuned GNNs with comparable effort, (b) provided a sensitivity analysis demonstrating that GNN performance is genuinely flat across hyperparameters on these specific datasets, or (c) transparently prefaced the relevant claims as *conservative lower bounds* rather than definitive relative performance statements. The benchmark contribution itself is independent and valuable, but the empirical recommendations are weakened by this asymmetry.

### Minor
- **No assessment of statistical significance for close comparisons.** With 5 runs and standard deviations reported, several key comparisons involve small margins (e.g., city-reviews: 93.36 vs. 93.04). The paper would benefit from a simple paired test or confidence interval to indicate whether observed differences are likely above noise. This is particularly relevant for the claim that PLR-augmented GNNs "always outperform" graph-agnostic models.

- **Low R² values on regression tasks are not interpreted.** Several regression results show very low R² values (e.g., GCN on avazu-devices at 0.005, LightGBM at 0.007). The paper does not discuss whether the absolute scale of these numbers affects the interpretation of relative improvements — a 0.01 difference in R² near zero may or may not be meaningful, and the reader is left to guess.

- **No baseline using graph-agnostic models with engineered structural features.** In practice, practitioners often feed graph-derived features (node degree, PageRank, clustering coefficients, etc.) into tree-based models. The paper compares GNNs against graph-agnostic models that completely ignore graph structure, which is the right first baseline, but adding a "graph features + GBDT" baseline would provide a stronger test of whether GNNs are needed or whether simpler structural features suffice.

### Trivial
- The ResNet baseline is acknowledged as a "simple baseline" not designed for tabular data, so its consistently weak performance is expected and not over-interpreted. Worth noting only because it occupies a column in the results tables.

## Nice-to-Haves
- An ablation quantifying the effect of unlabeled nodes (removing them or using only labeled subgraphs) would strengthen the claim that this characteristic benefits graph-aware models and is a useful dimension of the benchmark.
- A brief discussion of memory and runtime costs for GNNs vs. tabular models would help practitioners assess practical feasibility, especially given the larger datasets (hm-products: 170K nodes).

## Removed Points
The following points were raised by reviewers but are excluded from the main evaluation per policy:
- **Benchmark availability / "not yet released"** — Removed per policy: the paper states it will release upon completion of legal procedures. Cited entities are assumed to exist as of the current date.
- **Missing GNN hyperparameter values / architecture details in the main text** — Removed per policy: the paper references Appendices D and C for model configurations. The parser strips appendix content, but these sections exist in the original submission.
- **Missing sensitivity analysis for GNN hyperparameter insensitivity claim** — To the extent this may have been provided in the appendix, it should not be penalized as missing. The core concern about asymmetric tuning is retained in Major Weaknesses above because it is an experimental design issue that transcends any single appendix section.

## Novel Insights
The most valuable observation emerging from this review — one that goes beyond the paper's own framing — is that the *type of graph construction* (interaction-based vs. similarity-based, bipartite projection vs. direct edges) may be a stronger predictor of GNN success than any single architectural choice. The datasets where GNNs provide the largest gains (hm-groups: +15 points accuracy over graph-agnostic) involve bipartite projections where the graph captures co-purchase patterns, while datasets where margins are thin or negative (city-reviews, amazon-users) involve user-review or fraud-detection graphs. This suggests that the *alignment between graph construction and task label* may matter more than whether graph structure is present at all — a hypothesis the paper does not explore but that future work could build on.

## Suggestions
1. **Address the tuning asymmetry.** The single highest-leverage improvement is to either tune GNNs comparably (even a modest random search over 50 trials would suffice) or provide a sensitivity analysis showing flat performance across hyperparameters. If neither is feasible, clearly reframe all comparative claims about relative performance as *preliminary evidence using untuned GNNs*.
2. **Add a "graph features + GBDT" baseline.** Feeding degree, PageRank, and clustering coefficients into LightGBM would strengthen the practical recommendations by showing whether full GNNs are needed or simpler structural features suffice.
3. **Include statistical significance indicators** (e.g., 95% confidence intervals or paired test results) for the comparisons that matter most, especially the close ones.
4. **Discuss the regression R² floor.** Even a brief note on whether the near-zero R² values affect the interpretation of relative gains would improve the paper's thoroughness.

## Score and Decision

**Originality:** High. First benchmark of its kind fills a genuine gap between graph ML and tabular ML evaluations.  
**Importance:** High. Real-world data with heterogeneous features and graph structure is pervasive in industry; the benchmark directly supports both method development and fair comparison.  
**Claims:** Mostly well-supported, but the central comparative claims are weakened by asymmetric tuning. The benchmark contribution is unaffected.  
**Soundness:** Solid for the benchmark design and dataset construction; the experimental design has a notable methodological limitation in the tuning protocol.  
**Clarity:** Clear and well-organized.  
**Value to community:** High as a resource; moderate-to-high for the empirical insights (contingent on addressing the tuning concern).

Despite the tuning asymmetry — which is a real but not fatal issue, and one the paper is transparent about — the benchmark itself is a timely and needed contribution. The paper's core contribution (the datasets and their characterization) stands independently of any individual performance finding. The insights are useful and largely robust to the asymmetry (the asymmetry mostly *penalizes* GNNs, making their wins more, not less, convincing). The weaknesses are addressable and do not undermine the primary contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>