# Sensitivity-Constrained Fourier Neural Operators for Forward and Inverse Problems in Parametric Differential Equations

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Parametric differential equations of the form $\partial{\textbf{u}}/\partial{t} = f(\textbf{u}, \textbf{x}, t, \mathbf{p})$, where $\mathbf{p}$ represents physical system parameters, are fundamental across scientific and engineering disciplines. Recent advances in surrogate modeling, particularly deep learning frameworks like the Fourier Neural Operator (FNO), have demonstrated significant efficiency in approximating differential equation solution paths $\textbf{u}$. However, these approximations result in inaccurate solutions to inverse problems (using neural operators in an optimization routine for estimating physical system parameters), provide inaccurate estimates of \emph{sensitivities} (i.e., $\partial{\textbf{u}}/\partial{\textbf{p}}$: the dependence of the solution path on the physical parameters) needed for scenario analysis and optimization, and are highly sensitive to concept drift. These issues are all related and can be addressed by using a novel \emph{sensitivity loss} regularizer that we propose in this paper. This regularizer works with a wide range of neural operators, but for concreteness, we focus on applying it to the popular FNO framework, resulting in \emph{Sensitivity-Constrained Fourier Neural Operators} (SC-FNO). SC-FNO ensures accuracy in the solution paths, inverse problems, and sensitivity calculations, even under sparse training data or concept drift scenarios. Our approach maintains high accuracy for the solution paths $\mathbf{u}$ and significantly outperforms both the original FNO and FNO combined with Physics-Informed Neural Network (PINN) regularization on the remaining tasks.

Notably, in parameter inversion tasks from solution paths, SC-FNO exhibits markedly superior accuracy, even when FNO breaks down, underscoring the critical role of sensitivity awareness. For cases with more parameters (82 tested), SC-FNO can reduce training data demand, elevate the performance ceiling of neural operators, and even reduce training time. These conclusions are robust for various differential equations, neural operators, and different ways of supervising sensitivities for training.
These improvements, without large computational or memory costs, enhance the reliability and applicability of neural operators in complex physical systems modeling and engineering analysis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the author proposes a sensitivity loss as a regularizer for Fourier neural operator, called SC-FNO. Specifially, the sensitivity is measured by the derivative (jacobian) du/dp, where p is the physical parameter. The jacobian du/dp is computed via auto differentiation. Experiments are conducted on 2 ODEs and 2 PDEs. It shows that SC-FNO outperforms previous FNO and Pinn-FNO.

### Strengths
- This paper examines a notable case involving the system parameter $P$, where $ \frac{du}{dp} $ is computed as a sensitivity loss to regularize the model.
- The results indicate that SC-FNO achieves greater accuracy in $ \frac{du}{dp} $ and demonstrates enhanced robustness against perturbations in $p$.
- This approach aids inverse modeling in identifying the system parameters more effectively.

### Weaknesses
### Writing
The overall writing quality could be enhanced, with several important details suggested to be moved from the appendix into the main text.
- The physical parameter $P$ is central to the study and should be introduced more thoroughly. Currently, it is presented in a general form, but it’s important to clarify whether $P$ is a scalar in $\mathbb{R}$, a vector in $\mathbb{R}^d$, or a function in $L(\mathbb{R})$.
- Starting with a concrete example in the introduction would improve clarity and reader engagement.
- On Page 5, while introducing the ODEs and PDEs, the nature of the parameter $P$ remains ambiguous. Explicitly writing out the equation would help clarify its role.

### Methods
- It is unclear how $P$ is incorporated into the FNO model. If $P$ is a scalar, is it treated as a constant function and added as an additional channel?
- Computing the derivative requires additional runtime and memory, which should be discussed in detail.

### Experiments
- SC-FNO appears to achieve higher accuracy primarily on $\frac{du}{dp}$ but not significantly on the solution $u$ itself.
- Runtime and memory usage should be addressed, especially in comparison to alternative approaches.

### Questions
- What are the runtime and memory consumption, and which is the primary factor to consider?
- Can the model handle functional input such as $ \frac{du}{du_0} $? In this case, the Jacobian could be huge.
- Can the model account for parameters like the Reynolds number or viscosity as $P$?
- Can the model work on chaotic system such as the lorenz system, where the underlying parameter is very sensitive?

---
updates: the rebuttal addressed most of my questions. I am happy to raise my score to 8.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose a regularization technique that examines the gradient of the solution function with respect to parameters in differential equations. To the best of my knowledge, this approach to sensitivity regularizer, aimed at enhancing the generalization ability of neural operators, is unique. The paper is well structured, with clear motivation and objectives.

### Strengths
The study addresses the limitations observed when Fourier neural operators, combined with a physics-informed loss function, may yield suboptimal performance. The proposed regularization method appears to mitigate these challenges effectively.

### Weaknesses
The proposed approach requires additional information and computational resources, as it leverages direct solution-based information, such as a precomputed Jacobian in the differentiable numerical solver (Eq, (6)).

