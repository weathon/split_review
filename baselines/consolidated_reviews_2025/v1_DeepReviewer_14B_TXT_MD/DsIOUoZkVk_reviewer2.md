### Summary

This paper studies the theoretical aspect of contrastive learning, with a particular focus on multimodal alignment. It explores how representations from unpaired modalities can be effectively aligned by integrating out intermediate modalities. The authors provide a theoretical framework for understanding how contrastive learning can be applied to handle unseen modality pairs. Additionally, the paper presents numerical experiments to validate the theoretical findings and demonstrates the effectiveness of the proposed approach in multimodal alignment tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper offers a novel theoretical framework for understanding the alignment of unpaired modalities in contrastive learning, which is a valuable contribution to the field.

2. The authors conduct numerical experiments to validate their theoretical findings, providing empirical support for their claims.

3. The paper is well-written and easy to follow, making it accessible to readers with varying levels of expertise in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other baseline methods, which could provide a more comprehensive evaluation of the proposed approach's effectiveness. Specifically, the paper does not benchmark against existing multimodal alignment techniques, making it difficult to assess the relative performance gains of the proposed method. Without such comparisons, it is unclear whether the theoretical contributions translate into practical improvements over established methods.

2. The paper does not include an analysis of sensitivity to hyperparameters, which could be important for understanding the robustness of the proposed method. The authors should investigate how the performance of their method varies with different choices of learning rates, batch sizes, and other relevant hyperparameters. This analysis is crucial for practical application, as it determines the stability and reliability of the method under different experimental conditions.

### Suggestions

To address the lack of comparative analysis, the authors should include a benchmark against several established multimodal alignment methods. This would involve selecting a few representative baseline algorithms, implementing them on the same datasets used in the paper, and reporting their performance using the same evaluation metrics. For example, if the paper focuses on aligning image and text modalities, it would be beneficial to compare against methods that explicitly learn cross-modal embeddings, such as those based on canonical correlation analysis or other contrastive learning approaches. This would provide a clearer picture of the advantages and disadvantages of the proposed method compared to existing techniques. Furthermore, the authors should provide a detailed explanation of why the chosen baselines are relevant and how their method differs from them, highlighting the unique contributions of their work.

Regarding the sensitivity analysis, the authors should conduct a systematic study of how the performance of their method changes with different hyperparameter settings. This should include a range of values for key hyperparameters, such as learning rate, batch size, and the number of training epochs. The results of this analysis should be presented in a clear and concise manner, such as through tables or graphs, to show how the performance varies with each hyperparameter. It would also be beneficial to identify the optimal hyperparameter settings for the proposed method and discuss the potential reasons for the observed sensitivity. This analysis would not only improve the robustness of the method but also provide practical guidance for users who want to apply the method to their own datasets. The authors should also discuss the computational cost associated with different hyperparameter settings, which is important for practical applications.

Finally, the authors should consider including an ablation study to understand the contribution of different components of their proposed method. This would involve systematically removing or modifying different parts of the method and evaluating the impact on performance. For example, if the method involves a specific loss function or a particular architecture, the authors should analyze how the performance changes when these components are altered. This would provide a deeper understanding of the method's inner workings and help to identify the key factors that contribute to its success. The ablation study should be designed to isolate the effects of each component and provide a clear picture of their individual contributions.

### Questions

Please refer to the Weaknesses.

### Rating

6

### Confidence

2

**********
