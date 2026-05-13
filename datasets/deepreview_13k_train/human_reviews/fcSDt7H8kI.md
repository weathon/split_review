# Boosting Reinforcement Learning with Extremum Experiences

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Reinforcement learning research has achieved high acceleration in its progress starting from the initial installation of deep neural networks as function approximators to learn policies that make sequential decisions in high-dimensional state representation MDPs. While several consecutive barriers have been broken in deep reinforcement learning research (i.e. learning from high-dimensional states, learning purely via self-play), several others still stand. On this line, in our paper we focus on experience collection in high-dimensional complex MDPs and we propose a unique technique based on experiences obtained through extremum actions. Our method provides theoretical basis for efficient experience collection, and further comes with zero additional computational cost while leading to significant sample efficiency gains in deep reinforcement learning training. We conduct extensive experiments in the Arcade Learning Environment with high-dimensional state representation MDPs. We demonstrate that our technique improves the human normalized median scores of Arcade Learning Environment by 248% in the low-data regime.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new exploration strategy in reinforcement learning which focuses on taking extremum actions with minimum Q-values. Theoretically, the authors attempt to prove that the TD computed by taking the action with minimum Q-value (denoted as $a_{min}$) is above average (i.e., expected Q-value for a uniform policy) by an amount approximately equal to the disadvantage gap, which is referred to the expected Q-value for a uniform policy minus the Q-value for $a_{min}$. The proposed MaxMin TD Learning policy follows the $\epsilon$-greedy style, where the proposed algorithm takes $a_{min}$ instead of uniform random action for exploration.

### Strengths
- This paper proposes an interesting idea of improving the exploration efficiency by taking extremum action, which refers to the action with minimum Q-value. 

- The method comes with a nice theoretical motivation, where the authors show the proof of the relationship between TD error inferred by taking $a_{min}$ compared to that for a uniform policy, showing that taking $a_{min}$ as the extremum action more frequently could lead to novel transitions that accelerate learning.  

- The proposed method is very general and simple to apply, leading to no additional computational overhead compared to vanilla $\epsilon$-greedy.

- The authors show comparison results with UCB and $\epsilon$-greedy on a toy chain MDP domain and large-scale experimental results by comparing with NoisyNets and $\epsilon$-greedy on Atari 100K.

### Weaknesses
 - The theoretical contribution of this paper relies on several strong assumptions: (1) expected rewards for a uniform random policy and the $a_{min}$ is $\eta$-uniformed; (2) the Q-value for consequent states $s$ and $s'$ has little difference ($\delta$-smooth); (3) the initialized Q-function results in a policy that is close to uniform random. The main theoretical conclusion that the TD achieved by $a_{min}$ is above-average by an amount approximately equal to the disadvantage gap ($D(s)$) would be wrong if $\delta$ and $\eta$ are not close to 0, because the gap actually equals to $D(s) - 2\delta - \eta$. Specifically, the assumption of $\delta$-smoothness between consecutive states' Q-values seems particularly strong in environments with sparse rewards or complex dynamics. Moreover, in practice, deep neural networks used for Q-function approximation often exhibit highly non-uniform initial policy distributions, invalidating assumption (3). This discrepancy between theoretical assumptions and practical scenarios raises concerns about the applicability of the derived conclusions in real-world settings, especially when employing deep Q-networks.

- In the proposed Algorithm 1, the RL agent always takes $a_{min}$ for exploration action, and no action with intermediate Q-values could be taken for exploration. Unless $a_{min}$ would keep changing among the action set throughout the training, the proposed method would likely result in sub-optimal policy compared to $\epsilon$-greedy due to the limited exploration strategy. The concern is that consistently selecting $a_{min}$ might lead to a narrow exploration of the state space, potentially missing valuable transitions that could be discovered by sampling actions with intermediate Q-values. This is particularly relevant in environments where the optimal policy requires a diverse set of actions, not just those initially deemed least promising.

- The empirical results on the motivating example are not entirely convincing. The learning curves of MaxMin TD, $\epsilon$-greedy, and UCB are presented, but the exploration policies for the two baselines are not clearly specified. For instance, if a fixed $\epsilon$ is used for $\epsilon$-greedy, it might explain its sub-optimal performance in the chain MDP. A well-tuned $\epsilon$-greedy with a proper decay schedule would likely succeed in this simple environment. It is also unclear whether MaxMin TD learning can perform adequately without $\epsilon$ decay. A fair comparison would require all methods to employ either a fixed or decayed $\epsilon$, and these details should be explicitly stated.

