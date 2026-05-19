### Summary

This paper studies the training loss of diffusion models to investigate when and why diffusion models can learn the underlying distribution without suffering from the curse of dimensionality. Motivated by extensive empirical observations, the authors assume that the underlying data distribution is a mixture of low-rank Gaussians. Specifically, they show that minimizing the training loss is equivalent to solving the subspace clustering problem under proper network parameterization. Based on this equivalence, they further show that the optimal solutions to the training loss can recover the underlying subspaces when the number of samples scales linearly with the intrinsic dimensionality of the data distribution.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a novel perspective on diffusion models by linking them to subspace clustering, which helps explain their ability to learn low-dimensional data distributions.

2. The theoretical analysis is rigorous and well-supported by experimental results on both simulated and real-world datasets. The authors also provide insights into the phase transition behavior of diffusion models.

3. The discovery that the learned subspaces correspond to semantic representations has practical implications for image editing and other applications.

### Weaknesses

#### Some Related Works


#### comment

1. The assumption of MoLRG may be too restrictive for real-world data, which could limit the applicability of the theoretical results. The assumption that data lies on a union of low-dimensional subspaces, while empirically observed in some cases, may not hold for all datasets. The paper does not adequately address the sensitivity of the results to deviations from this assumption, particularly when the underlying data distribution exhibits more complex structures or non-linear relationships. This could significantly impact the practical relevance of the theoretical findings.

2. The low-rank parameterization of the DAE may not be suitable for all types of data or tasks. The paper does not provide a clear justification for why this specific parameterization is optimal or even necessary for the observed phase transition. It is unclear if the low-rank structure is a fundamental property of the data or an artifact of the chosen parameterization. Furthermore, the paper does not explore alternative parameterizations and their impact on the model's performance and generalization capabilities. This lack of exploration limits the understanding of the model's behavior and its potential limitations.

3. The experiments are primarily focused on image data, and it is unclear how well the findings would generalize to other domains. The paper lacks a thorough investigation into the applicability of the proposed method to other types of data, such as time series, audio, or text. The absence of such experiments makes it difficult to assess the broader impact and generalizability of the theoretical results. The paper should include experiments on diverse datasets to demonstrate the robustness and versatility of the proposed approach.

### Suggestions

The paper makes a significant contribution by linking diffusion models to subspace clustering, but there are several areas where the analysis could be strengthened. First, the assumption of a mixture of low-rank Gaussians (MoLRG) needs further justification and exploration. While the authors provide some empirical evidence, a more rigorous analysis of the sensitivity of the results to deviations from this assumption is needed. Specifically, the paper should investigate how the performance of the model degrades when the data distribution exhibits non-Gaussian characteristics or when the subspaces are not perfectly low-rank. It would be beneficial to include experiments with synthetic data that deviate from the MoLRG assumption to quantify the robustness of the theoretical findings. Furthermore, the authors should explore alternative data distributions and discuss the limitations of their approach in such scenarios. This would provide a more comprehensive understanding of the applicability of the proposed method.

Second, the low-rank parameterization of the denoising autoencoder (DAE) requires more detailed justification. The paper should provide a clear explanation of why this specific parameterization is optimal or even necessary for the observed phase transition. It is crucial to investigate whether the low-rank structure is a fundamental property of the data or an artifact of the chosen parameterization. The authors should explore alternative parameterizations and their impact on the model's performance and generalization capabilities. For example, experiments with a more flexible parameterization that does not enforce a low-rank structure could provide valuable insights into the role of the low-rank assumption. This would help to determine whether the observed phase transition is a general phenomenon or specific to the chosen parameterization. The paper should also discuss the potential limitations of the low-rank parameterization and its impact on the model's ability to capture complex data structures.

Finally, the paper should broaden the scope of its experimental evaluation to include other types of data beyond images. The current focus on image data limits the generalizability of the findings. The authors should include experiments on diverse datasets, such as time series, audio, or text, to demonstrate the robustness and versatility of the proposed approach. This would provide a more comprehensive understanding of the applicability of the method to different domains. Furthermore, the paper should investigate the performance of the model on datasets with varying levels of complexity and dimensionality. This would help to identify the limitations of the approach and provide guidance on its applicability to different types of data. The inclusion of such experiments would significantly enhance the impact and practical relevance of the paper.

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
