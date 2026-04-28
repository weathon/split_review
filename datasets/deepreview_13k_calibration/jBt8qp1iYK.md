# SCoRe: Submodular Combinatorial Representation Learning for Real-World Class-Imbalanced Settings

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Representation Learning in real-world class-imbalanced settings has emerged as a challenging task in the evolution of deep learning. 
Lack of diversity in visual and structural features for rare classes restricts modern neural networks to learn discriminative feature clusters.
This manifests in the form of large inter-class bias between rare object classes and elevated intra-class variance among abundant classes in the dataset. Although deep metric learning approaches have shown promise in this domain, significant improvements need to be made to overcome the challenges associated with class-imbalance in mission critical tasks like autonomous navigation and medical diagnostics. Set-based combinatorial functions like Submodular Information Measures exhibit properties that allow them to simultaneously model diversity and cooperation among feature clusters. In this paper, we introduce the SCoRe (Submodular Combinatorial Representation Learning) framework and propose a family of Submodular Combinatorial Loss functions to overcome these pitfalls in contrastive learning. We also show that existing contrastive learning approaches are either submodular or can be re-formulated to create their submodular counterparts. We conduct experiments on the newly introduced family of combinatorial objectives on two image classification benchmarks - pathologically imbalanced CIFAR-10, subsets of MedMNIST and a real-world road object detection benchmark - India Driving Dataset (IDD). Our experiments clearly show that the newly introduced objectives like Facility Location, Graph-Cut and Log Determinant outperform state-of-the-art metric learners by up to 7.6% for the imbalanced classification tasks and up to 19.4% for object detection tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses class imbalance problem in real world for representation learning tasks.
For this purpose, a SCoRe framework and a family of Submodular Combinatorial objectives are proposed to overcome lack of diversity in visual and structural features for rare classes.
Performance evaluation is conducted on two image classification benchmarks (pathologically imbalanced CIFAR-10, subsets of MedMNIST) and a real-world road object detection benchmark (India Driving Dataset ). The newly introduced objectives like Facility Location, Graph-Cut 
and Log Determinant can boost the large performance when compared with state-of-the-art metric learners.

### Strengths
+ The class-imbalance is a challenging problem, and the illustration of motivation is clear. The effect of class-imbalance on the performance metrics (mAP50) is shown for the object detection task of the IDD.
+ It seems novel by studying metric learners from an assemblage perspective, treating class-specific feature vectors as sets. 
+ There are some useful conclusions, e.g., the submodule combinatorial objective can construct more distinguishable clustering features for representation learning. At the same time, the derivation proves that the existing contrastive learning objectives are either submodular or can be reformulated as submodular functions.
+ Three novel objective functions: Facility-Location (FL), Graph-Cut (GC), and Log Determinant (LogDet).
+ Sufficient experiments on datasets with different degrees of class imbalance for different tasks (image classification and image detection), compared to SoTA metric/contrast learners, indicate the importance of combinatorial loss functions.

### Weaknesses
 - This paper shows comparative analysis related to metric learning and contrastive learning, without focusing on class imbalance issues. Missing some latest methods in Related Work.
- As far as I know, there are various methods available to address class imbalance or long-tail problems, such as focal loss, WPLoss, OHEM, data augmentation... What are the differences between SCoRe and these methods? And there are no comparative experiments with these methods.
- The formulas/symbols in the paper are unclear and lack more explanation.
For instance, 'f' is used to denote both the feature extractor and the submodular function; 'S' is utilized to represent both similarity kernels and total submodular information.
- There are minor writing errors, particularly related to subscript issues, concentrated in Section 3.1. For example, Sij(\theta) , yii=1,2,...|T |.

### Questions
- The class imbalance issue may be more pronounced in some other object detection datasets such as the MS COCO[1] or the LVIS[2] which is dedicated to long-tailed object detection. We are looking forward to see some results on them.
- How does SCoRe solve the localization/regression problem in object detection tasks under the class-imbalanced settings?
- Can you provide a detailed explanation of equation (1), as well as the distinction between Total Submodular Information and Total Submodular Correlation?
- Can you provide a visualization of the class distribution in the CIFAR-10 dataset or other dataset?
- Will codes be released in the future?
 [1] Microsoft COCO: Common Objects in Context. ECCV, 2014. [2] LVIS: A Dataset for Large Vocabulary Instance Segmentation. CVPR, 2019.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on improving the way deep learning models handle imbalanced class scenarios in real-world applications. In such situations, where some classes are rare, conventional neural networks struggle to learn useful features. This leads to a significant imbalance between rare and abundant classes in the data. To address this, the paper introduces the SCoRe framework, which utilizes Submodular Combinatorial Loss functions. These functions can effectively model feature diversity and cooperation among classes. Experimental results on image classification tasks, including imbalanced datasets like CIFAR-10 and object detection tasks, show that the proposed approach outperforms existing metric learning methods.

### Strengths
- The paper introduces a new approach to tackle the challenge of class-imbalanced data in deep learning, which is a critical problem in real-world applications.  

- This paper is generally easy to follow.

### Weaknesses
 - Unclear Link Between Diversity and Robust Representations: While the paper's motivation to employ submodular functions as loss functions to promote diversity is evident, the direct connection between diversity and the creation of robust representations from imbalanced datasets remains somewhat ambiguous. The paper does not clearly elucidate how fostering diversity contributes to the development of robust representations in such scenarios. Specifically, it is unclear how maximizing feature diversity within a class directly translates to improved generalization for rare classes, as opposed to simply learning more varied features that might not be discriminative. The paper should provide a more detailed explanation of the theoretical underpinnings of this connection.

- Limited Experimental Evidence: The experimental results exhibit certain weaknesses:
a) The paper compares its approach with well-known metric learning methods but does not utilize popular metric learning datasets, which could potentially limit the generalizability of the findings. The choice of datasets used for comparison is not standard for metric learning research, making it difficult to assess the true performance of the proposed method against state-of-the-art techniques. A comparison with standard metric learning datasets would strengthen the experimental validation.
b) All experiments are conducted on relatively small datasets, as opposed to widely recognized datasets commonly used in imbalanced classification, such as ImageNet-LT. This choice of datasets might limit the broader applicability and relevance of the research. The use of smaller datasets makes it difficult to ascertain the scalability and effectiveness of the proposed method on larger, more complex datasets with more severe class imbalances.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a family of submodular combinatorial objectives for representation learning tasks through the submodular combinatorial representation learning framework to overcome class imbalance in real-world vision tasks. The authors conduct experiments on two benchmark datasets to show the effectiveness of the proposed approach.

### Strengths
1. This paper is well-written and easy to read.
2. The performance seems good compared with other approaches.

### Weaknesses
1. The novelty is unclear. The method part only lists some existing metric learning losses.
2. The proposed framework is called the Submodular Combinatorial Representation learning framework. What does Combinatorial mean? It is unclear what the framework looks like since there are only some metric learning loss functions in the method part.
3. The authors do not compare with the recent state-of-the-art method since the latest method in Table 2 is in 2020.

### Questions
see the weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
