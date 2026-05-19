- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 6, 8, 5
Now I have all the information I need. Let me construct the final consolidated review, cross-checking every claim against the paper.

---

## Summary

This paper defines a systematic three-component framework (prompting, sampling, aggregation) for black-box confidence elicitation in LLMs, and benchmarks it across five models (GPT-3, GPT-3.5, GPT-4, Vicuna, LLaMA 2) and eight datasets spanning five reasoning types. The main findings are that LLMs exhibit overconfident verbalized confidence mimicking human speech patterns, that human-inspired prompting strategies can partially reduce miscalibration, that consistency among multiple responses substantially improves failure prediction (e.g., GSM8K AUROC from 54.8% to 92.7%), and that the gap between black-box and white-box methods is narrow. The paper contributes a well-organized method space and a broad empirical comparison.

## Strengths

- **Systematic framework unifying the method space.** The three-component decomposition (prompting, sampling, aggregation) in Section 3 and Figure 1 provides a clean organizational structure that subsumes previously isolated strategies. This is a genuinely useful conceptual contribution for future work in this area.

- **Broad and diverse empirical coverage.** The evaluation spans five LLMs of varying scales (including both open-source and closed-source APIs) and eight datasets across five reasoning types (commonsense, arithmetic, symbolic, ethics, professional knowledge). This breadth, documented in Section 4, exceeds concurrent work and supports the paper's goal of providing a "strong baseline."

- **Demonstration that consistency-based methods dramatically improve failure prediction on arithmetic tasks.** Table 2 (Section 5.3) shows that Self-Random sampling with M=5 raises GSM8K AUROC from 54.8% (near random) to 92.7%. This is the paper's strongest empirical result and directly supports its claim that sampling + aggregation strategies improve failure prediction.

- **Identification of human-like confidence patterns in LLMs.** Figure 2 (Section 5.1) reveals that verbalized confidence values cluster in multiples of 5 within the 80–100% range, mirroring patterns in human speech. This behavioral observation is a novel finding beyond prior likelihood-based uncertainty methods.

- **Quantification of the black-box vs. white-box gap.** Section 6 reports a narrow AUROC gap (0.522 vs. 0.605), providing a concrete benchmark for practitioners choosing between approaches.

## Weaknesses

### Fatal

None.

### Major

- **Comparative claims lack statistical error bars for most experiments.** Results are reported as point estimates without confidence intervals, error bars, or significance tests across the vast majority of tables and figures (only Table 3 includes variance estimates, for one aggregation comparison). Since sampling methods rely on random seeds and many comparisons involve small sets of datasets (5–8), it is impossible to assess whether observed differences (e.g., "Self-Probing maintains the most consistent advantage," "Misleading achieves the lowest average ECE in Table 2") are meaningful or noise. This does not invalidate the paper's qualitative findings, but it prevents the benchmark from serving as a definitive comparison. The paper should either provide estimates of variability (e.g., over multiple seeds) or clearly frame all comparative claims as qualitative patterns.

- **The Pair-Rank aggregation method rests on an unverified generative assumption.** The Proposition (Section 3.4) assumes that Top-K responses are drawn *without replacement* from a categorical distribution \(P\), and derives \(\mathbb{P}(S_u \succ S_v) = P(S_u)/(P(S_u)+P(S_v))\) from this assumption. The paper provides no justification—empirical or theoretical—for why LLM output ordering under the Top-K prompt should correspond to draws without replacement from a single distribution. The model could produce non-distinct guesses, exhibit ordering artifacts from decoding hyperparameters (temperature, repetition penalty), or violate the without-replacement structure entirely. No empirical check is offered (e.g., whether pairwise ordering frequencies match the predicted ratio). This does not necessarily invalidate Pair-Rank's empirical performance, but it makes the claimed theoretical grounding suspect. The paper should either provide empirical validation or downgrade Pair-Rank to a heuristic and discuss when it might fail.

### Minor

- **The paper's framing of "mitigating overconfidence" via ECE reduction is partially conflated with accuracy-driven effects.** The paper acknowledges this explicitly (Section 5.2, lines 266: *"a reduction in overconfidence is due to the diminished gap between average confidence and accuracy, not necessarily indicating a substantial increase in the model's ability to judge the correctness of its responses"*), which is commendable. However, the abstract and Section 5.2 title still treat ECE reductions as evidence that prompting "mitigates overconfidence." The example given (GPT-4 on GSM8K: ECE 0.064 by assigning 100% confidence to nearly all samples, with AUROC still 54.8%) shows that the model has not learned to express varying uncertainty; it is merely always confident and almost always right. A more consistently careful framing would separate the two failure modes (miscalibration vs. inability to discriminate) throughout, rather than only in the fine-print discussion.

