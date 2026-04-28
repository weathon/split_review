# On the Linear Speedup of Personalized Federated Reinforcement Learning with Shared Representations

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Federated reinforcement learning (FedRL) enables multiple agents to collaboratively learn a policy without sharing their local trajectories collected during agent-environment interactions. However, in practice, the environments faced by different agents are often heterogeneous, leading to poor performance by the single policy learned by existing FedRL algorithms on individual agents. In this paper, we take a further step and introduce a \emph{personalized} FedRL framework (\PFRL) by taking advantage of possibly shared common structure among agents in heterogeneous environments. Specifically, we develop a class of \PFRL algorithms named \FedRL that learns (1) a shared feature representation collaboratively among all agents, and (2) an agent-specific weight vector personalized to its local environment. We analyze the convergence of \FedTD, a particular instance of the framework with temporal difference (TD) learning and linear representations. To the best of our knowledge, we are the first to prove a linear convergence speedup with respect to the number of agents in the \PFRL setting. To achieve this, we show that \FedTD is an example of the federated two-timescale stochastic approximation with Markovian noise. Experimental results demonstrate that \FedTD, along with an extension to the control setting based on deep Q-networks (DQN), not only improve learning in heterogeneous settings, but also provide better generalization to new environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work propose a Personalized FedRL approach (similar to PFL but with RL) allowing local/per-agent learnable parameters for use in heterogeneous FedRL settings with convergence results. The authors find a linear relationship between the number of agent and the convergence timestep.

### Strengths
- The theoretical analysis have a proof sketch and the assumptions are clearly stated.
- I think the two timescale approximation result is novel
- Interesting results from cliff-walking and cartpole

### Weaknesses
 - Although the setup hold promise, evaluation is rather on the simple side. I consider it understandable for now since the main focus in on theory.
- If I understand correctly, the linear speed up is not a particular exciting result, since sample collection in unit time grows linearly with N.
- There is no comparison with other PFL methods, or parameter-sharing MARL methods.

### Questions
Is the problem definition of PFedRL includes "shared common structure", how does it affects learning? or anything else in the theory? In theory they can be completely different problem without any shared structure and the results still stand?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a personalized federated reinforcement learning (FedRL) framework, PFEDRL-REP, that incorporates shared representations to improve learning in heterogeneous environments. PFEDRL-REP collaboratively learns a shared feature representation among agents while maintaining agent-specific weight vectors for personalization. The authors analyze PFEDTD-REP, a variant using temporal difference learning, and prove it achieves a linear convergence speedup in terms of the number of agents, demonstrating scalability benefits. Experiments in both policy evaluation and control settings show that PFEDTD-REP enhances convergence and generalization in heterogeneous environments compared to non-personalized FedRL methods.

### Strengths
1. PFEDRL-REP is an innovative approach to FedRL, addressing a major challenge in heterogeneous environments by introducing a shared representation while allowing for agent-level personalization.
2. The paper provides a rigorous theoretical foundation, including proofs of convergence speedup under Markovian noise using a two-timescale stochastic approximation framework. 
3. The paper is well-structured and clear, with detailed explanations of the problem formulation, the PFEDRL-REP framework, and the two-timescale convergence analysis.

### Weaknesses
1. The experimental evaluation could be extended to include more complex environments, such as those with sparse rewards or high-dimensional state spaces, to better assess the scalability of PFEDRL-REP. 
2. The applicability of PFEDRL-REP to all types of environmental heterogeneity is not fully guaranteed, as the combination of shared feature representations and personalized weight vectors may not capture all nuances of diverse environments.

### Questions
1. Is PFEDRL-REP universally applicable across diverse heterogeneous federated RL problems? What if a shared feature representation could not represent the similarity between different environments and the heterogeneity could not be distinguished by the agent-specific weight vector?
2. Does PFEDDQN-REP maintain strong performance on more complex RL tasks, such as those with sparse rewards or high-dimensional state spaces? Additional experimental results on more challenging environments would provide valuable insights.

### Soundness
2

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
4

### Summary
The manuscript introduces PFEDRL, a framework for personalized federated reinforcement learning (FedRL) aimed at addressing heterogeneity across agent environments. The authors propose PFEDTD-REP, a specific instantiation of PFEDRL with temporal difference (TD) learning. Notably, they claim a linear speedup in convergence proportional to the number of agents, a desirable characteristic in large-scale federated RL systems. Experimental results in both value-based learning (CliffWalking) and control tasks (CartPole, Acrobot) validate the framework's advantages, with promising outcomes in personalization and convergence speedup.

### Strengths
+The paper is practically relevant and addresses real-world heterogeneity in federated RL environments

+The manuscript made some innovations in FedRL theories:

- First work to prove linear speedup in personalized federated RL with shared representations under Markovian noise

- Rigorous analysis of convergence rates using two-timescale stochastic approximation theory

### Weaknesses
while there are merits in the paper’s theoretical contributions, I am concerned with a few critical points:

1. regarding the motivation on personalization:

a. the paper lacks formal definition of what constitutes successful personalization. The authors should consider to design metrics to quantify personalization quality

b. thus, no theoretical guarantees that learned personalization (via agent-specific parameters in the paper) captures meaningful environment-specific adaptations. What happens to personalization quality when environments are very different from each other?

c. how does agent count N affects personalization? if we add more agents by increasing N, do we have better personlization or worse?

d. is there a tradeoff between personalization and global performance or the speedup?

2. regarding the problem formulation and approach:

a. does sharing this common representation breach privacy preservation?

b. In section 2.2, why does the transition from (1) to (2) preserve the problem properties?

3. regarding theoretical rigor

a. corollary 4.15 claims that linear speedup w.r.t agent count N is justified by “we can proportionally decrease T as N increases while keeping the same convergence rate”. However, this is not a precise claim as linear speedup generally implies that adding more agents N directly enhances the convergence rate, without requiring adjustments to T. Here, the convergence rate remains fixed only by reducing T, which does not reflect true linear acceleration in convergence. The paper could be misleading readers into believing that the convergence rate inherently improves with more agents, rather than simply adjusting the number of communication rounds to balance computational costs

b. related to 3.a) above, if the authors claims linear speedup w.r.t agent count N, they should provide comprehensive experimental validation showing how convergence behavior scales with varying numbers of agents. Notable prior work making similar speedup claims, such as Fan et al. [1] which is one of the earliest FedRL works missing from the related work, included thorough ablation studies demonstrating the impact of agent count N on convergence. The absence of such analysis is particularly concerning given the centrality of the linear speedup claim to the paper's contributions.

c. otherwise, how to determine the optimal number of agents? If we add more agents, will we get faster convergence? what about personalization? intuitively, more agents should increase the personalization complexity. 

4. regarding experimental evaluation.

a. Limited diversity in test environments (only classic control tasks) and no statistical significance is assessed 

b. how to empirically verify the personalization achieved?

c. ablation on agent count N should be conducted.

### Questions
1. how does agent count N affects personalization? if we add more agents by increasing N, do we have better personlization or worse?
2. is there a tradeoff between personalization and global performance or the speedup?
3. how to determine the optimal number of agents? If we add more agents, will we get faster convergence? what about personalization? intuitively, more agents should increase the personalization complexity.

### Soundness
3

### Presentation
3

### Contribution
3
