### Summary

This paper proposes Memoria, a memory module for Transformers that uses Hebbian theory to enhance long-term dependencies. Memoria employs a multi-level memory structure (working, short-term, and long-term memory) and introduces a Hebbian learning rule to strengthen connections between engrams. The authors evaluate Memoria on sorting, language modeling, and text classification tasks, showing improved performance compared to existing models.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective. The proposed method achieves better performance than the baseline models on sorting, language modeling, and text classification tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a thorough discussion of related work, particularly in the area of memory-augmented neural networks. For example, the paper does not discuss how Memoria compares to other memory-augmented models, such as those based on external memory or different memory architectures. A more comprehensive comparison with existing approaches would help to better position the contribution of this work.
- The paper does not provide a detailed analysis of the computational cost and memory requirements of the proposed method. It is important to understand the trade-offs between performance gains and computational overhead, especially when considering the scalability of the approach. The paper should include a breakdown of the computational complexity of each component of Memoria, including the memory access patterns and the Hebbian learning rule. Furthermore, the memory footprint of the proposed model should be analyzed, including the size of the working, short-term, and long-term memory, and how these scale with the input sequence length and the number of parameters.
- The paper does not provide a clear explanation of the hyperparameter selection process for the baseline models. It is important to understand how the baseline models were tuned to ensure a fair comparison with Memoria. The paper should specify the hyperparameter search space for each baseline model, the optimization algorithm used, and the criteria used to select the best hyperparameters. Without this information, it is difficult to assess the validity of the experimental results.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing memory-augmented neural networks. Specifically, the authors should discuss how Memoria's Hebbian-based memory interacts with other memory mechanisms, such as those found in models using external memory or different memory architectures. For example, how does Memoria compare to models that use different memory access patterns or different learning rules for updating the memory? A detailed comparison with these models would help to better position the contribution of this work and highlight its unique advantages and limitations. The authors should also discuss the potential for combining Memoria with other memory-augmented techniques to further improve performance. This would provide a more comprehensive understanding of the proposed method's place within the broader landscape of memory-augmented neural networks.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the computational complexity of each component of Memoria. This should include the time complexity of the memory access patterns, the Hebbian learning rule, and the cross-attention mechanism. The authors should also analyze the memory footprint of the proposed model, including the size of the working, short-term, and long-term memory, and how these scale with the input sequence length and the number of parameters. This analysis should be compared with the computational cost of the baseline models to provide a clear understanding of the trade-offs between performance gains and computational overhead. Furthermore, the authors should discuss the potential for optimizing the implementation of Memoria to reduce its computational cost, such as using sparse memory access patterns or efficient implementations of the Hebbian learning rule.

Finally, the paper needs to provide a more detailed explanation of the hyperparameter selection process for the baseline models. The authors should specify the hyperparameter search space for each baseline model, the optimization algorithm used, and the criteria used to select the best hyperparameters. This information is crucial for ensuring a fair comparison with Memoria. The authors should also discuss the sensitivity of the baseline models to different hyperparameter settings and how this might affect the experimental results. Without this information, it is difficult to assess the validity of the experimental results. The authors should also consider using a more standardized hyperparameter tuning procedure, such as Bayesian optimization, to ensure a fair comparison.

### Questions

- How does the proposed method compare to other memory-augmented Transformer models, such as those based on external memory or different memory architectures?
- What is the computational cost and memory requirements of the proposed method compared to the baseline models?
- How were the hyperparameters of the baseline models selected? Were they tuned for each task separately?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
