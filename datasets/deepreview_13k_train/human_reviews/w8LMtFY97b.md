# Hierarchical Uncertainty Estimation for Learning-based Registration in Neuroimaging

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Over recent years, deep learning based image registration has achieved impressive accuracy in many domains, including medical imaging and, specifically, human neuroimaging with magnetic resonance imaging (MRI). However, the uncertainty estimation associated with these methods has been largely limited to the application of generic techniques (e.g., Monte Carlo dropout) that do not exploit the peculiarities of the problem domain, particularly spatial modeling. Here, we propose a principled way to propagate uncertainties (epistemic or aleatoric) estimated at the level of spatial location by these methods, to the level of global transformation models, and further to downstream tasks. 
Specifically, we justify the choice of a Gaussian distribution for the local uncertainty modeling, and then propose a framework where uncertainties spread across hierarchical levels, depending on the choice of transformation model.
Experiments on publicly available data sets show that Monte Carlo dropout correlates very poorly with the reference registration error, whereas our uncertainty estimates correlate much better. % with the reference registration error.
Crucially, the results also show that uncertainty-aware fitting of transformations improves the registration accuracy of brain MRI scans. Finally, we illustrate how sampling from the posterior distribution of the transformations can be used to propagate uncertainties to downstream neuroimaging tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors present a method to estimate the uncertainty in medical image registration at 3 different stages: (1) on the estimate of the distribution of the deformation field at each voxel (assuming this is Gaussian and gathering a mean and standard deviation per point), (2) on the distribution of the fitted transformation, and (3) on the distribution of possible outcomes on the downstream task. The uncertainty from the first level is used in the transformation fitting step weighting down contributions from less certain pixels. By drawing samples of the fitted transformation, a distribution of results for the same downstream task is generated which is used to estimate the 3rd level of uncertainty. Authors demonstrate their approach in the context of registration-based Brain image segmentation where the given input image is deformed to match the standard MNI atlas and the labels from the atlas are propagated to the deformed image.

### Strengths
* Authors clearly lay out their proposed framework describing the 3 level of uncertainty they they aim to model.
* The results are presented such that each level of uncertainty is evaluated - this makes it easy for the reader to better understand the Authors important contribution.
* Authors provide analysis of the estimates of uncertainty, and demonstrate that the aleotoric uncertainty corresponds better with coordinate prediction error at the first level.
* The figures in the paper are very useful for visualizing the variations that arise from sampling the fitted transform - they demonstrate the fundamental problem with biomedical image registration in that the results from a downstream task are highly dependend on the transformation paramaters, but the uncertainty can be successfully quantified.

### Weaknesses
 * The addition of uncertainty in the fit transform did not impact the result from the Demons transformation model. Authors explain that this is likely because the loss from the Demons method is used in the segmentation loss and that leads to the average coordinates landing close to the optimum. This is unclear - please can Authors expand on this and also elaborate on whether they would expect to see improvements if they used an alternative to Demons?

 * The panel labels in Figure 2 are badly formatted - please make these clearer.

### Questions
* The panel labels in Figure 2 are badly formatted - please make these clearer.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a framework to integrate uncertainty estimation into deep learning-based image registration for neuroimaging. By propagating epistemic and aleatoric uncertainties from voxel-level predictions to transformation models and downstream tasks, the framework enhances registration accuracy and reliability. Experiments show that this uncertainty-aware approach can boost brain MRI registration performance.

### Strengths
1. This paper addresses an important problem in neuroimaging, aiming to use uncertainty estimation to enhance the accuracy and reliability of deep learning-based registration.
2. The figures and explanations are clear and well-organized, which makes complex ideas easier to understand.
3. The empirical findings are insightful. The authors compare their proposed method with other different methods.

### Weaknesses
1. The presentation could be improved. The background, motivation, and knowledge gap are not clearly explained, making it challenging to follow the paper’s purpose and direction. Although the study is about why uncertainty estimation matters in brain registration, it doesn’t make a strong case for why this is important. There isn’t enough support or reasoning behind this focus, which leaves readers unsure about the value or impact of the work.
2. The experiments are insufficient. This paper only compares its method to a single approach, RbR. Although RbR was released in 2024, it is still unpublished and available only on arXiv, which makes it less robust as a baseline for comparison. Including more established and published baselines would be essential to provide a solid foundation for evaluating the effectiveness of the proposed approach.
3. From the experimental results (e.g., Table 1), the introduction of uncertainty estimation does not appear to provide a statistically significant improvement to the model. This makes it difficult to assess its effectiveness and raises questions about the practical value of incorporating uncertainty estimation into the approach.
4. Most of the latest work in brain registration focuses on unsupervised learning, largely due to the high cost of collecting accurate transformation ground-truth for high-dimensional images (e.g., 3D MRI). However, this paper still stay on a supervised learning approach, making it seem less aligned with current trends and potentially less practical for real-world applications where labeled data is limited.
5. The evaluation criteria lack validity. This paper collects ground-truth transformations using NiftyReg, a tool introduced around 15 years ago. Since then, more state-of-the-art methods have been shown to outperform NiftyReg, indicating that the ground-truth it provides may be inaccurate. This undermines the reliability of the results presented in the paper and raises concerns about the credibility of its findings.
6. The novelty of this work is limited. The main contribution appears to be the addition of an uncertainty loss term, while the other loss terms and network architecture are based on existing work. This incremental improvement does not significantly advance the field, as much of the framework relies on previously established methods.

### Questions
1. Why is uncertainty estimation important in neuroimaging registration? What specific benefits does it bring, and why is it necessary?
2. For modeling epistemic uncertainty, why did the author choose to use Monte Carlo dropout, and how exactly was it implemented?
3. Given that the deformation field (non-linear transformation) is a high-dimensional tensor, how do authors verify the accuracy of the ground-truth labels when collecting them? As I understand, NiftyReg is a registration method—if this method is used to generate ground-truth labels, does that imply the proposed method can only perform as well as NiftyReg at best?
4. The total training loss includes multiple terms marked as optional in the paper. Are these terms truly necessary? Was an ablation study conducted to assess their impact on performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a registration framework that includes uncertainty estimation at three different levels (network output, transform models' parameters and downstream tasks). They show that uncertainty estimates correlate with registration errors and that estimating uncertainty can improve registration performance. The approach is applied to brain MRI registration.

### Strengths
- The framework proposed is flexible and can be applied to a broad range of registration techniques.
- The authors performed diverse experiments to validate their approach.
- The results are mostly convincing.
- The paper is well written and related works well introduced.

### Weaknesses
 - The ground truths considered originate from automatic registration and segmentation approaches but it is not mentioned whether quality control was performed and so to which extent they can be relied on.
- The experiments regarding the downstream task are limited to qualitative results and the fact that the segmentations are not overlaid on the T1w image only allows assessing differences between the segmentation maps but not whether one matches better the anatomy than another one.



### Questions
- In Figure 2, what does the error correspond to exactly?
- Could the authors comment on the run time cost of their approach or other considerations regarding its practical application?

===
- The authors already mention many related works but they could also consider:
    - Chen J et al. "A survey on deep learning in medical image registration: New technologies, uncertainty, evaluation metrics, and beyond." arXiv preprint arXiv:2307.15615 (2023).
    - Zhang X et al. "Heteroscedastic Uncertainty Estimation Framework for Unsupervised Registration." International Conference on Medical Image Computing and Computer-Assisted Intervention. Cham: Springer Nature Switzerland, 2024.
And comment especially on the second one.

### Soundness
3

### Presentation
3

### Contribution
2
