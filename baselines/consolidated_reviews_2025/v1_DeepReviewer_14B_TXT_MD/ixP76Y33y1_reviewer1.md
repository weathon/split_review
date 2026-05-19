### Summary

The authors investigate the relationship between generalization error and the intrinsic dimension of the training dataset, observing that the generalization error increases as the intrinsic dimension grows. They also note that the rate of increase varies between medical and natural imaging domains. To address this discrepancy, the authors propose a metric called "label sharpness," which is higher for medical image datasets. They suggest that the label sharpness can explain the difference in the relationship between generalization error and intrinsic dimension for the two domains. Additionally, the authors extend their analysis to the intrinsic dimension of learned representations and show that it is bounded by the dataset intrinsic dimension.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors conduct a thorough analysis of the relationship between generalization error and the intrinsic dimension of the training dataset. They also investigate the discrepancy between medical and natural imaging domains, which is an important contribution to the field.
2. The authors propose a new metric called "label sharpness" to explain the difference in the relationship between generalization error and intrinsic dimension for medical and natural imaging domains. This is a novel contribution that can help us better understand the behavior of neural networks.
3. The authors show that the intrinsic dimension of learned representations is bounded by the dataset intrinsic dimension. This is an important result that can help us better understand the behavior of neural networks.

### Weaknesses

#### Some Related Works


#### comment

1. While the authors provide a theoretical justification for their results, it is not clear how this can be used in practice. For example, how can we use the theoretical results to design better neural network architectures or training procedures? The theoretical analysis, while interesting, lacks concrete guidance for practical application. Specifically, the paper does not detail how the derived relationships between generalization error, intrinsic dimension, and label sharpness can be leveraged to improve model performance beyond the observed correlations. It remains unclear how one would use these theoretical insights to guide architectural choices, hyperparameter tuning, or data augmentation strategies. The connection between the theoretical findings and actionable improvements in model training is not explicitly established.
2. The authors only consider CNNs for their analysis. It would be interesting to see if the results generalize to other types of neural networks, such as transformers. The scope of the analysis is limited by the exclusive focus on CNNs. The paper does not provide any evidence or discussion regarding the applicability of the findings to other architectures, such as transformers, which have become increasingly prevalent in various domains, including medical imaging. This raises concerns about the generalizability of the conclusions and limits the impact of the study.
3. The authors only consider binary classification tasks. It would be interesting to see if the results generalize to multi-class classification tasks. The analysis is further constrained by the focus on binary classification tasks. The paper lacks any exploration of how the proposed metrics and relationships behave in multi-class scenarios, which are common in real-world applications. This limitation restricts the applicability of the findings and raises questions about their validity in more complex classification problems.

### Suggestions

To enhance the practical relevance of the theoretical results, the authors should provide concrete examples of how their findings can be used to improve neural network design and training. For instance, they could explore how the relationship between generalization error and intrinsic dimension can inform the selection of appropriate network depth or width for a given dataset. They could also investigate how label sharpness can be used to guide the development of data augmentation strategies that specifically target the identified boundaries between classes. Furthermore, the authors could demonstrate how their theoretical framework can be used to diagnose and address overfitting issues by analyzing the intrinsic dimension of the training data and the learned representations. This would involve showing how the proposed metrics can be used to identify when a model is learning a representation that is too complex for the given data, and how this information can be used to adjust the training process. The authors should also consider providing a practical algorithm or heuristic that practitioners can use to apply their theoretical findings to real-world problems.

To address the limitation of only considering CNNs, the authors should extend their analysis to include other neural network architectures, particularly transformers. This would involve conducting experiments on transformer-based models and comparing the results with those obtained for CNNs. The authors should investigate whether the relationship between generalization error, intrinsic dimension, and label sharpness holds for transformers, and if not, what are the key differences. This would require a detailed analysis of the intrinsic dimension of the learned representations in transformers and how they relate to the dataset intrinsic dimension. The authors should also explore whether the concept of label sharpness is applicable to transformers and if it can be used to explain the performance differences between transformers and CNNs. This would provide a more comprehensive understanding of the proposed framework and its applicability to different types of neural networks.

Finally, to broaden the scope of their analysis, the authors should investigate the generalizability of their findings to multi-class classification tasks. This would involve conducting experiments on datasets with multiple classes and analyzing how the proposed metrics and relationships behave in these scenarios. The authors should explore whether the concept of label sharpness can be extended to multi-class problems and if it can be used to explain the performance differences between different classes. This would require a detailed analysis of the decision boundaries in multi-class problems and how they relate to the intrinsic dimension of the dataset and the learned representations. The authors should also investigate whether the intrinsic dimension of the learned representations is still bounded by the dataset intrinsic dimension in multi-class scenarios. This would provide a more complete understanding of the proposed framework and its applicability to real-world problems.

### Questions

1. How can the theoretical results be used in practice to design better neural network architectures or training procedures?
2. Do the results generalize to other types of neural networks, such as transformers?
3. Do the results generalize to multi-class classification tasks?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
