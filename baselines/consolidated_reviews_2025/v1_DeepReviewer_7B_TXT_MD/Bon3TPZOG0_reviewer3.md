### Summary

This paper provides a theoretical analysis of diffusion models, showing that they learn the underlying data distribution by solving the subspace clustering problem. The authors prove that the training loss of diffusion models is equivalent to the subspace clustering problem under certain assumptions, and they derive a scaling law for the number of training samples required to learn the underlying distribution. They also demonstrate that the subspaces learned by diffusion models correspond to semantic representations of image data, which can be used to control image generation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical analysis of diffusion models, which is a significant contribution to the understanding of these models.
2. The authors show that the training loss of diffusion models is equivalent to the subspace clustering problem, which provides a new perspective on how diffusion models learn data distributions.
3. The paper derives a scaling law for the number of training samples required to learn the underlying distribution, which can guide the design of diffusion models.
4. The authors demonstrate that the subspaces learned by diffusion models correspond to semantic representations of image data, which can be used to control image generation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the data distribution is a mixture of low-rank Gaussians, which may not hold in real-world scenarios. The assumption of low-rank Gaussians simplifies the analysis but may not accurately reflect the complex, high-dimensional distributions encountered in practice. This could limit the applicability of the theoretical results to real-world datasets where the underlying data structure is likely more complex and less well-defined. The analysis does not address how the theoretical findings might degrade when the data deviates significantly from this assumption.
2. The paper does not provide a clear explanation of how the derived scaling law can be used to improve the training of diffusion models in practice. While the theoretical analysis is valuable, the paper lacks concrete guidance on how to leverage the scaling law to optimize the training process. For example, it is unclear how the derived scaling law can be used to determine the optimal number of training samples or the appropriate network architecture for a given dataset. The paper should provide more practical insights on how to use the theoretical findings to improve the training of diffusion models.
3. The paper does not compare the proposed method with other state-of-the-art methods for learning image distributions. The paper lacks a comparative analysis with existing methods, making it difficult to assess the relative performance and advantages of the proposed approach. Without such comparisons, it is hard to determine whether the proposed method offers any significant improvements over existing techniques. The paper should include a thorough comparison with relevant baselines to demonstrate the effectiveness of the proposed approach.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations imposed by the assumption of a mixture of low-rank Gaussians. The authors should explore the potential impact of this assumption on the applicability of their theoretical results. Specifically, they could investigate how the theoretical findings degrade when the data deviates from this assumption, perhaps by conducting experiments on datasets with more complex structures. Furthermore, the authors could consider exploring alternative data models that might be more suitable for real-world image data, such as models that incorporate spatial dependencies or non-Gaussian components. This would help to broaden the scope of the theoretical analysis and make it more relevant to practical applications. The authors should also provide a more detailed discussion of the conditions under which the derived scaling law is expected to hold, and how these conditions might be violated in practice.

To enhance the practical impact of the paper, the authors should provide more concrete guidance on how to use the derived scaling law to improve the training of diffusion models. This could include specific recommendations on how to determine the optimal number of training samples for a given dataset, or how to choose the appropriate network architecture to achieve the desired performance. The authors could also explore the possibility of using the scaling law to guide the design of new training strategies, such as curriculum learning or adaptive learning rates. Furthermore, the authors should provide a more detailed analysis of the computational cost associated with the proposed approach, and how this cost scales with the size of the dataset and the complexity of the model. This would help practitioners to make informed decisions about the feasibility of using the proposed method for their specific applications.

Finally, the paper needs a more comprehensive comparison with existing methods for learning image distributions. The authors should include a detailed analysis of the performance of their method relative to state-of-the-art techniques, such as GANs or VAEs. This comparison should include both quantitative metrics, such as FID or IS scores, and qualitative analysis of the generated images. The authors should also discuss the advantages and disadvantages of their method compared to these alternatives, and identify the specific scenarios where their method is expected to perform best. This would help to establish the novelty and significance of the proposed approach, and to provide a clear understanding of its strengths and weaknesses.

### Questions

1. Can the authors provide more evidence to support the assumption that the data distribution is a mixture of low-rank Gaussians?
2. Can the authors provide more practical insights on how to use the derived scaling law to improve the training of diffusion models?
3. Can the authors compare the proposed method with other state-of-the-art methods for learning image distributions?

### Rating

6

### Confidence

2

**********
