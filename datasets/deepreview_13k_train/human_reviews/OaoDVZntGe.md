# Inverse Attention Agent in Multi-Agent System

- Decision: Accept
- Scores: 5, 5, 3, 6

## Abstract
A major challenge for Multi-Agent Systems is enabling agents to adapt dynamically to diverse environments in which opponents and teammates may continually change. Agents trained using conventional methods tend to excel only within the confines of their training cohorts; their performance drops significantly when confronting unfamiliar agents. To address this shortcoming, we introduce Inverse Attention Agents that adopt concepts from the Theory of Mind, implemented algorithmically using an attention mechanism and trained in an end-to-end manner. Crucial to determining the final actions of these agents, the weights in their attention model explicitly represent attention to different goals. We furthermore propose an inverse attention network that deduces the ToM of agents based on observations and prior actions. The network infers the attentional states of other agents, thereby refining the attention weights to adjust the agent's final action. We conduct experiments in a continuous environment, tackling demanding tasks encompassing cooperation, competition, and a blend of both. They demonstrate that the inverse attention network successfully infers the attention of other agents, and that this information improves agent performance. Additional human experiments show that, compared to baseline agent models, our inverse attention agents exhibit superior cooperation with humans and better emulate human behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents an end-to-end method based on the attention mechanism to enable the easy adaptation of trained agents to different environments. The authors provided evaluations of model interactions with artificial and human agents.

### Strengths
- The paper proposes a novel approach to attention mechanism in the multi-agent system setting.
- The results are tested both with unseen artificial agents and with human agents' interaction with the proposed agent.

### Weaknesses
 - it is not clear to me and was not discussed in the text how the agent observation can be decomposed into a combination of goals.
- The authors collect the attention inference dataset but do not provide an analysis of how different realizations of such attention weights collections may influence the resulting inverse-attention agent performance (e.g. dataset collected with models with different training hyperparameters, random seeds, attention sizes).
- The authors provide no ablation study.

### Questions
- The reference of the "Attention is all you need" paper has an incorrect year of publication.
- The font sizes on figures 2 and 3 should be increased to improve readability.

### Soundness
2

### Presentation
3

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
This paper proposes a method for developing training a parameterized function to predict the agents attention weights in a goal oriented task proposed in Long et al 2020. The paper proposes to do that using an inverse attention network. A dataset is created from the most recently accumulated attention weights with respect to their local observations, and this is then used to train the inverse attention network to predict agent attention weights during inference. Additionally, the authors show that the inverse attention network, due to its simplicity, has a high prediction accuracy after convergence.

The agents have access to the local observation of each of the other agents, which it uses to predict the intentions of other agents, and alter its own actions accordingly. Experimental results show the efficacy of the inverse attention mechanism when compared to standard non communication based algorithms.

### Strengths
The proposed method approaches the problem of inferring intentions of agents by allowing each agent to access the observation of other agents and reason about what their intentions are. The approach offers a simple yet effective tool for multi-agent systems especially for heavily correlated environments, for example in dense environments. Altering agent behavior through explicit reasoning over other agents intentions is of great interest to the multi-agent community.

### Weaknesses
As part of the scalability analysis, a maximum number of 8 agents have been tested. Due to the concatenation of each agents attention weight, I would like an analysis on the limitations of the scalability, particularly for the accuracy of IW predictions and the complexity of processing each pairwise agent inference separately as number of agents grow to 20~50 agents.

The paper claims that agents generally perform poorly when unseen states are communicated by agents (heterogeneous or otherwise). The paper focuses on predicting just the attention weights instead of the actual hidden states to mitigate the above issue. Am I correct in assuming that as part of the IW networks training, each independent agent should have had encountered those states for it to make an accurate prediction of the other agents attention weights.

### Questions
The paper claims that agents generally perform poorly when unseen states are communicated by agents (heterogeneous or otherwise). The paper focuses on predicting just the attention weights instead of the actual hidden states to mitigate the above issue. Am I correct in assuming that as part of the IW networks training, each independent agent should have had encountered those states for it to make an accurate prediction of the other agents attention weights.

### Soundness
3

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
4

### Summary
This paper studies the setting similar to ad hoc teamwork, i.e., the trained agents encounter unfamiliar agents when performing tasks. It proposes an inverse attention network that infers the attention of other agents on each goal based on their observations and prior actions. Doing so helps maintain consistency in decision-making across different scenarios and the agent can adjust its final action by refining the attention weights given the outputs of the inverse attention network.

### Strengths
1. This work uses the gradient field (GF) representations to represent the goals of the agent within specific environments, which is an interesting idea.

2. This work conducts a human study to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The proposed inverse attention network requires the observation of agent $j$ when inferring the attention weights of agent $j$. Therefore, the proposed method only works in fully observable environments and will face problems in partially observable environments if the observations of other agents are unavailable. This is a significant limitation as many real-world scenarios involve partial observability, where an agent's view of the environment and other agents is limited. The method's reliance on complete observation of other agents restricts its applicability in more complex and realistic settings.

