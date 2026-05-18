Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper studies the double descent phenomenon through the lens of learned feature space geometry. It introduces a k-NN-based metric \(P\) that measures whether noisy training points have clean neighbors of the same original class in the penultimate layer representation, and shows that \(P\) correlates with test accuracy for FCNN and CNN architectures trained on MNIST and CIFAR-10 under varying label noise levels. The paper further proposes that over-parameterized models "isolate" noisy samples among clean data of the same class, and presents a conceptual perfect/imperfect learner framework in the Conclusion. The main claimed contribution is a mechanistic explanation for double descent.

## Strengths

- **Novel feature-space analysis methodology**: The use of k-NN on penultimate-layer representations to probe how models treat noisy training points relative to clean ones is a genuinely new approach for studying double descent. It moves beyond standard test-error curves to reveal internal representational structure.
- **Empirical correlation of \(P\) with test accuracy for FCNN and CNN**: The paper demonstrates a clear alignment between the trajectory of \(P\) and test accuracy across model widths for FCNNs on MNIST (Fig. 1) and CNNs on CIFAR-10 (Fig. 2), establishing an interesting empirical pattern that warrants further investigation.
- **Systematic replication and honest reporting of counter-evidence**: The paper tests three architectures (FCNN, CNN, ResNet18), two datasets (MNIST, CIFAR-10), and three noise levels (0%, 10%, 20%). The ResNet18 results, which directly contradict the isolation hypothesis, are explicitly acknowledged rather than suppressed. This honesty is a strength, even though it undermines the central claim.
- **Interpretable metric grounded in training data**: The metric \(P\) is computed entirely on the training set, yet it covaries with held-out test accuracy. This cross-validation-set correlation is an intriguing observation worthy of further study.

## Weaknesses

### Fatal
None. The paper's empirical observations have value even if the mechanistic interpretation is overreaching.

### Major

**1. The ResNet18 results directly contradict the "isolation" mechanism as a general explanation for double descent.**

The paper's central claim is that over-parameterized models "isolate" noisy samples among clean counterparts of the same class, and that this isolation drives the second descent. Yet for ResNet18 (Fig. 5), the metric \(P\) — measured using clean labels — drops to zero precisely at the interpolation threshold and stays there. The paper's own complementary analysis shows that for over-parameterized ResNets, k-NN predicts the *corrupted* (noisy) labels rather than the clean ones (lines 171–173). This means the model groups noisy points by their random labels, not by their original class. Double descent still occurs for ResNet18 despite this opposite pattern, so "isolation" in the paper's sense cannot be the mechanism that causes double descent.

The paper's explanation — "superior feature extraction ability of ResNets" (line 171) — is ad hoc and does not reconcile the contradiction. If the mechanism is only present for some architectures (FCNN, simple CNN) but not for ResNet, then it does not constitute a general explanation for the phenomenon. The paper would need to explain why the putative mechanism applies only to weaker architectures, and why double descent still arises when the exact opposite pattern holds.

**2. The causal claim that "isolation" drives double descent is not supported.**

The paper uses language suggesting a causal mechanism: "this phenomenon results from broader architectures genuinely interpolating noisy samples among correct samples" (line 22), and "the double descent phenomenon is a consequence of deep learning models learning how to separate the noise from the information" (line 38). However, the evidence is entirely correlational. The metric \(P\) is shown to co-vary with test accuracy for FCNN and CNN, but no causal intervention is performed — the paper never manipulates the feature space or \(P\) independently to show that changes in "isolation" produce changes in double descent. The ResNet18 case is particularly damaging here: \(P\) drops to zero while double descent persists, demonstrating that the correlation between \(P\) and test accuracy does **not** hold for all architectures where double descent is observed.

**3. The claim that double descent is "strictly related to noisy data" is potentially unfalsifiable.**

The paper states that "the double descent phenomenon is strictly related to imperfect models learning from noisy data" (line 190). However, double descent is observed even at 0% explicit label noise for CNN on CIFAR-10 (Fig. 3a). The paper attributes this to "intrinsic label errors" in the dataset (line 144). While intrinsic label noise is a real phenomenon, this reasoning makes the claim unfalsifiable: if any instance of double descent can be retroactively attributed to "intrinsic noise," then there is no observation that could contradict the theory. Without an independent, operationalized way to measure noise, the claim that "double descent requires noise" cannot be tested.

