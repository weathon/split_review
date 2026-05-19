### Summary

This paper proposes a new method for the few-shot learning task. The method is motivated by the overfitting problem of existing methods. The proposed method uses a consistency constraint to prevent the overfitting problem. The experiments show that the proposed method outperforms the existing methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The experiments show that the proposed method outperforms the existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is very similar to MaPLe. The main difference is that the proposed method adds a consistency constraint. However, the consistency constraint is not new. It is very similar to the regularization techniques in the image field. The main difference between the proposed method and the regularization techniques is that the proposed method adds the consistency constraint between the trainable model and the pre-trained model. However, the pre-trained model is fixed, so the trainable model is still trained with the supervision of the pre-trained model. Therefore, the proposed method is still a kind of regularization technique.
2. The experiments are not sufficient. The proposed method is only compared with MaPLe. Other methods, such as MaPLe, are not compared.
3. The paper is not easy to follow. The paper is not easy to follow. The authors should improve the writing of the paper.

### Suggestions

The paper's core weakness lies in the incremental nature of its contribution. While the authors frame the consistency constraint as a novel approach to preventing overfitting in few-shot learning, the underlying mechanism is fundamentally similar to existing regularization techniques. The consistency loss, which aims to align the feature representations of the trainable model with those of the pre-trained model, can be viewed as a form of implicit regularization. Specifically, it acts as a constraint that limits the extent to which the trainable model can deviate from the pre-trained model's learned feature space. This is analogous to adding a penalty term that discourages large weight updates, a common practice in regularization. The paper would benefit from a more thorough analysis of how this consistency constraint differs from other regularization methods, such as weight decay or dropout, in the context of few-shot learning. A more detailed theoretical justification for the proposed method would also be beneficial, perhaps by analyzing the optimization landscape and demonstrating how the consistency constraint helps to avoid sharp minima that lead to overfitting.

Furthermore, the experimental evaluation needs to be significantly expanded to provide a more robust assessment of the proposed method's effectiveness. The current comparison with only MaPLe is insufficient, given the numerous existing methods in few-shot learning. The authors should include comparisons with other state-of-the-art methods, such as those based on meta-learning or metric learning, to demonstrate the superiority of their approach. Additionally, the experimental setup should be more comprehensive, including a wider range of datasets and evaluation metrics. It would also be beneficial to analyze the performance of the proposed method under different few-shot learning settings, such as varying the number of shots and the number of classes. This would provide a more complete picture of the method's strengths and weaknesses and its applicability to different scenarios. The paper should also include an ablation study to analyze the impact of different components of the proposed method, such as the consistency constraint and the adapter, on the overall performance.

Finally, the paper's presentation needs improvement to enhance its clarity and readability. The current writing is somewhat dense and difficult to follow, making it challenging for the reader to grasp the key ideas and contributions of the paper. The authors should consider restructuring the paper to improve its flow and organization. This could involve providing a more detailed explanation of the proposed method, including a step-by-step description of the algorithm and the mathematical formulations. The paper should also include more illustrative examples and figures to help the reader understand the concepts. The authors should also ensure that the paper is well-written and easy to understand, with clear and concise language. The paper should also include a more thorough discussion of the limitations of the proposed method and potential directions for future research.

### Questions

Please see the weaknesses.

### Rating

3

### Confidence

5

**********
