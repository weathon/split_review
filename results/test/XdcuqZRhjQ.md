Now I have all the information I need. Let me synthesize the final review.

---

## Summary

The paper introduces LifelongSotopia, a benchmark that extends the SOTOPIA environment from single-episode social interactions to chained multi-episode interactions, enabling evaluation of language agents' social intelligence over lifelong/long-context settings. It tests three LLMs (GPT-4o, Gemini-1.5, Llama-3.1) with two memory mechanisms (full interaction history vs. summary-based advanced memory), comparing their believability (BEL) and goal completion (GOAL) against a human baseline. The main findings are that all LLMs decline in both dimensions over episodes with full-memory, and while advanced memory recovers performance on easy scenarios, all models fail on hand-crafted scenarios requiring explicit cross-episode reasoning — unlike humans.

## Strengths

- **Novel benchmark filling a clear gap.** LifelongSotopia is the first benchmark to chain multi-episode social scenarios from SOTOPIA, enabling evaluation of how social intelligence evolves over long contexts (Section 3.2). This addresses an understudied but important question in LLM agent evaluation.

- **Systematic comparison of memory mechanisms.** The paper compares two memory designs — full interaction history and summary-based advanced memory — across the same models and scenarios (Section 3.3, 5.3). This ablation cleanly separates the effect of memory design from model capability.

- **Human baseline grounds the comparison.** Human participants interacting in the same environment provide a practical reference point (Section 5.2). The qualitative analysis of how humans use past interactions (e.g., adopting negotiation strategies) concretely illustrates the gap.

- **BELEXT addresses the known evaluator degradation.** The paper identifies that GPT-4 overestimates BEL in long contexts and introduces a checklist-based penalty system (BELEXT) with manual validation (Section 3.4, Table 1). This shows methodological care and improves evaluation reliability for the BEL dimension.

- **Broad model coverage.** Three long-context models spanning different architectures and context windows (Gemini-1.5 up to 1M tokens, GPT-4o and Llama-3.1 at 128k) all show the same declining trend, demonstrating the challenge is not model-specific (Section 5.1–5.3).

## Weaknesses

### Major

- **GOAL evaluation over long contexts is not independently validated.** The paper discovers and corrects for GPT-4's overestimation of BEL in later episodes (via BELEXT with human validation), but applies no analogous correction or validation to GOAL scores. Since the central claim about lack of social intelligence (RQ2) rests on declining GOAL scores, an evaluator that degrades with context length could artificially produce the observed GOAL decline. The paper cites the original SOTOPIA validation of GPT-4 as a proxy for human judgment, but that validation was for single episodes, not the chained multi-episode setup here. Human annotation of a stratified sample of GOAL scores (especially from later episodes) would substantially strengthen the confidence in this result.

- **No measures of variance or statistical significance.** All figures report mean scores without error bars, confidence intervals, or any indication of spread across different character pairs, episode chain orderings, or random seeds (Figures 3, 4). A benchmark paper should enable readers to assess the reliability and significance of the observed trends. While the consistent pattern across all three models partially mitigates this concern, the lack of variance reporting is a notable omission.

### Minor

- **Human baseline is asymmetric.** Humans interact with an LLM-based character, while LLM agents interact with other LLM agents (Section 4). This is a confound: human-LLM interaction dynamics differ from LLM-LLM interaction dynamics in ways that could either inflate or deflate apparent human advantage. The paper's claim that "humans effectively use their past interactions to better plan and achieve their goals" is drawn from observing humans paired with LLM partners, not human-human interaction. A human-human baseline for at least a subset of episodes would make the comparison more rigorous.

- **The "harder scenarios" experiment uses only 5 hand-crafted scenarios.** The striking drop in GOAL shown in Figure 4 is based on only 5 scenarios (Section 5.3). The paper acknowledges this is a limitation, but these 5 scenarios carry substantial weight in the argument that "even with advanced memory, LLMs lack social intelligence." Without knowing the content, difficulty distribution, or showing results across diverse character pairs, this result is suggestive but not conclusive.

- **Advanced memory summary generation is underspecified and unvalidated.** The paper describes generating 200–300 word summaries (Section 3.3) but does not state what model or method produces them, nor validates whether they reliably capture information needed for future goal completion. Different summarization approaches could yield different results, and the current design does not allow the community to replicate or assess this component.

### Trivial

- The BELEXT penalty of 5 points per failed checkpoint (Section 3.4) is presented without justification. Different failure modes likely have unequal impact on believability, and a fixed penalty may over- or under-correct.

## Nice-to-Haves

- Human validation of a stratified sample of GOAL scores (especially from later episodes) to confirm the decline is not an evaluator artifact.
- Automatic diversity metrics for the generated scenario set beyond the manual check already performed.
- Analysis of how many of the 41 scenarios per relationship type are actually interdependent (the paper mentions some are, but does not quantify).

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:
- **Missing human experiment details** (number of participants, etc.): Likely in the appendix, which the parser strips.
- **Dropping other SOTOPIA-EVAL dimensions (KNO, SEC, REL, SOC, FIN):** Scope choice — the paper clearly scopes to BEL and GOAL for their research questions; evaluating all dimensions would be a different paper.
- **Advanced memory summary confound with evaluator (GPT-4o benefiting from GPT-4 summaries):** The paper does not specify which model generates summaries, and the claim that GPT-4o would benefit from stylistic alignment to GPT-4-generated text over other models is speculative and not well-founded.
- **Request to use non-GPT-4-based summarization:** While a valid suggestion, the specific concern about "stylistic alignment" is not supported by evidence.
- **"No analysis of scenario diversity or potential repetition":** The paper states a manual check was run to ensure quality and remove redundancies, following the same procedure as SOTOPIA.

## Novel Insights

None beyond the paper's own contributions. The reviewers' primary observations replicate the paper's own stated limitations (e.g., the need for better evaluator validation, the small number of hard scenarios). The strongest cross-cutting insight is that the paper's own discovery of the BEL evaluator problem (leading to BELEXT) should have prompted a parallel investigation of GOAL evaluator reliability — the paper noticed degradation in one metric but assumed the other was immune, which is a cautionary lesson for any work using LLM-as-judge for multiple dimensions.

## Suggestions

1. **Validate GOAL scores for long contexts.** Annotate a random stratified sample of episodes (by position in chain: early, middle, late) on GOAL with human judges. If the human-annotated GOAL trend matches GPT-4's, the central claim is secure. If not, a correction (analogous to BELEXT for BEL) is needed.
2. **Report variance.** Add error bars, bootstrapped confidence intervals, or at minimum report the range of scores across different character pairs/seed runs for the main figures.
3. **Collect human-human interaction data** for a subset of episodes to characterize the effect of the LLM partner on human performance.
4. **Specify the summary generation method** and ideally validate that the summaries encode the information necessary for cross-episode reasoning (e.g., by testing whether a human can use them to complete a held-out goal).
5. **Expand the hard-scenario set** beyond 5, or at minimum provide a description of the scenario types and difficulty calibration in the main text.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>