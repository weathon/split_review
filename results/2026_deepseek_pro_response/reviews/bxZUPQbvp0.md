## Summary

EconAgentBench introduces a suite of multi-turn benchmarks for LLM agents in three economic decision-making tasks — procurement, scheduling, and pricing — where the environment is unknown and must be learned through exploration via tool use. The environments are synthetically generated with scalable difficulty (BASIC, MEDIUM, HARD), and the paper evaluates seven frontier LLMs, finding that even cutting-edge models like GPT-5 fail to fully solve any HARD instance. The paper claims three contributions: the benchmark itself, validated difficulty scaling, and economically meaningful behavioral insights beyond aggregate scores.

## Strengths

- **Well-motivated canonical economic environments**: Each task maps to an established economic framework — procurement uses a Cobb-Douglas production function, scheduling is grounded in Gale-Shapley stable matching, and pricing employs a nested logit demand model (Berry, 1994). This ensures the benchmarks assess economically meaningful reasoning rather than arbitrary puzzles.
- **Clean, future-proof tool-use interaction protocol**: The benchmark requires only function calling (Table 1), a capability built into all frontier LLMs, with 3–5 tools per environment. The design avoids dependence on any specific agent framework and is compatible with future models.
- **Synthetic generation for scalability and contamination resistance**: Each environment is parameterized by randomly sampled values, enabling generation of arbitrarily many novel instances. This directly addresses the saturation and data contamination problems identified in related work.
- **Genuinely interesting empirical patterns**: GPT-5 strongly leads on stationary tasks (procurement 75.0, scheduling 90.5) while GPT-4.1 leads on non-stationary pricing (66.8), demonstrating the benchmarks measure different skill dimensions. The striking gap between o4-mini (60.9) and GPT-4o (9.0) on HARD procurement suggests reasoning models have particular advantages in combinatorial exploration — a finding the paper notes but could develop further.
- **Deliberate stationary vs. non-stationary design**: The split between stationary environments (procurement, scheduling — find one good solution) and non-stationary (pricing — continuously adapt to shifting conditions) tests qualitatively different agent capabilities, and the results confirm pricing is substantially harder than the other tasks.

## Weaknesses

### Fatal

None.

### Major

- **No non-LLM baselines make scores uninterpretable**: The paper reports only LLM agent scores normalized against OPT. Without any algorithmic or heuristic baseline — random search, hill climbing, or a classical algorithm adapted to the feedback format (e.g., a Gale-Shapley variant with blocking-pair feedback for scheduling, which is known to be solvable in polynomial time from such feedback) — the reader cannot tell whether a score of 75 in procurement is impressive or poor. For scheduling, the paper does incorporate a uniform-random-matching baseline in the scoring formula, but this is a static reference point, not an active algorithmic competitor. A benchmark paper must establish what performance looks like absent LLM capabilities to support its measurement claims. This gap undermines the interpretability of every result in Table 2.

- **Difficulty scaling validation is weak and partially contradicted by the data**: The paper claims "arbitrary difficulty scaling" as a core contribution (Section 1, item 2). The only validation (Section 4.1) is that HARD scores are lower than BASIC scores at p < 0.05 — confirming only a binary separation. More concerning, several model × environment combinations show MEDIUM and HARD scores that are essentially identical or reversed: o4-mini on scheduling scores 19.3 (MEDIUM) vs. 19.8 (HARD); GPT-4o on scheduling scores −4.5 (MEDIUM) vs. 3.2 (HARD); Claude 3.5 Sonnet on procurement scores 54.5 (MEDIUM) vs. 54.6 (HARD). The paper never acknowledges or discusses these anomalies. The data supports, at best, a binary separation (BASIC vs. everything else) rather than the smooth three-level gradient the paper claims. This is evidential — the data does not support the claimed property.

### Minor

- **No variance estimates or error bars reported**: With only 12 instances per condition and temperature 1, the scores in Table 2 have non-negligible variance. Yet no standard deviations, confidence intervals, or ranges are reported. Bolded "top-2" values (e.g., GPT-4.1 at 66.8 vs. Gemini 2.5 Pro at 62.8 in pricing HARD) are presented as meaningful rankings without evidence that differences exceed noise. This makes the benchmark's primary output — model rankings — scientifically fragile.

- **"Economic insights" analysis is largely correlational**: Section 4.3 presents budget utilization, best-so-far rate, and adaptability as revealing "economically meaningful insights regarding mechanisms." But budget utilization and best-so-far rate are near-tautological performance correlates: models that use more budget and make more improvements naturally score higher. The adaptability metric for pricing is confounded (the second-weakest model, Gemini 1.5 Pro, has the highest adaptability, which the paper acknowledges is "driven by poor-quality actions in the first 10 periods"). The paper itself admits for pricing that "it is challenging to develop metrics that shed insight on differences in performance." The claim of "economically meaningful insights" overstates what Section 4.3 demonstrates.

- **Temperature 1 without justification**: The paper queries all LLMs at temperature 1 (line 75), which introduces avoidable stochasticity. Standard practice in LLM evaluation is temperature 0 for reproducibility. The paper neither justifies this choice nor acknowledges it as a limitation.

- **Nonsaturation claim is borderline for scheduling**: GPT-5 scores 90.5 on scheduling HARD. While not 100 and with 0/12 solve rate, this leaves limited discriminative headroom for future, stronger models. The paper bundles all three environments into a blanket nonsaturation claim without acknowledging that scheduling may saturate sooner than procurement or pricing.

### Trivial

- The paper does not clarify whether the LLM agent is informed that pricing shifts follow a predictable pattern (linear vs. periodic), or must discover this from scratch. This ambiguity affects interpretation of pricing results.
- The 100-period horizon is stated without discussion of whether it is sufficient for the problem scale at each difficulty level (e.g., procurement HARD with n=100, k=10 has an enormous search space).

