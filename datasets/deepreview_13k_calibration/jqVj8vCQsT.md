# Learning a Neural Solver for Parametric PDE to Enhance Physics-Informed Methods

- Decision: Accept
- Avg Score: 5.60
- Scores: 3, 6, 8, 8, 3

## Abstract
Physics-informed deep learning often faces optimization challenges due to the complexity of solving partial differential equations (PDEs), which involve exploring large solution spaces, require numerous iterations, and can lead to unstable training. These challenges arise particularly from the ill-conditioning of the optimization problem, caused by the differential terms in the loss function. To address these issues, we propose learning a solver, i.e., solving PDEs using a physics-informed iterative algorithm trained on data. Our method learns to condition a gradient descent algorithm that automatically adapts to each PDE instance, significantly accelerating and stabilizing the optimization process and enabling faster convergence of physics-aware models. Furthermore, while traditional physics-informed methods solve for a single PDE instance, our approach addresses parametric PDEs. Specifically, our method integrates the physical loss gradient with the PDE parameters to solve over a distribution of PDE parameters, including coefficients, initial conditions, or boundary conditions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method to overcome the challenging optimization of PDE-loss in physics-informed methods by learning a modification on the gradient (w.r.t. model parameters), which intuitively serves as a preconditioner. The experiment displays a noticeable acceleration in convergence.

### Strengths
-	The method is full of imaginations!

-	The empirical result in the test cases investigated are surprising. The proposed method help significantly accelerate the convergence of pde-loss optimization.

### Weaknesses
- The theoretical analysis (main text and appendix B) is superficial and should not be considered as ‘proof’. In L814, the only important part of convergence analysis is circumvented by saying ‘the introduction of P as a preconditioner often results in κ(PA)<κ(A)’ instead of showing it. Thus the author actually didn’t prove anything. In fact, the effectiveness of the method is highly related to whether it can help mitigate the condition number, which might not hold true, not supported by either theoretical or empirical evidence. Also, L790-791 simplify the problem so much that the derivation could no longer provide insight to understanding the proposed method, unless the authors demonstrate the approximation to $Pv$ is reasonable in some sense, such as bounding the error introduced by this simplification.

- To train the model $\mathcal{F}_{\rho}$, one has to first fix a set of grid points. This is neither flexible nor suitable to leverage the advantageous of PINN. In many PINN papers, the pde residual are estimated in a Monte-Carlo manner by drawing random points and computing its pointwise residual, so as to eliminate the heave computational and memory cost. Moreover, since the paper are target at solving a family of PDEs, it is always the case that one has to use finer grids / higher resolution to adequately capture small-scale effects for some harder instances in the large PDE class. The authors should provide a clear strategy for handling varying grid resolutions and demonstrate the method's performance on non-uniform grids.

- Regarding the method itself, in my opinion, the performance significantly depends on how well $\mathcal{F}_{\rho}$ generalizes to unseen or even out-of-distribution data. Intuitively it seems like it would be harder for $\mathcal{F}_{\rho}$ to generalize than the surrogate model (as in PINO or physics-DeepONet) itself, since the mapping $\mathcal{F}_{\rho}$ try to approximate is more complicate. A systematic study on how well $\mathcal{F}_{\rho}$ needs to be learnt so as to ensure reasonable improvement on pde-loss convergence is necessary to make this method practical. This study should include quantitative metrics evaluating the generalization performance of $\mathcal{F}_{\rho}$ across different PDE families and parameter ranges.

- As mentioned in the limitations, the method will possibly suffer from a memory issue and is slow to train since it needs to back-propagate through several optimization iterations. This hinders the practicability of the method. A detailed analysis of the memory requirements and training time scaling with respect to the number of grid points, PDE complexity, and model size would be beneficial.

- The PDE considered are either 1D or linear, which are all quite toyish. The paper could benefit from studying their methods in some equations will optimization indeed brings severe challenges for physics-informed methods, for instance Navier-Stokes with relatively high Reynolds numbers. Otherwise, the experiments are not convincing. The inclusion of more challenging, non-linear, and higher-dimensional PDEs would significantly strengthen the paper's impact.

- Many details important for evaluating this paper are only mentioned in the appendix, e.g. the training and inference time cost. I am aware of the page limit, but the content should be briefly summarized in the main text, otherwise few readers notice they are there. Specifically, a table summarizing the training and inference times for each experiment, along with the corresponding hardware specifications, should be included in the main text.

### Questions
-	Do you have any intuition on what the model $\mathcal{F}_{\rho}$ is learning? The paper interprets it as a preconditioner, but this answer is very vague and lack of information.

Think this way: given infinite data and a perfect training, what is the resulting mapping of $\mathcal{F}_{\rho}$?

Then consider: what is the effect of $\mathcal{F}_{\rho}$? Does it necessarily (or, ideally) help reduce the condition number?

-	Are the baseline hybrid methods trained with exactly the same dataset (and same amount of data) as the proposed method?

