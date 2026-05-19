### Summary

This paper proposes a video-language pre-training framework called S-ViLM, which focuses on learning region-object correspondences and temporal-aware features. It includes two novel designs: inter-clip spatial grounding and intra-clip temporal grouping. Experimental results show that S-ViLM outperforms existing approaches in four downstream tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper proposes a novel video-language pre-training method, which includes intra-clip temporal grouping and inter-clip spatial grounding. 
2. This paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The performance of SViLM is not impressive. The method is only evaluated on old datasets and the performance is not promising compared to recent methods. For example, in action recognition, SViLM is only compared to the methods published in 2021 and 2022. The lack of evaluation on more recent benchmarks and comparison with state-of-the-art methods from 2023 makes it difficult to assess the true impact of the proposed approach. Specifically, the action recognition results on UCF101 and HMDB51, while showing some improvement over older methods, do not demonstrate a significant advancement over more recent self-supervised learning techniques.
2. The training of SViLM is complex and requires multiple steps, which may not be efficient. The paper does not provide a detailed analysis of the computational cost associated with each step of the training process. This makes it difficult to assess the practical feasibility of the method, especially when considering large-scale datasets and complex models. A breakdown of the time and resources required for each stage of training would be beneficial.
3. The ablation studies are not sufficient. The paper lacks a thorough investigation into the impact of various design choices, such as the number of groups in the intra-clip temporal grouping and the choice of learnable group tokens. A more detailed ablation study should explore the sensitivity of the model to these hyperparameters and provide a justification for the chosen values. Furthermore, the impact of different video and text encoders should be explored to understand the robustness of the proposed method.

### Suggestions

To address the concerns regarding the performance of SViLM, it is crucial to evaluate the method on more recent and challenging datasets. For action recognition, benchmarks such as Kinetics-400 or Kinetics-700 should be considered to provide a more comprehensive evaluation. Furthermore, the comparison should include state-of-the-art methods from 2023 to accurately assess the contribution of the proposed approach. The paper should also include a detailed analysis of the computational cost associated with each step of the training process. This analysis should include the time and resources required for each stage, such as feature extraction, temporal grouping, and spatial grounding. This would provide a better understanding of the practical feasibility of the method and allow for a more informed comparison with other approaches. Additionally, the authors should consider exploring techniques to optimize the training process and reduce the computational overhead.

To improve the ablation studies, the authors should conduct a more thorough investigation into the impact of various design choices. This should include exploring the sensitivity of the model to the number of groups in the intra-clip temporal grouping and the choice of learnable group tokens. The paper should also explore the impact of different video and text encoders on the performance of the model. For example, the authors could experiment with different pre-trained models for feature extraction and analyze their impact on the downstream tasks. This would provide a better understanding of the robustness of the proposed method and allow for a more informed selection of hyperparameters. Furthermore, the authors should provide a justification for the chosen values of the hyperparameters and explain how they impact the performance of the model.

Finally, the paper should provide a more detailed explanation of the intra-clip temporal grouping and inter-clip spatial grounding mechanisms. This should include a clear description of the mathematical formulations and the implementation details. The authors should also provide a visualization of the learned group tokens and the temporal boundaries to better understand the behavior of the model. This would help to clarify the technical contributions of the paper and make it easier for other researchers to reproduce the results. The paper should also include a discussion of the limitations of the proposed method and suggest directions for future research.

### Questions

1. What is the difference between spatial grounding and region-level contrastive learning? The paper only compares the method to the entity-level contrastive learning. It would be better to compare the method to the region-level contrastive learning method.
2. How does the intra-clip temporal grouping work? The paper only describes the calculation of the loss function of intra-clip temporal grouping, but does not describe how to group the features. It would be better to provide a detailed explanation of the intra-clip temporal grouping.
3. How does the model learn from the text modality during temporal grouping? The paper only describes the calculation of the loss function of intra-clip temporal grouping, but does not describe how to group the features. It would be better to provide a detailed explanation of the intra-clip temporal grouping.
4. In the ablation studies, how does the model perform when trained on HowTo100M? It would be better to provide the results of the ablation studies when trained on HowTo100M.
5. In the ablation studies, how does the model perform when only using the global contrastive loss? It would be better to provide the results of the ablation studies when only using the global contrastive loss.
6. In the ablation studies, how does the model perform when using different video and text encoders? It would be better to provide the results of the ablation studies when using different video and text encoders.
7. In the ablation studies, how does the model perform when changing the number of groups in the intra-clip temporal grouping? It would be better to provide the results of the ablation studies when changing the number of groups in the intra-clip temporal grouping.
8. In the ablation studies, how does the model perform when using different learnable group tokens? It would be better to provide the results of the ablation studies when using different learnable group tokens.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
