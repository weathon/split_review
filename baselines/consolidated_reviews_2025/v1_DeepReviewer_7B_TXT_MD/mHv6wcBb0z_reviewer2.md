### Summary

This paper proposes a novel regularization method to prevent model collapse in deep CCA. The authors also provide a theoretical analysis of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective.
3. The authors also provide a theoretical analysis of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is very similar to the existing methods in the literature. The authors should discuss the differences between the proposed method and existing methods.
2. The theoretical analysis, while present, does not sufficiently justify the novelty of the approach. It would be beneficial to see a more in-depth comparison of the theoretical underpinnings of the proposed method with those of existing regularization techniques, highlighting the unique aspects of the proposed approach.

### Suggestions

The authors should provide a more detailed comparison of their proposed regularization method with existing techniques, particularly those used in deep CCA and related representation learning tasks. This comparison should go beyond a superficial level and delve into the mathematical formulations and the underlying assumptions of each method. For instance, a discussion of how the proposed method's invariance to noise differs from the invariance achieved by methods like weight decay or dropout would be beneficial. The authors should also clarify why their specific formulation of the regularization term is more effective at preventing model collapse than other alternatives. This could involve a more detailed analysis of the optimization landscape and how the proposed regularization affects the convergence properties of the model. Furthermore, the authors should provide empirical evidence to support their claims, demonstrating the superiority of their method over existing techniques in various scenarios, including those with different noise levels and data complexities. 

To strengthen the theoretical analysis, the authors should provide a more rigorous justification for the proposed method's effectiveness in preventing model collapse. This could involve a more detailed analysis of the spectral properties of the learned representations and how the proposed regularization affects these properties. The authors should also discuss the limitations of their theoretical analysis and identify potential areas for future research. For example, it would be useful to explore the conditions under which the proposed method is guaranteed to prevent model collapse and the conditions under which it might fail. This would provide a more complete understanding of the method's strengths and weaknesses and its applicability to different types of data and tasks. The authors should also consider providing a more detailed explanation of the connection between the proposed method and the Correlation Invariant Property (CIP), clarifying how the regularization term enforces this property and why it is crucial for preventing model collapse.

Finally, the authors should consider expanding their experimental evaluation to include a wider range of datasets and tasks. This would help to demonstrate the generalizability of their method and its effectiveness in different scenarios. The authors should also consider comparing their method with a broader range of existing regularization techniques, including those that are not specifically designed for CCA. This would provide a more comprehensive evaluation of the proposed method's performance and its advantages over existing alternatives. The authors should also provide a more detailed analysis of the computational cost of their method and compare it with the computational cost of other regularization techniques. This would help to assess the practicality of the proposed method for large-scale datasets and complex models.

### Questions

Please see the above weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
