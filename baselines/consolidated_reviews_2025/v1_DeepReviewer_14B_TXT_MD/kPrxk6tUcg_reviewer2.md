### Summary

This paper proposes a neuron-enhanced autoencoder matrix completion method to improve the accuracy of recovering missing values. The theoretical analysis shows the generalization ability of the proposed method. The experimental results on synthetic and benchmark datasets demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper provides the theoretical analysis of the proposed method. The paper is well-organized.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-motivated. The authors only give one reason for the low performance of the existing methods, i.e., the assumption that the ratings are linear interactions between user features and item features. However, there are no theoretical and experimental results to support this claim. It is unclear why a linear interaction model is inherently insufficient for matrix completion, especially given the success of methods like PMF and PMF++ which leverage such interactions. The paper needs to provide a more rigorous justification for why nonlinearities are crucial in this context, perhaps by showing specific scenarios where linear models fail.
2. The novelty of the proposed method is limited. The proposed method is a combination of the autoencoder-based matrix completion method and the element-wise neural networks. The paper does not adequately explain why this specific combination is superior to other possible architectures or why it addresses the limitations of existing methods. The use of element-wise neural networks seems somewhat ad-hoc without a clear theoretical grounding.
3. The experiments are not convincing. There is no comparison between the proposed method and the state-of-the-art methods. The paper should include comparisons with recent, highly performing matrix completion algorithms to demonstrate the practical value of the proposed method. The lack of such comparisons makes it difficult to assess the actual contribution of this work.
4. The paper has some writing problems. For example, the paper uses "the following" twice in one sentence: "The following Theorem 3.1 is based on the assumption of missing completely at random (MCAR). The following assumption has been widely used in previous work of matrix completion".

### Suggestions

The paper needs to provide a more compelling motivation for the proposed method. The authors should elaborate on the limitations of linear interaction models in matrix completion, providing concrete examples or theoretical arguments to support their claim. For instance, they could discuss scenarios where user preferences or item characteristics exhibit nonlinear relationships that cannot be captured by linear models. This could involve showing how specific types of data distributions or interaction patterns lead to the failure of linear methods, thereby justifying the need for a nonlinear approach. Furthermore, the authors should provide a more detailed explanation of why the proposed method, specifically the combination of autoencoders and element-wise neural networks, is expected to overcome these limitations. A more rigorous analysis of the method's properties, such as its ability to capture specific types of nonlinearities, would be beneficial.

The experimental section needs significant improvement. The authors should compare their method against state-of-the-art matrix completion algorithms, including those that utilize deep learning techniques. This comparison should be performed on a variety of benchmark datasets, and the results should be analyzed in detail. The paper should also include ablation studies to evaluate the contribution of different components of the proposed method. For example, the authors could compare the performance of the method with and without the element-wise neural networks to demonstrate their effectiveness. Additionally, the authors should provide a more thorough discussion of the experimental results, including an analysis of the method's strengths and weaknesses. The paper should also include a discussion of the computational complexity of the proposed method and compare it to other methods.

Finally, the paper needs a thorough revision to address the writing issues. The authors should carefully proofread the paper to eliminate grammatical errors and awkward phrasing. The use of clear and concise language is essential for effective communication. The authors should also ensure that the paper is well-organized and that the arguments are presented in a logical and coherent manner. The paper should also include a more detailed explanation of the theoretical analysis, including a discussion of the assumptions and limitations of the analysis. The authors should also provide a more detailed explanation of the experimental setup, including the datasets used and the evaluation metrics.

### Questions

1. Why does the low performance of the existing methods come from the assumption that the ratings are linear interactions between user features and item features?
2. Why not compare the proposed method with the state-of-the-art methods?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
