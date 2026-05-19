### Summary

The paper proposes a method to remove undesired concepts from a pre-trained model. The method is based on an iterative process that involves pseudo-labeling and fine-tuning. The authors also introduce a metric to quantify the degree of concept forgetting.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-written and easy to follow. The authors provide a clear definition of concept forgetting and introduce a metric to quantify concept violation. The proposed method is simple and easy to implement. The authors also provide a theoretical analysis of the convergence of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers binary-level concept forgetting and does not explore multi-level concept forgetting, which is an important aspect of concept forgetting.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for practical applications.
3. The paper does not compare the proposed method with other state-of-the-art methods for concept forgetting.
4. The paper does not discuss the limitations of the proposed method and potential future directions.

### Suggestions

The paper introduces an interesting approach to concept forgetting, but its evaluation is limited to binary concept forgetting. To strengthen the paper, the authors should explore multi-level concept forgetting scenarios. For example, consider a dataset where each image contains multiple objects, each belonging to a different concept. The model should be able to forget a specific concept while retaining the ability to classify other concepts. This could involve datasets with multiple object instances per image, each annotated with different concepts. The authors could then evaluate their method's ability to forget one concept while maintaining performance on other concepts. This would require a more complex experimental setup, but it would provide a more comprehensive evaluation of the proposed method's capabilities. Furthermore, the authors should consider datasets where concepts are not mutually exclusive, which would make the problem more challenging and more relevant to real-world scenarios.

In addition to the limited scope of concept forgetting, the paper lacks a thorough analysis of the computational cost of the proposed method. The authors should provide a detailed breakdown of the time and memory requirements of their algorithm, especially when applied to large-scale datasets. This analysis should include the time taken for pseudo-label generation, model fine-tuning, and any other computationally intensive steps. The authors should also compare the computational cost of their method with other concept forgetting techniques. This would help to assess the practical feasibility of the proposed method and identify potential bottlenecks. Furthermore, the authors should discuss the scalability of their method to larger datasets and more complex models. This analysis should include the impact of dataset size and model complexity on the computational cost of the algorithm.

Finally, the paper should include a more comprehensive comparison with existing state-of-the-art methods for concept forgetting. The authors should compare their method with other techniques that address concept forgetting, such as those based on adversarial training or knowledge distillation. This comparison should include both quantitative and qualitative results, and it should also discuss the strengths and weaknesses of each method. The authors should also discuss the limitations of their method and potential future directions. For example, the authors could discuss the limitations of their method in handling complex concept forgetting scenarios, or they could discuss potential ways to improve the performance of their method. This would help to position the proposed method within the broader context of concept forgetting research and identify areas for future work.

### Questions

1. How does the proposed method handle multi-level concept forgetting?
2. What is the computational cost of the proposed method compared to other methods?
3. How does the proposed method compare to other state-of-the-art methods for concept forgetting?
4. What are the limitations of the proposed method and potential future directions?

### Rating

5

### Confidence

3

**********
