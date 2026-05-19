### Summary

The paper proposes a new method for training Differentially Private (DP) Deep Neural Networks (DNNs) without the need for per-sample gradient clipping. This method leverages Lipschitz constrained networks, which are DNNs where the parameter-wise gradient is bounded by a constant (ideally 1). The authors show that this approach can achieve privacy guarantees while avoiding the computational overhead of per-sample clipping. The paper also provides a Python package for enforcing Lipschitz constraints in practice and demonstrates the method's effectiveness on several datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper addresses a significant challenge in the field of Differentially Private (DP) learning, which is the computational cost and memory usage associated with per-sample gradient clipping. By proposing a method that eliminates this need, the authors offer a potentially more scalable and efficient solution for training DP models.

2. The authors provide a theoretical analysis of the proposed method, including bounds on the sensitivity of the network with respect to its parameters. This analysis provides a solid foundation for understanding the privacy guarantees of the method.

3. The paper is well-written and easy to follow. The authors clearly explain the motivation behind their approach, the technical details of the method, and the experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a thorough comparison with existing methods for DP training, particularly those that also aim to avoid per-sample gradient clipping. A more comprehensive comparison would help to highlight the advantages and disadvantages of the proposed method in relation to other approaches. Specifically, the paper lacks a detailed analysis of how the proposed method compares to techniques that use gradient compression or quantization, which are also used to reduce computational overhead in DP training. A comparison with methods that use these techniques would provide a more complete picture of the proposed method's performance and resource usage.

2. The experimental evaluation is limited to relatively small datasets (e.g., MNIST and CIFAR-10). It is unclear how the proposed method would scale to larger, more complex datasets, such as ImageNet or other datasets with higher dimensionality and more complex data distributions. The paper should include experiments on larger datasets to demonstrate the practical applicability of the proposed method in real-world scenarios. Furthermore, the paper should also investigate the impact of different network architectures on the performance of the proposed method. The current experiments only use a limited set of architectures, and it is unclear how the method would perform with more complex architectures such as transformers or larger convolutional networks.

3. The paper does not discuss the limitations of the proposed method, such as the potential impact of the Lipschitz constraint on the model's expressiveness and its ability to learn complex patterns in the data. A discussion of these limitations would provide a more balanced view of the proposed method and help to identify areas for future research. For example, the paper should discuss whether the Lipschitz constraint limits the model's ability to fit complex functions or to generalize to unseen data. It should also discuss the potential trade-offs between the Lipschitz constraint and the model's accuracy.

### Suggestions

To address the lack of comparison with existing methods, the authors should include a more detailed analysis of how their approach compares to other techniques used in DP training, such as gradient compression and quantization. This analysis should not only focus on the privacy guarantees but also on the computational cost and memory usage of each method. For example, the authors could compare their method to a baseline that uses gradient compression techniques, such as top-k compression, and analyze the trade-offs between privacy, accuracy, and computational cost. This would provide a more comprehensive understanding of the advantages and disadvantages of the proposed method. Furthermore, the authors should also discuss the potential for combining their method with other techniques, such as gradient compression, to further improve the efficiency of DP training.

To address the limited experimental evaluation, the authors should include experiments on larger, more complex datasets, such as ImageNet or other datasets with higher dimensionality and more complex data distributions. These experiments should also investigate the impact of different network architectures on the performance of the proposed method. For example, the authors could test their method on architectures such as transformers or larger convolutional networks, and analyze how the method scales with increasing model size and complexity. This would provide a more realistic assessment of the practical applicability of the proposed method in real-world scenarios. Additionally, the authors should also investigate the impact of different hyperparameters on the performance of the proposed method, such as the Lipschitz constant and the noise scale, and provide guidelines for selecting appropriate values for these parameters.

Finally, the authors should include a more thorough discussion of the limitations of the proposed method, such as the potential impact of the Lipschitz constraint on the model's expressiveness and its ability to learn complex patterns in the data. This discussion should include an analysis of whether the Lipschitz constraint limits the model's ability to fit complex functions or to generalize to unseen data. The authors should also discuss the potential trade-offs between the Lipschitz constraint and the model's accuracy, and provide guidelines for selecting appropriate values for the Lipschitz constant. Furthermore, the authors should also discuss the potential for future research to address these limitations, such as exploring alternative methods for enforcing the Lipschitz constraint or developing techniques for training non-Lipschitz networks in a DP setting.

### Questions

1. How does the proposed method compare to other techniques used in DP training, such as gradient compression or quantization, in terms of computational cost and privacy guarantees?

2. How does the proposed method scale to larger, more complex datasets, such as ImageNet or other datasets with higher dimensionality and more complex data distributions?

3. What are the limitations of the proposed method, such as the potential impact of the Lipschitz constraint on the model's expressiveness and its ability to learn complex patterns in the data?

### Rating

5

### Confidence

4

**********
