### Summary

This paper proposes a fine-grained token-wise pruner for large language models (LLMs) via token routing. The proposed method consists of three main steps: initial sparsity search, dynamic router training, and sparsity scheduler fine-tuning. The authors conduct extensive experiments on various LLMs, showing the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is technically sound and achieves state-of-the-art results on several benchmarks.
2. The authors conduct extensive experiments on various LLMs, showing the effectiveness of the proposed method.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be computationally expensive, especially for large language models. The initial sparsity search, dynamic router training, and sparsity scheduler fine-tuning steps all require significant computational resources. The paper lacks a detailed analysis of the computational overhead introduced by the token router itself, including the additional parameters and the computational cost of the routing mechanism during both training and inference. It is unclear how the computational cost of the router scales with the size of the model and the sequence length.
2. The proposed method requires a large amount of training data to achieve good performance. The paper does not provide a clear analysis of the data requirements for the dynamic router training and sparsity scheduler fine-tuning steps. It is unclear how the performance of the method would be affected by using smaller datasets or datasets with different characteristics. The sensitivity of the method to the size and quality of the training data needs to be investigated.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of the proposed method. This should include a breakdown of the computational overhead introduced by the token router, including the number of additional parameters, the FLOPs required for the routing mechanism, and the latency introduced during inference. The analysis should also investigate how the computational cost of the router scales with the size of the model and the sequence length. Furthermore, the authors should compare the computational cost of their method with other pruning techniques, such as block pruning, to provide a clear understanding of the trade-offs between performance and computational cost. This analysis should be presented in a way that allows readers to assess the practical applicability of the proposed method for different hardware and software configurations.

To address the concern about data requirements, the authors should conduct experiments with varying amounts of training data to determine the sensitivity of the method to the size of the training dataset. This should include experiments with smaller datasets and datasets with different characteristics. The authors should also investigate the impact of different data augmentation techniques on the performance of the method. Furthermore, the authors should provide a clear analysis of the data requirements for each step of the proposed method, including the initial sparsity search, dynamic router training, and sparsity scheduler fine-tuning. This analysis should provide guidance on the amount of data needed to achieve good performance and should help readers understand the limitations of the method when applied to different datasets. The authors should also discuss the potential for transfer learning to mitigate the data requirements.

Finally, the authors should provide a more detailed explanation of the sparsity scheduler fine-tuning step. This should include a description of the optimization algorithm used, the hyperparameters involved, and the convergence properties of the algorithm. The authors should also provide a more detailed analysis of the impact of the sparsity scheduler on the performance of the method. This analysis should include a comparison of different sparsity schedules and should provide guidance on how to choose the optimal sparsity schedule for different tasks and datasets. The authors should also discuss the potential for using adaptive sparsity schedules that can dynamically adjust the sparsity level based on the input data.

### Questions

1. How does the proposed method compare to other pruning techniques, such as block pruning, in terms of computational cost and performance?
2. How does the proposed method perform on other types of neural networks, such as convolutional neural networks or recurrent neural networks?
3. How does the proposed method handle the trade-off between accuracy and computational cost?

### Rating

6

### Confidence

3

**********
