# NF-MKV Net: A Constraint-Preserving Neural Network Approach to Solving Mean-Field Games Equilibrium

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Neural network-based methods for solving Mean-Field Games (MFGs) equilibrium have gained significant attention due to their effectiveness in high-dimensional settings. However, many algorithms face the problem that the density distribution evolution does not satisfy the mathematical constraints in the solution. This paper explores the neural network solution of MFGs equilibrium from the perspective of stochastic process, while coupling process-regularized Normalizing Flow (NF) frameworks and state-policy-connected time series neural networks to solve the McKean-Vlasov type Forward-Backward Stochastic Differential Equations (MKV FBSDEs) fixed point problems, which is equivalent of the MFGs equilibrium. First, we convert the MFGs equilibrium to MKV FBSDEs which introduce the density distribution into equations coefficients within a probabilistic framework, and construct neural networks to approximate value functions and gradients based on these equations. Second, we employ NF architectures—generative neural network models—and by imposing loss constraints on each density transfer function, the algorithm ensures compliance with volumetric-invariance and time-continuity. Additionally, this paper provides theoretical proofs of the algorithm's validity and demonstrates its applicability across various scenarios, showcasing its effective compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to couple “process-regularized Normalizing Flow (NF) frameworks and state-policy-connected time series neural networks to solve the McKean-Vlasov type Forward-Backward Stochastic Differential Equations (MKV FBSDEs) fixed point problems, which is equivalent of the Mean-Field Games (MFGs) equilibrium,” Empirical and theoretical validations are provided.

### Strengths
-	The paper presents detailed introduction and explanation of the proposed method, including how to convert solving a MFG to solving a McKean-Vlasov type Forward-Backward Stochastic Differential Equations (MKVFBSDEs) fixed point problem, how to use a NF to estimate density required, and how to couple the two processes. The paper is compressive, well-structed, and easy to follow. 

-	The paper present experiments for cases of traffic flow control, crowd motion, crowd motion with obstacles, and comparisons with RL-PIDL and APAC-Net.

-	I find the paper makes conceptual contributions of proposing a new family of neural networks that could have advantages.

### Weaknesses
-	The novelty is not cleared stated and explained. There have been works linking MFG and NF (Huang et al. 2023) [1], and converting MFG to MKVFBSDEs (Carmona et al. 2018) [2]. I would suggest to clearly explain the novelty and significance of this paper that exceeds a simple combination of the existing works. Specifically, the paper needs to clarify how the proposed method's approach to coupling the normalizing flow with the time-series network differs fundamentally from existing methods that also use NFs for density estimation in similar contexts. The explanation should go beyond just stating that the method solves a different problem, but rather detail the unique way the coupling is achieved and what advantages this specific coupling offers.

-	The experiments are not sufficient. I would suggest adding (1) experiments of comparison with Deep Generalized Schrödinger Bridge (Liu et al. 2022) [3], Ruthotto et al. (2020), and Chen (2021); (2) experiments in more scenarios, such as opinion depolarisation, path planning problem, etc. The current experiments, while demonstrating the method's capability, lack a thorough comparison with state-of-the-art methods in similar problem domains. The choice of baselines is also questionable, as RL-PIDL and APAC-Net are not directly comparable to the proposed method in terms of their underlying approach and goals. A more rigorous comparison against methods like Deep Generalized Schrödinger Bridge [3], which also tackles similar density estimation problems, is needed to properly benchmark the proposed method's performance. Furthermore, the experiments should include more diverse scenarios to test the robustness and generalizability of the method.

-	Theoretical analysis is nearly not given. I would suggest giving error analysis of using the proposed method to estimate the equilibrium of a mean-field game. The paper lacks a rigorous theoretical foundation. While empirical results are important, a theoretical analysis is crucial to understand the convergence properties and error bounds of the proposed method. The paper should provide a detailed error analysis, including how the discretization of the MKV FBSDEs affects the accuracy of the solution and how the neural network approximation contributes to the overall error. Without such analysis, it is difficult to assess the reliability and robustness of the method, especially in high-dimensional and complex scenarios.

