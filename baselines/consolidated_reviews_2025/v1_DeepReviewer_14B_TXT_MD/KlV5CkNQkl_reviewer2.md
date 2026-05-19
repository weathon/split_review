### Summary

This paper proposes a new example-based prediction explanation method, called HD-Explain, for neural network classifiers. The proposed method leverages the properties of Kernelized Stein Discrepancy (KSD) to identify training samples that provide the best predictive support to a test point. The authors conduct thorough analyses and experiments across multiple classification domains, where they show that HD-Explain outperforms existing methods from various aspects, including preciseness (fine-grained explanation), consistency, and computation efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.

2. The proposed method is novel and interesting. The authors leverage the properties of KSD to identify training samples that provide the best predictive support to a test point, which is a new approach in the field of example-based prediction explanation.

3. The authors conduct thorough analyses and experiments across multiple classification domains, where they show that HD-Explain outperforms existing methods from various aspects, including preciseness (fine-grained explanation), consistency, and computation efficiency.

4. The proposed method has the potential to be widely used in various applications, as it is model-agnostic and can be applied to any trained classifier.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the Kernelized Stein Discrepancy (KSD), which is a relatively new method in the field of machine learning. Although the authors provide a brief introduction to KSD in the paper, it may still be difficult for some readers to fully understand the method.

2. The authors only provide the source code for the proposed method, but not for the experiments. This makes it difficult for other researchers to reproduce the results and compare their methods with the proposed method.

3. The authors only evaluate the proposed method on a limited number of datasets. Although the authors claim that the proposed method is model-agnostic and can be applied to any trained classifier, it is difficult to say whether the method is truly effective without evaluating it on a wider range of datasets and models.

4. The paper lacks a more detailed discussion of the limitations of the proposed method. For example, the authors do not discuss the computational complexity of the method, or the potential for the method to be biased towards certain types of explanations.

### Suggestions

The paper would benefit from a more thorough explanation of the Kernelized Stein Discrepancy (KSD) and its connection to the proposed explanation method. While the authors provide a brief overview, a deeper dive into the mathematical underpinnings of KSD, including its relationship to divergence measures and its specific properties that make it suitable for identifying predictive support, would greatly enhance the reader's understanding. Specifically, the paper should elaborate on how the KSD is computed in practice, including the choice of kernel and its impact on the results. Furthermore, a discussion on the theoretical guarantees of KSD, such as its consistency and convergence properties, would add more rigor to the proposed method. This would help readers appreciate the theoretical foundations of the method and its potential advantages over other explanation techniques.

To improve the reproducibility of the results, the authors should provide the source code for the experiments, not just the implementation of the proposed method. This would allow other researchers to easily replicate the experiments and compare their methods with HD-Explain. The experimental code should include all the necessary scripts for data preprocessing, model training, and evaluation. Furthermore, the authors should provide detailed instructions on how to run the experiments, including the required software and hardware specifications. This would make the results more transparent and accessible to the research community. Additionally, the authors should consider releasing the trained models used in the experiments, which would further facilitate reproducibility and comparison.

Finally, the authors should conduct a more comprehensive evaluation of the proposed method on a wider range of datasets and models. This would provide more evidence for the effectiveness and generalizability of the method. The evaluation should include both synthetic and real-world datasets, as well as different types of models, such as convolutional neural networks and recurrent neural networks. Furthermore, the authors should consider evaluating the method on different tasks, such as image classification, natural language processing, and time series analysis. This would demonstrate the versatility of the method and its applicability to different domains. The authors should also provide a more detailed analysis of the limitations of the method, including its computational complexity and potential biases. This would help readers understand the strengths and weaknesses of the method and its suitability for different applications.

### Questions

1. Can the authors provide more details on the choice of the kernel function used in the KSD calculation? How does the choice of kernel affect the results?

2. The authors mention that the proposed method can be used to identify training samples that provide the best predictive support to a test point. Can the authors provide more details on how this is achieved? How does the method determine which training samples are most relevant to a given test point?

3. The authors mention that the proposed method is computationally efficient. Can the authors provide more details on the computational complexity of the method? How does the method compare to other example-based explanation methods in terms of computational efficiency?

### Rating

6

### Confidence

3

**********
