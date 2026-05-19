### Summary

The paper proposes a model-centric evaluation framework, OmniInput, to evaluate the quality of an AI/ML model’s predictions on all possible inputs. The key idea is to employ an efficient sampler to obtain representative inputs and the output distribution of the trained model, which, after selective annotation, can be used to estimate the model’s precision and recall at different output values and a comprehensive precision-recall curve.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper proposes a new model-centric evaluation framework, OmniInput, that constructs the test set by representative inputs, and leverages output distribution to generalize the evaluation assessment from representative inputs to the entire input space.

### Weaknesses

#### Some Related Works


#### comment

1. The contribution of the paper is limited. The authors proposed a model-centric evaluation framework based on the output distribution of the model. However, the method is not general enough, as it is only applicable to binary classification tasks. For multi-class classification tasks, the authors do not provide a detailed explanation of how the framework can be extended. The lack of a clear strategy for handling multiple classes significantly restricts the practical applicability of the proposed method.

2. The authors claim that the proposed method eliminates human biases introduced during the test data collection process. However, the method requires human evaluators to assign scores to each sample within the same "bin" of the output distribution. This introduces a new source of human bias during the evaluation process itself. The paper does not adequately address how this new form of bias is mitigated or controlled, especially considering the subjective nature of human judgment.

3. The paper lacks a detailed explanation of the sampling method used to obtain the output distribution. The authors should provide a more comprehensive description of the sampling algorithm, including its parameters and convergence properties. Without this information, it is difficult to assess the reliability and robustness of the generated output distribution, which is a critical component of the proposed framework.

4. The authors should provide a more detailed explanation of the evaluation process, including the number of human evaluators involved, the specific instructions given to them, and the measures taken to ensure consistency and reliability of their judgments. The current description lacks sufficient detail to allow for reproducibility or to assess the potential for variability in the evaluation results due to differences in human interpretation.

5. The authors should provide more experimental results to demonstrate the effectiveness of the proposed method. The current experiments are limited in scope and do not fully explore the potential and limitations of the framework. Additional experiments on diverse datasets and with different types of models would be necessary to validate the general applicability of the proposed approach.

### Suggestions

The paper introduces an interesting concept of using the model's output distribution for evaluation, but its current form has several limitations that need to be addressed. The primary concern is the lack of clarity on how the framework can be extended to multi-class classification problems. The authors should provide a detailed explanation of how the output distribution would be handled in such cases. For instance, would the framework require a one-vs-all approach for each class, or is there a more sophisticated method to handle multiple classes simultaneously? Furthermore, the paper should discuss the computational complexity of the proposed method, especially when dealing with high-dimensional output spaces. The authors should also provide a theoretical analysis of the proposed framework, including its convergence properties and error bounds. This would help to establish the theoretical foundations of the method and provide a better understanding of its limitations.

To address the issue of human bias, the authors should explore methods to quantify and mitigate the subjectivity introduced by human evaluators. One possible approach is to use multiple human evaluators and measure the inter-rater reliability. The authors could also explore the use of more objective evaluation metrics, such as comparing the generated samples with a reference dataset. The paper should also discuss the potential impact of human bias on the evaluation results and how this bias could affect the conclusions drawn from the study. Furthermore, the authors should provide a detailed analysis of the sensitivity of the evaluation results to different human evaluators and different annotation guidelines. This would help to assess the robustness of the proposed method and provide a better understanding of its limitations.

Finally, the paper needs to provide more details on the sampling method used to obtain the output distribution. The authors should describe the specific algorithm used, including its parameters and convergence properties. The paper should also discuss the potential impact of the sampling method on the evaluation results. For example, if the sampling method is not able to explore the entire output space, the evaluation results may be biased. The authors should also explore different sampling methods and compare their performance. The paper should also provide a detailed analysis of the computational cost of the sampling method and how it scales with the size of the input space. This would help to assess the practical applicability of the proposed method and provide a better understanding of its limitations.

### Questions

Please refer to the weakness.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