## Nice-to-Haves

- Add non-LLM baselines (random search, hill climbing, theoretically-informed algorithms) to contextualize LLM scores.
- Report variance (standard deviations or confidence intervals) for all scores in Table 2.
- Deepen the behavioral analysis beyond correlational metrics — e.g., characterize exploration strategies, analyze whether models detect non-stationarity in pricing, and compare exploration patterns of reasoning vs. non-reasoning models.
- Honestly discuss the MEDIUM/HARD anomalies in scheduling and procurement, and consider whether the current difficulty parameterization (n=20→50 for scheduling) produces a meaningful intermediate level.
- Justify or change the temperature 1 choice.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **HC: "No discussion of compute cost or practical feasibility"** — The paper states cost data is in Appendix A, which was stripped by the parser. Cannot penalize for missing appendix content.
- **HC: "Procurement scoring uses best action — a model could get lucky on period 1"** — In stationary exploration tasks, using the best-found solution is standard practice. The distinction from scheduling (which uses the final matching) is reasonable given the task structure. This is a design choice, not a flaw.
- **HC: "The paper does not discuss whether models engage in gaming behavior"** — This is a speculative nice-to-have, not a concrete weakness grounded in the paper.
- **HC: "Cobb-Douglas connection to real procurement is tenuous"** — The Cobb-Douglas production function is a standard, well-established economic model. This criticism reflects a reviewer preference, not a paper flaw.
- **SF: "Experimentally validated difficulty scaling" (as stated by Strength Finder claiming monotonic degradation across all three levels)** — The strength finder's claim of smooth monotonic degradation is contradicted by the MEDIUM/HARD anomalies documented in the Major weaknesses above. The validation only covers BASIC vs. HARD.
- **SF: "Real-world motivation with documented industry adoption"** — This is valid motivation but characterizes the problem importance rather than a contribution of the paper per se. Moved here as it is context, not a research contribution.

## Novel Insights

The paper reveals an interesting pattern that was not obvious a priori: reasoning-capable models (o4-mini, GPT-5, Gemini 2.5 Pro) dramatically outperform standard models on stationary exploration-optimization tasks (procurement, scheduling), but this advantage largely disappears on the non-stationary pricing task where GPT-4.1 (a non-reasoning model) achieves the top score. This suggests that reasoning capabilities are particularly valuable for structured combinatorial search but may not transfer to tasks requiring continuous adaptation to shifting environments — a finding with implications for how we think about LLM agent deployment across different economic contexts.

## Suggestions

- The single highest-leverage improvement is adding at least one algorithmic baseline per environment. For scheduling, an algorithm that uses blocking-pair feedback to iteratively resolve instabilities (building on the known theoretical result that stable matchings are learnable from such feedback, as cited in the paper itself — Bei et al., 2013; Emamjomeh-Zadeh et al., 2020) would provide a compelling comparison point and dramatically improve score interpretability.
- Report confidence intervals via bootstrap over the 12 instances, which is straightforward and would immediately strengthen the comparative claims.
- Consider replacing or augmenting the MEDIUM difficulty level for scheduling, since n=20 with k=2 blocking pairs appears insufficiently distinct from n=50 with k=5.

---

## Calibration Notes

**Round 1 bracket**: Based on comparison with MCU (4.00, rejected), LLM-Deliberation (4.75, rejected), AgentBench (6.20, accepted), AgentQuest (6.25, accepted), HAZARD (6.75, accepted), and high-band anchors (Spider 2.0, PhysBench at 8.00), the paper falls in the **5.0–6.0** range.

**Round 2 narrowing**: Robotouille (5.67, accepted) is the closest anchor — both are benchmark papers for LLM agents with real contributions but significant gaps (Robotouille: only 1 LLM tested, insufficient baselines; EconAgentBench: no non-LLM baselines, weak difficulty validation). EconAgentBench has advantages (7 models, synthetic generation) but also the overclaimed difficulty scaling and missing variance reporting. GridAgent (5.67, rejected) is at a similar level. τ-bench (6.50) is clearly stronger with its well-executed design, new metrics, and comprehensive analysis. The paper is clearly above LLM-Deliberation (4.75) and clearly below τ-bench (6.50).

**Anchor comparison summary**:
- MCU (4.00, R1): EconAgentBench is clearly stronger — better design, clearer writing, more systematic evaluation.
- LLM-Deliberation (4.75, R2): EconAgentBench is stronger — three distinct environments vs. one game template, synthetic generation, better model coverage.
- Robotouille (5.67, R2): Roughly comparable. Robotouille has a more focused task design and failure analysis; EconAgentBench has better model coverage and synthetic generation. Both have baseline/validation gaps.
- GridAgent (5.67, R2): Roughly comparable benchmark paper with similar strengths and weaknesses.
- AgentBench (6.20, R1): EconAgentBench is weaker — fewer environments (3 vs. 8), fewer models (7 vs. 27), no non-LLM baselines, weaker validation.
- AgentQuest (6.25, R2): EconAgentBench is weaker — AgentQuest has more environments and better execution, though both share some analytical gaps.
- τ-bench (6.50, R2): EconAgentBench is clearly weaker — τ-bench has a more polished design, new metrics, comprehensive analysis, and stronger execution.
- HAZARD (6.75, R1): EconAgentBench is weaker — HAZARD includes non-LLM baselines and has more polished execution.

**Final score**: 5.5 — comparable to Robotouille and GridAgent, with genuine contributions (synthetic economic environments, clean tool-use design, interesting empirical patterns) balanced by significant gaps (no non-LLM baselines, weak difficulty scaling validation, no variance reporting, overclaimed economic insights).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>