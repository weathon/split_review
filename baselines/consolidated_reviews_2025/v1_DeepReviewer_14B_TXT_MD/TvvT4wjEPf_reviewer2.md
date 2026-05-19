### Summary

This paper proposes a new technique for training RNNs with FHE, using a specialized regularization term to reduce the noise in FHE operations. The authors show that this approach achieves high accuracy on the MNIST dataset, with a small decrease in accuracy compared to the unencrypted domain, and evaluate the efficiency of their approach using the Concrete library.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

The paper tackles a very important problem, as RNNs are widely used in applications where data privacy is important, making them a good candidate for FHE. The authors achieve impressive accuracy on the MNIST dataset, with a small decrease in accuracy compared to the unencrypted domain, which is important for the applicability of their approach. Additionally, they evaluate the efficiency of their approach using the Concrete library, which is one of the few libraries that provides GPU support for FHE.

### Weaknesses

#### Some Related Works


#### comment

The paper is not very clear and is hard to follow. For example, the authors do not explain the basic terminology used in the paper, such as "overflow" and "message space", which are important concepts for understanding the problem they are trying to solve. Additionally, the paper lacks a high-level overview of the FHE scheme used in the paper, making it difficult to understand the technical details of their approach.

The paper also lacks a detailed description of the training process, specifically how the FHE operations are integrated into the backpropagation algorithm. It is unclear how the gradients are computed and updated when dealing with encrypted data, and how the noise in the FHE ciphertexts affects the training convergence. Furthermore, the paper does not provide a clear explanation of the specific RNN architecture used, including the number of layers, hidden units, and activation functions, making it difficult to reproduce the results.

Finally, the experimental evaluation is limited to the MNIST dataset, which is a relatively simple dataset. The authors should provide a more comprehensive evaluation of their approach on more complex datasets to demonstrate its practical applicability. The paper also lacks a comparison with other existing FHE-based RNN training methods, making it difficult to assess the novelty and advantages of the proposed approach.

### Suggestions

To improve the clarity of the paper, the authors should provide a more detailed explanation of the fundamental concepts, such as "overflow" and "message space," early in the paper. Specifically, they should explain how the finite precision of the ciphertext space in FHE leads to overflow issues during computations, and how this affects the accuracy of the model. A high-level overview of the FHE scheme used, including the key generation, encryption, decryption, and homomorphic operations, should also be included to make the paper more accessible to readers unfamiliar with FHE. This overview should also clarify the specific type of FHE scheme used (e.g., BGV, CKKS, BFV) and its implications for the proposed method.

To address the lack of detail in the training process, the authors should provide a step-by-step explanation of how the FHE operations are integrated into the backpropagation algorithm. This should include a clear description of how the gradients are computed and updated when dealing with encrypted data, and how the noise in the FHE ciphertexts affects the training convergence. The authors should also provide a detailed description of the RNN architecture used, including the number of layers, hidden units, and activation functions. This should be accompanied by a diagram or pseudocode to illustrate the flow of data and operations during training. Furthermore, the authors should discuss the challenges of training RNNs with FHE, such as the accumulation of noise and the computational overhead, and how their approach addresses these challenges.

To strengthen the experimental evaluation, the authors should evaluate their approach on more complex datasets, such as CIFAR-10 or a similar benchmark, to demonstrate its practical applicability. They should also compare their approach with other existing FHE-based RNN training methods, if available, or with other privacy-preserving machine learning techniques. This comparison should include metrics such as accuracy, training time, and computational cost. The authors should also provide an ablation study to evaluate the impact of different components of their approach, such as the regularization term, on the overall performance. Finally, the authors should discuss the limitations of their approach and suggest future research directions.

### Questions

1. Can this approach be applied to other datasets, such as CIFAR-10, to demonstrate its practical applicability?
2. How does the training process work in this approach? Is it similar to the inference process, just with additional training steps? 
3. How does the efficiency of this approach compare to other existing methods for training RNNs with FHE?

### Rating

5

### Confidence

3

**********
