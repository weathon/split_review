### Summary

This paper presents a novel example-based explanation method for neural classifiers. The key idea is to use Kernelized Stein Discrepancy (KSD) to identify training samples that provide the best predictive support to a test point. The paper shows that the KSD can be expressed in a closed form that depends on the gradient of the model and the probabilistic prediction. The paper provides several quantitative and qualitative evaluations that demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel idea to use KSD to identify the training samples that best support a test point. The proposed method is theoretically sound and well-motivated.
2. The paper provides several quantitative and qualitative evaluations that demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires computing the KSD between the test point and all training points, which can be computationally expensive for large datasets. The paper does not provide a detailed analysis of the computational complexity of the proposed method, especially in comparison to other example-based explanation methods. It would be beneficial to see a more thorough discussion of the scalability of the approach.
2. The paper does not provide a clear explanation of how the hyperparameter k, which determines the number of training samples to be selected, is chosen. The choice of k can significantly impact the quality of the explanations, and the paper should provide more guidance on how to select an appropriate value for k. It is unclear whether k is a fixed parameter or if it is tuned for each dataset.
3. The paper does not discuss the potential limitations of using KSD for identifying the most influential training samples. While KSD is a powerful tool, it may not capture all aspects of the relationship between training and test points. For example, KSD might not be sensitive to subtle differences in feature importance or to cases where the training data is located in a sparse region of the input space. A discussion of these potential limitations would be valuable.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of the proposed method, particularly in comparison to other example-based explanation techniques. This analysis should consider the cost of computing the KSD for each test point and the overall time required to generate explanations for a dataset of a given size. It would be helpful to see a breakdown of the computational cost associated with different steps of the algorithm, such as the computation of the KSD and the selection of the top-k training samples. Furthermore, the paper should explore potential optimizations to reduce the computational burden, such as using approximations of the KSD or employing parallel computing techniques. This would make the method more practical for large-scale datasets.

The paper should provide a more detailed explanation of how the hyperparameter k is selected and its impact on the quality of the explanations. The authors should discuss whether k is a fixed parameter or if it is tuned for each dataset. If k is tuned, the paper should describe the tuning process and provide guidelines for selecting an appropriate value. It would be beneficial to see an ablation study that examines the effect of different values of k on the quality of the explanations. This study should consider both quantitative metrics, such as the accuracy of the explanations, and qualitative metrics, such as the relevance of the selected training samples. The paper should also discuss the trade-offs between the number of training samples used and the quality of the explanations.

The paper should also discuss the potential limitations of using KSD for identifying the most influential training samples. While KSD is a powerful tool, it may not capture all aspects of the relationship between training and test points. For example, KSD might not be sensitive to subtle differences in feature importance or to cases where the training data is located in a sparse region of the input space. The paper should discuss these potential limitations and suggest possible ways to address them. For instance, the authors could explore alternative discrepancy measures or consider incorporating additional information, such as the local density of the training data, into the explanation process. A discussion of these limitations would provide a more balanced and nuanced view of the proposed method.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
