# Matrix Product Sketching via Coordinated Sampling

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
We revisit the well-studied problem of approximating a matrix product, $\bv{A}^T\bv{B}$, based on small space sketches $\mathcal{S}(\bv{A})$ and  $\mathcal{S}(\bv{B})$ of $\bv{A} \in \R^{n \times d}$ and $\bv{B}\in \R^{n \times m}$. We are interested in the setting where the sketches must be computed independently of each other, except for the use of a shared random seed. We prove that, when $\bv{A}$ and $\bv{B}$ are sparse, methods based on \emph{coordinated random sampling} can outperform classical linear sketching approaches, like Johnson-Lindenstrauss Projection or CountSketch. For example, to obtain Frobenius norm error $\epsilon\|\bv{A}\|_F\|\bv{B}\|_F$, coordinated sampling requires sketches of size $O(s/\epsilon^2)$ when $\bv{A}$ and $\bv{B}$ have at most $s \leq d,m$ non-zeros per row. In contrast, linear sketching leads to sketches of size $O(d/\epsilon^2)$ and $O(m/\epsilon^2)$ for $\bv{A}$ and $\bv{B}$. We empirically evaluate our approach on two applications: 1) distributed linear regression in databases, a problem motivated by tasks like dataset discovery and augmentation, and 2) approximating attention matrices in transformer-based language models. In both cases, our sampling algorithms yield an order of magnitude improvement over linear sketching.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of approximating the matrix product $A^T B$ using sketching-based techniques in a new setting with two key requirements: (1) preserving the potential sparsity of $A$ and $B$ and (2) ensuring that sketches of $A$ and $B$ can be computed independently—motivated by scenarios like distributed computing and multi-vector retrieval. Traditional linear sketches, often relying on dense random matrices, fail to preserve sparsity. However, sparsity preservation (requirement 1) can be achieved using importance sampling techniques, where rows of $A$ and $B$ are subsampled and reweighted. Unfortunately, existing importance sampling methods require knowledge of both $A$ and $B$ simultaneously, which contradicts requirement (2).

To address this, the paper proposes a new approach called coordinated random sampling, which only requires shared randomness to independently compute sketches of $A$ and $B$ by row subsampling, without further interaction between the matrices. This method is based on priority sampling: the same rows of $A$ and $B$ are selected only when they both contribute significantly to $A^TB$, even though rows are sampled independently within each matrix.

The paper shows that subsampling $O(1/\epsilon^2 \delta)$ rows of $A$ and $B$ suffices to achieve $\epsilon$ error in Frobenius norm with probability $1-\delta$, matching the best known result from dense linear sketches. This paper demonstrates one application of their proposed algorithm in sketched linear regression. Lastly, the paper empirically compares the effectiveness of coordinated random subsampling against linear sketches in terms of approximation accuracy with varying degrees of sparsity in the input matrices, and in two applications: 1) sketched linear regression, 2) approximation to the attention layer in autoregressive language models.

### Strengths
1. I found the presentation of this paper to be very clear and engaging. The problem setting, requirements, and notation are all well-defined, and the core idea is explained thoroughly, making it easy for readers to follow. The proof is presented in a clean and structured manner, enhancing readability.

2. The paper provides strong motivation for studying the problem of computing independent sketches and discusses several potential applications, demonstrating their proposed algorithm in a one important application: sketched linear regression. 

3. The setting of preserving sparsity of the inputs and computing independent sketches seems to be novel.

### Weaknesses
1. One concern I have regarding the experiments is that while vector quantization—a nonlinear compression technique—has been widely studied and applied in practice for approximating the computation of the key matrix in the attention layer, it remains unclear whether using linear compression techniques, such as approximate matrix products, to approximate $QK^T$ or just the key matrix $K$ could degrade model performance significantly in downstream applications. I suggest that the authors cite works that empirically investigate this issue (if there is any) or include explicit discussion and caveats when discussing the use of approximate matrix products for approximating the attention layer. The application discussed in Section 1.4 on multi-vector information retrieval seems more reasonable and well-suited for demonstrating the applicability of the proposed algorithm in experiments.

2. Additionally, some aspects of the experiment section need clarification. For instance, does the x-axis labeled “Sketch Size” in Figures 1-5 represent the percentage of rows subsampled from the input matrices? What does “Layer x” in Figures 4 and 5 refer to? Furthermore, what architecture is used for the autoregressive language model in the experiment? Providing these details would enhance the clarity of the experimental setup.

3. It would also be helpful to include empirical comparisons of memory usage between linear sketches (e.g., JL sketches) and the proposed method.