-	L308, isn’t $m$ the number of grid points instead of trajectories?

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
4

### Summary
Physics-informed Neural Networks (PINNs) are popular neural network-based approaches for solving partial differential equations and provide a compelling alternative to traditional PDE solvers. Unfortunately, the PINN objective yields a difficult optimization problem to train the network. The difficulty stems from the presence of an ill-conditioned differential operator in the loss, which leads to an ill-conditioned objective. The present paper proposes a framework for solving parametric PDEs based on learning an optimizer tailored to that class of problems. The authors provide a heuristic argument showing that the learned optimizer can be viewed as preconditioning the original loss. Preliminary experiments show the proposed approach yields better performance relative to existing methods.

### Strengths
- This is the first time I've seen the use of learned optimizers in SciML. I think this approach has the potential to be very useful.
- The potential connection between learning the optimizer is interesting, though still somewhat tenuous; see weaknesses below.
- The proposed framework outperforms vanilla baselines, which is good.

### Weaknesses
 **Related work**

 While I have not seen the idea of learning an optimizer applied in the SciML literature, it certainly is not new in the overall ML literature. The authors should explain how their approach fits into this existing body of work in the related work section.
The authors should mention Cho et al.'s recent work, which proposed a very effective method for solving parametric PDEs using PINNs.

**Theory**

The theoretical support for the benefit of learning the optimizer is weak. 
The argument provided in Appendix B is heuristic and relies heavily on the assumption that both networks are well-approximated by their first-order Taylor expansions. This regime only holds under certain strong assumptions, which the paper neglects to mention. Specifically, the Taylor expansion is only valid when the weights are close to the expansion point, which is not guaranteed during training. Furthermore, the analysis does not account for the non-convexity of the loss landscape, which can significantly impact the optimization dynamics. Finally, it is not apparent why it should be the case that $\kappa(PA) \ll \kappa(A)$. So, the potential connection between the learning optimizer is interesting but very tenuous.     
 
**Experiments**

The experiments in the paper are very weak. 
Comparing to the vanilla PINN alone using L-BFGS for training is inadequate. 
As is well known, better performance is achieved by using the combination of Adam+L-BFGS. Specifically, the Adam optimizer can help escape poor local minima, while L-BFGS can provide faster convergence in the vicinity of a good minimum. Plus, more sophisticated optimizers, like Muller et al.'s natural gradient approach or Rathore et al.'s NNCG, can greatly enhance PINN training. It would be much more compelling to compare to one of these more sophisticated approaches to training PINNs. The lack of comparison to these methods makes it difficult to assess the true value of the proposed approach.

The paper mentions the ability to cover parametric PDEs as a contribution, but none of the experiments demonstrate this advantage. Moreover, the method introduced in this paper should be compared to a dedicated PINN method for parametric PDES like that of Cho et al. (2024).

The authors' approach clearly has a higher time cost than the vanilla approach, but they do not provide runtimes for their method relative to the vanilla method. This makes it challenging to develop a concrete idea of how much more expensive their approach is. It is crucial to provide a detailed breakdown of the computational costs, including training time, inference time, and memory usage, to allow for a fair comparison.

**Presentation**

The text has many grammatical errors, which can sometimes make the presentation difficult to follow. I recommend the authors do a careful read-through and make appropriate edits. 
This will greatly improve the readability of the paper.

**Overall** 

I believe the paper contains some interesting ideas that have the potential to enhance the applicability of PINNs. 
Unfortunately, the paper is not ready for publication at ICLR. 
The experiments are lacking, so it is difficult to determine if the approach here would improve over more sophisticated variants of PINNs,  which are used in practice.
In addition, the theoretical contribution is too heuristic, and the presentation needs polishing.

### Questions
1) Why did you not include wall-clock times?

2) Why did you not include a comparison(s) with a more sophisticated variant of PINN(s)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an optimization process that can learn a set of parametric PDEs quickly and precisely while addressing the ill-conditioning issues that traditional PINNs face. The authors first train a physics-informed neural network on a dataset containing different PDE coefficients, initial conditions, and boundary conditions, enabling the network to predict PDE solutions in the initial step. Then, a solution approximation expressed as a linear expansion in a pre-defined basis is optimized to adapt to each PDE instance. This method enables fast learning of different PDE instances and effectively overcomes ill-conditioning issues.

### Strengths
A very good paper demonstrating a novel approach to addressing PINN’s limitations, with extensive experimental results to support the claims. 

The paper presents strong motivation and a thorough review of related work. 

The methods and the overall paper are easy to follow.

### Weaknesses
I have some questions about the training of the neural solver.

### Questions
My understanding is that the objective function for training the neural solver is data loss + PDE loss, which represents a soft-constrained optimization problem. Have you considered using a hard-constrained method, as in Lu et al. [1]?

