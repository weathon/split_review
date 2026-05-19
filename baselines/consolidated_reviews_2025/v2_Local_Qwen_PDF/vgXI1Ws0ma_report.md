## Summary
# Final Review Report

## Summary
This paper proposes Empowerment through Causal Learning (ECL), a method-agnostic framework for Model-Based Reinforcement Learning (MBRL) that integrates empowerment-driven exploration with iterative causal structure optimization. The core intuition is that agents can actively leverage learned causal structures to guide exploration, maximizing mutual information between actions and future states (empowerment) to improve controllability. The data collected through this targeted exploration is then used to refine the causal dynamics model and reward model. The framework includes a curiosity-based reward to prevent overfitting to the learned causal structure during downstream task learning. Experiments across six state-based and pixel-based environments demonstrate that ECL outperforms existing causal MBRL baselines (e.g., CDL, REG, GRADER) in causal discovery accuracy, sample efficiency, and asymptotic policy performance under both in-distribution and out-of-distribution settings.

## Strengths
1. **Novel Integration of Empowerment and Causal Learning:** The paper presents a compelling and well-motivated framework that bridges intrinsic motivation (empowerment) with causal structure learning. The idea of using empowerment to guide active exploration for causal discovery is conceptually strong and addresses a clear gap in passive causal MBRL methods.
2. **Method-Agnostic Design:** ECL is designed to be compatible with diverse causal discovery methods (both constraint-based and score-based), which enhances its flexibility and practical applicability across different environments and data regimes.
3. **Comprehensive Empirical Evaluation:** The experiments are extensive, covering six environments including state-based, pixel-based, ID, and OOD settings. The inclusion of a curiosity reward to mitigate overfitting to the causal mask is a thoughtful design choice that demonstrates attention to practical robustness.
4. **Clear Framework Structure:** The three-step pipeline (model learning, model optimization, policy learning) is logically organized and easy to follow. The use of state abstractions filtered by causal masks for reward modeling is a clean and effective implementation detail.

## Weaknesses
1. **Overstated Novelty and Causal Claims:** The abstract and introduction claim that ECL "pioneers the integration of empowerment with causal reasoning" and that empowerment "implicitly discovers causal relationships." These statements are strong and potentially overstated. Empowerment maximizes mutual information, which correlates with controllability but does not strictly guarantee causal discovery without additional structural assumptions. The novelty claim requires careful bounding against existing intrinsic motivation and causal RL literature.
2. **Unjustified Simplification in Empowerment Objective:** The derivation of the empowerment-driven exploration objective (Eq. 7 to Eq. 10) simplifies the problem to optimizing only the KL divergence term, ignoring the entropy difference terms $H(s_{t+1}|s_t; M) - H(s_{t+1}|s_t)$. The manuscript does not provide a theoretical justification for dropping these terms, which could bias the exploration policy if they are significant.
3. **Ambiguity in Curiosity Reward Implementation:** The curiosity reward (Eq. 11) relies on $P_{env}$, described as "ground truth dynamics collected from the environment." In standard MBRL, the agent does not have access to true transition dynamics. It is unclear whether $P_{env}$ is approximated via a large transition buffer or if the simulator provides exact transitions, which would limit real-world applicability.
4. **Weak Causal Attribution in Results:** The results section attributes improved sample efficiency and reward attainment primarily to the curiosity reward, without isolating its contribution from the empowerment-driven exploration. A controlled ablation is needed to clarify which component drives the observed gains.
5. **Related Work Lacks Critical Differentiation:** The Related Work section reads as a list of method summaries rather than a critical comparison. It does not explicitly contrast ECL with strongest baselines (e.g., CDL, REG) along decision-relevant axes such as exploration strategy, causal discovery mechanism, or computational complexity.

## Key Issues
1. **Validity of Empowerment Objective Simplification (Major):** The omission of entropy terms in the empowerment objective derivation lacks justification. If these terms are non-negligible, the simplified KL-only objective may lead to suboptimal exploration policies, threatening the validity of the core method.
2. **Accessibility of Ground Truth Dynamics (Major):** The reliance on $P_{env}$ for the curiosity reward is ambiguous. If exact simulator transitions are used, the method's applicability to real-world settings where true dynamics are unknown is severely limited. If approximated, the estimation protocol must be explicitly detailed.
3. **Causal Attribution of Performance Gains (Major):** The manuscript attributes gains to the curiosity reward without isolating its effect from empowerment-driven exploration. Without a matched ablation, the causal link between the proposed components and the observed performance improvements remains unverified.
4. **Overstatement of Novelty and Causal Discovery Claims (Major):** Claims that empowerment "implicitly discovers causal relationships" and that ECL "pioneers" this integration are strong and require bounding. Empowerment identifies controllable variables, which may correlate with causal variables but does not strictly guarantee causal discovery without additional regularization or structural assumptions.
5. **Related Work Differentiation (Minor):** The Related Work section fails to explicitly differentiate ECL from strongest baselines along decision-relevant axes, reducing the clarity of the paper's positioning and contribution boundary.

