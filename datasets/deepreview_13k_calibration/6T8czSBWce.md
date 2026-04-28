# High-dimension Prototype is a Better Incremental Object Detection Learner

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 3, 8, 8

## Abstract
Incremental object detection (IOD), surpassing simple classification, requires the simultaneous overcoming of catastrophic forgetting in both recognition and localization tasks, primarily due to the significantly higher feature space complexity. Integrating Knowledge Distillation (KD) would mitigate the occurrence of catastrophic forgetting. However, the challenge of knowledge shift caused by invisible previous task data hampers existing KD-based methods, leading to limited improvements in IOD performance. This paper aims to alleviate knowledge shift by enhancing the accuracy and granularity in describing complex high-dimensional feature spaces. To this end, we put forth a novel higher-dimension-prototype learning approach for KD-based IOD, enabling a more flexible, accurate, and fine-grained representation of feature distributions without the need to retain any previous task data. Existing prototype learning methods calculate feature centroids or statistical Gaussian distributions as prototypes, disregarding actual irregular distribution information or leading to inter-class feature overlap, which is not directly applicable to the more difficult task of IOD with complex feature space. To address the above issue, we propose a Gaussian Mixture Distribution-based Prototype (GMDP), which explicitly models the distribution relationships of different classes by directly measuring the likelihood of embedding from new and old models into class distribution prototypes in a higher dimension manner. Specifically, GMDP  dynamically adapts the component weights and corresponding means/variances of class distribution prototypes to represent both intra-class and inter-class variability more accurately. Progressing into a new task, GMDP constrains the distance between the distribution of new and previous task classes, minimizing overlap with existing classes and thus striking a balance between stability and adaptability. GMDP can be readily integrated into existing IOD methods to enhance performance further. Extensive experiments on the PASCAL VOC and MS-COCO show that our method consistently exceeds four baselines by a large margin and significantly outperforms other state-of-the-art results under various incremental settings. Source codes are included in supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper mainly focuses on the incremental object detection task. To effectively describe complex detection feature spaces, the authors propose to learn class prototypes based on Gaussian Mixture Distribution, which may better model the distribution relationships of different classes, thus facilitating the knowledge distillation procedure and incremental learning process. Furthermore, a dimension scaling progressive learning strategy and three additional loss functions are introduced to enhance the training stability and adaptability of the proposed prototype modeling method.

### Strengths
1. The motivation of this paper is clearly stated, and the proposed solution of modeling Gaussian Mixture Distribution based prototypes sounds reasonable.
2. The experiments under different settings are conducted and the ablation studies are comprehensive, which indicate the effectiveness of the proposed method and show the effects of introduced DSPL and DAPO strategies. 
3. The implementation details, including training/optimization details and hyper-parameter settings, are provided, which can increase the reproducibility of the proposed method.

### Weaknesses
1. The authors claim that their method learns higher-dimension prototypes. However, I cannot understand the definition of **"high-dimension"** here, does it mean that the representation of the ROI proposal feature vector $x$, where the prototypes are built on, is of high dimensionality? But as stated in the 306th-310th rows, the introduced dimension scaling progressive learning strategy transforms the original feature vector $x$ into a **lower dimensional** vector $z$, and calculates the prototypes based on $z$. This operation seems to conflict with the concept of **"high-dimension"**, could the authors make more discussions about this? Specifically, the paper should clarify whether the 'high-dimension' refers to the original feature space before dimensionality reduction, or if it refers to the number of mixture components within the Gaussian Mixture Model, which is not a dimension in the typical sense of feature vectors. The current description lacks clarity on this crucial point, potentially misleading readers about the actual feature space manipulation.