[1] Lu, Lu, et al. "Physics-informed neural networks with hard constraints for inverse design." SIAM Journal on Scientific Computing 43.6 (2021): B1105-B1132.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the problem of optimising Physics informed deep neural networks for solving PDE. Specifically, the paper addresses the issue of ill-conditioned optimization problems. 

Using a Fourier representation, the authors clearly lay out the problem with ill conditioning of general PINNs and give a numerical example to illustrate this. 

The paper describes how the problem can be transformed using a neural solver into one that can be optimised using gradient descent more quickly than the original problem.

### Strengths
Overall the paper does a good job of explaining the problem and describing the proposed solution. However there are a number of issues that need to be expanded upon in order to improve the thoroughness and reliability of the findings. 

In general I think the paper represents a useful contribution to the literature and I am leaning towards an acceptance. However, I do think that it could be significantly improved if some of the findings detailed in the appendices could be brought into the main body of the paper as described in this review. Although the paper is fully 10 pages long, some of the descriptive text, especially in the early part of the paper could be made more concise to make space for these valuable aspects of the findings to be included in the main body of the paper.

### Weaknesses
The parameters $\Theta$ are updated using gradient descent. This is nested within a additional optimisation process for tuning the parameters $\varrho$. Some results should be included in the main body of the paper which show the CPU time, including for the optimisation of $\mathcal{F}_\varrho$. There are some results presented in Appendix F but these should be discussed in the main paper as they are important for evaluating the usefulness of the method presented. 

The paper describes the problem in terms of the condition number $\kappa(A)$. A sketch proof is included in Appendix B to show that convergence is guaranteed and its speed is enhanced using this structure. However the wording around this sketch proof is quite confusing. Section B.2 there states "The introduction of $P$ as a pre-conditioner \textit{often} results in $\kappa(PA)<\kappa(A)$." and "the condition number is improved under \textit{some} optimality conditions. However in Sections B.3 and B.4 convergence and optimality is described as \textit{optimal} and \textit{guaranteed}. This inconsistency should be addressed due to the importance of this in supporting the empirical findings within the main part of the paper. 

The results in the paper show very good improvements in the optimisation time and the MSE for the example PDEs used. However a range of parameters for each PDE is quoted in table 1. In table 2 the MSE results for the different equations are shown, however there is no indication of how these errors vary within the parameter ranges. There are some results presented  for this in Appendix E, however these should be brought into the main part of the paper as it is important to show the robustness of the method. 

In general the paper is well written and formatted but  In line 436 and 437, the sentence reads ``Therefore our method should be primarily compared toe these baselines."

### Questions
My suggestions are included in the "Weaknesses" section and I would be very pleased to hear the authors' response to these suggestions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper propose a method that seems to be a PINO method to tackle learning of PDEs with the presents supervision from both data and equations.

### Strengths
The authors tackle and important problem in AI and science.

### Weaknesses
The writing and position of the paper is very limiting.

A few basic comments before we get to the main ones.
-1 In the intro:
Please note that when a PDE equation is given, that is complete supervision. Please avoid calling it unsupervised. PDE equation is absolute supervision, sufficient to solve the problem completely.
-2 In the intro:
Please pay more attention; there is a difference between neural networks and neural operators. One is for learning on the finite-dimensional setting; one is for functional data, that is your case. I only found out on page 8 that the authors talk about Fourier layers, and then I had to go through the referenced paper to realize that the authors use a neural operator for their solver. Even there, please explain you are doing operator learning and using neural operators. Please also define your neural operator architecture. FNO is not even defined or abbreviated in your work. Please bring the abbreviation and explain in your paper that your work is neural operator-based.

-3 In 3.3 
The authors need to define varrho in the equations in this section. I guessed what that was after reading page 8. There is no varrho in the equations in 3.3.

-4 In 3.3
Why choose linear span? We know such a thing is fine for easy problems and not sufficient for complex problems. That's why even the first paper proposing the PINO paradigm also deals with complex problems and doesn't use linear span simplification.

-5 In 3.3
 What does Solve even mean in alg2? I only guessed its meaning.

-6 In 3.3. Please be mindful of term solve and term prediction for F. The F predicts something and doesn't solve anything in the sense that solvers in the field of applied math solve.

-7 In 3.3 
Reading line 304, it feels that the authors first do PINO with only physics and then PINO with data. However, the intro implied that it is the other way. Which is done here?

-8 In 3.3 what is trajectory in line 308?

The main comment is the presentation. Reading the paper, it seems the paper is aiming to advance PINO. However, reading abstract, intro, and other sections up to page 8, the paper does not even talk about PINO. Everything the paper promotes and sugest they are doing is already propsed and establisehd in PINO paper. Please read the PINO paper carefully and possition your paper according to that. Also, in both abstract and intro, mantion what is new in your work. I could not find anuthing different than prior methods. And I am sure there are many things new and novel in this paper, but I just couldn't parse it when abstract and intro are all talking about basics of PINO.

### Questions
mentioned above.

### Soundness
1

### Presentation
2

### Contribution
1
