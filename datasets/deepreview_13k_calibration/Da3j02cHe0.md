# Efficient Physics-Constrained Diffusion Models for Solving Inverse Problems

- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 6, 3, 5, 1

## Abstract
Solving inverse problems in scientific and engineering domains often involves complex, nonlinear forward physics and ill-posed conditions. 
Recent advancements in diffusion model have shown promise for general inverse problems, yet their application to scientific domains remains less explored and is hindered by the complexity and high non-linearity of physics constraints. We present a physics-constrained diffusion model (PCDM) designed to solve inverse problems in scientific and engineering domains by efficiently integrating pre-trained diffusion models and physics-constrained objectives.
We leverage accelerated diffusion sampling to enable a practical generation process while strictly adhering to physics constraints by solving optimization problems at each timestep. By decoupling the likelihood optimization from the reverse diffusion steps, we ensure that the solutions remain physically consistent, even when employing fewer sampling steps.
We validate our method on a wide range of challenging physics-constrained inverse problems, including data assimilation, topology optimization, and full-waveform inversion. Experimental results show that our approach significantly outperforms existing methods in efficiency and precision, making it practical for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors address inverse problems by leveraging diffusion models as priors.
They formulate the problem as minimizing a composite objective function comprising a likelihood term, which enforces physics constraints, and a regularization term defined by a diffusion model.
As the resulting problem is difficult to solve directly, the authors utilizes a variable splitting scheme that alternates between minimization over the regularizer and the likelihood.
The regularization step is handled through a backward diffusion step, while the likelihood step is performed by minimizing and L2-regularized inverse problem.
The authors validate their approach on a set of three problems.

### Strengths
Solve inverse problems that arise in physics-constrained setups using a variable splitting scheme.

### Weaknesses
 **Insufficient coverage of the related work**

The authors provide a high-level overview of two lines of research: end-to-end supervised approaches and unsupervised approaches.
While, there is a wealth of methods in inverse problems with diffusion models priors, few are mentioned.
Notably, related works that leverage variable splitting schemes, also known as Split Gibbs sampling, are not discussed; for reference, see [1, 2, 3] and the corresponding Related Work sections.

**Methodological ambiguities**

Section 3.3 introduces the regularization step without a clear justification for its formulation. Specifically, _why it has this form?_. Furthermore, the method employs two regularization hyperparameters, $\lambda$ and $\mu$, yet only $\mu$ appears in the update equations.
Besides, the regularization step is independent of these hyperparameters.

**Lack of implementation details**

- The paper does not address the sensitivity of the method to its hyperparameters, namely the early stopping criterion and the timing of triggering the optimization (the parameter $t_s$ in line 256).
- The experimental section lacks specific implementation details, such as the hyperparameters for DPS and SDA; details regarding the used pre-trained diffusion models.
- The reported results raises some concerns In Table 1, DPS performance appears almost identical to the method that omits the prior (Opt w/o diff), which warrants further clarification as inverse problems are severely ill-posed hence pure optimization often yields an inconsistent solutions

### Questions
**Specific questions**

In the experiments, the formulation of the inverse problem in Experiments 4.1 and 4.3 is unclear, namely
 
- Experiment 4.1: is the operator $A$ a discretization of the d’Alembert operator? Additionally, is $s(r,t)$ provided within the dataset?
 - Experiment 4.3: Given that the problem is defined as a constrained optimization, how does the operator $A$ transform $x$ to yield the observation $y$?

Why was SDA excluded from Experiments 4.1 and 4.3? Although originally developed for data assimilation, it remains applicable as an inverse problem method.
Similarly, why was DPS omitted from Experiment 4.3?


**Broader questions**

- Could this method be applied to inverse problems in image restoration, and how would it compare to existing algorithms in the literature?
- The paper addresses problems of moderate dimensionality, approximately $5000$; have the authors considered Sequential Monte Carlo methods [1, 2, 3], which offer stronger theoretical guarantees?
Given this dimensionality, propagating multiple particles in parallel is feasible and would overcome mode-collapse.

---
.. [1] Dou, Zehao, and Yang Song. "Diffusion posterior sampling for linear inverse problem solving: A filtering perspective." The Twelfth International Conference on Learning Representations. 2024.

.. [2] Cardoso, Gabriel, Janati Yazid,, Sylvain Le Corff, and Eric Moulines. "Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems." The Twelfth International Conference on Learning Representations. 2023.

.. [3] Wu, Luhuan, et al. "Practical and asymptotically exact conditional sampling in diffusion models." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
1

### Presentation
1

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
This paper proposes a variable splitting method for solving physics-constrained inverse problems with diffusion model priors. Throughout the reverse diffusion process, the method alternates between two optimization problems: one to update the noisy estimated image with the diffusion model as a regularizer, and one to enforce data/physics constraints. The authors present experiments on full-waveform inversion, data assimilation, and topology optimization, showing quantitative and qualitative improvement upon baselines in all three applications.

