I have thoroughly read and cross-checked the paper against all reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes a causality-guided debiasing framework for LLMs that models how social biases influence decisions through different causal pathways (Figure 3). From this framework, the authors derive three principled prompting strategies: (I) nudging toward social-agnostic facts, (II) counteracting existing selection bias by assuming equal representation, and (III) nudging away from social-salient text. They propose Dual Directional Prompting (DDP) that combines these strategies and evaluate it on WinoBias, BBQ, and Discrim-Eval across GPT-3/3.5/4 and Claude 2. DDP achieves substantially reduced bias gaps — e.g., GPT-4 achieving only a 2.17% gap on WinoBias Type I — and outperforms ICL with contrastive examples on 8 of 9 BBQ social categories.

## Strengths

- **Novel causal formalization grounding prompt design in principled objectives.** The paper introduces a causal graph (Figure 3) that explicitly models selection mechanisms in training data and distinguishes three causal pathways through which social category information can influence LLM decisions. This yields formal conditional-independence objectives (Equations 1–3) that go beyond ad-hoc prompting and provide a theoretical vocabulary for designing and comparing debiasing strategies. The paper acknowledges that internal representations are "not directly observable or accessible" (Section 3.2), situating the graph as a modeling framework rather than a falsifiable mechanistic claim.

- **Strong empirical results across multiple models and benchmarks.** DDP achieves near-negligible bias gaps on WinoBias (GPT-4: 2.17% on Type I, 0.13% on Type II), substantially outperforming baselines including ICL with contrastive examples (best baseline gap: 9.23%). On BBQ, DDP achieves the highest accuracy on 8 of 9 social categories, with notable gains on subtle bias dimensions such as physical appearance and socioeconomic status. Improvements hold across GPT-3, GPT-3.5, GPT-4, and Claude 2.

- **Insightful ablation analysis (TT/TF/FT/FF categorization).** Table 2 attributes DDP's gains to correctly leveraging gender-agnostic world knowledge (TT group) and reducing cases where bias overrides correct knowledge (TF group). Fact Only performs well while Counteract Only degrades performance, revealing that fact-based reasoning is the primary driver — a finding that usefully guides future prompt design.

- **Practical applicability to black-box LLMs.** The entire framework operates through prompting alone, requiring no parameter access. DDP is demonstrated on GPT-4, GPT-3.5, and Claude 2 — closed-source models where fine-tuning and internal probing are infeasible.

## Weaknesses

### Fatal

None.

### Major

- **Gap between the causal claims and what is empirically verified.** The paper frames itself as "causality-guided" and "principled," with a "Theorem 3.1" proving that bias can be "completely removed" when the three strategies' objectives are satisfied. However, the proof assumes the conditional-independence conditions (Equations 1–3) hold over internal representations — conditions that are never measured or verified, and which the authors themselves note are "not directly observable or accessible." The link between each prompt strategy and its corresponding formal objective is asserted via intuitive correspondence (e.g., "Assume male and female are equally represented" ↔ Strategy II's conditional independence) but never formally derived or empirically validated at the representation level. A reduction in accuracy gap does not validate the causal graph. This does not invalidate the paper's empirical contribution — DDP clearly works — but it means the theoretical apparatus functions as a design metaphor rather than a testable causal theory. The paper would be stronger if it either (a) provided probing evidence that the prompts change internal representation dependencies as predicted, or (b) lowered its theoretical ambitions and presented the framework as an organizational taxonomy for prompt design.

- **Baselines are reasonable but not exhaustive.** The paper compares against Default, Zero-shot COT, and ICL with contrastive examples. While ICL subsumes counterfactual prompting (Oba et al., 2023, cited as similar), and Zero-shot COT relates to fairness-focused COT (Ganguli et al., 2023, cited as similar), neither of these specific methods is directly implemented. Direct comparison with targeted fairness instructions (e.g., "Please ensure your answer does not rely on stereotypes") or with more recent prompting-based debiasing methods would better isolate whether the advantage comes from the causal framing or simply from providing more information/harder reasoning steps. Additionally, no variance or statistical significance is reported for any experiment.

### Minor

- **The "unification" claim is stated but not substantiated.** The abstract and conclusion claim the framework "unifies existing prompting-based debiasing techniques," but no explicit mapping is provided. The paper does not show, e.g., how Zero-shot COT instantiates Strategy I, II, or III, or how ICL corresponds to the framework. The unification is asserted rather than demonstrated, weakening what would be a valuable organizational contribution.

- **BBQ evaluation is limited to the disambiguated setting.** The paper tests only the disambiguated BBQ setting where contexts are informative and the answer is one of two entities. Bias often manifests more strongly in ambiguous contexts where the correct answer is "unknown." Evaluating the ambiguous setting would provide a fuller picture of the method's robustness.

- **The label "Theorem 3.1" overstates the result.** The "proof" is a brief structural argument (four sentences) that says: if the two parents of Y are independent of A, then Y ⟂ A follows. This is a graph-theoretic observation, not a mathematical theorem in the usual sense. Overclaiming the formality of the result may mislead readers about the strength of the theoretical contribution.

