# Intransigent Teachers Guide Better Test-Time Adaptation Students

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 3, 5

## Abstract
Test-Time Adaptation (TTA) has recently emerged as a promising strategy that allows the adaptation of pre-trained models to changing data distributions at deployment time, without access to any labels. To address the error accumulation problem, various approaches have used the teacher-student framework. In this work, we challenge the common strategy of setting the teacher weights to be an exponential moving average of the student by showing that error accumulation still occurs, but only on longer sequences compared to those commonly utilized. We analyze the stability-plasticity trade-off within the teacher-student framework and propose to use an intransigent teacher instead. We show that not changing any of the weights of the teacher model within existing TTA methods allows them to significantly improve their performance on multiple datasets with longer scenarios and smaller batch sizes. Finally, we show that the proposed changes are applicable to different architectures and are more robust to changes in hyper-parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an intransigent teacher (IT) based approach for continual test-time adaptation (TTA), where the teacher model is kept frozen, and only the student model updates. The aim is to alleviate the problem of error accumulation that is persistent in longer horizons of target domains.
Experimental results on longer horizons of corruption sequences demonstrate that IT helps improve performance in compared settings on multiple benchmarks.

### Strengths
* Experiment with different approaches that use losses, such as consistency and contrastive losses.
* Improving performance on longer horizons on multiple benchmarks

### Weaknesses
 * Limited novelty. EMA-based continual TTA approaches already have a hyperparameter that decides how much weightage to be given to the student model weights and updates the teacher weights as a linear combination. If the weightage to student model weights is extremely low, it is effectively an "intransigent teacher." The paper does not sufficiently explore the parameter space of existing EMA methods to justify the need for a completely frozen teacher.
* CoTTA [1] and PETAL [2] have already proposed a resetting mechanism that preserves source knowledge by resetting some weights back to the source pre-trained model. The paper does not adequately address how the proposed approach compares to these resetting mechanisms, especially in the context of long adaptation horizons where catastrophic forgetting can be a major issue. The lack of a comparative analysis with adaptive resetting strategies is a significant weakness.
* Repeated loops of the same data showing poor performance can also mean that the model is overfitting to each target domain and drifting away from source knowledge, which is suitable for all the target domains. Approaches such as CoTTA [1] and PETAL [2] have a resetting mechanism that consists of a threshold hyperparameter while resetting. Tuning this hyperparameter is essential for longer horizons using the validation corruption data. Otherwise, the comparison with baselines is not fair. The paper does not provide sufficient details on how the baselines were tuned, particularly the resetting hyperparameters, and lacks a discussion on the sensitivity of the results to these choices.
* The proposed approach is limited to EMA student-teacher models. The paper does not explore the applicability of the intransigent teacher concept to other TTA frameworks, which limits the generalizability of the findings.

### Questions
* If we refer to CoTTA paper [1] Equation 2 and its supplementary [2], \alpha (\beta in the submitted paper) can be put to 1, and it will effectively lead to an "intransigent teacher." Is this understanding correct? If so, what is the novelty of this paper, and why is it not just a trivial extension in terms of methodology?
* Is the paper simply not setting the \beta value to 1 and experiments around it?
* Is repeating the same corruption sequence multiple times realistic? If the paper claims intransigent teacher helps, there should be new benchmarks with longer horizons of corruption sequences, rather than repeating the corruption sequence.
* Tuning this hyperparameter is essential for longer horizons using the validation corruption data. Otherwise, the comparison with baselines is not fair. Have the authors tuned the hyperparameters for the baseline approaches? Also, was any validation corruption data used?

**References**
1. Qin Wang, Olga Fink, Luc Van Gool, and Dengxin Dai. Continual test-time domain adaptation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022
2. https://openaccess.thecvf.com/content/CVPR2022/supplemental/Wang_Continual_Test-Time_Domain_CVPR_2022_supplemental.pdf
3. Dhanajit Brahma, and Piyush Rai. A probabilistic framework for lifelong test-time adaptation. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the challenges of Test-Time Adaptation (TTA) and proposes to use a static (intransigent) teacher model, which does not update its weights during adaptation. The authors demonstrate that this modification enhances performance across multiple datasets characterized by longer sequences and smaller batch sizes. Additionally, they provide evidence that their proposed method is adaptable across various model architectures and exhibits robustness against changes in hyper-parameters.

