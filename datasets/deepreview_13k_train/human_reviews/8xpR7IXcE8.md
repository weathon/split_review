# Classroom-Inspired Multi-Mentor Distillation with Adaptive Learning Strategies

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
We propose \textbf{ClassroomKD}, a novel multi-mentor knowledge distillation framework inspired by classroom environments to enhance knowledge transfer between student and multiple mentors. Unlike traditional methods that rely on fixed mentor-student relationships, our framework dynamically selects and adapts the teaching strategies of diverse mentors based on their effectiveness for each data sample. ClassroomKD comprises two main modules: the \textbf{Knowledge Filtering (KF)} Module and the \textbf{Mentoring} Module. The KF Module dynamically ranks mentors based on their performance for each input, activating only high-quality mentors to minimize error accumulation and prevent information loss. The Mentoring Module adjusts the distillation strategy by tuning each mentor's influence according to the performance gap between the student and mentors, effectively modulating the learning pace. Extensive experiments on image classification (CIFAR-100 and ImageNet) and 2D human pose estimation (COCO Keypoints and MPII Human Pose) demonstrate that ClassroomKD significantly outperforms existing knowledge distillation methods. Our results highlight that a dynamic and adaptive approach to mentor selection and guidance leads to more effective knowledge transfer, paving the way for enhanced model performance through distillation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
after reading the comments from other reviewers and corresponding responses, I would like to keep my initial score due to limited novelty and insufficient experiments.

———— 
This paper follows a setting in knowledge distillation where there are multiple teacher models involved. Instead of using traditional approach that all teacher models influence the student model, it proposes to first rank the performance and then filter out teacher models that underperform the student one. Afterwards, use a KL divergence driven weight assignment according to the performance gap. 

Experiments are conducted on CIFAR100, ImageNet and COCO. However, one thing to notice that on ImageNet and COCO pose estimation tasks, the authors only compare their method with the baseline student method without KD (NOKD).

### Strengths
+ The motivation that let more models teach the student model is not novel, but their approach to dynamically rank and select the better teachers per sample seems interesting and novel to me.

+ The paper is clearly written and easy to follow. The figure of motivation clearly shows the differences between their approach with earlier works. 

+ Experiments on CIFAR100 are very comprehensive.

+ Ablation studies are complete and cover many aspects of the proposed ClassroomKD.

### Weaknesses
I have the following concerns and hope to see the response from the authors.

1. How does the ClassroomKD compare to other multiple teachers approaches? For example, [A] proposes a dynamic framework that also learns from multiple teachers and multi-level knowledge. The proposed ranking the best seems very similar to the proposal in [A].

2. While experiments on CIFAR-100 are very comprehensive, the evaluation on ImageNet and COCO pose estimation are not sufficient. Could you clarify the meaning of the AVER performance in the two tables? Additionally, please explain the underlying method used for these experiments.

3. On CIFAR100, the performance gap between the proposed method and others is somewhat marginal. It may be not a good way to evaluate your method on CIFAR100 since it is considered overfitted in current research. Results on larger, more challenging datasets would provide more valuable insights into the effectiveness of your approach.
 
4. It would be beneficial to include comparisons with at least one state-of-the-art multi-teacher method on larger datasets such as ImageNet or COCO.

### Questions
Please see the above weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents ClassroomKD, a novel multi-mentor knowledge distillation framework inspired by classroom dynamics. It addresses challenges in multi-mentor distillation and consists of a Knowledge Filtering Module and a Mentoring Module. Experiments on multiple datasets show its superiority over existing methods.

### Strengths
1. The framework's dynamic mentor selection and adaptive teaching strategies are highly innovative. It simulates a classroom environment, a novel approach compared to traditional methods, and effectively solves problems in multi-mentor distillation.
2. Theories behind the KF and Mentoring Modules are reasonable. The loss function construction is also sound. Experiments on diverse datasets with detailed settings and in-depth result analysis provide strong evidence for the method's effectiveness. It contributes to knowledge distillation research, inspiring future work. Its good performance in computer vision tasks offers practical solutions.
4. The paper has a clear structure and logical flow. The writing is clear, and figures aid understanding. The appendix enriches the paper.

