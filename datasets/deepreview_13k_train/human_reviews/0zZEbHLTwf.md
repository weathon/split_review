# DeepFDM: A scientific computing method for Neural Partial Differential Equation (PDE) operators

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Solving Partial Differential Equations (PDE) has long been a critical challenge in many scientific and engineering domains. Recently, neural networks have shown great promise in solving PDEs by learning solution operators from data, offering a flexible and adaptive alternative to traditional numerical solvers. Despite these advancements, there is still a need for systematic benchmarking of neural operator methods against conventional approaches and for the development of datasets representing diverse distributions for robust evaluation.
In this paper, we introduce DeepFDM, a benchmark method for learning PDE solution operators based on numerical PDE solvers.   
DeepFDM leverages the structure of the PDE, in order to achieve better accuracy and generalization compared to neural solvers.  It is designed as a solver for a specific class of PDEs and not as a replacement for neural solvers.  Moreover, because DeepFDM learns the coefficients of the PDEs, it offers inherent interpretability.  We also introduce a principled method for generating training and test data for PDE solutions, allowing for a quantifiable measure of distribution shifts.  This method provides a structured approach to evaluate the out-of-distribution (OOD) performance of neural PDE operators. 
Our work sets a foundation for future comparisons of neural operator methods with traditional scientific computing approaches, providing a rigorous framework for performance benchmarking, at the level of the data and at the level of the neural solver.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript considers the problem of benchmarking neural PDE solvers and analysis of the robustness with respect to the diverse distributions. The authors propose DeepFDM, a benchmark method, and the procedure to generate train/test data for benchmarking with quantified shifts in distributions. The main idea of the DeepFDM method is to represent finite difference approximation of a particular type of PDEs through a convolutional neural network that parameterizes variable coefficients. Therefore, given a ground-truth input/output pair, such a model fits the target coefficients over the used grid. The second part of the work is the procedure to generate data with a controlled distribution shift that helps evaluate the trained model's robustness to input data out of the distribution where training data was generated. In experiments, DeepFDM shows better robustness to input data distribution shifts for the broad classes of equations than competitors while requiring fewer trainable parameters.

### Strengths
1. Fair benchmarking of the neural PDE solvers and evaluation of their robustness to the input data is very important for understanding the current state of this field and identifying the gaps in the current SOTA methods.
2. The proposed DeepFDM method provides more accurate predictions than competitors
3. The benchmarking procedure is well-described and could be used in other works for evaluation of the new neural PDE solvers,

### Weaknesses
1. The main weakness of this work is that the authors combined two different contributions in a single study: a dataset generation procedure for benchmarking neural PDE solvers and a DeepFDM method for fitting the PDE coefficients. 
2. The idea of parameterizing the finite-difference method via CNN is not new and has already appeared in other works like the smoothing operator in the multigrid methodб https://arxiv.org/abs/2102.12071 
3. The proposed method's scalability is not discussed or compared with competitors.
4. The presentation of the problem statement is confusing since the authors start not from the inverse problem of coefficient reconstruction but from the solution reconstruction problem.

### Questions
1. Why do the lines in Fig. 5 start from different initial points? It looks like the authors use different initializations, which is unfair for comparison.
2. What is the motivation for using Hellinger distance, not the KL divergence, for example? KL also admits closed-form for the distance between multivariate Gaussians.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper compares the performance of an inverse design method combined with a numerical solver against neural PDE solvers. The authors assume they are given data generated from a known PDE family but with unknown, spatially dependent coefficients. In this problem setting, the paper proposes to compare neural PDE solvers against numerical simulators. Since the PDE parameters are unknown, they are estimated by minimizing the difference between the output of a differentiable numerical solver and the given data.  The experiments show that the proposed model converges quicker than the considered neural PDE solvers and achieves lower errors both on in- and out-of-distribution data.

### Strengths
A novel way of comparing neural PDE solvers against numerical methods, which is in a sense more fair to the neural PDE solvers (if the neural PDE solvers are trained on real-word data).

### Weaknesses
1. The paper is not very clear in the type of problem it approaches. The writing could be improved to make the definition of the problem more easy to understand.
2. The usual setup in neural PDE solvers is that the PDE parameters are known. In this setting, neural PDE solvers have already been compared to numerical methods. The authors could better motivate their specific choice of problem definition (i.e., unknown, spatially-dependent PDE parameters).
3. The method is only a useful baseline if the neural PDE solver is trained on real-world data. When the neural PDE solver is used as a surrogate for a numerical solver, the PDE parameters would be known (since they would have been used to generate the training data).
4. There is no inference time evaluation. Faster inference is one of the main reasons for utilizing a neural PDE surrogate instead of a numerical method like the one considered in the paper.
5. Many experimental and model details are missing (see questions).

### Questions
1. How did you condition the neural PDE solvers on the coordinate-dependent PDE parameters? By adding the spatial coordinates to the solver inputs?
2. How did you create the spatially varying PDE parameters? Using the same method as generating the initial condition?
3. What did your data look like exactly?  You mentioned 1D and 2D problems. Which PDE in Tab. 1 is 1D, which is 2D? How large was the dataset? How large were the spatial and temporal resolutions?
4. What learning rate did you use? What optimizer? Did you train the models autoregressively or with 1-step errors only?
5. How did you introduce the distribution shift? Did you increase or decrease the standard deviation of the PDE parameters? How many basis functions N did you use in the beginning? Did all of them have the same standard deviation?
6. Why is the Hellinger distance between the parameters generating the initial conditions a good measure for the distribution shift?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents DeepFDM, a benchmark approach for learning PDE solution operators that combines the structure of traditional PDE solvers with neural networks. By leveraging the strengths of scientific computing, DeepFDM offers interpretability and aims to enhance accuracy and generalization within a specific class of PDEs, rather than acting as a replacement for neural PDE solvers.

