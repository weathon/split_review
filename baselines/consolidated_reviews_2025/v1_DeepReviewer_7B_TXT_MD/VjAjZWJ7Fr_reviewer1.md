### Summary

This paper proposes a graph-based framework for joint OOD generalization and OOD detection. The authors formulate the problem in a setting that contains both covariate shift and semantic shift. The key idea is to use contrastive learning on a graph constructed from both labeled ID data and unlabeled data to achieve good OOD generalization and OOD detection. The authors also show that minimizing the contrastive loss is equivalent to performing spectral decomposition on the graph adjacency matrix. Theoretically, the authors derive the top-k embeddings from the contrastive learning objective and analyze the linear probing error and separability of the embeddings. Empirically, the authors demonstrate improved OOD detection and OOD generalization performance on top of SCONE.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The theoretical analysis of the spectral decomposition of the graph adjacency matrix is interesting and provides insights into the properties of the contrastive learning objective.
2. The empirical results show that the proposed method improves upon SCONE on several benchmarks.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for formulating OOD generalization and OOD detection as a single framework is unclear. The authors mentioned that real-world applications often involve both covariate shifts and semantic shifts, but it is not clear why a unified framework is needed. It would be helpful to provide concrete examples of how the proposed method addresses both OOD generalization and OOD detection in a single framework, and how this is an improvement over existing methods that treat these tasks separately. For instance, it is not clear how the graph-based approach simultaneously learns representations that are invariant to covariate shifts and discriminative for semantic shifts, and what specific advantages this offers compared to a two-stage approach.
2. The theoretical analysis relies on a specific graph structure that may not generalize to more complex settings. The analysis focuses on the top-k singular vectors of the normalized adjacency matrix, but it is not clear how this analysis extends to the full learned embedding space. The paper does not provide a clear explanation of how the spectral properties of the top-k vectors relate to the overall performance of the model on OOD generalization and detection. It is also not clear how the theoretical results would be affected by different graph construction methods or by the presence of noise in the graph structure.
3. The empirical evaluation is limited to CIFAR-10 and its variants, which may not fully demonstrate the effectiveness of the proposed method. The experiments are primarily conducted on relatively small datasets, and it is not clear how the method would scale to larger, more complex datasets with higher dimensionality and more diverse data distributions. The paper lacks experiments on datasets with more complex semantic shifts, and it is not clear if the proposed method would be effective in such scenarios.

### Suggestions

The paper would benefit from a more detailed explanation of the motivation for unifying OOD generalization and OOD detection. The authors should provide concrete examples of real-world scenarios where both types of distribution shifts occur simultaneously, and how the proposed method addresses these challenges more effectively than existing approaches. For instance, they could discuss a scenario where a model trained on images of natural scenes needs to generalize to images with different lighting conditions (covariate shift) and also detect images of objects not seen during training (semantic shift). A clear explanation of how the graph-based approach achieves this dual objective would significantly strengthen the paper's motivation. Furthermore, the authors should clarify the specific advantages of their unified framework compared to a two-stage approach, where covariate shift is addressed separately from semantic shift detection. This could involve a discussion of potential benefits such as improved sample efficiency or reduced computational cost.

To address the concerns about the theoretical analysis, the authors should provide a more detailed explanation of how the spectral properties of the top-k vectors relate to the overall performance of the model. They should clarify how the theoretical results extend to the full learned embedding space, and how the choice of k affects the performance of the model. It would be beneficial to include a discussion of the limitations of the theoretical analysis, and how these limitations might affect the practical applicability of the method. The authors should also explore the sensitivity of the theoretical results to different graph construction methods and the presence of noise in the graph structure. This could involve a theoretical analysis of how different graph kernels or edge weighting schemes affect the spectral properties of the adjacency matrix, and how these changes impact the performance of the model. Additionally, the authors should provide a more intuitive explanation of why minimizing the contrastive loss leads to good OOD generalization and OOD detection performance.

Finally, the empirical evaluation should be expanded to include more complex datasets and a wider range of experimental settings. The authors should conduct experiments on larger, more diverse datasets with higher dimensionality and more complex semantic shifts. This would help to demonstrate the robustness and generalizability of the proposed method. The paper should also include a more detailed analysis of the experimental results, and a discussion of the limitations of the proposed method. The authors should also explore the sensitivity of the method to different hyperparameter settings, and provide guidance on how to choose appropriate values for these parameters. Furthermore, it would be beneficial to compare the performance of the proposed method with a wider range of baseline methods, including more recent approaches for OOD generalization and OOD detection.

### Questions

1. The motivation for formulating OOD generalization and OOD detection as a single framework is unclear. It would be helpful to provide concrete examples of how the proposed method addresses both OOD generalization and OOD detection in a single framework, and how this is an improvement over existing methods that treat these tasks separately.
2. The theoretical analysis relies on a specific graph structure that may not generalize to more complex settings. It would be helpful to discuss the limitations of the theoretical analysis and how these limitations might affect the practical applicability of the method.
3. The empirical evaluation is limited to CIFAR-10 and its variants, which may not fully demonstrate the effectiveness of the proposed method. It would be helpful to conduct experiments on more complex datasets to validate the effectiveness of the proposed method.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
