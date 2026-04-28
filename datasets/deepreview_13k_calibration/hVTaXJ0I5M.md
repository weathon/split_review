# Privately Counting Partially Ordered Data

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
We consider differentially private counting when each data point consists of $d$ bits satisfying a partial order. Our main technical contribution is a problem-specific $K$-norm mechanism that runs in time $O(d^2)$. Experiments show that, depending on the partial order in question, our solution dominates existing pure differentially private mechanisms, and can reduce their error by an order of magnitude or more.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work studies differentially private summation of items that satisfy a partial order. The authors show that the problem can be solved in time $d^2$ where $d$ is the number of bits and outperforms existing private algorithms.

### Strengths
1. Summing over items with partial orders is a fundamental problem that has not been fully studied under differential privacy. 
2. The proposed algorithm is very time-efficient, only quadratic in the number of bits. The speed-up is significant over some simple sampling algorithms
3. The estimation error is much better than standard privacy algorithms based on $\ell_{\infty}$ norm.

### Weaknesses
1. The algorithm is only for pure differential privacy. Approximate DP is sometimes more practical in many applications.
2. It would be helpful to the readers to provide a high-level overview of the algorithm and why it improves over standard algorithms through a simple example.

### Questions
How can the algorithm be adapted to approximate DP and achieve better results than pure DP?

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
2

### Summary
The paper presents a sampling algorithm that samples from a K-norm mechanism on an induced ball for counting partially ordered data. The algorithm presented in the paper runs in $O(d^2)$ time instead of $O(d^{2+\omega})$ time.

### Strengths
The paper proposes a sampling mechanism for a special instantiation of K-norm mechanism that improves the state of the art sampling algorithm by a factor of $O(d^\omega)$.

### Weaknesses
I found the paper rather hard to read and also difficult to figure out what are the contributions of the authors and what follows more or less from Chappell et al. (2017). I suggest that the authors make it explicitly clear by giving a high level overview of their proof stating clearly what steps requires their proof and what was already known in the literature. To me, it feels like the main contribution is the proof of Lemma 3.14, but I can be wrong and would love to stand corrected. 

If the authors can give me a better understanding of which aspect of their paper is new, I would be more than happy to increase the score.

### Questions
Please give us a good overview of which is your contribution and what are the challenges faced when using the previous algorithms to perform the sampling.

Also, what is the best known sampling algorithm that runs in time $O(d^{2+\omega})$? What happens if that sampling algorithm is instantiated with the set up that the authors propose? What difference from that sampling algorithm do the authors take?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Differentially private algorithms for counting queries have a long history and mechanisms that add carefully chosen noise when queries have some structure can improve accuracy. Some of these algorithms are often used in practice, e.g. by the US Census Bureau. For the case of pure DP, the K-norm mechanism of Hardt and Talwar improves on the Laplace mechanism that does not exploit the structure of the queries. The algorithm however requires sampling from the “sensitivity polytope” defined by the queries.

The current paper studies this sampling problem for the case when the queries have a “partially ordered” structure. E.g. surveys often have a sequence of questions where a No answer to a question implies a no answer to the next question. This imposes a constraint that the answer to $Q_{i+1}$ can be 1 only if $Q_{i}$ has answer 1. The authors study the more general case of partial orders.

The main contribution of this work is to show an efficient algorithm to sample from the sensitivity polytope defined by a partial order. For the case of d queries, the proposed algorithm runs in time $O(d^2)$. The paper follows a general schema in recent work by Joseph and Yu, where the sensitivity polytope is expressed as a union of simplexes. A simplex is easy to sample from, and thus the problem reduces to sampling a random simplex proportional to its volume. While Joseph and Yu used this approach for some set of problems, their work does not cover this natural set of constraints, and this is addressed in the current work.

The main contribution in my mind is to bring in the technical tools from recent works in the geometry of the poset polytopes, and apply them to this natural problem. The authors also do experiments comparing their algorithm to using K-norm for an \ell_p norm, and show that for random posets, using the K-norm improves noticeably the error in the estimate for random posets, as well as for an National Health Interview Survey.

### Strengths
- Brings in tools from another research area to improve algorithms/bounds for a natural and practical problem

### Weaknesses
 - The paper is difficult to read for someone who is not an expert in partial orders.

