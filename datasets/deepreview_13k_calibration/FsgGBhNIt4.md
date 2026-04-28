# Unsupervised Learning of Facial Attribute Representations Using StyleGAN

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Facial attributes (e.g., gender, age) encompass important social cues and play a pivotal role in computer vision. While supervised methods have dominated facial attribute analysis, they often require large annotated datasets, which are costly and time-consuming to create.
In this work, we circumvent this limitation by proposing a novel unsupervised learning framework that leverages StyleGAN to learn rich and disentangled facial attribute representations. Specifically, unlike prior methods that rely on labeled datasets or supervised techniques, our approach exploits the unique inductive bias of StyleGAN, namely Hierarchical Feature Modulation, to automatically discover semantically meaningful representations of facial attributes. This inductive bias enables StyleGAN to generate disentangled and interpretable facial attribute features at different layers, benefiting a variety of downstream tasks. To leverage StyleGAN representations, we employ GAN inversion methods to represent input images as StyleGAN features and propose a simple yet effective feature reduction method based on mutual information to improve the effectiveness and efficiency of the learned representations. Extensive experiments in few-shot facial attribute analysis tasks, including clustering, classification, and facial attribute annotation demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes to employ an unsupervised approach for facial attribute analysis, eliminating reliance on large labeled datasets. It illustrates that StyleGAN has a superior inductive bias, enabling the extraction of disentangled and interpretable facial attribute features at different layers. And A mutual information-based feature refinement method is proposed to enhance the effectiveness of these features in downstream unsupervised tasks.

### Strengths
1. This paper introduces the unsupervised approach to facial attribute analysis, reducing dependence on labeled data by fully exploring StyleGAN's feature extraction capabilities. It also introduces a novel mutual information-based feature refinement method, enhancing representation quality for unsupervised tasks.
2. The authors provide experiments across four classification tasks in three scenarios to demonstrate the framework's effectiveness.

### Weaknesses
1. Necessity of unsupervised facial attribute classification task

The primary contribution of the paper is its unsupervised approach to facial attribute classification, yet the necessity of this task not sufficiently justified:

a) Data Requirements for Supervised Classification: For relatively straightforward binary and ternary classification tasks (e.g., gender, presence of glasses, or age group), it is unclear if large amounts of labeled data are indeed required to achieve satisfactory results in a supervised setting. To establish the necessity of an unsupervised approach, the authors should provide experiments quantifying the data requirements for supervised classifiers on these tasks. For example, showing performance levels and data demands for a standard supervised classifier, such as a ResNet-18, across varying amounts of labeled data could substantiate the need for an unsupervised approach. Specifically, the performance of a supervised classifier trained with 10, 50, 100, and 500 labeled examples per class should be compared against the proposed unsupervised method.

b) Definition and Challenge of the Facial Attribute Analysis Task: The paper's definition of facial attribute analysis is somewhat ambiguous, as it appears to center only on simple binary and ternary classification tasks. Additionally, in the related work section, the cited literature does not treat facial attribute analysis as a primary task, often addressing it as an auxiliary component. Moreover, the specific attributes addressed here do not closely align with those in the cited works. Therefore, the authors should clarify the precise scope and significance of this task and its challenges in a way that more directly addresses the novelty of this contribution. Alternatively, citing literature that better aligns with the defined problem scope would strengthen the paper.


2. Insufficient explanation and experimentation on StyleGAN feature superiority
While the paper claims that StyleGAN features provide superior performance, further clarification and experimentation are needed to substantiate this claim:

a) Performance in Few-Shot Classification with True Labels: In the unsupervised few-shot classification setting presented in Table 3, when labels are set as TrueLabel, the MAE model achieves better results than StyleGAN (SG2) on certain tasks. The authors should explain why MAE outperforms SG2 here and clarify the contexts or conditions in which StyleGAN features are expected to excel over alternative approaches like MAE. This should include a discussion of the feature space dimensionality and the inherent inductive biases of both models, and how these impact performance in supervised vs. unsupervised settings.

b) Feature Reduction Method Justification: When discussing the feature reduction approach, the experiments only compare max pooling with mean pooling, without establishing the necessity of the reduction operation itself. To substantiate the proposed feature reduction, the authors should provide experiments demonstrating the effectiveness of reduction as a whole, perhaps by comparing results with and without reduction to highlight its impact on the performance. This could be done by comparing the clustering performance with and without the channel selection step, using metrics such as the Adjusted Rand Index (ARI) or Normalized Mutual Information (NMI).

