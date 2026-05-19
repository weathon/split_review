### Summary

The paper proposes a 1-bit full quantization training (FQT) method for deep neural networks, aiming to achieve the ultimate limit of FQT (the lowest achievable bitwidth). The authors provide a theoretical analysis of FQT based on both Adam and SGD optimizers. They introduce two techniques: Activation Gradient Pruning (AGP) and Sample Channel joint Quantization (SCQ), which reduce gradient variance and enhance the numerical precision of remaining gradients. The experimental results demonstrate that the proposed method achieves an average accuracy improvement of approximately 5% compared to previous FQT methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a theoretical analysis of the convergence of FQT under both Adam and SGD optimizers, which is valuable for understanding the behavior of FQT.
2. The proposed AGP and SCQ techniques effectively reduce gradient variance and enhance numerical precision, which is a significant contribution to the field of quantization.
3. The paper is well-structured and clearly written, making it easy to follow and understand.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with existing 1-bit quantization methods, particularly those that focus on training from scratch rather than transfer learning. The current comparison is limited to basic QAT and PSQ, which are not the most relevant baselines for evaluating 1-bit training. A more thorough comparison with methods that specifically address the challenges of 1-bit training, such as those employing adaptive quantization or mixed-precision techniques, would be necessary to contextualize the contribution of this work. The absence of such comparisons makes it difficult to assess the true novelty and effectiveness of the proposed approach.
2. The experimental results are primarily focused on transfer learning tasks, which may not fully demonstrate the capabilities of the proposed method in a broader range of applications. The paper does not explore the performance of the method on training from scratch or on different types of tasks, such as those with more complex data distributions or model architectures. This limited scope of evaluation raises concerns about the generalizability of the findings and the practical applicability of the method in diverse scenarios. The lack of experiments on training from scratch, in particular, is a significant gap, as this is a key area where full quantization techniques are most needed.
3. The paper does not provide a detailed analysis of the computational overhead introduced by the proposed techniques, such as AGP and SCQ. While the authors mention a speedup, a more detailed breakdown of the computational cost associated with each component of the method is needed. This should include a comparison of the runtime and memory usage of the proposed method with the baseline methods, as well as an analysis of the impact of these techniques on the overall training time and resource consumption. Without this detailed analysis, it is difficult to assess the practical efficiency of the proposed method.

### Suggestions

To strengthen the paper, the authors should significantly expand the experimental evaluation to include a more comprehensive comparison with state-of-the-art 1-bit quantization methods, particularly those designed for training from scratch. This should include a detailed analysis of the performance of the proposed method against methods that employ adaptive quantization or mixed-precision techniques. The comparison should not only focus on accuracy but also on other metrics such as training time, memory usage, and convergence speed. Furthermore, the authors should provide a more detailed analysis of the differences between their method and these existing approaches, highlighting the specific advantages and disadvantages of each. This would help to better contextualize the contribution of the proposed method and demonstrate its novelty and effectiveness.

In addition to expanding the experimental evaluation, the authors should also include experiments on training from scratch and on a wider range of tasks and datasets. This should include experiments on datasets with more complex data distributions and model architectures, as well as tasks that are more challenging for quantized training. The authors should also provide a detailed analysis of the performance of the method on these different tasks and datasets, highlighting any limitations or challenges that they encountered. This would help to demonstrate the generalizability of the method and its practical applicability in diverse scenarios. The lack of experiments on training from scratch is a significant gap, and the authors should address this by including such experiments to validate the method's effectiveness in a more fundamental setting.

Finally, the authors should provide a more detailed analysis of the computational overhead introduced by the proposed techniques, such as AGP and SCQ. This should include a breakdown of the runtime and memory usage of each component of the method, as well as a comparison of the overall training time and resource consumption with the baseline methods. The authors should also discuss the trade-offs between accuracy and computational efficiency, and how their method balances these two factors. This would help to better understand the practical efficiency of the proposed method and its suitability for different applications. Without this detailed analysis, it is difficult to assess the practical applicability of the proposed method.

### Questions

1. How does the proposed method perform on training from scratch, and how does it compare to other 1-bit quantization methods in this scenario?
2. What is the computational overhead of the proposed techniques, such as AGP and SCQ, compared to the baseline methods?
3. How does the proposed method perform on different types of tasks and datasets, and how does it compare to other 1-bit quantization methods in these scenarios?

### Rating

6

### Confidence

4

**********
