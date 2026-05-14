Now I have a thorough understanding of the paper and its calibration context. Let me compose the final review.

---

## Summary

This paper identifies and quantifies the "underthinking" phenomenon in LongCoT LLMs—where models prematurely switch between reasoning paths without fully exploring promising ones—and proposes SmartSwitch, a training-free, plug-and-play inference framework. SmartSwitch uses linguistic cues to detect thought switches, evaluates abandoned thoughts with an off-the-shelf process reward model (PRM), and injects a deepening prompt to encourage further exploration when a high-potential thought is prematurely discarded. Evaluated across five models (1.5B–32B) on five math benchmarks, SmartSwitch consistently improves accuracy (up to +23.3 points on AIME25) while simultaneously reducing inference time and response length.

## Strengths

- **Consistent, training-free accuracy gains across diverse models and benchmarks.** Table 1 demonstrates pass@1 accuracy improvements for all five models (DeepSeek-R1-Distill-Qwen 1.5B/7B/14B/32B and QwQ-32B) across all five benchmarks (AIME24, AIME25, AMC23, MATH-500, GaoKao2023en). Gains range from +0.6 to +23.3 points, with the strongest model (QwQ-32B) still gaining +7.2 points on AIME24. The plug-and-play, fine-tuning-free design makes the method broadly applicable.

- **Efficiency improvements alongside accuracy gains.** Despite explicitly encouraging deeper exploration, SmartSwitch reduces both average response length (Table 2, e.g., −14.2% for the 32B model on AIME24) and wall-clock inference time (Table 3, e.g., −19.7% for the same model). These gains include all PRM scoring and intervention overhead, demonstrating that selective deepening prunes wasteful exploration rather than merely inflating compute.

- **Well-motivated problem characterization.** The paper provides a concrete, quantitative operationalization of underthinking (UF metric, Eq. 1) and demonstrates its prevalence across six LongCoT models (Figure 1b), its correlation with problem difficulty (Figure 2a), and its association with incorrect answers (Figure 2b). SmartSwitch is shown to reduce both the UF metric and the raw number of thought switches (Figure 4), directly linking the mechanism to mitigated underthinking.

- **Thorough ablation studies.** The paper systematically ablates the PRM choice (Table 4, including an "Always Intervene" baseline that degrades performance to 18.9%, confirming the value of selective intervention), process division strategy (Table 6, four variants across five models), score-mapping policy (Table 7), and score threshold (Table 8). The ablations are well-conceived and provide practical guidance.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Comparison with existing underthinking mitigation method (TIP) is limited to a single model and benchmark.** Table 5 compares SmartSwitch against TIP only on DeepSeek-R1-Distill-Qwen-1.5B on AIME24. While the gain is substantial (40.0% vs. 31.3%), demonstrating consistent superiority across additional model scales or benchmarks would strengthen the claim that SmartSwitch is the preferred approach. This is addressable in rebuttal.

- **Threshold tuning conducted directly on test benchmarks.** Table 8 shows threshold sensitivity on AIME24, and the same threshold (0.70) is used for all other benchmarks. While the fact that a single threshold works across all five models is itself evidence of robustness, the paper provides no evidence that this value was selected via held-out validation rather than by maximizing AIME24 performance. This raises a mild concern about whether reported gains on AIME24 are partially inflated by hyperparameter tuning on the test set. The gains on other benchmarks (AIME25, AMC23, etc.) are less affected by this concern since the threshold was fixed before evaluating them.

- **Underthinking metric is heuristic and not validated against ground-truth reasoning quality.** The UF metric (Eq. 1) classifies any thought shorter than L tokens as underthinking, which conflates concise-but-complete reasoning with genuinely shallow exploration. The paper acknowledges this implicitly by treating the metric as a descriptive tool rather than a gold standard, but this limitation should be stated more explicitly when interpreting Figures 1–2.

### Trivial

- The paper reports "significant" improvements in the abstract and main text but does not provide formal statistical tests. This is a wording issue—"substantial" or "consistent" would be more precise than "significant" without accompanying statistical evidence.

- The causal mechanism for efficiency gains ("prunes wasteful reasoning on less fruitful thoughts") is stated as an interpretation (Section 5.3) but could be supported more directly, e.g., by analyzing where token savings occur in the reasoning trace.

## Nice-to-Haves

- Confidence intervals or bootstrapped standard errors for accuracy estimates on the smaller benchmarks (AIME24: 15 problems, AIME25: 15 problems, AMC23: 25 problems) would increase reader confidence in the reliability of reported gains. However, reporting point estimates without error bars on these competition benchmarks is standard practice in this subfield, so this is not a weakness per se.

- A held-out validation procedure for hyperparameter selection (e.g., splitting MATH-500 into tuning/evaluation halves) would formally rule out concerns about test-set overfitting and is straightforward to implement.

- Expanding the TIP comparison to at least one additional model scale and benchmark would make the comparative claim more robust.

- Reporting PRM score distributions for thoughts that lead to correct vs. incorrect final answers would validate the core assumption that higher PRM scores correlate with eventual success.

- A side-by-side case study showing a full reasoning trace with and without SmartSwitch intervention, annotated with switch detection points and PRM scores, would make the mechanism more concrete for readers.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim: "The main results lack statistical rigor, rendering the claimed improvements unreliable."** → **Demoted to Nice-to-Have.** Reporting point estimates without confidence intervals on small benchmarks like AIME is standard practice across this subfield. None of the human-reviewed anchor papers (e.g., Think-with-Me at 4.00, OptimalThinkingBench at 5.33, Hop Generalization at 5.50) were criticized for lacking confidence intervals on AIME-scale benchmarks. The 32-response averaging per problem provides a reasonable point estimate. The paper would benefit from error bars but their absence does not invalidate the results.

