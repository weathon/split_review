# Improving Robustness and Accuracy with Retrospective Online Adversarial Distillation

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Adversarial distillation (AD), transferring knowledge of a robust teacher model to a student model, has emerged as an advanced technique for improving robustness against adversarial attacks. However, AD in general suffers from the high computational complexity of pre-training the robust teacher, and the inherent trade-off between robustness and natural accuracy (i.e., accuracy on clean data). To address these issues, we propose retrospective online adversarial distillation (ROAD). ROAD exploits the student itself of the last epoch and a natural model (i.e., a model trained with clean data) as teachers, instead of a pre-trained robust teacher in the conventional AD. We revealed both theoretically and empirically that knowledge distillation from the student of the last epoch allows to penalize overly confident predictions on adversarial examples, leading to improved robustness and generalization. Also, the student and the natural model are trained together in a collaborative manner, which enables to improve natural accuracy of the student more effectively. We demonstrate by extensive experiments that ROAD achieved outstanding performance in both robustness and natural accuracy with substantially reduced training time and computation cost.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents ROAD, an adversarial self-distillation approach designed to tackle over-confidence issues and improve the tradeoff between clean and robust accuracy of robust models in Adversarial Training (AT). The method moderates over-confidence by generating soft labels for adversarial examples, merging predictions from the last epoch model with the original hard labels. Additionally, to maintain clean accuracy, a regularizer is introduced that aligns the predictions of the robust model with those of a natural model on clean samples. Experimental results exhibit superior performance on both natural accuracy and robustness compared with both AT and Adversarial Distillation (AD) methods among various evaluated scenarios.

### Strengths
S1: This paper primarily focuses on adversarial self-distillation, a promising avenue for future adversarial machine learning research due to its lower resource demands compared to AD.

S2: This paper introduces a simple yet effective framework that excels in both natural accuracy and robustness for adversarial self-distillation. The exhibited experimental results also partially reveal the ineffectiveness of existing AD methods under this scenario.

### Weaknesses
W1: Certain key aspects of the presented theory in Section 3.1.1 appear ambiguous from my vantage point. The authors attempt to convince that the soft label proposed in Equation 1 can prevent the model’s predictions from becoming overly confident because the proposed soft label can implicitly provide smaller weights to adversarial samples which have a drastically increased confidence. The authors prove this by demonstrating the norm of the gradient of the loss w.r.t the output logits $ \frac{\partial \mathcal{L}}{\partial z_{t, i}^{\prime}} $ obtained with the proposed soft label will become smaller than that obtained with the original hard label if the confidence of the model output for $x\prime$ increases in this epoch. However, existing works generally propose to constrain a relatively larger norm of gradient $\frac{\partial \mathcal{L}}{\partial \theta_{t}} $ [1] to mitigate the overconfidence issue. It appears that the authors do not provide sufficient proof that the effect of the introduced gradient norm scaling factor w.r.t to the logit also works for the gradient w.r.t to the model weights $\theta$.

W2: Several statements presented in Section 3.2 are deemed to be either inaccurate or not adequately substantiated. For example, the referenced studies do not specifically support the claim that 'distilling knowledge from the static natural teacher may impair robustness.' It is strongly advised that the structure and argumentation of this section be thoroughly revised for clarity and accuracy.

W3: The logical progression within Section 3 is obscure, and the transitions between subsections lack fluidity, challenging the reader's ability to discern the author's objectives. Furthermore, the exposition accompanying Equation 3 falls short of providing sufficient elucidation or the underlying intuition for introducing the Robustness Enhancement term in the construction of the final objective function.

### Questions
Q1: Considering Weakness W1, does the proof presented in Section 3.1.1 extend to ensuring that adversarial samples, which induce a significantly larger gradient norm with respect to the model weights $\theta$, can also be effectively penalized?

