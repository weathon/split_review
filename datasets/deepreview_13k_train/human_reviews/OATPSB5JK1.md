# Model-based Offline Reinforcement Learning with Lower Expectile Q-Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Model-based offline reinforcement learning (RL) is a compelling approach that addresses the challenge of learning from limited, static data by generating imaginary trajectories using learned models. However, these approaches often struggle with inaccurate value estimation from model rollouts. In this paper, we introduce a novel model-based offline RL method, Lower Expectile Q-learning (LEQ), which provides a low-bias model-based value estimation via lower expectile regression of $\lambda$-returns. Our empirical results show that LEQ significantly outperforms previous model-based offline RL methods on long-horizon tasks, such as the D4RL AntMaze tasks, matching or surpassing the performance of model-free approaches and sequence modeling approaches. Furthermore, LEQ matches the performance of state-of-the-art model-based and model-free methods in dense-reward environments across both state-based tasks (NeoRL and D4RL) and pixel-based tasks (V-D4RL), showing that LEQ works robustly across diverse domains. Our ablation studies demonstrate that lower expectile regression, $\lambda$-returns, and critic training on offline data are all crucial for LEQ.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a lower expectile Q-learning (LEQ) approach to address the overestimation issue in model-based offline RL. The LEQ loss assigns higher weight to lower Q-target values and lower weight to higher Q-target values. Through this training mechanism, LEQ achieves conservative value function estimation without the need for uncertainty estimation. Additionally, the authors introduce the $\lambda$-return as the Q-target and the policy update objective. Extensive experiments on offline RL tasks demonstrate that LEQ consistently outperforms previous baselines.

### Strengths
1. LEQ is a simple yet highly effective algorithm, easy to implement, and does not introduce significant computational complexity. It exhibits substantial performance advantages across a range of offline RL tasks.
2. Beyond its impressive performance improvements, the authors provide in-depth analysis of LEQ’s instability on several tasks, giving readers a comprehensive understanding of the algorithm and hinting at multiple future research directions.
3. The paper includes extensive performance comparisons and ablation studies, offering thorough insights into the contributions of each component of the algorithm.

### Weaknesses
I would greatly appreciate clarification on the following points:

1. Why did the authors choose to update the policy based on deterministic policy gradients? What considerations influenced this choice, and are there experimental differences between using a stochastic versus deterministic policy?
2. In Algorithm 1, the authors pretrain the policy with BC using the offline data, which is not typically done in algorithms like MOPO or MOBILE. How does BC pretraining impact the results, particularly in tasks like AntMaze?

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Lower Expectile Q-learning (LEQ), a novel model-based offline reinforcement learning method that utilizes lower expectile of Q values to avoid overestimation.  The success of LEQ is attributed to lower expectile regression, λ-returns, the lower expectile target for the policy training. LEQ significantly outperforms previous MBRL methods on long-horizon tasks and matches state-of-the-art model-free methods in various environments.

### Strengths
- The paper is well-written and easy to follow. The description to the thought of design and the algorithm is clear.
- The paper provides both experimental and theoretical analysis, which enhances the soundness of the lower expectile policy learning.
- The experiments are conducted on various types of tasks, including dense- and sparse-reward environments, along with state and image input formats, showing the effectiveness of LEQ.

### Weaknesses
See questions.

- I do not find any reference of Figure 2 in the paper. Could you please insert the figure into the proper place to better explain your method?
- How do you use the ensemble of world models for sampling? For example, do you randomly select one model for each step or for each rollout?
- For the experiments, though you include TT and TAC as baselines, I do not find any analysis of the related results. Could you please explain why to include TT and TAC, and provide what we can learn from comparing LEQ against them?
- In the proof of Theorem 1, it seems that the last inequality holds if $\mathbb{E}[W^\tau(Y>X)] \ge 1-\tau$. However, when $0<\tau \le 0.5$, we have $\tau \le W^\tau(\cdot) = |\tau - 1(\cdot)| \le 1-\tau$, so $\tau \le \mathbb{E}[W^\tau(\cdot)] \le 1-\tau$. As a result, the last inequality might be in the wrong direction.
- What is the difference between MBPO and Dyna training schemes, as you classify in Table 8? Previous works usually regard MBPO as a Dyna-style algorithm. For example, though you classify MOBILE into the MBPO style, MOBILE itself claims that "MOBILE is under the Dyna-style framework" and cite MBPO as a "Dyna-style model-based RL" method in Section 5 of its original paper[1].

