Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper proposes a backdoor-based DNN watermarking method that eliminates the need for any original training data by using a single out-of-distribution (OoD) image with strong augmentations to create a surrogate dataset for watermark injection. The method combines fine-tuning on this surrogate data with adversarial weight perturbation (WP) to improve robustness against removal attacks (fine-tuning, pruning, model extraction). Experiments on CIFAR-10, CIFAR-100, and GTSRB show that the method achieves high watermark success rates (e.g., 95.66% OoDWSR on CIFAR-10) with minimal accuracy degradation (<3%), and that WP substantially improves post-attack watermark retention (e.g., 57.52% vs. 19.94% after RT-AL on CIFAR-10).

## Strengths

- **Data-free, privacy-preserving watermark injection.** The paper convincingly demonstrates that a backdoor watermark can be injected without any access to original training data, using only a single OoD image. Victim model results (Table 2) show high OoDWSR (up to 95.66% on CIFAR-10) with <3% accuracy drop, directly supporting the core claim that training data is unnecessary.

- **Robustness across multiple removal attack families.** The method maintains statistically significant watermark evidence after fine-tuning (FT-AL, FT-LL, RT-AL), pruning (20%, 50%), and model extraction across all three datasets (Tables 2 and 4). p-values are consistently below 0.05, confirming statistical distinguishability between suspect and non-watermarked models.

- **Effectiveness of weight perturbation for robustness.** Table 7 provides direct ablation evidence: after RT-AL attack on CIFAR-10, OoDWSR drops to 19.94% (trojan_wm) without WP but stays at 57.52% with WP — a 3× improvement. Figure 5 further shows that WP shifts the parameter distribution while maintaining normality, avoiding easy detection.

- **Sample and time efficiency.** The method requires only one OoD image and 20–30 epochs of fine-tuning, with CIFAR-10 reaching stable accuracy and OoDWSR in just 10 epochs (Figure 2). This is a clear practical advantage over data-free methods that train a generator for hundreds of epochs (as the paper notes regarding Li et al. 2022).

- **Superior robustness over i.i.d. poisoning baselines.** Table 5 directly compares OoD-based vs. ID-based watermarking under the same RT-AL attack: ID-poisoned watermarks drop to 4.13% success rate, while OoD-poisoned watermarks retain 57.52%. This controlled comparison is a strong empirical finding that goes beyond the paper's core method.

## Weaknesses

### Fatal

None. The paper's core claims — that data-free watermark injection with a single OoD image is possible, efficient, and can be made robust via weight perturbation — are supported by the experimental evidence.

### Major

- **No direct quantitative comparison to the closest prior data-free method (Li et al. 2022).** The paper mentions Li et al. (2022) (lines 37, 81–82) as the most closely related data-free approach, notes that it is "time-consuming," and positions the proposed method as filling an efficiency gap. Yet no experiment compares against Li et al. or any data-free/OoD-based baseline on injection efficiency, robustness, or watermark quality. Without such a comparison, the claimed advantage over existing data-free methods is asserted rather than demonstrated. At minimum, a comparison on injection time (epochs/seconds) and post-attack OoDWSR for a representative setting would substantiate the paper's positioning.

### Minor

- **KL term in the WP objective is not ablated.** Equation (5) introduces a KL divergence term with trade-off β=6, justified as preserving main-task performance. However, the first term of L_inj already includes cross-entropy loss on clean samples against pseudo-labels for the same purpose. The paper never ablates β=0 to isolate whether the KL term actually contributes — it only compares with vs. without the full WP procedure (Table 7), which includes both adversarial perturbation and the KL term. The interaction and necessity of this term remain unclear.

- **No sensitivity analysis for key hyperparameters γ and β.** The perturbation constraint γ is set to 0.1 for CIFAR-10/GTSRB and 0.05 for CIFAR-100, while β is fixed at 6 everywhere (line 267). No rationale is given for these specific values, and no experiments show how performance (Acc, OoDWSR, post-attack OoDWSR) varies with γ or β. Since γ controls the perturbation radius and is central to the robustness claim, the method is under-characterized in this respect.

- **Verification false positive rate is not quantified.** The paper states (line 142) that a suspect model is considered a copy if its OoDWSR "far exceeds" the non-watermarked baseline rate (e.g., 0.0487 for trojan_wm on CIFAR-10). No threshold is specified, and no analysis is provided of how often a non-watermarked model trained on an unrelated distribution could accidentally exceed such a threshold. A false positive rate analysis is essential for any robust IP verification procedure.

