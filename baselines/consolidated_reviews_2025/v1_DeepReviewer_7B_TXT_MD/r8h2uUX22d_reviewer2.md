### Summary

This paper investigates the MLP-Mixer, a recent architecture that has achieved significant empirical success. The authors reveal that the MLP-Mixer can be interpreted as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. The authors also provide a theoretical analysis of the implicit regularization of the MLP-Mixer and conduct experiments to demonstrate the similarity between the MLP-Mixer and sparse-weight MLPs.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors provide a novel interpretation of the MLP-Mixer as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC.
2. The authors provide a theoretical analysis of the implicit regularization of the MLP-Mixer and conduct experiments to demonstrate the similarity between the MLP-Mixer and sparse-weight MLPs.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs. The claim of equivalence is not sufficiently supported by empirical evidence, particularly given the known differences in training dynamics and convergence properties between dense and sparse models. The authors should provide a more rigorous analysis, including metrics such as training time, memory usage, and generalization performance, to validate their claims.
2. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the implicit regularization of the MLP-Mixer and sparse-weight MLPs. The analysis of implicit regularization is not sufficiently detailed. The authors should provide a more in-depth analysis, including metrics such as the norm of the weight matrices, the effective sparsity of the weight matrices, and the convergence behavior of the models during training. Without such analysis, it is difficult to assess the validity of their claims.
3. The authors claim that the MLP-Mixer has an effective expression as a wide MLP with Kronecker product weights, which is equivalent to a sparse MLP with a hidden layer size of SC. However, the authors do not provide a quantitative comparison of the performance of the MLP-Mixer and sparse-weight MLPs. The authors should provide a more detailed analysis of the experimental results, including a comparison of the performance of the MLP-Mixer and sparse-weight MLPs on different datasets and architectures. The current analysis is not sufficient to support the authors' claims.

### Suggestions

The authors should provide a more comprehensive empirical evaluation of the MLP-Mixer architecture, focusing on a direct comparison with sparse-weight MLPs. This comparison should include not only the final performance metrics but also the training dynamics, such as convergence speed, training time, and memory consumption. Specifically, the authors should train both the MLP-Mixer and a sparse-weight MLP with the same hidden layer size (SC) using the same training data and hyperparameters, and then compare the performance. This would provide a more concrete understanding of the practical implications of the authors' theoretical findings. Furthermore, the authors should investigate the impact of different sparsity patterns and regularization techniques on the performance of the sparse-weight MLPs. This would help to determine the optimal configuration for achieving comparable performance to the MLP-Mixer.

To strengthen the analysis of implicit regularization, the authors should provide a more detailed quantitative analysis of the weight matrices. This should include metrics such as the norm of the weight matrices, the effective sparsity of the weight matrices, and the convergence behavior of the models during training. The authors should also investigate the impact of different regularization techniques, such as weight decay and dropout, on the implicit regularization of the MLP-Mixer and sparse-weight MLPs. This would help to understand the mechanisms underlying the observed similarities in performance. Furthermore, the authors should provide a more detailed analysis of the spectral properties of the weight matrices, which could provide additional insights into the implicit regularization.

Finally, the authors should provide a more detailed analysis of the experimental results, including a comparison of the performance of the MLP-Mixer and sparse-weight MLPs on different datasets and architectures. The authors should also investigate the impact of different hyperparameters on the performance of the models. This would help to determine the optimal configuration for achieving the best performance. The authors should also provide a more detailed analysis of the computational cost of the MLP-Mixer and sparse-weight MLPs, including the number of parameters, the training time, and the memory consumption. This would help to determine the practical implications of the authors' theoretical findings.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
