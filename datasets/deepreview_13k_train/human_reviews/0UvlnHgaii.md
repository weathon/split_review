# Toward Exploratory Inverse Constraint Inference with Generative Diffusion Verifiers

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
An important prerequisite for safe control is aligning the policy with the underlying constraints in the environment. In many real-world applications, due to the difficulty of manually specifying these constraints, existing works have proposed recovering constraints from expert demonstrations by solving the Inverse Constraint Learning (ICL) problem. However, ICL is inherently ill-posed, as multiple constraints can equivalently explain the experts' preferences, making the optimal solutions not uniquely identifiable. In this work, instead of focusing solely on a single constraint, we propose the novel approach of Exploratory ICL (ExICL). The goal of ExICL is to recover a diverse set of feasible constraints, thereby providing practitioners the flexibility to select the most appropriate constraint based on the needs of practical deployment. To achieve this goal, we design a generative diffusion verifier, which guides the trajectory generation process using the probabilistic representation of an optimal constrained policy. By comparing these decisions with those made by expert agents, we can efficiently verify a candidate constraint. Driven by the verification feedback, ExICL implements an exploratory constraint update mechanism that strategically facilitates the diversity within the collection of feasible constraints. Our empirical results demonstrate that ExICL can seamlessly and reliably generalize across different tasks and environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes ExICL to tackle Inverse Constraint Learning problem, which aims to recover a diverse set of feasible constraints through an exploratory constraint update mechanism. The designed generative diffusion verifier utilizes the guided sampling strategy to verify the feasibility of explored constraints. This paper also aims to guarantee the robustness of feasible constraints discovery by accurately estimating the cost of noisy trajectory.

### Strengths
1. Introduction clearly states the current issues in Inverse Constraint Learning and the related works section is complete.
2. The experiments are comprehensive, demonstrating the effectiveness of the proposed approach.

### Weaknesses
1. The contributions claimed in this paper are not apparent to me. Contents in 4.1 is quite close to what has been proposed in [1], and the non-convex objective theorem is inherited from [2]; the ambiguity of how things are defined in section 4.2, 4.3 impairs the significance of contributions again. There are many math notations are not defined or briefly mention. I will list each of them below in the question section. I found it confusing and hard to see how the idea works.
2. Again, theorem 4.1 seems related to some existing conclusion from Paternain's paper [2], and this theorem is critical as it supports the zero duality gap for non-convex objective. The theorem stated in this paper is not quite the same as what is shown in [2], as the constraints here are not constant but are functions, but constants in [2]. There is supposed to be a connection shown here to support the theorem or a direct proof. A typo follows the theorem in Equation (9): $\lambda\epsilon$ might be missing at the end in the exponential term.

### Questions
1. My biggest confusion is about how the reward and cost are defined, respectively. Usually reward is defined as the negative cost if cost is positive, but in this paper, it seems not. Can you explicitly show how they are defined and how different they are?
2. In section 4.2, on line 286, how is $\phi_\omega(s_t^i, a_t^i, i)$ defined? 
3. In section 4.3, can you explicitly give the expressions for dist$[1, \phi_\omega(s_t, a_t)$ and dist$[\tilde\phi_\omega(s_t, a_t), \phi_\omega(s_t, a_t)])$?
4. In algorithm 1, ``Updating $\lambda$ by minimizing the loss $\mathcal{L} = \lambda \mathbb{E}_{\hat\tau\sim \tilde{p}_M}[c(\tau) - \epsilon]$, why is no reward term involved here to update $\lambda$? Another question related to this in Table 2: there is a significant discrepancy between the magnitudes of the Reward and Cost. Could you provide some insight into this?

### Soundness
2

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
The paper tackles the safe reinforcement learning problem using a diffusion model and guidance to train a set of feasibility functions. Unlike traditional inverse constraint learning, which is difficult to verify whether a candidate constraint is feasible and returns a single constraint, the paper's algorithm rapidly recovers a diverse set of constraints once the diffusion model is trained on expert data. The paper's algorithm outperforms baselines on constrained mazes and Mujoco experiments regarding performance and sample efficiency.

