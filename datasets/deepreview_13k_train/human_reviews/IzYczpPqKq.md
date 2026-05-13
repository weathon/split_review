# Learning to Steer Markovian Agents under Model Uncertainty

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
Designing incentives for an adapting population is a ubiquitous problem in a wide array of economic applications and beyond. In this work, we study how to design additional rewards to steer multi-agent systems towards desired policies \emph{without} prior knowledge of the agents' underlying learning dynamics. Motivated by the limitation of existing works, we consider a new and general category of learning dynamics called \emph{Markovian agents}. We introduce a model-based non-episodic Reinforcement Learning (RL) formulation for our steering problem. Importantly, we focus on learning a \emph{history-dependent} steering strategy to handle the inherent model uncertainty about the agents' learning dynamics. We introduce a novel objective function to encode the desiderata of achieving a good steering outcome with reasonable cost. Theoretically, we identify conditions for the existence of steering strategies to guide agents to the desired policies. Complementing our theoretical contributions, we provide empirical algorithms to approximately solve our objective, which effectively tackles the challenge in learning history-dependent strategies.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework for steering the behaviors of agents towards desired outcomes within a reinforcement learning setting, where the exact learning dynamics of the agents are not known. Specifically, this work introduces the concept of Markovian agents, whose decisions are based only on their current states and immediate rewards, and explores the challenges posed by model uncertainty in practical applications. To address these challenges, the study develops a non-episodic RL approach and proposes the First-Explore-Then-Exploit (FETE) framework. This strategy involves initially exploring to identify the most accurate model from a predefined class and then exploiting this model to effectively steer agent behaviors. The theoretical contribution of the paper establishes that if the model class of learning dynamics is identifiable within finite steps, then a steering strategy with an ε-steering gap can exist. The empirical results in the paper demonstrate that their algorithm can operate under the assumption that each player has only two actions.

### Strengths
- The method introduced in the paper is commended for its intuitive and logical approach. By assuming that the learning dynamics of the agents are Markovian and can be learned in finite steps, the paper effectively simplifies the complex problem of steering under uncertainty.

- The paper provides transparency regarding the experimental assumptions detailed in the appendices. Moreover, the experimental setup involves a wide range of learning rate combinations, specifically up to 3^10.

- The paper is well-written and very easy to follow, with justification and explanation whenever needed in most places.

### Weaknesses
While I appreciate the application of reinforcement learning (RL) to address the steering problem, balancing exploration and exploitation amidst the uncertainty of agents' learning dynamics, but there are some concerns regarding the paper:

- A primary challenge highlighted is the agents' reluctance to disclose their learning dynamics, creating fundamental model uncertainty. The theoretical discussion posits that if the model class $F$ of the agents is identifiable, then an epsilon-steering strategy is viable. It would enhance the paper if the theoretical sections could more explicitly address how understanding the model class $F$ effectively reduces this uncertainty, thus better connecting the theoretical insights with the algorithmic implementations. Specifically, the paper does not clearly articulate how the choice of model class impacts the identifiability condition, nor does it provide guidance on selecting an appropriate model class in practice. For instance, if $F$ is too small, the true agent dynamics might not be representable, leading to poor steering performance. Conversely, if $F$ is too large, the identifiability condition might be difficult to satisfy, requiring excessive exploration. The paper should provide more rigorous analysis on the trade-offs involved in choosing the model class $F$.

- The algorithm proposed in the paper relies heavily on accurately specifying agents' learning dynamics, which presents a significant challenge when considering real-world complexities where agents' behaviors are influenced by others, such as herd behavior or nonconformity. These dynamic inter-agent interactions introduce variability that the algorithm may not capture effectively, given its current design focused on binary or categorical decision-making scenarios. This specificity restricts its utility, particularly in more complex decision environments where outcomes are not merely binary and agent behaviors are interdependent and continuously evolving. Consequently, while the algorithm provides a structured approach to steering agent decisions within a controlled setting, its application to broader, more realistic scenarios involving complex agent dynamics and multiple decision variables may require significant adaptations to accommodate these behavioral complexity.


