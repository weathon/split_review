## Summary
# Final Review Report

## Summary
This paper proposes State Decoupling with Q-supervised Contrastive representation (SDQC), a novel framework for safe offline reinforcement learning (RL). The core idea is to decouple global observations into reward-related and cost-related representations using a Q-supervised contrastive learning objective. Theoretically, the authors prove that this Q*-irrelevance representation is coarser than bisimulation while preserving the optimal policy, which should enhance generalization to out-of-distribution (OOD) states. Empirically, SDQC is evaluated on the DSRL benchmark and demonstrates superior safety performance (near-zero violations) compared to six baselines, including the recent FISOR method. The method also shows robust generalization in environments with varying obstacle configurations. The paper is well-structured and addresses a meaningful challenge in safe offline RL, though it contains critical notation errors in the method section and requires more nuanced discussion of the reward-cost trade-off.

## Strengths
1. **Novel Methodological Insight:** The proposal to decouple reward- and cost-related representations using Q-supervised contrastive learning is a creative and well-motivated approach to addressing OOD generalization in safe offline RL.
2. **Strong Theoretical Foundation:** Theorem 3.1 provides a rigorous proof that the Q*-irrelevance representation is coarser than bisimulation while preserving optimality. The entropy-based generalization argument is theoretically sound and adds significant value to the representation learning literature.
3. **Comprehensive Empirical Validation:** The experiments on the DSRL benchmark are extensive, covering multiple agents and tasks. The inclusion of generalization tests with varying obstacle counts effectively demonstrates the practical benefits of the proposed representation decoupling.
4. **Clear Ablation Studies:** The ablation studies (contrastive loss, network structure, anchor numbers) thoroughly validate the design choices and isolate the contribution of the contrastive representation learning component.

## Weaknesses
1. **Critical Notation Errors in Method:** Section 3.2 contains a critical logical error in the positive pair selection for contrastive learning (`arg min` $\Gamma$ instead of `arg max` $\Gamma$), which would invert the learning signal. Additionally, the distance definition in Eq. 4 uses a comma instead of a subtraction operator. These errors severely impact reproducibility.
2. **Insufficient Discussion of Reward-Cost Trade-off:** While SDQC achieves near-zero costs, it often yields lower rewards than baselines (e.g., AntVel). The manuscript claims SDQC "surpasses" baselines without acknowledging this deliberate safety-first trade-off, which reduces objectivity.
3. **Unscoped Novelty Claims:** The claim of being the "first to utilize decoupled representations for decision-making in safe RL tasks" is strong and requires precise scoping to state-based offline settings to avoid overgeneralization.
4. **Minor Formatting and Tone Issues:** Several typos ("proposeState", "notaiton", "limitκ") and slightly informal phrasing ("Regrettably", "It is reasonable to suspect") detract from the professional tone of the manuscript.

## Key Issues
1. **Contrastive Positive Pair Selection Error (Critical):** In Section 3.2, the positive pair is defined as $\tilde{s}_i = \arg\min_{s \in S' \setminus \{s_i\}} \Gamma(s_i, s)$. Since $\Gamma(s, \tilde{s}) = \exp(-d(s, \tilde{s})/\eta)$, minimizing $\Gamma$ maximizes the distance $d$, selecting the most dissimilar states as positives. This fundamentally breaks the contrastive learning objective. It must be changed to $\arg\max \Gamma$ or $\arg\min d$.
2. **Distance Definition Notation Error (Major):** The distance measure $d(s_1, s_2) := \sup_{a \in \mathcal{A}} |Q^*(z_\theta(s_1), a), Q^*(z_\theta(s_2), a)|$ uses a comma instead of a subtraction operator inside the absolute value. This renders the equation mathematically invalid.
3. **Reward-Cost Trade-off Omission (Major):** The experimental analysis emphasizes safety gains but omits discussion of the reward degradation relative to baselines like COptiDICE. For a constrained optimization problem, explicitly analyzing the Pareto frontier or acknowledging the safety-first design choice is essential for scientific objectivity.

## Actionable Suggestions
1. **Fix Contrastive Learning Formulation:** Change the positive pair selection in Section 3.2 to $\tilde{s}_i = \arg\max_{s \in S' \setminus \{s_i\}} \Gamma(s_i, s)$ and correct the distance definition to use a subtraction operator: $|Q^*(z_\theta(s_1), a) - Q^*(z_\theta(s_2), a)|$.
2. **Clarify Reward-Cost Trade-off:** In Section 4.1, add a paragraph discussing the reward-cost trade-off. Acknowledge that SDQC prioritizes strict safety constraints, which may result in lower rewards compared to baselines that tolerate soft constraints. Frame this as a deliberate design choice for safety-critical applications.
3. **Scope Novelty Claims:** Revise the "first to utilize decoupled representations" claim to specify "in state-based safe offline RL with Q-supervised contrastive learning" to ensure defensibility.
4. **Improve Narrative Flow:** Strengthen the transition from the Lagrangian instability discussion in the Preliminaries to the proposed HJ-based decoupling approach. Explicitly state that the instability motivates the separation of safety assessment from reward optimization.
5. **Proofread for Typos:** Correct "proposeState" to "propose State", "notaiton" to "notation", and "limitκ" to "limit $\kappa$". Replace informal phrases like "Regrettably" with "However".

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem):** Safe offline RL aims to learn safety-guaranteed policies without risky interactions, but struggles with OOD generalization during testing due to combinatorial state-space complexity.
- **S2 (Gap):** Existing methods often fail to maintain hard safety constraints under distributional shift, and classical representation learning (e.g., bisimulation) requires difficult model estimation.
- **S3 (Method):** We propose State Decoupling with Q-supervised Contrastive representation (SDQC), which decouples global observations into reward- and cost-related representations using a Q-supervised contrastive objective.
- **S4 (Theory):** We theoretically prove that SDQC yields a coarser representation than bisimulation while preserving the optimal policy, enhancing generalization.
- **S5 (Results):** Experiments on the DSRL benchmark show SDQC achieves near-zero violations in over half of the tasks, significantly outperforming baselines in safety assurance and OOD robustness.

### Introduction Outline
- **P1 (Background):** RL is powerful but unsafe for critical domains; Safe RL formulates this as CMDP.
- **P2 (Online to Offline Gap):** Online safe RL risks safety violations during training; Safe offline RL uses fixed datasets but struggles with OOD generalization in high-dimensional spaces.
- **P3 (OOD Motivation):** The core bottleneck is the inability to generalize across unseen reward-cost state combinations. Decoupling these factors can mitigate OOD failure.
- **P4 (Proposed Solution):** SDQC decouples observations into reward/cost representations using Q-supervised contrastive learning, avoiding model estimation errors.
- **P5 (Theoretical & Empirical Preview):** Theoretically coarser than bisimulation; empirically achieves superior safety and generalization on DSRL benchmarks.
- **P6 (Contributions):** 1) Novel SDQC framework, 2) Theoretical entropy bound proof, 3) Comprehensive empirical validation.

