### Summary

This paper presents an approach to determine the data domain of a black-box machine learning model, which is important for forensic investigations. The proposed method uses an image embedding model and a generative model to iteratively refine a textual description of a target class. The method is evaluated on several datasets and models, and it is shown to be more effective than a corpus-based approach in identifying the target class.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is novel and interesting. It is able to identify fine-grained attributes of a target class that are not present in the corpus-based method.
2. The proposed method is evaluated on multiple datasets and compared with a corpus-based method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on three models from the Hugging Face Model Hub. It is not clear how well the proposed method generalizes to other types of models, such as those trained on different datasets or using different architectures.
2. The proposed method is only compared with a corpus-based method. It would be more convincing if the proposed method is also compared with other forensic analysis methods, such as those based on model inversion or gradient-based techniques.
3. The proposed method relies on a large language model (GPT-4) for description summarization and enrichment. The performance of the proposed method may be affected by the quality of the generated descriptions. It is not clear how the performance of the proposed method varies with different large language models.
4. The proposed method is computationally expensive, as it requires generating and evaluating multiple images for each description. It is not clear how the computational cost of the proposed method scales with the size of the dataset or the complexity of the model.

### Suggestions

The paper would benefit from a more thorough evaluation of the proposed method's generalizability. While the authors evaluate on a few models from the Hugging Face Hub, these models may share similar architectures and training procedures, limiting the conclusions about the method's broader applicability. To address this, the authors should consider evaluating on a more diverse set of models, including those trained on different datasets, using different architectures (e.g., CNNs, RNNs, transformers), and with varying levels of complexity. This would provide a more robust assessment of the method's performance and its ability to handle diverse model types. Furthermore, it would be beneficial to analyze the performance of the method on models with different training objectives, such as those trained with adversarial training or reinforcement learning, to understand its limitations and potential biases.

In addition to comparing with a corpus-based method, the authors should also compare their method with other forensic analysis techniques. Model inversion techniques, which aim to reconstruct the input data that was used to train the model, could provide a valuable baseline for comparison. Similarly, gradient-based techniques, which analyze the model's gradients to identify important features, could reveal different aspects of the model's data domain. Comparing the proposed method with these techniques would provide a more comprehensive understanding of its strengths and weaknesses. The authors should also consider comparing with methods that use different types of generative models, such as GANs or VAEs, to assess the impact of the generative model choice on the overall performance. This would help to isolate the contribution of the proposed iterative refinement approach from the specific choice of generative model.

Finally, the paper should address the computational cost of the proposed method more thoroughly. While the authors mention that the method is computationally expensive, they do not provide a detailed analysis of how the computational cost scales with the size of the dataset or the complexity of the model. The authors should provide a more detailed breakdown of the computational cost, including the time required for each step of the algorithm, such as image generation, embedding extraction, and description refinement. They should also explore potential optimizations to reduce the computational cost, such as using more efficient generative models or employing parallel processing techniques. Furthermore, the authors should investigate the impact of the number of iterations on the performance of the method and provide guidelines for selecting an appropriate number of iterations for different datasets and models.

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
