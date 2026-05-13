# Is $k \times k$ Matrix Eigendecomposition Sufficient for Spectral Clustering?

- Decision: Reject
- Scores: 6, 5, 6, 1

## Abstract
Spectral clustering has been widely used in clustering tasks due to its effectiveness. However, its key step, eigendecomposition of an $n\times n$ matrix, is computationally expensive for large-scale datasets. Recent works have proposed methods to reduce this complexity, such as Nystr\"om method approximation and landmark-based approaches. While these methods aim to maintain good clustering quality while performing eigendecomposition on smaller matrix. The minimum matrix size required for spectral decomposition in spectral clustering is $k\times k$ (where $k$ is the number of clusters), as it needs to obtain $n\times k$ k-dimensional spectral embedding features. However, no algorithm can achieve good clustering performance with only a $k\times k$ matrix eigendecomposition currently. In this paper, we propose a novel distribution-based spectral clustering. Our method constructs an $n\times k$ bipartite graph between n data points and k distributions, enabling the eigendecomposition of only a $k\times k$ matrix while preserving clustering quality. We demonstrate that our approach can achieve efficient and effective spectral clustering through $k\times k $matrix eigendecomposition.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into the computational challenges in spectral clustering, specifically the high cost affiliated with the eigen-decomposition of large Laplacian matrices (commonly n × n, where n denotes the number of data points). The authors proposed a distribution-based method D-SPEC, which transforms the spectral clustering into the bipartite graph clustering with n × k adjacency matrix. In this way, the cost of eigen-decomposition is reduced to O(nk^2). The authors conducted extensive experiments on synthetic and real datasets, demonstrating that D-SPEC not only sustains the efficacy of clustering but also exhibits robust scalability on datasets with millions of data points.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed D-SPEC is interesting.
3. There are extensive experiments on synthetic and real datasets, which demonstrate the effectiveness and scalability of D-SPEC.

### Weaknesses
1. D-SPEC refines the n-by-n similarity matrix S (in Line 158) by filtering out the edges with weights smaller than $\tau$ and obtains landmarks/anchors (subgraphs). However, there is a paradox in the current setting. First, calculating the similarity matrix S requires O(n^2) time complexity, which is the same as the eigen-decomposition of the Laplacian matrix (which can be solved with efficient algorithms like Lanczos in O(n^2)). Thus, the D-SPEC makes no sense in terms of computational efficiency. Conversely, if D-SPEC chooses to sample p samples to construct the similarity matrix S (Line 165), then it degenerates into the most common approach of choosing landmarks/anchors. So the authors should provide a more detailed explanation for this paradox.

2. The number of landmarks/anchors (subgraphs) is indirectly determined by the parameter $\tau$. Could the authors provide some insights on how the parameter $\tau$ affects the number of landmarks/anchors and further impacts the clustering performance?

3. The paper introduces “distribution-based” as a core concept of the new method, but it does not provide a detailed explanation of what this means. Could you clarify how this method uses “distributions” for clustering and how it fundamentally differs from traditional point-based methods? What theoretical basis supports this choice, and are there practical cases where “distribution-based” clustering shows clear advantages over traditional methods?

4. There seems to be a mistake in Theorem 3.2. I think the eigenvector $v$ according to zero eigenvalues is not the one defined in Line 661. Besides, the proof of Theorem 3.2 is not rigorous enough. For example, the optimal solution of eign-decomposition is not unique, so can it be guaranteed that the obtained eigenvector is as stated in Theorem 3.2?

5. It would help to standardize the use of symbols throughout and to provide clear explanations when new symbols are introduced.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed a superior and effective distribution-based spectral clustering (D-SPEC)
algorithm, to solve the fundamental limitations of spectral clustering w.r.t. efficiency and effectiveness. First, D-SPEC proposes a novel distribution-based spectral clustering not the point-based method, which can contain more information of the original graph. Second, D-SPEC constructs an n×k bipartite graph between n data points and k distributions, enabling the eigendecomposition of only a k×k matrix, which is suitable for large-scale datasets. Finally, D-SPEC proves theoretically that distribution-based spectral clustering can preserve graph information and is more robust to noise. Comprehensive experiments verify the superiority of the proposed model.

### Strengths
1.The proposed D-SPEC Enhances effectiveness of spectral clustering by transitioning from a traditional point-based perspective to a distribution-based perspective.
2.The proposed D-SPEC Enhances the efficiency of spectral clustering by constructing a bipartite graph with n*k, which is a smaller matrix than the matrix with n*p, where p is the number of the sampling points).
3.The theoretical studies are very interesting.Theoretical proof that D-SPEC preserves graph information, along with a noise tolerance bound, demonstrates the robustness of D-SPEC.

