## Summary
# Final Review Report

## Summary
This paper introduces Submodular Reinforcement Learning (SUBRL), a framework for optimizing history-dependent rewards that exhibit diminishing returns, modeled via submodular set functions. The authors establish that general SUBRL is hard to approximate within logarithmic factors, even for deterministic MDPs. To address this, they propose SUBPO, a policy gradient algorithm that decomposes trajectory rewards into marginal gains to reduce variance and improve sample efficiency. The paper provides theoretical guarantees, showing that SUBPO achieves constant-factor approximations under specific assumptions (e.g., $\epsilon$-Bandit SMDPs and bounded curvature). Empirically, SUBPO is evaluated across diverse tasks, including biodiversity monitoring, Bayesian experiment design, and high-dimensional continuous control (car racing, MuJoCo Ant), demonstrating superior performance and scalability compared to modular RL baselines.

## Strengths
1. **Novel Problem Formulation:** The paper addresses a meaningful gap in RL by formalizing submodular rewards, which naturally capture diminishing returns in applications like coverage control and experiment design. This extends beyond standard additive MDPs and convex RL frameworks.
2. **Theoretical Rigor:** The authors provide a solid theoretical foundation, including an inapproximability result for general SUBRL and provable constant-factor approximation guarantees under specific assumptions (e.g., $\epsilon$-Bandit SMDPs and bounded curvature). The connection to DR-submodular optimization is well-motivated.
3. **Effective Algorithm Design:** SUBPO's use of marginal gain decomposition for policy gradient estimation is intuitive and empirically effective. The variance reduction mechanism leverages the submodular structure to provide more stable updates compared to trajectory-level rewards.
4. **Comprehensive Empirical Evaluation:** The experiments cover a wide range of tasks, from discrete grid worlds to high-dimensional continuous control (car racing, MuJoCo Ant), demonstrating the versatility and scalability of the proposed framework.

## Weaknesses
1. **Abrupt Narrative Transitions:** The introduction and abstract lack a clear, standalone problem statement. The transition from standard RL to submodular rewards is abrupt, and the specific gap in prior work (e.g., limitations of convex RL or adaptive submodularity) is not explicitly articulated.
2. **Vague Implementation Details:** The discussion on baselines and actor-critic extensions is high-level. It is unclear whether the critic should estimate the total submodular reward or the expected cumulative marginal gains, which is critical for reproducibility and variance reduction.
3. **Insufficient Experimental Analysis:** While results are reported, the analysis of *why* baselines fail (e.g., MODPO getting stuck) is superficial. The mechanism of redundant coverage due to lack of history tracking is not explicitly explained. Additionally, sample efficiency gains are not quantified.
4. **Overstated Novelty Claims:** The claim of being the "first work to consider submodular objectives in RL" is strong and potentially contestable by related work in adaptive submodularity or non-Markovian RL. This claim should be bounded or softened to maintain defensibility.
5. **Brief Conclusion:** The conclusion merely repeats introduction claims without summarizing key empirical insights, acknowledging limitations, or proposing concrete future work.

## Key Issues
1. **Claim-Evidence Alignment in Novelty:** The "first work" claim lacks precise scoping. Without explicit comparison to adaptive submodularity and convex RL, readers cannot assess the true incremental contribution. *Risk:* Rejection for overstated novelty. *Fix:* Soften claim to "to our knowledge" and explicitly differentiate from prior frameworks in Related Work.
2. **Reproducibility of Actor-Critic Extension:** The baseline $b(\tau_{0:i})$ and critic target are ambiguously defined. *Risk:* Implementation failures or high variance in reproduced results. *Fix:* Explicitly state that the critic predicts expected cumulative marginal gains and provide the target equation.
3. **Lack of Failure Mode Analysis:** The experiments show MODPO failing but do not explain the mechanism. *Risk:* Weak empirical narrative. *Fix:* Add analysis explaining how modular rewards lead to redundant coverage and quantify sample efficiency gains (e.g., epochs to 80% coverage).
4. **Theoretical Assumption Scope:** The provable guarantees rely on $\epsilon$-Bandit SMDPs or bounded curvature, which may not hold in general continuous control tasks. *Risk:* Overgeneralization of theoretical claims. *Fix:* Clearly bound the applicability of Theorem 3 and Proposition 3 in the text and conclusion.

## Actionable Suggestions
1. **Restructure Abstract and Introduction:** Follow a clear 5-sentence logic in the abstract: Problem -> Challenge -> Gap -> Method -> Result. In the introduction, explicitly bridge the gap between non-additive rewards and submodularity, and differentiate SUBRL from convex RL and adaptive submodularity.
2. **Clarify Critic Implementation:** In Section 4, explicitly state that the value function (critic) should be trained to predict the expected sum of future marginal gains given the current history. Provide the target equation for the critic loss to ensure reproducibility.
3. **Deepen Experimental Analysis:** For each experiment, add a sentence explaining the failure mode of the MODPO baseline (e.g., redundant coverage due to lack of history tracking). Quantify sample efficiency by reporting epochs or samples required to reach a fixed performance threshold (e.g., 80% of optimal coverage).
4. **Bound Novelty Claims:** Replace "first work to consider submodular objectives in RL" with "to the best of our knowledge, this is the first work to formally analyze submodular objectives in RL under general MDP dynamics." Add a comparison table or paragraph in Related Work highlighting differences with adaptive submodularity.
5. **Expand Conclusion:** Summarize key empirical insights, acknowledge limitations (e.g., reliance on specific MDP assumptions for theoretical guarantees), and propose concrete future work (e.g., learning submodular rewards from data, integrating RNN-based state representations).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** In reinforcement learning, rewards are typically modeled as additive and Markovian, ignoring the history of visited states.
- **S2 (Significance/Challenge):** However, many practical applications like coverage control and experiment design exhibit diminishing returns, where the value of a state depends on previously visited locations, breaking the Markov assumption.
- **S3 (Prior Gap):** Standard RL frameworks struggle with these history-dependent, non-additive rewards due to exponential state-space growth and the breakdown of the Bellman optimality principle.
- **S4 (Proposed Method):** To address this, we introduce Submodular RL (SUBRL) and propose SUBPO, a policy gradient algorithm that optimizes submodular rewards by greedily maximizing marginal gains.
- **S5 (Key Result):** We establish the hardness of general SUBRL, derive constant-factor approximation guarantees under specific MDP assumptions, and demonstrate SUBPO's sample efficiency and scalability across diverse high-dimensional tasks.

