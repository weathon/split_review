## Summary
# Final Review Report

## Summary

This paper addresses the decentralized safe multi-agent reinforcement learning (MARL) problem for homogeneous multi-agent systems. The authors propose DPDAC-ER (Decentralized Primal-Dual Actor-Critic with Entropy Regularization), a framework that combines three components: (1) a homogeneous constrained Markov game formulation where policy sharing provably preserves optimality and safety, (2) an on-policy decentralized primal-dual actor-critic algorithm with asymptotic convergence analysis via multi-timescale stochastic approximation, and (3) a practical off-policy deep-RL instantiation. Empirically, DPDAC-ER is evaluated on three safety-aware multi-robot coordination tasks (Aggregation, Swapping, Formation) with continuous action spaces and compared against centralized and decentralized baselines.

**Strengths:** The paper provides a clean theoretical formulation (homogeneous constrained MG with permutation-invariance properties) and a rigorous convergence analysis for the on-policy linear-critic variant. The decentralized dual variable update with consensus is a novel algorithmic contribution. Empirical results are promising and include meaningful ablation studies on communication topology, constraint thresholds, and local observation settings.

**Core weaknesses:** (1) A significant theory-practice gap exists — convergence guarantees proven for the on-policy linear-critic variant do not extend to the DRL-based practical algorithm, but this distinction is not explicitly stated. (2) Empirical evaluation lacks quantitative rigor (no numerical tables, variance reporting, or significance tests in the main text). (3) The assumption of global state and joint action observability weakens the "decentralized" claim. (4) The O(N) per-agent computation required for the joint log-probability in the actor update is not discussed as a scalability limitation. (5) Three separate contribution claims are listed when two are essentially the same algorithm at different abstraction levels.

**Novelty verdict:** Deferred (Retrieval-Disabled Mode active; external literature comparison unavailable in this run). Manual verification is required to assess the paper's novelty against the strongest related baselines, particularly relative to Chen et al. (2022), Hu et al. (2024), Lu et al. (2021), and Ying et al. (2023b).

## Strengths
1. **Clear theoretical formulation.** The homogeneous constrained Markov game (Definition 1) is a well-motivated extension of Chen et al.'s homogeneous MG to the safe MARL setting. The permutation-invariance and permutation-preserving properties are rigorously defined, and Theorem 1's proof that policy sharing preserves optimality is sound and useful for justifying decentralized policy learning.

2. **Rigorous convergence analysis.** The three-timescale stochastic approximation analysis (Theorem 3-5) for the on-policy linear-critic variant is technically complete and follows established methodologies (Borkar, 2008; Bhatnagar, 2010). The proof structure (consensus analysis → convergence analysis for critic/actor/dual) is well-organized, and the assumptions (1-7) are explicitly stated and discussed in Appendix C.

3. **Novel decentralized dual variable update.** The dual variable update with consensus (Eq. 8) is a meaningful algorithmic contribution. It handles the centralized cost constraint in a decentralized manner by sharing Lagrangian multipliers across the communication network. Propositions 1-2 provide correct theoretical guarantees on safety constraint satisfaction.

4. **Comprehensive ablation studies.** The experiments include ablations on communication topology (all-to-all vs. sparse vs. no communication), constraint thresholds, local observations (Appendix J.5), and reward-shaping baselines (Appendix J.6). These provide useful insights into when the method works and why.

5. **Entropy regularization justification.** The comparison between DPDAC-ER and DPDAC (without entropy) clearly demonstrates the value of entropy regularization for exploration in continuous spaces, and the 3D Formation task extension (Fig. 9) strengthens this evidence.

## Weaknesses
1. **(Major) Theory-practice gap with insufficient acknowledgment.** The convergence proof (Section 4) applies only to the on-policy algorithm with linear critics, finite state/action spaces, and decreasing step sizes (Assumptions 1-7). The practical DPDAC-ER algorithm (Section 5) uses neural networks, replay buffers, and constant learning rates — none of these satisfy the assumptions. The paper acknowledges this gap in one sentence ("Even though the decentralized algorithm proposed in Section 3 is theoretically convergent, the performance of this algorithm can be severely limited by the standard assumptions") but does not explicitly state which guarantees are preserved and which are lost. This can mislead readers into thinking DPDAC-ER inherits convergence guarantees.

