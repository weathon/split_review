# Solving High Frequency and Multi-Scale PDEs with Gaussian Processes

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Machine learning based solvers have garnered much attention in physical simulation and scientific computing, with a prominent example, physics-informed neural networks (PINNs). However, PINNs often struggle to solve high-frequency and multi-scale PDEs, which can be due to spectral bias during neural network training. To address this problem, we resort to the Gaussian process (GP) framework. To flexibly capture the dominant frequencies, we model the power spectrum of the PDE solution with a student $t$ mixture or Gaussian mixture. We apply the inverse Fourier transform to obtain the covariance function (by  Wiener-Khinchin theorem). The covariance derived from the Gaussian mixture spectrum corresponds to the known spectral mixture kernel. Next,  
	we estimate the mixture weights in the log domain, which we show is equivalent to placing a Jeffreys prior. It automatically induces sparsity, prunes excessive frequencies, and adjusts the remaining toward the ground truth. Third, to enable efficient and scalable computation on massive collocation points, which are critical to capture high frequencies, we place the collocation points on a grid, and multiply our covariance function at each input dimension. We use the GP conditional mean to predict the solution and its derivatives so as to fit the boundary condition and the equation itself. 
	As a result, we can derive a Kronecker product structure in the covariance matrix. We use Kronecker product properties and multilinear algebra to promote computational efficiency and scalability, without low-rank approximations. We show the advantage of our method in systematic experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work uses Gaussian processes to solve partial differential equations. The authors propose to use a spectral mixture kernel and learn the mixture weights from data with a sparsity-inducing prior. To achieve scalability, they place collocation points on a grid and assume a product kernel which induces Kronecker structure in the resulting covariance matrices. The approach is then evaluated on three common model PDEs in one and two dimensions.

### Strengths
Overall, the paper presents a promising idea for how to solve certain classes of PDEs with Gaussian processes. The idea of using a sparsity-inducing prior over the frequencies of a spectral mixture kernel seems very useful and the paper demonstrates the robustness and applicability of the approach.

### Weaknesses
There are some weaknesses in the paper regarding the claimed novelty of the approach, the experimental evaluation and the proper attribution of existing approaches.

In my opinion the following two statements from the paper are incorrect or at least too strong for what is presented in the paper:

1. Quote from the Abstract (also mentioned in contributions): "The covariance derived from the Gaussian mixture spectrum corresponds to the known spectral mixture kernel. We are the ﬁrst to discover its rationale and effectiveness for PDE solving." In my opinion, this is incorrect. Härkönen et al. (2023) construct a specific kernel for linear PDEs, which as they write explicitly at the end of Section 4.1 recovers the spectral mixture kernel (Wilson et al. 2013) as a special case.
2. "By contrast, for PDE solving, it is natural to estimate the solution values on a grid, which opens the possibility of using Kronecker products for efﬁcient computation. To our knowledge, our work is the ﬁrst to realize this beneﬁt and use the Kronecker product structure to efﬁciently solve PDEs."I disagree with this being the first instance of Kronecker product structure being used to efficiently solved PDEs. First of all, Kronecker product structure (on regular grids) is being used to solve PDEs (either via preconditioners or via the connection of separation of variables and tensor numerical methods (e.g. Gavrilyuk et al. 2019)). Second, as the authors mention themselves in the manuscript, the computational efficiency of product kernels on regular grids is well-known for GPs (Saatci, 2012). Further, PDE solvers based on GPs which use tensor product kernels (specifically Matern) have also been proposed previously (e.g. Wang et al. 2021).

The experimental evaluation is largely well-done. I have some questions about the baselines that are compared against. Specifically, the vanilla GP baseline with a Matern kernel. Is this using a product kernel? The authors write in the paper that "[...] it is extremely costly or practically infeasible for the existent GP solvers to incorporate massive collocation points, due to the huge covariance matrix.". Why should one not be able to leverage the Kronecker product + Toeplitz structure (see Sections 3.1 and 3.2 of Wilson et al. 2015) of a product of Matern kernels for the vanilla GP case as well? If this was not done here, the baseline that is presented here seems rather weak. I can imagine that a scale mixture still outperforms a vanilla Matern kernel, but the performance gap in terms of time and memory should be significantly smaller I would expect.

The paper discusses related work from the domain of PINNs well, but misses some of the work on Gaussian-process based PDE solvers. For example, the following papers used GPs to solve PDEs:

