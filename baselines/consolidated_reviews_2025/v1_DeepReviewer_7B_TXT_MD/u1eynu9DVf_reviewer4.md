### Summary

This paper proposes a method to forecast which examples will be forgotten after model updates. The authors propose a partially interpretable forecasting model based on the observation that changes in pretraining examples' logits resemble that of online learned examples. They also propose a black-box forecasting model based on inner products of example representations. The authors show that the proposed method can be used to reduce forgetting in the setup of continual model refinement.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear motivation and problem formulation. The proposed method is well-motivated and the experimental results are convincing.
- The proposed method is partially interpretable and can be used to understand why an example is forgotten.
- The authors propose a black-box forecasting model that does not require any fine-tuning, which is computationally efficient.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is only evaluated on BART0, P3-Test, and MMLU. It would be beneficial to evaluate the method on more datasets and models to demonstrate its generalizability.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to compare the computational cost with other methods.

### Suggestions

The paper would benefit from a more thorough evaluation of the proposed method. While the results on BART0, P3-Test, and MMLU are promising, it is crucial to assess the method's performance across a wider range of datasets and model architectures. Specifically, including datasets with different characteristics, such as those with varying levels of noise or different types of tasks, would provide a more robust understanding of the method's strengths and limitations. Furthermore, evaluating the method on different model architectures, such as encoder-only models or models with different pre-training objectives, would help to determine the method's generalizability. This would also help to identify potential biases or limitations of the method that may not be apparent from the current evaluation.

In addition to expanding the evaluation, a detailed analysis of the computational cost is necessary. The paper should provide a breakdown of the time and memory requirements for each step of the proposed method, including the forecasting model training and the example selection process. This analysis should be compared with the computational cost of other methods, such as random replay or other continual learning techniques. It would be beneficial to analyze the scalability of the method with respect to the size of the model and the dataset. This would help to understand the practical applicability of the method in real-world scenarios. The authors should also discuss the trade-offs between computational cost and performance, and provide guidelines for choosing the appropriate method based on the available resources.

Finally, the paper could benefit from a more in-depth discussion of the limitations of the proposed method. While the method shows promise, it is important to acknowledge its potential shortcomings. For example, the method may not perform well in scenarios where the forgetting patterns are highly complex or non-linear. The authors should also discuss the potential impact of the choice of the forecasting model on the overall performance. A more detailed analysis of these limitations would help to provide a more balanced view of the method and guide future research in this area.

### Questions

- How does the proposed method perform on other datasets and models?
- What is the computational cost of the proposed method compared to other methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
