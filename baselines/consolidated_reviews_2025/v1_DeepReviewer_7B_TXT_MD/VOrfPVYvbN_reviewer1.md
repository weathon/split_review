### Summary

This paper proposes a method to perform forensic analysis of a black-box machine learning model. The proposed method uses an image encoder and a generative model to iteratively refine a textual description of a target class, starting from a broad description, until the descriptions that optimizes the objective function (relevance and generality). The proposed method is evaluated on CIFAR-10, Places365, CelebA, and three models from the Hugging Face Model Hub. The proposed method is compared with a corpus-based method and shown to be more effective in identifying the target class.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed method is novel and interesting. It is able to identify fine-grained attributes of a target class that are not present in the corpus-based method.
- The proposed method is evaluated on multiple datasets and compared with a corpus-based method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only evaluated on three models from the Hugging Face Model Hub. It is not clear how well the proposed method generalizes to other types of models, such as those trained on different datasets or using different architectures.
- The proposed method is only compared with a corpus-based method. It would be more convincing if the proposed method is also compared with other forensic analysis methods, such as those based on model inversion or gradient-based techniques.
- The proposed method relies on a large language model (GPT-4) for description summarization and enrichment. The performance of the proposed method may be affected by the quality of the generated descriptions. It is not clear how the performance of the proposed method varies with different large language models.
- The proposed method is computationally expensive, as it requires generating and evaluating multiple images for each description. It is not clear how the computational cost of the proposed method scales with the size of the dataset or the complexity of the model.

### Suggestions

The evaluation of the proposed method should be expanded to include a wider range of models, including those trained on different datasets and using different architectures. This would provide a more comprehensive understanding of the method's generalizability. Specifically, it would be beneficial to evaluate the method on models trained on datasets with different characteristics, such as those with varying levels of noise, complexity, or domain-specific content. Furthermore, the method should be tested on models with different architectural architectures, such as convolutional neural networks, recurrent neural networks, or transformers. This would help to determine if the method is sensitive to the specific architecture of the target model. The evaluation should also include a more detailed analysis of the performance of the method on different classes within each dataset. This would help to identify any potential biases or limitations of the method.

In addition to comparing the proposed method with a corpus-based method, it should also be compared with other forensic analysis methods. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed method. Specifically, it would be beneficial to compare the method with model inversion techniques, which aim to reconstruct the input data that was used to train the model. It would also be useful to compare the method with gradient-based techniques, which aim to identify the features that are most important for the model's predictions. These comparisons should be performed on the same datasets and with the same evaluation metrics to ensure a fair comparison. The comparison should also include an analysis of the computational cost of each method, as well as the quality of the results.

The reliance on a large language model for description summarization and enrichment is a potential weakness of the proposed method. The performance of the method may be affected by the quality of the generated descriptions. It is important to investigate how the performance of the method varies with different large language models. This could be done by comparing the performance of the method when using different models, such as GPT-4, Llama, or other open-source models. The analysis should also include an investigation of the impact of the length and quality of the generated descriptions on the performance of the method. Furthermore, it would be beneficial to explore methods for automatically generating descriptions that are tailored to the specific target class, rather than relying on a general-purpose large language model.

### Questions

- How does the proposed method perform on models trained on different datasets or using different architectures?
- How does the proposed method compare with other forensic analysis methods?
- How does the performance of the proposed method vary with different large language models?
- How does the computational cost of the proposed method scale with the size of the dataset or the complexity of the model?

### Rating

3

### Confidence

4

**********
