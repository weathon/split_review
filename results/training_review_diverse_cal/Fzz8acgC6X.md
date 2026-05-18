Now I have all the information needed to produce a thorough, verified review. Let me compile it.

---

## Summary

This paper introduces Graph Distributional Analytics (GDA), a framework that uses Weisfeiler-Leman (WL) kernel embeddings combined with distributional distance metrics (cosine similarity, kurtosis) to characterize structural heterogeneity within graph classification datasets. GDA is positioned as a tool for understanding GNN model behavior by detecting bimodal classes, outliers, distribution shifts between train/test splits, and motifs correlated with misclassifications. Case studies on ENZYMES, MalNet-Tiny, and ogbg-ppa are presented to illustrate these capabilities.

## Strengths

- **Novel application of WL kernels for distributional diagnosis.** The paper provides a concrete pipeline (Section 3.1, Algorithm 1) that embeds graphs via the WL kernel, filters sparse dimensions with a principled threshold (κ = max(1, 0.002×|H|)), computes class-mean embeddings, and derives cosine-similarity-based scores. This specific combination is a reasonable approach to quantifying structural variation within graph classification datasets and goes beyond simple graph-kernel-based similarity.

- **Kurtosis-based detection of structurally heterogeneous classes is sound and well-motivated.** The paper defines kurtosis of cosine similarity scores (Section 3.2.2) and uses it to identify the bimodal transferase category in ENZYMES (Section 4.2.1, Figure 1). This provides a principled statistical method to flag classes where the "functional label ≠ structural form" problem exists, which is a genuinely useful diagnostic capability.

- **Scalability analysis is provided.** The paper states O(n·m) complexity for embedding and distribution analysis (Section 3.4), where n is graph count and m is average node count. This supports the claim of scalability to large datasets, which is a genuine advantage over perturbation-based explainers that must enumerate subgraphs.

- **Case studies demonstrate plausible utility.** The ogbg-ppa finding (a motif present in 12% of misclassified Category 5 graphs vs. 68% of Category 27 graphs, Figure 4) is a concrete example of GDA revealing a structural pattern that plausibly drives systematic misclassification. The MalNet-Tiny split-restructuring experiment (4.3% average improvement over baseline across 10 runs) is the paper's strongest quantitative result.

## Weaknesses

### Fatal

None. While the paper has significant issues, none individually invalidate the core contribution (that WL-based distributional analysis can be a useful diagnostic tool for GNN datasets). The most serious problems are in the framing and validation, which are major rather than fatal.

### Major

- **Unsupported claim of "outperforming baseline methods."** The abstract states that GDA "outperforms baseline methods in identifying specific structural features responsible for misclassifications." However, the experiments contain **no comparison to any baseline explainability method** (GNNExplainer, PGExplainer, SubgraphX, etc.). The word "baseline" in Section 4.1 refers to the same model without GDA-informed interventions (i.e., "baseline experiments" using prescribed splits), not to other methods. The paper never defines what "baseline methods" means in this context, let alone provides a comparison. This claim in the abstract is unsubstantiated and must be removed or properly supported.

- **Post-hoc structural attribution (Section 3.3) is underspecified to the point of being non-evaluable.** The mechanism is described in a single vague paragraph: "By rerunning the WL kernel with degree sequence tracking, we can identify specific substructures responsible for classification errors. The process involves examining how node labels evolve through each iteration, enabling us to pinpoint graph substructures that deviate from the class norm." No algorithm, pseudocode, formal definition, or example is provided. In the ogbg-ppa case study (Section 4.2.2), the paper reports that "a structural motif" was identified as present in 12% vs. 68% of two categories, but never explains **how** this motif was discovered — was it automated subgraph mining guided by GDA's scores, or manual inspection of individual graphs? Since structural attribution is presented as a central capability, this opacity makes a major component of the framework non-verifiable. A method-agnostic baseline comparison would at least establish the credibility of the claim.

- **Framing as "explainability" is misleading given what GDA actually does.** Existing GNN explainability methods (GNNExplainer, PGExplainer, SubgraphX) answer "which input features caused this *specific* prediction for this *specific* graph." GDA answers "which structural properties of the *dataset* tend to co-occur with misclassifications." These are fundamentally different tasks. The paper would be significantly stronger if it positioned GDA as a **diagnostic / exploratory data analysis tool** complementary to instance-level explainers, rather than as a competing explainability method. The related work section (Section 2) sets up GDA as addressing the same gaps as gradient/perturbation methods, but GDA provides none of the same functionality, creating a misleading comparison that the paper itself does not resolve.

### Minor

- **The normalized distribution score z(G) is defined (Section 3.1, Algorithm 1) but never used in any experiment.** The experiments rely on cosine similarity directly for outlier detection (Section 3.2.1) and kurtosis for class-level analysis (Section 3.2.2). The z(G) score does not appear in any result, figure, or analysis. Its presence creates confusion about which metric drives the framework's decisions. Either use z(G) or remove it.

