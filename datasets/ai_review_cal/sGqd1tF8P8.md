- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 6, 10, 6
Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper systematically studies whether a weak LLM (e.g., OPT-125M) can serve as a source of preference feedback for aligning larger LLMs via DPO. The proposed pipeline has three stages: train a weak LLM on a small labeled preference set, use it to label a larger unlabeled set, then train the target policy on those weak labels. The headline findings are that weak-LLM feedback matches or exceeds human feedback across model sizes, families, and tasks, and that supervisor model size has minimal impact.

## Strengths

- **Timely and well-motivated research question.** The paper clearly articulates the gap between expensive human annotation (RLHF) and expensive compute (RLAIF with GPT-4), motivating a practical middle ground. The empirical framing is clear and the connection to semi-supervised learning is appropriately noted.

- **Comprehensive evaluation across diverse axes.** The paper tests alignment under weak LLM feedback across four student model sizes (OPT-1.3B to 13B, Figure 2a), three additional model families (Llama-2-7B, Mistral-7B, Gemma-7B, Figure 3a), four supervisor capacities (125M to GPT-4, Figure 2b), multiple label/unlabel ratios (Figure 4a), and a non-dialogue task (TL;DR, Figure 4b). This breadth strengthens the empirical contribution.

- **Diagnostic analysis of label mismatches is insightful.** Section 4's decomposition into matched/mismatched sets reveals that weak LLM errors are not random: in the mismatched samples, 44.3% of the weak LLM's chosen responses have *higher* gold reward than the human-chosen response. The GPT-4 consistency analysis (Table 3, 0.84 vs 0.66) further supports the interpretation that mismatches occur primarily on genuinely ambiguous pairs. This is the most novel analytical contribution.

- **Practical significance.** The finding that a 125M-parameter model fine-tuned on a small labeled set can produce preference labels that enable alignment competitive with human-labeled data has clear practical value for reducing labeling costs.

## Weaknesses

### Fatal
None.

### Major

1. **GPT-4 comparison is not apples-to-apples.** The weak (OPT-125M), moderate (OPT-1.3B), and strong (Llama-3-8B) supervisors are all DPO-fine-tuned on the labeled set D_l before labeling D_u, while GPT-4 labels D_u zero-shot via RLAIF prompting (Section 3.3, lines 145-146). The paper acknowledges GPT-4 "relies solely on prompt engineering" but the framing — "OPT-125M can outperform GPT-4 in providing feedback on preferences" (line 146) — inflates the finding by comparing a task-fine-tuned model against a zero-shot model. The headline claim about supervisor size having "minimal impact" is built partly on this asymmetric comparison. A GPT-4 model given the same labeled data or few-shot demonstrations could perform differently, and this comparison does not establish that supervisor size *per se* is unimportant.

2. **Overclaimed scope from an automated metric.** The paper states that "weak LLM can surpass human judgments" (Section 4, line 236, line 388) based on the observation that in 44.3% of mismatched pairs, the weak LLM's chosen response has higher gold reward. But the gold reward model is itself a learned proxy trained on human preferences (the paper does not specify which model is used or whether its training data overlaps with the evaluation data). An automated metric alone cannot sustain the claim that weak LLM feedback *surpasses* human judgment — it can only show correlation with a particular reward model's preferences. A small-scale human evaluation on a sample of mismatched pairs would be needed to support this claim. The abstract's claim that weak LLM feedback "exceeds that of fully human-annotated data" is similarly too strong given the evaluation setup.

3. **No estimates of statistical uncertainty.** The paper reports only point estimates for gold rewards and win-rates across all experiments (Figures 2-4). No error bars, confidence intervals, or significance tests are provided. Given that the reported differences between conditions are often small (e.g., weak vs. human in Figure 2a), it is impossible to assess whether these differences are meaningful or within the noise of the measurement. This is particularly important for the GPT-4 win-rate analysis (Figure 3b), where ~50% is interpreted as "competitive" without any confidence bounds around the estimate from 100 samples.

### Minor

4. **Gold reward model is underspecified.** The paper never names which "large auxiliary gold reward model" is used (line 126), cites which specific model or training run it comes from, or reports its agreement with held-out human judgments. This significantly limits reproducibility. Given that gold reward is the primary evaluation metric, readers need to know what model was used.

