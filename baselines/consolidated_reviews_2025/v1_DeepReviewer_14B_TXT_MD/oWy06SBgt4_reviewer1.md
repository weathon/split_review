### Summary

This paper proposes a method to push the limit of low-precision fully quantized training (in which weights, activations, and gradients are all quantized) to 1-bit. The paper provides a theoretical analysis of the convergence of FQT based on SGD and Adam, and introduces an Activation Gradient Pruning (AGP) strategy to reduce the variance of gradients. The paper also proposes Sample Channel joint Quantization (SCQ) to make the method more hardware-friendly. The experimental results show that the proposed method outperforms per-sample quantization on transfer learning tasks in both vision and NLP domains, and can achieve a significant training speedup on Hygon and Raspberry Pi devices.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper provides a theoretical analysis of the convergence of FQT based on SGD and Adam, and introduces an AGP strategy to reduce the variance of gradients. This is a novel approach to improving the convergence of FQT.
- The paper proposes SCQ to make the method more hardware-friendly. This is a practical consideration that is often overlooked in research.
- The experimental results show that the proposed method outperforms per-sample quantization on transfer learning tasks in both vision and NLP domains. This demonstrates the effectiveness of the proposed method on a range of tasks.
- The paper implements the algorithm on Hygon and Raspberry Pi devices and achieves a significant training speedup compared to FP32 PyTorch. This shows the practical benefits of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only explores transfer learning tasks, and does not provide any results for training from scratch. This is a significant limitation, as training from scratch is a more challenging task that is more representative of real-world scenarios. The lack of results for training from scratch makes it difficult to assess the generalizability of the proposed method.
- The paper does not compare the proposed method to other low-precision training methods, such as 4-bit or 8-bit FQT. This makes it difficult to assess the relative performance of the proposed method. It is unclear whether the proposed 1-bit method offers a significant advantage over slightly higher precision methods, especially considering the potential for increased training instability at such low bitwidths.
- The paper does not provide any results for training large models, such as those with billions of parameters. This is a significant limitation, as training large models is becoming increasingly important in deep learning. The absence of results on large models leaves open the question of whether the proposed method can scale to the sizes required for state-of-the-art performance in many domains.
- The paper does not discuss the limitations of the proposed method in detail. This makes it difficult to assess the potential drawbacks of the method. For example, the paper does not discuss the potential for increased training instability due to the use of 1-bit quantization, or the potential for accuracy loss due to the pruning of activation gradients. A more thorough discussion of these limitations would be beneficial.

### Suggestions

The paper would benefit significantly from a more thorough evaluation of the proposed method. Specifically, the authors should include results for training models from scratch, not just transfer learning. This would provide a more realistic assessment of the method's capabilities and limitations. Furthermore, it would be valuable to compare the proposed 1-bit method against other low-precision training methods, such as 4-bit and 8-bit FQT. This would help to determine the trade-offs between precision and performance, and to identify the scenarios where the 1-bit method is most effective. The comparison should include not only final accuracy but also training stability and convergence speed. It is important to understand if the 1-bit method introduces any specific challenges in these areas compared to higher precision methods.

Additionally, the paper should include results for training larger models, such as those with billions of parameters. This would demonstrate the scalability of the proposed method and its applicability to more complex tasks. The authors should also provide a more detailed discussion of the limitations of the proposed method. This should include a discussion of the potential for increased training instability due to the use of 1-bit quantization, and the potential for accuracy loss due to the pruning of activation gradients. The authors should also discuss the computational overhead of the proposed method, and how it compares to other low-precision training methods. A thorough analysis of these limitations would provide a more balanced assessment of the proposed method and help to identify areas for future research.

Finally, the paper should provide more details on the implementation of the proposed method. This should include details on the specific hardware and software used, as well as the specific quantization and pruning techniques. The authors should also provide a more detailed analysis of the computational speedup achieved by the proposed method. This should include a breakdown of the time spent on different operations, such as forward propagation, backward propagation, and parameter updates. This would help to identify the bottlenecks in the training process and to guide future optimization efforts. The authors should also discuss the memory footprint of the proposed method, and how it compares to other low-precision training methods.

### Questions

- How does the proposed method perform on tasks other than transfer learning, such as training from scratch?
- How does the proposed method compare to other low-precision training methods, such as 4-bit or 8-bit FQT?
- How does the proposed method perform on large models with billions of parameters?
- What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

3

### Confidence

4

**********