2. The proposed method assumes the observations of an agent can be decomposed into a combination of $N$ goals within the environment. This assumption holds for the tested environments in MPE. However, in many environments, there are no explicit multiple goals, and how to decompose an observation into $N$ goals is unclear. The paper does not provide a clear methodology for determining these goals or how to handle environments where such a decomposition is not straightforward. This lack of generality limits the method's applicability to a narrow range of environments where goals are easily identifiable and decomposable.

3. When training the inverse attention network, this work only uses the agent $i$’s own data. This will introduce bias when the agent $i$'s experience cannot cover the trajectories of other agents. This approach may lead to an incomplete or skewed understanding of other agents' behaviors, as the training data does not reflect the full range of possible actions and strategies of other agents. The resulting model may not generalize well to situations where other agents behave differently from what agent $i$ has experienced.

4. The MPE environments are very simple and similar to each other. The scalability test only tries at most 4 agents which is small. The experiments do not adequately demonstrate the method's performance in more complex environments with a larger number of agents. The lack of scalability testing raises concerns about the method's practical applicability in real-world scenarios that often involve a large number of interacting agents.

5. This work does not compare with the existing works form the ad hoc teamwork domain.

### Questions
Please refer to the above weakness section.

### Soundness
3

### Presentation
3

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
This paper introduces Inverse Attention Agents for multi-agent systems (MAS), addressing the challenge of dynamically adapting to diverse environments with unfamiliar teammates and opponents. Traditional agents struggle to perform well outside of their training environments, while this method leverages Theory of Mind (ToM) combined with attention mechanisms to enhance agent interactions. The core contribution is the development of an Inverse Attention Network, which allows agents to infer the attention weights and intentions of others, enabling more flexible cooperation and competition. The method is validated through extensive experiments in cooperative and competitive tasks using the Multi-agent Particle Environment (MPE), where the proposed agents demonstrate superior performance, particularly in ad-hoc teaming and human-agent cooperation scenarios.

### Strengths
1) The integration of Theory of Mind with attention mechanisms in MAS is novel, offering a new method for enhancing agent adaptability to unfamiliar teammates and opponents.
2) The method is well-justified theoretically, and the experimental setup is thorough, covering a range of environments and both competitive and cooperative tasks.
3) The paper is clearly written, and the presentation of the methodology, particularly the detailed description of the inverse attention network, is well-done.
4) The ability to improve agent cooperation in ad-hoc settings is an important problem in MAS, and this work provides a promising solution. The method also shows potential for applications beyond the tested environments, such as human-agent interaction in robotics.

### Weaknesses
1. The method is currently only tested in relatively simple MPE environments. While the results are promising, the approach’s applicability to more complex real-world scenarios (e.g., autonomous driving, large-scale multi-agent simulations) is not well explored. The MPE environments, while useful for initial testing, lack the high-dimensional state spaces, complex dynamics, and partial observability that are characteristic of many real-world MAS problems. This raises concerns about the generalizability of the findings.

2. As the number of agents increases, the computational complexity of inferring attention weights for multiple agents may become a bottleneck. The paper does not fully address how the method scales with a larger number of agents or more diverse agent types. Specifically, the computational cost of the inverse attention mechanism, which involves calculating attention weights for each agent with respect to all other agents, could become prohibitive in large-scale systems. The paper needs to provide a more detailed analysis of the computational scaling of the proposed method.

3. The method assumes that agents are of the same type, which limits its generalization. In many real-world applications, interactions between heterogeneous agents (with different abilities or goals) are common, but the paper does not address this scenario. The current approach does not account for agents with different action spaces, observation spaces, or reward functions, which is a significant limitation for real-world applicability. The assumption of homogeneous agents restricts the scope of the method.

4. The inverse attention mechanism is trained in an offline manner, which may limit its adaptability in rapidly changing environments where real-time adjustments are necessary. The offline training of the inverse attention network may not capture the nuances of dynamic environments where agent behaviors and goals can shift rapidly. The paper needs to explore the potential for online adaptation of the inverse attention mechanism.

### Questions
1. Does the performance of inverse attention agents degrade as the number of agents increases, particularly in larger environments like the 4-4 Grassland game?

2. Why does the cooperative gain between multiple inverse attention agents not increase linearly, and is this due to cognitive loops or mutual inference inaccuracies?

3. Why do inverse attention agents perform inconsistently when cooperating with humans in some roles (e.g., sheep in Adversary), and how can this cooperation be made more robust?

4. How is the accuracy of the inverse attention network related to task success, and why doesn't high inference accuracy always correlate with better performance in tasks like Adversary?

5. What are the main factors behind the performance differences between inverse attention agents and baseline algorithms, and how can these differences be better explained?

6. Does the inverse attention mechanism perform better in competitive tasks than in cooperative ones, and how can its adaptability in complex cooperation tasks be improved?

### Soundness
3

### Presentation
3

### Contribution
3
