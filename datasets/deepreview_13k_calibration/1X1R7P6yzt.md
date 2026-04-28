# Discrete GCBF Proximal Policy Optimization for Multi-agent Safe Optimal Control

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Control policies that can achieve high task performance and satisfy safety constraints are desirable for any system, including multi-agent systems (MAS). One promising technique for ensuring the safety of MAS is distributed control barrier functions (CBF). However, it is difficult to design distributed CBF-based policies for MAS that can tackle unknown discrete-time dynamics, partial observability, changing neighborhoods, and input constraints, especially when a distributed high-performance nominal policy that can achieve the task is unavailable. To tackle these challenges, we propose **DGPPO**, a new framework that *simultaneously* learns both a *discrete* graph CBF which handles neighborhood changes and input constraints, and a distributed high-performance safe policy for MAS with unknown discrete-time dynamics.
We empirically validate our claims on a suite of multi-agent tasks spanning three different simulation engines. The results suggest that, compared with existing methods, our DGPPO framework obtains policies that achieve high task performance (matching baselines that ignore the safety constraints), and high safety rates (matching the most conservative baselines), with a *constant* set of hyperparameters across all environments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The proposed DGPPO framework addresses challenges in multi-agent systems (MAS) by learning both a discrete graph control barrier function (DGCBF) and a high-performance safe policy under unknown discrete-time dynamics, changing neighborhoods, and input constraints. DGPPO combines reinforcement learning and DGCBF, achieving high task performance and safety across varied environments without needing a pre-existing nominal policy or multiple hyperparameter sets, consistently outperforming other methods in both metrics of safety rate vs cost for various simulations.

### Strengths
- The proposed method (DGPPO) is an elegant way to solve the discrete-time distributed MASOCP (multi-agent safe optimal control problem) with unknown environment dynamics. This assumption was not present in previous work which had to differentiate through the given transition functions.
- The theorems introduced provide a solid foundation for the applicability of DGPPO in the discrete-time setting.

### Weaknesses
 - Scalability appears limited (only up to 7 agents) compared to the continuous time setting of GCBF+ [1] (most likely due to the present of unknown environment dynamics and the noise introduced through the sample score function gradient).
- The stability of DGPPO compared to the baselines does not seem appropriately explained. Is it a purely empirical observation or is there some theoretical justification available?
- In the given setting, why is the assumption of unknown dynamics interesting? To me, the environments considered are purely the settings of [1] without using the environment dynamics directly (even though they are available). Would it not be a better idea to consider an environment where the dynamics are not as simple as the ones in [1] or some complex unknown function (for e.g., common Mujoco robots)?

### Questions
1. Why is the dependency of the algorithm on a nominal policy a bad idea in the given settings? Since it appears easy enough to construct one (say a PID controller like in [1]) for the environments given, is this the right direction?
2. What is the difference between the training and inference situations in terms of the number of agents? Does the algorithm need to be retrained for every new number of agents unlike in [1] where the algorithm was trained on 8 agents and deployed on up to 1024 agents (albeit being purely concerned with single goal reaching while avoiding collisions)?
3. With regards to the sample efficiency and computation requirements, how is DGPPO w.r.t. the baselines (I noticed the training time was listed as 12 hours on the reference specifications)? On a related note, how is the benefit of a constant set of hyperparameters demonstrated? Can we confidently say the hyperparameter search for the baselines takes significantly longer (in wall clock time on a comparable machine)?
4.What are the restrictions on the definition of the avoid set $\mathcal{A}_i$ and the assumptions on the function $h_i^{(m)}$? Do the avoid sets primarily represent distance to $y^k$ greater than some safe radius?
5. The LiDAR part of the observation appears less clear. From the appendix (Sec B.2.1) is it right to say that only the LiDAR environments use the 32 equally spaced ray capturing relative positions? How are the obstacles in the VMAS environments represented to the agent?
6. The experiments with scalability to multiple agents (Fig. 5) appear quite close to the baselines. Is there a better comparison available?

### Soundness
3

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
The paper introduces a novel framework, Discrete Graph Control Barrier Functions Proximal Policy Optimization (DGPPO), for ensuring safe control in multi-agent systems (MAS) operating under unknown discrete-time dynamics and input constraints. Unlike prior approaches that rely on continuous-time models and known nominal policies, DGPPO incorporates discrete CBFs (DCBFs) and reinforcement learning to dynamically learn both a high-performance safe policy and a discrete graph CBF (DGCBF). Through extensive empirical validation across various simulated MAS environments, DGPPO claims to achieve both high task performance and safety without the need for hyperparameter adjustments specific to each environment.

