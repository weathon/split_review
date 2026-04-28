# Analyzing the Effects of Emulating on the Reinforcement Learning Manifold

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 8, 3

## Abstract
Reinforcement learning has become a prominent research direction with the utilization of deep neural networks as state-action value function approximators enabling exploration and construction of functioning neural policies in MDPs with state representations in high dimensions. While reinforcement learning is currently being deployed in many different settings from medical to finance, the fact that reinforcement learning requires a reward signal from the MDP to learn a functioning policy can be restrictive for tasks in which the construction of the reward function is more or equally complex than learning it. In this line of research several studies proposed algorithms to learn a reward function or an optimal policy from observed optimal trajectories. In this paper, we focus on non-robustness of the state-of-the-art algorithms that accomplish learning without rewards in high dimensional state representation MDPs, and we demonstrate that the vanilla trained deep reinforcement learning policies are more resilient and value aligned than learning without rewards in MDPs with complex state representations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the robustness of policies derived from expert demonstrations in the context of high-dimensional Markov Decision Processes (MDPs). The key contribution of this study is the demonstration that deep reinforcement learning policies, trained using the actual reward signal, exhibit much greater robustness against adversarial attacks and perturbations, as compared to policies obtained through inverse reinforcement learning.

The authors further ground their empirical findings with a theoretical framework. They illustrate that in the context of inverse soft-Q-learning with linear policies, the learned rewards are random for states not included within the manifold visited by the expert demonstrations.

### Strengths
* The paper studies a relevant problem in light of the current success of RLHF methods and the misalignement problem.
* The findings of the paper clearly point out a substantial lack of robustness of policies learned by IRL to both adversarial attacks and random perturbations.
 * Section 3 offers interesting insights into the shortcomings of linear Q-function approximators in the Inverse Soft Q-Learning setting.

### Weaknesses
 * The comparisons between the vanilla policies and those derived from IRL are unfair as the vanilla policy is trained on hundreds of thousands of tranisitions whereas its IRL counterpart gets to see only few thousands of transitions.

* The case of studied linear Q-function approximators in the theoretical part is quite restrictive. The assumptions used for Proposition 3.5 are very strong. A potentially more general direction would be to study smooth Q-approximators in the case of Lipschitz MDPs.

* Another weakness is that the authors do not offer no solutions to the problem of lack of robustness. This could be in the form of better training methods for the policy like regularization or better strategies to collect demonstrations.

### Questions
I have a few questions for the authors :

1. In the background paragraph, you do not distinguish between Imitation Learning and Inverse Reinforcement Learning. Although IRL covers a broader range of algorithms than can learn even from suboptimal data. Could you please clarify your choice?

2. Could you clarify what you mean by "Manifold setting" in the introduction?

3. Could you clarify what $\phi$ stands for in the inverse Q-learning objective?

4. Relating to the weaknesses, could you provide plots for the evolution of the performance of the IRL policy under adversarial and or perturbation setting in an online setting where it can perform X transitions?

5. I am aware this might not be possible for the current time window. It would've been interesting see a comparison of the robustness of policies learned from expert demonstrations and those learned by ranking of trajectories. As the latter case covers sub-optimal states it can be a potential solution to the robustness problem. Could you add such experiments?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigates the robustness of vanilla reinforcement learning algorithms compared to methods learning from expert demonstrations, such as inverse reinforcement learning (IRL). The study starts from the formulation of theoretical analysis that shows learning from demonstration can produce lower robustness. In particular, the authors argue that perturbations can cause agents to transition into states where the generated reward from IRL and the states are not correlated, eventually decreasing the agent's robustness by making it not achieve optimal returns in the task of interest. The authors then formulated a way to generate perturbations that cause this highlighted problem and showed vanilla reinforcement learning algorithms yield a lower drop in returns compared to methods learning from expert demonstration.

### Strengths
**Originality**

To the best of my minimal knowledge on the topic, the paper appears to be novel. I have not seen other works that establish theoretical analysis on the robustness of inverse reinforcement learning algorithms towards state perturbations.

