### Summary

This paper proposes a Reshape and Adapt for Output Quantization (RAOQ) approach to mitigate ADC quantization error in In-Memory Computing (IMC). The proposed method comprises two classes of mechanisms: (1) mitigating ADC quantization error by adjusting the statistics of activations and weights, through an activation-shifting approach and a weight reshaping technique, and (2) adapting to ADC quantization through a bit augmentation method. Experimental results demonstrate that RAOQ achieves state-of-the-art accuracy across different scales of neural network models for image classification, object detection, and natural language processing tasks at various ADC bit precisions, achieving practical IMC implementations.

### Soundness

3

### Presentation

3

### Contribution

3

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

The paper would benefit from a more detailed analysis of the computational overhead introduced by the proposed RAOQ method. Specifically, the authors should provide a breakdown of the computational cost associated with the A-shift and W-reshape operations, including the number of operations, memory accesses, and data movement involved. This analysis should be performed on the target IMC hardware to provide a realistic assessment of the method's practical implications. Furthermore, the authors should compare the computational overhead of RAOQ with other quantization-aware training methods, such as those based on gradient-based optimization or knowledge distillation. This comparison should include not only the training time but also the inference time and energy consumption, which are critical for IMC systems. A thorough analysis of these factors would help to establish the practical viability of the proposed method.

To further strengthen the paper, the authors should provide a more comprehensive comparison with existing quantization-aware training (QAT) methods. While the paper mentions that RAOQ is inspired by QAT, it does not clearly articulate the differences and advantages of RAOQ over other QAT techniques, especially those designed for analog computing. A detailed comparison should include a quantitative analysis of the performance of RAOQ against other QAT methods, such as those based on post-training quantization or quantization-aware training with different optimization strategies. The authors should also discuss the specific challenges that RAOQ addresses, such as the ADC quantization errors, and how these challenges are different from those addressed by other QAT methods. This comparison should also include a discussion of the hardware constraints that motivated the design of RAOQ and how it addresses these constraints. A more thorough comparison would help to establish the novelty and contribution of the proposed method.

Finally, the paper should include a discussion of the hardware implementation challenges of the proposed method. While the paper focuses on the algorithmic aspects of RAOQ, it does not address the practical considerations of implementing the A-shift and W-reshape operations in hardware. The authors should discuss the potential for increased complexity and the impact on the overall system design. For example, they should discuss the memory access patterns and data movement involved in these operations, and how these factors can affect the performance of the IMC system. Furthermore, the authors should discuss the potential for hardware acceleration of these operations and how they can be integrated into existing IMC architectures. A discussion of these challenges and potential solutions would strengthen the paper's practical relevance and provide valuable insights for future research in this area.

### Questions

1. Could you provide a detailed analysis of the computational overhead introduced by the proposed method, particularly the A-shift and W-reshape techniques?
2. Could you provide a comprehensive comparison with existing quantization-aware training (QAT) methods?
3. Could you discuss the hardware implementation challenges of the proposed method?

### Rating

6

### Confidence

3

**********
