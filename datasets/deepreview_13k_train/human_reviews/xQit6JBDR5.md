# Look Around and Find Out: OOD Detection with Relative Angles

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Deep learning systems deployed in real-world applications often encounter data that is different from their in-distribution (ID). A reliable system should ideally abstain from making decisions in this out-of-distribution (OOD) setting. Existing state-of-the-art methods primarily focus on feature distances, such as k-th nearest neighbors and distances to decision boundaries, either overlooking or ineffectively using in-distribution statistics. In this work, we propose a novel angle-based metric for OOD detection that is computed relative to the in-distribution structure. We demonstrate that the angles between feature representations and decision boundaries, viewed from the mean of in-distribution features, serve as an effective discriminative factor between ID and OOD data. Our method achieves state-of-the-art performance on CIFAR-10 and ImageNet benchmarks, reducing FPR95 by $0.88\%$ and $7.74\%$ respectively. Our score function is compatible with existing feature space regularization techniques, enhancing performance. Additionally, its scale-invariance property enables creating an ensemble of models for OOD detection via simple score summation

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to calculate the angle between the feature representation and the decision boundary, viewing from the mean of ID representations, to compute a score for identifying OOD examples. The method is evaluated on two popular benchmarks: CIFAR100 and Imagenet for OOD detection.

### Strengths
1. The paper is well-written and easy to follow.

2. Relying on the angle between feature representations and the decision boundary seems to be novel.

3. The geometric interpretation of the presented method is convincing.

4. The presented method can easily be integrated into existing frameworks.

### Weaknesses
1. I am somewhat skeptical about the performance gain. Although the paper claim performance gains across both benchmarks, the improvement is marginal for CIFAR100 (0.8% FPR95) and only evident on average. Looking at Table 1 and Table 2, the method lags behind other methods on an individual basis. It’s important to discuss why the method does not generalize well on an individual basis.

2. The method is only compared on ResNet architectures. How does it perform on other recent architectures, such as Vision Transformers? Given that the method relies heavily on feature and decision boundaries, validating it on diverse architectures is essential to confirm its architecture-agnostic and plug-in characteristics.

Minor Fixes: Please review the references. Some include only the publication year without the publication venue.

### Questions
Mostly, my concerns are on performance gain and the experiments on different architectures. If authors can convincingly address my concerns, I am willing to change my rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel method for out-of-distribution (OOD) detection based on feature representations in neural networks. The proposed approach, LAFO (Look Around and Find Out), introduces an angle-based metric that measures the angle between feature representations and decision boundaries relative to the mean in-distribution (ID) feature. This approach leverages the relationship between feature vectors and decision boundaries to differentiate between ID and OOD samples effectively.

### Strengths
1. The idea sounds novel. The paper introduces a novel angle-based metric for OOD detection, which measures the angle between feature representations and decision boundaries relative to the mean of in-distribution (ID) data.

2. This paper conducts extensive experiments to validate the proposed approach, including the standard benchmarks, and demonstrates its flexibility by incorporating it into ensemble methods and combining it with activation shaping algorithms.

3. This paper also explained the connection between LAFO and the similar approach fDBD.

### Weaknesses
1. The exploration of ID statistics beyond the mean is limited. As OOD detection can benefit from a richer representation of ID statistics, does the "ID mean" refer to the mean across all classes? How about class-specific means or other statistical summaries, such as variance or higher-order moments? If the author includes these experiments or analyses, the paper will be strengthened. Specifically, the paper should investigate whether using a single mean for all classes is sufficient, or if class-specific means would provide a more discriminative reference point for OOD detection. Furthermore, exploring the impact of using covariance or other higher-order statistics of the in-distribution data could reveal if the proposed angle-based metric is sensitive to the shape of the in-distribution feature space, not just its central tendency.

2. The experiments do not sufficiently address why and how LAFO enhances ensemble performance compared to other methods. It would be beneficial to see a more detailed analysis of how the angle-based scores behave in various ensemble settings, such as different architectures or training losses, to better understand when and why LAFO performs optimally. For example, the paper should analyze the correlation between LAFO scores and the performance of individual models within an ensemble. It should also investigate whether LAFO's performance gain is consistent across different ensemble sizes and model diversity. A deeper dive into the specific scenarios where LAFO excels, and where it might fall short, would provide a more complete understanding of its practical utility.

