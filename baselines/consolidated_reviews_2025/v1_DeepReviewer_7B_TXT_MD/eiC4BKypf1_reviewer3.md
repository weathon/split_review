### Summary

This paper presents a method for turning large language models (LLMs) into cognitive models. The authors fine-tune a LLM on behavioral data from decision-making tasks and show that the resulting models can predict human behavior better than traditional cognitive models. They also demonstrate that the embeddings learned by the LLM contain information about individual differences and that the models can generalize to unseen tasks. The authors suggest that their approach could lead to a domain-general model of human cognition.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to cognitive modeling by leveraging the power of LLMs.
- The authors provide empirical evidence that the fine-tuned LLMs can predict human behavior better than traditional cognitive models.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear explanation of why fine-tuning the last layer of the LLM is effective for cognitive modeling.
- The paper does not discuss the limitations of the proposed approach, such as the potential for overfitting or the generalizability of the model to different tasks and datasets.
- The paper does not compare the proposed approach with other existing methods for cognitive modeling.

### Suggestions

The paper would benefit from a more thorough investigation into the mechanisms that make fine-tuning the last layer of an LLM effective for cognitive modeling. Specifically, the authors should explore the representational changes that occur in the LLM's embedding space after fine-tuning. Techniques such as representational similarity analysis (RSA) could be used to compare the representations learned by the fine-tuned LLM with those of traditional cognitive models. This would provide a more concrete understanding of how the LLM's internal representations align with known cognitive processes. Furthermore, it would be beneficial to analyze the specific features or patterns in the LLM's embeddings that are most predictive of human behavior. This could involve techniques like feature importance analysis or ablation studies to identify the key components of the embedding that contribute to the model's predictive power. Understanding these aspects would strengthen the claims of the paper and provide a more solid foundation for future research.

To address the lack of discussion on limitations, the authors should conduct a more rigorous analysis of the model's performance on different subsets of the data. For example, they could examine the model's performance on tasks with varying levels of difficulty or on datasets with different demographic characteristics. This would help to identify potential biases or limitations of the model. Additionally, the authors should explore the model's sensitivity to different hyperparameters and training procedures. This would provide a better understanding of the robustness of the model and its potential for generalization. The authors should also consider the computational cost of fine-tuning large language models and discuss the scalability of their approach to larger datasets and more complex tasks. This would be important for assessing the practical applicability of the proposed method.

Finally, the paper should include a more comprehensive comparison with existing cognitive modeling approaches. This should not only include traditional cognitive models but also other machine learning-based models that have been applied to similar tasks. The authors should clearly articulate the advantages and disadvantages of their approach compared to these alternatives. This would provide a more complete picture of the state of the art and help to contextualize the contributions of the paper. For example, the authors could compare their model with a simple neural network trained on the same data or with a symbolic model of decision-making. This would help to demonstrate the unique value of using a large language model for cognitive modeling. The comparison should also include an analysis of the interpretability of the different models, which is a crucial aspect of cognitive modeling.

### Questions

- What are the limitations of the proposed approach?
- How does the proposed approach compare to other existing methods for cognitive modeling?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
