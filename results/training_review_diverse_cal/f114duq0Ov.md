Now I have all the facts. Let me compose the final consolidated review.

## Summary

This paper proposes M³-Impute, a graph-based missing value imputation method that explicitly incorporates missingness information through three novel components: (1) a refined embedding initialization that blends observed values with a small constant for missing entries, (2) a Feature Correlation Unit (FRU) with learnable soft masks to capture feature-wise dependencies, and (3) a Sample Correlation Unit (SRU) with mutual-sample and irrelevant-feature masking to capture sample-wise correlations. The method models tabular data as a bipartite graph and frames imputation as link prediction, extending the GRAPE framework with explicit missingness-aware masking.

## Strengths

- **Novel explicit modeling of missingness information.** Prior graph-based imputation (GRAPE) initializes embeddings without using the mask and does not filter by observability during correlation learning. M³-Impute's refined initialization (Eq. 1) and its soft-masking schemes in FRU (Eq. 2) and SRU (Eqs. 4–7) directly encode whether each value is observed. The ablation study (Table 2) confirms that each component contributes to the improvement over GRAPE, providing empirical support for the design.

- **Strong empirical performance on the reported 8 datasets.** In MCAR 30% setting (Table 1), M³-Impute achieves the best MAE on 6 of 8 datasets (Yacht, Wine, Concrete, Housing, Energy, Power) and second-best on 2 (Naval, Kin8nm), with up to 22.22% improvement over the second-best method. It also shows consistent gains under MAR and MNAR settings (Section 4.2). The method is robust across missing ratios from 10%–70% (Figure 1), different peer sample sizes, and initialization parameter ε (Table 3).

- **Thorough ablation and robustness analysis.** The ablation (Table 2) separates the contributions of the initialization unit, FRU, and SRU. Robustness experiments cover varying missing ratios, peer sizes, ε values, and GNN backbones (GraphSAGE, GAT, GCN in Table 4), all showing M³-Impute outperforming its GRAPE counterpart. This breadth of analysis strengthens confidence that the method's gains are not overfitted to a specific configuration.

- **Computational efficiency.** Inference on GPU completes in under one second for all tested datasets (Table 5), and CPU runtime is comparable to GRAPE — much faster than deep generative baselines like MIWAE and HyperImpute — making the accuracy gains practically feasible.

- **Clear problem formulation and reproducible architecture description.** The paper formally defines the bipartite graph construction, masked data matrix, imputation as link prediction, and provides Algorithm 1 summarizing the forward pass.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The initialization-only improvement over GRAPE is modest.** The "Init Only" variant in Table 2 achieves MAE very close to GRAPE's — often within one standard deviation (e.g., Yacht: 1.43±.01 vs 1.46±.01; Wine: both 0.60; Concrete: 0.74 vs 0.75; Housing: 0.63 vs 0.64; Energy: 1.35 vs 1.36). While the improvement is consistent (better on every dataset), its small magnitude means the initialization unit alone contributes little. The paper's larger gains come from FRU and SRU, which is consistent with the paper's own narrative, but the "initialization" is highlighted as one of three named contributions. The authors should clarify that the key novelty lies in FRU+SRU rather than over-claiming the initialization component's impact.

2. **Missing MLP architectural specifications.** The paper describes σ₁ through σ₆, φ_α, and φ_γ only as "MLP with GELU activation" without specifying number of layers, hidden dimensions, or output dimensionalities. Similarly, the GNN variant "E-GraphSage" is described only by reference to GRAPE. These omissions make independent reproduction unnecessarily difficult. While exact reproduction is not required for acceptance, providing these details (even in an appendix) would significantly strengthen reproducibility.

3. **Similarity-based sampling in SRU is not clearly better than uniform sampling.** The ablation (Table 2) shows that M³-Uniform (uniform random sampling) performs nearly identically to the full M³-Impute (similarity-proportional sampling) across all 8 datasets — often within 0.01 MAE. The paper acknowledges this in Section 4.3 but does not adequately justify why the more complex similarity-based sampling is needed. If the sampling strategy adds complexity without measurable benefit, the method would be simpler and equally effective with uniform sampling. The authors should either provide evidence that similarity-based sampling helps in specific settings (e.g., high missing ratios, certain data types) or simplify the method.

