# Enhanced Diffusion Sampling via Extrapolation with Multiple ODE Solutions

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Diffusion probabilistic models (DPMs), while effective in generating high-quality samples, often suffer from high computational costs due to the iterative sampling process. To address this, we propose an enhanced ODE-based sampling method for DPMs inspired by Richardson extrapolation, which has been shown to reduce numerical error and improve convergence rates. Our method, termed RX-DPM, utilizes numerical solutions obtained over multiple denoising steps, leveraging the multiple ODE solutions to extrapolate the denoised prediction in DPMs. This signiﬁcantly enhances the accuracy of estimations for the ﬁnal sample while preserving the number of function evaluations (NFEs). Unlike standard Richardson extrapolation, which assumes uniform discretization of the time grid, we have developed a more general formulation tailored to arbitrary time step scheduling, guided by the local truncation error derived from a baseline sampling method. The simplicity of our approach facilitates accurate estimation of numerical solutions without additional computational overhead, and allows for seamless and convenient integration into various DPMs and solvers. Additionally, RX-DPM provides explicit error estimates, effectively illustrating the faster convergence achieved as the order of the leading error term increases. Through a series of experiments, we demonstrate that the proposed method effectively enhances the quality of generated samples without requiring additional sampling iterations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work considers the problem of accelerating the inference of diffusion probabilistic models (DPM). Different from the distillation methods, the work adopts the ODE perspective of DPM and aims to propose an accelerated solver for solving the ODE associated with DPMs. The particular technique the work leverages is the Richardson extrapolation (RX), which is proven to achieve lower numerical errors given the same amount of iterations. Analogous to the RX in Euler, the authors derive the ODE solver for DPMs (eq. 22-23). Note that a rigorous mathematical justification of eq 22-23 is not presented, but a simple derivation of the truncation error in terms of total iteration number N is given (assuming eq. 22-23 to be true).

Two different experiments are conducted to demonstrate the performance of RX-DPMs. The first experiment focus on the RX-Euler case, which can be derived rigorously. The experiment clearly shows that RX-Euler leads to faster convergence. The second experiments focuses on RX-DPMs. The results demonstrate faster convergence of RX-DPMs than other DPMs, which, however, is not as significant as RX-Euler over Euler.

### Strengths
1. The paper is generally easy to follow.
2. The introduction of Richardson extrapolation is interesting.

### Weaknesses
1. The limitations of the proposed method is not well discussed.
2. The justification of equation 22 needs improvement on its clarity and rigor.
3. The second weakness leads to a disconnection in the logic flow from RX-Euler to RX-DPMs, which reduces the significance of the second contribution considered by the authors, that is, the proposal of an RX method on a non-uniform grid.

### Questions
---- Methodology ----
1. The authors are advised to define what truncation error means in the first place, as readers may have different interpretations of the error.
2. As pointed out in the weakness, the authors are advised to provide a more clear and rigorous justification of eq. 22-23.
3. Some symbols are used before proper definition, such as $\lambda$.

---- Experiment -----
1. [Fig.2] Please show the dimensionality of the images from CIFAR-10 and FFHQ.
2. [Fig.3] The authors are advised to explain why not all algorithms start at NFE=0.
3. A paragraph properly discussing the limitation of the proposed method is recommended. Besides RX may not be extended to SDE, another clear limitation of the method is the lack of rigorous mathematical justification.
4. The current experiment does not include any other fast DPM methods. To help properly evaluate the performance, the authors are advised to compare RX-DPMs with either a distillation-model-type or consistency-model-type method.

### Soundness
2

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
Inspired by the Richardson extrapolation, the author propose an enhanced ODE-based sampling method called RX-DPM for DPMs to reduce numerical errors and improve convergence rates. The author outline the algorithmic development process for the most simpliﬁed problem and explore an extension to a general DPM solver. The experiments show that RX-DPM can reduce the truncation error and achieve better sample qualities.

### Strengths
1. propose an diffusion sampling method called RX-DPM, inspiring by richardson extrapolation. The method can achieve accurate estimation of numerical solutions without additional computational overhead.Besides, the method is applicable to arbitrary discretizations of time steps.

2. The experiments show that RX-DPM can reduce the truncation error and achieve better sample qualities. RX-DPM shows strong generalization and practical effectiveness, performing well across various ODE designs, architectures, and base samplers.

### Weaknesses
1. The value of $p$ is not provided, and the experiment does not show how the sample quality changes as order $p$ increases.


### Questions
1. How to apply propose method into the SDE sampler?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors present an enhanced diffusion sampler called RX-DPM, inspired by Richardson extrapolation, which significantly improves the accuracy of existing ODE-based samplers. They create an algorithm for arbitrary discretization specifically designed for DPMs.
• In the paper they outline utilization of the algorithm utilizing Richardson extrapolation for general DPM solvers, accommodating arbitrary time step scheduling, beginning with the derivation of the truncation error formula for the Euler method on a non-uniform grid. They offer implementation details applicable to various diffusion samplers without adding extra function evaluations.
•The experiments with several established baselines reveal that RX-DPM demonstrates robust generalization capabilities and high practicality, irrespective of the ODE structures, architectures, or foundational samplers used.

