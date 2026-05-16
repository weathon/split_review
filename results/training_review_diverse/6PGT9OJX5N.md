Now I have all the information needed to write a thorough, verified review.

## Summary

This paper tackles data pruning under label noise, proposing a two-stage method (RoP) that (1) selects clean samples using a novel Neighboring Label Inconsistency (NLI) Score refined by feature and label propagation, and (2) re-labels the selected subset via robust learning (e.g., SOP+). The key insight is to use geometric neighbor relationships to combat selection bias induced by noisy labels.

## Strengths

- **Novel propagation-corrected selection metric.** The NLI-Score uses both feature propagation (Eq. 5) and label propagation (Eq. 6) to rectify neighboring predictions before computing distribution divergence with the candidate label. Ablation Table 6 shows that using propagation improves accuracy from 84.3% to 86.1% at 20% pruning on CIFAR-10N Worst even without re-labeling, confirming the technique's value.

- **Consistent empirical gains across diverse noisy benchmarks.** RoP_B outperforms 10 baselines on real noisy datasets (CIFAR-10N, CIFAR-100N, WebVision) and synthetic ImageNet-N. On CIFAR-10N Worst at 20% pruning, RoP_B reaches 88.4% vs. the next-best Pr4ReL at 86.9% (Table 1). On WebVision (Figure 4), RoP's lead widens to ~3% at 80% retention.

- **Dramatically cleaner selected subsets.** Table 3 is the single most compelling piece of evidence: when selecting 10K images from CIFAR-10N, RoP's subset contains only 4.8% noisy labels vs. 17% for the best baseline (Small). This directly demonstrates that the NLI-Score mitigates selection bias.

- **Insightful empirical calibration between NLI-Score and re-labelability.** Figure 3 shows a clear monotonic relationship across 14 bins — lower NLI-Score samples are re-labeled with ~95% accuracy vs. ~60% for the highest bin. This validates the two-stage design.

- **Practical efficiency.** Figure 5 shows RoP's selection time (~0.2 hrs on ImageNet-N at 20% selection) is nearly identical to lightweight GraNd and orders of magnitude faster than KCenter (~4 hrs).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by evidence; the issues below are addressable.

### Minor

- **No variance estimates in main results.** All tables report averages of 3 runs without standard deviations. Many improvements over baselines are 0.3–1.5%, and without error bars the reader cannot assess whether these differences are statistically meaningful given run-to-run noise. This is the most significant weakness. (e.g., Section 4.2: "Every experiment is run 3 times, and the average of the last accuracy is reported.")

- **Shallow technical comparison with the most related method (Pr4ReL).** Pr4ReL (Park et al., 2024) is the closest prior work — also a two-stage selection+re-labeling pipeline — yet the paper does not provide a side-by-side analysis of selection quality (e.g., precision/recall of clean sample identification) for RoP vs. Pr4ReL, analogous to Table 3. The empirical margins over Pr4ReL are modest (e.g., ~0.5–1.5%), making it unclear whether the propagation mechanism is responsible for the gains or whether the benefit comes from the NLI-Score itself. A direct selection-quality breakdown would isolate the contribution.

- **Limited analysis of why propagation helps.** The paper applies feature propagation (Eq. 5: single step, no discussion of iterative alternatives or damping) and label propagation through the original noisy-label-trained FC layer (Eq. 6), but does not analyze the mechanism. For example: do propagated features shift noisy samples toward correct class centroids? Are single-step and iterative propagation similar in practice? The ablation (Table 6) shows it works empirically, which is necessary but not sufficient for a complete account — the paper's own motivation emphasizes geometry, so understanding how propagation changes predictions would strengthen the narrative.

- **Ablation discussion does not address complementarity.** Table 6 shows that propagation ("Rec.") alone gives large gains and re-labeling further improves, but the two are not additive in a straightforward way. The paper states both are "effective" and "crucial" but does not analyze whether they are redundant or complementary. This limits insight into when each component matters.

- **Several aspects of the evaluation protocol could be clearer.** (a) The caption of Table 1 says results are "by using PreAct ResNet-18 and re-labeling method (SOP+)," and the critic plausibly asks whether baselines receive this re-labeling. The text in Section 4.2 ("We evaluate the accuracy of the selected subset by using SOP+ as the Re-labeling model") makes it clear that this applies to all methods — but stating it explicitly in the caption would remove any doubt. (b) The warm-up analysis in Figure 3 uses a 20% random subset; the relationship between this subset and the final pruned subset (both the warm-up and the final subsets are subsets of the same training data, but the warm-up is randomly selected while pruning targets clean samples) is not explained.

- **"Laplacian" terminology is technically inaccurate.** Eq. (4) defines E = D^{-1/2} S D^{-1/2}, which is the symmetric normalized adjacency matrix, but the text (line 89) calls it "the Laplacian of the adjacency matrix." The Laplacian would be L = I - D^{-1/2} S D^{-1/2}. The math in Eq. (5), V_new = (I+E)V, is correct for the operation they intend (a GCN-style propagation step); the mislabeling does not affect results but indicates imprecise exposition.

