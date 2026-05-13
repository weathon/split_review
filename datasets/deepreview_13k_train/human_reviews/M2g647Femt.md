# Solving Composable Constraints for Inverse Design Tasks

- Decision: Reject
- Scores: 5, 3, 5, 1

## Abstract
Inverse design tasks are an important category of problem in which we want to identify some input vector $x$ satisfying some desirable properties. In this paper we propose a mechanism for representing inequality constraints as Signed Distance Functions (SDFs). SDFs permit efficient projection of points into the solution region as well as providing a mechanism for composing constraints via boolean set operations. In this paper, we provide theoretical motivation for Signed Distance Functions (SDFs) as an implicit representation of inequality constraints. Next, we provide analysis demonstrating that SDFs can be used to efficiently project points into solution regions. Additionally, we propose two novel algorithms for computing SDFs for wide families of machine learning models. Finally, we demonstrate practical utility by performing conditional image generation using MNIST and CelebA datasets, and computational drug design using the ZINC-250K dataset. From the experimental results, we note that the composable constraints can reliably and efficiently compute solutions to complex inverse design tasks with deep learning models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an approach based on sign distance functions (SDFs) to solve inverse design problems. The goal is primarily to find the closest feasible solution to any given starting point. The main selling point of SDFs in this context is (approximate) composability. A search algorithm is introduced to represent SDFs for composable constraints based on multi-valued predictors (SINNs or ReLU networks). SDF composition is softened using logsumexp for effective iterative corrections. The method is illustrated on simple problems involving MNIST, Celeba, and molecular design. The only empirical comparison is to a gradient guided design.

### Strengths
SDFs seem like reasonable ways of representing constraints, especially since, if correctly represented, a single adjusted gradient step would get you to a feasible point (when SDF is differentiable). SDFs can be composed across inequality constraints via max or min operations resulting in a bound which also seems reasonable. Search algorithms are introduced to approximately recover SDFs for predictors represented by SINNs or ReLU networks.

### Weaknesses
Many technical details are missing from the main text (relegated to the appendices). The paper should be rewritten by incorporating technical details back into the main text (the portion of the appendix that I read is clearer than the main text that leaves many questions unanswered).

The task that the paper addresses can be viewed as a general multi-criteria optimization problem to which there are numerous methods available. E.g., how would a simple linearization as a way to search for points on the pareto front work in comparison? This would be a variant of GDD but with different weights and would likely match better with the (greater?) computational requirements for SDFs. The proposed approach also relies on a low dimensional well-behaving latent space so that a SINN or ReLU network remains suitable for extrapolation and mapping to properties. It would be helpful to provide comparisons to methods that are not limited in this way. E.g., a conditional generative model could already be superior as it would not be forced to use a low dimensional latent space prior to generation and evaluation (by an oracle not operating on the latent space). At minimum, scaling to higher dimensional latent spaces seems essential to demonstrate. Also, if composability is the key argument, one should demonstrate this with more constraints (more than 2 or 3) and intersections. In the evaluation, one could control whether the constraints are largely aligned vs competing to see how the method (and baselines) succeed in different scenarios. Broadly speaking, the empirical results/comparisons should refer to the state of the art methods and performances in each chosen task. None of the example problems fit this description.

Eq (2) does not seem to be used in the paper, only the feasibility problem from eq (1). Please clarify.

Theorem 1: please define "search algorithm" more precisely. Does it include augment gradient steps that start from extrema/critical points? What if no feasible solution exists?

Algorithm 1: x0 is presumably just x as in the rest of the algorithm. Algorithm here is defined for one dimensional x. Please rewrite. The algorithm also only returns a distance as a value while the design problem requires a gradient of the SDF. How is the gradient calculated on the basis of Algorithm 1?

How is the closeness to the initial point controlled or assessed when searching for a feasible point? Or is the assessment global?

### Questions
Eq (2) does not seem to be used in the paper, only the feasibility problem from eq (1). Please clarify. 

Theorem 1: please define "search algorithm" more precisely. Does it include augment gradient steps that start from extrema/critical points? What if no feasible solution exists?

Algorithm 1: x0 is presumably just x as in the rest of the algorithm. Algorithm here is defined for one dimensional x. Please rewrite. The algorithm also only returns a distance as a value while the design problem requires a gradient of the SDF. How is the gradient calculated on the basis of Algorithm 1?

How is the closeness to the initial point controlled or assessed when searching for a feasible point? Or is the assessment global?

### Soundness
3

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
3

