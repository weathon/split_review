Now I have all the information I need to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper proposes RAOQ, a quantization-aware training framework to mitigate ADC quantization error in analog in-memory computing (IMC) systems. The approach comprises three techniques — W-reshape (kurtosis regularization on quantized weights to increase variance), A-shift (unsigned-to-signed conversion of activations to increase second moment), and BitAug (bit-augmentation to aid SGD optimization). The paper demonstrates results on ImageNet classification (ResNet/MobileNet/EfficientNet), COCO object detection (YOLOv5s), and SQuAD question answering (BERT), across multiple bit precisions, showing that RAOQ restores accuracy to within <1% of no-ADC baselines where conventional QAT degrades substantially.

## Strengths

1. **First practical demonstration of ADC-aware QAT on large-scale, diverse tasks.** Prior IMC-aware training methods (Jin et al., Sun et al., Wei et al.) validated only on MNIST and CIFAR. Table 1 shows RAOQ working on ImageNet, COCO 2017, and SQuAD 1.1 across multiple model families (ResNet, MobileNet, EfficientNet, YOLOv5s, BERT-base/large) and ADC precisions (7–9 bit). This is a clear step forward in practical relevance.

2. **Ablation study systematically isolates each technique's contribution.** Table 3 shows, for three different model architectures, the individual and combined impact of W-reshape, A-shift, and BitAug. Each component improves over the conventional-QAT baseline, and all three together achieve the best result. This controlled evaluation validates that the gains are not an artifact of any single component.

3. **Competitive comparison on a common benchmark.** Table 2 compares RAOQ against prior ADC-aware methods (Jin et al., Sun et al., Wei et al.) on CIFAR-10 with matched model architectures and configurations. RAOQ consistently yields smaller accuracy drops relative to the no-ADC baseline, establishing superiority even in the regime where prior work operates.

4. **Problem motivation grounded in an accessible SQNR analysis.** Section 3 provides a walkable derivation linking ADC SQNR to Var[Y], and empirically shows (Fig. 2b–d) a proportional relationship between Var[Y] and the second moments of activations/weights. This gives the method a clear rationale: adjusting weight and activation statistics to increase signal range before ADC conversion.

## Weaknesses

### Major

None. The remaining issues are addressable in minor revisions or rebuttal and do not threaten the paper's core empirical claims.

### Minor

1. **The A-shift theoretical rationale does not fully address the effect of the introduced offset on ADC clipping.** A-shift produces activations x̄_s = x̄ − 2^{b_x−1}, and the IMC column output becomes y = Σ w̄_i x̄_s,i + 2^{b_x−1} Σ w̄_i. The paper treats the increase in E[x̄_s²] (second moment of the shifted activation) as the mechanism for SQNR improvement, but the offset term 2^{b_x−1} Σ w̄_i contributes a non-zero mean to y that depends on the per-column weight sum. Since the ADC quantization scheme (Eq. 3) is symmetric about zero with clipping boundaries (−2^{b_a−1}, 2^{b_a−1}−1), a large mean offset could cause asymmetric clipping. The paper states this offset is "precomputed offline" with "no overhead," but it is not made clear whether the offset is subtracted before the ADC (in which case the clipping concern is moot) or added after in the digital domain. The paper should clarify the digital/analog boundary for the offset handling. The empirical results are strong and suggest the offset is handled correctly, but the theoretical framing needs tightening. *Verification:* Lines 106–120 describe A-shift; the offset term is defined in Eq. (line 117) and the precomputation claim is on line 120, with no further elaboration.

2. **No-ADC accuracy after W-reshape is not explicitly reported.** The kurtosis loss drives quantized weights toward a high-variance tail-heavy distribution, which could in principle increase weight quantization error even before ADC quantization enters. The paper claims "the penalty does not degrade previous accuracy" (line 87) and "All QAT (without ADC involved) accuracy matches SOTA results" (line 141), but the ablation study (Table 3) and main results (Table 1) report only ADC-affected accuracy. Adding a column for the QAT-stage accuracy (with W-reshape and A-shift, without ADC) for each ablated configuration would directly alleviate the concern that the reshaping trades task performance for ADC robustness. This is a reasonable request that does not invalidate the current results but would strengthen the paper.

