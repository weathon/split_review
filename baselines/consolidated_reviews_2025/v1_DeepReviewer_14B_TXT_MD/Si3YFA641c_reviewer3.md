### Summary

This paper proposes a new method for evidential deep learning (EDL) by relaxing two non-essential settings of EDL. Specifically, the prior weight is treated as an adjustable hyper-parameter, and the variance-minimized regularization term is deprecated. The experiments show that the proposed method outperforms the state-of-the-art methods on uncertainty estimation tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and effective.
2. The experiments show that the proposed method outperforms the state-of-the-art methods on uncertainty estimation tasks.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is simple and effective, but it is not very novel. The idea of treating the prior weight as an adjustable hyper-parameter is not new, and the variance-minimized regularization term is a common technique in machine learning.
2. The experiments are limited to image classification tasks. It would be better to evaluate the proposed method on other tasks, such as natural language processing or time series analysis.
3. The paper does not provide a theoretical analysis of the proposed method. It would be better to provide some theoretical guarantees of the proposed method.

### Suggestions

The paper's primary weakness lies in its incremental contribution. While the proposed method demonstrates empirical improvements, the core ideas—adjusting the prior weight and deprecating variance-minimized regularization—are not fundamentally novel within the broader machine learning literature. To strengthen the paper, the authors should more clearly articulate the specific novelty of their approach within the context of EDL. A more detailed comparison to existing methods that also adjust prior weights or use similar regularization techniques would be beneficial. This comparison should highlight the unique aspects of their method and why it is particularly well-suited for EDL. Furthermore, the authors should explore the sensitivity of their method to the choice of hyper-parameters, especially the prior weight, and provide guidelines for selecting appropriate values in different scenarios. This would increase the practical value of the proposed method.

Expanding the experimental evaluation beyond image classification is crucial for demonstrating the generalizability of the proposed method. The authors should consider evaluating their method on diverse datasets and tasks, such as natural language processing (NLP) tasks like text classification or sequence tagging, or time series analysis tasks like anomaly detection or forecasting. These tasks often have different characteristics than image data, and evaluating the method on these tasks would provide a more comprehensive understanding of its strengths and limitations. For example, in NLP, the uncertainty estimation could be evaluated on tasks like sentiment analysis or question answering, where the model's confidence in its predictions is crucial. In time series analysis, the method could be tested on tasks like predicting future values or detecting anomalies, where the uncertainty in the predictions can be critical for decision-making. The authors should also consider comparing their method to other uncertainty estimation techniques that are commonly used in these domains.

Finally, the lack of theoretical analysis is a significant limitation. While empirical results are important, a theoretical understanding of why the proposed method works is essential for establishing its validity and for guiding future research. The authors should attempt to provide some theoretical guarantees for their method, such as convergence properties or bounds on the estimation error. This could involve analyzing the properties of the relaxed EDL objective function or studying the behavior of the method under different assumptions. Even a simplified theoretical analysis would greatly enhance the paper's contribution. For example, the authors could analyze the impact of the prior weight on the uncertainty estimates or investigate the conditions under which the variance-minimized regularization term is detrimental. This theoretical analysis would provide a deeper understanding of the method and make it more convincing.

### Questions

1. How does the proposed method compare to other uncertainty estimation methods, such as Bayesian neural networks or Monte Carlo dropout?
2. How does the choice of the prior weight affect the performance of the proposed method?
3. Can the proposed method be extended to other tasks, such as natural language processing or time series analysis?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