### Weaknesses
1.In Figure 1, is the leftmost figure is the example graph G that contains 3 subgraphs? an Annotation on the figure will make it clearer to readers.
2.The article contains many unclear symbols and expressions, such as 
(1)In Eq.(1), G_i denotes the i-th subgraph, in the following, G_j denotes the j-th subgraph, but i and j have different value ranges in other parts of the article (like i=1,2,...,n). Authors should use unified letter representation to prevent readers from misunderstanding.
(2)For the pseudo code of D-SPEC, in step 4, what is letter V? it was not defined in the previous text. As W is an n*k matrix, does the letter V denote n samples or k spectral embeddings (it is described in Theorem 3.4)? 
3.Figure 3 is not clear.  
4.What is the size and other information of 5 large-scale datasets in Figure 4? And Figure 4 cannot show D-SPEC’s efficiency.   
5.Compared existed methods, D-SPEC only gives a better method to construct a n*k bipartite graph. I think its innovation is not enough to be published in this top conference.

### Questions
1.In Figure 1, is the leftmost figure is the example graph G that contains 3 subgraphs? an Annotation on the figure will make it clearer to readers.
2.The article contains many unclear symbols and expressions, such as 
(3)In Eq.(1), G_i denotes the i-th subgraph, in the following, G_j denotes the j-th subgraph, but i and j have different value ranges in other parts of the article (like i=1,2,...,n). Authors should use unified letter representation to prevent readers from misunderstanding.
(4)For the pseudo code of D-SPEC, in step 4, what is letter V? it was not defined in the previous text. As W is an n*k matrix, does the letter V denote n samples or k spectral embeddings (it is described in Theorem 3.4)? 
3.Figure 3 is not clear.  
4.What is the size and other information of 5 large-scale datasets in Figure 4? And Figure 4 cannot show D-SPEC’s efficiency.   
5.Compared existed methods, D-SPEC only gives a better method to construct a n*k bipartite graph. I think its innovation is not enough to be published in this top conference.

### Soundness
3

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
4

### Summary
This paper presents a distribution-based spectral clustering algorithm, termed D-SPEC, that reduces the computational demand of spectral clustering to the eigendecomposition of a k × k matrix. By constructing an n × k bipartite graph, the authors enable clustering through a smaller matrix, preserving information while reducing complexity. D-SPEC is shown to perform competitively with traditional spectral clustering methods, especially in handling noise and maintaining graph structure, and experiments confirm its robustness on both synthetic and real datasets.

### Strengths
1.The proposed distribution-based clustering approach achieves efficient clustering with a k × k matrix eigendecomposition, a notable shift from traditional methods.
2. Explanations of the bipartite graph structure and eigendecomposition process are well-structured.
3. This approach is claimed that it has potential to enable large-scale spectral clustering, expanding practical applications of clustering for large datasets.

### Weaknesses
1.The approach assumes noise tolerance, but experimental validation of this property on noisy, complex graphs is limited.
2.The D-SPEC approach shows similarities with landmark-based clustering methods, lacking clear differentiation.
3. Limited testing on real-world, large-scale datasets reduces confidence in its applicability.
4.The theoretical sections are occasionally verbose, with redundant content that could be streamlined.

### Questions
1.How does D-SPEC’s noise tolerance compare to landmark-based or Nyström methods? A direct comparison would help clarify its advantages.
2.Could a hybrid method, combining landmarks and distribution-based clustering, improve flexibility?
3.How is the threshold parameter for bipartite graph construction determined? Is the method highly sensitive to this parameter?
4.How does the method handle non-spherical or poorly-separated clusters?
5.Does the approach suffer performance degradation in highly connected graphs?
6.Can the authors provide empirical comparisons of computation time between D-SPEC and traditional spectral clustering on large datasets?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper addresses spectral clustering's typical scalability limitations on large datasets. It explores whether spectral clustering can be effectively performed using only a small square matrix eigendecomposition. The authors propose a distribution-based method (D-SPEC) that constructs a bipartite graph between data points and landmarks to enable this reduced computation. Some experiment results are provided.

### Strengths
* The method is fast in some sense.
* There are some theoretical guarantees

### Weaknesses
* The research motivation is questionable. It assumes W must be fully connected. However, many graph-based clustering methods only use a sparse W (e.g., 10-NN). Eigendecomposition of a sparse matrix is cheap.
* The method can be sensitive to the hyperparameters (e.g., psi)
* The experiment results are not convincing, especially for the MNIST and CoverType datasets.

### Questions
* In Table 5, you listed the parameter search ranges. How did you choose the best in the ranges?
* Why D-SPEC is so bad for the covertype dataset?
* It is unsuitable to use k x k in the title because k is not defined yet.

### Soundness
2

### Presentation
2

### Contribution
2
