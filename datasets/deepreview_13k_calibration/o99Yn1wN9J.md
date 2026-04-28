# Looking into User’s Long-term Interests through the Lens of Conservative Evidential Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 6, 8

## Abstract
Reinforcement learning (RL) provides an effective means to capture users' evolving preferences, leading to improved recommendation performance over time. However, existing RL approaches primarily rely on standard exploration strategies, which are less effective for a large item space with sparse reward signals given the limited interactions for most users. Therefore, they may not be able to learn the optimal policy that effectively captures user's evolving preferences and achieves the maximum expected reward over the long term. In this paper, we propose a novel evidential conservative Q-learning framework (ECQL) that learns an effective and conservative recommendation policy by integrating evidence-based uncertainty and conservative learning. ECQL conducts evidence-aware explorations to discover items that are located beyond current observations but reflect users' long-term interests. It offers an uncertainty-aware conservative view on policy evaluation to discourage deviating too much from users' current interests. Two central components of ECQL include a uniquely designed sequential state encoder and a novel conservative evidential-actor-critic (CEAC) module. The former generates the current state of the environment by aggregating historical information and a sliding window that contains the current user interactions as well as newly recommended items from RL exploration that may represent short and long-term interests respectively. The latter performs an evidence-based rating prediction by maximizing the conservative evidential Q-value and leverages an uncertainty-aware ranking score to explore the item space for a more diverse and valuable recommendation. Experiments on multiple real-world dynamic datasets demonstrate the state-of-the-art performance of ECQL and its capability to capture users' long-term interests.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper aims to tackle the exploration problem for RL4RS algorithms. The paper propose a evidential conservative Q-learning framework (ECQL) that models the uncertainty of samples by an evidential network. The paper also controls the degree of exploration by a conservative critic update. Experiments on 4 datasets validates that ECQL outperforms dynamic models, sequential models, deep-learning models, bandit models, and stoa RL-based models.

### Strengths
Originality: The paper studies the exploration problem for RL-based RS, which is novel. Also, the application of the evidential network to quantify the exploration bonus is novel.
Quality: The paper does detailed and sufficient experiments in both recommendation metrics and rl-based metrics such as NCIS. Recent RL-based methods are compared. The paper also provides case studies on ECQL and SAC, about the relevance and the exploration ability.
Clarity: The paper is well written and easy to follow.
Significance: The paper proposes a new algorithm to tackle the exploration problem for RL-based RS. I like the idea of controlling exploration by a conservative Q-learning updating mechanism.

### Weaknesses
1.The paper does not open-source their code.
2.The paper does not discuss or compare other exploration methods that are widely used in RL, such as ICM and RND.
3.Why do online RL methods perform well in the offline learning setting, such as SAC,HAC in Table 2?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a approach to recommenders which aims to capture users' long-term interests through reinforcement learning and evidential uncertainty. The authors propose ECQL to address limitations in existing recommender systems, particularly in capturing evolving user preferences and long-term interests. The framework integrates evidence-based uncertainty and conservative learning to develop a conservative recommendation policy.
ECQL employs a typical sequential state encoder that generates the current state of the environment by aggregating,
A sliding window containing current user interactions, older actions and a newly recommended items from RL exploration
This approach allows the model to represent both short-term and potential long-term user interests.
Another module seems to perform rating prediction by maximizing the conservative evidential Q-value

### Strengths
The experimental results seem to somewhat validate the approach

### Weaknesses
The paper is extremely dense written and difficult to follow, moreover the approach is over-engineered (see figure) . It is unclear what and by how much each component is contributing to the model. It is unclear if all these components are needed. Moreover the datasets used to not seem to have strong sequential behavioural patterns and the reliance on ratings makes the method somewhat irrelevant to modern recommender systems.

### Questions
I suggest the authors try and simplify both the method and the presentation of the work.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a framework called Conservative Evidential Q-Learning (ECQL), which aims to learn effective and robust recommendation strategies by combining evidential uncertainty with conservative learning. ECQL leverages evidence-based exploration to discover items that may lie beyond the current observation range but reflect users' long-term interests. By evaluating strategies from an uncertainty-driven conservative perspective, ECQL reduces the risk of recommending items that deviate excessively from users' current interests.The core components include a Sequential State Encoder, which combines users' historical information with a sliding window that encompasses both current interactions and new items recommended through reinforcement learning exploration, and a Conservative Evidential Actor-Critic Module, which maximizes conservative evidential Q-values to predict scores based on evidence and explores the item space using an uncertainty-based ranking score.Experimental results demonstrate that ECQL excels at capturing users' long-term interests, progressively recommending items that are not significantly different from users' current preferences. This maintains recommendation relevance even with sparse interactions.

