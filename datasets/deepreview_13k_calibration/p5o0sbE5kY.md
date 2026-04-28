# Pretraining A Shared Q-Network for Data Efficient Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Offline reinforcement learning (RL) aims to learn a policy from a static dataset without further interactions with the environment. Collecting sufficiently large datasets for offline RL is exhausting since this data collection requires colossus interactions with environments and becomes tricky when the interaction with the environment is restricted. Hence, how an agent learns the best policy with a minimal static dataset is a crucial issue in offline RL, similar to the sample efficiency problem in online RL. In this paper, we propose a simple yet effective plug-and-play pretraining method to initialize a feature of a $Q$-network to enhance data efficiency in offline RL. Specifically, we introduce a shared $Q$-network structure that outputs predictions of the next state and $Q$-value. We pretrain the shared $Q$-network through a supervised regression task that predicts a next state and trains the shared $Q$-network using diverse offline RL methods. Through extensive experiments, we empirically demonstrate that the proposed method enhances the performance of existing popular offline RL methods on the D4RL and Robomimic benchmarks, with an average improvement of 135.94\% on the D4RL benchmark. Furthermore, we show that the proposed method significantly boosts data-efficient offline RL across various data qualities and data distributions. Notably, our method adapted with only 10\% of the dataset outperforms standard algorithms even with full datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a pretraining method for Offline RL. The method first pre-trains the Q-function to predict the forward dynamics of task based on a static dataset. The pre-train Q-function is then used as initilzation for standard offline RL training. The authors validate their proposed method across multiple offline RL benchmarks and baselines.

### Strengths
- The paper presents extensive experimental results of the proposed methods on both offline and online RL across multiple benchmarks and baselines that validates the effectiveness of the proposed method.
- The presented result is quite flexible and can be easily plugged into most offline/online RL methods.

### Weaknesses
 - The writing of the paper can be improved. There are some awkwardly written sentences (line 99 "..ability of an offline RL algorithm whether an agent can learn the desired policy...") and inconsistent switching between active and passive voice (line 192 "...underlying insights behind the proposed method are discussed", line 356 "The learning curves of TD3+BD are illustrated in Figure 3...", etc) that makes the paper hard to read.
- In Section 5.1, It not entirely clear to me what the authors mean by "pretraining ratios". Is the ratio of the amount of data used for pretraining or ratio of the total training time for pretraining?

### Questions
- The proposed method bares some similarities to Model-based RL methods as the paper proposed to first pretrain on the environments forward dynamics within the Q-function which is similar to how Model-based RL methods learn a seperate model to model the transition dynamics of the environment. Do the authors see any benefit/trade-offs in learning the dynamics within the Q-function itself vs learning the dynamics model seperately?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors focus on the problem of data-efficient offline reinforcement learning. To this end, they propose a very simple approach to improve downstream performance via pre-training. They utilize a Q-network with shared weights in addition to a future state prediction task on offline data. They provide mathematical justification for their approach and then evaluate their approach extensively with a number of other offline baselines on multiple datasets (D4RL, Robomimic). They show a quantitative margin of improvement in most settings.

### Strengths
1. The approach is very simple. It's largely just regression on future states.

2. Experimental evaluation is extensive with multiple environments used as well as multiple baselines for ablation.

3. Quantitative results are strong. The margin of performance over baselines shows promise.

### Weaknesses
1. This approach seems to be very similar to previous works which forecast future state information. For example, Self Predictive Representations (Schwarzer et al. 2020) and Predictive Belief Representations (Guo et al. 2018) predict future state information to improve performance of RL-trained agents.

2. There are some issues with presentation in the paper. For example, in Table 2, it appears that some of the baseline numbers are omitted (such as Expert IQL).

### Questions
1. Could you please elaborate on the novelty of the approach over previous similar work? How is this approach distinct from some of the papers mentioned above?

2. Could you clarify some of the omitted numbers in Table 2?

### Soundness
3

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
4

### Summary
The paper proposes using a dynamic loss to pre-train Q-networks, aiming to improve sample efficiency and performance in offline reinforcement learning. A large number of experiments have proved the effectiveness of the algorithm, regardless of the data collection strategies.

### Strengths
1. The paper structure is clear and easy to follow.
2. The proposed algorithm is simple and effective, although this simplicity raises some concerns (see weakness 1).
3. The experimental evaluation is comprehensive.

