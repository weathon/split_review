### Summary

This paper addresses the challenges posed by intra- and inter-learner shifts in Knowledge Tracing (KT) by introducing a novel task, Real-time Learning Pattern Adjustment (RLPA). The authors propose Cuff-KT, a method that enhances adaptability without the need for retraining, thus addressing the limitations of existing KT models. Cuff-KT achieves this through a controller and a generator that work together to adjust the model's parameters in real-time, responding to the evolving learning patterns of students.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces RLPA, a new task that addresses the intra- and inter-learner shifts, which is a novel contribution to the field of KT.
2. Cuff-KT is designed to be controllable, tuning-free, fast, and flexible, making it a practical solution for real-world applications.
3. The paper provides a clear problem formulation and a detailed explanation of the proposed method, including the controller and the generator.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of how the controller identifies "valuable learners," making it difficult to understand the effectiveness of this component.
2. The paper does not provide a clear definition of "tuning-free," which is a key characteristic of Cuff-KT.
3. The paper does not address the potential for overfitting in the generator, which could be a concern given the complexity of the model.
4. The paper lacks a clear explanation of how Cuff-KT reduces the computational cost compared to full fine-tuning.
5. The paper does not provide a clear justification for the use of low-rank decomposition in the generator.
6. The paper does not provide a clear explanation of how the value score in Equation (5) is calculated and how it relates to identifying valuable learners.
7. The paper does not provide a clear explanation of how the ZPD is calculated and how it relates to the learner's knowledge state.
8. The paper does not provide a clear explanation of how the SAA is calculated and how it relates to the learner's knowledge state.

### Suggestions

The paper needs to provide a more detailed explanation of how the controller identifies valuable learners. Specifically, the mechanism by which the controller assesses the learner's knowledge state and determines the need for parameter updates is unclear. The authors should elaborate on the specific metrics or criteria used by the controller to make this determination. For example, is there a threshold on the change in predicted probability that triggers an update? Or is it based on a comparison of the learner's current performance against their historical performance? A concrete example illustrating how the controller operates in a specific scenario would greatly enhance the reader's understanding. Furthermore, the paper should clarify the relationship between the value score and the concept of valuable learners. It is not clear how a higher value score directly translates to a learner being more valuable for parameter updates. The authors should provide a more detailed explanation of the underlying rationale and provide empirical evidence to support this claim.

The concept of "tuning-free" needs to be clearly defined and differentiated from other parameter-efficient fine-tuning methods. The paper should explicitly state what aspects of the proposed method make it tuning-free, and how this differs from methods like adapter-based tuning or bias-term fine-tuning. For instance, does tuning-free mean that no gradient-based optimization is performed on the main model's parameters? If so, this should be explicitly stated. The authors should also discuss the potential trade-offs of being tuning-free, such as potential limitations in adaptability or performance compared to methods that do involve some form of fine-tuning. A more detailed comparison with existing parameter-efficient fine-tuning methods would be beneficial to clarify the novelty and advantages of the proposed approach. Additionally, the paper should provide a more detailed explanation of how the low-rank decomposition is implemented and how the rank is chosen. The current explanation is insufficient to understand the practical implications of this design choice. The authors should also provide a more detailed explanation of how the ZPD is calculated and how it relates to the learner's knowledge state. The current explanation is insufficient to understand the practical implications of this design choice. The authors should also provide a more detailed explanation of how the SAA is calculated and how it relates to the learner's knowledge state. The current explanation is insufficient to understand the practical implications of this design choice.

Finally, the paper should provide a more detailed analysis of the computational cost of Cuff-KT compared to full fine-tuning. While the paper claims that Cuff-KT is faster, it does not provide a clear explanation of where these savings come from. A breakdown of the computational complexity of each step in both Cuff-KT and full fine-tuning would be helpful. For example, how does the low-rank decomposition affect the computational cost? The paper should also address the potential for overfitting in the generator, even with low-rank decomposition. While the paper mentions that the low-rank design reduces the risk of overfitting, it does not provide any empirical evidence to support this claim. The authors should conduct experiments to evaluate the generalization performance of the generator and discuss any techniques used to mitigate overfitting, such as regularization or early stopping. The paper should also provide a more detailed explanation of how the value score in Equation (5) is calculated and how it relates to identifying valuable learners. The current explanation is insufficient to understand the practical implications of this design choice.

### Questions

1. Can you explain more about how the controller identifies "valuable learners"?
2. What exactly do you mean by "tuning-free"?
3. How does Cuff-KT address the potential for overfitting in the generator?
4. How does Cuff-KT reduce the computational cost compared to full fine-tuning?
5. What is the purpose of using low-rank decomposition in the generator?
6. Can you explain more about how the value score in Equation (5) is calculated and how it relates to identifying valuable learners?
7. Can you explain more about how the ZPD is calculated and how it relates to the learner's knowledge state?
8. Can you explain more about how the SAA is calculated and how it relates to the learner's knowledge state?

### Rating

3

### Confidence

5

**********
