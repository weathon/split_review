### Summary

The paper introduces NARes, a large-scale neural architecture dataset for adversarial robustness, focusing on the macro search space based on Wide Residual Networks (WRNs). NARes contains 15,625 unique architectures with evaluations on four adversarial attacks (AutoAttack, PGD-20, PGD-CW40, and FGSM) and three common corruptions (CIFAR-10-C). The authors provide checkpoints for each architecture to facilitate further analysis and research. The paper also presents findings from the dataset, including the impact of model capacity on adversarial robustness, the relationship between stable accuracy and empirical Lipschitz constant, and the validation of existing robust architecture principles.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a large-scale dataset for adversarial robustness, which is a valuable resource for the research community. The dataset contains 15,625 unique architectures with evaluations on multiple adversarial attacks and common corruptions, providing a comprehensive assessment of model robustness.
2. The authors provide checkpoints for each architecture, which can be useful for further analysis and research. This allows researchers to easily access and analyze the performance of different architectures on adversarial attacks and common corruptions.
3. The paper presents findings from the dataset, including the impact of model capacity on adversarial robustness, the relationship between stable accuracy and empirical Lipschitz constant, and the validation of existing robust architecture principles. These findings can provide valuable insights into the relationship between architecture and robustness, and can help to develop new robust architectures.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks novelty in terms of the architecture search space. The authors only consider WRN, which has been widely used in previous works [1, 2]. The paper does not explore other architectures, such as ResNet or DenseNet, which could provide a more comprehensive understanding of adversarial robustness across different architectural families. The choice of WRN limits the generalizability of the findings to other architectures with different inductive biases. Specifically, the paper does not investigate how the robustness landscape differs across these architectures, which could reveal important insights about the relationship between architectural design and adversarial vulnerability.
2. The paper does not provide a detailed analysis of the computational cost associated with constructing the dataset. The authors should provide a breakdown of the computational resources required for training and evaluating the 15,625 models, including the number of GPUs, training time, and memory usage. This information is crucial for other researchers to assess the feasibility of using the dataset. The lack of this information makes it difficult to evaluate the practicality of the dataset for other researchers, especially those with limited computational resources.
3. The paper does not provide a detailed analysis of the diversity of the dataset. The authors should provide more information on the distribution of architectures in the dataset, such as the range of depths and widths, and the number of models with each configuration. This information is important to understand the coverage of the search space and to identify potential biases in the dataset. Without this information, it is difficult to assess the representativeness of the dataset and its potential for generalization.
4. The paper does not provide a detailed analysis of the limitations of the dataset. The authors should discuss the limitations of the dataset, such as the specific choice of adversarial attacks and common corruptions, and how these choices might affect the generalizability of the findings. The authors should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems. The paper should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems. For example, the use of CIFAR-10 as the primary dataset may not be representative of more complex datasets, and the choice of adversarial attacks may not cover the full spectrum of potential adversarial threats.
5. The paper does not provide a detailed analysis of the robustness of the models. The authors should provide more information on the robustness of the models, such as the distribution of robustness scores, and the correlation between robustness and other model properties, such as depth and width. This information is important to understand the relationship between model architecture and robustness. The paper should also discuss the limitations of using stable accuracy and empirical Lipschitz constant as metrics for adversarial robustness.
6. The paper does not provide a detailed analysis of the relationship between stable accuracy and empirical Lipschitz constant. The authors should provide more information on the relationship between stable accuracy and empirical Lipschitz constant, such as the correlation between the two metrics, and the implications of this relationship for adversarial robustness. The authors should also discuss the limitations of using these metrics as indicators of robustness.
7. The paper does not provide a detailed analysis of the validation of existing robust architecture principles. The authors should provide more information on the validation of existing robust architecture principles, such as the relationship between model capacity and robustness, and the impact of architectural modifications on robustness. The authors should also discuss the limitations of the validation of existing robust architecture principles, and the potential for new architectural principles to emerge from the dataset.

### Suggestions

The paper would benefit significantly from a more thorough exploration of the architectural search space. While the use of Wide Residual Networks (WRNs) is a reasonable starting point, the lack of diversity in the architectures limits the generalizability of the findings. The authors should consider including other popular architectures such as ResNet and DenseNet, which have different inductive biases and may exhibit different robustness properties. This would provide a more comprehensive understanding of the relationship between architecture and adversarial robustness. Furthermore, the authors should investigate how the robustness landscape differs across these architectures, which could reveal important insights about the relationship between architectural design and adversarial vulnerability. This could involve analyzing the sensitivity of different architectures to adversarial perturbations and identifying common patterns or trends. The inclusion of a more diverse set of architectures would also make the dataset more valuable to the research community.

In addition to expanding the architectural search space, the authors should provide a more detailed analysis of the computational cost associated with constructing the dataset. This should include a breakdown of the resources required for training and evaluating the 15,625 models, including the number of GPUs, training time, and memory usage. This information is crucial for other researchers to assess the feasibility of using the dataset. The authors should also provide a detailed analysis of the diversity of the dataset, including the distribution of architectures in terms of depth, width, and other relevant parameters. This would help to understand the coverage of the search space and to identify potential biases in the dataset. Furthermore, the authors should discuss the limitations of the dataset, such as the specific choice of adversarial attacks and common corruptions, and how these choices might affect the generalizability of the findings. This should include a discussion of the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems. The authors should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems.

Finally, the authors should provide a more detailed analysis of the robustness of the models, including the distribution of robustness scores and the correlation between robustness and other model properties. This would provide a more comprehensive understanding of the relationship between model architecture and robustness. The authors should also discuss the limitations of using stable accuracy and empirical Lipschitz constant as metrics for adversarial robustness. Furthermore, the authors should provide a more detailed analysis of the relationship between stable accuracy and empirical Lipschitz constant, including a correlation analysis and a discussion of the implications of this relationship for adversarial robustness. The authors should also discuss the limitations of the validation of existing robust architecture principles, and the potential for new architectural principles to emerge from the dataset. This should include a discussion of the limitations of the validation of existing robust architecture principles, and the potential for new architectural principles to emerge from the dataset.

### Questions

1. How does the dataset compare to existing adversarial robustness datasets in terms of the diversity of architectures and datasets covered?
2. How does the computational cost of constructing the dataset compare to other similar datasets?
3. How can the dataset be used to validate or challenge existing architectural principles for adversarial robustness?

### Rating

5

### Confidence

4

**********
