## Summary

The paper introduces MIAU (Membership Inference Attack Unlearning Score), a unified evaluation metric for machine unlearning that combines three MIA comparisons—Forget vs. Test, Retain vs. Forget, and Retain vs. Test—normalized between a baseline model (trained on full data) and a retrained reference model (trained without the forget set). The gap closure fraction is passed through a logistic transformation to produce a bounded [0, 100] score, with equal weighting across the three MIA sub-scores. The metric is positioned as an offline auditing tool for selecting among unlearning methods before deployment.

---

## Strengths

- **Well-motivated decomposition.** The argument that any single MIA comparison is necessary but not sufficient—and that all three together disambiguate targeted forgetting from global degradation or generalization loss—is clearly articulated and technically correct.
- **Broad experimental scope.** The paper evaluates across four datasets (MNIST, CIFAR-10, CIFAR-20, MUCAC), three architectures (ResNet-18, All-CNN, ViT), and four unlearning methods, and includes both softmax-based and saliency-map-based MIA variants, providing substantial breadth.
- **Honest acknowledgment of metric limitations.** The paper explicitly shows cases where MIAU does not exhibit monotonic behavior in gradual forgetting experiments (Figure 3) and where p-values are non-significant (Figure 4), rather than cherry-picking favorable results.
- **Interpretable design.** The normalization between baseline and retrain endpoints gives the score a clear meaning: percentage of the privacy gap closed relative to ideal retraining.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unreliable scores due to extreme variance.** The MIAU standard deviations across seeds are often as large as or larger than the scores themselves. For example, on CIFAR-20 AllCNN: Amnesiac is 40.07 ± 23.37, Teacher is 38.36 ± 20.35, and SSD is 8.55 ± 13.46. For SSD, the 95% confidence interval straddles zero, making it statistically indistinguishable from the baseline (0.10 ± 0.00). When the metric's variance is comparable to the differences between methods, its utility for method selection is severely compromised. This is not merely a minor instability; it calls into question whether MIAU is reliable enough to fulfill its core purpose.

2. **Metric fails its own validation criterion in most settings.** The central validation property is that MIAU should increase monotonically under progressive retraining (MIAU₂₅ < MIAU₅₀ < MIAU₇₅ < MIAU_full). Yet the paper itself reports this does not hold consistently—MNIST-AllCNN and CIFAR10-ResNet violate the ordering—and Figure 4 shows that the paired t-tests are non-significant (p >> 0.05) for most dataset/comparison pairs. If the metric cannot reliably detect the difference between 25% and 75% retraining, it does not have the sensitivity required to rank unlearning methods.

3. **Near-chance MIA accuracies undermine the entire framework.** Table 1 (CIFAR-20 AllCNN) shows raw MIA accuracies of 50–56%, and Table 3 (MUCAC ResNet-18) shows all MIA values in the 49–55% range across partial retrain levels. With such small absolute differences (1–5% above chance), the gap normalization in Eq. (1) amplifies noise. The paper's own MIAU values on MUCAC jump from ~14–26 (with std ~15–20) for partial retraining to 99.90 for full retraining—this non-linear cliff is driven by MIA values hovering at chance, not by genuine signal. No analysis is provided to characterize when MIA signals are too weak for MIAU to be interpretable.

### Minor

1. **α calibration and weighting are underspecified in the main text.** The logistic scaling parameter α = 13.8 is derived in an appendix, and the centering at f_i = 0.5 (rather than f_i = 0) is a consequential design choice: a method closing exactly half the gap receives a score of 50, but a method doing worse than baseline can receive very low scores regardless of absolute performance. The implications of this design choice (e.g., whether equal weighting β = γ = δ = 1/3 is appropriate when the three MIA tasks have very different noise levels) receive little analysis.

2. **Offline audit still requires full retraining.** The paper frames MIAU as avoiding the overhead of retraining in deployment, but the offline audit itself requires training at least one retrained reference model. The paper does not quantify the computational overhead of the audit phase relative to the deployment savings.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An analysis of under what conditions MIA signals are strong enough for MIAU to be informative (e.g., as a function of forget set size or model memorization level) would substantially improve the paper's practical guidance.
- A comparison of MIAU against alternative composite scores (e.g., reweighted combinations or robust aggregations) that might reduce variance would strengthen the design choices.

---

## Novel Insights

The paper surfaces a genuine and under-appreciated empirical finding: MIA-based signals for unlearning evaluation are largely near-chance across a range of well-studied benchmarks, and this near-chance behavior makes any metric built on MIAs—including the proposed MIAU—inherently noisy. This negative result has value for the community independently of the proposed metric, as it suggests that MIA-based unlearning evaluation may require qualitatively different settings (high memorization, larger forget sets, or stronger attacks) to provide meaningful signal.

---

## Suggestions

- Conduct a power analysis or empirically characterize the minimum forget-set size and model memorization level at which MIAU achieves adequate inter-method separability.
- Consider a variance-reduction strategy (e.g., calibration via held-out splits, bootstrap confidence intervals for the final MIAU score, or adaptive weighting of the three MIA components based on their signal-to-noise ratio) to address the high standard deviation issue.
- Provide guidance for practitioners on when the method is likely to be unreliable (e.g., when raw MIA accuracy is within 2–3% of 50%), so users do not apply MIAU in regimes where it will give misleading comparisons.

---

## Score and Decision

The paper addresses a real and important problem, and the proposed solution is systematic and interpretable in principle. However, the core empirical validation reveals that MIAU frequently exhibits variance that renders method rankings statistically unreliable, and that the metric fails its primary validation criterion (monotonic sensitivity to partial retraining) in a substantial fraction of evaluated settings. These issues are not superficial; they directly undercut the claim that MIAU provides "a reliable and consistent measure of forgetting quality." The paper is not without merit—the decomposition rationale is sound, the evaluation is broad, and the honest reporting of negative findings is commendable—but in its current state the metric's practical utility is not sufficiently demonstrated.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>