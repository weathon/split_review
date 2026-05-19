### Summary

The paper proposes a novel method for explaining predictions made by a trained model. The method is based on the Kernelized Stein Discrepancy (KSD) and aims to identify training samples that provide the best predictive support to a test point. The authors demonstrate the effectiveness of their method through extensive experiments on multiple classification tasks, showing improvements in precision, consistency, and computational efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to explaining predictions using KSD, which is a significant contribution to the field of explainable AI.

2. The authors provide a thorough experimental evaluation of their method, demonstrating its effectiveness across various classification tasks.

3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its advantages over existing approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential future research directions.

2. The authors should provide more insights into the practical implications of their method and how it can be used in real-world applications.

3. The paper could include a more comprehensive comparison with other state-of-the-art explanation methods to further demonstrate the superiority of the proposed approach.

### Suggestions

The paper would be strengthened by a more thorough discussion of the limitations of the proposed method. Specifically, the authors should address the sensitivity of the Kernelized Stein Discrepancy (KSD) to the choice of kernel and its parameters. While the paper mentions the use of a Gaussian kernel, a more detailed analysis of how different kernel choices and bandwidth parameters affect the explanation results is needed. For example, how does the method perform with kernels that are less sensitive to high-frequency features, and what are the trade-offs between computational cost and explanation quality when using different kernels? Furthermore, the authors should discuss the computational complexity of the KSD calculation, especially in relation to the size of the training dataset. This is crucial for understanding the scalability of the method to large datasets. A discussion of potential approximation techniques or optimizations to mitigate the computational burden would be beneficial. Finally, the authors should explore the limitations of the method in scenarios where the data distribution is highly complex or multimodal, and how this might affect the quality of the explanations.

To enhance the practical impact of the work, the authors should provide more concrete examples of how their method can be used in real-world applications. For instance, in medical diagnosis, how can the identified training samples be used to provide insights into the model's decision-making process? Can these samples be used to identify potential biases in the training data or to highlight areas where the model may be underperforming? The authors should also discuss how their method can be integrated into existing machine learning workflows and tools. This would involve addressing practical challenges such as the selection of appropriate hyperparameters and the interpretation of the identified training samples. Furthermore, the authors should explore the potential of using their method for model debugging and improvement, such as identifying mislabeled or noisy training samples that may be negatively impacting model performance. A more detailed discussion of these practical aspects would significantly increase the value of the paper.

Finally, the paper would benefit from a more comprehensive comparison with other state-of-the-art explanation methods. While the paper compares against some existing methods, a more detailed analysis of the strengths and weaknesses of each method is needed. For example, how does the proposed method compare to methods based on gradient-based attribution or perturbation-based techniques? The authors should also consider comparing their method with other example-based explanation methods, such as those based on counterfactual reasoning or prototype learning. A more thorough comparison should include a quantitative analysis of the explanation quality, such as the fidelity of the explanations to the model's predictions, as well as a qualitative analysis of the interpretability of the explanations. This would provide a more complete picture of the advantages and disadvantages of the proposed method compared to existing approaches and help to establish its position in the field of explainable AI.

### Questions

1. How does the proposed method compare to other state-of-the-art explanation methods in terms of explanation quality and computational efficiency?

2. What are the limitations of the proposed method, and how can they be addressed in future research?

3. How can the proposed method be used in real-world applications, and what are the potential benefits and challenges of using it in practice?

### Rating

6

### Confidence

3

**********