5. **The human-feedback baseline does not control for data quantity from the labeled set.** The pipeline trains the weak supervisor on D_l, so information from D_l flows into the policy trained on weak labels. The human baseline π_h* is trained on D_u only (human labels for D_u), discarding D_l entirely. While this design choice has a practical rationale (the paper wants to estimate "fully supervised data" performance), it means the comparison is not isolating the *source of feedback* — the weak pipeline benefits from training data (D_l) that the human baseline does not see. A stronger control would train an additional human baseline on D_l + D_u (human labels for both). The paper does not report this comparison. The practical finding remains interesting, but the framing as "weak LLM feedback vs. human feedback" overstates what the experiment actually compares.

6. **The GPT-4 win-rate result (~50%) is presented as supporting the claim but is open to different interpretations.** If weak LLM feedback genuinely "surpasses" human feedback, one might expect a win-rate significantly above 50%. The ~50% result is more consistent with the interpretation that the two conditions produce similar-quality outputs, which is a weaker but still valuable finding. The paper should more carefully calibrate the interpretation of this result.

### Trivial
None.

## Nice-to-Haves

- Adding a human evaluation on a random sample of test-set outputs from weak-aligned vs. human-aligned policies would substantially strengthen the main claims.
- Specifying the gold reward model (which model, training data, held-out accuracy) would improve reproducibility.
- Reporting error bars or confidence intervals (especially for the GPT-4 win-rate, which is based on 100 samples) would help assess the reliability of observed differences.
- The discussion comparing to Burns et al. (2023) is somewhat tangential; the paper could be more focused on its own contributions.

## Removed Points

- **Criticism that the gold reward metric is "circular" and that the evaluation cannot distinguish between "weak LLM feedback is better than human feedback" vs. "weak LLM happens to align with this reward model"**: This criticism applies equally to both conditions (both are evaluated with the same metric) and to essentially all automated evaluation in alignment research. The paper also provides GPT-4 win-rate as a second metric. Overstated as a fatal concern — relegated to the caveat about overclaimed scope (Major weakness #2).

- **Criticism that the human baseline is "unfairly disadvantaged" in data access**: Partially valid but overstated. The weak pipeline's use of D_l is integral to the approach, not a confound. The paper's practical framing is that you have a labeled subset and want to avoid labeling the rest. The comparison is meaningful for this scenario. However, an additional control (human baseline on D_l + D_u) would strengthen the analysis — captured as Minor weakness #5.

- **Strength that "controlled experimental design enables direct comparison" (from Strength Finder)**: This conflicts with the verified weakness about data asymmetry. Removed because it overstates the level of control.

- **Strength that "ablation on feedback-source capability is systematically varied"**: Partially valid but the GPT-4 comparison asymmetry undermines the strength of this claim.

- **Complaint about missing appendices or technical details**: The parser strips these; they exist in the original submission.

- **Nitpicks about wording, formatting, or grammar**: Parser artifacts, not author errors.

## Novel Insights

One genuinely novel observation emerges from synthesizing the reviews: the GPT-4 consistency analysis (Table 3) combined with the mismatched-set quality analysis (44.3% of weak LLM "errors" produce higher-quality responses) offers a nuanced resolution to the paper's central puzzle. The weak LLM is not "better" than humans at preference judgment — it is differently calibrated. It agrees with humans on clear-quality-gap examples (60.6% agreement) and disagrees primarily on examples where the quality difference is small enough that even GPT-4 vacillates (0.66 consistency vs 0.84). This suggests that the weak LLM's value lies not in superior judgment but in providing a consistent, low-cost labeler whose disagreements with humans fall mostly on genuinely ambiguous cases where even expert human judgments would have low inter-annotator agreement. This reframes the paper's headline: the result is not "weak LLMs beat human feedback" but rather "on the margin of difficulty where even strong annotators disagree, a weak fine-tuned model's labels are no worse than human labels for training purposes."

## Suggestions

1. Add a human baseline that trains on D_l + D_u (both human-labeled) to control for data quantity. A Figure showing weak feedback vs. this stronger baseline would clarify whether the advantage comes from feedback quality or from the extra labeled data used in supervisor training.

2. Either fine-tune GPT-4 on D_l (or provide few-shot demonstrations) for the supervisor comparison, or explicitly reframe the comparison as "task-fine-tuned small model vs. zero-shot large model" and adjust all claims accordingly.

3. Conduct a small-scale human evaluation on ~200 test-set generations comparing π_θ* vs. π_h* outputs, and on a sample of mismatched preference pairs. This would directly ground the claim about weak LLM "surpassing" human judgment.

4. Specify the gold reward model and report error bars or bootstrapped confidence intervals for key comparisons.

5. Calibrate the language: "matches or exceeds human feedback" would be more accurate as "matches human feedback, and sometimes produces outputs preferred by automated reward models" — a practically useful result that does not require overclaiming.
