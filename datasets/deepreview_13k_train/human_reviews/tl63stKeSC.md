# Solving PDEs via learnable quadrature

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Partial differential Equations (PDEs) are an essential tool across science and engineering. Recent work has shown how contemporary developments in machine learning models can directly help in improving methods for solution discovery of PDEs. This line of work falls under the umbrella of Physics-Informed Machine Learning. A key step in solving a PDE is to determine a set of points in the domain where the current iterate of the PDE's solution will be evaluated. The most prevalent strategy here is to use Monte Carlo sampling, but it is widely known to be sub-optimal in lower dimensions. We leverage recent advances in asymptotic expansions of quadrature nodes and weights (for weight functions belonging to the modified Gauss-Jacobi family) together with suitable adjustments for parameterization towards a data-driven framework for learnable quadrature rules. A direct benefit is a performance improvement in solving PDEs via neural networks, relative to existing alternatives, on a set of problems commonly studied in the literature. Beyond finding a standard solution for an instance of a single PDE, our construction enables learning rules to predict solutions for a given family of PDEs via a simple use of hyper-networks, a broadly useful capability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposed a method to sample the weights and locations of the collocation points used in physics-informed neural networks. The work proposes a data-driven method for sampling points by leveraging asymptotic expansions. The framework is provided for the strong and weak forms. For the strong form of PDEs weight function is proposed for collocation points, and for the weak form of PDEs, the weight function is used as a test function. The method's performance is also shown for a high-dimensional problem and for solving similar problems through hypernetworks.

### Strengths
The paper is nicely written and readable for the community. The paper tackles an existing problem in physics-informed neural networks. Choosing collocation points and their weights is challenging, and several advancements in PINNs have tried to tackle this problem.

Several comparisons are provided with baselines showcasing that the method performs well compared to other problems. 

With PINNs, one instance of PDE is generally solved, and with neural operators, a family of problems is solved concurrently. However, the latter requires a pre-computed dataset, often from a numerical solver. This paper tries to bridge the gap (although not the first paper to do so) in solving a family of problems through a PINN-based approach where no labeled datasets are required.

### Weaknesses
The number of collocation points taken in the numerical experiments is relatively low. It is not discussed why such a setting is kept for baseline methods, which typically require hundreds and thousands of points. The impact of this choice on the observed performance differences is unclear, especially given that methods like standard PINNs often benefit from a larger number of collocation points to better approximate the solution space. It would be beneficial to understand how the proposed method scales with an increased number of collocation points, and whether the observed performance gains are maintained or diminished in such scenarios. 

The presentation of Figures could be improved for better readability for the readers. Specifically, the axes labels and legends could be made more prominent, and the use of color could be optimized for better differentiation between different methods and results. The current figures make it difficult to quickly grasp the key findings and comparisons.

The choice of parameters in weight function is chosen empirically. The convergence of the proposed method may be largely dependent on those parameters. The lack of a systematic approach to parameter selection raises concerns about the robustness and generalizability of the method. A more rigorous analysis of the parameter space and its impact on the method's performance is needed to establish its reliability.

### Questions
First of all, most of the considered problems have smooth solutions, which are even tractable by the vanilla methods in the literature. It would be a nice experiment to see how the method performs for high-frequency functions/chaotic or multiscale problems.

The experiment provided for high dimension shows no significant gains with respect to the traditional Monte-Carlo approach. The authors reason the smooth solution to be the reason. Can the author perform a similar experiment for a problem that can help understand whether the method is advantageous in higher dimensions?

The authors have not compared their method with R3 [1]. Can the authors explain/compare the advantages/disadvantages compared to R3, one of the known methods in the adaptive collocation domain?

It would be nice to see the comparisons of the presented method with the baselines for more collocation points. Also, it is mentioned that the memory and computational costs of all the methods are almost identical. Does this relationship remain the same in the case with more collocation points? A quantitive comparison will also aid in assessing the method's training efficiency. In general, why is the method not trained with more collocation points?

Performing experiments for different parameter values of the proposed method would help readers to assess the robustness of the proposed method.

[1] Daw et al. Mitigating propagation failures in physics-informed neural networks using retain-resample-release (R3) sampling, ICML 2023.

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
4

### Summary
The authors discuss a data-driven method to compute quadrature weights for numerical integration used for the solution of partial differential equations. They introduce an algorithm to compute the weight functions, then obtain the quadrature points from it, and solve the PDE, all in an "end-to-end" pipeline. The procedure is demonstrated in several computational examples, solving the heat, wave, Burgers', diffusion, and advection PDEs.

### Strengths
The authors address a very important point in the solution of PDEs: where in space to evaluate the operators, and how to construct test functions for weak forms. Numerical integration in general (even beyond PDEs) is also an incredibly important topic, e.g. in the quantification of uncertainties (i.e., expectations that usually involves integrals).
The authors provide a good overview about classical schemes for integral weight constructions at the beginning. Data-dependent choice of test functions for weak forms, and choice of collocation points for strong form solutions, is at the heart of classical solution methods for PDEs, and both topics are being addressed in the paper. Learnable quadrature rule to compute the integral associated with the weak form is equally important, especially on more complicated domains and in higher dimensions, and the method may hold promise to address some of these challenges.

