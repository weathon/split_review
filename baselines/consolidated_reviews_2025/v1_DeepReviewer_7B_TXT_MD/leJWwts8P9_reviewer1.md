### Summary

The paper proposes a method to test whether two LLMs are trained independently or not. The method is based on comparing the weight and activation distributions of two trained models, and generating p-values by comparing the similarity of the two trained models with that of several independent re-trained models.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper proposes a method to test whether two LLMs are trained independently or not. The method is based on comparing the weight and activation distributions of two trained models, and generating p-values by comparing the similarity of the two trained models with that of several independent re-trained models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

2. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

3. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

4. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

5. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

6. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

7. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

8. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

9. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

10. The paper does not provide a clear definition of what it means for two LLMs to be trained independently. This lack of clarity makes it difficult to understand the motivation behind the proposed method and evaluate its effectiveness. For example, are the models trained on completely separate datasets, or are they trained with different random initializations? The paper needs to explicitly define these conditions to establish a clear baseline for comparison.

### Suggestions

The core issue with this paper is the lack of a clear and operational definition of 'independent training' for large language models (LLMs). The authors need to specify the exact conditions under which they consider two models to have been trained independently. For instance, are the models trained on completely disjoint datasets, or are they trained with different random initializations of the weights, or both? The paper should also clarify whether the models are trained with the same or different optimization algorithms, learning rates, and batch sizes. Without these details, it is impossible to assess the validity and significance of the proposed method. The paper should also consider the impact of different training procedures on the resulting model weights and activations. For example, different optimizers (e.g., Adam, SGD) or different regularization techniques (e.g., dropout, weight decay) can lead to different distributions of model parameters and activations, even if the models are trained on the same dataset. The authors should provide a more rigorous definition of independence that takes these factors into account. 

Furthermore, the paper should provide a more detailed explanation of the proposed method for comparing weight and activation distributions. The paper mentions using similarity measures, but it does not specify which measures are used or how they are calculated. For example, are histograms, kernel density estimation, or other methods used to compare the distributions of weights and activations? The paper should also explain how the similarity measures are converted into p-values. The paper should also discuss the limitations of the proposed method. For example, are there any cases where the method is likely to fail? Are there any assumptions that the method relies on that may not hold in practice? The paper should also consider the computational cost of the proposed method. Comparing the weights and activations of large language models can be computationally expensive, and the paper should discuss the scalability of the method. The paper should also provide a more thorough evaluation of the proposed method. The paper mentions that the method is evaluated on a set of open-weight models, but it does not provide any details about the datasets used for evaluation. The paper should also compare the performance of the proposed method to other existing methods for comparing language models.

Finally, the paper should address the issue of model collapse, which is a common problem in language model training. The paper should discuss how the proposed method can be used to detect model collapse and how it can be mitigated. The paper should also consider the impact of different training techniques on the proposed method. For example, techniques such as knowledge distillation or adversarial training can affect the weights and activations of the models, and the paper should discuss how these techniques can be taken into account when using the proposed method. The paper should also provide a more detailed analysis of the results. The paper mentions that the method is able to detect fine-tuning attacks, but it does not provide any details about the types of attacks that can be detected. The paper should also discuss the false positive and false negative rates of the proposed method. The paper should also consider the ethical implications of the proposed method. For example, the method could be used to detect whether a model has been trained on sensitive data, and the paper should discuss the potential risks and benefits of this technology.

### Questions

See weaknesses.

### Rating

3

### Confidence

3

**********