2. **(Major) Lack of quantitative empirical reporting.** The main results paragraph (Page 8, lines 96-108) describes outcomes qualitatively: "similar learning performance," "excellent learning stability," "outperforms MASAC-Lag." No numerical values (mean ± std) are provided in the main text. The learning curves in Fig. 1 are "smoothed," which can hide variance and transient constraint violations. Only 5 independent trials are used, which is relatively low for drawing strong statistical conclusions in safe MARL.

3. **(Major) Contribution inflation.** Three separate contribution claims are listed, but C2 and C3 describe the same algorithm at different fidelity levels (on-policy theoretical vs. off-policy practical). The practical version is essentially an engineering adaptation of the theoretical algorithm using standard DRL techniques (replay buffers, target networks, automatic entropy tuning), not a conceptually separate contribution.

4. **(Moderate) Scalability concern unaddressed.** The actor update (Eq. 7) requires each agent to compute log(π_{[θ_{i,t}]}(a_t|s_t)) = Σ_j log(π_{i,θ_{i,t}}(a_{j,t}|o_j(s_t))). This means each agent must evaluate its policy density for all N agents' actions, resulting in O(N) per-agent computation per time step. For large-scale swarms (N>100), this is expensive. The paper does not discuss this scaling behavior.

5. **(Moderate) Global state assumption weakens decentralization claim.** The problem formulation (Page 3, lines 88-94) assumes "each agent can observe the global state and the joint action." While this follows the parameter-communication line of work (Zhang et al., 2018), it qualifies what "decentralized" means: the algorithm is decentralized in training but not in observation. The paper should make this distinction more explicit.

6. **(Minor) Homogeneous agent assumption limits applicability.** The entire theoretical framework and algorithm design rely on agents being homogeneous (same action space, same local state space structure, same observation function). This excludes heterogeneous multi-robot systems where agents have different action capabilities or sensing modalities.

7. **(Minor) Conclusion lacks limitations discussion.** The conclusion mentions only one direction for future work (local observations) but does not discuss other important limitations: homogeneous assumption, scalability, theory-practice gap, or the reliance on a functioning communication network for safety.

## Key Issues
### Issue 1: Theory-practice gap undermines the paper's unified narrative
- **Severity:** High
- **Root cause:** The paper presents a single narrative arc (formulation → algorithm → convergence → practice → experiments), but the convergence proof and the practical algorithm operate under fundamentally different assumptions (linear critics vs. neural networks, on-policy vs. off-policy, decreasing vs. constant learning rates). The abstract and introduction do not prepare readers for this discontinuity.
- **Evidence:** Page 1 Abstract, Page 7 Section 5. Assumptions 1-7 vs. the practical algorithm in Section 5.
- **Required action:** Add an explicit bridging paragraph in Section 5 stating which theoretical properties are preserved and which are not.

### Issue 2: Empirical validation lacks quantitative rigor
- **Severity:** High
- **Root cause:** The main results paragraph (Page 8) describes outcomes qualitatively without reporting numerical values, variances, or statistical significance. Fig. 1 is smoothed, which can misrepresent tail behavior in safety-critical settings.
- **Evidence:** Page 8, Results paragraph (lines 96-108); Fig. 1 caption.
- **Required action:** Add a table with mean ± std over 5 seeds for all algorithms across all tasks, both for reward and cumulative cost at convergence.

### Issue 3: Contribution structure inflates novelty
- **Severity:** Medium
- **Root cause:** C3 (practical off-policy DRL version) is not conceptually distinct from C2 (on-policy algorithmic framework). The practical version is an engineering adaptation using standard DRL tools.
- **Evidence:** Page 2, Contributions list (lines 61-73).
- **Required action:** Merge C2 and C3 into a single contribution with theoretical and empirical sub-components.

