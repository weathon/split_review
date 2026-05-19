### Summary

This paper proposes a multi-resolution approach to self-supervised learning for speech, aiming to improve the quality of speech representations by processing speech at multiple resolutions simultaneously. The authors build upon the HuBERT architecture, incorporating a hierarchical transformer to handle both 20ms and 40ms resolutions. The model employs a combination of masked unit prediction objectives across these resolutions. Experimental results demonstrate that the proposed multi-resolution HuBERT (MR-HuBERT) model achieves performance improvements over the original HuBERT on various speech tasks, including speech recognition and SUPERB benchmark evaluations.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written, with clear explanations of the proposed method and experimental setup. The authors effectively communicate the motivation behind their approach and the rationale for using multi-resolution processing.
2. The experimental results are comprehensive, covering a range of tasks and datasets. The authors provide detailed comparisons with the original HuBERT model, demonstrating the performance gains achieved by MR-HuBERT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed MR-HuBERT model. While the authors mention a reduction in computational complexity, they do not provide a thorough comparison with the original HuBERT model in terms of training time, inference time, and memory usage. Specifically, the paper should include a breakdown of the computational cost associated with each component of the model (e.g., the 20ms and 40ms resolution encoders, the hierarchical transformer, and the masked unit prediction layers). This analysis should also consider the impact of different batch sizes and sequence lengths on the computational efficiency.
2. The paper does not provide a detailed comparison of the learned representations between the single-resolution and multi-resolution models. While the authors demonstrate performance improvements on downstream tasks, they do not analyze the properties of the learned representations, such as their disentanglement, robustness, and generalization capabilities. For example, the paper could include visualizations of the representation space, such as t-SNE plots, to illustrate the differences between the representations learned by the single-resolution and multi-resolution models. Additionally, the authors could evaluate the performance of the learned representations on out-of-distribution tasks or noisy data to assess their robustness.
3. The paper does not explore the limitations of the proposed approach in detail. For example, the authors do not discuss the potential challenges of applying MR-HuBERT to different speech domains, such as low-resource languages or noisy environments. The paper should also address the sensitivity of the model to hyperparameter settings and the potential for overfitting. Furthermore, the authors should discuss the scalability of the approach to larger datasets and more complex tasks.

### Suggestions

The paper would benefit from a more thorough analysis of the computational aspects of the proposed MR-HuBERT model. While the authors mention a reduction in computational complexity, a detailed breakdown of the computational cost associated with each component of the model is needed. This should include a comparison of training time, inference time, and memory usage between the MR-HuBERT model and the original HuBERT model. The analysis should also consider the impact of different batch sizes and sequence lengths on the computational efficiency. For example, the authors could provide a table showing the training time per epoch, inference time per sample, and peak memory usage for different batch sizes and sequence lengths. This would provide a more comprehensive understanding of the computational trade-offs involved in using the multi-resolution approach. Furthermore, the authors should discuss the potential for optimizing the model for different hardware platforms, such as GPUs or TPUs, to further improve its efficiency.

To strengthen the analysis of the learned representations, the authors should include a more detailed comparison between the single-resolution and multi-resolution models. This should go beyond simply demonstrating performance improvements on downstream tasks and delve into the properties of the learned representations. For example, the authors could include visualizations of the representation space, such as t-SNE plots, to illustrate the differences between the representations learned by the two models. This would help to understand whether the multi-resolution approach leads to more disentangled or robust representations. Additionally, the authors should evaluate the performance of the learned representations on out-of-distribution tasks or noisy data to assess their generalization capabilities. This could involve testing the model on speech data with background noise or on speech from different accents or dialects. Such an analysis would provide a more comprehensive understanding of the strengths and limitations of the proposed approach.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. The authors should discuss the potential challenges of applying MR-HuBERT to different speech domains, such as low-resource languages or noisy environments. This should include an analysis of the model's performance on languages with different acoustic characteristics or in environments with varying levels of noise. The authors should also address the sensitivity of the model to hyperparameter settings and the potential for overfitting. For example, they could investigate the impact of different learning rates, batch sizes, and regularization techniques on the model's performance. Furthermore, the authors should discuss the scalability of the approach to larger datasets and more complex tasks. This should include an analysis of the computational cost of training the model on larger datasets and the potential for using distributed training techniques to improve its scalability. Addressing these limitations would provide a more balanced and comprehensive evaluation of the proposed approach.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

3

**********
