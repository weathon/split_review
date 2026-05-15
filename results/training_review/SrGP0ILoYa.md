Now I have a thorough understanding of the paper and can verify each claim against the actual text. Let me synthesize the final review.

---

## Summary

TopER introduces a graph embedding method that replaces costly persistent homology computation with linear regression on node-count and edge-count sequences collected during filtration, producing a 2D vector (pivot *a*, growth *b*) per filtration function. The paper claims competitive classification performance across eight benchmark datasets, demonstrates interpretable 2D visualizations, and provides a theoretical stability guarantee. The core idea — summarizing the filtration curve with a simple linear fit instead of computing persistence diagrams — is computationally efficient ($O(n(|\mathcal{V}|+|\mathcal{E}|))$) and yields interpretable coordinates.

## Strengths

- **Computationally efficient and theoretically grounded design**: TopER replaces the cubic complexity of full persistent homology with linear regression on node/edge counts during filtration, achieving $O(n(|\mathcal{V}|+|\mathcal{E}|))$ complexity. The paper provides a stability theorem bounding embedding differences by the $L^1$ difference of filtration functions (Theorem 4.1, Corollary 4.2), and demonstrates scalability to 100K-node graphs in ~2 minutes (Fig. 3).

- **Interpretable 2D embeddings**: The (pivot, growth) coefficients have clear structural meaning — pivot reflects initial connectivity, growth reflects edge-accumulation rate. The paper shows visualizations that meaningfully separate graph classes and detect outliers across multiple datasets (Figs. 1, 5), a genuinely useful property for exploratory analysis.

- **Ablation study confirms complementary information across filtration functions**: The combined TopER vector (using up to 7 filtration functions) substantially outperforms any single function across all datasets (Table 4); e.g., BZR accuracy rises from 82.73% (best single) to 90.13% (full). This demonstrates that different topological perspectives capture complementary structural information.

- **Novel Popularity filtration function**: The proposed Popularity function extends node degree with neighbor-degree information, contributing to competitive performance on several datasets (Table 4).

## Weaknesses

### Fatal
None.

### Major

1. **Classification comparison uses numbers from different papers with potentially incompatible evaluation protocols.** The paper sources baseline results from original publications (line 260) without re-running them under the identical 90/10 stratified 10-fold CV protocol used for TopER. Different papers may use different train-test splits, CV folds, hyperparameter tuning, and metrics. The "average deviation" column (Table 2) averages across these heterogeneous settings, which has no clear statistical interpretation. The TopER vs. PH comparison (Table 5) suffers from the same issue, using results from Cai et al. (2020) which employed different experimental conditions. This does not invalidate the method's value but means the headline claim of "state-of-the-art" is not rigorously established.

2. **Clustering evaluation is weak and non-standard.** The clustering comparison uses only Spectral Zoo as a baseline (Table 3), which the paper itself notes is the only other model producing low-dimensional graph embeddings — but this is a very limited comparison. Moreover, the clustering task embeds graphs from *different datasets* and evaluates separation by dataset identity rather than clustering unlabeled graphs from a single source. The results are suggestive but do not constitute a rigorous clustering benchmark.

3. **Feature selection procedure may introduce data leakage.** The paper describes selecting filtration functions via t-test (p<0.05) and Lasso (cv=10) *before* describing the cross-validation procedure (Section 5.1, *Filtration functions*). It does not explicitly state that this selection is nested inside the outer 10-fold CV loop. If feature selection is applied on the full dataset before CV, the reported accuracy numbers would be optimistically biased. This is a methodological ambiguity that the authors must clarify.

### Minor

1. **The theoretical stability result offers limited new insight.** Theorem 4.1 and Corollary 4.2 transfer standard stability from persistence diagram Wasserstein distance to TopER vectors, then from function $L^1$ distance to persistence diagrams. The chain is: $\|$TopER diff$\|_1 \leq C \cdot W_1(PD) \leq C' \cdot \|f-g\|_1$. This is a clean application of known PH stability but does not add a new theoretical principle. No empirical verification of stability under graph perturbations (e.g., random edge noise) is provided.

2. **The choice of linear fit is not empirically justified.** The paper states that "line fitting may not always be a linear choice" and defers to the appendix (line 138), but no evidence is shown that the (node count, edge count) relationship is approximately linear for real graphs. For graphs with irregular growth patterns, a polynomial or spline fit might be more appropriate, and the sensitivity of results to this choice is unexplored.

