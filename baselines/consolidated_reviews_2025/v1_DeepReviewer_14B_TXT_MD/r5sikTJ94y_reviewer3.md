### Summary

This paper proposes a novel quantization-aware training (QAT) method for in-memory computing (IMC), called RAOQ. The method consists of two steps: 1) activation shifting (A-shift) and weight reshaping (W-reshape) to maximize the SQNR following ADC quantization; and 2) bit augmentation (BitAug) to improve the optimization process. The authors evaluate the proposed method on various datasets and models, and show that it can achieve high accuracy with low-precision ADCs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective, and can address a key challenge in IMC, i.e., ADC quantization.
3. The experiments are comprehensive and convincing, and the results demonstrate the superiority of the proposed method over existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide any details on the hardware implementation of the proposed method, such as the area, power, and latency overhead of the additional operations and parameters. This makes it difficult to assess the practical feasibility and cost-effectiveness of the method for real-world applications. For example, the activation shifting (A-shift) and weight reshaping (W-reshape) operations may require additional logic and memory, which could increase the area and power consumption of the IMC system. Furthermore, the bit augmentation (BitAug) method may introduce additional latency during training, which could slow down the development cycle.
2. The paper does not compare the proposed method with other QAT methods that are not specific to IMC, such as LSQ, LSQ+, and DFQ. This makes it hard to evaluate the generality and competitiveness of the proposed method. While the authors focus on IMC, it is important to understand how the proposed method performs compared to other state-of-the-art QAT methods. For example, methods like LSQ and LSQ+ are known for their effectiveness in quantizing neural networks, and it is unclear how the proposed method compares to these methods in terms of accuracy and efficiency. The lack of comparison with these methods makes it difficult to assess the novelty and contribution of the proposed method.
3. The paper does not discuss the limitations and future directions of the proposed method. For example, how does the method perform on different IMC architectures, such as crossbar arrays with different sizes and aspect ratios? How does the method handle the non-idealities and variations of IMC devices, such as sneak paths and device variations? Addressing these questions would help to identify the potential challenges and opportunities for future research.

### Suggestions

The paper should include a more detailed analysis of the hardware implications of the proposed method. Specifically, the authors should provide an estimate of the area, power, and latency overhead of the A-shift, W-reshape, and BitAug operations. This could be done by providing a high-level architectural diagram of the proposed hardware implementation, along with a breakdown of the resources required for each operation. For example, the authors could estimate the number of logic gates, memory bits, and multiplexers required for the A-shift and W-reshape operations. Furthermore, the authors should provide an analysis of the power consumption of these operations, taking into account the switching activity and capacitance of the hardware components. Finally, the authors should estimate the latency introduced by these operations, considering the critical path delay and the number of clock cycles required for each operation. This analysis would help to assess the practical feasibility and cost-effectiveness of the proposed method for real-world applications.

To better evaluate the competitiveness of the proposed method, the authors should compare it with other state-of-the-art QAT methods that are not specific to IMC, such as LSQ, LSQ+, and DFQ. This comparison should be performed on the same datasets and models, using the same evaluation metrics. For example, the authors could compare the accuracy and efficiency of the proposed method with LSQ and LSQ+ on ImageNet and COCO datasets, using ResNet and YOLO models. Furthermore, the authors should analyze the differences in the quantization schemes and training procedures used by these methods, and discuss how these differences affect the performance of the proposed method. This comparison would help to understand the strengths and weaknesses of the proposed method, and to identify the areas where it can be further improved. The authors should also discuss the potential for combining the proposed method with other QAT methods to achieve even better performance.

The paper should also discuss the limitations and future directions of the proposed method. For example, the authors should investigate how the method performs on different IMC architectures, such as crossbar arrays with different sizes and aspect ratios. This could be done by simulating the proposed method on different crossbar array configurations, and analyzing the impact of the array size and aspect ratio on the accuracy and efficiency of the method. Furthermore, the authors should investigate how the method handles the non-idealities and variations of IMC devices, such as sneak paths and device variations. This could be done by incorporating realistic device models into the simulation, and analyzing the impact of these non-idealities on the performance of the method. Finally, the authors should discuss the potential for extending the proposed method to other types of neural networks, such as recurrent neural networks and graph neural networks. This discussion would help to identify the potential challenges and opportunities for future research.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