### Summary
In this paper, the authors propose representing inequality constraints in inverse design tasks via signed distance functions (SDF).  Furthermore, the authors provide two algorithms for computing SDF based on Shepard interpolation neural networks and piece-wise linear neural networks.

### Strengths
1. The paper is well-written and well-organized. 


2. The research line for solving the constrained optimization through signed distance functions is interesting.

### Weaknesses
1.  The advantage of formulating the constrained optimization using the signed distance functions (SDF) compared with other constrained optimization solvers is not clear.

The authors employ the SDF to solve the constrained optimization. However, it is challenging to compute the boundary of the solution set in SDF (in Eq. (4)).  As a result, it can be very expensive to compute the SDF for general solution set S.   Specifically, for complex solution sets, the computation of the SDF, which involves finding the closest point on the boundary, can become intractable, especially in high-dimensional spaces. The paper does not adequately address the computational cost associated with this step, particularly when the solution set is defined by complex constraints. Furthermore, the paper does not provide a clear analysis of how the complexity of the solution set impacts the performance of the proposed SDF computation algorithms.

For the piece-wise linear neural networks,  the constrained optimization may be transformed as a linear constrained optimization problem.   What is the advantage of using SDF over linear programming solvers?  In addition,   even for piece-wise linear neural networks, the number of extreme boundary points grows exponentially as the depth grows.   The proposed method uses local search as an approximation. What is the advantage of the proposed method compared with other approximated solvers?   Because there is no comparison with other solvers and approximation techniques, it is unconvincing to justify the advantage and effectiveness of the proposed method. The paper lacks a discussion on the scalability of the local search approach, especially as the dimensionality of the input space and the complexity of the network increase. A more detailed analysis of the computational complexity and convergence properties of the local search would be beneficial.

Moreover, for the Shepard interpolation neural networks, the architecture may be too simple to handle the complex nature of the modern tasks in inverse design. The paper does not explore the limitations of the Shepard interpolation network in capturing complex non-linear relationships, which are common in many inverse design problems. The choice of this architecture seems arbitrary without a thorough justification.

2.  The empirical evaluation is unconvincing without comparing with related constrained optimization techniques and baselines.

In the experiments,  it seems only one baseline is compared.  The comparison with related constrained optimization and other inverse design baselines (e.g., target generation techniques,  (off-line) black-box optimization techniques, etc. ).  Because of the missing comparison, it is unconvincing to justify the advantage and practical performance of the proposed method in inverse design. The paper needs to demonstrate that the proposed method can achieve comparable or better performance than existing state-of-the-art methods in constrained optimization and inverse design. The lack of such comparisons makes it difficult to assess the practical utility of the proposed approach.

Moreover, the experiments on MNIST and CelebA are two simple.  It is better to include more practical generation tasks, e.g., high-resolution (1024x1024) image tasks with more complex target properties for better evaluation. The current experiments do not adequately demonstrate the scalability and effectiveness of the proposed method on more complex and realistic datasets. The paper should include experiments on more challenging datasets and tasks to better evaluate the practical applicability of the proposed method.

### Questions
1.  What is the advantage of formulating the constrained optimization using the signed distance functions (SDF) compared with other constrained optimization solvers?  Please add a more detailed discussion and comparison with other constrained optimization solvers and approximated solvers. 

2.  In the experiments, the empirical evaluation is unconvincing without comparing with related constrained optimization techniques and baselines.  Please add more comparisons with related constrained optimization methods and inverse design methods to justify the advantage of the proposed method.  In addition,  please include an evaluation of high-resolution (1024x1024) image tasks with more complex target properties to justify the practical performance of the proposed methods.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces an SDF-based approach for solving composable constraints in inverse design tasks. The core idea lies in representing the constraints using SDF and then using gradient-based method to optimize. In order to tackle the computation of SDE, the solutions using SINN and with ReLU have been proposed. The method has been investigated on image datasets and molecule datasets, showing that it can effectively optimize towards the target design objectives.

### Strengths
1. The approach is well motivated, the overall presentation is clear, and the method is easy to follow.

2. The proposed method of computing SDF using SINN and with ReLU activations is interesting and should be appreciated.

3. The method has been validated on image and molecule datasets.

### Weaknesses
1. While the approach is interesting, the scalability and practical applicability remain unclear. See Q1.

2. Lacking experiments on more complicated and practically meaningful inverse design tasks. See Q2.

3. Lacking important baselines like classifier (or classifier-free) guided diffusion models for inverse design. See Q3.

### Questions
Q1. What is the time/memory complexity of the algorithm using SINN/ReLU? Can the algorithm scale to larger datasets or bigger models?

