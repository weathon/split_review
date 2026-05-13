# Offline Imitation Learning without Auxiliary High-quality Behavior Data

- Decision: Reject
- Scores: 6, 8, 5, 6

## Abstract
In this work, we study the problem of Offline Imitation Learning (OIL), where an agent aims to learn from the demonstrations composed of expert behaviors and sub-optimal behaviors without additional online environment interactions. Previous studies typically assume that there is high-quality behavioral data mixed in the auxiliary offline data and seriously degrades when only low-quality data from an off-policy distribution is available. In this work, we break through the bottleneck of OIL relying on auxiliary high-quality behavior data and make the first attempt to demonstrate that low-quality data is also helpful for OIL. Specifically, we utilize the transition information from offline data to maximize the policy transition probability towards expert-observed states. This guidance can improve long-term returns on states that are not observed by experts when reward signals are not available, ultimately enabling imitation learning to benefit from low-quality data. We instantiate our proposition in a simple but effective algorithm, Behavioral Cloning with Dynamic Programming (BCDP), which involves executing behavioral cloning on the expert data and dynamic programming on the unlabeled offline data respectively. In the experiments on benchmark tasks, unlike most existing offline imitation learning methods that do not utilize low-quality data sufficiently, our BCDP algorithm can still achieve an average performance gain of more than 40\% even when the offline data is purely random exploration.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of Offline Imitation Learning (OIL), where an agent learns from both expert and sub-optimal demonstrations without further online interactions. Traditional studies in this domain rely heavily on high-quality behavioral data and falter when only low-quality, off-policy data is available. This research challenges that norm, asserting that even low-quality data can be beneficial for OIL. The authors propose a method that uses transition information from offline data to guide the policy towards states observed by experts, especially when reward signals are absent. They introduce an algorithm called Behavioral Cloning with Dynamic Programming (BCDP) that applies behavioral cloning to expert data and dynamic programming to unlabeled offline data. In tests, the BCDP algorithm outperforms many existing methods, showing a performance boost of over 40% even with purely random offline data.

### Strengths
The research presents a fresh perspective on offline imitation learning by challenging the conventional reliance on high-quality auxiliary data. Instead of seeing low-quality, off-policy data as a limitation, the authors innovatively harness its transition information to optimize objectives in states not observed by experts. The introduction of the BCDP algorithm, which combines behavioral cloning and dynamic programming, further underscores the paper's originality.

The quality of the research is evident in its comprehensive approach to the problem. Not only does the paper identify the challenge with low-quality auxiliary data, but it also offers a robust solution in the form of the BCDP algorithm. The empirical validation, where BCDP achieves state-of-the-art results on the D4RL benchmark across 14 tasks, attests to the method's efficacy and the overall quality of the research.

The paper lucidly articulates the challenges associated with offline imitation learning and the potential of low-quality data. The proposed BCDP algorithm is presented with clarity, making its methodology and implications easily understandable.

The research holds significant importance in the domain of imitation learning. By demonstrating that low-quality behavior data can be effectively leveraged, the paper breaks away from the traditional behavior quality assumption of auxiliary data, broadening the horizons of offline imitation learning. The potential extensions of BCDP, such as integrating it with model-based methods and addressing the existing imitation gap, highlight the paper's foundational contribution and its potential to pave the way for future advancements in the field.

### Weaknesses
The explanations for the experiment results, especially about the performance of BCDP, need more details.

One minor issue:
1. Table 1: the second-best result is not underlined.

### Questions
From Table 1, we can observe that BCDP performs very well for random or low-quality data. But when more expert knowledge is included, BCDP has inferior results than others. So, please
1. provide more details about the datasets, especially about the quality comparison regarding the experts.
2. explain why BCDP has less effective performance for non-random and human datasets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an effective use of low-quality offline data for off-policy imitation learning. They propose BCDP, which essentially does BC on the expert data while minimizing a SQIL-like Q-learning loss on both the expert data and offline data. This is similar to TD3+BC, where BC is used to provide some form of closeness to the offline data while TD3 maximizes an RL objective when rewards are present in the dataset. Experiments across multiple domains in the D4RL benchmark suite shows that BCDP outperforms other model-free offline IL baselines.

