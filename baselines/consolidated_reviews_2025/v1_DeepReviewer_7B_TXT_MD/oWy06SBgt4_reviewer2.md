### Summary

This paper explores the possibility of achieving 1-bit full quantization training (FQT) for deep neural networks. The authors provide a theoretical analysis of the convergence of FQT under both Adam and SGD optimizers. They also introduce an Activation Gradient Pruning (AGP) strategy to reduce gradient variance and propose a Sample Channel joint Quantization (SCQ) method to accelerate the computation of weight gradients. Experimental results demonstrate that the proposed method achieves an average accuracy improvement of approximately 5% compared to directly applying previous full quantization methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the convergence of 1-bit full quantization training under both Adam and SGD optimizers, which is a valuable contribution to the field.
3. The proposed AGP and SCQ methods are novel and effective in reducing gradient variance and accelerating the computation of weight gradients, respectively.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive comparison with existing 1-bit quantization methods, particularly those that focus on training from scratch rather than transfer learning. The current comparison is limited to basic QAT and PSQ, which are not the most relevant baselines for evaluating 1-bit training. A more thorough comparison with methods that specifically address the challenges of 1-bit training, such as those employing adaptive quantization or mixed-precision techniques, would be necessary to contextualize the contribution of this work. The absence of such comparisons makes it difficult to assess the true novelty and effectiveness of the proposed approach.
2. The experimental results are primarily focused on transfer learning tasks, which may not fully demonstrate the capabilities of the proposed method in a broader range of applications. The paper does not explore the performance of the method on training from scratch or on different types of tasks, such as those with more complex data distributions or model architectures. This limited scope of evaluation raises concerns about the generalizability of the findings and the practical applicability of the method in diverse scenarios. The lack of experiments on training from scratch, in particular, is a significant gap, as this is a key area where full quantization techniques are most needed.
3. The paper does not provide a detailed analysis of the computational overhead introduced by the proposed techniques, such as AGP and SCQ. While the authors mention a speedup, a more detailed breakdown of the computational cost associated with each component of the method is needed. This should include a comparison of the runtime and memory usage of the proposed method with the baseline methods, as well as an analysis of the impact of these techniques on the overall training time and resource consumption. Without this detailed analysis, it is difficult to assess the practical efficiency of the proposed method.

### Suggestions

To address the lack of comprehensive comparisons, the authors should include a more detailed comparison with state-of-the-art 1-bit quantization methods, especially those that focus on training from scratch. This should include methods that employ adaptive quantization or mixed-precision techniques, as these are more relevant baselines for evaluating 1-bit training. The comparison should not only focus on accuracy but also on other metrics such as training time, memory usage, and convergence speed. Furthermore, the authors should provide a more detailed analysis of the differences between their method and these existing approaches, highlighting the specific advantages and disadvantages of each. This would help to better contextualize the contribution of the proposed method and demonstrate its novelty and effectiveness. The authors should also consider including a discussion of the limitations of their approach compared to other methods, which would provide a more balanced view of the work.

To address the limited scope of experimental evaluation, the authors should include experiments on training from scratch, as well as on a wider range of tasks and datasets. This should include experiments on datasets with more complex data distributions and model architectures, as well as tasks that are more challenging for quantized training. The authors should also provide a detailed analysis of the performance of the method on these different tasks and datasets, highlighting any limitations or challenges that they encountered. This would help to demonstrate the generalizability of the method and its practical applicability in diverse scenarios. Furthermore, the authors should consider including experiments on different hardware platforms to evaluate the performance of the method in different settings. This would help to assess the practical efficiency of the proposed method and its suitability for different applications.

To address the lack of detailed analysis of the computational overhead, the authors should provide a more detailed breakdown of the computational cost associated with each component of the method, including AGP and SCQ. This should include a comparison of the runtime and memory usage of the proposed method with the baseline methods, as well as an analysis of the impact of these techniques on the overall training time and resource consumption. The authors should also provide a discussion of the trade-offs between accuracy and computational efficiency, and how their method balances these two factors. This would help to better understand the practical efficiency of the proposed method and its suitability for different applications. The authors should also consider including a discussion of the potential for further optimization of the proposed techniques to reduce their computational overhead.

### Questions

1. How does the proposed method perform on training from scratch, and how does it compare to other 1-bit quantization methods in this scenario?
2. What is the computational overhead of the proposed techniques, such as AGP and SCQ, compared to the baseline methods?
3. How does the proposed method perform on different types of tasks and datasets, and how does it compare to other 1-bit quantization methods in these scenarios?

### Rating

6

### Confidence

3

**********
