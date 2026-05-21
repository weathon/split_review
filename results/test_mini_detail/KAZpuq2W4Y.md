Now I have a solid understanding of the paper and the calibration landscape. Let me write the final review.

---

## Summary

This paper proposes HOMIL (Higher-Order Multi-Instance Learning), which extends ABMIL for WSI classification by augmenting standard first-order (attention-weighted mean) aggregation with second-order moments (attention-weighted covariance) to capture inter-feature relationships across patches. It also uses DBSCAN-based adaptive clustering to group similar patches, reducing the effective instance count from ~thousands to ~hundreds and dramatically cutting computational cost. Experiments on CAMELYON16 and TCGA-NSCLC compare against nine baselines under 5-fold cross-validation.

## Strengths

1. **Genuinely novel conceptual contribution.** Integrating second-order statistical moments into MIL aggregation for WSI classification is a clean, well-motivated extension of ABMIL. The paper clearly articulates why first-order moments alone are insufficient for heterogeneous slides, and the covariance formulation (Section 4.3.3) follows naturally from this insight. Prior MIL work on WSIs overwhelmingly focuses on first-order pooling.

2. **Dramatic computational efficiency gains are well-supported.** HOMIL's total 5-fold runtime on CAMELYON16 is 310s—over **23× faster** than MambaMIL (7200s), **35× faster** than HMIL (10800s), and **17× faster** than TransMIL (5175s)—while still achieving the top accuracy, AUC, and F1 in the comparison. The ablation (Table 3) confirms the clustering module drives this efficiency: removing it increases runtime by 71% (310s → 530s). These efficiency improvements are large enough to be meaningful regardless of small fluctuations in accuracy.

3. **Clean, informative ablation study.** Table 3 isolates the contributions of each module: removing second-order moments (w/o SOM) drops ACC by 1.00% and F1 by 1.60%; removing clustering (w/o CM) drops ACC by 1.26% and increases runtime by 71%. The degraded performance of the ABMIL-only variant (94.72% ACC) vs the full model (96.98% ACC) cleanly demonstrates synergy between the two proposed components.

4. **Consistent trends across two datasets.** HOMIL achieves the highest ACC, AUC, and F1 on both CAMELYON16 and TCGA-NSCLC, versus nine baselines. The performance ordering is stable across datasets, which strengthens the case that the approach generalizes rather than being tuned to a single benchmark.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation uses 5-fold CV on the full CAMELYON16 dataset (399 slides), not the official train/test split (270 train / 129 test).** The paper describes the official split in Section 5.1 ("270 for training and 129 for testing") but then evaluates using "a unified 5-fold cross-validation setup" (Section 5.2). Training on ~319 slides per fold (4/5 of 399) is substantially easier than training on 270 slides. While the *internal* comparison (HOMIL vs baselines under the same 5-fold CV) remains valid, the resulting numbers cannot be compared to published results from the baselines' original papers, which were reported on the official test set. The abstract's claim of "significantly improves the state-of-the-art performance" is therefore misleading, as the evaluation protocol differs from the standard used to establish prior SOTA. The paper does not acknowledge this deviation.

2. **Reported improvements are within standard error margins; no statistical significance testing.** On CAMELYON16, HOMIL's ACC is 96.98 ± 2.43 and ABMIL's is 94.72 ± 2.18 (standard errors). The 2.26% gap is well within the ±3% noise range of these standard errors. The same pattern holds on TCGA-NSCLC (e.g., ACC: 93.24 ± 2.47 vs 91.05 ± 2.05). With only 5 folds, a paired test has minimal power, and the paper reports neither per-fold results nor any significance test (e.g., Wilcoxon signed-rank or confidence intervals on the difference). Without this, it is unclear whether the improvements are systematic or reflect fold-level noise.