### Strengths
1.  The "intransigent teacher" concept is a fresh perspective that challenges existing methodologies in TTA, potentially leading to improved performance in real-world applications, such as LLM applications.
2. The authors support their claims with experimental results across multiple datasets, demonstrating the effectiveness of their approach in diverse scenarios. The proposed method shows robustness to hyper-parameter variations. 
3. The proposed approach is simple and can be generalized across different architectures.

### Weaknesses
1. While the empirical results are compelling, the theoretical justification for why the intransigent teacher improves performance could be elaborated further to enhance the understanding of the underlying mechanisms.

2. The implications of using an unchanging teacher model over extended periods or across highly variable data distributions could be discussed more thoroughly, as this might lead to stagnation in learning.

### Questions
See the weaknesses for details.

### Soundness
3

### Presentation
3

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
An interesting phenomenon found in the paper is that the intransigent teacher model is able to guide a more stable student model in long sequences of CTTA tasks. From the conclusions in the paper, it is clear that this approach can be applied to all methods of the mean-teacher architecture.

### Strengths
The phenomenon observed in the paper does to some extent replace the current method of the mean-teacher architecture and can achieve better results in long sequences of CTTA tasks.

### Weaknesses
The text lacks critical experimental and theoretical proofs and does not present targeted methods and analyses.

Limitations：
1. The paper does not provide a detailed analysis, but is only based on experimentally observed phenomena, and it is not possible to determine the specific reasons for the decline in generalizability of the teacher model, nor does it give a specific analysis of the decline in generalizability performance of the teacher model.
2. Why the intransigent teacher model outperforms the EMA updated teacher model in the long sequence CTTA task, relying only on experimental comparisons is not convincing.
3. Is the Intransigent teacher model just setting β to 1? How is this different from freezing the model? Is it understood to always use the source model as the teacher model? If so, it is no longer considered to be a mean-teacher framework.
4. Should the teacher model be locked in any scenario? It is suggested that the authors consider a scenario where the weights of the teacher model are dynamically adjusted, which might achieve better results.
5. Based on the phenomena you observed, the paper doesn't seem to suggest any targeted approach? Does this imply that you are just using the source model as a teacher model? I don't see any relevant methods in the source code either.
6. Although comparisons were made on three methods in the paper, the paper should have added more comparison experiments with the Mean-Teacher architecture method. Also, the authors need to provide segmentation experiments to further demonstrate the effectiveness of their proposed approach.

### Questions
See the weakness.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper challenges the existing teacher-student framework in test-time adaptation (TTA), where lifelong adaptations showed inevitable performance degradation. The paper proposes an intransigent teacher, which does not update the parameters but only uses test batch statistics. The intransigent teacher showed high stability in lifelong adaptation while improving performance compared to the original teacher-student-based methods.

### Strengths
- Writing is clear, comprehensive, and easy to understand.

- Proposed a simple yet effective solution for the practical scenario of lifelong adaptation.

- Extensive large-scale evaluations on various datasets/scenarios and state-of-the-art baselines.

### Weaknesses
 - The problem (model failures in lifelong adaptation) has already been discussed in RDumb, so the problem setting itself is not novel.

- The method only applies to existing teacher-student methods, thus limiting its applicability. At the same time, the intransigent teacher does not consistently outperform the baselines (e.g., RDumb in BS=64) or prevent failures (e.g., results in BS=10). Furthermore, the intransigent teacher (IT) shows significant accuracy drops in some cases, such as the ImageNet-C/R experiments, where CoTTA with stochastic reset experiences a 17.4%/11.0% reduction in accuracy when using IT. This raises concerns about the general applicability of the IT approach, especially given the importance of ImageNet-C as a benchmark. The fact that IT can degrade performance compared to a well-tuned baseline questions its necessity in all scenarios.


### Questions
- Please discuss the advantages/disadvantages of the proposed intransigent teacher compared to the important lifelong baseline, RDumb.

- Can we dynamically adjust the plasticity ($\beta$) to climb up to 1 (e.g., using the TTA accuracy estimation metrics [a, b] or using a fixed period)?

- Would this phenomenon also occur in non-corrupted lifelong test streams?

- Reporting single-pass results (akin to the original TTA setup) would help understand the performance compared to existing TTAs.

- (Minor) Typo: Page 8, Line 423: COTTA -> CoTTA

---

[a] Lee, Taeckyung, et al. "AETTA: Label-Free Accuracy Estimation for Test-Time Adaptation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[b] Kim, Eungyeup, et al. "Reliable Test-Time Adaptation via Agreement-on-the-Line." arXiv preprint arXiv:2310.04941. 2024.

### Soundness
3

### Presentation
4

### Contribution
2
