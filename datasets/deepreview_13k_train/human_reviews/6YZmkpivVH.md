# TpopT: Efficient Trainable Template Optimization on Low-Dimensional Manifolds

- Decision: Reject
- Scores: 3, 5, 8, 6

## Abstract
In scientific and engineering scenarios, a recurring task is the detection of low-dimensional families of signals or patterns. A classic family of approaches, exemplified by template matching, aims to cover the search space with a dense template bank. While simple and highly interpretable, it suffers from poor computational efficiency due to unfavorable scaling in the signal space dimensionality. In this work, we study TpopT (TemPlate OPTimization) as an alternative scalable framework for detecting low-dimensional families of signals which maintains high interpretability. We provide a theoretical analysis of the convergence of Riemannian gradient descent for TpopT, and prove that it has a superior dimension scaling to covering. We also propose a practical TpopT framework for nonparametric signal sets, which incorporates techniques of embedding and kernel interpolation, and is further configurable into a trainable network architecture by unrolled optimization. The proposed trainable TpopT exhibits significantly improved efficiency-accuracy tradeoffs for gravitational wave detection, where matched filtering is currently a method of choice. We further illustrate the general applicability of this approach with experiments on handwritten digit data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the template matching problem :

$$\max_{s\in S} \langle s, x\rangle$$
where $x$ is a fixed observed signal, and $S$ is a manifold. $S$ is described with samples $s_1, \dots, s_n$. 
The baseline for this problem is matched filtering, which enumerates the set of samples and solves $\max_{s\in \{s_1, \dots s_n\}} \langle s, x\rangle$.
First, the authors analyze the theory of Riemannian gradient descent on $S$ to solve the problem. They show that if the algorithm is initialized close enough to the solution, we get exponential convergence. 
Then, the authors turn to a practical algorithm to solve the problem when one can only access samples $s_1, \dots, s_n$ describing the manifold. 
They propose to learn an embedding to a lower dimensional space and optimize over it: they build anchor points $\xi_1, \dots, \xi_n$ using a dimensionality reduction technique and then construct a function $s(\xi)$ from these points, in order to maximize $\langle s(\xi), x \rangle$.
The function is constructed by approximating its Jacobian with weighted least squares. The corresponding iterations are then unrolled in a neural network to make the whole procedure learnable.
The authors validate the method on a gravitational wave detection problem and on the mnist problem, where the goal is to detect the digit "3" from the other.

### Strengths
The paper is quite well written and is pleasant to read.
The problem tackled here is interesting, and the numerical results are encouraging.

### Weaknesses
The main weakness of the paper is that it proposes a pipeline that contains many different steps that are then unrolled. The authors do not propose an ablation study where we can clearly see the benefits of each step in the pipeline: what about a method without unrolling? what about a method that implements gradient descent without the smoothing of the jacobians? What about preconditioning? What about a method directly differentiating through the embedding map $s\to \xi$? What is the impact of the number of training samples on the performance of the unrolled method? What is the role of the hyperparameters?

The other main weakness of the paper is its theoretical analysis. The proposed method is an unrolled gradient descent over the parameters $\xi$ that aims at approximating gradient descent over a **parameterization** of the manifold (i.e., $\min_\xi \langle s(\xi), x\rangle$, where ideally $s(\xi)$ describes the whole manifold $S$). The theoretical part of the paper is about Riemannian gradient descent over $S$ itself. There are, therefore, barely any links between the method proposed by the authors in practice and that studied in theory, and the efficiency of the proposed practical method is not grounded in any theory.

### Questions
- I think it would be great to discuss how much of the results in thm.1. are due to the linearity of the objective function: what happens when the objective function is no longer linear? 
- Page 5: what is $\phi$ ? is it the same things as $s$? it is not clear what the domain of $\phi$ is. 
- In the implementation of gradient descent, one needs to compute $s(\xi)$. The authors explain in detail how they approximate the Jacobian of this map, but how is $s(\xi)$ itself approximated for $\xi \notin \{\xi_1, \dots, \xi_n\}$?
- The authors choose a compactly supported kernel to reduce computations, but it still requires to compute pairwise distances : how much computations does it really gain?
- Eq.17 is an affine equation between $\xi$ and $x$. Why would we need to learn all the matrices $W(\xi_i, k)$ when we can simply learn the full linear operator, which has far fewer parameters ?


