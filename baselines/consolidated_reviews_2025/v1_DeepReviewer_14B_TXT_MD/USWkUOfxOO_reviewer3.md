### Summary

This paper addresses the problem of predictive uncertainty calibration in unsupervised domain adaptation (UDA). The authors propose a novel post-hoc calibration framework called Pseudo-Calibration (PseudoCal), which treats UDA calibration as a target domain-specific unsupervised problem rather than a covariate shift problem across domains. The key idea is to use inference-stage mixup to synthesize a labeled pseudo-target set that mimics the correct-wrong statistics of the real target set, and then apply temperature scaling to this labeled set. The authors conduct extensive empirical evaluations across various UDA scenarios and demonstrate the superior performance of PseudoCal over alternative calibration methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses an important and under-explored problem of predictive uncertainty calibration in unsupervised domain adaptation.
2. The proposed PseudoCal framework is technically sound and well-motivated. The use of inference-stage mixup and cluster assumption to synthesize a labeled pseudo-target set is innovative and effectively addresses the challenges of unsupervised calibration.
3. The authors conduct extensive empirical evaluations across various UDA scenarios and demonstrate the superior performance of PseudoCal over alternative calibration methods. The experiments are comprehensive and the results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from more in-depth analysis of the limitations of the proposed method. For example, how does PseudoCal perform under extreme domain shifts or with limited data? Are there any specific scenarios where PseudoCal might not be effective?
2. The authors could also discuss the computational overhead of PseudoCal compared to other calibration methods. Is the improvement in calibration performance worth the additional computational cost?
3. It would be helpful to provide more insights into the choice of hyperparameters for PseudoCal, such as the mixup ratio and the number of clusters. How sensitive is the performance of PseudoCal to these hyperparameters?

### Suggestions

The paper would be strengthened by a more thorough investigation into the robustness of PseudoCal under various challenging conditions. Specifically, the analysis of performance under extreme domain shifts should be expanded beyond the current partial-set UDA experiments. It would be beneficial to explore scenarios where the target domain exhibits significant changes in data distribution, such as variations in lighting, viewpoint, or background, which are common in real-world applications. For instance, experiments could be designed to simulate a scenario where the target domain contains novel classes not present in the source domain, or where the target domain data is noisy or corrupted. Such experiments would provide a more comprehensive understanding of the limitations of PseudoCal and its applicability in diverse settings. Furthermore, a more detailed analysis of the impact of limited target data is needed. While the authors mention that PseudoCal can be applied in limited source access scenarios, the performance of PseudoCal with limited unlabeled target data should be explicitly investigated. This could involve experiments with varying sizes of target datasets and analyzing the calibration performance as the amount of target data decreases. 

Regarding computational overhead, a more detailed breakdown of the computational cost of each step in PseudoCal would be beneficial. While the authors mention that the method is efficient, a quantitative comparison of the runtime and memory usage of PseudoCal with other calibration methods would be valuable. This should include a breakdown of the time spent on pseudo-label generation, clustering, and temperature scaling. It would also be useful to analyze the scalability of PseudoCal with respect to the size of the target dataset. For example, how does the runtime of PseudoCal change as the number of target samples increases? This analysis would help readers understand the practical implications of using PseudoCal in resource-constrained environments. Furthermore, the authors should discuss the potential for parallelizing the different steps of PseudoCal to further improve its efficiency.

Finally, a more detailed analysis of the hyperparameter sensitivity is needed. While the authors mention that the performance is relatively stable across a range of mixup ratios, a more rigorous analysis of the impact of different mixup ratios on the quality of the pseudo-labels and the final calibration performance is needed. This could involve plotting the calibration error as a function of the mixup ratio and analyzing the trend. Similarly, the authors should provide more guidance on how to choose the optimal number of clusters for k-means. While they mention that the number of clusters is set to the number of classes in the target domain, it would be useful to investigate the sensitivity of the method to this parameter, especially when the true number of classes is unknown or when there is a class imbalance in the target domain. The authors could explore the use of cluster validity indices to automatically determine the optimal number of clusters.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
