Now I have all the information needed to write the final consolidated review.

---

## Summary

This paper introduces LASeR, a method that iteratively trains LLMs using multiple reward models by casting RM selection as a contextual multi-armed bandit problem (LinUCB). Instead of ensembling all RMs simultaneously (which is computationally expensive and susceptible to conflicting signals) or committing to a single fixed RM (which may not generalize), LASeR selects one RM per batch based on query embeddings and observed training loss. The paper demonstrates gains across reasoning benchmarks (Table 1), instruction-following (Figure 2/3), and long-context best-of-n sampling (Table 3), along with wall-clock efficiency improvements.

## Strengths

- **Consistent gains across two model families on reasoning tasks (Table 1).** LASeR with Llama-3-8B achieves 76.32% average accuracy (+1.45% over the best single RM, +2.67% over RM ensemble), and the same pattern holds for Mistral-7B. LASeR is the only method that ranks first on all three datasets for both base models, while second-place methods vary.

- **Automatic adaptation of RM selection to query type, validated by per-category utilization analysis (Figure 7).** On WildChat, LASeR learns to favor Olmo/Eurus for creative-writing queries and Qwen for math queries — matching each RM's known strengths on RewardBench subsplits — without ever seeing the leaderboard. This is the most compelling evidence that the bandit is doing something meaningful beyond random selection.

- **Demonstrated robustness to noisy rewards (Figure 3).** When Gaussian noise (σ=0.3) is added to RM scores, LASeR suffers only a 0.55% accuracy drop on GSM8K versus a 1.6% drop for the sequential baseline. The Exp3 variant drops only 0.26%. This directly validates one of the paper's core motivations.

- **Significant efficiency advantage in wall-clock time (Figure 4).** LASeR trains in ~1/3 the time of sequential RM selection and ~1/2 the time of the offline RM ensemble, while achieving higher accuracy. The efficiency claim is concretely quantified.

- **Strong instruction-following performance on heterogeneous open-ended prompts.** On WildChat, LASeR achieves 71.45% AlpacaEval win rate against sequential RM selection and 56.34% against the best single RM, demonstrating the method's effectiveness when gold labels are unavailable.

- **Thorough analysis of conflicting RM signals (Figure 6).** The agreement analysis shows that RM pairwise preference agreement can be as low as 0.43 on MMLU and even lower on WildChat, concretely justifying why naive ensembling can be problematic and motivating LASeR's selective approach.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution — adaptive RM selection via a contextual bandit — is sound, supported by evidence, and clearly described. The weaknesses below are addressable without undermining the central claims.

### Minor

- **No variance or statistical significance reporting for main results.** Table 1 reports single accuracy values. The paper does not indicate whether results are averaged over multiple seeds, report standard deviations, or provide significance tests. Given that the margins over the best single RM are modest (~1.45%), and Sequential/Random baselines required 2.5× more training iterations, variance information is needed to assess robustness. This does not invalidate the results (which are consistent across two model families and multiple tasks), but it lowers confidence in the exact magnitudes reported.

- **The "Best RM" baseline understates what per-task selection could achieve.** The "Best RM" baseline uses Zephyr-7B-Alpha (highest overall RewardBench score). As the utilization analysis shows, for specific domains another RM would be more suitable. A per-dataset or per-task oracle baseline (selecting the best RM for each dataset from a development set) would give a more accurate upper bound for single-RM methods. The paper acknowledges this limitation (line 185-187), so this is a scope-for-improvement rather than a flaw, but the framing in the abstract and introduction suggests a broader claim than the comparison fully supports.

- **No discussion of the LinUCB α exploration parameter.** The α parameter in LinUCB (line 133) controls the exploration-exploitation tradeoff and is critical to the method's behavior. The paper does not report how α was chosen, whether performance is stable across a range of α values, or any sensitivity analysis. Given that sequential (full exploration) and best-RM (full exploitation) baselines are compared, readers need to know how sensitive LASeR is to this parameter.

- **Convergence stopping rule not specified.** The paper states models were trained "to convergence" based on dev set performance, but does not specify the stopping rule (e.g., no improvement over N iterations). This matters because the sequential/random baselines required 2.5× more iterations than LASeR — if the stopping rule favored early-stopping methods, the comparison could be affected.

- **Computational overhead of context embeddings not quantified.** The method computes a sentence embedding (last-token embedding from the policy model) for each batch to serve as the MAB context. The paper does not discuss the cost of these forward passes or whether they are subsumed by the response generation step. For Llama-3-8B this is unlikely to be prohibitive, but a brief quantification would help.

### Trivial
- The paper does not report the actual RewardBench scores for the four RMs used, which would help readers calibrate their relative strengths beyond the qualitative descriptions.

## Nice-to-Haves
- An "Oracle RM" column in Table 1 that selects the single best RM per dataset (based on validation performance) would give a tighter upper bound and more honestly quantify LASeR's advantage over single-RM approaches.
- A sensitivity analysis for the LinUCB α parameter across a few values would strengthen the robustness claims.
- Reporting results over 3 seeds with standard deviations would significantly increase confidence in the main results.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The long-context Best-of-n setting has an unclear MAB reward mechanism"** — REMOVED. The reviewer claimed the bandit has "no learning signal at all" because LLM weights don't change. This is a misunderstanding. The paper states (line 153) the MAB reward is the "negative normalized NLL loss on the train data," where the "best" response is selected by the chosen RM. Different RMs select different responses, producing different NLL values. The bandit therefore receives a different reward depending on which RM was selected and can learn. The mechanism is described sufficiently.

- **"Sequential baseline trained for 25 iterations vs 10 for LASeR suggests unfair comparison"** — REMOVED as framed as a weakness. The paper explicitly states that all methods were trained to convergence on a dev set; sequential methods took longer to converge. This is informative of the methods' relative efficiency, not a flaw in the comparison.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface a novel angle not already present in the paper's own analysis (the utilization analysis showing per-query RM adaptation, and the agreement analysis quantifying RM conflict, are the paper's own insights).

## Suggestions

1. Add a brief sensitivity analysis for the LinUCB α parameter to the existing analysis section. This would address the most substantive open question about the method's robustness.
2. Add a note clarifying that in the Best-of-n setting, the MAB reward varies per RM because different RMs select different "best" responses, leading to different NLL values. The current description is correct but could be made more explicit.
3. Report standard deviations or confidence intervals for the main reasoning results (Table 1), even if only over 2-3 seeds, to help readers assess the reliability of the reported margins.
4. Add the RewardBench scores of the four RMs used in the experimental setup for reader calibration.
5. Clarify the stopping rule used for convergence, even briefly (e.g., "no improvement on dev set for 3 consecutive iterations").

## Score and Decision

The paper introduces a practical, well-motivated method with strong empirical support across multiple domains (reasoning, instruction-following, long-context), two model families, and thorough diagnostic analyses (robustness, utilization, agreement). The weaknesses are addressable clarifications and standard reporting improvements — none threaten the core contribution. The paper is a solid contribution worthy of acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>