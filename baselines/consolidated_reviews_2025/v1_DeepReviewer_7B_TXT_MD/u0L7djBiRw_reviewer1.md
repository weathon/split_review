### Summary

This paper proposes a fast and robust Rademacher-like random embedding (RLE) algorithm, which can embed an n-dimensional vector into a k-dimensional space in O(n) time and space (assuming k << n). The authors provide theoretical analysis of the proposed approach and prove it is a Rademacher-like random embedding with O(n+k^2) computational complexity. The authors also conduct experiments on single-pass RSVD and randomized Arnoldi process to demonstrate the practical efficiency and effectiveness of the proposed RLE.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed RLE algorithm is simple and easy to implement.
2. The authors provide theoretical analysis and proofs for the proposed RLE algorithm.
3. The authors conduct experiments on single-pass RSVD and randomized Arnoldi process to demonstrate the practical efficiency and effectiveness of the proposed RLE.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed RLE algorithm is not novel. The idea of using a smaller Rademacher matrix and several random signs to implicitly generate an embedding matrix has been proposed in previous work (Balabanov & Nouy, 2019). The main difference is that the authors in this paper do not consider the mutual independence of whole matrix entries, which may lead to less robust performance. Specifically, the lack of mutual independence could lead to correlations between rows of the embedding matrix, potentially degrading the performance of algorithms relying on the embedding, such as those requiring an approximate isometry.
2. The theoretical analysis of the proposed RLE algorithm is not rigorous enough. The authors only provide the proof of Theorem 6, which states that the proposed RLE is an (ε,δ,d)-oblivious subspace embedding. However, the proofs of other theorems, such as Theorem 3, 4, and 5, are missing. The absence of these proofs makes it difficult to fully assess the theoretical properties of the proposed embedding, such as the preservation of vector norms and the orthogonality of vectors after embedding.
3. The experiments in this paper are not sufficient. The authors only conduct experiments on single-pass RSVD and randomized Arnoldi process. It is recommended to conduct experiments on more tasks, such as linear regression, classification, and clustering, to demonstrate the practical efficiency and effectiveness of the proposed RLE. The current experiments do not fully explore the potential applications of the proposed embedding in various machine learning tasks.
4. The authors do not compare the proposed RLE algorithm with other fast random embedding algorithms, such as sparse sign embedding and partial SVD embedding. It is recommended to compare the proposed RLE algorithm with these algorithms in terms of both efficiency and effectiveness. The lack of comparison with other state-of-the-art fast random embeddings makes it difficult to assess the relative advantages and disadvantages of the proposed method.

### Suggestions

The authors should provide a more detailed comparison with existing fast random embedding techniques, particularly those that also leverage smaller Rademacher matrices, such as the method proposed by Balabanov & Nouy (2019). A thorough comparison should not only focus on the theoretical aspects but also on the practical performance, including the computational cost and the accuracy of the embedding in various machine learning tasks. The authors should also investigate the impact of the lack of mutual independence on the performance of algorithms that rely on the embedding, such as those used in linear regression or classification. This could involve conducting experiments with different types of data and different parameter settings to assess the robustness of the proposed embedding.

To strengthen the theoretical analysis, the authors should provide complete proofs for all the theorems mentioned in the paper, including Theorems 3, 4, and 5. These proofs should clearly demonstrate the properties of the proposed embedding, such as the preservation of vector norms and the orthogonality of vectors after embedding. The authors should also provide a more detailed explanation of the assumptions and limitations of the theoretical results. Furthermore, the authors should investigate the practical implications of the theoretical results, such as how the parameters of the embedding affect the performance of the algorithms that use it. This could involve conducting sensitivity analysis experiments to assess the robustness of the proposed embedding to different parameter settings.

The experimental section should be significantly expanded to include a wider range of tasks and datasets. The authors should conduct experiments on linear regression, classification, and clustering tasks, using both synthetic and real-world datasets. The experiments should also include a comparison with other fast random embedding algorithms, such as sparse sign embedding and partial SVD embedding, in terms of both efficiency and effectiveness. The authors should also investigate the impact of different parameter settings on the performance of the proposed embedding in these tasks. This would provide a more comprehensive evaluation of the proposed method and its potential applications in various machine learning domains. The authors should also consider including experiments on large-scale datasets to assess the scalability of the proposed method.

### Questions

1. The proposed RLE algorithm is not novel. The idea of using a smaller Rademacher matrix and several random signs to implicitly generate an embedding matrix has been proposed in previous work (Balabanov & Nouy, 2019). The main difference is that the authors in this paper do not consider the mutual independence of whole matrix entries, which may lead to less robust performance. Please discuss the differences between the proposed RLE algorithm and the previous work in more detail.
2. The theoretical analysis of the proposed RLE algorithm is not rigorous enough. The authors only provide the proof of Theorem 6, which states that the proposed RLE is an (ε,δ,d)-oblivious subspace embedding. However, the proofs of other theorems, such as Theorem 3, 4, and 5, are missing. Please provide the proofs of these theorems.
3. The experiments in this paper are not sufficient. The authors only conduct experiments on single-pass RSVD and randomized Arnoldi process. It is recommended to conduct experiments on more tasks, such as linear regression, classification, and clustering, to demonstrate the practical efficiency and effectiveness of the proposed RLE. Please consider conducting experiments on more tasks.
4. The authors do not compare the proposed RLE algorithm with other fast random embedding algorithms, such as sparse sign embedding and partial SVD embedding. It is recommended to compare the proposed RLE algorithm with these algorithms in terms of both efficiency and effectiveness. Please compare the proposed RLE algorithm with these algorithms.

### Rating

3

### Confidence

4

**********
