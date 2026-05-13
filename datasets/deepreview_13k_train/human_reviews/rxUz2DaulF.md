# Q* Agent: Optimizing Language Agents with Q-Guided Exploration

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Language agents have become a promising solution to complex interactive tasks. One of the key ingredients to the success of language agents is the reward model on the trajectory of the agentic workflow, which provides valuable guidance during training or inference. However, due to the lack of annotations of intermediate interactions, most existing works use an outcome reward model to optimize policies across entire trajectories. This may lead to sub-optimal policies and hinder the overall performance. To address this, we propose Q\*Agent, leveraging an estimated Q value to generate intermediate annotations for open language agents. 
By introducing a reasoning tree and performing process reward modeling, Q\*Agent provides effective intermediate guidance for each step. This guidance aims to automatically annotate data in a step-wise manner.
Besides, we propose a Q-guided generation strategy that can significantly boost model performance by providing process guidance during inference.
Notably, even with almost half the annotated data, Q\*Agent retains strong performance, demonstrating its efficiency in handling limited supervision. We also empirically demonstrate that Q\*Agent can lead to more accurate decision making through qualitative analysis.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a method to train a language agent, enabling it to handle complex tasks. To this end, the authors initialize the language agent via performing behavioral cloning on the collection of expert trajectories. Then, the authors utilize the supervised fine-tuned agent to explore the environment and collect trajectories. Using the collected trajectories, QNet is trained via Q-learning. Finally, Q-guided exploration is used to inference, and the Q\*Agent is trained using SFT dataset and Q-guided trajectories. Based on this training steps, Q\*Agent achieves state-of-the-art performance.

### Strengths
The authors propose a method to train a language agent that achieves state-of-the-art performance.

### Weaknesses
I have some questions about this work, which are mentioned in the Questions section below.
1. As mentioned in Section 2.2, Q*Agent appears to be closely related to Q*(Wang et al., 2024a) and the Q-value model enhanced (Zhai et al., 2024). In my understanding, based on your summary, I am uncertain whether adding a behavioral cloning stage is an important contribution. Could you provide a more detailed explanation of your contributions compared to these previous works?
2. During the step 2 in Figure 1, Q*Agent stops exploring a branch’s nodes if the branch yields a zero reward. However, with this strategy, I wonder if Q*Agent disregards partially correct trajectories where only the final parts are incorrect.
3. In Q-guided self-training, why does the Q*Agent algorithm not use the dataset collected during step 2 in Figure 1?
4. In my understanding, the “exploration” steps, steps 2 and 4 in Figure 1, seem to be closer to exploitation rather than exploration. In RL literature, exploration typically aims to gather information about unknown parts of the environment. However, in this paper, both of these “exploration” steps use the best action based on current knowledge (reward of 1 or action with max Q), which generally aligns more closely with exploitation in RL. This terminology may be confusing for researchers who familiar with RL concepts.
5. In the experimental section, there are no results for Q*(Wang et al., 2024a) or the Q-value model enhanced (Zhai et al., 2024). Is there any reason these algorithms were omitted?
6. In the experimental section, performing SFT appears sufficient to achieve satisfactory results. Therefore, I am curious about the performance of Q*Agent when the SFT dataset shows poor performance, in order to observe the impact of RL.
7. I am confused by the definitions of Q*Agent-ST and Q*Agnet-I. As I understand it, during step 4 in Figure 1, Q*Agent-ST involves using QNet to compute Q-values for m actions and selecting the best action, while Q*Agent-I refers to using action sampled from the agent without using QNet. If this is correct, then what is the purpose of QNet?

Minor comment:
The notations in Appendix A.3 are somewhat confusing. The notations $\mathcal{A}$, $\mathcal{Q}$, and $q_m$ should be defined formally. Additionally, in line 7, $\arg\max$ is not used properly according to its definition.

### Questions
I am unsure whether I have fully understood this paper, so please let me know if I have any misunderstandings. I would be very happy to gain a complete understanding of your work.
1. As mentioned in Section 2.2, Q\*Agent appears to be closely related to Q\*(Wang et al., 2024a) and the Q-value model enhanced (Zhai et al., 2024). In my understanding, based on your summary, I am uncertain whether adding a behavioral cloning stage is an important contribution. Could you provide a more detailed explanation of your contributions compared to these previous works?
2. During the step 2 in Figure 1, Q\*Agent stops exploring a branch’s nodes if the branch yields a zero reward. However, with this strategy, I wonder if Q\*Agent disregards partially correct trajectories where only the final parts are incorrect.
3. In Q-guided self-training, why does the Q\*Agent algorithm not use the dataset collected during step 2 in Figure 1?
4. In my understanding, the “exploration” steps, steps 2 and 4 in Figure 1, seem to be closer to exploitation rather than exploration. In RL literature, exploration typically aims to gather information about unknown parts of the environment. However, in this paper, both of these “exploration” steps use the best action based on current knowledge (reward of 1 or action with max Q), which generally aligns more closely with exploitation in RL. This terminology may be confusing for researchers who familiar with RL concepts.
5. In the experimental section, there are no results for Q\*(Wang et al., 2024a) or the Q-value model enhanced (Zhai et al., 2024). Is there any reason these algorithms were omitted?
6. In the experimental section, performing SFT appears sufficient to achieve satisfactory results. Therefore, I am curious about the performance of Q\*Agent when the SFT dataset shows poor performance, in order to observe the impact of RL.
7. I am confused by the definitions of Q\*Agent-ST and Q\*Agnet-I. As I understand it, during step 4 in Figure 1, Q\*Agent-ST involves using QNet to compute Q-values for m actions and selecting the best action, while Q\*Agent-I refers to using action sampled from the agent without using QNet. If this is correct, then what is the purpose of QNet?