3. **Visualization evaluation is exclusively qualitative.** The paper provides compelling visualizations and plausible interpretations (e.g., MUTAG class differences in growth rate), but no quantitative metrics for embedding quality such as trustworthiness, continuity, or neighborhood preservation are reported.

4. **The "first topology-based graph representation learning method" claim is overstated.** Persistence diagram vectorization methods (e.g., PersLay, PLL) also produce low-dimensional graph embeddings. TopER's genuine novelty is in *bypassing PH computation entirely*, not in being the first to produce low-dimensional topology-based embeddings. The "first" qualifier should be more precisely scoped.

### Trivial
None.

## Nice-to-Haves

- Evaluating TopER embeddings with a simple non-parametric classifier (e.g., k-NN) to isolate the discriminative power of the raw (a,b) vectors without a learned MLP.
- Sensitivity analysis of the number and spacing of filtration thresholds $\{\epsilon_i\}$ on the resulting embeddings.
- Empirical stability verification by adding random edge noise and measuring change in TopER vectors.

## Removed Points

These points were flagged for removal; treat them with caution:

- **Criticism that the "refine" and "theorems" sections are missing from the paper**: The parser strips appendix sections from all papers; they exist in the original submission. Removed per hard rules.
- **Criticism that "the MLP conflates embedding quality with classifier ability" as a fatal flaw**: The paper evaluates embeddings through clustering (without MLP) and visualization, and the use of a learned classifier on extracted features is standard practice. Weakened to a nice-to-have suggestion (k-NN evaluation) rather than a core weakness.
- **Strength about "state-of-the-art classification performance" from the Strength Finder**: This conflicts with verified weakness #1 (incomparable baseline protocols). Per instructions, the weakness wins, so this strength is dropped from the main list.
- **Strength about "superior clustering quality" from the Strength Finder**: The weakness about a single baseline and non-standard clustering task undermines this claim. Tempered in the main review.

## Novel Insights

The reviews reveal an interesting tension: TopER's strongest contributions lie in efficiency and interpretability rather than raw classification accuracy, yet the paper leads with classification benchmarks whose rigor is questionable. Meanwhile, the reviewer's concern about the MLP conflating embedding and classifier contributions — though standard practice in the field — actually highlights an advantage of TopER that the paper underplays: because TopER produces *2D* vectors per filtration function, one could directly visualize the decision boundary of a simple classifier, making classification itself interpretable. The paper's own ablation study shows that even single-function TopER vectors (2D) achieve non-trivial accuracy (e.g., 82.73% on BZR with degree function alone), which is genuinely impressive for a 2D descriptor and deserves more emphasis. The central methodological issue — baseline comparison without re-implementation — is pervasive in this subfield and not unique to this paper, but it does mean the paper's strongest empirical claims should be read as suggestive rather than definitive.

## Suggestions

1. **Rerun baselines under a unified protocol** using an established framework (e.g., the Errica et al. 2020 codebase) to produce strictly comparable classification results. This is the single change that would most strengthen the paper.
2. **Explicitly state whether feature selection (t-test + Lasso) is nested inside the cross-validation loop.** If it is not, recompute all classification numbers with proper nested CV.
3. **Add at least one additional baseline for clustering** (e.g., k-means on simple graph statistics, or a standard graph kernel embedding) to contextualize the clustering results.
4. **Weaken the "first" claim** in the introduction to more precisely describe TopER's novelty (e.g., "the first topology-based method to bypass persistence diagram computation entirely, producing 2D embeddings at linear time").
5. **Include a quantitative visualization quality metric** (e.g., trustworthiness or Kullback-Leibler divergence of neighborhood distributions) to complement the qualitative visualizations.

## Score and Decision

The paper proposes a genuinely novel, efficient, and interpretable graph embedding method with a clean theoretical motivation. The core technical contribution is solid. However, the experimental evaluation has significant limitations: the classification baselines are not compared under identical conditions, the clustering evaluation is too narrow, and the feature selection procedure is not clearly documented as nested within CV. These issues are addressable but prevent full confidence in the reported results. The paper's strengths in efficiency, interpretability, and ablation insights are compelling.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>