### Minor

**1. The value of \(k\) in the k-NN analysis is not specified, and sensitivity to \(k\) is not examined.**

The paper defines the metric \(P\) using k-NN but never states what value of \(k\) is used or whether the results are robust to this choice. Since the behavior of \(P\) could be dominated by the nearest few points, this is a meaningful methodological gap.

**2. No baseline or comparison to chance for \(P\).**

The paper does not report what \(P\) would be for a trivial model (e.g., one that memorizes all labels) or for random features. Without such baselines, it is unclear whether the observed values of \(P\) indicate meaningful structure or simply reflect dataset statistics.

**3. The perfect/imperfect learner framework in the Conclusion is speculative and untested.**

The conceptual model in Fig. 6 (perfect learners without regularization vs. imperfect learners with suboptimal regularization) is introduced only in the Conclusion without any experimental validation. The paper itself acknowledges that "a comprehensive theoretical framework is yet to be developed" (line 196). While conceptual models can be useful, presenting this as a conclusion from the experiments overstates what the paper has actually demonstrated.

### Trivial
None.

## Nice-to-Haves

- A comparison of \(P\) to other generalization predictors (e.g., margin, sharpness, effective rank) would strengthen the claim that \(P\) is a "weak predictor of generalization."
- An analysis of test points whose nearest training neighbors include noisy points — verifying whether they are classified according to the clean neighbors rather than noisy ones — would connect the training-set metric to test-set behavior.
- Sensitivity analysis for optimization hyperparameters (learning rate schedule, batch size, training epochs) would clarify whether the observed patterns are robust.

## Removed Points

- The harsh critic's claim that "the explanation is circular — isolation is measured as P, and P correlates with test accuracy, so the 'explanation' is that test accuracy correlates with itself." This is removed because it is factually incorrect: \(P\) is measured on training data (whether noisy training points have clean neighbors of the same class), while test accuracy is measured on held-out data. They are distinct measurements on distinct data splits.
- The harsh critic's suggestion that the paper should "provide a more direct test of the isolation mechanism" by artificially manipulating the feature space — while a valid scientific goal — is an impractical ask for an academic paper and acknowledges the useful direction rather than a concrete flaw in the current submission.

## Novel Insights

The most instructive finding in this paper is the ResNet18 counter-example, which the authors treat as an exception but which actually reveals the paper's deepest insight: the correlation between \(P\) and test accuracy is architecture-dependent. CNNs, which lack skip connections, exhibit the "isolation" pattern (high \(P\) for over-parameterized models), while ResNets group noisy points by their corrupted labels. This architectural divergence suggests that the geometry of noisy data in feature space is shaped by optimization dynamics and architectural inductive biases — not by a universal "isolation" mechanism. The paper's honest reporting of this contradiction is more valuable than its proposed explanation, because it opens a concrete question: *what architectural properties cause the feature-space treatment of noisy data to differ, and how does this relate to generalization?*

## Suggestions

1. **Reframe the paper as a descriptive empirical study** of how feature-space geometry of noisy training points covaries with model width and architecture, rather than as a causal explanation of double descent. The observed correlation between \(P\) and test accuracy for FCNN/CNN is interesting in its own right and deserves careful characterization.
2. **Treat the ResNet18 results as a primary finding, not an exception.** Analyze what architectural differences (skip connections, depth, optimization dynamics) produce the divergent behavior, and what this reveals about when "isolation" does or does not occur.
3. **Specify and analyze the choice of \(k\)** in the k-NN metric, and provide baselines (chance level, random features) so readers can calibrate the values of \(P\).
4. **Remove or heavily qualify the perfect/imperfect learner framework** unless it can be empirically grounded with explicit regularization experiments that show double descent disappearing under "perfect" regularization.
5. **Replace causal language** ("this phenomenon results from," "is a consequence of") with correlational language that accurately reflects the evidence.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>