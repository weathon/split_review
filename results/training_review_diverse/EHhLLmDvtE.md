Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes RISE (eRror-Injected Self-Editing), a preference learning framework that constructs hard negative pairs by prompting the LLM itself to inject predefined subtle errors (miscalculations, substitutions, omissions) into tokens of correct solutions. These self-edited step-level pairs are combined with full-solution DPO pairs for training. Experiments on Qwen2 and Llama-3.1 series (7B–72B) show consistent improvements over base models on GSM8K, MATH, AQuA, and out-of-domain datasets, with RISE-Qwen2-7B achieving 59.9% on MATH (+7.9% over base, +4.1% over Step-DPO).

## Strengths

1. **Novel and well-motivated data construction paradigm**: The idea of having the model itself inject predefined subtle errors into correct solutions to create hard negatives is original and principled. Unlike prior step-wise methods that rely on sampling or external annotation, RISE provides controllable, targeted hard negatives that differ from correct solutions in only a handful of tokens. This is a genuine methodological contribution.

2. **Consistent gains across model scales without external annotations**: RISE improves over base models at both 7B/8B and 70B/72B scales across multiple datasets, using only self-generated data (no GPT-4 annotations, no process reward models). On MATH, RISE-Qwen2-7B (59.9%) outperforms Step-DPO (55.8%) and SVPO (59.5%) despite the latter requiring LLM-based annotations or reward-model approximations. On AQuA, RISE achieves 69.7% vs. Step-DPO's 63.0%.

3. **Targeted error reduction confirmed by analysis**: The error analysis (Figure 2) quantifies that RISE reduces predefined subtle errors more than standard DPO, with manual verification confirming 92% accuracy of the GPT-4o-based error detection. This provides direct evidence linking the method to its stated goal.

4. **Thorough exploration of design choices**: The paper systematically ablates the number of self-edited pairs (Figure 4), sampling attempts (Figure 5), and error-injection compositions (Table 5), yielding non-trivial insights (e.g., more self-edited pairs are not always better; random composition works best).

## Weaknesses

### Fatal
None.

### Major

1. **The ablation does not isolate whether the specific *injected errors* drive improvement, or merely the addition of step-level hard negatives.** The "w/o self-edited pairs" condition removes all self-edited pairs, not just the error-injection mechanism. To support the core claim that injecting predefined subtle errors is the active ingredient, the paper needs a control that compares against *random* step-level negatives — e.g., sampling a random incorrect step from a different incorrect solution, or applying random token perturbation (replacing a number with a random digit) rather than task-cognizant error injection. Without this control, the gains attributed to "targeting subtle errors" could equally come from any form of fine-grained step-level preference regularization. This gap directly affects the paper's central narrative.

2. **The incremental contribution of the novel component (self-edited pairs) is modest on some metrics, yet the abstract/headline numbers conflate the novelty with standard DPO gains.** For Qwen2-7B on GSM8K, the full-solution DPO baseline (w/o self-edited pairs) already achieves 88.3% (+2.9% over base), and adding self-edited pairs yields only +0.1% (88.4%). On MATH, full-solution DPO gains +6.0% and self-edited pairs add +1.7%. While the 1.7% MATH gain is meaningful, the paper's framing "notable improvements of 3.0% on GSM8K and 7.9% on MATH" presents the *total* improvement over base without distinguishing what portion comes from the novel error-injection mechanism. The ablation table is transparent, but the prominence given to headline numbers is misleading.

### Minor

3. **Comparison with Step-DPO is not fully controlled for training data differences.** The paper uses the same 9K problems as Step-DPO but discards the provided solutions, re-samples solutions, and ends up with only ~4.5K problems yielding usable pairs. Step-DPO results are cited from the original paper rather than re-run under matched conditions (same subset, same training size, same backbone checkpoint). While citing baselines is standard practice, the 4.1% MATH advantage over Step-DPO could partly reflect data quantity/quality differences rather than method superiority.

4. **Negative log-likelihood (NLL) loss contributes negligibly (~0.3%) and its stabilizing role is not empirically demonstrated.** The ablation shows the NLL loss barely affects accuracy (e.g., 88.2 vs. 88.4 on GSM8K for Qwen2). The paper motivates it as stabilizing training due to high pair similarity, but no training dynamics (reward divergence, perplexity, gradient norms) are shown to demonstrate instability or stabilization. This component should either be better justified or dropped to simplify the method.