- **Harsh Critic claim: "Extreme sensitivity of the score threshold... strongly suggest overfitting."** → **Demoted to Minor.** The harsh critic claims that moving threshold from 0.70 to 0.71 drops accuracy by 10 points, implying knife-edge sensitivity. But Table 8 tests the threshold across all five models simultaneously, and 0.70 is the best for all of them. This is evidence of a genuine optimal region, not random overfitting to one model. Additionally, 0.70 outperforms vanilla for all models, and even the worst thresholds (0.68, 0.69, 0.71) match or slightly exceed vanilla for some models. The valid concern—tuning on the test set—is already captured in the Minor weaknesses above with proportionate severity.

- **Harsh Critic claim: "Short thoughts can be logically complete and appropriate" (re: UF metric).** → The paper uses UF as a descriptive heuristic, not as a ground-truth label. This is already noted as a Minor weakness with appropriate framing.

- **Strength Finder claim: "SmartSwitch substantially surpasses the token-suppression method TIP"** → **Retained but contextualized.** The TIP comparison is real and favorable but limited in scope, as noted in Minor weaknesses above.

## Novel Insights

The paper's most novel empirical insight is the dual benefit of selective PRM-guided deepening: it simultaneously improves accuracy AND reduces inference cost. This is counterintuitive (one might expect deeper exploration to cost more tokens) and suggests that SmartSwitch effectively prunes unproductive exploration—the model spends fewer total tokens because it stops fruitlessly switching and instead commits to promising paths. The "Always Intervene" ablation (18.9%, below the 20.0% vanilla baseline) elegantly demonstrates that indiscriminate deepening is harmful, making the PRM's role in selectivity clear. This finding has implications beyond this paper: it suggests that the quality of reasoning exploration matters more than its quantity, and that external quality signals can guide more efficient compute allocation at inference time.

## Suggestions

- The simplest and most impactful improvement would be to select the score threshold via cross-validation on a held-out portion of MATH-500 (or another dataset not used for final evaluation) and report all benchmark results with that fixed threshold. This directly addresses the test-set tuning concern and is achievable in rebuttal.

- Expand the TIP comparison minimally—even adding one additional model (e.g., the 7B variant) on AIME24 would substantially strengthen the comparative claim.

- Replace "significantly enhances" with "substantially/consistently improves" throughout to avoid implying formal statistical testing that was not performed.

- Add a note in Section 3.2 clarifying that UF is a descriptive heuristic that correlates with but does not perfectly capture reasoning depth, so readers do not over-interpret the metric.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/89RGVbULYt.md` (Think-with-Me) | 4.00 | Reject | SmartSwitch is training-free vs. requiring GRPO fine-tuning, has broader experiments (5 models × 5 benchmarks vs. limited evaluation), and demonstrates efficiency gains alongside accuracy. SmartSwitch is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/PVooP3d7cI.md` (Price of a Second Thought) | 3.50 | Withdrawn | SmartSwitch has a more concrete mechanism (PRM-guided intervention vs. two-stage prompting) and stronger empirical results. SmartSwitch is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/N5kWa3sRJt.md` (OptimalThinkingBench) | 5.33 | Accept (Poster) | Both address underthinking; OptimalThinkingBench is a benchmark, SmartSwitch is a method. SmartSwitch's empirical contribution is comparably solid (systematic ablations, diverse evaluation). Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/qK4JKOu0Gx.md` (Hop Generalization) | 5.50 | Accept (Poster) | Hop Generalization has deeper mechanistic analysis; SmartSwitch has broader practical applicability. Roughly comparable overall contribution level. |
| `/home/wg25r/review_agent/human_reviews_2026/KBknLdXxTa.md` (CORE-MATH) | 5.50 | Accept (Poster) | CORE-MATH evaluates 61 models with rigorous benchmark construction. SmartSwitch has a more novel method but less exhaustive evaluation. Roughly comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/aQZIpELFwp.md` (Are Reasoning LLMs Robust) | 4.50 | Accept (Poster) | Both are intervention studies on reasoning LLMs. SmartSwitch has more practical impact (actual performance gains rather than robustness measurement). SmartSwitch is somewhat stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/ae6bKeffGZ.md` (Arithmetic-Bench) | 2.50 | Reject | SmartSwitch is substantially stronger across all dimensions. |
| `/home/wg25r/review_agent/human_reviews_2026/ZZAIF9fjlU.md` (ProofRM) | 4.50 | Reject | Different focus; SmartSwitch has a more complete methods+evaluation package. SmartSwitch is somewhat stronger. |

The paper proposes a practical, well-motivated, and carefully ablated inference-time intervention. Its key weaknesses—limited TIP comparison, threshold tuned on test benchmarks, and heuristic underthinking metric—are real but moderate in severity and largely addressable. The core contribution (training-free PRM-guided selective deepening that improves both accuracy and efficiency) is solid and supported by consistent evidence across models and benchmarks. Compared to anchors, this paper sits in the Accept (Poster) range, comparable to the 5.33–5.50 anchor papers in contribution quality, but somewhat below them in evaluation rigor. I assign a score of **5.0**.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>