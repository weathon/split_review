Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me write the consolidated review.

## Summary

This paper extends influence functions beyond utility to measure how training samples affect a classifier's fairness (demographic parity) and adversarial robustness. It proposes: (1) a tree-based influence estimation model (Algorithm 1) to interpret which feature ranges contribute positively or negatively to performance, and (2) a data trimming strategy (Algorithm 2) that removes negative-influence samples given a budget. Experiments span synthetic data, four real-world datasets (Adult, Bank, CelebA, Jigsaw), and seven application scenarios including distribution shifts, poisoning/evasion attacks, online learning with noisy labels, and active learning.

## Strengths

- **Unified influence-based data selection for utility, fairness, and robustness.** The paper formalizes influence functions for demographic parity and adversarial robustness — extensions not previously explored in a unified framework. Figure 2 shows that influence-based trimming significantly improves fairness DP (e.g., Adult from ~0.35 to ~0.05) and robustness accuracy (e.g., CelebA from ~0.55 to ~0.85) across four real-world datasets, while random trimming consistently fails.

- **Broad experimental scope across diverse challenging scenarios.** The paper evaluates its method in distribution shifts (Section 5.1, with 5 baseline fairness interventions), fairness poisoning attacks (Section 5.2), adaptive evasion attacks (Section 5.3), online learning with noisy labels (Section 5.4), and active learning (Section 5.5, with 5 baselines including the influence-based ISAL). This breadth demonstrates practical relevance beyond conventional classification.

- **Active learning result is well-controlled.** In Section 5.5, the influence-based sampling outperforms random, entropy, margin, uncertainty sampling, and ISAL on the Diabetic Retinopathy dataset over 5 runs with variance reported, providing the cleanest head-to-head comparison in the paper.

- **Computational efficiency rationale.** The paper explicitly contrasts with Shapley-value methods (TMC-Shapley requiring O(√n log²n) retrainings) and uses a single-model closed-form Hessian, making the approach practical for datasets up to tens of thousands of samples.

- **Demonstrated as a general preprocessing module.** In the distribution shift experiments (Section 5.1), influence-based trimming boosts the performance of existing fairness interventions (Correlation Shift, FairBatch, RLL, Influence-based Reweighing) — shown in Figure 4 as greener regions in fairness-accuracy plots.

## Weaknesses

### Fatal
None.

### Major

- **Core trimming experiments compared only to random baselines.** Figure 2, which presents the main results on four real-world datasets, compares the proposed method exclusively to random trimming. Given that the paper frames itself as answering "what data benefits my classifier?" in contrast to prior data valuation, comparison to at least one principled alternative (e.g., trimming by loss magnitude, or one Shapley-based method on a smaller dataset) is needed to establish relative merit. The absence is partially mitigated by the active learning experiment (Section 5.5) which has multiple baselines, and the distribution shift experiment (Section 5.1) which compares against established fairness interventions — but the paper's central claim rests on evidence that is only calibrated against chance.

- **Ethical gap: no analysis of which samples are trimmed for fairness.** The toy example (Figure 1D) reveals that the (+) class contains mostly majority-group samples and the (−) class contains mostly minority-group samples, and trimming negative-influence-for-fairness samples reduces DP disparity. The paper never analyzes, in real-world experiments, whether the trimmed set disproportionately removes samples from a particular sensitive group or class. If the method systematically removes minority-group samples to improve a metric, this undermines the normative claim that the method is a positive contribution to fairness. The ethics statement (Section 7) further claims "the approaches cannot be used in a problematic way by a malicious adversary," which is demonstrably naive — selective data removal could suppress underrepresented voices if applied adversarially.

- **Interpretability contribution is presented but never validated.** Algorithm 1 produces a regression tree on influence scores with hierarchical shrinkage, and the paper claims this "interprets the feature space." However, the paper provides no evaluation of: (a) how faithfully the tree approximates the true influence surface, (b) stability of the identified feature splits across data splits or hyperparameter choices, or (c) whether the tree reveals insights beyond direct inspection of raw influence scores. Only one example subtree (Figure 3) is shown, without quantitative fidelity metrics. The paper itself acknowledges this limitation (Section 7: "better interpretability mechanisms can be designed"), but as presented, this remains an untested add-on rather than a validated contribution.

### Minor

- **Influence function finite-removal gap is not explicitly validated.** The method uses influence scores derived from an infinitesimal-weight approximation (ε → 0) to guide complete sample removal. While this is standard practice in the influence function literature and the toy experiment (Figure 1) provides implicit end-to-end validation, a direct check of whether the influence ranking correlates with the actual effect of leave-one-out retraining would strengthen confidence in the core mechanism.

