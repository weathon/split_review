### Summary

The authors propose a new metric called label sharpness, which is used to measure the difference between images in the dataset. They provide a theoretical analysis of the relationship between generalization and intrinsic dimension, and conduct experiments to validate their theoretical findings.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors provide a theoretical analysis of the relationship between generalization and intrinsic dimension, and conduct experiments to validate their theoretical findings.
2. The authors propose a new metric called label sharpness, which is used to measure the difference between images in the dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis is not rigorous enough. For example, the authors assume that the model is over-parameterized and well-trained. However, in practice, the models are often not over-parameterized and well-trained. The assumption of over-parameterization is particularly concerning because it allows the model to perfectly fit the training data, which is not a realistic scenario for most practical applications. The analysis should consider the effects of under-parameterization and the implications for generalization, especially when the model capacity is limited.
2. The experiments are not comprehensive enough. For example, the authors only conduct experiments on small datasets. The lack of experiments on larger, more complex datasets limits the generalizability of the findings. It is unclear whether the observed trends would hold for datasets with higher dimensionality and more complex data distributions. Furthermore, the choice of datasets seems arbitrary and does not include a wide range of data modalities or complexities, which could limit the scope of the conclusions.
3. The paper is not well-written and is hard to follow. The introduction does not clearly state the research questions or hypotheses. The motivation for studying the relationship between generalization and intrinsic dimension is not well-articulated, and the connection to the proposed label sharpness metric is not clearly explained. The paper lacks a clear narrative, making it difficult for the reader to understand the significance of the work.

### Suggestions

The authors should address the limitations of their theoretical analysis by considering the effects of under-parameterization. Specifically, they should investigate how the generalization bounds change when the model capacity is not sufficient to perfectly fit the training data. This could involve analyzing the role of the model's architecture and the training process in determining the generalization performance. Furthermore, the authors should provide a more rigorous justification for their assumptions, such as the choice of loss function and optimization algorithm, and how these choices might affect the validity of their theoretical results. A more thorough discussion of the limitations of the theoretical framework is needed to ensure the robustness of the conclusions.

To strengthen the empirical validation, the authors should conduct experiments on a wider range of datasets, including larger and more complex datasets. This would help to assess the generalizability of their findings and determine whether the observed trends hold across different data modalities and complexities. The authors should also consider using more diverse evaluation metrics to assess the performance of their proposed label sharpness metric. Additionally, the authors should provide a more detailed analysis of the experimental results, including a discussion of the statistical significance of their findings and the potential sources of variability. The choice of datasets should be justified, and the authors should explain why they believe their results are applicable to a broader range of problems.

The introduction needs to be significantly improved to clearly state the research questions and hypotheses. The authors should provide a more detailed explanation of the motivation for their work and the significance of their findings. The connection between the theoretical analysis and the proposed label sharpness metric should be clearly explained, and the authors should provide a more intuitive explanation of their theoretical results. The narrative of the paper should be improved to make it easier for the reader to understand the significance of the work. The authors should also consider adding a section that discusses the limitations of their work and potential directions for future research.

### Questions

1. What is the meaning of the red and blue points in Figure 1?
2. What is the meaning of the red and blue curves in Figure 2?
3. What is the meaning of the red and blue curves in Figure 3?
4. What is the meaning of the red and blue curves in Figure 4?
5. What is the meaning of the red and blue curves in Figure 5?

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