### Issue 4: Scalability bottleneck in the actor update is not discussed
- **Severity:** Medium
- **Root cause:** The log(π_{[θ_{i,t}]}) term in Eq. (7) requires O(N) policy evaluations per agent per step.
- **Evidence:** Page 5, lines 111-112: "log(π_{[θ_{i,t}]}(a_t|s_t)) = Σ_{j=1}^N log(π_{i,θ_{i,t}}(a_{j,t}|o_j(s_t)))"
- **Required action:** Add computational complexity analysis and discuss scalability for large N.

### Issue 5: Global state assumption limits decentralization claim
- **Severity:** Medium
- **Root cause:** The paper claims "decentralized" but assumes global state observability, which is often unavailable in real decentralized multi-robot systems.
- **Evidence:** Page 3, lines 88-94.
- **Required action:** Clarify that "decentralized" refers to training architecture, not observation structure. Explicitly state this early in the paper.

## Actionable Suggestions
### S1 (Must): Add an explicit theory-practice bridge paragraph
- **Target:** Section 5 (Practical Algorithm Design), after line 81.
- **Action:** Add a paragraph that explicitly states the delta between theoretical guarantees and practical implementation.
- **Text:** "It is important to note that while DPDAC-ER inherits the algorithmic structure of the on-policy variant (primal-dual framework, policy consensus, entropy regularization), it does not inherit the convergence guarantees proven in Section 4. Those guarantees rely on linear function approximation, decreasing step sizes, and on-policy data — none of which hold in the DRL-based implementation. The empirical evaluation in Section 6 should therefore be interpreted as a practical demonstration, not as a validated theoretical claim."

### S2 (Must): Add a quantitative results table
- **Target:** Section 6 (Experiments), after the Results paragraph.
- **Action:** Add a table reporting mean ± std of undiscounted cumulative reward and cost for all algorithms across all three tasks at convergence (last 1000 episodes). Include the percentage of episodes where safety constraints are violated.
- **Table format:**
  | Algorithm | Aggregation (Reward / Cost) | Swapping (Reward / Cost) | Formation (Reward / Cost) |
  |---|---|---|---|
  | DPDAC-ER (ours) | X±σ / Y±σ | ... | ... |
  | MASAC-Lag | ... | ... | ... |
  | DAC-ER | ... | ... | ... |
  | MASAC | ... | ... | ... |
  | DPDAC | ... | ... | ... |

### S3 (Must): Restructure contribution claims
- **Target:** Page 2, Contributions list (lines 61-73).
- **Action:** Merge C2 and C3 into one contribution with dual facets (theoretical and empirical). Keep C1 as the model contribution.
- **Revised text:** C2: "A decentralized primal-dual actor-critic framework for safe MARL with entropy regularization. Asymptotic convergence of the on-policy, linear-critic variant is established via multi-timescale stochastic approximation (Theorems 3-5). A practical off-policy instantiation using deep neural networks (DPDAC-ER) is further developed, demonstrating strong empirical performance on continuous multi-robot coordination tasks."

### S4 (Must): Clarify the decentralization claim
- **Target:** Page 3, Problem Formulation (lines 88-94).
- **Action:** Add one sentence clarifying that the decentralization is in *training* (no centralized trainer, parameter consensus via communication network), not in *observation* (global state is assumed available).
- **Text:** "Note that 'decentralized' here refers to the training architecture: there is no centralized trainer, and each agent updates its policy using local experiences and neighbor-shared parameters. The global-state assumption follows the standard parameter-communication decentralized MARL setting (Zhang et al., 2018; Chen et al., 2022); a local-observation extension is provided in Appendix J.5."

### S5 (Nice-to-have): Add computational complexity analysis
- **Target:** Section 3 or Appendix.
- **Action:** Add a brief analysis of per-agent per-step computational cost, noting the O(N) scaling from the joint log-probability computation in Eq. (7).

### S6 (Nice-to-have): Expand conclusion with limitations
- **Target:** Section 7 (Conclusion), after the current text.
- **Action:** Add a limitations paragraph covering: homogeneous agent assumption, scalability to larger N, theory-practice gap, and reliance on functioning communication for safety.

