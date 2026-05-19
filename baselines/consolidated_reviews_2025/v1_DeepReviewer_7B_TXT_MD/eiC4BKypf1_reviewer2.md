### Summary

The paper proposes to use LLMs as cognitive models. The authors finetune LLMs on behavioral data and show that the resulting models are able to predict human behavior better than traditional cognitive models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and the idea is simple and interesting. The authors provide a lot of empirical evidence that the proposed method works well.

### Weaknesses

#### Some Related Works


#### comment

The paper lacks a strong theoretical foundation. It is not clear why fine-tuning LLMs on behavioral data would lead to better cognitive models. The authors do not provide a clear explanation of the underlying mechanisms that make LLMs suitable for modeling human cognition. Specifically, the paper does not address how the sequential processing capabilities of LLMs align with the cognitive processes they are intended to model, such as working memory or attention mechanisms. The paper also does not discuss the limitations of using LLMs for cognitive modeling, such as the potential for overfitting to the specific training data or the lack of interpretability of the model's internal representations. Furthermore, the paper does not explore the potential for bias in the LLMs, which could lead to inaccurate or unfair predictions of human behavior.

### Suggestions

The authors should provide a more detailed explanation of the theoretical underpinnings of their approach. This should include a discussion of how the architecture of LLMs relates to known cognitive processes. For example, they could discuss how the sequential nature of LLMs might be analogous to the processing of information in working memory or how the attention mechanisms in LLMs might relate to attention mechanisms in the brain. A more thorough discussion of these connections would strengthen the theoretical basis of the paper and provide a more compelling argument for using LLMs as cognitive models. Furthermore, the authors should address the limitations of their approach. This includes a discussion of the potential for overfitting, which could be addressed by using techniques such as regularization or cross-validation. They should also discuss the interpretability of the model's internal representations and how these representations relate to known cognitive processes. This could involve techniques such as probing or visualization of the model's internal states. Finally, the authors should address the potential for bias in the LLMs and how this bias might affect the predictions of the model. This could involve analyzing the training data for biases or using techniques such as adversarial training to mitigate bias. 

To improve the empirical evaluation, the authors should consider comparing their approach to a wider range of existing cognitive models, including both traditional models and other machine learning approaches. This would provide a more comprehensive assessment of the strengths and weaknesses of their approach. They should also consider evaluating their model on a wider range of tasks and datasets, including tasks that involve more complex cognitive processes. This would provide a more robust assessment of the generalizability of their approach. Furthermore, the authors should provide a more detailed analysis of the model's performance, including error analysis and a discussion of the model's strengths and weaknesses on different types of tasks. This would provide a more nuanced understanding of the model's capabilities and limitations. 

Finally, the authors should consider exploring the potential for using their approach to address specific cognitive problems. For example, they could use their model to study the effects of cognitive biases or to develop new interventions for cognitive impairments. This would provide a more concrete demonstration of the potential of their approach and would make the paper more impactful. The authors should also discuss the ethical implications of using LLMs for cognitive modeling, particularly in the context of human behavior. This should include a discussion of the potential for misuse of the technology and the steps that can be taken to mitigate these risks.

### Questions

What is the theoretical basis for using LLMs as cognitive models? How do the sequential processing capabilities of LLMs align with the cognitive processes they are intended to model?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
