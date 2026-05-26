Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

This paper proposes L-TTA, the first Test-Time Adaptation method designed specifically for Vision-Language Models under long-tailed test distributions. It introduces three co-designed components: Synergistic Prototypes (SyPs combining Deterministic Prototypes and Exclusionary Prototypes), Rebalancing Shortcuts (RSs) for learnable adaptation, and Balanced Entropy Minimization (BEM) as a reweighted entropy objective. The method is evaluated across 15 datasets under three imbalance ratios (10, 20, 50) and shows consistent improvements over 13+ baselines in both accuracy and macro-F1.

## Strengths

1. **First systematic study of long-tailed TTA for VLMs**: Section 1 and Figure 1 identify two failure modes (Text-induced Tail Erosion and Modality-bias Amplification) that are specific to this setting and not addressed by prior balanced-test TTA methods. This problem framing is novel and well-motivated.

2. **Consistent and substantial improvements across extensive benchmarks**: Tables 1–3 show L-TTA outperforms 13+ baselines on 15 datasets under three imbalance ratios, with particularly strong macro-F1 gains (e.g., +1.70% on OOD average at imb=10, +2.20% on cross-domain average). The gains hold across multiple backbones (Table 5, four additional architectures).

3. **Well-designed three-component system with ablation validation**: Table 6 systematically ablates each component (DP, EP, RS, BEM) and shows all contribute synergistically. SyP+RS alone (70.94% Acc) already outperforms all prior methods, and BEM adds a positive increment.

4. **Computational efficiency**: Table 4 shows L-TTA runs in 1.45h with 1.89GB memory on ImageNet, faster than many competing methods (SCAP: 2.96h, RLCF: 18.30h, WATT: 27.70h) while achieving better accuracy and macro-F1.

## Weaknesses

### Major

1. **Missing baseline: TTA with standard logit adjustment**: The paper repeatedly argues that standard logit adjustment or balanced softmax "may further exacerbate the model's bias toward the head classes" (Section 3.2), motivating BEM as a necessary variant. However, the paper **never tests the obvious baseline**—applying standard logit adjustment (or balanced softmax) on top of existing TTA methods (e.g., TPT + LA, DPE + LA). Without this comparison, the claim that BEM solves a problem unique to LT-TTA is unsubstantiated. The ablation (Table 6) shows BEM adds a small improvement over SyP+RS (+0.36% Acc), but whether standard logit adjustment would achieve similar or better gains is unknown. This is the most significant gap in the paper's empirical validation.

### Minor

2. **Exclusionary Prototype (EP) framing is partially misleading**: The paper motivates EPs as storing "the most improbable features of each class" to enrich tail representations. However, the update rule (Eq. 5) uses φ_c = 0 for the predicted class, meaning the feature of the predicted class is incorporated into its own EP with standard EMA weight—this is not "exclusionary" in the literal sense. The actual mechanism benefits tail classes through the prediction-guided weighting across all classes and the subtraction in Eq. 8. The naming is embellished but the underlying mechanism is sound. The authors should reframe the description to accurately reflect the update dynamics.

3. **Inconsistent and ambiguous reporting of hyperparameter K**: The Implementation Details (Section 4) states K = 0.3, while the ablation (Section 4.2) says "setting K = 0.2 yields the best performance." Figure 4c labels it as "b" instead of "K." It is unclear whether K is a discrete count or a ratio, and which value was actually used for main results. This ambiguity damages reproducibility.

4. **Theoretical propositions lack any empirical verification**: Propositions 1 and 2 make mathematical claims about gradient behavior of EM vs. BEM under long-tailed distributions. The paper provides proofs (in appendix) but offers zero empirical diagnostics—no gradient norm plots, no logit histograms, no trace of the optimization gap it claims BEM reduces. The ablation shows BEM is the least impactful component. Empirical verification of the claimed gradient dynamics would substantially strengthen the "theoretically interpretable" claim.

5. **Corruption benchmark in main text is limited**: Table 3 only uses Gaussian noise (with severity variations). While the paper references Appendix J for 16 corruption types, the main text claim of "robust performance on the corruption benchmark" would be better supported by aggregating over all corruption types in the main table.

6. **View count Q (set to 15) is not ablated**: The number of augmented views is a standard sensitivity hyperparameter for TTA methods; its absence weakens the otherwise thorough ablation study.

## Nice-to-Haves

- Ablation on the form of the affinity function A(x) = λ₁·exp(-λ₂(1-x)) in Eq. 8 would strengthen the design justification.
- Quantitative evidence for Failure Mode 2 (SAR on VLM backbone degrading performance) in the main paper rather than only Figure 1.
- Error bars or confidence intervals on main results to assess statistical significance.

## Removed Points

