# Performance Gaps in Multi-view Clustering under the Nested Matrix-Tensor Model

- Decision: Accept
- Scores: 6, 8, 6, 5, 6

## Abstract
We study the estimation of a planted signal hidden in a recently introduced nested matrix-tensor model, which is an extension of the classical spiked rank-one tensor model, motivated by multi-view clustering. Prior work has theoretically examined the performance of a tensor-based approach, which relies on finding a best rank-one approximation, a problem known to be computationally hard. A tractable alternative approach consists in computing instead the best rank-one (matrix) approximation of an unfolding of the observed tensor data, but its performance was hitherto unknown. We quantify here the performance gap between these two approaches, in particular by deriving the precise algorithmic threshold of the unfolding approach and demonstrating that it exhibits a BBP-type transition behavior \citep{baik_phase_2005}. This work is therefore in line with recent contributions which deepen our understanding of why tensor-based methods surpass matrix-based methods in handling structured tensor data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper quantifies the performance gap between the nested matrix-tensor model and its unfolding variant in multi-view clustering.   Specifically, the authors theoretically analyze the alignment level between the leading singular vector learned by the matrix-tensor model and the true signals. Their theoretical results give some interesting insights into tensor-based multi-view clustering. Finally, these results are verified by numerical experiments.

### Strengths
1. This paper gives a vital result, i.e., under the nested matrix-tensor model, the analysis of the unfolding method shows the theoretical superiority of the original tensor-based method in terms of accuracy.
2. The proposed theoretical results are interesting and can advance the understanding of tensor data processing in multi-view clustering.

### Weaknesses
1. The nested matrix-tensor model can only handle the multi-view clustering task in which the dimensionality of each view is the same. In real-world multi-view datasets, the dimensionality of each view is usually different. I wonder how this issue can be addressed in the nested matrix-tensor model.
2. In the summaries of the main contributions of Page 2, the authors can point out the corresponding theorems at the end of each contribution.
3. There is an error in the definition of $T^{(1)}$. Its element should be $T^{(1)}_{i,n_3 (j-1) +k }$.
4. What is the definition of "SNR"?
5. The significance of all variables in Eq. (2) should be specified for readability.
6. What is the definition of the inner product of two tensors?
7. All theorems lack necessary remarks. It critically hurts the reader's understanding of the proposed results. For example, in Theorem 2, $\zeta$ reflects the alignment level between $\hat{y}$ and $y$. However, $\zeta$ is equal to a complex formula. I can't understand how it can be close to $1$.
8. The detailed deduction of the last equation on Page 17 should be presented. It seems not apparent.
9. Cauchy's integral formula on Page 20 is not in a standard form. The authors should give the relevant references.
10. Some important multi-view clustering literature [1], [2] should be added.
[1] Efficient and Effective Incomplete Multi-view Clustering.TPAMI, 2021.
[2] SimpleMKKM: Simple Multiple Kernel K-means. TPAMI, 2022.

### Questions
See the previous box.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the *nested matrix tensor model* which is the simplest statistical model for the multi-view clustering problem. The multi-view clustering problem assumes that several *views* of a set of clustered points are available. Each view being a function of the input points. Here we consider that a view is defined as a rescaled version of the input signal, up to additive independent noise. 
The paper studies a solution of the simplified "nested matrix tensor" problem, relying on a tensor unfolding schema. Authors provide theoretical results for the proposed solution. The theoretical results borrow tools from random matrix and random tensor theory. REsults allow to identify regimes where the approach works or fails.

### Strengths
The papers focus is on an interesting theoretical model for a challenging and relevant application. Authors do a good job motivating the work and stating it both in comparison with theoretical related work and applied related work. The contribution of the paper is insightful and results are non-trivial. Authors have done a good job presenting the main results and providing numerical simulations and graphics that make the findings more accessible.

### Weaknesses
Gaps between info-theoretical and computational results are non-trivial in tensor problems and I may have missed it, but I could not see it discussed in this paper (see question).

When authors mention "impossible" or "possible" recovery, it is unclear to me whether they mean "information theoretically (im)possible" or "computationally (im)possible". Even though in the matrix case these two match, in random tensor problems there are different asymptotics for the two. It seems to me that authors are not dealing with info theoretical phase transitions but with numerical schemas: "assume we do unfolding and apply the algorithm proposed, we find a solution in this regime". Is this correct?

In a regime where SNR is high, authors mention that one can get good results with a simple tensor power iteration (no unfolding). What if we have a good enough guess for the initialization vector of the tensor power iteration? Are these two cases of any practical interest?

While authors mention that coefficients c_i are positive and "This models the fact that, in practice, we deal with large tensors whose dimensions have comparable sizes", I wonder if it could help the paper to also highlight the (easier) cases where n_3 --> infty while others are constant etc. and provide intuitions on what each of these easier cases mean (many views of the problem makes it easy to identify signal). These simple cases may appear trivial from the viewpoint of the developed theory here, but some may be insightful / useful in practice to know about.

From the plot it appears that the main bottleneck is the matrix SNR rho_M. Do we think that in practice (for the multiview clustering problem) it is relevant to consider the tensor formalism to get the bit of signal left in the tensor and get it back through unfolding?

### Questions
When authors mention "impossible" or "possible" recovery, it is unclear to me whether they mean "information theoretically (im)possible" or "computationally (im)possible". Even though in the matrix case these two match, in random tensor problems there are different asymptotics for the two. It seems to me that authors are not dealing with info theoretical phase transitions but with numerical schemas: "assume we do unfolding and apply the algorithm proposed, we find a solution in this regime". Is this correct? 

