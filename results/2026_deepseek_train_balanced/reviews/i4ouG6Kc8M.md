## Summary

This paper proposes a dual-metric model selection procedure for self-supervised vision transformers in histopathology, combining task-specific benchmark metrics (e.g., aggregated Jaccard index, weighted F1) with task-agnostic rank-based metrics (RankMe, LiDAR, α-ReQ). The authors train nine small-scale dinov1 encoders on LUAD data, select checkpoints mid-training rather than at convergence using their algorithm, and evaluate on out-of-distribution benchmarks and held-out downstream tasks. The paper documents interesting behavior—downstream performance peaks mid-training while the SSL loss continues to decrease—and shows that carefully selected small models can approach the performance of much larger foundation models on certain segmentation benchmarks.

## Strengths

1. **Systematic empirical study of training dynamics in histopathology SSL**: The paper trains nine diverse models (ViT-S, ViT-B, soft MoE variants, single and multi-magnification) and documents that downstream task-specific metrics peak mid-training and degrade thereafter, even as the SSL training loss monotonically decreases (Table 2, Figure 1). This is a non-trivial finding that contrasts with the natural-image SSL paradigm and is concretely evidenced.

2. **Concrete, reproducible model selection algorithm**: Algorithm 1 provides an explicit procedure for combining task-specific and task-agnostic metrics to select a checkpoint, going beyond prior rank-estimation work (RankMe, LiDAR, α-ReQ) that was validated only on linear probing tasks (§2.2). The paper clearly shows that rank-based metrics alone are poor predictors of segmentation performance (Figure 3, §5.1), motivating the need for a combined approach.

3. **Differentiation of checkpoint types tested on held-out tasks**: The three checkpoint types (classification-best, segmentation-best, all-round) are evaluated on independent held-out tasks (LUAD subtyping, slide-level EGFR classification) that were not used in the selection procedure (§5.3). This provides a degree of external validation that the selection approach generalizes beyond the benchmarks used to make the selection.

4. **Ablation over model scale, architecture, and data diversity**: The nine models span 21.6M to 922.3M parameters with variations in ViT scale, soft MoE capacity, and single vs. multi-magnification training data (Table 1). This gives practical insight into how architecture and data diversity interact with the selection procedure.

## Weaknesses

### Fatal

None. The empirical observations are real and the paper documents genuine behavior. However, the weaknesses below substantially undermine the core contributions.

### Major

1. **The dual-metric combination is not ablated against simpler baselines, so its added value is unsubstantiated.** Algorithm 1 uses task-agnostic metrics only to determine a candidate set of epochs (Step 3–4), but the final selection is driven entirely by normalized task-specific metrics (Step 5: $r_k = \sum_j N^{ts}_{s_k,j}$). The paper never compares this procedure against any of several natural simpler baselines: (a) selecting the checkpoint with the highest average task-specific benchmark performance alone, (b) selecting the checkpoint with the highest task-agnostic metric alone, or (c) simply using the final checkpoint (comparison against (c) *is* present in Table 2 via gray highlights, but (a) and (b) are missing). Without these comparisons, it is impossible to determine whether the dual-metric machinery adds value or whether the same (or better) checkpoints would be selected by a trivial "pick the epoch with the best average benchmark score." Since the title and central claim of the paper are about the *dual-metric* approach, this is a significant evidential gap. The paper acknowledges that "representation ranks are poor indicators of segmentation performance" (Figure 3), which makes it especially important to demonstrate that they contribute positively to the selection rather than being a source of noise.

2. **The comparison between the paper's models and foundation models is asymmetric, undermining the headline claim.** The paper selects the *best checkpoint across all training epochs* for each of its nine models (via Algorithm 1) and compares these against Virchow2, Virchow, and UNI (line 102, Table 2). The foundation models are evaluated at a single checkpoint (presumably the final published one). The claim that "small-scale models match/exceed state-of-the-art models trained on much larger datasets" (abstract, §6) therefore compares a post-hoc optimal checkpoint against a fixed one. The paper does label the external models as "Reference" entries "excluded from the comparative highlighting" (Table 2 caption), which partially mitigates this, but the abstract and conclusions nevertheless make direct comparative statements. A fair comparison would require either (a) applying the same selection procedure to the foundation models' intermediate checkpoints (if accessible) or (b) comparing against the foundation models' best reported performance under standard evaluation protocols and clearly stating the asymmetry as a limitation of the comparison, not of the claim.

### Minor

3. **No variance or confidence intervals reported for any benchmark result.** Table 2 reports point estimates rounded to two decimal places. Given that benchmarks like BACH and CRC are relatively small datasets, variance matters. The absence of any measure of uncertainty makes it impossible to assess whether the observed differences between checkpoints or between models are meaningful.