## Actionable Suggestions
1. **Justify or Restore Entropy Terms in Empowerment Objective:** Provide a theoretical justification for dropping the entropy difference terms $H(s_{t+1}|s_t; M) - H(s_{t+1}|s_t)$ in Eq. 10. If no strong justification exists, include these terms in the practical implementation and report the impact on training stability and performance.
2. **Clarify $P_{env}$ Estimation Protocol:** Explicitly state how $P_{env}$ is accessed or estimated for the curiosity reward. If using a large transition buffer, detail the buffer size, update frequency, and density estimation method. If relying on exact simulator transitions, acknowledge this as a limitation for real-world deployment.
3. **Add Controlled Ablation for Curiosity Reward:** Include an ablation study comparing ECL with and without the curiosity reward, keeping all other components fixed. This will isolate the contribution of the curiosity bonus to sample efficiency and prevent overclaiming its causal role in performance gains.
4. **Bound Novelty and Causal Claims:** Revise the abstract and introduction to replace strong claims like "pioneers the integration" and "implicitly discovers causal relationships" with bounded, evidence-consistent wording. For example: "ECL integrates empowerment-driven exploration with iterative causal structure optimization, focusing on controllable dimensions to facilitate more accurate causal discovery."
5. **Reorganize Related Work by Comparison Axes:** Restructure the Related Work section to explicitly contrast ECL with baselines along axes such as exploration strategy (passive vs. active), causal discovery mechanism (constraint-based vs. score-based vs. variational), and computational complexity. Add a clear differentiation statement highlighting ECL's unique value.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Domain):** In Model-Based Reinforcement Learning (MBRL), causal dynamics models improve generalization by filtering irrelevant state dimensions, but existing methods often learn these structures passively from fixed datasets.
- **S2 (Gap/Challenge):** Passive causal learning leads to inefficient exploration and slow convergence, as agents lack strategies to actively refine causal structures with high-quality, controllability-focused data.
- **S3 (Proposed Method):** We propose Empowerment through Causal Learning (ECL), a method-agnostic framework that integrates empowerment-driven exploration with iterative causal structure optimization to enhance agent controllability.
- **S4 (Key Results):** Evaluated across six state-based and pixel-based environments, ECL consistently outperforms causal MBRL baselines in causal discovery accuracy, sample efficiency, and asymptotic policy performance under both ID and OOD settings.
- **S5 (Bounded Implication):** These results demonstrate that actively leveraging causal structures for exploration facilitates more robust and efficient policy learning, with implications for scalable causal world modeling.

### Introduction Outline (Complete)
- **P1 (Big Picture):** MBRL leverages predictive dynamics models to enhance planning and sample efficiency. Integrating causal structures filters irrelevant variables, improving generalization and robustness against spurious correlations.
- **P2 (Concrete Gap):** However, current causal MBRL methods typically learn structures passively, missing opportunities to guide exploration. This passivity results in suboptimal data collection and slower causal model refinement.
- **P3 (Proposed Idea):** We hypothesize that agents can actively leverage causal structures to maximize empowerment (mutual information between actions and future states), focusing exploration on controllable dimensions and generating higher-quality transitions.
- **P4 (Method Overview):** ECL alternates between empowerment-driven exploration and causal mask optimization. A curiosity reward is introduced to prevent overfitting to the learned causal structure during downstream task learning.
- **P5 (Evidence Preview):** Experiments across diverse environments show ECL achieves superior sample efficiency and causal discovery accuracy compared to baselines like CDL and REG, validating the benefits of active causal exploration.
- **P6 (Contribution Summary):** We contribute (1) a method-agnostic framework integrating empowerment with causal learning, (2) an alternating optimization procedure for joint policy and mask refinement, and (3) extensive empirical validation across ID/OOD and pixel-based settings.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Justify or restore entropy terms in empowerment objective (Eq. 10). | Resolves validity risk in core method derivation. | Low-Medium |
| **P0** | Clarify $P_{env}$ estimation protocol for curiosity reward. | Ensures reproducibility and clarifies real-world applicability. | Low |
| **P1** | Add controlled ablation isolating curiosity reward vs. empowerment exploration. | Strengthens causal attribution of performance gains. | Medium |
| **P1** | Bound novelty and causal claims in Abstract/Introduction. | Improves scientific defensibility and reduces overstatement risk. | Low |
| **P2** | Reorganize Related Work by comparison axes and add differentiation statement. | Enhances paper positioning and clarity of contribution boundary. | Low |
| **P2** | Expand experimental fairness details (seeds, compute budget, hyperparameter tuning). | Improves reproducibility and baseline comparison credibility. | Low |