### Trivial

- The paper refers to "σ₁(m_s)" where m_s is a binary mask vector of length m, processed by an MLP to produce an m-dimensional real vector. Since m (the number of features) is small in the tested datasets (e.g., 7 for Yacht), this design choice is somewhat overparameterized — a learned per-feature scaling vector would be simpler. Not a structural problem, but worth noting for transparency.

## Nice-to-Haves

- The paper reports mean ± std from 5 runs, which is standard. Formal paired significance tests (e.g., Wilcoxon signed-rank) comparing M³-Impute against GRAPE across the 8 datasets would strengthen the claim that improvements are statistically meaningful beyond standard-deviation overlap.
- A deeper analysis of when FRU and SRU individually help most — correlating dataset properties (feature correlations, sample homogeneity, dimensionality) with the relative gains of each component — could provide practical guidance for practitioners choosing which component to prioritize.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing experimental results for the claimed 25 datasets / selection of reported datasets.** The harsh critic argues that the paper claims 25 datasets but only shows 8. The paper states "We conduct experiments on 25 open datasets" (Section 4.1) and claims "20 best and 4 second-best MAE scores on average" in the abstract/conclusion. However, the parser strips appendix sections from all papers; full experimental tables across all 25 datasets likely existed in the original submission's appendix. Following the rule that parser-stripped content should not be penalized, this criticism is removed. The main-text results on 8 datasets are self-contained and demonstrate the method's effectiveness.

- **The learnable weighting parameter α range is [0, 0.632].** The critic claims γ(x) = 1 − 1/e^{|x|} has range [0, 1−1/e] ≈ [0, 0.632]. This is factually wrong: as |x| → ∞, γ(x) → 1, so the range is [0, 1). The value 0.632 is γ(1), not the maximum. This criticism is removed.

- **The soft mask in FRU is overparameterized (subjective design preference).** The critic argues σ₁(m_s) mapping binary m_s to an m-dimensional vector via MLP is overparameterized. This is a design choice, not a verified weakness. The paper shows the design works empirically. Removed as a non-substantive preference.

- **SRU sampling introduces uncontrolled variance (already addressed).** The paper already analyzes this via the M³-Uniform ablation in Table 2, finding minimal difference. This is not an unaddressed gap. Removed.

- **Missing statistical significance testing / failure analysis.** These are nice-to-haves or scope items, not weaknesses. The paper provides std from 5 runs, which is standard practice in this literature. Feature-independence in Kin8nm and linear-correlation in Naval are discussed. Removed as not actual weaknesses.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest empirical evidence comes from the combination of all three components (init + FRU + SRU), yet the most novel and clearly impactful component is FRU+SRU rather than the initialization. The "Init Only" gains over GRAPE are tiny (often <0.02 MAE), while adding FRU or SRU yields visibly larger drops. The paper acknowledges this implicitly by listing all three as contributions, but a sharper decomposition — e.g., a direct head-to-head of "GRAPE + FRU only" vs. "full M³-Impute" — would cleanly isolate where the real novelty lives. The M³-Uniform result further suggests that the sophistication of SRU's sampling may be unnecessary, potentially simplifying the method without loss.

## Suggestions

1. Specify the layer counts, hidden dimensions, and output dimensionalities for all MLPs (σ₁–σ₆, φ_α, φ_γ) — even a brief sentence or appendix table would suffice.
2. Provide a clearer decomposition of the initialization contribution: state directly that the main gains come from FRU+SRU rather than from the initialization alone.
3. Either justify why similarity-based sampling is retained over uniform sampling (e.g., benefits on higher-dimensional or noisier data not included in the 8-dataset benchmark) or adopt the simpler uniform variant as the default.
4. Clarify whether the "25 datasets" claim refers to results in the appendix (which exists in the original submission) and, if possible, add a concise summary of all 25 results in the main paper (e.g., a win/loss/tie table).

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>