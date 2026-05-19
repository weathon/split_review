### Summary

This paper constructs a dataset of adversarially trained Wide-Residual Networks (WRNs) on CIFAR-10. The dataset contains 15,625 models with different depth and width settings, and evaluations on multiple adversarial attacks, including AutoAttack and various common corruption types. The authors also provide checkpoints during adversarial training to facilitate further research.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The authors have conducted a comprehensive analysis of the dataset, including robust accuracy, stable accuracy, and empirical Lipschitz constant. They also explore the relationship between model architecture and adversarial robustness, which is valuable for understanding the underlying principles of robustness.

2. The dataset is well-documented, with evaluations on multiple adversarial attacks and common corruptions, as well as checkpoints during training. This makes it a valuable resource for researchers in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The primary contribution of this paper is the construction of a dataset. However, the dataset is based on a relatively simple architecture, Wide Residual Networks (WRNs), which may limit its applicability to more complex or diverse architectures. The use of a single architecture type, even with varying hyperparameters, restricts the generalizability of the findings to other architectural paradigms such as Transformers or other convolutional network variants. This limits the dataset's utility for exploring robustness in a broader context.

2. The dataset is evaluated solely on the CIFAR-10 dataset. This raises concerns about the generalizability of the findings to other datasets with different characteristics, such as larger datasets like ImageNet or datasets with different data distributions. The performance of adversarial training can be highly dependent on the dataset's size, complexity, and modality, and evaluating on a single dataset like CIFAR-10 may not provide a comprehensive understanding of the dataset's robustness properties.

3. The paper does not provide a detailed analysis of the computational cost associated with constructing the dataset. Given the large number of models trained and evaluated, it is important to understand the resources required to create and use the dataset. This includes the time and GPU hours needed for adversarial training, as well as the memory requirements for storing the dataset. Without this information, it is difficult for other researchers to assess the feasibility of using the dataset.

4. The paper does not provide a detailed analysis of the diversity of the dataset. While the authors mention that the dataset contains 15,625 models with different depth and width settings, it is unclear how these settings are distributed and whether there are any biases in the selection of architectures. A more detailed analysis of the architecture space covered by the dataset would be beneficial.

5. The paper does not provide a detailed analysis of the limitations of the dataset. While the authors acknowledge that the dataset is limited to a single architecture and dataset, they do not discuss other potential limitations, such as the specific choice of adversarial attacks and common corruptions. A more thorough discussion of the limitations of the dataset would be beneficial for researchers who use it.

### Suggestions

The authors should consider expanding the dataset to include a wider range of architectures beyond Wide Residual Networks (WRNs). This could include, for example, ResNet variants with different depths and widths, DenseNets, or even some simple CNN architectures. This would significantly increase the generalizability of the dataset and make it more useful for researchers working on adversarial robustness. Furthermore, the authors should also consider including more diverse datasets beyond CIFAR-10, such as ImageNet or other datasets with different characteristics. This would help to assess the robustness of the models trained on the dataset across different data distributions and complexities. The inclusion of larger datasets would also help to evaluate the scalability of the dataset and the computational cost associated with training and evaluating models on it.

To address the lack of information regarding the computational cost, the authors should provide a detailed breakdown of the resources required to construct the dataset. This should include the number of GPUs used, the training time per model, the total training time, and the memory requirements for storing the dataset. This information is crucial for other researchers who want to use the dataset and understand the feasibility of creating similar datasets. The authors should also provide a clear explanation of how the models were trained, including the specific hyperparameters used and the optimization algorithm. This would allow other researchers to reproduce the results and to use the dataset for their own research. Furthermore, the authors should also provide a detailed analysis of the diversity of the dataset, including the distribution of depth and width settings, and the range of model complexities. This would help researchers to understand the coverage of the architecture space and to identify potential biases in the dataset.

Finally, the authors should provide a more thorough discussion of the limitations of the dataset. This should include a discussion of the specific choice of adversarial attacks and common corruptions, and how these choices might affect the generalizability of the findings. The authors should also discuss the limitations of the dataset in terms of the specific architecture and dataset used, and how these limitations might affect the applicability of the dataset to other research problems. This would help researchers to understand the scope of the dataset and to use it appropriately. The authors should also consider providing a tool or script to easily access and analyze the dataset, which would make it more accessible to the research community.

### Questions

1. How does the dataset compare to existing adversarial robustness datasets in terms of the diversity of architectures and datasets covered?

2. How does the computational cost of constructing the dataset compare to other similar datasets?

3. How can the dataset be used to validate or challenge existing architectural principles for adversarial robustness?

### Rating

3

### Confidence

4

**********
