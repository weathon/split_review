### Summary

This paper proposes a method to enhance the interchangeability of embeddings from different modalities, thereby enabling the learning of cross-modal tasks with uni-modal data. The authors provide a theoretical explanation of the unique geometry that arises from multi-modal contrastive learning, and introduce a three-step method called C^3 (Connect, Collapse, Corrupt) to address the modality gap and alignment noise. The method is shown to achieve state-of-the-art results on zero-shot evaluation settings when trained solely on uni-modal data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a theoretical explanation of the unique geometry that arises from multi-modal contrastive learning, which is a valuable contribution to the field.
2. The proposed C^3 method is simple yet effective, and it achieves state-of-the-art results on zero-shot evaluation settings across various tasks.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the proposed method addresses the modality gap and alignment noise. The description of the C^3 method is too brief and lacks details on how each step contributes to the overall goal. Specifically, the paper lacks a detailed explanation of how the 'Connect' step addresses the modality gap, and how the 'Corrupt' step mitigates alignment noise. The connection between the theoretical analysis of the geometry and the practical implementation of the C^3 method is not clearly established.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. The lack of information on training time, inference time, and memory usage makes it difficult to assess the practical applicability of the method, especially when compared to existing approaches. It is unclear whether the performance gains justify the potential increase in computational cost.
3. The paper does not provide a thorough comparison with existing methods. While the authors mention that their method is simple and effective, they do not provide a detailed comparison with other state-of-the-art methods in terms of performance, computational cost, and memory usage. The paper should include a more comprehensive comparison with existing methods to demonstrate the advantages of the proposed approach.

### Suggestions

The paper would benefit from a more detailed explanation of the C^3 method, particularly regarding how each step addresses the modality gap and alignment noise. The authors should provide a more in-depth analysis of the theoretical underpinnings of each step, and how they contribute to the overall goal of enhancing the interchangeability of embeddings between modalities. For example, the 'Connect' step should be explained in terms of how it reduces the modality gap, and the 'Corrupt' step should be explained in terms of how it mitigates alignment noise. A more detailed explanation of the mathematical formulations and the underlying assumptions would be beneficial. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method, including training time, inference time, and memory usage. This analysis should be compared with existing methods to demonstrate the practical applicability of the proposed approach. The authors should also provide a more thorough comparison with existing methods, including a detailed comparison of performance, computational cost, and memory usage. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to existing approaches. 

To improve the clarity of the paper, the authors should provide more concrete examples of how the C^3 method works in practice. For instance, they could provide a step-by-step walkthrough of how the method works on a specific example, such as image captioning. This would help the reader to better understand the practical implications of the proposed method. The authors should also provide a more detailed explanation of the experimental setup, including the datasets used, the evaluation metrics, and the hyperparameter settings. This would help the reader to reproduce the results of the paper. The authors should also provide a more detailed analysis of the results, including a discussion of the limitations of the proposed method and potential directions for future research. 

Finally, the authors should consider including ablation studies to evaluate the contribution of each step of the C^3 method. This would help to demonstrate the effectiveness of each step and to identify the most important components of the proposed method. For example, the authors could evaluate the performance of the method with and without the 'Connect' step, or with and without the 'Corrupt' step. This would provide a more detailed understanding of the proposed method and would help to guide future research. The authors should also consider including a discussion of the potential limitations of the proposed method, and potential directions for future research. This would help to provide a more balanced and comprehensive assessment of the proposed approach.

### Questions

Please see the weakness part.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
