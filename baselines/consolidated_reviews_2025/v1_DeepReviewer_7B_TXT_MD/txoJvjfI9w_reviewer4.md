### Summary

This paper addresses the vulnerability of in-context learning (ICL) in large language models (LLMs) to the order of demonstrations. The authors propose a novel Permutation-resilient learning (PEARL) framework based on distributional robust optimization (DRO), which optimizes the model to handle the worst-case permutations. The framework includes a hard permutation mining network (P-Net) that generates challenging permutations and adversarial training to improve the model's robustness. Experimental results show that PEARL significantly improves both average and worst-case performance across various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to enhance the robustness of LLMs against demonstration permutations in in-context learning (ICL). By leveraging distributional robust optimization (DRO), the authors address a significant vulnerability in LLMs, where the order of demonstrations can drastically impact performance.
- The proposed Permutation-resilient learning (PEARL) framework is well-motivated and technically sound. The use of a hard permutation mining network (P-Net) to identify challenging permutations is innovative and effective. The adversarial training process further enhances the model's robustness by exposing it to a wide range of permutations.
- The paper provides extensive experimental results across various tasks, demonstrating the effectiveness of PEARL in improving both average and worst-case performance. The results are consistent and show significant improvements over baseline methods.

### Weaknesses

#### Some Related Works


#### comment

 - While the paper demonstrates the effectiveness of PEARL, it could benefit from a more in-depth analysis of the computational cost associated with the proposed framework. Understanding the trade-offs between performance gains and computational resources is crucial for practical applications.
- The paper could explore the limitations of PEARL in scenarios where the number of demonstrations is very large or when the demonstrations are highly diverse. It would be valuable to understand how the framework scales with increasing input complexity and whether there are any specific types of demonstrations that pose challenges for PEARL.
- The paper primarily focuses on empirical results. A more theoretical analysis of the proposed framework could provide deeper insights into its behavior and limitations. For example, it would be interesting to analyze the convergence properties of the adversarial training process and the generalization bounds of the model under different permutation scenarios.

### Suggestions

The paper introduces an interesting approach to improve the robustness of in-context learning (ICL) by addressing the vulnerability to demonstration permutation order. However, the practical applicability of the proposed Permutation-resilient learning (PEARL) framework hinges on a more thorough analysis of its computational demands. Specifically, the paper should include a detailed breakdown of the computational resources required for training and inference, including memory usage, training time, and inference latency. This analysis should consider the impact of different model sizes and the number of demonstrations on the overall computational cost. Furthermore, it would be beneficial to compare the computational overhead of PEARL with other existing methods for improving ICL robustness. This would allow practitioners to make informed decisions about the trade-offs between performance gains and computational resources, which is crucial for real-world deployment.

In addition to computational cost, the paper should also investigate the scalability of PEARL with respect to the number of demonstrations and the diversity of the input data. The current experiments seem to focus on relatively small numbers of demonstrations. It is important to understand how the performance of PEARL changes as the number of demonstrations increases, especially when the number of demonstrations approaches the model's context window size. Furthermore, the paper should explore the impact of diverse demonstrations on the effectiveness of PEARL. For instance, how does PEARL perform when the demonstrations are semantically unrelated or when they contain conflicting information? A more comprehensive analysis of these scenarios would provide a better understanding of the limitations of the proposed framework and its applicability to real-world problems. It would also be valuable to investigate whether the hard permutation mining network (P-Net) can effectively identify challenging permutations in these diverse scenarios.

Finally, while the empirical results are promising, the paper would benefit from a more rigorous theoretical analysis of the proposed framework. Specifically, it would be valuable to analyze the convergence properties of the adversarial training process. Does the training process guarantee convergence to a stable solution, and what are the conditions under which it might fail to converge? Furthermore, it would be interesting to explore the generalization bounds of the model under different permutation scenarios. What are the theoretical limits of the model's performance, and how does the number of demonstrations affect these limits? A more theoretical analysis would provide a deeper understanding of the behavior of PEARL and its limitations, and would also help to guide future research in this area.

### Questions

- How does the performance of PEARL vary with different model sizes and architectures? Are there any specific model characteristics that make PEARL more or less effective?
- What is the computational cost of training and inference with PEARL, and how does it compare to other methods for improving ICL robustness?
- How does PEARL perform in scenarios with a large number of demonstrations or highly diverse demonstrations? Are there any specific types of demonstrations that pose challenges for the framework?
- Can the authors provide a more detailed theoretical analysis of the proposed framework, including convergence properties and generalization bounds?

### Rating

8

### Confidence

3

**********
