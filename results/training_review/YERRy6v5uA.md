Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the consolidated review.

## Summary

This paper revisits Graph Structure Learning (GSL) for GNNs, proposing a three-step framework (GSL bases generation → new structure construction → view fusion) to systematically analyze GSL's effectiveness. Through theoretical analysis (showing that graph convolution on GSL-constructed graphs does not increase mutual information beyond the GSL bases) and extensive experiments — adding GSL to baseline GNNs and removing it from SOTA GSL-based methods — the paper argues that GSL itself is largely unnecessary and that observed performance gains actually stem from pretrained GSL bases (e.g., via self-training).

## Strengths

- **Comprehensive three-step GSL framework (Section 3).** The paper decomposes GSL into bases generation, new structure construction, and view fusion, which is more systematic than prior surveys that focus almost exclusively on the structure-construction step. This taxonomy enables precise ablation of each component's contribution.

- **Extensive empirical evaluation with two complementary designs.** The paper performs both (a) GNN+GSL vs. GNN under controlled bases (Table 1) and (b) SOTA vs. SOTA-GSL ablation (Table 2), across 8 SOTA methods and numerous datasets including heterophilous, homophilous, and binary-class benchmarks. This two-pronged design strengthens the conclusion beyond what either experiment alone would support.

- **Identification that pretrained bases (self-training), not graph construction, drive performance (Section 5.3, Figure 5).** The ablation reveals that replacing raw features with pretrained representations (MLP(X), GCN(X,A), GCL(X,A)) substantially improves accuracy, while the graph reconstruction step itself provides negligible benefit. This insight redirects attention to more essential components like self-training.

- **Complexity analysis quantifying GSL's overhead (Section 4.3).** The paper provides a clean complexity breakdown ($O(|\mathcal{V}|^2F)$ for graph construction vs. $O(|\mathcal{E}|F)$ for GCN), making the practical cost argument concrete.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 2 is a direct consequence of the data processing inequality, and the paper explicitly acknowledges it does not cover optimization-based GSL.** The theorem states that for deterministic transformations of the bases B (graph convolution on a structure G' that is a deterministic function of B), mutual information cannot increase. This is a textbook application of the DPI, not a GSL-specific theoretical result. The paper's footnote admits "this theoretical analysis cannot be extended to optimization-based GSL," which includes methods like IDGL, GRCN, GloGNN, and NodeFormer — exactly the methods that dominate the literature. While the paper attempts to cover this gap through experiments (SOTA-GSL ablation), this creates a structural mismatch between the theoretical narrative ("GSL is unnecessary") and the methods actually tested theoretically. The theory only covers similarity-based GSL with deterministic bases, which is a narrow subset.

- **The synthetic observations (Section 4.1) use only kNN-based GSL, limiting support for the claim "no matter which type of graph structure construction methods are used."** The controlled CSBM-H experiments — the only place where MI is directly measured to support the theory — use kNN as the sole GSL variant. The paper does not test optimization-based or attention-based GSL on synthetic data, leaving a gap between the theoretical claim (MI bound) and the empirical observations in Figure 1. Since the theory is acknowledged not to cover optimization-based methods, the synthetic experiments could have tested at least one such method to strengthen confidence.

- **The paper's title, abstract, and conclusion claim broader generality than the evidence supports.** The title "Rethinking Structure Learning For Graph Neural Networks" and abstract statements like "GSL does not contribute to the improved performance" are framed as general conclusions about GSL. However, the evidence is confined to node classification on small-to-medium graphs (up to a few thousand nodes), similarity-based GSL variants in controlled experiments, and GSL methods whose designs incorporate graph construction as an explicit module. The paper does not discuss whether the findings extend to GSL for graph generation, link prediction, large-scale industrial graphs, or settings where GSL is used for adversarial purification. Narrowing the stated scope (e.g., "Rethinking Similarity-Based Structure Learning for Node Classification") would better match the evidence.

### Minor

- **The graph quality analysis (Section 5.2) is qualitative on a single dataset.** The adjacency-matrix visualizations for Wisconsin are illustrative but not supported by quantitative metrics (e.g., change in homophily, intra-class edge ratio) or multi-dataset statistics. The claim that "non-GSL methods produce more block-diagonal graphs than GSL methods" would be stronger with numerical evidence across datasets.

- **The explanation for why GCN+GSL's MI stays flat across homophily (Observation 3, Figure 1) is not fully developed.** The paper notes that GCN+GSL's green line is stable while MLP and GCN vary, and attributes this to GSL constructing graphs with stable homophily from feature-space kNN. But this is stated as a hypothesis without verification (e.g., measuring the homophily of the kNN-constructed graph across varying original-graph homophily levels).

- **The SOTA-GSL ablation (Table 2) description does not specify whether hyperparameters were re-tuned for the ablated variants or simply reused from the original models.** The paper states "within the same hyperparameter search space," which is ambiguous — re-tuning within the same search space is stronger than freezing hyperparameters, but this is not explicitly clarified.

