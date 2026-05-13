# Maximum Entropy Model Correction in Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
We propose and theoretically analyze an approach for planning with an approximate model in reinforcement learning that can reduce the adverse impact of model error. If the model is accurate enough, it accelerates the convergence to the true value function too. 
		One of its key components is the MaxEnt Model Correction (MoCo) procedure that corrects the model’s next-state distributions based on a Maximum Entropy density estimation formulation. Based on MoCo, we introduce the Model Correcting Value Iteration (MoCoVI) algorithm, and its sampled-based variant MoCoDyna. We show that MoCoVI and MoCoDyna’s convergence can be much faster than the conventional model-free algorithms. Unlike traditional model-based algorithms, MoCoVI and MoCoDyna effectively utilize an approximate model and still converge to the correct value function.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method for planning with an imperfect model, called MaxEnt Model Correction (MaxEnt MoCo). It *corrects* the next-state distribution of the model such that its expected value aligns with the true environment. This is achieved through Maximum Entropy density estimation.

Building on top of MaxEnt MoCo, they propose Model Correcting Value Iteration (MoCoVI) and the sample-based variant Model Correcting Dyna (MoCoDyna). Both methods iteratively update the basis function, using the value functions derived from MaxEnt MoCo.
Theoretical analysis suggests that the MoCoVI may converge to the true value function at a faster rate than approximate VI, under specific conditions. The efficacy of the proposed methods is empirically validated in a 6x6 grid world environment.

### Strengths
1. The paper delivers rigorous theoretical results.

2. The approach is novel to the best of my knowledge.

3. The paper is overall well organized, making it relatively easy to follow.

### Weaknesses
1. I am not fully convinced by the potential faster convergence of MoCoVI than VI. 

    Let’s say that the model is perfect, why should MoCoVI enjoy a faster convergence? Also, in Theorem 2, the comparison between the order of $\gamma'$  and the order of $\gamma$ could be oversimplified. For instance, the constant could matter: the big O hides the constant $(3\sqrt{2})^K$ which could become significant.  Besides that, the $\gamma'^K$ also hides $(\frac{1}{1-\gamma})^K$ but is not addressed in the paper.

    Another concern is regarding the maximum of the ratio over K steps in $\gamma'$. Can the authors comment on the implications of it on the robustness of the algorithm?

2. The gap between theory and experiments: the theoretical analysis suggests applicability to both finite and continuous MDPs, yet experimental validation is confined to a small-scale tabular MDP. Broadening the experimental scope to include continuous MDPs would substantiate the theoretical findings more comprehensively.

3. The requirement in MaxEnt MoCo to sample the dynamics `d` times for each state-action visited, seems to restrict its practical applicability.

4. The paper could be improved with additional clarifications in certain sections. I would ask the authors to help address the following:

    a. Is there any assumption on the action space? It does not appear to have been stated in the paper, except for MoCoDyna where Algorithms 1 assumes a finite MDP. It appears that there's an implicit assumption that MaxEnt MoCo and MoCoVI are applicable to both finite and infinite action spaces. However, the approximate VI method that MoCoVI is compared with, traditionally assumes a finite action space [Munos 2007]. Could the authors clarify why the finite action space assumption is not necessary for MoCoVI?

    b. The introduction claims that the theoretical analysis is applicable to “both finite and continuous MDPs”. Does this applicability refer to both the exact and approximate versions of the proposed methods? Considering the complexity often associated with analyzing continuous spaces in RL, a further explanation on how the proposed analysis overcomes these challenges would be beneficial.

    c. The algorithm for MoCoDyna, as presented in Section 5, is specific to finite MDPs, yet prior analysis encompasses both finite and continuous MDPs. The paper suggests the possibility of extending MoCoDyna to incorporate function approximation without elaborating on the approach. Could the authors clarify if the focus on finite MDPs is solely for the sake of a simpler presentation, or are there inherent difficulties when adapting the algorithm to function approximations?

    d. The significance of the additional `c` features in the `d+c` features in MoCoDyna is not clear. Could the authors provide clarifications, and guidance on how to select `c`?

    e. The paper assumes that we can make exact queries to P in MoCoVI. Yet, the algorithm description only has approximation $\psi$ and lacks details on how $\psi$ is updated.

Minor:

It would be beneficial if the algorithmic procedures for MaxEnt MoCo and MoCoVI were presented (perhaps in the appendix) in a structured algorithm format, similar to MoCoDyna. 

Typos:

1. Is the $|| V^{\pi_{PE}} ||_\infty$ before Sec. 3.2 missing anything?

2. Sec. 3.2: domain of $\phi$ should be $\mathcal{X}$ $\times \mathcal{A}$ instead of $\mathcal{X}$.

3. Sec. 3.1: in the equation at the end of paragraph 1, the expectation should be w.r.t. $\bar{P}$.

### Questions
Please see the weakness section for my questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method for MBRL, where a correction of the model is learnt. The correction improves the distribution of the next state prediction. The work consists of a model correcting approach, and its application to value iteration and to a dyna-based approach. A benefit of the approach is the combination of a model with a faster convergence thanks to the use of a model. The model-correcting prediction helps to keep the model close to the true dynamics of the environment.

