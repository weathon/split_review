### Summary

This paper provides a theoretical explanation for the empirical success of diffusion models in learning image distributions. The authors propose that diffusion models can effectively learn image distributions when the data is a mixture of low-rank Gaussians, and that the training loss of diffusion models is equivalent to solving the subspace clustering problem. They also demonstrate that the subspaces learned by diffusion models correspond to semantic representations of images, which can be used to control image generation. The paper provides a theoretical foundation for understanding how diffusion models learn image distributions and offers practical guidance for controlling image generation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical explanation for the empirical success of diffusion models in learning image distributions, which is a significant contribution to the field of deep learning.

2. The paper demonstrates that the subspaces learned by diffusion models correspond to semantic representations of images, which can be used to control image generation. This finding has practical implications for image editing and other applications.

3. The paper is well-written and easy to follow, with clear explanations of the theoretical concepts and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the data is a mixture of low-rank Gaussians, which may not hold in real-world scenarios. The authors should provide more evidence to support this assumption and discuss the limitations of this assumption.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is an important factor to consider when applying the method to large-scale datasets.

3. The paper does not compare the proposed method with other state-of-the-art methods for learning image distributions, which makes it difficult to assess the performance of the proposed method.

### Suggestions

The assumption of a mixture of low-rank Gaussians is a significant limitation that needs further investigation. While the authors provide some justification based on the intrinsic dimensionality of images, it is crucial to explore the sensitivity of the theoretical results to deviations from this assumption. For instance, real-world image datasets often exhibit more complex structures and dependencies than a simple mixture of Gaussians. The authors should consider analyzing the performance of their method on datasets with varying degrees of complexity and comparing it to the theoretical predictions. Furthermore, they should explore alternative data models that might be more suitable for real-world image data, such as mixture models with non-Gaussian components or models that incorporate spatial dependencies. This would help to establish the robustness of their theoretical framework and its applicability to a wider range of practical scenarios. A more thorough analysis of the limitations of the Gaussian assumption is essential for the practical relevance of the work.

Regarding the computational complexity, the authors should provide a more detailed analysis of the computational cost of their method, especially when applied to large-scale datasets. While the paper mentions that the method is efficient, a more rigorous analysis is needed to understand the scaling behavior of the algorithm with respect to the number of data points, the dimensionality of the data, and the complexity of the diffusion model. This analysis should include both theoretical bounds and empirical measurements. For example, the authors could analyze the time and memory requirements of the training process and compare them to other methods for learning image distributions. Furthermore, they should discuss the practical implications of the computational cost for real-world applications, such as training on high-resolution images or large datasets. This would help to assess the feasibility of the proposed method for different use cases.

Finally, the lack of comparison with state-of-the-art methods for learning image distributions is a significant weakness. The authors should compare their method with other approaches, such as generative adversarial networks (GANs) or variational autoencoders (VAEs), to demonstrate the advantages and disadvantages of their approach. This comparison should include both quantitative metrics, such as the Fréchet Inception Distance (FID) or Inception Score (IS), and qualitative analysis of the generated images. Furthermore, the authors should discuss the specific scenarios where their method is expected to outperform other methods and vice versa. This would help to position their work within the broader context of image generation and highlight its unique contributions. A more comprehensive comparison with existing methods is crucial for establishing the significance of the proposed approach.

### Questions

1. How does the proposed method perform on datasets with higher intrinsic dimensionality or more complex structures than the mixture of low-rank Gaussians?

2. What is the computational complexity of the proposed method, and how does it scale with the size of the dataset and the dimensionality of the data?

3. How does the proposed method compare with other state-of-the-art methods for learning image distributions in terms of performance and efficiency?

### Rating

6

### Confidence

3

**********
