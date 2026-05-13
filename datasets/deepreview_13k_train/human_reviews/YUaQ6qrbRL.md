# Right Time to Learn: Promoting Generalization via Bio-inspired Spacing Effect in Knowledge Distillation

- Decision: Reject
- Scores: 5, 5, 6, 8

## Abstract
Knowledge distillation (KD) is a powerful strategy for training deep neural networks (DNNs). While it was originally proposed to train a more compact “student” model from a large “teacher” model, many recent efforts have focused on adapting it as an effective way to promote generalization of the model itself, such as online KD and self KD. Here, we propose an easy-to-use and compatible strategy named Spaced KD to improve the effectiveness of both online KD and self KD, in which the student model distills knowledge from a teacher model trained with a space interval ahead. This strategy is inspired by a prominent theory named spacing effect in the field of biological learning and memory, positing that appropriate intervals between learning trials can significantly enhance learning performance. We provide an in-depth theoretical and empirical analysis showing that the benefits of the proposed spacing effect in KD stem from seeking a flat minima during stochastic gradient descent (SGD). We perform extensive experiments to demonstrate the effectiveness of our Spaced KD in improving the learning performance of DNNs (e.g., the additional performance gain is up to 2.31% and 3.34% on Tiny-ImageNet over online KD and self KD, respectively).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors perform a scheme on the lines of online and self KD to promote generalization of the model. They propose SpacedKD which is inspired from spacing effect in biological learning which highlights that study sessions across time is critical for memory formation. They argue that this spacing effect can be generalized to a kind of ensemble learning at the temporal scale. They implement this spaced KD in both online and self KD setups. For online KD, they just train the teacher in advanced for a certain number of steps termed as spaced interval. Then they just freeze this teacher and distill this knowledge to the student using the same data. They further provide a theoritical justification of its better generalization than online KD by analyzing the Hessian Matrix of the loss function of student in both the scenarios by arguing that if the student model converges to a local minimizer at step t of SGD then expected value of trace of hessian matrix using Spaced KD is lesser.  Furthermore, they provide experimental results to verify their claim on the CIFAR-100, ImageNet-100 and Tiny-ImageNet datasets for both self and online KD where they show significant gains.

### Strengths
The connection identified to the spacing effect in biological learning is quite interesting and provide intuitive backing for the method. The analysis of hessian of loss being lesser for spaced KD is also interesting and it being converging to a flatter local minima via SGD. 
The results show prominent gains in performance which is again promising. Furthermore, the authors have also provided analysis of using different value of the interval various architectures along with the different architecture of teacher student pairs (inclduing different architectures for teacher). Also, the analysis in presence of various corruptions further backs the use case of their method.

### Weaknesses
Not exactly clear from the paper what is the exact difference between spaced and online KD setup. Also, why is the description of implementing spaced KD for self distillation not provided. I understand that it is pretty straightforward to adapt it but for completeness it should be there and there might be some smal changes that would be required into a naive adaptation that helps improving the result. 

Regarding results, even though the authors have mentioned in one of the figure captions the reason for not providing results on ViT architecture, I feel that it is not justified. To test its applicability it should be tested on state of the architectures and large scale datasets. The major results revolve around CIFAR-100, Tiny-ImageNet and ImageNet-100 architectures and only one result is provided in the ImageNet-1k (and that too with a ResNet-18 architecture) leading to speculations that it might not give this sort of gains on ImageNet-1k or other large scale settings. Also, I dont understand what the Appendix A.5 results want to convey.

### Questions
Please check the weakness section.  Appendix A.5 is confusing. Does it imply that distilling from a teacher trained s steps ahead is not useful? But then this is the method right that first you should update teacher for s steps and then using that distill to student for those s steps. Also it would have been very useful to provide a psuedo code comparison for online and spaced KD so as to what exactly is the differennce. Overall I feel the presentation of the paper could have been improved especially the emipirical section. 

Anyhow, right now I am going with the marginally below acceptance but I would be happy to reconsider my rating based on the justifications provided in the rebuttal.

### Soundness
3

### Presentation
2

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
The paper introduces a new method for online knowledge distillation that uses the teacher model trained ahead of the student at each epoch, resulting in a flatter loss landscape.

### Strengths
The paper is well-written and easy to follow.

The experiments show the effective improvement of the proposed method over vanilla KD.

### Weaknesses
1) I did not get the connection between the proposed method and the spacing effect in biological learning mentioned in Section 3.2. The teacher has different weights from the student. Why does training for several additional epochs cause a spacing effect?