2. In Eq. (3), the details of how to assign the ground-truth label $y_{i,c}$ for each proposal feature vector should be clarified, can we find the details of such label assignment operation in previous works? The paper needs to explicitly state the criteria used to determine the ground-truth class label for each proposal. Is it based on Intersection over Union (IoU) with ground truth bounding boxes, or some other metric? A clear explanation of this assignment process is essential for reproducibility and understanding the training procedure. Furthermore, if this assignment process relies on a specific threshold or strategy, it should be explicitly mentioned and justified.

3. From Table 5, it can be seen that the performance of the proposed method is quite sensitive to the number of Gaussian mixture components, which may increase the difficulty of tuning this hyper-parameter for different application scenarios. The paper should provide a more detailed analysis on the impact of the number of Gaussian components on the final performance. It is not sufficient to simply show that performance varies; the authors should discuss why this sensitivity exists and how one might choose an appropriate number of components for a given dataset. Are there any guidelines or heuristics that can be used to determine the optimal number of components, or does it require extensive hyperparameter tuning for each new application?

4. In Section 3.2, there are some notations are confused. For example:
     1) In the 268th row, both the dimensionality of proposal feature $x_i$ and the size of input feature set are denoted as $N$.
     2) In the 276th to 277th rows, the component number of Gaussian mixture distribution is denoted as $K$, but it is also indicated by $M$ in Eq. (9) and (10).
     3) The notations of the proposal feature vector $x_i$ are bold in Eq. (4) and Eq. (7), but not in Eq. (2), (3) and (5). They should be consistent. These inconsistencies in notation make it difficult to follow the mathematical formulation and the overall method. The authors should carefully review the notation and ensure that each symbol is used consistently throughout the paper, and that each symbol is clearly defined when it is first introduced.

### Questions
1. For the confusion matrix in Figure 4, I am confused about the values calculated for the proposed GMDP method. Since the class prototypes of GMDP are Gaussian mixture distributions, I am not sure how to calculate the Jensen-Shannon (JS) divergence between them. Based on my knowledge, it can only get an upper bound value of this metric for a pair of Gaussian mixture distributions, so could the authors provide more details about such calculation process?

2. In the appendix A.2, I have noticed that the proposed method can also be integrated into a CL-DETR detector. Since this query-based method does not generate the proposal feature vectors, I am not very clear on how to produce the Gaussian Mixture Distribution prototypes for it. Could the authors provide more details for such integrating process?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new higher-dimension-prototype learning approach for knowledge distillation-based incremental object detection, which uses Gaussian mixture distributions to model the feature distributions of classes more effectively. This approach helps address the issue of knowledge shift caused by the introduction of new classes without access to previous task data. Dynamic Adaptive Prototype Optimization strategy improves the separation of class features and enhances the plasticity of class prototypes. Comprehensive experimental results support the efficacy of the proposed method.

### Strengths
1. This paper leverages the flexibility and expressiveness of Gaussian mixtures to capture the complex distributions of object features in high-dimensional spaces, alleviating the knowledge shift caused by the lack of previous data.

2. The proposed Dynamic Adaptive Prototype Optimization (DAPO) strategy is a well-reasoned enhancement that improves the plasticity and stability of class prototypes. By optimizing the separation and cohesion of class features, the strategy provides a robust mechanism for managing the intricacies of incremental learning.

3. The paper is well-organized and clearly written, which facilitates readers' understanding of the proposed approach.

4. The method is validated through extensive experiments, demonstrating consistent superiority over existing state-of-the-art methods.

### Weaknesses
1. Gaussian Mixture Distribution-based prototypes have been previously explored in class incremental learning[1-4]. Specifically, [1] highlights that embedding distributions in feature space are not convex or isotropic in practice. Thus, the author’s emphasis on the complexity of detection features compared to classification features may not provide substantial new insights. The innovation level is thus moderate.

2. This method is not specifically tailored for incremental object detection (IOD) tasks, which appears more suited for general class-incremental learning for modeling class distributions.

