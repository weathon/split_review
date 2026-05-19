- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Here is my consolidated final review.

---

## Summary

This paper investigates the role of the initial reasoning step in multi-step math problem solving by small language models (2B–8B). It first demonstrates, via an oracle experiment, that providing a correct first step from a large model (GPT-4) boosts small-model accuracy dramatically (up to +24 points on GSM8K). It then proposes QuestCoT, a prompting strategy where the small model generates a self-subquestion to determine the first step before continuing to reason. Evaluated on GSM8K, SVAMP, ASDiv, and MultiArith across 7 small models, QuestCoT shows mostly positive but modest improvements over standard CoT and sub-question decomposition.

## Strengths

- **Oracle experiment cleanly establishes the phenomenon.** Table 1 shows that GPT-4 first-step guidance produces large and consistent gains — e.g., OlMo-7B rises from 13.6% to 37.9% on GSM8K, and Gemma-2B from 7.5% to 17.8%. The pattern is monotonic with guide-model quality and holds across six small models. This is the paper's strongest evidence.

- **First-step leakage is convincingly ruled out.** The paper reports (Section 4, line 212) a manual check on 1000 development samples where the generated first step matched the final answer in only 1 case. Combined with the constraint that problems require 2–8 steps, this rules out the trivial explanation that guidance simply reveals the answer.

- **Improved reasoning across diverse models and datasets.** Table 2 reports QuestCoT results across 7 models (Gemma-2B, Phi3-Mini, LLaMA2-7B, OlMo-7B, Mistral-7B, Gemma-7B, LLaMA3-8B) and 4 datasets. Out of 28 model-dataset comparisons, 26 show improvements, with the largest gains for weaker models (OlMo-7B: +8.6 on SVAMP, +7.2 on MultiArith). QuestCoT also outperforms the sub-question decomposition baseline (Figure 2).

- **The first-step benefit extends beyond simple two-step problems.** Figure 3 (labeled fig:teachervsno) shows that GPT-4 first-step guidance improves Mistral-7B performance at every step count from 2 to 8 on GSM8K.

## Weaknesses

### Fatal
None.

### Major

- **Few-shot prompts are selected from the test set (Section 3.3, line 189).** This is a clear methodological concern: using test-set examples as in-context demonstrations can inflate absolute accuracy numbers, since the model sees reasoning traces from the exact distribution it is evaluated on. While both CoT and QuestCoT use the same prompt source (so the relative comparison between methods may still be directionally meaningful), the absolute numbers in Tables 2 and Figure 2 are not trustworthy as reported, and the paper provides no ablation to quantify the effect. This must be fixed (using training-set prompts) for the quantitative claims to be credible.

- **QuestCoT gains are small for many settings, with no significance testing.** Six out of 28 comparisons show improvements ≤1 point absolute; two comparisons show decreases (LLaMA2-7B on ASDiv: −0.5, Gemma-7B on MultiArith: −1.2). Gains above 2 points are concentrated in the weakest models (OlMo-7B, LLaMA2-7B, Mistral-7B), which have low baselines where variance can produce large relative swings. The paper reports no confidence intervals, standard deviations, or statistical significance tests. Given the small effect sizes, the claim that QuestCoT "consistently" helps is not statistically supported as presented.

### Minor

- **The gap between the oracle and QuestCoT is not analyzed.** The oracle experiment (Table 1) suggests the potential headroom is enormous (e.g., OlMo-7B GSM8K: 13.6% → 37.9% with GPT-4 guidance), yet QuestCoT captures only a fraction of that (13.6% → 19.4%). The paper never examines the quality of QuestCoT-generated first steps or explains why the method falls so far short of its own motivating upper bound. Without this analysis, the link between the phenomenon and the proposed solution remains circumstantial.

- **The claim of "consistent performance improvements" is slightly overstated.** The caption of Table 2 says QuestCoT "achieves the best results across all model sizes" and the introduction (line 28) says "consistent performance improvements were observed for all smaller models," but there are two decreases and several near-zero gains. The paper does honestly note the exceptions in the text (line 200), but the framing is more bullish than the data warrant.

- **Error analysis is qualitative only.** The "deeper exploration" (Section 5) provides illustrative examples and error categories, which are informative, but there is no quantitative breakdown (e.g., what fraction of errors does QuestCoT fix vs. introduce?). The Venn diagram (Figure 3) is a step in this direction but is limited to one model (Phi3-mini).

### Trivial

- None substantial; the paper is generally well written.

## Nice-to-Have

- **Comparison to self-consistency / majority voting** would contextualize the gains, since the paper's own motivation (Figure 1) shows that multiple sampling narrows the gap between small and large models. QuestCoT's greedy decoding gains could be compared against a simple multi-sample baseline.
- **A rough token-cost comparison** (average tokens per example for CoT vs. QuestCoT) would help assess the practical trade-off, since the limitations section mentions "some additional cost" without quantification.

## Removed Points

- **Harsh Critic's claim that "Figure 1 oversells" the gap convergence**: The statement "with 35 samples, this gap narrows to less than 10 points" (line 68) is factually accurate from the figure. The critic's assertion that the paper does not "comment that convergence is not complete" is a reading preference, not a flaw.
- **"No comparison to self-consistency or majority voting"** (as a weakness): Self-consistency is a different paradigm (multi-sample + voting) from the paper's focus on improving greedy decoding. It is a reasonable suggestion but not a weakness of the work as scoped. Moved to Nice-to-Have.
- **"Insufficient detail about Subques implementation"**: The paper cites the original Subques papers and describes the difference (adding sub-questions at each step vs. only at the first step). Further implementation details are a minor presentation concern at most.
- **Pure formatting/style nitpicks and speculation about what may be in a missing appendix**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent observation that the paper itself misses.

## Suggestions

1. **Re-run all experiments with prompts drawn from the training set.** This is the single most impactful fix. It will establish clean absolute numbers and may also affect the magnitude (or even direction) of observed gains.
2. **Report confidence intervals or bootstrapped standard errors** for the main comparisons (Table 2). Given small effect sizes, this is necessary to assess reliability.
3. **Analyze QuestCoT-generated first-step quality.** On a sample of 200–300 examples, have human (or LLM-based) judges evaluate whether the self-generated first step is correct. This would directly test the proposed mechanism and explain the oracle-to-method gap.
4. **Provide a per-instance confusion matrix** (CoT correct / QuestCoT correct) to quantify how often QuestCoT fixes errors versus introduces new ones, extending the Venn diagram analysis.
5. **Temper the language.** Replace "consistent performance improvements" and "all models" with more precise phrasing that acknowledges the observed decreases and the range of effect sizes.
