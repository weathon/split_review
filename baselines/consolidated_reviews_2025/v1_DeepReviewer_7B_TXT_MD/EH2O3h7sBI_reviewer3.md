### Summary

The paper proposes a new method for continual learning by combining prompt-tuning with gradient projection. The authors provide a theoretical analysis of the proposed method and demonstrate its effectiveness on several benchmark datasets.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper provides a theoretical analysis of the proposed method, which is a significant contribution to the field of continual learning.
2. The authors demonstrate the effectiveness of the proposed method on several benchmark datasets, which provides empirical evidence for its performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and lacks clarity in several places. For example, the authors should clearly explain the relationship between the proposed method and existing methods, and how the proposed method improves upon them. The motivation for using gradient projection in the context of prompt tuning is not clearly articulated, making it difficult to understand the core contribution.
2. The authors should provide more details about the experimental setup, including the specific hyperparameters used and the training procedure. The lack of detail makes it difficult to reproduce the results and assess the robustness of the method. For example, the specific architecture of the model, the learning rate schedule, and the batch size are not specified.
3. The authors should discuss the limitations of the proposed method and potential directions for future research. The paper does not adequately address the computational cost of the proposed method, especially in comparison to existing continual learning techniques. Furthermore, the paper does not discuss the potential impact of the proposed method on different types of tasks or datasets.

### Suggestions

The paper needs significant improvements in clarity and detail to be considered for publication. First, the authors should provide a more thorough explanation of the proposed method, clearly articulating the relationship between prompt tuning and gradient projection. The motivation for using gradient projection in this context needs to be explicitly stated, with a clear explanation of how it addresses the challenges of continual learning with prompt tuning. A detailed comparison with existing methods, highlighting the specific advantages of the proposed approach, is crucial. This should include a discussion of the limitations of existing methods and how the proposed method overcomes these limitations. For example, if the method builds upon existing work, the authors should clearly state the incremental contribution and how it differs from prior approaches.

Second, the experimental section requires substantial detail. The authors must provide a comprehensive description of the experimental setup, including the specific model architecture, the learning rate schedule, the batch size, and any other relevant hyperparameters. The training procedure should be described in sufficient detail to allow for reproducibility. Furthermore, the authors should include ablation studies to demonstrate the impact of different components of the proposed method. For example, they could investigate the effect of varying the gradient projection parameters or using different prompt tuning strategies. This would help to isolate the key factors contributing to the performance of the method and provide a deeper understanding of its behavior. The authors should also consider including experiments on a wider range of datasets and tasks to assess the generalizability of the proposed method.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential avenues for future research. The authors should address the computational cost of the method, especially in comparison to existing continual learning techniques. They should also discuss the potential impact of the proposed method on different types of tasks or datasets. For example, how would the method perform on tasks with different levels of complexity or on datasets with different characteristics? The authors should also consider discussing the potential for extending the method to other types of models or tasks. This would help to provide a more complete picture of the proposed method and its potential impact on the field of continual learning.

### Questions

See above.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
