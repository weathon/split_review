### Summary

The authors propose to study the effect of the intrinsic dimension of datasets on the generalization of deep neural networks. They propose to study this in natural image datasets and medical image datasets and propose that the discrepancy in the generalization behavior of models trained on these two types of datasets can be explained by the label sharpness of the dataset, a quantity that is typically higher for medical image datasets. They provide theoretical and empirical evidence for their claims.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The authors study an interesting problem that is relevant to the ICLR community. 
- The authors propose a new measure, the label sharpness of the dataset, to explain the discrepancy in the generalization behavior of models trained on natural image and medical image datasets. 
- The authors provide both theoretical and empirical evidence for their claims.

### Weaknesses

#### Some Related Works


#### comment

 - The authors use a limited set of models (only CNNs) and a limited set of datasets for their experiments. It is not clear if their findings generalize to other types of models and datasets. Specifically, the exclusive use of CNNs, even with varying depths, does not explore the impact of different architectural biases, such as those found in transformers or recurrent networks. Furthermore, the medical image datasets, while diverse in modality, may not fully represent the spectrum of challenges present in medical imaging, such as datasets with significant class imbalance or those requiring spatial reasoning beyond what is captured by the chosen datasets.
- The authors only consider binary classification tasks. It is not clear if their findings generalize to multi-class classification tasks. The extension of the proposed label sharpness measure to multi-class scenarios is not immediately obvious, and the current analysis does not address potential challenges in defining and interpreting this measure in a multi-class setting. This limits the applicability of the findings to a broader range of practical problems.
- The authors do not provide any practical guidance on how to use their findings to improve the performance of deep neural networks. The theoretical and empirical results, while interesting, lack concrete recommendations for model design or training strategies. The paper does not discuss how the observed relationship between intrinsic dimension, label sharpness, and generalization can be leveraged to develop more effective models or training procedures.

### Suggestions

To strengthen the paper, the authors should expand their experimental evaluation to include a more diverse set of models beyond CNNs. Specifically, incorporating transformer-based architectures, which have shown strong performance in various vision tasks, would provide valuable insights into the generalizability of their findings. Furthermore, exploring recurrent neural networks could be beneficial, especially when considering potential temporal dependencies in medical image sequences. The inclusion of these diverse architectures would help to determine if the observed relationship between intrinsic dimension, label sharpness, and generalization is consistent across different model families or if it is specific to CNNs. Additionally, the authors should consider including datasets with more complex characteristics, such as those with significant class imbalance or requiring more intricate spatial reasoning, to further validate the robustness of their claims.

To address the limitation of focusing solely on binary classification, the authors should extend their analysis to multi-class classification tasks. This would involve defining a suitable extension of the label sharpness measure to multi-class scenarios and investigating whether the observed relationships hold in this more general setting. For example, they could explore whether the label sharpness can be defined as a matrix capturing the relationships between all pairs of classes, or if a different approach is needed. Furthermore, the authors should analyze how the generalization behavior of models changes as the number of classes increases and whether the proposed framework can explain these changes. This would significantly broaden the applicability of their findings and make them relevant to a wider range of practical problems. The authors should also consider the impact of class imbalance in multi-class settings, as this is a common challenge in real-world applications.

Finally, the authors should provide more concrete guidance on how their findings can be used to improve the performance of deep neural networks. This could involve suggesting specific model design choices or training strategies based on the observed relationship between intrinsic dimension, label sharpness, and generalization. For example, they could explore whether regularization techniques can be tailored to the intrinsic dimension of the dataset or if data augmentation strategies can be used to modify the label sharpness. Furthermore, the authors should investigate whether their findings can be used to develop more robust models that are less susceptible to adversarial attacks. Providing such practical guidance would significantly increase the impact of their work and make it more useful to the broader machine learning community.

### Questions

- Can the authors provide more details on how they compute the intrinsic dimension of the datasets and the label sharpness of the datasets? It is not clear to me how these quantities are computed in practice. 
- The authors mention that they train their models until they fully fit to the training data. Can the authors provide more details on how they determine when the model has fully fit to the training data? 
- The authors mention that they use a fixed learning rate for all experiments. Can the authors provide more details on what learning rate they use and why they choose to use a fixed learning rate? 
- The authors mention that the label sharpness of a dataset is higher for medical image datasets than natural image datasets. Can the authors provide more insights into why this is the case? Is it because medical images are more similar to each other than natural images, or is it because the boundaries between different classes are more complex in medical images?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
