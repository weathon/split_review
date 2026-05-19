### Summary

The paper introduces a token-level pruning method for large language models (LLMs). FTP addresses the high computational demands of LLMs by developing a framework that prunes tokens based on their importance, thereby reducing inference costs without significant performance degradation. The method uses a learnable router to identify and skip less important tokens across model blocks, and it incorporates a search-based sparsity scheduler to allocate sparsity ratios for each block. The authors conduct extensive experiments on various LLMs, showing that FTP achieves better accuracy retention compared to other state-of-the-art pruning methods at similar sparsity levels.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. FTP introduces a fine-grained, token-wise pruning approach, which is more nuanced compared to traditional methods that often prune at the block or model level. The use of a learnable router to assess token importance on the fly is an advancement, allowing for more adaptive and context-sensitive pruning.
2. The paper provides a thorough set of experiments across different LLM architectures and benchmarks, demonstrating the effectiveness of FTP. The results indicate that FTP outperforms other pruning methods in terms of accuracy retention at comparable sparsity levels.
3. The motivation is clear: to reduce computational overhead in LLMs during inference without retraining, which is a significant issue in deploying these models in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from more detailed comparisons with recent token-level pruning methods, such as AOT-Sparse and Dynamic LLM Pruning, which also address token-level optimization in LLMs. 
2. The absence of complexity and memory cost analysis in the main text makes it challenging to evaluate the efficiency of FTP relative to other methods. 
3. The paper does not provide a clear explanation for why the methods mentioned in Weakness 1 perform worse than FTP in Table 1, especially considering that AOT-Sparse and Dynamic LLM Pruning achieve better performance than FTP in their original papers. Is the comparison in Table 1 based on reproducing their results within the FTP framework or on results reported in their respective papers? 
4. The lack of code and model availability hinders the reproducibility of the results, which is crucial for validating the claims made in the paper.

### Suggestions

The paper would significantly benefit from a more thorough analysis of the performance discrepancies between FTP and other token-level pruning methods, specifically AOT-Sparse and Dynamic LLM Pruning. The current comparison in Table 1 raises questions about whether the results for these methods are directly reproduced within the FTP framework or if they are taken from the original papers. If the results are reproduced, it is essential to detail the exact experimental setup, including any hyperparameter tuning or specific implementation choices, to ensure a fair comparison. If the results are from the original papers, it is crucial to acknowledge that differences in experimental setup and implementation details could affect the relative performance of each method. A more in-depth discussion of these potential confounding factors is needed to provide a clear understanding of FTP's advantages. Furthermore, the paper should include a detailed complexity and memory cost analysis in the main text. This analysis should not only focus on the training phase but also provide a clear breakdown of the inference costs, including the computational overhead of the router and the memory footprint of the pruned models. This would allow for a more comprehensive evaluation of FTP's efficiency compared to other pruning methods. 

To enhance the practical applicability of the proposed method, the authors should provide a more detailed explanation of how the sparsity scheduler is implemented and how it interacts with the learnable router. The paper should also include a discussion of the limitations of FTP, such as the potential for performance degradation in specific tasks or scenarios, and how these limitations could be addressed in future work. For example, it would be beneficial to analyze the impact of different sparsity levels on the performance of FTP across various tasks and model architectures. This would provide a more nuanced understanding of the trade-offs between computational efficiency and accuracy. Additionally, the authors should consider providing ablation studies to evaluate the contribution of each component of FTP, such as the learnable router and the sparsity scheduler, to the overall performance. This would help to identify the key factors that contribute to the success of FTP and provide insights into how it could be further improved.

Finally, the lack of code and model availability is a significant barrier to the reproducibility of the results. The authors should prioritize making the code and models publicly available to facilitate further research and validation of their claims. This would not only increase the credibility of the paper but also promote the adoption of FTP in real-world applications. The release of code and models should include clear documentation and instructions for use, ensuring that other researchers can easily reproduce the results and build upon the work presented in the paper. The authors should also consider providing pre-trained models for different LLM architectures to further facilitate the adoption of FTP.

### Questions

See Weaknesses

### Rating

6

### Confidence

4

**********
