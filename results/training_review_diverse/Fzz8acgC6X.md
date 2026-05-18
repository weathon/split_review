Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper introduces Graph Distributional Analytics (GDA), a framework that combines Weisfeiler-Leman (WL) graph kernel embeddings with distributional distance analysis (class-mean cosine similarity, kurtosis-based distribution diagnostics, outlier detection) to analyze graph datasets and understand GNN behavior at both population and sample levels. The authors evaluate GDA on ENZYMES, MalNet-Tiny, and ogbg-ppa datasets, demonstrating how the framework can identify structural anomalies, distributional shifts between data splits, and structural motifs associated with misclassifications.

## Strengths

- **Novel and practical combination of techniques for graph-level dataset analysis.** GDA weaves together WL embeddings, sparsity-based dimension filtering, class-mean cosine similarity, normalized distribution scores, and kurtosis-based distribution diagnostics (Section 3.1–3.2, Algorithm 1) into a unified pipeline that reveals structural patterns across entire graph datasets. While each component is individually known, their integration for population- and sample-level graph analysis — as opposed to node/edge-level attribution — is a genuinely useful contribution that fills a gap left by instance-level explainers (Section 2).

- **Concrete, quantified improvements from GDA-guided interventions across multiple datasets.** The framework's utility is demonstrated through several case studies with explicit numbers: a 2.3% improvement on the transferase category and 0.4% overall on ENZYMES after identifying and separating a bimodal cluster (Section 4.2.1); a 4.3% average improvement on MalNet-Tiny after restructuring dataset splits to address GDA-identified distribution shifts (Section 4.2.1). These are real, measurable gains.

- **Identification of specific structural motifs causing cross-category misclassification.** In the ogbg-ppa dataset, GDA identified a structural motif present in 68% of Category 27 samples that appeared in 12% of misclassified Category 5 samples (Section 4.2.2, Figure 4), enabling targeted mitigation. This demonstrates the framework's ability to surface concrete, actionable structural insights at the sample level.

- **Rigorous experimental setup across multiple dimensions.** All experiments were repeated over 10 distinct seeds with two architectures (GraphSAGE and GIN) across three diverse datasets with varying properties (ENZYMES: small molecular graphs, MalNet-Tiny: large function-call graphs, ogbg-ppa: protein interaction graphs). Initial "baseline" experiments used prescribed dataset splits (Section 4.1).

- **Domain-grounded analysis.** The bimodal distribution in transferases is explicitly linked to known biochemical variability in enzyme families (Section 4.2.1), showing that GDA can surface patterns that align with real-world domain knowledge rather than statistical artifacts alone.

## Weaknesses

### Fatal
None.

### Major

- **Framing as an "explainability" method that "outperforms baseline methods" is overclaimed and unsupported.** The paper consistently positions GDA as an explainability framework (title, abstract, Section 1, Section 3) and claims to "outperform baseline methods in identifying specific structural features responsible for misclassifications" (abstract). However, the experiments compare GDA-guided data modifications against the *model's original performance* — not against any existing explanation method (GNNExplainer, PGExplainer, SubgraphX, etc.). No evaluation of explanation quality (fidelity, sparsity, ground-truth overlap) is performed. GDA is better characterized as a dataset-level diagnostic and debugging tool that can *inform* explainability analyses rather than being an explainability method itself. The authors should either (a) frame GDA as a graph dataset diagnostic tool and remove claims about outperforming explanation methods, or (b) add quantitative comparisons against at least one existing graph-level explanation method on standard metrics.

- **Experimental interventions lack controlled comparisons.** The experiments validate GDA by showing post-hoc accuracy improvements after data manipulations (clustering and retraining, removing outliers, restructuring splits). It is unclear whether these same manipulations done *randomly* (random split restructuring, random removal of an equal number of samples) would produce similar or better gains. Without such controls, the experiments primarily show that the authors can brainstorm fixes guided by GDA's outputs, not that GDA provides *better* guidance than simple baselines. The paper would be substantially stronger by adding even one control: e.g., showing that GDA-guided split restructuring outperforms random split restructuring on MalNet-Tiny.

- **The ogbg-ppa "significant reduction" claim is unquantified.** The paper states that isolating the identified motif and adjusting the training process led to "a significant reduction in misclassification rates" (Section 4.2.2), but provides no numbers, no comparison to an alternative adjustment strategy, and no description of what the adjustment entailed. This is the paper's primary sample-level analysis result and needs to be reported with the same level of specificity as the other case studies. Without numbers, the claim is not verifiable.

- **Post-hoc structural attribution (Section 3.3) is critically underspecified.** The mechanism for identifying specific substructures responsible for misclassification is described in a single paragraph: "rerunning the WL kernel with degree sequence tracking" and "examining how node labels evolve through each iteration." No algorithm, no pseudocode, no example output, and no evaluation on synthetic data with known ground-truth motifs are provided. The ogbg-ppa motif (Figure 4) is presented without any explanation of how it was algorithmically extracted from the embedding analysis. This component is essential to GDA's claim of being more than a statistical diagnostic tool, and in its current state it is not reproducible.

### Minor

- **No runtime measurements to support the scalability claim.** The paper claims O(n·m) complexity and states that GDA "can handle large-scale graph datasets efficiently" (Section 3.4), but provides no wall-clock timing experiments, no comparison to the runtime of existing methods (GNNExplainer, SubgraphX), and no experiments on very large graphs where scaling would be non-trivial. Given that WL kernel embeddings themselves have costs that depend on graph size and iteration count, this claim needs empirical backing.

