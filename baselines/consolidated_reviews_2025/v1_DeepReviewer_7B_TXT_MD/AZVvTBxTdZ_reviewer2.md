### Summary

This paper introduces NARes, a large-scale neural architecture dataset for adversarial robustness, specifically focusing on the macro search space based on Wide Residual Networks (WRNs). NARes contains 15,625 unique architectures with evaluations on four adversarial attacks (AutoAttack, PGD-20, PGD-CW40, and FGSM) and three common corruptions (CIFAR-10-C). The authors provide checkpoints for each architecture to facilitate further analysis and research. The paper also presents findings from the dataset, including the impact of model capacity on adversarial robustness, the relationship between stable accuracy and empirical Lipschitz constant, and the validation of existing robust architecture principles.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper presents a large-scale dataset for adversarial robustness, which is a valuable resource for the research community.
2. The dataset includes evaluations on multiple adversarial attacks and common corruptions, providing a comprehensive assessment of model robustness.
3. The authors provide checkpoints for each architecture, which can be useful for further analysis and research.

### Weaknesses

#### Some Related Works

[1] Robust architecture search for adversarial robustness
[2] AutoAttack: a standardized evaluation of adversarial robustness
[3] Towards deep learning models resistant to adversarial attacks
[4] Towards deep learning models resistant to adversarial attacks
[5] Robust principle: a new design principle for adversarial robustness

#### comment

1. The paper lacks novelty in terms of the architecture search space. The authors only consider WRN, which has been widely used in previous works [1, 2]. The paper does not explore other architectures, such as ResNet or DenseNet, which could provide a more comprehensive understanding of adversarial robustness across different architectural families. The choice of WRN limits the generalizability of the findings to other architectures, and it is unclear if the observed trends would hold for other architectures with different inductive biases.
2. The paper does not provide a detailed analysis of the computational cost associated with constructing the dataset. The authors should provide a breakdown of the computational resources required for training and evaluating the 15,625 models, including the number of GPUs, training time, and memory usage. This information is crucial for other researchers to assess the feasibility of using the dataset.
3. The paper does not provide a detailed analysis of the diversity of the dataset. The authors should provide more information on the distribution of architectures in the dataset, such as the range of depths and widths, and the number of models with each configuration. This information is important to understand the coverage of the search space and to identify potential biases in the dataset.
4. The paper does not provide a detailed analysis of the limitations of the dataset. The authors should discuss the limitations of the dataset, such as the specific choice of adversarial attacks and common corruptions, and how these choices might affect the generalizability of the findings. The authors should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems.
5. The paper does not provide a detailed analysis of the robustness of the models. The authors should provide more information on the robustness of the models, such as the distribution of robustness scores, and the correlation between robustness and other model properties, such as depth and width. This information is important to understand the relationship between model architecture and robustness.
6. The paper does not provide a detailed analysis of the relationship between stable accuracy and empirical Lipschitz constant. The authors should provide more information on the relationship between stable accuracy and empirical Lipschitz constant, such as the correlation between the two metrics, and the implications of this relationship for adversarial robustness. The authors should also discuss the limitations of using stable accuracy and empirical Lipschitz constant as metrics for adversarial robustness.
7. The paper does not provide a detailed analysis of the validation of existing robust architecture principles. The authors should provide more information on the validation of existing robust architecture principles, such as the relationship between model capacity and robustness, and the impact of architectural modifications on robustness. The authors should also discuss the limitations of the validation of existing robust architecture principles, and the potential for new architectural principles to emerge from the dataset.

### Suggestions

The authors should expand the architecture search space beyond Wide Residual Networks (WRNs) to include other common architectures like ResNet and DenseNet. This would significantly increase the generalizability of the findings and provide a more comprehensive understanding of adversarial robustness across different architectural families. Specifically, the authors should explore a range of depths and widths for each architecture type, ensuring a diverse coverage of the search space. This would allow for a more robust analysis of how architectural choices impact adversarial robustness. Furthermore, the authors should provide a detailed analysis of the computational cost associated with constructing the dataset, including the number of GPUs, training time, and memory usage for each architecture. This information is crucial for other researchers to assess the feasibility of using the dataset and to understand the resources required to replicate the results. The authors should also provide a detailed analysis of the diversity of the dataset, including the distribution of architectures in terms of depth, width, and other relevant parameters. This would help to identify potential biases in the dataset and to understand the coverage of the search space. 

To further enhance the dataset, the authors should provide a more detailed analysis of the relationship between stable accuracy and empirical Lipschitz constant. This should include a correlation analysis between the two metrics and a discussion of the implications of this relationship for adversarial robustness. The authors should also discuss the limitations of using these metrics as indicators of robustness and explore other metrics that may be more informative. Additionally, the authors should provide a more detailed analysis of the validation of existing robust architecture principles, including the relationship between model capacity and robustness, and the impact of architectural modifications on robustness. This analysis should include a discussion of the limitations of the validation and the potential for new architectural principles to emerge from the dataset. The authors should also consider providing a tool or script to easily access and analyze the dataset, which would make it more accessible to the research community.

Finally, the authors should address the limitations of the dataset, such as the specific choice of adversarial attacks and common corruptions, and how these choices might affect the generalizability of the findings. The authors should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems. The authors should also consider providing a more detailed analysis of the robustness of the models, including the distribution of robustness scores and the correlation between robustness and other model properties. This would provide a more comprehensive understanding of the relationship between model architecture and robustness. The authors should also consider providing a more detailed analysis of the relationship between stable accuracy and empirical Lipschitz constant, including a correlation analysis and a discussion of the implications of this relationship for adversarial robustness.

### Questions

1. How does the dataset compare to existing adversarial robustness datasets in terms of the diversity of architectures and datasets covered?
2. How does the computational cost of constructing the dataset compare to other similar datasets?
3. How can the dataset be used to validate or challenge existing architectural principles for adversarial robustness?

### Rating

3

### Confidence

4

**********
