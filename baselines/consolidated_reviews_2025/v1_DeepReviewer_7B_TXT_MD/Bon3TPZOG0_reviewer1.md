### Summary

This paper studies the phase transition of diffusion models in learning image distributions. The authors show that the training loss of diffusion models is equivalent to solving the subspace clustering problem under certain assumptions. This equivalence allows the authors to derive a scaling law for the number of training samples required to learn the underlying distribution. The authors also demonstrate that the subspaces learned by the diffusion model correspond to semantic representations of images.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The authors provide a theoretical analysis of the training process of diffusion models, which is a novel perspective in the field.
- The authors derive a scaling law for the number of training samples required to learn the underlying distribution, which is a valuable contribution to the understanding of diffusion models.
- The authors demonstrate that the subspaces learned by the diffusion model correspond to semantic representations of images, which is an interesting finding.

### Weaknesses

#### Some Related Works


#### comment

 - The assumptions made in the paper, such as the mixture of low-rank Gaussians, may not hold in real-world scenarios. This limits the practical applicability of the theoretical results.
- The paper does not provide a clear explanation of how the derived scaling law can be used to improve the training of diffusion models in practice. The connection between the theoretical findings and practical applications is not well-established.
- The paper lacks a thorough comparison with existing methods for learning image distributions. It is not clear how the proposed approach compares to other state-of-the-art techniques in terms of performance and efficiency.

### Suggestions

The paper's theoretical analysis, while interesting, needs to be more closely tied to practical applications. The authors should provide concrete examples of how the derived scaling law can be used to optimize the training of diffusion models. For instance, can the scaling law be used to determine the optimal number of training samples for a given image resolution or dataset complexity? Can it be used to guide the selection of hyperparameters, such as the learning rate or batch size? Without such practical insights, the theoretical results remain somewhat abstract and difficult to leverage in real-world scenarios. The authors should also consider exploring the limitations of their assumptions more thoroughly. While the mixture of low-rank Gaussians may be a reasonable approximation for some datasets, it is unlikely to hold for all real-world image distributions. A more detailed discussion of the conditions under which the theoretical results are valid, and the potential impact of deviations from these assumptions, would be beneficial.

Furthermore, the paper needs a more comprehensive comparison with existing methods for learning image distributions. The authors should not only compare the performance of their approach with other state-of-the-art techniques but also discuss the computational cost and efficiency of each method. For example, how does the training time and memory usage of the proposed approach compare to that of other diffusion models or alternative generative models? A detailed comparison would help to contextualize the contributions of the paper and highlight its advantages and disadvantages. The authors should also consider including experiments on a wider range of datasets to demonstrate the generalizability of their findings. The current experiments are limited to a few specific datasets, and it is unclear whether the results would hold for other types of images or data distributions. Expanding the experimental evaluation would significantly strengthen the paper's claims.

Finally, the paper should provide a more detailed explanation of the connection between the learned subspaces and semantic representations. While the authors claim that the subspaces correspond to semantic attributes, they do not provide a clear methodology for verifying this claim. How can we quantify the semantic relevance of the learned subspaces? Are there any specific metrics or evaluation methods that can be used to assess the quality of the learned representations? The authors should also discuss the limitations of their approach in terms of semantic understanding. While the learned subspaces may capture some semantic information, it is unlikely that they provide a complete or comprehensive representation of the image content. A more thorough discussion of the limitations and potential future directions would be valuable.

### Questions

- How does the derived scaling law relate to the practical training of diffusion models? Can it be used to optimize the training process in any way?
- How does the proposed approach compare to other state-of-the-art methods for learning image distributions in terms of performance and efficiency?
- Can the authors provide more details on the experimental setup and the datasets used in the paper? Are the results consistent across different datasets and experimental settings?

### Rating

5

### Confidence

2

**********