4. Minor issues: Bad citation in line 109. “is include as” => “is included as” in line 324.

5. To improve clarity for readers, it would be helpful to include a description of $\tau_A$ in the output of Algorithm 1, explaining that it represents the threshold used to determine whether a row in the input matrix $A$ should be retained.

### Questions
Why is Theorem 3 presented as a constant probability guarantee rather than a high-probability guarantee? What specific challenges arise in deriving a high-probability guarantee in this context? Additionally, what makes it difficult to achieve a multiplicative $(1+\epsilon)$ guarantee instead of the additive error guarantee stated in the footnote on page 4?

In the context of sketched linear regression problems, the guarantee provided by Theorem 3 is relatively weak. A discussion on the challenges of obtaining a stronger guarantee would be valuable and could provide useful insights for future work.

### Soundness
4

### Presentation
4

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
Overview: The paper presents a method for sketching two matrices A and B, each held by a different party, such that the product of the matrices can be approximated up to an additive term of eps ||A||||B|| from the sketches alone. Each sketch consists of k rows/columns of the sketched matrix, for k=O(1/eps^2). For sparse matrices, such sketches can be more compact than the state-of-the-art linear sketches obtained via random projections. 

Techniques:  the paper presents two sketching methods: Threshold Sampling and Priority Sampling. Both methods are variants of coordinated sampling, where a shared random seed is used to sample columns/rows in a correlated manner. Threshold Sampling is simpler to analyze, while Priority Sampling offers better control over the sketch size.  In addition, the paper presents two applications of the proposed sketches, to multi-vector retrieval and regression-based dataset search.

The authors complement the theoretical development with empirical evaluation of their algorithms. In particular, both sketching methods are shown to improve (for sparse matrices) over the standard random projection approach, as predicted theoretically.

### Strengths
S1: Interesting problem.
S2: Elegant solutions.
S3: Solid experiments.

### Weaknesses
W1: The result and the approach are not very surprising, given the prior work of Bessa et al and Daliri et al
W2: The analysis of one of the algorithms (Threshold Sampling) seems fairly straightforward.

### Questions
Q: In the paper you write "In doing so, we encounter several technical challenges, including the fact that Priority Sampling—being a without-replacement sampling procedure—generates non-i.i.d. row samples from A and B.". Can you list some of the other technical challenges as well ?

### Soundness
3

### Presentation
4

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
The paper revisits the approximation matrix product problem. That is, given two matrix $A, B$, we want to compute a matrix $W$ in a fast time where $\|W - A^T B\|_F^2 \le \|A\|_F^2 \|B\|_F^2$. The paper studies the case where sketches must be computed independently of each other, except for the use of a shared random seed. The paper provides a new method that is based on coordinated random sampling and has sketch size $O(s/\epsilon^2)$ assuming $A$ and $B$ have $s$ non-zero entries per row. Based on this, the paper next proposes a new algorithm for the $\ell_2$ regression problem. Finally, the paper gives an empirical evaluation that demonstrates the advantage of the proposed algorithm.

### Strengths
- The theoretical analysis of this paper is solid. The paper gives a new sketching algorithm with size $O(s^2 /\epsilon^2)$. This bound will be better for sparse matrix compared to the previous methods, which is interesting to me.

- The paper gives a detailed experiment that demonstrates the advantage of the proposed algorithms.

- The presentation of the paper is good. The paper has a nice introduction section.

### Weaknesses
 - I still do not understand the motivation of the new model the paper discusses well (see the questions below). Maybe the authors can give more explanation about this？

- It will be better if the experiments can also give a comparison to the previous sampling-based method.



### Questions
Approximation Matrix Product: I am not sure I fully understand the motivation of the model considered, as mentioned by the authors, sampling to either $\|A_i\|_2$ and $\|B_i\|_2 $ can also get a good bound. The communication about the probability can be somewhat expensive but we can also sample from $A$ and then tell the other part the indices of the sampled rows, in which case we will have much better communication cost? 

Regression: there are some recent works that study the active regression problem where the goal is to access as fewer number of the entries of $b$ as possible, see, e.g, [1, 2]. In particular, it has been shown that sample $O(d/\epsilon)$ rows of $A$(where the sample probability is only computed from the matrix) can give a $(1 + \epsilon)$ relative error of the solutions. Can the authors give a comparison of both models?

Minor:

1.Line 238: that is $k \cdot |B_i|^2 / |B|_F^2$ ?

[1] Cameron Musco et al. Active Linear Regression for $\ell_p$ Norms and Beyond.

