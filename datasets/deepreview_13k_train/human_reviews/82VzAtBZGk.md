# Safe Reinforcement Learning in Black-Box Environments via Adaptive Shielding

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
Empowering safe exploration of reinforcement learning (RL) agents during training is a critical impediment towards deploying RL agents in many real-world scenarios. Training RL agents in unknown, \textit{black-box} environments poses an even greater safety risk when prior knowledge of the domain/task is unavailable. We introduce ADVICE (Adaptive Shielding with a Contrastive Autoencoder), a novel post-shielding technique that distinguishes safe and unsafe features of state-action pairs during training, thus protecting the RL agent from executing actions that yield potentially hazardous outcomes. Our comprehensive experimental evaluation against state-of-the-art safe RL exploration techniques demonstrates how ADVICE can significantly reduce safety violations during training while maintaining a competitive outcome reward.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a new shield based on contrastive learning to increase the safety of RL agents. This approach learns a latent representation that separates safe and unsafe state-action pairs. After learning this latent representation, it uses a KNN approach to classify, which requires a threshold K to indicate how many neighbors to consider a state-action pair unsafe. The paper shows how this parameter can be adapted online based on the safety of the RL agent. Finally, the paper provides empirical evidence that the proposed method increases the safety of the RL agent.

### Strengths
- The paper is well written. The description of the method is precise.
- The proposed method is original. It is the first method to use contrastive learning in a safe RL setting.
- The empirical evaluation indicates the approach can potentially increase the safety of RL algorithms.

### Weaknesses
 The problem formulation is incomplete. The paper does not define the safety properties expected from the RL agent.
- Lack of theoretical results. This paper provides only empirical results to support its claims.
- The results are presented in a convoluted way. In particular, the results disregard the safety violations of the agent in the first 1000 episodes. The reason for presenting the results in this way is unclear.
- The presentation of the DDPG-Lag as a constrained RL algorithm is imprecise, as it uses a fixed weight for the costs, which works as simple reward engineering. In general, with a Lagrangian relaxation, this weight should be adjusted online to ensure the accumulated cost stays below a predefined threshold [1].
- The evaluation in CMDPs is inconsistent. These approaches solve different problems where a predefined accumulated cost is allowed.
- Weak baseline. From the results in Figure 10, it is clear that Tabular Shield does not recognize any unsafe state-action pairs, making it an unsuitable baseline. This is not surprising considering how the state-action space is discretized. Perhaps it is necessary to finetune the discretization of this baseline. Alternatively, it would be more suitable to consider stronger baselines, such as the accumulating safety rules [2]

### Questions
- If the problem had a single initial state, would this be an issue for this approach? How does the diversity of initial states influence the performance of the ADVICE algorithm?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents ADVICE (Adaptive Shielding with a Contrastive Autoencoder), a novel post-shielding technique for safe reinforcement learning (RL) in complex black-box environments. ADVICE distinguishes between safe and unsafe state-action pairs during training using a contrastive autoencoder, protecting the RL agent from executing hazardous actions. The method includes an adaptation component based on the agent's recent performance, encouraging exploration when appropriate. Extensive experiments against state-of-the-art safe RL exploration techniques demonstrate that ADVICE significantly reduces safety violations during training while maintaining competitive outcome rewards.

### Strengths
- ADVICE introduces a new way to handle safety in RL using a contrastive autoencoder for distinguishing safe and unsafe actions.
- Despite prioritizing safety, ADVICE maintains competitive performance in terms of rewards compared to other methods.
-  ADVICE does not require prior knowledge about the environment, making it suitable for black-box scenarios.

### Weaknesses
 - ADVICE requires an initial period to gather data before it can be fully effective, which could be a disadvantage in some scenarios.
- The paper suggests that ADVICE might struggle with dynamic environments and could benefit from incorporating temporal context, which would add additional computational load.
- The performance of ADVICE is sensitive to hyperparameters like the safety threshold K, which might require careful tuning.

### Questions
- Can ADVICE be integrated with other RL algorithms except for DDPG?
- What are the potential limitations of using a contrastive autoencoder in the context of safe RL, and how might these be addressed?
- What are the implications of ADVICE's cold-start issue on its applicability in real-world scenarios where immediate safety is critical?

### Soundness
3

### Presentation
2

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
This paper proposes a post-shielding method ADVICE to reduce the constraint violation during the safe RL training. It first trains a neighbor model to classify the safety of state-action pair by contrastive learning in embedding space. Then it leverages this model to identify the safety of new state-action by the statistics of its K nearest neighbors and corrects the unsafe action to a safe one from a selected safe set. The authors conduct experiments on several safety gymnasium environments, which show that the proposed method can reduce the cumulative safety constraint violation during training.

### Strengths
- This paper proposes a new shield-based method for safe exploration, which is an important problem for application of RL.
- Overall, the paper is clearly written (e.g., fig. 1) and easy to follow. 
- The idea of classifying the safety of state-action in latent space is novel.

### Weaknesses
 - My biggest concern is the effectiveness of neighbor model in step 1, which determines whether a new state-action is safe or not. However, this key component in the proposed shielding method is trained based on data collected in an initial unshielded stage (line 161). During the execution, the policy will be updated and differ from the initial policy, which will lead to a severe distribution shift of state-action pair. Therefore, it's very questionable whether the neighbor model can still distinguish safe state from the unsafe one given unseen new state-action distribution. The use of a randomized environment does not fundamentally address this issue, as the policy changes during training, leading to a shift in the state-action distribution regardless of the environment's randomization.