3. The integration of GMDP and DAPO at the base stage of the model may inherently enhance the detector’s feature representation capacity. Given that the upper bound of Faster R-CNN has been exceeded in certain settings (e.g., the 19-1 setting), the comparisons with existing methods may be skewed. They are not designed for incremental scenarios.

[1] Steering Prototypes With Prompt-Tuning for Rehearsal-Free Continual Learning.

[2] Contrastive Learning of Multivariate Gaussian Distributions of Incremental Classes for Continual Learning.

[3] Class-Incremental Mixture of Gaussians for Deep Continual Learning.

[4] Saving 100x Storage: Prototype Replay for Reconstructing Training Sample Distribution in Class-Incremental Semantic Segmentation.

### Questions
Please address my concerns in the 'Weakness' section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper focuses on incremental object detection (IOD) and aims to address knowledge shift using enhanced high-dimensional prototype learning. Specifically, the authors propose a Gaussian Mixture Distribution-based Prototype (GMDP) to model the complex feature distribution based on both new and old models. To facilitate GMDP modeling, they further introduce a Dynamic Adaptive Prototype Optimization Strategy (DAPO). The proposed method can be readily integrated into existing IOD approaches, consistently improving their results.

### Strengths
1. The investigation into why accurate modeling of the complex distribution for IOD is necessary and compelling.
2. The experiments are convincing and comprehensive.
3. The paper is easy to follow, and the visualizations are helpful, making it easy for readers to grasp the main idea.

### Weaknesses
1. Lack of discussion regarding method complexity and training time.
2. As the core contribution involves adopting Gaussian Mixture Distribution, it would be beneficial to conduct ablation studies on the number of components in both two-stage and multiple-stage incremental settings. 
3. Minor: some of the best results are not boldfaced in Table 4.

### Questions
1. Do all classes share the same number of components in GMDP? Are there insights into how to determine the number of components for different classes? Intuitively, a unimodal Gaussian distribution may be sufficient for easily distinguished classes, while a multiple-component Gaussian distribution is more suitable for harder classes.
2. What are the weights of the losses in the DAPO? How are these values determined across different settings?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a higher-dimension prototype learning method that incorporates GMDP to address issues such as knowledge shift present in KD-based IOD methods. Additionally, a DAPO strategy is designed to enhance the adaptability and effectiveness of GMDP modeling. The authors conducted experiments on PASCAL VOC and MS-COCO, demonstrating the validity of the proposed method.

### Strengths
1. This paper proposes a novel approach by introducing a Gaussian Mixture Distribution-based Prototype(GMDP) to alleviate the knowledge shift.
2. GMDP can be readily integrated into existing IOD methods for better performance.
3. Experiments show that this method achieves SOTA results on PASCAL VOC and MS COCO.
4. The motivation is clearly articulated, and it includes figures that illustrate the issues with current IOD methods as well as the differences in feature spaces for classification and detection tasks.

### Weaknesses
1. The quality and clarity of the figures need further improvement. The legend for Figure 1 is inconsistent, and Figure 3 is blurry and has a low resolution.
2. Some descriptions need to be more precise and clear. For example, in line 303, "the old class C_o" should refer to a "class set". The variable z in Equation (6) has not been introduced; it should refer to proposals generated from the ROI layer. Additionally, how are the means and variances of the K components of GMD calculated? Are they based on the features x? For incremental learning tasks, is the computation of these means and variances confirmed before or after training?
3. As mentioned in line 515, "this poses significant challenges to the network’s fitting capability.", it lacks an experiment on the selection of the number of Gaussian componenets for larger models.

### Questions
Some descriptions need to be more precise and clear. For example, in line 303, "the old class C_o" should refer to a "class set". The variable z in Equation (6) has not been introduced; it should refer to proposals generated from the ROI layer. Additionally, how are the means and variances of the K components of GMD calculated? Are they based on the features x? Is the computation of these means and variances confirmed before or after training for incremental learning tasks?

### Soundness
3

### Presentation
1

### Contribution
3