### Weaknesses
The structure of the paper, as well as language and typesetting, should be improved significantly. I detail my concerns below. Beyond these issues about first impressions, the numerical experiments that should show the strength of the approach are lacking in detail - even when considering the appendix - and are impossible to reproduce with the given text. One of the main concerns I have with the experiments is that the authors only rely on the PINN loss approach to solving very simple and low-dimensional PDEs, where much better classical methods exist. No comparison to classical approaches is presented, in fact, it seems the "classical solution" is sometimes used as the ground truth, making it very hard to argue why this new method is worth pursuing (if the classical method can outperform it already). Here are some of the concerns in more detail:

* The structure of the paper is very confusing, and the text does not help to mitigate this. Examples: 
   - section 5.2 has a lot of "subsections" with boldface text. This list has multiple different abstraction levels, and does not just consist of "several assumptions or simplifications" as stated at the beginning: "Simple Poles" is completely different from "Root finding and Implicit Function Theorem", which again is different (on an abstract level) from "How to parameterize?".

   - l. 343: "Our goal is to report a solution function u." This sentence is stated in the middle of a section on finding weights / roots of polynomials. The entire papers goal is the latter, not "to report a solution".

* There are a lot of typesetting and language mistakes. I will not list all, just examples:
   - l. 345: "We use a simple (MLP) based neural network" -> should be "We use a simple MLP-based neural network" (even though it rather should be "We use a MLP")
   
* The figures are not designed well and confusing. For example:
   - figure 3: Why is there text "interlacing of roots!" inside the figure? What do the p_n and p_{n+1} stand for, the points or the polynomials? Do the blue points also count for "p_{n+1}"? This is all not clear from looking at the figure, it is necessary to read the entire text (even more than the caption) to understand what is shown.
   - figure 4: the axes labels are way too small. 

* Algorithm 1 is not self-contained either. The "solution function u_\theta" is not referenced, but described in an earlier section "How to parameterize?" - and even there it is not clear how many neurons, how many layers, which activation function etc. is used for u. Also, "Gradient based update" in Algorihm 1 is unclear - is mini-batching used, or is it a non-stochastic algorithm (in which case I doubt in can converge to a reasonably good minimum). Also, why is "theta" a "module", not a set of parameter?


* l429: "This illustrates the viability of LearnQuad for high dimensional PDEs" -> in this example, the authors try to obtain the solution u(x)=sum_i x_i^2 in 100 dimensions. There are no details given on (a) how many data points were used, (b) how long the computations took, (c) how the test errors were computed, etc. One of the (many) challenges of solving PDEs in very high dimensions is the computation of integrals - which is necessary for the computation of "L2 relative error". How did the authors compute the integral in 100 dimensions? I tried to compare the value of the true u(x) to a simple average over the boundary of the cube (0,1) in 100 dimensions on 100,000 points (which is by far not nearly enough, even for Monte Carlo), and I also obtained a "relative L2 error" of 0.089. So even a constant approximation will yield errors similar to the one in the paper, at least when a (very inaccurate) test error computation is used.

### Questions
* Why do the authors use a PINN loss and not a proper PDE solver? The quadrature weights should be amenable for classical solvers, especially in low dimensions, and the accuracy for the obtained PDE solution should be many orders of magnitude better.
 * Table 2: "We report the absolute relative error compared to the numerical solution obtained using the same number of domain points". I do not understand this sentence at all. If a numerical scheme with *the same number of grid points* can be used as a "ground truth" solution, why is the new algorithm necessary at all? Could we not just use the "numerical solution obtained using the same number of domain points" to begin with?
 * For the example in 100 dimensions, how was the L2 error computed?

### Soundness
2

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
3

### Summary
This work aims to improve sampling of neural network to solve partial differential equations using physics-informed neural networks. Instead of using Monte-Carlo sampling, which is benefitial in high-dimensions but sub-optimal in low-dimensions, the authors propose a data-driven methods for learning quadrature rules. This relies on a family of orthogonal polynomials of the form $w(x) = (1-x)^\alpha (1+x)^\beta h(x)$, where $h$ is a positive function, and quadrature nodes associated with the Gauss-Jacobi weight functions. They apply their method on a family of PDE and show that they can reach lower error than alternative sampling method.

### Strengths
The introduction is well-written and the proposed method displays good performance over the alternative sampling techniques on all the problems considered.

### Weaknesses
I find the paper very confusing and a large time is spent in reviewing background material (e.g. on orthogonal polynomials). It is not clear why one cannot simply use a standard Gaussian quadrature (if the solution is smooth) or a deep Galerking method with a variational formulation based on finite elements (if the solution is not smooth) and why one needs to learn the weight function.

The experiments seem promising but it is not clear how the L^2 error is computed: is it using the learnt weight function or on a uniform grid. In any case, this requires some convergence analysis to analyze the convergence rate of the proposed quadrature rule as the number of sampling point increases. Otherwise, I do not know why I should use this over any standard quadrature rules.

