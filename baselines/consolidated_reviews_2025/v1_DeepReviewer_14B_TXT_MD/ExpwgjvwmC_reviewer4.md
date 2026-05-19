### Summary

This paper proposes a model-centric evaluation framework, OmniInput, to evaluate the quality of an AI/ML model’s predictions on all possible inputs (including human-unrecognizable ones), which is crucial for AI safety and reliability. Unlike traditional data-centric evaluation based on pre-defined test sets, the test set in OmniInput is self-constructed by the model itself and the model quality is evaluated by investigating its output distribution. They employ an efficient sampler to obtain representative inputs and the output distribution of the trained model, which, after selective annotation, can be used to estimate the model’s precision and recall at different output values and a comprehensive precision-recall curve. Experiments demonstrate that OmniInput enables a more fine-grained comparison between models, especially when their performance is almost the same on pre-defined test sets, leading to new findings and insights for how to train more robust, generalizable models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The idea of model-centric evaluation is interesting and novel.
- The experimental results are comprehensive and insightful.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not discuss the limitations of the proposed method.
- The paper does not discuss the scalability of the proposed method.

### Suggestions

The paper introduces an interesting model-centric evaluation framework, but it would benefit from a more thorough discussion of its limitations. Specifically, the reliance on human annotation for evaluating the model's output distribution is a significant bottleneck. While the authors mention that the annotation effort is less than traditional methods, the process is still subjective and time-consuming. The paper should explore alternative approaches to reduce the reliance on human annotation, such as using pre-trained models or automated metrics to evaluate the generated samples. Furthermore, the paper should discuss the potential biases introduced by human annotators and how these biases might affect the evaluation results. For example, different annotators might have varying interpretations of what constitutes a valid or meaningful sample, leading to inconsistent evaluation outcomes. A more detailed analysis of the annotation process, including inter-annotator agreement and the impact of annotation quality on the final evaluation, would strengthen the paper.

Regarding scalability, the paper needs to address the computational cost of generating and evaluating the output distribution, especially for complex models and high-dimensional input spaces. The current approach, which relies on an efficient sampler, might not be sufficient for large-scale models or datasets. The paper should discuss the computational complexity of the proposed method and explore techniques to improve its scalability, such as using more efficient sampling algorithms or parallelizing the evaluation process. Additionally, the paper should consider the memory requirements of storing and processing the output distribution, which could be a limiting factor for large models. A discussion of these practical considerations would make the proposed method more applicable to real-world scenarios. The paper should also discuss the potential for approximation techniques to reduce the computational burden, such as using a subset of the output space for evaluation or employing dimensionality reduction techniques.

Finally, the paper should also discuss the limitations of the proposed evaluation framework in terms of its ability to capture all aspects of model performance. While the precision-recall curve provides a useful summary of the model's output distribution, it might not capture other important aspects, such as the model's robustness to adversarial attacks or its ability to generalize to unseen data. The paper should discuss these limitations and suggest potential extensions to the framework that could address these issues. For example, the framework could be extended to include adversarial robustness evaluations or to assess the model's performance on out-of-distribution data. A more comprehensive evaluation framework that considers multiple aspects of model performance would be more valuable for assessing the overall quality of AI/ML models.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