### Trivial
None.

## Nice-to-Haves

- Testing at least one optimization-based GSL variant (e.g., a differentiable similarity learning method) on the CSBM-H synthetic data to verify whether the MI bound empirically holds when bases are learned jointly.
- Reporting quantitative homophily metrics (edge homophily or node homophily) for GSL-constructed graphs across multiple datasets in Section 5.2.
- Measuring and reporting the homophily of the kNN-constructed graph in Figure 1 to support the flat-MI explanation in Observation 3.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about Table 3 (SOTA-GSL) results not being numerically available.** *(Rationale:* The table is included via `\input{}` in the original submission; the parser strips such inclusions. Per hard rules, doubts about missing content caused by the parser are invalid — the table exists in the paper.)

- **Criticism that GNN+GSL experiments use "only k-NN."** *(Rationale:* The paper explicitly states three graph construction methods: cosine similarity at graph level (cos-graph), node level (cos-node), and k-nearest neighbors (kNN). The critic's claim is factually wrong.)

- **Criticism about missing related works.** *(Rationale:* Per hard rules, I cannot comment on missing references without external verification capability.)

- **Criticism about Theorem 1 not being novel.** *(Rationale:* Standard Fano-inequality bounds are common baselines; their inclusion as background is not a weakness. The paper does not claim Theorem 1 as a contribution.)

- **Criticism that the paper's scope excludes graph generation, link prediction, or large-scale graphs.** *(Rationale:* The paper explicitly focuses on node classification. Demanding it address problems outside stated scope is scope creep. Soft rule applies.)

- **Criticism about "the paper never uses the framework to compare GSL methods."** *(Rationale:* The framework is used to design the ablation experiments (Section 5.1) and to categorize methods in the complexity analysis (Table 3, referenced in Section 4.3). The critic missed this usage.)

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper's theoretical contribution (Theorem 2) is strongest for the simplest GSL methods (deterministic, fixed-bases similarity construction), yet those are precisely the methods where practitioners would least expect surprising benefits. The real debate in the GSL community centers on optimization-based methods where the theory does not apply. This means the paper's core provocation — that GSL is "unnecessary" — rests disproportionately on the experimental SOTA-GSL ablation, not on the theory. A stronger paper would either extend the theory to cover learned bases (perhaps through variational bounds or PAC-Bayes analysis) or explicitly reframe the contribution as an experimental finding with a heuristic theoretical justification, rather than presenting the theory as the primary evidence.

## Suggestions

1. **Narrow the scope in the title and abstract** to reflect the paper's actual coverage (node classification, similarity-based and modular GSL methods). For example: "Rethinking Similarity-Based Structure Learning for Node Classification."

2. **Add a controlled synthetic experiment with a differentiable/optimization-based GSL variant** (e.g., learning a similarity metric with gradient descent on CSBM-H) to test whether the MI bound behavior holds when bases are jointly optimized.

3. **Quantify the visualization in Section 5.2** by reporting homophily metrics (edge homophily, intra-class edge ratio) for GSL and non-GSL constructed graphs across all datasets, with variance.

4. **Clarify the hyperparameter re-tuning procedure for the SOTA-GSL ablation:** specify whether hyperparameters were re-optimized for each ablated variant or simply carried over from the original model.

5. **Measure and report the homophily of the kNN-constructed graph** in Figure 1 as a function of original-graph homophily, to substantiate the explanation for why GCN+GSL's MI stays flat.

## Score and Decision

**Originality:** The question "is GSL necessary?" is well-motivated and the three-step framework is a useful organizational lens. However, the theoretical contribution (DPI-based MI bound) is not novel, and the core experimental insight (that removing GSL doesn't hurt) builds on prior observations (e.g., GNN strong baselines papers cited by the authors).

**Importance of research question:** High. Questioning a widely-used technique with substantial computational overhead is a timely and practically relevant inquiry.

**Claims supported:** Partially. The experimental evidence for similarity-based GSL on node classification is solid. However, the theoretical claim is weaker than the paper's framing suggests, and the scope of the claim ("GSL is unnecessary") exceeds the evidence base.

**Soundness of experiments:** Good overall. The two-pronged design (GNN+GSL and SOTA-GSL) is thorough. The main weakness is the kNN-only synthetic experiments and the qualitative graph-quality analysis.

**Clarity of writing:** Clear. The framework, observations, and experiments are well-structured and easy to follow.

**Value to the research community:** Moderate. The paper's main value is as a sanity check and a call for more rigorous evaluation practices in GSL research. The framework may be adopted by practitioners to decompose GSL methods.

The paper presents a well-executed empirical study that raises legitimate questions about GSL's effectiveness, but the theoretical contribution is standard and the claims are somewhat overbroad relative to the evidence. The core experimental findings are useful for the community, even if they do not settle the debate for optimization-based GSL methods.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>