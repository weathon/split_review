# Can Euclidean Symmetry Help in Reinforcement Learning and Planning?

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
In robotic tasks, changes of reference frames do not affect the underlying physics of the problem. Isometric transformations, including translations, rotations, and reflections, collectively form the Euclidean group. In this work, we study reinforcement learning and planning tasks that have Euclidean group symmetry. We show that MDPs with continuous symmetries have linear approximations that satisfy steerable kernel constraints, which are widely studied in equivariant machine learning. Guided by our theory, we propose an equivariant model-based RL algorithm algorithm, which is based on sampling-based MPPI for continuous action spaces. We test our proposed equivariant TD-MPC algorithm on a set of standard RL benchmark tasks. Our work shows that equivariant methods can give a great boost in performance on control tasks with continuous symmetry.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new algorithm for utilizing domain-inherent symmetry during training in RL. In contrast to previous work, it claims to first define a class of Geometric MDPs and provide practical implementations, which outperform a vanilla RL approach.

### Strengths
The paper tackles an interesting issue. Inherent symmetries are definitely under-utilized in current RL approaches in many ways. Incorporating the symmetry directly into the MDP (and not possibly other parts of the training loop) certainly warrants some additional exploration. Using a theoretical motivation to identify suitable domains is a good idea and presenting these domains should be (in an extended form) part of this paper's contribution.

The paper has been well proof-read for typos.

### Weaknesses
The main issue I have with this paper is that it reads like a primer for its own appendix, which is not how I reckon papers should be written. In general, the Appendix is referred to way too often (sometimes even sneakily like in a reference to Figure 11) and it thus contains way too many crucial parts of the overall argument. In contrast, the contribution is not as novel or groundbreaking that building up such a huge apparatus seems justified. A good theoretical class description and an extensive empirical study would have been appreciated.

As of now, the paper lacks focus on multiple fronts. various Theorems, Propositions, paragraph titles and types of lists make up the main body, but do not give it structure as the parts to not naturally follow from one another. As if the paper knows that it lost some people, the paper provides a recap on its own at the beginning of section 4. Perhaps beginning with the empirical study and the example domains and deriving the theoretical class from there would be easier?

The empirical study does a good job at motivating further research but lacks a definite conclusion. Most importantly, it would be nice to know how the described behavior translates to other means of training for MDPs.

Minor notes:
- "mappingto" instead of "mapping to" (p. 4)
- "demonstrat" instead of "demonstrate" (p. 5)

### Questions
see above

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work focuses on reinforcement learning and planning tasks that have Euclidean group symmetry. Motivated by geometric graphs, this work defines Geometric MDPs as the class of MDPs that corresponds to the decision process in Euclidean space. To investigate if Euclidean symmetry can guarantee benefits in model-based RL, this work presents a theoretical framework that studies the linearized dynamics of geometric MDPs. The theoretical results show that the matrices in linearized dynamics are G-steerable kernels, which can be used as a solution that significantly reduces the number of parameters. Inspired by the theoretical results, this work proposes an equivariant sampling-based model-based RL algorithm for Geometric MDPs. Empirical results in DeepMind Control suite demonstrated the effectiveness of the proposed method with continuous symmetries.

### Strengths
1.	The paper is well-written and formatted. The presentation of this work well connects the prior work: (1) value-based planning, (2) model-free equivariant RL, and (3) geometric deep learning.

2.	The first contribution of this work is Geometric MDPs, which define a class of MDPs with geometric structure and extend a previously studied discrete case to a continuous case. The symmetry properties in the Geometric MDPs are specified by equivariance and invariance of the transition and reward functions respectively. 

3.	The second contribution is providing theoretical guidance on assessing the potential benefits of symmetry in a Geometric MDP for RL. Focusing on linearized Geometric MDPs, the theory shows that the matrix-value function satisfies G-steerable kernel constraints, which is useful for parameter reduction. They also found that tasks have dominated global Euclidean symmetry and less local symmetry can have relatively better parameter reduction. 

