Now I have thoroughly read the paper. Let me produce the final consolidated review.

## Summary

SEED proposes an exemplar-free class-incremental learning method using a fixed ensemble of K experts that share a frozen initial backbone. For each new task, a single expert is selected (via a KL-divergence based criterion that maximizes distribution overlap of new classes) and fine-tuned, while the remaining experts are kept frozen. Inference uses a Bayes-classification ensemble across all experts. The method achieves large accuracy gains (10–17pp) in the challenging equal-split CIL setting across CIFAR-100, ImageNet-Subset, and DomainNet.

## Strengths

1. **Novel and principled selective expert-training paradigm.** Unlike prior ensemble methods (e.g., CoSCL) that update all experts on every task — incurring forgetting risk and computational cost — SEED updates only one expert per task. This directly bounds forgetting and encourages expert specialization. The ablation study confirms this: SEED (61.7%) substantially outperforms the standard ensemble baseline (56.9%) and the CoSCL ensemble loss variant (57.3%) with the same architecture (Tab. 2).

2. **KL-max expert selection is a clean, well-motivated criterion.** Selecting the expert whose latent-space Gaussian distributions for the new classes overlap the least (Eq. 2) is a principled way to minimize representational drift. The ablation (Fig. 6) shows KL-max outperforms random, round-robin, and KL-min selection strategies over 10 runs with random class orders, validating the design.

3. **State-of-the-art results in the hardest exemplar-free CIL setting.** In the equal-split scenario — where methods cannot rely on a large initial task or pretrained backbone — SEED outperforms the second-best method (FeTrIL) by 14.7pp, 17.5pp, and 15.6pp on CIFAR-100 for T=10, 20, 50 respectively (Tab. 1). Similar large margins hold on DomainNet (10–12pp) and ImageNet-Subset (9.1pp).

4. **Comprehensive ablation study validates each design component.** The ablation (Tab. 2) isolates the contributions of: (a) multivariate Gaussians vs. diagonal covariance vs. nearest-mean classifier, (b) temperature in softmax, (c) the ensemble strategy itself, and (d) the ReLU activation choice. Each component is shown to contribute meaningfully to the final result.

5. **Evaluation across diverse settings strengthens generality.** The paper tests on CIFAR-100, ImageNet-Subset, and DomainNet under equal-split CIL, large-first-task CIL, and task-incremental settings, with both task-aware and task-agnostic evaluation. This breadth supports the generality claims.

## Weaknesses

### Fatal
None.

### Major

1. **Missing parameter and compute budget for the main CIL experiments (Tab. 1).** SEED uses K=5 experts (with one shared backbone f and five expert-specific heads g_k). The main CIL comparison (Tab. 1) pits this ensemble against single-model methods (LwF, PASS, SSRE, FeTrIL) without reporting parameter counts, FLOPs, or inference cost for either side. The accuracy gaps are very large (10–17pp), but without this information it is impossible for the community to determine how much comes from the method's design versus from having additional model capacity. The paper does report parameter counts in the task-incremental setting (Tab. 3) and shows SEED can be more parameter-efficient than CoSCL, but this analysis is not extended to the CIL case. Moreover, the ablation's "standard ensemble" (which uses the same architecture as SEED) achieves 56.9% vs SEED's 61.7%, suggesting that ~4.8pp comes from the method design and the remaining gap over single-model methods comes from the ensemble itself. This is a correctable reporting gap, but it prevents full evaluation of the SOTA claim.

### Minor

1. **Class order not specified for main experiments (Tab. 1, Tab. 2).** The paper only states "random class order" for the selection-strategies experiment (Fig. 6) and the task-incremental table (Tab. 3). Whether Tab. 1 and Tab. 2 use a fixed or random class order is not stated. Since CIL results can vary with class ordering, this should be clarified. The standard deviations are reported and are modest, which mitigates the concern, but the missing detail is a reporting gap.

