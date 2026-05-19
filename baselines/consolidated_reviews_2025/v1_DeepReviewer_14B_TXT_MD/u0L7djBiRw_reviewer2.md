### Summary

The paper introduces a new random embedding, Rademacher-like embedding (RLE), which achieves O(n+k^2) computational complexity for embedding an n-dimensional vector into k-dimensional space. The authors provide theoretical analysis and empirical results demonstrating the effectiveness of RLE in applications such as single-pass randomized SVD and randomized Arnoldi process.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed RLE achieves linear time complexity O(n+k^2) when k is not larger than O(n^(1/2)), which is a significant improvement over existing methods like Gaussian and Rademacher embeddings that have O(nk) complexity.

2. The authors provide comprehensive theoretical analysis, proving properties such as pairwise independence of entries and the subspace embedding property.

3. Empirical results show that RLE outperforms Gaussian and sparse sign embeddings in terms of speed while maintaining comparable accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide a detailed comparison of the constants involved in the complexity analysis with existing methods. While the asymptotic complexity is improved, the actual runtime performance may depend heavily on these constants.

2. The numerical experiments are limited to specific datasets and parameter settings. It is unclear how the performance of RLE would generalize to other scenarios.

3. The proof of Theorem 6 is incorrect. The authors claim that the proof follows from Lemma 9 and Lemma 10, but there is a gap in the argument. Specifically, Lemma 10 only shows that $|u_i^T \Theta u_i - u_i^T u_i| < \epsilon_1$ for any vector $u_i$, but it does not show that $|u_i^T \Theta u_i - u_j^T \Theta u_j| < \epsilon_1$ for any two vectors $u_i$ and $u_j$. This is a crucial step in the proof of Theorem 6, and the authors need to provide a more rigorous argument.

### Suggestions

The paper introduces a novel Rademacher-like embedding (RLE) with a claimed computational complexity of O(n+k^2), which is a significant improvement over the O(nk) complexity of standard Gaussian and Rademacher embeddings. However, the practical implications of this theoretical improvement are not fully explored. Specifically, the authors should provide a more detailed analysis of the constant factors hidden within the O(n+k^2) complexity. For instance, while the asymptotic complexity is better, the actual runtime could be affected by the specific implementation details and the constants involved in the matrix operations. A comparison of these constants with those of existing methods, such as sparse sign embedding, would be beneficial. This would help to understand the practical scenarios where RLE would provide a substantial speedup. Furthermore, the authors should investigate the impact of different parameter settings on the performance of RLE. The current experiments use a fixed set of parameters, and it is unclear how the performance would vary with different choices of these parameters. A sensitivity analysis of the parameters would provide a more complete picture of the method's robustness and applicability.

To strengthen the theoretical foundation of the paper, the authors should address the gap in the proof of Theorem 6. The current proof relies on Lemma 10, which only provides a bound on the difference between $u_i^T \Theta u_i$ and $u_i^T u_i$ for a single vector $u_i$. However, the proof of Theorem 6 requires a bound on the difference between $u_i^T \Theta u_i$ and $u_j^T \Theta u_j$ for any two vectors $u_i$ and $u_j$. This requires a more careful analysis of the dependencies between the entries of the embedding matrix $\Theta$. The authors should either provide a corrected proof or clearly state the limitations of the current result. This is crucial for the validity of the theoretical claims made in the paper. The authors should also consider providing a more detailed explanation of the practical implications of the theoretical results. For example, how does the subspace embedding property translate into the performance of the randomized SVD and Arnoldi process? A more detailed discussion of these connections would help the reader understand the significance of the theoretical results.

Finally, the authors should consider expanding the numerical experiments to include a wider range of datasets and parameter settings. The current experiments are limited to specific datasets and parameter settings, which makes it difficult to assess the generalizability of the proposed method. The authors should consider including datasets with different characteristics, such as varying sparsity levels and dimensionality. Additionally, the authors should explore the performance of RLE with different choices of the parameter k, which controls the dimensionality of the embedding. This would provide a more comprehensive evaluation of the method's performance and help to identify the optimal parameter settings for different applications. Furthermore, the authors should compare the performance of RLE with other state-of-the-art random embedding techniques, such as Count-Sketch and SRHT, to provide a more complete picture of the method's strengths and weaknesses.

### Questions

1. The authors claim that the time complexity of RLE is O(n+k^2). However, the actual runtime performance may depend on the specific implementation and the constants involved. Can the authors provide a more detailed analysis of the constants and compare them with existing methods?

2. The numerical experiments are limited to specific datasets and parameter settings. How does the performance of RLE generalize to other scenarios?

3. The proof of Theorem 6 is incorrect. The authors claim that the proof follows from Lemma 9 and Lemma 10, but there is a gap in the argument. Specifically, Lemma 10 only shows that $|u_i^T \Theta u_i - u_i^T u_i| < \epsilon_1$ for any vector $u_i$, but it does not show that $|u_i^T \Theta u_i - u_j^T \Theta u_j| < \epsilon_1$ for any two vectors $u_i$ and $u_j$. This is a crucial step in the proof of Theorem 6, and the authors need to provide a more rigorous argument.

### Rating

3

### Confidence

4

**********
