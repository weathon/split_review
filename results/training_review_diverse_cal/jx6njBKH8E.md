Here is the final consolidated review.

---

## Summary

This paper proposes a novel attack scenario in which an adversary adversarially fine-tunes a pre-trained language model (using self-generated text, pseudo-labels from DetectGPT's perturbation discrepancy, and RLHF) to amplify exposure of the model's original *pre-training* data. On OPT models ≥1.3B parameters, the method achieves a 4–8× increase in extracted training sequences compared to the reference LM, with ablation studies suggesting the effect reflects genuine memorization rather than collapse to pseudo-labels.

---

## Strengths

- **Novel and timely threat model.** Unlike prior post-hoc extraction strategies (e.g., better prompts, ranking methods), this paper is the first to propose *adversarially fine-tuning the target LM itself* to amplify memorization of its pre-training data. The threat model is well-motivated by the growing availability of open-source models, parameter-extraction techniques, and fine-tuning APIs (Section 3).

- **Large, consistent amplification across model scales.** Table 2 shows that models ≥1.3B parameters exhibit 4–8× increases in true positives (e.g., OPT-1.3B from 97 to 775 extracted sequences). The effect grows log-linearly with parameter count (Figure 2), consistent with prior scaling laws for memorization.

- **Ablation studies show the effect is not trivial overfitting.** After deduplication, amplification persists (up to 8.4× for OPT-1.3B, Table 4). The fine-tuned LM produces mostly *new* extracted samples (70–98% non-overlapping with the reference LM, Table 5) and maintains or improves diversity (lower self-BLEU, higher unique n-grams, Tables 6–7). These results rule out simple collapse to repeating a few pseudo-labeled sequences.

- **Concrete evidence of exposure severity.** The fine-tuned LM can leak up to 1,163 verbatim words (Figure 4), and Wikipedia is identified as the most vulnerable data source (7.2× increase, Figure 3).

---

## Weaknesses

### Fatal

1. **Contradictory and unjustified use of perturbation discrepancy as a membership proxy.** This is the paper's single most critical problem. The paper describes DetectGPT correctly in Section 2.1: perturbation discrepancy *converges to 0 for machine-generated text* and takes *higher values for human-written text* (line 103). Yet the method repeatedly asserts the opposite: "lower values signify a higher probability of the text being human-written" (Figure 1 caption, line 24); "a lower discrepancy is assumed to more likely contain human-written text" (Section 4.1, line 197); "the text preferred by the target LM is likely human-written, meaning it would have a relatively lower perturbation discrepancy" (line 202). This is a direct contradiction of the cited DetectGPT framework. The paper offers no justification for this inversion, no alternative definition, and no empirical demonstration that the relationship reverses for self-generated texts containing training data. Because this inversion is the foundational premise for the entire pseudo-labeling pipeline, the core logic of the attack is uninterpretable. The fact that the experiments *do* show amplification despite this contradiction suggests the effect may be driven by an entirely different mechanism (e.g., the model simply becoming more confident and generating longer memorized strings), rather than the claimed mechanism of preferring texts with lower perturbation discrepancy.

2. **Missing control conditions needed to attribute the effect to the specific method.** The experiments compare fine-tuned LM vs. reference LM, but do not isolate *which* component of the method drives the amplification. At minimum, the following baselines are absent and needed to support the claimed contribution: (a) supervised fine-tuning (SFT) on the same pseudo-labeled pairs (treating "chosen" texts as targets), (b) RLHF with *random* pairing of texts rather than sorted-by-discrepancy pairs, and (c) RLHF with *inverted* pseudo-labels (favoring higher discrepancy). Without (a), it is unclear whether RLHF adds value over simply training on texts believed to contain training data. Without (b), it is unclear whether the pairing heuristic matters. Without (c), it is unclear whether the specific *direction* of the pseudo-label signal is responsible. The ablation studies (redundancy, uniqueness, diversity) address overfitting but do not isolate the pseudo-labeling *mechanism* itself.

### Major

3. **No evidence that pseudo-labels correlate with true membership.** Table 1 shows the RM can predict the pseudo-labels with ~62–70% accuracy, but this is circular — it only shows the RM can learn the pseudo-labeling rule, not that the rule corresponds to actual presence of training data. The paper does not provide a direct validation (e.g., on a small set where ground-truth membership is known) that texts with lower perturbation discrepancy actually contain more training data. This gap, combined with the sign contradiction (Weakness 1), means the paper's central assumption is completely unvalidated.

### Minor

4. **Qualitative analysis reveals most extracted data comes from Wikipedia (public, non-sensitive text).** This does not invalidate the method, but it substantially weakens the paper's framing around "sensitive information" and "privacy risk." The demonstrated attack amplifies memorization of public text. The paper should be more precise about what kind of risk it is amplifying.

5. **Verification uses only 10 of 12 original OPT training datasets.** CC-Stories and CCNewsV2 are omitted (the paper acknowledges this, line 285). The direction of potential bias (overestimate or underestimate of true positives) is not discussed.

### Trivial

None.

---

## Nice-to-Haves

- **Statistical significance / repeated runs for main extraction results (Table 2).** The paper states it did not conduct repeated experiments because generating 100,000 texts reduces bias. Confidence intervals or multiple seeds would strengthen confidence in the amplification factors.
- **Random-pairing ablation for the pairing heuristic.** The sorting-and-pairing strategy (Section 4.1) assumes that maximizing the discrepancy difference between pairs improves RM training. A random-pairing control would test this assumption.
- **Comparison of a standard TDE attack (e.g., Carlini et al. 2021) on the fine-tuned vs. reference models** to show the amplification is robust across attack methods, not just the paper's own extraction pipeline.

---

## Removed Points

- *"The assumption of full parameter access is too strong"* — The paper adequately justifies this assumption in Section 3.1 (public LMs, parameter extraction, fine-tuning APIs). The reviewer's suggestion to discuss black-box-only attacks is a reasonable extension, not a weakness.
- *"Low RM accuracy (62–70%) is a fatal concern"* — The reviewer overstates this. The RM accuracy is 12–20% above random (50%) with tight confidence intervals (±<2.3%), which is meaningful for binary preference from inherently noisy pseudo-labels. The paper also discusses why larger models yield noisier labels. This is a legitimate minor concern but not fatal — downgraded to Minor (folded into Weakness 3 above, which concerns the more fundamental lack of ground-truth validation).
- *"The paper should compare to existing TDE attacks on the same fine-tuned models"* — A reasonable ask but not a weakness; the paper's contribution is the amplification *relative to the reference model*, not a new extraction method.
- Generic strengths from Strength Finder that cite no concrete evidence — dropped.

---

## Novel Insights

The deep-review process reveals a tension that the paper's own experiments cannot resolve: the method works empirically (4–8× amplification), yet the stated mechanism is self-contradictory (low perturbation discrepancy should indicate *machine-generated* text per the cited DetectGPT, but the paper treats it as indicating human-written / training-data-containing text). This suggests either (a) the pseudo-labeling signal actually arises from a different property of the texts that happens to correlate with the inverted discrepancy (e.g., confidence, length, perplexity), or (b) the amplification is driven by RLHF's effect on the model's generation distribution (increased confidence, longer consistent sequences) that *coincidentally* produces more exact matches with training data. The paper's ablations on diversity and uniqueness rule out naive collapse but do not distinguish between these alternative explanations. A rigorous attribution experiment — ground-truth verification of the pseudo-label direction, control conditions with random/inverted labels — is essential before the claimed mechanism can be accepted.

---

## Suggestions

1. **Resolve the perturbation discrepancy contradiction.** Either correct the description throughout to align with DetectGPT (higher discrepancy → human-written → chosen), or provide a clear empirical justification for why lower discrepancy is preferred in *this specific setting* (e.g., by computing the correlation between perturbation discrepancy and true membership on a small labeled set). Without this, the core logic is uninterpretable.

2. **Add the SFT baseline** on the same pseudo-labeled pairs. If SFT achieves similar amplification, the RLHF component is unnecessary and the contribution is overstated. This is a high-leverage experiment that directly tests whether the claimed methodological novelty adds value.

3. **Validate pseudo-labels against ground truth.** Take a small set of generations, verify whether they contain training data (>50-token substring), and compute the correlation between perturbation discrepancy and true membership. Table 1 shows RM accuracy on pseudo-labels; this is not the same as showing pseudo-labels correlate with actual training data presence.

4. **Add an inverted-label control** (RLHF favoring *higher* discrepancy) to test whether the specific direction matters, or whether any training on self-generated data amplifies extraction.

---

## Score and Decision

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>