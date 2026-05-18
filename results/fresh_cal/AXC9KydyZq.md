Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper tackles mixture graph matching and clustering (MGMC), where graphs from different categories must be simultaneously matched and clustered. The authors propose M3C, a learning-free solver based on a Minorize-Maximization (MM) framework with a relaxed cluster indicator that avoids the premature convergence of hard clustering, and UM3C, an unsupervised extension incorporating edge-wise affinity learning and pseudo-label selection. Experiments on Willow ObjectClass and Pascal VOC show that M3C outperforms prior learning-free methods and UM3C achieves competitive or superior results relative to supervised approaches on some datasets, while being faster than the main unsupervised baseline GANN.

## Strengths

1. **First convergent MM framework for MGMC with a principled relaxed indicator.** Section 4.1 formulates the MGMC problem within an MM framework with proven monotonic increase (Eq. 3), and Section 4.2 introduces a relaxed cluster indicator (global/local/fuse-rank schemes) that demonstrably improves over hard clustering. The benefit is empirically validated: M3C consistently outperforms M3C-hard across all settings in Table 1 (e.g., MA 0.687 vs 0.620 with 2 outliers).

2. **Strong empirical results on the Willow ObjectClass benchmark.** In Table 1, UM3C achieves MA=0.955 (0 outliers), exceeding both the unsupervised GANN (0.896) and supervised BBGM (0.939) and NGMv2 (0.885). UM3C also maintains high clustering metrics (CP=0.988, RI=0.988). These gains hold with outliers: UM3C's MA (0.858 with 2 outliers, 0.815 with 4 outliers) substantially exceeds GANN (0.610, 0.461) and remains competitive with supervised methods.

3. **Decoupled affinity loss enables solver-agnostic learning.** Section 5.1 introduces a cross-entropy loss between learned and ground-truth/pseudo affinity matrices (Eq. 8), which is independent of the subsequent matching solver. This decoupling is a clean design choice that avoids the conflation of affinity construction and solver-specific optimization present in prior work like BBGM.

4. **Component-wise ablation quantifies each contribution.** Figure 4 (left) decomposes the contribution of the baseline M3C substitution, edge-wise affinity, Spline CNN, and label selection, showing measurable gains from each component. The pseudo-label selection ablation (Figure 4, right) demonstrates a ~5% improvement in pseudo-label matching accuracy during early training.

5. **Transferability to supervised pipelines.** Table 2 shows that combining a pretrained BBGM with UM3C fine-tuning on Pascal VOC improves clustering accuracy from 0.7973 to 0.8761 (3×8) and from 0.7261 to 0.7861 (5×10), demonstrating the framework's ability to boost supervised backbones on the clustering objective.

## Weaknesses

### Fatal

None.

### Major

1. **Overclaim of superiority over supervised methods without qualification.** The contribution list (item 3) states UM3C "even outperforms supervised models such as BBGM and NGM, establishing itself as the top-performing method for MGMC on the utilized public benchmarks." This claim is accurate on Willow ObjectClass (Table 1: UM3C MA=0.955 vs BBGM=0.939) but does **not** hold on Pascal VOC (Table 2: UM3C MA=0.498 vs BBGM=0.792 on 3×8). The mismatch is attributable to Willow's small, clean setup (3 classes × 8 images, specific categories Car/Duck/Motorbike) versus Pascal VOC's harder distribution. The paper should explicitly bound this claim to the Willow setting or provide a nuanced statement acknowledging the Pascal VOC matching accuracy gap. As written, the claim is broader than the evidence supports.

2. **Convergence guarantee vs. practical implementation gap.** The paper repeatedly claims that M3C "guarantees convergence" (abstract, intro, contributions). The MM framework (Section 4.1, Eq. 3) guarantees monotonic increase *provided the maximization step exactly maximizes the surrogate function*. However, the practical implementation (Section 4.3) uses off-the-shelf graph matching solvers (e.g., RRWM, MGM-Floyd) which are approximate heuristics with no guarantee of increasing the surrogate. The paper does not acknowledge this gap, nor does it show that the deployed algorithm empirically satisfies monotonic increase (the convergence study is deferred to the appendix, see line 331). This does **not** invalidate the contribution — many optimization papers use this pattern — but the text presents the guarantee as a property of the deployed algorithm rather than of the theoretical framework, which is misleading. The authors should explicitly state the condition under which convergence is guaranteed and show empirical convergence plots in the main paper.

### Minor

