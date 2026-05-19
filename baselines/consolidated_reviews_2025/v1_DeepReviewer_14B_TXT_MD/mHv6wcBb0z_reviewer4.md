### Summary

This paper proposes a noise regularization approach to address the model collapse issue in Deep Canonical Correlation Analysis (DCCA). The authors demonstrate that the weight matrices in DNNs tend to be low-rank, which contributes to model collapse. The proposed NR-DCCA method introduces random data to constrain the weight matrices and enforce the Correlation Invariant Property (CIP), mimicking the behavior of Linear CCA. Theoretical analysis shows that CIP is equivalent to the full-rank property of weight matrices, justifying the effectiveness of the noise regularization approach. Experiments on synthetic and real-world datasets demonstrate the consistent outperformance and stability of NR-DCCA compared to other DCCA-based methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper identifies and addresses the model collapse issue in DCCA-based methods, which is a significant problem in multi-view representation learning.
2. The proposed noise regularization approach is novel and effective in preventing model collapse by enforcing the Correlation Invariant Property (CIP).
3. Theoretical analysis provides a solid foundation for the proposed method, demonstrating the equivalence between CIP and the full-rank property of weight matrices.
4. The experiments on both synthetic and real-world datasets demonstrate the consistent outperformance and stability of NR-DCCA compared to other DCCA-based methods.
5. The proposed method is simple and can be easily applied to other DCCA-based methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on CCA as a multi-view representation learning method. It would be beneficial to discuss the limitations of CCA compared to other methods and how the proposed approach addresses these limitations. Specifically, the paper should acknowledge that CCA, while effective for capturing shared information, may not be optimal for scenarios where view-specific information is crucial or where the relationships between views are more complex than linear correlations. A discussion of how the proposed method might perform in such scenarios would be valuable.
2. The paper could provide more details on the implementation of the proposed method, such as the specific architecture of the neural networks used and the hyperparameter settings. For instance, the paper should specify the number of layers, the type of activation functions, and the dimensionality of the hidden layers in the neural networks used for DCCA and NR-DCCA. Furthermore, details on the optimization algorithm, learning rate, and batch size should be included to ensure reproducibility.
3. The paper could benefit from a more in-depth analysis of the computational complexity of the proposed method compared to other DCCA-based methods. While the paper mentions the use of noise regularization, it does not quantify the additional computational overhead introduced by this process. A detailed analysis of the time and space complexity, especially in relation to the size of the input data and the number of hidden units, would be beneficial.

### Suggestions

The paper should include a more thorough discussion of the limitations of CCA in the context of multi-view representation learning. While CCA is effective for capturing shared information, it may not be suitable for scenarios where view-specific information is important or where the relationships between views are non-linear. The authors should discuss how their proposed method addresses these limitations, or at least acknowledge them and suggest potential future research directions. For example, they could explore how the noise regularization approach might be adapted to handle non-linear relationships or how it could be combined with other techniques to capture view-specific information. This discussion would provide a more complete picture of the method's applicability and limitations.

To improve the reproducibility of the results, the paper should provide more detailed information about the implementation of the proposed method. This includes specifying the architecture of the neural networks used for DCCA and NR-DCCA, such as the number of layers, the type of activation functions, and the dimensionality of the hidden layers. The paper should also include details on the optimization algorithm, learning rate, batch size, and any other relevant hyperparameters. Furthermore, it would be beneficial to provide a pseudocode or a detailed algorithm description to clarify the implementation steps. This level of detail is crucial for other researchers to replicate the results and build upon this work.

The paper should also include a more detailed analysis of the computational complexity of the proposed method. While the paper mentions the use of noise regularization, it does not quantify the additional computational overhead introduced by this process. A detailed analysis of the time and space complexity, especially in relation to the size of the input data and the number of hidden units, would be beneficial. This analysis should compare the computational cost of NR-DCCA with other DCCA-based methods, providing a clear understanding of the trade-offs between performance and computational efficiency. This would help readers assess the practical applicability of the proposed method in different scenarios.

### Questions

1. How does the proposed method compare to other regularization techniques used in deep learning, such as dropout or weight decay?
2. Can the proposed method be applied to other multi-view representation learning methods beyond DCCA?
3. How does the choice of noise distribution affect the performance of the proposed method?
4. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
