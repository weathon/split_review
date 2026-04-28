# Towards Fair Knowledge Distillation using Student Feedback

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 5, 6, 6

## Abstract
With the advent of large-scale foundation models and their success in diverse fields, Knowledge Distillation (KD) techniques are increasingly used to deploy them to edge devices with limited memory and computation constraints. However, most KD works focus on improving the prediction performance of the student model distilled from large teacher models, and there is little to no work in studying the effect of distillation on key fairness properties, ensuring trustworthy distillation. In this work, we propose a fairness-driven distillation framework, BIRD (BIas-awaRe Distillation), which introduces a FAIRDISTILL operator to collect feedback from the student through a meta learning-based approach and selectively distill teacher knowledge. We demonstrate that BIRD can be augmented with different KD methods to increase the performance of a wide range of foundation models and convolu- tional neural networks after distillation. Extensive experiments across three fairness datasets show the efficacy of our framework over existing state-of-the-art KD meth- ods, opening up new directions to develop trustworthy distillation techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors adapt MAML  https://arxiv.org/abs/1703.03400 for improving fairness in knowledge distillation.

Overall, the authors use MAML to find a transformation on the teacher logits in a way which maximizes fairness *after* the student's update. This is analogous to the original use for MAML, which is to find model parameters such that the loss of the model *after* making an update on the target task is minimized. 

To summarize the authors' algorithm, one iteration proceeds in the following steps: 1) find a gradient update on the student with fixed transformation on the teacher, 2) find transformation on the teacher optimizing for the fairness objective under the updated student, 3) forget the the updated student from step 1) but use the updated transformation from step 2), and find a new update for the student parameters when optimizing jointly for knowledge distillation, one-hot cross entropy and fairness objectives.

The authors provide experiments and ablations across several image benchmarks and report good results on improved fairness.

### Strengths
The problem of fairness that the paper considers is important. The algorithm is very interesting and thought provoking. The results look good. I appreciate that the authors conduct a few interesting ablations shedding some light on the algorithm.

### Weaknesses
1. One major problem with the proposed method is that it needs the internal features of the teacher model for distillation (Eq. 4). However, as the paper mentioned in the motivation, most of the FMs in the real world only provide APIs. I.e., their features are barely accessible. This limitation seems to undermine the practical value of the proposed method severely.

2. Another concern is that the fairness is improved but in many cases at a price of degraded accuracy. E.g., CLIP- ResNet50 with UTKFace in Tab. 1， CLIP-ViT-32 −→ResNet18 with UTKFace in Tab. 2, CLIP-R50 −→ResNet18 with UTKFace in Tab. 2. Namely, the proposed method is not very strong. The fairness issue may be a concern, while accuracy also matters. 

A side concern is that, as seen above, the method does not perform well on the UTKFace dataset. Why?

3. Presentation: Some of the results are mistakenly highlighted. In Tab. 1, ∆mean-DEO, the highlighted results are sometimes not the best, which are quite confusing.

4. Minor issues.
- This paper seems quite relevant: https://aclanthology.org/2022.gebnlp-1.27.pdf. It reports a similar observation to Sec. 5.2 that KD amplifies biases.

### Questions
The observation that distillation harms fairness is not new, see https://arxiv.org/pdf/2106.10494.pdf section 3.7. It would be worthwhile reflecting this in the paper accordingly.

Can authors comment on a possible baseline directly optimizing for DEO (as introduced in the paper). A paper considering a related objective for distillation: https://proceedings.mlr.press/v216/wang23e/wang23e.pdf

'where L_reg is the regularization on f_S that penalizes student bias' -- is L_reg same as L_outer?

More baselines should be considered, e.g. what if we add equation 7 or 8 to the model objective? (is that the baseline from 5.2.4?) What if equation 6 is directly optimized for?

Why is it necessary to split the train dataset into a meta dataset and a new train dataset? What if one used the same (train) dataset for all the steps of the algorithm?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new fairness-aware KD method, BIRD (BIas-awaRe Distillation), for distilling foundation models. The main idea is to use a proposed FAIRDISTILL operator to collect feedback from the student through a meta-learning-based approach and selectively distill teacher knowledge.  This method can be used with several existing base KD methods for improved performance. Extensive experiments across three fairness datasets show the efficacy of the proposed method over other counterparts.

### Strengths
1. As FMs prevail day by day, distilling FMs is more important as well. The fairness problem of the distilled model is also of interest. This paper contributes to this axis.

2. The idea of selecting part of the teacher's feature for debiased distillation under the meta learning framework is technically sound and intuitive.

3. Empirically, the method is effective ("Results show that BIRD improves the fairness of the knowledge distillation framework by 40.91%") and it is ready to be used along with existing KD methods to enhance the fairness of the distilled student.

### Weaknesses
1. This paper proposes a meta-learning framework to solve the fairness issue in KD. I don't see why meta-learning can be used to resolve fairness here; the intuition and motivation are unclear. Specifically, the paper does not clearly articulate why a meta-learning approach, which typically focuses on learning to learn across tasks, is suitable for mitigating bias within a single task of knowledge distillation. The connection between meta-learning's ability to adapt to new tasks and the goal of reducing bias in a student model is not well-established. The paper should provide a more detailed explanation of how the meta-learning framework's inner and outer loop optimization specifically target and reduce bias, rather than just improving overall performance.


