### Summary

The authors investigate the discrepancies in how neural networks learn from different imaging domains, focusing on the differences between natural and medical images. They explore the relationship between the generalization error of a trained network and the intrinsic dimension of its training set, finding that this relationship varies significantly between medical and natural imaging domains. The authors propose that the higher intrinsic "label sharpness" of medical imaging datasets may contribute to this discrepancy. They also demonstrate that label sharpness is negatively correlated with a model's adversarial robustness, leading to higher vulnerability to adversarial attacks in medical image models. Additionally, the authors extend their analysis to the intrinsic dimension of learned representations and derive a generalization scaling law with respect to this dimension. Their theoretical results are supported by experiments with six models and eleven natural and medical imaging datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new measure of the intrinsic label sharpness of a dataset and derives a neural network generalization scaling law with respect to dataset intrinsic dimension, which includes label sharpness. The experiments support the derived scaling behavior within each of these two domains, and show a distinct difference in the scaling rate between them. 
2. The paper shows how a model's adversarial robustness relates to its training set's label sharpness, and shows that robustness decreases with higher label sharpness. 
3. The paper extends the analysis to the intrinsic dimension of learned representations and reconciles the scaling laws to show that the dataset intrinsic dimension serves as an approximate upper bound for the representation intrinsic dimension.
4. The theoretical results are supported by thorough experiments with six models and eleven natural and medical imaging datasets over a range of training set sizes.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on binary classification tasks, which may limit the generalizability of the findings to multi-class classification problems. The analysis does not explore how the proposed label sharpness metric and the derived scaling laws would behave in scenarios with more than two classes. It is unclear if the observed relationships would hold, or if new factors would emerge in multi-class settings. For instance, the distribution of label sharpness across different classes might vary significantly, potentially affecting the overall generalization behavior.
2. The paper does not provide a detailed analysis of the computational cost associated with estimating the intrinsic dimension and label sharpness, which could be a concern for large-scale datasets. The authors should provide a more thorough discussion of the time complexity of the algorithms used for these estimations, especially when dealing with high-dimensional data and large datasets. Furthermore, the paper lacks a discussion on the practical implications of these computational costs, such as the feasibility of applying these methods in resource-constrained environments.
3. The paper does not explore the impact of different data augmentation techniques on the intrinsic dimension and label sharpness of the datasets, which could be a factor in the observed discrepancies. The authors should investigate how common data augmentation techniques, such as rotations, scaling, and cropping, affect the estimated intrinsic dimension and label sharpness. It is possible that these augmentations could alter the underlying data manifold, thus affecting the observed relationships between intrinsic dimension, label sharpness, and generalization performance. The lack of this analysis limits the practical applicability of the findings.

### Suggestions

The authors should extend their analysis to multi-class classification problems to assess the generalizability of their findings. This could involve experimenting with datasets that have varying numbers of classes and analyzing how the label sharpness metric and the derived scaling laws behave in these scenarios. Specifically, they should investigate whether the relationship between label sharpness and generalization error remains consistent across different numbers of classes, and if not, what factors might be responsible for the discrepancies. Furthermore, they should explore the distribution of label sharpness across different classes and how this distribution affects the overall generalization performance. This would provide a more comprehensive understanding of the applicability of their proposed framework.

To address the computational concerns, the authors should provide a detailed analysis of the time complexity of the algorithms used for estimating intrinsic dimension and label sharpness. This analysis should include a discussion of how the computational cost scales with the size of the dataset and the dimensionality of the data. They should also explore potential optimizations or approximations that could reduce the computational burden, making these methods more practical for large-scale datasets. Furthermore, the authors should discuss the practical implications of these computational costs, such as the feasibility of applying these methods in resource-constrained environments. This would help to clarify the limitations of their approach and guide future research in this area.

Finally, the authors should investigate the impact of different data augmentation techniques on the intrinsic dimension and label sharpness of the datasets. This could involve experimenting with common data augmentation techniques, such as rotations, scaling, and cropping, and analyzing how these transformations affect the estimated intrinsic dimension and label sharpness. They should also explore whether these augmentations can be used to improve the generalization performance of models by modifying the underlying data manifold. This analysis would provide a more complete picture of the factors that influence the observed relationships and enhance the practical applicability of the findings. It would also be beneficial to explore if specific augmentations are more effective in modifying the intrinsic dimension or label sharpness, and how this relates to the generalization performance.

### Questions

1. How does the proposed framework extend to multi-class classification problems, and what are the potential challenges in applying it to such scenarios?
2. What is the computational cost associated with estimating the intrinsic dimension and label sharpness, and how does it scale with the size of the dataset?
3. How do different data augmentation techniques affect the intrinsic dimension and label sharpness of the datasets, and what are the implications for the observed discrepancies in generalization behavior?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
