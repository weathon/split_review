# Reinforcement Learning of Diverse Skills using Mixture of Deep Experts

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Agents that can acquire diverse skills to solve the same task have a benefit over other agents. Unexpected environmental changes for example may prohibit executing a learned behavior such that a complete retraining is necessary if the agent can not discard the invalid skill and rely on previously acquired, different ones. 
However, Reinforcement Learning (RL) policies mainly rely on Gaussian parameterization, preventing them from learning multi-modal, diverse skills. In this work, we propose a novel RL approach for training policies that exhibit diverse behavior. To this end, we propose a highly non-linear Mixture of Experts (MoE) as the policy representation, where each expert formalizes a skill as a contextual motion primitive. The context defines the task, which can be for instance the goal reaching position of the agent, or changing physical parameters like friction. Given a context, our trained policy first selects an expert out of the repertoire of skills and subsequently adapts the parameters of the contextual motion primitive. 
To incentivize our policy to learn diverse skills, we leverage a maximum entropy objective combined with a per-expert context distribution that we optimize alongside each expert. The per-expert context distribution allows each expert to focus on a context sub-space and boost learning speed. However, these distributions need to be able to represent multi-modality and hard discontinuities in the environment's context probability space. Moreover, the distributions should not rely on environmental pre-knowledge such as context boundaries, as they are usually not given. We solve these requirements by leveraging energy-based models to represent the per-expert context distributions and show how we can efficiently train them using the standard policy gradient objective. We show that our approach can learn precise and diverse skills of challenging robot simulation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach for acquisition of diverse skills using non-linear mixture of experts. The main ingredients of this approach are maximum-entropy objective for learning diverse experts, trust-region optimisation for stable bi-level optimisation, and energy-based models for automatic curriculum learning. Their approach demonstrates the learning of diverse skills for solving the same task.

### Strengths
- Section 3 on Diverse Skill Learning is well-written and describes the method and the contributions of the work in a clear manner, with the appropriate references to existing work in the area.
- Figure 5 provides good qualitative evidence of diverse skills being learnt by the proposed approach.
- The Conclusions mention a drawback of the approach in that it is unable to replan in the event of collisions, for instance. This is an important empirical detail and I liked the fact that it was raised in the paper.

### Weaknesses
 - Automatic curriculum learning is a key ingredient of the proposed method; however, an important set of approaches in this direction has not been covered in related work, such as [1] and others in this family of approaches.
- Figure 3-c which shows ablations on the TT environment has inconsistent number of episodic samples (X-axis) for the different approaches in the plot. It would be useful to have asymptotic performance of each of these approaches and then compare them in terms of this performance, and also in terms of training speed (eg: w/o automatic curriculum learning is slower than w/ automatic curriculum learning).
- In Figure 4 a-b as well, it would be nice to have the asymptotic performance for Di-Skill and BBRL to have a fair comparison of performance.
- While SVSL and BBRL are good CEPS baselines, it would also be nice to compare with a standard RL baseline such as PPO to better motivate the need for this approach.
- Minor points:
    - The environment description has been duplicated to some extent in the main text and the caption for Figure 4. It may help to prune that and instead include additional analysis.
    - Section 2 Prelimanaries -> Preliminaries

### Questions
- I am not sure why the prior $\pi(o)$ has been assumed to be uniform. For sparse reward tasks, I can imagine observations that are closer to the goal would be rarer than those closer to the initial state at the beginning of the episode. Or does this paper assume full access to the simulator in which resetting to any observation is possible?
- In the Experiments section, the paper mentions that the aim is to check whether Di-Skill is able to learn precise and diverse skills. The fact that it learns diverse skills is reasonably demonstrated in Figure 5, but I am yet to find evidence that precise skills are learnt. Could the authors please point me to that?
- Could the authors provide any insights on the learnt $\pi(o | c)$? Of the number of experts used, how often were they used when averaging across observations?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Di-SkilL, a reinforcement learning (RL) approach for training agents to exhibit multi-modal and diverse skills. The authors propose a mixture of experts (MoE) model that enables the agent to select and adapt from a repertoire of skills based on the context. The context in this work represents task definitions like goal positions or varying environmental parameters. The authors leverage energy-based models for per-expert context distributions to overcome challenges in multi-modality representation and hard discontinuities. They demonstrate the efficacy of their approach on complex robot simulation tasks.

### Strengths
The paper addresses an important and timely challenge in RL, that of equipping agents with the ability to learn and adapt to multiple skills for a given task. The energy-based approach for representing per-expert context distributions is innovative and offers a solution to traditional Gaussian parameterization limitations. The model's design, which avoids assumptions about the environment and doesn't require prior knowledge, increases its general applicability.

### Weaknesses
There might be concerns regarding the scalability and computational efficiency of the proposed method, especially in real-world robotic applications. This should be discussed.

Related work discussion and baseline are not sufficient, missing other MoE methods like PMOE [1].

### Questions
See Weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of learning diverse skills in contextual RL problems. It achieves so in the framework of contextual episode-based policy search and aims to learn a mixture of expert policies. It follows the previous work SVSL [Celik et al. 2022] to jointly learn a per-expert context curriculum $\pi(c|o)$ and a context conditioned policy $\pi(\theta|c, o)$. The key contributions of this work is (1) using softmax-based per-expert context distribution to model the curriculum which enables validity and multi-modality of the sampled context curriculum; (2) using trust-region and PPO to stabilize the bi-level policy training. The proposed approach is compared against two baselines BBRL and SVSL on Table Tennis Env and Box Pushing Env and shown to outperform baselines.

