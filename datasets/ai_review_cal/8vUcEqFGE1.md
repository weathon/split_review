- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes SUMIT, a self-supervised method for learning a bag-level distance in Multiple Instance Learning. The approach trains an encoder-decoder on instance embeddings using five losses (reconstruction, contrastive, invariance, clustering, triangle) and then computes bag-to-bag distance via energy distance on the instance embeddings. The key finding from ablations is that contrastive and invariance losses — which enforce within-bag instance similarity and robustness to sampling depth — improve bag separability, while reconstruction and triangle losses do not.

## Strengths

1. **Systematic ablation identifying which losses drive bag separation**: The paper tests each of the five losses individually (Figures 3b, 3c, 3d) and consistently shows that only contrastive and invariance losses improve the within-to-between class density ratio. This directly supports the central finding that within-bag instance similarity is the key driver of a useful bag-level metric.

2. **Downstream classification validation**: KNN classification using the learned bag distance shows accuracy improvements over raw instance-based distances across all tested datasets (Figure 6). This provides practical evidence that SUMIT's learned metric transfers to a concrete task.

3. **Introduction of a new multi-class MIL dataset (Wiki)**: The paper creates a Wikipedia-based MIL dataset where bags are city pages and labels are countries, with Bag-of-Words section features as instances (Table 1). This goes beyond the standard binary MIL benchmarks and allows evaluation in a multi-class setting.

4. **Useful negative result for reconstruction**: The paper shows that an autoencoder trained with only reconstruction loss *degrades* bag separation (Figure 3c). This is a non-obvious finding that strengthens the argument that bag-level objectives are necessary, not just improved instance representations.

5. **Clear problem framing**: The paper identifies the gap between standard set distances (Hausdorff, Wasserstein) — which operate on raw features without learning — and supervised MIL methods, positioning SUMIT as a learned, self-supervised alternative (Section 1).

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to any existing bag distance method — the most significant evaluation gap**: The related work section (Section 2) surveys six existing approaches that produce bag-level distances: Hausdorff distance, kernel methods, graph kernels, MInd, Contrastive MIL, and multi-instance clustering. Yet the paper's experiments compare SUMIT only against raw instance features and a reconstruction-only autoencoder. The reader cannot tell whether SUMIT outperforms, matches, or underperforms even the simplest existing approach (e.g., Hausdorff distance on original features). Since the evaluation metric (KDE self-to-other density ratio) is novel, the paper must compute it for at least one or two baseline distances to calibrate interpretation. Without this calibration, a "40% improvement over raw instances" could be meaningless if Hausdorff already achieves 80%. This omission undermines the paper's central claim that SUMIT provides a *good* bag-level distance — the evidence only shows it is better than doing nothing.

2. **Triangle loss is conceptually confused and not doing what the paper claims**: Section 3 (line 75) states the loss aims to "maximize the gap between the undirect distance from one instance to another through a third instance and the direct distance." The loss formula (line 185) is `L_Triangular = p(d(x_i,x_j) > d(x_i,x_k) + d(x_k,x_j))`, which computes the *proportion of triples violating the triangle inequality*. In Euclidean space, the triangle inequality *always* holds, so this proportion is identically zero and the loss is vacuous. Section 5 (line 223) then describes it as "minimizing deviations" — contradicting the Section 3 description. The paper never resolves whether the loss is minimized or maximized, and the formula as written cannot produce meaningful gradients. The negative results for triangle loss are therefore uninterpretable: they could indicate the loss is harmful, or simply that it does nothing. While this does not invalidate the core finding (contrastive/invariance work), it reflects a significant conceptual error in the method description and calls into question the clarity of the overall loss design.

### Minor

1. **Bag-membership vs. label-separation gap not discussed**: The contrastive loss uses bag membership as supervisory signal — instances from the same bag are attracted, those from different bags repelled. But the evaluation measures separation by *label class*. The paper acknowledges this relationship only briefly (line 11: same-genre books should be closer), but never discusses the conditions under which bag-membership contrast is a reasonable proxy for label contrast. For example, two positive bags from different classes would still have their instances repelled from one another, which is desirable; but two positive bags from the *same* class also have their instances repelled, which is undesirable. The empirical results suggest this tension is manageable on these datasets, but the paper offers no analysis of when or why the proxy holds.

2. **Overclaimed novelty**: The paper states it is "the first time the embedding of each instance is optimized to produce an optimal distance between bags" (line 77) and "the first effort explicitly targeted at developing an instance-based distance between bags" (line 283). Yet the related work cites "Contrastive Multiple Instance Learning" (23), which trains instance-level (tile-wise) encoders with SimCLR and uses contrastive loss on bag-level representations derived from those instance embeddings — directly producing a bag-level metric. The differences (energy distance on non-pooled instances vs. attention-pooled bag representations) are genuine, but the blanket "first" claim is too strong and should be qualified.

