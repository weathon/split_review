# Multi-Agent Decision S4: Leveraging State Space Models for Offline Multi-Agent Reinforcement Learning

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Goal-conditioned sequence-based supervised learning with transformers has shown promise in offline reinforcement learning (RL) for single-agent settings. However, extending these methods to offline multi-agent RL (MARL) remains challenging. Existing transformer-based MARL approaches either train agents independently, neglecting multi-agent system dynamics, or rely on centralized transformer models, which face scalability issues. Moreover, transformers inherently struggle with long-term dependencies and computational efficiency. Building on the recent success of Structured State Space Sequence (S4) models, known for their parameter efficiency, faster inference, and superior handling of long context lengths, we propose a novel application of S4-based models to offline MARL tasks. Our method utilizes S4's efficient convolutional view for offline training and its recurrent dynamics for fast on-policy fine-tuning. To foster scalable cooperation between agents, we sequentially expand the decision-making process, allowing agents to act one after another at each time step. This design promotes bi-directional cooperation, enabling agents to share information via their S4 latent states or memory with minimal communication. Gradients also flow backward through this shared information, linking the current agent's learning to its predecessor. Experiments on challenging MARL benchmarks, including Multi-Robot Warehouse (RWARE) and StarCraft Multi-Agent Challenge (SMAC), demonstrate that our approach significantly outperforms state-of-the-art offline RL and transformer-based MARL baselines across most tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a Structured State Space Sequence (S4) model to enhance the learning performance of offline pre-training combined with online fine-tuning in multi-agent reinforcement learning (MARL). Experimental results demonstrate that the proposed approach outperforms both offline RL-based and transformer-based MARL algorithms across several SMAC and RWARE tasks.

### Strengths
This paper is first  to apply the S4 model to sequence-based offline MARL tasks, contributing a novel framework for improving performance in these settings.

### Weaknesses
First of all, the writing in the paper lacks clarity, and the logical flow is sometimes hard to follow. There are several instances of grammatical errors and awkward phrasing that undermine the overall readability of the paper.


The paper primarily combines the S4 model with the SE MDP framework, which does not represent a significant departure from existing methods. While the S4 model itself is innovative, its application to SE MDP does not present a new solution that clearly advances the field. The motivation for the proposed method is not fully convincing. The paper asserts that the introduction of the S4 model to the SE MDP framework provides an advantage over MADT; however, MADT is also compatible with SE MDP, and the paper does not sufficiently clarify the comparative benefits of S4. The paper should provide a more detailed analysis comparing S4 with other multi-agent methods (such as MADT, QMIX, etc.) in the same experimental settings, particularly focusing on key aspects like cooperation, information sharing, and stability. A thorough comparison would help determine whether S4 offers substantial improvements over current approaches.


It is easy to see that using s4 model improves the ability of representation, and thus the results are not surprising.  The experimental evaluation is insufficient, and the paper would benefit from comparisons across a broader range of SMAC maps.  Additionally, the paper mentions that online fine-tuning has limited effectiveness, with some cases showing performance degradation. However, the authors do not provide a clear explanation of why this occurs, nor do they offer potential solutions to mitigate this issue. It is worth noting that in the SMAC 2c vs 64zg task, the proposed MADS4 method shows lower average returns with on-policy training without offline pretraining compared to MAPPO (which achieves a 100% win rate and an average return of 20.0), raising concerns about the practical effectiveness of the method.

### Questions
1. What does the sequential decision-making process bring to the cooperation in MARL, particularly in environments with limited communication or delayed feedback?
2. Could you provide a detailed computational comparison between the MADS4 and MADT methods, particularly in terms of training time, scalability, and computational complexity?
3. In Figure 4, could you clarify the number of interactions represented on the x-axis? Specifically, how many interactions correspond to the 60$\times$1e3 training iterations?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates using Structured State Space Sequence (S4) models for multi-agent offline reinforcement learning. The authors extend the Decision S4 model, originally designed for single-agent RL, to a multi-agent setting, following the decision transformer approach that frames offline RL as a sequence modeling problem. To enable cooperation among agents, the authors adopt a sequentially expanded MDP (SE-MDP) paradigm, dividing each decision-making step into mini-steps. Agents share information through the latent representation of S4 models. The proposed approach is evaluated on a subset of the Multi-Robot Warehouse (RWARE) and StarCraft2 Multi-Agent Challenge (SMAC) benchmarks. Experimental results demonstrate that the proposed approach outperforms several baseline methods.

