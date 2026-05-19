### Summary

This paper proposes a novel pruning at initialization (PaI) method called DPaI, which is based on a differentiable approximation of the node-path balancing (NPB) principle. DPaI is the first PaI method that takes into account network topology, specifically the Node-Path Balancing Principle, to achieve good sparse sub-networks. The authors claim that DPaI outperforms existing PaI methods and demonstrates superior performance on various architectures and datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to PaI by extending the NPB principle through a differentiable optimization.
2. The method is evaluated across multiple datasets and architectures, showing consistent improvements over baseline methods.
3. The paper provides a detailed explanation of the differentiable formulation and its integration into standard neural network training pipelines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the proposed method can be integrated into existing neural network training pipelines. The authors mention that DPaI can be used as a one-shot pruning method, but they do not provide specific details on how to use it in practice. For example, it is not clear how the masks should be initialized, how the pruning process should be performed, and how the resulting sparse network should be trained. The lack of concrete steps makes it difficult to reproduce the results and apply the method to new problems.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors claim that DPaI is efficient, they do not provide any quantitative comparisons with other pruning methods. It is important to understand the trade-offs between accuracy and computational cost, especially when dealing with large-scale models. The paper should include a detailed analysis of the time and memory requirements of the proposed method, as well as a comparison with other pruning techniques.
3. The paper does not provide a thorough discussion of the limitations of the proposed method. For example, it is not clear how the method performs on different types of neural networks or datasets. The paper should also discuss the potential challenges of applying the method to more complex models or tasks. The lack of a thorough discussion of the limitations makes it difficult to assess the generalizability of the proposed method.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the practical implementation of the DPaI method. Specifically, the authors should provide a step-by-step guide on how to integrate DPaI into a standard neural network training pipeline. This should include details on how to initialize the masks, how to perform the pruning process, and how to train the resulting sparse network. For example, the authors could provide a code snippet or a pseudocode algorithm that illustrates the key steps of the method. This would make it easier for other researchers to reproduce the results and apply the method to their own problems. Furthermore, the authors should clarify whether the method requires any modifications to the training procedure or if it can be used as a one-shot pruning method, as claimed in the paper. A clear explanation of these practical aspects is crucial for the adoption of the proposed method.

In addition, the paper needs a more thorough analysis of the computational cost of DPaI. The authors should provide a detailed comparison of the time and memory requirements of DPaI with other pruning methods. This comparison should include both training and inference time, as well as memory usage. The authors should also discuss the scalability of the method to larger models and datasets. For example, they could provide a table that shows the training time and memory usage of DPaI for different model sizes and datasets. This analysis would help to understand the trade-offs between accuracy and computational cost and would make it easier for researchers to choose the most appropriate pruning method for their specific needs. Furthermore, the authors should discuss the potential bottlenecks of the method and how they can be addressed.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. The authors should discuss how the method performs on different types of neural networks and datasets. For example, they could evaluate the method on different architectures, such as convolutional neural networks and recurrent neural networks. They should also discuss the potential challenges of applying the method to more complex models or tasks. For example, they could discuss how the method performs on tasks that require more complex reasoning or on datasets that have a large number of classes. The authors should also discuss the potential limitations of the method in terms of its sensitivity to hyperparameters or its robustness to adversarial attacks. A thorough discussion of the limitations would help to assess the generalizability of the proposed method and would provide a more balanced view of its strengths and weaknesses.

### Questions

1. How does the proposed method handle the initialization of the masks? Are the masks initialized randomly, or are they initialized based on some prior knowledge?
2. How does the proposed method perform on different types of neural networks and datasets? Are there any specific types of models or tasks where the method is expected to perform poorly?
3. How does the proposed method compare to other pruning methods in terms of computational cost? Can the authors provide a quantitative comparison of the training and inference time of DPaI with other pruning methods?

### Rating

3

### Confidence

4

**********
