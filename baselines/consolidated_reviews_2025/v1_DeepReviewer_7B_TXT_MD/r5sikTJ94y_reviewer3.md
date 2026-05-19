### Summary

This paper proposes a Reshaping and Adaptation for Output Quantization (RAOQ) approach to mitigate the impact of ADC quantization on IMC. The proposed approach includes two classes of mechanisms, including: 1) mitigating ADC quantization error by adjusting the statistics of activations and weights, through an activation-shifting approach and a weight reshaping technique, and 2) adapting to ADC quantization through a bit augmentation method. The authors conduct experiments on image classification, object detection, and natural language processing tasks, and show that the proposed approach can achieve state-of-the-art accuracy with practical IMC implementations.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed approach is well-motivated, and the authors provide a clear explanation of the problem and the proposed solution.

2. The authors conduct experiments on a wide range of tasks, including image classification, object detection, and natural language processing, and show that the proposed approach can achieve state-of-the-art accuracy with practical IMC implementations.

3. The authors provide a detailed analysis of the relationship between neural network activations, weights, and ADC quantization, and provide a theoretical justification for the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed approach is only evaluated on small-scale models, and it is unclear how it would perform on larger models, such as large language models (LLMs). The experiments do not explore the scaling behavior of the proposed method with respect to model size, which is a critical factor for real-world applications. The lack of experiments on larger models leaves a significant gap in understanding the practical applicability of the approach.

2. The authors do not provide a detailed analysis of the computational overhead introduced by the proposed approach. While the paper mentions the techniques used, it lacks a quantitative analysis of the additional computations required by the activation shifting, weight reshaping, and bit augmentation methods. This makes it difficult to assess the practical efficiency of the proposed approach, especially in resource-constrained environments.

3. The authors do not provide a detailed analysis of the hardware implementation of the proposed approach. While the paper mentions the techniques used, it lacks a discussion of the hardware requirements and constraints for implementing the activation shifting, weight reshaping, and bit augmentation methods. This makes it difficult to assess the practical feasibility of the proposed approach in real-world hardware.

### Suggestions

The authors should conduct experiments on larger models, such as large language models (LLMs), to demonstrate the scalability of the proposed approach. This would involve evaluating the performance of RAOQ on models with significantly more parameters and layers, which would provide a more comprehensive understanding of its practical applicability. The experiments should also include a detailed analysis of the accuracy degradation as the model size increases, and how the proposed techniques mitigate this degradation. Furthermore, it would be beneficial to explore the impact of different model architectures on the effectiveness of RAOQ, as some architectures may be more sensitive to ADC quantization than others.

To address the lack of computational overhead analysis, the authors should provide a detailed breakdown of the additional computations required by the activation shifting, weight reshaping, and bit augmentation methods. This analysis should include the number of operations, memory accesses, and data movement involved in each step. The authors should also compare the computational overhead of RAOQ with other quantization-aware training methods, and discuss the trade-offs between accuracy and computational efficiency. This analysis should be performed on different hardware platforms to provide a more comprehensive understanding of the practical implications of the proposed approach. It would also be beneficial to explore techniques for optimizing the implementation of RAOQ to reduce its computational overhead.

Finally, the authors should provide a detailed analysis of the hardware implementation of the proposed approach. This should include a discussion of the hardware requirements and constraints for implementing the activation shifting, weight reshaping, and bit augmentation methods. The authors should also discuss the potential for hardware acceleration of these methods, and how they can be integrated into existing IMC architectures. This analysis should include a discussion of the memory requirements, data movement patterns, and computational resources needed for implementing RAOQ. It would also be beneficial to explore the potential for co-optimizing the hardware and software implementations of RAOQ to achieve optimal performance.

### Questions

1. How does the proposed approach perform on larger models, such as large language models (LLMs)?

2. What is the computational overhead of the proposed approach, and how does it compare to other quantization-aware training methods?

3. What are the hardware requirements and constraints for implementing the proposed approach, and how can it be integrated into existing IMC architectures?

### Rating

6

### Confidence

3

**********