There seems to be quite a lot of confusion in the presentation between weak form and strong form (see the questions).

- Line 49: I don't understand this paragraph: integrating the equation would just give you an equation between two real number, the first one would correspond to the average of u over the domain. After integration, it is impossible to recover u. To solve (1), one can either solve it in the strong form, or in the weak form after integrating by a test function (smooth with compact support).
- The choice of the quadrature rule is basically equivalent to the choice of basis functions to approximate u. If one uses a finite element method, then one can employ a quadrature rule on each mesh element that integrates polynomial exactly up to the FEM degree, hence making zero integration error, and similarly for spectral methods.
- line 98: I would refrain from making such novelty statement
- I do not understand why introducing Cauchy residue theorem is necessary or Section 3, and 5.1.
- line 154: this requires the function spaces for u and f. If $f=0$, then the solution is trivial as $u=0$ with the choice of boundary conditions.
- Is there a connection with adaptive mesh refinement?
- line 203: the choice of this particular weight function is not motivated
- line 215: fix formatting for the equation
- line 244: "enable learning", I do not understand what this means
- line 248: a general statement like this is meaningless as certain equations are very easy to solve. Training a neural network to solve a PDE is often (always?) more computational intensive.
- How do you compute the L2 error in the numerical section?

### Questions
- Line 49: I don't understand this paragraph: integrating the equation would just give you an equation between two real number, the first one would correspond to the average of u over the domain. After integration, it is impossible to recover u. To solve (1), one can either solve it in the strong form, or in the weak form after integrating by a test function (smooth with compact support).
- The choice of the quadrature rule is basically equivalent to the choice of basis functions to approximate u. If one uses a finite element method, then one can employ a quadrature rule on each mesh element that integrates polynomial exactly up to the FEM degree, hence making zero integration error, and similarly for spectral methods.
- line 98: I would refrain from making such novelty statement
- I do not understand why introducing Cauchy residue theorem is necessary or Section 3, and 5.1.
- line 154: this requires the function spaces for u and f. If $f=0$, then the solution is trivial as $u=0$ with the choice of boundary conditions.
- Is there a connection with adaptive mesh refinement?
- line 203: the choice of this particular weight function is not motivated
- line 215: fix formatting for the equation
- line 244: "enable learning", I do not understand what this means
- line 248: a general statement like this is meaningless as certain equations are very easy to solve. Training a neural network to solve a PDE is often (always?) more computational intensive.
- How do you compute the L2 error in the numerical section?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This article is a combination of numerical analysis and machine learning. Based on the classic Gauss-Jacobi iteration method, it uses data-driven (machine learning) methods to set relevant weights and node information, making numerical simulation (numerical integration and numerical solutions of differential equations) more accurate and efficient.

### Strengths
Advantages:

1. Combining traditional numerical analysis methods with modern machine learning is a very novel point. It is not difficult to see from the article that the new framework not only includes the advantages of traditional iterative methods, but also improves the shortcomings of traditional iterative methods to a certain extent. (Especially in residual and weak form)

2. The experimental results are very extensive, and the experimental examples are very extensive. (Appendix content)

3. Greedy optimization in details improves performance (reflected in saving optimization/training time)

### Weaknesses
Disadvantages:

1. I want to know if the convergence theory of traditional methods (including convergence, stability and consistency) is still valid under your model if the weights and interpolation points are learned (I think you can add more mathematical proofs), and whether the machine learning method can improve the iteration step size. Specifically, how does the data-driven approach affect the spectral radius of the iteration matrix, which is crucial for convergence? Does the learning process guarantee that the spectral radius remains less than one, or are there conditions under which divergence could occur? Furthermore, how does the adaptive selection of weights and nodes impact the consistency of the numerical scheme, especially in the context of varying mesh sizes or when dealing with highly non-linear PDEs?

2. In terms of experiments, since various learning solvers are emerging, you can compare the results with some classic machine learning PDE solvers on the market, such as PINN (although I know you mentioned this, but I think you can compare widely), DeepONet, kernel method, etc. A more comprehensive comparison should include not only final accuracy but also computational cost (training time, inference time), sensitivity to hyperparameter settings, and robustness to noisy data. For instance, how does the performance of the proposed method compare to PINNs when the training data is limited or corrupted by noise? How does the computational cost scale with the problem size compared to methods like DeepONet, which directly learn the solution operator?

3. When mentioning the weights of the classic numerical analysis method, I want to know what the distribution of sampling (you also mentioned MCMC in the article) should be like if data-driven means (machine learning) are used, that is, how to ensure a relatively balanced optimization in different dimensions (whether high or low dimensions)? Or is there any potential mathematical explanation for this? Specifically, how does the method ensure that the learned weights and nodes adequately cover the solution space, especially in high-dimensional problems where the curse of dimensionality is a significant concern? Is there a theoretical justification for the chosen sampling strategy, and how does it compare to other sampling techniques used in numerical integration and PDE solving?

### Questions
The experimental results are very good and general, and I hope authors could add/do more theoretical analysis. I will be happy to improve my score in subsequent discussions.

### Soundness
3

### Presentation
3

### Contribution
3
