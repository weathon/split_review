Here is the consolidated review.

---

## Summary

Robotouille introduces a cooking-simulator environment and benchmark designed to test LLM agents on *asynchronous planning* — handling tasks with time delays (e.g., waiting for food to cook), interleavable subtasks, and multi-agent scenarios. The paper provides three datasets (synchronous, asynchronous, multi-agent) with 10 tasks × 10 procedural instances each, evaluates I/O, I/O CoT, and ReAct baselines on GPT-family models, and presents a failure-mode taxonomy organized by MDP uncertainty components. The headline result is that ReAct (gpt-4o) achieves 47% success on synchronous tasks but only 11% on asynchronous ones.

## Strengths

- **Novel and motivated benchmark gap.** The paper correctly identifies that existing interactive benchmarks (ALFWorld, WebShop, VirtualHome) lack time-delayed actions, and AsyncHow is non-interactive. Robotouille fills a genuine gap by providing an interactive environment where agents must reason about time delays and interleavable subtasks. The comparison in Table 1 makes this gap explicit.

- **Principled MDP formulation with explicit timer variables.** The formalism extending the standard MDP with timer variables $H_t$ and countdown functions $h(x)=d-(x-i)$ (Section 2) is a clean way to model time-delayed effects within a step-based framework, enabling provably optimal plan comparison and quantitative optimality rates.

- **Structured failure-mode taxonomy by MDP uncertainty.** Categorizing failures by which component of the MDP the agent is uncertain about (state, actions, transition function, goal) is more systematic than typical qualitative failure analyses. The nested pie charts (Fig. 5) and the repeated-transitions analysis (Fig. 6) provide concrete diagnostic value — revealing that transition-function uncertainty dominates async failures (56.8%) while goal uncertainty dominates sync failures (64.1%).

- **Flexible goal specification system.** The language goal system that captures a combinatorial number of satisfying states (e.g., "lettuce and cheese must be somewhere at the table" allowing any arrangement) is more realistic than exact-state matching used in most prior benchmarks and is a thoughtful design contribution.

- **Follow-up investigation with ReAct+Prior.** The ablation showing that explicit rule priors reduce 'one item at a station' violations by 50% (8→4 failures out of 30 runs) provides causal evidence about the specific bottleneck, even though the overall performance gain was statistically insignificant.

## Weaknesses

### Major

- **The sync vs. async comparison is confounded by multiple complexity dimensions.** The asynchronous dataset differs from the synchronous dataset along several axes simultaneously: ingredients start uncooked (introducing time delays), more station types are present (stoves, fryers, sinks), the "one item at a station" rule applies across more stations, and task horizons are longer (new recipes: fried items, soup). The paper's own failure analysis (Finding 4) shows that the dominant async failure is transition-function uncertainty (56.8%), specifically violating the "one item at a station" rule (53.4%) — which the paper itself notes "mainly observe[s] similar transition failures in both settings." Without a controlled ablation (e.g., an async variant with cooking times set to zero to isolate complexity from timing), the 47%→11% performance gap cannot be confidently attributed to asynchronous planning requirements rather than general planning difficulty in a larger state space. This undermines the benchmark's core construct validity claim.

- **Baseline coverage is too thin for a benchmark paper.** Only three baselines are evaluated: I/O, I/O CoT (2023), and ReAct (2022). No more recent agent architectures are tested — no Reflexion, Tree-of-Thought, Plan-and-Solve, RAP, Code-as-Policies, or any open-source LLM agents. For a benchmark intended for community adoption at ICLR in 2025/2026, this evidence base is insufficient to demonstrate that the benchmark discriminates meaningfully between methods of varying sophistication, or that the difficulty is not trivially surmountable by a slightly better approach.

- **Main quantitative results lack statistical reporting.** The headline numbers (47%, 11%) are reported as point estimates with no confidence intervals, standard errors, or significance tests, despite using stochastic sampling (temperature 0.7) over only 100 runs per setting. In the one place uncertainty is reported (ReAct vs. ReAct+Prior on Tasks 1–3, 30 runs each), the result is "statistically insignificant" with large standard errors relative to the difference. A benchmark paper's central quantitative comparisons should be accompanied by uncertainty quantification to establish reliability.

- **Only proprietary GPT models are evaluated.** All experiments use gpt-4o, gpt-4, and gpt-3.5-turbo. No open-weight models (Llama 3, Mistral, Qwen, etc.) are tested. This limits reproducibility for researchers without API access, raises the question of model-specific findings, and raises the barrier to entry for the community to use the benchmark.

