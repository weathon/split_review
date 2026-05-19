- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes DSN (Don't Say No), a jailbreak attack that combines two loss objectives: (1) maximizing the probability of affirmative responses with a Cosine Decay weight schedule to mitigate the "token shift" problem, and (2) suppressing refusal responses via Unlikelihood loss. The paper also introduces an Ensemble Evaluation pipeline that integrates NLI contradiction scoring with HarmBench and GPT-4 evaluators through majority voting. Experiments across five model families and three datasets show DSN consistently outperforms vanilla GCG and AutoDAN baselines, with demonstrated transferability to gpt-3.5-turbo and minimal computational overhead (0.77% increase).

## Strengths

1. **Principled refusal-suppression objective.** The paper identifies that refusal responses are more constrained and predictable than harmful responses, and formulates a loss that explicitly minimizes the probability of refusal tokens rather than only maximizing affirmative tokens. This is a genuine conceptual departure from prior GCG-style attacks. Evidence: Section 4.1 describes the intuition, Equation (2)–(3) define the Unlikelihood loss, and Figure 4 shows that the DSN loss (with Cosine Decay) produces suffixes whose loss correlates with ASR, whereas the vanilla GCG loss does not.

2. **Consistent empirical outperformance across diverse settings.** DSN outperforms GCG in 29 out of 30 settings across five model families (Llama-2, Llama-3, Llama-3.1, Qwen2, Gemma2) and three datasets (AdvBench, JailbreakBench, MaliciousInstruct) under both Refusal Matching and HarmBench metrics (Table 6, line 601–605). The improvement is particularly notable for well-aligned models like Llama-2-13B (24% → 38% under Refusal Matching, 53% → 64% under HarmBench).

3. **General applicability of DSN loss beyond GCG.** The DSN loss is successfully applied to AutoDAN by replacing its target loss, yielding higher ASR on Vicuna-7B and Mistral-7B (Figures 8–9, lines 456–472). This demonstrates the loss function is not tied to the GCG optimizer.

4. **Ensemble Evaluation with explicit handling of semantic contradictions.** The NLI-based contradiction detection (Algorithm 1) addresses known failure modes of Refusal Matching — including semantic shifts where a response starts affirmatively but later refuses (Table 2). The ensemble achieves the best Accuracy (0.82) and F1 (0.86) among all individual components on human-annotated data (Table 4, line 560–577). Shapley value analysis confirms NLI is the highest-contributing component (0.176, Table 5), validating its design.

5. **Negligible computational overhead.** DSN adds only 0.77% runtime compared to GCG (line 663), making it practical to deploy.

## Weaknesses

### Fatal
None. The paper's core claims are supported by the evidence presented.

### Major

- **The claim that Cosine Decay alone mitigates token shift is not fully isolated from the refusal suppression term.** The primary evidence for Cosine Decay's effectiveness (Section 4.2, line 421, Figure 4) compares the *full* DSN loss (Cosine Decay + refusal suppression) against vanilla GCG. The α=0 ablation does exist and isolates Cosine Decay (line 543: "None represents the DSN attack with Cosine Decay and α=0"), but this ablation is presented in a separate section (Figures 6, 9, 10) and is not referenced when the Cosine Decay claim is made. Moreover, on Vicuna under the JailbreakBench metric, the α=0 condition appears to underperform GCG (Figure 6b — the exact numbers cannot be verified from text alone, but the paper's own claim of "consistently outperforms...across all hyperparameter selections" may not hold for the α=0 point on this model/metric combination). The paper should directly compare (a) GCG, (b) GCG + Cosine Decay only (α=0), and (c) full DSN in the same Figure 4-style experiment to cleanly attribute improvements to each component.

### Minor

- **Refusal loss formulation is under-specified for multi-token keywords.** Equation (4) defines \(\mathcal{L}_{\text{refusal}} = \sum_{y \in \text{RKL}} \sum_i \mathcal{L}_{\text{Un}}(y, x_{i:i+\text{RTL}(y)})\), but \(\mathcal{L}_{\text{Un}}\) (Equation 2) was defined for probability distributions \(p, q\). It is unclear how the Unlikelihood loss is computed for multi-token keywords like "sorry, i cannot" — as a product over tokens, an average, or some other aggregation. The refusal keyword list (line 196) is also described only with example strings; a complete list would aid reproducibility.

- **No experimental comparison against attacks that also address token shift.** The paper cites AmpleGCG (liao2024amplegcg) as having identified the token shift phenomenon, and lists it and AdvPrompter (paulus2024advprompter) in related work (lines 44, 116), but does not include them as baselines. Since these methods also improve upon GCG's optimization, it is unclear whether DSN's gains are additional or overlapping. This is the most impactful missing comparison.