3. **Missing details on the invariance loss aggregation function**: The invariance loss (line 171) uses `Agg(\tilde{X}_i)` but never defines the aggregation function (mean? sum? max?). This makes the loss not fully reproducible from the paper as written.

4. **No error bars or standard deviations for KNN classification results**: Figure 6 reports KNN accuracy improvements of up to ~15 percentage points but does not show standard deviations, confidence intervals, or train/test split details, despite 5-fold CV being mentioned for the main experiments. The reader cannot assess the variability or statistical significance of these results.

5. **Evaluation scope narrower than the motivation**: The introduction motivates bag-level distances for clustering, dimension reduction (MDS, UMAP, t-SNE), and statistical tests. The experiments evaluate only KDE density ratios and KNN classification. The claimed broader applications are not demonstrated.

### Trivial
- The `α` variable in the contrastive loss "where" clause is undefined.
- The paper says "maximize the gap" for triangle loss in Section 3 but "minimize deviations" in Section 5 — inconsistent wording that should be harmonized.
- Figure references appear before the figures in the running text (e.g., Fig. 2 cited on line 227 but appears at line 241), which is a layout issue.

## Nice-to-Haves
- An ablation comparing energy distance vs. alternative set distances (Wasserstein, sum-of-instance-distances, Hausdorff) on the learned embeddings would clarify whether the energy distance is a key design choice.
- An ablation comparing contrastive-only, invariance-only, and their combination would clarify whether one subsumes the other.
- A discussion of when bag-membership contrast is expected to be a good proxy for label contrast (e.g., datasets where within-label instance similarity exceeds cross-label instance similarity).

## Removed Points
These points from the input reviews are excluded with brief justification:

- **"Evaluation metric is novel so comparisons are meaningless"** (from Harsh Critic's Section-by-section): This is not a weakness of the paper; the paper introduces a metric and uses it consistently. The issue is lack of baselines, which is already captured as a Major weakness above.
- **"Paper doesn't demonstrate clustering/dimension reduction benefits"** (from Harsh Critic): Already captured as Minor weakness #5 (evaluation scope narrower than motivation).
- **"Reproducibility concerns about hyperparameters"**: The paper reports the architecture, optimizer (Adadelta), epochs (2000), and 5-fold CV. Minor details like temperature τ are reasonable to omit in a short paper. This is a formatting nitpick.
- **"Figures are low quality JPEGs"**: This is a PDF extraction artifact, not an author error.
- **"SSE in clustering loss is undefined"**: SSE is standard notation for Sum of Squared Errors in k-means; the surrounding text ("minimize the within-cluster variances, measured as squared Euclidean distances") makes this clear.
- **"Missing related works"**: Cannot be verified without external sources; removed per instructions.
- **"Strength: addressed an important problem"**: This is generic and superficial; removed per instructions.
- **"Strength: this paper targeted an interesting question"**: Same reason as above.
- **Various typos/grammar nitpicks**: These are PDF extraction artifacts, not author errors.

## Novel Insights
The two reviews together surface a tension that the paper itself does not address: the contrastive loss optimizes for bag-membership separation (instances from different bags pushed apart), but the evaluation measures label-class separation. This framing mismatch is common in self-supervised learning but is particularly acute in MIL because positive bags share a latent concept — instances from two different positive bags may be more similar to each other than to negative instances from their own bag. The paper's empirical finding that this mismatch does not prevent good label separation on standard MIL benchmarks is interesting, but without analysis of when the proxy holds, the method's generality is unclear. The second novel observation is that the paper's own diagnostic — KDE self-to-other density ratio — could serve as a lightweight evaluation protocol that any future bag-distance method could report, enabling head-to-head comparison even if the datasets differ.

## Suggestions
1. **Add at least two baseline comparisons** — compute the KDE density ratio and KNN accuracy for Hausdorff distance on original features and for the bag representations from Contrastive MIL (23). This single change would most dramatically increase the paper's evidentiary value.
2. **Fix the triangle loss**: either correct the loss to minimize violations of the triangle inequality (if that was the intent) with a proper formulation, or remove it entirely. The current formulation cannot produce meaningful gradients in Euclidean space.
3. **Report standard deviations or confidence intervals** for all quantitative results, especially KNN accuracy (Figure 6).
4. **Define the aggregation function** `Agg` in the invariance loss.
5. **Tone down the novelty claim** — the paper makes a meaningful contribution without needing "first" language that is difficult to verify and may be contradicted by [23].
