# BDQL: Offline RL via Behavior Diffusion Q-learning without Policy Constraint

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Offline reinforcement learning (RL) algorithms often constrain the policy or regularize the value function within an off-policy actor-critic framework to overcome the overestimation on out-of-distribution (OOD) actions.
And the on-policy style offline algorithms also cannot escape from these constraints (or regularization). 
In this paper, we propose an on-policy style algorithm, Behavior Diffusion Q-Learning (BDQL), which has the potential to solve offline RL without introducing any potential constraints.
BDQL first recovers the behavior policy through the diffusion model and then updates this diffusion-based behavior policy using the behavior Q-function learned by SARSA.
The update of BDQL exhibits a special two-stage pattern. 
At the beginning of the training, thanks to the precise modeling of the diffusion model, the on-policy guidance of the behavior Q-function over the behavior policy is effective enough to solve the offline RL.
As training processes, BDQL suffers from the OOD issue, causing the training fluctuation or even collapse.
Consequently, OOD issue arises after BDQL solves the offline problem which means the policy constraint is not necessary for solving offline RL in BDQL. 
Although the policy constraint can overcome the OOD issue and then completely address the training fluctuation, it also has a negative impact on solving the offline problem in the first stage. 
Therefore, we introduce the stochastic weight averaging (SWA) to mitigate the training fluctuation without affecting the offline solution. 
Experiments on D4RL demonstrate the special two-stage training phenomenon, where the first stage does have the capability to solve offline RL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The current paper introduces a new offline RL algorithm using diffusion models for policy, named BDQL. The algorithm has three components: 1. it performs behavior cloning on the offline dataset, 2. critic learning by SARSA on the offline dataset, 3. policy improvement by deterministic policy gradient with the critic trained by SARSA, and stabilizing training with stochastic weight averaging. In the experiment, the paper compares BDQL with several baselines on the d4rl benchmark.

### Strengths
1. The paper lists important preliminaries so even readers who are not familiar with diffusion models can understand the context. 

2. The ablation study is throughout. 

3. The experiment compares with a variety of baselines.

### Weaknesses
1. The significance of section 2.2 is unclear, since both methods are not used in the current paper. 

2. The SARSA update requires the assumption that the offline data is coming from trajectories, and the data collecting policy is a single stationary policy. Specifically, the standard SARSA update relies on sequential transitions within a trajectory, which is not guaranteed in a general offline dataset. The assumption of a single stationary policy is also restrictive, as many real-world datasets are collected by multiple policies or non-stationary policies.

3. The choice of using SARSA to train the critic is actually confusing. According to the proposed algorithm, in the statistically asymptotical case, optimization is done perfectly, and offline data has good coverage, the critic will converge to the Q-function of the behavior policy, which might not be a strong policy, and the diffusion policy is just the argmax policy according to the Q-function of the behavior policy, which might be better than the behavior policy, but the performance is still not guaranteed. So it is hard to see why even in the most ideal setting this algorithm would return a strong policy. The algorithm essentially learns a policy that is at best as good as the behavior policy, and it is not clear how this can lead to performance improvements over the behavior policy, especially in the context of offline RL where the goal is to learn a policy that is better than the behavior policy.

4. The argument on regularization for ood from the current algorithm is not very convincing. It seems like an alternative way of regulizing with behavior cloning with a diminishing regularization coefficient. Using this perspective, one can also suspect if this varying objective is causing the instability in the practical performance. The connection between the proposed method and OOD generalization is not clearly established. The method appears to be more of a behavior cloning variant with a time-varying regularization, which does not directly address the fundamental issues of OOD generalization in offline RL.

5. No concrete algorithm box is provided. 

6. The usage of the term "theoretical performance" in the experiment section is confusing.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript studies the offline RL problem without policy constraint by utilizing the diffusion model as the tool. The authors further suggests the Stochastic Weight Average (SWA) to mitigate the training fluctuation. The superiority of the method is validated from D4RL tasks.

### Strengths
The introduction of diffusion model is a good trial for the offline RL community.  Although some papers have combined diffusion model in offline RL, this paper also devotes some ideas in this area. 
The presentation is clear, and the paper is easy to follow.

### Weaknesses
1. First, from the experimental studies, the results of BDQL is not convincing. The performance of BDQL is close to other competitors and BDQL-SWA is even inferior to other competitors. 
2. From the authors' explanation, the Theoretical performance refers to the on-policy scenario, and the Practical performance refers to the offline scenarios. In offline scenario, the performance of BDQL-SWA is still not good enough. 
3. In SWA, the author mentions ``SWA averages the multiple checkpoints during the optimization''. Do you mean averaging the parameters of the models at different training time? So it is similar to the Target Actor/Critic network trick in most offline RL methods?

### Questions
1. Some offline-RL baselines, such as BEAR are missed in experiment, and the recent popular SPOT [1] method is not considered in experiments as well. It is suggested to consider the baselines in offline-RL methods.
2. The author claims that the BDQL has sufficiently solves the offline RL problem (OOD issue), and the OOD issue only causes fluctuation in training. The authors tries to illustrate this point with some ablation studies. However, this claim seems weak. It is suggested to add some theoretical analysis supporting this claim.
3. Actually, the diffusion model is time-costly in model inference. Will this issue also occur in BDQL? Some ablation studies on computation issues are suggested. 
4. The review will consider increase the rating when some concerns are replied and solved.

[1] Supported Policy Optimization for Offline Reinforcement Learning. https://arxiv.org/abs/2202.06239

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discovers a good property of one-step RL (policy improvement with fixed behavior value function) equipped with an estimated diffusion-based behavior policy: due to accurate modeling of the behavior policy, one-step RL without any policy constraint can reach a strong enough performance before it suffers from OOD actions. To mitigate training fluctuation or collapse and stabilize the evaluation of learned policies, this paper introduces stochastic weight averaging of policy checkpoints. Experiments on MuJoCo tasks from D4RL demonstrate that the proposed BDQL-SWA provides good performance without policy constraints.

### Strengths
1. A good property of one-step RL with estimated diffusion behavior policies is discovered, which leads to a simple and clear algorithmic design.
2. Detailed ablation studies illustrate the contribution of each component.

### Weaknesses
1. The good property of two-stage training in BDQL is only validated in MuJoCo tasks, which are relatively simple. There is a lack of experiments on more complex datasets, such as AntMaze and Adroit domains from MuJoCo, or even heteroskedastic datasets [2]. Also, it is only validated empirically, without theoretical analysis.
2. The performance of BDQL-SWA on MuJoCo tasks still trails behind modern offline RL methods.
3. It is not the first time diffusion models have been utilized to model complex behavior distributions, which has been done by Chen et al. [1]. The authors should explicitly clarify this and sufficiently discuss the difference with them.

### Questions
1. Why 'The output of the diffusion policy is the deterministic action rather than the distribution of action'? If I understand correctly, the diffusion policy models a stochastic state-conditioned action distribution as Equation (3) rather than a single deterministic action. So Equation (8) should be $\mathbb{E}_{s_t \sim \mathcal{D}, a \sim \pi_\theta(s_t)} [Q_\phi(s_t, a)]$? Does this one still follow the deterministic policy gradient (DPG) theorem?
2. The name of 'theoretical performance' is inappropriate. Better names can be 'online validation performance,' 'best performance,' or 'ideal performance.'

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
