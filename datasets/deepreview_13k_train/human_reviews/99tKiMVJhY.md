# Learning Decentralized Partially Observable Mean Field Control for Artificial Collective Behavior

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Recent reinforcement learning (RL) methods have achieved success in various domains. However, multi-agent RL (MARL) remains a challenge in terms of decentralization, partial observability and scalability to many agents. Meanwhile, collective behavior requires resolution of the aforementioned challenges, and remains of importance to many state-of-the-art applications such as active matter physics, self-organizing systems, opinion dynamics, and biological or robotic swarms. Here, MARL via mean field control (MFC) offers a potential solution to scalability, but fails to consider decentralized and partially observable systems. In this paper, we enable decentralized behavior of agents under partial information by proposing novel models for decentralized partially observable MFC (Dec-POMFC), a broad class of problems with permutation-invariant agents allowing for reduction to tractable single-agent Markov decision processes (MDP) with single-agent RL solution. We provide rigorous theoretical results, including a dynamic programming principle, together with optimality guarantees for Dec-POMFC solutions applied to finite swarms of interest. Algorithmically, we propose Dec-POMFC-based policy gradient methods for MARL via centralized training and decentralized execution, together with policy gradient approximation guarantees. In addition, we improve upon state-of-the-art histogram-based MFC by kernel methods, which is of separate interest also for fully observable MFC. We evaluate numerically on representative collective behavior tasks such as adapted Kuramoto and Vicsek swarming models, being on par with state-of-the-art MARL. Overall, our framework takes a step towards RL-based engineering of artificial collective behavior via MFC.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies mean field control problems with decentralized decisions and partial observations. After introducing the problem, the authors prove theoretical results connecting the mean field problem and the N-agent problem. They then propose a policy-gradient based method and provide experimental results on several examples.

### Strengths
The paper seems rigorous and has both theoretical contributions and numerical experiments.

### Weaknesses
Some assumptions seem quite restrictive, such as Assumption 1b which says that the policies should be uniformly Lipschitz (see question below).

### Questions
Is it possible to replace the assumption on policies (which means restricting a priori the set of policies) by an assumption on the model which would ensure that the optimal policy satisfies this Lipschitz property? And would this be sufficient for your purposes

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper applies MARL to the proposed decentralized partially observable mean-filed control (Dec-POMFC) model, which can be reduced to single-agent MDP. A PPO-based method in the CTDE framework is applied to solve such problems. Theoretical analysis is also given.

### Strengths
- The paper is well written.

### Weaknesses
 - It is unclear to me where the particular difficulty is from. If it is from the partial observation, how do you solve the partial observation problem? Note that many Dec-POMDP problems can be grouped into weakly-coupled POMDP [1] where the partial observation can be sufficient to make optimal decisions.
- The CTDE training is very common in MARL, and the baseline of IPPO is not fair as it cannot use global information while the proposed method uses more information.
- The benchmark looks simple. It would be good to include more realistic and complex benchmarks to indicate the importance of the studied question and the proposed method.

### Questions
- What is the particular difficulty of solving the Dec-POMFC system, and how does the proposed method solve such difficulty? It would be easier to follow the paper if these questions were explicitly explained.
- How much information do you assume each agent can observe? i.e. how severe is the partial observation problem in the proposed model and algorithm?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript introduces Decentralized Partially Observable Mean Field Control (Dec-POMFC) to extend scalable MFC to a decentralized and partially observable system. The paper includes rigorous theoretical proof. The experiments are performed on representative collective behavior tasks such as adapted Kuramoto and VIcsek swarming models, against the SoAT IPPO methods.

### Strengths
The paper tackles a challenging problem featuring partial observability, multiple agents, and decentralization. This area is worth exploring.

The paper is well-written and provides very details algorithm description and theorectical proof. The experiments are carefully carried on.

### Weaknesses
The experiments were carried out on adapted Kuramoto and VIcsek swarming models. The authors report training curves, and the returns as the number of agents increases in the main manuscript. However, there is no direct comparison with the SoAT methods in terms of the second method.  In addition, there is no explicit summary or discussion about significant improvement, and it is hard for the reviewer to judge the contribution of the proposed methods in terms of the experimental results.

### Questions
1. The manuscript mentioned extending the proposed methods to handle additional practical constraints and sparser interaction. However, the reviewer sees it can be hard given the adopted assumptions in the paper. The reviewer is curious about the feasibility of making this extension.

2. The author claims about the generality of the proposed method. Can the authors elaborate on which design in the algorithm contributes to this generality in addition to using RL itself?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
