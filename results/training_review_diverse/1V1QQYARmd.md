Now I have thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes an unsupervised OOD detection method that computes a k-NN density estimate on intermediate neural network embeddings and aggregates these scores across layers. The core insight — the "Label Smoothed Embedding Hypothesis" — is that training with label smoothing contracts same-class embeddings more than cross-class embeddings, making k-NN density a stronger OOD discriminator. The paper provides finite-sample theoretical guarantees (Theorem 1, 2) for k-NN radius as an OOD detection statistic, a theoretical model for label smoothing's benefit (Proposition 1), and empirical results on several benchmark datasets.

## Strengths

1. **Well-motivated, simple method.** The combination of k-NN density estimation on label-smoothed embeddings is clean and clearly motivated. The paper builds on a known property of label smoothing (Müller et al., 2019) and transforms it into a practical OOD score in a straightforward way.

2. **Consistent empirical benefit from label smoothing.** Table 1 shows that k-NN(α=0.1) achieves higher ROC-AUC than k-NN(α=0.0) on nearly every dataset pairing (e.g., MNIST→Fashion MNIST: 0.878 vs 0.785; CIFAR10→SVHN: 0.829 vs 0.804; Fashion MNIST→MNIST: 0.933 vs 0.913). The ablation in Table 2 corroborates this at the individual-layer level.

3. **Finite-sample theoretical guarantees for k-NN density in OOD detection.** Theorem 1 and Corollary 1 provide uniform recall and precision bounds: any point with f(x)=0 has r_k(x) ≥ r, and any point with r_k(x) ≥ r has f(x) ≤ λ, where r and λ decay at rates (k/n)^{1/(β+d)} and (k/n)^{β/(β+d)}. Theorem 2 shows ranking preservation under density gaps. While the techniques draw on Dasgupta & Kpotufe (2014), the application to OOD detection with these specific guarantees is new.

4. **Strong ablations on k, α, and layer choice.** Figure 2 shows stable performance across k (recommending k=1) and a consistent unimodal effect of α. Table 2 shows label smoothing benefits every layer individually. These provide concrete deployment guidance.

5. **k-NN density outperforms other embedding-based density methods.** SVM and Isolation Forest on the same embeddings with identical layer aggregation achieve lower performance (e.g., MNIST→Fashion MNIST: SVM 0.748, iForest 0.612 vs k-NN(0.1) 0.878), isolating the discriminative power of the k-NN radius statistic itself.

## Weaknesses

### Fatal
None.

### Major

1. **Missing key baselines limits empirical contribution.** The paper's central empirical claim is that the method is "competitive" and "outperforms many OOD baselines," but standard and widely-used methods are absent from the comparisons — specifically Mahalanobis distance (Lee et al., 2018) and energy-based OOD detection (Liu et al., 2020). These methods operate on the same regime (intermediate representations and logits, respectively) and are considered standard in the OOD detection literature. The paper includes DeConf (an improved ODIN), but ODIN is not the same as energy-based detection, and neither Mahalanobis distance nor energy-based methods appear. The comparison against POEM (which has an unfair advantage via outlier pool access) is valuable but does not substitute for these standard baselines. Without them, the claim that the method is "competitive" cannot be fully assessed against current best practices.

2. **Significant gap between theoretical conditions and practical regime.** Theorem 1 requires k ≥ 2⁸·log(2/δ)²·d·log n. For realistic embedding dimensions — e.g., d=256 (DNN penultimate layer) with n=60,000 — this condition requires k on the order of millions, far exceeding the training set size. The paper recommends k=1 for practical use, which is several orders of magnitude below the theoretical requirement. The paper never discusses this gap, does not report the embedding dimensions used in experiments, and provides no analysis of how the method's empirical success relates to the theory given that the theoretical conditions are unmet. This disconnect between the theory and practice is a significant omission that should be addressed.

### Minor

1. **Proposition 1 does not empirically connect to label smoothing.** The contraction mapping φ is constructed entirely from assumptions about how label smoothing behaves, but the paper provides no empirical evidence that label smoothing actually induces this specific geometric transformation (beyond the 2D histograms in Figure 1). The paper presents this as "theoretical intuition," which is fair, but the result would be considerably stronger with direct measurement of how label smoothing changes distance ratios across layers.