### Questions
Please address the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a framework for solving mean-field game equilibria by parameterizing the evolution of agent densities using continuous normalizing flows, offering a potentially more scalable alternative to existing methods for addressing the coupled partial differential equations, whether or not deep learning is employed. The authors constrain the probability flow generated by the normalizing flows by minimizing the residuals of the Hamilton-Jacobi-Bellman equation alongside the value function. They empirically validate their proposed algorithm through numerical experiments, comparing it with current methods for solving mean-field games.

### Strengths
* This paper presents a novel framework that address the limitations of most existing methods for solving mean-field games, in particular, the scalability to high dimensions and the expressivesness of modeling time-dependent probability densities.

### Weaknesses
 * The authors assert in the abstract that the paper provides theoretical justifications for their method; however, I have not seen any reporting of the claimed theoretical results.
* The paper includes confusing and self-contradictory notation and expressions. For instance, the authors use the symbol $\phi$ to refer to both the value functions in Section 2.1 and the neural network parameters in Section 3.2. Overall, the presentation is unclear and difficult to follow. I recommend that the authors clean the notations and better organize the paper. 
* The empirical validation is insufficient to demonstrate the practical benefits of the proposed algorithm. I recommend that the authors consider incorporating some of the experiments conducted in [1], for example, their synethic 2D examples in Section 4.1, which are more complicated and meaningful navigation tasks than what is reported in this paper. If time permits, I would also recommend that the authors try LiDar experiments reported in [1].

### Questions
I wonder if the authors could explore connections between the class of mean-field game problems they are considering and the Schrödinger Bridge problems, both of which model processes with fixed initial and terminal conditions. Reformulating their methods within the context of Schrödinger Bridge problems would significantly strengthen the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Neural network-based methods for solving Mean-Field Games (MFGs) equilibrium are effective in high-dimensional settings but struggle with ensuring the density distribution is one throughout evolutions. This paper addresses this issue by exploring neural network solutions for MFGs equilibrium using a stochastic process approach. It combines process-regularized normalizing flow frameworks with state-policy-connected time series neural networks to solve McKean-Vlasov type Forward-Backward Stochastic Differential Equations, which are equivalent to MFGs equilibrium. The approach converts MFGs equilibrium into MKV FBSDEs, incorporating density distribution into the equations' coefficients within a probabilistic framework, and using neural networks to approximate value functions and gradients. The normalizing flow architectures enforce loss constraints on each density transfer function to ensure the density distribution requirements. Empirical results show better performances than some existing methods.

### Strengths
1. The method is novel. Whereas many works try to use a generic neural network to solve physical problems, it is refreshing to see a work designing neural architectures catered towards the problem at hand.
2. The mathematical derivation is sound, and the problem of solving MFGs is interesting. 
3. While limited, the numerical experiments are nicely conducted.

### Weaknesses
1. Evaluating the loss l_HJB is very expensive, having to compute the Laplacian of the value function u. Is there a way to avoid this? The computation of the Laplacian, involving second-order partial derivatives with respect to both spatial and temporal variables, is indeed a significant computational bottleneck. Specifically, the need to calculate $\partial_{x^{i}}^2$ for each dimension $i$ of the state space, and then sum these terms, can be particularly burdensome in high-dimensional settings. Furthermore, the temporal derivative $\partial_t^2$ also adds to the computational cost, especially when using finite difference approximations. This expense limits the scalability of the method to more complex, high-dimensional problems.
2. While it is true that normalizing flows preserve the volume of distribution along evolution time, it does not usually achieve SOTA performances like other generative models. Is it possible to use other generative models for this purpose? While volume preservation is a useful property, the limitations of normalizing flows in terms of expressiveness and the ability to model complex distributions are well-documented. This can lead to suboptimal performance compared to other generative models that may not explicitly enforce volume preservation but can capture more intricate data patterns. The choice of normalizing flows may therefore be a limiting factor in achieving state-of-the-art results.
3. While the idea is nice and the numerical experiments are thoughtful, they do appear limited, any chance to conduct a more thorough empirical study? The current experiments, while demonstrating the method's feasibility, lack the breadth and depth needed to fully assess its robustness and generalizability. Specifically, the absence of experiments in higher-dimensional state spaces and with more complex obstacle configurations raises concerns about the method's applicability to real-world scenarios. A more thorough empirical study should include a wider range of problem settings and benchmark comparisons.

