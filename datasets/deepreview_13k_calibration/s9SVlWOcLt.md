# Proto Successor Measure: Representing the space of all possible solutions of Reinforcement Learning

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
Having explored an environment, intelligent agents should be able to transfer their knowledge to most downstream tasks within that environment. 
Referred to as ``zero-shot learning," this ability remains elusive for general-purpose reinforcement learning algorithms.  While recent works have attempted to produce zero-shot RL agents, they make assumptions about the nature of the tasks or the structure of the MDP. We present \emph{Proto Successor Measure}: the basis set for all possible solutions of Reinforcement Learning in a dynamical system. We provably show that any possible policy can be represented using an affine combination of these policy independent basis functions. Given a reward function at test time, we simply need to find the right set of linear weights to combine these basis corresponding to the optimal policy.  We derive a practical algorithm to learn these basis functions using only interaction data from the environment and show that our approach can produce the optimal policy at test time for any given reward function without additional environmental interactions. \textbf{Project page:} \href{https://agarwalsiddhant10.io/projects/psm.html}{\color{myredorange}agarwalsiddhant10.io/psm.html}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In the paper, the authors present a novel approach to unsupervised reinforcement learning. They first present a theoretical foundation for the algorithm by showing that any state-action visitation distribution and any successor measure $M^{\pi}$ in a single MDP form an affine set. This motivates their approach - first learn the basis of the affine set (in an unsupervised manner, without a specific policy or reward), and then, given the affine space, the only optimization left given a downstream task is to find the optimal linear representation in the space. The authors present a practical algorithm to achieve both steps and evaluate it on two simple benchmarks and a robotic manipulation benchmark while comparing to two common unsupervised-rl baselines.

### Strengths
1. As far as I know, the authors are the first to make the observation that all state-action visitation distributions in an MDP can be represented as an affine set. This can have a potential impact on the field of unsupervised-rl in particular and other fields in rl in general. 

2. The theoretical claims in papers are well supported and presented in a precise and clear way

3.  The suggested algorithm can potentially leverage large offline datasets to effectively learn representations for downstream zero-shot tasks, which can have a significant practical impact.

### Weaknesses
1. The tasks chosen in the experiments section are quite simplistic, and it is not clear how the method would hold in more complex environments (e.g. with large state space or a more complex transition function). Specifically, the grid world and maze environments lack the high-dimensional state spaces and complex dynamics that are characteristic of real-world RL problems. The evaluation should include environments with continuous state and action spaces, and more complex transition functions to properly assess the scalability of the proposed method.

2. The technical details of the proposed algorithm are missing, e.g. how $\Phi$ is parametrized, what optimizer is used, etc. Further, the technical details of the benchmarks are also missing, e.g. what is the horizon and reward function of each task (without these it is hard to assess the quality of the success rate), etc. For example, it is unclear what neural network architecture is used to parameterize the basis functions, what the learning rate and batch size are, and what specific optimization algorithm is used. The lack of these details makes it difficult to reproduce the results and assess the practical viability of the method. The benchmark details should include the exact reward function used, the episode horizon, and any specific state or action space discretization that was used.

3. The limitations of the proposed approach were not discussed in the paper. For instance, it is not clear under what conditions the affine set assumption might break down or how the method would perform in environments with stochastic transitions or partial observability. The paper should include a discussion of the potential failure modes and limitations of the proposed approach.

4. While the paper is well-written and the ideas are presented clearly, it is hard to keep track of its high-level flow. A high-level flow for Sections 4 and 5 could have helped the readability of the paper

5. A theoretical discussion and analysis of the dimensionality of the affine space is missing in Section 4 (i.e. what affects $d$). It is not clear what factors influence the dimensionality of the affine set, and how this dimensionality relates to the complexity of the MDP. A theoretical analysis of this would be beneficial for understanding the applicability of the method to different types of MDPs.

### Questions
1. Typos:

    a. Line 432: toform -> to form
    
    b. Line 279 and Line 257: Add figure numbers

2. In line 267 you mention the derivation for the basis vector is in the supplementary material. I did not find such a derivation, is it missing? If so please add one and add an exact reference to it.  

3. At the end of Section 5.1 you presented a two-player game optimization strategy and suggested simplifying it with the single-player game presented in Section 5.2. Are there any practical benefits of one approach or another? I would suggest incorporating a discussion on this into the paper or adding some sort of an ablation study on that to the empirical experiments. 