2. The experiments are mainly conducted on CelebA and UTKFace, two small datasets. I think it is necessary to evaluate a larger benchmark, such as a dataset that a mixup of gender/racial images with other non-biased images, i.e., animals,  to verify the effectiveness of the proposed method on a larger scale setting. The same issue is on the choice of student models; more models should be evaluated, such as ViT (not as a teacher but as a student model). The limited scale of the datasets makes it difficult to generalize the findings to more complex and realistic scenarios. Furthermore, the choice of student models is also limited; exploring a wider range of architectures, particularly those that differ significantly in their inductive biases (such as Vision Transformers), would provide a more robust evaluation of the proposed method's general applicability. The paper should also consider evaluating the method's performance with more complex teacher models and different distillation strategies.


3. It is disappointing that this paper is only focused on the fairness of classification. The application of classification is very limited and has been extensively explored over the past decades. I think it is essential to test KD fairness on more settings, such as multi-turn vqa. Otherwise, I suggest changing the title to a more specific topic, i.e. "Towards Fair Knowledge Distillation on Image Classification". Focusing solely on classification limits the scope and impact of the work. The paper should explore the applicability of the proposed method to more complex tasks, such as multi-turn VQA or image retrieval, where fairness concerns are also present. These tasks often involve different types of data and require more complex models, providing a more comprehensive evaluation of the method's effectiveness in diverse scenarios.

### Questions
NAN

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates making student models with less gender & racial bias in knowledge distillation. The meta-learning framework is used to achieve this goal, and the experiments are done on CelebA and UTK datasets.

### Strengths
The motivation of this paper is sound, fairness in KD is indeed an important topic in the era of large models. This paper is well-presented.

### Weaknesses
1. While the paper's overarching framework appears to draw heavily from the "learning how to teach" paradigm (as detailed in Park et al., 2021; Liu et al., 2021; Zhou et al., 2021), its overall contribution may be perceived as somewhat incremental. This perception arises from the adaptation of a pre-established framework to address knowledge distillation. Despite this, the proposed solution stands out due to its technical novelty and apt alignment with the problem statement. A deeper dive by the authors into the technical distinctions between their work and prior studies would further solidify their contribution.

2. For the benefit of practitioners, the authors might consider expanding their ablation section to detail not just the memory overhead, but also the time overhead associated with the distillation process. This is particularly relevant given the well-documented time-intensive nature of meta-learning-based approaches. Specifically, the authors should provide a breakdown of the time cost per iteration for both the meta-learning component and the overall distillation process, allowing for a more granular understanding of the computational demands.

### Questions
See weakness. My main concerns are the following: 1) it is not clear why the meta-learning framework is effective for **fairness** (not the overall results.), 2) the experiments are insufficient regarding the size of the dataset, the model size of the students, and the tasks.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study introduces a "student-aware selective feature distillation" approach, drawing inspiration from meta-learning, which enables the teacher to impart unbiased information effectively to the student.

### Strengths
1. The authors have lucidly articulated both the problem definition and the corresponding solution formulation.

2. Distinguishing itself from prior research, this study emphasizes adapting the teacher's predictions to remain unbiased. This adjustment, in turn, facilitates the training of a student that naturally inherits this unbiased character due to the teacher's modified features.

3. The introduction of a meta-learning inspired transfer approach is both well-conceived and aptly presented, offering a compelling solution for unbiased (or fair) knowledge transfer.

4. In the results section, the authors comprehensively address pivotal concerns, including the problem's justification (5.2.1), the efficacy of their proposed method (5.2.2), the technique's adaptability across various KD frameworks (5.2.3), and insightful ablation studies that dissect various components of their framework (5.2.4 and 5.2.5).

### Weaknesses
1. I am curious about the results when we apply BIRD to existing methods, and test their performance according to the conventional criteria? eg. The Top-1 and Top-5 accuracy on CIFAR-100 and ImageNet. Will it degrade when pursuing fairness? I want to see more comparison results.

### Questions
Can the authors detail how the CLIP-Resnet-50 to ResNet 18 KD is performed. How is the KD distillation performed in the absence of the class-probability distribution of CLIP?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper targets on the fairness problem in knowledge distillation. The proposed method, BIRD, collects the feedback from the student model through a meta-learning-based approach and selectively distill teacher knowledge. BIRD is orthogonal with existing methods and computationally effective. Extensive experiment results show that BIRD can enhance the fairness remarkably.

### Strengths
1. This paper is overall well-written and easy to follow. 
2. This paper targets on an interesting problem, the fairness in knowledge distillation. 
3. The proposed method is orthogonal with existing methods, enhancing the fairness remarkably.

### Weaknesses
1. I am curious about the results when we apply BIRD to existing methods, and test their performance according to the conventional criteria? eg. The Top-1 and Top-5 accuracy on CIFAR-100 and ImageNet. Will it degrade when pursuing fairness? I want to see more comparison results.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
