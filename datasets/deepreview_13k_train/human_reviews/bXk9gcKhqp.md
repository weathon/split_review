# Rethinking the Polynomial Filter of GNNs via Graph Information Activation Theory

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Recently, it has been a hot research topic to design different polynomial filters in graph neural networks (GNNs). Most of the existing GNNs only pay attention to the properties of polynomials when designing the polynomial filter, thus not only bringing additional computational costs but also ignoring embedding the graph structure information into the construction process of the basis. To address these issues, we theoretically prove that any polynomial basis with the same degree has the same expressive ability and the finely designed polynomial basis that only considers the polynomial property can at most bring linear benefit for GNNs. Then, we propose a graph information activation (GIA) theory that provides a new perspective for interpreting polynomial filters and then analyse some popular bases using the GIA theory. Based on the GIA theory and analysis, we design a simple basis by utilizing the graph structure information and further build a simple GNN (i.e., SimpleNet), which can be applied to both homogeneous and non-homogenous graphs. Experiments on real datasets demonstrate that our SimpleNet can achieve better or comparable performance with relatively less running time compared to other state-of-the-art GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the polynomial filter of GNNs and proposes a convolutional operator based on the normalized Laplacian of the graph. It gives theoretical results and empirical results for their proposed architecture.

### Strengths
This paper presents some theoretical and empirical results that will be of interest to the GNN community.
The theoretical results are very simple: Theorem 1 is a standard result in algebra about polynomials, and Theorem 3.3 can be easily checked from first principles.
The matrix $2I-L=I+D^{-1/2}AD^{-1/2}$ is very similar to the matrix used in GCN by Kipf and Welling. The only difference is that here the authors use powers of this matrix, whereas for GCN only the first power is used. Given the good performances of GCN, it is not surprising that the authors get better results here.

### Weaknesses
Empirical results are weak. The datasets Cora, Citeseer, and Pubmed have been used for a long time, and there is now a consensus that these datasets are not really helpful anymore. Indeed, the numbers in Table 3 are very close, showing that all architectures have similar performances. To get a better benchmark, you can, for example, have a look at Dwivedi, Vijay Prakash, et al. "Benchmarking graph neural networks." arXiv preprint arXiv:2003.00982 (2020).

There is a problem with equation (7), which is not invariant (under permutation of the nodes), I think it should be $\alpha_k$ instead of $\alpha_s$. The current formulation implies that the weights associated with each neighbor are node-specific, which would break the permutation invariance of the overall operation. This is because the function $f(x) = \sum_{k=0}^K\sum_{s \in N_k(t)} \alpha_s x_s$ would not satisfy $f(Px) = Pf(x)$ for a permutation matrix $P$ unless all $\alpha_s$ are equal. This is a significant issue, as permutation equivariance is a fundamental requirement for graph neural networks to operate correctly on arbitrary graphs.

### Questions
How did you get the numbers in your section 4? Did you run experiments yourself with all architectures?

There is a problem with equation (7), which is not invariant (under permutation of the nodes), I think it should be $\alpha_k$ instead of $\alpha_s$.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper delves into the exploration of polynomial-based graph convolutional networks (GCNs). The authors demonstrate that any polynomial basis of the same degree harbors identical expressive capability and leads to the same global optimal solution. Additionally, they establish that meticulously crafted polynomials can, at best, yield linear advantages for GCNs. Given the aforementioned demonstrations, the authors argue against the necessity of overly intricate design of polynomial bases solely based on polynomial properties. Following this, they introduce a novel framework termed Graph Information Activation (GIA) theory, which sheds fresh light on the interpretation of polynomial filters within GCNs. Subsequently, a simplistic basis encapsulating graph structure information is proposed, laying the foundation for the introduction of SimpleNet. The efficacy of SimpleNet is corroborated through experimental evaluations on benchmark node classification datasets, showcasing its superior performance in terms of both accuracy and computational efficiency when juxtaposed with existing GCNs.

### Strengths
1. SimpleNet exhibits both structural simplicity and robust performance.

