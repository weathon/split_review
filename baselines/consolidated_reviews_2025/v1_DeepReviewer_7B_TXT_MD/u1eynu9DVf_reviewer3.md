### Summary

This paper studies the problem of forgetting in language model refinement. The authors propose a method to forecast which examples will be forgotten when the model is updated. They introduce two methods: a logit-based forecasting method and a black-box representation-based forecasting method. The authors demonstrate that the proposed methods can reduce forgetting in the setup of continual model refinement.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The problem of forgetting in language model refinement is interesting and important.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. The authors propose to forecast forgetting by analyzing the logit changes of examples. This idea is similar to the idea of analyzing the gradient changes of examples, which has been studied in continual learning. The authors should discuss the differences between the proposed method and the gradient-based methods in continual learning.
2. The authors should provide more details about the proposed method. For example, the authors should provide more details about the logit-based method and the representation-based method. The authors should also provide more details about the hyperparameters used in the experiments.
3. The authors should provide more analysis of the experimental results. For example, the authors should analyze why the proposed method can improve model refinement. The authors should also analyze the limitations of the proposed method.

### Suggestions

The paper introduces an interesting problem of forecasting forgetting in language model refinement, but the proposed methods lack sufficient novelty and detail. The core idea of using logit changes to predict forgetting is not new, and the authors need to clearly differentiate their approach from existing gradient-based methods in continual learning. A more thorough discussion is needed to highlight the specific advantages of their logit-based approach, especially in the context of language models where the relationship between logit changes and actual forgetting might be different from other domains. Furthermore, the authors should provide a more detailed explanation of how the logit changes are calculated and how they are used to forecast forgetting. For example, are they using the magnitude of the change, the direction of the change, or a combination of both? The paper would benefit from a more rigorous analysis of the logit changes and their correlation with actual forgetting.

To improve the clarity and reproducibility of the proposed methods, the authors should provide more details about the implementation. Specifically, the logit-based method and the representation-based method should be described in more detail, including the specific architectures used, the training procedures, and the hyperparameters. The authors should also discuss the sensitivity of the methods to different hyperparameter settings. For example, how does the choice of the learning rate, the batch size, or the number of training epochs affect the performance of the methods? Furthermore, the authors should provide a more detailed explanation of how the representation-based method is implemented, including the specific representation learning model used and how the representations are used to forecast forgetting. The lack of these details makes it difficult to assess the validity and generalizability of the proposed methods.

Finally, the authors should provide a more in-depth analysis of the experimental results. It is not enough to simply show that the proposed methods can improve model refinement. The authors should analyze why the proposed methods are effective and what are the limitations of these methods. For example, how does the performance of the methods vary with the size of the model, the size of the dataset, or the type of forgetting? The authors should also discuss the computational cost of the proposed methods and compare them with other methods for model refinement. Furthermore, the authors should provide a more detailed analysis of the forgetting phenomenon, including the types of examples that are most likely to be forgotten and the reasons why they are forgotten. This would provide a more comprehensive understanding of the problem and the effectiveness of the proposed methods.

### Questions

See the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