4. How many seeds were used in the experiments in the empirical study? 

5. You discussed the quality of the Q function based on the visualizations in lines 440-444. Did you also perform a quantitative study on this (e.g. by comparing to the oracle optimal Q function)?   

6. Did you use the same offline dataset mentioned in the paper for all baselines? 

7. Did you perform a hyperparameter tuning procedure for your algorithm and the baselines? If so, can you elaborate on this? 

8. In the robotic manipulation task (Section 6.2), how did you handle a continuous state space? Doesn't that make the basis function continuous?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Proto Successor Measure (PSM), a zero-shot RL method that compresses any MDP to allow for optimal policy inference for any reward function without additional environmental interactions. The method seems technically sound.  But experiments are limited.

### Strengths
1. The proposed Proto Successor Measure (PSM) method combines policy-independent basis functions with biases, enabling it to generate new policies from offline data without additional environment interactions, and allowing it to adapt to different tasks.
2. The paper introduces a policy-independent basis function set, Φ, which can be shared across different tasks and policies. Since these basis functions are independent of specific policies, new policies can be generated simply by adjusting the combination weights. This reduces the need for retraining on new tasks, enhancing generalization capability and computational efficiency.

### Weaknesses
1. The paper cites "Planning with Diffusion for Flexible Behavior Synthesis" for its world model, but this work primarily focuses on using diffusion models for trajectory planning and is not directly related to world models in reinforcement learning. Relevant world-model references could include "Dream to Control: Learning Behaviors by Latent Imagination."
2. The paper represents policies as a compact discrete codebook, approximating an infinitely large policy space through a discrete set. While this simplifies optimization, it may also impose limitations. A discrete policy codebook can only represent a finite subset of the policy space, potentially leaving some strategies uncovered and leading to suboptimal results in certain tasks. Specifically, the method's reliance on a discrete codebook may struggle with tasks requiring fine-grained control or continuous policy adjustments. The approximation of the policy space could lead to a situation where the optimal policy lies between the discrete options, resulting in a suboptimal solution. This limitation is particularly concerning in complex environments where subtle variations in policy can lead to significant differences in performance.
3. The experimental setup is fairly limited, testing only two basic environments (Grid World and FetchReach), with relatively simple tasks. There is a lack of more complex, high-dimensional environments (such as robot control tasks in Meta-World or Mujoco) to demonstrate PSM's generalization capabilities and applicability. This limitation may affect the persuasiveness of the method's performance in a broader range of environments. The current experiments do not sufficiently demonstrate the method's ability to handle the complexities of real-world scenarios. The chosen environments are not representative of the challenges encountered in more sophisticated robotic tasks, where high-dimensional state and action spaces, along with complex dynamics, are common.

### Questions
See previous section.

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
4

### Summary
The paper is considering the 'zero-shot learning' problem, where the RL agent learns to understand a given environment and is expected to solve downstream tasks with different reward functions. The authors first show that any valid policy, by using its visitation distribution and successor measure, can be represented by some affine combination of basis vectors (in the discrete settings). And a corresponding algorithm is proposed to learn such basis vectors and then solve the optimization problem through the form of a  Lagrangian dual. A couple of experiments are provided to show its advantage.

### Strengths
> **Originality**
- The paper proposed a novel perspective to represent the set of all valid policies using their visitation-based probability measures, which further gives rise to a concise representation of the optimization problem in zero-shot RL.

> **Quality**
- Despite notational confusions, theoretical results provide some new insights for understanding an arbitrary policy.

> **Clarity**
- The presentation is mostly easy to follow, though some notations/theorem need more clarifications.

### Weaknesses
 > **Originality**
- A bit more summary of baseline methods would better show which part of the paper is novel, while which was already discussed.

> **Quality**
- In Line 368-370, some procedure to recover the optimal policy in the setting of continuous spaces is provided. However, the former theoretical results are based on proof in the setting of finite discrete spaces. The extension to continuous spaces lacks sufficient theoretical justification, particularly regarding the convergence and stability of the proposed method in such domains. The paper needs to address how the functional operators are approximated in practice and how this approximation affects the theoretical guarantees.
- As implied by Equation (10), the final step is to solve the dual problem, some theoretical analysis of the computational cost could help. Specifically, the paper should discuss the complexity of solving the linear program, considering the number of constraints and variables, and how this scales with the size of the state and action spaces. Furthermore, practical considerations such as the choice of solver and its impact on performance should be addressed.

