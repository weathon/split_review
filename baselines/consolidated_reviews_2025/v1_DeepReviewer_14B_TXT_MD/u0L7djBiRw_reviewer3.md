### Summary

The paper proposes a new random embedding method called Rademacher-like embedding (RLE). The method uses a smaller Rademacher matrix and several auxiliary random arrays to implicitly generate an embedding matrix. The proposed method achieves O(n+k^2) time and space complexity, which is linear if k is not larger than O(n^{1/2}). The paper also provides theoretical analysis of the proposed method and applies it to single-pass randomized SVD and randomized Arnoldi process.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The proposed method achieves linear time complexity when k is not larger than O(n^{1/2}).

The paper provides theoretical analysis of the proposed method.

The paper applies the proposed method to single-pass randomized SVD and randomized Arnoldi process.

### Weaknesses

#### Some Related Works


#### comment

The proposed method is not very novel, as it is based on existing Rademacher embedding.

The paper does not provide a detailed comparison with existing methods, such as SRHT and Count Sketch.

The paper does not provide a clear explanation of the advantages and disadvantages of the proposed method compared to existing methods.

The paper does not provide a detailed analysis of the practical implications of the proposed method, such as its performance on real-world datasets and its sensitivity to parameter settings.

### Suggestions

The paper should provide a more thorough comparison with existing random embedding techniques, specifically SRHT and Count Sketch. The current discussion lacks a detailed analysis of the trade-offs between these methods and the proposed RLE. For instance, while SRHT is known for its fast computation using fast Fourier transforms, it may not be as robust as RLE in certain scenarios. A more detailed comparison should include a discussion of the specific conditions under which each method performs best, considering factors such as the dimensionality of the data, the desired level of accuracy, and the computational resources available. Furthermore, the paper should include a more rigorous analysis of the theoretical properties of RLE, such as its concentration bounds and its ability to preserve pairwise distances or other relevant geometric properties of the data. This would help to better understand the strengths and limitations of the proposed method compared to existing alternatives.

To improve the practical relevance of the paper, the authors should include a more comprehensive evaluation of the proposed method on real-world datasets. The current evaluation is limited to synthetic data and does not provide a clear picture of how RLE performs in practical applications. The paper should include experiments on a variety of datasets with different characteristics, such as high-dimensional data, sparse data, and data with complex structures. The evaluation should also include a sensitivity analysis of the method to different parameter settings, such as the size of the Rademacher matrix and the number of auxiliary random arrays. This would help to identify the optimal parameter settings for different applications and to understand the robustness of the method to variations in these parameters. The paper should also compare the performance of RLE with other state-of-the-art random embedding methods on these real-world datasets.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. While the paper mentions that RLE achieves linear time complexity when k is not larger than O(n^{1/2}), it does not discuss the implications of this constraint in practical applications. The paper should also discuss the potential drawbacks of using a smaller Rademacher matrix and auxiliary random arrays, such as the potential loss of information or the introduction of bias. A more thorough discussion of these limitations would help to provide a more balanced view of the proposed method and to guide future research in this area. The paper should also discuss the potential for future work, such as exploring different types of auxiliary random arrays or developing adaptive methods for choosing the size of the Rademacher matrix.

### Questions

How does the proposed method compare to existing methods, such as SRHT and Count Sketch, in terms of performance and robustness?

What are the advantages and disadvantages of the proposed method compared to existing methods?

How does the proposed method perform on real-world datasets?

How sensitive is the proposed method to parameter settings?

### Rating

3

### Confidence

4

**********
