# Alternating Projections With Volume Sampling

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
The method of Alternating Projections (AP) is a fundamental iterative technique with applications to problems in machine learning, optimization and signal processing. Examples include the Gauss-Seidel algorithm which is used to solve large-scale regression problems and the Kaczmarz and projections onto convex sets (POCS) algorithms that are fundamental to iterative reconstruction. Progress has been made with regards to the questions of efficiency and rate of convergence in the randomized setting of the AP method. Here, we extend these results with volume sampling to block (batch) sizes greater than 1 and provide explicit formulas that relate the convergence rate bounds to the spectrum of the underlying system. These results, together with a trace formula and associated volume sampling, prove that convergence rates monotonically improve with larger block sizes, a feature that can not be guaranteed in general with uniform sampling (e.g., in SGD).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper study the spectral gap of the projection operators appearing in Randomized Gauss-Seidel and Kaczmarz method, and establish a bound that associates with the spectrum of the coefficient matrix in a recursive way.

### Strengths
The result of this paper is overall interesting.

### Weaknesses
While the result is interesting, whether it is useful or important is questionable, and it also seems not difficult to obtain the result. Moreover,  the organization and presentation of the paper can be improved. For example, the last line on pg. 1 is too long to understand; more details on the existing results of the randomized block Gauss-Seidel and randomized block Kaczmarz could be provided and compared so that the readers can appreciate the importance of the work more.

While I understand the importance of solving large scale linear systems, I am still not sure whether volume sampling is very practical or not. Could you please  provide more details on the volume based sampling, e.g., the computational complexity of it, in addition to just mentioning several references?

I am not sure  whether "increasing batch size under volume sampling always guarantees improvements" is true or not in practice. For example, if $A\in\mathbb{R}^{m\times n} ~(m\ge n)$ is a Gaussian matrix,  by the random matrix theory, the condition number of any $n\times n$ block would be very large, it will even be unstable to solve this sub-system. Maybe more numerical experiments are desirable.

I didn't state the last question clearly. I was meaning why randomized block Kaczamarz method is not tested?

### Questions
1) Why $\lambda_\min$ is referred to as spectral "gap"?
2)  Assume $A\in\mathbb{R}^{m\times n}$ is a random Gaussian matrix. For randomized block, will it work well if the block size is $n$? If not, is there an interpretation based on the quantity provided in the paper?
3) Why only randomized block Gauss-Seidel is tested in the experiments?

### Soundness
3

### Presentation
2

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
The paper focuses on improving the efficiency and convergence rate of alternating projection methods in a randomized setting. By incorporating volume sampling for block sizes greater than 1, explicit formulas are derived to relate convergence rate bounds to the underlying system's spectrum. The authors argue that the results, combined with a trace formula and volume sampling, demonstrate that larger block sizes lead to monotonically improving convergence rates.

### Strengths
While the analytical investigations presented in the manuscript appear to be sound, their current impact and significance appear marginal.

### Weaknesses
This manuscript exhibits a disregard for advancements and established findings within the field (e.g., Chung et al. on ``Sampled limited memory methods for massive linear inverse problems'', Dereziński and Mahony on ``Recent and Upcoming Developments in Randomized Numerical Linear Algebra for Machine Learning''). Various authors have investigated block alternating projection methods which remains uncited. The authors' assertion that Stochastic Gradient Descent (SGD) is limited to one-row sampling is inaccurate. In fact, the SGD may include any number of samples of the matrix A.  The authors use a confusing non-standard mathematical notation employed throughout the manuscript making it harder for readers to follow. For instance, the conditional statement "a \in A" lacks clarity and rigorous definition. The authors' claim that the randomized Kaczmarz minimizes the objective function f(x) = ||x-x_\star||, where x_\star is the solution of Ax = b, makes no sense to me. Additionally, the authors do not make it accessible to the reader what algorithms are ``Feller'' means. The manuscript suffers from precision in methodology and analysis. Beyond that analytical investigations, and relevant applications are missing.

A more comprehensive and in-depth analysis and a presentation of a large-scale application would be necessary to fully appreciate their potential contributions to the field.

### Questions
see above

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
3

### Summary
This paper proposed a new algorithm for solving linear systems Ax=b, with adaptive minibatch sampling probabilities. The new approach incorporate volume sampling and tricks for reducing computational overhead to O(n) per iteration. The authors provide theoretical convergence analysis of the proposed method, demonstrating significant benefits over standard Gauss-Seidl methods. The numerical experiments validates the theoretical results.

### Strengths
The theoretical and algorithmic contribution appears to be solid and novel. To the best of the reviewer's knowledge this work is the first one to show such convergence rates is achievable. However, the reviewer is not familiar with this line of work, so could be overrating the novelty of the paper.