2) The theoretical part is not robust. The proposed method assumes that the teacher trained ahead is close to the local minimizer $\phi^*$, so why not use a well-trained model instead?

3) There is a lack of comparison with other KD methods like [1,2]

[1] Self-Distillation from the Last Mini-Batch for Consistency Regularization.

[2] Self-Knowledge Distillation with Progressive Refinement of Targets.

### Questions
1) What are the numerical values of x and y in Figure 2a?

2) As 0.5 epochs mean training on half of the dataset, would this cause a bias towards that half of the dataset? Is the training dataset shuffled?

3) How can the proposed method be applied to self-distillation in [3], where the teacher is the deepest layer of models and the students are the shallow layers?

4) What dataset was used for Figure 3, and which settings were used for the experiments?



[3] Be Your Own Teacher: Improve the Performance of Convolutional Neural Networks via Self Distillation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies a variant of Knowledge Distillation, designed with Space Interval learning, inspired by the spacing effects observed in biological learning. 

Design: The Space Interval method is applied to Online KD, where the teacher model is trained a few intervals (s iterations) ahead of the student. The teacher’s weights are then frozen and used to train the student, who lags behind. The hypothesis is that, by updating the teacher less frequently, it provides more stable guidance to the student. 

Theoretical Analysis: The authors use the trace of the Hessian matrix as a measure of the loss landscape’s flatness, where a smaller Hessian trace indicates a flatter, and thus potentially more generalizable, landscape. They show that the loss landscape of the new paradigm has flatter Hessian trace ompared to the traditional Online KD, suggesting improved generalization. 

Experimental Results: The proposed method outperforms the traditional Online KD on CIFAR-100, Tiny-ImageNet, ImageNet-100, and ImageNet-1K datasets by approximately 1–2% on average with three ResNet variants. The authors also provide experiments demonstrating robustness improvements over online and self-KD counterparts, along with ablation studies on learning rate, batch size, and loss functions.

### Strengths
Overall, the paper is easy to follow. The idea seems simple to implement and appears interesting as inspired by biological learning processes. Empirically, it achieves a few percentage points of improvement over existing online methods, as demonstrated in the experimental sections.

### Weaknesses
 The results are overall encouraging, there are few points to be clarified with the authors in term of bio-inspiration, the generality of the method, the settings used across experiments and the seemingly conflicts between theoretical and empirical results as in Questions section.

 1. While the bio-inspiration is interesting, the learning mechanism applied here differs from the spacing effects observed in biology. In biological learning, spacing effects enhance learning and memory retention of a subject when study sessions or practice trials are spread across intervals of time. However, in this application, the teacher is trained at intervals while the student learns continuously which seems the design is not well-aligned with the biological inspiration. Could the authors provide deeper details on this point to show the bio-inspiration is valid.

 2. In the online setting, most experiments use a teacher with the same architecture as the student. To demonstrate the generality of the method, could the authors conducting experiments where the teacher’s architecture is significantly larger than the student's?

 3. As shown in Fig. 3, the period of applying Space KD is critical. Are all experiments using the best setting or different experiments has different periods? Could the authors provide details on the optimal settings used across the experiments in the paper and explain how these settings were selected?

 4. Is there a conflict between the theoretical analysis and the empirical results? While the theoretical analysis is independent of the period during which Space KD is applied, the empirical results indicate that it is only useful in the last 10 epochs of training? Could the authors provides also the only online KD baseline's results in Fig. 3 for the comparision?

### Questions
1. While the bio-inspiration is interesting, the learning mechanism applied here differs from the spacing effects observed in biology. In biological learning, spacing effects enhance learning and memory retention of a subject when study sessions or practice trials are spread across intervals of time. However, in this application, the teacher is trained at intervals while the student learns continuously which seems the design is not well-aligned with the biological inspiration. Could the authors provide deeper details on this point to show the bio-inspiration is valid.

2. In the online setting, most experiments use a teacher with the same architecture as the student. To demonstrate the generality of the method, could the authors conducting experiments where the teacher’s architecture is significantly larger than the student's?

3. As shown in Fig. 3, the period of applying Space KD is critical. Are all experiments using the best setting or different experiments has different periods? Could the authors provide details on the optimal settings used across the experiments in the paper and explain how these settings were selected?

