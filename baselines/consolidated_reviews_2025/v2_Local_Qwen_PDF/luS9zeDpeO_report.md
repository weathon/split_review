## Summary
This paper addresses decentralized safe multi-agent reinforcement learning (MARL) for homogeneous systems, where agents maximize team-average return and joint policy entropy while satisfying cumulative team-average cost constraints. The authors formalize a *homogeneous constrained Markov game* model, proving that policy sharing preserves optimality and safety under permutation-invariant settings. They propose an on-policy decentralized primal-dual actor-critic algorithm with a novel consensus-based dual variable update to handle centralized constraints without a global trainer. Asymptotic convergence is established via multi-timescale stochastic approximation. Finally, a practical off-policy deep RL variant (DPDAC-ER) is developed for continuous action spaces, demonstrating effectiveness on three safety-aware multi-robot coordination tasks. The work provides a theoretically grounded framework for decentralized safe MARL, though it relies on strong symmetry assumptions and global state availability in its primary formulation.

## Strengths
- **Theoretical Rigor:** The paper provides a solid theoretical foundation by formalizing the homogeneous constrained Markov game and proving that policy sharing preserves optimality and safety under permutation-invariant settings. The convergence analysis using multi-timescale stochastic approximation is well-structured and aligns with established MARL literature.
- **Novel Algorithmic Design:** The decentralized primal-dual actor-critic algorithm creatively addresses the challenge of centralized constraints in a decentralized network. The consensus-based dual variable update and the use of permuted observations to compute joint entropy locally are elegant methodological contributions.
- **Practical Implementation:** The transition from theoretical linear critics to a practical off-policy DRL architecture (DPDAC-ER) is well-motivated. The inclusion of entropy regularization and automatic temperature adjustment enhances exploration in continuous action spaces, addressing a key limitation of prior decentralized safe MARL methods.
- **Comprehensive Evaluation:** The experiments cover three distinct safety-aware multi-robot tasks with continuous actions. The ablation studies on communication networks, constraint thresholds, and local observations provide valuable insights into the algorithm's behavior and robustness.

## Weaknesses
- **Strong Symmetry Assumptions:** The homogeneous constrained Markov game model requires strict permutation-invariance and permutation-preserving properties for state transitions, rewards, costs, and observations. This significantly restricts applicability to highly symmetric environments and limits generalizability to heterogeneous or asymmetric multi-agent systems.
- **Theoretical-Practical Gap:** The convergence analysis relies on linear critic approximators with full column rank feature matrices (Assumption 4), which contradicts the practical DRL implementation using neural networks. The manuscript does not explicitly acknowledge this gap or discuss how convergence guarantees extend to the NN-based variant.
- **Unverified Causal Claims in Results:** The results section speculates that DPDAC-ER outperforms MASAC-Lag in the Formation task due to "different policies at the early stage... sampling richer experiences." This causal explanation lacks empirical validation (e.g., policy diversity metrics or entropy coefficient ablation), reducing scientific rigor.
- **Overstated Local Observation Performance:** The ablation on local observation claims the modified algorithm "maintains its learning performance," but Appendix J.5 clearly shows performance degradation compared to global-state variants. This overstatement misleads readers about the algorithm's robustness under partial observability.
- **Missing Limitations in Conclusion:** The conclusion merely repeats the abstract without acknowledging key limitations (e.g., reliance on global state, permutation assumptions, or the theoretical-practical gap), reducing scientific transparency.

## Key Issues
1. **Claim-Evidence Mismatch in Results:** The assertion that policy diversity causes superior performance in the Formation task is speculative. Without diversity metrics or entropy sensitivity ablations, this claim lacks empirical grounding.
2. **Unbounded Novelty Claims:** Statements like "justifies the use of policy sharing in safe MARL for the first time" are risky without explicit bounding to the homogeneous constrained MG setting. Prior works may have used policy sharing heuristically in safe RL.
3. **Theoretical-Practical Disconnect:** Assumption 4 mandates linear critics for convergence proofs, but Section 5 uses neural networks. The manuscript fails to bridge this gap, leaving reviewers uncertain about the validity of convergence guarantees for the practical algorithm.
4. **Overstated Local Observation Robustness:** Claiming that DPDAC-ER-L "maintains learning performance" contradicts Appendix J.5 results showing clear degradation. This misrepresentation undermines trust in the ablation analysis.
5. **Missing Limitations Discussion:** The conclusion lacks a transparent discussion of model constraints (permutation invariance, global state reliance), which is essential for scientific defensibility and future work positioning.

