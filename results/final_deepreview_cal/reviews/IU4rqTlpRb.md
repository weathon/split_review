Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 bracket**: Plausible score range is **5.0 to 7.5**. The paper clearly exceeds the ~3.0 weak anchor cluster and is below the ~8.0 strong anchor cluster. The most directly comparable anchor is "Jogging the Memory of Unlearned LLMs" (6.75, Accept).

**Round 2 narrowing**: The paper is stronger than "Jogging the Memory" (6.75) because it identifies a specific causal driver (syntax) rather than just documenting relearning, provides controlled experiments that isolate the mechanism, and offers a principled mitigation. It is weaker than top-quartile papers (7.5+) due to missing ablations for the diversification method, no error bars/variance reporting, and the "primary driver" claim slightly exceeding the evidence. **Final score: 7.0**.

---

## Summary

This paper identifies syntactic similarity—rather than topical relevance—as the primary driver of benign relearning in LLM unlearning. Through controlled experiments on TOFU (varying syntactic overlap while controlling for topicality), a re-analysis of the BLUR benchmark that removes confounds, and mechanistic analyses (representation/gradient alignment, template vs. keyword loss ratios), the paper makes a compelling case that structural overlap between relearn and target sets enables recovery. It then proposes syntactic diversification (paraphrasing forget queries with GPT-4o prior to unlearning) as a practical mitigation that suppresses relearning and improves utility.

## Strengths

- **Controlled causal experiment on TOFU isolating the syntax mechanism** (Section 5, Figure 4): The paper constructs contrasting relearn sets—topically-relevant (same entity, different structure) and syntactically-similar (same structure, different entity)—with quantified syntactic similarity scores (0.4513 vs. 0.2349). Across GA, NPO, and SCRUB, the syntactically similar set consistently achieves higher recovery. This is the cleanest evidence to date that syntactic overlap drives relearning independent of topicality.

- **Re-analysis of BLUR exposing confounds and showing syntactic alignment** (Section 4, Table 1, Figures 2–3): The paper identifies two confounds in BLUR's evaluation—unequal dataset sizes biasing step counts and non-monotonic recovery trajectories—and corrects them by standardizing the step budget and reporting best-step ROUGE-L. Under this fairer protocol, the topical-relevance ordering collapses. The paper further shows that syntactic similarity scores (character-level Levenshtein) align better with recovery than BLUR's topical tiers. This is a methodological contribution in its own right that improves evaluation standards for the field.

- **Mechanistic explanation via template-keyword imbalance** (Section 6, Figures 5–6): The paper provides a dual analysis: (a) representation and gradient cosine similarities showing syntactically similar sets align much closer to the target set under the unlearned model, and (b) the loss ratio (template NLL / keyword NLL), which rises sharply during unlearning, demonstrating that unlearning disproportionately suppresses template tokens while leaving keywords undersuppressed. This explains why syntactically similar data can quickly restore the template structure and recover forgotten keywords. The template-keyword analysis is conceptually novel and goes beyond prior work.

- **Principled mitigation that turns the diagnosis into a solution** (Section 7, Figures 8–9, Table 2): Syntactic diversification—paraphrasing forget queries into heterogeneous structures—reduces the syntactic similarity between forget and relearn sets from 0.4513 to 0.2241. This essentially eliminates relearning at 50 unlearning steps (Figure 8b), balances the loss ratio to ~1 (Figure 9 top), and improves utility metrics across Real Authors, World Facts, and Retain sets (Table 2). The method is simple, grounded in the paper's own mechanistic analysis, and practically useful.

## Weaknesses

### Major

- **Missing ablations for the diversification method** (Section 7): The paper attributes the mitigation effect to *syntactic* diversification, but never ablates against simpler data augmentation strategies such as synonym replacement (same structure, different tokens), random word dropout, back-translation, or adding irrelevant tokens. Without these baselines, it is unclear whether the effect requires structural variation per se, or whether any form of input perturbation during unlearning would help. This is a methodological gap that weakens the paper's central claim about syntax being the active ingredient in the mitigation.

- **No statistical variance or error bars reported**: None of the bar charts (Figures 2, 5) or line plots (Figures 3, 6, 8, 9) include error bars, confidence intervals, or multi-seed variance. For the main TOFU experiments (Figure 4), it is unclear whether the differences between topically-relevant and syntactically-similar conditions are consistent across random initializations. Given that the paper's core claim about syntax being "the primary driver" rests on the magnitude of this difference, variance reporting is essential.

### Minor

- **"Primary driver" claim slightly exceeds the evidence**: The paper states that syntactic similarity is the *primary* driver of benign relearning (abstract, Section 5.3). The TOFU experiment compares two specific cells of a 2×2 design (high-syntax/low-topic vs. low-syntax/high-topic) but does not include the full factorial crossing (high-syntax/high-topic, low-syntax/low-topic). The claim is well-supported for the TOFU setting, but "primary" in a general sense would require a formal interaction test. The BLUR re-analysis is correlational (syntactic similarity scores correlate with recovery) and does not control for confounds such as dataset size or content diversity. The authors should moderate the "primary" language to reflect these bounds.