Q2. Instead of the relatively preliminary inverse design tasks here presented in the paper, there are a lot more that are of practical interest, such as [1], [2]. Can the method be applied to these tasks?

Q3. The proposed approach can be viewed as a gradient-based approach. There are many other methods that directly build in inverse design targets in the generation process, such as using classifier-guidance or classifier-free guidance approaches with diffusion models. These methods should be considered as a valid baseline and would probably be more time-efficient than the proposed approach judging from the runtime provided in the appendix.

[1] Song et al. Solving Inverse Problems in Medical Imaging with Score-Based Generative Models. ICLR'22.

[2] Bao et al. Equivariant Energy-Guided SDE for Inverse Molecular Design. ICLR'23.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposed a new optimization approach for inequality constraints modeled as signed distance functions (SDFs). The authors demonstrated the composability of SDFs and algorithms for approximating SDFs for a specific family of ML models of SINNs and piecewise linear nets. Experimental results on image and molecule datasets demonstrated better results.

### Strengths
- Algorithms for computing SDFs for SINNs and piecewise linear were proposed with solid mathematical proof.

### Weaknesses
1. **The motivation behind the paper on using SDFs for inequality constraints is unclear**. As a special case of the gradient-based method, it is unclear why we should use SDFs to model the constraints instead of directly optimizing along the gradient direction (or the reverse direction, depending on the task) of the objective $M(x)$. For all experiments in the paper, the thresholding operation seemed unnecessary, as a high metric always indicates better performance (e.g., more confidence in classification, or better synthesizability). The direct approach is also "composable" by summing over the gradient terms for different objectives.

2. **The generative models used in the paper were outdated**. VAE-based models are clearly inferior to diffusion or flow-based generative models, which have achieved remarkably better generation quality. Many existing pre-trained generative models exist with available checkpoints (e.g. Stable Diffusion series, [1], and [2] for molecules) and almost every up-to-date approach for solving inverse problems can be effectively applied to them (including, but not limited to [1], [3], [4], [5]). It is unclear why the authors did not carry out experiments on these models.

3. **The experiments were small-scale and limited**. In addition to the small and outdated generative model, the experiments were limited to classification tasks. Even though the authors proposed the approach to solving inverse problems, the standard inverse problems in CV domains like image inpainting, superresolution, and deblurring (all experimented in previous work) were never addressed.

4. **The baselines compared were extremely limited**. Essentially only the guided gradient approach was compared as the baseline, despite the fact that wide range of available methods for solving inverse problems. For example, [1]&[3] are gradient-free methods, [4]&[5] are gradient-based methods, and [6] is an RLHF approach applicable to non-differentiable objectives. [5]&[7] also extended constrained generation to molecule baselines. However, none of these approaches were compared.

5. **The proposed approach of calculating SDF may be time- and computation demanding**. The approximation for SDF relies on an iterative algorithm and differentiation through such an iterative procedure to obtain the gradient information. Therefore, it is expected to be extremely computation-intensive and memory-demanding, as all intermediate results must be stored for backpropagation. However, sampling time was never analyzed or provided as empirical results in the paper.

6. **Results in Figure 3 were extremely poor**. It looks as if the classifier has been adversarially attacked instead of generating the desired digit classes. The desirable digits were not even generated in (a)-(d) and were hardly distinguishable in (g). The captions are also confusing. If the authors started with some fixed image, which one was the starting image? Which one was the generation from the baseline?

7. Constraints in model machine learning practice often rely on a pre-trained model as the evaluator, e.g., the CLIP score in [4]. It is not practical to limit the classifier to piecewise linear nets or SINNs. The iterative algorithm also makes it prohibitively expensive to scale up to large pre-trained models like CLIP, especially when backpropagation is needed through the whole iterative algorithm.

### Questions
Besides the issues mentioned in the Weakness section, I have the following additional questions:

8. I do not understand the claim made in the paper that SDFs are computationally intractable. For a given evaluation function or a pre-trained evaluation model $M(x)$, the SDF can be easily calculated as $-\mathrm{sign}(M(x)-k)\\|M(x)-k\\|_2$ for the constraint $M(x)\ge k$, which does not require any iterative algorithm to calculate. One can always directly calculate the gradient with respect to this objective (or $-\mathrm{sign}(M(x)-k)\\|M(x)-k\\|_2^2$, for stability).

9. For the same reason, the gradient guidance baseline used in the paper seemed to have adopted an erroneous setting according to the objective in line 119-120. Such an objective is designed for equality constraints but not for inequality constraints. The objective mentioned in my previous question should be the correct objective instead.

### Soundness
1

### Presentation
2

### Contribution
1