Here are some Misc. remarks:
- some citations should be in parenthesis
- The sphere $\mathbb{S}^{D-1}$ should be defined
- Trivializations (Lezcano Casado, Mario. "Trivializations for gradient-based optimization on manifolds." Advances in Neural Information Processing Systems 32 (2019).) are a good reference for the discussion around eq.6.
-Equations 7 and 8 are missing references; to the best of my knowledge these are not novel. 
- A reference for multidimensional scaling, and its equivalence to PCA, is welcome.
- Fonts in figures are sometimes too small, they should be the same size as the main text's figures.
- The provided `TpopT_MNIST.ipynb` is not runnable, since the file `data_MNIST/data_dim3.pkl` is not provided. The `get_gradient` function also calls a `X_base` variable never defined. Please provide self-contained code.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is about signal detection. It proposes to replace (parameterized) template matching via exhaustive search over the search space by optimization. The running assumption is that the template space is a manifold (e.g. translations and rotations of a prototype, or gravitational waves generated by a model which depends on a small number of parameters).

The authors use Riemannian gradient descent on the template manifold. They prove that it converges to the "best" template (at the smallest angle) provided that it is initialized sufficiently close to the global optimum, where the value of "sufficiently close" depends on the curvature. Experiments on stylized gravitational waves and rotated and shifted MNIST suggest that the proposed method performs well in some settings.

### Strengths
I am not on top of the latest research in learning-based template matching, but I like this paper. It is well presented, written in a sober way, the results are clear and the application is important. It is commendable that the authors derived theoretical results and identified a parameter region where their method should outperform MF. The learning strategy via unrolling Riemannian gradient descent with kernel-smoothed gradients is elegant and well motivated.

### Weaknesses
On the negative side, the experiments are much too stylized, especially the MNIST one. Are there no real, complex datasets where one could test the proposed methods? (I am quite sure there must be.) At the very least one shuold eavlauate the performance on the MNIST toy example with noise, including a challenging setting with a lot of noise. It is also not completely clear (even after reading F.1) how much noise \sigma = 0.3 in the gravitational wave example actually corresponds to. When you say that the signal amplitude is constant at a=1, does it mean that it's normalized so that the inf-norm is 1? (I see that for waveforms it's the l2 normalization---are "waveforms" here "templates"?) It would be great (and necessary) to considerably improve the experiments.

Another thing that I am missing is the sliding window aspect (especially in the gravitational wave application). In streaming detection applications the signal is very long and one can take advantage of the FFT to efficiently compute the dot product with a template at many shifts (if S is generated by other groups which admit a FFT then those can be included as well). In experiments in this paper (at least that is how I interpret it) S is generated by varying some physical parameters but not the shift where the template occurs. It is not clear to me what would be faster in a real streaming application, especially when the signal manifold has dimension as low as 2.

Further, one can expect the landscape like the one in Figure 4 (right) whenever the involved signals are oscillatory. This problem is well studied for example in full waveform inversion where it's known as cycle skipping. It is often addressed by moving to some optimal transport-based loss instead of l2 (dot product). I also wonder about the suitability of PCA-style dimension reduction tactics for such oscillatory signals.

### Questions
In Section 4 (paragraph Embedding), are there conditions on d, n, N under which the suggested dimension reduction makes sense? Does the topology of S play a role anyhow?

One other confusing thing is about interpolation to get Jacobians (not smoothing). In (12) you introduce a kernel estimate of the Jacobian at some \xi_i which is in the dataset (it needs to be since you need s_i to compute (12)), but then later you need it for arbitrary points. Do you then obtain it by linear interpolation? Just synthesizing via PCA seems to result in a globally linear space which is not what you want.

Practicalities: what is \kappa in practice? How to know it? Can you given an estimate (and compare complexity with MF) in some cases?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors provided a proof of convergence of Riemannian gradient descent on the signal manifold, and demonstrated its superior dimension scaling compared to MF. We also proposed the trainable TpopT architecture that can handle general nonparametric families of signals.  In my view, this work represents a significant accomplishment.

### Strengths
The authors investigated the TpopT (TemPlate OPTimization) as an alternative scalable framework for detecting low-dimensional families of signals which maintains high interpretability, proved that it has a superior dimension scaling to covering and proposed a practical TpopT framework for nonparametric signal set.

