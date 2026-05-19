### Summary

This paper proposes a novel Information-Theoretic Hierarchical Perception (ITHP) model for multimodal learning. The model utilizes the concept of information bottleneck to construct compact latent states for different modalities, enabling a hierarchical fusion of multimodal information. The model is designed to distill relevant information from multiple modalities in a sequential manner, mimicking a hierarchical information processing approach observed in human cognition and neural systems. The authors evaluate the proposed model on three multimodal datasets: MUStARD, MOSI, and MOSEI, focusing on tasks such as sarcasm detection, sentiment analysis, and emotion recognition. The results demonstrate that ITHP achieves competitive performance compared to existing multimodal fusion methods and, in some cases, even surpasses human-level benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-structured and clearly written, making it easy to follow the proposed methodology and experimental results. The authors provide a thorough explanation of the theoretical foundations of the ITHP model, including the formulation of optimization problems and the derivation of loss functions. The use of the information bottleneck principle to construct compact latent states for different modalities is a novel approach that aligns well with the goal of multimodal fusion. The empirical evaluation of ITHP on multiple benchmark datasets demonstrates its effectiveness in various multimodal tasks, including sarcasm detection, sentiment analysis, and emotion recognition. The results show that ITHP achieves competitive performance compared to existing methods and, in some cases, even surpasses human-level benchmarks, highlighting the potential of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

While the paper presents a novel approach to multimodal fusion, it could benefit from a more in-depth discussion of the limitations and potential failure cases of the ITHP model. Specifically, the paper does not explore the sensitivity of the model to different hyperparameter settings, such as the Lagrange multipliers used in the information bottleneck. A more detailed analysis of how these parameters affect the performance of the model would be valuable. Additionally, the paper could provide more insights into the interpretability of the learned latent states. While the authors claim that the latent states capture meaningful information, it would be helpful to provide visualizations or other methods to validate this claim. Finally, the paper could benefit from a more thorough comparison with other state-of-the-art multimodal fusion techniques, including those that do not rely on information bottleneck principles. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach.

### Suggestions

To enhance the paper, the authors should conduct a more rigorous analysis of the ITHP model's sensitivity to hyperparameter settings, particularly the Lagrange multipliers within the information bottleneck. A systematic exploration of how varying these parameters affects the model's performance across different datasets and tasks would provide valuable insights into the robustness of the approach. For instance, the authors could perform a grid search or use an adaptive method to identify optimal Lagrange multipliers for each task, and then report the performance variance across these settings. Furthermore, it would be beneficial to investigate the impact of different initialization strategies for the latent states and how these choices influence the final performance. This analysis should include a discussion of the trade-offs between compression and information retention, and how the model balances these competing objectives. Such an analysis would strengthen the paper by demonstrating a thorough understanding of the model's behavior under different conditions.

In addition to hyperparameter sensitivity, the interpretability of the learned latent states is a crucial aspect that needs further investigation. While the authors claim that these states capture meaningful information, providing concrete examples of how these states relate to the input modalities would be highly beneficial. For example, the authors could visualize the latent states using dimensionality reduction techniques like t-SNE or PCA, and then correlate these visualizations with the input data. Furthermore, they could explore methods to quantify the information content of each latent state, such as mutual information or other information-theoretic measures. This would provide a more rigorous assessment of the interpretability of the model and help to validate the claim that the latent states capture meaningful information. It would also be useful to explore whether the learned latent states are consistent across different tasks and datasets, and if there are any patterns or structures that emerge from the latent space.

Finally, the paper would benefit from a more comprehensive comparison with other state-of-the-art multimodal fusion techniques, including those that do not rely on information bottleneck principles. This comparison should not only focus on performance metrics but also on the computational complexity and resource requirements of each method. For example, the authors could compare the ITHP model with attention-based fusion methods, graph neural networks for multimodal fusion, and other methods that explicitly model inter-modal relationships. This would provide a more complete picture of the strengths and weaknesses of the proposed approach and help to position it within the broader landscape of multimodal learning. The comparison should also include a discussion of the limitations of the proposed approach and potential avenues for future research, such as exploring different architectures for the latent state construction or investigating the use of other information-theoretic measures.

### Questions

1. How does the ITHP model perform when applied to other multimodal tasks beyond sarcasm detection, sentiment analysis, and emotion recognition? Are there specific types of multimodal data or tasks where the model is expected to perform particularly well or poorly?
2. Can the authors provide more insights into the interpretability of the learned latent states? How can we validate that these states capture meaningful information from the input modalities?
3. How sensitive is the ITHP model to the choice of hyperparameters, such as the Lagrange multipliers used in the information bottleneck? Have the authors conducted any ablation studies to assess the impact of these parameters on the model's performance?
4. How does the computational complexity of the ITHP model compare to other state-of-the-art multimodal fusion techniques? Are there any specific computational bottlenecks that need to be addressed for practical applications?

### Rating

6

### Confidence

3

**********