[2] Xue Chen et al. Active regression via linear-sample sparsification active regression via linear-sample sparsification.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Given two matrices $\mathbf{A} \in \mathbb{R}^{n \times d}$ and $\mathbf{B} \in \mathbb{R}^{n \times m}$, the problem of approximately computing the product $\mathbf{A}^\top \mathbf{B}$ using sketching techniques has been extensively studied, with a wide range of applications in machine learning and numerical linear algebra. The existing work includes two types of sketching methods: (1) Generating a random matrix $\boldsymbol{\Pi} \in \mathbb{R}^{k \times n}$ such that $(\boldsymbol \Pi \mathbf{A})^\top (\boldsymbol \Pi \mathbf{B}) \approx \mathbf{A}^\top \mathbf{B}$; (2) Sampling and reweighting the rows of $\mathbf{A}$ and $\mathbf{B}$ to obtain $\widetilde{\mathbf{A}}$ and $\widetilde{\mathbf{B}}$ such that $\widetilde{\mathbf{A}}^\top \widetilde{\mathbf{B}} \approx \mathbf{A}^\top \mathbf{B}$. This paper studies matrix multiplication in the $\textit{sketching setting}$, which requires the sketches $\mathcal{S}(\mathbf{A})$ and $\mathcal{S}(\mathbf{B})$ of $\mathbf{A}$ and $\mathbf{B}$ are computed independently. Nevertheless, the classical sampling method does not work as the rows are sampled with non-uniform probabilities. This paper applies the sampling method effectively in the sketching setting by virtue of the $\textit{coordinated sampling method}$ (aka $\textit{priority sampling}$), which ensures that the number of commonly sampled row indices from $\mathbf{A}$ and $\mathbf{B}$ is guaranteed. Furthermore, the proposed algorithm achieves the same guarantee as the existing sampling method and is more efficient when the two input matrices are sparse. In addition, the developed method can be extended to $\ell_2$ regression. The experimental results prove the effectiveness of the proposed algorithm on synthetic and real datasets.

### Strengths
(1) This paper studies the approximate matrix multiplication in the sketching setting by the coordinated sampling technique. The proposed algorithm matches the guarantee of the existing sampling-based method and is more efficient when the input matrices are sparse.    
(2) The developed algorithm also works for $\ell_2$ regression problem and improves the existing bound when the input matrix is sparse.        
(3) This paper is well-written and easy to understand.

### Weaknesses
 (1) In essence, the coordinated sampling technique is nearly the same as the threshold sampling method and has also been applied in other sketching work [DLT'07, DFMSZ'24]. From the technique perspective, this paper's contribution is kind of limited. Specifically, while the paper highlights the coordinated sampling's ability to guarantee a fixed sketch size, it does not sufficiently differentiate itself from existing threshold sampling methods in terms of the core sampling strategy. The analysis seems to re-derive results that are conceptually similar to those already present in the literature, without offering significant novel theoretical insights or substantial practical advantages over existing approaches.

(2) The restriction in sketching setting often occurs when communications matter, like in distributed systems. Although this paper proposes an algorithm that works in the sketching setting, there are no specific applications in distributed sketching. The paper does not provide a compelling use case where the independent sketching is crucial. While the authors mention that this setting is relevant when compressing multiple matrices, they do not provide concrete examples or elaborate on the practical advantages of their method in such scenarios. The lack of a clear and detailed application makes it difficult to assess the real-world impact of the proposed algorithm.

(3) This paper claims that priority sampling is more complicated than threshold sampling whose sketch size can only be bounded in expectation. However, in Figure 1 and Figure 4, we can see that priority sampling does not outperform threshold sampling. The experimental results do not sufficiently justify the use of priority sampling. The fact that priority sampling does not show a clear advantage over threshold sampling in the experiments raises questions about the practical value of the proposed method. The paper needs to provide more compelling evidence to support the claim that priority sampling is superior or necessary in certain scenarios.

### Questions
In Algorithm 3, it requires computing the leverage score of each row of $\mathbf{A}$ (i.e., $\mathbf{A}_i (\mathbf{A}^\top \mathbf{A})^{-1} \mathbf{A}_i^\top$) and $(\mathbf{A}^\top \mathbf{A})^{-1}$.   
(1) What's their running time?  
(2) Can you compare this algorithm with the linear regression in the work of Clarkson and Woodruff [CW'13]?  
(3) For sketched regression, do we only care about the size of sketches? If so, in Section 1.4, it needs to compute $\min {\mathbf{x}} ||\mathbf{A}^i \mathbf{x} - \mathbf{b}||_2$ for each $i$. Then the running time could be more crucial.

### Soundness
3

### Presentation
3

### Contribution
2
