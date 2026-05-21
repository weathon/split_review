Now I have enough calibration data. Let me write the final review.

## Summary

The paper introduces the Language Confusion Gate (LCG), a lightweight plug-in intervention for mitigating language confusion in multilingual LLMs without modifying the base model. The method is grounded in insightful mechanistic analysis showing that output token embedding norm imbalance biases models toward high-resource languages. LCG trains a small two-layer MLP via norm-adjusted self-distillation to predict allowable language families at each decoding step, dynamically masking disallowed tokens only when needed. Evaluated across five models (Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS) in both standard and thinking modes, LCG reduces confusion by an order of magnitude (e.g., CJ confusion from 4.5% to 0.1% on Qwen3-8B) with negligible overhead (0.4% latency increase) while preserving task performance and legitimate code-switching capabilities.

## Strengths

- **Mechanistic insight grounds the method in a verifiable cause of confusion.** The analysis showing that output token embedding norms for high-resource languages (CJ 10.74%, Latin 4.61%) dominate the top 5% of norms while low-resource languages are severely underrepresented (0.14%) on Qwen3-8B (Table 1) is clean and directly motivates the norm-adjusted self-distillation training. Figure 2 concretely demonstrates that norm-adjustment removes CJ tokens from the top-10 logits at a confusion point, validating the training signal.

- **Order-of-magnitude confusion reduction across diverse models with no task degradation.** Results are consistent and persuasive: on Qwen3-30B, CJ confusion drops from 1.0% to 0.0% and Latin confusion from 4.4% to 0.4% while BLEU increases from 13.2 to 13.4 (Table 3). On Qwen3-8B, CJ confusion drops from 4.5% to 0.1% and Latin from 12.1% to 2.0% with BLEU unchanged at 12.1. The ablation comparing norm-adjusted vs. unadjusted LCG (Table 3) consistently shows the adjusted version outperforms across every model, directly validating the proposed training method.

- **Legitimate code-switching is largely preserved.** The human annotation study showing 86.7% preservation of English tokens at validated code-switch points (Section 5.3) directly addresses the critical challenge of distinguishing erroneous mixing from valid multilingual behavior. Post-intervention code-switch rates on FLORES-WITH-LATIN remain above the Claude Sonnet 4 baseline (e.g., Qwen3-8B: 25.90% vs. 23.29%), demonstrating that the method does not eliminate necessary language blending.

- **Extremely lightweight and practical.** The gate intervenes on only 0.33–0.38% of generated tokens, and the production benchmark shows a 0.4% increase in generation step time (15.95ms to 15.99ms). This is a genuine practical advantage over training-based alternatives.

- **Thorough evaluation scope.** Experiments cover five models across two inference modes (standard and thinking), three benchmarks (FLORES+, INCLUDE, Humaneval-XL), and multiple baselines (ICL, greedy, ORPO, no-rule ablation), demonstrating generalizability.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No statistical significance or variance reported for confusion rates.** The confusion rates are small percentages (e.g., 0.0%, 0.1%, 0.4%), and the paper reports only point estimates from single runs. Given the stochasticity in both gate training and decoding, it is unclear whether the observed reductions are stable across runs. Reporting confidence intervals, standard deviations from multiple seeds, or at minimum acknowledging this limitation would strengthen the claims.

- **ORPO baseline comparison lacks sufficient detail.** The description of the ORPO setup is minimal ("prepare a multilingual dataset, and synthesize samples with language confusion as rejected samples") with no information on dataset size, training steps, hyperparameters, or tuning efforts. This limits the strength of the claim that "LCG outperforms training-based methods." The paper's core contribution does not depend on the ORPO comparison (the ICL, greedy, and no-rule baselines already demonstrate LCG's advantages), so either providing full details or de-emphasizing the ORPO comparison would be appropriate.

- **No direct evaluation of gate accuracy.** The gate is trained to predict language families from hidden states, but the paper never reports metrics like precision, recall, or F1 for the gate's predictions on held-out confusion points. Reporting these would provide a useful diagnostic and help identify failure modes. Additionally, the paper does not discuss the potential circularity where the gate's pseudo-targets are derived from the model's own norm-adjusted logits, which could reflect persistent confusion patterns.

- **Human annotation methodology for code-switch preservation is underspecified.** The 86.7% figure is cited without details on number of annotators, inter-annotator agreement, selection criteria for examples, or how "natural" code-switching was defined. Adding a brief description would improve credibility.

### Trivial

- The caption text in Figure 1 is duplicated (appears twice in the paper).
- Table 4's title incorrectly reads "'No-Think' Models" when describing thinking model experiments (results on Humaneval-XL with reasoning models).

## Nice-to-Haves

- Evaluating on additional low-resource languages (e.g., Tamil, Swahili, Burmese) would further demonstrate generalizability, though the current set (Arabic, Hebrew, Korean, Thai, Greek, Russian, Vietnamese, Chinese) is already reasonable.
- Reporting gate accuracy (language family prediction precision/recall) on held-out confusion points would provide a useful diagnostic.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Evaluation metric for Latin confusion may overcount errors"** — The harsh critic suggests the FLORES-NO-LATIN metric may count proper nouns like "iPhone" as confusion. However, the paper evaluates translation tasks where ground-truth references contain zero Latin characters (translations into Arabic/Hebrew/Korean/Thai from English), so a correct translation should not contain such tokens. Both baselines and LCG are measured under the same detector, so relative comparisons hold. The critic acknowledges this but still presents it as a weakness; it is at most a trivial concern and not a methodological gap.