## Actionable Suggestions
- **Bound Novelty Claims:** Explicitly scope the "first time" policy sharing claim to the homogeneous constrained MG setting. Acknowledge prior heuristic uses of policy sharing in safe RL to avoid overstatement.
- **Bridge Theoretical-Practical Gap:** Add a paragraph in Section 4 acknowledging that linear critics are for theoretical tractability, while NNs are used in practice. Discuss how the convergence analysis provides foundational insights for the DRL variant.
- **Validate Causal Claims:** Replace speculative explanations in the Results section with cautious observations. Add a compact ablation on entropy coefficient sensitivity or policy diversity metrics to substantiate claims about exploration benefits.
- **Correct Local Observation Claims:** Revise the ablation text to acknowledge that DPDAC-ER-L underperforms global-state variants, highlighting the value of global information when available.
- **Expand Conclusion:** Restructure the conclusion to include validated findings, bounded limitations (permutation assumptions, global state reliance), and concrete future work directions.
- **Clarify Actor Update Scaling:** Explicitly justify the `N` multiplier in Eq. (7) by explaining its origin from the gradient of the sum of `N` identical local log-probabilities under policy sharing.

## Storyline Options + Writing Outlines
**Abstract Outline:**
- S1: Define decentralized safe MARL for homogeneous systems with team-average return/entropy maximization and cumulative cost constraints.
- S2: Highlight the challenge of centralized constraints in decentralized networks and the need for robust exploration in continuous spaces.
- S3: Introduce the homogeneous constrained Markov game model, proving policy sharing preserves optimality/safety under permutation invariance.
- S4: Present the on-policy decentralized primal-dual actor-critic algorithm with consensus-based dual updates and its asymptotic convergence.
- S5: Describe the practical off-policy DRL variant (DPDAC-ER) and summarize effectiveness on three safety-aware multi-robot tasks.

**Introduction Outline:**
- P1: Establish cooperative MARL context and the impracticality of CT paradigms under limited communication.
- P2: Introduce decentralized MARL and the emerging need for safety constraints, highlighting the gap in continuous action spaces.
- P3: Explain the technical bottleneck (occupancy measure estimation, lack of entropy regularization) motivating the proposed approach.
- P4: Summarize contributions: homogeneous constrained MG model, policy sharing optimality proof, decentralized primal-dual algorithm with convergence guarantees, and practical DRL implementation.
- P5: Preview experimental validation on multi-robot coordination tasks and ablation insights.

## Priority Revision Plan
**P0 (Critical - Must Fix):**
- Bound novelty claims to the homogeneous constrained MG setting and acknowledge prior heuristic uses of policy sharing.
- Add explicit acknowledgment of the theoretical-practical gap between linear critics (Assumption 4) and NN implementation.
- Correct overstated local observation performance claims to match Appendix J.5 results.

**P1 (Major - Should Fix):**
- Replace speculative causal explanations in Results with cautious observations or add entropy sensitivity ablation.
- Clarify the `N` multiplier in Eq. (7) actor update and justify entropy scaling under local observations.
- Expand Conclusion to include validated findings, bounded limitations, and future work.

**P2 (Minor - Nice to Have):**
- Improve transition flow between CT and decentralized MARL in Introduction.
- Add policy diversity metrics to Appendix J.6 to strengthen exploration claims.
- Refine figure captions to explicitly state main conclusions and comparison baselines.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Evaluate DPDAC-ER vs baselines | 3 tasks, 10 agents, continuous actions | Reward, Cost | DPDAC-ER matches MASAC-Lag safety, outperforms in Formation | Safe decentralized learning works | No variance reporting |
| E2 | Ablation: Communication | Sparse vs all-to-all vs no comms | Reward, Cost | No comms fails; sparse suffices | Consensus necessary | No topology robustness test |
| E3 | Ablation: Constraints | Varying cost thresholds | Reward, Cost | Higher returns with weaker constraints | Trade-off balance works | Limited threshold range |
| E4 | Ablation: Local Obs | Global vs local obs (DPDAC-ER-L) | Reward, Cost | Local obs underperforms global | Global info valuable | Performance drop unaddressed |

**Proposed Research Experiments:**
- **P0: Entropy Sensitivity Ablation:** Test DPDAC-ER across varying target entropy `H0` values to validate the claim that entropy regularization drives exploration and performance gains. *Success Criterion:* Clear performance peak at reported `H0`, demonstrating causal link.
- **P1: Policy Diversity Metrics:** Compute trajectory variance or KL-divergence between agent policies during early training to empirically support the "richer experiences" hypothesis. *Success Criterion:* Higher diversity correlates with Formation task outperformance.
- **P2: Multi-Seed Variance Reporting:** Run all main experiments over ≥5 random seeds with mean±std shading. *Success Criterion:* Stable learning curves confirming result reliability.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a theoretically sound framework for decentralized safe MARL with a novel consensus-based dual update and solid convergence analysis. The practical DRL implementation addresses a meaningful gap in continuous action spaces. However, the score is moderated by strong symmetry assumptions that limit generalizability, an unaddressed theoretical-practical gap regarding critic approximators, and overstated claims in the results and conclusion sections. With targeted revisions to bound claims, acknowledge limitations, and validate causal explanations, the paper's scientific defensibility would significantly improve.

**Post-Revision Target:** [7.5, 8.5]/10