### Weaknesses
1. The authors assert that GNNs can be conceptualized as optimizers, and can be mathematically formulated in a uniform optimization form as depicted in Equation 4. However, this claim appears to be unfounded. As elucidated in [1], only PPNP and APPNP align with the representation provided by Equation 4.
2. The so-called Graph Information Activation theory posited by the authors is essentially a reintroduction of graph coloring.
3. The test datasets comprising Cora, Citeseer, Pubmed, Computers, and Photos are too small, thus rendering the assertion that GNN FixedMono outperforms BernNet less convincing. I recommend that the authors evaluate GNN FixedMono and BernNet using the Open Graph Benchmark.
4. This paper omits an analysis of SimpleNet concerning the over-smoothing issue.

### Questions
1. Why consider adding the term $\sum^{K\_{1}}\_{i=0}\alpha\_{i}(2\mathbf{I}-\mathbf{L})^{i}$ and the term $\sum^{K\_{2}}\_{j=0}\beta\_{j}\mathbf{L}^{j}$ instead of concatenating them?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors claim that there is no essential difference between existing different graph polynomial filters. Their theoretical results show that all $K$-order polynomial graph filters have the same expressive power in terms of linearly expressing the element in polynomial space. Furthermore, the convergence rate of various graph polynomial filters is no more than a linear constant related to the condition number. Then they introduce the GIA theory to emphasize the necessity of ''positive activation'', i.e., each node feature is linear expressed by its $K$-hop neighbours’ feature vectors with non-negative coefficients. Based on this, they design a spectral GNN that linearly combine different order low-pass and high-pass filters and verify its effectiveness on benchmark datasets.

### Strengths
- The research question of this paper is interesting and meaningful, i.e., investigating the key differences between different graph filters.
- The proposed simpleNet achieve a good trade-off between performance and computation efficiency.

### Weaknesses
 - The presentation quality of this paper needs to be improved, e.g., there are many symbol errors in the proof (See Questions for detail). Although these errors do not affect the final results, rigidity is one of the most fundamental requirements for scientific papers.
- I appreciate the efforts devoted to investigating the key differences between different graph filters. However, I think that the linear expression ability and convergence rate are not enough to reveal the essential differences between different graph filters. First, although authors have shown that different graph polynomial filters have the same expressive ability, their performances may also vary greatly, depending on their implementations approaches (e.g., ChebNet [1] and ChebNetII [2]). Specifically, the practical differences in performance between filters like Chebyshev polynomials and Lanczos polynomials, which have the same theoretical approximation power, are not sufficiently addressed. Besides, it is still unclear the relation between this expressive ability and node classification performance. Second, in the implementation of these spectral GNNs, the raw features are first commonly feed into a MLP and then transformed by the filters, namely $Z=\gamma(L)\sigma(\sigma(XW_1)W_2)$. Due to the involve of two parametric matrix $W_1, W_2$ and the non-linear activation function $\sigma(\cdot)$ in the forward process, the optimization of these spectral GNNs is non-convex, which could not be directly simplified as a convex problem in Eq. (4). The analysis overlooks the impact of this non-convexity. Analyzing the training dynamic [3,4] of the model could be a more applicable approach. Third, the optimization approaches (SGD or Adam) also have significant impacts on the performances, which should be considered in the analysis.
- The heterophilic graph datasets seem to be out-of-date. It has been shown that results obtained on these datasets are not reliable. The authors are encouraged to evaluate on the datasets presented in [5].

### Questions
Q1: There are many symbol errors in the proof of Lemma 3.1. and Lemma 3.2. The denominator of Eq. (16) should be $\left(\sum_{i=1}^n a_i\right)^2$. The authors claim that Eq. (17) is a quadratic function of $x$, thus it should be corrected as
$$
f(x) = \left( \sum_{i=1}^n \frac{a_i}{\lambda_i} \right) x^2 - \frac{\lambda_1+\lambda_n}{\sqrt{\lambda_1 \lambda_n}}x + \left( \sum_{i=1}^n \lambda_i a_i \right).
$$
In Eq.~(19), the third term in the first bracket should be $\sum_{i=2}^{n-1} \lambda^{-1}_i a_i$. 

Also, Eq. (39) should be corrected as $\left(A^{k+1}\right)\_{ij}=\sum_{r=1}^n \left(A^k \right)\_{ir} A\_{rj}$.