### Questions
- I do not find any reference of Figure 2 in the paper. Could you please insert the figure into the proper place to better explain your method?
- How do you use the ensemble of world models for sampling? For example, do you randomly select one model for each step or for each rollout?
- For the experiments, though you include TT and TAC as baselines, I do not find any analysis of the related results. Could you please explain why to include TT and TAC, and provide what we can learn from comparing LEQ against them?
- In the proof of Theorem 1, it seems that the last inequality holds if $\mathbb{E}[W^\tau(Y>X)] \ge 1-\tau$. However, when $0<\tau \le 0.5$, we have $\tau \le W^\tau(\cdot) = |\tau - 1(\cdot)| \le 1-\tau$, so $\tau \le \mathbb{E}[W^\tau(\cdot)] \le 1-\tau$. As a result, the last inequality might be in the wrong direction.
- What is the difference between MBPO and Dyna training schemes, as you classify in Table 8? Previous works usually regard MBPO as a Dyna-style algorithm. For example, though you classify MOBILE into the MBPO style, MOBILE itself claims that "MOBILE is under the Dyna-style framework" and cite MBPO as a "Dyna-style model-based RL" method in Section 5 of its original paper[1].

[1] Model-Bellman Inconsistency for Model-based Offline Reinforcement Learning. Yihao Sun, Jiaji Zhang, Chengxing Jia, Haoxin Lin, Junyin Ye, Yang Yu. Proceedings of the 40th International Conference on Machine Learning, PMLR 202:33177-33194, 2023.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
To to address the uncertainty of model data $Q$ value estimation, the authors  introduce low expectile regression into the algorithm, and propose a novel model-based offline RL method. This method can achieve conservative estimation for model data and demonstrates superior performance across multiple datasets.

### Strengths
1) The article is well-written overall, with clear logic and a detailed introduction on how to incorporate low expectile regression into RL algorithm. The experiments are thorough, validating the algorithm's superiority across multiple datasets.

2) The methodology presented in the article is very intriguing. Unlike traditional value penalization methods, this paper innovatively employs low expectile regression to alleviate the issue of inaccurate model data estimation.

### Weaknesses
1) Theoretical: The article does not provide the theoretical analysis of how the use of low expectile regression impacts the final Q-values of the model data. Additionally, it does not offer theoretical guarantees for policy improvement , as seen in algorithms like COMBO and MOBILE.

2) Algorithm: The method presented in this paper directly scales the loss values of the overestimated model data by a factor of $\tau$, without considering the differences among the model data. For example, the scaling coefficient $\tau$ should vary depending on the degree of error in the model data.

### Questions
1) Does the addition of the third loss term in Eq. (7) affect final performance? The authors could provide simple experiments for analysis.

2) Why does the policy update use only the generated model data and not the precise offline data? Most model-based offline RL algorithms currently use accurate offline data to update policy.

3) Is there an error about the definition of $L_2^{\tau}$ in Eq. (1)? According to my understanding, in Eq. (4), $L_2^{\tau}(u)=\|\tau-\mathbb{I}(u>0)\|u^2$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel model-based offline reinforcement algorithm called Lower Expectile Q-Learning (LEQ). LEQ is similar to prior model-based offline RL algorithms with three main additions. 1) LEQ uses expectile regression for both critic and policy training, to obtain conservative Q-value estimates and actions respectively. 2) LEQ uses $\lambda$-returns for both critic and policy training. 3) The critic is trained with both model-generated and the provided offline data, while the actor is trained with only model-generated data. There are a number of other smaller additions, such as the use of EMA regularization when training the critic and some hyperparameter changes to prior work.

