### Summary

This paper proposes a method to quantize neural networks to 1-bit, which is a challenging task. The authors provide a theoretical analysis of the convergence of 1-bit full quantization training (FQT) under both Adam and SGD optimizers. They also introduce two techniques, Activation Gradient Pruning (AGP) and Sample Channel joint Quantization (SCQ), to reduce gradient variance and enhance the numerical precision of remaining gradients. The method is evaluated on transfer learning tasks using ResNet-18 and VGGNet-16, achieving an average accuracy improvement of approximately 5% compared to previous FQT methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a theoretical analysis of the convergence of 1-bit full quantization training (FQT) under both Adam and SGD optimizers. This analysis is important for understanding the behavior of 1-bit FQT and for guiding the development of future methods.
- The proposed method achieves an average accuracy improvement of approximately 5% compared to previous FQT methods on transfer learning tasks using ResNet-18 and VGGNet-16.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a comprehensive comparison with existing 1-bit quantization methods, particularly those that focus on training from scratch rather than transfer learning. The current comparison is limited to basic QAT and PSQ, which are not the most relevant baselines for evaluating 1-bit training. A more thorough comparison with methods that specifically address the challenges of 1-bit training, such as those employing adaptive quantization or mixed-precision techniques, would be necessary to contextualize the contribution of this work. The absence of such comparisons makes it difficult to assess the true novelty and effectiveness of the proposed approach.
- The experimental results are primarily focused on transfer learning tasks, which may not fully demonstrate the capabilities of the proposed method in a broader range of applications. The paper does not explore the performance of the method on training from scratch or on different types of tasks, such as those with more complex data distributions or model architectures. This limited scope of evaluation raises concerns about the generalizability of the findings and the practical applicability of the method in diverse scenarios. The lack of experiments on training from scratch, in particular, is a significant gap, as this is a key area where full quantization techniques are most needed.
- The paper does not provide a detailed analysis of the computational overhead introduced by the proposed techniques, such as AGP and SCQ. While the authors mention a speedup, a more detailed breakdown of the computational cost associated with each component of the method is needed. This should include a comparison of the runtime and memory usage of the proposed method with the baseline methods, as well as an analysis of the impact of these techniques on the overall training time and resource consumption. Without this detailed analysis, it is difficult to assess the practical efficiency of the proposed method.

### Suggestions

The paper would benefit significantly from a more comprehensive experimental evaluation. Specifically, the authors should include a comparison with state-of-the-art 1-bit quantization methods that are designed for training from scratch, not just basic QAT and PSQ. This would provide a more accurate assessment of the proposed method's performance and its advantages over existing techniques. The comparison should not only focus on accuracy but also consider other metrics such as training time, memory usage, and convergence speed. Furthermore, the authors should evaluate their method on a wider range of tasks and datasets, including those with more complex data distributions and model architectures. This would help to demonstrate the generalizability of the method and its applicability to diverse scenarios. For example, experiments on datasets with higher dimensionality or more complex relationships between features would be valuable.

In addition to expanding the experimental evaluation, the authors should also provide a more detailed analysis of the computational overhead introduced by their proposed techniques. This analysis should include a breakdown of the runtime and memory usage of each component of the method, such as AGP and SCQ, and a comparison with the baseline methods. The authors should also discuss the trade-offs between accuracy and computational efficiency, and how their method balances these two factors. This would help to better understand the practical applicability of the proposed method and its suitability for different applications. For example, a detailed analysis of the memory footprint of the proposed method compared to existing 1-bit quantization techniques would be beneficial.

Finally, the authors should clarify the specific scenarios where their method is most effective and where it may not be suitable. For example, they should discuss the limitations of their method in terms of model architecture, dataset complexity, and training data size. This would help to provide a more balanced and realistic assessment of the proposed method's capabilities and limitations. The authors should also discuss the potential for future work, such as exploring alternative techniques for reducing gradient variance or enhancing numerical precision, and how these techniques could be integrated into the proposed method.

### Questions

- How does the proposed method perform on training from scratch, and how does it compare to other 1-bit quantization methods in this scenario?
- What is the computational overhead of the proposed techniques, such as AGP and SCQ, compared to the baseline methods?
- How does the proposed method perform on different types of tasks and datasets, and how does it compare to other 1-bit quantization methods in these scenarios?

### Rating

6

### Confidence

3

**********
