# Maximum Coverage in Turnstile Streams with Applications to Fingerprinting Measures

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
In the maximum coverage problem we are given $d$ subsets from a universe $[n]$, and the goal is to output at most $k$ subsets such that their union covers the largest possible number of distinct items. The input can be formalized as an $n \times d$ matrix $A$ where entry $A_{ij} \neq 0$ if item $i$ is covered by subset $j$ and $A_{ij} = 0$ otherwise.  In this paper we create the first linear sketch to solve the maximum coverage problem. The sketch has size sublinear in the input and is directly applicable to distributed and streaming settings, often offering significant runtime improvements. We focus on the application to the turnstile streaming model which supports insertions and deletions. In this model, updates take the form $(i,j, \pm 1)$ which update $A_{ij}$ to $A_{ij} + 1$ or $A_{ij} - 1$, depending on the sign. Previous work has largely focused on more restrictive models, such as the set-arrival model where each update reveals an entire column of $A$, or the insertion-only model which does not allow deletions. We design an algorithm with an $\tilde{O}(d/\varepsilon^3)$ space bound for all $k \geq 0$. We note that when $k$ is constant, this space bound is nearly optimal up to logarithmic factors.

We then turn to fingerprinting for risk measurement. The input is an $n \times d$ matrix $A$ where there are $n$ users and $d$ features, and the goal is to determine which $k$ features (or columns in $A$) together pose the greatest re-identification risk. Our maximum coverage sketch directly enables a solution to targeted fingerprinting for risk measurement. Furthermore, we present a result of independent interest: a linear sketch of the complement of $F_p$, the $p^{\text{th}}$ frequency moment, for $p \geq 2$. We use this sketch to solve general fingerprinting for risk management. Empirical evaluation confirms the practicality of our fingerprinting algorithms, demonstrating a speedup of up to $210$x over prior work. We also demonstrate that our general fingerprinting algorithm can serve as a dimensionality reduction technique, with an application to facilitating enhanced feature selection efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper the authors consider the problem of choosing at most k subsets from a stream such that the number of distinct items covered by the subsets is maximized. This is an interesting problem with applications in other areas - as demonstrated in the paper. The authors give a O~(d/\epsilon^2) algorithm where d is the number of sets in the stream and \epsilon is an approximation parameter.

### Strengths
The algorithms presented in the paper are interesting.

### Weaknesses
It is clear that the most important parameter is k. And when analysis the complexity of the algorithms the authors have avoided discussing the dependency of the space complexity on k. This makes it very hard to properly judge the true contribution of the paper. The analysis focuses on the number of sets, d, and the approximation parameter, epsilon, but the impact of k on memory usage is not clearly articulated. Specifically, the space complexity is given as O~(d/epsilon^2), which hides the potentially significant impact of k. For instance, if the algorithm requires storing intermediate results related to each of the k selected subsets, the space complexity could be significantly higher than what is presented. This lack of clarity makes it difficult to compare this algorithm with existing approaches, especially in scenarios where k is large or comparable to d.

### Questions
What is the actual dependency on k?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the maximum coverage problem in a streaming setting:  Given $d$ sets over an universe $[n]$ and an integer $k$. Find $k$ sets whose union is maximized.  The input (represented as $n \times d$ matrix) arrives as a stream. Earlier works studied this problem in the insertion-only streaming model. This work studies the problem in the turnstile model, where deletions are allowed. The main contribution is the design of a sketch-based algorithm that use $\tilde {O} (d/\epsilon^3)$ space.

### Strengths
1. This is the first algorithm for the maximum coverage problem in the turnstile model.

### Weaknesses
1. The writing could be improved to enhance the readability of the paper. I am not able to completely understand the proposed algorithm and verify the claims. Please see the Questions for details.
2.  There is a large body of work on streaming submodular maximization. A discussion on the relationships of those works to the current work is missing.  For example,
      [1]. https://proceedings.neurips.cc/paper_files/paper/2020/file/6fbd841e2e4b2938351a4f9b68f12e6b-Paper.pdf
      [2]. https://dl.acm.org/doi/10.1145/3519935.3519951
      [3]. https://proceedings.neurips.cc/paper_files/paper/2020/file/9715d04413f296eaf3c30c47cec3daa6-Paper.pdf
