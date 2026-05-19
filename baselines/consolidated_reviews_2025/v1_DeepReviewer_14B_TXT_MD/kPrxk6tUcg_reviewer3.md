### Summary

The paper proposes a novel method called AEMC-NE (Neuron-Enhanced AutoEncoder Matrix Completion) for collaborative filtering and matrix completion. The method adds an element-wise autoencoder to each output of the main autoencoder to enhance the reconstruction capability. The paper provides theoretical analysis for AEMC-NE and investigates the generalization ability of autoencoder and deep learning in matrix completion, considering both missing completely at random and missing not at random. The paper also presents numerical results on synthetic data and benchmark datasets to demonstrate the effectiveness of AEMC-NE in comparison to many baselines.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a novel method called AEMC-NE (Neuron-Enhanced AutoEncoder Matrix Completion) for collaborative filtering and matrix completion.
2. The paper provides theoretical analysis for AEMC-NE and investigates the generalization ability of autoencoder and deep learning in matrix completion, considering both missing completely at random and missing not at random.
3. The paper presents numerical results on synthetic data and benchmark datasets to demonstrate the effectiveness of AEMC-NE in comparison to many baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of the motivation behind the proposed method. It is not clear why the element-wise autoencoder is added to each output of the main autoencoder. The authors should provide a more detailed explanation of the intuition behind this design choice and how it enhances the reconstruction capability of the model.
2. The paper does not provide a thorough comparison with existing methods. While the paper compares AEMC-NE with some baselines, it does not include a comprehensive comparison with state-of-the-art methods in the field. The authors should include more baselines and provide a more detailed analysis of the results.
3. The paper does not discuss the limitations of the proposed method. The authors should discuss the potential limitations of AEMC-NE and how it may not perform well in certain scenarios. This would provide a more balanced view of the method and its applicability.
4. The paper does not provide a detailed analysis of the computational complexity of the proposed method. The authors should provide an analysis of the time and space complexity of AEMC-NE and compare it with existing methods. This would help in understanding the scalability of the method.

### Suggestions

The paper needs to provide a more detailed explanation of the motivation behind the proposed AEMC-NE method. Specifically, the rationale for adding an element-wise autoencoder to each output of the main autoencoder is not clear. The authors should elaborate on the specific problem that this design choice aims to solve. For instance, do they expect the element-wise autoencoders to capture fine-grained patterns in the data that the main autoencoder might miss? Or is it intended to address some specific type of noise or missing data pattern? A clear explanation of the underlying intuition is crucial for understanding the novelty and effectiveness of the proposed method. Furthermore, the authors should provide a more detailed analysis of how the element-wise autoencoders interact with the main autoencoder and how they contribute to the overall reconstruction capability. This could involve visualizing the learned representations or providing a mathematical analysis of the model's behavior.

In addition to a more thorough explanation of the method's motivation, the paper would benefit from a more comprehensive comparison with existing state-of-the-art methods. The current comparison is limited and does not provide a clear picture of how AEMC-NE performs relative to the best available techniques. The authors should include a wider range of baselines, including both traditional matrix factorization methods and more recent deep learning approaches. Furthermore, the comparison should not only focus on the final performance metrics but also on other aspects such as convergence speed, robustness to different data distributions, and sensitivity to hyperparameter settings. A detailed analysis of these aspects would provide a more complete understanding of the strengths and weaknesses of AEMC-NE. The authors should also consider using more challenging datasets to further validate the effectiveness of their method.

Finally, the paper needs to address the limitations of the proposed method and provide a detailed analysis of its computational complexity. The authors should discuss the potential scenarios where AEMC-NE might not perform well, such as datasets with very high sparsity or specific types of noise. This would help in understanding the applicability of the method and its limitations. Furthermore, the authors should provide a detailed analysis of the time and space complexity of AEMC-NE, including the number of parameters and the computational cost of each operation. This analysis should be compared with existing methods to understand the scalability of AEMC-NE. The authors should also discuss the potential for parallelization and optimization techniques to improve the efficiency of the method.

### Questions

1. Can the authors provide more details on the motivation behind the proposed method? Why is the element-wise autoencoder added to each output of the main autoencoder?
2. Can the authors provide a more thorough comparison with existing methods? What are the strengths and weaknesses of AEMC-NE compared to other state-of-the-art methods?
3. Can the authors discuss the limitations of the proposed method? In what scenarios might AEMC-NE not perform well?
4. Can the authors provide a detailed analysis of the computational complexity of the proposed method? How does the computational cost of AEMC-NE compare with existing methods?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
