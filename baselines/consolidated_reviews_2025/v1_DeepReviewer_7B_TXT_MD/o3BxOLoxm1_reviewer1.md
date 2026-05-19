### Summary

This paper proposes a method to guide pretrained diffusion models to generate samples that satisfy certain conditions. The method is "training-free", i.e., it does not require retraining the diffusion model, and it is "low-cost" in the sense that it does not require too many inference steps to produce a sample that satisfies the condition. The method is based on the manifold hypothesis, which states that real data does not lie in a full d-dimensional space, but rather in a lower-dimensional manifold. The proposed method is based on the observation that the noisy data lies in a lower-dimensional manifold, and that the guidance step should be performed on this manifold. The paper proposes two ways of performing the guidance on the manifold: (1) projecting the gradient of the loss function onto the tangent space of the manifold, and (2) using a pre-trained autoencoder to map the data to the manifold. The proposed method is evaluated on several tasks, including super-resolution, deblurring, and style transfer.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The proposed method is interesting and novel. The idea of performing guidance on the manifold is interesting and could be useful for other applications. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

The paper has several weaknesses that I will discuss below.

First, the paper does not provide a clear motivation for why the proposed method is useful. The authors claim that the method is "training-free" and "low-cost", but they do not explain why these properties are important. For example, why would a user want to use the proposed method instead of a standard diffusion model? The paper does not discuss the trade-offs between the proposed method and standard diffusion models. For example, how does the proposed method compare to standard diffusion models in terms of sample quality, diversity, and computational cost? The paper should provide a clear motivation for why the proposed method is useful, and it should discuss the trade-offs between the proposed method and standard diffusion models.

Second, the paper does not provide a clear explanation of how the proposed method works. The paper mentions that the method is based on the manifold hypothesis, but it does not explain what this hypothesis is or how it is used in the proposed method. The paper also does not explain how the gradient of the loss function is projected onto the tangent space of the manifold. The paper should provide a clear explanation of the proposed method, including the mathematical details of how the gradient is projected onto the tangent space.

Third, the paper does not provide a clear explanation of the experimental setup. The paper mentions that the proposed method is evaluated on several tasks, including super-resolution, deblurring, and style transfer. However, the paper does not provide details about the datasets, the evaluation metrics, and the implementation details. The paper should provide a clear explanation of the experimental setup, including the datasets, the evaluation metrics, and the implementation details.

Finally, the paper does not provide a clear explanation of the results. The paper mentions that the proposed method outperforms standard diffusion models in terms of sample quality and computational cost. However, the paper does not provide details about the specific results, such as the quantitative metrics and the qualitative examples. The paper should provide a clear explanation of the results, including the quantitative metrics and the qualitative examples.

### Suggestions

The paper needs to provide a more compelling motivation for the proposed method. The authors should clearly articulate the limitations of existing diffusion models that the proposed method aims to address. For example, are there specific scenarios where standard diffusion models struggle, and how does the proposed method overcome these challenges? The paper should also discuss the trade-offs between the proposed method and standard diffusion models. For example, does the proposed method sacrifice sample quality or diversity for computational efficiency? A thorough comparison of the two approaches, highlighting the specific advantages and disadvantages of each, is necessary to justify the use of the proposed method. Furthermore, the paper should discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameter settings or its applicability to specific types of tasks. Without a clear motivation and a detailed comparison, it is difficult to assess the practical value of the proposed method.

The paper needs to provide a more detailed explanation of the proposed method, including the mathematical details of how the gradient is projected onto the tangent space of the manifold. The paper should clearly define the manifold hypothesis and explain how it is used in the proposed method. The paper should also explain how the projection onto the tangent space is achieved, including the specific mathematical operations involved. A clear and concise explanation of the method is essential for the reader to understand the core contribution of the paper. The paper should also provide a step-by-step explanation of the algorithm, including the input, the output, and the intermediate steps. This would help the reader to understand how the method works in practice.

Finally, the paper needs to provide a more detailed explanation of the experimental setup and the results. The paper should clearly describe the datasets used, the evaluation metrics, and the implementation details. The paper should also provide a clear explanation of the results, including the quantitative metrics and the qualitative examples. The paper should also discuss the statistical significance of the results and the potential sources of variability. The paper should also provide a comparison of the proposed method with other state-of-the-art methods, including standard diffusion models. Without a clear and detailed explanation of the experimental setup and the results, it is difficult to assess the validity and the significance of the proposed method.

### Questions

What are the advantages of the proposed method over standard diffusion models?

How does the proposed method compare to standard diffusion models in terms of sample quality, diversity, and computational cost?

What are the limitations of the proposed method?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
