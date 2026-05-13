# A Continual Learning Perspective to Entropy Regularized Deep Reinforcement Learning

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Research on Continual Learning (CL) tackles learning with non-stationary data distributions. The non-stationary nature of data is also one of the challenges of deep Reinforcement Learning (RL), and as a consequence, both CL and deep RL rely on similar approaches to stabilize learning, from the use of replay buffers to the choice of regularization terms. However, while dynamic neural architectures that grow in size to learn new tasks without forgetting older ones are well researched in CL, it remains a largely understudied research direction in RL. In this paper, we argue that Policy Mirror Descent (PMD), a regularized policy iteration RL algorithm, would naturally benefit from dynamic neural architectures as the current policy is a function of the sum of all past Q-functions. To avoid indefinitely increasing the neural architecture, we study PMD-like algorithms that only keep in memory the last $M$ Q-functions, and show that a convergent algorithm can be derived if $M$ is large enough. This theoretical analysis provides insights on how to utilise a fixed budget of Q-functions to reduce catastrophic forgetting in the policy. We implement this algorithm using a new neural architecture that stacks the last $M$ Q-functions as 3-dimensional tensors to allow for fast GPU computations. StaQ, the resulting algorithm, is competitive with state-of-the-art deep RL baselines and typically exhibits lower variance in performance. Beyond its performance, we argue that the simplicity and strong theoretical guarantees of StaQ's policy update makes it an ideal research tool over which we can further build a fully stable deep RL algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a growing neural architecture (named StaQ) for a regularized policy iteration algorithm in the deep reinforcement learning domain. This dynamic algorithm makes use of all past Q-functions saved in memory to improve the policy by reducing catastrophic forgetting. To remain memory viable a convergent algorithm is derived from a fixed budged of Q-functions, resulting in smaller non infinite memory usage.

### Strengths
The clarity of the paper is good and can be easily understood. The proposed method to improve stabilty and mitigating catastrophic forgetting is relevant and a logical area of research in a reinforcement learning context. The chosen environments for evaluation make sense and provide strong validation for the StaQ method. The experiments are detailed and with multiple relevant baselines. The algorithm should be reproduceable with the given information. Limitaions and problems are explicitly acknowledged, specifically the exploration method, that can be improved. The Suggestions for future research provide a guide for logical future improvements and relevant research topics.
Overall this research could be a valuable addition for the reinforcement learning community.

### Weaknesses
Although the paper uses well-known baselines (DQN, TRPO, PPO), it also should include baselines like SAC and EWC, which were mentioned in the introduction chapter 1. While a rigorous mathematical foundation that clearly demonstrates the theoretical underpinnings of the proposed method is provided, there are instances where the density of formulas make the text hard to read. Reducing or summarizing some of the mathematical details in favor of intuitive explanations might improve readability. This is especially true for chapter 3 Preliminaries.

### Questions
Given that entropy regularization doesn’t solve the exploration problem in RL, could additional exploration strategies have synergistic effects with StaQ’s policy averaging?

### Soundness
3

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
4

### Summary
This paper proposes StaQ, a deep reinforcement learning (RL) algorithm inspired by continual learning (CL) techniques. StaQ addresses the instability often observed in deep RL training by using a policy update mechanism based on Policy Mirror Descent (PMD) with a growing neural architecture. This architecture, called Stacked Neural Networks (SNNs), stores and averages a large number (M) of past Q-functions, effectively stabilizing learning by smoothing out the policy updates.

The main idea in the paper is to leverage the stabilizing effect of averaging Q-functions in PMD. PMD updates the policy based on a weighted average of past Q-functions. StaQ approximates this by storing the last M Q-functions in the SNN and using them for the policy update. Moreover, the authors claim that the SNN architecture allows for efficient computation of these averages on GPUs. 

The algorithm also includes a theoretical analysis showing that for sufficiently large M, a modified version of finite-memory PMD converges to the optimal policy. Experiments on various benchmark tasks demonstrate that StaQ achieves competitive performance compared to standard baselines like PPO, DQN.

### Strengths
1) Integrating the SNN architecture with PMD is a novel approach that effectively addresses the instability issue in deep RL.
2) The authors provide a theoretical analysis of the convergence properties of the finite-memory PMD, offering insights into the algorithm's behavior.
3) The experimental results demonstrate the effectiveness of StaQ in achieving stable and competitive performance on MinAtar and Mujoco envs. 
4) The policy update is optimization-free, simplifying the overall algorithm and potentially increasing stability. (in discrete cases)

