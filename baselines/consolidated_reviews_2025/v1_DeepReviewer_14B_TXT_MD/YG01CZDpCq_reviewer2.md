### Summary

This paper proposes an Adaptive Prompt Prototype Learning (APPLe) for VLMs. Specifically, they build various prompts as class prototypes to cover the visual variance. An adaptive attention mechanism is designed to weigh the importance of different prototypes. Experiments are conducted on three representative tasks, i.e., generalization to unseen classes, new target datasets, and unseen domain shifts.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is simple but effective.
3. The experimental results demonstrate the effectiveness of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The time complexity of this method is not favorable due to the requirement of producing multiple prompt prototypes for each class, which may limit its application in real-world scenarios. The paper does not provide a detailed analysis of the computational cost associated with generating and utilizing these multiple prototypes, especially in comparison to single prompt methods. This lack of analysis makes it difficult to assess the practical scalability of the proposed approach.
2. The performance improvement on some datasets is not significant, such as on the Caltech101 and OxfordPets datasets. While the method shows gains on some datasets, the marginal improvements on others raise questions about its general applicability and whether the added complexity of multiple prototypes is always justified. The paper should provide a more in-depth analysis of why the method struggles on certain datasets.
3. The ablation experiments in Table 3 do not demonstrate the effectiveness of the proposed method. The individual contributions of the attention mechanism and the prototype decorrelation loss are not clearly isolated, and the ablation study does not provide sufficient evidence to support the necessity of each component. The paper needs to provide a more granular ablation study to demonstrate the impact of each component.

### Suggestions

The paper should include a more thorough analysis of the computational cost associated with the proposed method. This analysis should include a breakdown of the time and memory requirements for generating and utilizing the multiple prompt prototypes, and a comparison with single prompt methods. It would be beneficial to provide a theoretical analysis of the time complexity, as well as empirical results on the actual runtime. Furthermore, the authors should explore potential optimizations to reduce the computational overhead, such as using more efficient prompt generation techniques or employing pruning strategies to reduce the number of prototypes needed. This would make the method more practical for real-world applications.

To address the inconsistent performance across datasets, the authors should investigate the characteristics of datasets where the method performs poorly. This could involve analyzing the diversity of visual features within each class, the complexity of the background, and the overall data distribution. It would be helpful to provide a more detailed analysis of the failure cases and discuss why the proposed method struggles on certain datasets. The authors could also explore adaptive strategies for selecting the number of prototypes based on the characteristics of the dataset, or consider using different types of prompts for different datasets. This would help to improve the robustness and generalizability of the method.

The ablation study in Table 3 needs to be significantly improved to demonstrate the effectiveness of each component of the proposed method. The authors should conduct a more granular ablation study that isolates the impact of the attention mechanism and the prototype decorrelation loss. This could involve comparing the performance of the method with and without each component, and also exploring different variations of each component. For example, the authors could compare different attention mechanisms or different decorrelation loss functions. The ablation study should also include a detailed analysis of the results, explaining why each component is necessary and how it contributes to the overall performance of the method. This would provide a more convincing argument for the effectiveness of the proposed approach.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
