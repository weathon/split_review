### Summary

This paper addresses the vulnerability of in-context learning (ICL) to demonstration permutation order, which can lead to instability in large language models (LLMs). The authors propose a novel framework called PEARL (Permutation-resilient learning) that leverages distributional robust optimization (DRO) to enhance the model's robustness against demonstration permutations. PEARL includes a hard permutation mining network (P-Net) that identifies the most challenging permutations for the LLM, and the LLM is trained to minimize the loss under the worst-case permutation. The authors demonstrate the effectiveness of PEARL through experiments on the LLaMA-3 model, showing significant improvements in both average and worst-case performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a novel approach to address the instability of ICL by leveraging DRO, which is a significant contribution to the field of LLMs.
- The use of P-Net to identify challenging permutations is innovative and efficient, avoiding the need for exhaustive search.
- The paper provides extensive experimental results, demonstrating the effectiveness of PEARL in improving both average and worst-case performance.
- The paper is well-written and easy to follow, with clear explanations of the proposed methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

 - The paper primarily focuses on the LLaMA-3 model, and it would be beneficial to see how PEARL performs on other LLMs, particularly those with different architectures or sizes.
- The computational cost of training P-Net and the LLM is not thoroughly discussed, which could be a concern for practical applications.
- The paper could benefit from a more detailed analysis of the types of permutations that PEARL is most effective against, and whether there are specific patterns or characteristics that make certain permutations more challenging.
- The paper does not explore the potential limitations of PEARL, such as scenarios where it might not be effective or could even degrade performance.

### Suggestions

The authors should provide a more comprehensive evaluation of PEARL across a wider range of LLMs, including models with different architectures (e.g., encoder-decoder models, models with different attention mechanisms) and varying parameter sizes. This would help to establish the generalizability of the proposed method and identify any potential architecture-specific limitations. For example, it would be valuable to see how PEARL performs on models that use different types of attention mechanisms or those that have been trained with different pre-training objectives. Furthermore, the authors should investigate the impact of the P-Net's architecture and hyperparameters on the overall performance of PEARL. A sensitivity analysis of these parameters would provide valuable insights into the robustness and reliability of the method. It is also important to analyze the computational overhead introduced by PEARL, especially in comparison to standard ICL. This analysis should include not only the training time but also the inference time, as the permutation process could potentially slow down the model. 

To better understand the behavior of PEARL, the authors should conduct a more in-depth analysis of the types of permutations that are most effectively handled by the method. This could involve categorizing permutations based on their structure or the semantic relationships between the demonstrations, and then analyzing how PEARL performs on each category. For example, are permutations that reorder similar demonstrations more challenging than those that reorder dissimilar ones? Are there specific patterns of permutation that lead to the most significant performance drops? This analysis could provide valuable insights into the underlying mechanisms of ICL instability and guide the development of more effective mitigation strategies. Additionally, the authors should explore the limitations of PEARL, such as scenarios where it might fail to improve performance or even degrade it. This could involve testing PEARL on tasks that are inherently robust to demonstration order or on tasks where the optimal demonstration order is highly task-specific and difficult to learn using PEARL. 

Finally, the authors should consider exploring alternative methods for generating challenging permutations, beyond the hard permutation mining network (P-Net). For example, they could investigate using reinforcement learning to train an agent that generates permutations that are specifically designed to challenge the LLM. This could potentially lead to more effective and efficient methods for improving the robustness of ICL. Furthermore, the authors should also consider the potential for combining PEARL with other techniques for improving the robustness of LLMs, such as adversarial training or data augmentation. This could lead to more comprehensive and effective methods for mitigating the instability of ICL. The authors should also consider the potential for using PEARL to improve the interpretability of LLMs by identifying the key demonstrations that are most important for a given task.

### Questions

- How does PEARL compare to other methods for improving the robustness of LLMs, such as adversarial training or data augmentation?
- Can the authors provide more details on the computational cost of training P-Net and the LLM, and how it scales with the size of the model and the number of demonstrations?
- Are there any specific scenarios or tasks where PEARL might not be effective or could even degrade performance?

### Rating

6

### Confidence

3

**********
