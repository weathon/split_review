## Summary

This paper studies decentralized safe multi-agent reinforcement learning under a homogeneous-agent setting. It formalizes the homogeneous constrained Markov game, proves that policy sharing preserves optimality and safety in this setting (Theorem 1), and proposes an on-policy decentralized primal-dual actor-critic algorithm with asymptotic convergence guarantees (Theorems 3–5) under linear function approximation. A practical off-policy deep RL variant (DPDAC-ER) is then developed, with experiments on three continuous multi-robot coordination tasks showing competitive performance against centralized safe and decentralized baselines.

## Strengths

- **Theorem 1 provides the first theoretical justification that policy sharing preserves both optimality and safety in homogeneous constrained Markov games** (Section 3). This formally grounds a commonly used heuristic (shared policy parameters for homogeneous agents) in the safety-constrained setting, which prior work had not established.

- **The decentralized dual variable update (Equation 8) is a genuine algorithmic innovation.** It enables the handling of a *centralized* safety constraint (team-average cost) without a centralized trainer, using consensus-based updates communicated over a sparse, time-varying graph. This is nontrivial because the centralized constraint couples agents' dual variables, yet each agent can compute its local dual update using the initial-state distribution and its own critic.

- **Asymptotic convergence is proven for all three update steps (critic, actor, dual variable) under standard multi-timescale stochastic approximation assumptions** (Theorems 3–5, Section 4). The proofs are given in the appendix and follow established analytical frameworks (Borkar, Zhang et al., Chen et al.), which gives confidence in their correctness.

- **The practical DPDAC-ER algorithm demonstrably achieves safe policies on three continuous multi-robot tasks** (Aggregation, Swapping, Formation), with learning curves showing cost satisfaction and competitive reward relative to the centralized safe baseline (MASAC-Lag) and clear improvements over the no-entropy variant (DPDAC). The ablation studies empirically validate the necessity of both the consensus mechanism and entropy regularization.

## Weaknesses

### Major

- **Significant gap between the theoretical analysis and the practical algorithm.** The convergence theory (Theorems 3–5) assumes linear critics, finite state/action spaces, decreasing stepsizes, and on-policy sampling. The practical DPDAC-ER uses neural network critics, continuous spaces, replay buffers, and constant learning rates. While the paper acknowledges this disconnect transparently (Section 5, first paragraph) and references Appendix I.1 for a relationship analysis between the on-policy and off-policy updates, no formal approximation bound, bias guarantee, or constraint satisfaction guarantee is provided for the practical algorithm. The dual variable update in the practical version (Equation 15) replaces an expectation over the initial-state distribution and current policy (Equation 8) with an expectation over replay buffer samples — two fundamentally different objects — and the paper provides no analysis of whether the ODE in (12) still governs the dynamics under this change. This weakens the connection between the strongly motivated theoretical framework and the claims supported by experiments.

- **The "decentralized" framing relies on global state and joint-action observability.** The paper assumes each agent observes the global state and joint action (Section 2.2). This is consistent with a well-established line of decentralized MARL work (Zhang et al., 2018; Chen et al., 2022; Hu et al., 2024) that uses consensus for parameter information rather than for information acquisition, and the paper is transparent about this assumption. However, it means the central source of difficulty addressed is the absence of a *centralized trainer*, not the absence of global information. The practical relevance of this framing is limited when agents cannot observe the global state — for instance, in large-scale or partially observable systems. The local-observation ablation is relegated to the appendix (J.5) rather than being a main result, and the main experiments all use global observability.

### Minor

- **No experimental comparison with existing decentralized safe MARL baselines.** The related work cites Lu et al. (2021) and Ying et al. (2023b) as prior decentralized safe MARL methods, and the paper argues they face challenges in continuous settings. A direct empirical comparison — even adapting them with Gaussian policies or showing why adaptation is infeasible — would substantially strengthen the claim that DPDAC-ER advances the state of the art. The current baselines (MASAC-Lag is centralized; DAC-ER and DPDAC are not safety-constrained baselines from prior work) do not fill this gap.

- **Constraint type is centralized (team-average), which bundles individual agents' safety.** The problem formulation (1) uses a centralized constraint on team-average cost. In many safety-critical applications, each agent has an individual safety threshold (e.g., each robot should not collide). While the paper states it can handle multiple constraints, this is not demonstrated.

### Trivial

- The local observation ablation, which directly addresses the most limiting assumption, is only summarized in a single sentence in the main text and detailed in the appendix. Given the importance of this assumption, a summary table or brief main-text figure would be more appropriate.
- The paper does not provide statistical hypothesis tests for claims of superiority (e.g., "outperforms MASAC-Lag in Formation"), only reporting 5-trial means and confidence intervals.

## Nice-to-Haves

- An approximation guarantee or bounded-bias analysis for the off-policy practical algorithm, even a simple argument, would significantly tighten the theory-practice connection.
- A discussion of constraint violations *during training* (not just at convergence) would be practically relevant for deployment in safety-critical systems.
- A computational complexity / communication overhead comparison with centralized-training methods would help practitioners understand the trade-offs.

## Removed Points

