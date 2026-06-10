## Summary

GDA combines Weisfeiler-Leman (WL) graph kernels with cosine-similarity-based distribution analysis to characterize the structural distribution of graphs within and across classes. The paper reports case studies on ENZYMES, MalNet-Tiny, and ogbg-ppa showing that GDA can detect bimodal class structures (e.g., transferase enzymes), identify distribution shifts between data splits, and pinpoint structural motifs correlated with misclassifications. The central empirical claim is that GDA-informed data interventions yield measurable accuracy improvements (up to 4.3%).

## Strengths

- **Quantified benefit from distribution-aware data restructuring (MalNet-Tiny).** Section 4.2.1 (line 209) reports a 4.3% average performance improvement over baseline across 10 runs after GDA detected and corrected distribution shifts between training/validation/test splits. This is a concrete, measurable outcome that demonstrates practical utility.

- **Specific structural motif identified as a cross-category confounder (ogbg-ppa).** Section 4.2.2 (lines 216–217) identifies a structural motif present in 12% of misclassified Category 5 samples but prevalent in 68% of Category 27 samples. This provides an interpretable, graph-level finding that node/edge-level explainers struggle to produce, directly supporting the claim of identifying structural features responsible for misclassifications.

- **Bimodal distribution detection with external corroboration (ENZYMES transferase).** GDA detects a bimodal distribution in transferase enzymes, confirms it with biochemical literature (Giegé et al., 2012; Breton et al., 2006), and reports a 2.3% improvement for that category after cluster-aware training — a validated data-centric insight.

- **Feature-agnostic operation.** GDA operates on graph structure alone without requiring node or edge features, making it applicable to datasets where gradient-based methods (Grad-CAM, Integrated Gradients) fundamentally cannot operate (e.g., MalNet-Tiny).

## Weaknesses

### Fatal

None.

### Major

- **Abstract's "outperforms baseline methods" claim is completely unsupported.** The abstract states GDA "outperforms baseline methods in identifying specific structural features responsible for misclassifications," yet Section 4 contains zero comparisons to GNNExplainer, PGExplainer, SubgraphX, Grad-CAM, Integrated Gradients, or any other explainability method. All of these are discussed in the Related Work but never used as baselines. The only "baseline" is the default dataset split. This claim should be removed or substantiated with direct experimental comparison.

- **GDA does not explain GNNs in the sense the paper claims — it analyzes dataset structure without ever interacting with the model.** The entire pipeline (WL embedding, class-mean computation, cosine similarity scoring, kurtosis) operates on raw graph structure. There is no backpropagation through the GNN, no analysis of latent representations, no feature attribution w.r.t. model parameters, and no mechanism tying the analysis to any specific prediction. The paper positions GDA against GNNExplainer and Grad-CAM (instance-level, model-specific explainers) but delivers something categorically different: a data-centric structural analysis tool. This framing mismatch inflates the contribution and obscures what the method actually does. The paper would be stronger if it transparently scoped itself as a data analysis tool for understanding structural heterogeneity and distribution shifts — a useful but different contribution.

- **Experimental reporting lacks quantitative rigor.** No standard deviations are reported despite the setup stating "ten runs with seeds set to {1,...,10}" (Section 4.1). The 4.3% and 2.3% improvements are given as point estimates without variance. The ogbg-ppa motif analysis claims "a significant reduction in misclassification rates" with no before/after numbers. There are no confusion matrices, per-class accuracy tables, or precision/recall/F1 for any dataset. Baseline (pre-GDA-intervention) performance numbers are never reported, making it impossible to assess whether reported improvements are meaningful in context.