> **Clarity**
- In Equation (1) - (3), a comma or $\times$ is missing between $\mathcal{S}$ and $\mathcal{A}$.
- In Section A.1, Proof of Lemma 4.1: first, the left bracket is in the wrong place in Line 659; and an explicit definition of matrix $S$ would help
- In Section 4, toy example, there is a reference to the derivation of Equation (5), which does not appear in the Appendix.
- Without more explicit explanation of $\Phi^{vf}$, currently Theorem 4.4. is not easily accessible. Some definitions would help. The paper should clarify how this feature map is constructed and what properties it possesses to ensure the validity of the theorem. The connection between this feature map and the visitation distribution should also be made more explicit.
- Equation (7) seems to be important in forming the method, however, model densities and other notations used there are not defined.

> **Significance**
- Although the abstract implicitly claims to not make assumptions on the MDP structure, according to both theories and experiments, discrete state and action spaces are focused on in this paper. The theoretical results, particularly the proof of Theorem 4.1, rely on the assumption of a finite action space, which limits the applicability of the method to continuous action spaces without further justification.

### Questions
- In the procedure in Section 5.3, is the reward function assumed to be known?
- Are Lemma 4.1 and Theorem 4.2 proposed by the paper or in former literature?

### Soundness
2

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
The authors introduce a Proto Successor Measure (PSM), which is a method to solve RL problems with a focus on achieving zero-shot learning. PSM works by creating a basis set for all possible solutions in an environment by decomposing the state-action visitation distributions, using linear combinations of policy-independent basis functions. This allows an agent to compute the optimal policy for any given task by adjusting the weights associated with the basis functions.

### Strengths
1: The authors claim: "*We show that any solution of the Bellman Flow constraint for the visitation distribution
can be represented as a linear combination of policy-independent basis functions and a bias*". In Chapter 4 and the appendix, the mathematical reasoning to support this claim looks sufficient and is well-written. However, I do not know whether the authors are the first to prove this. If so, it would be beneficial to point this out in the paper, preferably at the end of the introduction.

Other strengths:
- Interesting idea, and a nice visual comparison to baselines in a maze environment.
- The paper is easy to read through.

### Weaknesses
1: The authors claim: "*We show that any solution of the Bellman Flow constraint for the visitation distribution
can be represented as a linear combination of policy-independent basis functions and a bias*". In Chapter 4 and the appendix, the mathematical reasoning to support this claim looks sufficient and is well-written. However, I do not know whether the authors are the first to prove this. If so, it would be beneficial to point this out in the paper, preferably at the end of the introduction.

Other strengths:
- Interesting idea, and a nice visual comparison to baselines in a maze environment.
- The paper is easy to read through.

1: This paper looks like it has been created in haste, with nonexistent figure references in line 257 and 279, a relatively large whitespace left on page 9 after the conclusion, and a missing reproducibility statement.

2: The claim: "*We show that PSM can produce the optimal Q function and the optimal
policy for any goal conditioned task in a number of environments outperforming prior baselines.*" is not sufficiently proven. First of all, only a maze environment and Fetchreach are used, which does not correlate to "a number of environments". Second, the authors claim to outperform prior baselines. However, performance is only compared in the Fetchreach environment. Adding to this, in Section 5.2 of [Ahmed Touati & Yann Ollivier, 2021], it seems their Forward-Backward (FB) algorithm easily solves the Fetchreach environment. Can the authors comment on this performance discrepancy? Also, for completeness and to say you outperform prior baselines, the authors could at least add the Ms. Pacman environment as done in prior work.

3: Evaluation: No other evaluations or ablations can be found in the very limited Appendix section.

4: There is no real discussion or future work component in this paper, although there is space for it.

Other weaknesses:
- Fig.1: Figure 1 should be trimmed. The part of the image with "Find a Behaviour in a Dynamical System" is not necessary and confusing.
- References: The references are organized very poorly:
    - Line 535, Line 540, Line 543 , Line 576, Line 579, Line 581, Line 591, Line 593, Line 599: All these references have no venue.
    - Line 611 & Line 616: These are two double references of exactly the same papers.
    - For a lot of references that have been published in conferences, only the Arxiv reference is given.
    - This correlates with my statement in weakness 1, where it just feels that this paper has not been carefully prepared but has been submitted prematurely.

### Questions
- Why are there no ablations, and no other quantitative evaluations other than the Fetchreach environment?

### Soundness
3

### Presentation
3

### Contribution
2