3. **Pseudo-label regeneration schedule unspecified.** The paper (Section 5.2) describes generating pseudo labels using the M3C solver and selecting pairs via the relaxed indicator, but does not state how often pseudo labels are updated during training (every epoch? every N iterations? This is essential for reproducibility.

4. **Class imbalance in affinity loss not addressed.** The cross-entropy loss in Eq. 8 treats each of the \((n_1n_2)^2\) entries as a binary classification task. However, \(K^{gt} = \text{vec}(X^{gt})\text{vec}(X^{gt})^\top\) is rank-1 with extremely few 1-entries, creating severe class imbalance. The paper does not mention any weighting, thresholding, or sampling strategy to handle this. Without such handling, the loss may be dominated by negative entries.

5. **No variance or confidence intervals reported.** The paper reports means over 50 tests (line 258) but no standard deviations, error bars, or confidence intervals. Given the stochastic nature of some components (e.g., spectral clustering initialization, random sampling of graphs), this makes it difficult to assess the statistical significance of reported improvements.

6. **Pseudo-label accuracy evaluation may conflate with M3C's own output.** Section 5.2 uses the relaxed indicator to select graph pairs with higher affinity for pseudo-label training. The ablation (Figure 4, right) reports "matching accuracy of pseudo labels." It is unclear whether this accuracy is measured against ground-truth correspondences or against M3C's own matching output. If the latter, the metric measures self-consistency rather than genuine improvement, risking confirmation bias. The paper should clarify the evaluation protocol for this metric.

7. **Time comparisons within learning-free vs learning-based categories are fair, but the paper does not report training times.** The hardware split (laptop CPU for learning-free, workstation GPU for learning-based, line 249) means cross-category time comparisons are not meaningful. The paper only does within-category comparisons (UM3C vs BBGM/NGMv2/GANN — all GPU; M3C vs DPMC/MGM-Floyd — all CPU), which are fair. However, training time for learning-based methods (UM3C, GANN, BBGM) is not reported, leaving an incomplete picture of computational cost.

### Trivial

8. The normalization term \(1/\sum c_{ij}\) in Eq. 2 scales the objective by the total number of in-cluster pairs. The paper does not discuss how variable cluster sizes affect this normalization; a brief analysis would be helpful.

9. Hyperparameter sensitivity (\(r\) for relaxed indicator ratio, \(\alpha\) for affinity fusion weight) is deferred to the appendix. At least a brief discussion of robustness in the main text would strengthen the paper.

## Nice-to-Haves

- **Clarify convergence empirically in the main paper.** Showing a convergence plot (objective value vs iteration) would bridge the theory-practice gap and make the convergence claim fully credible.
- **Test on more diverse settings** (more clusters, more graphs per cluster) in the main paper rather than only in the appendix.
- **Add an analysis of cross-cluster contamination risk** in the relaxed indicator's matching composition space (Section 4.3), where paths may go through graphs from different underlying clusters.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Time comparisons across different hardware are meaningless."** The critic claimed UM3C vs BBGM time comparisons conflate hardware. However, both UM3C and BBGM are learning-based methods run on the same GPU workstation (line 249). The within-category comparisons are valid. Cross-category comparisons (learning-free vs learning-based) are not emphasized in the text. **Removed: factually incorrect.**

- **"DPMC convergence instability not empirically demonstrated."** The paper's claim about DPMC (line 28) cites prior work (WangAAAI20). The paper is not required to re-demonstrate properties of prior methods. **Removed: not a weakness of this paper.**

- **"Proposition 1 is essentially trivial."** The proposition that hard clustering converges in one step with fixed cluster sizes is a genuine property of the framework that motivates the relaxation. While straightforward given the setup, it is correctly presented as an observation about hard clustering's limitations. **Removed: subjective nitpick.**

- **Various speculative concerns** about cross-cluster contamination in matching compositions, about the relaxed indicator's transitivity, and about the lack of broader datasets — these either speculate beyond what the paper claims or ask the paper to solve problems outside its stated scope. **Removed.**

## Novel Insights

The two reviews, taken together, surface an interesting tension in the paper's framing: the theoretical novelty (first convergent MGMC algorithm via MM) and the empirical strength (UM3C beating supervised methods on Willow) are both real, but each comes with a caveat that the paper under-acknowledges. The convergence guarantee is formally correct for the MM procedure but relies on an exact maximization that the practical algorithm does not implement; the supervised-beating claim is correct on one benchmark but contradicts the Pascal VOC matching results. This pattern suggests the paper would be stronger if it leaned into a more nuanced narrative — presenting the MM framework as a *principled alternating optimization* (not a strict guarantee in practice) and the empirical results as "competitive with supervised methods on clean benchmarks" rather than as a sweeping superiority claim. The relaxed indicator and decoupled affinity loss are the most robust contributions because they are design innovations whose value is empirically demonstrated independent of whether the convergence guarantee is exact.

## Suggestions

1. **Qualify the convergence claim.** Add a sentence in Section 4.1 acknowledging that the theoretical guarantee holds when the maximization step is solved exactly, and that in practice approximate solvers are used. Show an empirical convergence plot (objective vs iteration) in the main paper or at least reference the appendix study.

2. **Bound the supervised-comparison claim.** In the contributions and abstract, replace "even outperforms supervised models" with "achieves competitive or superior results on Willow ObjectClass while using no supervision, and shows strong clustering improvements on Pascal VOC when combined with pretrained backbones." This is more accurate and still impressive.

3. **Report the pseudo-label update schedule** (how often labels are regenerated during training).

4. **Address the class imbalance in affinity loss** — describe any weighting scheme or note that the loss is dominated by negatives and explain why it still works.

5. **Add standard deviations or error bars** to the main tables, especially for the 50-test runs.

6. **Clarify the pseudo-label accuracy metric** in the ablation (Figure 4, right) — is it measured against ground truth or against M3C's own matching output?

## Score and Decision

**Overall assessment**: This is a solid contribution to the MGMC problem. The MM-based framework with relaxed clustering is a principled advance over prior heuristic approaches (DPMC, GANN). The unsupervised learning pipeline with decoupled affinity loss is well-designed. The empirical results on Willow ObjectClass are strong, and the transfer learning experiment on Pascal VOC shows the framework's utility beyond its standalone performance. The main weaknesses — overclaiming the convergence guarantee's practical strength and overgeneralizing the supervised comparison result — are presentation issues that can be fixed with careful rewriting. The missing experimental details (pseudo-label schedule, loss handling, variance) are standard concerns that should be addressed in a revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>