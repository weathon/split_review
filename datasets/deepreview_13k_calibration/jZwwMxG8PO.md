# Extending Mercer's expansion to indefinite and asymmetric kernels

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Mercer's expansion and Mercer's theorem are cornerstone results in kernel theory. While the classical Mercer's theorem only considers continuous symmetric positive definite kernels, analogous expansions are effective in practice for indefinite and asymmetric kernels. In this paper we extend Mercer's expansion to continuous kernels, providing a rigorous theoretical underpinning for indefinite and asymmetric kernels. We begin by demonstrating that Mercer's expansion may not be pointwise convergent for continuous indefinite kernels, before proving that the expansion of continuous kernels with bounded variation uniformly in each variable separably converges pointwise almost everywhere, almost uniformly, and unconditionally almost everywhere. We also describe an algorithm for computing Mercer's expansion for general kernels and give new decay bounds on its terms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extended  Mercer’s theorem to any continuous kernels with bounded range, removing the original requirement for the kernel function to be symmetric and positive definite. Two main results are derived in this paper: first, it is proven that Mercer's expansion may not converge absolutely and uniformly for indefinite kernel; second, it is proven that a kernel with uniform bounded variation has Mercer's expansion that coverges pointwise a.e., a.u. and unconditionally a.e.. Notably, the authors described an algorithm for computing Mercer's expansion for general kernels.

### Strengths
1. The theoretical analysis in this paper is comprehensive and rigorous.

2. The paper establishes a theoretical foundation for Mercer’s expansion applied to non-regular kernels, such as indefinite and asymmetric kernels, potentially offering fundamental tools for future research in the theory of kernel-based method.

3.  A sufficient condition of uniformly bounded variation is proposed to ensure the validity of Mercer’s expansion.

### Weaknesses
The parameter $\alpha$  first appears in Theorem 2 (maybe I missed something)  before it is introduced (in Line 303). I suggest the authors make the writing more self-contained. The current results are limited to kernel functions defined on product intervals, specifically  $K: [a,b]\times [c,d]\to R$. While the authors provide a sufficient condition of uniformly bounded variation, the practical implications of this condition could be further explored. It is not immediately clear how restrictive this condition is in the context of commonly used kernels. For example, it would be beneficial to see a discussion of whether common kernels used in machine learning, such as Gaussian or polynomial kernels, satisfy this condition when extended to non-symmetric or indefinite cases. The paper would also benefit from a more detailed discussion on the limitations of the proposed algorithm for computing Mercer's expansion, especially in cases where the kernel is highly oscillatory or has discontinuities.

### Questions
The present results apply only to kernel functions defined on product intervals, specifically  $K: [a,b]\times [c,d]\to R$.  My question is whether by following a similar argument as that in your manuscript, these results could be extended to more general settings, such as compact domains or multiple dimensions.

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
3

### Summary
This manuscript studied the Mecer's decomposition for indefinite and asymmetric kernel. 

They extend Mercer's expansion to continuous kernels, providing some theoretical underpinning for indefinite and asymmetric kernels. 

1. Mercer's expansion may not be pointwise convergent for continuous indefinite kernels, 
2. Prove that the expansion of continuous kernels with bounded variation uniformly in each variable separably converges pointwise almost everywhere, almost uniformly, and unconditionally almost everywhere.
3. Describe an algorithm for computing Mercer's expansion for general kernels and give new decay bounds on its terms.

### Strengths
The authors claim to have established some fundamental results for ``Mercer's decomposition'' for indefinite, asymmetric kernels.

The following points seem novel to me:

1. It is generally expected that ``Mercer's decomposition'' does not behave well when the kernel \( K \) is not positive definite and asymmetric. The authors provide several examples of this behavior:
   - 1. It does not converge pointwise.
   - 2. It converges pointwise but not absolutely.
   - 3. It converges pointwise but not uniformly.

2. They demonstrate that if the decay rate of the singular values is sufficiently fast and there is some smoothness condition on the kernel, there are some unconditional convergence results.

3. They assert that the smoother the kernel, the faster the decay rate of the singular values.

### Weaknesses
The concern regarding the mathematical novelty of this paper is that most of the results in this manuscript are anticipated.

Since it is not fair to judge an ICLR paper solely based on its mathematical novelty, it would be beneficial if the authors could explore the necessity of studying Mercer's decomposition for indefinite, asymmetric kernels more thoroughly.

1.Could the authors discuss why the utilization of asymmetric kernels is necessary in data analysis?
2.Could the authors provide examples of several classes of asymmetric kernels of general interest?
3.Are there any application examples that demonstrate the use of asymmetric kernels?

### Questions
Same as the weakness. Especially the application consideration of the asymmetric kernel/

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper shows that if an asymmetric and non-positive definite kernel satisfies the uniform bounded variation property on the two coordinates (Eq. (3)), then it admits a Mercer decomposition which converges pointwise, unconditionally almost everywhere, and almost uniformly. Also, the paper provides an algorithm on computing Mercer expansion for general kernels.

### Strengths
The paper is written in a rigorous manner where the proof of the main theorem is stated clearly in the appendix. Also, the authors explain the importance of this paper as filling the gap in the literature on general asymmetric and non-positive definite kernels.

### Weaknesses
However, the contribution of the paper seems limited. The kernel needs to be defined on two (different) intervals in the theorem, which is too simple for practical implications. And the proof of the main theorem is more or less the result from Rademacher–Menchov Theorem and Hölder inequality. I think that the authors could have extended the proof to kernels with high-dimensional compact input spaces, or explain why it is difficult to perform such an extension. The practical utility of the algorithm presented in Section 5 is also unclear, as it is not explicitly stated whether this approach is novel or a standard technique. Furthermore, while the authors claim that the bounds in Eq. (8) are asymptotically tight, they do not provide sufficient empirical evidence to support this claim, which weakens the impact of the theoretical results.

### Questions
1. Could the authors explain why they did not extend the main theorem to kernels with high-dimensional compact input spaces?
2. I am not very familiar with but interested in computing/approximating Mercer extension of a general kernel. Is the procedure in section 5 novel or is it a standard approach in the literature? If it is novel, it is worth to explain more on the algorithm's complexity and accuracy. 
3. In line 639 "We believe the bounds in eq. (8) are asymptotically tight." Do you have any experimental results with general asymmetric kernels to support your hypothesis?

### Soundness
3

### Presentation
3

### Contribution
2