## Priority Revision Plan
| Priority | Issue | Action | Expected Impact |
|---|---|---|---|
| **P0 (Critical)** | Contrastive positive pair selection error (`arg min` $\Gamma$) | Change to `arg max` $\Gamma$ or `arg min` $d$. | Fixes fundamental learning signal; ensures method works as intended. |
| **P0 (Critical)** | Distance definition notation error (comma instead of minus) | Correct to $|Q^*(z_\theta(s_1), a) - Q^*(z_\theta(s_2), a)|$. | Restores mathematical validity and reproducibility. |
| **P1 (Major)** | Reward-cost trade-off omission | Add discussion acknowledging lower rewards for higher safety. | Improves objectivity and scientific rigor. |
| **P1 (Major)** | Unscoped novelty claims | Scope "first" claim to state-based safe offline RL. | Prevents reviewer pushback on overgeneralization. |
| **P2 (Minor)** | Typos and informal tone | Fix "proposeState", "notaiton", "limitκ"; replace "Regrettably". | Enhances professional presentation. |
| **P2 (Minor)** | Weak motivation transition | Link Lagrangian instability to HJ decoupling motivation. | Strengthens narrative cohesion. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | SDQC vs SOTA baselines on DSRL | Safety-Gymnasium, Bullet-Safety-Gym; 3 seeds | Normalized reward, cost | SDQC achieves near-zero cost in >50% tasks | Safety superiority | Reward-cost trade-off not analyzed |
| E2 | Generalization to unseen obstacles | CarGoal, CarPush with varying obstacle counts | Reward, cost | SDQC maintains safety; baselines fail | OOD robustness | Limited to obstacle count variation |
| E3 | Ablation: Contrastive loss | CarGoal2 w/ and w/o contrastive loss | Reward, cost, t-SNE | Loss degrades performance and clustering | Contrastive necessity | Single task evaluated |
| E4 | Ablation: Network structure | ATN vs MLP encoder | Reward, cost | ATN outperforms MLP | Encoder design | Hyperparameter sensitivity not fully explored |

### Research-Theme Gap Diagnosis
The core claim of OOD generalization is well-supported by obstacle variation tests, but lacks evaluation under other distributional shifts (e.g., dynamics changes, sensor noise). The reward-cost trade-off is under-analyzed, leaving the practical utility in reward-sensitive safety tasks unclear.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| OOD Robustness | SDQC generalizes beyond obstacle shifts | Test under dynamics perturbations or sensor noise | FISOR, BCQ-Lag | Reward, cost | Stable cost under perturbation | Low | Broader OOD validation |
| Reward-Cost Trade-off | SDQC operates on safe Pareto frontier | Vary cost constraint $\kappa$ and plot reward vs cost | COptiDICE, CDT | Reward, cost | Clear Pareto improvement | Low | Objective trade-off analysis |
| Computational Efficiency | Three-phase training overhead is justified | Measure training/inference time vs safety gain | FISOR | Time, cost | Safety gain outweighs time cost | Low | Practical deployment insight |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a novel and theoretically grounded approach to safe offline RL, with strong empirical results on safety assurance. The theoretical contribution (Theorem 3.1) is a significant strength. However, the score is reduced due to critical notation errors in the method section (contrastive positive pair selection and distance definition) that threaten reproducibility, and the lack of nuanced discussion regarding the reward-cost trade-off. These issues are fixable but currently undermine the methodological rigor.

**Post-Revision Target:** [7, 8]/10

**Justification:** If the critical notation errors are corrected and the reward-cost trade-off is properly analyzed, the paper will be methodologically sound and objectively presented, significantly strengthening its contribution to the safe offline RL community.