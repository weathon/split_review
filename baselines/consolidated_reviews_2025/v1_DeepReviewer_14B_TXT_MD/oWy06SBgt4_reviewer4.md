### Summary

This paper proposes a 1-bit fully quantized training (FQT) method. The authors first provide a theoretical analysis of FQT based on Adam and SGD, revealing that the gradient variance influences the convergence of FQT. Then, they introduce an Activation Gradient Pruning (AGP) strategy to reduce the variance of the quantizer. Finally, they propose a Sample Channel joint Quantization (SCQ) strategy to address the issue of unaccelerated weight gradient computation. The authors conduct experiments on various datasets and models, demonstrating the effectiveness of their proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to understand.
2. The authors provide a theoretical analysis of FQT based on Adam and SGD, which is a valuable contribution to the field.
3. The proposed AGP and SCQ strategies are novel and effective in reducing the variance of the quantizer and accelerating weight gradient computation.
4. The authors conduct extensive experiments on various datasets and models, demonstrating the effectiveness of their proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other state-of-the-art 1-bit quantization methods. It would be beneficial to compare the proposed method with other existing methods to demonstrate its superiority.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. It is important to analyze the computational cost of the proposed method to understand its practicality.
3. The paper does not discuss the limitations of the proposed method. It is important to discuss the limitations of the proposed method to understand its applicability.

### Suggestions

The paper would benefit significantly from a more thorough comparison against existing 1-bit quantization techniques. While the authors introduce novel AGP and SCQ strategies, a direct comparison with established methods, even if those methods are not directly applicable to the FQT setting, would provide valuable context. For example, a comparison could be made against methods that use similar quantization techniques but in a different training regime, such as post-training quantization or quantization-aware training. This would help to clarify the specific advantages of the proposed method in the FQT setting and highlight the unique contributions of AGP and SCQ. Furthermore, the authors should consider including a discussion of the trade-offs between the proposed method and existing techniques, such as the computational overhead of AGP and SCQ compared to simpler quantization methods. This would provide a more complete picture of the practical implications of the proposed approach.

In addition to the comparison with other methods, a more detailed analysis of the computational cost is needed. The paper should include a breakdown of the computational cost of each component of the proposed method, including the AGP and SCQ strategies. This analysis should consider both the forward and backward passes, as well as the overhead of the quantization and dequantization operations. It would also be beneficial to analyze the memory footprint of the proposed method, as this can be a limiting factor in practical applications. The authors should also discuss the potential for optimizing the implementation of the proposed method to reduce its computational cost. For example, they could explore the use of specialized hardware or optimized libraries to accelerate the computation. This would help to make the proposed method more practical and accessible to a wider range of users.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the authors mention that their method is applicable to convolutional neural networks, they should also discuss the potential challenges of applying the method to other types of neural networks, such as recurrent neural networks or transformers. The authors should also discuss the potential impact of the proposed method on the accuracy of the trained models, as well as the sensitivity of the method to hyperparameter settings. Furthermore, the authors should discuss the potential for extending the proposed method to other quantization levels, such as 2-bit or 4-bit quantization. This would help to provide a more complete understanding of the applicability and limitations of the proposed method.

### Questions

1. Can the authors provide a comparison with other state-of-the-art 1-bit quantization methods?
2. Can the authors provide a detailed analysis of the computational cost of the proposed method?
3. Can the authors discuss the limitations of the proposed method?

### Rating

6

### Confidence

4

**********
