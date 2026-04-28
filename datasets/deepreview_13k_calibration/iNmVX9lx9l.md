# Fast Summation of Radial Kernels via QMC Slicing

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The fast computation of large kernel sums is a challenging task, which arises as a subproblem in any kernel method.
We approach the problem by slicing,  which relies on random projections
to one-dimensional subspaces and fast Fourier summation. We prove bounds for the slicing error and
propose a quasi-Monte Carlo (QMC) approach for selecting the projections based on spherical quadrature rules.
Numerical examples demonstrate that our QMC-slicing approach significantly outperforms existing methods
like (QMC-)random Fourier features, orthogonal Fourier features or non-QMC slicing  on standard test datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In order to reduce the compute time of kernel summations in large dimension, this paper studies 1D slicing when computing kernels on R^d of the form (x,x’) -> F(\| x – x’ \|). The paper is directly built on a work of Hertrich (2024), that introduced the framework of the generalized Riemann-Liouville fractional integral transform to characterize the relationship between the sliced approximation and its target. In a first contribution, a novel error bound is proven with a characterization of the variance of the estimator when Slices are uniformly distributed. In a second contribution, the authors discuss quasi-Monte-Carlo designs (spherical, Sobol) to choose the slices and improve the error rates. The paper is completed by numerical simulation on summations of kernels on artificial data and on MNIST data. While QMC-slicing is interesting in terms of approximation error (convergence rate) their design is expensive and prohibitive for d>= 3.

### Strengths
Although slicing has been thoroughly explored in reducing the complexity in time of optimal transport, slicing the computation of kernels is a novel topic, very rencelty introduced.
- The novel error bound differs from Hertrich (2024, SIAM Journal on Mathematics of Data Science and arxiv) with a characterization of the vairance of the slicing estimator, which confirms the rate in O(1/sqrt(P)).
- The most interesting and promising part from my point of view is related to the exploration of quadrature rules to construct the sequence of slices and not sampling it. The proposed scheme (approximation of a spherical design) comes with a bound on the approximation error.

### Weaknesses
 - About the motivation:The number of data is usually considered as the most emblematic issue with kernels in Machine Learning and existing approximation schemes aim at reducing the compute time involved by operations with the Gram matrix as well as the complexity in memory. The authors motivate their work by the case when the dimension of data is large. Contrary to optimal transport problems that are defined in a variational way,  computing sums of kernels at the era of distributed computing is not a crucial obstacle.

- Limited contribution given previous works:
The most important weakness of the paper is its incrementality with respect to the work of Hertrich (2024) well cited in the paper. 
The revisited error bound in the case of the Monte-Carlo estimate does not seem sufficient to make a difference so the new component of the work deals with the proposition of the quasi-Monte-Carlo design for the slicing method.
- No applicabe scale for the spherical deisgn: Unfortunately, the spherical design studied in depth here cannot be reasonably computed for  realistic values of d. 
So finally either Monte-Carlo estimation or classic Sobol sequences have to be used in practise (dataset MNIST) which again limits dratsically the novelty of the paper.

In terms of experiments, I would not consider the dimension of MNIST data as a computational obstacle and would definitevely expect higher dimensional data for a conference like ICLR.

Moreover it would have been interesting to apply this new approximated way to compute sums of kernels in a statistical kernel-based test or in an online learning algorithm of a kernel machine where this approximation can make sense. Studying then the convergence of the obtained estimator would have been entirely new.

### Questions
1° Can you comment on the interest of slicing in Optimal Transport versus in kernel summation ? 
2° It would be interesting to describe the differences point by point of this work and those of Hertrich (2024).
3° Could you clearly describe the analytical complexity in time of each QMC scheme ?
4° Can you find and experiment an example in Machine learning where the sliced kernels can make a difference ? 
5° is it possible to run the same tests on larger dimensional data ?

After rebuttal, I've increased my score (most of the concerns have been addressed except those concerning the experimental results.

### Soundness
3

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
4

### Summary
This paper proposes a quasi-Monte Carlo (QMC) slicing approach for fast radial kernel summation, which is commonly required in kernel methods across machine learning. By using QMC sequences and spherical quadrature rules, the authors derive error bounds for various kernels, such as the Gauss, Laplace, and Matérn kernels, and show that QMC slicing significantly improves computation time and accuracy. Numerical experiments confirm that QMC slicing outperforms non-QMC slicing and other approximation methods, particularly in lower-dimensional cases, while maintaining favorable error rates.

### Strengths
1.The QMC slicing method introduces an approach to fast kernel summation.
2.The methodology is well-documented, with explanations of error bounds and smoothness results.
3.QMC slicing has the potential to improve efficiency in kernel-based methods.

