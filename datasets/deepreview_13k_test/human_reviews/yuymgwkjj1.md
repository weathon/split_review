# Correcting the Bias of  Normalizing Flows by Synthetic Outliers for Improving Out-of-Distribution Detection

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Out-of-distribution (OOD) detection is critical for ensuring the reliability and robustness of deep learning models in real-world applications. While normalizing flows have demonstrated impressive performance for various task of image OOD detection, recent findings suggest that they still encounter limitations and severe biases when applied to datasets with different statistics. Specifically, it has been observed that normalizing flow models tend to assign higher likelihoods to OOD samples with low complexity, which undermines the effectiveness of likelihood based OOD detection methods. In this paper, we explore the bias related to data complexity linked to normalizing flow models  in OOD detection. We propose a novel method for bias correction by incorporating synthetic outliers during training, guiding the model to assign lower likelihoods to OOD samples. Additionally, we introduce a specialized training objective that leverages the softplus function for OOD data, ensuring a smooth and effective training process. Extensive experiments on benchmark and high-dimensional real-world datasets, including both images and texts, confirm that our proposed approach significantly enhances OOD detection accuracy, achieving performance comparable to models trained with a limited number of real outliers. Moreover, our method increases the Lipschitz constant, supporting the hypothesis presented in related literature.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the problem of OOD detection, specifically focusing on correcting the likelihood bias in normalizing flows that affects their performance in OOD detection. The authors propose incorporating synthetic outliers during training and introduce an adversarial likelihood objective, utilizing the softplus function to improve model stability. Experiments on both benchmark datasets and high-dimensional real-world datasets show that the proposed method achieves significant improvements in OOD detection accuracy, yielding results comparable to models trained with limited real outlier data.

### Strengths
- The paper proposes a novel approach by using synthetic outliers to correct bias in normalizing flows for OOD detection, uniquely addressing data complexity issues. The softplus-based objective further enhances model stability, setting this method apart in improving robustness.

- The experimental setup is thorough, including benchmarks across various datasets and both image and text modalities. The results consistently demonstrate the effectiveness of the proposed approach, particularly in improving AUROC and other detection metrics.

- The paper is well-organized, and the methodology is explained in detail, making it easy for readers to understand the approach. The visualizations, such as complexity distributions and comparisons between standard and softplus-based training, add clarity to the results and methodology.

### Weaknesses
- The choice of synthetic outliers, particularly using Gaussian blur for images, may limit applicability to cases where blurring captures outlier characteristics. For complex datasets with nuanced OOD structures, more sophisticated synthetic outlier generation techniques may be needed.

- While the softplus objective enhances stability, it introduces additional computational overhead, especially in high-dimensional data scenarios. The paper could explore potential optimizations for large-scale datasets.

- The method’s performance is heavily tied to the complexity assumptions underlying the model. The complexity-adjusted scoring approach, while effective, might misinterpret data with atypical structures. Additional investigation into adapting complexity measures could broaden the method's applicability.

### Questions
- How does the method handle OOD data that exhibit similar complexity levels to the ID data but differ in semantic content? Could the current approach potentially overlook such cases?

- Is the choice of Gaussian blur for synthetic outlier generation extendable to other domains, or would you recommend domain-specific modifications for applications outside of vision and text?

- Could you elaborate on any observed trade-offs between using synthetic outliers versus real outliers in terms of computational efficiency and detection accuracy?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aim to alleviate a well-known weakness of normalizing flows models towards detecting complexity for the task of out-of-distribution (OOD) detection. To accomplish this, the presented methodology is composed of three changes. First, the method applies gaussian blur to the original in-distribution (ID) images to generate synthetic OOD images. Second, the method add an additional softplus function to the maximum likelihood objective to prevent numerical instability. Lastly, the method construct a new OOD score that is the combination of the predicted likelihood and the complexity of the image. The paper reveals that these modification improved the OOD detection capabilities of the normalizing flow model considerably.

### Strengths
1. The motivation and methodology design is concise and very written.
2. The dataset used for evaluation is comprehensive: SVNH, LSUN, CelebA, CIFAR-10, CIFAR-100 for visual recognition; Chest X-ray, RealBlur, and KonIQ-10K for high-resolution imaging, and movie reviews, AG News, SST-2, and WikiText-2 for text.
3. Detection performance shows improvement from the addition of synthetic outliers and complexity scoring.