Although these typos do not affect the final result, I encourage the authors to correct them in order to avoid unnecessary misunderstandings for other readers.

Q2: The motivation and the advantages of the GIA theory is not so clear. What performance gain the positive and proper activation could bring? Is there any connection between the generalization and positive (or proper) activation? What extra insights could the GIA theory bring?

Q3：The proposed fixedMono and learnedMono seem to be variants of JKNet [6] where different hidden features of different neighborhood ranges are combined. The only difference is the way that combining these features. The authors adopt a linear combination, while Xu et al. use LSTM or max pooling. The authors should clarify this and compare with JKNet.

[6] Xu et al, Representation Learning on Graphs with Jumping Knowledge Networks. ICML 2018.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
While the most GNNs designs various polynomial filters, this paper proves that the "expressive power" of the polynomial filter only depends on the degree of the polynomial. From this analysis, this paper proposes simple polynomial filters. This paper also conducts experiments on homogenous and non-homogenous datasets.

### Strengths
1) The simpleness of the polynomial filter. This filter may be easy to understand in terms of behavior analyses. Also, this filter is easy to implement.

### Weaknesses
1) Weakness of Thm. 3.1.
Thm 3.1 is the key argument of the equivalence of the "expressive power." However, this is rather weak, since the K linear independent components does not warrant the downstream machine learning algorithms performance. Maybe a set of K eigenvectors has the same expressive power, some random projection onto the K space may have the same expressive power -- but I believe that the "expressive power" we want to know in this context may be more nuanced one. Specifically, the theorem only shows that any polynomial filter of degree K can be represented by a linear combination of K basis polynomials, but it doesn't guarantee that any such combination will be useful for a specific downstream task. The theorem is more about representation equivalence than practical performance equivalence.

2) Computational complexity.
Even if the original graph has a sparse structure, i.e. $m << n^2$, the filter has a dense matrix, which is $O(n^2)$ since the multiplication of two sparse matrices does not preserve the sparse structure. Therefore, the filter does not enjoy the sparseness, and thus the computational complexity therefore increases from the simple filters, like GCN whose polynomial filter is basically the same as $\tilde{A}$. This is a significant drawback, especially for large graphs where computational efficiency is crucial. The authors do not address the practical implications of this dense matrix computation, such as memory usage and scalability.

3) Weakness of the Experimental results.
Seeing homogeneous results (Table 3), the proposed method is more or less same as the existing methods considering the variances. Also, for non-homogeneous results (Table 4), in some datasets proposed methods underperform the exiting ones. Seeing Table 5, as expected from the discussed of my 2) above, the computational time is not appealing. Thus, the proposed methods at this stage do not improve the exiting methods and are slow. While in the limitations the authors stated that the proposed methods underperform for non-homogenous datasets, I think that this comes form the nature of the filter designs. See more for the questions.

4) Insufficient comparison with exiting filters.
In the page 3 of (Defferrard et al, 2016) the complexity of the polynomial filter is discussed. The point of 2) is actually discussed, and also, the Krylov subspace is expected to serve as a better filter, and materialized in [i]. Thus, the authors may want to compare with [i] experimentally and theoretically. Also, since the filter perspective is well-studied in [ii], the authors may want to compare as well. See the questions for the connection between this paper and [ii].

### Questions
1) From [ii], the established GNNs are known to be a low-pass filter, i.e., the eigenspace of the graph Laplacian associated with smaller eigenvalues has homogeneous information. Thus, the larger eigenspace captures non-homogeneous information.
From this observation, we expect that (2I-L)^k amplifies the homongeous information, much faster than L^k. Thus, the underperfomrance on non-heterogeneous datasets is expected. Also, if we increase k_{1} and k_{2}, the larger $k$s become dominant, and thus the performance decreases in Fig.2 is also explained as an oversmoothing.

The question is, can we expand like 

\sum_{k} (a_{k}I - L)^k + \sum_{k'} (b_{k'}I + L)^k'

So that we have a better control on the amplification of the eigenspaces? By this in theory we expect better performance on non-homogenous datasets.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