3. **Baseline hyperparameter tuning is undocumented.** The paper gives explicit hyperparameters for HOMIL (lr 1e-4, weight decay 1e-5, dropout 0.4, 100 epochs) but states only that "All methods are implemented in a unified codebase" (Section 5.2). No information is provided about whether baseline hyperparameters (learning rate, weight decay, dropout, architecture choices, training epochs) were tuned per method or set to defaults. Given that performance differences between methods are small (1–2%), whether baselines received comparable tuning effort directly affects the fairness and informativeness of the comparison.

### Minor

4. **Covariance compression mechanism is under-motivated.** The paper compresses the d×d covariance matrix to a d-dimensional vector via row-wise 1D convolution followed by max-pooling over positions and kernels (Section 4.3.3). Convolution assumes local structure along feature dimensions, but the paper provides no justification for this assumption—feature dimensions of a learned embedding (CONCH, 512-dim) have no natural ordering. No ablation compares this approach to simpler alternatives such as flattening + linear projection, eigenvalue decomposition, or vectorizing the upper triangle. While not fatal (the compression is a practical means to an end), this design choice is a core part of the claimed contribution and should be better justified or ablated.

5. **No empirical evidence for the central clustering claim.** The paper motivates DBSCAN by stating it forms "large clusters for abundant normal tissues and small clusters for rare pathological regions" (Section 4.1, Section 4.2). This claim is central to the method's adaptive-granularity narrative, but no evidence is provided—no cluster-size distributions, no qualitative comparisons with tissue annotations, no visualization of clustering outcomes. Without this, the adaptive-clustering claim remains intuitive but unsubstantiated.

6. **No limitations or failure-case discussion.** The paper has no limitations section and does not discuss settings where the method might underperform (e.g., when DBSCAN produces very few clusters, or when the compression rate is too aggressive). A brief mention of sensitivity analysis is deferred to the appendix (stripped in submission), which is a placeholder with no actionable content to evaluate.

### Trivial

- PCA dimension d' = 32 for clustering is used without justification or sensitivity analysis visible in the main text (sensitivity analysis mentioned as "Appendix: Sensitivity Analysis").
- The covariance matrix in Section 3.2 and Section 4.3.3 is actually an unnormalized scatter matrix (no division by K or K−1); the term "covariance" is used loosely throughout.
- Per-fold results are not reported, making it impossible to assess variance across individual folds.

## Nice-to-Haves

- Reporting results on the official CAMELYON16 test split (129 slides) in addition to 5-fold CV would allow direct comparison with published SOTA and resolve the evaluation protocol concern.
- An ablation comparing the convolution-based covariance compression to a simple learned linear projection (flatten → MLP → d-dim) would clarify whether the convolution structure adds value or is incidental.
- A visualization of cluster-size distributions across slides (e.g., histogram of cluster sizes, overlaid with ground-truth tissue annotations for a few exemplar slides) would substantially strengthen the adaptive-clustering narrative.
- Reporting hyperparameters and tuning procedures for each baseline method (search space, number of trials, best configuration) would address fairness concerns.

## Removed Points