c) Generalization Claims of StyleGAN Features: The generalization capability of StyleGAN features is tested using the AFHQ-Wild dataset. However, since StyleGAN was pre-trained on this dataset, while MAE and VGG were not, this setup does not offer a fair assessment of StyleGAN’s generalization capabilities. To strengthen this claim, additional experiments should be conducted on datasets not used in StyleGAN's pre-training, thereby providing a more unbiased comparison of generalization between these models. For example, evaluating performance on a dataset like CelebA, which is distinct from the training data of StyleGAN, would provide a more robust assessment.

### Questions
1. Necessity, Definition, and Challenges of the Task

Please provide experiments or analyses showing data requirements for simple supervised classification tasks (e.g., gender, age group) to demonstrate the necessity of an unsupervised approach. Clarifying the specific scope and unique challenges of facial attribute analysis would also help establish its importance and relevance in this work.

2. Clarifications and Experiments on StyleGAN Feature Superiority

Could you clarify why MAE outperforms SG2 in the few-shot classification with True Labels? Additionally, please provide justification for the feature reduction step itself (beyond comparing max and mean pooling) and consider testing StyleGAN’s generalization on datasets it hasn’t been pre-trained on to offer a more balanced view.

### Soundness
2

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
This paper aims to learn disentangled and distinguishable features in an unsupervised manner. It employs the inductive bias of StyleGAN to automatically discover semantically meaningful representations of facial attributes

### Strengths
Using self-supervised learning to enhance facial feature representation is a reasonable and common approach.

### Weaknesses
1.	This article claims that the MAEs-based methods still use a large amount of labeled data. This assertion is questionable. To my knowledge, methods based on MAE can significantly reduce the training data requirements for downstream tasks after pre-training on a large amount of unlabeled data.
2.	The experimental comparison in Fig. 2 is unfair. VGG16 is pre-trained on ImageNet dataset. Comparing to the other model pre-trained on face images, VGG16 naturally performs less well in disentangle the glasses feature. The authors should also pre-train VGG16 on the same FFHQ dataset.
3.	It's strange that this method selects feature channels based solely on 8 images. The paper lacks experimental results to demonstrate that using just 8 images is sufficient to select the appropriate channels.
4.	To my knowledge, this article introduces two uncommon few-shot tasks: clustering and annotation. However, the article does not provide detailed explanations for these tasks nor demonstrate their academic value. Furthermore, this article also lacks comparisons with other state-of-the-art methods on these tasks.
5.	In line 260 and line 261, the sentence “ clustering, annotation, and clustering” is a typo.

### Questions
Please address my concerns on the insufficient experiments.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study presents an unsupervised learning framework for facial attribute analysis that overcomes the need for extensive annotated datasets. Utilizing StyleGAN, the framework learns rich and disentangled representations of facial attributes without labeled data. The approach capitalizes on StyleGAN's Hierarchical Feature Modulation to automatically identify semantically meaningful features across different layers. To enhance the use of these representations, GAN inversion techniques are employed to convert input images into StyleGAN features, complemented by a feature reduction method based on mutual information. Experiments in few-shot facial attribute analysis, including clustering, classification, and annotation tasks, demonstrate the effectiveness of this framework.

### Strengths
The research point is interesting, learning facial attribute representation from an unsupervised perspective.

### Weaknesses
1. The novelty of the paper appears limited. The proposed method appears to rely primarily on StyleGAN's feature decoupling capability and does not offer substantial insights.
2. The description of the method is overly brief and difficult to comprehend. The core of the proposed approach is quantitative justification, lacking sufficient explanation of the purpose of the strategy and the definitions of key indicators (IntraMI/InterMI).
3. The main issue with the experimental section is the lack of comparative methods. In fact, there are numerous studies focused on face representation learning that could provide valuable context.
4. Some references focusing on learning facial representations are missing:
[1] General Facial Representation Learning in a Visual-Linguistic Manner
[2] FaceXFormer: A Unified Transformer for Facial Analysis

### Questions
Please refer to the Strengths and Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
