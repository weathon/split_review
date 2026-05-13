# Reinforcement Learning from Imperfect Corrective Actions and Proxy Rewards

- Decision: Accept
- Scores: 5, 3, 8, 8

## Abstract
In practice, reinforcement learning (RL) agents are often trained with a possibly imperfect proxy reward function, which may lead to a human-agent alignment issue (i.e., the learned policy either converges to non-optimal performance with low cumulative rewards, or achieves high cumulative rewards but in an undesired manner). To tackle this issue, we consider a framework where a human labeler can provide additional feedback in the form of corrective actions, which expresses the labeler's action preferences although this feedback may possibly be imperfect as well. 
In this setting, to obtain a better-aligned policy guided by both learning signals, we propose a novel value-based deep RL algorithm called **I**terative learning from **Co**rrective actions and **Pro**xy rewards (ICoPro), which cycles through three phases: 
(1) Solicit sparse corrective actions from a human labeler on the agent's demonstrated trajectories; 
(2) Incorporate these corrective actions into the Q-function using a margin loss to enforce adherence to labeler's preferences; 
(3) Train the agent with standard RL losses regularized with a margin loss to learn from proxy rewards and propagate the Q-values learned from human feedback. Moreover, another novel design in our approach is to integrate pseudo-labels from the target Q-network to reduce human labor and further stabilize training. 
We experimentally validate our proposition on a variety of tasks (Atari games and autonomous driving on highway). On the one hand, using proxy rewards with different levels of imperfection, our method can better align with human and is more sample-efficient than baseline methods. On the other hand, facing corrective actions with different types of imperfection, our method can overcome the non-optimality of this feedback thanks to the guidance from proxy rewards.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, a framework is proposed where a human labeler can offer additional feedback in the form of corrective actions, reflecting the labeler's action preferences, even though this feedback may also be imperfect. Within this context, a novel value-based deep RL algorithm, Iterative Learning from Corrective actions and Proxy rewards (ICoPro), is introduced. This algorithm follows a three-phase cycle: (1) Eliciting sparse corrective actions from a human labeler on the agent's demonstrated trajectories; (2) Integrating these corrective actions into the Q-function using a margin loss to ensure adherence to the labeler's preferences; (3) Training the agent with standard RL losses, augmented with a margin loss to learn from proxy rewards and propagate the Q-values acquired from human feedback.

### Strengths
This paper explores an intriguing imitation learning problem in which human demonstrations are imperfect, although some corrective actions may be available. Additionally, there is no explicit reward signal, but certain action preferences (raw reward) are provided.

### Weaknesses
1) The performance of the human feedback policy would significantly impact the total performance of the proposed method. For example, if the human feedback is from an expert policy, then the cloning from its behaviors is reasonable and helpful for improving the performance. But if the human feedback is from a sub-optimal or even a random policy, then its behaviors may be harmful. Therefore, what we concern is how the level of sub-optimality of the human feedback policy would impact the performance of the algorithm.
	Currently, in Section 5.3 the authors have simulated the sub-optimal human feedback by inserting noisy actions, but we think such simulation is not enough for the explanation for this problem. Maybe the authors could utilize a half-trained Rainbow policy to generate the imperfect behaviors.

	2) The positions (states) of human feedbacks are also important for the efficiency and effectiveness. We observe that the authors selected the feedback positions with the method in RLIF [1], but we does not see the comparison and discussion with RLIF.
	Besides, to be fair, maybe this trick should also be utilized to other methods for comparison introduced in this paper.

[1] RLIF: Interactive imitation learning as reinforcement learning.

	3) The working scenarios. In our opinion, this method could be seen as a method that online learning while cloning from a specific behavior policy (human feedback). So why such combination could solve the problem of sub-optimality of the proxy reward and the human feedback? For example, if the proxy reward and human feedback make the similar mistake, then such combination would not work. Clearly, in such scenarios, the proposed method could achieve the claimed performance.

	4) In this paper, the authors raised an interesting and inspiring problem. However, the problem lacks of mathematical formulation and theoretical evidence for its effectiveness.

       5)  I found that the methodology adopted in this paper is closely related to those references cited in line 229 and the difference to each of those should be clearly stated. In addition, if the range of reward is not limited, then the loss of  eq.1 could be negative, as this expression is different from that of the traditional margin loss.

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new pipeline to learn from corrective actions and proxy rewards, which is interesting and useful for the practical use of RL algorithms. The pipeline of the algorithm is reasonable. The experiments show the effectiveness of the proposed methods.

### Strengths
The general idea of the paper is interesting. Involving human labelers in the training process is a very promising way to effectively enhance the training process. The paper is easy to follow.

### Weaknesses
One major weakness is that the experiments are kind of weak to support learning from corrective actions. The paper only provides two environments that are involved by real human labeler (Pong and Highway). Most of the environments are using simulated labeler. More environments that show the necessity to involve human labels would be great to support the idea of the paper.



The writing of the paper could be improved. 

- The abstract could be further condensed. 

- Line 178~185: $\mathcal{S}, \mathcal{A}$ is not defined. The $Q$ function is not formally defined.

- Line 182: Is $\pi^*$ a typo? Do you refer $\pi^*$ to an optimal policy, or greedy policy, or arbirtrary policy?

- Line 353: You should use $a^L \sim $ rather than $a^L=$ if the action is sampled from some $\epsilon$-greedy distribution.

  

The motivation for combining the two sources of signals is good, but the description in the paper (from Line 66~80) does not make sense to me. The paper stated 'In contrast, our key insight is that the two sources of signals can complement each other.. while the effects of suboptimal corrective actions may be weakened by proxy rewards'.  However, the proxy rewards could also be suboptimal, as it's only an approximation of the real reward function.