### Strengths
First of all, the paper's performance curves are very solid, especially for long-term return environments where the sparse reward used by BCDP could hamper learning. The experimental setup is pretty solid and covers all bases across the D4RL benchmark, with notable good results in sparse reward domains and domains with very low-quality offline data, such as datasets collected by random agents.

The paper was also well written and easy to follow. The graphs were somewhat unusual to see on an RL paper, but relevant in the context of what the paper is trying to show. It was easy to understand the author's reasoning throughout the paper.

### Weaknesses
There are some missing citations I think: for example, there has been some work on the model-based side with offline imitation learning, but with the assumption that the offline data has coverage over the expert traces in the state space [1]. This is reminiscent of what this paper's algorithm does, where the Q-learning update happens across a union of an expert batch and an offline batch.

There was also a paper where behavioral cloning combined with RL has been used in autonomous driving [2], which does something similar to what this paper does, but in the online setting. This is very similar to TD3+BC though, and therefore it may not be a really big weakness to not cite this.

### Questions
I didn't really have any big questions on this paper -- very solid!

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of Offline Imitation Learning (OIL) in the absence of auxiliary high quality data samples. Towards this goal, authors propose Behavior Cloning with Dynamic Programming (BCDP) which maximizes probability of transition to expert-observed states. BCDP abstracts data quality from IL by implementing BC on expert data samples and DP on unlabeled offline data samples. Practically, BCDP incorporates the TD3 algorithm wherein DP is carried out over value functions using the Bellman equation formulation. Empirical evaluation on a range of tasks demonstrates competitive performance to IL baselines.

### Strengths
* The paper is well organized.
* Experiments carried out by authors are sufficient.

### Weaknesses
 * **Motivation:** While the paper aims to leverage low-quality data samples, its motivation for the same is unclear. Instead of highlighting the algorithmic design choices, authors focus on the split of datasets. This corresponds to implementing offline RL on only a subset of data samples. For instance, Section 1 and Figure 1 do not motivate the need for an expert-specific dataset split. Moreover, it is unclear as to what conclusions can be drawn from Figure 1. Authors should explain the task definition, complexity of task completion, number of trajectories, number of samples in each trajectory for the BC expert and the ratio of expert to non-expert data split.
* **Practical Implementation:** While the work combines offline IL with DP, it leads to the well-established and pre-existing paradigm of offline RL. Practical implementation of BCDP presented in Section 3.2 is akin to applying offline RL on a different dataset split. As the authors note, BCDP is a special case of TD3+BC. However, its differences from TD3+BC or other offline RL algorithms remain unclear. The core mechanism of BCDP, which involves using Bellman updates to propagate value estimates, is fundamentally the same as in standard off-policy RL algorithms, raising questions about its novelty. The paper does not adequately explain how the specific combination of BC and DP in BCDP leads to unique advantages over existing methods.
* **Choice of Baselines:** While the authors state that their approach is similar to TD3+BC and offline RL, BCDP is not compared to these methods. Authors claim that "they have selected TD3+BC as our most similar offline RL algorithm, which allows it to be considered as an ablation study for our approach". However, an abaltion study of TD3+BC with BCDP is missing. It would be worthwile to compare BCDP with TD3+BC or a conservative algorithm such as CQL. This would help evaluate the utility of BCDP with established offline RL methods. The lack of direct comparisons against relevant offline RL algorithms such as CQL and BEAR makes it difficult to assess the true contribution of BCDP.
* **OOD Evaluation:** The requirement and intuition behind DRG metric is unclear. From my understanding, DRG is a state occupancy measure based on agent's visitation towards particular states. Hence, it does not quantify the policy's performance at test time (as per Q3). A positive DRG does not indicate how the agent performed on unobserved states. It only indicates that the agent successfully evaded unobserved states. This leaves Q3 unanswered. In order to evaluate OOD performance, authors could use standard methods/metrics. For instance, BCDP could be evaluated on a set of heldout states or initialized in a new state (or random seed). Similarly, authors could measure the confidence of agent by assessing the probability of actions taken in unobserved states. The reliance on DRG as a primary metric for OOD performance is not sufficiently justified, and the paper lacks a clear definition of what constitutes an 'unobserved state' in the context of the experiments.
* **Writing and Presentation:** In general, writing and presentation should be refined. Sentences and verbs could be made complete and grammatical errors could be reduced. Authors should also provide the missing ablations of TD3+BC and clearly explain what they wish to observe from Q3.