### Questions
1. Why is the CSI baseline used for CIFAR10 OOD benchmark, but not used for imageNet benchmark?

2. Did you consider the application of LAFO on multi-modal foundation models, such as CLIP?

3. The feature is evaluated through the composed function $f_1\circ...\circ f_{L-1} \circ g $, can you explain the reason why using this way or show some references for this? Did you consider other ways to represent features?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents Look Around and Find Out (LAFO), a novel approach for out-of-distribution (OOD) detection using angle-based metrics. By calculating angles between feature representations and decision boundaries in relation to the mean of in-distribution (ID) features, LAFO improves OOD detection performance by leveraging the geometric relationships within feature space. The proposed method demonstrates robust performance across multiple benchmarks (CIFAR-10, ImageNet), significantly reducing false positive rates (FPR95) compared to state-of-the-art methods. Additionally, LAFO is hyperparameter-free, scale-invariant, and compatible with ensemble models, which enhances its practical utility.

### Strengths
- The angle-based approach relative to ID mean is novel in differentiating ID and OOD samples.
- LAFO’s lack of hyperparameters simplifies its use in practical scenarios and avoids overfitting issues associated with tuning.
- The model achieves impressive results on CIFAR-10 and ImageNet, showcasing its scalability from smaller to larger datasets.
- LAFO can be combined with other activation shaping methods, demonstrating flexibility in enhancing model confidence scores.

### Weaknesses
 - While effective, using only the ID mean for centering may limit adaptability across highly variable datasets. Incorporating other statistics, such as the covariance matrix or higher-order moments of the in-distribution features, could potentially capture more complex data structures and improve robustness, especially when dealing with multimodal in-distribution data. This could lead to better separation of in- and out-of-distribution samples in more challenging scenarios.
- The experiments focus on ResNet architectures. Additional comparisons with transformer-based or CLIP-based architectures are needed to fully assess the generalizability of LAFO, given the different inductive biases and feature representations learned by these models. For example, transformer models often have more global receptive fields and might interact differently with the proposed angle-based metric. It would be beneficial to see how LAFO performs when applied to features extracted from these architectures.
- The paper does not fully explore scenarios where LAFO may struggle, such as in cases with minimal separability between ID and OOD distributions. Specifically, the paper should include experiments where the OOD data is semantically close to the ID data, or where the OOD data is generated through adversarial perturbations of the ID data. These scenarios could reveal limitations of the method in cases where the geometric separation is not as clear.
- Although LAFO is efficient, the paper could address its performance in real-time or resource-constrained settings to provide a more comprehensive view. While the method is claimed to be efficient, a more detailed analysis of its computational cost, especially in terms of memory and time complexity, would be valuable. This should include a breakdown of the computational cost of each step, such as feature extraction and angle calculation, and how these costs scale with the size of the input data and the dimensionality of the feature space.

### Questions
The effectiveness of LAFO in scenarios with severe ID class overlapping?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposed a novel angle-based metric for OOD detection that is computed relative to the in-distribution structure. They demonstrate that the angles between feature representations and decision boundaries, viewed from the mean of in-distribution features, serve as an effective discriminative factor between ID and OOD data. Experiments on CIFAR10 and ImageNet shows SOTA performance compared to other detection methods.

### Strengths
The performance is good and the analysis is easy to understand.
The metric is scale-invariant, allowing ensemble for better performance.
The experiment is comprehensive.

### Weaknesses
1. From Figure 1, the angle \alpha is helpful for better distinguishing ID and OOD data. And there lacks a comparison between the sine of \alpha, the sine of \theta, and the division of them. I think only the sine of \alpha in Figure 2 is not convincing to demonstrate that the angle \alpha is not very informative for ID and OOD separation.

2. For experiments, I think the author should report detection results on a vanilla trained model, which is a more common and practical setting for post-hoc detection methods. The current results are all based on supervised contrastive training models.

3. For experiments, it should compare with ReAct method on ImageNet OOD benchmark (in Table 2), since my empirical experience tells that ReAct always shows remarkable performance on ImageNet dataset.

### Questions
no more question

### Soundness
2

### Presentation
3

### Contribution
2
