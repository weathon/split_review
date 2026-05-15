Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

---

## Summary

This paper proposes Test-Time Ensemble (TTE), a wrapper method for test-time adaptation that constructs an ensemble teacher via EMA weight averaging (adaptive momentum) and dropout, then distills de-biased knowledge back to the student adapter using reverse KL divergence. The method is motivated by an empirical finding that TTA models exhibit linear mode connectivity. TTE integrates with existing TTA methods (Tent, SAR, DeYO) and yields consistent accuracy improvements across ImageNet-C (label shifts, batch size 1, mix shifts, continual non-i.i.d.) and natural distribution shifts.

## Strengths

- **Consistent and substantial empirical gains across diverse challenging scenarios**: Tables 1–3 show that TTE improves accuracy over three strong TTA baselines, with especially large gains on ResNet50-GN (e.g., +9.9% on Label Shifts for DeYO+TTE) and in continual non-i.i.d. settings where baselines collapse to near-zero accuracy (Table 3). The improvements hold across four different test-time scenarios.
- **Effective collapse prevention in extreme conditions**: In continual TTA with non-i.i.d. conditions (Table 3), TTE maintains stable accuracy (49.7% on ResNet50-GN, 61.6% on ViTBase) while all baselines (Tent, CoTTA, SAR, DeYO) drop to near-zero in later stages. This is a practically important result.
- **Seamless integration with multiple TTA methods**: TTE is a general plugin that wraps around Tent, SAR, and DeYO without modifying their core objectives, showing consistent improvements across all three. This demonstrates broad applicability beyond a specific algorithm.
- **Low hyperparameter sensitivity**: Figure 6 shows that TTE steadily outperforms DeYO across a wide range of dropout ratios and temperature values, indicating the method is robust to hyperparameter choices and easy to deploy.
- **First empirical demonstration of linear mode connectivity in TTA models**: Figure 1 provides evidence that weight-space interpolation of two independently adapted TTA models can match or approach output-space ensemble accuracy, which is a novel insight that opens the door for weight-averaging strategies in online TTA.

## Weaknesses

### Fatal
None.

### Major

- **Core claim about representation enrichment is not directly verified**: The paper frames its contribution as "enhancing model representations" and "promoting representation diversity," yet provides no representation-level analysis — no feature diversity metrics, effective rank, t-SNE/UMAP visualizations, or prediction agreement/disagreement between fₑ and fₐ. The observed accuracy improvements could plausibly arise from the distillation objective acting as a training stabilizer rather than from genuinely enriched representations. This is a gap between the paper's stated motivation and its evaluation, and would need to be addressed either with direct evidence or by reframing the contribution.

- **The LMC motivation is not fully connected to the actual method**: Figure 1 demonstrates linear mode connectivity for two *independently adapted* TTA models (trained on different corruptions). However, TTE uses an EMA of a *single model's weights over time* — a fundamentally different object. The paper does not verify that the EMA trajectory maintains LMC with the current adapter during normal (non-collapsed) operation. The loss barrier analysis (Figure 3) is shown only for a collapse scenario. Without this bridge, the EMA ensemble is a heuristically motivated technique rather than a direct consequence of the claimed LMC property. This weakens the paper's most foundational insight.

### Minor

- **De-biasing step may produce invalid distributions**: The subtraction in Equation (5) — ŷ′ₑᵢ = ŷₑᵢ − w(sᵢ)·c_bias — can produce vectors with negative elements, yet the paper uses reverse KL divergence as the distillation loss, which requires valid probability distributions. No normalization, softmax, or clipping is mentioned after the correction. In practice the method works (Figure 7), but this is an underspecified implementation detail that should be clarified.

- **Adaptive momentum has limited validation**: Table 6 shows that constant momentum 0.999 achieves the best result for ViTBase, outperforming lower constant values. Yet the main method uses adaptive momentum with m₀=1.0 (always ≤1), which is more aggressive than 0.999. The only comparison of adaptive vs. constant momentum is a single continual-TTA run (Figure 5, ViTBase only) showing +1.8% — no error bars reported, and not replicated across architectures. The main tables do not report results using the best tuned constant momentum, making it unclear whether the adaptive scheme is genuinely beneficial or simply a complex way to achieve a fixed slow update.

- **No comparison with simpler collapse-mitigation alternatives for de-biasing**: The de-biasing scheme subtracts an accumulated bias vector weighted by cosine similarity. The paper does not compare this against simpler strategies such as label smoothing, confidence masking, or entropy regularization, which are standard baselines for preventing collapse in unsupervised adaptation. The sensitivity analysis (Figure 7) shows performance degradation at certain hyperparameter values, indicating the method is not entirely parameter-insensitive.