Q2: Because the paper appears to lack a comprehensive exploration of the tuning strategy of the hyperparameter $\lambda$ introduced in Equation 1, could you elucidate on the potential effects of employing a constant value for $\lambda$, or linearly increase the value of $\lambda$ instead of using the sine increasing schedule?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel method called "Retrospective Online Adversarial Distillation" (ROAD) to improve the robustness of Deep Neural Networks (DNNs) against adversarial attacks while also maintaining high natural accuracy (accuracy on clean data). Unlike conventional Adversarial Distillation (AD) methods which involve training a robust teacher model and then transferring the knowledge to a student model, ROAD utilizes the student model from the last epoch and a natural model (trained with clean data) as teachers.

### Strengths
1. the idea of extending from distillation to self-distillation is very natural and expected to work out well. 

2. the idea of the asymmetry between how robust model and natural model influences each other is also very interesting, although the choices do not seem to be sufficiently discussed. 

3. the model achieves reasonably good empirical performances.

### Weaknesses
1. the paper involves several interesting design that collaboratively contribute to strong performances, thus a more detailed ablation study (more than the one the authors offered) is probably necessary, for examples
    - why is the asymmetry of how robust model and natural model influence each other is necessary? The current ablation study only touches briefly on the removal of these losses. However, since the authors emphasized on this asymmetry, it will be quite essential to discuss what if we use the same way of how these models influences each other. For example, what if we use soft labels from natural model also, or what if when we train the natural models, we use KL regularization also. Specifically, the paper should investigate the effect of using a symmetric knowledge transfer method, where the natural model receives knowledge via KL-divergence similar to standard online distillation. Additionally, it would be beneficial to quantify the impact of using a hyperparameter, similar to the $\gamma$ used for the robust model, to regulate the KL-divergence term when transferring knowledge to the natural model. This would provide a more comprehensive understanding of the role of asymmetric knowledge transfer in the proposed method.

2. The "LS" method does not seem to ever get spelled out, thus very hard to evaluate the relevant discussions. The paper cited is not immediately about the topics discussed in this paper. 
    - As a result, I do not see how "Effects on utilizing last epoch predictions" in ablation study is relevant. It is difficult to understand the significance of the "Effects on utilizing last epoch predictions" section in the ablation study without a clear definition of the "LS" method. A more detailed explanation of this method and its connection to the overall framework is needed to properly assess the relevance of this part of the ablation study.

3. the current ablation study in Figure 4 seems to suggest that self-distillation does not matter that much, a major performance boost comes from the natural model part, which seems quite counter-intuitive. It could be helpful if the authors explain more about this. Specifically, it would be valuable to see a more direct comparison between the performance with and without self-distillation, keeping all other factors constant. This would help isolate the specific contribution of self-distillation to the overall performance.

### Questions
1 the current ablation study in Figure 4 seems to suggest that self-distillation does not matter that much, a major performance boost comes from the natural model part, which seems quite counter-intuitive. It could be helpful if the authors explain more about this. 

2. in table 1 and 2, it will be helpful to have a natural model for references.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a novel technique designed to address the challenges inherent in balancing the trade-off between robust accuracy and natural accuracy while considering the computational overhead associated with adversarial distillation methods. The proposed method, referred to as ROAD, introduces a single-step training approach that incorporates self-distillation, employing the previous epoch's network as the teacher model. Additionally, a natural model is concurrently trained to provide guidance in the context of natural images, thus enhancing the aforementioned trade-off. ROAD leverages the utilization of soft-labels to penalize overconfident predictions, fostering collaborative learning.

### Strengths
- The paper addresses an important topic in the adversarial training domain.
-  It is well written and easy to follow. The algorithms and methodology is well explained
- The results cover three different networks and attacks (including AA)

### Weaknesses
 **Motivation:**
The assertion positing that overconfidence serves as a factor impeding the generalization capacity of robust models, as detailed in Section 3.1.1, warrants substantiation through references or empirical analysis within an AT context. It remains unclear how the resolution for penalizing overconfident predictions is incorporated via the utilization of soft labels.