- **"Hamel dimension" is used incorrectly.** The paper defines "Hamel dimension, a, as the cardinality of the set of unique labels L." Hamel dimension is a specific concept from linear algebra (the dimension of a vector space over a field in terms of a Hamel basis) and is not standard terminology for counting unique labels in graph embeddings. This will confuse readers and adds unnecessary jargon.

- **Empirical results lack error bars / confidence intervals in the main text.** The paper reports specific improvement percentages (2.3% for transferases, 0.4% overall, 4.3% after split restructuring) and notes that experiments were run with 10 seeds and "both GraphSAGE and GIN architectures." However, no standard deviations, confidence intervals, or per-seed ranges are reported in the main text. While the appendices (which are stripped by the parser) may contain these, the main text should provide at least a summary of variance. Without it, the reader cannot assess whether the reported improvements are stable or driven by a single seed.

### Trivial

- The phrase "Figure ??" appears on line 201 (parser artifact from figure cross-reference); the paper should ensure clean rendering.

## Nice-to-Haves

- A controlled version of the split-restructuring experiment (e.g., random restructured splits that didn't come from GDA's guidance) would help rule out the possibility that any data reorganization yields small improvements due to regularization effects.
- The κ threshold discussion in Section 3.1 could benefit from reporting the actual dimensionality reduction achieved (e.g., "from X dimensions to Y dimensions for dataset Z") to substantiate the claim that reduction is "significant."
- Direct comparison to at least one existing explainability method on a specific task (e.g., "does GDA's identified motif agree with GNNExplainer's important substructures?") would strengthen the positioning relative to prior work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that κ removes "approximately ≤1 graph"** — The reviewer's math is incorrect. The threshold is |H|×κ = max(1, 0.002×|H|). For |H|=5000, this gives 10, not 1. The paper's claim that this reduces dimensionality is defensible for the stated threshold. (Removed: factually wrong.)

- **Criticism about "Figure ??" appearing before Figure 1** — This is a parser artifact from PDF extraction, not an error in the original submission. (Removed: formatting artifact per hard rules.)

- **Criticism that "sample-level analysis is limited by lack of domain knowledge" undermines GDA's value** — The paper explicitly acknowledges this limitation ("the simplicity [of benchmark datasets] precludes in-depth study of individual samples") rather than hiding it. This self-awareness is a strength, not an additional weakness. (Removed: criticism ignores paper's own acknowledgment.)

- **Strength about "post-hoc structural attribution via WL label tracking" from the Strength Finder** — This claimed strength cites Section 3.3's mechanism as "interpretable, sample-level explanation," but the mechanism is vague and underspecified (see Major weakness above). This strength conflicts with a verified weakness, so the weakness prevails. (Moved to Removed Points.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel insight that the paper itself does not already contain or imply.

## Suggestions

1. **Remove or substantiate the "outperforms baseline methods" claim.** Either add a direct comparison to at least one existing explainability method (e.g., does GDA detect the same motifs as GNNExplainer? does it find them more efficiently?), or replace the claim with a more accurate statement about GDA's utility as a diagnostic tool.

2. **Operationalize Section 3.3.** Provide a concrete algorithm describing how WL labels / degree sequences are mined for structural attribution. Specify whether the motif discovery in ogbg-ppa was automated or manual; if automated, give the procedure; if manual, acknowledge this limitation and frame it as a human-in-the-loop capability.

3. **Reposition the paper's framing.** Move away from "explainability" (which implies instance-level feature attribution) toward "distributional diagnosis" or "structural data analysis for GNN interpretability." This better matches what GDA actually does and avoids misleading comparisons in the related work section.

4. **Add variance estimates to the main-text results.** Report means ± std across the 10 seeds for all claimed improvements (the 2.3%, 0.4%, and 4.3% numbers). If space is tight, a small table would suffice.

5. **Either use z(G) in experiments or remove the definition.** If z(G) serves a conceptual purpose (normalizing cosine similarity across classes with different variances), explain why it is useful even if not directly reported. Otherwise, dropping it simplifies the exposition.

## Score and Decision

This paper has a reasonable core idea — using WL-kernel-based distributional analysis as a diagnostic tool for GNN datasets — and presents several case studies that illustrate its potential. The kurtosis-based detection of bimodal enzyme classes and the ogbg-ppa motif finding are genuinely informative demonstrations. However, the paper's impact is substantially undermined by (a) an unsupported claim of outperforming baseline methods with no comparison provided, (b) a vague and non-operationalized structural attribution mechanism that is presented as a central capability, and (c) a framing that overstates GDA's role as an "explainability" method when it is fundamentally a dataset-level diagnostic tool. These issues are addressable with revision, but in their current form they significantly diminish confidence in the paper's claims.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>