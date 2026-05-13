Now I have a thorough understanding of the paper and can synthesize the review. Let me carefully evaluate the reviewers' claims against the actual paper content.

## Summary

This paper introduces GSM-Symbolic, a benchmark built from symbolic templates of GSM8K problems that enables generating diverse variants of grade-school math questions, allowing evaluation of LLM performance as a distribution rather than a single accuracy point. The key findings are: (1) LLMs show noticeable variance across different instantiations of the same question; (2) performance degrades when numerical values are changed versus names; (3) performance decreases and variance increases with question difficulty; and (4) adding seemingly relevant but operationally irrelevant "No-Op" clauses causes catastrophic performance drops (up to 65%) across all tested models, even when 8-shot examples of the same question are provided.

## Strengths

- **The GSM-Symbolic template framework is a genuine methodological contribution.** The template system with explicitly defined variables, domains, and constraints enables generating unlimited controlled variants, moving beyond single-point GSM8K evaluation to distributional evaluation. Quality controls include automated correctness verification and manual review of samples (Section 3.1).

- **The No-Op finding is striking and well-demonstrated.** The demonstration that inserting a single irrelevant clause (e.g., "5 were smaller than average") causes models to incorrectly incorporate it into their computation is a clear, interpretable failure mode. The o1-mini and Llama-3-8B examples in Figure 6 are particularly compelling concrete evidence.

- **The few-shot No-Op experiments (NoOp-Symb and NoOp-NoOp) are important controls.** The finding that providing 8 shots of the same question variant does not recover performance (Figure 7b) rules out the hypothesis that the failure is a simple prompting issue, strengthening the claim that deeper reasoning deficiencies exist.

- **The name-vs-number ablation (Section 4.2) provides informative decomposition.** Disentangling sensitivity to superficial name changes from numerical changes reveals a clear gradient where numerical changes cause more variance and performance degradation, providing insight into what types of changes LLMs are most fragile to.

- **Large-scale evaluation across 25 models gives findings generality.** Consistent patterns across model families, sizes, and both open and closed models strengthen the empirical contribution.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming: the leap from "LLMs are fragile to distractors" to "LLMs cannot perform genuine reasoning."** The paper's experiments convincingly show that LLMs are fragile—performance varies across instantiations, degrades with difficulty, and catastrophically fails when distractors are added. However, the paper repeatedly frames this as evidence that LLMs cannot perform genuine/formal reasoning and instead only do pattern matching (abstract: "current LLMs are not capable of genuine logical reasoning"; Section 4.2: "assuming that LLMs are not performing formal reasoning"; conclusion: "It may resemble sophisticated pattern matching more than true logical reasoning"). The experiments show fragility, but they do not rule out that models perform some form of reasoning that is simply brittle. A model that correctly solves 80-90% of standard GSM8K problems through a combination of learned patterns and genuine arithmetic computation, but fails when distractors are present, is not the same as a model that "cannot perform formal reasoning." The No-Op finding demonstrates that models cannot *robustly* reason, not that no reasoning occurs at all. This distinction matters because the paper's theoretical framing about pattern matching vs. reasoning is not directly tested by the experiments—the experiments only test robustness.

- **The data contamination claim is speculative and presented without ruling out confounds.** Section 4.1 and Figure 2 show that GSM8K performance sits on the right tail of the GSM-Symbolic distribution for 21/25 models, and the paper presents this as "hinting at potential data contamination." However, alternative explanations are not analyzed: (a) the original GSM8K problems may use systematically smaller/simpler numbers than GSM-Symbolic's template-generated ranges (the example in Figure 1 uses ranges like 5–100 and 100–500, which may produce harder arithmetic); (b) the 100 selected templates may not be representative of the full difficulty distribution. The paper states this as "one explanation" (line 149), which is appropriately hedged, but subsequent references (e.g., the contribution bullet in Section 1: "hinting at potential data contamination") elevate it beyond the evidence.

### Minor

- **Variance estimates lack statistical quantification.** Each accuracy data point in the GSM-Symbolic distribution (Figure 2) is computed from only 100 questions. At ~80% accuracy, the standard error on each accuracy estimate is approximately 4 percentage points, meaning some of the observed "variance" across the 50 sets is statistical noise. The paper does not report confidence intervals or standard error bounds. While the qualitative patterns (rightward shift, increased variance with difficulty) are likely robust since they appear consistently across 25 models, precise claims about variance magnitude should be treated with appropriate uncertainty.

- **The difficulty manipulation in Section 4.3 confounds number of reasoning steps with number of distractor numbers.** Adding clauses adds both more reasoning steps AND more numerical values to process. The paper acknowledges this in a footnote (line 192) but does not attempt to disentangle the two factors. This limits the strength of the conclusion that "models are not performing formal reasoning" from the difficulty degradation alone—though the No-Op experiment does address this more directly.

- **The Figure 7(c) anomaly (weaker models outperform on NoOp-Symb) is underanalyzed.** The paper notes this is "a very notable observation" but does not provide an explanation or deeper analysis. If weaker models that perform poorly on standard GSM-Symbolic perform relatively better when given same-question in-context examples, this could suggest that the stronger models' pattern-matching is more entrenched—consistent with the paper's thesis—but it could also suggest a different mechanism. Deeper analysis of this finding would strengthen the paper.

### Trivial
- None.

## Nice-to-Haves

