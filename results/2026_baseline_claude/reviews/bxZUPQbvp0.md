## Summary
EconAgentBench introduces a benchmark suite for evaluating LLM agents in three unknown economic environments—procurement (Cobb-Douglas utility optimization), scheduling (stable matching with unknown preferences), and pricing (nested-logit demand with non-stationary parameters). Each environment comes in three difficulty levels (BASIC, MEDIUM, HARD) generated synthetically. The paper evaluates seven LLM agents (including GPT-5 and Gemini 2.5 Pro), demonstrates the effectiveness of difficulty scaling, shows the benchmarks are not yet saturated at HARD, and uses secondary behavioral metrics to surface economically meaningful insights about model differences.

---

## Strengths

- **Grounded in canonical economic theory.** The three environments map cleanly onto well-studied economic problems: Cobb-Douglas procurement, Gale-Shapley stable matching, and Berry nested-logit pricing. This grounding gives the benchmark intellectual legitimacy and ensures that "optimal" is always well-defined and computable—an important property for score normalization.

- **Scalable difficulty via instance size with empirical validation.** The paper verifies (one-sided Welch's t-tests, p < 0.05) that HARD instances are harder than BASIC for all agents and all three environments, confirming that instance-size scaling is a principled anti-saturation mechanism rather than an ad-hoc choice.

- **Genuine coverage of exploration under uncertainty.** By withholding effectiveness scores (procurement), worker/task preferences (scheduling), and all demand parameters (pricing), the benchmark specifically tests *deliberate exploration* rather than pattern matching on known facts. This is a real gap in existing benchmarks, which mostly test static question-answering.

- **Interesting cross-model finding.** GPT-5 dominates the two stationary environments while GPT-4.1 (a non-reasoning model) leads on the non-stationary pricing task. This empirically motivates the claim that different environments measure distinct capability dimensions, and raises an economically meaningful question about whether reasoning models are slower to adapt to dynamic environments.

- **Secondary behavioral metrics add analytical depth.** Budget utilization (procurement), best-so-far rate (scheduling), and adaptability (pricing) go beyond scalar scores and help diagnose *why* models differ—e.g., the observation that all three reasoning-model-based agents exhibit high budget utilization is consistent with their known mathematical reasoning strengths.

---

## Weaknesses

### Fatal
None.

### Major

1. **No algorithmic or classical baselines.** Every environment has a well-known polynomial-time algorithm that could serve as an upper bound or calibration reference (e.g., Gale-Shapley for scheduling, LP relaxation for procurement, first-order pricing for the nested logit). Without showing where such baselines fall on the scoring scale, it is impossible to know whether a procurement score of 75 represents near-optimal behavior or is far from tractable. Including even a "random exploration" baseline and a classical-algorithm baseline would dramatically increase the interpretability of every number in Table 2.

2. **Only 12 instances per difficulty level; no uncertainty estimates in Table 2.** With 12 instances, individual model comparisons in Table 2 (e.g., o4-mini 60.9 vs. Claude 3.5 Sonnet 54.6 on HARD procurement) may not be statistically distinguishable. The paper reports t-tests for the difficulty-scaling claim but not for any pairwise model comparison. Presenting standard errors or confidence intervals alongside the point estimates in Table 2 is necessary for readers to judge whether the ranking is reliable or noise-driven.

3. **Pricing analysis is explicitly acknowledged as inconclusive.** The paper states that "without high-scoring LLM agents, it is challenging to develop metrics that shed insight on differences in performance" and characterizes the adaptability analysis as "preliminary." Yet pricing is presented as an equal third pillar of the benchmark. A benchmark paper should either provide meaningful analysis of all three components or clearly scope the contribution accordingly.

### Minor

1. The 100-period horizon is fixed without justification. For the scheduling environment, blocking-pair feedback grows quadratically with matching size, so the information available per period is not comparable across BASIC and HARD—this could confound difficulty-scaling conclusions.

2. The success metric for pricing (average over last 50 of 100 periods normalized by OPT) lumps together very different behaviors in the last 50 periods. A model that learns quickly and then degrades is treated the same as one that learns slowly and stabilizes. A more granular temporal plot would be informative.

3. Temperature is fixed at 1 for all models. Given that reasoning models (o4-mini, GPT-5) often have their own internal temperature handling, this may not be a meaningful or equivalent control across model families.

### Trivial
- Negative scores in scheduling (possible when the agent's final matching is worse than uniform random) are not intuitive; a brief reminder of this interpretation in the Table 2 caption would help readers.

---

## Nice-to-Haves

- Ablation over the number of periods to test how quickly each model saturates its performance within a run (learning curves), which would make the benchmark more informative for practitioners choosing how many API calls to budget.
- A simple greedy or random-exploration agent (non-LLM) as a baseline across all three environments to anchor the scale.
- A brief discussion of how the benchmark could extend to multi-agent scenarios (e.g., competitive pricing, bilateral matching markets with strategic agents), which is a natural next frontier.

---

## Novel Insights

The most genuinely novel empirical insight is the *differential advantage of reasoning vs. non-reasoning models across stationary and non-stationary settings*: GPT-5 and o4-mini (reasoning models) excel at stationary procurement and scheduling, while GPT-4.1 (non-reasoning) leads at non-stationary pricing. This pattern—if robust across more instances—would suggest that chain-of-thought reasoning, while useful for solving fixed optimization problems through deliberate search, may hinder adaptive behavior in dynamic environments where confident plan-revision is more valuable than careful deliberation. This is an economically and algorithmically interesting hypothesis that future work could test more rigorously.

---

## Suggestions

- Add standard deviations or 95% confidence intervals to all entries in Table 2; include pairwise significance tests for the HARD model comparisons.
- Include at least one non-LLM baseline per environment (e.g., Gale-Shapley for scheduling, greedy hill-climbing for procurement) to calibrate the scoring scale.
- Show per-period learning curves for at least one representative model per environment to illustrate what "improvement over time" actually looks like and validate the 100-period design choice.
- Increase the instance count from 12 to at least 30 per difficulty level to support reliable model ranking conclusions.

---

## Score and Decision

EconAgentBench addresses a real and growing need—rigorous evaluation of LLM agents in structured economic decision-making—and does so with principled benchmark design grounded in economic theory, scalable synthetic generation, and an interesting multi-model evaluation. The main limitations are the small instance count (constraining statistical power for model comparisons), the absence of algorithmic baselines (limiting score interpretability), and the underdeveloped pricing analysis. These are substantive issues for a benchmark paper, but they do not invalidate the core contribution: the benchmark environments themselves are sound, and the overall framing and initial findings are valuable to the community.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>