### Introduction Outline (Complete)
- **P1 (Motivation & Gap):** Establish standard RL limitations for trajectory-dependent rewards. Introduce diminishing returns as a natural abstraction for coverage/experiment design. Highlight the gap: prior works (convex RL, adaptive submodularity) lack scalable policy optimization for general MDP dynamics.
- **P2 (Proposed Framework):** Introduce SUBRL and the core intuition of marginal gain decomposition. Explain how this reduces variance and enables efficient policy gradient updates.
- **P3 (Theoretical Contributions):** Summarize the inapproximability result for general SUBRL and the provable guarantees under $\epsilon$-Bandit and bounded curvature assumptions.
- **P4 (Empirical Contributions):** Preview the diverse experimental settings (discrete path planning, continuous control) and the key finding: SUBPO-M achieves performance comparable to history-tracking SUBPO-NM with superior sample efficiency.
- **P5 (Contribution Summary):** Clearly list the three main contributions (Framework/Hardness, Algorithm/Guarantees, Empirical Versatility) in distinct bullet points.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Restructure Abstract & Introduction to explicitly state problem, gap, and solution. | Improves narrative flow and reader engagement; clarifies research motivation. | Low |
| **P0** | Soften "first work" novelty claim and differentiate from adaptive submodularity/convex RL. | Increases defensibility against reviewer scrutiny on novelty. | Low |
| **P1** | Clarify critic implementation details (predict cumulative marginal gains). | Ensures reproducibility and validates variance reduction claims. | Medium |
| **P1** | Add failure mode analysis for MODPO baseline and quantify sample efficiency. | Strengthens empirical narrative and provides concrete evidence of gains. | Medium |
| **P2** | Expand Conclusion to include limitations and future work. | Provides a complete, balanced closing and guides future research. | Low |

**Page Coverage Audit:**
- Page 1: 3 annotations (Abstract, Intro P1, Intro P2) - Covered
- Page 2: 1 annotation (Preliminaries) - Covered
- Page 3: 1 annotation (Problem Statement) - Covered
- Page 4: 1 annotation (Gradient Estimator) - Covered
- Page 5: 1 annotation (Baseline/Actor-Critic) - Covered
- Page 7: 1 annotation (Related Work) - Covered
- Page 8: 1 annotation (Experiments) - Covered
- Page 9: 1 annotation (Conclusion) - Covered
- *Note: Pages 6, 10-23 contain figures, references, and appendix proofs; substantive paragraphs in main body are fully covered.*

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | SUBPO handles diminishing returns better than modular RL | Gorilla nest coverage (discrete) | Normalized $J(\pi)$ | SUBPO-M matches SUBPO-NM, beats MODPO | Sample efficiency | No variance reporting |
| E2 | History-dependence improves item collection | Grid world with item groups | Normalized $J(\pi)$ | SUBPO-NM > SUBPO-M > MODPO | History tracking value | Markovian policies insufficient |
| E3 | Submodular rewards optimize experiment design | Bayesian D-optimal design | Mutual Information | SUBPO-M efficient exploration | Versatility | Synthetic GP functions |
| E4 | SUBPO scales to continuous control | Car racing (continuous) | Lap completion rate | SUBPO learns to drive, MODPO stuck | Scalability | Coverage reward is surrogate |
| E5 | SUBPO handles high-dim observation spaces | MuJoCo Ant | Domain coverage area | SUBPO explores, MODPO stationary | High-dim scalability | Discretized reward computation |

### Research-Theme Gap Diagnosis
The core claim of sample efficiency and scalability is supported, but statistical reliability is weak due to missing variance/std reporting. The theoretical guarantees rely on simplified MDP assumptions that do not fully align with the complex continuous control tasks evaluated.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | SUBPO gains are consistent across seeds | Run E1-E5 with 5+ random seeds | Same baselines | Mean $\pm$ Std $J(\pi)$ | Overlapping CIs or significant p-value | Low | Robustness |
| Critic Target Validation | Predicting marginal gains reduces variance more than total reward | Compare critic targets in E1 | Standard value critic | Gradient variance | Lower variance with marginal target | Low | Reproducibility |
| OOD Generalization | SUBPO generalizes to unseen density maps | Train on synthetic, test on real nest data | MODPO | Coverage drop | Smaller drop for SUBPO | Medium | External validity |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Scoring Rationale:**
The paper presents a novel and theoretically grounded framework for submodular RL, with strong empirical demonstrations across diverse tasks. The core idea of marginal gain decomposition for policy gradients is intuitive and effective. However, the score is moderated by the lack of statistical variance reporting, vague implementation details for the actor-critic extension, and overstated novelty claims that need bounding. The theoretical guarantees are valuable but rely on simplified assumptions that do not fully cover the evaluated continuous control tasks. Addressing the key issues—particularly clarifying the critic target, quantifying sample efficiency, and softening novelty claims—would significantly improve the paper's defensibility and reproducibility, justifying the post-revision target.