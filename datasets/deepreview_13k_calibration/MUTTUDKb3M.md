# DRIMA: Differential Reward Interaction for Cooperative Multi-Agent Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Multi-agent reinforcement learning (MARL) owning to its potent capabilities in complex systems has gained remarkable research attention nowadays, in which collaborative decision-making and control for multi-agent systems is one of the key research focuses.
The prevalent learning framework is centralized training with decentralized execution (CTDE), in which the decentralized execution realizes strategy flexibility, and the use of centralized training ensures stationarity and goal consistency while becoming incapable when facing scalability and complexity situations.
To address this issue, we follow the concept of distributed training with decentralized execution (DTDE).
Decentralization is naturally accompanied by the game during the learning process, which has not been entirely studied in related work, resulting in the constrained strategy combination of MARL.
In this paper, we devise a novel approach of differential reward interaction (DRI) with conflict-triggered for the distributed evaluation that enables overall goal consistency through highly efficient local information exchange.
With this collaborative learning method, the DRI-based MARL can eliminate the notorious issue of converging to saddle equilibriums of stochastic games.
Meanwhile, it possesses provable convergence and is well compatible for general value-based and policy-based algorithms.
Experiments in several benchmark scenarios demonstrate that DRIMA realizes collaborative strategy learning with enhanced global goal-achieving.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
An important issue in DETD is the interactions among agents, which manifest in simultaneous decision-making and reward conflicts. To address these challenges, this paper introduces DRIMA, a differential reward interaction-based MARL method. Specifically, the authors model the information interactions among agents as an undirected graph network, where each node represents an agent and each edge represents the connections between them. Based on this, they propose an exchange reward rule based on the overall performance of the policy. They evaluate the quality of the team policy based on the differential reward of the current agent's action. The authors conduct a theoretical analysis of their method from the perspectives of two-player matrix games and multi-player Markov games. Their experiments focus on general-sum games, specifically validating the method's effectiveness in matrix games, MPE, and SMAC.

### Strengths
1.	The authors conducted a theoretical analysis of the convergence of their method.
2.	The authors used "Two-player matrix game" and "Multi-Player Markov Game" to analyze the effectiveness of their method.

### Weaknesses
1.	The interaction rule in line 164 lacks a formal definition, and $r^i-\bar{\mu}^{N^i}$  and $\bar{r}^{N^i}-\bar{\mu}^{N^i}$ lack more direct definitions, making it difficult to understand. Specifically, the paper introduces a differential reward interaction but does not clearly define how this interaction is calculated or how it influences the agents' learning process. The terms $r^i$ and $\bar{r}^{N^i}$ are not explicitly defined in the context of the interaction, leaving ambiguity about whether they represent instantaneous rewards, expected rewards, or some other form of value. The lack of clarity makes it difficult to assess the soundness of the proposed interaction mechanism.
2.	The paper does not provide sufficient experiments in SMAC to demonstrate its effectiveness. While the authors claim to validate the method in SMAC, the limited number of scenarios and the lack of diversity in the experimental setups raise concerns about the generalizability of the results. The experiments do not cover a wide range of SMAC maps or agent configurations, which are crucial for demonstrating the robustness of the proposed method. The absence of comparisons against strong baselines in SMAC further weakens the experimental validation.

### Questions
1.	What’s the formal definition of “reward interaction”?
2.	In line 193, what do $r^i_t-\bar{\mu}_t^{N^i}$ and $\bar{r}_t^{N^{-i}} - \bar{\mu}_t^{N^i}$ represent? And how does the opposite sign between them “indicates the conflict contribution of action decision relating to the individual and other neighbors’to the current neighbor-joint policy”? As a key contribution of the paper, the authors need to carefully explain the meaning of each part in this section to help readers understand their ideas.

3.	In the authors' paper, each agent in the MAS is modeled with an individual reward. However, in the SMAC environment, each agent shares the same reward. How does the method in the paper address this situation?

4.	Based on Question 3, in many cooperative multi-agent systems, each agent shares a team reward, meaning that $r^i$ in Formula 2 is the same and equal to $\bar{r}^{N^i}$. Does the conflict-triggered differential reward interaction still apply in this case?

5.	In the MPE experiments, the method was not compared with QMIX. Please explain the choice of baselines.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Although the Centralized training with decentralized execution (CTDE) framework is currently popular, it faces challenges in terms of scalability and handling complex tasks. This paper introduces a new approach called differential reward interaction (DRI) with conflict-triggered, which enables agents to achieve a unified overall goal by exchanging local information with each other. This method also overcomes the issue of saddle equilibrium in policy combination, a common challenge in game theory and optimization. The effectiveness and superiority of the proposed method, DRIMA, are demonstrated through its application in matrix games, Multi-Agent Particle Environment (MPE) scenarios, and Star-CraftⅡ.

### Strengths
1.	The overall structure of the paper is complete, the content is sufficient, and the experimental evidence is persuasive.
2.	The paper proposes that if personal rewards conflict with neighbor rewards, personal rewards should be reshaped as the neighbor-averaged reward to maintain the group consistency. This idea is similar to Reward Centering or Advantage Functions.