4.	Based on the theory, they extend previous work TD-MPC to incorporate symmetry into sampling-based planning algorithms. The implementation is performed to ensure several components satisfy G-equivariance.

### Weaknesses
1.	Although Euclidean symmetry can bring significant savings in parameters, it does not always offer practical benefits for some tasks with local coordinates, e.g., the locomotion tasks. This is because the local coordinate systems used in many control tasks, such as those involving articulated bodies, often break the global Euclidean symmetry. For instance, a robot arm might have rotational symmetry around a joint, but this symmetry is not preserved when considering the entire robot's configuration in a global frame. The paper does not sufficiently address how the proposed method would handle tasks where the relevant symmetries are local rather than global.

2.	The proposed method assumes the symmetry group is known, which may limit its practical application. In many real-world scenarios, the underlying symmetries are not explicitly known or easily identifiable. The method relies on the ability to define the appropriate group of transformations for the given task, which is a significant limitation. The paper does not provide any guidance on how to discover or estimate the symmetry group when it is not readily available, which is a critical practical concern.

### Questions
1.	Since the proposed method extends previous work from discrete case to continuous case, can the proposed method also cover the tasks with discrete actions? 

2. How is the performance of the proposed method compared to other well-known RL algorithms, e.g., SAC, and DDPG on DeepMind Control suite?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies continuous symmetry in model-based planning by showing that such MDPs have linear approximations that satisfy steerable kernel constraints. The proposed algorithm follows an MPC style algorithm and is evaluated on a few tasks with continuous symmetries.

### Strengths
1. The paper is well-motivated and well-written. 
2. The proposed methodology is accompanied with theoretical analysis for giving insight into the use of symmetry in model-based planning.

### Weaknesses
### 1. Experimental setup and the baselines 
* The choice of the baselines is very limited. The proposed algorithm is only compared against a non-equivariant TD-MPC. I would consider the other baselines as ablation studies of the proposed algorithm with different subgroups ($D_8$, $D_4$, $C_8$). To better evaluate the performance of the algorithm, I suggest the authors use at least one other baseline from the literature on symmetry in continuous control RL, such as [1], and at least another baseline from model-based RL, such as Dreamer [2].

* The proposed algorithm is evaluated on only four environments, two of which (2D point mass and 3D point mass) are toy problems. In fact, the 2D point mass is mainly used for debugging purposes and is rarely reported in a scientific paper due to its simplicity. I suggest the authors incorporate more experiments either from the robotics literature or works on continuous symmetry in RL, such as [3]. The current set of environments does not adequately demonstrate the method's ability to scale to more complex, high-dimensional problems.

* Finally, I strongly encourage the authors to look into [9, 10] and follow their guidelines for reporting statistically significant results in RL. The absence of statistical significance reporting makes it difficult to assess the robustness of the experimental findings.

### 2. Overclaims and missing related work
* The authors have overlooked some essential papers, and I have identified some of their stated contributions as overstated. On page 2 (first paragraph), they state that their approach expands on earlier research on planning on 2D grids, yet [4] has already examined the equivariant Muzero which integrates symmetries in a complex model-based planning algorithm. Furthermore, they assert that they are extending equivariant model-free RL to continuous states and actions, while [1] has already accomplished this in a broader context, not solely restricted to Euclidean symmetry. Some examples of other missing references are [5, 6]. The authors need to more carefully position their work with respect to the existing literature to avoid overstating the novelty of their contributions.

### 3. Incremental contributions
* The definition of Geometric MDP appears to be a rebranding of MDP homomorphisms [7], which was also extended to continuous states and actions [1]. It is not clear why the authors have chosen to rename a well-studied concept in the literature by adding some restrictions on the group symmetry. This can be very misleading to an inexperienced reader. The paper needs to clearly articulate the specific differences between Geometric MDPs and existing formulations of MDP homomorphisms, especially in continuous state and action spaces.

* Additionally, the contributions of this paper appear to be incremental with respect to the prior work of [7] which explored the use of symmetry in model-based planning. The authors should clarify the novel aspects of their approach beyond the existing literature on MDP homomorphisms and symmetry in model-based RL.

