Now I have good calibration data. Let me consolidate everything into a final review.

## Summary

The paper identifies that existing robust learning methods for noisy labels or long-tailed data produce heterogeneous effects across sub-populations (some helped, some hurt). It proposes a Fairness Regularizer (FR) that constrains the per-sub-population performance gap, and shows that adding this regularizer to several baselines (CE, LS, NLS, Focal, PL, Logit-adj) improves overall test accuracy on synthetic and real-world long-tailed noisy datasets (CIFAR-10/100, CIFAR-10N/100N, Clothing1M). The central claim is that fairness constraints *improve* rather than degrade learning in this setting.

## Strengths

1. **Important, under-explored problem**: The paper correctly identifies that existing work largely treats label noise and long-tailed distributions in isolation, and that the *interaction* between the two produces per-sub-population disparities that prior methods do not address. This framing is timely and practically relevant.

2. **Novel use of fairness regularization in this context**: While fairness regularizers are standard in algorithmic fairness, applying them to improve *overall accuracy* (not just group fairness) under coupled noise and imbalance is novel. The paper explicitly acknowledges this departs from the usual fairness–accuracy trade-off (line 31), which is an honest and interesting claim.

3. **Broad experimental scope**: The paper tests 6 baseline methods × 2 noise models (imbalance, symmetric) × 2 noise rates × 3 imbalance ratios on CIFAR-10/100, plus real-world noisy datasets (CIFAR-10N, CIFAR-100N, CIFAR-20N, Animal-10N) with two imbalance levels each, plus Clothing1M with a λ sweep. This coverage is extensive.

4. **Per-class analysis supports the mechanism**: Figure 4 shows that FR specifically improves tail sub-populations — the blue "improved" points cluster in the lower-left (low baseline accuracy) region. This directly supports the paper's central narrative.

5. **Hyperparameter robustness on Clothing1M**: Table 3 shows that for most methods, a wide range of λ values (0.1 to 2.0) outperform λ=0.0, demonstrating that FR is not brittle to the choice of regularization strength.

6. **Simple, plug-and-play method**: FR can be added to any existing baseline with minimal code change, increasing practical impact.

## Weaknesses

### Major

1. **Inconsistent empirical gains across settings**: While FR(G2) improves in most settings, the gains vary substantially, and there are non-trivial cases where FR *hurts* performance. For example, on CIFAR-10 with symmetric noise (ρ=0.5, r=50), Logit-adj drops from 32.45 to 31.14 with FR(G2); on CIFAR-100 with imbalance noise (ρ=0.5, r=10), Logit-adj drops from 30.92 to 27.57 with FR(G2). The paper does not analyze what distinguishes these failure cases from successes. Without understanding *when* FR works and *why* it sometimes fails, the method remains an ad-hoc regularizer whose effects are unpredictable in individual settings.

2. **Statistical testing methodology is questionable**: The paired t-test in Table 2 aggregates 12 observations from *different* experimental conditions (2 noise types × 2 noise rates × 3 imbalance ratios) into a single test. These 12 points are not drawn from a single population — the data distribution, noise structure, and effective sample sizes differ across settings. While the paired nature (baseline vs baseline+FR under identical conditions) mitigates some concerns, pooling heterogeneous conditions into one test can produce statistically significant but practically meaningless results. The paper's conclusion that FR "consistently improves" based on this test is overstated, especially since FR(KNN) fails significance for most baselines on CIFAR-100 (1/6 significant), and Logit-adj+FR(G2) on CIFAR-10 has p=0.803. **The authors should report per-setting confidence intervals (e.g., over 3–5 seeds) for a representative subset of the main results instead of, or in addition to, the pooled test.**

3. **Weak theoretical grounding**: The paper claims a theoretical result (lines 193–197: "solving the risk minimization on the noisily labeled long-tailed data under the introduced fairness constraints returns the Bayes optimal classifier") but provides no proof, no reference to an appendix, and no experiment demonstrating this. For binary Gaussian data this may be straightforward, but relegating this to an unsubstantiated "observation" box without proof or demonstration weakens the paper's intellectual contribution.

### Minor

4. **The regularizer's behavior under label noise is undertreated**: The relaxation in Equation 5 replaces accuracy with average model probability on the *noisy* label ỹ. This means that when the noisy labels in a sub-population are systematically wrong, the regularizer could encourage the model to have high confidence on incorrect labels — the exact opposite of what is intended. The paper notes (line 324) that it avoids using noisy class labels as sub-population indices for FR(KNN), but the relaxation itself still depends on ỹ. This limitation should be explicitly discussed and ideally analyzed (e.g., what happens when noise rates differ across sub-populations?).

5. **The empirical motivation (Section 3) is illustrative but limited**: The influence analysis uses only CIFAR-10 with k-means clustering for sub-population discovery, 4 methods, and a handful of selected tail sub-populations. It convincingly shows *that* tail sub-populations have higher influence under noise, but does not establish that this influence is caused by the *coupling* of long-tail and noise (vs. noise alone), nor does it show that FR *reduces* this influence. The gap between the motivating observations and the proposed solution is not bridged by experiment.

### Trivial

