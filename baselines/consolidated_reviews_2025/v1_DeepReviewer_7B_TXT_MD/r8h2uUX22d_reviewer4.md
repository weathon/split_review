### Summary

This paper studies the MLP-Mixer architecture, which is a recent architecture that has achieved significant empirical success. The authors reveal that the MLP-Mixer can be interpreted as a wide MLP with sparse weights. The authors provide a theoretical analysis of the implicit regularization of the MLP-Mixer and conduct experiments to demonstrate that the MLP-Mixer is similar to sparse-weight MLPs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a novel interpretation of the MLP-Mixer as a wide MLP with sparse weights.
3. The authors provide a theoretical analysis of the implicit regularization of the MLP-Mixer and conduct experiments to demonstrate that the MLP-Mixer is similar to sparse-weight MLPs.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs. Specifically, the paper lacks a direct comparison of training time, memory usage, and convergence speed between the MLP-Mixer and a sparse-weight MLP with a comparable number of parameters. This makes it difficult to assess the practical advantages of the proposed interpretation.
2. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the implicit regularization of the MLP-Mixer and sparse-weight MLPs. The paper does not provide a clear definition of the implicit regularization being compared, nor does it provide metrics to quantify this regularization. Without a precise definition and quantifiable metrics, it is hard to evaluate the claim of similarity in implicit regularization.
3. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs. The paper lacks a detailed analysis of the experimental results, including a comparison of the performance of the MLP-Mixer and sparse-weight MLPs on different datasets and architectures. This makes it difficult to generalize the findings and assess the robustness of the proposed interpretation.

### Suggestions

The paper would benefit significantly from a more thorough empirical evaluation that directly compares the MLP-Mixer with sparse-weight MLPs. Specifically, the authors should conduct experiments to compare the training time, memory usage, and convergence speed of the MLP-Mixer with a sparse-weight MLP that has a similar number of parameters. This would provide a more concrete understanding of the practical implications of the proposed interpretation. For example, the authors could train both models on the same dataset and measure the time it takes to reach a certain performance level, as well as the memory footprint of each model during training. Furthermore, it would be beneficial to analyze the sparsity patterns of the weight matrices in both models to understand how the sparsity affects the training dynamics and final performance. This would provide a more comprehensive picture of the similarities and differences between the two architectures.

To address the lack of quantitative comparison of implicit regularization, the authors should provide a clear definition of the implicit regularization being compared. This definition should be based on a well-established theoretical framework for analyzing implicit regularization. For example, the authors could use the concept of the effective dimension of the weight matrices or the spectral norm of the Hessian matrix to quantify the implicit regularization. Furthermore, the authors should provide metrics to quantify the implicit regularization of both the MLP-Mixer and the sparse-weight MLP. This could involve measuring the change in the weight matrices during training or analyzing the eigenvalues of the Hessian matrix. By providing a precise definition and quantifiable metrics, the authors can make a more rigorous comparison of the implicit regularization of the two architectures. This would also help to understand the underlying mechanisms that lead to the observed similarities in performance.

Finally, the paper should include a more detailed analysis of the experimental results, including a comparison of the performance of the MLP-Mixer and sparse-weight MLPs on different datasets and architectures. This would help to assess the robustness of the proposed interpretation and to identify the factors that contribute to the performance of the MLP-Mixer. For example, the authors could evaluate the performance of both models on a variety of image classification datasets, such as CIFAR-10, CIFAR-100, and ImageNet, and analyze the results in terms of accuracy, training time, and memory usage. Furthermore, the authors could investigate the impact of different hyperparameters, such as the learning rate and the number of hidden layers, on the performance of both models. This would provide a more comprehensive understanding of the strengths and limitations of the proposed interpretation and would help to guide future research in this area.

### Questions

1. Can the authors provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs?
2. Can the authors provide a quantitative comparison of the implicit regularization of the MLP-Mixer and sparse-weight MLPs?
3. Can the authors provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs on different datasets and architectures?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