- **The loss ratio analysis (Figure 6) does not specify which unlearning method was used**: The caption and surrounding text refer only to "unlearn" and "relearn" without identifying whether GA, NPO, or SCRUB produced the data. Since the paper shows large method-specific differences in relearning behavior (Figure 4), the loss ratio dynamics may also vary by method. This should be clarified.

- **Forget efficacy after diversification is indirectly reported but could be more direct**: While Figure 8b shows that the diversified model produces zero target keywords at relearn step 0 (confirming it has forgotten), the paper does not report standard forget-set metrics such as ROUGE-L on target queries or the percentage of "refusal/empty" outputs for the diversified model. The Relearn Success Rate at step 0 is informative but a more complete evaluation would include additional metrics.

- **Limited model scope in the main text**: The main experimental results use Llama-2-7b-chat. Phi model results are deferred to Appendix B.3 and GPT-2 results also appear in the appendix. A brief summary of these additional results in the main text would strengthen claims of model-family independence.

## Nice-to-Haves

- A full 2×2 crossing experiment on TOFU (high/low syntax × high/low topic) would cleanly resolve the "primary driver" claim and is a natural extension.
- An alternative syntactic similarity measure (e.g., parse-tree similarity or template-mining similarity) would strengthen the claim that it is *syntactic structure* that matters, not just character-level token overlap. Appendix I mentions this but no results are shown.
- Reporting the cost (API calls, time) of GPT-4o paraphrasing and whether a smaller model suffices would aid practitioners.

## Removed Points

These points were raised by reviewers but removed or demoted after verification against the paper:

- **Criticism about BLUR's Lorem Ipsum puzzle**: The harsh critic claimed it is "puzzling how randomly generated filler text syntactically aligns with Harry Potter target queries." However, Table 1 shows the syntactic similarity scores for WHP are 0.1894 (D_hi), 0.1767 (D_mid), and 0.1818 (D_low)—all similar. Character-level Levenshtein distance captures patterns like common function words, punctuation, and character distributions. The paper's claim is correlational (syntactic similarity aligns with recovery), not causal about WHP specifically. This criticism misunderstands what the paper claims about this correlation and is thus removed.

- **Criticism about missing related work**: Removed per instruction—I cannot verify missing references.

- **Criticism about "forget efficacy after diversification is not directly reported"**: This is factually incorrect. Figure 8b shows the Relearn Success Rate at relearn step 0 (which is the forget efficacy) is 0 for 37/43/50 unlearning steps, indicating successful forgetting. The paper does report this.

- **Various formatting/style nitpicks and reproducibility concerns about undisclosed hyperparameters**: Removed per hard rules.

## Novel Insights

The most novel synthesis from the reviews is that the paper's two contributions—(1) identifying template suppression as the mechanism and (2) proposing syntactic diversification as mitigation—are elegantly linked: because the analysis shows that unlearning disproportionately targets template tokens over keywords, the natural remedy is to break template rigidity by diversifying query forms. This analysis-to-mitigation arc is clean and is not weakened by the missing diversification ablations (which would only further confirm which component of the perturbation drives the effect). The BLUR re-analysis also provides a useful methodological lesson: benchmark evaluations that do not control for step budgets across conditions of unequal size can produce spurious conclusions about what factors drive relearning.

## Suggestions

1. Add ablation baselines for the diversification method: synonym replacement (same structure, different tokens), random word dropout, and back-translation. This is the single highest-leverage experiment to confirm that *syntactic* variation is the active ingredient.
2. Report variance (error bars / confidence intervals) across at least 3 seeds for the main TOFU experiments (Figure 4) and the diversification results (Figure 8).
3. Tone down "primary driver" to "a stronger and more consistent driver" or "a previously overlooked driver" in the abstract and conclusion.
4. Clarify which unlearning method produced Figure 6 (loss ratio).
5. Include a brief summary of Phi / GPT-2 results in the main text, at least one sentence per model.
6. Add a small table of forget-set metrics (e.g., % empty/refusal outputs, ROUGE-L on target queries) for the diversified model to complement Figure 8.

## Score and Decision

**Calibration**: Round 1 bracket: 5.0–7.5. Round 2 narrowed to 6.5–7.5 by comparing against "Jogging the Memory of Unlearned LLMs" (6.75, Accept), which documents relearning but lacks mechanistic analysis and mitigation. The present paper is stronger in depth (causal identification, mechanism, mitigation) but held back by missing ablations and variance reporting. Score of **7.0** places it above the best comparable anchor (6.75) while acknowledging fixable gaps that prevent it from reaching the 7.5+ tier.

**All anchors retrieved (non-exhaustive list of relevant ones)**: fMNRYBvcQN (6.75, Round 1&2—directly comparable, paper is stronger), CIN2VRxPKU (5.33, Round 1—less relevant, paper is stronger), 8SPSIfR2e0 (5.75, Round 1—less relevant), Q1MHvGmhyT (6.00, Round 1&2—less relevant), NGKQoaqLpo (7.50, Round 2—different topic but similar structure, paper is weaker), HVFMooKrHX (6.60, Round 2—less relevant), fXJCqdUSVG (6.50, Round 2—less relevant).

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>