### Minor

- **The follow-up findings rest on very small samples.** Finding 2 (async successes are less optimal) is based on approximately 11 successful async runs (~11% of 100). Finding 6 (prioritization boosts performance: 16% vs. 6%) does not specify how many runs were in each group or whether the categorization was post-hoc. Finding 7 is explicitly "statistically insignificant." These are honestly reported but the paper draws conclusions from them that are not supported by the data.

- **The optimal planner used for optimality ratios is never specified.** The paper computes $\|\tau^*\|$ as the "number of steps taken by an optimal planner" but never describes what this planner is, how it was obtained (hand-coded BFS? exact solver?), or whether optimality is guaranteed. This affects the validity of the optimality rate metric and the step-limit cutoff (1.5× optimal).

- **The paper does not state whether the environment, datasets, and evaluation code will be released.** For a benchmark paper, this is a standard expectation that should be explicitly stated.

- **The multi-agent dataset is listed as a contribution (#2) but entirely unevaluated.** While the paper transparently says "leaving multi-agent for future work," listing it as a co-equal contribution alongside the evaluated sync and async datasets is somewhat inflated.

### Trivial

- The Discussion section (Section 5) reads as generic suggestions (fine-tuning, RAG, code-use) not tightly grounded in the paper's specific findings, and could be substantially tightened.

- The paper's claim that the datasets contain "10 unique tasks each with 10 procedurally generated instances" means the sync and async datasets each contain 100 evaluation runs total, which is modest — this is not a criticism per se but is relevant context for the CI concern above.

## Nice-to-Have

- A controlled "syncretic" dataset variant: same state space and station count as the async dataset but with all cooking delays set to zero. This would cleanly isolate whether the performance gap is due to time delays or general complexity.
- Evaluation on at least 2–3 open-weight model families (e.g., Llama 3 70B, Qwen 2.5 72B) via ReAct to establish generality and reproducibility.
- Reporting bootstrapped 95% confidence intervals for the main sync vs. async success rates.
- A larger, more diverse task set — 10 task types per setting is small for a benchmark, and all tasks are cooking/assembly.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Timer formalism vs. implementation disconnect ("waiting while cooking").** The harsh critic claimed a contradiction between step-based timers and "waiting while cooking." This is not a problem: in a step-based MDP, the agent can take any valid action during a step, including unproductive ones that waste time while timers count down. "Waiting" simply means taking inefficient actions — fully consistent with the formalism. **Removed because factually incorrect.**

- **The performance gap only reflects general planning complexity, not async planning.** This criticism is partly valid (see the confound in Major weakness #1), but the harsh critic overstated it as a fatal structural issue when the paper acknowledges the relationship between the two settings and frames it as a finding about common failure modes. The benchmark does test async planning — the question is whether the main gap is *solely due* to async timing. Kept as the first Major weakness with softened framing.

- **Multi-agent dataset is unevaluated.** The paper explicitly says "leaving multi-agent for future work" (Section 1, line 16). The criticism is valid as an observation but not as a weakness — the paper is transparent about this. **Removed from weaknesses** (mentioned only as a minor note above about inflated contribution framing).

- **Missing limitations section.** The paper does not have an explicit limitations paragraph. This is common in shorter conference papers and not a substantive weakness. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves did not identify. The most interesting tension — that the dominant failure mode (rule violations) is shared across both settings yet async performance is dramatically worse — is already discussed in the paper.

## Suggestions

1. **Add a controlled ablation with zero cooking delays** for the async tasks (same state space, same number of stations, but all time delays set to zero). This is the single most important experiment to establish that the benchmark isolates asynchronous planning ability.
2. **Report bootstrapped confidence intervals** on the main sync vs. async success rates and on the ReAct+Prior comparison.
3. **Expand baseline coverage** to include at least one open-weight model (e.g., Llama 3 70B via ReAct) and one more recent agent architecture (e.g., Reflexion or any code-writing agent).
4. **Specify the optimal planner** used for computing $\|\tau^*\|$ and confirm it is guaranteed optimal (e.g., BFS over the state space or A* with an admissible heuristic).
5. **State code/dataset release plans explicitly** in the paper.
6. **Expand the task set** — even 5–10 more asynchronous task types would significantly strengthen the benchmark's coverage.

## Score and Decision

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>