- J. Cockayne, C. Oates, T. Sullivan, M. Girolami, *Probabilistic numerical methods for PDE-constrained Bayesian inverse problems*, AIP Conf. Proc. 1853 (2017)
- Wang, Junyang, et al. *Bayesian numerical methods for nonlinear partial differential equations.* Statistics and Computing 31, 2021 URL: https://arxiv.org/abs/2104.12587
- Pförtner, Marvin, et al. *Physics-informed Gaussian process regression generalizes linear PDE solvers.* arXiv preprint arXiv:2212.12474 (2022).
- Chen, Yifan, Houman Owhadi, and Florian Schäfer. *Sparse Cholesky factorization for solving nonlinear PDEs via Gaussian processes.* arXiv preprint arXiv:2304.01294 (2023).

### Questions
- What about the marginal uncertainty output by the Gaussian process? Does it capture the approximation error of the mean or is it miscalibrated? 
- What's the impact of the number of components of the mixture kernel on the approximated solution? An ablation such as a plot of number of components vs error would be informative. Also how does it affect the difficulty of the optimization problem? I could imagine choosing too many components makes the optimization problem significantly harder to solve in practice.
- Do the kernel matrices you define have Toeplitz structure? Stationary kernels on a 1D grid would have. This could further accelerate the required computations (see Section 3.2. of Wilson et al. 2015).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a solver for partial differential equations (PDE), specifically designed for high-fidelity and multi-scale PDEs, using Gaussian Process. Current PDE solver methods can be highly unstable and sensitive to hyperparameters. The authors bypass this problem by modeling the solution in the frequency domain and estimate target frequencies from the covariance function of the Gaussian process. The authors also propose an efficient algorithm to scale up the learning algorithm.

### Strengths
The authors described their method in detail, analyzed the runtime complexity, and provided multiple sets of experiments.

### Weaknesses
The paper abstract right now is very hard to follow for interested readers, instead of focussing on what the authors did in their methodologies, it should focus mainly on the contributions from a high level. The introduction clarifies the authors’ motivation well, however certain rearrangement of figures can help make it better. When the authors say their method is focussed on high fidelity and multi-scale PDEs, they can exhibit this with a figure (perhaps by moving figure 2,3 up in the first 2 pages).

“While effective, the performance of this method is unstable, and is highly sensitive to the number and
scales of the Gaussian variances, which are difficult to choose beforehand” - this statement should be associated with an example figure/experiment/prior work. The claim of instability needs more concrete evidence, perhaps by showing how small changes in hyperparameters lead to large variations in the solution quality. Furthermore, the sensitivity to the number and scales of Gaussian variances should be demonstrated with a specific example, showing how different choices affect the convergence and accuracy of the solution. Without this, the claim remains unsubstantiated and difficult to evaluate.

### Questions
See weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors consider the problem of solving high-frequency partial differential equations (PDEs) using a Gaussian Process approach. The aim is to propose an alternative to PINNs, which struggle for high-frequency or multiscale PDE using a GP framework. To do so, the authors consider a prior distribution of the solution to the PDE as a mixture of student t distributions to capture high frequencies. Then, they propose a computationally fast GP method, which consists of constructing a sample grid on the domain through a Cartesian product of points, which is then exploited in the algorithm.

### Strengths
- The paper is well-structured and the problem is clearly introduced and motivated.
- The authors perform several numerical experiments on synthetic datasets, which show that their method outperform PINNs in terms of resulting accuracy of the solution.

### Weaknesses
 - One of the weaknesses of the paper is that the difference between prior GP-based works in the literature is unclear. The authors should clearly state the differences between their work and the existing ones, in particular the papers by Chen et al (JCP, 2021) and Raissi et al (JCP, 2017), cited in this work. I believe that the two differences are: (1) The use of student-t distribution and (2) using a Kronecker product grid to speed-up computations. In the current version, the title and abstract of the paper might be misleading to readers in the sense that this paper is not the first one to consider solving a PDE with GP.
