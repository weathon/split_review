### Summary

This paper introduces a novel approach to dataset distillation by incorporating conceptual information from large language models (LLMs) into a diffusion-based generative process. The method, termed CONCORD (CONCept-infORmed Diffusion), aims to enhance the quality and controllability of distilled datasets by explicitly guiding the image generation process with fine-grained concepts relevant to each category. Unlike previous dataset distillation methods that primarily focus on matching the overall distribution of the original data, CONCORD retrieves category-specific concepts from LLMs to inform the denoising process in diffusion models, ensuring that generated images accurately represent essential object details. The paper demonstrates that CONCORD achieves state-of-the-art performance on ImageNet-1K and its subsets, improving both the visual quality and training effectiveness of the distilled datasets. Additionally, the method is shown to be flexible and can be integrated into various diffusion-based pipelines, enhancing its practical applicability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. **Innovative Use of LLMs for Conceptual Guidance**: The integration of LLMs to provide fine-grained, category-specific concepts is a novel approach that significantly enhances the controllability and quality of generated images. This method addresses the limitations of previous dataset distillation techniques, which often lack instance-level control and may produce images with incomplete or inaccurate object details.

2. **Improved Performance and Generalization**: CONCORD achieves state-of-the-art results on ImageNet-1K and its subsets, demonstrating its effectiveness in generating high-quality distilled datasets. The method's ability to maintain performance across different datasets and settings highlights its robustness and generalization capabilities.

3. **Flexibility and Practicality**: The proposed method can be easily integrated into existing diffusion-based generative pipelines, making it a versatile tool for dataset distillation. This flexibility allows researchers and practitioners to apply CONCORD to a wide range of tasks and models without requiring extensive modifications.

4. **Comprehensive Experimental Validation**: The paper provides extensive experimental results, including ablation studies and comparisons with state-of-the-art methods. These experiments thoroughly validate the effectiveness of CONCORD and provide insights into the contributions of each component of the method.

### Weaknesses

#### Some Related Works


#### comment

1. **Computational Overhead**: The method involves an additional computational cost due to the concept-informing process, which is conducted throughout the diffusion denoising process. This might limit its applicability to few-step diffusion techniques, which aim to reduce computational overhead. The paper does not provide a detailed breakdown of the computational cost associated with the concept retrieval and integration steps, making it difficult to assess the practical scalability of the method, especially for large-scale datasets or real-time applications. The reliance on LLMs for concept retrieval could introduce significant latency, and the impact of this on the overall distillation time needs further investigation.

2. **Dependence on CLIP Model for Concept Validity Evaluation**: The method relies on a CLIP model to evaluate the validity of the retrieved concepts by calculating the activation of text descriptions on real images. While CLIP is a powerful model, its performance can be influenced by the specific pre-training data and the nature of the text embeddings. This dependence introduces a potential bottleneck, as the quality of the distilled dataset is directly tied to the CLIP model's ability to accurately capture the semantic relationships between text and images. The paper does not explore the sensitivity of the method to different CLIP models or alternative approaches for concept validity evaluation, which could be a limitation.

3. **Limited Exploration of Negative Concept Selection Strategies**: While the paper proposes a weighted sampling strategy for negative concept selection, it does not thoroughly explore other potential strategies or provide a detailed analysis of their impact on the distillation process. The current approach might not be optimal for all categories, especially those with complex or ambiguous boundaries. A more comprehensive exploration of negative sampling techniques, such as adversarial sampling or curriculum learning, could potentially lead to further improvements in the quality of the distilled datasets.

### Suggestions

To address the computational overhead, the authors should provide a detailed analysis of the time complexity of each step in the CONCORD pipeline, including concept retrieval, concept integration, and the diffusion process. This analysis should include a breakdown of the time spent on LLM queries, CLIP embedding calculations, and the diffusion denoising steps. Furthermore, the authors should explore techniques to reduce the computational cost of concept retrieval, such as caching frequently used concepts or employing more efficient LLM prompting strategies. It would also be beneficial to investigate the trade-off between the number of diffusion steps and the quality of the generated images, as reducing the number of steps could significantly decrease the computational cost, albeit potentially at the expense of image quality. The authors should also consider exploring alternative, less computationally intensive methods for concept integration, such as using lightweight attention mechanisms or feature injection techniques.

To mitigate the dependence on the CLIP model, the authors should explore alternative methods for concept validity evaluation. This could involve using other pre-trained models or developing a custom evaluation metric that is less reliant on a specific model. The authors should also investigate the sensitivity of the method to different CLIP models and provide a comparative analysis of their performance. Furthermore, the authors could explore the possibility of using a ensemble of models for concept validity evaluation, which could potentially improve the robustness and accuracy of the method. It would also be beneficial to investigate the impact of different text prompts on the CLIP embeddings and explore techniques to generate more robust and consistent embeddings.

To improve the negative concept selection strategy, the authors should explore a wider range of sampling techniques, such as adversarial sampling, curriculum learning, or importance sampling. A detailed analysis of the impact of these different strategies on the quality of the distilled datasets should be provided, including a comparison of their computational cost and effectiveness. The authors should also investigate the possibility of dynamically adjusting the negative sampling strategy based on the characteristics of the target category. For example, categories with complex boundaries might benefit from more aggressive negative sampling techniques. Furthermore, the authors could explore the use of hierarchical concept selection, where negative concepts are selected at different levels of abstraction, which could potentially improve the diversity and quality of the generated images.

### Questions

1. **Scalability and Efficiency**: Given the additional computational cost of the concept-informing process, how does CONCORD scale with larger datasets or more complex categories? Are there any strategies to reduce the computational overhead, such as optimizing the concept retrieval or integrating more efficient diffusion techniques?

2. **Concept Validity Evaluation**: How sensitive is the performance of CONCORD to the choice of the CLIP model used for concept validity evaluation? Have the authors explored alternative methods for evaluating concept validity, and if so, how do they compare to the CLIP-based approach?

3. **Negative Concept Selection**: The paper proposes a weighted sampling strategy for negative concept selection. Have the authors explored other sampling strategies, and if so, what were the results? How does the choice of negative concept selection strategy impact the diversity and quality of the generated images?

4. **Generalization to Other Modalities**: While the paper focuses on image datasets, could the CONCORD method be adapted for other data modalities, such as text or audio? What modifications would be necessary to extend the method to these domains?

### Rating

6

### Confidence

4

**********
