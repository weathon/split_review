## Summary

This paper extends the AgentScope multi-agent platform with an actor-based distributed mechanism, environment interaction support, a heterogeneous configuration pipeline, and a web-based management interface to enable very large-scale LLM-powered multi-agent simulations. The core technical contribution is a distributed execution engine that supports agent-level parallel execution via two multi-process modes (one-to-one and many-to-one) and automatic centralized-to-distributed workflow conversion through a proxy/placeholder mechanism. The paper demonstrates the platform running a "guess 2/3 of the average" game with up to 1 million agents on 4 devices and provides behavioral observations across LLMs, prompts, background settings, and game variants.

## Strengths

- **1-million-agent simulation on 4 devices in 12 minutes (Fig 2a, Section 4.2):** The paper provides a concrete runtime measurement directly validating its scalability claim. Using Llama3-8B with a basic prompt, 1M agents complete in 12 minutes on 4 devices. Even the heaviest configuration (Llama3-70B + chain-of-thought prompt) finishes in ~10.6 hours. This is a clear, quantified demonstration of large-scale feasibility.

- **Controlled speed comparison isolating the parallelization mechanism (Fig 2b, Section 4.2):** Using a dummy model request to remove LLM inference time, the paper shows the proposed distributed mechanism completes a 1M-agent simulation in 40 seconds versus ~12 days for serial execution and ~8.6 hours for async I/O (the approach used by AutoGen, MetaGPT) — a 26,000× and 774× improvement respectively. This directly quantifies the efficiency gain from the actor-based parallelism design.

- **Near-linear horizontal scalability from 1 to 4 devices (Fig 2c, Section 4.2):** For Llama3-70B with 10,000 agents, running time decreases from 22 minutes (1 device) to 5.6 minutes (4 devices)—a 3.93× speedup. This provides empirical evidence for the claimed linear scaling benefit.

- **Practical automatic workflow conversion (Section 3.1, Fig 1):** The two-stage proxy/placeholder mechanism converts centralized workflows to distributed ones with a single `to_dist` function call, requiring no user code modifications beyond that. This addresses a real usability barrier in distributed multi-agent systems.

- **Systematic ablation of LLM prior knowledge (Section 4.6, Fig 8):** The paper varies the game ratio to 1/2 and 51/100, showing that the 51/100 condition initially mimics 1/2 (indicating LLMs treat 51/100 as an approximate fraction from training data) but can be corrected with an explicit note. This is a well-designed controlled experiment that produces practically useful insights for prompt engineering.

- **Measurable behavioral differentiation from the background generation pipeline (Section 4.4, Fig 5):** Agents with generated Ph.D. backgrounds consistently report lower numbers than elementary-school agents (e.g., Qwen2-72B shows an 8.24 gap), with a monotonic trend across five education levels. This provides quantitative evidence that the automatic generation pipeline produces meaningful behavioral diversity, not just surface-level variation.

## Weaknesses

### Major

- **Unsubstantiated comparative claims against Ray, with no experimental comparison.** The paper states (line 60) that the proposed mechanism "makes a significant advancement over existing actor-based distributed frameworks, such as Ray ... which allocate a new worker process for each actor, resulting in wasted computational resources." Despite this explicit claim of superiority, there are *zero experiments comparing against Ray* — no runtime comparison, no resource utilization comparison, no scalability comparison. Similarly, the comparison against AutoGen/MetaGPT is done via a re-implemented "async I/O mode" rather than directly benchmarking those platforms. The core scalability demonstration is impressive in absolute terms, but without comparative baselines, the paper's central efficiency claims lack the competitive context needed to establish advancement over the state of the art.

- **No repeated runs or variance reporting for behavioral experiments.** All behavioral results (Figs 3–9) are presented as single runs with no error bars, confidence intervals, or statistical significance tests. Since LLMs are inherently stochastic (the paper itself mentions adjusting random seed and temperature during generation), the reported behavioral patterns — e.g., "agents with Ph.D. report lower numbers," "MistralAI-8×22B is least sensitive to educational backgrounds" — could be driven entirely by sampling noise. This methodological gap makes the behavioral observations (which occupy roughly 60% of the experimental space) uninterpretable as evidence. The runtime benchmarks (Fig 2) are less affected by this (variance from LLM inference dominates), but even there, single runs without variance do not allow the reader to assess reliability.

### Minor