- **No analysis of failure cases or qualitative examples.** The paper lacks case studies showing where DDP helps and, just as importantly, where it hurts or introduces errors. A few representative examples would help interpret the accuracy numbers.

### Trivial

None that are not parser artifacts.

## Nice-to-Haves

- Probing analysis (e.g., measuring whether internal gender representations shift under different prompts) would substantiate the causal claims but is outside the paper's stated scope of black-box access. If probing is feasible for some models, it would significantly strengthen the paper.
- Testing a control condition that directly provides the correct base-answer (without asking the model to generate it) would disentangle whether DDP's gains come from the *process* of answering the base question or the *content* of the answer.
- Reporting variance across multiple runs or prompt phrasings would strengthen empirical rigor.
- Testing on additional models (e.g., Llama, Gemini) on the BBQ benchmark would demonstrate generality beyond GPT-4.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"The medical example is disconnected from the NLP setting... without any demonstration."** — The paper explicitly says "We will see in Section 3 that such property of selection also applies to NLP contexts" (line 65), and Section 3.1 directly applies the selection framework to NLP training data. The criticism ignores the forward reference.

2. **"The 'ideally diverse and comprehensive' imaginary corpus is not operationalized."** — This is a standard counterfactual construct in causal inference about selection bias, used to explain how stereotypes arise in training data. It is not meant to be operationalized.

3. **"Edges in Figure 3(a) are asserted without justification."** — Edges in causal graphs are always asserted based on domain knowledge assumptions. This is standard practice in causal modeling. The paper provides textual justification for each edge.

4. **"The input prompt directly changes PPC... is an unsupported leap."** — The paper explicitly models this as a selection mechanism (Section 3.2, lines 100–101) and acknowledges it is a modeling choice. Causal graphs are constructed from domain assumptions; the paper's assumptions are clearly stated.

5. **"Future work about reward models is speculative."** — Future work is inherently speculative. Criticizing it as disconnected from the paper's contribution is a style nitpick.

6. **"Self-debiasing (Schick et al., 2021) is a missing baseline."** — Self-debiasing requires access to output logits or modified decoding, which is incompatible with the paper's black-box prompting setting.

7. **"Si et al. 2022 use 32 ICL examples"** — The paper uses the same 16 ICL examples as Si et al. (2022) for WinoBias, consistent with the cited work's setting. The 8-shot BBQ setting also follows Si et al. (2022).

8. **Generic strengths from the Strength Finder** (e.g., "The problem is important and timely," "The paper is clearly written") — These are dropped as they lack specific, citable content and do not distinguish this paper.

## Novel Insights

The most notable insight that emerges across the reviews is that the paper's empirical contribution — DDP's strong bias reduction — is more robust than its theoretical framing. The ablation analysis (TT/TF/FT/FT) revealing that fact-based reasoning (Strategy I) drives performance while counteracting bias (Strategy II) alone degrades accuracy is itself a non-obvious finding: it suggests that encouraging better knowledge use is more effective than directly suppressing biased reasoning for these benchmarks. This finding is independent of the causal graph and could guide practical debiasing even for readers who set aside the theoretical framework entirely. Conversely, the reviews surface a genuine tension: the paper needs the causal framework to differentiate itself from "just another prompting trick," but the framework cannot be verified at the level of internal representations without probing — which the black-box setting prohibits. This tension is inherent to the paper's design and is not resolved.

## Suggestions

1. **Reframe the theoretical contribution.** Either (a) add probing experiments on open models to verify that the prompts affect internal representation dependencies as predicted, or (b) lower the theoretical register — treat the causal graph as a design metaphor/taxonomy rather than a testable theory, and drop the "Theorem" label in favor of a "structural observation" or "sufficient condition." The empirical results are strong enough to stand on their own.

2. **Add stronger baselines** — at minimum, implement direct fairness instructions ("Please do not use stereotypes") and, if possible, replicate the specific prompting methods from Oba et al. (2023) and Ganguli et al. (2023) rather than citing them as "similar."

3. **Provide an explicit mapping table** showing how prior prompting-based debiasing methods instantiate each strategy (or combinations thereof). This would substantiate the unification claim and make the paper a more useful reference.

4. **Report variance** across at least 3 random seeds or prompt phrasings, and include a statistical significance test (e.g., McNemar's) for the key DDP-vs-ICL comparison.

5. **Add a qualitative analysis** — 3–5 representative examples where DDP succeeds (especially on subtle bias categories like socioeconomic status) and, critically, 1–2 failure cases or cases where accuracy drops.

## Score and Decision

The paper makes a solid empirical contribution — DDP is an effective prompting strategy for reducing bias in LLMs, evaluated across multiple models and benchmarks with strong results. The causal framework, while overclaimed in its current presentation, provides a useful conceptual vocabulary for organizing prompting strategies. The main weaknesses are the gap between the theoretical framing and what is actually verified, the lack of stronger baselines, and the overstated "Theorem."

These are addressable weaknesses. The empirical core is sound and the practical contribution is significant — DDP clearly works better than alternatives on these benchmarks.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>