### 4. Discrepancy between theory and experiments
* One of the key contributions of the paper, as claimed by the authors, is the study of continuous group symmetries in RL. Unfortunately, in their practical algorithm they are using discretized subgroups (page 8). This raises doubts regarding the soundness of the paper and the connection between theoretical analysis and the experimental results. The authors need to provide a more compelling justification for using discrete subgroups in their implementation, given their theoretical focus on continuous symmetries, and explain how this discretization does not compromise the theoretical guarantees.

### 4. Limiting assumptions
* The MDP dynamics is assumed to be deterministic (page 5, second paragraph) without any justification or insight into its reason. The assumption of deterministic dynamics is a significant limitation that restricts the applicability of the proposed method to real-world scenarios. The authors should discuss the implications of this assumption and how it might affect the performance of their algorithm in stochastic environments.

### Questions
1. What are the key distinguishing features of Geometric MDPs compared to MDP homomorphisms?
2. Why is the MDP dynamics assumed to be deterministic? Which part of the algorithm breaks in the case of stochastic dynamics?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The authors study equivariant model-based reinforcement learning.
- They first show that E(n)-equivariant MDPs give rise to an equivariant Bellman operator.
- They then focus on methods based on linearization of the MDP and show that LQR can be made equivariant.
- Their main contribution is an equivariant version of MPPI based on TD-MPC.
- They implement a version of this algorithm for discrete subgroups of E(2) and E(3) and demonstrate it on toy experiments (moving a point mass) and simple robotic gripping tasks.

### Strengths
- E(3) equivariance in robotics is compelling: many environments have underlying symmetries and data is often expensive to generate.
- As far as I know, this work is the first to study how to make MPPI equivariant (though not the first to study equivariant model-based RL, see below).
- The evaluation on robotic reaching tasks is relevant.

### Weaknesses
 - The paper does not adequately discuss two important aspects of equivariance in robotics: What if the equivariance is latent, i.e. the observations are not given in known, simple representations of the symmetry group – instead, they are given in pixels? And what if the symmetry group is partially broken, for instance by object positions or the direction of gravity?
- The main contribution – the equivariant modification of MPPI – leaves some questions open (see below), which I'm sure can be addressed during the rebuttal.
- The paper presents the discussion of continuous groups as a main contribution. But it does not actually talk about architectures for equivariance to continuous groups, and all the experiments stick to discrete subgroups.
- Most of the experiments are on toy settings where the benefits of equivariance is obvious. It would be more interesting to see if these benefits carry over to more complex environments.
- The authors miss some references on equivariance in model-based RL and planning:
	- A. Deac at al, "Equivariant MuZero", arXiv:2302.04798
	- J. Brehmer et al, "EDGI: Equivariant Diffusion for Planning with Embodied Agents", arXiv:2303.12410
- The paper writing could be improved. Theoretical results like Theorem 2 should be stated more precisely in the main paper. In Sections 3 and 4, I found it difficult to follow the flow of the arguments. (The problem may not be the paper, though, but come from my lack of in-depth knowledge of MPC.)

### Questions
- As the most minor nitpick of all, why do you cite Einstein's special relativity paper for E(3) equivariance? That was the one work that made clear that E(3) is *not* the fundamental symmetry group of nature ;)
- In Section 4, the proposed method require a "G-steerable equivariant MLP" for continuous groups G. What architectures do you have in mind? If I'm not mistaken, you never experiment with any such architecture for continuous G, right?
- To make MPC equivariant, the action sampling needs to be equivariant. Just after Eq. (11), you describe as the main problem that "action sampling is not state-dependent". Why? Isn't the equivariant learned policy used for action sampling?
- I wasn't able to follow the logic behind the G-sample method, could you explain that a bit more slowly, please?
- Is it fair to compare non-equivariant and equivariant methods with equal parameter count? Usually, equi methods have less parameters than non-equivariant counterparts with similar capabilities. This choice thus strikes me as a bit unfair to the baselines.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
