### Summary

This paper introduces a new large-scale dataset for 2D and 3D multimodal language models and a new model Omni3D that can reason in both 2D and 3D spaces. The authors also propose a new training framework that leverages chain-of-thought prompting to improve model performance. The paper demonstrates the effectiveness of the proposed approach through extensive experiments on various benchmarks, including 3D grounding and referring expression comprehension tasks. The results show that Omni3D outperforms existing baselines and achieves state-of-the-art performance on several benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise description of the proposed dataset, model architecture, and training framework. The figures and tables are well-organized and informative.
2. The proposed dataset is a valuable contribution to the community. It provides a unified framework for 2D and 3D multimodal reasoning tasks and can facilitate further research in this area.
3. The proposed model, Omni3D, achieves state-of-the-art performance on several benchmarks, demonstrating its effectiveness and generalizability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed approach. It would be helpful to understand the training and inference time of Omni3D compared to existing models.
2. The paper does not provide a detailed analysis of the limitations of the proposed approach. It would be helpful to understand the scenarios where the model may fail or underperform.
3. The paper does not provide a detailed analysis of the impact of different design choices on the performance of the model. It would be helpful to understand the sensitivity of the model to different hyperparameters and architectural choices.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed Omni3D model. Specifically, the authors should provide a breakdown of the training time, including the time spent on each stage (e.g., pre-training, fine-tuning), and the inference time for different input sizes and complexities. This analysis should also include a comparison with the computational costs of existing state-of-the-art models for both 2D and 3D multimodal reasoning. Furthermore, it would be valuable to explore the memory footprint of the model during training and inference, as this is a critical factor for practical deployment. Such an analysis would allow readers to better understand the trade-offs between performance and computational resources, and would facilitate the adoption of the proposed approach in resource-constrained environments.

In addition to computational cost, a more detailed analysis of the model's limitations is needed. The authors should investigate scenarios where the model fails to generalize or underperforms, such as in cases with occluded objects, unusual viewpoints, or complex spatial relationships. This analysis should include a qualitative assessment of the model's predictions, highlighting the types of errors it makes and the underlying reasons for these errors. For example, it would be useful to examine whether the model struggles with specific object categories or spatial configurations. Furthermore, the authors should explore the impact of different types of noise or artifacts in the input data on the model's performance. This would provide a more comprehensive understanding of the model's robustness and its limitations in real-world scenarios. A detailed error analysis would also help identify areas for future improvement.

Finally, the paper should include a more detailed ablation study to assess the impact of different design choices on the model's performance. This should include an analysis of the sensitivity of the model to different hyperparameters, such as learning rate, batch size, and the number of training epochs. The authors should also investigate the impact of different architectural choices, such as the choice of visual encoder, the number of layers in the model, and the specific type of chain-of-thought prompting used. This analysis should include a systematic exploration of the design space, with clear explanations of the rationale behind the design choices. Such an ablation study would provide valuable insights into the model's behavior and would help guide future research in this area.

### Questions

See weaknesses.

### Rating

6

### Confidence

3

**********
