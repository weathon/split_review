# Enhanced Label Propagation through Affinity Matrix Fusion for Source-Free Domain Adaptation

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Source-free domain adaptation (SFDA) has gained significant attention as a method to transfer knowledge from a pre-trained model on source domains toward target domains without accessing the source data. Recent research in SFDA has predominately adopted a self-training paradigm, focusing on utilizing local consistency constraints to refine pseudo-labels during self-training. These constraints encourage similar predictions among samples residing in local neighborhoods. Despite their effectiveness, the importance of global consistency is often overlooked. Moreover, such self-training-based adaptation processes suffer from the "confirmation bias": models use self-generated sub-optimal pseudo-labels to guide their subsequent training, resulting in a loop of self-reinforcing errors. In this study, we address the global consistency limitation by employing a label propagation method that seamlessly enforces both local and global consistency, leading to more coherent label predictions within the target domain. To mitigate the "confirmation bias", we propose utilizing an affinity matrix derived from current and historical models during the label propagation process. This approach takes advantage of different snapshots of the model to obtain a more accurate representation of the underlying graph structure, significantly enhancing the efficacy of label propagation and resulting in more refined pseudo-labels. Extensive experiments prove the superiority of our approach over the existing methods by a large margin. Our findings not only highlight the significance of incorporating global consistency within the SFDA framework but also offer a novel approach to mitigate the confirmation bias that arises from the use of noisy pseudo-labels in the self-training paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on source-free domain adaptation and proposes to utilize an affinity matrix derived from current and historical models during the label propagation process. The proposed method takes advantage of different snapshots of the model to obtain a more accurate representation of the underlying graph structure, significantly enhancing the efficacy of label propagation and resulting in more refined pseudo-labels. Extensive experiments show that the proposed method achieves superior domain adaptation performance, which does not require source domains.

### Strengths
-a. It incorporates label propagation to leverage both local and global relationships between the instances in the target domain for source-free domain adaptation.
- b. It investigates the critical role of data augmentation as a fundamental component in the self-training-based SFDA framework.
- c. The experiments are extensive, and the performance of the proposed method is promising in source-free domain adaptation scenario.

### Weaknesses
1. The proposed method seems a bit similar to HCL (Huang et al., 2021) which also exploits current and historical models for source-free domain adaptation. It would be better to discuss and compare the differences, pros and cons of HCL and the proposed method.
2. The proposed label propagation method seems similar the method of “Temporal Assembling for semi-supervised learning”. It would be better to discuss and compare the differences, pros and cons of this method and the proposed method.
3. The ablation study is not clear. Why the baseline in Table 4 outperforms the source model by a large margin? Do all the other methods in other tables use the same baseline as in Table 4?

### Questions
see Weaknesses

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach for source-free domain adaptation called Enhanced Label Propagation through Affinity Matrix Fusion. This approach is designed to enhance the quality of pseudo-labels in the target domain by synergizing the predictions of an old model with the current model. To achieve this, the method constructs an affinity matrix and employs label propagation techniques to refine pseudo-labels. These refined labels are then used to calculate gradients from an alternative augmentation perspective. Additionally, the approach incorporates a prediction diversity loss and leverages BN adaptation techniques. Experimental evaluations are conducted on popular datasets such as Office-31, Office-Home, and VisDA-C, yielding results that are comparable to state-of-the-art methods.

### Strengths
1. The paper is well written.
2. As stated by the authors, label propagation technology was originally employed for making predictions on unlabeled data in a semi-supervised setting. However, this paper introduces a novel application by using it to refine pseudo-labels.

### Weaknesses
1. This proposed method combines several previously established techniques, such as label propagation, consistent loss with two views, BN adaptation, and prediction diversity loss. It lacks novelty in terms of its technical components. It seems the sole innovation lies in applying label propagation technology for refining pseudo labels additionally using historical model outputs.
2. The experimental results show only a marginal advantage on Office-31 and Office-Home datasets.