3. **Empirical validation of the Var[Y]–second-moment relationship is limited.** Section 3's study uses only the first few layers of ResNet50 and MobileNetV2, with randomly sampled or generated inputs, to establish the proportional link that motivates W-reshape and A-shift. The paper acknowledges this (line 73: "To manage computation complexity"), and the methods are ultimately validated by strong end-to-end results. Still, the foundational claim that "Var[Y] can be increased by maximizing Var[w̄] and E[x̄²]" would be strengthened by showing it holds for deeper layers and for the shifted activation distribution after A-shift. As it stands, the motivation is plausible but the evidence is thin.

4. **No sensitivity analysis for the kurtosis coefficient λκ.** The loss weight λκ (Eq., line 98) controls the trade-off between weight reshaping and task accuracy, but no value is reported and no ablation varying λκ is shown. A brief sensitivity study showing the impact of λκ on both weight variance and final accuracy would help justify the chosen value and demonstrate robustness.

5. **No ablation for the signed-vs-unsigned activation claim for non-ReLU activations.** The paper states that for GELU/SiLU, "quantizing these activations as a signed number or unsigned number does not have much impact on the overall performance" (line 108), citing Bhalgat et al. (2020), and uses this to justify A-shift. While the claim is referenced, given that A-shift is one of the three core contributions, showing this explicitly (e.g., comparing signed vs. unsigned QAT accuracy for a BERT/Transformer variant) would be more self-contained.

### Trivial

- The offset handling in A-shift (precomputed offline) could be described with one more sentence clarifying whether it is removed before or after ADC conversion.
- The kurtosis loss coefficient λκ is defined but its numerical value(s) used in experiments are not stated.

## Nice-to-Haves

- A sensitivity analysis for λκ (kurtosis loss weight) showing the impact on both weight variance and accuracy.
- An explicit comparison of signed vs. unsigned quantization accuracy for non-ReLU activations (GELU, SiLU) to substantiate the claim used to motivate A-shift.
- A brief empirical check (even on 1–2 layers) of whether the Var[Y]–second-moment relationship holds for deeper layers and for the shifted activation distribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"BitAug description is absent from the main text"** (Critical Issue 1 from Harsh Reviewer). The extracted text jumps from Section 4.1 to Section 5 with no Section 4.2. Section 8 ("Reproducibility") is also visibly truncated (ends mid-sentence at "clarity.4"), confirming that the PDF parser dropped substantial content. Per the instructions, parser-stripped sections should not be treated as author errors. The original submission very likely contains a Section 4.2 describing BitAug.

2. **"No comparison with other IMC methods on large-scale tasks"** — The reviewer acknowledges this is because no prior work has scaled beyond CIFAR-10. The paper provides a fair comparison on CIFAR-10 (Table 2) and correctly notes the absence of scalable prior art. This is not a weakness of the paper.

3. **"Excluded layers handling"** — The paper clearly states which layers are excluded and why (depthwise convolutions at <7% compute, BMM2 at <1.5%), and this is standard practice in IMC papers. Not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviewers' points largely converge on what the paper already claims (strong empirical results, reasonable motivation) with concerns about analytical rigor that are standard for an empirical systems paper of this type.

## Suggestions

- Add one sentence clarifying whether the A-shift offset is subtracted before ADC conversion or added in the digital domain. This addresses the main theoretical ambiguity without changing the method.
- In the ablation study (Table 3), add a row or column showing the no-ADC accuracy for each combination of techniques. This would definitively answer the concern about W-reshape degrading the pre-ADC model quality.
- Report the λκ values used in experiments and, if space permits, a brief ablation over a few values.

## Score and Decision

The paper makes a solid empirical contribution — it is the first to demonstrate ADC quantization mitigation at practical scale across multiple modalities and tasks. The weaknesses are minor and addressable in revision. The missing BitAug description is a parser artifact, not an author omission. The core claims (RAOQ improves ADC-affected accuracy across diverse models and bit precisions) are well supported by Tables 1–3.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>