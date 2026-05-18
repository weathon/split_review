Now I have a thorough understanding of the paper and can verify the reviewer's claims directly. Let me produce the consolidated review.

---

## Summary

This paper proposes an unsupervised OOD detection method that computes a k-NN density estimate on a neural network's intermediate embeddings (normalized by the average in-distribution k-NN radius) and aggregates scores across layers. The core thesis is that training the backbone with label smoothing contracts in-distribution embeddings more than OOD ones, improving k-NN radius separability. The paper provides finite-sample theoretical guarantees for k-NN based OOD detection (Theorems 1–2, Corollary 1), an idealized result linking label smoothing to improved k-NN separation (Proposition 1), and empirical results on small-scale image benchmarks showing that the method outperforms several baselines, including POEM which has access to an outlier pool.

## Strengths

1. **Simple and well-motivated method with strong empirical signal.** The k-NN radius on intermediate embeddings is a natural, softmax-free OOD score. Table 1 shows the method achieves the highest ROC-AUC on 19 of 24 dataset pairings, outperforming POEM (which has an unfair advantage of training on an outlier pool), as well as SVM, Isolation Forest, and Robust k-NN applied on the same embeddings. The consistent improvement from label smoothing across datasets is compelling.

2. **Thorough ablation studies validate hyperparameter choices.** Section 4.4 systematically studies the effect of \(k\), label smoothing strength \(\alpha\), and layer selection. Figure 2 demonstrates stability across \(k\) and identifies a non-monotonic effect of \(\alpha\) with a clear optimal range. The paper recommends practical defaults (\(k=1,\ \alpha=0.1\)) backed by empirical evidence.

3. **Ablative baselines isolate the discriminative power of the k-NN distance.** By comparing against SVM and Isolation Forest applied to the same layer embeddings and aggregated identically, Table 1 shows that the k-NN radius consistently outperforms these alternatives, confirming it is a particularly effective density proxy for OOD detection.

4. **New finite-sample guarantees for k-NN in the OOD detection setting.** Theorems 1–2 and Corollary 1 provide high-probability bounds on recall, precision, and density-rank preservation for k-NN radius-based OOD detection. While the techniques follow Dasgupta & Kpotufe (2014), the application to OOD detection with these specific guarantees (uniform control of false positives, ranking preservation) is new.

## Weaknesses

### Fatal

None.

### Major

1. **Missing standard baselines weakens the empirical contribution.** The paper compares against softmax confidence, Robust k-NN, DeConf, SVM, Isolation Forest, and POEM, but omits widely used distance-based detectors such as the Mahalanobis distance detector (Lee et al. 2018) and the energy-based detector (Liu et al. 2020). These baselines operate on the same embeddings and directly test whether the k-NN radius adds value over simpler distance scores. Without these comparisons, it is difficult to assess the relative contribution of the proposed statistic versus established alternatives. This is the most significant gap in the evaluation.

2. **The theoretical connection to label smoothing is weak.** Proposition 1 models label smoothing's effect as a hand-designed contraction mapping \(\phi\) with strong assumptions (convex support, uniform lower-bounded density, a specific origin-based contraction, \(\gamma_{\text{in}}<\gamma_{\text{out}}\)) that are not validated against actual label-smoothed embeddings. The paper acknowledges this is a "theoretical intuition" (line 120), and the assumptions are clearly stated. However, the contribution list (§1) describes this as showing "why the Label Smoothed Embedding Hypothesis improves the k-NN based OOD score." The gap between the idealized mapping and real neural network behavior is large enough that the result does not convincingly explain the mechanism. An empirical validation (e.g., measuring actual contraction ratios in label-smoothed vs. non-smoothed models) would substantially strengthen the paper's narrative.

### Minor

3. **No practical guidance for threshold selection.** The evaluation uses ROC-AUC (threshold-agnostic), but real-world deployment requires a fixed threshold without OOD data. The paper gives no heuristic or procedure for setting the threshold — not even an analysis of the training-set distribution of \(\hat{T}\). This limits practical usability.

