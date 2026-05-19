- Decision: Reject
- Avg Score: 2.86
- Scores: 1, 5, 3, 1, 6, 1, 3
Good. Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes using tools from topological data analysis—specifically persistent homology and Betti curves—to compare the global functional structure of deep neural networks. The authors train four CNN architectures (extended LeNet, AlexNet, VGG-16, ResNet-18) on 30 disjoint 10-class subsets of ImageNet, extract neuron activations, reduce them via k-means++, compute persistent homology, and define a Betti curve similarity (BCS) metric to compare models across architectures, datasets, and training epochs. The empirical results show that BCS varies meaningfully across model pairs and subsets, and that it can track changes in representations over training.

## Strengths

1. **Novel application of TDA to DNN comparison.** The paper introduces Betti curve similarity as a tool for comparing the global topological structure of DNN functional graphs—a genuinely different lens from standard representation similarity methods (Section 2.5, Eq. 5). The claim that this is the first use of BCS for DNN functional graph comparison (line 136) is specific and verifiable from the paper.

2. **Systematic empirical design with controlled replication.** Four distinct CNN models trained on 30 disjoint 10-class ImageNet subsets (fixed seed 1234), with activations extracted at seven epoch checkpoints (0, 10, 20, 30, 40, 50, 60) (Sections 2.1–2.2). This provides a robust basis for studying how BCS varies across architectures, datasets, and time.

3. **BCS reveals structure not captured by accuracy.** The paper demonstrates a concrete example (subset 27, Figures 8–9) where three models (ResNet-18, VGG-16, AlexNet) share high BCS despite having distinct accuracies, while all differ from extended LeNet—showing that BCS captures representational information orthogonal to task performance.

4. **Clear methodological pipeline with explicit formalization.** The functional graph is formalized as a finite metric space via Spearman correlation distance (Eq. 1), Betti curves are defined (Eq. 4), and BCS is specified as the infinity norm of their difference (Eq. 5). Computational feasibility is reported (66 minutes avg. per dataset excluding training, Section 2), and hardware/software details are provided.

## Weaknesses

### Fatal

None. The core idea is conceptually sound and the empirical results, while not definitive, are not fundamentally invalid.

### Major

1. **k-means++ reduction is not validated, despite acknowledged poor cluster quality.** The paper reports that silhouette scores show the clusters were "poorly separated" (line 59), meaning the centroids do not faithfully represent the distribution of activations. Yet the entire PH pipeline depends on reducing tens of thousands of activations to 1000 centroid representatives, and no control experiment is provided to check whether the persistent homology of the reduced set approximates that of the full set. Because PH is sensitive to point density and distribution, truncation to poorly-separated centroids could introduce artifacts that drive the observed Betti curve similarities. A stability analysis (e.g., comparing PH on random subsets, testing different k values, or validating against full activations for a small sample) is needed to establish that the measured topological signatures are not dominated by reduction artifacts. _This is the paper's most significant weakness — without it, the reliability of all quantitative results is uncertain._

2. **No statistical quantification of differences.** The paper uses language like "statistically significant sample size" (line 32) and claims that similarity is "low" for subset 11 and "high" for subset 27, yet provides no error bars, confidence intervals, or hypothesis tests for any Betti curve similarity value. Figures 4–8 show only point averages (across subsets or epochs) without any measure of variance. The key observations (e.g., that BCS distinguishes models, or that representations converge over training) are supported only by visual inspection of single bars. This is an evidential gap: the qualitative patterns may be real, but the current presentation does not establish whether the observed differences exceed what might arise from noise.

### Minor

3. **No comparison to established representation similarity methods.** The paper presents BCS as a tool for comparing DNNs, but the field already has several widely-used similarity measures (CKA, SVCCA, PWCCA, regression accuracy). The study does not evaluate whether BCS provides complementary, redundant, or weaker information relative to these baselines. Without such comparison, the value proposition of BCS over existing tools is unclear. (Note: This is a minor weakness because the paper is framed as an exploratory empirical study rather than a claim that BCS outperforms existing methods.)

4. **The distance function d_ρ is a pseudometric, not a metric (as acknowledged), but the practical implications for Vietoris–Rips homology are not discussed.** Distinct activations with zero distance (perfect correlation) would create simplices that should not exist in a strict metric space. While this is unlikely to be numerically impactful with real-valued activations, the paper does not address it.

### Trivial