### Questions
* Can you please explain the task definition and setting of Figure 1? How many trajectories are present in the dataset? How many samples are present per trajectory? What is the ratio of expert to non-expert data samples?
* How is BCDP different from TD3+BC? What would be the potential advantages of using BCDP over TD3+BC with expert demonstrations? How does BCDP compare to TD3+BC?
* How does BCDP compar to existing offline RL methods such as CQL, BEAR, BRAC or IQL?
* What does DRG indicate? How does DRG quantify the performance of policy in unobserved states? Can BCDP be evaluated on a set of heldout states or new random seeds? Does the agent present high confidence in its actions on unobserved states?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes BCDP, a method for offline imitation learning with low-quality behavior data from which good policy cannot be directly extracted. The idea is simple: mimic expert on expert state, and reach expert state as frequently as possible when the agent is off the expert trajectory. Inspired by TD3+BC, BCDP designs an auxiliary reward that is 1 on expert state and 0 on non-expert state, and maximize a weighted sum of log likelihood on the expert dataset and auxiliary reward over the union of expert and non-expert dataset. On several testbeds with low-quality (e.g. random) auxiliary dataset, BCDP outperforms many offline imitation learning methods.

### Strengths
1. The paper answers a timely and interesting question of today's offline Imitation Learning (IL) community on how to utilize low-quality auxiliary data, which is not well-addressed by prior work and useful in real-life applications.

2. The idea proposed by the paper is sound and simple, and is backed up by theoretical lower bound of performance and experiment results with ablation.

### Weaknesses
 **1. The reward design seems to be too strict.** Currently, judging from section 3.2, the reward for a state-action pair is 1 if and only if the state-action pair belongs to the expert dataset. However, with continuous state/action space and low quality auxiliary dataset, it is very likely that none of the state-action pairs in $D^O$ has a reward of 1 - and with pertubation in the continuous environment, it is even likely that every state appear in $D^O\cup D^E$ is unique and no state in the auxiliary dataset $D^O$ lead to any reward. In such case, the optimization relies on the smoothing effect of the critic network. Thus, I suggest to add an ablation on replacing the current, identical reward with the discriminator used in prior work such as DWBC, ORIL or DemoDICE.  Furthermore, the current reward design does not explicitly encourage the agent to reach *unseen* expert states, which might be crucial for generalization, especially in sparse reward environments. The binary reward provides no gradient information for states that are not in the expert dataset, potentially hindering exploration towards the expert's state distribution. A more nuanced reward function, such as one based on a distance metric to the expert states or a learned discriminator, could provide a smoother gradient and encourage the agent to explore states that are close to the expert's trajectory, rather than only focusing on exact matches. 

**2. The hyperparameter is not specified, and some auxiliary plots are missing.** Currently, the value of some important hyperparameters are missing, e.g., weight for maximizing Q in the objective, network architecture, learning rate, number of steps to update, frequency of updating with policy gradient from critic. Also, the paper does not include learning curves. The absence of these details makes it difficult to reproduce the results and assess the sensitivity of the method to different hyperparameter settings. Furthermore, the lack of learning curves makes it challenging to understand the training dynamics and convergence behavior of the proposed algorithm. Including these curves would provide valuable insights into the stability and efficiency of the learning process.

3. I encourage the authors to include discussion on the **limitation of the current work.**

### Questions
I have two question apart from those listed in the weakness: 

1. How does the method perform compared to model-based imitation learning method (e.g., [1, 2, 3])? It might be hard to extract useful policy from low-quality behavior data, but those data could be useful for building up dynamic models, and thus help model-based methods.    

2. Why is policy gradient with respect to Q function updated only every d steps? intuitively, updating it every step with a smaller coefficient would make the gradient descent process smoother. 

**References**

[1] W. Zhang et al. Discriminator-Guided Model-Based Offline Imitation Learning. In CoRL, 2022.

[2] A. Hu et al. Model-Based Imitation Learning for Urban Driving. In NeurIPS, 2022.

[3] R. Kidambi et al. MobILE: Model-Based Imitation Learning From Observation Alone. In NeurIPS, 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
