# AdaRec: Adaptive Sequential Recommendation for Reinforcing Long-term User Engagement

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Growing attention has been paid to Reinforcement Learning (RL) algorithms when optimizing long-term user engagement in sequential recommendation tasks. One challenge in large-scale online recommendation systems is the constant and complicated changes in users' behavior patterns, such as interaction rates and retention tendencies. When formulated as a Markov Decision Process (MDP), the dynamics and reward functions of the recommendation system are continuously affected by these changes. Existing RL algorithms for recommendation systems will suffer from distribution shift and struggle to adapt in such an MDP. In this paper, we introduce a novel paradigm called Adaptive Sequential Recommendation (AdaRec) to address this issue. AdaRec proposes a new distance-based representation loss to extract latent information from users' interaction trajectories. Such information reflects how RL policy fits to current user behavior patterns, and helps the policy to identify subtle changes in the recommendation system.
To make rapid adaptation to these changes, AdaRec encourages exploration with the idea of optimism under uncertainty. The exploration is further guarded by zero-order action optimization to ensure stable recommendation quality in complicated environments. We conduct extensive empirical analyses in both simulator-based and live sequential recommendation tasks, where AdaRec exhibits superior long-term performance compared to all baseline algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel paradigm to tackle the challenge of distribution shift in large-scale online recommendation systems. In these systems, the dynamics and reward functions are continuously affected by changes in user behavior patterns, making it difficult for existing reinforcement learning (RL) algorithms to adapt effectively.

AdaRec proposes a multi-faceted approach to address this issue. It introduces a distance-based representation loss, which extracts latent information from users' interaction trajectories. This information reflects how well the RL policy aligns with current user behavior patterns, allowing the policy to detect subtle changes in the recommendation system.

AdaRec's approach to addressing distribution shift in recommendation systems appears promising and aligns with current challenges in the field. The full paper's empirical results and detailed methodology will be necessary to assess the significance and practical applicability of this novel paradigm in real-world recommendation systems.

### Strengths
1. AdaRec introduces a novel paradigm for addressing distribution shift in large-scale online recommendation systems, which is a significant and challenging problem in the field.

2. The use of zero-order action optimization to ensure stable recommendation quality in complicated environments is a strong point, as it addresses the need for robustness in real-world recommendation systems.

3. The claim of superior long-term performance is supported by extensive empirical analyses in both simulator-based and live sequential recommendation tasks, indicating a commitment to evaluating the proposed solution rigorously.

### Weaknesses
1. The use of "optimism under uncertainty" and zero-order action optimization may introduce additional complexity to the approach, which could be a drawback in terms of implementation and computational cost.


### Questions
Does the computational cost of reinforcement learning need to be analyzed?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel paradigm called AdaRec to address the challenge of evolving user behavior patterns in large-scale online recommendation systems. The goal is to optimize long-term user engagement by leveraging Reinforcement Learning (RL) algorithms. By introducing a distance-based representation loss to extract latent information from users' interaction trajectories, AdaRec helps the RL policy identify subtle changes in the recommendation system. To enable rapid adaptation, AdaRec encourages exploration using the idea of optimism under uncertainty. It also incorporates zero-order action optimization to ensure stable recommendation quality in complex environments.

### Strengths
1. The problems studied in this paper exist widely in recommendation systems, and have been ignored by previous researchers, which is a very promising and important research direction.
2. The paper presents a distance-based representation loss to identify the subtle user behavior patterns changes, which is novel and interesting.
3. Extensive empirical analyses in simulator-based and live sequential recommendation tasks demonstrates that AdaRec outperforms baseline algorithms in terms of long-term performance.

### Weaknesses
1. The writing of the paper needs further improvement. 
(1)	What is the specific meaning of State Space S?
(2)	The paper should give a brief introduction before using some reinforcement learning concepts.
2. Although I agree with that the user behavior patterns are evolving in recommendation systems, the study in Section 3 does not make sense to me. At different time stamp, user interaction history statistics are different, that is, the distribution of states are different, so different interaction frequency may not reflect the change of user behavior patterns. There is no evidence to support the argument “As previously discussed, given the same distribution of states s_t and actions a_t, the users’ return time exhibits fluctuations across different weeks.” 
3. In reinforcement learning, there are many exploration strategies. What are the advantages of the schemes mentioned in the paper, and the comparison experiments with other schemes need to be provided.

### Questions
1. What is the specific meaning of State Space S?
2. The comparison experiments with other exploration schemes need to be provided.

### Soundness
2 fair

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
This paper studied the challenges of users’ complicated behavior changes in online recommendation systems. In different periods, users’ behaviors change in terms of preferences, return time and frequencies of immediate user feedback. To handle this challenge, the authors propose an adaptive sequential recommendation method to optimize long-term user engagement. Specifically, the authors utilize a context encoder to encode user’s behavior patterns and regularize the encoder to produce a similar latent representation for states with similar state values. An optimistic exploration is further utilized to encourage exploration. Experiments are carried out using a recommender simulator and an online A/B test.

### Strengths
1.	The paper is well-organized and easy to follow.
2.	Experiments are carried out on both a recommender simulator and an online A/B test, which is comprehensive.
3.	The authors conduct an ablation study to validate the effectiveness of each component.

### Weaknesses
1.  One major concern about the proposed method is the regularization loss in the proposed context encoder, which seems problematic to me. The motivation of this paper is to handle the distribution shift of the evolving user behavior patterns. However, encouraging states with similar state values to have similar latent encoding representation does not solve the distribution shift issues. The estimated state value function can still face the challenge of user behavior shift, resulting in an inaccurate state value estimation. Specifically, the regularization term seems to assume that similar state values imply similar underlying user behavior patterns, which is not necessarily true. Two states might have similar long-term values due to different reasons, and forcing their latent representations to be close might hinder the encoder's ability to capture the true dynamics of user behavior evolution. This could lead to a situation where the encoder fails to distinguish between different types of user behavior shifts, thus limiting the overall performance of the proposed method.

2.  Another major concern is the novelty of the proposed method. To my knowledge, using context encoder to encoder user behavior patterns is not new in the recommendation context, which is also discussed in the related work section. The novelty of adding regularization loss in the context encoder is limited. The adopted exploration mechanism from RL literature is rather general and it is unclear how it particularly handles the user exploration in the recommendation context, which usually involves large action space. The exploration strategy, while common in RL, doesn't seem tailored to the specific challenges of recommendation systems, such as the need to balance exploration with the risk of recommending irrelevant items and causing user disengagement. The paper does not provide sufficient justification for why a standard optimistic exploration method is suitable for this specific problem, especially considering the large action space and the potential for negative user experiences with overly exploratory recommendations.

3.  As this paper aims to handle the user behavior evolution challenge in the sequential recommendation setting, some baselines in the Non-RL recommender literature are missing such as [1, 2].

### Questions
See the Weaknesses for the questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
