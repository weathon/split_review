### Summary

This paper proposes a fairness regularizer to improve the performances of sub-populations on the tail and the overall learning performance. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The idea of introducing fairness regularizer is novel and interesting.
3. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that they propose a fairness regularizer to improve the performances of sub-populations on the tail. However, the authors do not provide the performances of different sub-populations. The authors should provide the performances of different sub-populations to demonstrate that the proposed method can improve the performances of sub-populations on the tail.
2. The authors should provide the comparison with state-of-the-art methods to demonstrate the superiority of the proposed method.
3. The authors should provide the ablation study to demonstrate the effectiveness of different components of the proposed method.

### Suggestions

The paper introduces a fairness regularizer, which is an interesting approach. However, the evaluation lacks crucial details that would solidify its claims. Specifically, the authors should provide a breakdown of performance across different sub-populations, especially focusing on the tail sub-populations. This is essential to validate the core claim that the proposed method improves performance on the tail. The current evaluation only provides overall performance metrics, which do not reveal the per-sub-population impact. For example, a table or figure showing the accuracy or F1-score for each sub-population, categorized by their size or frequency, would be beneficial. This would allow for a direct assessment of whether the method truly benefits the tail sub-populations, or if the observed improvements are primarily driven by head sub-populations. Without this detailed analysis, the claim of improved tail performance remains unsubstantiated.

Furthermore, the paper needs a more thorough comparison with existing state-of-the-art methods. While the authors mention related work, a direct comparison with established techniques is missing. This comparison should not only include overall performance metrics but also the performance on tail sub-populations. The authors should select a few representative state-of-the-art methods that address similar problems, such as long-tailed learning or class imbalance, and compare their performance with the proposed method. This comparison should be done on the same datasets and using the same evaluation metrics. This would provide a clear understanding of the advantages and disadvantages of the proposed method compared to existing approaches. Without this comparison, it is difficult to assess the novelty and practical value of the proposed method.

Finally, an ablation study is crucial to understand the contribution of different components of the proposed method. The authors should systematically remove or modify different parts of the fairness regularizer to see how each component affects the overall performance. For example, they could remove the fairness term entirely, or modify the way the fairness is measured. This would help to identify the key components that are responsible for the observed improvements. The ablation study should also include an analysis of the hyperparameters of the proposed method, such as the weight of the fairness regularizer. This would provide insights into the sensitivity of the method to different parameter settings and help to identify the optimal configuration. Without this ablation study, it is difficult to understand the inner workings of the proposed method and its robustness.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