### Strengths
The authors present an innovative combination of reinforcement learning and discrete-time CBFs to address the challenges of safety and task performance in MAS with unknown dynamics. The extension to the DCBF framework in discrete-time and the introduction of DGCBFs allow for neighborhood adaptability, overcoming limitations associated with continuous-time CBFs. The approach is well-motivated, tackling safety in unknown environments without requiring a predefined nominal policy—a substantial improvement for multi-agent reinforcement learning (MARL). I particularly appreciate the rigorous theoretical presentation to support the proposed approach.

### Weaknesses
While DGPPO introduces a novel safety mechanism for MAS, nonetheless I believe there are few critical concerns that could limit the effectiveness and general applicability of the approach.

**Lack of clear performance metrics**: 

while DGPPO is shown to achieve high safety, the empirical results focus primarily on safety metrics and the minimization of constraints. It remains unclear if the agents are successfully accomplishing global objectives. Without metrics like mean global success rate or reward, it is difficult to assess if the agents are merely achieving safety (e.g., by staying stationary) rather than making meaningful progress toward the task goals while satisfying the safety constraints. This is especially relevant as the DGPPO framework does not incorporate a nominal policy, meaning that without these metrics, the experiments risks overlooking cases where the agents avoid unsafe states at the expense of task completion. Does the proposed framework present mechanisms to ensure that safety constraints do not excessively dominate the objective?

**Limited scalability experiments**: 

the authors state that DGPPO scale well w.r.t to the baseline approach tested, however testing 5 agents instead of 3 as in the original experiment, I believe it is too limited to claim scalability of the proposed approach. Crucially, as stated from the authors themselves the proposed approach requires both stochastic and deterministic rollouts to enforce DGCBFs. While this approach ensures safety in discrete-time settings, it also introduces significant sample inefficiency, which may limit the framework’s scalability to larger or more complex MAS. Hence, an extensive test with for instance 10 or 15 agents would strength the results of the paper.
Moreover while the authors employ GNNs with attention mechanisms to handle changing agent neighborhoods, the computational complexity of GNNs in larger MAS could become important. In high-density environments with frequent neighborhood changes, maintaining an updated and accurate DGCBF through GNNs could pose significant computational challenges, possibly impacting real-time applicability. A detailed discussion on the scalability of GNN-based policies for larger agent systems would add valuable context to the method’s limitations.

**Dependence on hyperparameter $\nu$ for constraint enforcement**: 

the authors claim on the fact that DGPPO is less sensitive to hyperparameters does not seem to be properly backed up. From the plot in Fig. 6b the value of $\nu$—responsible for controlling the weight on constraint minimization steps—significantly impacts performance. Misalignment in $\nu$ could lead to either overly conservative or unsafe policies, showing that DGPPO still requires careful tuning, contrary to its stated hyperparameter robustness.

### Questions
Q1: How does DGPPO ensure that agents achieve the global objective, rather than just meeting safety constraints?  

Q2: Could DGPPO’s rollout requirements be reduced to improve sample efficiency without compromising safety?  

Q3: What are the practical scalability limits of DGPPO when applied to larger MAS, particularly with the use of GNNs?

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
3

### Summary
This paper proposes a safe multi-agent reinforcement learning method based on distributed control barrier functions (CBFs) for multi-agent systems with limited perception capabilities. Simulation results on several multi-agent safe coordination tasks demonstrate the effectiveness of the proposed method.

### Strengths
(1) The multi-agent safe optimal control problem considered in this paper is both general and challenging, as neither the system model nor a nominal policy is available in advance.

(2) The learned policy is safe, which does not require additional safety filters in implementation.

(3) Extensive simulations are conducted, and state-of-the-art baselines are compared.

### Weaknesses
There exist several theoretical issues in the paper. The motivation of employing the discrete graph CBF is unclear. Some implementation details should be incorporated. See Questions part for more details.

(1) The policy in this work only takes local observations as input, such that it is decentralized. Why do you refer to it as a distributed policy?