### S7 (Nice-to-have): Add statistical significance test
- **Target:** Section 6 results paragraph.
- **Action:** When reporting the comparison with MASAC-Lag, add a paired t-test or Wilcoxon signed-rank test over the 5 seeds to assess whether the reward difference in the Formation task is statistically significant.

## Storyline Options + Writing Outlines
### Abstract Outline (complete 4-5 sentence structure)

The current abstract is reasonable but can be tightened. Recommended structure:

- **S1 (Problem):** "We study the decentralized safe multi-agent reinforcement learning (MARL) problem for homogeneous multi-agent systems, where agents must maximize team-average return while satisfying cumulative safety constraints under limited communication."
- **S2 (Model):** "A homogeneous constrained Markov game is formally characterized, establishing that policy sharing provably preserves both optimality and safety in this setting."
- **S3 (Algorithm - Theoretical):** "An on-policy decentralized primal-dual actor-critic algorithm is proposed, with asymptotic convergence proven via multi-timescale stochastic approximation under standard linear-critic assumptions."
- **S4 (Algorithm - Practical):** "A practical off-policy deep-RL instantiation (DPDAC-ER) is then developed, incorporating entropy regularization for efficient exploration in continuous spaces."
- **S5 (Results - bounded):** "Experiments on three safety-aware multi-robot coordination tasks demonstrate that DPDAC-ER achieves competitive reward-cost trade-offs against centralized and decentralized baselines, though convergence guarantees apply only to the on-policy variant."

### Introduction Outline (paragraph-by-paragraph)

**Current structure (diagnosis):** P1 describes CT-based MARL and its limitations. P2 describes decentralized MARL and the continuous safe MARL challenge. The current order is logical but the connection between the two paragraphs could be stronger, and the gap that entropy regularization fills is not foreshadowed.

**Recommended structure:**

- **P1 (Big Picture + Problem):** Start with cooperative MARL and the practical need for safety. Establish that existing CT-based safe MARL methods require centralized training, which is infeasible under communication constraints. *Key claim:* Safe MARL under decentralized training is qualitatively harder than reward-only decentralized MARL because safety constraints couple agents across the network.
- **P2 (Gap):** Review existing decentralized MARL methods (Zhang et al., 2018; Chen et al., 2022) and existing decentralized safe MARL methods (Lu et al., 2021; Ying et al., 2023b). Explicitly state their limitations: (i) discrete action spaces only, (ii) poor sample efficiency in continuous spaces, (iii) reliance on hard-to-estimate occupancy measures. *Key claim:* No existing decentralized safe MARL method works effectively in continuous action spaces.
- **P3 (Solution):** Present the key ideas: (i) homogeneous constrained MG with permutation-invariance enables policy sharing, (ii) entropy regularization improves exploration in continuous spaces, (iii) primal-dual method with consensus handles coupled constraints in a decentralized manner. *Key claim:* This is the first decentralized safe MARL framework that combines entropy regularization with primal-dual consensus for continuous tasks.
- **P4 (Evidence + Contributions):** Preview the theoretical and empirical results. State contributions as two items (model + algorithm with theoretical and practical facets). End with a roadmap.

### Alternative Storyline Candidates

**Candidate A (Theory-first — current, but fix the theory-practice bridge):** 
Most faithful to the paper's current structure. Fix by adding an explicit "What This Paper Does vs. Does Not Prove" box in Section 5.

**Candidate B (Empirical-first):** 
Start with the practical algorithm and its empirical success, then backtrack to theory as supporting justification. This would front-load the experimental results and reduce emphasis on convergence theory. *Risk:* May attract criticism for insufficient theoretical depth from the ICLR audience.

**Candidate C (Problem-driven):** 
Organize around the specific challenges of decentralized safe MARL: (1) coupled safety constraints, (2) limited communication, (3) continuous action spaces. Present DPDAC-ER's components as solutions to each challenge. This is more reader-friendly for practitioners.

