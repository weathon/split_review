### Summary

The paper proposes a novel Rademacher-like random embedding (RLE) algorithm for efficiently reducing the dimensionality of high-dimensional vectors. The RLE algorithm leverages a smaller Rademacher matrix and several random signs to implicitly generate an embedding matrix, achieving linear time and space complexity. The authors provide theoretical analysis demonstrating that the proposed RLE maintains the 2-norm of vectors and exhibits pairwisely independent entries. Experimental results show that the RLE algorithm achieves 1.7x speed-up on average while maintaining accuracy in single-pass randomized SVD and randomized Arnoldi process.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a novel Rademacher-like random embedding (RLE) algorithm that achieves linear time and space complexity, which is a significant improvement over existing methods.
2. The authors provide theoretical analysis and proofs for the proposed RLE algorithm, demonstrating its effectiveness in preserving vector norms and exhibiting pairwisely independent entries.
3. The paper presents experimental results that demonstrate the practical efficiency and effectiveness of the RLE algorithm in single-pass randomized SVD and randomized Arnoldi process, achieving 1.7x speed-up on average while maintaining accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the impact of the embedding dimension k on the accuracy of the RLE algorithm. It is unclear how the choice of k affects the performance of the algorithm, especially in terms of preserving the structure of the original data. Specifically, the paper lacks a discussion on how the distribution of the Rademacher matrix and the random signs interact to influence the final embedding, and how this interaction changes with different values of k. A more thorough analysis should explore the trade-offs between embedding dimension and accuracy, potentially including a sensitivity analysis of the algorithm's performance with respect to k.
2. The paper does not compare the proposed RLE algorithm with other state-of-the-art fast random embedding methods, such as sparse sign embedding and partial SVD embedding. While the authors mention that their method is faster than Gaussian embedding, a more comprehensive comparison with other fast methods is needed to fully demonstrate the advantages of the proposed approach. The comparison should not only focus on speed but also on accuracy and memory usage, especially when dealing with large-scale datasets. The paper should include a detailed analysis of the computational complexity of the proposed method compared to other methods, and provide empirical evidence to support the claims of improved efficiency.

### Suggestions

The paper should include a more detailed analysis of the impact of the embedding dimension k on the accuracy of the RLE algorithm. This analysis should explore the relationship between k and the preservation of the original data's structure. For instance, the authors could investigate how different values of k affect the reconstruction error of the original data after embedding and reconstruction. This could involve experiments with varying k and metrics such as the Frobenius norm of the difference between the original and reconstructed matrices. Furthermore, the paper should provide a theoretical justification for the choice of k, possibly by relating it to the properties of the Rademacher matrix and the random signs used in the embedding process. This would help in understanding the limitations and applicability of the proposed method.

To strengthen the paper, the authors should include a more comprehensive comparison of the proposed RLE algorithm with other state-of-the-art fast random embedding methods. This comparison should not only focus on speed but also on accuracy and memory usage. The authors should consider including methods such as sparse sign embedding and partial SVD embedding in their experimental evaluation. The comparison should be conducted on a variety of datasets, including both synthetic and real-world datasets, to demonstrate the robustness of the proposed method. The paper should also provide a detailed analysis of the computational complexity of the proposed method compared to other methods, and provide empirical evidence to support the claims of improved efficiency. This would help in understanding the practical advantages of the proposed method over existing approaches.

Finally, the paper should provide a more detailed explanation of the implementation of the RLE algorithm, including the specific choices made for the Rademacher matrix and the random signs. The authors should also discuss the potential limitations of the proposed method, such as its sensitivity to the choice of parameters and its performance on different types of data. This would help in understanding the practical applicability of the proposed method and its potential for future research. The paper should also include a discussion of the potential impact of the proposed method on various applications, such as machine learning and data analysis.

### Questions

1. How does the choice of the embedding dimension k affect the accuracy of the RLE algorithm? Are there any guidelines for selecting an appropriate value of k for different types of data?
2. How does the proposed RLE algorithm compare with other state-of-the-art fast random embedding methods, such as sparse sign embedding and partial SVD embedding, in terms of speed, accuracy, and memory usage?

### Rating

6

### Confidence

3

**********
