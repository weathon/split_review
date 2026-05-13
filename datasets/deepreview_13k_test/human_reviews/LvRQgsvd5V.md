# Non-Adversarial Inverse Reinforcement Learning via Successor Feature Matching

- Decision: Accept
- Scores: 6, 6, 8, 3

## Abstract
In inverse reinforcement learning (IRL), an agent seeks to replicate expert demonstrations through interactions with the environment.
Traditionally, IRL is treated as an adversarial game, where an adversary searches over reward models, and a learner optimizes the reward through repeated RL procedures.
This game-solving approach is both computationally expensive and difficult to stabilize.
In this work, we propose a novel approach to IRL by \emph{direct policy optimization}: exploiting a linear factorization of the return as the inner product of successor features and a reward vector, we design an IRL algorithm by policy gradient descent on the gap between the learner and expert features.
Our non-adversarial method does not require learning a reward function and can be solved seamlessly with existing actor-critic RL algorithms.
Remarkably, our approach works in state-only settings without expert action labels, a setting which behavior cloning (BC) cannot solve.
Empirical results demonstrate that our method learns from as few as a single expert demonstration and achieves improved performance on various control tasks

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work considers inverse RL in the state-only setting. Leveraging the linear structure of returns, as inner product of successor features and reward weight, the authors could model inverse RL without adversarially optimizing the reward weight, while is often done in prior works. This allows one to directly optimize policy through minimizing the gap between the successor features of expert policy and of the learned policy.

### Strengths
- The paper is well organized and easy to follow

- The motivation is sound and the resulting algorithm is straightforward (without requiring min-max optimization)

### Weaknesses
- It is quite surprising that IQL failed most of the tasks in Figure 3

- The choice of baselines could be expanded. While SFM considers the state-only setting, GAIfO is the only baseline that originally proposed for this setting. It might be reasonable to include a few baselines that are designed for state-only setting, for example [1, 2] (with public implementation if my memory serves me right) and some more up-to-date baselines are appreciated. 

----

Note: I have not actively followed the recent literature on successor features, so I am uncertain about its novelty when applied to the IRL setting. As a result, I have a low confidence score.

[1] Gangwani, Tanmay, and Jian Peng. "State-only imitation with transition dynamics mismatch." arXiv preprint arXiv:2002.11879 (2020).
[2] Zhu, Zhuangdi, et al. "Off-policy imitation learning from observations." Advances in neural information processing systems 33 (2020): 12402-12413.

### Questions
- what are the hyperparameter search space for SFM and baselines respectively?

### Soundness
2

### Presentation
3

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
This paper introduces Successor Feature Matching (SFM), a novel non-adversarial approach to Inverse Reinforcement Learning (IRL). The key innovation is reformulating IRL as a direct policy optimization problem that matches successor features between the agent and expert demonstrations. The method has three notable contributions:

1. A non-adversarial approach that avoids the computational expense and instability of traditional adversarial IRL methods
2. The ability to learn from state-only demonstrations without requiring expert action labels
3. Strong performance from as little as a single expert demonstration

The method leverages successor features to estimate expected cumulative features and uses policy gradient descent to minimize the gap between learner and expert features. The authors demonstrate superior performance compared to both adversarial and non-adversarial baselines across multiple control tasks.

### Strengths
1. The non-adversarial approach using successor features is novel and elegantly simple compared to existing methods
2. The approach is well-justified with clear theoretical analysis and proofs
3. The method works with state-only demonstrations and single examples, making it widely applicable
4. SFM integrates seamlessly with existing actor-critic frameworks
5. Demonstrates superior performance across multiple tasks and metrics
6. Shows consistent performance even with weaker policy optimizers

### Weaknesses
1. The paper doesn't fully address how SFM handles the exploration problem inherent in IRL
2. The current implementation is tied to deterministic policy gradients, potentially limiting its applicability
3. The method currently only works with state-only base feature functions
4. While comprehensive, the evaluation is limited to DMC suite tasks; testing on more diverse environments would strengthen the claims