- **Only one simulation scenario evaluated.** All experiments use the "guess 2/3 of the average" game. While this is a well-studied benchmark, demonstrating the platform on only a single scenario limits the generalizability claims. The paper's infrastructure (environment support, agent-environment interactions, heterogeneous configurations) would be more convincingly validated by showing at least one additional scenario with different interaction patterns (e.g., a social simulation, a market simulation, or a coordination task).

- **No ablation isolating the contribution of individual system components.** The paper claims four contributions (distributed mechanism, environment module, config pipeline, management interface), but there is no experiment showing the marginal effect of each component. For instance, how much of the runtime improvement comes from the many-to-one multiprocess mode versus the one-to-one mode? How much does the environment module add to the overhead? The platform is presented as a monolith, making it hard to assess which design choices drive the reported performance.

- **No evaluation of generated background quality.** The configurable tool and background generation pipeline are presented as contributions, but the paper only shows downstream behavioral results. There is no evaluation of whether the generated backgrounds are realistic, diverse, or meaningfully distinct from a simpler randomization baseline. The behavioral differences in Fig 5 are suggestive but could also arise from prompt phrasing rather than genuinely diverse character models.

- **Claims about "linear scalability" are supported by only 1–4 devices.** The paper states "provides linear benefit on running time from the addition of devices" (line 22), but Fig 2c shows data for only 1–4 devices. Linear scaling over 4 points is weak evidence for a general scalability claim. Testing on more devices would significantly strengthen this result.

### Trivial

- None.

## Nice-to-Haves

- A comparison against the unmodified (non-distributed) AgentScope would cleanly isolate the marginal improvement from the distributed mechanism.
- Reporting behavioral observations with multiple seeds and variance ranges would transform the exploratory analysis into credible evidence.
- Demonstrating the platform on an additional scenario (e.g., a market or social simulation) would substantially strengthen the generalizability claims.
- Adding experiments on more devices (e.g., 8 or 16) to substantiate the linear scaling claim.

## Removed Points

The following points from the inputs were removed:

- **Harsh critic: "Serial execution is a straw-man baseline that no serious practitioner would use."** — Removed because serial execution is a perfectly valid lower-bound baseline to quantify the magnitude of improvement. The paper is not claiming serial execution is a competitor; it is using it as an anchor. The real issue (no comparison against Ray/AgentScope) is retained in Major.
- **Harsh critic: "The claim that AutoGen and MetaGPT rely on asynchronous I/O is presented without citation to specific technical analysis."** — Removed because the paper does cite Wu et al., 2023 and Hong et al., 2024b. A detailed technical analysis is not required for this kind of high-level architectural characterization in a systems paper.
- **Harsh critic: "The behavioral observations are shallow... not tested against any null hypothesis... read as post-hoc interpretation of a single run."** — The core concern (no variance/error bars) is retained in Major. The characterization as "shallow" and "post-hoc" is removed as it conflates weakness severity with rhetorical characterization. The retained weakness captures the substance.
- **Strength finder: Several generic/overlapping strengths were consolidated.** The strength about "systematic ablation isolating LLM prior knowledge" is retained (it is specific). The strength about "automatic workflow conversion" is retained. These were not removed.

## Novel Insights

The most interesting observation beyond the paper's own framing is the interaction between the two multi-process modes (one-to-one and many-to-one) and how the proxy/placeholder mechanism effectively solves a workflow orchestration problem that existing actor frameworks (Ray) leave to the user. The paper's design insight — that the many-to-one mode suits I/O-bound agent workloads while one-to-one suits compute-bound workloads — is practically valuable but is presented as a design decision rather than tested experimentally. An ablation comparing these two modes across different workload types would be a natural extension.

## Suggestions

1. **Add direct experimental comparison against Ray** (and ideally unmodified AgentScope) for the runtime benchmarks. This is the single most important addition — the paper's strongest claim ("advancement over Ray") is currently a speculation.
2. **Run all behavioral experiments with at least 3–5 seeds** and report means with error bars (standard deviation or confidence intervals). Without this, the behavioral analysis cannot be interpreted as evidence.
3. **Demonstrate the platform on at least one additional scenario** with different interaction dynamics to support generalizability claims.
4. **Shorten or relegate the behavioral analysis** to a supplementary role (appendix or brief demonstration) and expand the infrastructure benchmarking to include ablations and comparisons.
5. **Add scalability data on more than 4 devices** to substantiate the linear-scaling claim.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>