3. Experimental results are not evaluated on turnstile streams.

### Questions
1. Is the model is strict-turnstle model?
2. Line 200: L_1 sketches are trivial. Do you mean L_0 Skteches?
3. The description of the algorithm is confusing and not precise.  For example
    a. Line 9. All rows are concatenated to obtain v. However, each entry in the matrix is 0-1. So $v$ is a binary vector? I assume $v$ contains row numbers/elements of the universe? (For example, if elements $i$ is in sets 3, 4 8. Then the vector $v$ contains the number $i$, at 3 positions.
    b. When you are keeping an L_0 sample of $v$, what do they contain?  It seems to me that they contain a sample of rows  (excluding all zero rows, and hashed into the same bucket) from $A'_m$?  Is this correct?
    c. Line 23: I do not understand what it means to "if $r$ has less then ..... edges among $L_0$ samplers". Clarifying the above question will help understand this line.

4. Claim 3.1: Consider the instance where $m = 1$. $A'_1$ contains approximately half the rows. Shouldn't this need $n/2$ memory? What am I Missing?
5. Line 276-277: $k \log d/\epsilon^2$ is a fixed number. How can this be OPT?
6. Claim 3.2: McGregor & Vu's proof relies on (set) insertion only model? Is it easy to see that it translates into a turnstile model?
7. Line 294: What are $c_1, c_2, \cdots$?  They are not defined earlier
8.  As defined a linear sketch is a matrix drawn from a family of matrices. The algorithm is implicitly defining a family of matrices. Can you define these matrices more explicitly? For the sketch to be linear, the $L_0$ sampler needs to be linear. This should be clarified.

I will revise my score after the discussion period.

### Soundness
2

### Presentation
2

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
The paper addresses the problem of constructing a linear sketch for the maximum $k$ coverage problem. Given a set of $n$ items and $d$ subsets, the objective of the maximum $k$ coverage problem is to select $k$ subsets that maximize the number of items covered. The problem can be represented using a matrix $A \in \{0, 1\}^{n \times d}$, and the goal of the linear sketch is to find a matrix $S$ such that $SA$ is significantly smaller than $A$ while still enabling an approximate solution to the original $k$ coverage problem using $SA$. 
Since the sketch is linear, it naturally extends to the turnstile model, where the entries of $A$ can be updated over time. 

The paper also demonstrates the application of this sketching technique to the problem of fingerprinting for risk management, with empirical studies indicating substantial speed improvements over previous methods.

### Strengths
1. The paper constructs a linear sketch that supports input updates for the maximum $k$ coverage problem.
2. Experimental evaluations demonstrate a significant speedup compared to prior work.
3. Overall, I find the paper to be well-written.

### Weaknesses
1. The paper claims that Algorithm 1 constructs a linear sketch. However, it is not immediately clear whether the $L_0$ sampler and the $L_1$ sketch used within Algorithm 1 are themselves linear sketches. The linearity of these components is crucial to the overall claim of Algorithm 1 being a linear sketch. A more detailed explanation is needed to clarify whether these components are indeed linear. If they are, providing a brief explanation or referencing the specific mechanisms that ensure their linearity would significantly improve the paper's clarity. For instance, how do these components handle updates in a way that maintains the properties of a linear sketch?  Without this, the reader may struggle to fully grasp the linear nature of the entire algorithm.

2. Line 209 states, "$|x_i| \ge \epsilon^2 || x ||_p$". It is unclear what the value of $p$ is in this context. Is it a specific value, or does this inequality hold for arbitrary values of $p$? Clarifying the scope of $p$ is essential for understanding the conditions under which this statement is valid.

3. In line 222, the $\tilde{O}$ notation omits $\epsilon$, while in line 224, $\epsilon$ is included. This inconsistency in notation can lead to confusion. It is important to maintain consistency in the use of the $\tilde{O}$ notation throughout the paper.

4. Line 226 states "$\alpha - \epsilon$". This appears to be a typo and should be corrected to "$1 - 1 / e - \epsilon$" to accurately reflect the approximation factor.

### Questions
1.	Line 209, $|x_i| \ge \epsilon^2 || x ||_p$. What is the value of $p$, or does this apply to arbitrary value of $p$?
2.	Line 222, $\epsilon$ is missing in the $\tilde{O}$ notation, whereas in line 224, the $\epsilon$ is not omitted in the $\tilde{O}$ notation.
3.	Line 226, $\alpha - \epsilon$ -- > $1 - 1 / e - \epsilon$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper provides streaming algorithms for maximum coverage and fingerprinting for risk measurement problems. The streaming algorithms are in the turnstile model (input elements can inserted or deleted). Previous results on streaming algorithms were known only for the insertion-only model. Let us discuss the main results for both problems:

Max-coverage:
In the maximum coverage problem, we are given subsets S1, ..., Sd of a universal set U (of size n) and an integer k, and the task is to find the k subsets that together cover the largest size subset of U. The problem is NP-hard. There is a poly-time (1-1/e)-approximation algorithm that is known to be tight. The input for this problem can be seen as a 0/1 matrix A of size nxd, where A(i, j)=1 iff i is in the subset S_j. In a previous work, McGregor and Vu (2018) gave a (1-1/e-\eps)-approximation streaming algorithm in the insertion-only set-arrival model using O(d/\eps^2) space. In the set-arrival model, the entire column of the matrix A is seen in one step. Bateni et al. (2017) gave a (1-1/e-\eps)-approximation algorithm in the insertion-only edge-arrival model using O(d/\eps^2) space. In the edge-arrival insertion-only model, a single matrix entry gets updated from 0 to 1. This paper explores the edge-arrival turnstile model, where in every step, one matrix entry may get updated from 0 to 1 or from 1 to 0.

Fingerprinting for Risk Management:
In targeted fingerprinting, the input is an n×d matrix A with n users and d features. The goal is to identify at most k features {f1,f2,...,fk} such that the number of users who share identical values at positions {f1,f2,...,fk} is minimized.

### Strengths
Extending the known results for the turnstile model is interesting.

### Weaknesses
There is significant scope for improving the write-up. There is a lack of clarity in many of the statements that leaves the reader confused:
- What is F_k in the abstract?
- The introduction assumes the knowledge about the definition of a sketch. Writing 1-2 sentences defining a sketch before using it in the discussion would be good.
- The abstract states the space usage to be O(d/\eps^2), but the main theorem (Theorem 1) gives the space-bound as O(d/\eps^3). This discrepancy needs to be addressed.
- Remark 1 is unclear and confusing. It starts talking about 'sampling rates', l_0-sampler, etc. without discussing any random process or algorithm. I had no option but to move on without understanding Remark 1. Specifically, the connection between sampling rates and the l_0-sampler is not explained, nor is it clear how these concepts relate to the overall algorithm.
- Lines (141-143): It is unclear what the estimation problem is. Are x_i values given in the streaming setting, or is it (i, \pm 1)? Unless this is made clear, I am not sure how to interpret Theorem 3. The description lacks detail on how the updates to x_i are received and processed in the streaming model, and how this relates to the stated theorem.
- Understanding the sketch algorithm (Algorithm-1) is extremely challenging given that the format of the sketch is not defined. Is H_{\leq d} a matrix or a subset of (element, subset) pairs? How is this sketch updated in the stream on an insertion and deletion? This does not come out clearly from the pseudocode. In line 14 of Algorithm 1, it is said that "sketches and samplers handle updates." Which sketches are these? The algorithm description needs to specify the exact data structure used for the sketch, how it is initialized, and how it is modified upon each update. The pseudocode lacks sufficient detail to understand the update process.

### Questions
Some questions are mentioned in the other parts of the review.

### Soundness
2

### Presentation
1

### Contribution
3