### Strengths
The work is well motivated and the introduction / background are concise yet provide enough detail to set the scene. The paper is well, logically written. At times, it leads to a question (eg isn't computing this for all (x,a) expensive?, in the intro), to later answer the question. The approach is interesting and improves over conventional approaches. Good theoretical contributions.

The appendices are useful, equally logically structured, and contain additional analysis and proofs.

### Weaknesses
The main weakness in my view is the limited number of experiments, moreover the experiments are relatively simple.  I would have liked to see how the approach is used and how its performs (also in terms of time) for large or continuous environments (which seems to be planned for future work).

I'm not quite sure about the related work and comparison to approaches that use multiple models to improve predictions, which would be a more appropriate comparison (apart from OS-VI, eg residual models or even ensemble models), along with a comparison of computational costs (during training or inference). Even the additional empirical results in the appendix are not particularly large.

### Questions
- In the introduction, you say MaxEnt MoCo first obtains $E[\phi_i(X')]$ for all $(x,a)$. That sounds expensive and seems to be computed on demand; but what is the cost of solving the lazy approximation (P1).
- Can you comment about computational cost and scalablity of the approach given that the experiments were limited?
- I may have missed it but would it make sense to compare how close the dynamics of the real environment with the predicted and corrected one? If that's the case, evaluations of how well the environment can be predicted might be helpful even without additional results from RL experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Value Iteration (VI) and Dyna-style sample-based version utilizing an approximate environmental model. Under the assumption that the approximate model $\hat{\mathcal{P}}$ is given, a corrected model $\bar{\mathcal{P}}$ is derived by minimizing the KL divergence $D_{KL} ( \cdot \parallel \hat{\mathcal{P}})$ with feature matching constraints. The proposed method, MoCoVI and MoCoDyna, employ the corrected dynamics to learn a state value function. Then, the value function trained with the corrected dynamics is used as a new basis function used in the feature matching constraints. MoCoVI and MoCoDyna are compared with OS-VI and OS-Dyna, respectively, on the modified Cliffwalk environment. The experimental results show that the proposed methods converge to the true value function faster than the baselines.

### Strengths
The motivation is well explained, and the paper is overall well-written and well-organized. The proofs given in the supplementary materials are complicated, but the authors provide a detailed explanation.

### Weaknesses
The proposed method is evaluated on the modified Cliffwalk environment that is relatively small. I am unsure if the proposed method is scalable, particularly concerning the optimization procedure in MaxEnt MoCo. The computational cost of correcting each sample in the model and the overall impact on training time needs further clarification. While the dual problem having only *d* parameters is mentioned, the practical implications of this in larger environments are not entirely clear. The scalability concern is especially relevant when considering the potential need for parallelization and adjusting the computation cost mentioned in the author's response. A more thorough analysis of the computational complexity and memory requirements would strengthen the paper.


The function approximator for the value function is unclear. The authors state that $V$ is never approximated by $\sum_{i}^d w_i \phi_i$. However, the role of the basis functions and how they contribute to the value function estimation needs further elaboration. The concern about adding $V$ as a new basis function at the next iteration and its potential linear dependence on the existing basis functions is valid. Although the authors suggest a workaround with a properly designed BasisCreation function, the specific implementation details and potential issues are not discussed in the paper.


On page 4, the authors mentioned that the number of basis functions, $d$, is usually small, but I am unsure whether it is true in general. It is unclear how *d* would be chosen in practice, especially in tasks with huge state spaces. The modified Cliffwalk environment appears to be a toy problem, and the authors' claim that *d* would remain small in more complex environments needs further justification. The trade-off between the number of basis functions, the accuracy of the query results, and the computational cost of the correction procedure should be explicitly addressed.


The paragraph below equation (3.2) contains the sentence: $\bar{\mathcal{P}}$ is not constructed by the agent. This statement is unclear and requires further explanation. It would be helpful to clarify how the agent utilizes $\bar{\mathcal{P}}$ without explicitly constructing it.

### Questions
1. At the $k$-th iteration, the proposed method uses the basis functions $\phi_{k+1:k+d}$ and the query results $\psi_{k+1:k+d}$ to obtain $V^k$. I would like to know why $\psi_{1:k}$ and $\psi_{1:k}$ are discarded. Would you discuss this point?
2. The function approximator for the value function is unclear. Is $V$ approximated by $\sum_{i}^d w_i \phi_i$? If so, adding $V$ as a new basis function at the next iteration is problematic because it is linearly dependent on the basis functions. 
3. On page 4, the authors mentioned that the number of basis functions, $d$, is usually small, but I am unsure whether it is true in general. I do not know the details of the modified Cliffwalk environment, but I think it is a toy problem. Is $d$ still small if the proposed method is applied to tasks with huge state space?

The following are minor comments.
- The end of the second paragraph in Section 2.2: $\phi(Z)$ should be $\phi_i(Z)$. 
- The paragraph below equation (3.2): I do not understand the following sentence: $\bar{\mathcal{P}}$ is not constructed by the agent.
- In the first paragraph of Section 3.2, the authors define the function $\phi: \mathcal{X} \to \mathbb{R}^d$, but $\phi (x, a)$ is used to compute $\epsilon_{\mathrm{Model}}(x, a)$. Is it a typo?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
