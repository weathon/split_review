# Bayesian Offline-to-Online Reinforcement Learning : A Realist Approach

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Offline reinforcement learning (RL) is crucial for real-world applications where exploration can be costly. However, offline learned policies are often suboptimal and require online finetuning. In this paper, we tackle the fundamental dilemma of offline-to-online finetuning: if the agent remains pessimistic, it may fail to learn a better policy, while if it becomes optimistic directly, performance may suffer from a sudden drop. We show theoretically that the agent should adopt neither optimistic nor pessimistic policies during the offline-to-online transition. Instead, we propose a Bayesian approach, where the agent acts by sampling from its posterior and updates its belief accordingly. We demonstrate that such an agent can avoid a sudden performance drop while still being guaranteed to find the optimal policy. Based on our theoretical findings, we introduce a novel algorithm that outperforms existing benchmarks in our experiments, demonstrating the efficacy of our approach. Overall, the proposed approach provides a new perspective on offline-to-online finetuning that has the potential to enable more effective learning from offline data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use a Bayesian approach to balance exploration and exploitation in the offline-to-online RL domain. Theoretical analysis shows the regret of the proposed method. experimental results show good performance compared to some popular baselines.

### Strengths
see question part

### Weaknesses
The paper proposes to use a Bayesian method to balance exploration and exploitation to avoid performance drop. A distributional RL method is combined with the ensemble approach to do the Bayesian exploration. The theoretical analysis seems sound and the performance of the proposed method is good. However, I still have some concerns.
1. As we all know, the ensemble trick is helpful in improving the performance of RL methods and is widely used in practice. It seems that it is unfair to use an approach with the ensemble method to compare with other methods without the ensemble. I wondering if there is an ablation study to show the performance of an ensemble version of TD3 or TD3+BC. 

2. The key part of the algorithm is not clear. Specifically, the mask m samples from a distribution M. What is the format of M and how does it initialize and update? what is the difference between the usage of m compared to the original ensemble method? In the online part, it seems that the distribution M can be seen as the priori according definition of Bayesian. However, the authors choose to use uniform distribution to choose policy, which is the same as the original ensemble method. Could the authors explain it?

### Questions
The paper proposes to use a Bayesian method to balance exploration and exploitation to avoid performance drop. A distributional RL method is combined with the ensemble approach to do the Bayesian exploration. The theoretical analysis seems sound and the performance of the proposed method is good. However, I still have some concerns.
1. As we all know, the ensemble trick is helpful in improving the performance of RL methods and is widely used in practice. It seems that it is unfair to use an approach with the ensemble method to compare with other methods without the ensemble. I wondering if there is an ablation study to show the performance of an ensemble version of TD3 or TD3+BC. 

2. The key part of the algorithm is not clear. Specifically, the mask m samples from a distribution M. What is the format of M and how does it initialize and update? what is the difference between the usage of m compared to the original ensemble method? In the online part, it seems that the distribution M can be seen as the priori according definition of Bayesian. However, the authors choose to use uniform distribution to choose policy, which is the same as the original ensemble method. Could the authors explain it?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a streamlined approach to transitioning from offline to online reinforcement learning (RL) through posterior sampling, eliminating the need for explicit pessimism or optimism. An information-theoretic guarantee for regret is presented. For practical algorithms, in the offline phase, an ensemble of policies is trained with bootstrap mask; in the online phase, at each step a policy is sampled from the ensemble to perform actions, and the collected data is used to update each policy network in the ensemble. The proposed method demonstrates competitive performance when benchmarked against existing algorithms.

### Strengths
- The explicit identification of the finetuning dilemma in offline-to-online setting is commendable.
- The streamlined Bayesian formulation is novel.
- The information-theoretic analysis on the regret bound is mostly clear and easy-to-understand.

### Weaknesses
 - In Section 4's discussion of the replay buffer, the authors employ a symmetric sampling design, a technique previously proposed and validated in multiple prior works, e.g., [BSKL23] and [Ross et al., 2012]. It is essential to ensure that these references are comprehensively cited to acknowledge the contributions they provide and give readers a better context.
- It looks like the information ratio $\Gamma_t$ lacks of a formal definition in the paper. If so, please include this in the revision.
- Figure 2 / Appendix E: the experimental setting is slightly unclear. For UCB and LCB, what is the algorithm applied in the offline phase? Wouldn't a fair comparison for TS be using LCB at the offline phase and UCB at the online phase? The authors should also explicitly state the bandit setting (e.g., the distribution arm probabilities) for people to replicate the experiments.
- Line 4 of section 3.1: information pain --> information gain.
- Please include additional implementation specs for each experiment in the revision, e.g., the algorithm/approximation used for posterior updates, practical methods used for mutual information computation, etc.
- Why do ODT and Off2On have zero score on Antmaze tasks?
- The regret is for linear MDP. Could the author provide some discussion or proof sketch for the nonlinear case?
- A naive extension would be to use pessimistic TS (cf., [A23]) in the offline phase + optimistic TS (cf., [HZHS23]) in the online phase. Would the same analysis framework apply?