It is worth noting that self-distillation has already demonstrated its efficacy in numerous studies pertaining to supervised and adversarial training methods. These approaches often involve the utilization of a prior model's time-stamp or an Exponential Moving Average (EMA) model for the purpose of regularization. Furthermore, online collaborative training has been well-established in the existing literature, e.g. ACT [2] and CAD [4] among others. The incorporation of soft labels and label-smoothing techniques in AT is studied, so it's somewhat perplexing, as their novelty is not readily apparent.

**Complexity:**

- The ROAD method still maintains two separate networks.
- It necessitates the retention of an additional copy of the network (from the last epoch) in GPU memory and, in aggregate, entails three supplementary forward propagation steps.

**Baselines:**

- The paper appears to lack references to several relevant baselines, encompassing both new and established methods [1-4].
In particular, the omission of comparative data with respect to collaborative and online distillation training techniques, such as ACT and MAT, is noteworthy. Moreover, the results of these techniques in the paper do not match those from the baseline references [1], specifically as presented in Table 3. The paper briefly mentions IAD but fails to provide a comparative analysis of its results.
- Further inconsistencies arise from comparisons with the RSLAD paper, wherein the AA and other attack-related metrics appear to surpass the corresponding figures reported in the ROAD paper. Similar discrepancies are apparent in the case of SEAT results.
- A comprehensive evaluation of the ROAD method would ideally encompass additional benchmarks, including but not limited to Weight Averaging [5] and AWP [6].

### Questions
- The related works section requires an update, incorporating more relevant and recent works.
- Please review the baseline models and consider adding more baselines (check the previous section for reference).
- In Section 3.1.2, the RSLAD also utilizes soft labels. Can we access the reliability diagram for it and obtain further information about the differences between these two methods?
- In Section 3.3, the second term of the objective function resorts to TRADES (involving the KL loss between robust and natural accuracy). Is this necessary when a separate model exists solely for natural images?
- The hyperparameter lambda is based on a hypothesis (that robust models are substantially poor in natural accuracy at early stages of training, as discussed in Section 3.2). Can we see some supporting evidence or results for this hypothesis? Ablations with different schedules for lambda to evaluate its impact on the results would be beneficial.
- Is the primary improvement stemming from the natural model, self-distillation, or solely from soft-labels? Further ablation experiments are necessary by removing each component individually.
- In Figure 4, does the orange line include guidance from the natural model with one-hot labels? What are the results when both self and natural model guidance objectives are replaced with one-hot labels?
- In Section 4.5, the computational cost should be compared with other online distillation methods.
- In Figure 5 (a) and (b), is the observed effect due to gamma or lambda? Why is there a significant difference between the CIFAR-10 and CIFAR-100 datasets? Hyperparameters should ideally not be highly sensitive to datasets and settings to develop more generalizable solutions.
- clarification and explanation of the differences between various concepts related to label smoothing

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the adversarial robustness via model distillation and proposes retrospective online adversarial distillation,  which exploits the student itself of the last epoch and a natural model as teachers to guide target model training. The paper proves the effectiveness of the proposed method through experiments and provides theoretical analysis.

### Strengths
1. The proposed method is single-stage adversarial distillation, but this is not the first time.
2. The authors provide a theoretical and experimental analysis of the label for robust overfitting.

### Weaknesses
1. The proposed method is single-stage adversarial distillation, but this is not the first time.
2. The authors provide a theoretical and experimental analysis of the label for robust overfitting.

1. The novelty of this paper is insufficient. It is highly overlapped with previous work, such as the use of soft labels, which was explored in the previous work [1]. Secondly, the use of online training methods was explored in the work of [2], and the use of natural models as teacher was explored in [3].

2. Lack of ablation experiments, such as the impact of natural models, and the selection of robust models (different checkpoints)

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
