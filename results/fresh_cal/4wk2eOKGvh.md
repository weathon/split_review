Now I have all the information needed to produce the final consolidated review. Let me write it.

## Summary

This paper proposes Test-Time Ensemble (TTE), a method that enhances existing test-time adaptation (TTA) approaches by combining (1) adaptive weight-space averaging of the adapter network into an ensemble network via EMA, (2) dropout in the penultimate layer to promote representation diversity, and (3) a de-biased, noise-robust knowledge distillation objective (reverse KL) to prevent model collapse. The method is motivated by an empirical observation that TTA models exhibit linear mode connectivity, enabling weight-space ensemble benefits. TTE integrates with existing TTA methods (Tent, SAR, DeYO) and yields consistent accuracy gains across ImageNet-C, ImageNet-S, ImageNet-R, and ImageNet-V2 under challenging label-shift, batch-size-1, mix-shift, and continual-TTA scenarios.

## Strengths

- **Empirical demonstration of linear mode connectivity in TTA models**: Figure 1 and Eq. 1 show that weight-space interpolation between two TTA models adapted to different corruptions yields accuracy at least as good as output-space interpolation, establishing that TTA models are linearly connected and can benefit from weight averaging — a non-trivial extension of an insight from offline robust fine-tuning to the online TTA setting.

- **Consistent and practically meaningful accuracy gains**: Tables 1–3 report that integrating TTE improves accuracy by up to +9.9 % (ResNet50-GN, Label Shifts) and +3.9 % (ViTBase) over strong baselines, and prevents the near‑0 % collapse that all baselines suffer in continual non-i.i.d. TTA (Table 3). The gains hold across two architectures, three baseline methods, and four challenging scenarios, demonstrating robustness and general applicability.

- **Adaptive weight-space ensemble with momentum modulation**: Eq. 2 defines an EMA whose momentum decreases when the divergence between student and ensemble predictions is high. Figure 5 shows this dynamic scheme yields +1.8 % improvement over a fixed momentum in continual TTA, a concrete validation of the design choice beyond a simple static EMA.

- **Thorough evaluation across architectures, datasets, and shift types**: Experiments cover ResNet50-GN and ViTBase on four datasets (ImageNet-C, ImageNet-S, ImageNet-R, ImageNet-V2) under Label Shifts, Batch Size 1, Mix Shifts, and continual non-i.i.d. TTA, with hyperparameter sensitivity analysis and ablation studies.

- **Computational efficiency by design**: TTE requires only one additional forward pass for the ensemble network (fₑ) and avoids storing multiple models, keeping overhead minimal compared to multi-prediction or dense-augmentation alternatives.

## Weaknesses

### Fatal
None.

### Major

- **Reverse KL noise-robustness claim insufficiently validated in the actual TTA setting.** Section 3.2 and Figure 4 motivate the use of reverse KL divergence by analyzing its gradient behavior under *oracle* conditions (true labels used to distinguish correct from incorrect predictions). However, the paper does not provide a direct ablation in the *unsupervised* TTA setup (without true labels) comparing TTE with reverse KL vs. forward KL. Since the method works as a package, this does not invalidate the overall contribution, but the specific benefit of the reverse-KL design choice over standard KL in the intended use case is not isolated. This is the most significant gap in the paper's evidence chain and should be addressed with a dedicated ablation.

### Minor

- **De-biasing scheme (Eqs. 3–4) slightly underspecified.** After subtracting \(w(s_i) \cdot c_{bias}\) from \(\hat{y}_e\), the result \(\hat{y}'_{e,i}\) can produce entries outside \([0,1]\). The paper mentions "the effects of label smoothing" but does not specify whether further normalization (e.g., softmax or clamping) is applied before the KL divergence. Clarifying this would improve reproducibility.

- **Connection between temporal EMA and the linear mode connectivity observation could be more explicitly argued.** The preliminary experiment (Figure 1) interpolates between two separately adapted models (different corruptions). The actual method uses a temporal EMA of a single continuously adapting model. While both are weight-space operations, the paper does not discuss how the temporal EMA trajectory relates to the interpolation between stationary adapted models. A brief discussion would strengthen the motivation.

- **Computational overhead stated but not concretely measured.** The paper notes "only an additional feedforward pass" (Section 4.1) but does not report wall-clock time, inference speed, or FLOPs comparisons. Providing concrete numbers would substantiate the "computationally efficient" claim.

### Trivial
None.

## Nice-to-Haves

- **Direct comparison with mean-teacher-style self-ensembling** (e.g., applying a standard EMA teacher without the adaptive momentum or dropout mechanisms) on standard (non-continual) TTA scenarios would further isolate the contribution of TTE's specific design choices. The paper already compares with CoTTA in continual TTA.
- Including standard deviation or confidence intervals in the main tables (currently deferred to appendix) would help readers assess significance at a glance.

## Removed Points

- **Criticism about adaptive EMA creating a feedback loop** (Harsh Critic, Issue 2): The concern that momentum (Eq. 2) depending on the loss being optimized could lead to instability is speculative and contradicted by the paper's empirical evidence (Figure 5 shows adaptive momentum improves results by +1.8 %). Removed as unsubstantiated.
- **Criticism about missing comparison with Mean Teacher / self-ensembling methods**: The paper already compares with CoTTA, a self-ensembling method for TTA, and covers Tent, SAR, DeYO as primary baselines. Suggesting additional baselines is reasonable as a suggestion but not a weakness. Moved to Nice-to-Haves.
- **Criticism about lack of statistical significance in main tables**: The paper provides standard deviations in appendix tables. Moved to Nice-to-Have.

## Novel Insights

None beyond the paper's own contributions. The core insight — that linear mode connectivity holds for TTA models and can be exploited for efficient weight-space ensemble during online adaptation — is the paper's primary intellectual contribution, and the reviews do not surface observations beyond this.

## Suggestions

1. **Add an ablation comparing forward-KL vs. reverse-KL distillation in the actual unsupervised TTA setting** (e.g., on Label Shifts or Mix Shifts with ImageNet-C). This would either confirm the noise-robustness claim or appropriately qualify it.
2. **Clarify the post-processing of \(\hat{y}'_{e,i}\)** after the de-biasing subtraction (Eq. 4) — specify whether softmax is applied, or whether the values are clamped, or whether the KL divergence naturally handles values outside [0,1].
3. **Report wall-clock time or relative inference overhead** (e.g., "TTE adds X% to the per-step time compared to the baseline") to substantiate the computational efficiency claim.

## Score and Decision

The paper presents a solid empirical contribution with a well-motivated method, thorough evaluation, and consistent gains across diverse challenging scenarios. The main weakness (insufficient isolation of the reverse-KL contribution in the actual TTA setting) is addressable and does not undermine the core claim that TTE improves TTA performance. The writing is clear, and the method is simple to integrate with existing approaches.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>