### Weaknesses
1. The proposed method appears overly simplistic and lacks novelty. Similar architectures, such as TD-MPC series [1,2] and JOWA [3], also use a shared backbone network to train both dynamics models and value functions, and the latter also pre-trains the backbone using dynamic loss for initialization. The analysis section is largely qualitative while occupies a disproportionate amount of space. Additionally, the relationship between rank and matrix infinity norm is unclear, as is the claim that higher rank is more likely to reduce error (line 257).

2. The absence of comparisons with offline model-based RL algorithms is a significant oversight. Given that the proposed method uses a pre-training approach similar to model-based methods and offline model-based RL also aims to improve data-efficiency, comparisons with algorithms such as MoRel [4], MOPO [5], COMBO [6], and RAMBO [7] would be highly relevant. I recommend including at least two offline model-based RL algorithms in the comparisons to ensure fairness and comprehensiveness.

3. Directly extracting AWAC and CQL algorithm results from the TD3+BC paper in Table 2 is inappropriate. I suggest either using results from the original papers of these algorithms or, preferably, reproducing the experiments. The reported results for AWAC and CQL appear to be significantly lower than those from a reputable offline RL algorithm library [8].

4. Obviously, the authors are not the first to raise the problem of data efficiency in the offline RL field (line 501). In addition to offline model-based RL, many other works [9,10,11] have also studied the problem of data efficiency, experimenting on datasets with different downsampling rates.

### Questions
1. The paper mentions "supervised learning domain (Chebotar et al., 2023 ...)" in reference to Q-former. However, doesn't Q-former use TD-learning, which falls under the RL domain rather than supervised learning?

2. Could you clarify what "pretraining ratios" (line 362) refers to? Is it the ratio of pre-training steps to total training steps?

3. In some cases (e.g., Figure 8 SMM), increasing the data amount leads to a decrease in offline RL performance. Could you provide a qualitative explanation for this phenomenon?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a method to enhance data efficiency in offline RL by incorporating a pre-training phase, during which the encoded features are used to predict the features of the next state. The paper analyzes why the learned features are well-suited for subsequent RL training and demonstrates performance gains when integrating this pre-training phase with state-of-the-art offline RL methods.

### Strengths
1) The paper tries to propose a theoretical analysis on the reason why such a predictive pre-training phase helps.
2) A comprehensive experimental analysis is provided

### Weaknesses
1) The concept of learning a predictive representation for RL is not new.
For example, previous papers [Schwarzer et al., 2020, 2021, Hafner et al., 2024] have leveraged predictive representation for RL and demonstrated improved sample efficiency with this approach.
The primary difference between this paper and the papers mentioned above is the evaluation setting:
the proposed method is evaluated under an offline RL setting.
Are there any other key differences I may have overlooked?
2) The analysis of the effect of predictive pre-training is somewhat unclear to me.
If I understand correctly, the logic behind the analysis is as follows:
predictive pre-training $\rightarrow$ high rank feature space $\rightarrow$ smaller error between $C(H_\phi)$ and $Q^\pi$ $\rightarrow$ smaller error between $Q^\pi$ and $Q_{\phi, \theta}$.
- For the first implication, empirical results are presented, but a theoretical analysis is missing.
- Could you provide an explanation for the second implication? A clearer explanation or proof for why a higher rank feature space leads to smaller error would be helpful.
- Could you give a more explicit derivation of how Equation 5 supports the final implication?

I believe the analysis would benefit from greater coherence throughout, which would strengthen the paper.

- M. Schwarzer, A. Anand, R. Goel, R. D. Hjelm, A. C. Courville, and P. Bach-
man. Data-efficient reinforcement learning with self-predictive representa-
tions. In International Conference on Learning Representations, 2020.
- M. Schwarzer, N. Rajkumar, M. Noukhovitch, A. Anand, L. Charlin, D. Hjelm,
P. Bachman, and A. Courville. Pretraining representations for data-efficient
reinforcement learning. In Conference on Neural Information Processing Systems, 2021
- D. Hafner, J. Pasukonis, J. Ba, and T. Lillicrap. Mastering diverse domains
through world models, 2024. URL https://arxiv.org/abs/2301.04104.

### Questions
1) Is the encoder fixed after the pre-training or not?
Which one is better?
2) Could you explain more about the percentage ratio/percentage rate (line 362)? 
Is the training set separated into two parts?
For example, 5% data is used for pre-training the representation and the other data is used for RL training.

### Soundness
3

### Presentation
3

### Contribution
2