(2) The modified constraint (11b) is too strict which cannot be satisfied by a lot of policy classes, such as the Gaussian policy. This constraint, requiring the expectation of the CBF to be negative, is overly restrictive and may lead to overly conservative policies or prevent convergence for many common policy parameterizations.

(3) In (12), please provide the explicit gradient formula when the safety condition is violated. Note that the authors provide a gradient in (41). Nevertheless, this gradient is not associated to the policy loss function (under safety violation) in (12). The gradient provided in (41) appears to be a score function gradient, while the update in (12) requires a policy gradient. The connection between these two is not clearly established, and it is unclear how the score function gradient is used to update the policy parameters when the safety constraint is violated.

(4) Theorem 3 is very difficult to understand. The orthogonality assumption is impractical. The reviewers also find that the authors try to replace the stationary state distribution (which is a function associated to the policy parameter $\theta$) with a constant state distribution in this theorem to obtain their gradient $g$ in (13). What is the purpose of giving Theorem 3? What is the relationship between (13) and (14)? The theorem's use of a fixed state distribution $\rho$ for calculating the gradient $g$, while the actual policy induces a different state distribution $\rho^{\pi_\theta}$, is a significant concern. This substitution undermines the validity of the gradient calculation and its relevance to the actual policy optimization process. The relationship between the derived gradient $g$ and the policy loss function in (14) is also unclear.

(5) The reason of using discrete graph CBFs should be explained clearly. Note that we can regard the multi-agent system as a large but single agent. Then, you can directly use the discrete CBF given in Theorem 2 to learn safe policies. In this case, the distributed control nature can still be preserved as the learned observation-based policy is end-to-end. The advantage of using a discrete graph CBF over a standard discrete CBF for the entire multi-agent system is not well-justified. The paper should explain why the graph structure is necessary and how it improves performance or safety compared to a monolithic approach.

(6) Theorem 4 is hard to understand. What is the relationship between the discrete graph CBF and the discrete CBF? Similar to Theorem 1, it is important for the authors to show that the safe set is forward invariant based on the discrete graph CBF. The connection between the discrete graph CBF and the standard discrete CBF is not clearly defined. It is also crucial to demonstrate that the safe set remains forward invariant under the proposed discrete graph CBF, which is not explicitly shown in the paper.

(7) In (11b), the safety constraint is calculated using a stochastic policy $\pi$. However, in Fig. 1, deterministic policies are used for estimating the discrete graph CBF. This discrepancy between the theoretical formulation and the implementation raises concerns about the validity of the approach. The paper should clarify why a deterministic policy is used for estimating the CBF while a stochastic policy is used in the safety constraint.

(8) Why do the agents have different GAEs in your algorithm? Are you suggesting that the agents are heterogeneous and that their local policies differ?

### Questions
(1) The policy in this work only takes local observations as input, such that it is decentralized. Why do you refer to it as a distributed policy? 

(2) The modified constraint (11b) is too strict which cannot be satisfied by a lot of policy classes, such as the Gaussian policy.

(3) In (12), please provide the explicit gradient formula when the safety condition is violated. Note that the authors provide a gradient in (41). Nevertheless, this gradient is not associated to the policy loss function (under safety violation) in (12).

(4) Theorem 3 is very difficult to understand. The orthogonality assumption is impractical. The reviewers also find that the authors try to replace the stationary state distribution (which is a function associated to the policy parameter $\theta$) with a constant state distribution in this theorem to obtain their gradient $g$ in (13). What is the purpose of giving Theorem 3? What is the relationship between (13) and (14)? 

(5) The reason of using discrete graph CBFs should be explained clearly. Note that we can regard the multi-agent system as a large but single agent. Then, you can directly use the discrete CBF given in Theorem 2 to learn safe policies. In this case, the distributed control nature can still be preserved as the learned observation-based policy is end-to-end.

(6) Theorem 4 is hard to understand. What is the relationship between the discrete graph CBF and the discrete CBF? Similar to Theorem 1, it is important for the authors to show that the safe set is forward invariant based on the discrete graph CBF.

(7) In (11b), the safety constraint is calculated using a stochastic policy $\pi$. However, in Fig. 1, deterministic policies are used for estimating the discrete graph CBF.

(8) Why do the agents have different GAEs in your algorithm? Are you suggesting that the agents are heterogeneous and that their local policies differ?

### Soundness
2

### Presentation
2

### Contribution
2
