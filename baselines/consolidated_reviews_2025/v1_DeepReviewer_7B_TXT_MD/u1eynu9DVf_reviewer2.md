### Summary

This paper studies the problem of model refinement, i.e., updating a pretrained model with new data. The authors focus on the problem of forgetting, i.e., the updated model forgets some of the knowledge it learned from the pretraining data. The authors propose to forecast which examples will be forgotten after the model is updated. The authors propose two methods to forecast forgetting, including a logit-based method and a representation-based method. The authors also show that the proposed method can be used to improve model refinement.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The problem of forgetting is important and has been studied for a long time. The authors focus on the problem of forgetting in the context of model refinement, which is a relatively new problem. The authors propose a new method to forecast forgetting, which is interesting.

2. The authors conduct extensive experiments to evaluate the proposed method. The results show that the proposed method can improve model refinement.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very novel. The authors propose to forecast forgetting by analyzing the logit changes of examples. This idea is similar to the idea of analyzing the gradient changes of examples, which has been studied in continual learning. The authors should discuss the differences between the proposed method and the gradient-based methods in continual learning.

2. The authors should provide more details about the proposed method. For example, the authors should provide more details about the logit-based method and the representation-based method. The authors should also provide more details about the hyperparameters used in the experiments.

3. The authors should provide more analysis of the experimental results. For example, the authors should analyze why the proposed method can improve model refinement. The authors should also analyze the limitations of the proposed method.

### Suggestions

The authors should more clearly articulate the novelty of their approach compared to existing methods in continual learning, particularly those that analyze gradient changes. While the paper focuses on logit changes, a more thorough discussion is needed to differentiate the proposed method from gradient-based approaches. Specifically, the authors should elaborate on the theoretical underpinnings that make logit-based analysis distinct and potentially more effective for forecasting forgetting in the context of model refinement. For instance, they could discuss whether the logit changes capture different aspects of forgetting compared to gradient changes, and if so, why. Furthermore, a more detailed explanation of how the proposed methods are implemented, including the specific architectures used for the forecasting models and the exact training procedures, would greatly enhance the reproducibility and understanding of the work. This should include details on the loss functions, optimization algorithms, and any regularization techniques used. 

To strengthen the experimental section, the authors should provide a more in-depth analysis of the results. Instead of just reporting performance metrics, they should investigate why the proposed method leads to improved model refinement. For example, they could analyze the correlation between the predicted forgetting and the actual forgetting, and whether the method is more effective for certain types of examples or model architectures. Additionally, the authors should explore the limitations of their approach. For example, how does the method perform when the model is updated with a large number of examples, or when the examples are highly diverse? What are the computational costs associated with the proposed method, and how do they compare to other methods? Addressing these questions would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach. 

Finally, the authors should consider including ablation studies to evaluate the contribution of different components of their method. For example, they could evaluate the performance of the logit-based method without the representation-based component, or vice versa. This would help to isolate the impact of each component and provide a more nuanced understanding of the proposed method. Furthermore, the authors should also consider comparing their method with other state-of-the-art methods for model refinement, not just random replay. This would provide a more comprehensive evaluation of the proposed method and demonstrate its advantages over existing approaches. The authors should also discuss the potential for combining their method with other techniques for model refinement, such as knowledge distillation or parameter pruning.

### Questions

1. How does the proposed method compare to other methods for model refinement, such as knowledge distillation and parameter pruning?

2. How does the proposed method perform when the model is updated with a large number of examples?

3. How does the proposed method perform when the examples are highly diverse?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