- The recursive K-norm mechanism can improve the error bounds. It would be valuable to see the error comparison. Relatedly, Hardt and Talwar seem to have lower bounds and one can also minimize over matrix mechanisms. It would be valuable to compute the lower bounds and see how far off they are from the upper bounds here.
- For larger d, I would expect that (eps, delta)-DP algorithms with a small delta would become competitive quickly, and have the advantage of being easier to sample from. A comparison even with the simplest Gaussian mechanism, for a small delta (say 10^-6 - 10^-9) would make the paper better.
- In the case of surveys, the poset structure would be further restricted to a “product structure”, where Q2-Q5 may depend on Q1, and Q7-Q9 may depend on Q6, but Q1-Q5 and Q6-Q10 are independent of each other. In this case, you should be able to reduce the run time from d^2 to dk, where k is the size of the largest dependency. This seems like a natural extension of the current work and should be written down.

### Questions
- The recursive K-norm mechanism can improve the error bounds. It would be valuable to see the error comparison. Relatedly, Hardt and Talwar seem to have lower bounds and one can also minimize over matrix mechanisms. It would be valuable to compute the lower bounds and see how far off they are from the upper bounds here.
- For larger d, I would expect that (eps, delta)-DP algorithms with a small delta would become competitive quickly, and have the advantage of being easier to sample from. A comparison even with the simplest Gaussian mechanism, for a small delta (say 10^-6 - 10^-9) would make the paper better.
- In the case of surveys, the poset structure would be further restricted to a “product structure”, where Q2-Q5 may depend on Q1, and Q7-Q9 may depend on Q6, but Q1-Q5 and Q6-Q10 are independent of each other. In this case, you should be able to reduce the run time from d^2 to dk, where k is the size of the largest dependency. This seems like a natural extension of the current work and should be written down.

### Soundness
3

### Presentation
2

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
The paper primarily focuses on differentially private counting when data points satisfying a partial order. Previous best approaches takes time $\tilde{O}(d^{2+\omega})$ where $\omega\geq 2$ is the matrix multiplication exponent. In contrast, this work provides a fast sampler for the induced norm ball that runs in $O(d^2)$. To achieve this, this work starts with connecting the poset ball to double order polytope, then reduces the problem to uniformly sampling a non-interfering pair of chains with the results from Chappell and finally to sampling an extended bipartition. Experiments are conducted to show that the final sampler reduces error over existing DP mechanisms. To complement the sampler, this work also shows a negative result for rejection sampling.

### Strengths
S1: This paper addresses the problem by providing a sampler with more than cubic speedup over the previous algorithms. 

S2: The proof path leading to the final sampler is clear and well-organized.

S2: This paper also investigates the rejection sampling and provides a negative result. 

S3: The paper conducts experiments on both synthetic and real-world partial orders to demonstrate error reductions of their sampler.

### Weaknesses
W1: The comparison with previous research, particularly with the work of Joseph & Yu, does not seem sufficiently thorough. (summarized in the questions)

It remains unclear how the specific data characteristics of the partial order setting necessitate a fundamentally different sampling approach compared to the work of Joseph & Yu. While the authors mention a different norm ball, the paper lacks a detailed explanation of why existing techniques cannot be adapted or modified. The core innovation of the proposed sampler is not clearly articulated, making it difficult to assess its true contribution beyond a problem-specific modification of existing ideas. The paper should provide a more rigorous analysis of the limitations of existing sampling methods when applied to partial order data, and precisely highlight how the proposed method overcomes these limitations.

W3: The results of the experiments appear to be incomplete (also summarized in questions.)

The experimental section focuses solely on error reduction, neglecting to validate the claimed speedup of the proposed algorithm. Given that the primary contribution is a fast sampler, the absence of runtime comparisons with previous approaches is a significant oversight. The experiments should include a detailed analysis of the computational cost of the proposed sampler, demonstrating its practical efficiency compared to existing methods. Without this, the practical significance of the proposed sampler remains unclear.

### Questions
Q1: Although the authors have introduced the differences between their work and that of Joseph & Yu in the related work section, they do not seem to have adequately demonstrated the innovative aspects of their work. Furthermore, the structure of the paper appears similar, as Joseph & Yu also considered rejection sampling. It seems that this paper merely modifies the sampling technique based on changes in the characteristics of the input data, without showcasing its unique core technology.

It would be beneficial if the authors can provide a more detailed comparison, such as explaining how the data considered in this paper differs from that considered by Joseph & Yu; why their sampling technique is not well-suited to our current data; and how the sampling method proposed in this paper leverages the new data characteristics and what innovations it introduces.


Q2: The experiments in the paper only investigate the error reduction of the sampler. Since the main contribution of the paper is a sampler faster then previous algorithms, it would be beneficial for the authors to conduct experiments that demonstrate speedup of their algorithm and compare it with former approaches.

### Soundness
2

### Presentation
3

### Contribution
2
