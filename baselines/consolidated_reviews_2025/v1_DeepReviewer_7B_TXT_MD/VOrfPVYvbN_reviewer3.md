### Summary

The paper proposes a new approach to determine the data domain of a black-box machine learning model. The method uses an image embedding model and a generative model to iteratively refine a textual description of a target class. The approach is evaluated on multiple datasets and compared with a corpus-based method, showing improved performance in identifying the target class.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper proposes a new approach to determine the data domain of a black-box machine learning model. The method uses an image embedding model and a generative model to iteratively refine a textual description of a target class. The approach is evaluated on multiple datasets and compared with a corpus-based method, showing improved performance in identifying the target class.

2. The paper is well-structured and clearly written, making it easy to follow the proposed method and its evaluation.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on three models from the Hugging Face Model Hub. It is not clear how well the proposed method generalizes to other types of models, such as those trained on different datasets or using different architectures.

2. The proposed method is only compared with a corpus-based method. It would be more convincing if the proposed method is also compared with other forensic analysis methods, such as those based on model inversion or gradient-based techniques.

3. The proposed method relies on a large language model (GPT-4) for description summarization and enrichment. The performance of the proposed method may be affected by the quality of the generated descriptions. It is not clear how the performance of the proposed method varies with different large language models.

4. The proposed method is computationally expensive, as it requires generating and evaluating multiple images for each description. It is not clear how the computational cost of the proposed method scales with the size of the dataset or the complexity of the model.

### Suggestions

The paper's evaluation is limited by the narrow selection of models. To strengthen the claims of generalizability, the authors should evaluate their method on a more diverse set of models, including those trained on different datasets (e.g., CIFAR-100, ImageNet subsets) and with different architectures (e.g., ResNets, EfficientNets, Vision Transformers). Furthermore, it would be beneficial to explore models trained with different objectives, such as those trained with adversarial training or reinforcement learning. This would provide a more comprehensive understanding of the method's robustness and limitations. The current evaluation, while showing improvement over a corpus-based baseline, does not fully address the potential for overfitting to the specific characteristics of the three Hugging Face models used.

The comparison with only a corpus-based method is insufficient to establish the superiority of the proposed approach. The authors should compare their method with other forensic analysis techniques, such as model inversion attacks and gradient-based techniques. Model inversion attacks, which aim to reconstruct the input data used to train the model, could provide a valuable baseline for comparison. Gradient-based techniques, which analyze the model's gradients to identify important features, could reveal different aspects of the model's data domain. Including these comparisons would provide a more complete picture of the proposed method's strengths and weaknesses relative to existing techniques. It is important to understand how the proposed method performs against methods that are not explicitly designed for data domain analysis.

The reliance on GPT-4 for description summarization and enrichment introduces a potential source of variability and bias. The authors should investigate how the performance of the proposed method varies with different large language models. It is important to understand whether the method is sensitive to the quality of the generated descriptions or if it can effectively handle less precise or more diverse descriptions. Furthermore, the computational cost of the method is a concern. The authors should provide a more detailed analysis of how the computational cost scales with the size of the dataset and the complexity of the model. This analysis should include a breakdown of the time required for each step of the algorithm, such as image generation, embedding extraction, and description refinement. It is important to understand the practical limitations of the method and how it can be optimized for different scenarios.

### Questions

1. How does the proposed method perform on models trained on different datasets or using different architectures?

2. How does the proposed method compare with other forensic analysis methods?

3. How does the performance of the proposed method vary with different large language models?

4. How does the computational cost of the proposed method scale with the size of the dataset or the complexity of the model?

### Rating

3

### Confidence

4

**********
