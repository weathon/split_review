### Summary

This paper aims to improve the performance of normalizing flows for out-of-distribution (OOD) detection. The authors propose to train the normalizing flow model with synthetic outliers, which are generated from in-domain data by some data augmentation and image processing techniques. The synthetic outliers are used to minimize the likelihood of out-of-distribution samples. The authors also propose a softplus-based penalty to avoid numerical instability. The proposed method is evaluated on several image and text datasets, and the results show that it can improve the OOD detection performance compared to the baseline methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive and the results are promising.

### Weaknesses

#### Some Related Works

[1] Inverting the flow: Invertible generative models for anomaly detection.
[2] Anomaly detection with invertible flow models.

#### comment

1. The novelty of this paper is questionable. The method is a combination of data augmentation and outlier exposure, which have been proposed in the literature. The use of the softplus function in the loss function seems to be a minor modification that does not add much value. The paper fails to demonstrate a significant advantage over existing methods. Specifically, the paper does not adequately address how the proposed method differs fundamentally from existing data augmentation techniques used in conjunction with outlier exposure. The synthetic outlier generation, while utilizing common techniques, lacks a clear justification for why these specific methods are superior to other possible augmentations or synthetic data generation strategies. The paper also fails to provide a rigorous ablation study to isolate the impact of the softplus function, making it difficult to assess its contribution beyond a simple smoothing parameter.
2. The paper only compares with basic baselines, such as MLE and RO, and does not include any recent state-of-the-art methods for OOD detection with normalizing flows, such as Ref. [1]. The paper does not provide a clear explanation of why these comparisons were omitted. The lack of comparison with methods that explicitly address the likelihood bias in normalizing flows, such as those using contrastive learning or adversarial training, makes it difficult to assess the true performance of the proposed method. Furthermore, the paper does not discuss the computational cost of the proposed method compared to existing approaches, which is a crucial factor for practical applications.
3. The paper only shows the results on a limited number of datasets, mostly low-dimensional image datasets like CIFAR and SVHN, and text datasets. The paper does not test the method on more challenging and realistic datasets, such as ImageNet or COCO, which are widely used for OOD detection. The results are not convincing enough to demonstrate the generalization and robustness of the method to different domains and modalities. The paper also lacks a thorough analysis of the failure cases of the proposed method, which would provide valuable insights into its limitations and potential areas for improvement. The absence of experiments on high-resolution images and more complex data distributions raises concerns about the scalability and applicability of the method to real-world scenarios.

### Suggestions

The paper needs to provide a more thorough justification for the novelty of the proposed method. It should clearly articulate how the combination of synthetic outlier generation and the softplus loss function differs from existing data augmentation and outlier exposure techniques. A detailed ablation study is necessary to isolate the impact of each component, particularly the softplus function, and demonstrate its specific contribution to the overall performance. The authors should also explore alternative synthetic outlier generation methods and provide a rationale for their choice. Furthermore, the paper should include a discussion of the computational cost of the proposed method compared to existing approaches, which is a crucial factor for practical applications. The paper should also include a more detailed analysis of the failure cases of the proposed method, which would provide valuable insights into its limitations and potential areas for improvement.

To address the lack of comparison with state-of-the-art methods, the authors should include a comprehensive comparison with recent methods for OOD detection with normalizing flows, including those that explicitly address the likelihood bias. This should include methods that use contrastive learning, adversarial training, or other techniques to improve the robustness of normalizing flows for OOD detection. The authors should also provide a clear explanation for why certain methods were omitted from the comparison and justify their choice of baselines. The comparison should not only focus on overall performance but also consider the computational cost, robustness, and sensitivity to hyperparameters of each method. A more detailed analysis of the strengths and weaknesses of the proposed method compared to existing approaches would greatly enhance the paper's contribution.

Finally, the paper needs to demonstrate the generalization and robustness of the proposed method by testing it on more challenging and realistic datasets, such as ImageNet or COCO. The authors should also explore the applicability of the method to other data modalities, such as audio or time series data. The paper should include a thorough analysis of the performance of the method on high-resolution images and more complex data distributions. This would provide valuable insights into the scalability and applicability of the method to real-world scenarios. The authors should also discuss the limitations of the method and potential areas for future research. The paper should also include a more detailed analysis of the failure cases of the proposed method, which would provide valuable insights into its limitations and potential areas for improvement.

### Questions

1. How does the proposed method compare with other recent methods for OOD detection with normalizing flows?
2. How does the proposed method perform on more challenging and realistic datasets, such as ImageNet or COCO?

### Rating

6

### Confidence

3

**********
