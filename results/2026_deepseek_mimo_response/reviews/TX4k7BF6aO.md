## Summary
This paper proposes ARPO (Agentic Reinforced Policy Optimization), an RL algorithm for training multi-turn LLM-based agents that use external tools. Motivated by the empirical observation that token entropy spikes after tool-call feedback, ARPO branches additional rollouts at high-entropy tool-call steps rather than only performing full trajectory-level sampling. Experiments across 13 benchmarks in mathematical reasoning, knowledge-intensive reasoning, and deep search show consistent improvements over trajectory-level RL baselines (GRPO, DAPO, REINFORCE++) at roughly half the tool-call budget.

## Strengths
- **Well-motivated core mechanism via entropy analysis**: The paper provides concrete pilot experiments (§2, Figures 1–2) documenting entropy spikes after tool calls across search-based and code-based agents, with three specific observations (Ob.1–3) giving a data-driven rationale for the branching mechanism rather than ad hoc heuristics.
- **Consistent empirical improvements across 13 benchmarks**: Table 1 shows ARPO outperforms all trajectory-level RL baselines on both Llama3.1-8B (+4.2 avg over best baseline) and Qwen2.5-7B (+1.8 avg). Table 2 shows ARPO-14B achieves 43.7% on GAIA and 10.0% on HLE, surpassing even DeepSeek-R1-671B (25.2% and 8.6%), while trained with only 1k RL samples.
- **Substantial tool-call efficiency gain**: Figure 7a demonstrates ARPO uses ~250–300 tool calls per training step versus ~400–450 for GRPO, roughly halving the tool-call budget — a direct, quantifiable efficiency improvement for agentic RL training where each tool call involves external API latency.
- **Rollout diversity evidence**: Section 5.2 presents PCA/DBSCAN clustering over 7.6k trajectories showing ARPO produces 54 clusters vs. 48 for GRPO with greater inter-cluster separation, supporting the claim that entropy-based branching improves structured exploration.
- **Pass@K scaling analysis**: Figure 6 shows consistent Pass@1 to Pass@5 scaling for both Qwen3-8B and Qwen3-14B with ARPO, confirming the branching mechanism increases the breadth of correct behaviors the model can produce.

## Weaknesses

### Fatal
None

### Major
- **No variance or statistical significance reported**: All results in Tables 1 and 2 are single numbers with no error bars, confidence intervals, or mention of repeated runs. RL training is inherently stochastic, and margins between ARPO and strongest baselines are sometimes small (e.g., 58.3 vs. 56.5 avg on Qwen2.5-7B). Without variance estimates, it is impossible to judge whether improvements are statistically meaningful or within noise.

- **Theoretical contribution ("GPG Theorem") is overstated**: §3.3 (Equation 6) presents the "Generalized Policy Gradient Theorem" as a novel result, but it is the standard policy gradient theorem with macro-actions defined over token segments — the options framework (Sutton, Precup & Singh, 1999) established this pattern long ago. The paper claims it "encompasses the traditional Policy Gradient Theorem as a specific instance" (line 170) and that ARPO is "an advanced implementation of the GPG Theorem," misrepresenting a standard restatement as a new contribution.

### Minor
- **Soft advantage contribution is essentially standard GRPO**: §3.2 presents "Advantage Attribution Estimation" as a contribution, but the adopted (soft) setting explicitly retains the original GRPO loss formulation (line 142: "While we retain the original GRPO loss formulation"). The novelty lies entirely in the partial rollout mechanism, not in any advantage computation. The hard variant, which would represent a genuine alternative, performs worse and is not adopted.

- **Ambiguous normalization definition**: Line 96 states "the normalization means summing all the values of ΔH" while line 106 continues "and dividing by the vocab size V." Since H_t is already a scalar per token (from Eq. 1, which sums over vocabulary), the normalization procedure is confusing and impedes reproducibility.

- **Complexity claim is vacuous in the worst case**: Line 116 claims ARPO "reduces the computational complexity of each rollout from the trajectory-level RL's O(n²) to between O(n log n) and O(n²)." Since the upper bound O(n²) matches the baseline, the claim of "reducing" is unfounded in the worst case.

### Trivial
None

## Nice-to-Haves
- Hyperparameter sensitivity analysis in the main text for ARPO-specific parameters (α, β, τ, branching budget allocation). The method introduces more knobs than baselines.
- Report total compute (including additional forward passes for entropy monitoring) alongside tool-call savings.
- Acknowledge potential systematic bias from using Qwen2.5-72B-instruct as judge when training Qwen-family models.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Critic's claim that "GRPO actually beats ARPO on HLE NS and xBench SF" for Qwen3-14B: verified against Table 2, this is incorrect. ARPO-14B beats GRPO-14B on HLE NS (10.3 vs 7.9) and xBench SF (13.7 vs 12.6). The critic misread the table.
- Critic's claim about ARPO not achieving best on "2Wiki for Reinforce++": checking Table 1 Qwen2.5-7B, ARPO gets 76.1 on 2Wiki which IS the best result. Factually wrong.
- Qwen-as-judge bias speculation: common practice applied equally to all methods.
- DBSCAN hyperparameter concern: clustering is supporting evidence, not a core claim.

