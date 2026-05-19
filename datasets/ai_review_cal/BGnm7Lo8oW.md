- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6
Now I have a complete understanding. Let me write the consolidated review.

## Summary

This paper investigates what constitutes a suitable reward function for self-improving Chain-of-Thought (CoT) reasoning on unstructured text at pretraining scale — a setting where traditional accuracy-based rewards fail. The authors introduce Reasoning Advantage (RA), a normalized, clipped loss-based reward that uses an empty-CoT baseline. Through systematic experiments on "what" reasoning is rewarded and "where" reasoning is useful, they show RA outperforms standard loss and delta loss. On a newly introduced MMLU-FREE-FORM benchmark, RA is the only reward function that enables self-improvement, yielding a ~7% zero-shot transfer improvement on GSM8K. The paper is honest about the limitations on fully unstructured text (OpenWebMath), where insufficient CoT diversity is identified as the key bottleneck.

## Strengths

1. **GSM8K transfer result is concrete and convincing**: Section 5.2 (Figure 2b) shows RA improves zero-shot GSM8K accuracy by ~7%, while all other reward functions yield <0.5% improvement. This is the strongest evidence that RA enables genuinely generalizable reasoning improvement, not just fitting to the reward metric.

2. **Systematic what/where analysis of reward functions**: Section 5.1 (Tables 2-4, Figure 1) compares reward functions on two distinct diagnostic tasks — classifying CoT quality (correct/incorrect/random) and identifying optimal CoT insertion locations. RA achieves the best accuracy (66.3%) and AUC (77.0%), substantially ahead of delta loss (58.3%, 64.4%) and standard loss (44.6%, 39.4%). The analysis reveals concretely why standard loss fails (it cannot distinguish incorrect from random CoTs) and why normalization helps (it discounts locations where the suffix is trivially predictable).

3. **MMLU-FREE-FORM is a well-motivated intermediate benchmark**: The dataset cleanly isolates the challenges of free-form QA (no exact-match verification, variable answer structure) while retaining a higher density of reasoning opportunities than raw web text. This enables controlled experiments that would be infeasible on fully unstructured corpora.

4. **Honest diagnosis of the pretraining-scale failure**: Section 6.1 candidly reports that offline RL with RA on OpenWebMath yields only 0.01% of CoTs above threshold and identifies the root cause as insufficient CoT diversity, not a reward function failure. The paper correctly separates the reward quality problem from the exploration problem, providing a clear direction for future work.

## Weaknesses

### Fatal
None.

### Major

1. **RA formula is ambiguously specified**: The definition of RA is garbled by the PDF parser on line 113, but the surrounding text indicates it is "clipped delta loss normalized by the Empty CoT baseline," following the general form `(R-B)/B` from line 99. Since both R_clipped and the empty-CoT baseline B_clipped are negative (log probabilities ≤ 0), the formula `(R_clipped - B_clipped) / B_clipped` would produce a *negative* RA for better CoTs and a *less negative* or positive RA for worse CoTs — inverting the intended ranking. The paper's own empirical results (Figure 1, Table 2) unambiguously show RA correctly ranks CoTs (correct > incorrect > random), so the implementation must use a different normalization (e.g., dividing by |B_clipped| or -B_clipped). The paper needs to provide an exact, unambiguous formula. This does not invalidate the empirical results — the method clearly works — but it is a reproducibility barrier that must be resolved.

