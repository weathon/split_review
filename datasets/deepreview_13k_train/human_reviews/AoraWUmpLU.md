# Exploring the Impact of Activation Functions in Training Neural ODEs

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Neural Ordinary Differential Equations (ODEs) have been successful in various applications due to their continuous nature and parameter-sharing efficiency. However, these unique characteristics also introduce challenges in training, particularly with respect to gradient computation accuracy and convergence analysis. In this paper, we address these challenges by investigating the impact of activation functions. We demonstrate that the properties of activation functions—specifically smoothness and nonlinearity—are critical to the training dynamics. Smooth activation functions guarantee globally unique solutions for both forward and backward ODEs, while sufficient nonlinearity is essential for maintaining the spectral properties of the Neural Tangent Kernel (NTK) during training. Together, these properties enable us to establish the global convergence of Neural ODEs under gradient descent in overparameterized regimes. Our theoretical findings are validated by numerical experiments, which not only support our analysis but also provide practical guidelines for scaling Neural ODEs, potentially leading to faster training and improved performance in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents several theoretical results about Neural ODEs, built around sufficient regularity of activations:
- It proves that "optimize then discretize" setting, built upon the use of classical ODE solvers, is well-posed under the assumption of Lipschitz-continuous activations (proposition 1).
- It proves that "discretize-then-optimize" setting, built as an Euler scheme discretization of the ODE by growing the depth of a residual neural network, is also well posed in the sense that the solution of the discretization scheme converges to the actual solution of the ODE in the infinite depth limit, if the activations and there derivatives are lipschitz-continuous (proposition 2). It has to be noted that authors gives explicit convergence rates.
- It shows that under the "discretize-then-optimize" setting with fixed depth L, the associated residual network converges in infinite width limit to a fixed kernel with explicit form, under the assumption of Lipschitz continuity of activations (proposition 3).
- It shows that under the assumption of Lipschitz continuity of activations, the infinite depth and width limits commute, implying that the neural ODE converges to a Gaussian process with covariance given as the infinite depth limit of the covariance of proposition 3 (theorem 1).
- Similar results are shown for the convergence of the NTK (proposition 4 and theorem 2)
- In section 5, authors show that the resulting limiting covariance of the gaussian process as well as NTK are Semi-positive definite (lemma 3, proposition 5, corrolary 1), resulting in derivation of explicit convergences rates (theorem 3).
Finally empirical evidences of the theoretical results are presented in section 6.

### Strengths
- precise, rigorously demonstrated theoretical results
- clear presentation
- extension of fundamental NTK results to neural ODEs, using classical ODE analytical tools (Picard theorem, Groenwald theorem etc).

### Weaknesses
 - Typo : the index of the last h in equation 1 should probably be T instead of t
- Figure 1 : a,b,c should rather be in log-log scale to better appreciate the slope comparison with 1/L.
- I don't think it's quite right (or at least I don't understand exactly why, but I'm not a specialist in Neural ODEs) that the title of the paper focuses on the impact of activations and their regularities, whereas most of your results use these as hypotheses for theorem proving. In my opinion, you should assume a more theoretical title (or present more results comparing activations, but it seems to me that this is a slightly different job than what you present, which is amply sufficient from a theoretical point of view).

### Questions
I don't think it's quite right (or at least I don't understand exactly why, but I'm not a specialist in Neural ODEs) that the title of the paper focuses on the impact of activations and their regularities, whereas most of your results use these as hypotheses for theorem proving. In my opinion, you should assume a more theoretical title (or present more results comparing activations, but it seems to me that this is a slightly different job than what you present, which is amply sufficient from a theoretical point of view).

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the role of activation functions in the training dynamics of Neural ODEs, particularly focusing on the convergence and stability properties of two key methods: "Optimize-then-discretize" and "Discretize-then-optimize." The authors establish theoretical guarantees for the convergence of both methods under certain conditions on the activation functions, and they provide numerical experiments to support their findings.

### Strengths
Theoretical Analysis: The paper offers a rigorous mathematical analysis of the well-posedness of Neural ODE solutions and their gradients, focusing on the impact of activation function smoothness. The authors clearly demonstrate the importance of Lipschitz continuity for both the activation function and its derivative to ensure stable and accurate gradient computation.

NTK Analysis: The paper extends the concept of the Neural Tangent Kernel (NTK) to the continuous setting of Neural ODEs. This is a valuable contribution, as it provides insights into the training dynamics of these models. The authors show that the NTK converges to a deterministic limit under certain conditions, which helps explain the convergence properties of gradient descent in Neural ODE training.

Global Convergence Proof: The authors establish the global convergence of Neural ODEs under gradient descent in the overparameterized regime, under assumptions about the activation function's nonlinearity and non-polynomial nature. This theoretical result provides a strong foundation for understanding the optimization behavior of Neural ODEs.