### Strengths
**Originality & Significance**

While there is abundant research on using S4 for reinforcement learning, there is limited work on adapting S4 in a multi-agent offline RL setting. This work is well-placed in the literature and could provide the community with valuable insights on the effectiveness of S4 in multi-agent offline RL.


**Clarity**

The paper is well-structured and generally easy to follow. However, some technical details require further clarification. For instance, the model inference process and communication costs could be elaborated upon. Please refer to the "Weaknesses" section for a more detailed discussion.

### Weaknesses
1. The reviewer has some concerns about the experimental results presented in the paper. Specifically, only one sequence-based baseline (MADT) is used, and the improvements demonstrated by the proposed method over this baseline are relatively small, with some falling within confidence intervals. To strengthen the experimental section, the reviewer suggests comparing the proposed method with more competitive baselines o, such as [a], which have been reported to achieve better results on SMAC than MADT. This would provide a more convincing demonstration of the effectiveness of the proposed method.

2. The reviewer found some technical contents that need further clarification. Specifically, the mechanism for information sharing during the testing and inference phases remains unclear. The current configuration, which appears to involve a chain of information sharing, could potentially introduce dependencies between agents during inference. If the reviewer understands correctly, the authors use the S4 convolutional nature to address the issue.However, the precise methodology remains unclear. This is a crucial technical aspect of the paper and requires further elaboration.


3. The reviewer found some citations missing, which may lead to confusion. For example, the Methodology section discusses the concept of Sequentially Expanded MDPs without providing any accompanying citations. This omission could lead to confusion among readers regarding the original contributions of this work versus those of prior research.The reviewer recommends that add appropriate citations, such as [b], and explicitly differentiate between the elements that are drawn from existing literature and the novel contributions introduced in this work. This clarification will enhance the overall transparency and understanding of the research presented.

### Questions
1. In a sequentially expanded MDP, how to decide the order of agents? Does the order have a significant impact on the overall performance? 

2. L52 - L53. Please provide citations for the mentioned regularization methods. It is unclear to the reviewer what ‘these regularization techniques’ are referring to and why it is challenging.

3. Could you elaborate on the potential communication cost and delay by sharing the information among all agents? Would it be scalable to hundreds of agents? 

4. There are some inconsistencies between figure 2 and Algo 1. In Figure 2, the agent doesn’t take observations as input, but in Algo 1 it does. 

5. Algo 1, what is $d^t_i$? Please provide a formal definition.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes using the Structured State Space Sequence (S4) model for offline MARL and tests it on the Multi-Robot Warehouse (RWARE) and StarCraft Multi-Agent Challenge (SMAC).

### Strengths
This work is interesting in exploring whether offline MARL could benefit from advancements in models such as S4.

### Weaknesses
(1) The motivation for using S4 instead of a transformer does not fully convince me. The paper claims, “Existing transformer-based approaches for offline MARL either train agents independently, without fully considering them as a multi-agent system, or rely on a centralized transformer model, which suffers from scalability issues.” However, the proposed method also requires the global environment state, and it seems to require the global environment state even during execution (This is strong requirement!)! Then when does your method scale with respect to the number of agents? This needs further clarification.

(2) The paper introduces the setting of a Sequentially Expanded MDP, which implies a sequential structure in the decision-making process. Why limit the proposed algorithm to this setting? This requires justification. Additionally, how do you determine the order of agents? Is it done randomly, since your test cases do not have a predefined order?

(3) Another major concern is the information sharing with limited communication. This assumes that an agent can communicate with the previous agent who just made a decision. This is already a strong form of coordination and should not be assumed to come freely. Could you provide real-world examples where this is applicable? And how the agents could acheieve this?

(4) Is the comparison with other works fair? The proposed algorithm is tested with this information-sharing mechanism and sequential structure, while other algorithms are not. If other algorithms had access to similar forms of communication and coordination, they might also benefit.

### Questions
(1) It is necessary to discuss and compare your approach with CFCQL (see 1’), which is the state-of-the-art CQL-based method designed for offline MARL. It performs very well in SMAC domains, so a comparison would be valuable.