Minor comment:
The notations in Appendix A.3 are somewhat confusing. The notations $\mathcal{A}$, $\mathcal{Q}$, and $q_m$ should be defined formally. Additionally, in line 7, $\arg\max$ is not used properly according to its definition.

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
4

### Summary
The paper introduces Q*Agent, a novel approach of building language agents through learning a Q function and use it to select action. Experimental results on the WebShop benchmark show that QAgent achieves strong performance and efficiency gains compared to baseline methods.

### Strengths
1. This paper introduced learning a Q function, which provides step-wise feedback instead of outcome-based rewards for the language agents. 
2. It proposed two ways of leveraging Q functions, one for selecting actions in inference and one for filtering data in training/finetuning.

### Weaknesses
1. The experimental study is limited on one domain. It is unclear how effective the proposed method on other types of agent task, or even on other types of websites.

2. The experimental study lacks discussion about related work. For inference-time self-improvement, the experiment only compared the proposed method with best-of-N and ignores a large body of related work on language agent. I think the following work need to be discussed and compared with the proposed method.
 - Some fundamental work on self-improvement on language agent, for example the Reflexion and LATS methods.
 - Some work use a trained model (not per-step) to provide feedback for self-improvement at the inference time. E.g. "Autonomous Evaluation and Refinement of Digital Agents Jiayi Pan, Yichi Zhang, Nicholas Tomlin, Yifei Zhou, Sergey Levine, Alane Suhr"
 - Some work use per-step feedback in self-improvement, without finetuning a separate Q functions, in language agent tasks. E.g. "Tree Search for Language Model Agents Jing Yu Koh, Stephen McAleer, Daniel Fried, Ruslan Salakhutdinov"

When compare with methods without finetuning a new model, the paper also needs to justify the cost of finetuning additional model.

3. It seems the base approach in the experimental study include common prompting methods such as CoT, few-shot, ReAct etc. It is unclear if the benefit of the proposed method is orthogonal, or covered by these basic prompting approaches for language agent.

### Questions
1. Can you replace the illustrative example in Figure 2 with an example from (or more close to) the experimental study in this paper. This prevent it from over-claiming or misleading the applicability of the proposed method.
2. Please use $Q^\star$ instead of $Q^*$ to denote the optimal state-action value function.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper study a critical problem in agent scenarios: the absence of process rewards for each intermediate step. The authors propose an approach that involves three main steps: 1. collecting a large number of interaction trajectories by constructing a reasoning tree; 2. using Bellman's equation to estimate the expected Q of each step; and 3. training a QNet to estimate the process reward Q values for states and actions. The experiments validate the effectiveness of QNet in providing intermediate step rewards during both training and reasoning, demonstrating its ability to offer process-based guidance and improve agent performance compared to trajectory-based rewards.

### Strengths
This paper is well-motivated. The lack of process rewards is a significant challenge in agent tasks. The proposed method reduces the costs associated with obtaining high-quality data annotations.

Considering training step-level verifiers is demonstrated to be effective in LLM reasoning tasks, applying the approach to agent tasks is of great significance.

### Weaknesses
The paper is poorly written, lacking many essential explanations and details. For example, in Section 4.4, the authors state, "we also introduce augmenting action diversity with perturbation during this stage, which is realized by prompting LLM to paraphrase the task description," yet they do not provide any discussion on prompt implementation or examples of action diversity. The termination condition for the tree construction process is not clarified, and several definitions, such as $C_t$ in Equation (4), are missing.
The experimental setup also deeds further clarification. Some critical hyper-parameters, such as the discount factor $\gamma$ for extracting Q-values is not listed. The metrics for performance in Table 1 are not explained. The sampling number per step of Q* Agent-I is not provided.
For visualization, the horizontal axis in Fig. 3(a) should indicate the number of sampled actions. Additionally, Fig. 3(b) lacks a label for the ordinate. 
Overall, there are too many issues with the paper to list them all here.

