### Summary

The paper proposes a unified perspective for Shapley value estimation and a simple amortized estimator SimSHAP. The unified perspective reveals the relationships between different Shapley value estimation methods, while SimSHAP achieves comparable accuracy with orders of magnitude faster computation. The effectiveness of SimSHAP is validated through extensive experiments on both tabular and image datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel unified perspective for Shapley value estimation, which reveals the relationships between different estimation methods.
2. The proposed SimSHAP estimator achieves comparable accuracy with orders of magnitude faster computation.
3. The effectiveness of SimSHAP is validated through extensive experiments on both tabular and image datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The unified perspective of Shapley value estimation is interesting and provides a novel viewpoint for future research.

2. The contribution on SimSHAP is marginal. The SimSHAP is simple to follow. However, the authors claim that SimSHAP is a simple and fast amortized Shapley value estimator. The SimSHAP is based on FastSHAP. The difference between SimSHAP and FastSHAP is the metric matrix. It seems that the performance improvement is marginal. From Table 4, SimSHAP is not faster than FastSHAP.

3. The experimental results are not convincing. The authors only use one image dataset, CIFAR-10, to evaluate the performance of SimSHAP. The authors should evaluate the performance of SimSHAP on other image datasets, e.g., Imagenet.

### Suggestions

The paper's primary weakness lies in the limited empirical validation of the proposed SimSHAP method. While the unified perspective on Shapley value estimation is a valuable contribution, the practical impact of SimSHAP appears incremental. The authors should provide a more thorough evaluation of SimSHAP's performance across a wider range of datasets and model architectures. Specifically, the current evaluation is limited to CIFAR-10 for image data, which is insufficient to demonstrate the general applicability of the method. The authors should include experiments on more complex image datasets, such as ImageNet, and also consider other data modalities to show the robustness of SimSHAP. Furthermore, a more detailed analysis of the computational cost of SimSHAP compared to FastSHAP is needed. The claim that SimSHAP is faster is not fully supported by the results in Table 4, and a more rigorous analysis of the runtime, including a breakdown of the different computational steps, would be beneficial.

To strengthen the empirical evaluation, the authors should also consider including a comparison with other state-of-the-art Shapley value estimation methods, not just FastSHAP. This would provide a better understanding of the relative performance of SimSHAP. The evaluation should also include a more detailed analysis of the accuracy of SimSHAP, beyond the insertion/deletion metrics. For example, the authors could consider using metrics that directly measure the similarity between the estimated Shapley values and the true Shapley values, or at least provide a more detailed analysis of the error distribution. Additionally, the authors should provide a more detailed explanation of the experimental setup, including the specific hyperparameters used for training SimSHAP and the baseline methods. This would make the results more reproducible and allow for a more thorough comparison with other methods.

Finally, the authors should also provide a more detailed discussion of the limitations of SimSHAP. For example, the authors should discuss the potential impact of the choice of the metric matrix on the performance of SimSHAP. They should also discuss the potential limitations of the amortized approach, such as the potential for bias or the sensitivity to the training data. A more thorough discussion of these limitations would help to provide a more balanced assessment of the proposed method. The authors should also consider providing an ablation study to analyze the impact of different components of SimSHAP on its performance. This would help to identify the key factors that contribute to the performance of SimSHAP and provide a better understanding of its behavior.

### Questions

1. Can the authors provide more details on the implementation of SimSHAP and the experimental setup?
2. Can the authors provide more results on other image datasets and model architectures?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
