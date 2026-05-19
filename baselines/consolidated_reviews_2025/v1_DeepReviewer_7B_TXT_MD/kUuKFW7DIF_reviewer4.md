### Summary

The paper introduces a multi-resolution HuBERT model, which processes speech at multiple resolutions simultaneously to improve the quality of speech representations. The model employs a hierarchical transformer architecture and masked unit prediction objectives across multiple resolutions, achieving performance gains over the original HuBERT model on various speech tasks, including speech recognition and the SUPERB benchmark evaluations. The authors also provide a detailed analysis of the computational efficiency of the proposed model, highlighting a 9-13% reduction in computational complexity compared to the original HuBERT model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its implications.
2. The authors provide a thorough comparison of MR-HuBERT with the original HuBERT model, demonstrating the performance improvements achieved by the proposed approach across various speech tasks.
3. The paper includes a detailed analysis of the computational efficiency of MR-HuBERT, highlighting its potential for practical applications in resource-constrained environments.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed MR-HuBERT model. While the authors mention a reduction in computational complexity, they do not provide a thorough comparison with the original HuBERT model in terms of training time, inference time, and memory usage. Specifically, the paper should include a breakdown of the computational cost associated with each component of the model (e.g., the 20ms and 40ms resolution encoders, the hierarchical transformer, and the masked unit prediction layers). This analysis should also consider the impact of different batch sizes and sequence lengths on the computational efficiency.
2. The paper does not provide a detailed comparison of the learned representations between the single-resolution and multi-resolution models. While the authors demonstrate performance improvements on downstream tasks, they do not analyze the properties of the learned representations, such as their disentanglement, robustness, and generalization capabilities. For example, the paper could include visualizations of the representation space, such as t-SNE plots, to illustrate the differences between the representations learned by the single-resolution and multi-resolution models. Additionally, the authors could evaluate the performance of the learned representations on out-of-distribution tasks or noisy data to assess their robustness.
3. The paper does not explore the limitations of the proposed approach in detail. For example, the authors do not discuss the potential challenges of applying MR-HuBERT to different speech domains, such as low-resource languages or noisy environments. The paper should also address the sensitivity of the model to hyperparameter settings and the potential for overfitting. Furthermore, the authors should discuss the scalability of the approach to larger datasets and more complex tasks.

### Suggestions

To strengthen the paper, the authors should provide a more granular analysis of the computational costs associated with each component of the MR-HuBERT model. This should include a detailed breakdown of the training and inference times for the 20ms and 40ms resolution encoders, the hierarchical transformer, and the masked unit prediction layers. Furthermore, the analysis should consider the impact of different batch sizes and sequence lengths on the computational efficiency. For instance, the authors could present a table showing the training time per epoch, inference time per sample, and peak memory usage for different batch sizes and sequence lengths. This would provide a more comprehensive understanding of the computational trade-offs involved in using the multi-resolution approach. Additionally, the authors should discuss the potential for optimizing the model for different hardware platforms, such as GPUs or TPUs, to further improve its efficiency.

To address the lack of analysis on learned representations, the authors should include visualizations of the representation space, such as t-SNE plots, to illustrate the differences between the representations learned by the single-resolution and multi-resolution models. This would help to understand whether the multi-resolution approach leads to more disentangled or robust representations. Furthermore, the authors should evaluate the performance of the learned representations on out-of-distribution tasks or noisy data to assess their generalization capabilities. For example, they could test the model on speech data with background noise or on speech from different accents or dialects. This would provide a more comprehensive understanding of the strengths and limitations of the proposed approach. The authors should also consider using quantitative metrics to evaluate the quality of the learned representations, such as measures of disentanglement or robustness.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed approach. This should include an analysis of the potential challenges of applying MR-HuBERT to different speech domains, such as low-resource languages or noisy environments. The authors should also address the sensitivity of the model to hyperparameter settings and the potential for overfitting. For example, they could investigate the impact of different learning rates, batch sizes, and regularization techniques on the model's performance. Furthermore, the authors should discuss the scalability of the approach to larger datasets and more complex tasks. This should include an analysis of the computational cost of training the model on larger datasets and the potential for using distributed training techniques to improve its scalability. Addressing these limitations would provide a more balanced and comprehensive evaluation of the proposed approach.

### Questions

1. Could you provide a more detailed analysis of the computational complexity and efficiency of the proposed MR-HuBERT model compared to the original HuBERT model? Specifically, how does the multi-resolution processing affect the training time, inference time, and memory usage?
2. Could you provide a more detailed comparison of the learned representations between the single-resolution and multi-resolution models? For example, do the multi-resolution representations exhibit better disentanglement, robustness, or generalization capabilities?
3. What are the potential limitations of the proposed approach in different speech domains, such as low-resource languages or noisy environments? How sensitive is the model to hyperparameter settings, and what measures can be taken to prevent overfitting?

### Rating

6

### Confidence

3

**********