**Quality - Experiments**

While I did not extensively check the theoretical contributions made in this paper, the experiments that empirically demonstrate the issues with the perturbations proposed in the earlier (theoretical) sections seem to be sound. It believe it empirically demonstrates the claim regarding the robustness issues of IRL methods.

**Clarity**

In general, the paper is well-written. Despite having introduced plenty of theorems throughout the document, the authors did a good job outlining the role of each theorem in highlighting the weaknesses of IRL methods in terms of their robustness. Similarly, I found the experiments (and their analysis) were well written in terms of explaining the overall argument of the paper. 

**Significance**

In general, I find that the problem being tackled in this paper could provide highly valuable results for the broader ICLR community. Most reinforcement learning researchers would be highly concerned with the robustness of the policies they trained. While the theoretical analysis seems limited to inverse RL methods, it's still valuable knowledge that perhaps can spur further research in this area. At least, this paper provides the broader RL community with something to consider when choosing between vanilla RL and IRL from expert demonstrations.

### Weaknesses
 **Clarity - Perturbation used in experiments**

While it may be tricky to produce, it may be useful to show what the perturbations used in the environment really look like. I believe this could help readers further understand the type of "noises" introduced to demonstrate the claims in this paper. Specifically, it would be beneficial to understand the magnitude and frequency of these perturbations, and whether they are applied to the state space directly or through some transformation. For example, are these perturbations Gaussian noise added to the state vectors, or are they more structured changes that alter the underlying dynamics of the environment? Furthermore, it would be helpful to see how these perturbations affect the state space distribution and whether they push the agent into regions outside of the training distribution. This would help in assessing the severity of the perturbations and their relevance to the claims made about robustness.

### Questions
I do not have further questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper examines the robustness of deep neural policies in adversarial settings. It evaluates the robustness of the deep reinforcement learning algorithm and contrasts it with both imitation learning and inverse reinforcement learning methods. The paper also discusses scenarios in which the optimal trajectory changes due to action perturbations in the policy within the inverse reinforcement learning context.

### Strengths
- The domain and motivation are compelling, with a focus on understanding the manifold and assessing minor changes for generalization.
- Attempts have been made to offer both theoretical motivation and empirical evaluation.

### Weaknesses
 - Throughout the paper, numerous instances of ambiguous language complicate understanding.
- The connections between Lemmas, Propositions, Corollaries, and their proofs to the paper's central message are unclear.
- The experiments are missing crucial details, including specifics on the policy architecture, and the explanations of the results are unclear.

- The paper intends to analyze the reinforcement learning manifold. However, the meaning is not evident from the text. Could you clarify what this entails and how the theoretical and empirical analyses relate to it?

- In several sections, the paper mentions "with reward" and "without reward." However, their exact meanings are unclear. Does "without reward" refer to imitation and inverse RL? Furthermore, "without reward" is commonly associated with unsupervised RL, where the agent does not receive a reward signal. Could you please provide clarification? It's crucial to maintain this distinction consistently throughout the paper.

- Throughout the paper, several instances of vague language make comprehension challenging. For instance, does “that focus on learning via emulating affect” refer to imitation learning?
And what exactly is meant by "learning from exploration"? Is it referring to regular reinforcement learning?


- "Our paper is the first to focus on the adversarial vulnerabilities of deep neural policies that can learn without a reward function." Could you clarify how the proposed method learns without a reward function?


- The related work is presented without clearly delineating how the current work differs or aligns with it. Providing these comparisons would enhance the related work section.


- While the paper references the general term "deep reinforcement learning," the analysis primarily centers on Q-learning-based approaches. The examination of another form of algorithm, specifically policy gradient, is absent. I suggest the author specify the exact type of algorithm analyzed in the paper for clarity and completeness.