5. **AIME24 results show no improvement, and the paper's explanation is plausible but unsubstantiated.** The paper attributes the lack of gain on AIME24 to "non-subtle errors" but provides no analysis of what kinds of errors the model makes on these problems or why RISE fails to help. Similarly, the claim that Llama-3.1-8B "prefers more self-edited pairs because its solutions contain around three more steps" (Section 3.5) is stated without reporting actual step counts or correlation evidence.

### Trivial
None.

## Nice-to-Haves

- A control experiment using random token perturbation (e.g., replacing a random digit/operator with another random one) vs. task-cognizant error injection would directly validate the design.
- Reporting the success rate and naturalness of error-injected steps (e.g., a small human evaluation of whether edited steps look like plausible mistakes) would increase confidence in the data quality.
- Reporting the raw counts of how often each error operation (REPLACE/SWAP/DELETE) is selected and the α threshold value for the Levenshtein filter would aid reproducibility.

## Removed Points

These are flagged to be removed from the main review but retained here in case they are useful:

- **Missing hyperparameters (β, λ, α, learning rate, batch size, epochs)**: Removed per instruction to treat undisclosed hyperparameters as nitpicks about reproducibility. However, readers should note that the paper omits several training hyperparameters (DPO β, NLL weight λ, Levenshtein threshold α, learning rate, batch size, epochs) that would be needed for exact reproduction.

- **"The 75% figure should be presented as a finding, not a universal premise"**: Removed because the paper clearly references Figure \ref{num_error} which is a specific experimental result, making the claim properly grounded.

- **"Editing prompt not provided in full"**: Removed because the prompt is shown in full in Figure 2 (the edit prompt figure).

- **"The paper speculates Llama-3.1 has more steps without evidence"**: Removed because the paper explicitly states "its full solutions contain around three more steps than those of Qwen2-7B-Instruct" (line 241), which is a factual claim about the collected data, not speculation.

- **"Step-DPO variant not specified for SVPO"**: Removed because SVPO has one main method and further specification is unnecessary for this comparison.

- **"What happens when a step cannot be edited"**: Removed because the paper explains that any token modification disrupts correctness in math solutions, and the LD filter catches unrealistic edits.

## Novel Insights

The most interesting observation arising from this review is that the paper's results inadvertently reveal an important methodological insight: **standard full-solution DPO on self-sampled pairs already accounts for the majority of the gain** (e.g., +6.0 of the +7.9 MATH points for Qwen2-7B), and the error-injected step-level pairs provide a relatively small additional boost. This suggests that the primary mechanism driving improvement in step-wise preference learning for math may be simply exposure to more granular preference signals, with the specific error type being a secondary factor. The finding that more self-edited pairs can hurt performance (Figure 4) further suggests there is a sweet spot for step-level regularization — too many edits overwhelm the training signal. These observations are worth deeper investigation across different preference learning frameworks.

## Suggestions

1. Add a control condition using random step-level negatives (e.g., random token perturbation, or selecting an unrelated incorrect step) to isolate whether task-cognizant error injection is specifically beneficial.
2. Reframe the abstract and introduction to report incremental gains of the self-edited component separately from the total gain, or at least contextualize the relative contribution.
3. Re-run Step-DPO under matched training conditions (same subset of problems, same training size) for a fairer comparison, or soften the comparative claims.
4. Either provide training dynamics showing that the NLL loss stabilizes training, or remove it to simplify the method.
5. Report the α threshold value and the distribution of edit operations selected during self-editing.

## Score and Decision

**Score: 6.0**

**Decision: Accept**

The paper presents a novel, well-motivated framework for constructing hard negative preference pairs through error-injected self-editing. The core idea is creative and the empirical evaluation is broad (two model families, 7B–72B, six datasets). The method consistently improves over base models and achieves competitive or state-of-the-art results without requiring external annotations. However, the paper's central claim — that *specific* error injection drives improvement — is not fully disentangled from the more general benefit of adding step-level hard negatives. The incremental gain of the novel component is modest on some metrics, and the abstract's framing conflates the total gain with the novel contribution. These are significant enough to prevent a higher score, but the paper's contributions are real and the method is clearly useful. With the suggested control experiments, the paper could become a strong contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>