- For the large-scale Atari 100K evaluation, the choice of baselines is insufficient. Given the focus on exploration policy, it is crucial to include comparisons with UCB-variant baselines. Furthermore, neither noisy networks nor $\epsilon$-greedy represent the state-of-the-art methods on Atari 100K. Stronger baselines that incorporate more sophisticated exploration strategies should be considered to provide a more comprehensive evaluation.

- The learning curves for the noisy net are missing in the Atari 100K figures (e.g., Fig 2 and Fig 4). These curves should be included for each game to allow for a complete comparison of the methods.

- The evaluation could be strengthened by including a more diverse set of tasks, such as the full Atari 2600 suite and continuous control tasks like MuJoCo. This would help to assess the generality of MaxMin TD Learning and its applicability to both value-based and policy-based algorithms.

### Questions
Please refer to the WEAKNESSES section.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an exploration method based on minimizing the state-action value function. The method is incorporated into temporal difference based on Q-learning with function approximation. Experiments are conducted using a toy chain MDP and several Arcade Learning Environments. The results are compared to the $\epsilon$-greedy baseline.

### Strengths
- The paper addresses the important problem of exploration in reinforcement learning.
- It attempts to provide theoretical justification and analyzes empirical results using toy examples and standard benchmark tasks.

### Weaknesses
 - Several claims in the paper require further evidence.
- The empirical evaluation lacks detail.
- Details are lacking in addressing the research questions and contributions proposed in the introduction.

- An assumption of the proposed method is that the Q-function, in the initial phase of training, would assign similar values to similar states.
“...early in training the Q-function, on average, will assign approximately similar values to states that are similar…”, “....when the Q-function on average assigns similar maximum values to consecutive states”. 
It is unclear how this assumption holds. If a random Q-function processes different consecutive states, then the output value might be arbitrary and not necessarily dependent on the input, even for slightly varied states. Thus, the output could be any random number, not necessarily a similar value.

- The text in the plots of Figure 1 is too small and difficult to read. What do each of the plots represent? Are they for different $\epsilon$ values? Which plot corresponds to which value? Also, how does a change in ε affect the results of the proposed MaxMin TD learning?

- It is mentioned that "All of the results in the paper are reported with the standard error of the mean”. However, Figure 2 shows the results for the median on the y-axis. Could you clarify what this means?

- The claim “.....thus creates novel transitions in exploration with more unique experience collection.” is made, but no evidence is presented in the paper. The results are only compared based on reward performance. How can we be certain that the change in results is due to this particular claim?

- In Table 1, the Human Normalized Median is 0.0927 for MaxMin TD and 0.0377 for $\epsilon$-greedy. If 1 is the highest achievable score, then these numbers appear quite low. Do both algorithms fail to learn anything useful? In that case, stating a 248% improvement seems misleading.

- What is the QRDQN algorithm baseline in Figure 5? It is not discussed in the paper. What is the difference between $\epsilon$-greedy in Figure 1 and Figure 5? While it is briefly mentioned in the footnote of the supplementary materials, detailed references are not presented.

- It is mentioned in the introduction as a contribution that the proposed method "...reaches approximately the same performance level as model-based deep reinforcement learning algorithms," suggesting that the proposed method performs better than model-based. However, no model-based baseline is presented in the experiments, nor is it explained in the text.

### Questions
An assumption of the proposed method is that the Q-function, in the initial phase of training, would assign similar values to similar states.
“...early in training the Q-function, on average, will assign approximately similar values to states that are similar…”, “....when the Q-function on average assigns similar maximum values to consecutive states”. 
It is unclear how this assumption holds. If a random Q-function processes different consecutive states, then the output value might be arbitrary and not necessarily dependent on the input, even for slightly varied states. Thus, the output could be any random number, not necessarily a similar value.

The text in the plots of Figure 1 is too small and difficult to read. What do each of the plots represent? Are they for different $\epsilon$ values? Which plot corresponds to which value? Also, how does a change in ε affect the results of the proposed MaxMin TD learning?

It is mentioned that "All of the results in the paper are reported with the standard error of the mean”. However, Figure 2 shows the results for the median on the y-axis. Could you clarify what this means?

The claim “.....thus creates novel transitions in exploration with more unique experience collection.” is made, but no evidence is presented in the paper. The results are only compared based on reward performance. How can we be certain that the change in results is due to this particular claim?

In Table 1, the Human Normalized Median is 0.0927 for MaxMin TD and 0.0377 for $\epsilon$-greedy. If 1 is the highest achievable score, then these numbers appear quite low. Do both algorithms fail to learn anything useful? In that case, stating a 248% improvement seems misleading.

What is the QRDQN algorithm baseline in Figure 5? It is not discussed in the paper. What is the difference between $\epsilon$-greedy in Figure 1 and Figure 5? While it is briefly mentioned in the footnote of the supplementary materials, detailed references are not presented.