6. The number of sub-populations in FR(G2) yields a head:tail ratio of "usually close to 5" (line 322), but no analysis of how sensitive results are to this split point.

## Nice-to-Haves

- Report error bars (standard deviation over 3+ random seeds) for a representative subset of Table 1's settings to substantiate the claimed improvements.
- Include specialized methods for combined long-tail + noisy labels (e.g., Wei et al., 2021; Karthik et al., 2021) as additional baselines to contextualize FR's relative contribution.
- Provide a per-class accuracy breakdown (like Figure 4) for settings where FR hurts, to show whether the loss is concentrated in certain classes.

## Removed Points

- **"The results in Table 1 are deeply mixed"** (harsh critic, point 1): The critic cherry-picks a few settings where FR underperforms while ignoring that FR(G2) improves in the large majority of settings (e.g., CE+FR(G2) wins 24/24 settings). This characterization overstates the inconsistency. However, the underlying concern about non-universal gains is valid and retained as Major weakness #1.
- **"The paired t-test is invalid"** (harsh critic, point 1): "Invalid" is too strong. The paired structure (same baseline and conditions) does provide meaningful signal; the test would be invalid if the pairs were independent samples from different populations, but each pair is matched. The real concern is that heterogeneous effect sizes across conditions could inflate significance — this is retained as Major weakness #2 but framed appropriately.
- **"The fairness regularizer introduces an auxiliary learning signal that depends on sub-population labels, but the paper never addresses the fundamental circularity"** (harsh critic, point 2): "Never addresses" is inaccurate. The paper explicitly states (line 324) that it does not use noisy class labels as sub-population indices. However, the concern about the relaxation's dependence on ỹ is valid and retained as Minor weakness #4.
- **"Comparison to state-of-the-art long-tail + noise methods"** (harsh critic, Missing Parts): Moved to Nice-to-Haves, as missing comparison methods do not constitute a weakness in a paper that already tests 6 baselines across 3 noise types.
- **"The paper does not show that FR reduces the influence of tail populations"** (harsh critic, point 3): This is a valid request for direct evidence connecting the motivation to the method, retained as Minor weakness #5.

## Novel Insights

None beyond the paper's own contributions. The core insight — that fairness constraints can improve overall accuracy under coupled label noise and long-tailed distributions — is the paper's primary novel claim. The reviews surface this clearly without adding fundamentally new interpretations.

## Suggestions

1. Replace the pooled t-test with per-setting confidence intervals from multiple seeds for a representative subset of Table 1 (e.g., CE and Logit-adj on both datasets at ρ=0.5, r=10 and r=100). This would provide more interpretable evidence than the aggregated test.
2. Add a simple synthetic experiment (e.g., the binary Gaussian case) that demonstrates *why* FR helps, proving or simulating the claim that the fairness-constrained solution recovers the Bayes classifier. This would substantially strengthen the paper's theoretical credibility.
3. Analyze the failure cases: include a brief discussion of what distinguishes settings where FR hurts from settings where it helps (e.g., does it correlate with baseline quality, noise rate, number of sub-populations?).
4. Acknowledge the limitation that Equation 5's relaxation depends on the noisy label, and briefly discuss how heterogeneous noise rates across sub-populations could affect the regularizer's behavior.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | How it compares to the paper under review |
|------|-----------|-------------------------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3GurO0kRue.md` (On Harmonizing Implicit Subpopulations) | 6.50 | Stronger theoretical foundation and more consistent empirical gains; current paper is less rigorous |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OeKp3AdiVO.md` (Rethinking Classifier Re-Training) | 6.25 | SOTA-level results on long-tail; current paper has more mixed results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/b66P1u0k15.md` (Pareto Deep Long-Tailed Recognition) | 6.00 | Stronger empirical consistency and theoretical framing |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6ARlSgun7J.md` (Enhancing Tail Performance) | 6.25 | Strong theoretical analysis and consistent gains; current paper weaker theoretically |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wfgZc3IMqo.md` (Robust Classification via Regression) | 6.00 | More established methodology with cleaner empirical story |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/u1yvEwYfK9.md` (Label Shift Correction) | 5.67 | Comparable tier — has clear method but weaker-than-SOTA results |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dW7FRwi1eA.md` (Meta Denoiser) | 4.25 | Weaker experimental design; current paper is stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LXnTFMvn8A.md` (Accuracy-Fairness Pareto Frontier) | 3.75 | Weak experimental validation; current paper has stronger empirical evidence |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RwiUmrEHgR.md` (Cost Sensitive Loss) | 3.00 | Weak baselines, no theoretical grounding; current paper is substantially stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PGT9OJX5N.md` (Noisy Data Pruning) | 3.00 | Limited novelty; current paper is more novel |

The paper identifies a genuine problem and proposes a novel, simple intervention. It is clearly stronger than papers scoring 3–4, which lack either empirical scope, novelty, or both. However, compared to papers scoring 6+, it falls short on: (a) the consistency of empirical gains, (b) the rigor of its statistical methodology, and (c) the depth of theoretical justification. The unsubstantiated theoretical claim and the lack of per-setting error bars are notable gaps. A 5.0 reflects a paper with a worthwhile core contribution whose evidence is not yet fully convincing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>