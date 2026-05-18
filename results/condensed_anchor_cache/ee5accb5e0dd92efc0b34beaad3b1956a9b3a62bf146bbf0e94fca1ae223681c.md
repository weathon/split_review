- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Merged Review

### Summary

The paper investigates representation learning in actor-critic deep RL, focusing on whether decoupling actor and critic representations leads to specialization in information encoding. Using information-theoretic metrics (mutual information), the authors find that when decoupled, the actor’s representation specializes in action-relevant features while the critic’s representation focuses on value and dynamics information. They also examine how different representation learning objectives interact with this specialization and affect sample efficiency. The study is conducted with on-policy policy gradient algorithms (PPO, DCPG) on ProcGen environments.

### Strengths

- **Novel and theoretically-grounded perspective**: The paper provides a fresh analysis of representation specialization using mutual information metrics (four metrics defined), and the claim that actor and critic objectives can contradict each other under a shared architecture is supported theoretically (e.g., Theorem 3.1). The analysis is considered interesting and novel even if the fact of decoupling leading to different representations is not surprising.  
- **Strong empirical evidence**: Extensive experiments convincingly demonstrate the impact of decoupled vs. coupled representations, and the effect of different representation learning objectives on the resulting representations. The authors test and confirm hypotheses when results contradict assumptions, uncovering novel insights such as the underestimated role of the critic in exploration.  
- **Insightful conclusions for algorithm design**: The findings on how specialized representation learning objectives (e.g., value distillation, dynamics prediction, MICo) can improve sample efficiency and generalization are considered a good contribution to the RL community. The analysis helps clarify the decoupling findings from earlier work and provides actionable guidance for designing auxiliary losses consistent with actor/critic specialization.  
- **Good quality and reproducibility**: Authors plan to release code and data. The study is well-conducted and the assumptions are reasonable.

### Weaknesses

- **Limited algorithm scope**: The study exclusively uses on-policy policy gradient methods (PPO, DCPG). It is unclear whether the conclusions hold for off-policy algorithms (e.g., DDPG, SAC, TD3) or Q-learning-based methods. This limits generalizability (Reviewers 1, 4, 5).  
- **Limited environment scope**: Experiments are performed only on discrete state and action spaces (ProcGen). It is not clear if the analysis (especially mutual information computation) can be applied to continuous control tasks, as mutual information may become intractable (Reviewer 5).  
- **Clarity and presentation issues**: Several reviewers found the writing dense and difficult to follow. Reviewer 1 noted the structure (especially Sections 6.1 and 6.2) could be improved with clearer headings, bullet points, and bolded summary sentences. Reviewer 3 highlighted overwhelming notations, unclear motivation for definitions, and many specific places where reasoning is missing (e.g., why I(Z, level ID) measures overfitting, purpose of Theorem 3.1, meaning of “increasing I(Z_A, V)” in value distillation, interpretation of Figure 3, etc.). In contrast, Reviewer 4 found the writing clear and easy to follow.  
- **Missing explanations and definitions in main text**: Key details are relegated to the appendix without sufficient high-level explanation in the main paper. Examples include: what the delta percentage represents in Figure 1, how mutual information is measured (only in appendix), the definition of the dynamics prediction objective from Moon et al. (only cited), and the MICo objective (not introduced with an equation). Figures 7 and 8 (important results) are placed in the appendix. A performance plot linking information-theoretic metrics to returns is missing (Reviewer 1).  
- **Questioned or disagree with specific claims**: Reviewer 2 disagrees with the statement that “an optimal or near-optimal representation can never be reached under a shared architecture” – arguing that from a reduced MDP viewpoint, a shared architecture can still be optimal for both policy and value, even if less concise.  
- **Role of increased compute/parameters**: The decoupled approach introduces additional compute and parameters. Reviewer 2 and Reviewer 5 note that this increased capacity may itself contribute to improved performance, and the paper does not control for this (e.g., by comparing with larger capacity shared networks). Reviewer 1 asks whether conclusions (e.g., about overfitting in coupled representations, or unintended specialization in Section 6.2) would change with larger model size or larger batch sizes.  
- **Missing ablations and clarity on metrics**:  
  - Reviewer 1 asks whether the sum I((Z,Z’); A) + I(Z,Z’) is a good performance indicator (based on Figures 3 and 7), and suggests moving Figures 7-8 to the main paper.  
  - Reviewer 1 suggests testing whether a larger batch size in PPO (as used in value distillation) alone explains the reduced overfitting.  
  - Reviewer 3 has many specific line questions about definitions and reasoning (e.g., Equation 6 variables, why I((Z*_A, Z*’_A); A) is maximized under optimal policy, why maximizing J^π biases the policy to collect trajectories with high I(O; V), why actor objective promotes invariant quantities).  
  - Reviewer 4 would like explicit highlight of the best representation learning objectives and most important specializations with quantitative measures.  
  - Reviewer 5 asks whether conclusions hold for continuous environments and suggests adding minimize/maximize indicators to tables/plots for metrics.  

- **Baseline/comparison concerns**: The paper uses the idea of “context” (MDPs with different starting states); Reviewer 2 questions why this framing is needed over a standard MDP with varying start states. The evaluation breadth is considered lacking by Reviewer 2.