**Execution Strategy:**
1. **Week 1:** Address P0 items by revising the empowerment objective derivation and clarifying the $P_{env}$ implementation details. Update the Abstract and Introduction to bound claims.
2. **Week 2:** Execute P1 ablation study (ECL w/ vs. w/o curiosity reward) and integrate results into the main text or Appendix.
3. **Week 3:** Refine Related Work structure and add experimental fairness details. Perform final proofreading and consistency checks across all sections.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Task learning performance across environments | Chemical, Physical, Manipulation; Baselines: CDL, REG, GNN, MLP | Episodic Reward Mean | ECL-Con attains highest reward across 3 environments | Superior policy learning | Lacks ablation isolating curiosity reward |
| E2 | Sample efficiency analysis | Chemical (Full), Physical, Manipulation (Pick); Baselines: CDL, ECL-Sco | Episode Reward Mean over episodes | ECL shows elevated sample efficiency vs CDL | Improved learning efficiency | No statistical significance tests reported |
| E3 | Causal graph learning accuracy | Chemical (Chain, Collider, Full); Baselines: CDL, REG, GRADER | Accuracy, Recall, Precision, F1, ROC AUC | ECL achieves near-perfect scores in Chain/Collider | Accurate causal discovery | Limited to chemical environments in main text |
| E4 | OOD generalization | Chemical, Manipulation; ID vs OOD state predictions | Mean Accuracy, Log-likelihood | ECL maintains performance in OOD settings | Strong generalization | OOD construction method not fully detailed |
| E5 | Pixel-based task learning | Robodesk, Cartpole, DMC; Baseline: IFactor | Average Return, Visualization | ECL surpasses IFactor in Robodesk | Efficacy in latent state environments | Limited to 3 pixel-based tasks |

### Research-Theme Gap Diagnosis
The core research-value claims (new knowledge in active causal exploration, reproducibility of empowerment-driven optimization, and impact on sample efficiency) are partially supported. The main gap is the lack of controlled ablations to isolate the contribution of the curiosity reward versus empowerment-driven exploration. Additionally, the theoretical justification for simplifying the empowerment objective is missing, which weakens the methodological robustness claim.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| Curiosity reward contribution | Curiosity reward prevents overfitting to causal mask, improving downstream performance. | Run ECL with and without curiosity reward on Chemical/Manipulation tasks. | ECL-full vs ECL-no-curiosity | Episodic Reward, Success Rate | Statistically significant gain with curiosity reward | 1-2 days | Isolates component contribution, strengthens causal attribution |
| Entropy term impact | Omitted entropy terms in Eq. 10 have negligible impact on exploration policy. | Compare KL-only objective vs full objective (with entropy terms) on empowerment maximization. | ECL-KL vs ECL-Full | Empowerment Gain, Policy Reward | Comparable performance validates simplification | 2-3 days | Resolves validity risk in method derivation |
| $P_{env}$ approximation robustness | Approximating $P_{env}$ via transition buffer yields similar curiosity rewards to exact dynamics. | Vary buffer size for $P_{env}$ estimation and measure reward variance. | Exact $P_{env}$ vs Buffer sizes (1K, 10K, 100K) | Reward Variance, Policy Stability | Small variance across buffer sizes | 1 day | Clarifies real-world applicability and reproducibility |

### Traceability Rule
Every proposed experiment maps directly to unresolved core claims: E1 addresses curiosity reward attribution (Weakness 4), E2 addresses empowerment objective simplification (Weakness 2), and E3 addresses $P_{env}$ accessibility (Weakness 3). These experiments will materially improve validity, novelty, and robustness claims.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually strong and well-motivated framework that integrates empowerment-driven exploration with causal structure learning in MBRL. The method-agnostic design and comprehensive empirical evaluation across diverse environments are significant strengths. However, the score is moderated by several validity and clarity concerns: the unjustified simplification of the empowerment objective, ambiguity in the curiosity reward's reliance on ground truth dynamics, and overstated novelty/causal claims. Additionally, the lack of controlled ablations to isolate component contributions weakens the causal attribution of performance gains. Addressing these issues would substantially improve the paper's scientific defensibility and impact.

**Post-Revision Target:** [7.5, 8.5]/10

**Justification:** If the authors provide a theoretical justification for the empowerment objective simplification (or restore the entropy terms), clarify the $P_{env}$ estimation protocol, and add controlled ablations isolating the curiosity reward's contribution, the validity and robustness claims will be significantly strengthened. Bounding the novelty claims and improving the Related Work differentiation will further enhance the paper's positioning. These revisions are feasible and directly address the core weaknesses, making a strong acceptance highly achievable.