### Weaknesses
1) While the policy is stabilized, the Q-function learning still suffers from catastrophic forgetting, requiring ad-hoc workarounds like epsilon-softmax exploration.
2) The reliance on entropy regularization for exploration may not be sufficient for challenging exploration tasks, as evidenced by the performance on MountainCar? 
3) The current SNN implementation only supports MLPs, limiting its applicability to tasks requiring other architectures like CNNs or LSTMs.

### Questions
1) The theoretical analysis assumes exact Q-function computation. How does the approximation error introduced by using neural networks affect the convergence guarantees in practice?
2) Moreover, the paper mentions using the min or mean of two target Q-functions. What is the motivation behind this choice, and how does it impact performance in different environments? Maybe this is already discussed in the paper and I missed it?
3) How does the computational cost of StaQ scale with the memory size M and the size of the state-action space?
4) Could alternative CL techniques for mitigating catastrophic forgetting in the Q-function, such as rehearsal methods or regularization-based methods, be integrated into StaQ?
5) Just curious: How can the SNN architecture be extended to support other types of neural networks like CNNs and RNNs? Have the authors thought about this (since its mentioned as a potential future direction)

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed Stacked NNs (SNNs), stacking weights with respect to iterations and theoretically analized the convergence resultsof Policy Mirror Descent (PMD) algorithms with SNNs. They proposed StaQ using these concepts (PMD with SNNs) and validated its effectiveness by experimental results.

### Strengths
1. Theoretically Solid Approach
2. Simple Algorithm
3. Outperforming Experimental Results

### Weaknesses
1. Only valid for discrete actions
2. More Weights (More memory)
3. InComplete Experiemtal Design Yet

### Questions
**Q1:** There are numerous tasks, such as Meta-world (https://arxiv.org/abs/1910.10897), to validate the stability-plasticity dilemma. Thus, I am curious whether the MuJoCo tasks chosen by the authors are truly appropriate for studying this dilemma. For instance, in my personal opinion, many of the MuJoCo environments exhibit flat regions and necessitate the acquisition of new skills, as like Acrobat and CartPole. Could the authors elaborate on why these tasks are deemed suitable for investigating the stability-plasticity dilemma?

**Q2:** Given that Table 2 in the supplementary material indicates a memory size of 300, it would be beneficial to specify the inference and training speed of the proposed method in comparison to other Q-learning algorithms.

**Q3:** While the authors analyzed stability throughout the paper to prevent catastrophic forgetting, it appears that plasticity has not been adequately addressed. Someone may think that the remarkable performance may be an effect by emphasizing stability. Indeed, I think that some tasks (e.g., MuJoCo, Acrobat, CartPole) used are relatively static and do not require the development of new skills. I would appreciate the authors’ insights on this matter.

**Q4:**  The paper referenced in (http://proceedings.mlr.press/v139/peer21a/peer21a.pdf) considered the ensemble of $Q$-functions, and reported a reduction in bias as illustrated in Figure 5. It may be beneficial for the authors to compare the proposed StaQ approach with it.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces StaQ, an algorithm based on Policy Mirror Descent that uses a growing neural architecture to retain Past Q-functions. By limiting memory to the last M Q-functions, StaQ balances between scalability and stability. The authors experiments are evaluated on Classic Control, Mujoco, and the Minatar environment. StaQ shows strong performance in the Mujoco domain, and is compared against PPO, TRPO, DQN and Munchausen DQN.

### Strengths
- Well written.

- Extensive Related Work.

- Interesting approach of stacking neural networks.

### Weaknesses
- Evaluation: The classic control environments are, in my opinion, not informative when comparing RL algorithms. The same holds for the Minatar environments. The only baseline that is representative for RL algorithms in this paper therefore are the Mujoco environments. I would advise the authors to refrain from using Minatar and Classic control in their submissions.

- In line 393-396, you draw comparisons between your algorithms value functions and computational efficiency with those of SAC. However, what is the reason you do not compare to SAC in your evaluations, but instead to TRPO and PPO?

- Figure 3a:  *"Individual runs of StaQ show a clearer trend (2 runs plateau and one continues increasing),
while M-DQN, the closest performing baseline oscillates more around zero"*. I do not understand the reason why the authors would show this figure, as well as the caption. How is two runs plateauing and one increasing superior over another oscillating around zero? The first shows a 33% success rate while the second is oscillating a little more. I believe this figure and the connected conclusions around it are not contributing to the paper. What was the intended idea of this figure?

- Ablations: In the main paper, only Fig. 3b and Fig. 4 show some ablations of which 1 represents ablations on Acrobot. It would be much more informative if the authors would run a variety of ablations on all of the Mujoco environments, and normalize them into 1 score. As said in my first point, results and ablations on Acrobot are not informative to the reader.

### Questions
-

### Soundness
3

### Presentation
3

### Contribution
2
