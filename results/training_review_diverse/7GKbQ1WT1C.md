Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a causality-guided debiasing framework for LLMs that models how social information influences LLM decisions through distinct causal pathways. From this framework, the authors derive three prompting strategies: (I) encouraging fact-based reasoning via social-agnostic fact, (II) counteracting existing selection bias via counterfactual assumptions, and (III) discouraging biased reasoning via explicit instructions. The combined method (DDP) is evaluated on WinoBias (gender bias in coreference) and BBQ (social bias in QA), showing strong empirical results across GPT-3, GPT-3.5, GPT-4, and Claude 2.

## Strengths

- **Novel perspective that reframes debiasing as regulating causal pathways.** The paper introduces causal graphs (Figures 3a/3b) that distinguish how social information can enter LLM decisions through separate routes (social-agnostic fact vs. social-salient text, modulated by selection mechanisms). This provides a principled organizational structure for understanding different debiasing approaches, going beyond the ad-hoc prompt engineering that characterizes most prior work. The three strategies are derived from specific pathways in the graph rather than assembled through trial and error.

- **Strong empirical results on multiple benchmarks across multiple LLMs.** On WinoBias Type I with GPT-4, DDP achieves a bias gap of only 2.17% with 94.57% accuracy on anti-stereotypical sentences, far outperforming the next best baseline (ICL: 9.23% gap; see Table 1). On BBQ, DDP achieves the highest accuracy across 8 of 9 social categories (Table 3). The results are consistent across GPT-3, GPT-3.5, GPT-4, and Claude 2, demonstrating that the practical effectiveness of the method is robust across model families and scales.

- **Ablation study that provides insight into the mechanisms.** The paper decomposes DDP into Fact Only (Strategy I) and Counteract Only (Strategy II) components and categorizes responses into TT/TF/FT/FF (Table 2). This reveals that Fact Only drives most of the gains while Counteract Only alone degrades performance, but DDP (combining both) improves over Fact Only — indicating that the strategies interact in non-trivial ways. The categorization into knowledge errors (FF) vs. bias errors (TF) provides a useful diagnostic lens.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the formal causal framework and empirical validation.** The paper presents three conditional-independence conditions (Equations 1–3) and Theorem 3.1 as the theoretical backbone, asserting that if these hold, the decision Y is independent of social category A. However, these conditions are never tested or measured — we do not know whether the proposed prompts actually enforce the claimed conditional independences in the model's internal representations. The conditions are simply assumed to hold when the prompts are applied. The "prompt properly considered" (PPC) selection variable plays a central causal role in the framework but is defined abstractly (the paper asserts that "if the LLM is well-trained and well-aligned, we can expect that the model will always condition on PPC"). A framework whose central theoretical quantities are not operationalized or verified is not a causal framework in a substantive sense — it is a motivation dressed in causal vocabulary. The paper would be stronger if it either provided evidence (e.g., probing-based measurement of mutual information between representations) or openly acknowledged that the causal framework serves as an organizational intuition rather than a verified mechanism.

2. **Theorem 3.1 is a straightforward restatement of the conditions.** The theorem states that if the three conditional-independence conditions (Equations 1–3) hold, then Y ⟂ A. The "proof" notes that both parents of Y are conditionally independent of A, so Y is independent — a direct consequence of d-separation given the assumed conditions. This is not a novel theoretical insight; it is a restatement of what the conditions already assert. The real scientific question is whether the prompts *achieve* those conditions, and the paper provides no evidence for that. Presenting this as Theorem 3.1 gives a false sense of theoretical depth.

3. **Inconsistent application of strategies across datasets without principled justification.** On WinoBias, DDP combines Strategies I and II (fact-based reasoning + counterfactual equal-representation assumption). On BBQ, DDP combines Strategies I and III (fact-based reasoning + "don't use social category" instruction). Strategy II is dropped and Strategy III is added, but the paper provides no explanation for why. If the framework is truly principled and the strategies are derived from causal pathways, the choice of which strategies to combine should follow from the causal structure of each task. Without this explanation, the paper reads as engineering different prompts for different datasets and then retroactively labeling them with strategy names — which weakens the claim that the framework is unifying or principled.

4. **Limited baselines relative to the strength of the claim.** The paper compares against only three baselines: Default, ICL with contrastive examples (Si et al., 2022), and Zero-shot COT (Kojima et al., 2022). While these are reasonable, several prompting-based debiasing approaches exist that could have been included — for instance, fairness-specific instructions, rephrasing prompts designed to avoid stereotypical paths, or variations of the "don't be biased" instruction used in practice. Given that the paper claims DDP provides a "principled" framework and state-of-the-art results, a broader baseline comparison would be necessary to demonstrate that the causal framing actually yields practical dividends beyond reasonable prompt engineering.

### Minor

5. **The ablation study does not directly compare DDP vs. Fact Only on the primary evaluation metric.** Table 2 reports the TT/TF/FT/FF error categorization for Fact Only, Counteract Only, and DDP, but this does not directly translate to the bias gap (pro-anti accuracy difference) used as the main metric in Table 1. The reader cannot determine from the reported data whether DDP (I+II) improves the bias gap over Fact Only (I) alone, or by how much. Given the importance of establishing that the causal strategies contribute beyond the simple "ask about facts" approach, this comparison should be reported.

