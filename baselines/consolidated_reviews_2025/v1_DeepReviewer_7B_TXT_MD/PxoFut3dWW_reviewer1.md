### Summary

This paper proposes a pruning approach for large language models (LLMs) that uses a simple yet effective metric to prune weights without the need for retraining. The authors introduce Wanda, a pruning method that considers both weight magnitude and input activation norms, allowing it to effectively prune LLMs while maintaining performance. The method is evaluated on several LLMs, showing competitive results compared to existing pruning techniques.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.
- The proposed pruning method is simple and easy to implement, yet it achieves competitive results compared to existing pruning techniques.

### Weaknesses

#### Some Related Works

[1] SparseGPT: Massive Language Models Can Be Accurately Pruned at Initialization
[2] ShortGPT: Fine-tuning Small Language Models using Generative Pretrained Transformer
[3] AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration
[4] SparseLLM: A Sparse Training Paradigm for Efficient LLM Inference
[5] SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs

#### comment

 - The paper lacks a comparison with recent pruning methods such as SparseGPT [1], ShortGPT [2], AWQ [3], SparseLLM [4], and SmoothQuant [5], which are all mentioned in the related work section.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, especially in comparison to other pruning techniques.
- The paper does not discuss the potential impact of the proposed method on the robustness of the pruned models.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameter settings.
- The paper does not discuss the potential limitations of the proposed method in terms of its applicability to different types of LLMs or tasks.

### Suggestions

The paper should include a more thorough comparison with recent pruning methods, such as SparseGPT, ShortGPT, AWQ, SparseLLM, and SmoothQuant. This comparison should not only focus on performance metrics but also on computational cost, memory usage, and the complexity of implementation. A detailed analysis of the trade-offs between these methods would provide a more comprehensive understanding of the proposed method's strengths and weaknesses. For example, the authors could compare the number of FLOPs required for pruning and inference, the memory footprint of the pruned models, and the ease of implementation for each method. This would allow readers to better assess the practical value of the proposed method in different scenarios. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method, especially in comparison to other pruning techniques. This analysis should include the time required for pruning, the memory usage during pruning, and the impact on inference speed. It would be beneficial to provide a breakdown of the computational cost for different parts of the method, such as the calculation of the pruning metric and the actual pruning operation. This would help readers understand the computational overhead of the proposed method and its suitability for different applications. 

The paper should also include a discussion on the potential impact of the proposed method on the robustness of the pruned models. It is important to investigate whether the pruning method affects the model's sensitivity to adversarial attacks or noisy inputs. This analysis should include experiments that evaluate the robustness of the pruned models under different attack scenarios. For example, the authors could evaluate the models' performance against adversarial examples generated using different attack methods. Additionally, the authors should analyze the sensitivity of the proposed method to different hyperparameter settings. This analysis should include a discussion of how the performance of the pruned models varies with different values of the hyperparameters, such as the pruning rate and the threshold for weight removal. The authors should provide guidelines for selecting appropriate hyperparameter values to achieve the best performance. This would help readers understand the robustness of the proposed method and its sensitivity to different settings. 

Finally, the paper should discuss the potential limitations of the proposed method in terms of its applicability to different types of LLMs or tasks. The authors should investigate whether the proposed method is effective for different model architectures, such as encoder-decoder models or models with different activation functions. It would also be beneficial to evaluate the method on a wider range of tasks, such as text classification, question answering, and machine translation. This would provide a more comprehensive understanding of the method's applicability and limitations. The authors should also discuss the potential challenges of applying the proposed method to very large models or models with complex architectures. This would help readers understand the limitations of the proposed method and its potential for future research.

### Questions

- How does the proposed method compare to recent pruning techniques in terms of performance, computational cost, and memory usage?
- What is the impact of the proposed method on the robustness of the pruned models?
- How sensitive is the proposed method to different hyperparameter settings?
- How does the proposed method perform on different types of LLMs or tasks?

### Rating

5

### Confidence

4

**********
