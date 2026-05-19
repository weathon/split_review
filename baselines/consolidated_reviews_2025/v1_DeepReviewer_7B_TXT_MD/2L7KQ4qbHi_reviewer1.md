### Summary

This paper proposes a method for concept forgetting, which is the ability of a model to forget undesired concepts. The proposed method is Label Annealing (LAN), which is an iterative algorithm that performs two stages: pseudo-label generation and model fine-tuning. LAN reduces concept violation and maintains high model accuracy. The paper also provides a definition of concept violation and compares LAN with other baseline methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a clear definition of concept violation and proposes a metric to quantify it.
3. The paper compares LAN with other baseline methods and shows that it performs better in terms of concept violation and accuracy trade-off.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only considers binary-level concept forgetting and does not explore multi-level concept forgetting, which is an important aspect of concept forgetting.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for practical applications.
3. The paper does not compare the proposed method with other state-of-the-art methods for concept forgetting.
4. The paper does not discuss the limitations of the proposed method and potential future directions.

### Suggestions

The paper should explore multi-level concept forgetting, which is a more challenging and realistic problem. The current approach of only considering binary-level forgetting limits the applicability of the proposed method. For example, in a medical diagnosis scenario, a model might need to forget specific subtypes of a disease, which would be a multi-level concept forgetting problem. The authors should consider how their method could be extended to handle such cases, possibly by incorporating a hierarchical structure of concepts or by using a more fine-grained pseudo-label generation process. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed method. The current analysis is insufficient, and the paper should provide a more thorough evaluation of the time and memory requirements of the algorithm, especially when applied to large-scale datasets. This analysis should include a breakdown of the computational cost of each stage of the algorithm, such as pseudo-label generation and model fine-tuning, and should also consider the impact of different hyperparameter settings on the computational cost. This analysis is crucial for assessing the practical feasibility of the proposed method.

The paper should also compare the proposed method with other state-of-the-art methods for concept forgetting. The current comparison is limited, and the paper should include a more comprehensive evaluation of the proposed method against existing techniques. This comparison should include both quantitative and qualitative results, and it should also discuss the strengths and weaknesses of each method. For example, the paper could compare the proposed method with methods that use adversarial training or methods that use knowledge distillation. This comparison would provide a better understanding of the advantages and disadvantages of the proposed method and would help to position it within the broader context of concept forgetting research. Finally, the paper should discuss the limitations of the proposed method and potential future directions. The paper should acknowledge the limitations of the current approach and discuss potential avenues for future research. For example, the paper could discuss the limitations of the pseudo-label generation process, the potential for catastrophic forgetting, or the challenges of applying the method to more complex datasets. The paper should also discuss potential future directions, such as exploring different fine-tuning strategies, incorporating attention mechanisms, or applying the method to other domains.

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
