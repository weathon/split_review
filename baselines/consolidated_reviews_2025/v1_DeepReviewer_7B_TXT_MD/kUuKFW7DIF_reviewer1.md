### Summary

This paper proposes a multi-resolution approach to self-supervised learning for speech, aiming to improve the quality of speech representations by processing speech at multiple resolutions simultaneously. The authors build upon the HuBERT architecture, incorporating a hierarchical transformer to handle both 20ms and 40ms resolutions. The model employs a combination of masked unit prediction objectives across these resolutions. Experimental results demonstrate that the proposed multi-resolution HuBERT (MR-HuBERT) model achieves performance improvements over the original HuBERT on various speech tasks, including speech recognition and SUPERB benchmark evaluations.

### Soundness

2

### Presentation

2

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

To address the lack of detailed computational analysis, the authors should provide a more granular breakdown of the computational costs associated with each component of the MR-HuBERT model. This should include a comparison of training and inference times, as well as memory usage, between the MR-HuBERT model and the original HuBERT model. The analysis should also consider the impact of different batch sizes and sequence lengths on the computational efficiency. For example, the authors could present a table showing the training time per epoch, inference time per sample, and peak memory usage for different batch sizes and sequence lengths. Furthermore, the authors should provide a more detailed explanation of how the multi-resolution processing affects the computational cost, including the overhead associated with the hierarchical transformer and the masked unit prediction layers. This analysis should also consider the potential for parallelization and optimization of the model for different hardware platforms.

To better understand the properties of the learned representations, the authors should include a more detailed comparison between the single-resolution and multi-resolution models. This should include visualizations of the representation space, such as t-SNE plots, to illustrate the differences between the representations learned by the two models. The authors should also evaluate the performance of the learned representations on out-of-distribution tasks or noisy data to assess their robustness. For example, the authors could evaluate the performance of the models on speech data with background noise or on speech from different accents or dialects. Additionally, the authors should analyze the disentanglement properties of the learned representations, such as whether they capture different aspects of the speech signal, such as phonetic and semantic information. This analysis should also consider the potential for using the learned representations for other downstream tasks, such as speech generation or speech editing.

To address the limitations of the proposed approach, the authors should discuss the potential challenges of applying MR-HuBERT to different speech domains, such as low-resource languages or noisy environments. The paper should also address the sensitivity of the model to hyperparameter settings and the potential for overfitting. For example, the authors could investigate the impact of different learning rates, batch sizes, and regularization techniques on the performance of the model. Furthermore, the authors should discuss the scalability of the approach to larger datasets and more complex tasks. This should include an analysis of the computational cost of training the model on larger datasets and the potential for using distributed training techniques to improve the scalability of the approach. The authors should also discuss the potential for using the proposed approach for other speech-related tasks, such as speech translation or speech summarization.

### Questions

1. How does the multi-resolution processing affect the computational complexity and efficiency of the MR-HuBERT model compared to the original HuBERT model? Could you provide a detailed analysis of the training time, inference time, and memory usage for both models?
2. What are the properties of the learned representations in the MR-HuBERT model compared to the single-resolution HuBERT model? Could you provide visualizations or other analyses to demonstrate the differences in the learned representations?
3. What are the limitations of the proposed approach in different speech domains, such as low-resource languages or noisy environments? How sensitive is the model to hyperparameter settings, and what measures can be taken to prevent overfitting?

### Rating

5

### Confidence

4

**********
