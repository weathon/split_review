Now I have enough calibration data. Let me finalize.

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Non-Parameterized Randomization | fvTaoyH96Z | 2.33 | R1 | Much weaker — narrow scope, theoretical issues |
| Foundation Policies with Memory | It4KL6XnPq | 3.00 | R1 | Weaker — limited contribution |
| Reward as Observation | 473sH8qki8 | 2.00 | R1 | Much weaker |
| Discovering Minimal RL Envs | VDkye4EKVe | 3.00 | R1 | Weaker |
| Generalization Gap in Offline RL | 3w6xuXDOdY | 6.50 | R1/R2 | Comparable — benchmark paper, thorough but limited novelty. Our paper has stronger theory but weaker experimental completeness |
| MORL Generalization | tuEP424UQ5 | 5.75 | R1/R2 | Our paper is stronger — has a framework + re-evaluation, not just a benchmark |
| Level Sampling for ZSG | X1p0eNzTGH | 5.67 | R1/R2 | Our paper is stronger — clearer contribution, less confused |
| GRAM | UfczlMudN6 | 6.00 | R2 | Comparable — method paper, similar score. Our paper has broader scope |
| CodeIt | JlSyXwCEIQ | 5.75 | R2 | Different topic, comparable quality |
| InnateCoder | QiUitwJDKI | 5.75 | R2 | Different topic, our paper has stronger meta-contribution |

**Round 1 bracket:** 5.5–7.0
**Round 2 narrowing:** The paper sits around 6.0 — above the 5.75 cluster, comparable to GRAM (6.00), slightly below 3w6xuXDOdY (6.50) due to claim overstatement and missing ablation.

**Final score: 6.0, Accept**

---

## Summary
This paper re-evaluates claims from prior work that programmatic policies generalize better than neural policies in RL. Across TORCS, KAREL, and PARKING, the authors show that neural policies can achieve comparable OOD generalization when experimental factors (reward design, observation sparsity, model complexity) are controlled. The paper proposes an expressivity/discoverability framework and argues that neural networks' fundamental limitation is fixed memory capacity, preventing them from solving tasks requiring instance-scaling working memory (e.g., pathfinding). A proof-of-concept uses FUNSEARCH to synthesize BFS for a modified Karel maze.

## Strengths
- **KAREL results (Table 2) are genuinely strong**: PPO + a_{t-1} (feedforward network with last-action augmentation and partial observability) achieves perfect return (1.00) on four of five Karel tasks at 100×100 scale, matching or exceeding LEAPS. This is a clean and convincing demonstration that neural policies can generalize on these benchmarks when given appropriate inductive biases.
- **The expressivity/discoverability framework (Definitions 2–3, Section 5)** provides a useful, falsifiable vocabulary for diagnosing OOD generalization failures. Decomposing the problem into whether a generalizing solution exists in the policy space and whether search can find it gives the field a principled way to distinguish confounded evaluations from genuine representational limitations.
- **Identification of instance-scaling memory as a principled boundary (Section 5)** is a solid theoretical contribution. The argument that fixed-capacity hidden states cannot encode solutions requiring working memory that grows with input size (Ω(log|V|) bits to index vertices, BFS frontiers of Θ(|V|), nested subproblem stacks) pinpoints when programmatic representations have an inherent advantage. The paper acknowledges and engages with the Turing-completeness counterargument rather than ignoring it.
- **The sparsity explanation (Section 4.4)** coherently ties together the empirical findings across domains: programmatic policies naturally use fewer input features (e.g., a single variable in a Boolean guard), while neural networks attend to all available variables and learn brittle spurious correlations. This is testable and connects to broader work on visual distractions in RL generalization.

## Weaknesses

### Fatal
None.

### Major
- **The Abstract's "match or exceed" claim is overstated for TORCS.** NDPS generalizes in 3/3 seeds (100%). DRL (β=0.5) on G-TRACK-1: only 13/30 seeds (43%) learn the training track, with ~76% of those generalizing to G-TRACK-2 and ~69% to E-ROAD — yielding roughly 33% and 30% overall success rates. For AALBORG, 4/15 seeds (27%) learn the training track. A policy class that generalizes in 27–33% of attempts does not "match" one that generalizes in 100%. The headline claim should be substantially qualified, e.g., "can generalize on OOD tracks when they succeed at learning the training track." The paper reports these numbers honestly in Table 1 but the abstract's summary claim does not reflect them.
- **The KAREL re-evaluation conflates two interventions without a critical ablation.** The paper's key result is that PPO + a_{t-1} (partial observations + last action) generalizes while PPO with ConvNet (full state) and PPO with LSTM (partial state) do not. But the intervention changes two things simultaneously: (i) the observation space is reduced from full to partial, and (ii) the last action is appended. Since the paper motivates a_{t-1} explicitly as necessary to resolve partial observability (Figure 3), the improvement could come from Markovian state recovery rather than sparsity. Without an ablation of PPO with partial observations *without* a_{t-1}, the claimed mechanism is not isolated. This is the single most important experiment to add.