- **"Second-order moment compression is not principled"** → downgraded to Minor (weakness #4): the critic's framing that this is a structural flaw is too strong; the convolution is a valid learned projection, but the lack of justification and ablation makes it a minor concern.
- **"No discussion of prior work on covariance in MIL (e.g., DeepO2P, bilinear pooling)"** → REMOVED per rule against "missing related works" as I cannot verify these references exist or are on-topic.
- **"Sensitivity analysis is a placeholder"** → REMOVED: the paper explicitly states the analysis is in the appendix, which was stripped during parsing. Not a weakness of the paper as submitted.
- **"Time for baselines not broken down by training vs inference"** → REMOVED: the total time comparison already fairly shows the efficiency advantage, and this level of detail is not standard.
- **Strength Finder's generic strengths** → REMOVED: strengths like "the paper addressed an important problem" or "the writing is clear" are generic. Only concrete, evidence-backed strengths are retained.

## Novel Insights

The most interesting observation from the review synthesis is that the reviewer and strength finder are in genuine agreement about the paper's conceptual merit and the value of its efficiency gains—they diverge primarily on whether the evaluation is sufficient to support the claimed conclusions. This tension is a useful signal: the paper does something genuinely novel (second-order moments in MIL for WSIs) and produces a real practical benefit (order-of-magnitude speedup over transformer-based competitors), but the gap between what is demonstrated and what is claimed is too wide. The efficiency gains are large and unambiguous; the accuracy improvements are small and uncertain. The paper would benefit from reframing its contributions around the efficiency–accuracy tradeoff rather than claiming unequivocal SOTA.

## Suggestions

1. **Reframe the central claim.** Instead of claiming "significantly improves state-of-the-art performance," frame the contribution as: (a) a principled extension of ABMIL with second-order moments, and (b) a large computational efficiency gain through adaptive clustering, with competitive or better accuracy. This is honest and well-supported by the evidence.

2. **Report results on the official CAMELYON16 test split** as a separate column/table. If the 5-fold CV numbers hold up on the official split, the paper becomes much stronger; if they don't, understanding the gap would be informative.

3. **Add per-fold results** and some form of significance assessment—even a simple paired t-test or Wilcoxon signed-rank across 5 folds would help gauge whether improvements are systematic.

4. **Ablate the covariance compression** against a simpler learned linear projection (e.g., flatten C → MLP → d-dim vector). If the convolution structure adds no benefit, simplify and remove it.

5. **Add 2–3 qualitative cluster visualizations** showing that DBSCAN does indeed group normal tissue into large clusters and pathological regions into small ones. This would validate the central mechanism without requiring extensive annotation effort.

6. **Document baseline hyperparameter tuning**—even a brief statement like "all baselines use default parameters from the original papers, with learning rate 1e-4 and 100 epochs" would address the concern.

## Score and Decision

**Calibration report:**

*Round 1 (bracketing):*
- Weak band (<3.5): **Mamba-HMIL** (avg 3.25, scores 3,3,1,6) — similar MIL-for-WSI paper. Lacked novelty (combination of existing components), unclear motivation, poorly written. **HOMIL is substantially stronger** (clearer novelty, cleaner ablations, much better writing).
- Middle band (3.5–7.5): **Pseudo Bag** (avg 4.67), **VLSA** (avg 5.67), **PSMIL** (avg 6.67). Pseudo Bag had novelty concerns vs. prior work. VLSA accepted as Poster with marginal gains but comprehensive experiments. PSMIL accepted as Poster with strong theoretical contributions. **HOMIL is stronger than Pseudo Bag but weaker than VLSA and PSMIL.**
- Strong band (>7.5): Anchors retrieved (avg ~8.0) are on topics distant from MIL/WSI and are not useful direct comparators.

*Round 2 (narrowing 4.5–5.5):*
- **BoneMet** (avg 6.0, Accept Poster) — dataset contribution, marginal technical novelty. HOMIL has more technical novelty. **HOMIL is weaker due to evaluation gaps.**
- **Pseudo Bag** (avg 4.67) — already read in full. HOMIL has clearer novelty and better ablation.
- **Mamba-HMIL** (avg 3.25) — already read in full. HOMIL is clearly stronger.

*Final bracket: 4.5–5.5. The paper sits at the upper end of this bracket: the core idea is genuinely interesting, the efficiency gains are real and large, and the ablation study is clean. However, the evaluation protocol issue (5-fold CV on full CAMELYON16 vs. official test split), lack of significance testing, and undocumented baseline tuning prevent this from being a paper in the 5.5–6.5 range where accepted papers typically sit.*

**Overall assessment:** The paper addresses an important problem with a novel and well-motivated extension. The computational efficiency results are impressive and clearly supported. However, the evaluation methodology has a structural gap (non-standard evaluation protocol on CAMELYON16, undocumented baseline tuning, no significance testing) that makes the central claim of "state-of-the-art accuracy improvement" unverifiable. The paper can be strengthened substantially by addressing these issues in revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>