**Recommendation:** Keep the current structure (Candidate A) but add the theory-practice bridge paragraph (Suggestion S1). The current structure is appropriate for ICLR's audience, which values theoretical contributions.

## Priority Revision Plan
### P0 (Critical — must fix for acceptance)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0 | Theory-practice gap | Add bridge paragraph in Section 5 (S1) | Prevents reviewer rejection; addresses a fundamental honesty concern |
| P0 | Missing quantitative results | Add numerical table with mean±std (S2) | Required for empirical claims to be credible |
| P0 | Contribution inflation | Merge C2 and C3 (S3) | Aligns claims with actual novelty |

### P1 (High — significantly improves quality)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1 | Global state assumption | Clarify "decentralized training" vs. "decentralized observation" (S4) | Improves framing and prevents misinterpretation |
| P1 | Missing limitations | Expand conclusion with limitations paragraph (S6) | Improves scientific honesty and reviewer perception |

### P2 (Nice-to-have — improves completeness)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2 | Scalability concern | Add O(N) complexity analysis (S5) | Helps practitioners understand deployment limits |
| P2 | Statistical significance | Add significance test for Formation task comparison (S7) | Strengthens empirical claims |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Theory-practice gap in Abstract/Section 5]
    → Add explicit bridge paragraph acknowledging lost guarantees
    → Restructure contribution list (merge C2+C3)
    → Expected: manuscript honesty + reviewer trust restored

[Missing quantitative results in Section 6]
    → Add results table with mean±std + violation rates
    → Add statistical significance test for key comparison
    → Expected: empirical claims become verifiable

[Weak decentralization framing]
    → Clarify "decentralized training" vs "decentralized observation"
    → Mention local-observation extension from Appendix J.5
    → Expected: scope boundaries made explicit

[Incomplete conclusion]
    → Add limitations paragraph (homogeneous assumption, scaling, theory-practice gap)
    → Expected: scientific completeness improved
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | Main comparison: DPDAC-ER vs 4 baselines | 3 tasks, N=10, continuous actions, sparse comm | Reward, cumulative cost (undiscounted) | DPDAC-ER ≈ MASAC-Lag; both safe; DPDAC-ER better in Formation | C3 (practical algorithm effective) | No numerical table; only smoothed curves; 5 seeds only |
| E2 | Communication ablation | Sparse vs. all-to-all vs. no comm | Same as E1 | No comm fails in 2/3 tasks; all-to-all no better than sparse | Communication consensus needed for safety | No analysis of why no-comm fails (dual variable divergence) |
| E3 | Constraint threshold ablation | Different cost thresholds in Swapping, Formation | Same as E1 | Lower thresholds → lower reward (expected trade-off) | Algorithm effective across safety levels | Only 2 tasks; thresholds chosen ad-hoc |
| E4 | Local observation extension | 5-agent simplified Formation; DPDAC-ER-L vs DPDAC-ER, MASAC-Lag | Same as E1 | DPDAC-ER-L performs well with sparse comm | Algorithm works under local observation | Only simplified task; Ci,t = ∅ (no observation sharing) |
| E5 | Reward-shaping baseline comparison | DAC-ER with w*ci,t penalty | Same as E1 | DAC-ER with reward shaping yields lower reward or diverges | Independent constraint handling is better | Only 3 w values tested |
| E6 | 3D Formation task (entropy regularization) | DPDAC-ER vs DPDAC in 3D | Same as E1 | DPDAC degrades significantly; DPDAC-ER stable | Entropy regularization crucial for high-dim tasks | Only one 3D task; qualitative curves only |
| E7 | Toy experiment (theoretical algorithm) | N=10, binary actions, linear critics | Reward, cost | Centralized & decentralized primal-dual achieve optimal; unconstrained baseline violates | Convergence of theoretical algorithm | Very simple setting; only 10 agents; 2 actions |

### Research-Theme Gap Diagnosis