- **No confidence intervals or statistical tests for most experiments.** Figure 2, Figure 4, and Table 1 report point estimates without variance or significance tests. Given that trimming budgets are modest (≤5–10%), it is unclear whether the observed improvements are statistically significant. The right y-axis in Figure 2 ("influence value of the trimmed samples") does not specify whether values are sums, means, or medians. The active learning experiment (Section 5.5) is the only one with error bars over multiple runs.

- **Poisoning defense claim is overstated.** The paper calls its method "potentially the first defense" against fairness poisoning attacks (Section 5.2). However, post-defense fairness does not consistently reach pre-attack levels (e.g., Drug dataset DP: 0.180 pre-attack → 0.249 post-defense under NRAA according to the table), and no comparison baselines (e.g., loss-based trimming, random trimming under attack) are provided. The claim is too strong for the evidence presented.

- **Online learning (Section 5.4): Bank dataset shows no improvement.** The paper transparently acknowledges this ("all given datasets (except Bank)") but offers no analysis of why trimming fails on Bank. Understanding failure modes would strengthen the paper.

- **Ethics statement is overly strong.** Claiming the approach "cannot be used in a problematic way by a malicious adversary" (Section 7) ignores the obvious dual-use potential of data selection to suppress minority data or manipulate metrics.

### Trivial

- The right y-axis label in Figure 2 ("influence value of the trimmed samples") should specify whether the plotted quantity is the sum, mean, or cumulative influence.

## Nice-to-Haves

- Comparing against a Shapley-based data valuation method (e.g., TMC-Shapley or KNN-Shapley) on a smaller dataset would strengthen the claim that influence-based selection offers practical advantages.
- Analyzing the demographic composition of trimmed samples in the fairness experiments would address the ethical gap.
- Validating the decision tree's fidelity (e.g., R² between tree predictions and actual influence scores) would substantiate the interpretability contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Unlabeled active learning handling not explained" (Harsh Critic, Section-by-Section note on Introduction).** The paper explicitly states: "we train our tree estimation model (Algorithm 1) without labels" (line 162). This criticism is factually wrong.

2. **"Algorithm 2 description is ambiguous" (Harsh Critic, Section 3.2 note).** The critic's own analysis confirms the description is consistent with trimming the most negative influence samples. The text and surrounding context are sufficient for understanding.

3. **"Extension to non-convex models not supported by experiments" (Harsh Critic, Section 2 note).** The paper explicitly scopes itself: "our paper is primarily focused on convex models and resolving the undecided research question of deep learning influence fragility is not our goal" (line 47). Criticizing absence of non-convex experiments is scope creep.

4. **"ξ vs ξ̄ notation inconsistent" (Harsh Critic, Section 3.1 note).** These are parser-induced formatting artifacts from equation extraction; the original submission's notation is standard.

5. **"Bank dataset not improving unexplained" (Harsh Critic, Section 5.4).** The paper acknowledges this transparently ("except Bank"). The absence of explanation is a minor point, but presenting it as a major omission ignores the paper's own admission.

6. **Strength Finder: "Interpretable feature-space analysis" claimed as core strength.** This conflicts with the verified weakness that the interpretability is not validated. Per the rules, when a strength and weakness disagree, the weakness wins. Moved here.

## Novel Insights

None beyond the paper's own contributions. The central observation — that influence functions can be extended beyond utility to fairness and robustness metrics, and that this enables data selection across diverse application scenarios — is the paper's own contribution, not a synthesis from the reviews.

## Suggestions

1. Add at least one additional baseline to Figure 2 (e.g., trimming by training loss magnitude, or a lightweight Shapley-based method on a smaller dataset) to calibrate the relative effectiveness of influence-based selection.
2. Analyze the demographic composition of trimmed samples in the fairness experiments and discuss the ethical implications — particularly whether minority-group samples are disproportionately removed.
3. Provide a direct validation (even on one dataset) of how well influence scores correlate with actual leave-one-out retraining effects for finite removal.
4. Add confidence intervals or error bars to the main experimental figures (Figure 2, Table 1) to establish statistical significance.
5. Tone down the poisoning defense claim ("potentially the first defense") or add a simple baseline comparison.
6. Clarify the Figure 2 right y-axis quantity (sum/mean/median of influence values).

## Score and Decision

This paper tackles an important and well-motivated problem: understanding what data benefits a classifier across utility, fairness, and robustness. The extension of influence functions to fairness and robustness metrics is a genuine contribution, and the breadth of application scenarios demonstrates practical relevance. However, the core experimental evaluation (Figure 2) compares only to random trimming without establishing relative merit against alternative data selection strategies. The interpretability contribution is presented as a core contribution but remains unvalidated. The fairness application contains an unexamined ethical blind spot regarding which samples are removed. These gaps are substantive enough that the paper does not meet the bar for acceptance in its current form. With additional baselines, validation of the interpretability component, and ethical analysis, this work could become a solid contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>