- The construction of safe or unsafe sets $\mathcal S, \mathcal U$ is also problematic. In eq. (3), the feature (state-action pair) is classified as safe if it's start or next state reaches the goal while the feature with next state crashed is unsafe. Such classification obviously introduces some spurious correlations, e.g., the state-action pair is identified as unsafe because it's far from the goal instead of it will truly crash with obstacles. Meanwhile, the contrastive learning objective excludes the inconclusive features, the majority of the collected data, which makes the coverage of training data on state-action space very limited and further exacerbates the distribution shift issue. The reliance on only terminal or accepting states for defining safety and unsafety is a significant limitation, as it ignores the vast majority of the state-action space where safety is not immediately clear. This approach risks creating a model that is overly sensitive to specific terminal conditions and not robust to the nuances of the overall state-action space.
- In experiment, although the results in fig.2 show that ADVICE has smaller cumulative safety violation, ADVICE also performs similarly to baselines on some other tasks (e.g., fig. 8(c) &9). Meanwhile, it's very weird that DDPG-lag and DDPG have very close results (also see questions), suggesting the DDPG-lag baseline is not well-tuned.

Minor issues:
- line 142, distinguish -> distinguishes 
- Eq.(2), $F$ -> $\mathcal F$
- many notations are not defined before using. E.g., $\mathbb Z_+$ in eq. (2), $E$ in line 2 of Algorithm 1.

### Questions
- What are the data of visualization in last column in fig.2? Are they training data for neighbor model?
- Does the "constrained randomised goal" correspond to "randomised CMDP" in fig.7(d)?
- Why do not you use the standard tasks provided by safety-gymnasium (e.g., PointGoal, CarButton, ...) instead of customizing the tasks? The original tasks should be harder because all the layouts (agent, goal and obstacles) are randomized in each episode and they can better test the ability of safety exploration.
- In the experiment, why are the performances of DDPG and DDPG-lag very similar in terms of reward or safety violation? DDPG does not take safety into the consideration and only aims to maximize the reward. The lagrangian in DDPG-lag will thus be almost useless if it performs similarly to DDPG.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a framework to address the problem of safety within unknown environments using a combination of techniques including shielding, contrastive learning and latent feature representations. The framework therefore consists of many components that have been combined under one roof. The target is so called black box environments where the benefit of information relating to safe states is not a priori available so special techniques need to be employed to enable training and execution to proceed as safely as possible. The empirical results show that the framework, ADVICE increases safety violations by a meaningful margin though often at the expense of return

### Strengths
The methodology is intuitive and the motivation and requirement of each component are reasonably well explained. The problem setting is one of significant interest to the RL community and the approach seems original.

### Weaknesses
Although some parts of the paper are well explained, especially the non-technical elements and the intuition of the algorithm, many important details are skipped. This leaves the reader to simply guess how important aspects of the framework work. Also, some maths expressions seem to have been written without due care which further adds to confusion. The framework involves various interdependent learning processes - specifically, in addition to the regular policy updates, the action and hence the reward received at a given state depends on the latent representation (which presumably is being updated) as well as the value of K which varies in quite an abrupt manner. This generates concerns about convergence guarantees and the numerical stability of the framework. The paper would benefit from some analysis or at least a discussion on this aspect. Additionally, within the framework there are a number of functions within the method that have max/min functions - this introduces a high level of discontinuity which can be harmful for some learning methods e.g. gradient-based learning methods, and may cause numerical instabilities.

The novelty of the paper as a whole could be more clearly spelled out. Lastly, although the framework achieves a significant reduction in safety, this often comes at a notable expense to the return. I would like to see how this compares to the frameworks that have some calibration aspect for the performance:safety ratio.

### Questions
1. In environments with a highly non-smooth reward function, similar features can induce very different rewards (specifically different levels of safety). What exactly is the function $h_\theta$ in (1)? If this function does not relate to safety or reward then the issue of non-smoothness in the safety w.r.t. features may be problematic here.

2. Given that $\mathcal{U},\mathcal{S},\mathcal{I}$ are defined as sets, the construction of $g$ in (3) does not seem like a function since it maps elements of $F_E$ to sets. Perhaps $\mathcal{U},\mathcal{S},\mathcal{I}$ need not be sets for this construction.

3. The construction of $\mathcal{C}$ in (4) also seems spurious since it maps a product of sets to a set which is the union of other sets. Also, it seems not to consider the cases of two dissimilar features in $U$ and secondly, two dissimilar features in $S. 

4. What are $S$ and $U$ in (4) - in page 3, the subindex of $f$ represents time, the indices $i,j \in S$ etc. in (4) therefore seem incorrect.

5. In relation to the construction of the function $g$ in (3), in the black box setting, how can we know which are accepting states?

6. In line 6 of the algorithm, how can we be sure that constructing an action by taking a cartesian product across action dimensions will produce a valid action in the environment? The set of valid actions may only be a subset of this product space e.g. a robot may not be able to lift both its feet off the ground simultaneously.

7. What is the definition of a safety violation - specifically, is there a notion of safety violation that can be used to detect such violations in black-box environments?

### Soundness
3

### Presentation
2

### Contribution
2