### Questions
- While this paper usefully demonstrates the benefit of steering, it does not sufficiently address whether the proposed steering methods are adequately effective when compared to other potential steering strategies. For example, expanding the comparative analysis to include non-Markovian agent models could help justify the emphasis on Markovian agents in the introduction. Non-Markovian models, which account for past states and decisions in their decision-making processes, often represent more realistic and complex environments. Including such models in the analysis would provide a more comprehensive assessment of the proposed strategies.

- Considering exploration is crucial for addressing the uncertainty in agents' learning dynamics, it would be valuable to investigate how an exploration-focused approach like Random Network Distillation (RND) could impact the results (more than random exploration FETE-RE in Section 6.2). This could provide practical insights into managing uncertainty more effectively in complex multi-agent environments.

### Soundness
3

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
3

### Summary
This paper proposed an RL framework that helps multi-agent systems towards specific behaviors or policies using additional incentives or rewards, even without prior knowledge of agent learning models.

### Strengths
Strengths:

1. The authors introduce a new objective function that balances the goal of steering agents toward a target policy while minimizing the overall steering cost.
2. The paper provides sufficient conditions under which the proposed steering strategies are effective, ensuring a low gap between target and actual agent behavior and achieving Pareto optimality.
3. The paper includes experimental results in different environments, demonstrating the algorithms' performance under varying model uncertainty conditions.

### Weaknesses
Weakness:

1. Poor writing: The writing in this paper needs significant improvement; it appears to have been put together in a hurry, making it very difficult to read. As a new research problem, the steering problem has not been well-motivated or clearly formulated, leaving key concepts ambiguous. For example, the definitions of "desired policies" and "desired behaviors" are unclear, and it’s difficult to understand their precise meaning in this context. If we already know the desired policies, why any learning is necessary？ Furthermore, the concept of the "mediator" is not introduced or explained and suddenly appears in the paper. Similarly, the notation f∗ is introduced abruptly at line 210 without any prior explanation, creating confusion. The new learning objective presented in line 220 is also hard to understand and lacks sufficient clarification regarding its purpose and relevance.
2. The transitions between paragraphs are also weak, resulting in a lack of cohesion throughout the text. Starting from the problem formulation section, the paper becomes increasingly difficult to follow, with unclear structure and insufficient explanations, making it hard for readers to grasp the main ideas and contributions.

### Questions
1. The paper mentions comparison experiments with control methods. In which scenarios does the proposed method outperform control methods, and in which scenarios does it show similar or inferior performance?
2. Could you provide a more precise definition of "desired policies" and "desired behaviors”? What exactly does "desired policy" mean in this paper? Is "desired behavior" different from it?
3. If we already know the desired policy, why is there still a need for learning? Are there certain situations in the steering problem where learning is still required, even if the desired policy is known?
4. Why steering is necessary in multi-agent systems? Can existing algorithms find the equilibrium or approximated equilibrium for MAS?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the challenge of steering multi-agent systems towards desired policies without having prior knowledge of the agents' learning dynamics. The focus is on a new class of learning dynamics called Markovian agents. The authors propose a model-based non-episodic reinforcement learning (RL) framework and formulate an optimization objective incorporating history-dependent steering strategies to handle model uncertainty. The paper presents theoretical results and practical algorithms to achieve this steering, validated with empirical studies.

### Strengths
*Conceptual Novelty and Relevance*: The paper introduces an approach to steering agents by focusing on Markovian agents with limited cognitive resources.

*Theoretical Contributions*: The authors provide a comprehensive theoretical analysis, including sufficient conditions for achieving low steering gaps and the existence of history-dependent steering strategies. 

*Algorithmic Development*: The proposed algorithms (belief-state-based steering strategy for small model classes and a First-Explore-Then-Exploit (FETE) framework for large classes) effectively balance the trade-off between tractability and optimality.

### Weaknesses
This is a solid paper with well-grounded contributions. My primary concern, however, is that the current setting is limited to a tabular MDP with a finite model class. While this simplified setting is acceptable for a theoretical paper, the corresponding experiments appear relatively basic. I am curious about whether the proposed Steering Dynamics framework can be extended effectively to more realistic scenarios (or if the Steering Dynamics framework is helpful in any real-world situation?) involving non-tabular MDPs and an infinite model class.

### Questions
1. What will happen if the model set $\mathcal{F}$ is uncountably infinite?

2. What will happen for a non-tabular MDP setup?

### Soundness
3

### Presentation
3

### Contribution
3