- **The normalized distribution score z(G) adds no information.** Equation (9) defines z(G) = S_c(G) / RMS(S_c(G')). Since the denominator is constant across all graphs within a class, z(G) is monotonically related to S_c(G) and carries no information beyond the cosine similarity itself. The paper interprets lower z(G) as "significant deviations," but this is identical to saying lower S_c(G) indicates lower similarity to the class mean — which was already the definition. This is not a meaningful normalization.

### Minor

- **Kurtosis definition and interpretation are internally inconsistent.** Section 3.2.2 defines excess kurtosis (subtracts 3) but then states "A kurtosis value greater than 3 indicates a distribution with heavy tails" and "less than 3 indicates light tails." If the formula already subtracts 3, the threshold should be 0 (standard normal → 0). This error affects the interpretability of the ENZYMES transferase analysis where high kurtosis is cited as evidence of bimodality. The formula or the threshold should be corrected.

- **No ablation or sensitivity analysis for the sparsity filtering threshold κ.** The threshold is set to max(1, 0.002 × |H|) with justification only as "conservative" (Section 3.1). How many dimensions are retained vs. removed, and whether the distribution scores are robust to this choice, is never analyzed.

- **No ablation of WL kernel depth h.** The number of WL iterations is a key hyperparameter controlling the granularity of structural information captured. It is never discussed beyond being mentioned in the method.

- **Post-hoc structural attribution (Section 3.3) is described at a placeholder level.** The paper states that "rerunning the WL kernel with degree sequence tracking" can "identify specific substructures responsible for classification errors," but provides no algorithm, no detail on how substructures are extracted from label evolution, and no formal description of how "responsibility" is attributed. The ogbg-ppa motif finding would be stronger if accompanied by a concrete method description.

### Trivial

- Equation (1) writes τ_h(G) = Σ_{v∈V} l_h(v), summing discrete hash labels directly. The intended operation is clearly a histogram of label frequencies (as in the standard WL subtree kernel), but the notation is imprecise as written.

## Nice-to-Haves

- Reporting standard deviations and per-model breakdowns (GraphSAGE vs. GIN) for all experiments would significantly strengthen the paper.
- A comparison of GDA-informed data splits against simple alternatives (e.g., stratified by graph size) would demonstrate whether GDA provides value beyond common-sense baselines.
- Sensitivity analysis of the WL depth h and sparsity threshold κ would improve methodological transparency.

## Removed Points

- *"The method does not explain GNNs" as a fatal flaw* — Demoted from Fatal to Major. The method does surface structural insights that explain *why* models underperform (e.g., bimodal classes cause confusion), which is a legitimate form of explanation. The problem is the framing mismatch with instance-level model-specific explainers, not that the method has no explanatory value.
- *Equation (1) notation error as a "technical concern"* — Demoted to Trivial. The intent is clear from the algorithm description (histogram of labels); the notation is imprecise but not misleading.
- *Sparsity filtering "no ablation" as a critical issue* — Demoted to Minor. A valid observation, but not central to the paper's claims.
- *"No comparison to any existing explainability method"* — Merged into the Major weakness about the unsupported "outperforms" claim.
- *"No confusion matrices, per-class accuracy tables"* — Merged into the Major weakness about experimental rigor.
- *Strength Finder's generic strengths (e.g., "addresses an important problem")* — Removed. These are not specific to the paper's evidence.
- *Strength about O(n·m) complexity* — Removed. This is a stated property, not an empirically demonstrated strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Reframe the paper transparently as a **data-centric graph analysis tool** rather than a GNN explainability method. Remove or substantially qualify the "outperforms baseline methods" claim unless baselines are actually evaluated.
2. Fix the kurtosis inconsistency: either use raw kurtosis (threshold 3) or excess kurtosis (threshold 0).
3. Report standard deviations for all experimental results, provide per-class breakdowns, and include baseline (pre-intervention) performance numbers.
4. Add ablations for WL depth h and sparsity threshold κ.
5. Either remove the z(G) normalization or explain what information it adds beyond S_c(G).
6. Provide a concrete algorithm for the post-hoc structural attribution (Section 3.3) rather than a paragraph-level description.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>