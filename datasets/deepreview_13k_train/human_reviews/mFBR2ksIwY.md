# MACCA: Offline Multi-agent Reinforcement Learning with Causal Credit Assignment

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Offline Multi-agent Reinforcement Learning (MARL) is valuable in scenarios where online interaction is impractical or risky. While independent learning in MARL offers flexibility and scalability, accurately assigning credit to individual agents in offline settings poses challenges because interactions with an environment are prohibited. %partial observability and emergent behavior. 
In this paper, we propose a new framework, namely \textbf{M}ulti-\textbf{A}gent \textbf{C}ausal \textbf{C}redit \textbf{A}ssignment (\textbf{MACCA}), to address credit assignment in the offline MARL setting.
Our approach, MACCA, characterizing the generative process as a Dynamic Bayesian Network, captures relationships between environmental variables, states, actions, and rewards. Estimating this model on offline data, MACCA can learn each agent's contribution by analyzing the causal relationship of their individual rewards, ensuring accurate and interpretable credit assignment. Additionally, the modularity of our approach allows it to seamlessly integrate with various offline MARL methods. Theoretically, we proved that under the setting of the offline dataset, the underlying causal structure and the function for generating the individual rewards of agents are identifiable, which laid the foundation for the correctness of our modeling. In our experiments, we demonstrate that MACCA not only outperforms state-of-the-art methods but also enhances performance when integrated with other backbones.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents the MACCA algorithm, which describes the generation process as a dynamic Bayesian network, capturing the relationships among variables, states, actions, and rewards in the environment. By analyzing the causal relationships of agent rewards, it learns the contribution of each agent, addressing the credit assignment problem in offline multi-agent reinforcement learning. Specifically, MACCA employs the Bayesian network $G$ to construct the causal relationships among states, actions, and individual rewards. It models the relationship of state $\boldsymbol{s}$ and action $\boldsymbol{a}$ to individual reward $r_t^i$ through masks $C^{i, s \rightarrow r}$ and $C^{i, a \rightarrow r}$ MACCA's loss integrates losses from both the causal model and the policy model. MACCA's superiority is demonstrated on offline datasets from MPE, MA-MuJoCo, and SMAC.

### Strengths
1. The paper is well-written and easy to understand.  The original contributions are highlighted clearly.
2. This paper provides a thorough and complete set of theoretical proofs. The proofs provided are clear, rigorous.
3. Experiments/ablations are abundant, and experimental results are convincing.

### Weaknesses
1. While MACCA establishes causal relationships among states, actions, and individual rewards in offline datasets, this "causal relationship" doesn't seem to have a strong correlation with offline multi-agent reinforcement learning. It appears that this "causal relationship" might also be applicable in online reinforcement learning，rather than being specifically designed for offline multi-agent reinforcement learning. The core issue is that the causal modeling, while interesting, doesn't inherently address the unique challenges of offline MARL, such as the lack of exploration and potential distributional shift between the offline data and the target policy's state-action space. The paper needs to better justify why this causal approach is particularly beneficial in the offline setting compared to other methods that directly address the offline challenges.
2. The design specifics of $c^{i, s \rightarrow r}$ and $c^{i, a \rightarrow r}$ are not elaborated upon, and the particular networks used are not clearly mentioned. It is unclear how the binary masks are generated and what the architecture of the networks $\psi_g^{s \rightarrow r}$ and $\psi_g^{a \rightarrow r}$ are. This lack of detail makes it difficult to understand the implementation and reproduce the results. Specifically, the dimensions of the input and output layers, the activation functions used, and the number of hidden layers should be explicitly stated.
3. There isn't much explanation regarding the setting of the hyperparameter $h$, nor is there any mention of whether the value of $h$ remains consistent across different offline environments. The paper lacks a clear explanation of how the threshold $h$ is chosen and whether it is tuned for each environment or kept constant. The sensitivity of the algorithm to this hyperparameter and its impact on performance should be discussed. Furthermore, the rationale behind using a fixed threshold across different environments needs to be justified, considering that different environments may have different scales of rewards and state/action spaces.
4. Concrete code has not been provided.