- Evaluate with non-greedy decoding (e.g., temperature > 0 with majority voting) to assess whether the observed variance is an artifact of argmax sensitivity or reflects genuine performance instability.
- Error categorization of No-Op failures: quantify what fraction of errors involve the model specifically executing the distractor operation versus making other types of errors, to more directly test the "blindly convert surface-form cues to operations" hypothesis.
- Control for number magnitude in difficulty experiments by generating GSM-Symbolic variants with the same number of clauses but different number ranges to isolate the effect of reasoning steps from arithmetic complexity.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic's point about the false dichotomy between "formal reasoning" and "pattern matching"** — This is substantially the same concern as the main overclaiming weakness above, but the harsh critic phrases it as the introduction "framing the reasoning debate as a binary." This is a framing preference rather than a separate weakness; the core issue (experimental evidence doesn't establish the strong claim) is already captured above.

- **Harsh Critic's claim that the paper doesn't engage with work documenting compositional generalization or systematic reasoning** — This is a "missing related works" criticism; per instructions, we cannot confirm the existence of specific uncited works and should not include this.

- **Harsh Critic's claim about small sample sizes inflating variance** — This is kept as a Minor weakness (lack of statistical quantification), but the harsh critic's specific quantitative estimate (true SD of 4% vs observed 5.7%) goes beyond what we can verify without access to the raw data. The general point about measurement noise is valid and retained.

- **Harsh Critic's claim about greedy decoding amplifying variance** — The paper uses greedy decoding because it standard practice for GSM8K evaluation. Requesting different decoding strategies is a nice-to-have, not a methodological flaw in the current evaluation. The paper's conclusions about relative performance differences (GSM8K vs GSM-Symbolic, difficulty scaling) would likely hold under any consistent decoding strategy.

- **Harsh Critic's point about the abstract overclaiming name-only changes** — The paper's abstract says "performance of all models declines when only the numerical values in the question are altered." Looking at Section 4.2, this claim is about numerical values specifically, and the data supports it. The abstract does not overstate name-only changes.

- **Strength Finder's claim about "statistically grounded observation" for data contamination** — This is removed because the 21/25 observation is descriptive, not statistically grounded as evidence for contamination, and this claim conflicts with the verified weakness about alternative explanations.

- **Strength Finder's claim about NoOp showing "models cannot genuinely understand mathematical concepts"** — This is removed as it mirrors the paper's overclaiming. The NoOp experiment shows fragility to distractors, not necessarily a complete lack of understanding.

## Novel Insights

The most novel insight from combining the reviews with the paper's content is that the NoOp-Symb and NoOp-NoOp experiments (Figure 7b) represent the paper's most rigorous test of the pattern-matching hypothesis. While the variance and difficulty results are consistent with pattern matching, they are also consistent with brittle reasoning. The NoOp experiments are more diagnostic because they show that models incorporate operationally irrelevant information into their computation chains in specific, predictable ways (e.g., subtracting "smaller" numbers)—a finding that is more specifically about the *mechanism* of failure (surface-form cue → operation mapping) rather than just its *existence*. However, the Figure 7(c) anomaly, where some weaker models perform better with same-question in-context examples, is an underexplored finding that could refine the hypothesis: it suggests that in-context examples of the correct reasoning chain can scaffold reasoning in some models but not others, which implies the failure is not simply "no reasoning capability exists" but rather "reasoning is susceptible to specific types of interference."

## Suggestions

- Soften the theoretical claims throughout the paper. Replace assertions like "current LLMs are not capable of genuine logical reasoning" with more precisely supported claims like "current LLMs exhibit fragile reasoning that deteriorates systematically with problem variation and is susceptible to irrelevant distractors." This aligns conclusions with evidence while preserving the important empirical findings.

- For the data contamination argument: either control for number magnitude confounds (e.g., by generating GSM-Symbolic variants using numbers from the same distribution as original GSM8K) or acknowledge more prominently that the right-tail observation has multiple explanations beyond contamination.

- Add confidence intervals or error bars to the accuracy distributions to distinguish genuine performance variation from measurement noise.

- Provide error categorization for No-Op failures (what fraction involve the distractor operation vs. other errors) to more directly substantiate the "blindly convert surface-form cues to operations" hypothesis.

- Analyze the Figure 7(c) anomaly more deeply—why do weaker models like Gemma-2B and Mistral-7B benefit more from same-question in-context examples on NoOp-Symb than stronger models?

## Score and Decision

The paper makes a valuable and well-executed empirical contribution. The GSM-Symbolic framework and the No-Op finding are genuinely important for the community. The main issue is one of framing: the conclusions overclaim relative to what the experiments establish. The experiments show fragility and susceptibility to distractors—important and well-documented findings—but do not establish that "LLMs cannot perform genuine reasoning" as a categorical claim. This is a significant overclaiming issue, but the underlying empirical work is sound and impactful. The data contamination claim is speculative but presented with appropriate hedging ("one explanation could be"). The statistical methodology could be more rigorous but the qualitative patterns are consistent across 25 models, making the core findings robust.

**Originality:** High — the GSM-Symbolic template approach and the No-Op design are novel and impactful evaluation methodologies.

**Importance of research question:** High — understanding the limitations of LLM mathematical reasoning is critical for the field.

**Claims well-supported:** Partially — the empirical findings are well-supported, but the theoretical interpretation ("no genuine reasoning") goes beyond what the experiments establish.

**Soundness of experiments:** Good — large-scale, consistent across models, with sensible controls (NoOp-Symb, NoOp-NoOp). Missing statistical quantification and some confounds not controlled.

**Clarity of writing:** Good — the paper is well-structured and the examples (Figure 6) are clear and illustrative.

**Value to community:** High — the benchmark and the No-Op finding will likely influence future evaluation practices.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>