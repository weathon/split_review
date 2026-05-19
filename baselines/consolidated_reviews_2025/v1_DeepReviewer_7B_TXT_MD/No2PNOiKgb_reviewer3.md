### Summary

The paper proposes an improved method for indoor scene decomposition of indoor scenes. The method introduces a small number of negative primitives and ensembles multiple regressors with different numbers of primitives. The method achieves state-of-the-art results on the NYUv2 dataset.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. 
2. The experiments are thorough and the ablation studies are comprehensive. 
3. The proposed method achieves state-of-the-art results on the NYUv2 dataset.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The main contributions include introducing negative primitives and ensembling multiple predictions with varying numbers of primitives. However, the effectiveness of negative primitives and ensembling is well-known in machine learning. The refine-then-choose strategy, while intuitive, lacks a strong theoretical justification. The paper does not provide a clear explanation of why this specific order is optimal, nor does it explore alternative selection strategies. Furthermore, the method's reliance on a fixed set of primitives limits its ability to adapt to novel scene structures. The experiments are primarily conducted on the NYUv2 dataset, which may not fully demonstrate the generalizability of the proposed approach to more diverse and complex scenes. The paper also does not address the computational cost associated with ensembling multiple models, which could be a significant limitation for real-time applications.

### Suggestions

The paper should provide a more rigorous analysis of the refine-then-choose strategy. Instead of simply stating that it works well, the authors should explore the underlying reasons why this order is effective. For instance, they could investigate whether the refinement process is more prone to introducing errors in certain regions or primitive types, and how this affects the selection process. A more detailed analysis of the error characteristics of the refined predictions could lead to a more principled approach to selection, rather than relying on empirical observation. Furthermore, the authors should consider exploring alternative selection strategies, such as weighted averaging or a more sophisticated voting scheme, to see if they can achieve better performance or robustness. The current approach of selecting the best prediction based on a single metric may be too simplistic and could be improved by considering multiple factors, such as depth accuracy, surface normal consistency, and semantic coherence.

To address the limitations of the fixed primitive set, the authors could explore methods for dynamically adapting the set of primitives based on the scene content. This could involve learning a mapping from the scene to a set of relevant primitives or using a more flexible representation that can accommodate a larger number of primitives. For example, they could investigate the use of learned features to guide the selection of primitives or explore methods for combining primitives in a more flexible way. This would allow the method to adapt to novel scene structures and improve its generalizability. Additionally, the authors should conduct experiments on more diverse datasets to evaluate the method's performance in different scenarios. This would provide a more comprehensive assessment of the method's strengths and weaknesses and help to identify areas for improvement. The current focus on the NYUv2 dataset limits the ability to draw conclusions about the method's performance in more challenging real-world scenarios.

Finally, the paper should address the computational cost associated with ensembling multiple models. The authors should provide a detailed analysis of the computational complexity of their method and explore ways to reduce its computational overhead. This could involve techniques such as model pruning, knowledge distillation, or parallel processing. The paper should also discuss the trade-off between accuracy and computational cost and provide guidance on how to choose the number of models to ensemble based on the available resources. Without a clear understanding of the computational cost, it is difficult to assess the practical applicability of the proposed method, especially in real-time applications. The authors should also consider the memory footprint of their method, as this could be a limiting factor for deployment on resource-constrained devices.

### Questions

1. How does the method perform on more diverse and complex scenes beyond the NYUv2 dataset? Are there any limitations or challenges in generalizing the approach to different types of indoor environments?
2. What is the computational cost of the proposed method, especially with the ensembling of multiple models? How does this impact its practical applicability in real-time scenarios?

### Rating

5

### Confidence

4

**********
