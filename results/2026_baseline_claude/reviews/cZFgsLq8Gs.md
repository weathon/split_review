## Summary

DeepScientist is a fully autonomous, goal-oriented AI scientific discovery system that frames discovery as a Bayesian Optimization problem over a persistent "Findings Memory." Operating on three frontier AI tasks (Agent Failure Attribution, LLM Inference Acceleration, AI Text Detection) using 20,000+ GPU hours on 16 H800 GPUs, the system generates ~5,000 unique ideas, validates ~1,100, and produces 21 SOTA-surpassing findings and 5 full research papers—outperforming human SOTA by 183.7%, 1.9%, and 7.9%, respectively. Human expert evaluation scores the generated papers comparably to average ICLR 2025 submissions (5.00 vs 5.08), and automated comparison against 28 papers from competing AI Scientist systems shows a 60% simulated acceptance rate vs. 0% for all others.

---

## Strengths

- **Genuinely impressive empirical results on frontier tasks.** All three benchmarks have strong, recently published (2024–2025) human-designed baselines (ICML Spotlight, ACL Outstanding, ICLR), and the system surpasses all three. The 183.7% accuracy improvement on Agent Failure Attribution and 7.9% AUROC gain on AI text detection are large, non-trivial improvements, not marginal tweaks.

- **Rigorous, independent human expert evaluation (Table 3).** A dedicated program committee of three active LLM researchers—two with ICLR reviewer experience, one with AC experience—evaluated the generated papers with strong inter-rater agreement (Krippendorff's α = 0.739). Two of five papers scored 5.67, above the average ICLR 2025 submission (5.08), and the evaluation specifically praises ideation novelty rather than superficial quality.

- **Honest, quantified failure analysis.** The paper candidly reports that 60% of failed trials were due to implementation errors, not flawed hypotheses, and that the overall success funnel is ~1% (21/1100+ validated yield progress). This intellectual honesty, combined with the ablation showing zero successes under random idea selection, is strong support for the value of the system's selection mechanism.

- **Meaningful scaling study (Figure 6).** The near-linear relationship between parallel GPUs and SOTA-surpassing findings (0→0→1→4→11 across 1→2→4→8→16 GPUs), corroborated by serial 4-week single-GPU runs, provides actionable evidence that the shared Findings Memory creates compounding value—not mere brute-force parallelism. This is an important empirical insight for the community.

- **Meaningful comparison against competing AI Scientist systems (Table 2).** Benchmarking against 28 papers from 5 systems (AI Scientist, HKUSD AI Researcher, AI Scientist-V2, CycleResearcher, Zochi) using the same automated reviewer protocol, with all competitors at 0% acceptance, strongly contextualizes the contribution.

---

## Weaknesses

### Fatal
None. The core results are experimentally validated and corroborated by independent human evaluators.

### Major

- **The 1.9% LLM Inference Acceleration improvement lacks statistical validation.** A gain of 3.65 tokens/second (190.25→193.90) is a small absolute change in a metric that varies considerably with hardware load, batch size, and implementation details. No variance, confidence intervals, or repeated-run statistics are provided for this result. Given that speculative decoding throughput is sensitive to VRAM state and scheduling, the claimed improvement could plausibly be within the noise envelope of the hardware. This undermines one of the three core claims.

- **Human supervision in the loop is underspecified but material.** Section 4 states: "Three human experts supervise the process to verify outputs and filter out hallucinations." The paper claims "fully autonomous" discovery throughout, but the nature and extent of this supervision is never clearly defined. If humans are correcting runtime errors, pruning output, or selectively re-running experiments, the autonomy claim is meaningfully qualified. The paper does not distinguish between passive monitoring and active intervention.

- **The "three years vs. two weeks" comparison (Figure 1) is misleading.** The left panel aggregates the cumulative output of many independent research groups, each operating without dedicated compute for this single problem, while the right panel represents a dedicated 20,000 GPU-hour sprint. These are fundamentally different operational regimes; conflating them as equivalent "progress timelines" overstates the result. The paper would be stronger if it framed this as "achieves SOTA in two weeks on dedicated compute" rather than directly competing with the aggregate human timeline.

### Minor

- **UCB hyperparameters (w_u = w_q = κ = 1) receive essentially no ablation.** The paper acknowledges these are task-agnostic and fixed, but the surrogate model's estimates of utility, quality, and exploration are LLM outputs with unknown calibration. A sensitivity analysis or even a qualitative discussion of how results might change with different weightings would strengthen confidence in the BO framing.

- **The A2P method's core idea—counterfactual abductive reasoning—is closely related to existing work in causal inference and counterfactual reasoning for LLM evaluation.** The paper would benefit from a more explicit comparison to existing causal attribution and abductive reasoning methods to clearly delineate novelty beyond applying these ideas to the agent failure domain.

- **The comparison set in Table 2 (28 papers from competing systems) appears unbalanced in favor of DeepScientist** because those systems were not designed for frontier AI tasks, operate on toy domains, and produce output structurally weaker than DeepScientist's goal-targeted output. The 0% vs. 60% comparison, while impressive, partly reflects domain difficulty rather than pure system quality.

### Trivial

- Gemini-2.5-Pro and Claude-4-Opus are used for specific roles; the sensitivity of results to model choice is not discussed and is unlikely to change the main findings.

---

## Nice-to-Haves

- Report statistical variance/CIs for all quantitative SOTA comparisons, especially for the inference acceleration task.
- Clarify what human supervision in the pipeline entailed operationally (e.g., number of interventions, types of hallucinations filtered, whether any experimental restarts were triggered by human decision).
- A direct comparison of DeepScientist's discovered methods against a human researcher who is given the same starting code, same compute budget, and same benchmark—rather than the "aggregate years of research" framing—would be both fairer and more impactful.
- Discuss whether the discovered methods (A2P, ACRA, PA-TDT) hold up on additional benchmarks or if they are benchmark-specialized, which is important for assessing generality.

---

## Novel Insights

The most genuinely novel insight in this paper is the empirical demonstration that shared-memory Bayesian Optimization over thousands of heterogeneous trial records—including failures—produces near-linear scaling in SOTA-surpassing discoveries as a function of parallel GPUs. This "knowledge-sharing synergy" (as opposed to embarrassingly parallel search) is a non-obvious result: it implies that the marginal value of additional compute in autonomous science scales with collective failure knowledge, not just with additional tries. The discovery trajectory visualization for AI text detection (Figure 5), showing the system pivoting from T-Detect → TDT → PA-TDT in a coherent conceptual arc anchored to identified limitations, supports a qualitatively different mode of search than prior AI Scientist systems: purposeful, self-directed sequential improvement on a frontier.

---

## Suggestions

1. **Run the LLM inference benchmark with multiple seeds and report mean ± std** to substantiate the ACRA result. A 1.9% improvement is publishable if statistically reliable, but currently the claim rests on a single-point comparison.
2. **Provide a clear table delineating what "human supervision" meant**: number of manual interventions, categories of hallucinations filtered, and whether any experiments were re-run at human request. This will allow the community to reproduce the system's level of autonomy.
3. **Reframe Figure 1's narrative**: instead of "comparable to three years of human research," use "achieves SOTA in two dedicated weeks of compute" — this is still a strong result and is not subject to the compositional fallacy of comparing against cumulative, multi-group, multi-project human timelines.
4. **Ablate the acquisition function weights** by comparing UCB with equal weights vs. utility-only exploitation vs. exploration-only, even on a single task, to empirically ground the Bayesian Optimization framing.

---

## Score and Decision

The paper makes a genuine and timely contribution to autonomous scientific discovery. The core empirical results—particularly A2P exceeding trained 7B models on agent failure attribution, and PA-TDT's AUROC gain on RAID—are supported by independent expert evaluation, scale appropriately with compute, and demonstrate behaviors qualitatively different from prior AI Scientist systems. The Bayesian Optimization framing is principled and the failure analysis is unusually honest. The weaknesses—insufficient statistical rigor on one of three core results, underspecified human supervision, and some misleading comparative framing—are addressable in revision and do not invalidate the paper's central claims.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>