### Weaknesses
The numerical experiments remain a significant weakness. The absence of a direct comparison to a standard randomized block Gauss-Seidel method makes it difficult to assess the practical advantages of the proposed algorithm. The current experiments only demonstrate that increasing batch size improves convergence, which is not sufficient to justify the complexity of the proposed method. The use of synthetic data further limits the impact of the experimental results, as it is unclear how the method would perform on real-world datasets with different characteristics. The paper would benefit from experiments on real datasets, such as those found in the UCI repository or LIBSVM, to demonstrate the practical applicability of the proposed method. The lack of comparison to existing methods, such as those discussed in Gower, R. M., & Richtárik, P. (2015), makes it hard to understand the novelty of the work in practice.

### Questions
Please improve the numerical studies, as mentioned above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the problem of solving the linear equation $ Ax = b $ using a randomized sequential approach, where in each iteration, the vector $ x $ is updated along a small number of randomly selected directions. Two specific instances of this approach, known as the Gauss-Seidel and Kaczmarz algorithms, are examined in detail. The convergence rate of this algorithm is characterized by the spectral gap of the associated Markov semigroup, which, in the context of this problem, is equal to the expectation of a certain random projector. 

The paper's main contributions are presented in Theorems 2 and 3, where a recursive formula is derived for calculating this expectation. Specifically, if the randomly chosen blocks are of size $ n$, and the probability of selecting each block is proportional to the squared volume of the parallelepiped formed by the rows of  $A $ corresponding to that block, then the expectation $\Phi_n$ of the random projector satisfies the relation
$$
\Phi_n = \Phi_1 \left( \frac{{\mathrm{Tr}}(\Phi_{n-1})}{n-1} \mathbf{I} - \Phi_{n-1} \right).
$$
The paper provides full proof of this result and includes numerical experiments demonstrating the proposed methodology's practicality and effectiveness.

### Strengths
The paper deals with a simple problem that a large audience can understand.

The material is rather well presented.

### Weaknesses
1. In my view, the primary weakness of the paper lies in the relevance of its results to the ICLR community. While the problem addressed is indeed elegant in its simplicity, its broader applicability to machine learning remains unclear. Specifically, the linear equation $Ax = b$ can be viewed as finding the stationary points of the quadratic function $f(x) = \|Ax - b\|^2$. Consequently, a natural next step would be to explore how these results could extend to the more general problem of minimizing an arbitrary loss function $f(x)$.   
  However, the paper lacks discussion on potential extensions in this direction. It would enhance the impact and relevance of the work if the authors demonstrated that the analyzed algorithms are, in fact, special cases of more general optimization algorithms applied to $f(x)$, with a quadratic function as a specific instance. Such an extension or contextualization would not only strengthen the theoretical insights but also significantly broaden the practical appeal to the ICLR audience, who are often focused on non-linear and complex loss landscapes in machine learning tasks.

2. I believe the presentation of the main results could be significantly enhanced. Specifically, the statements in Theorems 1 and 3 may not fully warrant their designation as theorems. Theorem 1 could be more appropriately presented as a proposition or lemma, while Theorem 3 might be better formatted as a numbered equation. In my view, the paper would benefit from having a single theorem that consolidates the claims currently in Theorems 2 and 3.

3. I have some doubts concerning the proof of Theorem 2. See the question in the next section.  
 
4. Below are the typos that I found:

- line 74: I believe that the function $f(x)$ should be defined as $f(x) = \|A^{-1/2}(b - Ax)\|^2$, otherwise I do not manage to obtain Eq. (1).
- line 95: "rows of $a\in A$" -> "rows $a\in A$"
- line 108: "It is easy"
- line 131: the denominator $M$ should be replaced by the squared Forbenius norm of $A$, which is also the same as $\mathrm{Tr}(AA^T)$.
- line 132: the denominator $N$ should be replaced by the squared Forbenius norm of $A^{1/2}$, which is also the same as $\mathrm{Tr}(A)$.
- line 219: remove either "a" or "the" in "a the recursive"
- line 220: "analysis of the set"
- line 221: "subset $A_n$" -> "subsets $A_n$"
- Several places in Section 4.1: "projector to" -> "projector into"
- line 294: I do not understand the sentence ``We first establish $E[P_n]$ ..., and in the following section..."
- line 346: "volume squared" -> "squared volume" ?

5. There is an issue with how references are cited within the text. I recommend using the LaTeX command \citep when the reference is not integral to the sentence structure.

### Questions
The proof of Theorem 2 appears to contain flaws in its current form. While this issue might be possible to address, it does not seem to be a straightforward fix. Indeed, the proof relies on the fact that the right hand side of the equation on line 320 is equal to the expression given on line 326, with $1$ replaced by $s$ and summed over all $s$ from 1 to $n$. Here, the authors use Theorem 1. However, Theorem 1 is true when the vectors are linearly independent. The right-hand side (RHS) of the display on line 320 contains also $Q_n$s corresponding to linearly dependent $a_1,\ldots,a_n$. Of course, the corresponding term in the RHS of line 320 is then zero, but it is not clear to me that in such a case $\sum_{s=1}^n Q_1^s\big((v_{n-1}^{\bar s})^2\mathbf I - Q_{n-1}^{\bar s}\big) = 0$.

### Soundness
2

### Presentation
3

### Contribution
1
