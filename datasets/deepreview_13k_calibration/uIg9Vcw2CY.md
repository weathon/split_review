# BiLO: Bilevel Local Operator Learning for PDE inverse problems

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
We propose a new neural network based method for solving inverse problems for partial differential equations (PDEs) by formulating the PDE inverse problem as a bilevel optimization problem. At the upper level, we minimize the data loss with respect to the PDE parameters. At the lower level, we train a neural network to locally approximate the PDE solution operator in the neighborhood of a given set of PDE parameters, which enables an accurate approximation of the descent direction for the upper level optimization problem.
The lower level loss function includes the L2 norms of both the residual and its derivative with respect to the PDE parameters. 
We apply gradient descent simultaneously on both the upper and lower level optimization problems, leading to an effective and fast algorithm. The method, which we refer to as BiLO (Bilevel Local Operator learning), is also able to efficiently infer unknown functions in the PDEs through the introduction of an auxiliary variable.
Through extensive experiments over multiple PDE systems, we demonstrate that our method enforces strong PDE constraints, is robust to sparse and noisy data, 
and eliminates the need to balance the residual and the data loss, which is inherent to the soft PDE constraints in many existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates a method for parameter identification in PDEs (similar to optimal control). The idea is to replace the PDE constraint with novel functional that penalises both the residual as well as the derivative of the residual with respect to the parameters. The latter is local in the parameters, hence the motivation for the title of the paper. The paper also models the solution as a neural network similar to PINNS. This approach is equipped with an efficient learning strategy and initialisation. It is evaluated on various simple PDEs as well as a more complicated one related to tumour growth.

### Strengths
The problem considered is important and challenging. Across various communities do people search for efficient solutions, thus making the paper potentially significant. The paper is original in that the idea has not been considered before. The presentation is clear and the ideas do come across well. I really like the tumour growth example applying such methods to more than just box-standard applications.

### Weaknesses
The paper is based on a lot of heuristics and I have doubts that this idea in general will be useful for others solving similar problems.

1. The entire idea of local solutions is neither well-defined nor do I believe that what is being computed are local solutions in the sense that they actually solve the PDE in a neighbourhood of the parameters. Also they still use the global residual encouraging both local and global behaviour. It is not clear how to entangle the two: are both important?

2. The optimisation algorithm in general will not solve the bilevel optimisation problem. This problem has been studied for decades (or more; see the papers cited in the paper itself) and the community agrees that the proposed algorithm does not do it (in general). I agree with the arguments in the appendix but this is for a much simpler case and in my opinion will not generalise. This is why methods like the "adjoint method" etc exist. Note that this is also a current research topic in the optimisation community which investigate similar but still very different algorithms compared to the one proposed here. The paper also makes the claim that the PDE constraint "does not need to be solved to solved to optimality". I agree this is true but the statement needs to quantitative. There will be an accuracy that is needed to make sure the computed directions actually descent. This is completely ignored at present. See e.g.
Pedregosa, Fabian. "Hyperparameter optimization with approximate gradient." International conference on machine learning. PMLR, 2016.
The paper starts with a very good initial estimation of the solution which is probably the key reason why it works well in the numerical examples. I don't believe this generalises well to other problems.

Minor comments:
- line 199, typo a(x, f(x))

### Questions
1. Discuss (perhaps using numerical evidence) that indeed the solutions computed are solutions to the PDE. Also discuss (again potentially with numerical evidence) that the solutions computed are local solutions and not global solutions.
2. Discuss (perhaps using numerical evidence) what the proposed algorithm actually converges to stationary solutions (or even global minima) of the bilevel problem.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper intends to solve PDE constrained inverse problem with neural operators, which is formulated into a bi-level optimization problem. In the lower level optimization, a neural operator is learned and trained on a fixed initial guess of PDE parameter $\Theta_0$, which is named "local neural operator" by the authors. In the upper level optimization, the optimal or targeted parameter $\Theta$ is approximated.

In the experiment, the authors benchmarked their method on a tumor growth and imaging model and compared results to PINN-based method.

### Strengths
The paper basically argues for solving inverse problem with neural operators instead of PINN for both efficiency and accuracy. The support of the argument is mostly empirical. However, the experiment is well designed in both diversity and careful measurement, e.g., in addition to measuring accuracy of solution and unknow parameter (function), the author deliberately choose the initial guess that is far from ground truth in their experiment, which is a strong evidence for the effectiveness of the method.

### Weaknesses
What is the motivation of using neural operator for PDE-constrained inverse problem? Neural operator is known for its generalization on various input functions, boundary conditions, initial data, etc. However, in the setting of this paper, a "local" neural operator is learned, meaning narrow generalization ability and abandoning the advantage of neural operators. Could the authors elaborate on the advantages of using a local neural operator versus a more general neural operator in this context? What specific benefits does the local approach provide for PDE inverse problems that outweigh the loss of broader generalization ability?