### Questions
Please address the concerns in the weakness part.   
I am happy to raise my score if the authors provide further feedback.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper prove a new algorithm for the offline to online RL problem by just running Thompson Sampling on both the offline and online stages. The theoretical algorithm shows that the algorithm has low Bayesian regret during the online stage, regardless of the coverage of the offline dataset. Based on the theory results, the paper proposes a practical version of the Thompson Sampling algorithm by bootstrapping from a distribution of the neural networks, and the experiments on the standard benchmarks indeed improves upon the previous algorithms in the same setting.

### Strengths
1. The paper performs an extensive comparison with relevant baselines, and the empirical results indeed demonstrate the proposed algorithm outperforms the other baselines. 

2. The paper also includes a thorough ablation study. 

3. The paper also includes a proof-of-concept experiment for the theory part, which better improve the credibility of the theory.

### Weaknesses
1. The presentation of the theory results could be improved. Some details are left out and some indication of the theory results could be better explained. For example, the theory algorithm that is used to give the results in Thm 3.2 (and generate the results of Fig. 2) is not given so it is a little bit hard to contextualize the results. Is the algorithm running TS-LCB in the offline stage and switch to TS in the online stage? It would be beneficial to explicitly state the algorithm used for the theoretical analysis, including how the posterior is updated and how the policy is derived from the posterior in both offline and online phases. The current description is too high-level to fully understand the theoretical implications.

2. From my understanding, the proposition 3.3 is trying to argue that using UCB in online stage will cause the performance drop? I am not sure that one-step suboptimality corresponds exactly to the "performance drop". The connection between one-step suboptimality and the observed performance drop in practice needs further clarification. It's not immediately clear why a single suboptimal step would necessarily lead to a significant drop in overall performance, especially considering that UCB has cumulative regret guarantees. A more detailed explanation of how this one-step suboptimality manifests as a practical performance issue is needed.

3. It would be helpful is any explanation why TS is performing better than theory in Fig. 2. The discrepancy between the empirical performance of Thompson Sampling and the theoretical bounds presented in Figure 2 raises questions about the tightness of the theoretical analysis. It would be valuable to discuss potential reasons for this gap, such as the specific choice of priors, the approximation errors introduced by the practical implementation, or the limitations of the theoretical assumptions. A more thorough discussion of these factors would improve the understanding of the results.

4. At the ending remark of the theory section, the paper mentions that [Song et al., 2022] benefits only when offline data has sufficient coverage, but to my best knowledge it seems that [Song et al., 2022] indeed requires and benefit from sufficient coverage from offline data. So to my understanding the current paper is achieving a best-of-both-world (kind of, not exactly) results of [Xie et al, 2021] and [Song et al., 2022]. The comparison with [Song et al., 2022] needs to be more precise. While the paper claims to achieve a best-of-both-worlds result, the exact conditions under which this is true need to be clearly stated. The current description is somewhat vague and could be misleading without a more rigorous comparison of the assumptions and guarantees of the different methods.

5. The current coverage is not the tightest in the linear case. Is the tightest coverage (as in [1]) applicable in the current analysis? It is unclear whether the analysis can be extended to incorporate tighter coverage notions, such as those used in [1]. The paper should discuss the limitations of the current coverage notion and whether the theoretical results can be improved by using a tighter coverage notion.

6. Some indexing on $h$ seems to be off in eq 3. Also in eq 4, are the linear features not $h$-dependent? The indexing issue in equation 3 needs to be addressed. Additionally, the assumption of $h$-independent linear features in equation 4 should be clarified. It's not clear if this is a limitation of the analysis or if it can be generalized to $h$-dependent features. A discussion of the implications of this assumption is needed.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of fine-tuning pre-trained offline Reinforcement Learning (RL) agents. Specifically, the study introduces a Bayesian approach called BOORL, where the dataset is treated as priors and online interactions are utilized to update posteriors. By sampling actions from these posteriors, this method effectively avoids excessive optimism or pessimism in off-to-on settings. Experimental results on the D4RL benchmark demonstrate that BOORL outperforms other baseline methods.

### Strengths
- This paper provides a theoretical analysis in linear MDPs under the offline-to-online settings.
- The motivation and main idea of the proposed method are reasonable and interesting.
- This writing is clear and easy to follow.
- The proposed method outperforms previous baselines in the experiments.

### Weaknesses
 - Experiments were solely performed on the less challenging locomotion tasks. Obtaining results from the more demanding antmaze tasks would provide stronger evidence.
- The performance of PEX significantly deviates from the original results and my personal experience, indicating a potential bug in the code or suboptimal parameter tuning.
- The legend in Figure 2 can be put to the top of two images to avoid overlapping with the curves.

### Questions
- There are some missing SOTA baselines for offline-to-online fine-tuning in the experiments: Reincarnating RL [1] and InAC [2]. Moreover, the current results of PEX seems to be problematic.

- In Figure 5, the three curves usually have the same starting points except for "hopper-medium-replay-v2", "walker-medium-replay-v2", and "halfcheetah-medium-expert-v2". Why does BOORL have a different value at step 0 in these tasks?

[1] (Agarwal et al., NeurIPS' 22) Reincarnating reinforcement learning: Reusing prior computation to accelerate progress

[2] (Xiao et al., ICLR' 23) The In-Sample Softmax for Offline Reinforcement Learning

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
