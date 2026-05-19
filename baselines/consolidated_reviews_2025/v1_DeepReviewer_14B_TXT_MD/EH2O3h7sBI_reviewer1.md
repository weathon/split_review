### Summary

The paper proposes a new method for continual learning that combines prompt-tuning with a gradient projection approach. The authors provide theoretical guarantees against forgetting. The method is evaluated on diverse datasets and the experiments demonstrate the efficiency of reducing forgetting in various incremental settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel method for continual learning that combines prompt tuning with a gradient projection approach
- The proposed method provides theoretical guarantees against forgetting
- The method is evaluated on diverse datasets and the experiments demonstrate the efficiency of reducing forgetting in various incremental settings
- The paper is well-written and easy to follow

### Weaknesses

#### Some Related Works


#### comment

 - The method's performance may be sensitive to the choice of hyperparameters, such as the threshold value.
- The paper could provide more insights into the practical implications and limitations of the proposed method.

### Suggestions

The paper should include a more thorough analysis of the hyperparameter sensitivity, particularly regarding the threshold value used in the gradient projection. While the authors mention a threshold, they do not provide a clear methodology for selecting this value, nor do they explore the impact of different choices on the final performance. A sensitivity analysis, perhaps by plotting performance metrics against a range of threshold values, would be beneficial. Furthermore, the paper should discuss the computational cost associated with tuning this parameter, as well as any potential trade-offs between performance and computational efficiency. It would be helpful to see a discussion of how the threshold interacts with other hyperparameters, such as the learning rate, and whether there are any dependencies that need to be considered during implementation. This analysis should also include a discussion of the range of values that are considered reasonable for the threshold, and whether this range is dataset-dependent. 

In addition to hyperparameter sensitivity, the paper should provide a more detailed discussion of the practical limitations of the proposed method. For example, the authors should discuss the computational resources required to train the model, as well as the memory footprint of the method. It would be beneficial to compare the computational cost of the proposed method with that of other continual learning methods. The paper should also discuss the scalability of the method to larger datasets and more complex tasks. Are there any limitations in terms of the number of tasks or the size of the input data that the method can handle? Furthermore, the authors should discuss the potential for catastrophic forgetting when the method is applied to a very large number of tasks, and whether there are any strategies to mitigate this issue. A discussion of the practical challenges of implementing the method in a real-world setting would also be valuable.

Finally, the paper should provide more insights into the theoretical underpinnings of the method. While the authors claim to provide theoretical guarantees against forgetting, the discussion of these guarantees is somewhat limited. A more detailed explanation of the theoretical framework, including the assumptions that are made and the limitations of the analysis, would be beneficial. The paper should also discuss the relationship between the theoretical guarantees and the empirical results. Are there any discrepancies between the theoretical predictions and the observed performance? If so, what might be the reasons for these discrepancies? A more thorough discussion of the theoretical aspects of the method would help to strengthen the paper and provide a more solid foundation for future research.

### Questions

- How does the method perform in terms of computational efficiency compared to other continual learning methods?
- Are there any potential drawbacks or limitations of the proposed method that are not discussed in the paper?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
