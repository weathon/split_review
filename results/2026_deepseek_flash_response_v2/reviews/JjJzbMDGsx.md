## Summary

This paper introduces the Language Confusion Gate (LCG), a lightweight two-layer MLP that plugs into any LLM at decoding time to dynamically mask tokens from unintended language families, trained via norm-adjusted self-distillation. The paper provides a mechanistic analysis showing that output token embedding norm bias favors high-resource languages, and uses this insight to create better training signals. Evaluated across 5 models (Qwen3-30B, Qwen3-8B, Llama3.1-8B, Gemma3-12B, GPT-OSS) on FLORES+ and INCLUDE benchmarks, LCG reduces language confusion by roughly an order of magnitude (e.g., Qwen3-8B CJ% from 4.5% to 0.1%) while maintaining task performance with only 0.4% overhead.

## Strengths

- **Mechanistic identification of output token embedding norm bias as a cause of language confusion**: The paper decomposes logits geometrically (Eq. 3) and empirically shows in Table 1 that tokens from high-resource languages (CJ, Latin) disproportionately occupy the top 5% of embedding norms while low-resource tokens are severely underrepresented (e.g., 0.14% in Qwen3-8B). Figure 2 demonstrates that norm-adjusted logits remove CJ tokens from the top-10. This finding directly informs the training signal and goes beyond prior work that identified confusion points without isolating this mechanism.

- **Norm-adjusted self-distillation outperforms unadjusted self-distillation**: The ablation in Table 3 shows consistent gains — e.g., Llama3.1-8B Latin% drops from 5.7% (LCG-unadjusted) to 2.9% (LCG-adjusted) and Qwen3-30B Latin% from 0.7% to 0.4% — demonstrating that the norm-adjustment component adds clear value beyond standard self-distillation.

- **Quantified minimal overhead**: The paper provides direct runtime measurements: 15.95ms per generation step without LCG vs. 15.99ms with LCG (0.4% overhead), and reports a sparse intervention rate of 0.33–0.38% of tokens. This concrete evidence supports the plug-in design claim.

- **Preserves task performance while reducing confusion by an order of magnitude across diverse architectures**: Evaluation covers 5 models (both standard and reasoning modes) across FLORES+ and INCLUDE benchmarks. Confusion drops substantially while BLEU/accuracy remain stable or slightly improve.

- **Explicit handling of legitimate code-switching with human-validated preservation**: The paper evaluates on FLORES-WITH-LATIN, reports that LCG allows English code-switch tokens at 86.7% of human-validated confusion points, and measures code-switch rate changes. This shows the method distinguishes erroneous confusion from acceptable mixing.

- **Identifies a critical failure mode of ORPO that LCG avoids**: Figure 3 shows ORPO reduces INCLUDE accuracy from 61.4 to 57.3 on Qwen3-8B while LCG preserves accuracy, an important finding for practitioners considering training-based interventions.

## Weaknesses

### Fatal
None.

### Major

- **Missing empirical comparison against directly related inference-time methods**: The Related Work discusses Nie et al. (2025), who suppress language-switching neurons during inference, and Ji et al. (2025), who propose post-hoc smoothing for suppressing Chinese tokens during decoding. These are the closest existing methods to LCG — they operate at inference time, target the same problem, and face the same challenge of distinguishing confusion from legitimate code-switching. Yet the experimental comparison (Figure 3) includes only ICL, greedy decoding, and a self-implemented ORPO baseline. Without comparison against these directly relevant inference-time methods, the paper's claim to advance beyond existing work is not fully substantiated.

- **No explicit statement that FLORES+ evaluation data is disjoint from training data**: The paper trains LCG on a dataset that includes "FLORES+ Dataset... to generate translation pairs" (Section 5.1) and evaluates on "FLORES+" (Section 5.2), partitioned into FLORES-NO-LATIN and FLORES-WITH-LATIN. The paper never states that the evaluation split is disjoint from the training split. If the same FLORES+ samples were used in both training and evaluation, the measured confusion reduction could be inflated. This needs explicit clarification.

- **No measures of uncertainty or statistical significance**: Every result — confusion rates, BLEU scores, accuracy, Pass@1/Pass@10 — is reported as a single point estimate with no confidence intervals, standard deviations, or significance tests. Confusion rates are often low (0–12%), meaning the absolute number of confused responses per condition is small. Without variance estimates, the reader cannot judge whether reported improvements are consistent or due to sampling noise. This is especially consequential for small differences (e.g., Table 4: Pass@1 drop from 83.81 to 83.13 where the paper claims performance is "maintained").

### Minor