### Strengths
This paper provides a highly detailed and well-structured presentation of its content. The problem statement is thoroughly explained, supported by experimental results that clearly validate the proposed framework's effectiveness. Each experimental result is precise and comprehensive. The theoretical derivations are carefully detailed, making it easier for readers to follow the logical flow and understand the underlying principles. In addition, the extensive experimentation reinforces the paper’s claims, offering solid evidence for the model’s advantages in capturing long-term user interests and providing stable recommendations. Overall, the combination of clear theoretical foundations with rigorous experimental validation makes this paper a valuable contribution to the field.

### Weaknesses
1. The abstract does not mention the motivation behind the proposed method, which might leave readers somewhat confused.

2. Introducing uncertainty into exploration strategies in reinforcement learning has already been extensively studied, so the novelty of this paper is not particularly outstanding.

3. The paper could benefit from adding some related work on the use of uncertainty in recommendation systems.

4. It would be helpful to experimentally verify whether the evidence network’s evidential score can serve as a plug-and-play component in an ε-greedy strategy to improve the performance of other RL4Rec methods.



### Questions
1. The motivation for introducing an uncertainty-aware exploration strategy is not clearly explained. The correspondence between the solution and the problem is unclear, and it doesn’t explain why uncertainty-aware exploration can effectively capture user’s evolving preferences and achieve the maximum expected reward over the long term, while existing methods cannot.

2. There is generally a balance between exploration diversity and accuracy performance. Further explanation is needed on how the proposed uncertainty-based exploration strategy reflects this balance.

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
4

### Summary
This paper proposes a model based on evidential conservative Q-learning for sequential recommendation. It integrates the evidential uncertainty into the rating scores to encourage exploration in reinforcement learning. Meanwhile, conservative regularization terms are added to avoid the over-optimistic estimation of the Q-values. Some theoretical analyses are given to justify proposed methods. Experiments on several datasets empirically validate the superior performance with compared baselines on certain metics.

### Strengths
1.	The studied problem is important. Building a model to pursue long-term reward while making efficient exploration and avoiding user dissatisfaction is a valuable and challenging topic for both academic and industry.
2.	Modeling the uncertainty by introducing vacuity of evidence is interesting and novel.
3.	Theoretical proofs are given to justify proposed methods, building connections between the evidential uncertainty and the conservative policy update.
4.	Empirical experimental results are promising, revealing superior performance over several baselines.

### Weaknesses
1.	Based on the definition in Eq. (2), it appears that the candidate item pool throughout the training iterations is restricted to items with which the user has interacted. This limitation may introduce inconsistencies between training and inference and lead to bias issues. Specifically, by only training on items a user has already interacted with, the model might not learn to effectively recommend novel items, which is a crucial aspect of a robust recommender system. This could lead to a situation where the model performs well on known items but fails to generalize to new items that could be of interest to the user.
2.	In Eq. (2), it says that 'Wt indexes the time step reached by the current sliding window.' I’m unclear about the definition of 'time step' and its correlation with the original appearance position of a recommended item. Furthermore, it appears that this down-weight term is absent from both their theoretical and experimental analyses, raising questions about its necessity and rationale. The lack of clarity on how this 'time step' is defined and used makes it difficult to assess the impact of this term on the model's performance. The absence of this term in the theoretical analysis further weakens the justification for its inclusion.
3.	It says that “During testing, for item i′ not appearing in user u’s interaction history Hu, a neutral rating ratingu, i′ = τ will be assigned to give neutral feedback”.  This will lead to complete overlook of all missing user-item interaction values, which can make the evaluation results highly biased on metrics except for NCIS. This approach effectively ignores the vast majority of potential user-item interactions, which are typically unobserved in real-world scenarios. This could lead to an overly optimistic evaluation of the model's performance, as it is not being tested on the full spectrum of possible recommendations.
4.	It's somewhat puzzling that a model optimized for long-term rewards can outperform state-of-the-art baselines, which are optimized for immediate rewards, on one-step metrics such as Precision and NDCG. This raises questions about the validity of using these one-step metrics to evaluate a model designed for long-term reward optimization. It also suggests that the model's performance on these metrics might not be a true reflection of its ability to achieve long-term goals.

### Questions
All my questions are listed in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