(3) The claim, “However, extending these regularization techniques to multi-agent learning presents significant challenges due to the exponential growth of the joint state-action space as the number of agents increases,” is inaccurate. CFCQL has extended CQL to the multi-agent setting, and the growth is linear with the number of agents, not exponential.

(4) This works states that  "these algorithms do not provide guarantees of global-level regularizations and fail to explicitly or implicitly learn cooperative behavior." What exactly does it mean by "global-level regularizations"? What are the global regularizations in the proposed method?

(5) For the 5m_vs_6m task, why do all algorithms fail to reach the performance level of the offline good dataset?

(6) How are the the results obtained for OMAR on the SMAC task? The official repository only contains the continuous version of OMAR, with no discrete versions available. Did authors implement the descrete action version for OMAR by yourself?

1' Shao, J., Qu, Y., Chen, C., Zhang, H., & Ji, X. (2024). Counterfactual conservative Q learning for offline multi-agent reinforcement learning. Advances in Neural Information Processing Systems, 36.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Multi-Agent Decision S4 (MADS4), an innovative approach to offline multi-agent reinforcement learning (MARL). The authors build on the success of Structured State Space Sequence (S4) models in single-agent tasks and extend them to MARL by leveraging their parameter efficiency, long-context handling capabilities, and faster inference compared to transformers. The paper introduces a Sequentially Expanded Markov Decision Process (SE-MDP) framework that promotes inter-agent cooperation by enabling sequential action-taking with limited communication between agents. The results on benchmark environments (Multi-Robot Warehouse and StarCraft2) demonstrate the superior performance of MADS4 over state-of-the-art baselines in offline MARL settings.

### Strengths
1) The use of S4 models provides clear benefits in terms of efficiency, handling longer temporal contexts, and faster inference times. This is a critical advantage over transformers, especially for offline reinforcement learning tasks that involve long trajectories.
2) The paper provides empirical results showing that MADS4 outperforms state-of-the-art methods on RWARE and SMAC, highlighting its potential for cooperative multi-agent tasks that require coordination among agents.
3) Offline reinforcement learning in MARL is a challenging but important area, especially when online interaction with the environment is costly or risky. The focus on leveraging pre-collected data is a strength of this work, aligning it with real-world applications.

### Weaknesses
1) The choice of environments (RWARE and SMAC) does not sufficiently test the generalizability of MADS4. These benchmarks are widely used but do not fully capture the complexity of real-world multi-agent tasks. Testing in environments with higher-dimensional state spaces or dynamic agent interactions (e.g., more heterogeneous teams or real-time strategy games) would provide stronger evidence of scalability and robustness.
2) The paper mainly compares MADS4 to transformer-based models. However, given the growing body of work in MARL using other architectures like graph neural networks (GNNs) or attention mechanisms that directly model agent interactions, it would be valuable to include comparisons to such baselines.
Insufficient Analysis of Sequential Dependencies: The SE-MDP framework introduces a strong assumption of sequential action-taking, which may not always be practical in environments where agents need to act simultaneously or in parallel. This limitation isn’t fully addressed, and the paper does not provide an alternative for situations where this sequential action may be a bottleneck.
3) The focus on S4 models without considering the possible limitations of these models (such as their effectiveness in high-dimensional continuous action spaces) reduces the generality of the conclusions. Additionally, the paper does not explore whether there are settings where transformers might outperform S4, such as tasks that require more flexible attention mechanisms.

### Questions
1. How does the sequential dependency between agents in SE-MDP affect performance in environments that require real-time parallel actions from all agents? Would MADS4 struggle in such settings, and if so, how could it be adapted?
2. Have you considered testing MADS4 in environments with more dynamic interactions, such as continuous control tasks or real-world applications (e.g., autonomous driving, resource allocation)?
3. How does MADS4 compare to architectures like graph neural networks, which are also designed for multi-agent cooperation? It would be beneficial to see a comparison with GNN-based approaches to understand the specific advantages of S4.
4. Given that the S4 model relies on long-term dependencies, what are the trade-offs in using S4 over transformers in tasks with varying sequence lengths? Would transformers perform better in environments with shorter sequences or fewer agents?
5. Can you provide more intuition or formal analysis regarding the gradient flow between agents in SE-MDP? How does this contribute to stability, and why does it improve learning compared to other methods?

### Soundness
4

### Presentation
3

### Contribution
3
