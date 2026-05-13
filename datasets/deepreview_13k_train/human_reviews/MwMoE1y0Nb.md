# Understanding Distribution Alignment Through Category Separability In An Infant-Inspired Domain Adaptation Task

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
We introduce a novel distribution shift, called the VI-Shift, that mimics the trade-off between object instances and viewpoints in the visual experience of infants. Motivated by findings in infant learning literature, we study this problem through the lens of domain adaptation, but without ImageNet pretraining. We show that the performances of two classic domain adaptation methods, Joint Adaptation Network (JAN) and Domain Adversarial Neural Networks (DANN), deteriorate without ImageNet pretraining. We hypothesize that the separability of source and target category clusters in the feature space plays a crucial role in the effectiveness of JAN. So, we propose 3 metrics to measure category separability and demonstrate that target separability in the pretrained network is strongly correlated with downstream JAN and DANN accuracy. Further, we propose two novel loss functions that increase target separability during pretraining by aligning the distribution of within-domain pairwise distances between the source and target distributions. Our experiments show that the application of these loss functions modestly improves downstream accuracy on unseen images from the target dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
*Problem*: Domain adaption in a setting where the labelled (source) dataset, Toybox12, has images of a small number of object instances from 12 categories, but from many viewpoints. The unlabelled (target) dataset is IN-12, containing natural images with many instances of the same categories sourced from ImageNet/MSCOCO. 

*Methodology*: Pretrain features with a variety of techniques, from supervised to self-supervised, and then finetune the network with a domain adaptation method (JAN). Measure the final classification accuracy as the evaluation metric. 

*Analysis*: The authors develop three metrics to quantify the separability of class clusters in the pretrained feature space, and draw correlations between these metrics and downstream JAN accuracy. Based on these findings, authors develop a new metric which performs better than DCL constrastive learning initialisation.

### Strengths
* I find the problem tackled in this paper to be very interesting and worthy of further study. The problem setting mimics the way in which infants learn about object categories - wherein only a few object instances are available to the infant, but the infant has the ability to play with the object and look at it from a number of viewpoints. 
* The dataset contribution seems interesting, with the proposed dataset extending the Visda-2017c challenge with real videos and test instances, rather than rendered 3D objects for training.
* The proposed method provides a solid boost over standard DCL contrastive learning baseline, improving performance from 50.6 to 56.7.

### Weaknesses
 * The main weakness for me is the primary evaluation methodology. Specifically, authors use JAN finetuning and accuracy as a metric by which to evaluate pretrained features. I can see two issues with this: (i) in many cases, simple linear probing seems to substantially outperform JAN evaluation (Table 1). I cannot see why linear probing is not used as the primary metric. Given this, it is unclear to what extent the findings are an artefact of JAN failure modes. (ii) In a similar vein, if a domain adaptation method is to be used as the evaluation metric, why not use a more modern approach, e.g (FixBi, Na et al. 2021, CoVi Na et al. 2021). It is not clear if the conclusions drawn are specific to JAN or generalizable to other domain adaptation techniques. 
    * Perhaps I have misunderstood something here. 
* The proposed metrics to measure feature space separability seem a little underwhelming to me, with a maximum correlation with final accuracy of only 0.5. This indicates that either other metrics might be better (e.g simple k-means/k-NN accuracy) or that cluster separation of pretrained features is not actually linked to downstream JAN accuracy. It's possible that the proposed metrics are not capturing the relevant aspects of feature space structure that are important for domain adaptation.
* The authors propose a new contrastive learning technique without trying extensive baselines over simple DCL. For instance, supervised contrastive learning is quite similar in spirit to the proposed method (Supervised Contrastive Learning, Khosla et al). The paper would be strengthened by a more thorough comparison to existing contrastive learning methods, especially those that incorporate label information.

### Questions
* Did the authors try other self-supervised or contrastive baselines? (e.g MAE, Supervised Contrastive Learning, DINO etc)
* Did the authors try other class separability metrics, like k-NN or k-Means?

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
4

### Summary
This paper introduces VI-Shift, a new concept in distribution shift inspired by cognitive psychology and the way infants learn. The problem  of VI-Shift focuses on learning from viewpoint-dominated images and generalizing to instance-dominated images. To study this, the paper introduces two new benchmarks and formalizes the task as a domain adaptation (DA) problem. The authors also consider the popular DA method, Joint Adaptation Network (JAN), with ResNet backbones. Additionally, they propose two Maximum Mean Discrepancy (MMD)-based loss functions, Pairwise-MMD and Neighbors-And-Strangers-MMD (NAS-MMD), to improve model accuracy in this specific setting.

### Strengths
- The idea of focusing on VI-shit is novel and interesting, especially considering the connection between deep learning and cognitive science
- The two introduced benchmarks are interesting and can be used by other researchers to study this novel problem of VI-shift.
- The paper is well written and all the contributions of this work are well detailed.
- The paper has many contributions, ranging from introducing new datasets and task and proposing a deep architecture for the task.

### Weaknesses
 -The paper primarily focuses on distribution alignment strategies, such as JAN, which is somewhat limiting given that various other domain adaptation (DA) paradigms could be explored to address the proposed VI-Shift problem. Specifically, adversarial domain adaptation methods, such as Domain-Adversarial Neural Networks (DANN) and Adversarial Discriminative Domain Adaptation (ADDA), could have been evaluated as potential solutions. Additionally, since the paper emphasizes contrastive learning, it would be valuable to examine how self-supervised learning approaches based on pretext tasks might perform in this context.
- The use of contrastive learning losses for domain adaptation is not novel, see e.g. [1]
- Since large Vision and Language Models (VLMs) are currently the mainstream it would have been important to show how multimodal models, such as CLIP, perform in this novel setting. Methods like CLIP have been already used for DA tasks, see e.g. [2]