Another concern is the regularizer’s potential weakness to noise in practical settings. Derivative-based techniques are typically vulnerable to data noise, which could affect prediction accuracy, especially in applications beyond simulation, such as parameter inversion. In real-world applications, obtaining accurate derivative information can be challenging. While the finite difference methods employed in this paper are an option, they may perform poorly under noisy conditions.

### Questions
1. Could the authors elaborate on the approach to ensure fair comparisons between the standard Fourier neural operator and the proposed method in Tables 1, 2, and 3? Including details on training times, model complexity, and the number of learnable parameters would enhance the rigor of the paper. 

2. Higher-order derivatives might be utilized in constructing the loss function (as in Equation (6)). It would be beneficial if the authors discussed the potential advantages or limitations of incorporating these higher-order terms. 

3. Although Fourier neural operators are generally applicable to rectangular domains, other neural operators are available even for non-rectangular domains. Given that the authors provided results using DeepONet in D.6, could they consider including experiments across various domain shapes or grid resolutions to further validate the robustness of the proposed approach?
 
4. Has the proposed method been tested in scenarios involving bifurcation, where small parameter changes induce rapid solution changes (e.g. the exponential model y’=py with p near zero)? 

5. The computational cost associated with this model may increase significantly as the number of parameters grows, or if parameters are represented as functions rather than scalars. While results are presented for a four-parameter case in Table 1, could authors consider examining more complex cases – such as those with over ten parameters, function-based parameters, or parameters with probability density function across a range?

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
This paper introduces a sensitivity loss regularizer for neural operators, specifically applying it to the Fourier Neural Operator (FNO) framework, resulting in Sensitivity-Constrained Fourier Neural Operators (SC-FNO). SC-FNO improves accuracy in solution paths, inverse problem-solving, and sensitivity calculations, even under sparse data and concept drift. It outperforms both standard FNO and FNO with PINN regularization in parameter inversion tasks, achieving high accuracy without large computational or memory costs. These enhancements extend the applicability and reliability of neural operators in modeling complex physical systems.

### Strengths
1. The paper's proposed Sensitivity-Constrained approach is applicable to various neural operators, offering high research value.
2. The paper is clearly written, with no redundant mathematical derivations, and offers excellent readability.
3. In modeling PDEs, this approach not only enables accurate approximation of the target variable but also effectively models its derivatives.

### Weaknesses
1. There is no enough discussion on the memory overhead introduced by AD (Automatic Differentiation) and FD (Finite Differences).
2. The experiments are limited. It is not sure whether this method remains effective in complicated and high-resolution PDE scenarios.

### Questions
In above part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a sensitivity-constrained loss in the original FNO model, making it suitable for ODE/PDE inversion problems. Definitely this loss can make the prediction more stable with respect to the physical system parameters. This loss works with a wide range of neural operators and other supervising sensitivity tasks. The paper is well-written. The method is effective compared to the original FNO and FNO-PINN. The experiments on five ODE/PDE problems are impressive.

### Strengths
1.The paper focus on the sensitivity prediction to physical ODE/PDE systems, which is important. 

2.The paper’s contribution is clear, and the paper is easy to follow.

3.The experiments are diverse.

4.The paper’s improvements help enhancing the reliability and applicability of neural operators in complex physical systems modeling and engineering analysis.

### Weaknesses
1.The idea of using gradient loss to guarantee sensitivity is not new, such as the gradient PINN and others. 

2.The sensitivity loss is supervised, which means additional labeled data {\partial u}/{\partial p} are needed compared to original FNO. On the other hand , if we have additional labeled data, it is directly to add the supervised loss in the total loss, which is SC-FNO exactly, so I think the novelty is rather limited. Although the {\partial u}/{\partial p}  can also be approximately computed from the original data, the numerical error influence is not analyzed. On the contrary, the PINN loss is unsupervised.

3.The SC-FNO loss is hybrid, the training process should be reflected in the main text or appendix. SC-FNO should be hard to train compared to FNO, but the author didn’t mention the difference.

4.Since the PINN-FNO also add the PINN loss as the regularizer to guarantee the prediction of physical parameters, I wonder why it behaves bad to SC-FNO. Maybe the training difficulty is different. The author use a learnable coefficients combination of the hybrid loss Liebel & Körner (2018) in Algorithm 3, but FNO-PINN may be trained well for adaptive hybrid loss as in Wang S, Wang H, Perdikaris P. Improved architectures and training algorithms for deep operator networks[J]. Journal of Scientific Computing, 2022, 92(2): 35.

5. SC-FNO architecture,  as well as the Algorithm, should be exhibited in the main text,  not the appendix.

### Questions
See in the weaknesses 2-4.

Why use R^2 as metric, why not the relatively L^2 norm as in the original FNO paper？The metric should be comparable to existing works.

### Soundness
2

### Presentation
2

### Contribution
3