6. **The fairness notion (statistical parity, Y ⟂ A) is adopted without sufficient discussion.** The paper defines unbiased decisions as independence between the decision and social category. This is known to be controversial — it can conflict with legitimate uses of social information (e.g., medical treatment decisions where gender or age may be relevant). The paper briefly acknowledges this in Figure 1's caption but does not engage with the normative implications. Since the entire debiasing effort targets this independence, a brief discussion of when this notion is appropriate vs. inappropriate would strengthen the framing.

### Trivial
None.

## Nice-to-Haves

- **Validate the causal assumptions empirically.** For instance, use activation or probing-based methods to measure whether the "Fact Only" prompt actually reduces the mutual information between gender-related representations and the model's decision. This would turn the causal story from a narrative into a testable hypothesis.
- **Include stronger baselines** such as fairness-specific instruction prompts, or rephrasing baselines that avoid stereotypical pathways without using the causal framework.
- **Explain the strategy selection process.** If Strategy II (counterfactual equal representation) is not used on BBQ because some social dimensions (e.g., physical appearance, religion) do not admit a natural "equal representation" counterfactual, say so explicitly. This would turn an apparent inconsistency into a principled scope condition.
- **Compare Fact Only vs. DDP on the bias gap metric** to quantify the marginal benefit of adding the causal strategies beyond the simple fact-based reasoning prompt.

## Removed Points

- **"Discrim-Eval mentioned but no results shown":** The paper states it conducts experiments on three benchmarks including Discrim-Eval. Results could be in the appendix, which was stripped by the parser. Removed per instruction to remove missing-appendix criticisms.
- **"Causal graphs are ornamental / narrative dressed in causal vocabulary":** This phrasing is too harsh. The causal graphs do provide a structured way to think about distinct debiasing pathways. The genuine problem is that the formal conditions are unverified (captured in Weakness 1 above), not that the graphs are meaningless.
- **"Fact Only alone already achieves strong results" as evidence the causal apparatus adds nothing:** DDP (I+II) does outperform Fact Only on the TT/TF/FT/FF metrics (Table 2), indicating the combined method provides benefit. This specific sub-claim is factually overstated by the critic.
- **Point about the paper lacking cost/failure-mode discussion of base question generation:** The paper explicitly states "the generation of base questions can be done by regular expression or one additional LLM query" and suggests using a smaller LLM. This adequately addresses the concern.
- **Formatting/style nitpicks:** Removed as parser artifacts.

## Novel Insights

The reviews surface an interesting tension not fully articulated in the paper itself: the causal framework's value may be primarily *taxonomic* rather than *mechanistic*. The paper is most convincing when it treats the causal graph as a way to systematically organize different prompting strategies (fact-based reasoning, counterfactual equalization, anti-bias instructions) into a coherent typology with distinct targets — this is genuinely useful for practitioners. The framework is least convincing when it claims to offer rigorous causal guarantees, because the theoretical conditions (Equations 1–3) and Theorem 3.1 add no empirical content beyond what the strategies already enact. The paper would be much stronger if it leaned into the taxonomic contribution and dropped or substantially downplayed the formal causal language.

## Suggestions

1. **Reframe the causal framework's role.** Present the causal graphs as an *organizational framework* for categorizing debiasing strategies by which pathway they regulate, rather than as a formally verified causal model. This would align the framing with what is actually demonstrated.

2. **Report Fact Only vs. DDP on the bias gap.** Add a direct comparison of Fact Only (Strategy I alone) vs. DDP (I+II) on the pro-anti accuracy gap to demonstrate the marginal benefit of combining strategies.

3. **Explain the strategy selection across datasets.** Add a brief justification for why Strategy III is used on BBQ instead of Strategy II (e.g., "Strategy II's counterfactual equal-representation assumption is natural for binary categories but less straightforward for multi-faceted social dimensions like religion or appearance; we therefore use Strategy III for those cases").

4. **Include two additional baselines** — at minimum a fairness-specific instruction baseline and one more recent prompting-based debiasing method — to strengthen the empirical comparison.

5. **Tone down the formal claims about Theorem 3.1.** The theorem should be presented as a straightforward consequence of the conditions rather than a substantive theoretical result. The text already partially does this ("a sufficient condition"), but the presentation as a numbered theorem invites expectations that are not met.

## Score and Decision

This paper has a real and useful empirical contribution — the finding that prompting an LLM to reason about a social-agnostic version of a question and using that answer as context reduces decision bias. The empirical results are strong and consistent across models and datasets. However, the paper overclaims its theoretical contribution substantially: the causal framework is presented as a rigorous foundation but its central conditions are unverified, the theorem is a trivial restatement, the strategies are applied inconsistently without principled explanation, and the baseline comparison is limited. These issues are significant enough that the paper in its current form does not deliver on its stated contributions. A substantially revised version — one that reframes the causal framework as an organizational tool rather than a verified mechanism, adds baselines, and justifies the strategy choices — could be a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>