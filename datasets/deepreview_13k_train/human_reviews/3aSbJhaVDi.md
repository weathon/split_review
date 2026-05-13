# Exploiting Open-World Data for Adaptive Continual Learning

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Continual learning (CL), which involves learning from sequential tasks without forgetting, is mainly explored in supervised learning settings where all data are labeled. However, high-quality labeled data may not be readily available at a large scale due to high labeling costs, making the application of existing CL methods in real-world scenarios challenging. In this paper, we delve into a more practical facet of CL: open-world continual learning, where the training data comes from the open-world dataset and is partially labeled and non-i.i.d. Building on the insight that task shifts in continual learning can be viewed as transitions from in-distribution (ID) data to out-of-distribution (OOD) data, we propose OpenACL, a method that explicitly leverages unlabeled OOD data to enhance continual learning.  Specifically, OpenACL considers novel classes within OOD data as potential classes for upcoming tasks and mines the underlying pattern in unlabeled open-world data to empower the model's adaptability to upcoming tasks. Furthermore, learning from extensive unlabeled data also helps to tackle the issue of catastrophic forgetting. Extensive experiments validate the effectiveness of OpenACL and show the benefit of learning from open-world data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes openACL, the open-world continual learning. The author consider the situation that the training data in one task may come from the open-world dataset (OOD), and considers such OOD data (from novel classes) to mine the underlying pattern in unlabeled open-world data. So that the model’s adaptability to upcoming tasks will be  empowered. At last, the author organizes extensive experiments validate the effectiveness of OpenACL and show the benefit of learning from open-world data.

### Strengths
1. The idea of establish novel prototype from OOD under the semi-supervised pattern is new, it involved the discovery of novel class and also utilize the provided labeled data for seen classes;

2. The experimental setting and result seems well, the result with ablation study, relative discussion make the conclusion reasonable

### Weaknesses
1. The recognition of the OOD/novel class when constructing the novel prototype is not clear, which make the learning process a little confuse. The author mention "the novel prototypes are used to cluster representations from novel classes", but under the setting from this paper, that OOD/Novel class may existing with labeled classes data in same task, the author applied the self-supervised learning at first to cluster each class (include OOD) [1], or recognize the novel class after see the labeled classes data [2]? It is unclear how the method differentiates between novel classes and labeled classes during the initial clustering phase, especially since both are present simultaneously within a task. The paper needs to clarify whether the self-supervised learning is applied to all data indiscriminately, or if there is a mechanism to pre-identify or separate the OOD data before clustering.

2. During the prototype-adaptation, the author remain the existing prototypes as static and not subjected to updates post clustering. Here when the model parameters updated and previous prototype may also drift [3], how should the author solve this issue? The lack of updates to existing prototypes after the initial clustering raises concerns about the method's robustness to model drift. As the model parameters are updated during training, the feature space can shift, potentially rendering the original prototypes less representative of their respective classes. This could lead to misclassification and reduced performance over time. It is crucial to address how the method maintains the relevance of these prototypes in the face of changing feature representations.

3. The idea of applying prototype for incremental learning with open-set recognition is not novelty, especially using the contrastive learning, like [1,2,4], the author should make further discussion and comparison with recent works.

### Questions
Please see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the Open SSCL problem, which aims to leverage unlabeled out-of-distribution (OOD) data to assist continual learning, because these data may become in-distribution (ID) at a future task. To tackle this problem, an algorithm, namely Open ACL is discussed. Specifically, Open ACL consists of three steps. First, the cosine distances between data in seen classes and their prototypes are minimized, to improve the perceived similarity on data points in the same seen class. Second, dissimilarity among data in different classes is improved by contrastive learning. Third, novel prototypes are adapted from centroids of K-means. Experiments show that Open ACL is able to defeat baselines in standard image classification SSCL benchmarks.

### Strengths
1. This paper has precisely identified the problem of data shortage in open world continual learning, and proposes to improve learning with additional OOD data. It bridges a gap in state-of-the-art class-incremental continual learning, where OOD data are generally excluded and only ID data is used.
2. The proposed method, Open ACL aims to group data points in the same class with similar representations, while separating data points in different classes with dissimilar ones. This technique is able to handle OOD data from unseen classes, preparing knowledge for encountering them in future.
3. The presentation is easy to follow.

### Weaknesses
The experiment design seems to be inconsistent with the method. How are unlabeled OOD data being input per task? I assume that for each task, the model will receive some ID data from its current classes, and some OOD data from future classes. However, it seems that all training data points, including labeled and unlabeled, are ID.

### Questions
Please respond to the weakness I mentioned above. If this can be clearly addressed, I am willing to improve my rating.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is concerned with open-world continual learning. The proposed approach (called OpenACL) is based on the assumption that the novel classes in the out-of-distribution (OOD) data for the current task may become training data in future tasks. Instead of identifying and rejecting OOD samples, the authors use them to adapt a model to a new task and improve the model performance in CL. The proposed approach maintains multiple prototypes for seen tasks and reserves extra prototypes for unseen tasks. Both labeled and unlabeled
data are learned to improve the adaptation ability and tackle catastrophic forgetting for prototypes.