### Questions
1. Why is it important to preserve the volume of distributions? 
2. Followingly, all flow methods preserve the volume. Generative methods through flow matching, for instance, preserve the volume while achieving SOTA results, why not consider them?

### Soundness
2

### Presentation
2

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
This paper presents a deep learning-based approach to solve mean-field game problems. The proposed approach first models the value function with MKV FBSDEs where the gradient of the value function is parameterized with a neural network. Next, a MAF normalizing flow  architecture is employed for the Fokker-Planck equation and a loss function encode constraints constraints on each density transfer function. The aim is to have time continuity and volumetric invariance constraints satisfied.

### Strengths
This work introduces some interesting ideas. Instead of directly addressing the MFG system, it uses a formulation based on stochastic FBSDEs. It also employs two neural networks: one to parameterize the value function and another for the normalizing flow. The normalizing flow enables density and likelihood approximation at the final time.

### Weaknesses
1. This work claims that hard constraints are guaranteed; however, these constraints are only enforced using a soft penalty. This should be clarified earlier, in the abstract, and when the authors state their contributions. It would also benefit the paper if the authors explain the implications of using soft penalties rather than hard constraints.
2. The paper claims there are proofs of the algorithm's validity, but I could not find them in the manuscript. The authors should either remove this claim or include them in the main draft or the appendix. 
3. The MAF flow is used to generate the Fokker-Planck equation. A continuous normalizing flow automatically satisfies the time continuity constraints as hard constraints. I recommend the authors look at "Bridging mean-field games and normalizing flows with trajectory regularization" by Huang et al. Note continuous NFs are also used in the work "A Machine Learning Framework ..." by Ruthotto et al, which is also cited in this paper.
4. Lack of code for reproducibility - note these can be submitted anonymously as well. For example, the authors could submit an anonymous GitHub repository or a file sharing service. Additionally, the authors could include a brief description of how to run the code in the paper.

Minor:

1. Line 274: "In Section 3.2, we have expressed the value function and its gradient". There is no value function or gradient in section 3.2. The authors should reference the correct section. 
2. Line 129: "... is solvable". It would strengthen this paper if the authors cite or show this result.
3. Line 153: "However, a challenge arises in that MFG, unlike Optimal Transport (OT), lacks initial and terminal density distributions. ... This makes it difficult to frame the problem as a complete density evolution problem". I do not believe there is any difficulty here. See point 3 above, where density can be preserved with continuous NFs.

Overall, the manuscript felt like it was hastily written as it had many long complex sentences with grammatical errors, which made it somewhat difficult to read and understand. 

For example, in Line 18, "This paper explores the neural network solution of MFGs equilibrium from the perspective of stochastic process, while coupling process-regularized Normalizing Flow (NF) frameworks and state-policy-connected time series neural networks to
solve the McKean-Vlasov type Forward-Backward Stochastic Differential Equations (MKV FBSDEs) fixed point problems, which is equivalent of the MFGs equilibrium." Could be made more clear by instead stating: "This paper explores the neural network solution of MFGs equilibrium from the perspective of stochastic process. The goal is to couple a process-regularized Normalizing Flow with a McKean-Vlasov type Forward-Backward Stochastic Differential Equation for the value function."

Other examples of such sentences include: 

2. Line 58: "To summarize..."
3. Line 123: "be in force".
4. Line 133: "We consider..."

### Questions
1) what does $-1\dagger$ represent in eqns (4) and (5)? 
2) Equation (5) is one of the primary ingredients of this work. Where did this equation come from? Please either show this or cite exactly the reference for this. 
3) Line 253: "Multiple f_i are coupled to finally get the function f we need." Is f here the same as the objective function in equation (1)?

### Soundness
2

### Presentation
1

### Contribution
2