4. **AUC estimation on the slide-level task uses a non-standard aggregation method.** The paper reports that it "estimate[s] the AUC from the set of predictions that are concatenated from all ten splits" (line 148). Concatenating predictions from different splits treats them as i.i.d. when they are not—each split has a different training/aggregation configuration. The standard practice for k-fold evaluation is to report the mean and variance of AUC across splits.

5. **Training data source and hyperparameter details are missing, harming reproducibility.** The paper states models are trained on LUAD data from "public datasets" (§1.3) but never specifies which dataset(s) (e.g., TCGA-LUAD, CPTAC, etc.). ViT patch size, learning rate schedule, batch size, augmentation strategy, and optimizer are not reported. For a paper evaluating 9 models across >230 epochs, these omissions are a barrier to reproduction.

6. **Claims about "histopathology" are broader than the evidence supports given the limited scope.** The paper restricts to a single SSL method (dinov1) and a single tissue type (LUAD) (§1.3). While this scope is honestly stated, the conclusions (§6) frame the findings as general properties of "self-supervised learning in histopathology" without sufficient caveats. The observed training dynamics could be specific to dinov1's inductive biases on a narrow data distribution.

7. **The held-out evaluation provides at best mixed support for the practical usefulness of distinguishing checkpoint types.** The paper's own results show that for the slide-level EGFR task, "AUC performance values do not substantially deviate between checkpoint types" (line 148), and for multi-FOV models on LUAD subtyping, "best-segmentation and best all-round model selection criteria can be comparable to or better than best-classification ones" (line 140). Only the ViT-S model shows a clear preference. These results are honestly reported but weaken the claim that distinguishing checkpoint types is reliably meaningful for downstream use.

### Trivial

None.

## Nice-to-Haves

- The paper documents that training longer is detrimental for histopathology SSL but does not analyze *why* this pattern emerges more strongly than in natural images. A targeted investigation (e.g., do representations collapse? Is it dataset narrowness? SSL method-specific?) would significantly strengthen the contribution beyond documenting the phenomenon.
- The algorithm's two-stage design (candidate generation via pairs, then re-ranking via task-specific metrics) could be replaced by a simpler convex combination of normalized metrics with a tuned weight, which would be more interpretable and directly ablatable.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Step 4 of Algorithm 1 contains a typographical error in the inner index range"* — Likely a parser artifact from PDF extraction; the original submission would not have garbled notation. Removed per hard rules about formatting artifacts.
- *"The §1.1 framing presents the selection method as efficient when it requires full benchmark evaluation"* — The paper explicitly acknowledges this as a limitation in §6 ("exploring the generalization of each checkpoint is expensive"). The criticism ignores that addressal.
- *"Algorithm 1 is unnecessarily complex"* — This is a subjective design opinion, not a factual weakness.
- *"The finding about training longer being detrimental is a restatement of known early stopping"* — The value is in demonstrating this specifically for histopathology SSL, which differs from the natural-image paradigm. Moved to Nice-to-Have.

## Novel Insights

The harsh critic's analysis correctly identifies that the dual-metric procedure effectively delegates all decision-making to task-specific metrics in the final step, reducing task-agnostic metrics to a weak pre-filter. This observation is sharper than anything in the paper itself and points to a concrete path for improvement: if the authors want to demonstrate genuine value from the task-agnostic metrics, they need to show that the candidate set produced by the dual-metric pairs yields better checkpoints than the candidate set produced by task-specific metrics alone, or show that the method helps when benchmark data is unavailable—not when it is fully available as in the current setup.

## Suggestions

1. **Add the critical ablations.** Compare Algorithm 1 against (a) selecting the checkpoint with maximum average task-specific benchmark performance only, and (b) selecting the checkpoint with maximum task-agnostic metric only. If the full algorithm does not outperform (a), the contribution is not the dual-metric combination but rather the fact that mid-training checkpoints are better—which is a different (and weaker) finding.

2. **Fix the foundation model comparison.** Either apply the same checkpoint selection to intermediate checkpoints of foundation models (if feasible) or clearly state in the abstract and conclusions that the comparison is an asymmetric "our best checkpoint vs. their final checkpoint" and discuss what this asymmetry means for the conclusions.

3. **Report variance/uncertainty.** Add standard deviations or confidence intervals for all benchmark results and use proper k-fold AUC reporting (mean ± std across folds) instead of concatenating predictions.

4. **Specify training details.** Provide the training data source(s), ViT patch size, optimizer, learning rate schedule, batch size, and augmentation strategy to enable reproducibility.

5. **Temper the generality of claims.** Qualify conclusions to reflect that findings may be specific to dinov1 training on LUAD data until tested with other SSL methods and tissue types.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>