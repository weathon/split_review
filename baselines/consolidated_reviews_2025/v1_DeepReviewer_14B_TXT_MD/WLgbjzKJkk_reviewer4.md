### Summary

This paper proposes a novel method called CO-MOT to boost the performance of end-to-end Transformer-based MOT. The authors investigate the issues in the existing end-to-end MOT using Transformer and find that the label assignment can not fully explore the detection queries as detection and tracking queries are exclusive to each other. Thus, they introduce a coopetition alternative for training the intermediate decoders. Also, they develop a shadow set as units to augment the queries, mitigating the unbalanced training caused by the one-to-one matching strategy. Experimental results show that CO-MOT achieves significant performance gains on multiple datasets in an efficient manner. The authors believe that their method as a plugin significantly facilitates the research of end-to-end MOT using Transformer.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. 
2. The proposed method is technically sound and achieves state-of-the-art performance on several benchmarks. 
3. The proposed method is efficient and can be applied to any e2e-MOT method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more analysis on the effectiveness of the proposed method. Specifically, it would be beneficial to see a more detailed breakdown of performance gains across different scenarios, such as varying object densities or occlusion levels. The current analysis lacks a granular view of where the method excels and where it might still struggle. For example, are the improvements consistent across all object classes, or are they more pronounced for certain types of objects? A more in-depth analysis of these aspects would strengthen the paper's claims.
2. The authors should provide more analysis on the efficiency of the proposed method. While the paper mentions efficiency, it lacks a detailed comparison of computational costs, such as FLOPs or inference time, against other state-of-the-art methods. A quantitative analysis of the computational overhead introduced by the proposed method would be valuable. Furthermore, it would be useful to understand how the method scales with increasing image resolution or the number of tracked objects. This would provide a more complete picture of the method's practical applicability.

### Suggestions

To address the lack of detailed effectiveness analysis, the authors should consider including a more granular evaluation of their method's performance. This could involve breaking down the results by different object categories, occlusion levels, and object densities. For instance, they could analyze how the method performs on small, medium, and large objects, or how it handles scenarios with varying degrees of occlusion. Additionally, it would be beneficial to include qualitative examples that illustrate the method's strengths and weaknesses in different scenarios. This would provide a more comprehensive understanding of the method's capabilities and limitations. Furthermore, the authors could explore the impact of different hyperparameter settings on the performance of the method, providing insights into its sensitivity and robustness.

Regarding the efficiency analysis, the authors should provide a more detailed comparison of the computational costs of their method against other state-of-the-art approaches. This should include a quantitative analysis of FLOPs, inference time, and memory usage. It would be beneficial to compare the proposed method with other transformer-based MOT methods, as well as non-transformer-based methods, to provide a comprehensive view of its efficiency. The authors should also investigate how the method scales with increasing image resolution and the number of tracked objects. This would provide valuable insights into the method's practical applicability in real-world scenarios. Furthermore, it would be useful to analyze the computational overhead introduced by the proposed coopetition label assignment and shadow set strategies, providing a clear understanding of their impact on the overall efficiency of the method.

Finally, the authors should consider exploring the limitations of their method in more detail. This could involve analyzing scenarios where the method fails or performs poorly. For example, they could investigate how the method handles situations with very fast-moving objects, or scenarios with significant changes in object appearance. Understanding these limitations would provide valuable insights into the method's weaknesses and potential areas for future improvement. Furthermore, it would be beneficial to discuss the potential impact of different training data on the performance of the method, and how the method might be adapted to handle different types of data. This would provide a more complete picture of the method's capabilities and limitations.

### Questions

Please refer to the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
