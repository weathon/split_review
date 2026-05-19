### Summary

This paper proposes a novel tuning method for large vision-language foundation models that enhances their performance in downstream tasks and also improve zero-shot generalization. The proposed method is Consistency-guided Prompt learning (CoPrompt), which is a fine-tuning method for vision-language models. The basic idea of CoPrompt is to enforce a consistency constraint in the prediction of the trainable and pre-trained models to prevent overfitting on the downstream task. Additionally, the authors introduce two additional components into the consistency constraint to further boost the performance: enforcing consistency on two perturbed inputs and combining two dominant paradigms of tuning, prompting and adapter. The experimental results show that CoPrompt outperforms existing methods on a range of evaluation suites, including base-to-novel generalization, domain generalization, and cross-dataset evaluation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and effective. The authors propose a consistency-enforced fine-tuning method for large foundation models that enables learning a new task from a few samples without losing zero-shot generalizability. The method incorporates the knowledge of a pre-trained LLM with consistency constraints on the text branch and data augmentations on the image branch to improve the generalization further. The method combines the two strong paradigms of tuning foundation models, prompting and adapter, into a single framework to improve performance on new tasks. The experimental results show that CoPrompt sets a new state-of-the-art for a range of evaluation suites, including base-to-novel generalization and cross-dataset recognition.

2. The paper is well-written and easy to follow. The authors provide a clear and concise introduction to the problem and the proposed method. The experimental results are presented in a clear and organized manner. The ablation studies are comprehensive and provide insights into the effectiveness of each component of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. While the authors mention that the method is efficient, they do not provide any quantitative results to support this claim. It would be helpful to compare the computational cost of the proposed method with existing methods in terms of training time and memory usage.

2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameter settings. While the authors mention that they performed a sensitivity analysis, they do not provide any details about the specific hyperparameters that were analyzed or the range of values that were tested. It would be helpful to provide a more detailed analysis of the sensitivity of the proposed method to different hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed CoPrompt method. While the authors claim efficiency, a detailed comparison against existing methods is crucial. This should include not only training time but also memory usage, especially when dealing with large vision-language models. For instance, providing a breakdown of the FLOPs required for both training and inference, along with the memory footprint of the model and intermediate computations, would offer a more concrete understanding of the method's practical applicability. Furthermore, it would be beneficial to compare the computational cost of CoPrompt with other parameter-efficient tuning methods, such as prompt tuning or adapter-based approaches, to highlight its advantages and disadvantages in terms of computational resources. This analysis should be conducted on a standard hardware setup to ensure reproducibility and allow for fair comparisons.

In addition to computational cost, a more detailed sensitivity analysis of the hyperparameters is needed. The authors mention a sensitivity analysis but do not provide specifics. It is important to understand how the performance of CoPrompt varies with different hyperparameter settings, such as the learning rate, batch size, and the number of training epochs. A grid search or a more sophisticated hyperparameter optimization technique could be used to identify the optimal hyperparameter values. The analysis should also include a discussion of the impact of different hyperparameter choices on the convergence speed and the final performance of the model. For example, it would be useful to show how the performance changes when the learning rate is varied across a reasonable range, and how the batch size affects the stability and efficiency of the training process. This would provide valuable insights into the robustness of the method and its sensitivity to hyperparameter tuning.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors demonstrate the effectiveness of CoPrompt on several benchmark datasets, it is important to acknowledge the potential limitations of the approach. For example, it would be useful to discuss the performance of CoPrompt on datasets with different characteristics, such as those with more complex visual scenes or those with a larger number of classes. It would also be beneficial to discuss the potential challenges of applying CoPrompt to real-world applications, such as those with limited computational resources or those with noisy data. Addressing these limitations would provide a more balanced and realistic assessment of the proposed method.

### Questions

1. Can the proposed method be applied to other types of foundation models, such as language models or multimodal models?

2. How does the proposed method perform on other types of tasks, such as object detection or image segmentation?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