### Strengths
* The proposed method is simple and intuitive. Although the methodology lacks technical novelty (see weaknesses), it’s helpful to see that such a simple extension of DPS and other plug-and-play diffusion-based inverse solvers may already go a long way in handling physics inverse problems.
* Validation is done on three very different tasks, and task-specific baselines and the DPS baseline are compared against for each task.

### Weaknesses
 * The technical contribution is marginal. The idea of variable splitting for diffusion-based inverse solving is not new (Equation 16 is similar to the proximal optimization step in Equation 8 of Song and Shen et al. 2022). The main difference in this work is that there may not be a closed-form solution to Equation 16, so iterative gradient-based optimization is used at each likelihood step. However, the use of iterative gradient updates within a variable splitting framework is a fairly standard approach, and the paper does not provide sufficient justification for why this specific implementation is novel or particularly effective compared to existing methods.
* In Tables 1 and 2, the smaller number of reverse steps used by PCDM is touted. This is a little misleading, as the Table 1 caption says that PCDM involves 1000 likelihood iterations in addition to 200 reverse steps. For expensive forward models, it may be the case that these 1000 likelihood iterations are very costly. Also, a clarifying question: does one likelihood iteration mean an entire optimization round of Equation 16, or do the 1000 likelihood iterations account for all the gradient steps needed to solve Equation 16 throughout the algorithm? The paper needs to clearly define what constitutes a single likelihood iteration, especially given that it involves iterative optimization, and provide a detailed breakdown of the computational cost associated with each step.
* I have concerns about how fair the comparison to DPS is. In Figure 3(b), the DPS reconstruction clearly doesn’t match the visual statistics of Kolmogorov flow. I would expect DPS to at least produce something that appears visually plausible even if it doesn’t agree with the physical model. For example, in Figure 4 of SDA (Rozet and Louppe 2023) and Figure 5 of Feng et al. 2024, the DPS reconstructions at least look qualitatively reasonable. I would also be curious how hyperparameters for DPS were chosen. The lack of detail regarding hyperparameter selection for the baselines raises concerns about the reproducibility and fairness of the comparisons. Specifically, it is unclear if the DPS baseline was optimized for the specific tasks or if default parameters were used, which could significantly impact its performance.

### Questions
* Please comment on how hyperparameters for baselines, including DPS, were chosen. I recommend making an appendix to include such details.
* Often it makes more sense to think of physics constraints as priors (i.e., checking whether a solution satisfies a physical model doesn’t involve the observed measurements). Does it make sense in that case to move the physics-consistency term into Equation 12 as an additional regularizer?
* It’s surprising that “Opt w/o diff” in Table 1 has the worst data residual, given that it only optimizes the likelihood term. The authors suggest that this is because it struggles with local minima, but I was under the impression that adding a diffusion regularizer would only complicate the optimization landscape. I would appreciate comments from the authors on why they believe “opt w/o diff” struggles to fit the data and whether they observed the same trend with the other tasks (why wasn’t opt w/o diff included as a baseline for the other tasks?).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes doing MAP estimation using a diffusion plug and play prior (PnP). Namely, the paper aims at solving
$$argmin \|y - \mathcal{A}(x)\| + \lambda \mathcal{R}(x).$$

To do so, it follows the traditional PnP route by using ADMM to split this into solving two proximal problems:

$$ z_{i+1} = argmin_{z} \mathcal{L}_\mu(z, x_i) $$

$$ x_{i+1} = argmin_{x} \mathcal{L}_\mu(z_{i+1}, x) $$

Finally, it replaces the prior proximal problem by a forward backward (with one step) sampling, namely equation (15).
It then evaluates the approach in non-linear problems coming from physics.

### Strengths
The paper proposes an adapted method to solving several physics problems where adapting to a physical constraint is cast as having high likelihood. The numerical applications are relevant.

### Weaknesses
My main concern is the novelty aspect of the paper. Indeed, several papers have investigated the applications of pretrained diffusion generative models as PnP priors. In particular, Algorithm 1 of [1] is essentially the same as the one proposed in this paper. Unless I'm mistaken, this makes the only novelty in this paper w.r.t. [1] to be the physical applications, which are indeed interesting. But I do not reckon it is worth being accepted to ICLR.

Furthermore, even if the proposed algorithm is conceptually different, it is still part of the broad Plug and Play family and I would expect at least a comparison with [1] or any other Plug and Play with diffusion paper.



### Questions
For the major point, see weaknesses.

Minor questions and remarks.