### Strengths
The paper is, in general, clearly written, well-documented and easy to follow. The review of the state of the art covers almost the relevant literature. The experimental results are extensive and demonstrate the superiority of the proposed approach.

### Weaknesses
There is a confusion of the concepts and terminology being used (see the Questions section)

The authors need to clarify the following aspects:
- They claim (first paragraph, page 2, middle): "Instead of identifying and eliminating OOD samples during training, we may leverage...". The problem of OOD detection is addressed at inference time, not during training. You could simply refer as: unlabeled training data or semi-supervised learning. Please correct this aspect through the paper and clarify which problem you want to address.
- Since you want to identify and label unknown samples, your problem is related to Novel Class Discovery problem, not OOD detection.
See for instance references [1, 2] (below). Please discuss and clarify these aspects in the paper and update accordingly the related work section.
- The idea of reserving new prototypes for future classes is not new. It was addressed in [3] (see below). However, it limits considerably the generalization capability of your approach. In a real-world problem, you do not know how the distribution of novel classes will look like, so it is not posible to 'pre-define' prototypes. Some other approaches such as self-supervised learning might be preferred instead to discover new clusters in the unlabeled data.
- Compare your approach with some methods for Novel Class Discovery

### Questions
The authors need to clarify the following aspects:
- They claim (first paragraph, page 2, middle): "Instead of identifying and eliminating OOD samples during training, we may leverage...". The problem of OOD detection is addressed at inference time, not during training. You could simply refer as: unlabeled training data or semi-supervised learning. Please correct this aspect through the paper and clarify which problem you want to address.
- Since you want to identify and label unknown samples, your problem is related to Novel Class Discovery problem, not OOD detection.
See for instance references [1, 2] (below). Please discuss and clarify these aspects in the paper and update accordingly the related work section.
- The idea of reserving new prototypes for future classes is not new. It was addressed in [3] (see below). However, it limits considerably the generalization capability of your approach. In a real-world problem, you do not know how the distribution of novel classes will look like, so it is not posible to 'pre-define' prototypes. Some other approaches such as self-supervised learning might be preferred instead to discover new clusters in the unlabeled data.
- Compare your approach with some methods for Novel Class Discovery


References:
[1] Subhankar Roy, Mingxuan Liu, Zhun Zhong, Nicu Sebe, Elisa Ricci. Class-incremental Novel Class Discovery (ECCV 2022)
[2] K J Joseph, Sujoy Paul, Gaurav Aggarwal, Soma Biswas, Piyush Rai, Kai Han, Vineeth N Balasubramanian. Novel Class Discovery without Forgetting (ECCV 2022)
[3] Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, De-Chuan Zhan. Forward Compatible Few-Shot Class-Incremental Learning. (CVPR 2022)

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies continual learning in open-set scenarios and proposes a prototype-based approach, OpenACL, to leverage open-world data to enhance model performance on new tasks while mitigating catastrophic forgetting. The authors also demonstrate the effectiveness of the proposed method in online continual learning setting through experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet.

### Strengths
- To the best of my knowledge, this paper is the first to combine open semi-supervised learning with continual learning, so the work is novel.
- The motivation to improve the model's generalization ability to new tasks by leveraging unlabeled OOD data rather than eliminating it directly is reasonable. 
- The paper is well written and easy to follow.

### Weaknesses
1. My biggest concern is that the problem definition of Open SSCL seems unreasonable. The authors assume that large amounts of unlabeled data can be accessed at any time and are not affected by task switching. Furthermore, the input x for unlabeled and labeled samples comes from the same distribution. Such a setting is incompatible with traditional continual learning to a certain extent, or reduces the difficulty of its core problem, catastrophic forgetting. In particular, the ablation experiments provided by the appendix also show that without unlabeled data, the proposed method is inferior to ER in terms of accuracy. It is recommended that the authors provide more examples or explanations on the practicality and importance of the problem definition, rather than simply combining Open SSL and CL settings.

2. The experiments only focus on the setting of online continual learning (OCL), but the selected baselines are not specifically designed for OCL. Could the authors compare the results of offline continual learning? Or Could it be compared with the OCL methods mentioned in [1]?

3. The authors mention that the hyperparameters for baselines are set to the suggested value in their original implementation, but when the experimental settings are different from the original paper, how can the authors ensure that the setting of the hyperparameters is fair?

### Questions
1. In Table 1, why are the results worse for Independent using SimCLR/FixMatch?  Could the authors provide further analysis?
2. The baseline Single denotes training a single network on data from all tasks. Why is it affected by the new task in Figure 2 & 3? (It is recommended that the legend not block the image content)
3. Although the paper focuses on OCL settings, it seems to be limited to labeled datasets only. Because unlabeled data can be accessed at any time, as more and more tasks are learned, unlabeled data is learned more and more times. Have the authors considered that the unlabeled dataset will also change as the task changes?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
