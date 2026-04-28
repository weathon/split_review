# A Contrastive Teacher-Student Framework for Novelty Detection under Style Shifts

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 8, 6, 3

## Abstract
There have been several efforts to improve Novelty Detection (ND) performance. However, ND methods often suffer significant performance drops under minor distribution shifts caused by changes in the environment, known as style shifts. This challenge arises from the ND setup, where the absence of out-of-distribution (OOD) samples during training causes the detector to be biased toward the dominant style features in the in-distribution (ID) data. As a result, the model mistakenly learns to correlate style with core features, using this shortcut for detection. Robust ND is crucial for real-world applications like autonomous driving and medical imaging, where test samples may have different styles than the training data. Motivated by this, we propose a robust ND method that crafts an auxiliary OOD set with style features similar to the ID set but with different core features. Then, a task-based knowledge distillation strategy is utilized to distinguish core features from style features and help our model rely on core features for discriminating crafted OOD and ID sets. We verified the effectiveness of our method through extensive experimental evaluations on several datasets, including synthetic and real-world benchmarks, against nine different ND methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a contrastive teacher-student framework for novelty detection (ND) that improves robustness under style shifts. By generating OOD samples through core feature interventions while preserving style, the method aims to reduce spurious correlations and enhance detection accuracy. Experimental results show significant AUROC improvements, though the focus on style shifts may limit generalizability to other types of distribution changes.

### Strengths
+  Innovative Approach to OOD Generation: The paper proposes a novel method for generating out-of-distribution (OOD) samples by intervening in core features of in-distribution (ID) samples. This method leverages saliency maps to identify core regions, making it uniquely capable of creating OOD samples that retain style features but diverge in core attributes.
+ Comprehensive Experimental Results: The paper demonstrates the proposed method's effectiveness across multiple datasets and settings, including autonomous driving and medical imaging, which reinforces the practical applicability of the method in real-world scenarios.

### Weaknesses
 + Potential Bias in Robustness Evaluation: The experimental setup for robustness focuses heavily on distribution shifts primarily related to style changes. Since the OOD generation method itself targets this specific type of shift, the evaluation may unfairly favor the proposed method over other ND approaches, which were not designed with style changes as the main concern. This narrow focus on style-based OOD shifts limits the generalizability of the results and may not reflect the performance of the proposed method in more varied OOD scenarios (e.g., class or content-based distribution shifts).


### Questions
+ How might the proposed approach perform in scenarios where OOD samples differ from ID samples based on content or class shifts rather than style changes?
+ Have the authors considered conducting additional evaluations using datasets with OOD shifts that are unrelated to style, to better understand the generalizability of the proposed method ？

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Using knowledge distillation models for anomaly detection, the model tends to learn features related to style, leading to poor performance in cases of style transfer. Therefore, by applying style variations to obtain augmented samples while retaining labels, a more robust representation can be achieved. At the same time, by identifying and distorting the core areas of ID samples through a feature attribution method for data augmentation, unnecessary correlations between style features and labels can be weakened. Minor improvements have been made to the knowledge distillation model part, updating the weights of the binary layer to enhance the teacher's knowledge.

### Strengths
1.The ablation study is very comprehensive, and the experimental results and datasets are also abundant.
2.The paper is well-written and organized, with an easy-to-understand approach and a clear presentation of the method.There are various experimental details and pseudocode implementations.

### Weaknesses
1.There are no more intuitive experiments to demonstrate that the unwanted correlation between style features and labels has been weakened.
2.The OOD generation strategy heavily borrows from methods in self-supervised learning that preserve and do not preserve semantics, and moreover, there are not many improvements to the knowledge distillation model, which makes the innovation somewhat lacking.Improve the knowledge transfer mechanism in the distillation process, or develop new technologies to more effectively extract knowledge from the teacher model.

### Questions
1.If the hyperparameters the parameter alpha have little impact on the experiment, why are they still retained?
2.The proof of the theorem 1 does not seem to effectively demonstrate the effectiveness of the improvement through generating ODD (Out-of-Distribution) samples.

### Soundness
3

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
The paper introduces a novel approach for novelty detection under style shift by creating manual OOD training samples from content distortion. The method uses a saliency detector to distinguish the content part from the style part in the input image, then applies strong augmentations to distort the content in the original image to generate OOD samples. A knowledge distillation network is utilized, where the teacher network consists of a frozen encoder and a binary classification head, and the student network is a fully trainable model. The student network is trained with a contrastive objective, aiming to bring closer the ID features of the student-teacher networks and to push away the OOD features. Experiments have been conducted to demonstrate the effectiveness of the proposed approach.

### Strengths
1. The paper is clearly presented, with a good logical flow and well-designed figures.
2. The experiments show a visible improvement in novelty detection under style shift.
3. The paper provides theoretical analysis from a causal perspective.