### Questions
1. Why exclusively employ the previous model h_{t-m} instead of a fused model (such as \sum_{i=1}^{m} h_{t-i}) for retrieving historical information?
2. Is there a particular rationale behind the choice of the negative dot product loss as opposed to other commonly used loss functions? I couldn't find any ablation results in the paper.

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper proposes to leverage label propagation and self-supervised learning methods in SFDA (Source-Free Domain Adaptation) problem, aiming to obtain the global semantic information and reduce the confirmation bias in the target domain. Specifically, the authors use both historical model snapshots and the current model to build the affinity matrix and further adopt the label propagation technique to refine pseudo-labels for the target domain. Moreover, they also use batch normalization adaptation and self-supervised learning methods, including data augmentation, to improve their algorithm. The experimental results on several SFDA benchmarks verify the effectiveness of the proposed method.

### Strengths
- The paper is well-organized and easy to follow.
    
- The idea of introducing label propagation in SFDA is interesting. However, some recent works [1] also mentioned this research topic, which reduces the novelty of this paper.
    
- The proposed method is concise, and the experimental results are relatively promising.
    
 [1] Chunwei Wu, Guitao Cao, Yan Li, Xidong Xi, Wenming Cao, Hong Wang, “Chaos to Order: A Label Propagation Perspective on Source-Free Domain Adaptation.” ACM Multimedia 2023

### Weaknesses
 - My main concern with this paper is about the novelty. The proposed method has two main contributions: the label propagation technique and the self-training framework. Recently, the self-training and data augmentation methods have been widely used in SFDA research. And some recent papers also adopted the label propagation in SFDA [1,2]. There lacks some necessary discussions compared with the state-of-the-art works. Specifically, the paper does not adequately address how their label propagation differs from existing methods, particularly in the context of leveraging historical model information. The novelty of combining historical model information with label propagation is not clearly established, and the paper needs to provide a more detailed comparison with existing techniques that use similar concepts.
    
- I have some questions about the experimental part. Please refer to the Question section.

### Questions
I have some questions about the experimental part.

- To build your affinity matrix while using the historical models, should you save all previous affinity matrices and also the neighbor banks? Is this method of storage consuming and effective?
    
- By observing the curves in Fig 4 left panel, does this mean the utility of the fused affinity matrix will be continuously decreasing during the adaptation process?
    
- Also, in Figure 4, right panel, why, at epoch 0 (the initial step), are the ratios of two affinities not equal?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses source-free domain adaptation (SFDA) task, where a source pretrained model is adapted to an unlabeled target domain in the absence of the source data. The submission proposes to tackle the problem by label propagation, along with considering historical model embedding and introducing data augmentations.

### Strengths
- Motivation is clear and sound: The proposed method is based on label propagation, to deal with the noisy pseudo labels/predictions, historical feature embeddings are considered in the affinity matrix definition.

- Experiments on several benchmarks show the effectiveness of the proposed method.

### Weaknesses
 - Label propagation is already investigated in the normal domain adaptation [a] (and also source-free domain adaptation [b]), the authors may consider discussing those works in the related works section.


- One major improvement comes from data augmentations, which is a universal way to improve the performance in unsupervised learning. I think in the ablation study, results with Baseline + HAF should be provided on all datasets, to indicate how much improvement data augmentation could introduce into label propagation.

- (Major) Some techniques used in the submission are quite general and not new, such as BN statistics adaptation (which is achieved by forwarding target data to source model before starting adaptation), and uncertainty weight in Eq. 8 (and also diversity loss in Eq. 9). As there is no ablation study about those techniques, I posit they can improve all existing SFDA methods. For fair comparison, at least results without BN adaptation should be provided. Or BN adaptation should be added to all existing methods in the main tables, otherwise we do not know how many gains are really from label propagation, which is the key module in the submission.

- In the appendix, it mentions that there are two strong augmentations deployed, how about only using one or multiple ones in turn?

- The hyperparameter $\lambda$ is set manually (0.1 for office datasets and 0 for visda), how about the performance without using diversity loss, or using a decaying weight on this term?

### Questions
Please check the weakness above, without detailed ablation studies, currently I think the submission is a bit incremental by combining several general techniques.

By the way, I think the method is also somehow similar to BYOL. The label propagation part with weak augmentation could be regarded as the projection layer in BYOL, though the operation in the submission is in the output space (classification prediction). The authors could think about it.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
