Now I have all the information needed. Let me compile the final review.

## Summary

This paper applies topological data analysis (TDA) — specifically persistent homology and Betti curve similarity — to analyze the internal representations of DNNs. The authors train four CNN architectures (Extended LeNet, AlexNet, VGG-16, ResNet-18) on 30 disjoint 10-class subsets of ImageNet, extract neuron activations at multiple epochs, reduce them via k-means++ to 1000 points, compute persistent homology of the resulting metric spaces, and compare models using the infinity-norm of their Betti curves. The paper reports patterns such as increasing functional similarity over training and differences in similarity across data subsets and architectures.

## Strengths

- **Betti curve similarity captures temporal evolution of internal structure.** The paper shows that the similarity between a ResNet-18 at epoch 0 and epoch 60 is low, while adjacent-epoch similarity increases over training (Figure 4). This directly demonstrates the measure's ability to quantify how the functional graph changes during learning, supporting the claim that TDA tools can analyze training dynamics.

- **The method reveals representation differences that accuracy alone does not capture.** For subset 27, accuracy varies across models (Figure 9), but Betti curve similarity shows that ResNet-18, VGG-16, and AlexNet share high similarity while Extended LeNet is markedly different (Figure 8). This provides a concrete example where the topological measure detects structure that performance metrics miss.

- **Systematic multi-model, multi-subset experimental design.** The study trains four distinct architectures on 30 disjoint subsets of ImageNet with 7 checkpoint epochs each. This provides a reasonably broad basis for the empirical results and helps distinguish architectural effects from dataset-specific artifacts.

- **Clear operationalization of the pipeline.** The paper describes the full pipeline — activation extraction, k-means++ reduction, correlation distance, Vietoris–Rips persistent homology, and Betti curve similarity — in sufficient detail to be reproducible, using established libraries (Giotto-tda, PyTorch).

## Weaknesses

### Fatal
None.

### Major

1. **No baselines or comparisons to existing similarity measures.** The paper claims Betti curve similarity is a "useful tool" for analyzing DNNs, but never compares it to any existing method such as CKA, CCA/SVCCA, or even simple activation-distance-based similarity. Without baselines, the reader cannot assess whether the topological approach provides unique value or merely recapitulates patterns that simpler methods would also reveal. For a paper whose central contribution is a new analysis tool, some evidence that the tool adds information beyond what existing methods provide is essential.

2. **No quantification of uncertainty or statistical testing.** The paper reports average Betti curve similarity across 30 subsets but provides no error bars, confidence intervals, or variance estimates on any figure. Claims like "similarity between the models seems to be increasing when compared at the same epoch" (line 159) and "statistically the models are creating distinct internal representations" (line 169) are presented without any formal test (correlation test, permutation test, etc.). Without measures of dispersion or statistical significance, the reader cannot judge whether the observed patterns are reliable or could arise by chance.

3. **Insufficient validation of the k-means++ reduction.** The paper acknowledges that silhouette scores show clusters are poorly separated (line 59), argues that the reduction captures global structure, and that local structure is less important. However, no experiment quantifies the approximation error introduced by reducing to 1000 points — for example, by comparing PH results from full and reduced activation sets for a smaller network. Given that the entire topological analysis operates on the reduced set, this gap raises concerns about whether the extracted topological features reflect genuine properties of the functional graph or artifacts of the clustering.

### Minor

4. **No sensitivity analysis.** The paper does not explore how results depend on key methodological choices: the number of clusters k in k-means++, the number of test images, the choice of Spearman vs. Pearson correlation, or the use of absolute correlation (which discards sign information). These are likely important for reproducibility and for understanding the robustness of the observed patterns.

5. **Architecture adaptation details omitted.** The paper states that models are "essentially the same as their original counterparts" (line 43) but does not explain how AlexNet and VGG-16 (designed for 224×224 input) were adapted to 64×64 images. Modifications to strides, kernel sizes, or layer counts could affect activations and thus the results. This omission hinders reproducibility.

6. **The distance function's limitations are discussed but their implications for topological interpretation are not explored.** The paper acknowledges that the distance \(d_\rho\) fails the positivity axiom of a metric (line 73) and that the absolute correlation discards sign information, but does not discuss how these choices might affect the Vietoris–Rips complex or the topological features extracted. A brief analysis of alternative distance formulations would strengthen the methodological justification.