### Weaknesses
1. The generated OOD samples might still contain content (core feature) information about ID samples. From the visualized illustrations, it appears that most core features are preserved even after distortion. I am concerned that treating them as negative samples in a contrastive objective might impact the performance of the ND model. Specifically, the distortions applied, while altering the appearance, often seem to maintain the overall shape and structure of the core content. For example, if the core feature is a specific object shape, the distorted version often retains a similar shape, even if the texture or internal details are modified. This could lead the model to learn that these distorted versions are still within the distribution of the ID data, hindering its ability to effectively detect true novelties.
2. In the student-teacher framework, features from different layers within the pre-trained ResNet networks are extracted for contrastive learning. It has been shown that different layers are associated with processing different levels of features; for example, early layers focus on textures and edges, middle layers focus on local patterns, and deep layers capture high-level semantic features. Within this framework, the ideal generated OOD samples should only differ in semantic features while retaining the same local patterns and other style-associated features. Therefore, I believe the framework’s design is not sufficiently justified from a conceptual perspective. The use of features from early layers, which are sensitive to low-level details, might introduce noise or irrelevant information into the contrastive learning process, as these layers are not primarily capturing the high-level semantic differences that should distinguish OOD samples. This could lead to a less effective separation of ID and OOD feature spaces.

### Questions
See Weaknesses Above.

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
The manuscript proposes a method that addresses the issue of style variations in novelty detection by creating auxiliary OOD sets combined with a task-oriented knowledge distillation strategy. This approach enhances the model's robustness by generating OOD samples through the identification and distortion of core features. However, the method not only requires the use of saliency methods to identify key objects in images but also necessitates the application of hard transformations to regions with high saliency values. This adds significant detection costs and poses challenges for direct application in certain segmentation tasks, which may limit the method's practical usability in real-world scenarios. Additionally, while task-based knowledge distillation strategies have already been applied in some OOD detection tasks, the innovation of the proposed method is somewhat limited. The core idea remains focused on mitigating the impact of different styles on OOD detection. However, in real-world applications, variations in style as well as changes between ID and OOD categories can lead to significant fluctuations in performance. It is crucial for the model to accurately identify OOD categories not only under a single style but also across various style scenarios, such as sunny and rainy conditions. This broader applicability holds substantial research value.

### Strengths
The manuscript proposes a novel novelty detection method that combines data augmentation with a knowledge distillation strategy. By integrating a saliency detection task, the method effectively improves detection accuracy and validates its effectiveness across various datasets, particularly in some medical imaging datasets, which adds significant research value. The overall experimental results are comprehensive, and the method description is relatively clear.

### Weaknesses
1.	The method relies on saliency detection to identify key objects in the image and applies hard transformations to regions with high saliency values. This may lead to significant computational and time costs. In practical applications, such costs could limit its widespread use, especially in detection and segmentation tasks where multiple OOD key objects are present in the scene, making direct application impractical.
2.	Style Variation in Real-World Scenarios: The core idea of the paper is to mitigate the impact of different styles on OOD detection. However, style variations in real-world scenarios are complex, and changes between ID and OOD can significantly affect model performance. The research value of the model lies in its ability to accurately identify OOD categories across various stylistic contexts, such as sunny and rainy conditions.
3.	Currently, task-based knowledge distillation strategies have been applied in several OOD detection tasks. The method does not clearly demonstrate how it differs from other approaches that utilize knowledge distillation. The manuscript may need to further elaborate on the innovative aspects of this approach.

### Questions
1. The manuscript needs to further clarify the detection costs associated with creating auxiliary OOD sets and the limitations it poses for downstream OOD detection and segmentation tasks.
2. The manuscript needs to further articulate the necessity and innovation of the proposed task-oriented knowledge distillation in comparison to other knowledge-based methods for novelty detection.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper focuses on the problem of novelty detection under style shifts. And this paper proposes a ND method that crafts an auxiliary OOD set with style features similar to the ID set but with different core features. Then, a task-based knowledge distillation strategy is utilized to distinguish core features from style features. In essence, the performance of the proposed method mainly rely on the quality of the generated data. And this paper only utilizes some commonly-used operations and does not propose any inspired ideas.

### Strengths
Novelty detection under style shifts is an important problem. Employing data augmentation is a reasonable solution.

### Weaknesses
1. The motivation of this paper is not clear. This paper aims to address novelty detection under style shifts, which involves two shift problems, i.e., covariate shift and semantic shift. However, this paper does not sufficiently analyze why existing methods could not solve these two shifts simultaneously. To the best of my knowledge, there exist some methods that aim to leverage large-scale models, e.g., CLIP, to solve this challenge. The authors should introduce these methods and make an analysis.

2. In Introduction Section, it is better to show a figure to analyze the corresponding problems of existing methods. Besides, I am not clear why the proposed method could solve these two shift problems. The authors should give more interpretations.

3. The proposed method involves data generation and other multiple operations, e.g., contrastive learning. In essence, these operations are commonly used methods and this paper does not propose any inspired ideas, which lacks novelty.

4. In the experiments, the authors should compare more state-of-the-art methods. The testing datasets are somewhat small. The authors should verify their method on more dataset. Besides, the authors should give some feature-level visualization analysis, which is better to understand the proposed method.

### Questions
See the weakness.

### Soundness
2

### Presentation
2

### Contribution
1