- **Computational cost is understated**: The paper states that TTE requires "only an additional feedforward pass for fₑ," which doubles the inference cost. No wall-clock time or FLOPs comparison is provided. For ViTBase, this is a non-trivial increase that should be quantified.

- **Limited scope of distillation loss comparison (Figure 4)**: The comparison between standard and reverse KL divergence is shown for only one corruption type (Gaussian noise) and one method (Tent). This is insufficient to establish reverse KL as a generally beneficial choice across diverse distribution shifts.

- **Near-zero gains on ImageNet-V2 (intrinsic shifts)**: Table 4 shows accuracy gains of 0.0–0.1% on ImageNet-V2. The paper acknowledges this briefly ("further investigation is needed") but does not discuss *why* TTE fails for intrinsic shifts, which limits the claimed broad applicability.

### Trivial
- Figure 5 (adaptive vs. constant momentum comparison) does not report error bars.
- Table 5 component ablation — from the available text, it is unclear whether dropout and weight-space ensemble contributions are isolated separately.

## Nice-to-Haves
- A wall-clock time or FLOPs comparison to quantify the claimed efficiency of TTE.
- Comparison of the de-biasing scheme against simpler alternatives (label smoothing, confidence masking) to isolate its advantage.
- A t-SNE/UMAP visualization or feature diversity metric comparing baseline TTA and TTE representations.
- Testing TTE on segmentation or detection tasks to verify generality beyond image classification.

## Removed Points
These points were flagged to be removed; treat them with caution:

- **Missing appendix content / theoretical analysis deferred to appendix**: The hard rule states these are parser artifacts, not author omissions. Removed.
- **Missing related works**: The hard rule states I cannot confirm the existence of omitted references without external sources. Removed.
- **Pure formatting/style nitpicks**: Per hard rules on parser artifacts. Removed.
- **Criticism about "no loss barrier metric" in preliminary experiment**: The paper shows accuracy interpolation (Figure 1) which is one way to visualize LMC, and mentions loss barrier in Figure 3. The objection about not reporting the standard loss-barrier metric is noted but the paper partially addresses it; moved here as it is a weaker criticism than the major LMC gap above.
- **"Circular dependency" in adaptive momentum (momentum → ensemble → loss → momentum)**: This is a standard design pattern in teacher-student frameworks (e.g., self-training, CoTTA) and does not constitute a unique flaw; many such systems have feedback loops that work in practice. The paper's empirical results demonstrate the method's effectiveness despite any theoretical circularity. Removed.
- **The criticism that Figure 4 is limited to "single corruption and single method" was kept as a minor point above** (this is already addressed).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution**: Either provide direct representation analysis (effective rank, feature diversity, t-SNE) to substantiate the "enhancing representations" claim, or honestly reframe the contribution as "stabilization via robust distillation from a weight-averaged teacher" — the empirical results are strong enough to stand without the representation-enrichment narrative.

2. **Bridge the LMC gap**: Measure loss barriers between fₐ at different time steps and between EMAs fₑ and fₐ during normal (non-collapsed) adaptation to verify that the EMA trajectory benefits from LMC in the same way as independently adapted models.

3. **Clarify the de-biasing normalization**: Explicitly state whether softmax or normalization is applied to ŷ′ₑ after Equation (5) to ensure valid probability distributions for KL divergence.

4. **Strengthen adaptive momentum validation**: Report accuracy for the best tuned constant momentum in the main test scenarios (not just one continual-TTA run), replicate across architectures, and include error bars.

5. **Quantify computational cost**: Report wall-clock time or FLOPs comparison to contextualize the "only an additional feedforward pass" claim.

## Score and Decision

The paper presents a practically effective method with consistent and often substantial accuracy gains across diverse challenging TTA scenarios. The collapse prevention in continual non-i.i.d. settings is particularly noteworthy. However, two gaps weaken the paper relative to its stated ambitions: the core "representation enhancement" narrative is unevaluated, and the LMC motivation is only partially connected to the actual EMA-based method. The method's empirical contributions are real, and the identified issues are addressable with additional analysis and presentation revisions.

**Score: 6.0** — A solid empirical paper with a useful method, but it would benefit from (a) reframing the contribution to match the evidence, (b) closing the LMC motivation gap, and (c) adding missing ablations and clarifications. In its current form, the paper overclaims slightly relative to what is actually shown.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>