- **Key parameters are set arbitrarily with no sensitivity analysis.** The sparsity threshold κ is set to 0.002 (Section 3.1), the outlier detection threshold α is mentioned as "typically set to 2 or 3" (Section 3.2.1), and the number of WL iterations h is never specified for any experiment. All three parameters can affect the analysis, and no ablation or sensitivity study is provided. At minimum, the value of h used in each experiment should be stated.

- **No statistical tests for the reported improvements.** The experiments use 10 runs, but no p-values, confidence intervals, or effect sizes are reported for the improvements (0.4%, 2.3%, 4.3%). It is possible that these gains are within the range of random seed variation, particularly the 0.4% overall improvement on ENZYMES.

### Trivial

- **"Hamel dimension" is misused.** The paper defines the "Hamel dimension, a, as the cardinality of the set of unique labels L" (Section 3.1). Hamel dimension is a linear-algebra concept about bases of vector spaces, not a synonym for "number of unique elements." The intended concept is simply the dimensionality of the embedding space.
- **Algorithm 1 pseudocode contains formatting issues** (e.g., the condition `if ∑... ≤ |H|×κ` is missing an `if` keyword; `|H|` and `|\dot{H}|` are used inconsistently).
- **The phrase "outperforms baseline methods" in the abstract** (as discussed above) is misleading since there is no comparison to any explanation method baselines.

## Nice-to-Haves

- A comparison against simpler alternatives (e.g., pairwise graph distances, raw WL histograms with PCA) would strengthen the claim that GDA's specific design choices matter.
- A synthetic experiment with known ground-truth motifs would validate the post-hoc structural attribution mechanism.
- Reporting which specific hidden channel sizes and layer counts were used for each architecture would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not demonstrate GDA as a method for GNN explainability in any meaningful sense"** (Harsh Critic Point 1, first sentence): Overstated. GDA does identify structural features responsible for misclassifications (e.g., the ogbg-ppa motif), which is a form of explainability at the population/sample level, even if it differs from instance-level attribution. The core criticism (lack of comparison to explanation baselines) is kept in the Major section with more precise framing.
- **"Novelty is overstated; the core pipeline is a straightforward application of standard techniques"** (Harsh Critic Point 3): The combination of these techniques for graph-level dataset analysis is genuinely novel in its application domain, even if each component is individually well-known. The novelty criticism is downgraded to a Minor weakness (lack of comparison against simpler alternatives) rather than presented as a structural flaw.
- **"κ = 0.002 is arbitrary and dataset-dependent"**: This is folded into the Minor weakness about missing sensitivity analysis.
- **"The number of WL iterations h is never specified"**: Folded into the Minor weakness about missing sensitivity analysis.
- **Strength 3 from Strength Finder ("Scalability and dataset-agnostic design")**: Conflicts with the verified weakness that scalability is claimed but not demonstrated with runtime data. Removed.
- **Strength 7 from Strength Finder ("Seamless integration with existing explainability methods")**: This is asserted but not demonstrated with any experimental evidence. Removed.
- **Formatting/style nitpicks** (e.g., "missing parentheses" in pseudocode, capitalization issues): Removed per instructions (parser artifacts / trivial presentation issues).

## Novel Insights

The most interesting observation to emerge from this review is the tension between the paper's framing and its actual contribution. The paper convincingly demonstrates that WL embedding + distributional analysis can surface meaningful structural patterns in graph datasets (bimodal enzyme classes, split distribution shifts, cross-category motifs) — but these are diagnostic insights about *datasets*, not explanations of *model predictions*. This distinction matters because the former can be validated directly by examining whether the identified patterns are real (e.g., do transferases actually have two structural subtypes?), while the latter requires evaluating whether the identified features actually drove the model's decisions. The paper's evidence supports the former claim strongly and the latter claim weakly, suggesting that GDA's main value is as a dataset introspection tool for practitioners — a role for which its scalability and dataset-agnostic design are genuine assets, even if the "explainability" framing needs recalibration.

## Suggestions

1. **Reframe the contribution.** Replace "explainability" language with "dataset diagnostics" or "structural distribution analysis" throughout. Remove the claim about "outperforming baseline methods" unless explanation-method baselines are added.
2. **Add at least one controlled comparison.** Compare GDA-guided split restructuring against random split restructuring on MalNet-Tiny to show that GDA's guidance provides non-trivial benefit.
3. **Provide the missing ogbg-ppa numbers.** Report exact pre- and post-intervention accuracy or misclassification rates for the motif-based adjustment.
4. **Specify the algorithmic details of the post-hoc structural attribution** (Section 3.3) and validate it on a synthetic dataset with known ground-truth motifs.
5. **Report runtime measurements** on datasets of varying size to substantiate the scalability claim.
6. **Add a sensitivity analysis** for κ, the outlier detection threshold α, and the WL iteration count h.
7. **Report the exact model architecture hyperparameters** (hidden dimensions, number of layers, etc.) used in experiments.
8. **Add statistical significance tests** (e.g., paired t-tests or confidence intervals) for the claimed improvements.

## Score and Decision

The paper introduces a genuinely useful tool for graph dataset analysis, supported by concrete case studies with measurable improvements. However, the framing is substantially overclaimed — the paper positions itself as an explainability method without comparison to any existing explanation baselines, the post-hoc attribution component is critically underspecified, and the experiments lack controlled comparisons that would rule out random-chance effects. These are major issues that the authors cannot fully resolve in a rebuttal without additional experiments and reframing. In its current form, the paper is not ready for acceptance but points in a promising direction.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>