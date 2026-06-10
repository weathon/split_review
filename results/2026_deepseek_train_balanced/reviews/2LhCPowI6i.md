## Summary

This paper proposes a simple confidence-thresholding filter for generative replay in class-incremental continual learning: the classifier rejects generated pseudodata it cannot classify with sufficient confidence, preventing itself from retraining on low-quality samples. The method is tested on EMNIST (up to 16 tasks) with four model combinations (RealNVP/VAE × BNN/VCL) and three confidence thresholds. The central claim is that filtering produces a small positive accuracy improvement that scales with the number of tasks.

---

## Strengths

- **Model-agnostic, architecturally non-intrusive method.** The filtering operates purely on generated data rather than modifying the generator's loss or the classifier's architecture (Algorithm 2, lines 120–131). As the paper notes, this contrasts with the approach of Aljundi et al. (2019) and makes the method applicable to any existing generative replay system without redesign. This is a genuine advantage for a technique positioned as a "general" addition.

- **Systematic multi-configuration evaluation.** The method is tested across 4 model combinations (RealNVP+BNN, RealNVP+VCL, VAE+BNN, VAE+VCL), 3 confidence thresholds (90%, 95%, 99%), with 30 random seeds each (Section 3, line 138). This breadth strengthens confidence that the observed effects are not specific to a single architecture or hyperparameter setting.

- **Extended benchmark relative to standard practice.** The paper uses EMNIST Balanced (47 classes, up to 16 tasks) rather than the standard 5-task SplitMNIST (Section 2.2.1, lines 107–108). This provides a stronger testbed for the scalability analysis than is common in prior generative replay evaluations.

---

## Weaknesses

### Fatal
None.

### Major

- **Survivorship bias from terminated runs undermines the central scaling claim.** The paper explicitly reports (Section 3, line 138) that for higher thresholds and later tasks, "some generators entered infinite loops… In such circumstances, the training was terminated, so not all thirty resulting data points are available for higher task numbers." The no-filtering baseline has no equivalent termination mechanism. This means the comparison at higher task numbers systematically excludes the worst-performing filtering runs while retaining all baseline runs. The paper's main evidence — the positive Pearson correlation between improvement and task count (Table 1) — is therefore suspect: the correlation could be partially or entirely an artifact of increasingly selective survivorship in the filtering condition. The paper never discusses or controls for this bias. Given that the abstract and conclusion foreground scalability as the key finding, this gap is severe.

- **No forgetting metrics reported.** In continual learning, overall cumulative accuracy conflates new-task learning ability with old-task retention. The paper reports only cumulative accuracy after each task (Section 3, line 138). It provides no per-task accuracy trajectories, no backward transfer / forgetting measure, and no analysis of whether filtering differentially affects retention of early versus late tasks. Without this, it is unclear whether filtering genuinely improves retention or simply makes the model better at the most recent tasks. Since generative replay is fundamentally about combating forgetting, this omission is significant.

- **No empirical comparison against existing methods, including the most closely related one.** The paper acknowledges Aljundi et al. (2019) as "conceptually similar" (lines 24, 161) — that work also uses classifier confidence on generated samples, but via a loss-function term rather than hard filtering — and cites Van de Ven et al. (2020) and Kirichenko et al. (2021). The paper positions filtering as "a stricter variant" of the Aljundi approach but provides zero empirical comparison against it or any other method from the literature. The experiments compare only against "generative replay without filtering" (i.e., an ablated version of itself). For a top-venue publication, demonstrating that the method adds value beyond existing approaches — especially the one it explicitly contrasts with — is necessary.

- **The self-confirmation dynamic is acknowledged but not analyzed.** The paper's justification (Section 4, line 157) is that filtering "automatically reinforce[s] the presence of features important for distinguishing between classes." This is precisely what a self-confirmation loop does: the classifier selects training data consistent with its current decision boundaries, trains on that data, and reinforces those boundaries. The paper acknowledges that filtering reduces diversity and can harm generalization for small task counts (line 159), but it never analyzes whether the "improvement" for larger task counts reflects genuinely better representations or merely the classifier becoming increasingly overconfident on a narrower slice of the generated data distribution. Because the test set is real (not generated), this is not a fatal confound — the accuracy numbers are real — but it does mean the mechanism by which filtering helps is unclear and could be shallower than claimed.

### Minor

- **Single dataset.** All experiments use EMNIST. While this is an improvement over 5-task SplitMNIST, the claim that "this pattern can be expected to be relevant for even larger problems" (Section 4, line 159) is speculative given the evidence covers only one dataset with up to 16 tasks. A second dataset (e.g., CIFAR-100 class-incremental split) would significantly strengthen the generality claim.

- **The "n times" in Algorithm 2 (line 123) is unspecified.** The BNN is run multiple times per sample, but the number of stochastic forward passes is not stated. This is needed for reproducibility.

- **Correlation values not reported numerically.** Table 1 states Pearson correlations are "statistically significant with α=0.05" but the actual coefficient values are not visible in the extracted text. Raw values should be reported.

### Trivial
None.

---

## Nice-to-Haves

- **Qualitative analysis of filtered vs. rejected samples.** Showing examples of what the filter accepts and rejects (e.g., blurry vs. clear, boundary vs. prototypical) would help ground the mechanism.
- **Uncertainty calibration analysis.** The paper uses Bayesian neural networks with stochastic forward passes, yet never examines whether filtering changes prediction calibration or uncertainty quality.
- **Comparison against Van de Ven et al. (2020) and Kirichenko et al. (2021),** which the paper cites but does not benchmark against.

---

## Removed Points

These points were removed with justification:

1. **Missing training hyperparameters (optimizer, LR, epochs, batch size).** Removed per Hard Rule: nitpicks about reproducibility such as undisclosed hyperparameters should be removed. The code is also referenced as publicly available (line 35).
2. **"Ambiguous whether algorithm 1 or 2."** The paper clearly describes the pseudocode as algorithm 2 (pseudodata generation loop, lines 116–131). Strawman.
3. **"Ambiguous whether filtered data trains the generator or only the classifier."** Line 157 explicitly states "removed from the training set used both by the solver and the generator." Strawman.
4. **Strength about positive correlation with task count.** Dropped per the rule that strengths conflicting with a verified weakness should be removed — the survivorship bias concern directly undermines this claimed strength.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface any insight that the paper itself does not contain.

---

## Suggestions

1. **Address survivorship bias directly.** Re-analyze results by: (a) reporting the fraction of terminated runs per configuration, (b) recomputing correlations with worst-case imputation for terminated runs, or (c) redesigning the generation budget to avoid infinite loops before the experiment terminates.
2. **Add forgetting metrics.** Report per-task accuracy after each new task, or compute standard backward transfer / forgetting measures.
3. **Benchmark against Aljundi et al. (2019).** Since the paper frames the method as a "stricter variant" of that approach, an empirical comparison is essential.
4. **Add at least one additional dataset** (e.g., CIFAR-100) to support the generality claim.
5. **Specify the number of stochastic forward passes** ("n times" in Algorithm 2, line 123).

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>