### Questions
Could you please elaborate more practical examples that involving human labelers is necessary?

### Soundness
3

### Presentation
3

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
This paper proposes to use proxy reward (the reward that is easily defined and might not accurately reflects the desired behavior) and the offline corrective action (labeller assigns correct actions to the rollouts generated by the agent, and those corrective actions will not be used to the environment as the labelling process is offline) to train policies.

The training can be split into 3 phases: data collection, finetune-phase, and propagation-phase. In the data collection phase, agent rolls out trajectories with epsilon-greedy exploration and human provide offline corrective actions. In finetune phase, marginal loss is applied to the Q values to make sure the Q values for corrective actions are high. In propagation phase, RL loss (TD loss with the proxy reward) and the marginal loss (the imitation loss that enforces the learned policy to be closed with previous agent policy) are used together.

### Strengths
1. Good to see the author provides source code.
2. Human-in-the-loop with offline corrective feedback is a quite interesting setting. Previous work either focus on online demonstration (HGDagger, PVP etc) or offline labeling (PbRL, TAMER), but this work focus on offline corrective action (not the reward labeling but the action).
3. Human-in-the-loop methods suffer from the cost of human subjects, as they need to be very attentive if in a online human-AI shared control setting. This paper adopts the offline setting and utilize the proxy reward, which is an interesting way to scale up the human-in-the-loop method.

### Weaknesses
1. Further analysis will greatly improve the technical depth of the paper. Further analysis on ablations and why the method work is needed. These include: why marginal loss in propagation phase works? How well the method work with human labeler in different optimality? The ablations study are presented in Section 5.2 and Table 2 while in Appendix A, while there is no discussion on the reasons. The author just put the results there. See more on "Questions".
2. All ablation studies are conducted in the Atari, and further discussion is needed. Why ablations fail? What insights can we get from the ablation studies?
3. As a paper studying human-in-the-loop policy learning, there is no enough weights on real-human experiments. Section 5.4 shows the experiment with real human subject. I will expecting far more information about this experiment. Why don't put the evaluation results of the trained policies in each iteration of the training and compare it against the baselines? Is there qualitative results showing the human's corrective actions and the agent's actions?
4. Follow question 3, providing corrective actions is actually very boring and time-consuming. The setting might be even more exhausting than online human supervision. I doubt whether the method is applicable at all in real-human setting.

### Questions
1. Why the marginal loss in propagation phase works? IIUC the "w/o aTGT" ablation is the experiment ablating the marginal loss in propagation correct? It seems that adding that term can help in terms of the final results. But more analysis is needed. For example, will adding the term improve the learning efficiency and reduce human interventions? In Sec 5.2 the ablation studies only show the performance in tasks but the other metrics such as "human efficiency" is not compared.
2. How to ensure the label quality? In more complex task like driving, human labeler is hard to understand the outcome of their "corrective actions". For example to rescue a car from crashing left car, the human labeler might steer the car all to the right hand side. And this action though seems to be correct, but it's impossible to be applied in real world (you can't rotate the steering wheel immediately from left to right), and it will also cause unknown outcome such as car rollover. There is no guarantee on the quality of the data especially in the offline setting. In motivation the authors suggest this paper can work with suboptimal human labeler but **no experiment shows the method still work on suboptimal experts**.
3. I will expect more discussion on human cost. What designs in the method can improve human efficiency (less corrective actions)? Line 259-261 says "In addition, training with pseudo-labels can
reduce the cost of collecting human labels by leveraging the large number of unlabeled states in
Denv" No experiment supports this claim and I will consider this to be a overclaim. Is there any evidence showing that the agent converge to same performance with less human (here the simulated expert) involvement?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel method that integrates additional (imperfect) corrective actions into the reinforcement learning (RL) process to address limitations in the imperfect proxy reward function.

### Strengths
The paper is well-organized and easy to follow, and the experimental section provides sufficient evidence to support the authors' claim that their approach improves the learning of an optimal policy.

### Weaknesses
1. The reviewer is curious about the performance information available to the labeler that allows them to decide whether an action is good or bad, considering that the queries are sampled from a dataset rather than occurring in real-time. In the experiments, a trained Q-network is used as the labeler, which simplifies the collection of corrective actions. Although there is a user study involving human labelers in two environments (Highway and Pong), this does not fully address my concern.

2. The term "sample-efficient" is mentioned frequently throughout the paper, yet no clear metrics are provided to quantify this efficiency. It would be helpful to include some metrics to validate this claim.

3. Some relevant literature is missing from the discussion. For instance, ranking-based reinforcement learning [1]. The authors could also refer [2], which might offer more effective corrective actions than relying solely on the target Q-network, especially during the early stages when the model is undertrained.

There are a few minor issues with the writing. For example:

In the related work section, the discussion on the limitations of the offline setting is mentioned but not clearly explained. Providing more clarity here would be helpful. Table I includes some abbreviations, such as PR1 and PR2, which I assume stand for Proxy Reward. However, additional explanation would improve understanding for readers unfamiliar with these terms.
   
Reference:
[1] Brown, Daniel S., Wonjoon Goo, and Scott Niekum. "Better-than-demonstrator imitation learning via automatically-ranked demonstrations." Conference on robot learning. PMLR, 2020.
[2] Zhan, Huixin, Feng Tao, and Yongcan Cao. "Human-guided robot behavior learning: A gan-assisted preference-based reinforcement learning approach." IEEE Robotics and Automation Letters 6.2 (2021): 3545-3552.

### Questions
1. What interface is used for the corrective action process?
2. The entire approach is based on the Q-function, which is limited to discrete action spaces. Can this method be extended to continuous action spaces (without discretization)?

### Soundness
3

### Presentation
3

### Contribution
3
