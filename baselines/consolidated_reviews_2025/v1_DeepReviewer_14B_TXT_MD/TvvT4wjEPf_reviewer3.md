### Summary

This paper proposes a novel regularization technique to mitigate numerical overflow during the training of RNNs over encrypted data using FHE. The authors demonstrate that their approach achieves state-of-the-art results in terms of latency, model performance, and scale, specifically using a 1.9M parameter, multi-layer RNN evaluated on the encrypted MNIST dataset.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a significant challenge in the field of privacy-preserving machine learning, specifically the overflow issue in FHE-based RNNs, which is a novel and important contribution.
2. The authors provide a thorough experimental evaluation, demonstrating the effectiveness of their approach across various metrics, including accuracy and latency.
3. The use of GPU acceleration and the CGGI variant of FHE showcases the practical applicability of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational complexity and accuracy trade-offs. The current comparison lacks a rigorous analysis of how the proposed method's performance scales with increasing model size and input sequence length compared to other FHE-based approaches. A more in-depth discussion of the specific computational bottlenecks and how the proposed regularization technique alleviates them would be beneficial.
2. The authors should provide a more in-depth analysis of the limitations of their approach, especially concerning the types of RNN architectures and datasets for which the OAR method is most effective. The paper does not explore the sensitivity of the OAR method to different RNN cell types (e.g., LSTM, GRU) or the impact of varying dataset characteristics (e.g., sequence length, data distribution) on the method's performance. It is unclear how the method would perform with more complex sequential data or with RNNs that have a larger number of parameters.
3. While the paper focuses on the MNIST dataset, it would be valuable to see results on more complex datasets to better understand the generalizability of the approach. The MNIST dataset is relatively simple and may not fully capture the challenges of real-world applications. The paper should include experiments on datasets with higher dimensionality, more complex temporal dependencies, and greater variability to demonstrate the robustness of the proposed method.

### Suggestions

To strengthen the paper, the authors should include a more detailed analysis of the computational complexity of their proposed method, specifically in comparison to existing FHE-based RNN approaches. This analysis should consider the number of homomorphic operations, the size of the ciphertexts, and the overall latency. It would be beneficial to provide a breakdown of the computational cost associated with each step of the training process, including the forward pass, backward pass, and parameter update. Furthermore, the authors should investigate how the computational cost scales with the size of the RNN model, the length of the input sequences, and the precision of the FHE parameters. This analysis should be accompanied by empirical results that demonstrate the practical implications of these scaling properties. For example, the authors could compare the training time and memory usage of their method with other FHE-based RNN methods on datasets with varying sequence lengths and model sizes. This would provide a more comprehensive understanding of the trade-offs between accuracy, latency, and computational cost.

In addition to the computational analysis, the authors should conduct a more thorough investigation of the limitations of their approach. This should include an evaluation of the OAR method's performance on different RNN architectures, such as LSTMs and GRUs, and on datasets with varying characteristics. The authors should explore how the OAR method's effectiveness is affected by the complexity of the data, the length of the sequences, and the number of parameters in the model. For example, they could evaluate the method on datasets with longer sequences, more complex temporal dependencies, and higher dimensionality. This would help to identify the types of RNNs and datasets for which the OAR method is most suitable. Furthermore, the authors should analyze the sensitivity of the OAR method to the choice of hyperparameters, such as the regularization strength, and provide guidelines for selecting appropriate values for different scenarios. This would make the method more practical and easier to use in real-world applications.

Finally, the authors should expand their experimental evaluation to include more complex datasets beyond MNIST. This would provide a better understanding of the generalizability of the proposed method and its ability to handle real-world challenges. The authors could consider using datasets such as CIFAR-10, CIFAR-100, or ImageNet, which have higher dimensionality and more complex data distributions. They could also explore datasets with longer sequences and more complex temporal dependencies, such as those found in natural language processing or time series analysis. This would demonstrate the robustness of the OAR method and its applicability to a wider range of problems. The authors should also compare the performance of their method with other state-of-the-art privacy-preserving machine learning techniques on these datasets to provide a more comprehensive evaluation of its strengths and weaknesses.

### Questions

1. How does the OAR method perform with different RNN architectures, such as LSTMs or GRUs?
2. Can the authors provide more insights into the computational overhead introduced by the OAR method, especially in terms of training time and memory usage?
3. How does the choice of FHE parameters affect the overall performance and security of the proposed method?

### Rating

6

### Confidence

3

**********