* Is the left term in eq(6) $x_{t-1}$ ? Otherwise it is not a sampling process, as it does not evolve through time.
* What is $ \hat{\epsilon}_{t}$ in equation (15) ? 
Is it equation (7) with $x_{t_k}$?
* Equation (15) mixes indexes between $t_k$ and $t$.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes PCDM (physics-constrained diffusion model), an inverse problem solver that leverages diffusion model as plug-and-play prior. PCDM uses the idea of variable splitting and proposes to solve the underlying optimization problem with implicit diffusion model regularization. The authors demonstrate its application in full-waveform inversion, data assimilation, and topology optimization.

### Strengths
1. Applying plug-and-play diffusion model methods to physics-constrained inverse problems is relatively new to the diffusion model community. 
2. The paper is generally easy to follow.

### Weaknesses
1. The proposed PCDM appears to be mathematically equivalent to a special case of the algorithm in Li et al. [1] (specifically, the case using Tweedie's formula). The claim of algorithmic novelty is questionable (line 100).
2. The "physics-constrained" aspect really comes from the inverse problem itself instead of the novel algorithmic design. Most existing gradient-based plug-and-play diffusion model methods can incorporate that physics loss such as DiffPIR [2], DPS,DAPS [3], RED-diff [4], [5]. These methods are not compared or  discussed in the paper. 
3. The experimental comparison excludes many recent and relevant algorithms. For example DiffPIR [2] and DAPS [3], RED-diff [4].  
4. Reproducibility concerns: important experimental and implementation details are insufficiently documented. See more concrete questions in the next section.
5. There is a lack of ablation studies on important algorithm design parameters, such as the number of likelihood steps per iteration, the optimization threshold $t_s$, and sensitivity to the optimizer configurations. 
6. The Opt w/o diff baseline's performance is surprisingly good, contrasting with typical FWI literature and my own experiments. The implementation details for this baseline and the FWI setup are unclear, raising concerns about the validity of the comparisons. Specifically, the optimization algorithm, initialization strategy, and hyperparameter settings are not sufficiently detailed. 
7. The omission of residuals for InversionNet and VelocityGAN hinders a fair comparison of measurement consistency across all methods. Given the availability of the Deepwave implementation, calculating these residuals should be straightforward. 
8. The hyperparameter selection criteria for all compared methods are not well-defined. Simply using values from prior work without adaptation is inappropriate, especially given the differences in experimental setups. The lack of a clear explanation of how these values were chosen makes it difficult to assess the validity of the results.

### Questions
1. I'm a bit surprised at how well the Opt w/o diff baseline can recover the large structure of the ground truth, as shown in Figure 2 and Table 1. This contrasts with traditional FWI literature findings [1] and my own experimental validation on OpenFWI dataset. I'm curious how the authors implement the FWI problem and the corresponding baselines. More specifically, 
	1. What is exactly the Opt w/o diff baseline in Table 1? Is that the Adam optimizer? What initialization strategy was employed? What are the specific hyperparameters used to report the results? 
	3. Why are the residuals of InversionNet and VelocityGAN omitted from Table 1?  
	4. Given that OpenFWI paper does not provide the gradient implementation of the forward model, how did the authors implement the gradient? 
2. What are the hyperparameter selection criteria across compared methods? 
3. Is there any supplementary material or code to facilitate the reproducibility?

[1] : Virieux, Jean, and Stéphane Operto. "An overview of full-waveform inversion in exploration geophysics." _Geophysics_ 74.6 (2009): WCC1-WCC26.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper propose a method for the solution of an inverse problem where the forward problem is a solution of some physical simulating. 
The claim is that the result of the algorithm produces solutions that do not only honour the prior but also obey the physics.

### Strengths
The results look interesting. The paper may be improved so the results will make sense.

### Weaknesses
To be honest I could not understand the paper, even though I have been working in this field for many years.  The authors invented new jargon, "physics constrained" which means, what exactly? What is the constraint they are fulfilling? On which variables? How do you deal with the constraints? Lagrange multipliers? elimination? penalty?
There is a huge branch of inverse problems that treat them as PDE constrained optimization. Clearly, this escaped from the authors. There is a large number of papers that introduce constraints into inverse problems (e.g 0 \le x) but clearly this is not one of these examples. The authors should try to rewrite the paper and be a bit more precise about what they do,

Similarly, in section 3, the equations flow smoothly and I can easily understand how to get from (7) and the way to (10). 
Then you switch to section 3.2 and I cannot see how (11) and on is related to the previous section. 

Finally in ADMM (eq 12) there is another term for Lagrange multiplier that you are missing. The solution of your problem is different than the original problem.

### Questions
1. What is physics constrained, please define mathematically

2. How to get from the Langevin dynamics of (8-9) to your optimization problem (11-12)

3. Why and how are the two related

4. Why don't you use Lagrange multipliers for (12), add a term p^T(z-x)

5. Can you clarify the overall algorithm?

6. How do you ensure that you fit the data to some given tolerance?

### Soundness
1

### Presentation
1

### Contribution
1
