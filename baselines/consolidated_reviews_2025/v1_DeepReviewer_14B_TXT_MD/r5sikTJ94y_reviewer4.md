### Summary

The paper proposes a quantization-aware training (QAT) method for in-memory computing (IMC) systems. The proposed method, RAOQ, consists of two steps: 1) activation shifting (A-shift) and weight reshaping (W-reshape) to maximize the SQNR following ADC quantization; and 2) bit augmentation (BitAug) to improve the optimization process. The authors evaluate the proposed method on various datasets and models, and show that it can achieve high accuracy with low-precision ADCs.

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

1. The paper does not provide any details on the hardware implementation of the proposed method, such as the area, power, and latency overhead of the additional operations and parameters. This makes it difficult to assess the practical feasibility and cost-effectiveness of the method for real-world applications.
2. The paper does not compare the proposed method with other QAT methods that are not specific to IMC, such as LSQ, LSQ+, and DFQ. This makes it hard to evaluate the generality and competitiveness of the proposed method.
3. The paper does not discuss the limitations and future directions of the proposed method.

### Suggestions

The paper would benefit significantly from a more detailed discussion of the hardware implications of the proposed RAOQ method. While the focus is on algorithmic improvements, the practical viability of any in-memory computing (IMC) solution hinges on its hardware efficiency. Specifically, the authors should provide an analysis of the area, power, and latency overhead introduced by the activation shifting (A-shift), weight reshaping (W-reshape), and bit augmentation (BitAug) operations. This analysis should consider the specific hardware primitives required for these operations within an IMC architecture, such as additional analog circuits for shifting or digital control logic for weight reshaping. Furthermore, the authors should discuss how these overheads scale with the size of the IMC array and the precision of the analog-to-digital converters (ADCs). Without this information, it is difficult to assess the practical trade-offs between accuracy gains and hardware costs, which is crucial for real-world deployment.

To better contextualize the performance of RAOQ, the authors should include a comparison with established quantization-aware training (QAT) methods that are not specific to IMC, such as LSQ, LSQ+, and DFQ. This comparison should be performed on a common set of benchmarks and with similar model architectures to ensure a fair evaluation. The authors should analyze the differences in the quantization schemes, training procedures, and hyperparameter settings between RAOQ and these other methods. This would help to clarify whether the performance gains of RAOQ are primarily due to its specific design for IMC or if it offers a more general advantage over existing QAT techniques. Furthermore, the authors should discuss the potential for adapting RAOQ to other hardware platforms beyond IMC, which would broaden the impact of their work.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors should discuss the sensitivity of RAOQ to the choice of hyperparameters, the robustness of the method to variations in ADC characteristics, and the scalability of the approach to larger and more complex models. The authors should also explore the potential for combining RAOQ with other techniques, such as network pruning or knowledge distillation, to further improve the efficiency and accuracy of IMC systems. Addressing these limitations and outlining future research directions would strengthen the paper and provide a more complete picture of the proposed method.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