### Weaknesses
1. In-depth Analysis of Limitations: The limitations section could be enhanced. For example, more details on challenges in applying to other domains and the impact of framework complexity on performance and tuning difficulties are needed. Specifically, the paper should discuss the potential for negative transfer when applying ClassroomKD to tasks with significantly different feature spaces than those used in the computer vision experiments. Furthermore, the computational overhead introduced by the dynamic mentor selection and adaptive teaching strategies should be analyzed in detail, including its impact on training time and resource consumption. The discussion should also address the sensitivity of the framework to the number of mentors and the potential for performance degradation with too many or too few mentors.
2. Exploration of More Practical Application Scenarios: While successful in computer vision, its potential in other areas like NLP and recommendation systems should be explored to show broader applicability. The paper should discuss how the knowledge filtering and mentoring modules would need to be adapted for sequential data in NLP or for user-item interaction data in recommendation systems. For example, how would the concept of 'mentors' and 'students' translate to these different data modalities, and what modifications would be needed to the loss functions to accommodate these changes? The paper should also discuss the challenges of applying the framework in scenarios with limited labeled data or in online learning settings.
3. Sensitivity Analysis of Hyperparameter Settings: A sensitivity analysis of hyperparameters would help researchers better understand and apply the method. The paper should provide a more detailed analysis of the impact of the temperature parameter τ on the distillation process, including a discussion of the optimal range for different tasks and datasets. Furthermore, the influence of other hyperparameters, such as the weighting factors for the knowledge filtering and mentoring losses, should be investigated. The paper should also discuss the potential for overfitting to specific hyperparameter settings and provide guidelines for selecting appropriate values for new tasks.

### Questions
see the weaknesses

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work deals with a multi-teacher knowledge distillation method, where the key idea is to assess the fitness of each teacher at individual training sample level, and use that fitness to select the teachers for knowledge distillation in a weighted manner. The proposed method has been evaluated on a number of image classification tasks in comparison to previous methods.

### Strengths
Clear writing up and presentation.

Good coverage of the literature.

Reasonably good experiment design and setup and presentation.

### Weaknesses
 **Novelty**:
1) This data sample conditioned teacher weighting idea has been proposed in [Ref-A] where even more advanced meta-learning based optimization algorithm was proposed for model training - bilevel optimization algorithm, in addition to other complexity and challenges, like data access to other domains and label scarcity. In general, this proposed work is a subset of Ref-A in techniques.
- [Ref-A] Wang Z, Ye M, Zhu X, Peng L, Tian L, Zhu Y. Metateacher: Coordinating multi-model domain adaptation for medical image classification. Advances in Neural Information Processing Systems. 2022 Dec 6

2) More justification should be added on why only those mentors/teachers with higher probability estimation on the true class label are selected and activated for distillation, whilst the remaining teachers are not. For example, in cases that the student model makes too confident precision for a specific training sample, those less confident teachers may provide a signal to soften this predictive confidence. This is because, in knowledge distillation, the key knowledge with the teacher is mostly about the class distribution, rather than seeking the maximum of true class probability. Under this consideration, the proposed knowledge filtering design is questionable. 

3) Similarly, more discussion and explanation about how Eq (8) represents the performance gap should be made. The similar concern holds here as the above.

**Experiments**:
1) The performance gap in comparison to previous art knowledge distillation is some limited, mostly within 0.5%. This suggests the benefits of this method is not significant. 

**Presentation issues**:
1) In general, the first appearance of previous work should come with a reference, e.g., no reference for DGKD (Line 50), and no reference for those mentioned methods in Fig 1's caption. The authors need to take a careful global check for this. 

2) The two concepts, performance gap (Line 52) and capacity gap (Ling 40), seem mixed and they are not properly defined, discussed and compared in the Introduction. 

**Overall**:
Given the limited novelty in terms of techniques, lacking of solid design rationales,  and not significant experimental advantage, I do not find enough significance of accepting this work at the current shape. More research works are needed to further enhance it for future submission.

### Questions
Please check the weaknesses above.

### Soundness
2

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
4

### Summary
This paper presents a knowledge distillation framework ClassroomKD to improve knowledge transfer from multiple mentors to a student model by dynamically selecting mentors based on their effectiveness for each data sample. The framework includes a Knowledge Filtering Module, which ranks and activates high-quality mentors, and a Mentoring Module, which adjusts each mentor's influence according to the performance gap with the student. Experiments on CIFAR-100, ImageNet, COCO Keypoints, and MPII Human Pose indicate that ClassroomKD performs competitively with existing methods, suggesting that adaptive mentor selection can enhance knowledge transfer and model performance.

### Strengths
1. This paper provides an in-depth analysis of existing methods and highlights their respective limitations.
2. The proposed framework is effective, and some experimental results look good.
3. The paper is well-written and easy to understand.

### Weaknesses
1. In the second section, recent literatures on knowledge distillation from the past two years is limited, and it is recommended to include additional references. For example: [1] Logit standardization in knowledge distillation  [2] Class attention transfer based knowledge distillation.
2. In Figure 2, based on the article's content, the indicator label for Active mentors should be "M’"
3. According to the results in Table 1, the improvement achieved by the proposed method compared with the single-teacher distillation methods appears modest. Theoretically, the use of multiple mentors should yield a more significant improvement than a single mentor. It is recommended to conduct further experimental analysis to explore this aspect.

### Questions
Please refer to the Strengths and Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3
