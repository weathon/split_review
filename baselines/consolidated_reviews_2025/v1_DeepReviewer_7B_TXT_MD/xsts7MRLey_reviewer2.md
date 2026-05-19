### Summary

This paper proposes a benchmark for unsupervised domain adaptation (UDA) in time series classification. The authors provide a comprehensive evaluation of existing UDA methods for time series classification, including seven new benchmark datasets. The paper also discusses the importance of hyperparameter tuning in UDA and proposes a new method for selecting the best hyperparameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a comprehensive evaluation of existing UDA methods for time series classification.
3. The paper introduces seven new benchmark datasets for time series classification.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for why unsupervised domain adaptation is necessary for time series classification. The authors should provide more context on the challenges of time series classification and how UDA can address these challenges.
2. The paper does not provide a clear explanation of the proposed method for selecting the best hyperparameters. The authors should provide more details on the method and its advantages over existing methods.
3. The paper does not provide a clear comparison of the proposed method with existing methods. The authors should provide more details on the comparison and its significance.

### Suggestions

The paper would benefit from a more thorough explanation of the specific challenges in time series classification that necessitate the use of unsupervised domain adaptation (UDA). While the authors mention domain shifts, they should elaborate on the nature of these shifts in the context of time series data. For example, are the shifts due to changes in sensor characteristics, experimental conditions, or other factors? Providing concrete examples of these shifts and how they impact the performance of standard time series classification models would significantly strengthen the motivation for using UDA. Furthermore, the authors should discuss the limitations of existing supervised methods in handling these shifts, highlighting the practical need for UDA techniques. This would help to establish the importance of the proposed benchmark and the potential impact of the research.

Regarding the hyperparameter selection method, the authors should provide a more detailed explanation of the proposed approach. Specifically, they should clarify the underlying assumptions and the rationale behind the method's design. It would be beneficial to include a step-by-step description of the method, along with a discussion of its computational complexity and scalability. A comparison with other hyperparameter optimization techniques, such as grid search or random search, would also be valuable. The authors should also discuss the potential limitations of their proposed method and under what conditions it might not perform well. This would provide a more balanced and comprehensive evaluation of the proposed approach.

Finally, the paper needs a more rigorous comparison of the proposed hyperparameter selection method with existing techniques. The authors should not only compare the performance of the methods but also provide a detailed analysis of their strengths and weaknesses. This analysis should include a discussion of the computational cost, the sensitivity to different types of domain shifts, and the robustness to different hyperparameter settings. The authors should also consider using a wider range of evaluation metrics to provide a more comprehensive comparison. Furthermore, the authors should discuss the practical implications of their findings and provide guidance on how to choose the most appropriate method for a given application. This would make the paper more useful for both researchers and practitioners.

### Questions

1. What is the motivation for using unsupervised domain adaptation for time series classification?
2. How does the proposed method for selecting the best hyperparameters compare to existing methods?
3. What is the significance of the comparison between the proposed method and existing methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
