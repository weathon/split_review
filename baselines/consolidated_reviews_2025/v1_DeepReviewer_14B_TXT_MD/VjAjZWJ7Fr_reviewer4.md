### Summary

This paper presents a novel graph-based framework for addressing both OOD generalization and detection problems. The authors propose a spectral contrastive loss derived from the spectral decomposition of the graph's adjacency matrix. The framework enables end-to-end training and establishes a theoretical equivalence between learned representations and spectral decomposition on the graph. The paper provides theoretical insights into OOD generalization and detection performance through spectral analysis of the graph. Empirical results demonstrate the effectiveness of the proposed algorithm, showcasing improvements in both OOD generalization and detection performance compared to state-of-the-art methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel graph-based framework for jointly addressing OOD generalization and detection, which is a significant contribution to the field.
2. The theoretical analysis provides valuable insights into the relationship between spectral decomposition and OOD performance, enhancing the understanding of the problem.
3. The proposed spectral contrastive loss is derived from a solid theoretical foundation and has both practical and theoretical value.
4. The empirical results demonstrate the effectiveness of the proposed algorithm, showcasing substantial improvements in OOD generalization and detection performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the unlabeled data is a mixture of ID, covariate-shifted OOD, and semantic-shifted OOD data. However, in real-world scenarios, it is often difficult to guarantee that the unlabeled data contains all three types of data. The performance of the proposed method may be affected if the unlabeled data does not meet this assumption. Specifically, the method's reliance on a specific mixture ratio of these data types is not thoroughly explored, and the sensitivity to deviations from this ratio is unclear. For example, what happens if the unlabeled data is predominantly in-distribution with very little OOD data, or vice-versa? The paper should include a more detailed analysis of how the performance degrades under different mixture ratios.
2. The paper uses a specific distance-based method (KNN distance) for OOD detection. While this method aligns with the theoretical analysis, it may not be the most effective method in all scenarios. The paper could benefit from exploring other OOD detection methods and comparing their performance with the proposed method. The choice of KNN distance, while simple, might not capture complex relationships in the feature space, and a more sophisticated distance metric or a learned distance function could potentially yield better results. The paper lacks a discussion on the limitations of KNN distance and how it might affect the overall performance, especially in high-dimensional spaces where KNN can suffer from the curse of dimensionality.
3. The paper focuses on a specific data setup and learning goal. It is unclear how the proposed method would perform in other scenarios or with different types of data. The paper could benefit from exploring the generalizability of the proposed method to other datasets and tasks. The current evaluation is limited to a specific set of datasets and tasks, and it is not clear how the method would perform on datasets with different characteristics, such as those with different modalities (e.g., text, audio) or those with different types of distribution shifts. The paper should include a more comprehensive evaluation across a wider range of datasets and tasks to demonstrate the robustness and generalizability of the proposed method.

### Suggestions

The paper should include a more thorough investigation into the sensitivity of the proposed method to the mixture ratio of ID, covariate-shifted OOD, and semantic-shifted OOD data in the unlabeled set. Specifically, the authors should conduct experiments where the proportions of these data types are systematically varied, and the impact on both OOD generalization and detection performance is measured. This analysis should include scenarios where one or more of the data types are underrepresented or overrepresented. Furthermore, the authors should explore the theoretical implications of these variations and discuss how the spectral properties of the graph are affected by changes in the data mixture. This would provide a more complete understanding of the method's robustness and limitations.

To address the limitations of using KNN distance for OOD detection, the authors should explore alternative distance metrics or learned distance functions. For example, they could investigate the use of Mahalanobis distance, which takes into account the covariance structure of the data, or explore learning a distance metric using a neural network. The paper should also include a comparative analysis of the performance of these different methods, along with a discussion of their strengths and weaknesses. This would provide a more comprehensive evaluation of the OOD detection capabilities of the proposed framework and potentially lead to improved performance. The authors should also discuss the computational cost of these different methods and how it might affect their practical applicability.

Finally, the paper should include a more comprehensive evaluation of the proposed method on a wider range of datasets and tasks. This should include datasets with different modalities (e.g., text, audio) and different types of distribution shifts. The authors should also explore the performance of the method on tasks beyond image classification, such as object detection or semantic segmentation. This would provide a more complete picture of the generalizability of the proposed method and its potential for real-world applications. The paper should also include a discussion of the limitations of the method and potential directions for future research.

### Questions

1. How does the proposed method perform when the unlabeled data does not contain all three types of data (ID, covariate-shifted OOD, and semantic-shifted OOD)?
2. Can the authors provide more insights into the choice of the distance-based method (KNN distance) for OOD detection? Are there any other OOD detection methods that could be explored?
3. How does the proposed method perform on other datasets and tasks beyond the ones presented in the paper? Are there any limitations to the generalizability of the method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