7. **The subset 27 finding is presented without statistical backing.** The observation that Betti curve similarity reveals structure that accuracy does not (Section 3.2) is the paper's strongest illustrative result, but it rests on a single subset with no quantification of how robust or general this pattern is across the other 29 subsets.

### Trivial

8. **The term "functional graph" is used to denote a finite metric space of activations** — not a graph in the usual sense. While the paper defines it clearly, the terminology could cause confusion, especially given different uses of "functional graph" in neuroscience.

9. **The abstract says "the curve similarity" while the paper defines only the infinity-norm of Betti curves.** The language could be more precise to distinguish the specific measure used from the broader family of curve-similarity methods.

## Nice-to-Haves

- Validate the pipeline on a synthetic or controlled setting with known ground truth (e.g., random vs. trained networks, or identical architectures with shared initialization) to show the measure behaves as expected.
- Compare Betti curve similarity against at least one standard representational similarity measure (e.g., linear CKA) across all models and subsets to quantify the unique information provided by the topological approach.
- Add a limitations section acknowledging constraints: 10-class subsets, subsampled ImageNet, four architectures, potential stability issues with Betti curves from 1000-point sets.
- Perform sensitivity analysis on the main hyperparameters (k in k-means++, number of test images, correlation measure) to assess robustness.

## Removed Points

- **Missing related work on TDA for DNNs (Naitzat et al., Rieck et al., etc.):** Per meta-review policy, I cannot verify the existence or relevance of these specific citations, so this criticism is removed.
- **Criticism about a "lack of research question":** The paper is an exploratory empirical study and states its aims clearly (analyze global structure, provide a similarity framework). For its type, the framing is adequate; this critique reflects a mismatch of expectations rather than a genuine flaw.
- **Criticism that some observed patterns "could be trivial" (model becoming less similar to its untrained self):** The paper directly acknowledges these patterns are expected (line 159), which is standard practice for establishing sanity checks. Presenting expected results first builds credibility before showing more surprising findings.
- **Criticism about the "curve similarity" terminology in the abstract:** The paper defines the specific measure in the methods section. Abstract-level imprecision is standard and does not mislead.

## Novel Insights

The harsh reviewer's central critique — that the paper demonstrates a tool's output without establishing its value relative to simpler alternatives — is a useful structural observation. It highlights a common pitfall in TDA-for-ML papers: showing that topological descriptors produce varying outputs across conditions is not the same as showing they provide *useful* information. The paper's strongest counterexample is the subset 27 finding, where accuracy alone does not cluster models the way Betti curve similarity does, but this example is too thinly developed to carry the paper's validity argument on its own. To move beyond demonstration to contribution, the paper would need to systematically establish what the topological lens reveals that standard representational similarity analyses do not.

## Suggestions

1. Add at least one baseline comparison (e.g., linear CKA) across all model pairs and subsets. If Betti curve similarity correlates strongly with CKA, the paper should be reframed around what the topological perspective adds despite the correlation. If it diverges under specific conditions, those conditions are the paper's main finding.
2. Add error bars (standard deviation across subsets) to all figures and a simple statistical test (e.g., correlation with epoch number, permutation test comparing within-architecture vs. cross-architecture similarity).
3. Quantify the k-means++ approximation error by running the full pipeline on a smaller network without reduction, or by comparing PH results at multiple reduction sizes.
4. Specify how AlexNet and VGG-16 were adapted to 64×64 input to ensure reproducibility.
5. Provide a focused, statistically grounded analysis of the subset where Betti curve similarity detects structure that accuracy misses (e.g., subset 27) — this is the paper's most compelling result and deserves more than a brief observation.

## Score and Decision

This paper introduces a genuinely interesting application of TDA to DNN analysis, backed by a substantial experimental effort (4 architectures × 30 subsets × 7 epochs). The core ideas are sound and the exploratory findings are suggestive. However, the empirical validation is insufficient to support the paper's claims of usefulness: there are no baselines, no error bars, no statistical tests, and no sensitivity analysis. The reader cannot assess whether the reported patterns are meaningful, reliable, or unique to the topological approach. Major revisions — particularly adding baselines, quantifying uncertainty, and establishing the method's added value — would be needed before the contribution becomes convincing.

**Originality:** Good. Applying Betti curve similarity to compare DNN functional graphs is novel.

**Quality:** Weak. The experimental design is thorough, but the analysis is purely descriptive without validation.

**Clarity:** Adequate. The pipeline is described clearly, though key architectural details are missing.

**Significance:** Potentially moderate, but not established by the current evidence.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>