### Questions
1. How would the method perform on tasks with sparse rewards or requiring significant exploration?
2. Could the approach be extended to work with stochastic policies?
3. How does the method compare to recent offline IRL approaches?
4. What are the computational requirements compared to adversarial methods?
5. How sensitive is the performance to the choice of successor feature architecture?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces Successor Feature Matching (SFM), a novel method to Inverse Reinforcement Learning (IRL) which is non-adversarial and does not require expert action labels. SFM directly optimizes a policy to match the expert's successor features (SFs) using policy gradient ascent. The paper claims that SFM offers several advantages over existing IRL methods, including simplified training, state-only learning and robustness to optimizer choice.
The paper supports these claims through empirical evaluations on the DeepMind Control suite, demonstrating that SFM outperforms state-of-the-art adversarial and non-adversarial baselines on a variety of single-demonstration tasks. Additionally, the paper explores the impact of different base feature functions on SFM's performance, finding that Forward Dynamics Models (FDM) lands the best results.

### Strengths
- **Novel and well-motivated approach:** SFM provides a new angle in IRL by leveraging SFs for direct policy optimization, offering an alternative to adversarial methods.
- **Strong empirical results:** Experiments demonstrate the superiority of SFM over sota methods on normalized return and optimality gap across single-demonstration tasks, demonstrating its effectiveness.
- **State-only learning:** The ability to learn from state-only demonstrations is a great contribution.
- **Robustness to RL optimizer choice:** SFM's performance with both strong (TD7) and weaker (TD3) optimizers shows versatility, making it potentially useful for resource-limited applications.
- The experiments are conducted in clear logic and the analysis and observations are novel and interesting.

### Weaknesses
- **Dependence on deterministic policy gradients:** The current formulation of SFM is tied to deterministic policy gradient algorithms. Exploring extensions to stochastic policies would broaden its scope. However, it's clearly mentioned by the authors in the discussion part.
- **Exploration Challenges:** as stated by the authors, the presented method does not fully resolve IRL exploration issues. I wonder how the performance may vary significantly across domains requiring extensive exploration.

### Questions
- How does SFM handle scenarios where expert demonstrations do not cover the entire state space, particularly in sparse-reward or high-dimensional tasks?
- Can the authors elaborate on potential extensions of SFM to stochastic policy optimizers, and any early experiments indicating feasibility?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes Successor Feature Matching (SFM) in the Inverse Reinforcement Learning (IRL) problem.  The authors focused generalized reward-like properties of  successor features (Barreto et al. 2017), e.g. recovering reward, discounted accumulation. These allowed SFM for alternative formulation of policy optimization using L2 loss in Eq. (4). The experimental results suggest that the proposed SFM yields good scores in single-demonstration benchmarks and much more impressive scores among state-only IRL algorithms.

### Strengths
1. The proposed SFM, in contrast to adversarial methods, is more rooted in the historical context of early IRL studies.
2. In my opinion, IRL (or even RL) methods do not have to restrict themselves to formulating scalar reward signals. Adaptation SF (Barreto et al., 2017) expands the notion of IRL into feature learning, which can relax some rigidity in RL-IRL formulation. Since the features have successfully formulated vectorized signals in the transfer learning tasks in RL, this could be a significant contribution that relaxes studies of IRL. 
3. The proposed method achieved good performance among modern IRL methods.
4. Propositions 1-3 are straightforward to understand.

### Weaknesses
1. I do not understand why "non-adversarial" property is framed as the main contribution throughout the paper. Adversarial learning and SFM are not mutually exclusive. Eq. (3) shows that the base feature can be trained with adversarial learning by setting $\mathcal{L}_\mathrm{feat} = \mathrm{Eq. (3)}$. If the author intended to deepen our understanding of the role of adversarial learning in IRL, they should have provided (1) another theoretical justification of non-adversarial learning and (2) ablation studies, including Eq. (3) in Fig. 6, and (3) results of combining various base feature losses that verifies adversarial losses might deteriorate IRL performance.  
2. Compared to Figs. 4 and 5, single-demonstration task performance in Fig 3 is only sometimes good, suggesting that SF is more focused on representing states. For some scenarios, action representation performance might be necessary.   
3. To demonstrate scalability, including more complex (or demonstrative) benchmarks in Fig. 3 would be beneficial to IRL researchers to grasp the model's performance. 
4. There are no supporting tables in the appendix that measure the performance of the learning curves in Figs. 3, 5, 6.

### Questions
1. How applying l2-loss  in Eq.(4) can be understood for the policy $\pi_\mu$? 
2. I think SFM (random) performed well; what is the reasoning behind this and presenting Eqs? (9-11)? Could the base feature only trained with arbitrary unsupervised learning with only states without the next states, actions, or goals?

### Soundness
3

### Presentation
2

### Contribution
2