### Weaknesses
1.The adaptability of the theoretical error bounds to various types of data and kernels remains unclear.
2.While effective, the QMC slicing method lacks clear differentiation from existing fast summation methods, such as Random Fourier Features (RFF).
3.Experiments are focused on limited, synthetic datasets, raising concerns about the method's generalizability.
4.Some parts of the theory section are overly condensed, especially around error bounds and smoothness assumptions.

### Questions
1.How scalable is the QMC slicing method for very high-dimensional data (e.g., 100+ dimensions)?
2.Does the QMC slicing approach generalize to non-standard kernels often used in machine learning?
3.How do theoretical error bounds hold up on real-world datasets with noise and variability?
4.Can the authors compare the computational efficiency of QMC slicing to Random Fourier Features and other fast summation methods?
5.What are the practical trade-offs in terms of error convergence rate with QMC slicing?
6.Are there specific use cases or domains where this approach is expected to outperform current alternatives?

### Soundness
2

### Presentation
3

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
The paper proposes a slicing based fast calculation of the sum of radial kernels. The authors analyses bounds on slicing error, and ensure a better error rate based on the smoothness result.

### Strengths
- The theoretical analysis in the paper seemingly technically sound, though I couldn't follow the proofs.

### Weaknesses
 - Overall, the paper is difficult to follow those who are not familiar with the topic. Readability can be improved.

- Empirical evaluation is only on purely kernel sum calculations. Showing benefit on actual computation of some learning model would have been convincing.

### Questions
- How is the optimization problem (10) is solved in practice? How large is this additional computational cost? Figure 2 contains it? In particular, when P and d is large, it seems expensive.

### Soundness
3

### Presentation
2

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
This paper derived the error bounds of slicing, a fast approximation algorithm for computing kernel sums, for various kernels. The paper also incorporated quasi-Monte Carlo (QMC) sequences on the sphere into the slicing method to improve its error rate. The paper conducted experiments to demonstrate that the QMC-slicing approach outperforms the non-QMC slicing method and other baselines like Random Fourier Features (RFF) in terms of error rate.

### Strengths
1. The authors proposed the QMC-slicing method and demonstrated that it has better error rates than the original slicing method. The QMC-slicing method exhibits a better expected error bound than RFF while maintaining a similar time complexity; this demonstrates its effectiveness and potential as a fast kernel summation algorithm.
2. The authors provided a comprehensive analysis of the slicing error for the negative distance kernel, the thin plate spline, the Laplace kernel and the Gauss kernel. The derived error bounds could be useful for future research on slicing and fast kernel summation.
3. Overall, the paper is well-written and clear to understand. Background knowledge on fast kernel summation, slicing and QMC are well-explained. Details of derivation, e.g. the applicability of the QMC methods for slicing, have been sufficiently provided.

### Weaknesses
1. The authors considered several QMC sequences in the experiments, and observed difference in slicing error between these different sequences. It would be helpful if the authors could further analyze the results and discuss more on how the choice of QMC sequences affects slicing error, under what circumstances would some QMC sequences outperform others, etc. Specifically, the paper lacks a detailed discussion on the properties of different QMC sequences (e.g., discrepancy, uniformity) and how these properties relate to the observed error rates in the slicing method. For instance, while the authors mention using distance QMC designs, they do not delve into why these designs perform better than other QMC sequences, such as Sobol or Halton sequences, in the context of slicing. A more in-depth analysis of the interplay between QMC sequence characteristics and the specific requirements of the slicing algorithm would significantly strengthen the paper.
2. As mentioned in Section 5, the observed error rates of QMC-slicing are significantly better than the theory. It would be helpful if the authors discuss more about this phenomenon and the reason behind it. The paper should explore potential reasons for this discrepancy, such as the specific properties of the kernel functions used or the limitations of the theoretical bounds. A discussion on whether the theoretical bounds are tight or if there are other factors contributing to the better-than-expected performance would be beneficial. It would also be useful to investigate if the observed error rates follow a different scaling with respect to the number of slices or the dimensionality compared to the theoretical predictions.

### Questions
1. The authors mentioned that QMC-slicing exhibits a smaller advantage in high dimensions (d=200), but it still outperforms other baselines. What if the dimensionality is even higher, e.g. d=10,000? Does QMC-slicing still perform better than slicing and (QMC-)RFF?
2. In this paper, only Gauss, Laplace, Matern and negative distance kernels are considered. How would QMC-slicing perform in the case of other kernels, e.g. sigmoid kernel?

### Soundness
3

### Presentation
3

### Contribution
3