Meanwhile, PINN is known for low requirement of data and being suitable for inverse problem. The experiment indeed shows that the improvement of the method proposed here over PINN is quite marginal considering noise (see Table 2&3). Given the relatively small improvement over PINN shown in Tables 2 and 3, could the authors provide a more comprehensive discussion of the advantages of their method? Are there specific scenarios where the proposed approach significantly outperforms PINN that may not be captured in the current experiments?

Also, how does the proposed method compare to the bi-level optimization approach for PINNs presented in [1]? Could the authors discuss the key differences and potential advantages of their method over this existing work?

### Questions
N.A.

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
4

### Summary
This paper proposes BiLO, which formulates upper and lower inverse problems into bilevel optimization. BiLO integrates adjoint methods and PINNs, while eliminating the need for balancing residual and data loss. BiLO has high robustness to sparse and noisy data, and effectively infers unknown PDE parameters and functions through auxiliary variables. Experimental results show that BiLO enforces strong PDE constraints, is robust to sparse and noisy data, and eliminates the need to balance the residual and the data loss, which is inherent to the soft PDE constraints in many existing methods.

### Strengths
- **Elimination of Residual-Data-Loss Balancing**. By separating the optimization process into two levels, BiLO eliminates the need to balance the residual and data loss;
- **Local Operator Learning**. Local PDE solution operators ensure precise gradient computation and lead to faster parameter inference.
- **Robustness**. Experimental results show that BiLO can handle noisy measurements and unseen data. 
- **Generalization Power**. The proposed method could infer unknown functions (e.g., variable diffusion coefficients) with the auxiliary variables.

### Weaknesses
 - **Lack of Theoretical Guarantees**. The paper offers mainly empirical results. 
- **Scalability Concerns**. The experiments are limited to low-dimensional PDE problems. It is unclear how the method scales to higher-dimensional or more complex PDEs.
- **Computational Overhead**. Although the method achieves accurate results, solving both upper and lower-level optimization problems simultaneously introduces computational complexity.
- **Presentation**. The presentation of this paper could be further improved. The paper also seems to be completed in a rush and needs further proofreading. There are multiple typos (e.g., line 37, "... or deep learning, methods.", redundant comma) and duplicate bibitems (e.g., second and third last references on pp.15 are identical).

### Questions
- On line 177, "The use of Lu0 is not mandatory for training the local operator with fixed Θ0, though it can speed up the training process", does it mean fixed initial parameters throughout training or just during initialization?
- Scalability. How does BiLO perform on higher-dimensional PDEs? How could BiLO reduce computational overhead for large-scale problems?
- Can the authors provide a more rigorous theoretical analysis of the convergence behavior for the bilevel optimization process?
- Comparison with SOTA Neural Operators. The paper focuses on comparing BiLO with PINNs. Could the authors provide some comparison over neural operators (e.g., DeepONet, FNO)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work aims to infer parameters in parametric PDEs using some observed solution data. This type of problem is widely found in scientific and engineering applications. The authors propose a neural network method for solving inverse problems governed by partial differential equations (PDEs). This method contains two steps: the pre-train step using the data and collocation points and the fine-tune step using the automatic differentiation. The proposed approach incorporates the traits of PINN, operator learning, and the adjoint method.

### Strengths
1. This paper is well-written. 
2. The proposed method is mesh-free, avoiding the difficulties caused by mesh generation. 
3. The algorithm is easy to implement and can provide fast inference for inverse problems once it has finished training.

### Weaknesses
1. The PDE-constrained optimization problem considered in this work only involves the equality constraint, but in practice, the inequality constraints are typical, e.g., the box constraint. 
2. The pre-train step is crucial, and this step is minimizing the residual loss with collocation points. When the solution has a low-regularity property, this pre-train step will have a large generalization error if the collocation points are not properly chosen. This will overshadow the capability of the proposed method.


### Questions
1. The initial parameter $\Theta$ seems important to the propsoed method. How do you choose it?
2. Again, I wonder how the proposed method works if the initial guess of $\Theta$ is far away from the ground truth.
3. In this work, the loss function is easy to construct since the equality constraint only exists. How do you generalize your method to inequality constraints? The inequality constraints are common in practice.
4. Which grids does the observed data locate? Please clarify this issue in the numerical experiments.
5. In this work, the noise is set to the Gaussian with a small variance. How about the noise with a large magnitude? 
6. About the training procedure. The simultaneous gradient descent is applied in the fine-tuning step instead of the alternative gradient descent. Could you plot the training loss curve for this step?

### Soundness
3

### Presentation
4

### Contribution
3
