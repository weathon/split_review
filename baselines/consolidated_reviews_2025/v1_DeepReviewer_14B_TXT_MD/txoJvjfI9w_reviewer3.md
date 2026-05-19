### Summary

The paper addresses the instability of large language models (LLMs) in in-context learning (ICL) due to the sensitivity to the order of demonstrations. The authors propose a novel framework called PEARL (Permutation-resilient learning) to enhance the robustness of LLMs against different permutations of input demonstrations. PEARL employs a hard Permutation mining Network (P-Net) that uses optimal transport and the Sinkhorn algorithm to generate challenging permutations, combined with adversarial training to systematically improve LLM performance. The paper demonstrates that PEARL effectively mitigates permutation attacks and improves both average and worst-case performance across various tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to permutation resilience in LLMs using distributionally robust optimization (DRO) and a P-Net, which is a significant contribution to the field.
2. The methodology is well-supported by theoretical analysis and empirical results, showing improvements in both average and worst-case performance.
3. The paper is well-structured and clearly explains the problem, methodology, and results, making it accessible to readers with a background in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed analysis of the computational complexity and scalability of PEARL, especially when applied to very large language models.
2. There is a lack of discussion regarding the potential limitations or trade-offs introduced by the proposed method, which could provide a more balanced view of the framework's applicability.

### Suggestions

The paper should include a more rigorous analysis of the computational demands of the proposed PEARL framework, particularly concerning its application to large language models. While the authors mention the use of a smaller P-Net, a detailed breakdown of the computational cost associated with the Sinkhorn algorithm and the adversarial training process is needed. Specifically, the analysis should consider the time complexity of the Sinkhorn algorithm in relation to the size of the input permutations and the number of iterations required for convergence. Furthermore, the paper should discuss the memory footprint of PEARL, especially when dealing with large language models, and how this might impact its scalability. It would be beneficial to see a comparison of the computational resources required by PEARL versus standard training methods, including the number of FLOPs, memory usage, and training time, for different model sizes and permutation set sizes. This would provide a clearer understanding of the practical limitations of the approach and its applicability to real-world scenarios.

Additionally, the paper needs a more thorough discussion of the potential trade-offs and limitations introduced by the PEARL framework. While the authors claim that PEARL improves both worst-case and average performance, it is important to investigate whether this improvement comes at a cost. For instance, does the adversarial training process lead to overfitting on the permutation mining network (P-Net), and how does this affect the generalization performance of the LLM? The paper should also explore the sensitivity of PEARL to the choice of hyperparameters, such as the learning rate and the number of adversarial training iterations. A sensitivity analysis would help to understand the robustness of the framework and its practical applicability. Furthermore, the paper should discuss the potential limitations of PEARL in handling more complex input structures or tasks, beyond the simple permutation of demonstrations. It is important to understand the scope of the proposed method and its limitations in real-world scenarios.

Finally, the paper should provide more insights into the convergence properties of the adversarial training process between the P-Net and the LLM. While the authors mention that the P-Net aims to maximize the LLM's loss, and the LLM seeks to minimize it, a more detailed analysis of the convergence behavior is needed. Specifically, the paper should discuss whether the training process converges to a stable solution or oscillates between different states. It would be beneficial to see a convergence analysis, including the loss curves of both the P-Net and the LLM, and how these curves change over time. The paper should also discuss the potential for instability during the adversarial training process and how this can be mitigated. A more thorough understanding of the convergence properties of the framework would increase the reliability and reproducibility of the results.

### Questions

1. How does the computational complexity of PEARL scale with the size of the language model and the number of permutations considered?
2. Are there any trade-offs or potential performance degradations in certain scenarios when using PEARL compared to standard training methods?
3. How does the framework ensure convergence during the adversarial training process between the P-Net and the LLM, and what measures are in place to prevent overfitting?

### Rating

6

### Confidence

4

**********