### Questions
1. Is the MACCA algorithm applicable to online reinforcement learning? Because it seems that in online reinforcement learning, causal relationships can also be applied, and the causal relationships among states, actions, and individual rewards can be constructed through Bayesian networks. Why is it emphasized that the MACCA algorithm is primarily for offline environments?
2. The paper's explanation regarding the setting and values of the hyperparameter $h$ seems to be unclear. Is the value of $h$ set the same across all offline datasets?
3.  In the ablation study section, the impact of $\lambda_1$ on the causal structure, specifically its influence on the state's effect on individual rewards, was explored. However, has the impact of $\lambda_2$ on the causal structure been considered? I didn't see this part being researched in the paper.
4.  In the related work section on multi-agent credit assignment, it seems that recent approaches in value decomposition, such as wqmix, qplex, resq, etc., have not been considered. These methods tackle the credit assignment challenge among agents using value decomposition techniques and, from what I understand, they have demonstrated commendable performance. Have you considered applying the methods from wqmix, qplex, resq, etc., to offline multi-agent environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies offline multi-agent reinforcement learning. It proposes to learn the causal structure between states and actions and the team reward from the offline dataset with supervised learning to tackle the credit-assignment problem. Experiments are conducted to demonstrate the effectiveness of the algorithm.

### Strengths
1. The empirical performance looks compelling.
2. The idea of extracting the causal structure behind the team reward is interesting.
3. This paper is clearly written and easy to follow.

### Weaknesses
1. The presumed data-generating process is restrictive.

Minor Mistake:
There is a 'shaply' on the seventh line of the first paragraph of Section 5

### Questions
1. Have the authors ever considered extending the algorithm to scenarios where the team reward cannot be decomposed as the sum of individual rewards? What can be the possible solution?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper looks into the problem of credit assignment for individual agents in a shared environment, with the potential impact of other issues such as partial observability and emergent behavior. Specifically in offline multi-agent reinforcement learning (MARL) settings, the diversity in different distributions of data complicates the task of assigning individual credits. To address this problem, the paper proposes a framework named Multi-Agent Causal Credit Assignment (MACCA). After discussing the related work in offline MARL and multi-agent credit assignment and the preliminaries of the method, the paper breaks down the MACCA framework into offline data generation, causal model learning, and policy learning with assigned individual rewards. The estimates of the observation and reward produced by the agents in the policy learning phase are fed into the policy network for generating the next-state actions. The authors conducted experiments in various environments and compared their method with the other baselines that follow the centralized training with decentralized execution (CTDE) and independent learning paradigms. They also carried out ablation studies to evaluate the interpretability and efficiency of their approach.

### Strengths
The methodology in this paper is written in an organized manner. At the start of section 4, the two major components (causal and policy models) are described. The overall objective is defined and then elaborated in the subsections. It is very obvious that the method consists of generative process, causal model learning phase, and policy optimization by reading this section. In the experiments, a sufficient number of baselines are applied for performance comparison and most of them are relatively new. Three different MARL testbeds are used for evaluation, which shows the generalization capability of the method. Careful ablation studies are performed in order to clarify the impacts of causal structure, ground truth individual reward, and causal graph setting. Furthermore, the math used here is formal and clear, improving the soundness of this work. The proof of identifiability is correct and a good supplement to the paper.

### Weaknesses
The overall writing quality needs to be improved. There are some grammatical errors, and the details will follow.

Although the evaluation of MACCA has been conducted in multiple benchmarks to demonstrate its generalizability, it is questionable whether the method has top performance in all of the environments that belong to a specific benchmark. For example, the SMAC benchmark has more than 20 original battle scenarios, including a few Super Hard challenges. However, only three of the maps, including a single Super Hard challenge, are shown in the results. It is unclear if the method would perform as well across the full suite of SMAC environments, especially given the diversity of challenges they present.