### Strengths
The authors introduce an innovative sampling technique for diffusion models. This method, RX-DPM, appears to surpass previous sampling methods due to its incorporation of Richardson extrapolation, specifically adapted for DPMs. The algorithm effectively reduces local truncation error, resulting in improved sample quality.
The authors demonstrated the effectiveness of RX-DPM through experiments with established baseline models and datasets, as well as by comparing RX-DPM to other sampling methods.

### Weaknesses
There is a notable absence of performance comparisons regarding computation time and FLOPS, as the study only evaluates the number of function evaluations (NFE) of the algorithm without contrasting the computational costs of each step of RX-Euler with the standard Euler method for DPMs. Specifically, the paper does not detail the overhead introduced by the Richardson extrapolation step, which involves additional linear combinations and could potentially impact the overall sampling time, especially when considering the memory access patterns and computational graph overhead. It is crucial to understand not just the number of forward passes, but also the time required for each step, including the overhead of the proposed method.

Furthermore, most of the experiments involving NFE variation focus on low to moderate-resolution images, not exceeding 256 by 256 pixels, while leading diffusion models are capable of generating high-resolution images, such as 512 by 512 pixels or more. Consequently, the study lacks a thorough quality comparison of the methods across high-resolution datasets like AFHQv2 and FFHQ, particularly for varying NFEs beyond 10 or 11. The evaluation should include a more comprehensive analysis of the visual quality and fidelity of generated samples at higher resolutions and lower NFE counts, as the benefits of the proposed method might not scale uniformly across different resolutions and NFE regimes.

### Questions
What is the difference of the proposed method with alternative methods in the literature in terms of sampling time?
Why extrapolation does not require additional NFE? In which scenario us the method is applicable for SDE?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors proposed an enhanced ODE-based sampling method for DPMs based on Richardson extrapolation. They claimed that they used non-uniform discretization approach with arbitrary time step scheduling and utilized an additional ODE solution over an interval of k time steps.

### Strengths
The idea of using Richardson extrapolation for ODE-based sampling method is not done in diffusion model although the idea has been explored in solving odes.

### Weaknesses
1. The technical part (section 4) of the paper is poorly written. I am concerned that there might be some technical errors in the formulas that lead to the main algorithm. The authors need to check carefully and they also need to refer to some existing mathematical results on using Richardson extrapolation in numerically solving odes. Also the mentioned that one of the contribution is arbitrary discretization of time steps; however it is not clear if they have actually implemented it.   

2. The experiment part is not well written either. It is ambiguous on the relationship between RX-DPM  and RX-EDM and RX-DDIM, 

I believe this paper needs a major revision before it is published. Please also refer to the following section - Questions.

### Questions
1. In page 4, line 127 p(x, \sigma) = p_data \dot N(0, sigma^2 I), the right hand side of the equation does not make sense to me.
2. I believe the local truncation error at line 196/197 in the right of eqn. (10) should not have the first term. Please check. As a result, if this is a mistake, it propagates into the following equations, and might cause major technical issue for this paper. 
3. From eqn. (13) to eqn. (14) to eqn. (15), in page 4, the function f disappeared, the only reason provided was because function f is smooth. I wonder if there is an error here. They could have used the Appendix to explain the soundness of this algorithm.
4. The authors mentioned that eqn. (17) in page 5 is obtained from eqn. (16) in page 4; however, eqn. (16) has k in both subscript and superscript, one can not randomly set k =1 for superscript, and keep k in subscript; which resulting in two different values.
5. It is unclear how the authors interpret DDIM as Eqn. (20). Somehow they jumped from equation (3) to eqn. (20) without explanation.
6. In section 4.3, the authors first proposed an estimate of x_{t_{i-k}}, then jumped to RX-Runge-Kutta in page 4, when they mentioned they "consider the second order Runge-Kutta ..", but it did not mention for what reason to consider it. From the notation, I guess is they use to to estimate the truncated error. Then they jumped again into algorithm 1, in which they brought up ode solver \Phi that was not explained before. The whole section should be reorganized and be rewritten so that the algorithm can be clearly explained. 
7. The paper should explicitly state that their proposed numerical solution is backward although it was time reverse in diffusion model.
8. The authors only mentioned that "We acknowledge that there are some
limitations to our method’s application in SDE ...". First of all, they proposed their algorithm for ODE, but they did not really extend it to SDE. Second, they did not state what is their limitation. Third, I would appreciate some discussion on the sensitivity of this algorithm as well as complexity cause by using the Richardson extrapolation because it is actually a more complicated way to calculate the derivative approximation.

### Soundness
2

### Presentation
2

### Contribution
2
