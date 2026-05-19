### Summary

This paper investigates the use of Sparse Autoencoders (SAEs) to interpret In-Context Learning (ICL) in large language models. The authors adapt the Sparse Feature Circuits (SFC) methodology to analyze ICL, discovering task-detecting features that enable zero-shot task performance. They apply their approach to the Gemma-1 2B model, providing insights into the mechanisms underlying ICL. The paper contributes to the field of mechanistic interpretability by demonstrating the effectiveness of SAEs in understanding complex model behaviors.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces the Task Vector Cleaning (TVC) algorithm, which addresses the challenge of decomposing task vectors using SAEs. This algorithm is a significant contribution to the field, as it enables the identification of sparse task vectors that are more interpretable and aligned with human understanding.

2. The authors validate the causal relevance of the extracted task features through steering experiments, demonstrating that these features have a substantial impact on task performance. This empirical evidence strengthens the claim that the identified features are indeed meaningful components of the model's decision-making process.

3. The paper adapts the Sparse Feature Circuits (SFC) methodology to analyze ICL, which is a novel application of this technique. The authors also introduce modifications to the SFC approach, such as token position categorization and loss function adjustments, to better handle the complexities of ICL prompts. These modifications enhance the applicability of SFC to a broader range of tasks and models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the Gemma-1 2B model, which may not fully represent the behavior of larger or different types of language models. The scaling properties of SAEs and the SFC methodology with respect to model size and complexity are not thoroughly explored. It is possible that the identified task vectors and circuits might differ significantly in larger models, which could limit the practical applicability of the findings. The analysis lacks a discussion on how the identified features might generalize to models with different architectures or parameter counts, such as larger models with tens or hundreds of billions of parameters, or models with different architectural designs like transformers with varying attention mechanisms.

2. While the paper identifies task-detection features, it does not provide a comprehensive analysis of how these features interact within the model. The causal relationships between different task-detection and task-execution features are not fully explored, and the paper lacks a detailed analysis of how these features contribute to the overall ICL performance. A more thorough investigation of the feature interactions and their impact on task performance would enhance the understanding of the underlying mechanisms. The paper should include visualizations or quantitative analyses of feature activations across different tasks to better understand their interdependencies.

3. The paper's reliance on specific task vectors and SAE parameters might limit the generalizability of the findings. The choice of layer and attention head for feature extraction is not fully justified, and the paper does not explore the sensitivity of the results to different parameter settings. A more detailed analysis of the robustness of the identified features to variations in SAE parameters and task vector extraction methods would strengthen the conclusions. The paper should include ablation studies to assess the impact of different parameter choices on the identified features and their interpretability.

### Suggestions

To address the limitations regarding model-specific findings, the authors should conduct experiments on a wider range of language models, including larger models with different architectures. This would involve adapting the SAE training and SFC analysis to models with varying parameter counts and architectural designs. For example, the authors could explore models with different attention mechanisms or those trained on different datasets. This would provide a more comprehensive understanding of the generalizability of the identified task vectors and circuits. Furthermore, the authors should investigate how the identified features scale with model size, and whether the same types of features are relevant across different model scales. This could involve analyzing the sparsity patterns of the SAEs and the activation patterns of the identified features as the model size increases. Such an analysis would provide valuable insights into the robustness and scalability of the proposed approach.

To enhance the understanding of feature interactions, the authors should conduct a more detailed analysis of the causal relationships between different task-detection and task-execution features. This could involve using techniques such as ablation studies to assess the impact of removing specific features on the overall ICL performance. The authors should also explore the potential for feature interference and how it affects the model's ability to perform different tasks. For example, they could analyze the activation patterns of different features across different tasks to identify which features are most relevant for each task and how they interact with each other. Visualizations of feature activations, such as heatmaps or activation maps, could also be used to better understand the interdependencies between features. This would provide a more comprehensive understanding of the underlying mechanisms of ICL.

To improve the robustness of the findings, the authors should conduct a more thorough analysis of the sensitivity of the results to different SAE parameters and task vector extraction methods. This could involve varying the number of SAE layers, the sparsity level of the SAEs, and the parameters used for feature extraction. The authors should also explore different methods for selecting the task vector, such as using different loss functions or regularization techniques. A detailed analysis of the impact of these variations on the identified features and their interpretability would strengthen the conclusions. Furthermore, the authors should provide a more detailed justification for the choice of layer and attention head for feature extraction, and explore the impact of using different layers and attention heads. This would provide a more robust and reliable analysis of the identified features.

### Questions

1. How do the identified task vectors and task-execution features vary across different layers and attention heads within the Gemma-1 2B model? What is the rationale behind selecting specific layers and attention heads for analysis?

2. The paper primarily focuses on the Gemma-1 2B model. How do you expect the findings to generalize to larger or different types of language models? Have you conducted any preliminary experiments to assess the scalability of your approach?

3. The identified task-detection features are crucial for enabling zero-shot task performance. Can you provide more insights into how these features interact within the model? How do they contribute to the overall ICL performance?

4. The paper mentions that the explanations need to include moving parts aside from task-detection attention output features. Can you elaborate on this point? What specific components are necessary to capture the full effect of in-context learning?

5. How does the computational cost of your approach scale with model size and complexity? Are there any optimizations or techniques that can be used to reduce the computational burden?

### Rating

5

### Confidence

4

**********