- **Threat model does not discuss inference-based detection of the watermark.** The paper assumes the OoD image and augmentation process are secret, preventing an attacker from generating verification samples (lines 136–138). However, an attacker could probe the suspect model with a diverse set of OoD inputs or random noise and look for anomalous high-confidence predictions to a specific class, potentially inferring the watermark's existence or trigger characteristics. This class of membership-inference attacks should at least be acknowledged.

- **T-test independence assumption is not discussed.** The T-test compares output logits of the suspect model against a non-watermarked model. As the suspect model may be derived from the victim (through fine-tuning, pruning, or extraction), the outputs may not be independent — violating a core assumption of the test. The paper should discuss whether this affects the validity of the resulting p-values.

- **No analysis of computational overhead.** The paper claims time efficiency but does not report the training time cost of the min-max WP optimization (v-step + w-step) compared to standard fine-tuning without WP. This matters for practitioners evaluating the efficiency claim against alternatives.

- **Robustness experiments only consider i.i.d. data for removal attacks.** The attacker is assumed to use i.i.d. data for fine-tuning/pruning removal. An attacker with access to a different OoD dataset (or even a different single OoD image) could attempt removal differently. This scenario is not explored.

### Trivial

- The description of OoD images in the main text is minimal (only names and "dense" vs. "sparse" categorization given on line 487). Basic content information (approximate resolution, general visual content) would help readers assess the generality of the image choice findings.

## Nice-to-Haves

- A sensitivity analysis of γ in {0.05, 0.1, 0.2} and β in {0, 3, 6, 12} on CIFAR-10 (trojan_wm) would substantially strengthen the method's characterization.
- Providing a confidence-based verification procedure (e.g., threshold defined as mean + 3σ of non-watermarked OoDWSR) would make the IP verification claim more actionable.
- Reporting wall-clock training time with vs. without WP for at least one dataset would help practitioners assess the efficiency trade-off.
- A baseline using random noise (rather than a natural OoD image) as the source would help validate the "expressive single image" claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Weight perturbation ablation is incomplete (only CIFAR-10, one attack)."** The paper states (line 546): "More results for WP can be referred to sec:extended_wp," pointing to an appendix. Per the guidelines, appendix content is stripped by the parser and cannot be assumed missing in the original submission. Removed.
- **"The paper does not discuss unique patch diversity from the single OoD image."** The paper explicitly states the surrogate dataset is of a "desired size" (line 119). The diversity concern is inherent to all single-image methods and is addressed by the augmentation pipeline (cropping, rotation, shearing, color jittering, line 123), which is standard practice in this line of work (Asano et al. 2022). This is a feature, not a bug.
- **Various generic/formatting nitpicks from the harsh critic's "Other Observations" section.** The IDWSR observation is an observation, not a weakness; the computational cost point is already covered above as a minor weakness; other stylistic comments lack substantive impact on the paper's evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same assessment: the paper's core idea is clever and validated, but its evaluation suffers from missing comparisons and ablations that prevent the contribution from being fully substantiated. No reviewer identified a hidden flaw or unanticipated implication beyond what the paper already discusses.

## Suggestions

1. **Add a direct comparison to Li et al. (2022)** on at least CIFAR-10 for injection time, OoDWSR, and post-attack robustness. If Li et al.'s generator-based training is prohibitively slow to replicate, report this as a qualitative observation and compare against a simpler data-free baseline (e.g., using random noise images as the surrogate dataset) to isolate the contribution of a natural OoD image.
2. **Ablate the KL term** by setting β=0 with WP still active, and report results for all attack types on CIFAR-10. If results are similar, the term can be removed or simplified.
3. **Provide sensitivity curves** for γ on CIFAR-10 (trojan_wm) showing Acc, OoDWSR, and post-RT-AL OoDWSR.
4. **Define a concrete verification threshold** (e.g., OoDWSR > μ_non-wm + k·σ_non-wm) and report the resulting false positive rate over multiple non-watermarked models.
5. **Discuss the T-test's independence assumption** and, if possible, use a paired or permutation test as a robustness check.

## Score and Decision

This paper presents a genuinely clever and practical approach to a real problem. The core idea — exploiting a single OoD image's representational diversity for data-free watermarking — is well-motivated and validated by solid experimental results. The weight perturbation mechanism is shown to meaningfully improve robustness, and the finding that OoD-injected watermarks are intrinsically harder to remove than ID-injected ones is a novel empirical insight. However, the evaluation has significant gaps: the missing direct comparison to the closest prior data-free method (Li et al. 2022) is the most serious, as it prevents the paper from substantiating its claimed advantage over existing work. Additional issues (KL term not ablated, no hyperparameter sensitivity analysis, unquantified verification false positive rate) are individually minor but collectively reduce the paper's thoroughness. These are all addressable with revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>