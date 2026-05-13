# AuG-KD: Anchor-Based Mixup Generation for Out-of-Domain Knowledge Distillation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Due to privacy or patent concerns, a growing number of large models are released without granting access to their training data, making transferring their knowledge inefficient and problematic. In response, Data-Free Knowledge Distillation (DFKD) methods have emerged as direct solutions. However, simply adopting models derived from DFKD for real-world applications suffers significant performance degradation, due to the discrepancy between teachers' training data and real-world scenarios (student domain). The degradation stems from the portions of teachers' knowledge that are not applicable to the student domain. They are specific to the teacher domain and would undermine students' performance. Hence, selectively transferring teachers' appropriate knowledge becomes the primary challenge in DFKD. In this work, we propose a simple but effective method \M. It utilizes an uncertainty-guided and sample-specific anchor to align student-domain data with the teacher domain and leverages a generative method to progressively trade off the learning process between OOD knowledge distillation and domain-specific information learning via mixup learning. Extensive experiments in 3 datasets and 8 settings demonstrate the stability and superiority of our approach

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study introduces a technique for knowledge distillation wherein a student model learns from a pre-trained teacher model, even when the domains differ. Assuming a consistent label space across both domains, the research addresses the inherent distribution shift. It suggests the development of an 'anchor network' designed to extract domain-neutral features within the latent space. These domain-agnostic images, generated via latent features, are then employed as samples, mixed with student domain data, to facilitate efficacious distillation.

### Strengths
1. The manuscript is articulated with clarity, ensuring effective comprehensibility to the readers.

2. The authors masterfully contextualize their work in the introduction, clearly delineating their approach from conventional Generic KD and DFKD paradigms.

3. Their introduction of the anchor-based mixup strategy not only showcases novelty but also delivers a marked improvement in knowledge distillation outcomes when benchmarked against prior DFKD techniques and selected source-free domain adaptation methods.

4. The strategy to employ a mask for distinguishing between domain-specific and domain-neutral features is underpinned by a solid rationale, and its formulation and application are both commendably executed.

### Weaknesses
Major:

1. The proposed problem definition appears to closely resemble source-free domain adaptation (SFDA) [1]. The only distinction being that the target domain network is more lightweight compared to the pre-trained teacher network. As a result, the problem setup seems to simply be a specific instance of the broader source-free domain adaptation scenario. This raises concerns about the novelty of the problem statement. Specifically, the core idea of adapting a model to a new domain without source data is already well-explored in SFDA. The authors need to more clearly articulate what unique challenges arise from the student model being lightweight that are not already addressed by existing SFDA methods. The fact that the teacher model is fixed also does not seem to be a significant departure from typical SFDA scenarios, where the source model is often pre-trained and not fine-tuned during adaptation.

2. Given the dataset $D_{s}$, which consists of OOD student domain data with labels, I wonder about the performance of the student when trained solely on $D_{s}$  in a supervised manner. Did the authors conduct any initial tests to gauge baseline performance? Without such a baseline, I question how the authors determined the severity of the problem. It is crucial to understand how much the student's performance is improved by the proposed method compared to simply training on the target domain data, as this would provide a better understanding of the problem's difficulty and the effectiveness of the proposed solution.

Minor:

1. In Equation 2, the left-hand side (LHS) includes $z_{0}$  in its argument, but $z_{0}$ is absent from the right-hand side (RHS). Clarification is needed regarding the functional operations. This inconsistency is observed in Equations 2 and 3 as well. The relationship between the latent variable $z_0$ and the generated images $x$ and $\tilde{x}$ needs to be explicitly stated in the equations themselves rather than relying on the text description. The functional dependency should be clear from the equations alone.

2. For Equation 4, while the expectation is based on $z_{0}$, $z_{0}$ is not reflected in the RHS's loss combination. A similar issue is present in Equation 6. The equations should explicitly show how $z_0$ is used to compute the loss, rather than implying it through the expectation. The link between the latent space and the loss calculation is not clear enough.

3. In Equation 4, the loss function $L_{generator}$ is introduced. However, it's unclear whether this loss is optimizing the generator weights, the latent space, or both. This lack of clarity persists in Equations 5, 6, and 10. The equations should specify which parameters are being optimized by each loss function. It is crucial to differentiate between the optimization of the generator's weights, the encoder's weights, the student's weights, and the latent space itself.

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
3 good

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
This paper explores a significant and practical problem, Out-of-Domain Knowledge Distillation (OOD-KD). The authors believe that adopting models derived from DFKD for real-world applications suffers significant performance degradation, due to the discrepancy between teachers’ training data and real-world scenarios (student domain). Therefore, teachers’ knowledge must be selectively transferred. So the authors proposed AuG-KD, which utilizes an uncertainty-guided and sample-specific anchor to align student-domain data with the teacher domain. Experiments illustrate the effectiveness of the method.

### Strengths
1. It is valuable to explore the relationship between OOD and data-free distillation.

2. Although experiments were conducted on multiple dataset settings, the scale was small.