### Weaknesses
My primary concern revolves around the assumption of $\sigma$ in Theorem 1. While I understand this assumption simplifies the conclusion, it imposes a stringent constraint that the noise variance must be significantly smaller than the initialization magnitude. This is a challenging condition to meet in practical scenarios. Specifically, the requirement that $\sigma$ scales inversely with $\sqrt{d}$ seems particularly restrictive, potentially limiting the applicability of the theoretical results to cases with very low intrinsic dimensionality. Furthermore, the proof relies on a bounded Riemannian Hessian matrix with the constant $L$, yet the main paper does not introduce any assumptions regarding the existence or smoothness of the Riemannian Hessian, which is a critical requirement for the convergence analysis of gradient descent on Riemannian manifolds. The absence of such assumptions makes the theoretical guarantees less robust.

In the main paper, the computational complexity of all methods should be presented in a tabular format. This would allow for a clear comparison of the computational costs associated with each method.

In the experimental results, it is essential to include a convergence comparison of all methods, not just final performance. This is necessary to effectively demonstrate the superior convergence properties of TpopT, rather than just its final accuracy. The current presentation lacks a clear visualization of how TpopT's optimization path compares to other methods.

According to Figure 5, my understanding is that when the number of hidden layers in the MLP increases, its performance may possibly become the best. If that is the case, what would be the advantage of TpopT? The paper needs to clarify the specific scenarios where TpopT outperforms deep learning methods, especially given the potential for MLPs to achieve high performance with sufficient complexity.

### Questions
1. My primary concern revolves around the assumption of $\sigma$ in Theorem 1. I understand that this assumption can simplify the conclusion, but it implies that the variance of noise should be much smaller than the initialization assumption, which is exceedingly challenging in practical scenarios. Furthermore, I have observed that the proof relies on a bounded Riemannian Hessian matrix with the constant $L$, yet the main paper does not introduce any assumptions regarding the existence of the Riemannian Hessian. I propose that the authors consider removing the assumptions related to $\sigma, \tau$, and $\epsilon$ and instead directly utilize $L$ and $\tau$ to characterize the convergence rate.

2. In the main paper, the computational complexity of all methods should be presented in a tabular format.

3. In the experimental results, it is essential to include a convergence comparison of all methods to effectively demonstrate the superiority of TpopT.

4. According to Figure 5, my understanding is that when the number of hidden layers in the MLP increases, its performance may possibly become the best. If that is the case, what would be the advantage of TpopT?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a scalable framework for identification of signals modeled via manifolds that searches for a best match template via optimization, in contrast with the common matched filter approach that searches for a best match in a fixed set of templates. The proposed approach uses a kernel space embedding of the manifold data points, where the navigation of the manifold uses gradient descent and is trained via the popular unrolled optimization approach.

### Strengths
The proposed approach relies on a combination of kernel methods and data-centric optimization of iterative approach parameter vectors and matrices.

Theoretical results provide probabilistic accuracy guarantees that depend on properties of the manifold.

### Weaknesses
The presentation is not always clear. The proposed algorithm is not crisply stated.

For several common applications of manifold (e.g., delay of arrival estimation and other 1-D manifolds), there is no comparison between the proposed approach and existing parametrizations (e.g., polar, spline, etc.). The parametrization have been helpful in reducing the computational complexity and the density of samples needed during navigation. In this sense, the comparison with only matched filtering is too coarse given the extent of the literature.

Some practical considerations are addressed via "brute force", e.g., pushing for global optimality by increasing the number of initializations of the algorithm.

While Section 4 says any embedding can be used, several assumptions are made as the narrative progresses.

Since this is a data-centric method, there should be more discussion of the quality and quantity of manifold sampling needed to have acceptable performance.

The experimental section does not illuminate the performance of the embedding parametrization, e.g., what is the quality of the manifold samples obtained from TPoP vs. other methods, including the aforementioned parameterized approximations. There is also no discussion of training computational complexity or storage requirements for the experiments, including a comparison to MP or other methods. Finally, the computational comparison is given only in terms of "complexity", not running time.

The potential upside to MP implemented using FFT is not limited to the noiseless case or the single-dimensional (time series) case; a comparison including this implementation would be fair.

Minor comments:

* The connection between the Jacobians in (15) and the embedding distances in (16) should be stated more explicitly.
* Similarly, the relationship between (17) and (6) should be explicitly described. 
* When discussing the computational complexity of TpopT after Figure 4, the authors should revisit the description of the parameters involved.
* There is a typo after eq. (22) "?"

### Questions
In (16), what is the value of i?

How is the formulation of supplement Theorems 2 and 12 (in particular eq. 2) comparable to Theorem 1 in the manuscript? 

Can the authors define the logarithmic map used in supplement eq. 20?

In supplement eq. 23, what does $$\Pi$$ represent?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