While DeepFDM is designed specifically for certain types of PDEs, it shows limited generalization to other PDE classes, reducing its applicability in diverse scenarios. Additionally, the paper lacks a detailed analysis explaining why DeepFDM outperforms traditional methods, which weakens the justification of its advantages. Providing a rigorous theoretical analysis with established approaches would strengthen the work and clarify the specific benefits of DeepFDM in terms of accuracy and generalization.

### Strengths
The paper highlights a need for benchmarking in PDE solutions, pointing out that while neural networks can flexibly solve a variety of equations, there’s limited systematic comparison with established numerical methods. This motivation is well-founded, especially in scientific and engineering fields that demand rigorous performance metrics.

 DeepFDM seems to target both in-distribution (ID) and out-of-distribution (OOD) performance, providing a structured method for generating training and test data that reflects distribution shifts. This contribution is valuable since robust OOD performance is crucial for practical applications.

### Weaknesses
DeepFDM is presented as a benchmark method; however, its applicability is limited to a specific class of partial differential equations (PDEs). The paper does not sufficiently discuss how this restriction affects DeepFDM's generalizability, particularly in scenarios that require flexibility across various forms of PDEs, such as nonlinear PDEs and complex boundary conditions.

For instance, in the case of hyperbolic equations with shock locations, finite difference methods (FDM) may struggle to accurately capture the discontinuities inherent in these solutions. This limitation could significantly impact the performance and reliability of DeepFDM when applied to a broader range of PDE types.

Please explicitly state the objectives and justify  the choice of comparison methods in the context of those objectives. More specifically,
Why do the authors compare DeepFDM to both neural networks like ResNet and Unet, as well as neural operators like FNO? It’s unclear whether the authors aim to solve individual instances of PDEs or to learn a solution operator.

### Questions
You need to compare your methods fairly with both ResNet and Unet, as well as FNO, since they represent different categories—traditional neural networks versus neural operators.

Please discuss the trade-offs between finite difference and automatic differentiation in your specific context, and to provide justification for the choice of FD and AD. There is considerable evidence that automatic differentiation outperforms FD in terms of training loss.

Can you explain why DeepFDM doesn't show oscillation in Fig. 5, unlike the other methods?
How does the computational cost and training time of DeepFDM compare to the other approaches?
Given that Fig. 5 doesn't show significant improvement, can you clarify what advantages DeepFDM offers in terms of training dynamics?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The goal of this work is to design a benchmark method for learning PDE solution operators based on numerical PDE solvers. The authors proposed DeepFDM, which focuses on one class of PDEs and takes advantage of the structure of PDEs. DeepFDM learns the coefficients of the PDEs, and distribution shifts using the Hellinger distance are quantified. The results are compared with FNO, U-Net, and ResNet.

### Strengths
The paper explores benchmarking neural operator methods and OOD performance of neural PDE operators, which is meaningful in scientific computing. 

For one family of PDEs, it provides a neural network based solver with coefficients inferred.

### Weaknesses
- The motivation of choosing the known family of time dependent PDEs with periodic boundary conditions, and bounded coefficients is not clear to me. The problem setup seems very restricted, and the method is only applicable to learn from initial conditions.
- It should be made clear that if the method is data-driven/known PDE, PDE solver/operator learning in the beginning. According to my understanding, the PDE needs to be known to use the finite differences solver. DeepFDM learns an operator from the initial condition for a specific family of PDEs to the solution at next time step, and the iteratively solve for a longer time. The problem setup should be more rigorous. 
- The literature review in Section 2.1 is not well organized or well-written. The papers of PDE discovery, PINN and operator learning are mentioned without a focus. Some claims are not correct and language is vague. For example, “Lu et al. (2019) propose the DeepONet architecture, which learns PDE solution operators. However, in this case, the PDE is fully known and the PDE residual is included in the loss.” It is not correct. There is no PDE known in vanilla  data-driven DeepONet. The authors may refer to Physics-informed DeepONet. “Neural PDE operators aim to learn to solve a given PDE from data, without assuming that the form of the PDE is known.” This claim is conflicting with the above point. 
- One main issue is that it ‘s not fair to compare DeepFDM with FNO, U-Net, and ResNet, since the PDE structure is known and of course it can perform better than pure data-driven methods. This makes the results not convincing. 
- There is an existing paper on distribution shift quantification: M. Zhu, H. Zhang, A. Jiao, G. E. Karniadakis, & L. Lu. Reliable extrapolation of deep neural operators informed by physics or sparse observations. Computer Methods in Applied Mechanics and Engineering, 412, 116064, 2023.
- Some notations are clearly defined. For example, m in the dataset, A, A* and \hat{A}.
- There are no metrics for coefficient fields if the author considers solving the inverse problem.
- I don't see Appendix B in the manuscript. 
- "In this case, the solution is generated on a higher resolution grid, and then coarsened (upsampled)." It should be "downsampled".

### Questions
- Could you explain your definition of the benchmarking method? What makes DeepFDM a benchmarking method for PDE operator learning?
- Do you want to focus on the inverse problem or forward problem? Could you explain how you make sure it is fair to compare with FNO, U-Net, and ResNet?
- Could you provide a detailed description on datasets and training process?

### Soundness
2

### Presentation
3

### Contribution
2