- Throughout the paper, I find it challenging to link the various Lemmas, Propositions, Corollaries, and their proofs to the central message of the paper. For instance, the purpose and significance of Lemma 3.1 (and its proof) remain unclear to me. The necessity and meaning behind Propositions 3.3 and 3.5 are also ambiguous. What is the intent of Definition 4.1? How does it relate to the main objective of the paper?

- The caption for Table 1 is unclear and requires significant revision. Both Table 1 and Table 2 mention the tasks Pong and Seaquest, yet the results display three different games. How were these results derived?

- “The state-of-the-art imitation and inverse reinforcement learning policy is trained via the inverse Q-learning algorithm described in Section 2.” However, I do not see this detailed in the paper. How can both imitation and IRL be trained via Q-learning? The explanation seems to be absent and unclear.

- For Figure 1, which environment is being depicted? Is it an average of all three games (Seaquest, BeamRider, and Breakout)? The purpose and message of Figure 1 are unclear.


- Overall, the writing needs revision. It predominantly consists of lengthy sentences, making comprehension challenging. Addressing this by crafting shorter, simpler sentences would be beneficial.

- Implementation details appear to be missing in the paper. Which architecture is used to represent the policy? Which specific algorithms are utilized for IRL and imitation? Without these specifics, it's challenging to justify the performance presented.

- While the paper seems to concentrate on high-dimensional cases, how do the outcomes vary in a low-dimensional representation?

### Questions
The paper intends to analyze the reinforcement learning manifold. However, the meaning is not evident from the text. Could you clarify what this entails and how the theoretical and empirical analyses relate to it?

In several sections, the paper mentions "with reward" and "without reward." However, their exact meanings are unclear. Does "without reward" refer to imitation and inverse RL? Furthermore, "without reward" is commonly associated with unsupervised RL, where the agent does not receive a reward signal. Could you please provide clarification? It's crucial to maintain this distinction consistently throughout the paper.

Throughout the paper, several instances of vague language make comprehension challenging. For instance, does “that focus on learning via emulating affect” refer to imitation learning?
And what exactly is meant by "learning from exploration"? Is it referring to regular reinforcement learning?


"Our paper is the first to focus on the adversarial vulnerabilities of deep neural policies that can learn without a reward function." Could you clarify how the proposed method learns without a reward function?


The related work is presented without clearly delineating how the current work differs or aligns with it. Providing these comparisons would enhance the related work section.


While the paper references the general term "deep reinforcement learning," the analysis primarily centers on Q-learning-based approaches. The examination of another form of algorithm, specifically policy gradient, is absent. I suggest the author specify the exact type of algorithm analyzed in the paper for clarity and completeness.

Throughout the paper, I find it challenging to link the various Lemmas, Propositions, Corollaries, and their proofs to the central message of the paper. For instance, the purpose and significance of Lemma 3.1 (and its proof) remain unclear to me. The necessity and meaning behind Propositions 3.3 and 3.5 are also ambiguous. What is the intent of Definition 4.1? How does it relate to the main objective of the paper?

The caption for Table 1 is unclear and requires significant revision. Both Table 1 and Table 2 mention the tasks Pong and Seaquest, yet the results display three different games. How were these results derived?

“The state-of-the-art imitation and inverse reinforcement learning policy is trained via the inverse Q-learning algorithm described in Section 2.” However, I do not see this detailed in the paper. How can both imitation and IRL be trained via Q-learning? The explanation seems to be absent and unclear.

For Figure 1, which environment is being depicted? Is it an average of all three games (Seaquest, BeamRider, and Breakout)? The purpose and message of Figure 1 are unclear.


Overall, the writing needs revision. It predominantly consists of lengthy sentences, making comprehension challenging. Addressing this by crafting shorter, simpler sentences would be beneficial.

Implementation details appear to be missing in the paper. Which architecture is used to represent the policy? Which specific algorithms are utilized for IRL and imitation? Without these specifics, it's challenging to justify the performance presented.

While the paper seems to concentrate on high-dimensional cases, how do the outcomes vary in a low-dimensional representation?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