2. **Theoretical novelty relative to prior work is modest.** The paper acknowledges that its techniques "use similar techniques" to Chaudhuri & Dasgupta (2010) and Dasgupta & Kpotufe (2014). The contribution is in applying these to OOD detection and providing specific OOD-relevant bounds, which is useful but incremental. The ranking preservation result (Theorem 2) requiring a density gap ϵ_{k,n} is the most OOD-specific result, but its practical import is limited by the condition that the gap be sufficiently large.

3. **Standard errors reported only as summary statistics.** The paper reports "mean, median, and max" standard errors (0.0119, 0.00815, 0.0727) rather than showing per-entry standard errors in Table 1. Given the max is 0.0727 (a sizable fraction of many AUC differences), readers cannot assess which comparisons are statistically robust.

4. **Evaluation limited to relatively small-scale datasets.** The experiments use MNIST, Fashion MNIST, SVHN, CIFAR10, and CelebA. While these are standard benchmarks, the method's scalability to higher-resolution, larger-scale problems (e.g., ImageNet-scale) is untested. Given that k-NN methods incur storage and search costs on training embeddings, scalability implications are unclear.

### Trivial
- No dedicated limitations section, which would be helpful for flagging the dimensionality gap, computational cost at scale, and Euclidean-distance-based OOD assumption.

## Nice-to-Haves
- **Add Mahalanobis distance and energy-based OOD detection baselines.** These are the most natural competitors because they also use the trained model's representations without requiring additional data or outlier pools.
- **Provide direct empirical evidence for the contraction mechanism.** Compute the ratio of average OOD k-NN distance to average ID k-NN distance for models with and without label smoothing across layers. If this ratio increases, it directly validates the mechanism Proposition 1 attempts to model.
- **Discuss the dimensionality gap between theory and practice.** Report the embedding dimensions used, discuss whether the effective dimensionality is lower due to manifold structure, and contextualize the theoretical bounds accordingly.
- **Include a dedicated limitations section** covering: (a) sensitivity to the curse of dimensionality, (b) computational cost of storing all training embeddings and computing nearest neighbors at test time, (c) sensitivity to layer choice, and (d) the Euclidean-distance assumption (which may not hold for certain semantic shifts).

## Removed Points

- **α=0.1 not tuned / may understate performance** — The paper explicitly acknowledges this as a design choice ("we always use... α=0.1") and provides an ablation showing the effect of α. Using a fixed default without tuning is a feature (robustness), not a weakness. Removed per rule about weaknesses the paper already addresses.

- **Theoretical results presented without enough detail to verify correctness** — The critic noted this but said "for a conference review this would be fine assuming the appendix is present." Since the parser strips the appendix, this criticism cannot be evaluated and is removed per hard rules.

- **POEM included despite being outperformed** — The critic lists POEM as an inadequate baseline, but the paper's method outperforms POEM despite POEM having an unfair advantage (outlier pool access). This is a strength of the paper, not a weakness.

- **Missing related works** — Removed per hard rules about not having external sources to confirm existence of cited work not mentioned in the review.

- **Generic formatting/style nitpicks** — None present in the original reviewer input.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated claims and limitations without surfacing a cross-cutting observation that the paper itself misses.

## Suggestions

1. Add Mahalanobis distance (Lee et al., 2018) and energy-based (Liu et al., 2020) baselines to Table 1 to substantiate the claim of competitiveness.
2. Compute and report the ratio of OOD-to-ID k-NN distances with and without label smoothing across layers as direct evidence for the contraction hypothesis.
3. Report embedding dimensions for each architecture, discuss the effective vs. ambient dimensionality, and address why the theoretical condition k ≥ c·d·log n is not met in practice while the method still works.
4. Add per-entry standard errors (or confidence intervals) to Table 1 so readers can assess variability per dataset pairing.
5. Add a limitations paragraph covering the curse of dimensionality, computational cost of k-NN storage/search at scale, and the Euclidean distance assumption.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>