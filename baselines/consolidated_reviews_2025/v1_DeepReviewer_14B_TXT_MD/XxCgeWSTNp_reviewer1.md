### Summary

The paper proposes a parametric family of sampling SDEs for Lévy-Itô diffusion models by introducing a time-dependent parameter that controls the noise level. The authors show that the marginal probability densities of the forward and reverse processes are identical, ensuring that the sampling SDE accurately reflects the data distribution. Experimental results demonstrate that the proposed sampling SDE improves image generation quality with a small number of function evaluations (NFE).

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The introduction of a noise-controlling parameter in the sampling SDE is a novel contribution. This approach broadens the applicability of Lévy-Itô diffusion models and offers improved sampling quality, particularly when the number of function evaluations is limited.

### Weaknesses

#### Some Related Works


#### comment

The time-dependent parameter $\eta_t$ plays a crucial role in the proposed sampling SDE, but the paper lacks a detailed discussion on the selection of this parameter. The authors should provide more comprehensive guidelines for choosing $\eta_t$, including a discussion on how different choices affect the trade-off between sampling quality and computational cost. While Figure 4 illustrates the impact of $\eta_t$ on FID, it would be beneficial to include a more systematic analysis of how to choose $\eta_t$ for different datasets and model architectures. Additionally, the paper should discuss the sensitivity of the results to the choice of $\eta_t$ and provide recommendations for robust selection strategies. Furthermore, the paper should explore the relationship between the optimal $\eta_t$ and the properties of the Lévy process, such as the stability parameter $\alpha$, and provide insights into how these properties influence the choice of $\eta_t$.

### Suggestions

The paper should include a more detailed analysis of the parameter $\eta_t$, focusing on practical guidelines for its selection. This should go beyond the empirical results shown in Figure 4 and delve into the theoretical underpinnings of how $\eta_t$ affects the sampling process. Specifically, the authors should investigate the relationship between $\eta_t$ and the convergence rate of the reverse SDE, and how this relationship is influenced by the stability parameter $\alpha$ of the Lévy process. A theoretical analysis of the error introduced by different choices of $\eta_t$ would be valuable, potentially leading to a more principled approach for selecting this parameter. For instance, the authors could explore how the choice of $\eta_t$ affects the higher-order moments of the generated samples, and how this relates to the quality of the generated images. This analysis should also consider the computational cost associated with different values of $\eta_t$, providing a clear trade-off between sampling quality and computational efficiency. 

Furthermore, the paper should explore adaptive strategies for selecting $\eta_t$ during the sampling process. Instead of using a fixed $\eta_t$ throughout the reverse SDE, the authors could investigate methods for dynamically adjusting $\eta_t$ based on the current state of the sampling process. This could involve using a feedback mechanism that monitors the convergence of the reverse SDE and adjusts $\eta_t$ accordingly. For example, one could consider using a larger $\eta_t$ in the early stages of the reverse SDE to explore the sample space more broadly, and then gradually decrease $\eta_t$ as the sampling process converges to a stable solution. This adaptive approach could potentially lead to improved sampling quality and efficiency, especially when dealing with complex data distributions. The authors should also consider providing a sensitivity analysis of the results with respect to different choices of $\eta_t$, which would help to understand the robustness of the proposed method.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed method, including a wider range of datasets and model architectures. This would help to assess the generalizability of the proposed approach and its effectiveness in different scenarios. The authors should also compare the performance of the proposed method with other state-of-the-art sampling techniques for Lévy-Itô diffusion models, providing a clear benchmark for the proposed approach. This comparison should not only focus on the final sample quality, but also on the computational cost and convergence rate of the different methods. The experimental evaluation should also include a detailed analysis of the impact of the stability parameter $\alpha$ on the choice of $\eta_t$, providing practical guidelines for selecting this parameter in different scenarios. This would help to make the proposed method more accessible and useful for a wider range of applications.

### Questions

1. How does the choice of $\eta_t$ affect the convergence rate of the reverse SDE?
2. Can the authors provide guidelines for selecting $\eta_t$ based on the properties of the dataset or the desired sampling quality?
3. Are there any theoretical results that justify the choice of $\eta_t$?

### Rating

6

### Confidence

3

**********