4. **The empirical evaluation is restricted to small-scale image benchmarks (MNIST, Fashion-MNIST, SVHN, CIFAR-10, CelebA).** While these are standard, the method's behavior on higher-dimensional feature spaces and larger training sets is unexplored. The paper does not discuss how k-NN radius separability scales with dimensionality or dataset size. Broader evaluation (e.g., Tiny ImageNet, CIFAR-100 as ID) would strengthen generality claims.

5. **The Label Smoothed Embedding Hypothesis is only tested qualitatively.** Figure 1 visually demonstrates that label smoothing contracts ID points more than OOD points, but no quantitative measure of clusterability (e.g., ratio of within-class to between-class k-NN radii) is reported. A simple numeric comparison would make the mechanism more concrete.

### Trivial

6. **The claim of "new" theoretical results is slightly overstated.** The paper acknowledges in §5 that its analysis "uses similar techniques" to Dasgupta & Kpotufe (2014). The results are indeed new in their application to OOD detection, but the framing in the abstract and contribution list could be more precise about what is novel versus adapted.

## Nice-to-Haves

- A quantitative test of the Label Smoothed Embedding Hypothesis: report the ratio of average within-class to between-class k-NN distance on the training embeddings with and without label smoothing.
- A comparison of the aggregate multi-layer score against the best single layer (Table 2 suggests the penultimate layer often performs well alone; showing whether aggregation helps beyond it would clarify the benefit of the multi-layer scheme).
- An analysis of why the mean (vs. median or quantile) was chosen for normalization, and whether it affects separability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *DeConf hyperparameter criticism* ("suggests either the implementation was suboptimal or the hyperparameter search was insufficient"): The paper explicitly states it searched the range from the original paper and found \(\epsilon=0\) optimal. This is standard and transparent reporting. Removed as speculative.
- *Robust k-NN tuning criticism* ("no tuning is reported for that baseline"): Using the original paper's hyperparameters (k=50, cosine similarity) is standard practice for baselines. Removed.
- *k=1 stability concern* ("most unstable nearest neighbor estimator"): The ablation in Figure 2 shows performance is stable across k, directly addressing this concern. Removed.
- *Hyperparameter selection criticism* ("effectively using test OOD data for hyperparameter selection"): The ablation studies on a subset of pairings establish defaults that are then applied across all datasets, which is standard practice with transparent reporting. Removed.
- *"Paper never tests the hypothesis directly"*: Figure 1 and its caption explicitly show the contraction effect, constituting a direct test. The test is qualitative rather than quantitative, which is noted in the Minor weaknesses. Removed as stated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a common tension between the paper's general k-NN theory (which does not depend on label smoothing) and the method's specific claim about label smoothing's benefit. This gap is partially acknowledged by the paper but is more significant than the paper's narrative suggests. The observation that k=1 works best (when k-NN is typically noisy at k=1) is interesting and deserves further investigation — the ablation shows it is empirically stable, which runs counter to the usual intuition about 1-NN variance.

## Suggestions

1. **Add Mahalanobis and energy-based detectors to the baseline comparison.** These are standard, embedding-based OOD methods that directly test whether k-NN radius adds discriminative power over simpler distance scores. Their inclusion would substantially strengthen the empirical evaluation.

2. **Provide a quantitative validation of the Label Smoothed Embedding Hypothesis.** Report the ratio of average k-NN radii for ID vs. OOD points (or within-class vs. between-class) with and without label smoothing. This would turn the qualitative observation in Figure 1 into a concrete, reproducible number.

3. **Either ground Proposition 1 empirically or reframe it.** Show that actual label-smoothed embeddings exhibit the kind of contraction modeled by \(\phi\) (e.g., measure the contraction ratio for ID vs. OOD points). Alternatively, replace the proposition with a simpler empirical analysis that directly measures how label smoothing changes the ID/OOD k-NN radius ratio.

4. **Add threshold-selection guidance.** Analyze the distribution of \(\hat{T}\) on the training set and propose a heuristic (e.g., a percentile of the training \(\hat{T}\) values) for setting the OOD threshold without access to validation OOD data.

5. **Consider evaluating on CIFAR-100 as ID** with standard OOD benchmarks (Tiny ImageNet, LSUN, SVHN) to demonstrate scalability beyond 10-class problems.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>