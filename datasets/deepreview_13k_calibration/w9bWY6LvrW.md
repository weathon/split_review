# Marvel: Accelerating Safe Online Reinforcement Learning with Finetuned Offline Policy

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5

## Abstract
The high costs and risks involved in extensive environment interactions hinder the practical application of current online safe reinforcement learning (RL) methods. While offline safe RL addresses this by learning policies from static datasets, the performance therein is usually limited due to reliance on data quality and challenges with out-of-distribution (OOD) actions. Inspired by recent successes in offline-to-online (O2O) RL, it is crucial to explore whether offline safe RL can be leveraged to facilitate faster and safer online policy learning, a direction that has yet to be fully investigated. To fill this gap, we first demonstrate that naively applying existing O2O algorithms from standard RL would not work well in the safe RL setting due to two unique challenges: \emph{erroneous Q-estimations}, resulted from offline-online objective mismatch and offline cost sparsity, and \emph{Lagrangian mismatch}, resulted from difficulties in aligning Lagrange multipliers between offline and online policies. To address these challenges, we introduce \textbf{Marvel}, a novel framework for O2O safe RL, comprising two key components that work in concert: \emph{Value Pre-Alignment} to align the Q-functions with the underlying truth before online learning, and \emph{Adaptive PID Control} to effectively adjust the Lagrange multipliers during online  finetuning. Extensive experiments  demonstrate that Marvel significantly outperforms existing baselines in both reward maximization and safety constraint satisfaction. By introducing the first policy-finetuning based framework for O2O safe RL, which is compatible with many offline and online safe RL methods, our work has the great potential to advance the field towards more efficient and practical safe RL solutions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to solve two issues in offline-to-online safe RL, Q value estimation error and Lagragian multiplier mismatch, and proposes a new algorithm. The proposed method first re-trains Q function with an online objective to correct Q estimation and then uses an adaptive PID control to update Lagrangian multiplier. The authors run experiment on several safe RL tasks and claim their method outperforms other baselines.

### Strengths
- Offline-to-online method is important to the practical application of safe RL.
- The two challenges pointed out by this paper (i.e., Q value estimation error and Lagragian multiplier mismatch) are insightful.
- The experiment is extensive, and the proposed method outperforms the compared baseline.

### Weaknesses
 - Some concerns on VPA:
  - If you believe the pretrained Q functions from offline learning is not accurate, why not directly learn a new Q function by online objective or eq.(8)&(9) instead of training based on the pretrained Q functions? I believe it is a very straightforward baseline which should be compared. The paper does not adequately justify why fine-tuning a potentially flawed Q-function is superior to learning a new one from scratch using the online objective, especially given the limited online interaction steps. The concern is that the initial bias in the offline Q-function could hinder the learning process, and this needs to be explicitly addressed with a comparison to a from-scratch approach.
  - The error in Q value estimation is not only from the mismatch between offline and online learning objective, but also from the distribution shift issue due to the online policy update. Can the proposed method mitigate error from this aspect? While the paper claims that VPA mitigates distribution shift, it does not provide a strong argument for how VPA addresses the issue of the online policy moving the agent to out-of-distribution states. The method should explicitly discuss how the online policy's exploration affects the Q-function accuracy and how VPA handles this.

- Although the experiments show that adapative PID Lagrangian updater can stablize the cost performance, its effectiveness is still questionable. The adaptive PID introduces three more hyperparameters $\alpha, \beta, \gamma$. Along with original $K_p, K_i, K_d$, there are **six** hyperparameters for the updater in total. However, the adaptive PID only shows a marginal improvement over PID in fig.5. Meanwhile, the original hyperparameters of PID are not well tuned. The authors select $K_p=10^{-4}, K_i=10^{-5}, ...$, which are not only very different from the original PID Lagrangian paper [1], but also different from the recent safe RL benchmarks using PID update [2][3], which provide more stable performances of PID update than the reported one in fig.5. The paper needs to justify the hyperparameter choices for both PID and aPID, and provide a more thorough analysis of the performance gains of aPID over PID, given the increased complexity.

- The experiment results show that the proposed method outperforms other offline-to-online baselines or naively starting from offline policy. However, in the experiment, we can find those offline-to-online methods are even worse than purely online learning (i.e., learning from scratch). Therefore, I believe those baselines are not strong enough to illustrate the effectiveness of new method. Meanwhile, the performance of purely online learning is also significantly under-reported: SAC-Lag can quickly achieve ~700 reward with even smaller cost in Ballcircle according to [3]. It can also achieves > 2500 reward in Halfcheetach-velocity in [2]. The paper needs to include stronger baselines, including a direct comparison to online learning methods with similar interaction budgets, to better demonstrate the value of the proposed offline-to-online approach. The current results do not show a clear advantage over well-tuned online methods.

minor issues:
- I don't think PPO ("Schulman et al 2017", the first citation in line 93) is a safe RL algorithm, it is a standard RL algorithm.