In a regime where SNR is high, authors mention that one can get good results with a simple tensor power iteration (no unfolding). What if we have a good enough guess for the initialization vector of the tensor power iteration? Are these two cases of any practical interest? 


While authors mention that coefficients c_i are positive and "This models the fact that, in practice, we deal with large tensors whose dimensions have comparable sizes", I wonder if it could help the paper to also highlight the (easier) cases where n_3 --> infty while others are constant etc. and provide intuitions on what each of these easier cases mean (many views of the problem makes it easy to identify signal). These simple cases may appear trivial from the viewpoint of the developed theory here, but some may be insightful / useful in practice to know about. 

From the plot it appears that the main bottleneck is the matrix SNR rho_M. Do we think that in practice (for the multiview clustering problem) it is relevant to consider the tensor formalism to get the bit of signal left in the tensor and get it back through unfolding?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of estimating a planted signal that is hidden in a nested matrix-tensor model, which generalizes the classical spiked rank-one tensor model. The paper compares the performance of two approaches: tensor-based and matrix-based. The tensor-based approach exploits the tensor structure of the data, while the matrix-based approach uses the unfolding of the tensor. The paper derives the exact algorithmic threshold of the matrix-based approach, and shows that it undergoes a BBP-type transition behavior. The paper also compares and quantifies the performance gap between the two approaches.

### Strengths
1. The paper compares the performance of tensor-based and matrix-based approaches, providing insights into the advantages of tensor-based methods for structured tensor data.

2. This paper provides a rigorous theoretical analysis of the proposed framework.

3. The paper quantifies the performance gap between these two approaches and derives the precise algorithmic threshold of the matrix-based approach.

### Weaknesses
1. The paper does not provide a detailed comparison with other state-of-the-art methods for multi-view clustering. Specifically, it lacks a discussion of how the proposed tensor-based and matrix-based approaches compare to existing methods in terms of computational complexity, convergence rates, and robustness to noise. A more thorough comparison would involve analyzing the specific algorithmic steps of competing methods and contrasting them with the proposed framework.

2. The paper does not include experimental results on real-world datasets to validate its theoretical findings. While the theoretical analysis is rigorous, it is crucial to demonstrate the practical relevance of the results by applying the proposed methods to real-world multi-view datasets. This would involve selecting appropriate datasets, defining evaluation metrics, and comparing the performance of the tensor-based and matrix-based approaches.

3. It is best to provide more detailed experiments to compare the tensor-based method and matrix-based method. The current experiments seem limited in scope, and it would be beneficial to explore a wider range of parameter settings and data characteristics. For instance, varying the signal-to-noise ratio, the number of views, and the dimensionality of the data would provide a more comprehensive understanding of the performance gap between the two approaches.

4. It is better to provide a citation for “BBP-type”.

### Questions
1. Are the theoretical results of this paper also applicable to tensors with orders greater than 3?

2. How to choose the parameters $(p, n, m)$ in Figure 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on theoretical analysis for Multiview clustering. Specifically, the authors quantify the performance gap between the tensor-based approach and the unfolding approaches.

### Strengths
1.	The motivation of this paper is clear.
2.	Providing theoretical analysis for tensor-based Multiview clustering is important.
3.	The proofs seem strict.

### Weaknesses
1. There are few tensor-based Multiview clustering methods mentioned, thus, it is difficult to understand which kinds of tensor-based methods are suitable for these theoretical results. Specifically, the paper does not delineate the specific tensor decomposition methods that the theoretical analysis applies to. For example, are CANDECOMP/PARAFAC (CP) decomposition, Tucker decomposition, or other tensor factorization methods covered by the analysis? The lack of specificity makes it difficult to assess the practical relevance of the theoretical findings.

2. The experimental results are not sufficient. For example, in practice, there are many tensor-based and matrix or vector-based Multiview clustering methods, so what about the performance gaps between them and is the theoretical results applicable for them? The experiments should include a more comprehensive set of methods for comparison, including various tensor-based methods (e.g., CP-based, Tucker-based) and matrix-based methods (e.g., spectral clustering on concatenated or averaged views). The current experiments only demonstrate the theoretical results in a limited setting, failing to show the broader applicability of the analysis.

3. The potential inspiration for researchers of the work is not clear. The paper does not clearly articulate how the theoretical results can be used to guide the development of new tensor-based multiview clustering methods. It is unclear how the theoretical gap can be leveraged to design algorithms that are guaranteed to perform better than matrix-based approaches in practical scenarios. The paper needs to discuss the implications of the theoretical findings for future research directions.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The authors quantify the gap between the best rank-one approximation of a tensor and that of its unfolding matrix.

### Strengths
The theoretical analysis of the paper is solid and the results is interesting.

### Weaknesses
The assumption that both of Z and W follow the Gaussian distribution with zero mean and unit variance, is too strong. As $X=(\boldsymbol{\mu}\boldsymbol{h}^T)\otimes\boldsymbol{\mu} + \boldsymbol{Z}\otimes\boldsymbol{\mu}+\boldsymbol{W}$, thus the variance of Z and W affect the performance of the rank-one approximation in a different manner. But the authors do not discuss the part and simply assume both Z and W follow the normal distribution.

### Questions
1, It is important to introduce and define all symbols used in the paper when they are first mentioned. So it is better to define symbol $\otimes$ in Nested Matrix-Tensor Model.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