### Minor
- **FUNSEARCH proof-of-concept is underdeveloped.** Section 5 describes three FUNSEARCH runs synthesizing BFS in two sentences with minimal experimental detail: the maze configuration (Figure 7), success criteria, total runs attempted, and verification of generalization are not described. The paper also does not empirically test whether neural policies fail on this task, relying only on the theoretical argument. The proof-of-concept can either be expanded with experimental detail or honestly reduced to a conceptual argument — the theoretical claim about memory capacity stands either way.
- **Thesis framing is imprecise.** The paper frames its core finding as showing that the generalization gap "arises from uncontrolled experimental factors." But as the expressivity/discoverability framework itself clarifies, the original gap arose because both representations were expressive but neural policies' superior optimization (discoverability) caused them to overfit to speed. The reward function was identical for both policy classes — the confound is a discoverability asymmetry, not an uncontrolled experimental factor. A more precise framing using the paper's own framework would strengthen the narrative.
- **Section 6 overextends empirical warrant.** Claims that other works' (Cui et al. 2024, Guo et al. 2023, Qiu & Zhu 2022) reported advantages "may also be attributed to confounding factors related to discoverability" are speculative without re-evaluation. While appropriate for a discussion section, the paper should more clearly acknowledge that these claims are conjectural.

### Trivial
- The HARVESTER failure (0.04 on 100×100 for PPO + a_{t-1}) is noted but not analyzed. Understanding why this task resists generalization when the other four succeed would sharpen the paper's claims about *when* the gap can be closed.

## Nice-to-Haves
- Add the missing KAREL ablation: PPO with partial observations but without a_{t-1}, to disentangle sparsity from Markovian state recovery.
- Analyze the HARVESTER failure case to understand boundaries of the approach.
- Report lap time standard deviations for TORCS to contextualize consistency relative to NDPS.
- Develop or reduce the FUNSEARCH proof-of-concept with full experimental detail.

## Removed Points
These points are flagged to be removed — treat them with caution:

- **Claimed "internal inconsistency" between thesis and TORCS evidence** — REMOVED. The paper's expressivity/discoverability framework explicitly accounts for this: both representations are expressive, but neural policies' stronger optimization under β=1.0 leads to speed-overfitting (a discoverability failure), while programmatic policies' constrained search naturally finds slower-but-generalizing policies. The paper acknowledges this in Section 4.4 ("We conjecture that NDPS and PROPEL would not generalize to OOD problems if they could find better optimized policies"). This is a framing clarity issue (kept as Minor above), not an inconsistency.
- **Claimed selective application of expressivity/discoverability framework** — REMOVED. The paper explicitly addresses the Turing-completeness counterargument: "Although recurrent models are, in theory, computationally universal (Siegelmann & Sontag, 1994; 1995), recent work has shown that they are more limited, theoretically (Nowak et al., 2023) and empirically (Delétang et al., 2023)." The argument about fixed-capacity hidden states being insufficient for instance-scaling memory is valid for practical architectures as trained.
- **Concern about pathfinding example (Example 1) embedding memory-scaling** — REMOVED. This is a standard tree-search POMDP formulation used to illustrate the formalism; it does not undermine the paper's argument.
- **Concern about NDPS using a neural oracle** — REMOVED. This is a detail of the original method; the paper's re-evaluation uses DDPG directly, not distillation, so it does not affect the comparison.
- **Criticism that the paper "does not explain why programmatic representations generalize better" is contradictory with claiming to debunk it** — REMOVED. The paper's motivation is clearly stated: prior work provided empirical evidence without explanation, and the re-evaluation reveals the gap was due to confounds rather than representation.
- **Demand for reward shaping literature engagement** — REMOVED. The paper explicitly addresses this by noting Equation 2 is an intrinsic reward (evaluation uses lap time/crash metrics, not the shaped reward), which is a reasonable justification without needing to invoke the full reward shaping literature.

## Novel Insights
The most novel insight is the identification of **instance-scaling working memory as the precise criterion** that cleanly separates neural and programmatic representations. Tasks requiring memory that grows with input size (pathfinding, nested subproblems) are where neural networks are provably inexpressive with fixed-capacity architectures, while tasks with constant-memory solutions can be solved by either representation given appropriate inductive biases. The expressivity/discoverability decomposition, while drawing on existing ideas in deep learning theory, is applied here in a way that moves the conversation from "are programmatic policies better?" to "for which problem structures does the choice of representation fundamentally matter?"

## Suggestions
- Qualify the TORCS "match" claim in the abstract to reflect the reliability gap (e.g., "when they succeed at learning the training track, neural policies generalize comparably to programmatic ones").
- Add the PPO with partial-observations-only ablation to isolate the sparsity mechanism in KAREL.
- Either expand the FUNSEARCH proof-of-concept with experimental detail or reframe it as a conceptual argument — the theoretical claim about memory capacity stands either way.
- Reframe the thesis more precisely using the expressivity/discoverability language: the original gap was a discoverability asymmetry with identical reward, not an "uncontrolled experimental factor."

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>