### Strengths
- The idea of amortizing the ICL loop cost by pre-training a diffusion model is interesting.
- The paper provides convincing empirical results that show the superiority of their method compared to the baselines of their experiments, both for reward and cost. It also investigates how reliable feasibility functions are on expert non and non-expert data.
- While they have not directly demonstrated the advantages of having multiple constraint candidates returned by the algorithm (aside from possibly making search more efficient), this seems like a practical feature to have for real world use cases.

### Weaknesses
 - While the authors list computational concerns as one of the advantages Ex-ICL has over ICL, they do not conclusively show Ex-ICL's computational advantage. Figure 6 shows that Ex-ICL is more sample efficient in constraint inference, but a true test of computational efficiency should also take into account diffusion model training time. The paper does not provide a clear comparison of the wall-clock time required for training the diffusion model versus the time saved by the amortized inference, making it difficult to assess the overall computational benefit.
- The experiments on maze and Mujoco are comprehensive but are fairly simple. For example, the baseline paper [1] includes a more realistic experiment on traffic scenarios. The current experiments lack the complexity and diversity of real-world scenarios, making it difficult to generalize the findings to more complex tasks. The experiments should be extended to include more challenging environments to better demonstrate the robustness of the proposed method.
- There's not enough detail in the main paper or appendix on methodology (how is \phi parameterized?) Specifically, the paper lacks details on the architecture of the feasibility function, the choice of activation functions, and the number of parameters. Without these details, it is difficult to reproduce the results or understand the model's capacity and limitations.

### Questions
- How are you selecting the constraint out of the constraint pool discovered by Ex-ICL for the experiment section?
- Why does Figure 4's Ex-ICL figure have so much larger variance for bad trajectory cost value than other methods?
- How sensitive are the results to exploration coefficient \delta and exploration round m? Also, would it be instructive to showcase model performance for Ex-ICL that only searches over a single \delta?

### Soundness
3

### Presentation
2

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
The authors consider inverse constraint learning, and improve on previous work by constructing an algorithm that can generate a set of constraints, and verify those constraints by applying techniques developed in diffusion modelling for RL. In particular, the authors construct a guidance term that is the gradient of a set of feasiblity terms, which they can use for on the fly verification of the proposed feasilibity functions, thereby eliminating a costly second optimization loop. The authors test their proposed algorithm on a variety of RL benchmarks.

### Strengths
- The technique makes clever use of the advanatages found in diffusion techniques: being able to modify the policy at run time by applying guidance terms
- The paper strikes a good balance of building a new method out of existing elements.

### Weaknesses
The authors seem to omit some details of their mechanism, which I think are quite crucial to the paper. These are:
- how is reward treated? Is a separate reward model that is (1) differentiable, and (2) conditioned on diffusion time (i in the author's notation) trained following Janner et al? These details are not present in Alg. 1, but are necessary to evaluate the gradient p_Mc in eqns (9) and (10).
- It is also not made clear whether in (9) and (10) the feasibility functions and reward are made to condition on diffusion time i, as I would expect it should since only tau_i is available at i.
- After algorithm 1 is complete, how is the final policy constructed for the experiments? Perhaps this is as simple as running eqn. (9) and (10) a final time, but this is not specified either.
- After algorithm 1 completes, how are constraints chosen by the practitioner as the abstract says? How do the authors choose what constraints they apply when sampling their final evaluations? This is stated in the abstract but is not discussed in the paper at all.
- How is constrained data collected? Is there an expert that already includes the constraint?

Minor:
- A few scattered grammar errors could be addressed

### Questions
See also questions under "weaknesses"
- Do the authors have some intuition why their method seems to outperform baselines significantly for HalfCheetah, marginally for Limited-Walker and only ties for Blocked-Ant?
- In the MuJoCo experiments, is the reward presented in Table 2 the feasible reward? I.e. are rewards truncated after a constraint has been violated? It seems that that would be the more inveresting metric to report, I would recommend the authors report that metric, and if they already do so make it clear it is that metric.

### Soundness
3

### Presentation
3

### Contribution
3