### Weaknesses
1. The motivation behind the setting of this paper is confusing. Why do we need to use out-of-distribution teachers when we have student domain data? Wouldn’t it be better to directly train the teacher under the student domain?
2. Lack of discussion with DFND[1], MosiacKD[2] and ODSD[3]. We think that since generation methods are known, sampling methods should also be compared.
3. Why not conduct experiments with CIFAR10 and CIFAR100? This is the mainstream dataset in the DFKD. Furthermore, can this method generalize on ImageNet?

### Questions
See Weaknesses.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies on a new but practical problem: Out-of-Domain Knowledge Distillation (OOD-KD). OOD-KD resembles Data-Free Knowledge Distillation (DFKD), which assumes the unavailability of teacher model’s training data except for one significant difference: teacher models’ training data and student models’ test data are not IID distributed. To tackle OOD-KD, the authors propose AuG-KD to align student-domain data with the teacher domain and leverage a generative method to progressively evolve the learning process from OOD knowledge distillation to domain-specific information learning. Experimental results demonstrate its promise of the proposed methods.

### Strengths
1.	The problem proposed is new but practical. With the development of ML techniques, most large-scale models are released in a black box or without access to their training data. Under this circumstance, OOD problems are unavoidable. This work focuses on this novel problem and offers a practical solution.

2.	The writing is clear and sophisticated. To best clarify the problem and its solution, this work utilizes formulae, method framework, pseudocode, flow chart and visualization.

3.	The experiments are extensive. This work conducts its experiments on 3 datasets and 8 settings in five times. Besides, 3 more ablation studies are designed to substantiate the effectiveness of each module of the method. In the appendix, 3 more baselines are taken into consideration. Quite a lot of DFKD methods pay little attention to the repeatability and stability, conducting each experiment with only one seed. This work considers more rigorously in the experiment settings.

4.	The experiment analyses are detailed and convincing. Apart from analyzing the stability and superiority of their proposed method, this work steps further. They provide a clear explanation towards the high variance of each method in the data perspective, which lacks related analysis in previous studies. Besides, they provide visualization for the mixup samples generated by their methods.

### Weaknesses
1.	The detail of the scheduler function is not released. Although the important characteristics of scheduler functions are provided in the main body, I cannot figure out the specific scheduler function used in the experiments. It is unclear how the scheduler's parameters are set and whether these parameters are sensitive to the performance of the method. The description of the scheduler function's properties is not sufficient to reproduce the experiments or to understand the impact of different scheduling strategies.
2.	The ablation study of the effectiveness of each component is not clear. The setting seems ambiguous and in need of further explanation. Specifically, the ablation study lacks a clear definition of what each ablation setting represents in terms of the proposed modules. The reported results for 'w/o Anchor' and 'w/o Mixup' are not sufficiently explained, making it difficult to understand the individual contributions of each module. The large performance difference between these two settings is also not well justified.

### Questions
1.	The same to weakness 1. To be specific, could you provide more details about which scheduler function you use and what kind of scheduler function would be preferred?

2.	The same to weakness 2. More specifically, the ablation result of w/o Anchor has a great performance improvement compared to that of w/o Mixup. Could you further explain it?

3.	This work provides detailed visualization on the mixup sample generated in the main body. We could see a gradual change as f increases. However, are there any relationships between the imgs at the same position with different f?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposed a new task of Out-of-Domain Knowledge Distillation (OOD-KD) extended from data-free knowledge distillation, which focused on the distribution shift between teacher domain and student domain. The main challenges are (1) the absence of teacher domain's data, (2) how to selectively transfer teachers' knowledge due to the distribution shift, and (3) how to balance OOD KD and domain-specific information learning. To tackle these three challenges, the method consists of a data-free learning generator, anchor learning module, and mixup learning module. Experiments on three datasets verified the effectiveness of the proposed method.

### Strengths
+ This work proposed a new problem for knowledge distillation, Out-of-Domain Knowledge Distillation (OOD-KD), which is challenging and practical to solve.

+ The presentation and organization of this paper is good. It is easy to figure out the main challenges and the solutions.

+ The experimental results on Office-31, Office-Home, and VisDA-2017 reached state-of-the-art performance.

### Weaknesses
 - The class-specific mask is essential in anchor learning, but there lacks visualizations on masks to show whether they correctly captured class-specific information.

- According to ablation study 5.3 (a), the contribution of anchor is not significant compared to mixup module, which doubts the effectiveness and necessity of anchor learning module. Here raises a question about why anchor learning is necessary and successfully selectively transfer teachers' knowledge.

- A related work [1] shared the similar motivation on the invalid IID hypothesis and the gap between teacher domain and student domain. Although the research problem is different ([1] focused on conventional KD while this work proposed OOD-KD), it would be more comprehensive if the comparison between this work and [Niu et al., NeurIPS 2022] can be discussed, especially on the above mentioned similarities on motivations, and how to selectively transfer teachers' knowledge.

### Questions
Please see Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
