### Summary

This paper introduces RAOQ, a novel approach to address the ADC quantization challenges in In-Memory Computing (IMC). RAOQ includes three key components: Activation Shifting (A-shift) to shift activations to avoid zero, Weight Reshaping (W-reshape) to increase the variance of weights, and Bit Augmentation (BitAug) to adapt to ADC quantization. The method aims to improve the accuracy of IMC systems, which are designed to perform computations in memory for energy efficiency and reduced data movement. The paper demonstrates the effectiveness of RAOQ across various tasks, including image classification, object detection, and natural language processing, achieving state-of-the-art accuracy with practical IMC implementations.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation of the paper is clear, and the proposed method is reasonable.
3. The paper provides comprehensive experimental results, demonstrating the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the proposed method, particularly the A-shift and W-reshape techniques. It is unclear how these operations impact the overall inference time and energy consumption, which are critical for IMC systems. A more thorough analysis, including a breakdown of the computational cost for each component, is needed to fully assess the practical implications of the proposed method.
2. The paper does not provide a comprehensive comparison with existing quantization-aware training (QAT) methods. While the paper mentions that the proposed method is inspired by QAT, it does not clearly articulate the differences and advantages of RAOQ over other QAT techniques, especially those tailored for analog computing. A more detailed comparison, including quantitative results and a discussion of the specific challenges addressed by RAOQ, is necessary to establish its novelty and contribution.
3. The paper does not discuss the hardware implementation challenges of the proposed method. While the paper focuses on the algorithmic aspects of RAOQ, it does not address the practical considerations of implementing the A-shift and W-reshape operations in hardware. This includes the potential for increased complexity and the impact on the overall system design. A discussion of these challenges and potential solutions would strengthen the paper's practical relevance.

### Suggestions

To address the lack of computational overhead analysis, the authors should provide a detailed breakdown of the time complexity for each component of RAOQ, including A-shift, W-reshape, and BitAug. This analysis should consider the number of operations, memory accesses, and data movement involved in each step. Furthermore, the authors should present empirical results demonstrating the actual inference time and energy consumption of the proposed method on the target IMC hardware. This could include a comparison with a baseline model without RAOQ, as well as other quantization-aware training methods. The analysis should also consider the impact of different bit precisions for activations and weights, as this can significantly affect the computational cost. A clear understanding of the computational overhead is crucial for evaluating the practical applicability of RAOQ in real-world IMC systems.

To better position RAOQ within the context of existing quantization-aware training (QAT) methods, the authors should provide a more detailed comparison, including a quantitative analysis of the performance of RAOQ against other QAT techniques, especially those designed for analog computing. This comparison should not only focus on the final accuracy but also consider other factors such as the number of training epochs, the computational cost of training, and the sensitivity to hyperparameter tuning. The authors should also discuss the specific challenges that RAOQ addresses, such as the ADC quantization errors, and how these challenges are different from those addressed by other QAT methods. A clear articulation of the advantages and disadvantages of RAOQ compared to existing QAT techniques would help to establish its novelty and contribution to the field. This should include a discussion of the specific hardware constraints that motivated the design of RAOQ and how it addresses these constraints.

Finally, the authors should include a discussion of the hardware implementation challenges of the proposed method. This should include an analysis of the complexity of implementing A-shift and W-reshape operations in hardware, as well as the potential impact on the overall system design. The authors should also discuss the potential for increased memory access patterns and the impact on the overall system performance. A discussion of these challenges and potential solutions would strengthen the paper's practical relevance and provide valuable insights for future research in this area. This discussion should also consider the trade-offs between accuracy, energy efficiency, and hardware complexity, which are crucial for the practical deployment of IMC systems.

### Questions

1. How does the proposed method compare with other quantization-aware training (QAT) methods in terms of accuracy, computational overhead, and hardware implementation?
2. What are the hardware implementation challenges of the proposed method, and how can they be addressed?

### Rating

5

### Confidence

4

**********