Empirical Validation: The paper presents several numerical experiments to validate the theoretical findings. These experiments demonstrate the convergence of Neural ODE outputs and gradients to their finite-depth ResNet approximations, the behavior of the NTK, and the convergence properties of Neural ODEs under gradient descent.

### Weaknesses
Lack of Demonstration for "Discretize-then-optimize" Convergence Issue: While the paper theoretically analyzes the convergence problem of "Discretize-then-optimize" with non-smooth activation functions, it does not provide a dedicated numerical experiment to showcase this issue. This would be valuable for empirically confirming the theoretical claims and for understanding the practical implications of using non-smooth activations with this method.

The lack of a numerical demonstration of the "Discretize-then-optimize" convergence problem weakens the overall impact of the paper. Without empirical evidence, the theoretical claims regarding the convergence issue remain unsubstantiated, and the practical implications of using non-smooth activation functions with this method remain unclear.

### Questions
1.
Could you provide a numerical experiment that specifically highlights the convergence problem of the "Discretize-then-optimize" method when using an activation function that does not meet the Lipschitz continuity requirements? This would strengthen the paper by providing empirical support for your theoretical analysis.

2.
How does the choice of numerical ODE solver in the "Optimize-then-discretize" method impact the accuracy of the gradient computation and the overall training dynamics? Exploring the sensitivity of the method to different solvers would be valuable.

3.
What are the practical implications of your findings for the choice of activation functions in real-world applications of Neural ODEs? Providing guidance on activation function selection based on the desired trade-off between theoretical guarantees and empirical performance would be beneficial.

Addressing these points would significantly improve the paper and provide a more comprehensive understanding of the impact of activation functions on Neural ODE training.

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
The authors studied activation functions in the training dynamics of neural ODEs. They showed that the choice of activation function has significant impacts on the dynamic and asymptotic behavior. Additionally, they propose a new mathematical framework to study continuous models from the perspective of approximation theory. Finally, the authors conduct experiments to empirically validate their theoretical results.

### Strengths
The paper is well-written. The ideas presented are novel and represent a significant contribution in the context of neural ODEs. The main strength is the theoretical foundation of the work.

### Weaknesses
The proofs are generally well-written and clear, but since they are in the appendix, the flow of the paper's main narrative can sometimes be interrupted.

### Questions
No questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies the convergence of gradient descent for training neural ODEs from the neural tangent kernel perspectives, with experimental results validating the theoretical claims.

### Strengths
(1) The paper extends NTK theory from general regression problems with ReLU nets to Neural ODEs with ResNet architectures. The analysis and results are novel for Neural ODEs.

(2) The empirical results validate the theorems.

### Weaknesses
(1) Some prior work has extended NTK theory to analyze CNNs (for image classification tasks), PINNs, Transformers, and various gradient-based algorithms beyond vanilla gradient descent. However, related references are missing. Specifically, the paper should discuss how its analysis compares to existing NTK results for convolutional architectures, which are commonly used in image-based neural ODEs, and also for sequence models like Transformers, given their relevance to time-series data. Furthermore, the analysis should be contextualized with respect to the growing body of work on NTK theory for physics-informed neural networks (PINNs), which also involve solving differential equations.

(2) SGD is more commonly used in practice, making a convergence analysis of SGD particularly valuable and interesting. The current analysis focuses solely on gradient descent, which is a simplified optimization method. A discussion on how the results might extend to SGD, or what challenges might arise in such an extension, would significantly enhance the practical relevance of the paper. This should include a discussion on the impact of mini-batch size and noise on the convergence behavior.

(3) The results are specific to ODEs of the form given in Equation (2). Theorem 2 does not hold for PINNs if the underlying PDE is nonlinear. How would Theorem 2 apply if the ODE were not limited to this special case? The paper needs to address the limitations of the current analysis in the context of more general ODEs and PDEs. Specifically, it should discuss the conditions under which the current analysis might fail for more complex systems, and what modifications would be necessary to extend the results to these cases. For example, the paper should address the challenges in analyzing systems with non-autonomous dynamics or with higher-order derivatives.

(4) This paper claims that the nonlinear and non-polynomial nature of the activation function is crucial for convergence. However, I believe the convergence results (Theorem 3) may also hold with polynomial activation functions, provided that Condition (1) of Assumption 1 is further strengthened to ensure linear independence. The paper should provide a more rigorous justification for the necessity of non-polynomial activations, or at least acknowledge the possibility of convergence with polynomial activations under specific conditions. The current discussion is not sufficiently nuanced, and further clarification is needed.

(5) From the title, the topic of the paper is exploring the smoothness of activation functions in neural ODEs. However, after reading your paper, your main contribution is developing the global convergence of GD in training neural ODEs. The title is quite strange...

### Questions
See weakness.

### Soundness
4

### Presentation
4

### Contribution
3