- **"Potential circularity in pseudo-target generation"** (from "Strengthening the Paper on Its Own Terms") — The harsh critic speculates that pseudo-targets could reflect persistent confusion if the model consistently confuses languages. This is speculative; the empirical results showing strong confusion reduction suggest this is not a practical problem. Removed as an unsubstantiated concern.

- **"Missing parts: evaluation on more low-resource languages like Tamil, Swahili"** — Moved to Nice-to-Haves. The paper already covers 8 target languages across diverse scripts; requesting more is scope creep.

- **Generic strengths from Strength Finder** — Strengths like "Extensive evaluation across five models" and "Superiority over multiple baselines" are duplicative of the concrete strengths already listed. Generic framing like "the paper addressed an important problem" is removed.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation across these reviews is that the norm-adjustment ablation (LCG-adjusted vs. LCG-unadjusted) provides stronger evidence for the paper's core mechanistic claim than any individual confusion-reduction number. Because the only difference between the two conditions is whether the self-distillation targets are debiased via norm-adjustment, the consistent improvement of LCG-adjusted across all models (Table 3: e.g., Latin confusion on Llama3.1-8B drops from 5.7% to 2.9%) directly validates that the norm imbalance identified in Section 3.2 is not just a correlation but causally relevant to confusion behavior. This is a cleaner experimental design than often seen in intervention papers, and the human-review framing of this as "validates the training method derived from mechanistic insight" correctly identifies it as the paper's strongest piece of evidence.

## Suggestions

1. Add a brief "Statistical Significance" section or paragraph reporting confidence intervals for the main confusion rates, ideally from 3 runs with different random seeds for gate training.
2. Either provide full hyperparameter details for the ORPO baseline (dataset size, learning rate, number of steps, tuning procedure) or explicitly de-emphasize the comparison and frame ICL/greedy/no-rule as the primary baselines.
3. Report the gate's own language-family prediction accuracy (precision/recall/F1) on a held-out set of confusion points from the model's own generations, to provide a direct diagnostic of what the gate learns.
4. Add a brief description of the human annotation process for the 86.7% code-switch preservation figure (number of annotators, inter-annotator agreement, example selection criteria).
5. Fix the minor issues: correct the Table 4 caption title, remove the duplicated Figure 1 caption text.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Score | Round | Comparison |
|---|---|---|---|
| Crosslingual Capabilities and Knowledge Barriers (BCyAlMoyx5) | 5.67 (Reject) | R1 | Weaker: studies a well-known phenomenon with methodological issues in model selection; LCG has a novel method and cleaner evaluation |
| Multilingual Code LLM Evolution (eznTVIM3bs) | 5.25 (Accept) | R1 | Weaker: limited to code LLMs, narrower scope; LCG covers more models and has more actionable contributions |
| The Same but Different (NCrFA7dq8T) | 6.60 (Accept) | R1, R2 | Comparable: both well-executed with clear contributions; the mechanistic interpretability paper is more fundamental but limited to 2 languages/2 tasks, while LCG is more applied with broader practical impact |
| MLLM Dynamic Correction Decoding (4z3IguA4Zg) | 6.00 (Accept) | R1 | Comparable: similar structure (analysis → intervention → evaluation); LCG has more thorough evaluation across more models and tasks |
| Constrained Decoding Cross-lingual Label Projection (DayPQKXaQk) | 7.00 (Accept) | R2 | Slightly stronger: cleaner experimental design, broader methodological novelty; LCG is comparable in writing quality and practical impact |
| Fast and Slow Generating (4a9doRh3Jv) | 5.25 (Reject) | R2 | Weaker: less focused contribution, evaluation less thorough |
| Scaling Laws for Multilingual (T2h2V7Rx7q) | 5.25 (Reject) | R2 | Weaker: narrower contribution; LCG has more empirical substance |
| Transform Chat LLMs to Non-English (US2UCMvzvP) | 6.25 (Reject) | R2 | Comparable but narrower scope; LCG has stronger evaluation |
| Self-Distillation Through Time (uZ5K4HeNwd) | 7.00 (Accept) | R2 | Stronger: more ambitious technical contribution, broader implications |
| Unified Representation Space (FrFQpAgnGE) | 7.00 (Accept) | R2 | Stronger: broader scope, deeper analysis of model internals |
| Better Instruction-Following Through MBR (7xCSK9BLPy) | 7.33 (Accept) | R1, R2 | Stronger: cleaner evaluation, broader applicability |

**Round 1 bracket:** 5.5–7.5. The paper is clearly stronger than the 5.25–5.67 Reject-level anchors and competitive with the 6.0–6.6 Accept-level anchors.

**Round 2 narrowing:** The paper sits between the 6.0/6.6 Accepts and the 7.0+ Accepts. It is comparable to the 6.60 mechanistic interpretability paper and the 6.00 decoding intervention paper but a step below the 7.00+ papers in terms of methodological rigor (primarily due to the lack of variance reporting and thin ORPO baseline). Within the Accept quality band, this is a solid mid-to-high paper — not a breakthrough, but a competent, well-motivated contribution with clear practical value.

**Final score:** 6.5 — between the 6.00 (MLLM Decoding) and 6.60 (Same but Different) anchors, closer to the upper end due to the broader evaluation scope and practical applicability.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>