2. **In-domain evaluation on MMLU-FREE-FORM partially overlaps with the reward signal**: The "expected accuracy" metric on the MMLU test set (P(answer|question, generated CoT)) is the same form of quantity that RA maximizes during training (log-likelihood of the suffix). While the held-out test set and different questions mean this is not strictly circular, it reduces the evidential weight of the in-domain result. The GSM8K transfer result (exact-match accuracy on math word problems) is the non-circular evidence, and it is strong — but the paper presents both as co-equal evidence. A clearer distinction between the in-domain result (which shows RA training doesn't collapse) and the transfer result (which shows genuine generalization) would strengthen the paper.

3. **The RA filtering threshold (0.2) is stated without principled justification**: The paper says this threshold "is a decent threshold for 'good reasoning' in our experience" (line 181). For the MMLU-FREE-FORM experiment, using different absolute thresholds for different reward functions may create an unfair comparison — functions with tighter thresholds (fewer, higher-quality CoTs) versus looser ones (more, lower-quality CoTs). The paper partially addresses this by plotting against training steps, but a controlled comparison (e.g., keeping the same number/fraction of CoTs for each reward function) would be cleaner.

### Minor

1. **Absolute GSM8K baseline accuracy not reported**: The paper reports RA "improving accuracy on [GSM8K] by nearly 7%" but does not state what the base accuracy is. This makes it hard to assess whether this is a 7 percentage point improvement or a 7% relative improvement, and from what starting point.

2. **Clipping threshold ε is undefined**: The paper defines clipping but never states the value of ε used in experiments. If it is a hyperparameter, it should be reported and ideally ablated.

3. **Only Mistral-7B is used**: The experiments use a single model family. Replication on another 7B model (e.g., Llama-2-7B) would strengthen the generality claims. Given the "academic compute" constraint, this is understandable but worth noting as a limitation.

### Trivial
None.

## Nice-to-Haves
- Include a qualitative analysis showing examples of CoTs selected by RA vs. other reward functions on MMLU-FREE-FORM, demonstrating that RA-selected CoTs contain more genuine reasoning rather than answer repetition or summarization.
- Report exact-match accuracy on MMLU-FREE-FORM in addition to "expected accuracy" for consistency with the GSM8K evaluation.
- A worked numerical example of RA computation would resolve the formula ambiguity and help readers understand the normalization.

## Removed Points
The following points from the input reviews were removed with justification:

- **"Missing related works (Quiet-STaR already did this)"** — FACTUALLY WRONG. The paper discusses Quiet-STaR in Section 3 (lines 76-77) and compares to the "Average reward" baseline used by Quiet-STaR in Table 3. The paper's claim of being "first to provide this type of analysis on reward functions" refers specifically to the what/where analysis of reward properties, which Quiet-STaR did not provide.
- **"Random CoT is a strawman"** — The experiment already includes "incorrect" CoTs (GPT-4o without post-rationalization) as a stronger baseline, with "random" CoTs serving as a lower-bound sanity check.
- **"Code/dataset release concerns"** — The paper states it will open-source all code and MMLU-FREE-FORM. Per hard rules, questioning the existence/availability of cited entities is not permitted.
- **"Statistical significance should use paired bootstrap tests"** — The paper already uses 95% bootstrap confidence intervals, which is standard for this type of evaluation.
- **"Missing appendix content"** — Parser strips these; they exist in the original submission.
- **"Missing hyperparameter details (ε, etc.)"** — The clipping threshold ε is an implementation detail; its absence is at most minor. It has been noted as a minor weakness above.
- **Generic strength "computationally feasible experimental design"** — Generic; not a concrete strength specific to this paper's contribution.
- **Generic strength "desirable criteria established and validated"** — Overlaps with specific strengths already listed; kept only the specific empirical validations.

## Novel Insights

The most interesting observation emerging from the synthesis is the *separation of reward quality from exploration quality* in the pretraining-scale experiment (Section 6.1): RA correctly identifies good CoTs when they exist (only 0.01% pass the threshold, and those that do are genuinely superior to the rest), yet the method fails because the generation process never produces sufficiently diverse CoTs. This cleanly isolates the bottleneck as an *exploration problem* rather than a *credit assignment problem*, which is a non-obvious finding — many works in this space assume the reward function is the limiting factor. The implication is that progress on this task may come more from advances in diverse CoT generation (online RL, quality-diversity algorithms) than from further reward engineering.

## Suggestions

1. **Clarify the RA formula**: Provide an unambiguous equation in standard mathematical notation. Given the empirical results, it is likely that RA = (R_clipped(p,r,s) - R_clipped(p,"",s)) / |R_clipped(p,"",s)| or equivalent. Include a worked numerical example to demonstrate that better CoTs receive higher scores.

2. **Restructure the evaluation narrative**: Present the GSM8K transfer result as the primary evidence of generalization, and position the in-domain MMLU-FREE-FORM result as a sanity check (demonstrating that RA training does not collapse or overfit). Explicitly acknowledge the overlap between the reward metric and the in-domain evaluation metric, and explain why the transfer result avoids this concern.

3. **Ablate the threshold**: In the MMLU-FREE-FORM experiment, compare filtering by (a) the absolute RA threshold of 0.2, (b) keeping the top-k CoTs per question, and (c) keeping the same number of CoTs as other reward functions naturally produce — to verify that RA's advantage is not an artifact of more aggressive selection.