The versatility of the method needs to be verified in more agent tasks.

Equation (3) is not the cross-entropy loss.

Line 415: Table 2 is not organized into three sections.

### Questions
In Section 5.5, how were the "Averaged reward" and "Reward" obtained during inference? I believe the average step-level reward is unavailable during inference.

What the advantage of utilizing bellman equation to estimate Q-values compared to widely-used MCTS.

The authors state that the average depths of tree searching for agent tasks are large. Any specific statistics? The authors in [1] state that the average number of steps for Webshop is 6.8.

Reference:
[1] Putta P, Mills E, Garg N, et al. Agent q: Advanced reasoning and learning for autonomous ai agents[J]. arXiv preprint arXiv:2408.07199, 2024.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an LLM agent algorithm based on Q-value-guided training and inference-time decision-making to tackle complex interactive (decision-making) tasks. The primary motivation is to provide more efficient feedback to the agent through step-wise rewards. By integrating the LLM agent within an MCTS-like framework, the approach optimizes the LLM agent, addressing the issue of sparse rewards that arise from solely using trajectory rewards in existing algorithms.

### Strengths
The main contribution of this paper lies in its ability to construct step-wise rewards for each step using an MCTS-like approach, based solely on the final reward. These rewards are then used to train a Q-value network to support decision-making at inference time.
In the overall algorithm design, after conducting SFT, the authors make a few adjustments to the MCTS. They utilize a “tree pruning” approach to reduce the search space and train a Q-value network based on calculated Q-values. This allows the Q-value network to guide the agent's decision-making at inference time by selecting actions that maximize the Q-value.

### Weaknesses
 + **Algorithm Framework**: The core framework of this paper is derived from the MCTS, yet the authors did not evaluate or compare its relationship to MCTS. Specifically, the paper lacks a clear explanation of how the proposed method's exploration and exploitation strategies differ from those in MCTS, and how these differences impact performance. A direct comparison, even on a simplified version of the task, would be beneficial to understand the advantages and disadvantages of the proposed approach relative to MCTS.
  + **Known Environment Assumption**: Unlike tasks such as mathematical reasoning, the interactive tasks in this paper require constructing a reasoning tree using the environment to achieve state transitions (i.e., generating the next state based on the current state and action). However, the authors did not discuss this assumption, particularly how the environment's response is deterministic or stochastic, and how this affects the tree search. The paper should clarify whether the environment is assumed to be a black box or if some knowledge of its dynamics is required.
  + **Tree Pruning**: The main improvement of this work over MCTS lies in tree pruning, considering the vast action space for LLM as a generative model. If a simulation fails to get a positive reward, Q* Agent discards the node that attempted to expand. This approach essentially explores a few trajectories that can reach the final goal within an enormous decision space and then performs Q-value extraction. However, for complex tasks that may require dozens of steps to reach the final goal (getting a positive final reward), the probability of finding a successful trajectory is exceedingly low, severely limiting the algorithm's applicability. The authors even restrict expansion to only the first three to five steps, making the algorithm suitable only for tasks requiring exploration at the very beginning of each episode. The paper should address how the algorithm would perform on tasks requiring more extensive exploration and how the pruning strategy affects the overall search.
  + **Task-specific Q-value Network**: This method requires training a task-specific Q-value network for each task and using the corresponding network during decision-making, limiting the algorithm's generalization capability, which is a core advantage of LLMs (otherwise, a task-specific agent could be directly trained with RL). Using RL to train the LLM with this Q-function could mitigate this issue. The authors should discuss the trade-offs between training a task-specific Q-network and using a more generalizable approach, and how this impacts the overall applicability of the method.
  + **MDP Design**: The state definition includes the entire interaction history. When the interaction sequence becomes lengthy, this introduces a large number of tokens, further constraining the algorithm's performance on complex tasks. The authors should explore alternative state representations that can reduce the token length while preserving the necessary information for decision-making, such as using a summary of the interaction history.
+ **Experimental Results**: Experimentally, the authors only compares the proposed method with some simple baselines on the WebShop benchmark. While it achieves some performance improvement, the improvement is relatively small. Other experimental results do support the effectiveness of the proposed Q-guided decision-making. However, no ablation studies were conducted on techniques like tree pruning, making the experiments insufficiently comprehensive. The paper should include ablation studies to demonstrate the impact of each component of the proposed method, such as the tree pruning strategy and the depth of exploration.
  + **Experimental Setup**: Only WebShop is selected as the experimental platform, limiting the results' credibility. The authors also do not show variance or the number of test episodes, making it difficult to assess the impact of randomness on the results, especially given the small performance improvement. The paper should include the variance and the number of test episodes to provide a more robust evaluation of the method.
  + **Limited Experimental Content**: It is recommended that the authors conduct ablation studies on techniques in the tree construction phase, particularly on stop expansion and the "early stage" length in tree pruning.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
