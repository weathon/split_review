### Summary

This paper presents a benchmark for evaluating unsupervised domain adaptation (UDA) techniques for time series classification. The benchmark includes seven new benchmark datasets covering various domain shifts and temporal dynamics, facilitating fair and standardized UDA method assessments with state of the art neural network backbones (e.g. InceptionTime's backbone). This benchmark offers insights into the strengths and limitations of the evaluated approaches while preserving the unsupervised nature of domain adaptation, making it directly applicable to practical problems. The paper also provides a comprehensive evaluation of nine algorithms integrated with cutting-edge backbone architectures (e.g. InceptionTime's backbone) and scrutinizes their performance across a set of 12 datasets, including 7 novel ones we introduce to diversify domain contexts. Additionally, we delve into the crucial aspect of hyperparameter tuning criteria, an important point in UDA, given the absence of labeled data in the target domain.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- This paper presents a comprehensive benchmark for evaluating unsupervised domain adaptation (UDA) techniques for time series classification, including seven new benchmark datasets covering various domain shifts and temporal dynamics. This benchmark offers insights into the strengths and limitations of the evaluated approaches while preserving the unsupervised nature of domain adaptation, making it directly applicable to practical problems.
- The paper provides a comprehensive evaluation of nine algorithms integrated with cutting-edge backbone architectures (e.g. InceptionTime's backbone) and scrutinizes their performance across a set of 12 datasets, including 7 novel ones we introduce to diversify domain contexts.
- Additionally, we delve into the crucial aspect of hyperparameter tuning criteria, an important point in UDA, given the absence of labeled data in the target domain.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for why unsupervised domain adaptation is necessary for time series classification. The authors should provide more context on the challenges of time series classification and how UDA can address these challenges.
- The paper does not provide a clear explanation of the proposed method for selecting the best hyperparameters. The authors should provide more details on the method and its advantages over existing methods.
- The paper does not provide a clear comparison of the proposed method with existing methods. The authors should provide more details on the comparison and its significance.

### Suggestions

The paper would benefit from a more detailed explanation of the specific challenges in time series classification that necessitate the use of unsupervised domain adaptation (UDA). While the authors mention domain shifts, they should elaborate on the nature of these shifts in the context of time series data. For example, are the shifts due to changes in sensor characteristics, experimental conditions, or other factors? Providing concrete examples of these shifts and how they impact the performance of standard time series classification models would significantly strengthen the motivation for using UDA. Furthermore, the authors should discuss the limitations of existing supervised methods in handling these shifts, highlighting the practical need for UDA techniques. This would help to establish the importance of the proposed benchmark and the potential impact of the research.

Regarding the hyperparameter selection method, the authors should provide a more detailed explanation of the proposed approach. Specifically, they should clarify the underlying assumptions and the rationale behind the method's design. It would be beneficial to include a step-by-step description of the method, along with a discussion of its computational complexity and scalability. A comparison with other hyperparameter optimization techniques, such as grid search or random search, would also be valuable. The authors should also discuss the potential limitations of their proposed method and under what conditions it might not perform well. This would provide a more balanced and comprehensive evaluation of the proposed approach. Furthermore, the authors should clarify how the validation set is used to select the best hyperparameters and how this process is different from standard hyperparameter tuning approaches.

Finally, the paper needs a more rigorous comparison of the proposed hyperparameter selection method with existing techniques. The authors should not only compare the performance of the methods but also provide a detailed analysis of their strengths and weaknesses. This analysis should include a discussion of the computational cost, the sensitivity to different types of domain shifts, and the robustness to different hyperparameter settings. The authors should also consider using a wider range of evaluation metrics to provide a more comprehensive comparison. Furthermore, the authors should discuss the practical implications of their findings and provide guidance on how to choose the most appropriate method for a given application. This would make the paper more useful for both researchers and practitioners in the field.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