5. **Minor exposition issues.** The description of the Vietoris–Rips complex uses an $\epsilon/2$ convention (line 121) which differs from the more common $\epsilon$ convention; this is a valid alternative but could confuse readers. The text contains a few parser-level artifacts (e.g., "filpping", "overftiting", "flitration").

## Nice-to-Haves

- A stability analysis of BCS with respect to the choice of k in k-means++ (e.g., k=500, 2000) would substantially strengthen the paper.
- A sanity check using randomized activations or noise would confirm that BCS captures model-specific structure rather than generic properties of the reduction.
- Normalizing BCS to a fixed range (e.g., [0,1]) would make values more interpretable across experiments.
- A discussion of scalability to larger architectures (e.g., ResNet-50, ViT) and full ImageNet would help contextualize the method's practical applicability.

## Removed Points

These points were flagged by reviewers but are removed from the main evaluation for the reasons stated:

- **"ILSVRC2017 is a typo"**: The reviewer asserts the dataset should be "ILSVRC2012." However, ILSVRC challenges ran through 2017; the citation (Russakovsky et al., 2015) covers the ImageNet project more broadly, and the exact year label does not affect reproducibility or the scientific content. Removed as an overly narrow nitpick.
- **"Extended LeNet's poor performance confounds analysis"**: The paper explicitly notes "As expected, the extended LeNet model performs the worst" (line 43) and uses it as a lower-capacity baseline. The performance gap is a feature of the design, not an unaddressed confound.
- **"Vietoris–Rips $\epsilon/2$ definition contradicts the usual definition"**: Both $\epsilon$ and $\epsilon/2$ conventions exist in the literature; this is not an error. The implementation (Giotto-tda) will use a consistent convention regardless of the exposition.
- **"Novelty claim is vague"**: The paper specifically states "As far as we are aware this is the first time that the Betti curve similarity has been used to compare the global structure of DNNs across datasets and epochs" (line 136) and "modify and add upon work by Corneanu et al." (line 12), with the additions being multi-subset, multi-epoch analysis and the BCS metric itself. The novelty is scoped and specific.
- **"Missing related works"**: Cannot be externally verified; removed per instructions.
- **Typographical nitpicks** (filpping, overftiting, flitration): These are parser-extraction artifacts, not author errors. Removed per hard rules.
- **"Scalability discussion is missing"**: The paper reports concrete runtime figures (66 minutes avg. per dataset) and hardware specifications. This provides sufficient feasibility context for the presented experiments. The request for broader scalability analysis is a nice-to-have, not a weakness.
- **"The pseudometric issue could create problems"**: The paper acknowledges the distance is not strictly positive (line 73). With real-valued activations and Spearman correlation, exact zero distances between distinct activations are practically impossible, making this a theoretical concern with negligible empirical impact.

## Novel Insights

The two reviews largely converge on the same key issues (unvalidated reduction, lack of statistical rigor) and the same strengths (systematic design, interesting qualitative patterns). The most useful insight from synthesizing the reviews is recognizing that the **k-means++ validation gap is the paper's decisive vulnerability** — not because the reduction is necessarily wrong, but because the paper itself reports that the clusters are poorly separated, yet proceeds without any stability check. This is an unusual situation where the authors' own diagnostic (poor silhouette scores) actively undermines confidence in the downstream results, and a simple control experiment (e.g., random subset vs. centroid subset, varying k) could either validate or refute the approach. The lack of error bars is a secondary but compounding issue: even if the PH computation were faithful, we wouldn't know if the observed BCS differences are meaningful.

## Suggestions

1. **Validate the reduction step.** Compare the persistent homology / Betti curves of the k-means++ reduced set against those of a random subsample of activations of the same size, or against the full set for a small network. Report stability across different values of k (e.g., 500, 1000, 2000). This is the single most impactful improvement you can make.

2. **Add statistical measures.** Include error bars (e.g., bootstrapped 95% confidence intervals across subsets or k seeds) on all BCS plots. For key comparisons (subset 11 vs. subset 27), consider a permutation test against the null distribution across subsets.

3. **Compare against CKA on at least one experiment.** Running CKA on the same activation sets for one model pair (e.g., ResNet-18 vs. VGG-16) across subsets would show whether BCS provides genuinely new information or correlates highly with existing measures.

4. **Clarify what is claimed as novel.** Make explicit in the introduction that the contributions are: (a) applying BCS to DNN functional graphs for the first time, (b) the comparison across multiple disjoint datasets, and (c) the epoch-wise tracking of representational change. This is already implicit but could be stated more crisply.