- I am very surprised by the Spectral method experiment performed by the authors. A quick experiment with Chebfun (https://www.chebfun.org/) allows me to solve the 1D Poisson equation to 10 digits accuracy in a fraction of a second.
- The authors state at the end of Section 5 that their work is "the first to [...] use the Kronecker product structure to efficiently solve PDEs". I believe this sentence is erroneous. It is completely natural when using spectral methods to exploit the Kronecker product structure of the domain (see e.g. Fortunato & Townsend, 2019).
- The authors offer very little conclusion and the main limitation section from the Appendix should appear in the main text. One of the key limitation of the method is that it is limited to simple geometry, where one can use a Kronecker product structure. However, this severely limits the applicability of the method and questions its advantages over spectral methods.

### Questions
- Is there any concrete advantage of using the Student t distribution over the Gaussian distribution? The authors state that the Student t distribution is beneficial for high frequency but the performance seems very similar in the experiments of Table 1.
- The experiments in Section 6 should provide the source terms (at least in Appendix) to allow for reproducibility.
- Equation (6) should include the domain on which the integration is performed.
- Minor comment: 2nd sentence of p.2: "the performance of this method is unstable" -> "this method is unstable"
- Section 6: Timings should be reported in main text as it's one of the main advantage of the proposed method.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses the numerical solution of multi-scale partial differential equations (PDEs) with Gaussian processes (GPs).
To this end, the submission proposes to use variations of the spectral mixture kernel as a prior model.
Additionally, selecting a covariance function that factorises into the product of dimension-wise covariances implies a Kronecker structure in the covariance matrices.
As a result, the algorithm requires less-than-cubic complexity to evaluate the loss function, and a user can optimise the PDE solution and (hyper)parameters efficiently. 
Experiments demonstrate the advantage of this method over physics-informed neural networks and those Gaussian-process-based solvers that use more traditional prior distributions.

### Strengths
The topic of the paper (machine-learning-based PDE solvers) is of growing interest in the ICLR community and contributes some valuable concepts to this area. More specifically, the following contributions are novel, to the best of my knowledge:

* Using a spectral mixture kernel for solving multi-scale PDEs
* Numerically optimising the joint distribution of PDE solution and PDE information can be efficient if a Kronecker-factorised prior is used (something that is not necessarily the case for more traditional MLE or MAP estimation without further assumptions).

The manuscript is easy to follow for a reader who is roughly familiar with physics-informed neural networks, PDEs, and GPs.
Overall, I consider this to be a good paper.

### Weaknesses
The weaknesses of this submission are mostly presentational (with two exceptions that concern the experiments).
I believe the following issues can _and should_ all be corrected before publication.


1. The manuscript misses a range of closely related work about solving partial differential equations with Gaussian processes:

    * Howhadi [1] discusses Bayesian numerical homogenisation (solving multi-scale PDEs with GPs), a central piece of related work that this paper should address prominently. 
    * Accessing the derivatives of the Gaussian process as a function of $\vec{\mathcal{U}}$ (the trick suggested in Equation (13)) is discussed in Section 2 and Section 3 in the paper by Krämer et al. [2].
    * The related work section (Section 5) mentions the work on solving PDEs with GPs by Chen et al. (2021) and Long et al. (2022b) but completely misses all work that belongs to the field of probabilistic numerical algorithms (see, for instance, [1-3] below and the references therein).

    I am aware that large parts of the ICLR community may be more familiar with physics-informed neural networks than with Gaussian-process-based differential-equation solvers and that taking this into account for the exposition therefore makes sense for an ICLR paper. However, the works mentioned above are closely related and must be discussed appropriately.

2. I am surprised the submission never mentions traditional approaches to solving multi-scale problems, such as those based on numerical homogenisation (a starting point could be [4]). I know that the paper targets the ICLR community and that large parts of this community may be more interested in machine-learning-based PDE solvers than traditional PDE solvers. Still, existing approaches should be credited by (at least) mentioning their existence. (This relates to point 4. below)

3. I am also surprised that the experiments only discuss the precision of the approximations rather than the work required to achieve this precision. The experiments in Appendix C suggest that the per-iteration runtime of the proposed algorithm is comparable to that of a physics-informed neural network. However, Figure 9 indicates that tens of thousands of iterations are needed. What is each algorithm's overall runtime (training time) to achieve the precisions in Tables 1 and 2?

4. What would we find if we included a non-machine-learning-based solver in the experiments and compared the runtime to the accuracy of all these methods? I would like to see this comparison. I am not saying that the proposed method must outperform traditional solvers, which have been studied and optimised for a long time, but that the context is critical.


5. This could be personal taste, but I think the paper might benefit from a slightly more rigorous notation surrounding Equation (14), for instance, by clarifying which joint probability density Equation (14) is the logarithm of. I am imagining something like mentioning $$\mathcal{L} = \log p(\mathcal{U}, \mathcal{H} \mid \Theta, \tau_1, \tau_2)$$ somewhere at the beginning of Section 4. Contextualising this term against the maximum-a-posteriori and maximum-likelihood loss for the same estimation problem would be even better. What do the authors think?


I consider points 1 and 2 essential and 3 and 5 slightly less important to resolve before publication. 
I expect all four of those issues to be relatively straightforward to fix.
Point 4 would be optional, as incorporating it is non-trivial. However, I would like to see those results.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
