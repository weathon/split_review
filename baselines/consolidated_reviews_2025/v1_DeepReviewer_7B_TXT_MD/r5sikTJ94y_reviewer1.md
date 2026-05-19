### Summary

This paper introduces RAOQ, a method to mitigate ADC quantization errors in IMC. RAOQ comprises three key components: 1) Activation shifting (A-shift) to shift activations to avoid zero, 2) Weight reshaping (W-reshape) to increase the variance of weights, and 3) Bit augmentation (BitAug) to adapt to ADC quantization. Experimental results demonstrate that RAOQ achieves high accuracy across various tasks, including image classification, object detection, and NLP, even with limited ADC bit precisions.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow.
2. The proposed method is straightforward and easy to implement.
3. The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation is unclear. It is not clear why the authors emphasize the importance of ADC quantization. In the introduction, the authors mention that ADC quantization is a major source of quantization error and that previous works have focused on hardware design to address this issue. However, the authors do not explain why ADC quantization is particularly important for IMC. The paper lacks a clear explanation of how ADC quantization impacts the performance of In-Memory Computing (IMC) systems, especially given that the core argument is that IMC is designed to avoid memory access bottlenecks. The paper needs to articulate why ADC quantization is a critical concern that needs to be addressed specifically for IMC, rather than just being a general quantization issue.
2. The novelty is limited. The proposed method is similar to previous methods, such as quantization-aware training (QAT) and bit augmentation (BitAug). The paper does not sufficiently differentiate the proposed method from existing techniques. The A-shift and W-reshape techniques, while presented as novel, bear a strong resemblance to existing methods in the literature. The paper needs to provide a more detailed analysis of how these techniques differ from and improve upon existing approaches, particularly in the context of IMC.
3. The experiments are insufficient. The paper does not include experiments on large language models (LLMs) or experiments on the latest hardware platforms. The experiments are limited in scope and do not adequately demonstrate the generalizability of the proposed method. The absence of experiments on large language models, which are increasingly important in many applications, raises concerns about the practical applicability of the method. Furthermore, the lack of experiments on the latest hardware platforms limits the relevance of the results in real-world scenarios.

### Suggestions

The paper should begin by clearly articulating the specific challenges posed by ADC quantization within the context of In-Memory Computing (IMC). It needs to explain why ADC quantization is a critical concern for IMC systems, especially given that IMC is designed to mitigate memory access bottlenecks. The authors should provide a detailed analysis of how ADC quantization impacts the performance of IMC systems, including the specific types of errors that can arise and their consequences. This analysis should go beyond simply stating that ADC quantization is a source of error and should explain why it is a particularly challenging problem for IMC. For example, the authors could discuss how the analog nature of ADCs introduces noise and quantization errors that can propagate through the IMC system and degrade the accuracy of the computations. This would help to establish the motivation for the proposed method and justify its importance.

To address the limited novelty, the authors should provide a more detailed comparison of their method with existing quantization-aware training (QAT) and bit augmentation (BitAug) techniques. The paper should clearly delineate the differences between the proposed method and existing approaches, highlighting the unique contributions of the proposed method. For example, the authors could discuss how the A-shift and W-reshape techniques differ from existing methods in terms of their implementation, computational complexity, and impact on the performance of IMC systems. The authors should also provide a theoretical analysis of the proposed method, demonstrating why it is expected to be more effective than existing approaches. This analysis should include a discussion of the mathematical properties of the proposed method and how they contribute to its effectiveness. Furthermore, the authors should provide a more detailed explanation of the BitAug technique and how it differs from existing bit augmentation methods.

Finally, the paper needs to include more comprehensive experimental results to demonstrate the generalizability and practical applicability of the proposed method. The authors should include experiments on large language models (LLMs) to show that the method is effective for a wide range of applications. The experiments should also be conducted on the latest hardware platforms to ensure that the results are relevant to real-world scenarios. The authors should also provide a detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and the areas where further research is needed. This analysis should include a comparison of the proposed method with existing approaches, highlighting the advantages and disadvantages of each method. The authors should also provide a discussion of the computational cost of the proposed method and how it compares to existing approaches.

### Questions

1. What is the motivation for emphasizing ADC quantization?
2. What is the novelty of the proposed method?
3. What are the experiments on LLMs and the latest hardware platforms?

### Rating

3

### Confidence

3

**********