2. **No analysis of why SEED loses to FeTrIL on large-first-task ImageNet-Subset (T=11, 21).** The paper (line 181) honestly acknowledges that SEED underperforms FeTrIL for T=11 and T=21 on ImageNet-Subset in the large-first-task scenario, but offers no analysis of the cause. Since the paper claims plasticity as a core advantage, understanding this failure mode (e.g., insufficient shared representations, forgetting among experts, or the frozen backbone limiting learning on later tasks) would strengthen the characterization of when SEED is and is not appropriate.

3. **No analysis of temperature (τ) sensitivity.** The ablation shows τ=3 outperforms τ=1 (59.2% vs 61.7%), but no sensitivity analysis is provided. It is unclear whether τ=3 is robust or carefully tuned.

4. **No discussion of covariance estimation reliability with few samples.** In the T=50 split, each class has only ~10 training samples. Estimating full covariance matrices from so few samples is statistically questionable. The paper mentions singular covariance as a limitation (line 342) and says they address it by reducing latent space size, but provides no analysis of when estimates become unreliable or how the dimensionality S is chosen relative to available samples.

### Trivial
None.

## Nice-to-Haves

- Report inference cost (relative FLOPs or wall-time) for the ensemble vs. single-model baselines, since the paper already notes sharing f for computational efficiency but does not quantify it.
- Show learning curves (per-task accuracy) for the large-first-task scenario as was done for the equal-split setting in Fig. 4, to make the plasticity/stability trade-off more concrete where SEED struggles.
- Ablate unfreezing the shared backbone f (or making it expert-specific) to illuminate how much SEED's performance relies on the frozen-shared-backbone design choice.

## Removed Points

- **Harsh Critic's point about expert selection using all new-task data before training**: While factually correct, a single forward pass over the training data to compute selection statistics is negligible compared to the training cost (multiple epochs × forward + backward passes). This does not constitute a meaningful weakness and is standard practice in methods that analyze data before training.

- **Harsh Critic's "Inference cost" point**: Already partially acknowledged by the paper's shared-backbone design. The request for a wall-time benchmark is reasonable but belongs in Nice-to-Haves, not Weaknesses, since the main CIL setting's parameter count concern subsumes this.

## Novel Insights

The Harsh Critic's observation that the parameter count concern in Tab. 1 has no counterpart analysis in the CIL setting — even though Tab. 3 provides it for task-incremental — is the most actionable gap. Notably, the paper could partially address this without new experiments by estimating head-to-backbone parameter ratios from the architecture configuration (ResNet32 on CIFAR-100, ResNet18 on ImageNet). The mild conflict between the large CIL gains (requiring plasticity) and the failure on large-first-task ImageNet-Subset (where FeTrIL's stability wins) suggests that SEED's advantage may be bounded to settings where the tasks provide roughly equal data and where representational drift over the backbone is the main obstacle — deeper analysis of this boundary would strengthen the paper's framing.

## Suggestions

1. **Add parameter counts and relative compute to Tab. 1.** Report total parameters for SEED (broken down: shared backbone + K expert-specific heads + Gaussian parameters) and for each baseline. Include a brief note on training/inference FLOPs relative to a single-model baseline. This is the single highest-leverage fix and directly addresses the fairness concern.

2. **State class order explicitly for Tab. 1 and Tab. 2** (fixed order, random per run, or averaged over multiple orderings).

3. **Add a brief analysis of the large-first-task failure cases** (ImageNet-Subset, T=11, 21). A sentence hypothesizing the mechanism (e.g., whether the shared frozen backbone limits task-specific feature learning in later tasks, or whether the single-expert training per task causes underfitting when tasks are smaller) would substantially strengthen the paper's characterization of its own method.

4. **Add a temperature sensitivity analysis** (e.g., τ ∈ {1, 2, 3, 5}) or at minimum note that τ=3 was selected based on validation.

5. **Discuss covariance estimation reliability**, particularly for T=50 where per-class samples are ~10. Report the latent dimension S and the condition number or regularization used.

## Score and Decision

The paper introduces a clean, well-executed method for exemplar-free CIL and demonstrates substantial empirical improvements across multiple challenging settings. The main weakness — missing resource accounting for the ensemble in the central experiments — is an information gap rather than a methodological flaw, and is addressable without altering the method or running new experiments. The remaining concerns are minor. The paper is solid and should be accepted once the parameter/compute analysis is added.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>