Regarding the MACCA architecture, clearly, the policy learning part is crucial for the model. However, this part is mostly taken from previously established methods such as I-CQL, OMAR and MA-ICQ, especially the term $J_{\pi}$. Also, after looking at the experiments in different environments, it is not clear whether MACCA-CQL, MACCA-OMAR, or MACCA-ICQ has the SOTA performance overall. The paper does not provide a clear comparison of these variants, making it difficult to assess the specific contribution of the causal credit assignment method.

The code for the proposed method is not included in the submission. The disclosed information about the hyper-parameters and environmental settings is limited. This lack of transparency makes it difficult to reproduce the results and evaluate the practical applicability of the method. Specifically, the absence of detailed hyperparameter tuning strategies and sensitivity analysis hinders a thorough understanding of the method's robustness.

A few more points worth mentioning:
 
- The figure or the algorithm in Appendix D can be moved to the main paper to improve the clarity of the description for MACCA.
 
- In section 3, when defining the Dec-POMDP, an additional $\Omega$ is included in the tuple as it denotes the joint observation space. Then the observation function is expressed as $\mathcal{O}(s, i) : \mathcal{S} \times \mathcal{A} \rightarrow \Omega$.
 
- In section 4.1: Define $D_s$ and $D_a$ as the {numbers} of dimentions of ... The {masks}... are vectors and ...

- In section 4.2: $\psi_r$ is {used} for {approximating} ...

- In section 4.3: each agent's state-action-id {tuple} ...

- In the first paragraph of section 5: ... variants of credit assignment method using {Shapley} value, ...

### Questions
-In section 4.1, are the masks in the expression for the reward learned or manually set?

-There is a long and confusing sentence in section 4.2: "Its primary objective is to ... reduce the number of features that a given depends on, ... mitigates the risk of overfitting." What does "reduce the number of features that a given depends on" mean?

-Is the hyper-parameter $h$ learned?

-Can you mention how many independent tasks do the Multi-agent Particle Environment and the Multi-agent MuJoCo have, respectively?

-In section 5.3 you mentioned that "It is important to note that our method is not highly sensitive to the hyperparameters despite using them to control the learned causal structure." Can you justify this argument?

-You showed the visualizations of two causal structures in MPE. Have you done similar work in MA-Mujoco and SMAC?

-In the sub-section "Visualization of Causal Structure." in 5.3, what do "S2R" and "A2R" stand for?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
MACCA is a reward decomposition mechanism in offline MARL, which follows centralized training and decentralized execution. It factorizes the shared global reward into individual rewards according to the causal relationship among states, actions, and rewards. The individual rewards can be seamlessly optimized by existing offline MARL methods. The experiments are performed on offline datasets of MPE, MA-MuJoCo, and SMAC.

### Strengths
+ The paper is well-organized.
+ The experiments are extensive, and MACCA achieves performance gain.
+ The experiment settings and hyper-parameters are detailed.

### Weaknesses
There are two main drawbacks in this paper:

The target of credit assignment is not the immediate reward, but the cumulative reward of the whole trajectory, which is affected by the immediate reward and the transition (long-horizon rewards). However, this paper only considers the decomposition of immediate reward, ignoring the long-horizon causal relationship. For example, in the delayed reward setting (SMAC), the agents only receive the reward at the last timestep, the credit assignment of the whole trajectory in MACCA is only related to the state and actions of the last timestep, which is unreasonable.

The states of the environments adopted by this paper are low-dimension vectors. It is hard to capture the causal relationship between image state and reward.

### Questions
The proposed reward decomposition mechanism is not specific to offline MARL. The results will be more convincing if MACCA achieves performance gain in the online MARL (SMAC tasks).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
