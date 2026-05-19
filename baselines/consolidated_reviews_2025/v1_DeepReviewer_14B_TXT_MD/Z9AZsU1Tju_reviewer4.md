### Summary

This paper introduces a novel multimodal learning approach inspired by neuroscience, called Information-Theoretic Hierarchical Perception (ITHP). The ITHP model leverages the information bottleneck principle to create compact and informative latent states for downstream tasks. The model designates a prime modality and treats other modalities as detectors in the information pathway, aiming to distill the most valuable information from multimodal data while minimizing redundancy. The authors demonstrate the effectiveness of ITHP on sarcasm detection and sentiment analysis tasks, showing that it outperforms state-of-the-art benchmarks and even surpasses human-level performance in certain metrics on the CMU-MOSI dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to multimodal learning by integrating insights from neuroscience and applying the information bottleneck principle in a hierarchical manner. This is a unique perspective compared to traditional fusion models.
2. The authors provide a thorough experimental evaluation of the ITHP model on multiple datasets, including MUStARD, CMU-MOSI, and CMU-MOSEI. The results demonstrate that the model consistently outperforms state-of-the-art benchmarks across various evaluation metrics.
3. The paper is well-structured and clearly explains the methodology, experiments, and results. The use of figures and tables effectively supports the textual content.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the limitations of the ITHP model and potential areas for future research. Specifically, the current discussion lacks a rigorous analysis of scenarios where the model might underperform, such as when dealing with highly asynchronous modalities or when the prime modality is significantly less informative than the others. A deeper exploration of the model's sensitivity to the quality and relevance of the prime modality is needed.
2. The authors should provide more insights into the computational complexity of the ITHP model and how it scales with an increasing number of modalities. The paper lacks a detailed analysis of the time and memory requirements of the model, particularly concerning the training process. It would be beneficial to understand how the model's performance and resource consumption change as the number of modalities increases, and whether there are any practical limits to the number of modalities that can be effectively used.

### Suggestions

The paper should include a more thorough investigation into the selection of the prime modality. While the authors mention that prior knowledge is used, they should also explore the impact of different prime modality choices on the model's performance. For example, an ablation study could be conducted where each modality is treated as the prime modality in turn, and the resulting performance is analyzed. This would provide a better understanding of the model's sensitivity to the choice of prime modality and help identify scenarios where a particular modality is more suitable as the prime. Furthermore, the authors should discuss strategies for automatically selecting the prime modality when prior knowledge is not available or when the relevance of modalities is unclear. This could involve techniques such as mutual information analysis or feature importance ranking to determine the most informative modality for a given task.

To address the computational complexity concerns, the authors should provide a detailed analysis of the model's time and memory requirements, including the training and inference phases. This analysis should consider the impact of the number of modalities, the dimensionality of the input features, and the size of the latent space. The authors should also discuss potential strategies for optimizing the model's performance, such as using more efficient neural network architectures or employing techniques like model pruning or quantization. Furthermore, it would be beneficial to explore the scalability of the model to a larger number of modalities, and to identify any practical limitations in terms of computational resources. The authors should also consider the trade-off between model performance and computational cost, and provide guidance on how to choose an appropriate model configuration for different application scenarios.

Finally, the paper should include a more detailed discussion of the model's limitations and potential failure modes. This should include an analysis of scenarios where the model might underperform, such as when dealing with highly asynchronous modalities or when the prime modality is significantly less informative than the others. The authors should also discuss the model's sensitivity to noise and outliers in the input data, and explore techniques for improving the model's robustness. A more thorough analysis of these limitations would provide a more complete picture of the model's capabilities and help guide future research in this area.

### Questions

1. How does the model handle scenarios where the modalities are highly asynchronous or when there is a significant difference in the quality or relevance of the modalities?
2. Can the authors provide more insights into the computational complexity of the ITHP model and how it scales with an increasing number of modalities?
3. Are there any plans to extend the ITHP model to handle a larger number of modalities, and what are the potential challenges in doing so?

### Rating

6

### Confidence

3

**********
