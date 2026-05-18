- Decision: Reject
- Scores: 3, 6, 3

## Merged Review

### Summary
This paper addresses extrapolation error in cooperative multi-agent reinforcement learning (MARL). The authors argue that value factorization methods such as QMIX mitigate extrapolation error by focusing on local utilities, but do not fully eliminate it. To further reduce extrapolation errors, they propose two simple modifications: annealed multi-step bootstrapping and ensembled independent value functions. The methods are evaluated on QMIX in SMAC, SMACv2, and Google Research Football (GRF), and on on-policy algorithms (MADDPG, FACMAC) in SMAC. Results show performance improvements over baselines. The paper also includes theoretical analysis of extrapolation error propagation and ablation studies.

### Strengths
- The paper provides a theoretical analysis of extrapolation error propagation in MARL and argues that value factorization helps mitigate this error.
- The proposed modifications (annealed multi-step bootstrapping and ensembled independent value functions) show consistent performance improvements over baselines across multiple environments (SMAC, SMACv2, GRF) and on-policy algorithms (MADDPG, FACMAC).
- Ablation studies on ensemble size and the lambda annealing parameter are included.
- One reviewer found the paper well-written, clear, and easy to follow; another commended the testing across numerous maps.
- Extrapolation error in online MARL is a relatively unexplored topic; the paper is among the first to address it with both analysis and mitigation methods.

### Weaknesses
- **Lack of novelty and limited MARL-specific insights**: Two reviewers (1 and 3) argue that the work lacks novelty. The techniques are adapted from single-agent RL without new insights unique to multi-agent settings. The discussion on extrapolation error is seen as a natural extension that does not address challenges specific to MARL such as agent interdependence and coordination. One reviewer notes the paper reads like a stitching together of existing works rather than providing a new perspective.
- **Insufficient experimental rigor**:
  - Main results (Table 1) lack standard deviations, hindering assessment of significance. The number of seeds, evaluation procedure, and evaluation interval are not reported.
  - No implementation details or hyperparameter searches are provided for baseline methods; parameters were only searched for the proposed method, which may bias results.
  - Two of the three environments are SMAC and SMACv2, which share similarities; a more diverse environment set would strengthen the evaluation.
  - Some learning curves are missing in Appendix Figure 10 (last column).
- **No direct evidence that the proposed method mitigates extrapolation error**: The paper claims that the techniques reduce extrapolation error, but no results directly measure or compare extrapolation error between methods. The Target Estimation Error (TEE) could be influenced by overestimation due to the max operator, and no analysis disambiguates these factors.
- **Parameter sharing and model capacity confounding**: It is unclear whether parameter sharing was used in baselines. If so, the ensemble introduces many more parameters (each agent has multiple value networks), which could explain improvements rather than extrapolation error mitigation. This is especially concerning because small ensembles (M=1,2) perform worse than the QMIX baseline. The paper should disentangle capacity from extrapolation reduction.
- **Fundamental limitations of value factorization**: The claim that value factorization mitigates extrapolation error is not comprehensive. The factorization assumes independence of agent utilities and may fail when an agent’s optimal action depends on others’ actions, potentially leading to suboptimal Nash equilibria. The paper does not address the impact of this assumption on solution quality.
- **Writing clarity and logical consistency** (one reviewer): While one reviewer found the paper well-written, another criticizes the writing as messy, with subjective statements lacking evidence (e.g., line 352 on behavior policy alignment after convergence). Some conclusions are inconsistent with results (e.g., line 294 states λ_max increases leading to performance degradation, but Figure 2 shows λ_max decreasing and performance improving). Too many results are placed in the appendix but referenced in the main text, affecting readability.
- **Missing justifications**: The paper switches from analyzing QPLEX (Section 3) to using QMIX (Section 4) without explanation. A justification is needed.