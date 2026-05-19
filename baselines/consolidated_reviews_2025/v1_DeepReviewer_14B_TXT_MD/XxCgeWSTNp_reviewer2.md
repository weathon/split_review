### Summary

The paper proposes a novel parametric family of reverse-time Stochastic Differential Equations (SDEs) for Lévy-Itô diffusion models, which improves the quality of generated samples, especially when the number of function evaluations (NFE) is limited. The authors demonstrate the effectiveness of the proposed method on image and speech generation tasks, showing that it outperforms existing methods in terms of sample quality and diversity.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new parametric family of reverse-time SDEs for Lévy-Itô diffusion models, which is a novel contribution to the field of generative modeling.
2. The proposed method is theoretically sound and is supported by rigorous mathematical derivations and proofs.
3. The authors demonstrate the effectiveness of the proposed method on both image and speech generation tasks, showing that it outperforms existing methods in terms of sample quality and diversity.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on image and speech generation tasks, which are continuous domains. It would be interesting to see how the proposed method performs on other types of data, such as discrete data or time-series data.
2. The paper could provide more details on the computational cost of the proposed method compared to existing methods. This would help readers understand the trade-offs between sample quality and computational efficiency.
3. The paper could provide more insights into the choice of the parameter $\eta$ and how it affects the performance of the proposed method. A more detailed analysis of the parameter's impact on sample quality and diversity would be valuable.

### Suggestions

The paper introduces a novel parametric family of reverse-time SDEs for Lévy-Itô diffusion models, which is a promising contribution. However, the evaluation is limited to continuous domains like images and speech. To strengthen the paper, the authors should explore the method's applicability to discrete data, such as text or graphs. This would involve adapting the framework to handle discrete state spaces, potentially using techniques like Gumbel-Softmax or other discrete diffusion approaches. Furthermore, the authors should investigate the performance on time-series data with complex temporal dependencies, which would require careful consideration of the time-axis modeling. Demonstrating the method's versatility across diverse data types would significantly enhance its impact and practical relevance.

Regarding computational cost, the paper should provide a more detailed analysis of the proposed method's efficiency. While the number of function evaluations (NFE) is a relevant metric, it does not fully capture the computational overhead. The authors should report the actual runtime and memory usage of their method compared to existing approaches, including both training and inference times. This analysis should consider different hardware configurations and batch sizes to provide a comprehensive understanding of the computational trade-offs. Furthermore, the authors should discuss the impact of the parameter $\eta$ on computational cost, as different values of $\eta$ might lead to varying levels of computational complexity. A thorough analysis of computational efficiency is crucial for assessing the practical applicability of the proposed method.

Finally, the paper needs a more in-depth analysis of the parameter $\eta$. The current discussion lacks a clear understanding of how different values of $\eta$ affect the generated samples. The authors should provide a detailed ablation study, systematically varying $\eta$ and analyzing its impact on sample quality, diversity, and convergence speed. This analysis should include both quantitative metrics (e.g., FID, IS) and qualitative assessments (e.g., visual inspection of generated samples). Furthermore, the authors should provide insights into how to choose an appropriate value for $\eta$ for different datasets and tasks. A more thorough understanding of the parameter's role is essential for the practical application of the proposed method.

### Questions

1. How does the proposed method perform on other types of data, such as discrete data or time-series data?
2. Can the authors provide more details on the computational cost of the proposed method compared to existing methods?
3. Can the authors provide more insights into the choice of the parameter $\eta$ and how it affects the performance of the proposed method?

### Rating

6

### Confidence

2

**********