- **The Ensemble's AUROC (0.79) is marginally lower than NLI alone (0.80).** While the ensemble improves Accuracy (0.82 vs. 0.80) and F1 (0.86 vs. 0.81), the 0.01 AUROC drop is not discussed. The Shapley values show NLI has the highest contribution (0.176), but they do not explain why including the other components (both with positive Shapley values) reduces AUROC. A brief discussion of this would improve the paper's rigor.

- **NLI threshold \(T\) is not specified.** Algorithm 1 requires a threshold \(T\) but the paper never states its value or how it was selected. This affects reproducibility.

- **Transfer analysis is incomplete.** While DSN achieves high transfer ASR to gpt-3.5-turbo (max up to 95%, line 644–645), the paper reports that transfer to GPT-4, Claude, and Gemini fails entirely (lines 655–657). The paper acknowledges this but offers only hypotheses without analysis. A small ablation (e.g., varying the white-box model used for optimization) could provide insight into whether the failure stems from alignment differences or optimization properties.

### Trivial
- The AUROC gap between NLI (0.80) and Ensemble (0.79) is trivially small (0.01) and could be due to randomness or threshold effects. The paper should note this explicitly.

## Nice-to-Haves
- Include AmpleGCG or another post-GCG attack as a baseline to contextualize the magnitude of DSN's improvements.
- Provide the complete refusal keyword list and specify the NLI contradiction threshold \(T\).
- Clarify the multi-token Unlikelihood computation (product or average over tokens).
- Add error bars or confidence intervals to the ASR-over-steps figures (Figures 7, 10, 11) for all reported curves, not just the margin plots; the paper mentions "repeated experiments" (line 433) but this is not applied uniformly.
- A brief analysis of why the ensemble's AUROC slightly trails NLI alone would strengthen the evaluation section.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Ensemble Evaluation degrades performance relative to its best component."** — The harsh critic framed this as a critical flaw. However, the ensemble improves Accuracy (0.82 vs. 0.80) and F1 (0.86 vs. 0.81) over NLI alone, while AUROC drops only 0.01 (0.79 vs. 0.80). On 2 of 3 metrics the ensemble is strictly better; the claim of "superior performance" is well-justified. Removed because the criticism is factually correct in the narrowest sense (AUROC) but misleading overall.

2. **"Cosine Decay effectiveness is not isolated from refusal suppression."** — The paper DOES have this isolation: the α=0 condition (line 543: "None represents the DSN attack with Cosine Decay and α = 0"). The harsh critic's assertion that "no ablation removes only the refusal term" is factually wrong. The real issue (which I retain as a Major weakness above) is that the Figure 4 experiment uses the full DSN loss to support a Cosine Decay claim, and the α=0 ablation is presented in a different section without cross-reference.

3. **"Statistical significance: many figures show ASR curves without error bars"** — The paper explicitly states that "shadow regions with the dotted lines are the margin plots representing the mean and variance of repeated experiments" (line 433) for Figure 7. The critic's claim is inaccurate for at least one major figure. For other figures, the paper reports "max ASR among multiple rounds" (line 615). This is a partial criticism at best.

4. **Criticisms about missing appendix content, reference availability, or missing related work** — These are removed per the hard rules (appendix content is stripped by the parser; cited references are assumed to exist; related work gaps cannot be verified without external sources).

## Novel Insights

While the individual components (Cosine Decay weighting, Unlikelihood loss) are borrowed from prior work, the paper's key insight — that refusal suppression is a more tractable optimization target than affirmative elicitation because refusals form a smaller, more predictable set — is not found in prior jailbreak literature. The combination of these components in a single loss function, and the demonstration that the resulting loss correlates with jailbreak success better than the vanilla GCG loss (Figure 4), is the paper's genuinely novel contribution. The Ensemble Evaluation pipeline's use of NLI to detect semantic contradictions (as opposed to simple keyword matching or LLM-as-judge) is a practical novelty that addresses a real failure mode in jailbreak evaluation.

## Suggestions

1. **Run a clean ablation for Cosine Decay.** Directly compare (a) GCG loss, (b) GCG + Cosine Decay (α=0, no refusal term), and (c) Full DSN in the same Figure 4-style experiment to unambiguously attribute improvements.

2. **Add at least one stronger baseline.** The most impactful addition would be AmpleGCG, which also addresses token shift and would show whether DSN's gains are complementary or redundant.

3. **Specify the refusal loss computation for multi-token keywords.** Clarify whether \(\mathcal{L}_{\text{Un}}(y, x_{i:i+RTL(y)})\) is a product, average, or sum of per-token unlikelihood losses. Provide the refusal keyword list in an appendix.

4. **Acknowledge the AUROC pattern.** A one-sentence explanation in the Ensemble Evaluation section (e.g., "The slightly lower AUROC of the ensemble (0.79 vs. 0.80 for NLI) likely reflects noise from the LLM evaluators on borderline cases, while Accuracy and F1 benefit from the diverse signals") would resolve this concern.

5. **State the NLI threshold \(T\)** used in Algorithm 1 and describe how it was selected.