### Questions
- What is the input to tSNE in fig.1(b)? Current caption is quite confusing, and I don't understand why the visualization shows cost is sparser.
- What are the $\mu$ and $\hat{Q}$ in eq.(8)?
- How do you get the true Q-values in table 1? E.g., what is the policy for MC simulation? how many simulations do you get for the Q computing? And are the state-action pairs for evaluation in "dataset" in table 1 the same as the VPA training dataset?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenges of safe RL by proposing Marvel, a framework that bridges offline and online RL to achieve safer and faster policy learning. Based on the authors’ claim, Marvel tackles these issues with two key components: Value Pre-Alignment, which adjusts Q-functions for accurate value estimation, and Adaptive PID Control, which optimizes Lagrange multipliers for balancing rewards and safety constraints during online fine-tuning. Experimental results show that Marvel outperforms presented baselines.

### Strengths
(1) Interesting topics: it focuses on an interesting topic: safety in reinforcement learning, specifically exploring offline-to-online adaptation to enable safer and more efficient policy learning—a crucial yet underexplored area in RL.

### Weaknesses
 (1) Typo: In Lines 413 and 414, the HalfCheetah, Hopper, and Swimmer in DSRL are from Safety-gymnasium [1], not Bullet-Safety-Gym.

(2) Confusion about experiment results: Why do the results of training-from-scratch look so poor? Based on the report [1], SAC-Lag should achieve 600+ rewards on Ball-Circle and 350+ rewards on Car-Circle.

(3) Concerns about the experiment results. The experiment results shown in Figure 6 indicate that the proposed method can not reach a reasonable reward. For example, in Drone-Circle, the agent should achieve a reward of 600+ using SAC-Lag. However, the proposed Marvel only achieves 150-.

### Questions
(1) Can you clarify what the x-axis “steps” means in Figure 1 and Figure 2? Does it mean the optimizer update times?

(2) Can you compare your method to pure offline safe RL baselines such as CDT [1] and pure online safe RL baselines such as PPO-Lag and SAC-Lag?

Reference:

[1] Zuxin Liu, et al. "Constrained decision transformer for offline safe reinforcement learning." International Conference on Machine Learning. PMLR, 2023.

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
3

### Summary
This paper focuses on offline-to-online (O2O) safe reinforcement learning (RL). It identifies two main issues causing inefficiency in previous methods: erroneous Q-estimations and Lagrangian mismatch. To address these issues, the authors propose two methods: Value Pre-Alignment and Adaptive PID Control. These methods aim to improve the standard O2O safe RL framework. Several experiments provide evidence of the effectiveness of these two components.

### Strengths
1. The explanatory experiments in the Method section really enhance the reader's understanding of the proposed methods. Improvements in the clarity of some figures could further aid in the visualization of the results.
  
2. The paper is well-written, with each part of the methods meticulously described and well-motivated, contributing to a coherent and comprehensive presentation of the research.

### Weaknesses
1. The algorithms and baselines lack stability in some environments. More repeated experiments may be needed. The improvement over baselines is not significant, showing performance gaps only in two tasks: BallCircle and CarCircle.
  
2. All figures need to be polished, especially Figure 3. The legend should not be limited to one or two figures but could be placed below all figures. Additionally, the lines representing each method should be improved, as it is difficult to distinguish between methods in some figures.

### Questions
1. How would the method perform if equipped with a large-scaled model, such as the structure of Guided Online Distillation?
  
2. How does aPID improve baselines, as the paper claims it can enhance their performance?

3. Could other types of O2O baselines be considered, such as Online Decision Transformers [1], which do not involve Q-functions?

4. What are the base algorithms for Warm Start?

5. A guide for hyperparameter settings would be beneficial, such as for $\alpha$ and $\alpha_c$. Is the method sensitive to these hyperparameters?

[1] Zheng Q, Zhang A, Grover A. Online decision transformer[C]//international conference on machine learning. PMLR, 2022: 27042-27059.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article systematically investigates the challenges of O2O (Offline-to-Online) in safe RL and proposes corresponding solutions. Specifically, the paper 1) employs value pre-alignment to counteract erroneous Q-estimations and 2) utilize adaptive PID control to overcome Lagrangian mismatch. The method introduced has demonstrated outstanding performance across datasets in DSRL.

### Strengths
1. The O2O in safe RL is a very important but overlooked issue. This paper systematically explores this issue.
2. The paper's writing logic is very clear, progressing methodically from problem analysis, to problem formulation, and finally to the solution. So the understanding is relatively easy.

### Weaknesses
1. This paper studies the problem of Offline to Online finetuning for safe RL. The first challenge can be viewed as a common issue in the O2O (Offline-to-Online) domain. The second challenge is unique to safe RL, but I question its significance. Figure 2 suggests that a good initialization of Lagrange multipliers is more conducive to ensuring a reasonable cost. However, even if the initial values of the Lagrange multipliers are not reasonable, they can be adjusted through Equation (3). The proposed aPID seems to merely expedite this adjustment process, as shown in Figure 5. In addition, all baselines involve aPID, but the performance is still poor. This also indicates that **challenge 2 is not crucial**.