- **"EP mischaracterization undermines the narrative of a core component" (Critic's Critical #1)**: The critic claimed the EP update rule contradicts its stated motivation. While the "exclusionary" label is slightly embellished for the predicted-class case, the update rule (Eq. 5) IS consistent with the stated goal of enriching tail-class representations through prediction-guided cross-class feature aggregation. Features from samples unlikely to be class c receive higher weight in EP_c's update. The mechanism works as intended; only the naming is imprecise. Downgraded from "Critical" to "Minor."

- **"Theoretical propositions are asserted but never validated empirically" (Critic's Critical #3)**: The critic called this a critical issue. However, the paper does provide formal proofs (in appendix), and end-task metrics are the standard validation in this field. The lack of gradient dynamics plots is a reasonable omission for a systems paper. Downgraded to "Minor."

- **"Failure Mode 2 not quantitatively shown" (Section-by-Section)**: The critic demanded quantitative SAR-on-VLM results in the main body. This is a motivation example; the paper's core evaluation is against 13+ VLM baselines, not SAR. Asking for this is scope creep.

- **"Affinity function form not ablated" (Section-by-Section)**: This is a nice-to-have enhancement, not a weakness.

- Various strength-finder sycophancy removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The review corpus does surface a useful perspective: the paper's value lies more in the complete L-TTA system (SyPs + RSs + BEM) than in any single component. The EP and BEM components individually contribute modestly (ablation Table 6), but their synergy with RSs produces the observed gains. The missing baseline issue is the dominant concern.

## Suggestions

1. **Run the missing baseline**: Compare TTA methods (TPT, DPE, SCAP) enhanced with standard logit adjustment (using the same class priors) against L-TTA. If BEM outperforms standard LA, the BEM narrative is strongly validated. If not, the paper should honestly reframe BEM's contribution.
2. **Clarify the EP naming**: Either rename EPs to "complementary prototypes" or "adaptive prototypes" and describe them accurately as accumulating cross-class features weighted by prediction confidence.
3. **Resolve the K inconsistency**: State definitively whether K is a ratio or count, reconcile the 0.3 vs 0.2 discrepancy, and clarify which value was used in main results.
4. **Add gradient diagnostics**: A single figure showing head vs. tail gradient norms during EM vs. BEM for the first few TTA steps would verify Proposition 2 and significantly strengthen the theoretical claim.
5. **Aggregate corruption results**: Show the average over all 16 corruption types in Table 3, with per-type results in appendix.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round & Query | Comparison |
|-----------|-----------|---------------|-----------|
| pdzHpQbGrn | 2.50 | R1-topic-low | Fundamentally flawed; our paper is much stronger |
| JIlIYIHMuv | 2.50 | R1-topic-low | Fundamentally flawed; our paper is much stronger |
| b20VK2GnSs | 7.00 | R1-topic-mid | Concept drift for MLLMs; our paper is weaker (cleaner method but less theoretical depth) |
| BUDxvMRkc4 | 4.67 | R1-topic-mid / R2 | Long-tailed CLIP classification; our paper addresses harder problem with more experiments |
| lF9QXpfNHm | 4.67 | R1-topic-mid | Open-world TTA for VLMs; our paper has stronger methodology and more components |
| yD2JMeKumt | 6.00 | R1-weakness (missing baseline) | DOTA: distributional TTA for VLMs; comparable quality but our method is clearer |
| 75PhjtbBdr | 6.25 | R2 | Multi-label BEM; comparable quality, cleaner narrative but narrower scope |
| 3Z2flzXzBY | 6.40 | R2 | PASLE: selective label TTA; our experiments are more extensive |
| eXrUdcxfCw | 4.80 | R2 | Continual TTA with prototypes; our method is more novel |
| NeVbEYW4tp | 5.00 | R2 | Efficient TPT; our paper has stronger results |

**Round-1 bracket**: [4.5, 6.5]. The low-band (<3.5) anchors share no common failure modes with our paper—they are fundamentally flawed in ways our paper is not. The middle-band anchors (4.4–7.0) span reject to accept and our paper sits among them.

**Round-2 narrowing**: Queries within (4.5, 6.0) and (5.0, 6.5) confirmed the bracket. Our paper is clearly stronger than the 4.67–5.00 rejects (better methodology, more experiments) and comparable to the 5.67–6.25 papers. It is weaker than the 7.00 accept paper (which has cleaner narrative and stronger theoretical framing).

**What low-band anchors failed at**: The 2.33–2.50 papers had fundamental issues: incomplete methods, poor experimental design, or disconnected contributions. Our paper shares none of these failures.

**Final score position**: The paper sits between the 4.67–5.00 reject cluster (which it clearly outperforms) and the 6.25–7.00 accept cluster (which it falls short of due to the missing baseline gap). The missing baseline is a significant weakness that prevents the paper from being a clear accept but does not invalidate its overall contribution.

**My final score**: 5.5

The paper introduces a novel problem and a well-designed system with extensive empirical validation. However, the missing baseline for BEM (the central loss function) is a significant gap that weakens a core narrative claim and would need to be addressed before acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>