### Weaknesses
1. The in-distribution performance is completely missing in the evaluation. While the paper shows that adding synthetic OOD images via blurring improves detection performance, how does it affect the normalizing flow's ability to model the ID data distribution (i.e. FID between the generated images and ID images)?
2. The performance gains from using synthetic outliers is very marginal compared to complexity score. It is unclear whether it is even necessary (especially considering 1.) because after adding the complexity score (shown in Table 3), the effect of adding synthetic data is very marginal (sometime even slightly worse than MLE in the case of SVNH). 
3. The significance and novelty with the addition of the complexity score is weak since it is underexplored in this work. The usage of JPEG2000 compression to calculate complexity limits its uses to only image data, and hence, the lack of evaluation of complexity scores on high-resolution image data and text data.
4. The paper does not provide literature support of the claim "synthetic outliers enhance the local Lipschitz constant, improving model stability and performance" in line 432-437. This claim is counterintuitive: the Lipschitz constant provides an upper bound on the change in model prediction, which is looser with higher constant. i.e. prediction can be more sensitive towards small perturbations, and hence, less stable. Empirical evidence or theoretical justification is needed to justify this counterintuitive claim.

### Questions
1. The paper claim to estimate Lipschitz Constant by taking the L_infinity norm of the gradient vector. How are the samples selected here? 
2. What is the slope and R^2/correlation of likelihood vs. complexity in Figure 3? It seems like the relationship between likelihood and complexity is rather weak.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to improve the out-of-distribution detection performance of Normalizing Flows. The paper is motivated by observation from a previous work that generative models, including normalizing flows, assign high likelihood to less complex OOD data, resulting in misclassifying such OOD data as ID data. To address the issue, the proposed method proposes to generate simple OOD data by simply applying Gaussian blur on ID data. Then, the model proposes to minimize the softplus function of likelihood of these synthetic OOD for training stability. As a result, the paper demonstrates non-trivial OOD detection performance improvement upon NF baselines.

### Strengths
- The paper is well-written and easy to follow.
- The paper introduces a simple yet effective approach to improve the OOD performance of NF models.
- The proposed idea of generating low-complexity OOD to mitigate previously found drawbacks of NF models is well motivated.

### Weaknesses
- The proposed augmentation method is rather too simple that it raises several concerns.
   - There could be several cases in a real-world scenario, where a blurry image is not OOD but ID instead. How to handle such cases?
   - Would this work on more real-world datasets, such as MVTecAD and ShanghaiTech?

- The paper lacks enough discussions on prior works. For example, there is another OOD/anomaly detection paper that extends NF framework design to learn to handle synthetic OOD [A]. Can authors provide discussions and quantitative comparisons against this method (with the same augmentation suggested by the authors or by this paper)?

- In the paper, it says "By fine-tuning the outlier synthesis probability through validation, we achieve an optimal balance between maximizing the likelihood of ID samples and minimizing the likelihood of OOD samples." What is a validation set here? What kind of data is in the validation set? What is its size?

- I'm not really convinced that using synthetic OOD with low complexity is the key. If you generate enough and diverse OOD samples, wouldn't it be helpful even though it's complex? What about applying aug methods that make it more complex (cutmix, mixup, etc)? I believe these kinds of augmentation methods will lead to more complex OOD data but still improve the OOD performance, possibly more than simple Gaussin blurs. The experiments on this could strengthen the authors' claims.


[A] SANFlow: Semantic-Aware Normalizing Flow for Anomaly Detection and Localization, NeurIPS 2023

### Questions
I have incorporated questions in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
- The author finds that normalizing models tend to assign higher likelihood to the input data. Therefore, when the complexity of ID data is lower than that of OOD data, the model will detect OOD samples better. To correct this bias, the author generates synthetic outliers with lower complexity while forcing the model to assign lower likelihood to them.

### Strengths
- The paper is well organized and easy to follow.
- The author provides many formulations which help to understand the main pipeline of the manuscript.
- The experiments demonstrate that synthetic outliers improve the detection performance of normalizing flow models.

### Weaknesses
- Synthetic outliers is not a novel topic in OOD detection. Similar papers include NPOS (arXiv:2303.02966), VOS (arXiv:2202.01197), SSOD (arXiv:2307.00519), to name a few. Besides, there are also many papers which generate synthetic OOD images to provide auxiliary supervision. Therefore, it seems that this manuscript is not creative enough.
- Lack of comparisons with other OOD synthesis methods.
- The performance is poor compared with SOTA techniques. The OpenOOD benchmark (https://github.com/Jingkang50/OpenOOD) collects main OOD detection methods and demonstrates their FPR95 and AUROC.

### Questions
see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
