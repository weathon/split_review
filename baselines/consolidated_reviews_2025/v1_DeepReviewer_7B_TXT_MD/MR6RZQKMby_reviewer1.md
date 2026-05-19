### Summary

This paper proposes a new metric called model kinship, which is inspired by biological evolution. The authors argue that model kinship can help guide the selection of candidate models for merging and can also serve as an early stopping criterion. The authors conduct extensive experiments to demonstrate the effectiveness of model kinship in understanding the model evolution process and propose a new model merging strategy: Top-k Greedy Merging with Model Kinship. The experimental results show that the proposed method can achieve better performance on benchmark datasets compared to the vanilla greedy merging strategy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The authors propose a new metric called model kinship, which is inspired by biological evolution. The authors argue that model kinship can help guide the selection of candidate models for merging and can also serve as an early stopping criterion.
2. The authors conduct extensive experiments to demonstrate the effectiveness of model kinship in understanding the model evolution process and propose a new model merging strategy: Top-k Greedy Merging with Model Kinship.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 1. The authors claim that model kinship can help guide the selection of candidate models for merging and can also serve as an early stopping criterion. However, the authors do not provide any theoretical analysis or empirical evidence to support these claims. The experiments are conducted on a limited set of models and datasets, and the results may not generalize to other scenarios. Specifically, the paper lacks a rigorous definition of 'kinship' in the context of neural network weights, making it difficult to assess the validity of the proposed metric. The paper does not explore the sensitivity of the kinship metric to different weight initialization schemes or optimization algorithms, which could significantly impact the observed correlations with performance gains.
2. The authors use the term "evolution" to describe the merging process, which is confusing and misleading. The merging process is more accurately described as an iterative model selection process, rather than biological evolution. The analogy to biological evolution is superficial and does not provide any meaningful insights into the merging process. The paper does not address the fundamental differences between biological evolution and the optimization process in neural networks, such as the lack of a clear fitness landscape and the absence of genetic recombination.
3. The authors do not provide a clear explanation of how the proposed merging strategy differs from existing methods. The paper does not adequately compare the proposed method with other state-of-the-art merging techniques, such as those based on gradient-based optimization or Bayesian methods. The paper also does not discuss the computational complexity of the proposed method and its scalability to larger models and datasets. The experimental results are not presented in a way that allows for easy comparison with existing methods, making it difficult to assess the practical value of the proposed approach.

### Suggestions

The authors should provide a more rigorous definition of 'model kinship' and explore its relationship with other established metrics for measuring the similarity of neural network weights. This could involve comparing the proposed metric with existing measures of weight similarity, such as cosine similarity or Euclidean distance, and analyzing the correlation between these metrics and performance gains. The authors should also investigate the sensitivity of the kinship metric to different weight initialization schemes and optimization algorithms. Furthermore, the authors should provide a theoretical analysis of the proposed merging strategy, explaining why it is expected to perform well and under what conditions. This analysis should include a discussion of the convergence properties of the method and its relationship to existing optimization techniques. The authors should also conduct experiments on a wider range of models and datasets to demonstrate the generalizability of their findings.

The authors should clarify the analogy between model merging and biological evolution and avoid using the term 'evolution' unless it is supported by a clear and rigorous mapping between the two processes. If the authors choose to maintain the analogy, they should provide a detailed explanation of the mapping and address the fundamental differences between biological evolution and the optimization process in neural networks. The authors should also avoid using the term 'evolution' altogether and use more precise terminology to describe the merging process, such as 'iterative model selection' or 'ensemble learning'.

The authors should provide a more detailed comparison of the proposed method with existing state-of-the-art merging techniques. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to other approaches, as well as a quantitative evaluation of the performance of the proposed method on benchmark datasets. The authors should also discuss the computational complexity of the proposed method and its scalability to larger models and datasets. The experimental results should be presented in a way that allows for easy comparison with existing methods, such as by providing tables or graphs that show the performance of the proposed method and other methods on different datasets and model sizes.

### Questions

1. What is the definition of model kinship? How is it different from other metrics for measuring the similarity of neural network weights?
2. How does the proposed merging strategy differ from existing methods? What are the advantages and disadvantages of the proposed method compared to other approaches?
3. What is the computational complexity of the proposed merging strategy? How does it scale to larger models and datasets?

### Rating

3

### Confidence

4

**********
