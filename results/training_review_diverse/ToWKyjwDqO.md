Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces a family of generative judge models (8B, 12B, 70B) trained with Direct Preference Optimization (DPO) on three complementary types of preference data: Chain-of-Thought Critique (for reasoning), Standard Judgement (for direct supervision), and Response Deduction (for understanding good/bad responses). The models are evaluated across 13 benchmarks spanning pairwise comparison, single rating, and classification tasks. The largest model achieves top performance on 10/13 benchmarks, surpassing GPT-4o and prior specialized judge models.

## Strengths

1. **Novel application of preference optimization to generative judge training.** The paper is the first to apply DPO to train LLMs as generative judges, moving beyond the standard SFT paradigm used by prior work (Prometheus, FLAMe, Auto-J, etc.). The motivation—that SFT only teaches models to imitate correct reasoning without learning to avoid incorrect judgements—is well-articulated and supported by citations (Section 2). The three-pronged data construction (CoT critique, standard judgement, response deduction) is a systematic design that targets distinct capabilities.

2. **Causal evidence through task-level ablation.** The ablation study (Figure 4, Section 5.4) concretely shows that removing any one of the three training tasks degrades performance on pairwise and classification tasks. This provides direct evidence that all three data types contribute to a well-rounded judge, going beyond a simple "our method works" claim.

3. **Comprehensive evaluation across diverse benchmarks.** The paper evaluates on 13 benchmarks across 3 task types (pairwise, single rating, classification) spanning safety, reasoning, instruction following, factuality, and bias. The 70B model achieves the best performance on 10/13 benchmarks, including being the first generative judge to exceed 90% on RewardBench (Section 5.2).

4. **Demonstrated practical properties.** The models show strong robustness to position and length biases (91.41% average consistency for the 70B model), flexibility across different prompting strategies (Section 5.4), and downstream utility as reward models for improving a separate generator model via DPO (Figure 5).

## Weaknesses

### Fatal
None.

### Major

1. **The advantage of DPO over SFT is not directly tested.** The paper repeatedly motivates its approach by arguing that SFT is suboptimal (Section 2: "SFT alone is known to be suboptimal"; Section 3: "via preference optimization instead of pure SFT"), yet it never includes an ablation that keeps the data constant and varies only the training objective (DPO+SFT vs. pure SFT on the same positive examples). Every baseline comparison (Prometheus, Auto-J, FLAMe, etc.) confounds the training objective with differences in data composition, teacher models, and scale. The observed gains could therefore be driven primarily by the new data curation pipeline rather than by preference optimization per se. Given that the paper uses a combined DPO+SFT loss (Eq. 1 already includes a length-normalized SFT term), adding a pure-SFT baseline trained on the same positive examples would be straightforward and would substantially strengthen the central claim.

2. **"Best of two runs" reporting for pairwise comparisons inflates results in a non-standard way.** The evaluation procedure (Section 4.2) states: "we run each benchmark twice, exchanging the order of responses in the second run. We report the best performance of these two runs." This practice (a) makes headline numbers depend on arbitrary swap assignment, (b) systematically overstates accuracy by cherry-picking the favorable ordering for each sample where the model is inconsistent, and (c) deviates from the community standard of reporting averaged accuracy or consistency-gated accuracy (accuracy only on samples where the judge agrees with itself). While consistency is analyzed separately (Table 5), the main results in Tables 1–3 are the "best-of-two" numbers. This is especially problematic given that some of the performance margins over baselines are narrow (0.5–1%). The paper should report averaged accuracy or consistency-gated accuracy as the primary metric.

### Minor

3. **Potential evaluation benchmark overlap with training data is not systematically ruled out.** The training data description (Section 4.1) is vague: "take inspiration from the datasets proposed by [FLAMe]" and "utilizing datasets similar to those used by several other judge models [Prometheus, OffsetBias, Skywork-Critic, Self-Taught]." Several evaluation benchmarks—PreferenceBench (in-domain for Prometheus 2), EvalBiasBench (from OffsetBias), and parts of RewardBench—could share data sources with the training set. The paper explicitly addresses this concern for LLM-AggreFact by using an older version, but no analogous check is provided for other benchmarks. A training/evaluation disjunction table would significantly strengthen confidence in the results as evidence of generalization rather than memorization.

4. **Unusual length-normalized SFT loss without justification.** The SFT term in Eq. 1 normalizes the log-likelihood by the total sequence length: $-\log M_s(y_i^w|x_i)/(|y_i^w|+|x_i|)$. Standard SFT loss does not include this normalization. The choice is not motivated, and no ablation studies its effect. If the normalization meaningfully changes behavior (e.g., by down-weighting longer critiques), this should be explicitly discussed and ablated. Similarly, the DPO coefficient $\beta$ is never reported or ablated.

5. **Negative example quality is unanalyzed.** For the CoT Critique preference pairs and the Response Deduction task, the weaker teacher (Llama-3.1-8B-Instruct) generates negative examples. If the weaker teacher frequently generates responses close to the positive, the preference signal may be weak. The paper does not report how often the teacher's judgement matched ground truth, the distribution of negative quality, or how many negatives were discarded. This analysis would help assess data quality.

