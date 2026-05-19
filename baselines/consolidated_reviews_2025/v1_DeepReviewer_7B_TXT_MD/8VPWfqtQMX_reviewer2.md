### Summary

This paper proposes a new method for domain generalization, called in-context risk minimization (ICRM). The method is inspired by the success of in-context learning in large language models, and the idea is to train a model to predict the label of a test sample given a sequence of samples from the same environment as context. The authors provide theoretical analysis and empirical results to support their claims.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The idea of using in-context learning for domain generalization is novel and interesting. The authors provide a theoretical analysis to support their claims.
2. The authors provide extensive experiments to evaluate the performance of ICRM. The results show that ICRM outperforms several baseline methods on several datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of why in-context learning is effective for domain generalization. While the authors provide some intuition, a more rigorous explanation is needed. Specifically, the paper does not clearly articulate how the in-context learning mechanism allows the model to generalize to unseen environments. The connection between the in-context examples and the target environment's distribution is not well-established. It is unclear how the model learns to adapt to new environments based on the provided context, especially when the context and target environments are significantly different.
2. The paper does not provide a clear definition of the in-context learning mechanism. The authors should provide a more formal definition of the in-context learning mechanism and how it is implemented in the proposed method. The description of the context construction and the model's training process is vague. It is not clear how the model uses the context to make predictions, and how the context is selected. The lack of a formal definition makes it difficult to understand the method and to reproduce the results.
3. The paper does not provide a clear explanation of the theoretical analysis. The authors should provide a more detailed explanation of the theoretical analysis and how it supports the proposed method. The assumptions and limitations of the theoretical analysis are not discussed. The theoretical analysis is not well-integrated with the empirical results, and it is not clear how the theoretical findings translate to the practical performance of the method.

### Suggestions

The authors should provide a more detailed explanation of the in-context learning mechanism and how it facilitates domain generalization. This explanation should include a formal definition of the in-context learning process, including how the context is constructed and how the model uses the context to make predictions. The authors should also provide a more rigorous justification for why in-context learning is effective for domain generalization, perhaps by relating it to existing theories of generalization or by providing a more detailed analysis of the model's behavior. For example, they could analyze the feature representations learned by the model and show how they change when the context is provided. Furthermore, the authors should clarify the relationship between the context and the target environment, and how the model is able to generalize to unseen environments based on the provided context. This could involve analyzing the similarity between the context and the target environment, and how this similarity affects the model's performance.

To improve the clarity of the paper, the authors should provide a more detailed description of the experimental setup and the implementation of the proposed method. This should include a clear explanation of how the context is constructed, how the model is trained, and how the predictions are made. The authors should also provide a more detailed explanation of the theoretical analysis, including the assumptions and limitations of the analysis. The theoretical analysis should be integrated more closely with the empirical results, and the authors should provide a clear explanation of how the theoretical findings translate to the practical performance of the method. For example, they could provide a more detailed analysis of the convergence properties of the proposed method, and how these properties relate to the generalization performance.

Finally, the authors should provide a more thorough discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the assumptions made by the method, and the conditions under which the method is expected to perform well or poorly. The authors should also discuss the potential for extending the method to other domains and tasks, and the challenges that might be encountered. This discussion should be more detailed than the current discussion, and should include a more critical analysis of the limitations of the method.

### Questions

1. How does the proposed method compare to other domain generalization methods that do not use in-context learning?
2. What are the limitations of the proposed method, and how can these limitations be addressed in future work?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