**Weakly supported claims:**
1. **"Scalability" to larger swarms**: All experiments use N=10. The O(N) per-agent computation in the actor update and the communication overhead from consensus are not evaluated at scale (N=50, 100).
2. **"Sample efficiency" from entropy regularization**: While DPDAC-ER outperforms DPDAC, there is no comparison against other exploration methods (e.g., intrinsic motivation, count-based exploration).
3. **Robustness to communication failures**: The communication ablation tests "no communication" as an extreme but does not test intermittent failures, delayed messages, or packet loss.

### Proposed Research Experiments

**P0 Experiment: Scalability analysis**
- **Target Claim:** DPDAC-ER scales to larger swarms (N=50, 100).
- **Hypothesis:** The O(N) per-agent computation and consensus overhead will not cause significant degradation up to N=50, but may become a bottleneck at N=100.
- **Minimal Design:** Run DPDAC-ER on the Aggregation task with N=10, 25, 50, 100. Report per-step computation time, communication overhead, reward, and cost.
- **Success Criterion:** Reward and cost performance at N=50 is within 20% of N=10 performance.
- **Cost:** Low (uses existing environments; only requires varying N and adding timing instrumentation).
- **Expected Gain:** Validates (or bounds) the scalability claim, identifies bottlenecks.

**P1 Experiment: Statistical robustness**
- **Target Claim:** DPDAC-ER reliably finds safe policies.
- **Hypothesis:** The safety constraint satisfaction is statistically significant across multiple seeds.
- **Minimal Design:** Run DPDAC-ER for 10 seeds (instead of 5) on all three tasks. Report mean ± std of cost and reward at convergence. Perform paired t-test between DPDAC-ER and MASAC-Lag.
- **Success Criterion:** Cost constraint satisfied in ≥ 8/10 seeds; reward difference with MASAC-Lag is statistically significant.
- **Cost:** Low (5 more seeds per task).
- **Expected Gain:** Strengthens empirical credibility.

**P2 Experiment: Communication robustness**
- **Target Claim:** DPDAC-ER is robust to realistic communication imperfections.
- **Hypothesis:** DPDAC-ER degrades gracefully under random communication link failures and delays.
- **Minimal Design:** Add two scenarios: (a) random link failures with probability p ∈ {0.1, 0.3}, (b) delayed consensus updates with lag of 1-2 time steps. Compare with the current sparse communication setting.
- **Success Criterion:** Safe policies maintained (cost ≤ threshold) with ≤ 15% reward degradation under p=0.1 link failure rate.
- **Cost:** Medium (modifying communication simulation).
- **Expected Gain:** Demonstrates practical applicability beyond idealized settings.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper has meaningful theoretical contributions (homogeneous constrained MG formulation, convergence analysis for the on-policy linear-critic variant) and a well-motivated practical algorithm. However, the significant theory-practice gap, the lack of quantitative empirical reporting, and the inflated contribution structure reduce the overall research value and validity confidence. The novelty cannot be fully assessed in this run due to Retrieval-Disabled Mode, and the strong global-state assumption limits the practical scope of the decentralization claim. The score prioritizes research value and methodological soundness as primary dimensions.

**Post-Revision Target: [6.5, 7.5] / 10**

**Expected improvement after revision:** If the authors address the P0 items (theory-practice bridge paragraph, quantitative results table, restructured contributions) and at least one P1 item (clarified decentralization framing, expanded conclusion with limitations), the paper would be significantly stronger. The upper bound of 7.5 assumes that a follow-up manual novelty verification confirms the contributions as partially overlapping (not substantially overlapped) with existing literature. If novelty is found to be substantially overlapped, the score ceiling would be lower.

| Dimension | Score (out of 10) | Weight | Notes |
|-----------|------------------|--------|-------|
| Research Value | 6 | High | Solves an important problem (decentralized safe MARL) but with restrictive assumptions |
| Novelty | Deferred | High | Cannot assess without literature retrieval |
| Soundness/Validity | 5 | High | Theory is sound for on-policy version; practice version lacks guarantees |
| Reproducibility | 5 | Medium | Pseudocode provided; but no numerical tables, hyperparameters in appendix only |
| Presentation | 6 | Medium | Well-structured but abstract is slightly misleading; writing is generally clear |