- **Gate's own precision/recall not reported**: The paper reports confusion reduction but never reports the gate's accuracy, precision, or recall at the token or step level. Metrics like how often the gate predicts the wrong language family, or how often Rule 2 fires because the gate's prediction conflicts with high-confidence model output, would help assess whether the gate is learning the right signal.

- **Training hyperparameters underspecified**: The paper does not report the 2-layer MLP's hidden dimension, learning rate, batch size, optimization algorithm, number of training steps, or validation criteria in the main text. While some of these may appear in the appendix, they are essential for reproducibility.

- **Token classification validation not described**: The paper classifies 151k+ vocabulary tokens into language families using a heuristic (Section 4.1). The accuracy of this mapping is not validated or reported (e.g., manual spot-checks), which is relevant since the entire gate depends on this mapping.

### Trivial
None.

## Nice-to-Haves
- Reporting how often each intervention rule (Section 4.3) fires during evaluation would help interpret the method's behavior.
- Estimating how many FLORES-NO-LATIN examples might have legitimate Latin-character uses that the ground-truth reference simply doesn't include would strengthen the evaluation design.

## Removed Points
- Criticism about Equation (3) being a standard dot product decomposition: The paper is transparent about this and frames it as a "critical, often-overlooked factor," not a novel derivation. This characterization is accurate.
- Criticism about code-switch reduction from 46.34% to 25.90% having weak justification: The paper provides human-validated preservation (86.7% at confusion points), acknowledges the reduction, and compares against multiple baselines. The treatment is appropriate and the paper explicitly notes the baselines "are just references for comparison but not a ground truth optimal code-switch rate."
- Criticism about Claude Sonnet 4 potentially under-code-switching: This is speculative. The paper already caveats its baselines appropriately.
- Criticism about "Large Reasoning Models seem to reintroduce the problem" being an overclaim: The paper attributes this to prior work (Guo et al., Wang et al.) and evaluates on thinking models. This is appropriately supported.
- Pure formatting/style nitpicks, reproducibility nitpicks about appendix content (which the parser strips), and speculation about unreleased references are excluded per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The most novel aspects are already clearly articulated by the paper: the identification of token embedding norm bias as a mechanistic cause of language confusion, and the use of norm-adjusted self-distillation to train a lightweight gate that distinguishes confusion from legitimate code-switching.

## Suggestions
1. Add a comparison against at least one directly related inference-time baseline (e.g., implementing the neuron suppression approach of Nie et al. 2025 or the post-hoc smoothing of Ji et al. 2025 on the same models and benchmarks).
2. Explicitly state whether the FLORES+ evaluation split is disjoint from the training split, and if so, describe how the split was made.
3. Add confidence intervals or bootstrapped standard deviations for all main metrics, especially confusion rates and Pass@k scores.
4. Report the gate's own accuracy/precision/recall at the token level, and report how often each intervention rule fires.
5. Provide training hyperparameters (hidden dimension, learning rate, batch size, optimization, validation criteria) for the gate MLP.

## Calibration

**Round 1 — Bracketing**: Searched weak (score ≤3.5), middle (3.5–7.5), and strong (≥7.5) bands for similar topics (multilingual LLM decoding interventions, norm/embedding analysis, self-distillation). Weak band returned papers averaging ~3.0 (mostly rejected with significant flaws). Middle band returned papers averaging 5.25–6.67. Strong band returned papers averaging 8.0 (top-tier work on different topics like retrieval heads and training stability). Plausible bracket: **4.0–7.5**.

**Round 2 — Narrowing**: Searched within (5.5–7.0) and (6.0–7.5) for more targeted anchors. Read 5 anchors in full:

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| Crosslingual Knowledge Barriers (Reject) | 5.67 | R1 | Weaker — descriptive study with limited novelty; our paper has a concrete novel method and broader evaluation |
| DeCo Hallucination Mitigation (Accept) | 6.00 | R2 | Comparable — similar analysis→intervention structure, similar evaluation gaps; our method is cleaner |
| TransLLM (Reject) | 6.25 | R1 | Our paper is more original (mechanistic insight + clean method vs. engineering pipeline) |
| EmbedLLM (Accept) | 6.67 | R2 | Comparable — different domains; our presentation is clearer but EmbedLLM has broader experiments |
| Scaling Laws Multilingual (Reject) | 5.25 | R1 | Weaker — minimal practical improvement; our paper has stronger empirical results |

**Final score determination**: The paper is clearly stronger than the 5.25–5.67 rejected papers. It is comparable to the DeCo paper at 6.00 and slightly below EmbedLLM at 6.67. The missing comparison against directly related inference-time methods (Nie et al., Ji et al.) is a genuine gap that prevents a higher score. **Score: 6.0**.

<score>6.0</score>
<decision>Accept</decision>