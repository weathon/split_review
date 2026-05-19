### Summary

This paper provides a theoretical framework for understanding why diffusion models can learn high-dimensional data distributions using relatively few samples, avoiding the curse of dimensionality. The authors assume that the underlying data distribution is a mixture of low-rank Gaussians (MoLRG) and parameterize the denoising autoencoder (DAE) in the diffusion model according to the score function of this distribution. They demonstrate that optimizing the training loss of diffusion models under these assumptions is equivalent to solving a subspace clustering problem. This equivalence implies that diffusion models, in this setting, learn the low-dimensional subspaces of the data distribution. The authors further show that the number of samples required to learn the underlying distribution scales linearly with the intrinsic dimensionality of the data, explaining the models' ability to break the curse of dimensionality. They also empirically validate that the learned subspaces correspond to semantic representations of image data, enabling image editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel theoretical perspective on diffusion models by linking them to subspace clustering, offering insights into their effectiveness in learning high-dimensional data.
2. The authors rigorously prove that the sample complexity scales linearly with the intrinsic dimensionality under their assumptions, explaining why diffusion models can avoid the curse of dimensionality.
3. The paper includes extensive experiments on both simulated and real-world datasets to support their theoretical findings and demonstrate practical implications.

### Weaknesses

#### Some Related Works


#### comment

1. The assumption of a mixture of low-rank Gaussians (MoLRG) for the data distribution may be too restrictive for real-world data. While the authors justify this assumption based on empirical observations, it's unclear how the theoretical results would generalize to data distributions that deviate significantly from MoLRG. Specifically, the assumption that each semantic category can be perfectly represented by a low-rank Gaussian is a strong one, and real-world data often exhibits more complex structures, including non-Gaussian clusters and overlapping semantic categories. The paper does not provide a clear analysis of how the performance of the proposed method degrades as the data deviates from the MoLRG assumption, which is a critical consideration for practical applications.
2. The low-rank parameterization of the denoising autoencoder (DAE) might limit the model's capacity to capture complex data structures beyond low-dimensional subspaces. While the authors argue that this parameterization is motivated by the low-rank property of the Jacobian of the DAE, it is not clear if this parameterization is optimal for all types of data. The paper does not explore the trade-off between the low-rank parameterization and the model's ability to capture more complex, non-linear relationships in the data. It is possible that for some datasets, a more flexible parameterization could lead to better performance, even if it does not strictly adhere to the low-rank assumption.

### Suggestions

The paper makes a significant contribution by linking diffusion models to subspace clustering and providing a theoretical framework for understanding their sample efficiency. However, the strong assumptions made about the data distribution and the DAE parameterization limit the practical applicability of the results. To address the limitations of the MoLRG assumption, the authors could explore the robustness of their theoretical results to deviations from this assumption. For example, they could analyze the performance of the proposed method on synthetic datasets with varying degrees of non-Gaussianity or overlapping clusters. This would provide a more comprehensive understanding of the method's limitations and its applicability to real-world data. Furthermore, the authors could investigate alternative parameterizations of the DAE that are less restrictive than the low-rank assumption. For instance, they could explore the use of more flexible neural network architectures that can capture more complex data structures while still maintaining some form of regularization to prevent overfitting. This would allow the method to be applied to a wider range of datasets and potentially improve its performance on complex data.

To further strengthen the paper, the authors should provide a more detailed analysis of the relationship between the learned subspaces and the semantic representations of the data. While the paper demonstrates that the learned subspaces correspond to semantic attributes, it does not provide a clear explanation of why this is the case. A more in-depth analysis of the properties of the learned subspaces and their relationship to the underlying data structure would be beneficial. For example, the authors could investigate the alignment of the learned subspaces with known semantic boundaries in the data or explore the use of interpretability techniques to understand the semantic meaning of the learned representations. This would provide a deeper understanding of the method's ability to capture semantic information and its potential for image editing applications.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and potential directions for future research. While the paper acknowledges the limitations of the MoLRG assumption and the low-rank parameterization, it does not fully explore the implications of these limitations for practical applications. A more thorough discussion of these limitations and potential solutions would be valuable for the readers. For example, the authors could discuss the challenges of applying their method to datasets with more complex semantic structures or explore the use of alternative data representations that are more suitable for diffusion models. This would provide a more balanced perspective on the contributions of the paper and its potential impact on the field.

### Questions

1. How does the performance of the proposed method degrade when the data distribution deviates from the mixture of low-rank Gaussians assumption?
2. Is the low-rank parameterization of the DAE essential for the observed phase transition, or could other parameterizations also achieve similar results?
3. How does the choice of the number of subspaces (K) affect the performance and generalization of the model in practice?
4. Can the proposed method be extended to other types of data beyond images, such as text or audio?

### Rating

6

### Confidence

3

**********