- **The Multi-Step prompt aggregates step confidences multiplicatively (\( \prod C_i \)) without discussing whether independence across steps can be assumed.** If step-wise errors are correlated (which is likely in sequential reasoning), this systematically deflates the final confidence. The paper does not discuss this issue.

- **The Misleading sampling strategy (feeding suggestive cues like "I think the answer might be X") could confound uncertainty with persuasibility.** A model that simply follows misleading hints may change its answer regardless of its own uncertainty. The paper does not discuss or control for this confound.

- **The number K of Top-K guesses is not analyzed for sensitivity.** The paper does not state what K is used or whether results change with different values of K. A sensitivity analysis would strengthen the claims about Top-K methods.

- **Sample sizes per dataset are not reported.** Since calibration and AUROC metrics depend on sample size for reliability, this information would be useful for interpreting the results.

### Trivial

- Table 1 caption reads "Vanilla Verbalized Confidence of 4 models" but the table lists five models (GPT-3, Vicuna, LLaMA 2, GPT-3.5, GPT-4).

## Nice-to-Haves

- While full prompt templates are stated to be in the appendix (which is stripped in this version), including key templates in the main paper or making them easily accessible would improve reproducibility.
- A brief discussion of how decoding hyperparameters (temperature, top-p) affect the sampling strategies would be valuable, especially given the "without replacement" assumption in Pair-Rank.
- The recommendation for practitioners (Top-K + Self-Random + Avg-Conf or Pair-Rank) could be hedged more explicitly given the paper's own finding that no method consistently wins across all settings.

## Removed Points

These points were considered and excluded from the main review for the following reasons:

- **Criticism about the paper "conflating calibration with accuracy" implying the paper is unaware of the issue**: The paper explicitly discusses this conflation at line 266 and gives the GPT-4/GSM8K example. The criticism that the paper "still treats ECE reductions as evidence" overstates what the paper does; the acknowledgment is present and reasonable, though the framing could be more consistent. Retained in weakened form as a Minor issue rather than a Major one.
- **Criticism about the reproducibility section and prompts being in the appendix**: Per policy, appendix content is stripped by the parser; criticisms about missing appendix content are removed. The prompts exist in the original submission.
- **Speculation that Pair-Rank "may be exploiting" ECE gamming**: This is a speculation about a potential failure mode without evidence in the paper. Removed as insufficiently grounded.
- **Criticism about the paper not testing whether verbalized confidence is semantically tied (Section 3.1 claim)**: While this is a valid suggestion for future work, it is a scope-expansion request, not a weakness of what the paper actually does.
- **Concern about whether models comply with Top-K prompt instructions (distinctness of guesses, tie handling)**: Reasonable in spirit but presented without evidence of actual non-compliance; downgraded to a minor note.
- **General comment about "the paper reads as a collection of observations"**: This is a stylistic opinion without concrete evidence, removed as not an actionable weakness.

## Novel Insights

A synthesis of the reviews reveals an interesting tension not fully explored by the paper itself: the methods that achieve the lowest ECE (e.g., Pair-Rank at 6.9% average ECE) do not consistently achieve the highest AUROC (Pair-Rank's average AUROC is 67.6, while Avg-Conf achieves 66.9). This suggests that in the black-box confidence elicitation setting, **calibration and discrimination may be partially competing objectives**—methods that distribute probability mass to match accuracy (good calibration) may not simultaneously produce well-separated scores for correct vs. incorrect answers (good discrimination). The paper observes this pattern but does not frame it as a design tension; future work could explore whether a principled Pareto tradeoff exists, or whether specific combinations of sampling and aggregation can improve both metrics simultaneously.

## Suggestions

1. **Add statistical grounding.** Even a small number of repeated runs (3–5 seeds) with variance estimates for the central comparisons (e.g., Table 1 baselines, Table 2 sampling comparisons) would substantially strengthen the reliability of the benchmark. If API costs prohibit extensive repetition, acknowledge this limitation explicitly and frame comparative claims as qualitative patterns.

2. **Validate or reframe Pair-Rank.** Either (a) provide empirical evidence that Top-K response orderings conform to the without-replacement categorical assumption (e.g., check whether observed pairwise frequencies match the predicted \(P(S_u)/(P(S_u)+P(S_v))\) form), or (b) remove the Proposition's theoretical claim and present Pair-Rank as an empirically-motivated heuristic, with a discussion of conditions under which it might fail.

3. **Consistently separate miscalibration from discrimination failure.** The paper already does this in one discussion paragraph (line 266); extend this careful framing to the abstract, titles, and conclusions so that "reducing overconfidence" is not used synonymously with "lowering ECE."

4. **Report sample sizes per dataset** in the experiment setup section.

5. **Add sensitivity analysis for K in Top-K** to establish robustness of the method.
