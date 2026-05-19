### Summary

The paper addresses the issue of catastrophic forgetting in language models during model refinement. To mitigate this, the authors propose forecasting which upstream examples will be forgotten during model updates, allowing for targeted replay of these examples. They introduce two forecasting methods: a partially interpretable logit-change based model and a black-box representation-based model. The study demonstrates that these forecasting methods can effectively reduce forgetting in language models, with the representation-based model performing well across different model types and tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper introduces a unique approach to mitigating catastrophic forgetting by forecasting which examples will be forgotten during model updates.
2. The authors provide thorough experiments across different model types and fine-tuning setups, showcasing the generalizability of their approach.
3. The forecasting methods, especially the representation-based model, are shown to be computationally efficient, which is crucial for practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The logit-change based forecasting method works well on BART but fails on FLAN-T5, and the paper does not fully explore the reasons behind this discrepancy. This inconsistency raises questions about the robustness of the method across different model architectures. The lack of analysis on why the logit-based method fails on FLAN-T5, especially given its success on BART, is a significant oversight. It is crucial to understand if this failure is due to differences in model architecture, pre-training data, or fine-tuning procedures. Without this analysis, the general applicability of the proposed method is questionable.
2. The paper acknowledges that the forecasting models may not perfectly capture the complex dynamics of model updates, especially in sequential learning scenarios. This limitation could affect the long-term effectiveness of the forecasting methods in continual learning settings. The assumption that forecasting forgetting based on a single updated example can generalize to sequential updates is a simplification that needs further justification. The paper does not adequately address how the forecasting model's performance degrades as the number of sequential updates increases, and how this degradation impacts the overall effectiveness of the proposed method.
3. The study primarily focuses on sequence-to-sequence models and does not explore the effectiveness of the forecasting methods on other types of language models or tasks (e.g., classification). This limits the generalizability of the findings. The lack of experiments on other model architectures and tasks, such as text classification or masked language modeling, raises concerns about the broad applicability of the proposed forecasting methods. It is important to evaluate the method on a wider range of tasks to demonstrate its robustness and versatility.

### Suggestions

The paper should delve deeper into the reasons behind the failure of the logit-change based forecasting method on FLAN-T5. A more detailed analysis of the differences between BART and FLAN-T5, such as their pre-training objectives, model architectures, and fine-tuning procedures, is needed. Specifically, the authors should investigate whether the logit-based method is sensitive to the type of instruction tuning used in FLAN-T5, or if the method is more suitable for models trained with a denoising objective like BART. This analysis should include experiments that isolate the impact of these factors on the performance of the logit-based forecasting method. Furthermore, the authors should explore alternative forecasting methods that are less sensitive to model architecture and fine-tuning procedures, or propose modifications to the logit-based method to make it more robust across different models. This could involve incorporating additional information into the forecasting model, such as the specific updates made to the model parameters during fine-tuning, or using a more sophisticated model to capture the complex dynamics of model updates.

The paper needs to address the limitations of the forecasting models in sequential learning scenarios more thoroughly. The current approach of training the forecasting model on a fixed pre-trained model and applying it to sequentially updated models is a simplification that may not hold in practice. The authors should investigate how the forecasting model's performance degrades as the number of sequential updates increases, and how this degradation impacts the overall effectiveness of the proposed method. This could involve experiments that simulate more realistic continual learning scenarios, where the model is updated on a stream of data over an extended period. The authors should also explore strategies to adapt the forecasting model to the changing parameters of the language model during sequential updates. This could involve periodically retraining the forecasting model on the updated language model, or using a meta-learning approach to learn a forecasting model that is robust to changes in the language model's parameters. The paper should also provide a more detailed analysis of the trade-offs between the computational cost of retraining the forecasting model and the benefits of improved forecasting accuracy.

Finally, the paper should expand the scope of its experiments to include other types of language models and tasks. The current focus on sequence-to-sequence models limits the generalizability of the findings. The authors should evaluate the proposed forecasting methods on other tasks, such as text classification, masked language modeling, or other tasks that are commonly used in natural language processing. This would provide a more comprehensive assessment of the robustness and versatility of the proposed methods. The authors should also investigate whether the forecasting methods are sensitive to the specific characteristics of the tasks, such as the length of the input sequences or the complexity of the output space. This analysis should include a comparison of the performance of the forecasting methods on different tasks, and an investigation of the factors that contribute to the differences in performance. The authors should also explore the possibility of using task-specific forecasting models, or adapting the forecasting models to the specific characteristics of the tasks.

### Questions

1. Why does the logit-change based forecasting method work well on BART but fail on FLAN-T5? What are the underlying factors that contribute to this discrepancy?
2. How does the forecasting model perform in long sequential learning scenarios? Is there a degradation in performance as the model continues to learn over multiple updates?
3. Can the forecasting methods be adapted or extended to other types of language models or tasks beyond sequence-to-sequence models?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