### Weaknesses
1.	The paper does not clearly define "differential rewards" or "conflicts". Specifically, while the paper mentions $r^i - \mu^i$ as a differential reward, it doesn't explicitly state what \mu^i represents in the context of multi-agent learning, nor does it clarify how this relates to the concept of a differential reward in single-agent RL. The definition of "conflict" is also vague. It is mentioned that conflict occurs when there is an opposite sign between $r^i - \bar{\mu}^{N^i}$ and $\bar{r}^{N^{-i}} - \bar{\mu}^{N^i}$, but the meaning of these terms and why this constitutes a conflict is not sufficiently explained. 
2.	The purpose of Equation 2 is not intuitively explained. The paper states that it is related to the "differential reward" concept, but the connection is not clear. A straightforward example illustrating how Equation 2 reshapes the reward and why this is beneficial for multi-agent learning would be very helpful. The lack of a clear explanation makes it difficult to understand the motivation behind this equation.
3.	The relationship between Equation 2 and the differential action-value function is not explained. While the paper defines a differential action-value function, it does not show how the reshaped reward from Equation 2 affects this function. It is unclear how the reshaped reward is incorporated into the learning process and how it impacts the policy update.
4.	In Section 2.2, $\mu_\pi^i$ in the differential action-value function represents the average reward per step for agent i. However, in Section 3.2, $\bar\mu_\pi$ represents the average of the average rewards per step for the agent itself. It is unclear why the notation changes and whether there is a contradiction between the two. The paper needs to clarify the difference between these two terms and ensure consistency in notation.
5.	Around lines 244-247, it is stated that $\beta_t$ in Equation 4 is the step size, but it is not explicitly stated whether this is the step size for the Actor or the Critic. Given the context of policy updates, it is more likely to be the step size of the Actor, but this needs to be explicitly stated to avoid ambiguity.
6.	The example in Figure 2 is somewhat abstract. The paper mentions the issue of gradient directions under different views, but it does not provide a detailed explanation of how these different views arise and how they lead to conflicting gradient directions. A more concrete example with specific scenarios would help in understanding this issue.

### Questions
1.	Did you draw on the idea of the advantage function? If so, where does the specificity of your method lie? What are the advantages compared to methods using the advantage function?
2.	Did you draw on the concept of Reward Centering? If so, what is the specificity of your method?
3.	Some questions about the Weakness section.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a conflict-triggered differential reward interaction (DRI) method to identify and reshape conflicting payoffs between agents. The experiments conducted on matrix games and continuous space tasks MPE demonstrate the effectiveness of the algorithm.

### Strengths
1. The paper is well-motivated overall.
2. The paper proposes deals with saddle equilibriums based on conflict-triggered differential rewards.

### Weaknesses
1. The proposed algorithm lacks experimental comparisons with recent works on MARL cooperation. Specifically, the paper does not benchmark against state-of-the-art methods designed for cooperative multi-agent settings, making it difficult to assess the relative performance gains of the proposed conflict-triggered differential reward interaction (DRI) method. The absence of such comparisons limits the ability to understand whether the method offers a significant improvement over existing techniques or if it merely replicates known results with a different approach.
2. The current Figure 2 is not very comprehensible for understanding the conflict-triggered mechanism of DRI. The boundaries between the various colored surfaces are not easily distinguishable, making it hard to visualize how the differential rewards are triggered and how they reshape the payoff landscape. This lack of clarity hinders the understanding of the core mechanism of the proposed algorithm.
3. Including experimental results from more complex SMAC scenarios in the main paper would better demonstrate the applicability of the proposed method. The current experiments, while demonstrating the method's effectiveness in matrix games and continuous space tasks, do not fully capture the complexity of real-world multi-agent scenarios. The inclusion of SMAC results would provide a more robust evaluation of the method's performance in more challenging environments.

### Questions
1. As the method exploit the MFT concept, could it be applied to large-scale multi-agent environments?
2. I am wondering whether conflict-triggered differential rewards might hinder early exploration.

### Soundness
2

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
4

### Summary
This paper follows the distributed training with decentralized execution (DTDE) training paradigm and focuses on the cooperation between multiple distributed agents. The authors argue that the conflicting payoffs of different agents would emphasize the game between agents and hinder cooperative behaviors. To mitigate this, they proposed a conflict-triggered differential reward interaction (DRI) method to reconstruct the individual rewards. The proposed method, DRIMA, is tested on matrix games, MPE, and SMAC to verify its effect.

### Strengths
1. This article provides a detailed description of the use of DRIMA in the context of specific tasks from easy (Prisoner's dilemma) to hard (general Markov games). The pseudo-code in the appendix also makes the proposed method easier to follow.
2. The authors have proved the convergence of learning with the differential reward, which makes DRIMA technically solid.
3. Experiment and theory corroborate each other very well in DRIMA. The use of DRIMA effectively helps the raw algorithms jump out NE and reach the global optimum in matrix games.

### Weaknesses
1. The performance of DRIMA in SMAC is not significant. Even with the inclusion of communication between agents, DRIMA is still inferior to CTDE in some scenarios. Specifically, while the authors demonstrate DRIMA's ability to achieve comparable convergence in some SMAC tasks, the fact that it does not consistently outperform CTDE, even with communication, raises concerns about its practical value in complex, real-world scenarios. The lack of a clear advantage in these more challenging environments suggests that the proposed method may not be robust enough for general application.
2. It seems DRIMA often exhibits a slower start in experiments. This is detrimental to sample efficiency, and I suggest the authors give further explanation or improvements. The slower initial learning phase could be a significant drawback in scenarios where rapid adaptation is crucial. The authors should investigate the underlying causes of this slow start, such as the exploration-exploitation balance in the early stages of training, and consider strategies to mitigate it, such as modified exploration policies or curriculum learning.

### Questions
1. When tested on SMAC, how do the authors define the individual rewards of the agents?
2. See Weaknesses 2.

### Soundness
3

### Presentation
3

### Contribution
3
