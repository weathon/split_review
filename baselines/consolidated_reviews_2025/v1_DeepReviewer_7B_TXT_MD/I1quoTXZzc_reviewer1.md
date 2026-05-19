### Summary

This paper proposes a novel approach to concept bottleneck models (CBM). The key idea is to use energy-based models to learn the joint energy of input, concepts, and class labels. This allows for concept correction and conditional interpretation. The authors demonstrate the effectiveness of their approach through experiments on three datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The idea of using energy-based models to learn the joint energy of input, concepts, and class labels is novel and interesting.
- The proposed approach shows promising results on three datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The idea of using energy-based models to learn the joint energy of input, concepts, and class labels is not new. It has been widely used in many existing works, such as the cited papers (e.g., Kim et al., 2023a; 2023b; Kim et al., 2023c). The paper does not adequately distinguish its approach from these existing uses of energy-based models. Specifically, the paper needs to clarify how its method of defining and utilizing the joint energy differs fundamentally from prior applications in concept bottleneck models. The current explanation lacks the necessary detail to establish a clear novelty claim.
- The experiments are conducted on three datasets. It would be better to include more datasets to demonstrate the effectiveness of the proposed approach. The current selection of datasets, while relevant, does not provide sufficient breadth to fully assess the generalizability of the proposed method. The paper should include datasets with varying characteristics (e.g., different concept complexities, data modalities) to provide a more robust evaluation.

### Suggestions

The paper should provide a more detailed explanation of how the proposed energy-based model for joint energy differs from existing uses of energy-based models in concept bottleneck models. Specifically, the authors should clarify the novel aspects of their approach, such as the specific form of the energy function, the training procedure, and how these differ from prior work. A more thorough comparison with existing methods, highlighting the unique contributions of this work, is needed to establish the novelty of the proposed approach. For example, the authors could discuss how their method addresses specific limitations of previous energy-based approaches in the context of concept bottleneck models, such as the handling of complex concept dependencies or the integration of concept correction and conditional interpretation.

To strengthen the experimental evaluation, the authors should include a more diverse set of datasets. The current selection of datasets, while relevant, does not provide sufficient breadth to fully assess the generalizability of the proposed method. The authors should consider including datasets with varying characteristics, such as different concept complexities, data modalities (e.g., images, text, audio), and dataset sizes. This would provide a more comprehensive evaluation of the proposed method's performance and robustness. Furthermore, the authors should provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method on different datasets. This would help to identify the specific scenarios where the proposed method performs well and where it may have limitations.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed approach. The authors should provide a comparison of the training and inference time of the proposed method with existing concept bottleneck models. This would help to assess the practical applicability of the proposed method. The authors should also discuss the scalability of the proposed method to larger datasets and more complex models. This would help to understand the limitations of the proposed method and identify potential areas for future research.

### Questions

- What are the differences between the proposed approach and existing approaches that use energy-based models to learn the joint energy of input, concepts, and class labels?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