- *Criticism that the agent must "know the mapping from observation indices to agent indices"* — The paper explicitly addresses this in Section 3, noting that each agent can compute permuted observations via the bijective observation function (Definition 1, condition (iii)), and the homogeneous structure ensures agents can identify which observation belongs to which agent through permutation. This is well-justified within the model's assumptions.
- *Criticism that the decentralized label is "misleading" or "overclaimed"* — The paper places itself in a specific, well-documented line of decentralized MARL (parameter-consensus with global observability), clearly distinguishes this from local-observation approaches, and discusses the local-observation extension. The framing is accurate given the cited prior work.
- *Criticism about the entropy regularization in actor update (7) requiring shared log-probability computation* — The paper explicitly explains how each agent computes this locally via the permutation mechanism (Definition 1, condition (iii)), which is a direct consequence of the homogeneity assumption. This is handled, not a gap.
- *Strengths that are generic/superficial* — Removed generic statements about "the problem being important" or "addressing a significant challenge." Only concrete, evidence-backed strengths are retained.

## Novel Insights

The two reviewers do not produce insights that go substantially beyond what the paper itself states. The key observation is that the paper's most original contribution — Theorem 1 proving that policy sharing preserves optimality in the safe, constrained setting — is a non-trivial extension of Chen et al. (2022) to the safety-constrained case, and it provides a clean theoretical foundation for a widely used but previously unverified heuristic. The consensus-based dual variable update is also a well-motivated algorithmic contribution. Neither reviewer identified a perspective that the paper's own discussion misses.

## Suggestions

1. **Bridge the theory-practice gap**, even informally. Add a paragraph or appendix section that characterizes when the off-policy updates approximate the on-policy gradient (e.g., when the replay buffer is fresh enough, or under bounded density-ratio assumptions). This would make the theory feel less disconnected from the experiments.
2. **Add a decentralized safe baseline** to the experiments. Adapting Lu et al. (2021) or Ying et al. (2023b) to continuous action spaces, even with simplified versions, would directly validate the claim that prior methods are insufficient.
3. **Promote the local-observation results** from the appendix to the main text (at least as a summary table or a single additional subplot in Figure 1). This directly addresses the paper's most limiting assumption and would significantly strengthen the contribution.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| z1WiEHnjQs.md (Decentralized independent policy opt.) | 3.33 | R1 | Weaker: paper lacks practical experiments, withdrawn |
| RAdBtquPiI.md (Bender's oracle safety) | 3.40 | R1 | Weaker: different subfield, provable safety but weaker RL integration |
| D78HxVUg1Q.md (Robustness to uncertainty MARL) | 2.50 | R1 | Weaker: limited contribution, withdrawn |
| Q8ypeYHKFO.md (SafeDiffuser) | 3.33 | R1 | Weaker: different problem (safety via diffusion), withdrawn |
| 1X1R7P6yzt.md (DGPPO — discrete GCBF safe MARL) | 6.67 | R1 | **Slightly stronger**: tighter coupling between theory and practice; both accepted |
| GvsCOOPxoI.md (Provable DEC-POMDP learning) | 6.17 | R1 | Comparable: strong theoretical contributions, but rejected |
| VA1tNAsDiC.md (Best Possible Q-learning) | 4.00 | R1 | Weaker: restrictive assumptions, limited experiments |
| v9fQfQ85oG.md (MOMARL Pareto-stationary) | 4.75 | R1 | Weaker: limited experiments, withdrawn |
| fDaLmkdSKU.md (Near-optimal constrained learning) | 5.80 | R2 | Similar: theory-oriented, accepted poster; DPDAC-ER has stronger experiments |
| ZuflmOaxb7.md (Federated NPG for multi-task RL) | 4.75 | R2 | Weaker: tabular only, no experiments, rejected |
| hB2hXtxIPH.md (Greedy Sequential Execution) | 7.00 | R2 | Stronger: clearer experiments on common benchmarks, accepted spotlight |
| AOlm45AUVS.md (Offline MARL low interaction rank) | 7.00 | R2 | Stronger: cleaner theory-experiment connection, accepted poster |
| BfUDZGqCAu.md (Personalized federated RL) | 6.67 | R2 | Comparable to slightly stronger: solid convergence theory + experiments |

**Round 1 bracket:** 5.0–7.0 (the paper is clearly above the weak anchors at 2.5–4.0 and below the strong anchors at 8.0).

**Round 2 narrowing:** Compared against the most relevant anchors — DGPPO (6.67) has a tighter theory-practice connection, while the constrained learning paper (5.80) is more theory-focused. DPDAC-ER sits between these: it has stronger empirical evaluation than the constrained learning paper but a larger theory-practice gap than DGPPO. The rejected papers at 4.0–4.75 lack either experiments or have more fundamental issues. The papers at 6.67–7.00 have either cleaner theory-practice connections or experiments on standard benchmarks.

**Final placement:** 6.0 — a solid paper with genuine theoretical contributions (Theorem 1, convergence analysis) and a reasonable practical algorithm validated on three tasks. The theory-practice gap and the missing decentralized safe baseline prevent it from reaching the 6.67–7.0 level, but the contributions are clearly above the 4–5 range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>