It is mentioned in the introduction as a contribution that the proposed method "...reaches approximately the same performance level as model-based deep reinforcement learning algorithms," suggesting that the proposed method performs better than model-based. However, no model-based baseline is presented in the experiments, nor is it explained in the text.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work looks at improving sample complexity of deep reinforcement learning (RL) algorithms from the lens of experience collection. A new method based on minimizing state-action value function to increase information gain is proposed. Modifying episilon-greedy, the algorithm leads to more novel experiences by taking actions with the smallest Q-value. Experimentally, the proposed method demonstrates significant improvement in sample complexity in the Arcade Learning Environment, without additional learning parameters.

### Strengths
1. The proposed method is well motivated and empirically shows significant improvements in sample efficiency.
2. The paper, in general, is well-structured.

### Weaknesses
1. The first few definitions is unclear and unintuitive. Specifically, the paper introduces terms without sufficient context, making it difficult to grasp their significance within the broader RL framework. For instance, the notion of minimizing the state-action value function to increase information gain is not immediately obvious, and more explanation is needed to clarify this connection.
2. The definition of $\hat{a}$ is confusing in Definition 3.2. It's unclear whether $\hat{a}$ represents a specific action selection mechanism or a general placeholder. The notation does not clearly articulate how this action is derived or how it relates to the overall objective of the algorithm. This ambiguity makes it hard to follow the subsequent theoretical development.
3. There needs to be a related work section. It is unclear how this approach position among existing works. The paper lacks a discussion of how the proposed method compares to existing exploration techniques in RL, such as those based on intrinsic motivation or uncertainty quantification. Without this context, it's difficult to assess the novelty and significance of the contribution.
4. Figure 1 is too small. The details in the figure are difficult to discern, making it hard to understand the experimental setup or results being presented. The small size hinders the reader's ability to properly evaluate the experimental design.
5. Missing standard deviation in Figure 3. The absence of error bars or standard deviation makes it impossible to assess the statistical significance of the results. It is crucial to include these measures to determine the robustness of the observed improvements.
6. [Minor] the repetition of the questions in conclusion seems like a waste of space to me.

### Questions
1. Based on Figure 4, Max-Min TD seems to have higher variance, why is that?
2. Would the method be as effective in sparse-reward setting given that it ties directly to the size of TD?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new algorithm, MaxMin TD Learning, by modifying $\epsilon$-greedy exploration in DQN. Specifically, with probability $\epsilon$, the argmin action is selected given the state-action values. Theoretically, this leads to higher temporal difference error under certain assumptions. In practice, the proposed algorithm is shown to achieve higher sample efficiency than DQN with $\epsilon$-greedy exploration.

### Strengths
As far as I know, the presented idea is novel and easy to implement. Generally, the paper is easy to follow. The advantage of the proposed algorithm is supported by both theories and experiments. All algorithms are tested in 100K Atari games.

### Weaknesses
The major weaknesses are insufficient experiments, a gap between theory and experiments, and a lack of explanation.

- How large is $\mathcal{D}(s)$, $\delta$, and $\eta$ in practice? Is $\mathcal{D}(s) − 2\delta − \eta$ positive or negative in practice?
- In Section 4, a fixed step size is used. How does the performance of the algorithms vary with different step sizes?
- In Section 4, $\epsilon$ is chosen from $[0.15, 0.25]$. In practice, a smaller $\epsilon$ is usually used. How is the performance of the algorithms with smaller $\epsilon$, such as $\epsilon \in [0.01, 0.05]$? How sensitive is MaxMin TD learning to $\epsilon$ compared to DQN?
- In Figure 4, not all tasks (e.g. Amidar, Bowling, BankHeist, and StarGunner) are trained with 200M frames although it is claimed so.
- In Section 3, it is claimed that, in the early phase of the training, in expectation over the random initialization $\theta \sim \Theta$, the TD error is higher when taking the minimum value action than that of a random action. However, this contradicts the experimental results shown in Figure 3, especially Figure 3(a).
- Lack of explanation: Why would a higher TD error help exploration and speed up training in general? I don't see a clear connection between them. I believe that it is very important to explain the logic behind.

### Questions
- In Definition 3.2 & 3.5: What is $\hat{a}(s,\theta)$?
- In Proposition 3.4, $a_t \sim \mathcal{U},(\mathcal{A})$: typo.
- In Section 4, it is mentioned that the maximum achievable reward in 100 steps is 10. However, the learning curve in Figure 1 (b) is above 10 in the end. How do you get the data used in Figure 1?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