## Novel Insights
The paper's genuinely novel observation is that token entropy systematically spikes after tool-call feedback in LLM-based agents, and that this signal can be leveraged to improve exploration efficiency in agentic RL. While entropy-based exploration is not new in RL, the specific application to multi-turn tool-use contexts with empirical characterization across search and code tools is a meaningful contribution to the agentic RL literature.

## Suggestions
- Report mean ± std across at least 3 seeds for main results (Tables 1 and 2).
- Reframe the theory section: either drop the GPG "theorem" or present it honestly as a formalization connecting the algorithm to standard PG with macro-actions.
- Clarify the normalization procedure in §3.1 Step 2 with a precise mathematical definition.
- Drop "Advantage Attribution Estimation" as a named contribution and focus the narrative on entropy-based adaptive rollout.

## Calibration Report

**Round 1 — Bracketing:** Queried "reinforcement learning training LLM agents tool use multi-turn" across three score bands.
- Weak (<3.5): E2CR6hmV1I (3.00), P0eEalHM5h (3.40), IB1HqbA2Pn (3.25) — all rejected papers with limited novelty.
- Middle (3.5–7.5): PNHjoWcQje/StepTool (5.50, rejected, similar topic), cVyELMpMRS/REFUEL (6.50, accepted, multi-turn RL), Dpqw0namg3/LAM Simulator (6.00, rejected), hILVmJ4Uvu/TWOSOME (6.00, accepted).
- Strong (>7.5): 9pW2J49flQ/DeepLTL (8.00), mMPMHWOdOy/WizardMath (8.00), OI3RoHoWAN/GenSim (8.00) — all highly influential.
- Initial bracket: **5.5 – 7.0**.

**Round 2 — Narrowing:** Queried in (5.0, 6.5) and (6.0, 7.5).
- New anchors: DlqRpj68xe/Q-shaping (5.67, rejected), fp6t3F669F/AgentQuest (6.25, accepted), zAdUB0aCTQ/AgentBench (6.20, accepted), S2oTVrlcp3/SmartPlay (6.75, accepted), womU9cEwcO/Auto reward (6.67, accepted).
- ARPO is clearly stronger than StepTool (5.50) and TWOSOME (6.00, which had "nothing novel" per reviewers), comparable to REFUEL (6.50) but with broader evaluation, and below the 8.0 papers.
- Final score: **6.5**.

**Reporting all retrieved anchors across both rounds:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| E2CR6hmV1I | 3.00 | 1 | Much weaker; limited novelty and poor results |
| P0eEalHM5h | 3.40 | 1 | Much weaker; narrow domain, weak evaluation |
| IB1HqbA2Pn | 3.25 | 1 | Much weaker; mixed results, limited scope |
| zEhTnQZB3D | 2.33 | 1 | Much weaker; tangential topic, poor results |
| DWLlTNhig1 | 4.75 | 1 | Weaker; narrower evaluation, less novel mechanism |
| PNHjoWcQje | 5.50 | 1+2 | ARPO clearly stronger: broader eval, more novel mechanism |
| Dpqw0namg3 | 6.00 | 1+2 | ARPO stronger: more algorithmic contribution, broader benchmarks |
| cVyELMpMRS | 6.50 | 1 | Comparable; REFUEL has cleaner theory, ARPO has broader eval |
| hILVmJ4Uvu | 6.00 | 1+2 | ARPO stronger: "nothing novel" per TWOSOME reviewers |
| DlqRpj68xe | 5.67 | 2 | ARPO stronger: broader domain, more comprehensive eval |
| fp6t3F669F | 6.25 | 2 | Different (benchmark); ARPO has algorithmic contribution |
| zAdUB0aCTQ | 6.20 | 2 | Different (benchmark); ARPO has algorithmic contribution |
| S2oTVrlcp3 | 6.75 | 2 | Different (benchmark); ARPO has algorithmic contribution |
| womU9cEwcO | 6.67 | 2 | Comparable: both address LLM agents with automatic rewards |
| 9pW2J49flQ | 8.00 | 1 | ARPO not at this level; DeepLTL is highly influential |
| 4KqkizXgXU | 8.00 | 1 | ARPO not at this level |
| mMPMHWOdOy | 8.00 | 1 | ARPO not at this level; WizardMath broadly impactful |
| OI3RoHoWAN | 8.00 | 1 | ARPO not at this level; GenSim broadly impactful |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>