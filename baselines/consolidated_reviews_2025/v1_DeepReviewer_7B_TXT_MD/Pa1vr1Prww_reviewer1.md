### Summary

The paper explores the use of Sparse Autoencoders (SAEs) to interpret In-Context Learning (ICL) in large language models. The authors identify task vectors and task-execution features within the model's activations, aiming to provide a clearer understanding of the mechanisms underlying ICL. They adapt the Sparse Feature Circuits (SFC) methodology to analyze these features and discover task-detecting components that enable zero-shot task performance. The study focuses on the Gemma-1 2B model, demonstrating the potential of SAEs in enhancing interpretability research for larger models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach by combining SAEs with Sparse Feature Circuits (SFC) to analyze In-Context Learning (ICL) in large language models, which is a creative and innovative contribution to the field of mechanistic interpretability.

2. The authors successfully identify and decompose task vectors into sparse features, providing a deeper understanding of the mechanisms that enable ICL. This decomposition allows for a more granular analysis of how models handle different tasks.

3. The paper demonstrates the effectiveness of task-detection features in enabling zero-shot task performance, which is a significant finding that advances our understanding of how models generalize to unseen tasks.

4. By adapting the SFC methodology to the more complex ICL setting, the authors provide a valuable extension to existing interpretability tools, making it possible to analyze the intricate circuits involved in ICL.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of SAEs in identifying task vectors and task-execution features, the complexity of the Gemma-1 2B model may limit the generalizability of the findings to other model architectures. The specific layer and attention head selection process is not fully justified, and it is unclear how these choices might influence the identified features. A more detailed analysis of the sensitivity of the results to different layer and attention head combinations would be beneficial.

2. The paper primarily focuses on the Gemma-1 2B model, which may not fully represent the behavior of larger or different types of language models. The scaling properties of SAEs and the SFC methodology with respect to model size and complexity are not thoroughly explored. It is possible that the identified task vectors and circuits might differ significantly in larger models, which could limit the practical applicability of the findings. The paper should include a discussion on the potential limitations of applying these methods to models with different architectures or sizes.

3. Although the paper identifies task-detection features, it does not provide a comprehensive analysis of how these features interact within the model. The causal relationships between different task-detection and task-execution features are not fully explored, and the paper lacks a detailed analysis of how these features contribute to the overall ICL performance. A more thorough investigation of the feature interactions and their impact on task performance would enhance the understanding of the underlying mechanisms.

### Suggestions

To address the limitations regarding model-specific findings, the authors should conduct a more rigorous analysis of the sensitivity of their results to different layer and attention head combinations within the Gemma-1 2B model. This could involve systematically varying the selected layers and attention heads and observing how the identified task vectors and circuits change. Furthermore, the authors should explore the scaling properties of their methods by applying them to larger models, even if it is computationally challenging. This would provide a better understanding of the generalizability of their findings and the potential limitations of their approach. The analysis should also include a discussion on the potential impact of different model architectures on the identified features. For example, it would be beneficial to investigate whether the identified task vectors and circuits are specific to the Gemma-1 2B architecture or if they are more generalizable across different model families.

To enhance the understanding of feature interactions, the authors should conduct a more detailed analysis of the causal relationships between different task-detection and task-execution features. This could involve using techniques such as ablation studies to assess the impact of removing specific features on the overall ICL performance. The authors should also explore the potential for feature interference and how it affects the model's ability to perform different tasks. A more thorough investigation of the feature interactions and their impact on task performance would enhance the understanding of the underlying mechanisms. This could involve visualizing the feature activations and their relationships using techniques such as dimensionality reduction. The authors should also consider using causal inference methods to identify the causal relationships between features and task performance.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and the potential directions for future research. This should include a discussion of the computational challenges associated with applying their methods to larger models and the potential impact of different model architectures on the identified features. The authors should also discuss the potential for using their findings to improve the design of language models and to develop more effective methods for in-context learning. This discussion should also include a consideration of the ethical implications of their work, such as the potential for misuse of their findings to develop models that are less transparent and more difficult to control.

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