### Questions
- How other DA adaptation techniques (e.g. adversarial approaches) perform in this new setting?
- Could VLMs-based approaches be already effective to address the VI-shift problem.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the distribution shift problem inspired by infant visual learning. The authors propose metrics to measure category separability in feature space, demonstrating a strong correlation between target cluster separability and JAN accuracy. To improve performance, they introduce MMD-based loss functions that align the distribution of within-domain pairwise distances between source and target domains, leading to improved downstream performance.

### Strengths
1. An innovative perspective bridging cognitive science and machine learning through modeling infant visual learning patterns in domain adaptation. This interdisciplinary approach provides valuable insights into both fields while introducing a novel problem formulation.

2. The author conducted detailed empirical analysis of feature space characteristics through multiple metrics. The thorough evaluation demonstrates the relationship between category separability and model performance.

3. The author proposed a practical solution through the NAS-MMD loss function, which shows improvements across multiple categories.

### Weaknesses
1. The theoretical foundation (motivation) for the viewpoint-dominated to instance-dominated knowledge transfer is not clear. As the study performs classification based on images, different viewpoints capture the instance from different aspects and they (the viewpoint and instance) can’t be separated. And there are no relevant biological studies stating that infants transfer knowledge of objects from viewpoint to instance. The infants may be able to recognize objects mainly from instance-dominated images with limited viewpoint image support. So the motivation is not convincing and lacks evidence. The paper would benefit from additional citations or discussion of cognitive science literature supporting this specific learning progression.

2. The dataset construction methodology requires a more detailed explanation. While the paper mentions using ImageNet and MS-COCO for IN-12 construction, a more comprehensive description of the category selection criteria would improve reproducibility. For example, in Figure 1 (b), the categories of IN-12 should correspond to the Toybox dataset (as stated in line 120). It appears in the figure that the categories are mostly different.

3. The choice of JAN as the primary domain adaptation method needs stronger justification. A comparative analysis with other state-of-the-art domain adaptation distribution-related approaches (for example, [1][2]...) would better illustrate the findings. Also, the author should further elaborate on why chose JAN instead of DCL for distribution analysis? Why not directly make improvements on the Linear approach? The comparison of Linear evaluation in Table 1 lacks details (like network structure, parameter size, training process etc.)

4. The dimensional reduction technique selection (UMAP) would benefit from comparative analysis with alternatives like t-SNE and PCA. The rationale for removing outlier samples should be further elaborated.

5. The connection between the JAN-based distribution analysis and the DCL-based implementation could be better established. DCL may not share the same domain adaptation results as JAN.

6. The proposed NAS-MMD loss is a variant of MMD with limited contribution. The idea of moving neighbours closer and taking negative samples apart has been widely used in domain adaptation tasks.

7. The quality of the visual presentation in Figure 4 could be enhanced.

### Questions
Please refer to the weaknesses of the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a question of how human and embodied visual agents learn object information with the tradeoff between object instances and object viewpoints. For this question, this work presents two kinds of data distribution: viewpoint-dominated (VD) distribution that is rich in the distribution of viewpoints; and also instance-dominated (ID) distribution that is rich in the number of different category instances.

To make a formal analysis of this problem, this work presents to study the DA problem from a VD dataset to an ID dataset with 12 categories. They found the the popular JAN model does not perform well. To this end, they propose 3 metrics to measure the category separability in the feature space and found that this is highly correlated with the JAN's performance. Finally, the work proposes a set of new loss functions that can improve the performance of JAN.

### Strengths
1. This work is motivated by an interesting problem.

In the Introduction, this paper presents a very interesting problem: is there a tradeoff between VD and ID data distribution when human or AI agents learn visual concepts? As mentioned in the paper, this problem has a lot of background support in psychology can could be potentially very interesting to explore in the area of visual learning.

2. This work includes a clear analysis and presentation.

This paper includes clear and comprehensive experiments about the properties of JAN, the proposed metrics, and loss functions. The visualizations are very clear and support the paper's arguments.

### Weaknesses
1. The relationship of human learning from VD vs ID data is not well connected with the DA problem.

Although this paper presents an interesting problem of the tradeoff between VD and ID data in visual concept learning, the main technical part of this paper focuses on doing DA from a VD dataset to an ID dataset. It is very vague to me why the problem of DA from VD to ID is related to the visual concept learning process from these data distributions. It seems to me that the technical part of this paper can be conducted on other DA problems, like from animation to real images, and also leads to the same conclusions. Therefore, it is unclear why VD and ID is important in this paper.

2. It is questionable whether it is necessary to study the problem assuming that the model is not trained on ImageNet.

The paper focuses on the performance of JAN without ImageNet pertaining; while the ImageNet pretrained version simply surpasses all the other models in this paper. It is unclear why it is important to ignore ImageNet pertaining, given that ImageNet pertaining is very common and widely used. 

In other words, if the conclusion and proposed method only works for non-ImageNet pertaining model and yields worse performance than vanilla ImageNet pretrained ones, the technical application contribution of this paper is limited.

3. The focus on JAN needs more justification.

This paper's technical part centers around a popular DA method, JAN. I agree that JAN is a popular method and has been well studied, however, there are many other popular and newer DA methods (like MCD, for example) that claim to achieve better performance than JAN. This work should either prove that the conclusion and proposed method also works for newer methods or explain why only studying JAN is important and sufficient.

4. Unclear whether performance improvement of the proposed method is significant.

As shown in Table 3, the proposed method leads to performance improvement from 50.64 to 56.72. Although there is some improvement, it is unclear how significant this improvement is. After all, when compared with all other numbers in Table 1, 56.72 is still quite low and far from solving the problem.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