### Strengths
1. The topic of optimizing a set of expert policies with diverse strategies for the same task is beneficial to improving robustness of the robotic control and helps capture the multi-modality nature of some real-world tasks.

2. The idea of achieving automatic multi-modality context curriculum learning via applying softmax on sampled context is intuitive.

3. The experiments show the proposed algorithm performs better or at least similar to baseline algorithms on evaluated problems.

### Weaknesses
1. While the concept of the proposed technique is easy to follow, some important details are missing and it might affect the reproducibility of the proposed approach. Specifically, the parameterization of the motion primitives and the exact method for converting policy parameters into robot action trajectories are not sufficiently detailed. The description of the context space and how it relates to the motion primitives is also unclear. Furthermore, the implementation details of the energy-based model (EBM) for the per-expert context distribution, including the specific neural network architecture and training procedure, are not provided, making it difficult to reproduce the results.

3. The novelty over previous work seems incremental. The core idea of using a mixture of experts with a context-dependent policy is not new. The main contribution seems to be the use of a softmax-based per-expert context distribution and the application of trust-region and PPO for training stability. However, the benefits of these specific choices are not thoroughly justified, and the improvements over existing methods are not substantial enough to warrant a significant contribution.

3. More extensive evaluation are needed. The current evaluation is limited to two environments, Table Tennis and Box Pushing, which are not sufficiently diverse to demonstrate the general applicability of the proposed approach. The lack of comparison to other state-of-the-art methods, especially those using different policy parameterizations, further limits the impact of the evaluation. The absence of ablation studies on the individual components of the proposed method also makes it difficult to assess the contribution of each component.

### Questions
1. To better understand the action space of the contextual episode-based policy, could the author give some details or examples of the concept of motion primitives and how to convert the policy parameters into the episode-wise robot action trajectory?

2. Eq (3) seems to be not original from this work, a proper reference would help readers to understand the background of this line of work.
The derivation from Eq (4) to Eq (5) and Eq (6) is unclear. It would be more clear to have an intermediate objective which is jointly optimizing for $\pi(\theta|c, o)$ and $\pi(c|o)$, and derive from there to have two separate objectives for bi-level optimization.

3. In Section 3.1, it says “mapping the context $c$ to a mean vector and a covariance matrix” and “Note that in most cases a context dependent covariance matrix is not useful and introduces unnecessary complex relations.” It is confusing that whether the covariance matrix in the implementation is context dependent.

4. Line 10 in Section 3.2, should “Fig. 2c” be “Fig. 2d”?

5. Which terms in Eq (8) and Eq (9) accounts for encouraging the coverage of the context space by experts? From the formulation, it seems to try to learn a set of policy each of which can solve the entire task space as much as possible. The learning of policies seem to be relatively independent and is it possible to learn a set of experts whose preferred context distributions are the same.

6. More testing environment description would be helpful. Some details about action space and reward definitions are missing for both tasks.

7. Evaluating the algorithm on more environments will make the comparison more thorough. For example, it would be helpful to evaluate on the other tasks used in Otto et al. 2023.

8. It would also helpful to show complete comparison against both SVSL and BBRL on all evaluated tasks (at least provide comparison plots in Appendix)

9. Given the proposed approach is built upon SVSL with two improvements, it would be great to do ablation study on both improvement techniques.

10. The multi-modality in this work is achieved by mixture of experts, however each expert is still modeled by uni-model gaussian policy. 

11. Recent work (Huang et al. 2023 [1]) proposes some multi-modal policy parameterization. How is the proposed approach compare to this work and can the proposed approach enhanced by the policy reparameterization from [1]?

12. Is this proposed approach also applicable to step-based RL problems?

[1] Huang et al, Reparameterized Policy Learning for Multimodal Trajectory Optimization.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for learning diverse skills to solve different contexts of the same task. The method is designed to prioritize experts that are promising in different contexts. The algorithm involves training each experts in the corresponding task context and updating the joint distribution of experts and task contexts. Experimental findings indicate that this approach effectively trains experts in two robotics domains and yields a certain degree of diversity among the trained experts.

### Strengths
The idea is interesting and could has the potential be applied in more complex domains.

### Weaknesses
1. The motivation behind the research is not clearly articulated. It is unclear whether the authors intend to discover diverse solutions within the same task or seek experts for all tasks/contexts. The paper does not clearly distinguish between these two goals, making it difficult to understand the core contribution. For example, is the aim to find multiple ways to achieve the same goal in a fixed environment, or to have a set of experts that each excel in different variations of the task?
2. The paper lacks sufficient detail regarding the definition of the mixture of experts model, including the definition of an expert. The description of how the experts are parameterized and how they interact with the context is vague. It is unclear how the gating function is implemented, and how the context is used to select an expert. Furthermore, the relationships between context (c), expert (o), and the parameter θ are not adequately explained. The paper should provide a clear mathematical formulation of the MoE model and the role of each component.
3. The experimental section appears to be confined to relatively simple scenarios, and the demonstrated diversity of the trained experts is limited. The environments used, while perhaps challenging in some aspects, do not fully demonstrate the potential of the proposed method in complex, high-dimensional tasks. The diversity of the learned behaviors is not thoroughly analyzed, and it is not clear if the different experts are truly learning distinct strategies or simply converging to similar solutions.

### Questions
1. What is the goal of the method? Is it trying to discover diverse solutions or seek experts for different contexts/tasks?
2. What is the definition of a expert and how it is executed in certain context/task.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