4. Is there a conflict between the theoretical analysis and the empirical results? While the theoretical analysis is independent of the period during which Space KD is applied, the empirical results indicate that it is only useful in the last 10 epochs of training? Could the authors provides also the only online KD baseline's results in Fig. 3 for the comparision?

### Soundness
3

### Presentation
3

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
This paper introduces Spaced Knowledge Distillation (Spaced KD), a bio-inspired approach to knowledge distillation that incorporates spacing intervals in the training process to enhance model generalization. Inspired by the "spacing effect" observed in biological learning, Spaced KD involves training a teacher model a few steps ahead of the student model and periodically transferring knowledge at intervals. This technique allows the student model to find flatter minima in the loss landscape, which leads to better generalization and improved robustness to noise. Extensive experiments demonstrate that Spaced KD yields superior performance across multiple datasets and architectures compared to traditional KD methods without additional training costs.

### Strengths
1) Novelty: The paper introduces a fresh approach by integrating the bio-inspired “spacing effect” into knowledge distillation (KD), which is relatively unexplored in existing literature.

2) Strong Theoretical Foundation: The authors provide a well-structured theoretical analysis linking Spaced KD to flat minima, supporting claims about enhanced generalization. The use of Hessian trace analysis to demonstrate why Spaced KD leads to better generalization adds rigor and robustness to the claims.

3) Comprehensive Experiments: The experimental results are extensive, spanning multiple datasets (CIFAR-100, Tiny-ImageNet, ImageNet-100, and ImageNet-1K) and network architectures (ResNet variants, DeiT-Tiny, PiT-Tiny). These experiments show consistent improvements with Spaced KD, reinforcing the method’s general applicability.

4) Practicality: Spaced KD is straightforward to implement, making it accessible for a broad range of applications without requiring additional training time or major architectural modifications. This ease of integration enhances its appeal for both academia and industry.

5) Robustness and Generalization Gains: Spaced KD demonstrates superior robustness to noise and out-of-distribution data, an increasingly valued property in modern AI. This robustness adds significant value, especially for real-world applications where models encounter varied data distributions.

### Weaknesses
1) Incremental Novelty: While Spaced KD introduces a creative application of the spacing effect to knowledge distillation, it lacks a fundamentally new mechanism within the KD framework. This incremental contribution may limit its overall impact, as the method primarily builds on existing KD techniques without significantly advancing the underlying theory. The core idea of transferring knowledge from a teacher to a student, even with a temporal delay, does not introduce a novel loss function or optimization strategy that fundamentally alters the knowledge distillation process. The method essentially modifies the timing of knowledge transfer, rather than introducing a new way of representing or utilizing the knowledge itself. This limits the novelty to the application of a bio-inspired concept rather than a theoretical breakthrough in distillation techniques.

2) Interval Sensitivity and Adaptability: The success of Spaced KD hinges on selecting an effective interval for knowledge transfer. However, the paper does not explore adaptive strategies for dynamically tuning this interval, which may constrain Spaced KD’s versatility across diverse tasks and datasets with varying training schedules. The paper does not investigate how the optimal interval might change with different learning rates, batch sizes, or optimizers. The lack of a systematic approach to determine the optimal interval could lead to suboptimal performance in practical applications where manual tuning is not feasible or efficient. Furthermore, the paper does not address the potential for the optimal interval to change during the training process itself, which could necessitate a dynamic adjustment strategy.

3) Applicability Across Model Sizes and Architectures: Spaced KD is demonstrated only with identical teacher and student models of the same size, without addressing model compression. It remains uncertain how this approach would perform if applied to different model sizes or architectures, such as a transformer teacher model paired with a CNN student. The potential to generalize Spaced KD for cross-architecture or cross-size distillation remains unexplored. The paper does not provide any analysis on how the spacing interval should be adjusted when the teacher and student models have different capacities or representational capabilities. This lack of exploration limits the applicability of the proposed method in scenarios where model compression or transfer learning across different architectures is required.

### Questions
1) Applicability Across Model Sizes and Architectures: How does Spaced KD perform when the teacher and student differ in size or architecture? Specifically, can it support scenarios where the teacher is larger or has a different architecture (e.g., a transformer teacher with a CNN student), or does it rely on identical model sizes?

2) Comparison with Gradient-based Methods: How does Spaced KD differ from traditional gradient-based methods where gradients are updated after each batch? Given that Spaced KD introduces intervals between teacher and student updates, is this approach essentially a modified gradient update, or does it provide additional benefits that distinguish it from standard gradient optimization?

### Soundness
3

### Presentation
3

### Contribution
2