6. **Bias claim is slightly overbroad.** The section title claims "Our models are less biased than comparable judge models," but on EvalBiasBench the models trail Llama-3-OffsetBias (a comparable 8B model). The paper does acknowledge this ("trailing only Llama-3-OffsetBias"), so the claim is technically true but somewhat misleading without this caveat in the title. The strength in bias mitigation is mainly in positional consistency, not across all bias categories.

7. **Prompt ablation limited in scope.** The fixed-prompt robustness test (Section 5.4) is conducted only on the 8B model and only on pairwise benchmarks. It is unclear whether the 70B model—which is more capable but might be more sensitive to prompt variations—exhibits the same robustness.

### Trivial

8. **No limitations section.** The paper lacks a discussion of limitations (e.g., reliance on a 70B teacher which may propagate biases, cost/scalability of 680K preference pairs, limited evaluation on non-English or domain-specific settings). While common in conference submissions, its absence is noticeable given the paper's comprehensive evaluation.

9. **Response deduction motivation is briefly stated.** The intuition that "such a reverse task helps our model to understand the evaluation task in hindsight" (Section 3.3) is plausible but the mechanism is not elaborated. The ablation validates it empirically, so this is a presentation issue rather than a substantive gap.

## Nice-to-Haves

- An SFT-only ablation (trained on the same positive examples, same data) would directly validate the benefit of preference optimization and address the paper's core motivation.
- Reporting consistency-gated accuracy or averaged accuracy (over the two orderings) as the primary pairwise metric, with "best-of-two" as a supplementary statistic, would align with community standards.
- A training/evaluation data disjunction table showing overlap checks for each evaluation benchmark would address leakage concerns.
- An analysis of the DPO coefficient $\beta$ and the length-normalization in the SFT loss would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No significance testing or variance reporting"** — REMOVED. With temperature-0 decoding for non-proprietary models, there is no sampling variance. The "best-of-two" procedure does introduce order-effect variance, but this is already addressed under the "best of two runs" weakness (Major #2). Significance testing is not standard for this type of LLM benchmark paper, and the two runs provide insufficient samples for meaningful statistical tests.
- **"Reference answers provide unfair advantage"** — REMOVED. Providing reference answers (gold-standard responses) in single-rating benchmarks is standard practice in the Prometheus/FeedbackBench evaluation paradigm, and all baselines have equal access to the same information.
- **"Response deduction motivation is hand-wavy"** — DOWNGRADED to Trivial (#9). The ablation validates it empirically, so the brevity of the intuition is a presentation issue, not a substantive gap.
- **"Hyperparameter sensitivity (β, length normalization)"** — The length normalization point is kept as Minor (#4). The β coefficient is a standard DPO parameter; requesting its full ablation is a nice-to-have, not a weakness.

## Novel Insights

The most striking finding that emerges across the reviews is the sharp tension between the paper's clear empirical success (SOTA on 10/13 benchmarks, first generative judge above 90% on RewardBench) and the methodological gaps that prevent clean attribution of that success. The responses achieve strong results, but the evaluation reporting choices ("best of two runs") and the missing SFT ablation mean the paper cannot definitively answer whether the performance comes from preference optimization, the data curation pipeline, the evaluation procedure, or some combination. This is a recurrent pattern in the judge-model literature—impressive empirical results that lack the controlled ablations needed to isolate *why* they work. The paper's three-task data design and the task-level ablation are genuine contributions; the missing pieces are in experimental design and reporting, not in the core idea.

## Suggestions

1. **Add an SFT-only baseline:** Train the same base models on the same positive examples (removing the DPO loss and negative examples) and compare on all 13 benchmarks. This single addition would directly validate the paper's central thesis.
2. **Fix pairwise evaluation reporting:** Replace "best of two runs" with either (a) average accuracy across the two orderings, or (b) consistency-gated accuracy (accuracy on samples where the judge agrees with itself). Report "best of two" only as supplementary.
3. **Provide a training/evaluation disjunction table:** List every training dataset and every evaluation benchmark, with explicit checks for overlapping instances.
4. **Justify or ablate the length-normalized SFT loss** in Eq. 1, and state the DPO β value.

## Score and Decision

This paper makes a genuine contribution: it is the first to apply DPO to generative judge training, introduces a well-motivated three-type preference data construction, and achieves strong empirical results across a comprehensive evaluation suite. The core idea is sound and the task-level ablation provides causal evidence for the multi-task data design. However, the paper has two major methodological weaknesses—the missing SFT ablation and the non-standard "best of two runs" evaluation—that prevent clean interpretation of its central claims. These are fixable in revision and do not invalidate the contribution, but they are substantial enough that the paper would be stronger with these addressed. On balance, the novelty, importance, and empirical strength outweigh the methodological gaps, which are clearly addressable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>