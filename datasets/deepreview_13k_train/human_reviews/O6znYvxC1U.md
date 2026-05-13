# Bayesian Treatment of the Spectrum of the Empirical Kernel in (Sub)Linear-Width Neural Networks

- Decision: Accept
- Scores: 5, 8, 6

## Abstract
We study Bayesian neural networks (BNNs) in the theoretical limits of infinitely increasing number of training examples, network width and input space dimension. Our findings establish new bridges between kernel-theoretic approaches and techniques derived from statistical mechanics through the correspondence between Mercer's eigenvalues and limiting spectral distributions of covariance matrices studied in random matrix theory. 
   Our theoretical contributions first consist in novel integral formulas that accurately describe the predictors of BNNs in the asymptotic linear-width and sublinear-width regimes. Moreover, we extend the recently developed renormalisation theory of deep linear neural networks, enabling a rigorous explanation of the mounting empirical evidence that hints at the theory's applicability to nonlinear BNNs with ReLU activations in the linear-width regime.
   From a practical standpoint, our results introduce a novel technique for estimating the predictor statistics of a trained BNN that is applicable to the sublinear-width regime where the predictions of the renormalisation theory are inaccurate.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies bayesian neural networks in the linear ($P/N = \text{constant}$ for data $P$ and width $N$) regime and sub-linear ($P/(N N_0) = \text{constant}$) regime. The authors operate under a spectral universality assumption, which treats the eigenfunctions of the limiting kernel as random with a covariance determined by the posterior kernel. The authors argue that this spectral universality assumption is logically equivalent to a kernel renormalization theory which was derived for deep linear networks. This kernel renormalization is a scale shift in the kernel by a variable $u$ which needs to be solved for self-consistently. In the sublinear regime, the kernels are rank-deficient which the authors acknowledge by allowing for a singular spectrum and utilizing the pseudo-inverse.

### Strengths
This paper studies the important problem of characterizing feature learning in nonlinear Bayesian neural networks and provides an original idea to apply a spectral universality idea to characterize feature learning. It further aims to justify some of the recent applications of kernel renormalization theory to nonlinear networks.  Showing that the spectral universality assumption implies and is implied by the kernel renormalization picture is an interesting contribution. The authors also provide a few experiments to support their claims.

### Weaknesses
However, the spectral universality assumption is not proven directly and the distribution of kernel eigenfunctions in either the proportional regime or the sublinear regime has not been characterized outside of the spectral universality assumption. The experiments are somewhat limited. I have a number of questions below, which if addressed could lead me to increase my score.

### Questions
1. What do the authors suspect would happen for networks in the $N \gg P$ regime with mean-field / $\mu$P scaling that preserves strong feature learning? In this case, [theory](https://arxiv.org/abs/2205.09653) predicts that the kernels are non-random but the preactivations can become non-Gaussian as was also shown in the [Bayesian setting](https://arxiv.org/abs/2406.16689). Do the spectral universality assumptions break down?
2. What do the authors think of the spectral universality assumption for cases where the matrices [pick up low rank spikes](https://arxiv.org/abs/2410.18938) such as learning single or multi-index models.  Do spiked kernels violate the kernel renormalization theory?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper gives integral formulas describing the outputs of BNNs in the linear and sublinear width regimes.

### Strengths
The theoretical contributions are extremely strong, especially around the integral formulas describing the outputs of BNNs in the linear and sublinear width regimes.

### Weaknesses
The primary weakness is around the experimental results.  These are restricted to MLPs on very simple datasets.  Though I would be happy to consider an argument that the results should generalise and/or that it would be prohibitively difficult to get results outside this setting.

The experimental results are presented very poorly.  For instance:
* The plots do not have labelled x and y-axes.
* The legends are very confusing. As an example: "on the left (respectively, on the right)."

There are also numerous prior works around deep kernel processes and machines that would be worth discussing in the related work:
* https://arxiv.org/abs/2010.01590
* https://arxiv.org/abs/2108.13097

while this work uses a very different theoretical approach, it ultimately addresses similar conceptual issues.

### Questions
N/A

### Soundness
3

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
4

### Summary
The authors propose combining ideas from random matrix theory to evaluate limits of infinite width Bayesian neural networks (such as the classic work by Neal (1996)) when the number of observations also goes to infinity as well as the number of input dimensions. The paper provides novel claims of the behavior of the limit in sublinear regimes.

### Strengths
Using Marchenko-Pastur to evaluate this type of limits, seems like a good idea. Combining these approaches with Mercer's theorem seems valuable. The ideas of random matrix theory in general seem underutilized in the ML community.

### Weaknesses
1. It is not immediately clear how the integrals in Theorem 3.4 can be explicitly evaluated. 
2. Notation for $\Phi^*$ in Theorem 3.4 was never defined.
3. Between lines 300 and 303, the authors claim that for __small__ datasets the computations would not be too computationally intensive. However, in footnote 3 (p. 6), they claim that the limit can be approximated using __large__ objects. It is not completely clear what has to be large or small for the evaluations to be feasible. 
4. Section 4 appears to be incomplete. It is not evident from the writing which of the figures correspond to the two examples they mention at the beginning of the section. 
5. In the first experiment they mention, with the "linear teacher", the authors do not specify how the $\beta$ is defined.

### Questions
1. For Figures 1 and 2, how many simulations are the authors using to obtain the error bars? Also, is there any uncertainty around the blue lines in the same figures? If so, it should be reported.
2. Can the authors reconcile the differences between the simulations in Figure 2 between their proposed estimates and the blue lines? 
3. In Theorem 3.3, the authors bring in the notation: 
$\mathbf{x}\sim \lim\_{{N_0}\to\infty} \mathbb{P}\_{N_0},$ without having defined $\mathbb{P}\_{N_0}$. 
Does $\mathbb{P}\_{N_0}$ correspond to $p\_\mathbf{x}$ for a specific dimension of $N\_0$?
4. The authors emphasize the rectified linear unit (ReLU) activation function (deservedly so). However I wonder if this approach can also work for other activation functions?

### Soundness
2

### Presentation
2

### Contribution
3