### Trivial
- The paper uses "nerghborhood" (line 111) and "dose not" (line 266) in a few places. Minor proofreading issues.

## Nice-to-Haves
- A t-SNE visualization or histogram of NLI-Score distributions with and without propagation would concretely illustrate how the method changes the feature space.
- Reporting the precision/recall of clean-sample identification for RoP vs. Pr4ReL (analogous to Table 3) would directly address the most natural comparison.
- Standard deviations for all main tables would greatly increase confidence in the results and are an easy fix since 3 runs are already performed.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Incomplete algorithm pseudocode (Harsh Critic point 2c):** The critic cites lines containing "6: end for" and "7: Density-based coverage pruning" as evidence of incomplete pseudocode. These are parser artifacts — the \section command was accidentally applied to algorithm text during PDF extraction (line 158: `\section{6: end for}`). The original paper has proper pseudocode, and the paper subsequently describes the 5 steps in narrative form (lines 168–171). Removed as a parser artifact.
- **"Geometry-based motivation vs. label-based metric is tenuous":** The critic argues the paper motivates geometry-based resilience but then uses a label-based metric. This misunderstands the method: the NLI-Score uses geometric information (KNN in feature space + graph propagation on neighbor features) to compute the label inconsistency. RoP explicitly leverages geometric neighbor structure, consistent with its motivation. Removed as a misunderstanding.
- **Several points about missing appendix content / proofs / references:** The parser strips these; they exist in the original submission.

## Novel Insights
The reviews surface one genuinely useful observation beyond the paper's own contributions: the "Laplacian" terminology error (calling the normalized adjacency matrix a Laplacian) reveals a broader pattern — the paper's technical exposition is functional but could benefit from more precise mathematical language. This is a presentation issue, not a scientific one, but fixing it would improve clarity for readers who know graph signal processing. Also notable is the tension between the paper's strong selection-quality evidence (Table 3: 4.8% vs. 17% noise) and the modest downstream accuracy margins (0.3–1.5%): this suggests that even much cleaner subsets yield only incremental gains when the final model (SOP+) is already robust to label noise. The paper does not discuss this diminishing-returns dynamic, which is worth exploring in future work.

## Suggestions
1. **Report standard deviations** for all main tables (easy fix — 3 runs already performed).
2. **Add a direct selection-quality comparison (precision/recall) with Pr4ReL**, analogous to Table 3, to isolate the contribution of the NLI-Score metric from the re-labeling stage.
3. **Clarify the evaluation protocol** by explicitly stating in Table 1's caption that all baselines also receive SOP+ re-labeling on their selected subsets.
4. **Deepen the analysis of propagation** with at least one diagnostic (e.g., NLI-Score histograms before/after propagation, or a comparison of single-step vs. iterative propagation) to justify the design choice.
5. **Correct the "Laplacian" terminology** in Eq. (4): E = D^{-1/2} S D^{-1/2} is the symmetric normalized adjacency matrix, not the Laplacian.

## Score and Decision

**Originality:** 6/10 — The NLI-Score with propagation is a novel combination of existing ideas (KNN + graph propagation + label inconsistency), but each component is individually known. The two-stage pipeline for noisy-label pruning is also not entirely new (Pr4ReL preceded it), though the specific use of propagation to refine neighbor predictions is novel.

**Importance of research question:** 8/10 — Data pruning under label noise is a practically important and underexplored area. Real-world datasets inevitably have noisy labels.

**Claims well-supported:** 6/10 — The central claim (RoP selects cleaner subsets and trains better models) is supported by consistent evidence across multiple datasets. However, the lack of error bars and the shallow comparison with the most related method weaken the claim somewhat.

**Soundness of experiments:** 7/10 — The experimental design is reasonable: multiple datasets, real and synthetic noise, 10 baselines, abalation studies, and efficiency analysis. The main shortcomings are the missing variance estimates and the ambiguous protocol clarity.

**Clarity of writing:** 6/10 — The paper is readable but has several imprecise statements (Laplacian terminology, incomplete discussion of propagation mechanism) and some minor writing issues.

**Value to the research community:** 7/10 — The clean-subset selection results (Table 3) alone are valuable as a demonstration that geometry-aware metrics substantially reduce selection bias under label noise. The method is practical, efficient, and easy to implement.

The paper has genuine strengths: a well-motivated selection metric, strong clean-sample identification (Table 3), consistent empirical gains, useful ablation studies, and practical efficiency. The weaknesses are real but incremental — missing error bars, thin comparison with the closest competitor, and some analysis gaps — none of which undermine the core contribution. The paper would benefit from a revision to address these issues, but in its current form it already constitutes a solid contribution to the data pruning literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>