2. Guided Online Distillation is an important baseline of this paper. Regarding the reason "its usage of large pretrained model leads to an unfair comparison with standard RL frameworks", I have some disagreements. Guided Online Distillation is based on decision transformer (DT). Despite having more parameters, DT is far away from a large model. Moreover, DT's performance on D4RL is typically weaker than that of standard RL algorithms, such as IQL.

### Questions
1. The meanings of 'Warm Start', 'From Stractch', and 'PID' are not clear in introduction, which makes the Figure 1 is hard to understand.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the warM-stArt safe Reinforcement learning with Value prE-aLignment (Marvel) framework, featuring Value Pre-alignment (VPA) and Adaptive PID Control (aPID). VPA aligns pretrained Q-functions with true Q-values using offline data, promoting active exploration while managing costs. aPID adjusts Lagrange multipliers based on cost violations, ensuring stable online learning. Marvel outperforms baselines, achieving safe, high-reward policies with a few online interactions, and is compatible with many state-of-the-art safe RL methods.

### Strengths
1. The motivation for offline-to-online safe RL is clear, focusing on using offline data to accelerate online fine-tuning and reduce risky interactions in safety-critical scenarios.
2. The design of the method appears reasonable, introducing two key components that seem well thought out.
3. The results seem to indicate better performance, with evaluations conducted across various robots and tasks.

### Weaknesses
1. The method lacks theoretical justification regarding sample efficiency, leaving it unclear how it enables more efficient online finetuning.
2. The evaluation results are unconvincing, with certain key comparisons missing.

3. The proposed method appears to perform poorly after the offline pre-training phase. As shown in Table 2, the method either struggles to satisfy the cost threshold (e.g., CarRun and AntCircle) or fails to achieve high rewards, with a significant gap compared to the rewards reported in DSRL. For instance, in the DSRL paper, the rewards for safe trajectories satisfying the cost threshold of 20 are reported as 250+ for AntCircle (compared to 4 in Table 2), 2500+ for HalfCheetah (113 in Table 2), and 1500+ for Hopper (62 in Table 2). This raises concerns about the claim that the method can 'quickly find a safe policy with the best reward using only a few online interactions.' While it is acceptable for an offline pre-trained policy to be sub-optimal, it should at least demonstrate sufficient performance to serve as a strong starting point for online fine-tuning.

4. Regarding the entropy terms in equations (8) and (9), if the cost values of state-action pairs where the policy has high entropy increase, the policy will likely be updated to avoid those state-action pairs during learning. This is because the overestimated cost values would lead to constraint violations (i.e., $\mathbb{E}[ \text{cost} ] \leq \text{cost threshold}$). Consequently, this could result in an overly conservative policy. It is unclear how this increased cost can 'encourage the agent to explore areas where the policy was uncertain after the offline phase,' and how it prevents the agent from becoming overly conservative during online fine-tuning.

5. Regarding the "true" Q-values in calculating Spearman’s rank correlation coefficient, the authors use the learned policy for MC simulation. However, typically, the "true" Q-values refer to the Q-values of the (unknown) behavior policy. It is unclear why the Q-values of the learned policy can represent the Q-values of the behavior policy.

### Questions
1. For Value Pre-Alignment, how do the entropy terms in equations (8) and (9) contribute to achieving the desired optimistic/pessimistic estimation of rewards/costs? Besides, when calculating Spearman’s rank correlation coefficient, how are the "true" Q-values obtained or estimated?
2. For adaptive PID, could the authors explain why the non-linearity, i.e., tanh, is applied only to $K_p$ rather than to all $K_p$, $K_i$, and $K_d$, given that the authors state that the non-linearity can help respond quickly to larger errors while avoiding frequent adjustments and reducing oscillations (lines 351-354)? Additionally, the aPID introduces several more hyperparameters, e.g., the initial $K_p$, $K_i$, $K_d$, and their respective minimum and maximum values; how are these hyperparameters selected in practice, and is the proposed method sensitive to variations in their values?
3. For evaluation of O2O offline RL methods[1, 2, 3], typically it involves first assessing the performance of the offline pretrained policy (e.g., rewards and costs), followed by online finetuning, and then evaluating the finetuned policy to observe performance changes. To strengthen the analysis, could the authors provide: \
 a) Performance metrics for the offline pretrained policies prior to fine-tuning. \
 b) Details on the online finetuning process, including the number of online interaction steps and the cumulative cost, e.g., Figure 2 in [4]. \
 c) Comparison of the finetuned policy performance with pure online safe RL methods. \
 d) Analysis of whether the proposed method achieves higher rewards with fewer constraint violations. \
[1] https://proceedings.mlr.press/v202/yu23k/yu23k.pdf \
[2] https://arxiv.org/pdf/2110.06169 \
[3] https://arxiv.org/pdf/2201.10070 \
[4] https://proceedings.mlr.press/v202/liu23l/liu23l.pdf

### Soundness
2

### Presentation
3

### Contribution
2
