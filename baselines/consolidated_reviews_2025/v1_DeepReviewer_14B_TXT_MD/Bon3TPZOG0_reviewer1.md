### Summary

This paper studies diffusion models through the lens of subspace clustering, motivated by the observation that real data often lies on low-dimensional subspaces. The authors assume a mixture of low-rank Gaussian (MoLRG) distribution for the data and parameterize the denoising autoencoder (DAE) accordingly. They demonstrate that, under this setup, training diffusion models is equivalent to solving the canonical subspace clustering problem. This connection explains why diffusion models can break the curse of dimensionality and exhibit a phase transition from failure to success in learning distributions as the sample size increases. The authors also find that the discovered subspaces correspond to semantic representations of image data, enabling image editing. Experimental results on both simulated and real-world datasets validate their theoretical findings.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a novel perspective on diffusion models by linking them to subspace clustering, which helps explain their ability to learn low-dimensional data distributions.
2. The theoretical analysis is rigorous and well-supported by experimental results on both simulated and real-world datasets. The authors also provide insights into the phase transition behavior of diffusion models.
3. The discovery that the learned subspaces correspond to semantic representations has practical implications for image editing and other applications.

### Weaknesses

#### Some Related Works


#### comment

1. The assumption of MoLRG may be too restrictive for real-world data, which could limit the applicability of the theoretical results. While the authors argue that MoLRG is a reasonable model, it is unclear how the theoretical guarantees would degrade with deviations from this assumption. Specifically, the analysis relies on the data being exactly represented as a mixture of low-rank Gaussians, and it is not clear how the results would be affected by data distributions that only approximately fit this model. Furthermore, the paper does not explore the sensitivity of the results to the choice of rank in the low-rank Gaussian components, which could be a critical factor in practice.
2. The low-rank parameterization of the DAE may not be suitable for all types of data or tasks. The authors justify this parameterization based on the low-rank property of the Jacobian of the DAE, but it is not clear if this property holds for all types of data and architectures. For example, it is unclear if this parameterization would be effective for data with more complex structures or for tasks that require learning more intricate relationships between data points. The paper also does not provide a detailed analysis of the trade-offs between the low-rank parameterization and the expressive power of the DAE.
3. The experiments are primarily focused on image data, and it is unclear how well the findings would generalize to other domains. The paper does not provide any experimental results on other types of data, such as time series or text data, which could have different characteristics and require different modeling approaches. It is also unclear if the observed phase transition behavior would be consistent across different data modalities.

### Suggestions

The paper makes a compelling theoretical connection between diffusion models and subspace clustering under the assumption of a mixture of low-rank Gaussians (MoLRG) data distribution. However, the practical applicability of these results hinges on the validity of this assumption. To strengthen the paper, it would be beneficial to explore the robustness of the theoretical findings to deviations from the MoLRG assumption. This could involve analyzing the impact of different types of noise or data distributions that only approximately fit the MoLRG model. Furthermore, the paper should investigate the sensitivity of the results to the choice of rank in the low-rank Gaussian components. A more detailed analysis of how the performance of the diffusion model changes with varying ranks would provide valuable insights into the practical limitations of the proposed approach. It would also be useful to explore alternative parameterizations of the DAE that are less restrictive than the low-rank assumption, and compare their performance with the proposed method.

While the paper provides a theoretical analysis of the phase transition behavior of diffusion models, it would be beneficial to provide more practical guidance on how to choose the sample size to ensure successful learning. The current analysis provides a theoretical bound, but it does not offer clear guidelines for practitioners on how to determine the appropriate sample size for a given task. It would be useful to develop a more practical metric or heuristic for determining the sample size based on the characteristics of the data and the desired level of performance. Additionally, the paper should investigate the impact of different training parameters, such as the learning rate and the number of epochs, on the observed phase transition behavior. A more detailed analysis of these factors would provide a more complete understanding of the practical challenges of training diffusion models.

Finally, the paper should broaden the scope of its experimental evaluation to include other data modalities beyond images. This would help to assess the generalizability of the proposed approach and identify potential limitations. For example, it would be interesting to see how the proposed method performs on time series data or text data, which have different characteristics and may require different modeling approaches. It would also be useful to investigate the performance of the method on more complex tasks, such as image generation or text generation, which may require more expressive models. Such experiments would provide a more comprehensive evaluation of the proposed approach and help to identify its strengths and weaknesses.

### Questions

1. How does the choice of the score function parameterization affect the performance of the diffusion model? Are there other parameterizations that could be more effective?
2. How does the performance of the proposed method compare to other subspace clustering algorithms on real-world datasets?
3. How does the sample size required for successful learning scale with the intrinsic dimensionality of the data in practice?
4. Can the proposed method be extended to other types of diffusion models, such as score-based or flow-based models?

### Rating

6

### Confidence

3

**********
