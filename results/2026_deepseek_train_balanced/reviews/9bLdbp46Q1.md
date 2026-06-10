Here is the final consolidated review:

## Summary

This paper proposes ARC (Adaptive Retention & Correction), a test-time plug-in for continual learning that mitigates classifier bias. ARC operates during inference by: (1) detecting test samples from past tasks via two confidence-based criteria (Out-of-Task detection), (2) dynamically retraining the classifier on correctly-classified past-task samples (KR), and (3) correcting predictions for misclassified past-task samples using a Task-based Softmax Score with temperature scaling (KC). The method requires no modifications to training and is evaluated by plugging into 8 CL methods (Finetune, iCarL, Der, Memo, L2P, DualPrompt, CODA-Prompt, SLCA) on Split CIFAR-100 and Split ImageNet-R, showing consistent improvements in average accuracy (avg +2.7% and +2.6%) and forgetting reduction.

## Strengths

1. **Broad plug-and-play compatibility across 8 diverse CL methods without training modification**: Table 1 shows ARC improves Average Accuracy for every method tested on both benchmarks, from +0.7% (SLCA on CIFAR-100) to +6.6% (iCarL on ImageNet-R). This coverage substantially exceeds prior bias-correction methods (BiC, IL2M, OBC) that require stored memory or modified training pipelines.

2. **Method operates entirely at test time, applicable to memory-free CL settings**: ARC works for four memory-free methods (L2P, DualPrompt, CODA-Prompt, SLCA), yielding improvements of 0.7–3.0% on CIFAR-100 and 1.4–2.7% on ImageNet-R (Table 1), directly addressing the paper's motivation that the field is shifting toward memory-free paradigms.

3. **Empirical validation of both detection assumptions across all methods**: The empirical validation table reports Assumption 1 holds with 88.4% accuracy (averaged across 8 methods) and Assumption 2 holds with 71.9% accuracy on Split ImageNet-R. These measurements directly support the viability of the ARC pipeline.

4. **Novel w = c/ĉ ratio metric with ablation support**: The ratio-based score (Assumption 2) compares full-task confidence to past-task-only confidence. The ablation (Table "adaptive correction ablation") shows it outperforms using raw confidence (w = c) by an average of 0.5% across Finetune, iCarL, Der, and Memo.

5. **Substantial forgetting reduction, especially for non-prompt methods**: ARC reduces Forgetting by an average of 8.0% on CIFAR-100 and 7.0% on ImageNet-R (Section 4.2). For non-prompt methods, the reduction is 11.2% and 10.0% respectively — e.g., Finetune's forgetting drops from 29.8 to 10.8 on CIFAR-100 (a 19.0-point reduction).

## Weaknesses

### Major

1. **No comparison against generic test-time adaptation baselines, leaving it unclear whether gains stem from ARC's specific mechanisms or from any test-time update**. ARC updates the classifier during testing, unlike the standard frozen-model evaluation used for baselines. The paper acknowledges this (line 66: "we follow the setting of online TTA"), but no TTA baselines (e.g., self-training with pseudo-labels, SHOT, or CoTTA) are compared. The reported gains (e.g., +2.7% CIFAR-100, +2.6% ImageNet-R) could partially reflect the generic benefit of test-time updating rather than ARC's specific OOD detection and correction mechanisms. The ablation studies show that individual design choices (w ratio, temperature) contribute, but they do not establish that ARC outperforms a simpler TTA approach. Without this control, the paper's central claim that ARC's specific mechanisms drive the improvements is incompletely supported.

### Minor

1. **Hyperparameter values (β, γ, T) are not reported**. The method depends on three thresholds — β (confidence threshold for Assumption 1), γ (ratio threshold for Assumption 2), and T (TSS temperature). None are specified anywhere in the paper. No sensitivity analysis is provided either, making it impossible to assess whether results reflect a carefully tuned operating point or a robust range.

2. **No variance or multiple-run statistics reported**. Every result in Table 1 is a single number with no indication of variability. Since online TTA means test-sample arrival order matters (KR gradient updates depend on order), results could be sensitive to random ordering.

3. **Computational overhead of test-time gradient updates is not discussed**. KR performs a gradient update per qualifying test sample during inference. The paper provides no analysis of additional latency or FLOPs compared to base methods.

4. **The 92.9% upper bound on CIFAR-100 is cited without explanation** (line 219). The reader cannot calibrate how much of the remaining gap ARC closes without knowing what defines this bound.

5. **Anomaly in KR ablation for L2P is noted but not explained**. The ablation (Table "adaptive retention ablation") shows L2P achieves 86.6% with only ℒ_EM but only 86.2% with the combined ℒ_CE + ℒ_EM objective. The paper mentions this in passing but does not analyze why cross-entropy supervision from pseudo-labels hurts this method.

### Trivial

None.

## Nice-to-Haves

- **Systematic analysis of sensitivity to test-set composition**: The conclusion (line 354) acknowledges performance "may depend on the distribution of test samples." A controlled analysis varying the proportion of past-task test samples (e.g., 5% to 50%) would quantify this limitation's scope.
- **Comparison with a simple self-training TTA baseline** (e.g., pseudo-labeling all test samples with a confidence threshold, without ARC's OOD detection or task-specific corrections) would directly address the main confound.

## Removed Points

These points were considered but removed from the main review:

- **"Priority claim is too strong" (Harsh Critic)**: The paper says "we are among the first to analyze such possibility" (line 68). This is appropriately softened with "among the first." **Reason**: not a substantive weakness.
- **"TSS temperature schedule lacks principled justification" (Harsh Critic)**: The schedule is heuristic, but this is acceptable for an empirical paper, and the ablation confirms its contribution (0.6% drop without it). **Reason**: the paper does not claim a theoretical derivation; the heuristic is empirically validated.
- **"Method depends on test distribution in ways not analyzed" (Harsh Critic)**: The paper acknowledges this limitation (line 354). Requesting a full systematic analysis goes beyond what's standard to expect; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a generic TTA baseline**: Apply a simple test-time adaptation (e.g., self-training with an MSP threshold on all test samples, without ARC's OOD detection or w-ratio filtering) to at least 2–3 base methods to control for the confound of test-time updating.
2. **Report hyperparameter values and sensitivity analysis**: Specify β, γ, and T used in the main experiments; add a plot showing accuracy as each threshold varies.
3. **Report variance**: Run main experiments with ≥3 random test orderings; report mean ± std.
4. **Define the upper bound**: Clarify what 92.9% represents and how it is computed.
5. **Add computational overhead analysis**: Report inference time per sample with and without ARC for at least one base method.
6. **Analyze the L2P KR anomaly**: Investigate why ℒ_CE hurts L2P and discuss implications.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>