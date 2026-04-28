# Enhancing Compositional Generalization via Compositional Feature Alignment

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Real-world applications of machine learning models often confront data distribution shifts, wherein discrepancies exist between the training and test data distributions. In the common multi-domain multi-class setup, as the number of classes and domains scales up, it becomes infeasible to gather training data for every domain-class combination. This challenge naturally leads the quest for models with Compositional Generalization (CG) ability, where models can generalize to unseen domain-class combinations. To delve into the CG challenge, we develop CG-Bench, a suite of CG benchmarks derived from existing real-world image datasets, and observe that the prevalent pretraining-finetuning paradigm on foundational models, such as CLIP and DINOv2, struggles with the challenge. To address this challenge, we propose Compositional Feature Alignment (CFA), a simple two-stage finetuning technique that i) learns two orthogonal linear heads on a pretrained encoder with respect to class and domain labels, and ii) fine-tunes the encoder with the newly learned head frozen. We theoretically and empirically justify that CFA encourages compositional feature learning of pretrained models. We further conduct extensive experiments on CG-Bench for CLIP and DINOv2, two powerful pretrained vision foundation models. Experiment results show that CFA outperforms common finetuning techniques in compositional generalization, corroborating CFA's efficacy in compositional feature learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the challenge of compositional generalization in machine learning and focuses on generalization to unseen domain-class combinations. The author present a real-world benchmark named CG-Bench and propose the compositional feature alignment method to improve the CG performance of pretrained models. Extensive experiments demonstate the effectiveness of the method.

### Strengths
S1: This paper solve a new setting or problem: can the model generalize to unseen domain-class combinations?

S2: The overall writing is clear, including problem introduction and theoretical and experimental verification of experimental methods.

S3: Some visualization experiments are shown to help the understanding of the review or reader.

### Weaknesses
W1: The setting of compositional generalization (CG) means that the pre-trained model is tested on the unseen domain-class combinations and the setting of domain generalization means that the pre-trained model is tested on the unseen domain samples? if yes, what is the difference between CG and some papers in open-set tasks to solve domain generalization problems?

W2: To solve the CG problem, the authors propose a method to align the class information in different domain. I'm more curious about why the two-stage training method can achieve this goal? If possible, I would tend to see experiments on each stage of visualization.

W3: I am more concerned about different training stages and ablation experiments related to orthogonal loss.

### Questions
see weaknesses

If the authors solve my concers, I tend to imporve my socre.

### Soundness
3 good

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
This paper tackles the challenge of data distribution shifts in machine learning applications. In particular, it emphasizes the multi-domain, multi-class setup where obtaining training data for every domain-class combination becomes impractical, and they try to examine the compositional generalization (CG) for learning models. The authors propose a simple solution in the form of CG and introduce "CG-Bench," a suite of CG benchmarks derived from real-world image datasets. They tested CLIP and DINOv2, and show the effectiveness of both the proposed benchmark and method.

---
# Post rebuttal

I appreciate the provided two solutions (lessen the need for a fully domain-labeled dataset). I encourage the author to incorporate all the discussion into their revision.

### Strengths
I personally believe the studied topic of compositional generalization is crucial in real-world machine learning applications, especially in scenarios with multi-domain, multi-class setups. The introduction of "CG-Bench" is commendable, providing the research community with a dedicated suite of benchmarks for evaluating CG performance.

The proposed two-stage process is clear and logically structured, with a rationale that suggests a theoretical underpinning for the method. I personally pretty like Figure 4 which provided a great comparisons between vanilla CLIP features and the features obtained by this paper.

### Weaknesses
It is hard to obtain the class and domain labels. Therefore, the studies in this paper are hard to scale-up to real world system. 

Based on Table 1, it seems the proposed method would usually cause negative effects to ID Acc.

### Questions
Besides, I feel the caption of Figure 2 could be improved to help reader understand the goal of the proposed method.

Please also address the concerns raised above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deals with the challenge of compositional generalization, which in detail is the generalization to unseen domain-class combinations. To this end, the paper proposes CG-Bench, a suite of CG benchmarks derived from existing real-world image datasets. Furthermore, Compositional Feature Alignment (CFA), a two-stage finetuning technique is proposed. Evaluation is performed on CG-Bench using CLIP and DINOv2 vision foundation models fine-tuned using the proposed CFA approach.

### Strengths
·         The paper is well written and easy to understand, e.g., Figure 2 is very useful for understanding the definition of Compositional Feature Structure.

·         The proposed method is novel and interesting, and it seems to work well in the case of datasets such as Color-CIFAR. The results in Figure 4 show that the learned features are disengaged across classes and domains.

·         The proposed CG-Bench compositional generalization benchmark is also novel and well-curated.

### Weaknesses
·         Theorem 1 holds only at the global minimum of the objective function (4). However, in practice when the features Z are from large neural networks such as CLIP the global minimum is unlikely to be obtained. In that case, features would likely not conform to the compositional feature structure defined in Definition 1. Therefore, it is unclear if Theorem 1 has any practical significance.

·         While the features seem to be disentangled in the case of the simple Color-CIFAR dataset as shown in Figure 2, it is not clear if the same effect can be observed in the case of more complex datasets such as DomainNet.

·         Stability of the model during training is not discussed in detail. This is important because of the complex two-stage training process. The paper should include experiments where the number of training steps in the first and second stage are varied and analyze the effect on the performance of the final model.

·         From the results in Table 1, the performance gain over the reweight strategy is minimal (<1%) for all datasets. The biggest performance gain comes from the use of WiSE-FT (Wortsman et al., 2022). Also, compared to the reweight strategy, the proposed approach uses 2-staged training. Therefore, it is not clear whether the increase in training complexity is justified by the small performance gain.

·         In Table 1, the reweight baseline with WiSE when using the DINOv2 model seems to be missing. Comparing reweighting and the proposed CFA method the gain in performance without WiSE seems to be <0.3%, especially in the case of OfficeHome and DomainNet.

·         Can the proposed approach take advantage of unlabeled data? This is important because prior work such as CLIP or DINOv2 does not need explicit domain/class labels, unlike the proposed CFA approach.

### Questions
·         For models trained using CFA, do we observe the disentanglement similar to Color-CIFAR in Figure 2 in case of larger datasets such as DomainNet?

·         Additional details of the reason for the small performance gain of the proposed CFA approach over the reweight baseline in Table 1 would be helpful.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