In summary, the approach is clearly explained, comprehensively evaluated and the components are individually studied. Therefore while none of the contributions of the paper are particularly novel or likely to have a major impact on the direction of the field, I believe the paper should be accepted due to the thoroughness of the work. LEQ will likely provide a strong general-purpose baseline for model-based offline RL in future work.

### Strengths
- **Clarity**
  - The method is clearly motivated and explained.
  - The results are clearly analyzed and summarized.
  - The paper is generally well-written and structured.
- **Quality and Comprehensiveness**
  - LEQ is comprehensively evaluated across a wide-range of benchmarks. The results are realistically strong all-around, and the authors do a good job of analyzing the strengths of the method. In particular, LEQ appears to perform better than the baselines (impressively both model-based and model-free) at long horizon tasks, such as the larger AntMaze environments.
  - The authors appear to do a good job of ensuring fair comparisons with a wide range of baselines.
  - There are extensive ablation studies to justify the method's contributions and design decisions.
- **Significance**
  - The quality of the work suggests that LEQ will provide a strong and computationally fast baseline for future work on offline RL.

### Weaknesses
 - **Significance**
  - None of the components of the model are particularly novel, and as a result, I wouldn't expect LEQ to be able to solve any problem that is not already solvable by existing offline RL algorithms. While the all-around improvement is of benefit to the community, this reduces the significance of the work.
  - Other insights such as the benefit of using $\lambda$-returns are generally well-established, and the improvements in hyperparameters are likely to be environment specific and therefore not very generalizable. 
  - While standard practice in offline RL, the use of differing hyperparameters per environment (specifically $\tau$, as provided in Table 10), also limits the significance and generality of the work. However, the results for all expectiles provided in the Appendix is helpful and appreciated.
- **Originality**
  - In addition to the novelty of the components, the use of expectile regression as used in IQL for model-free offline RL appears to have already been applied ot model-based offline RL in IQL-TD-MPC [1]. This method appears as a baseline for the AntMaze results, but does not appear in the other results (Tables 2,3,4) or in the Related Work. Given the apparent similarity in the approach, this method should be explained and distinguished in the paper's motivation/related work and ideally used as a baseline for all results. The citation for this method is also wrong in Section 5.3.

### Questions
- On line 256, the authors state "because of the expectile term ..., we cannot directly compute the gradient... thus we optimize the unnormalized version of the expectile". Please could the authors expand on this line? What is meant by the 'unnormalized' version of the expectile? Also, on line 258 the authors say they approximate the expectation with the learned Q-estimator in order to derive the surrogate loss. But then on line 266 they say the surrogate loss provides a better approximation than the Q-estimator, which naively seems contradictory (without going through Appendix B). Could the authors clarify this please?
- In Equation 7, can you confirm that $\beta$ and $\beta_{EMA}$ are independent hyperparameters? Assuming so, it would be less confusing to use a different symbol for $\beta_{EMA}$.
- Could you explain the main difference between LEQ and IQL-TD-MPC and include this in the paper?
- In Section 5, LEQ is compared with the baselines in terms of performance. It would also be helpful to have some comparison in terms of computational cost/run-time, as this is also an important aspect of these algorithms (and LEQ appears quite strong in this regard from the appendix). Could this be included?
- In Section 5.3, the authors discuss failed trajectories that attempt to pass through walls, and that 'this could be addressed by... improving the number of ensembles for the world models.' This is an interesting failure case, but I found this confusing as my understanding is that LEQ uses a single world model - is this the case? Do the authors have any hypothesis or evidence that using an ensemble would address this issue? 
- Similarly in Section 5.4, the authors discuss variance in performance during training due to optimistic prediction. Does a reduced value of $\tau$ in the expectile regression (more conservative estimates) address this issue?
- Section 6.1 on Limitations seems out of place at the end of the work. This seems more appropriate before the conclusion (ideally included as an additional ablation in 5.6 with a minimal termination predictor on one or two environments). Could this paragraph be moved before the conclusion?

### Soundness
3

### Presentation
3

### Contribution
2
