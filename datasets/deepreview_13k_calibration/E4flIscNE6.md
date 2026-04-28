# Meta-Collaboration in Distillation: Pooled Learning from Multiple Students

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Knowledge distillation (KD) approximates a large teacher model using a smaller student model. KD can be used to train multiple students of different capacities, allowing for flexible management of inference costs at test time. We propose a novel distillation method we term meta-collaboration, wherein a set of students are simultaneously distilled from a single teacher and can improve each other through information sharing during distillation. We model this information sharing through a separate network designed to predict instance-specific loss mixing for each of the students. This auxiliary network is trained jointly with the multi-student distillation, utilizing a separate meta-loss aggregating student model loss on a separate validation set. Our method improves student accuracy for all students and beats to state-of-the-art distillation baselines, including methods that use multi-step distillation, combining models of different sizes. In particular, addition of smaller students to the pool clearly benefits larger student models, through the mechanism of meta-collaboration. We show average gains of 2.5\% on CIFAR100 \& 2\% on TinyImageNet datasets; our gains are consistent across a wide range of student sizes, teacher sizes, and model architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework for distilling the knowledge from a pretrained teacher to multiple students simultaneously. It uses a trainable network to learn the cross-entropy and KL-divergence weights for the K students. This trainable network is trained with a bi-level optimization strategy. The K students are also supervised by the PooledStudent logits. Experiments show promising results.

### Strengths
1. This paper is clearly written.
2. Distilling a pertained teacher to multiple students simultaneously is an interesting question.

### Weaknesses
1. The novelty looks incremental. It looks to me that the paper combines offline KD and online KD by training multiple students simultaneously while learning the loss weights with the meta-learning strategy (bi-level optimization).
2. Only two small datasets CIFAR-100 and tiny-ImageNet are used.
3. More comprehensive ablation studies about the weight-learning strategy (e.g., C-NET) and the PooledStudent logits should be conducted. Specifically, the paper lacks a thorough analysis of how the learned weights from C-NET compare to simpler, manually set weighting schemes. Furthermore, the rationale for using PooledStudent logits as supervision remains unclear, and the paper does not sufficiently explore the impact of this choice on the overall performance.

### Questions
1. It misses some ablation studies to show how the learned weights by C-NET are better than other weight strategies, e.g., manually set.
2. Why use PooledStudent logits as the supervision? Theoretical or empirical explanation is supposed to be provided.
3. Experiments on large-scale datasets, e.g., ImageNet, should be reported.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a distillation method called meta-collaboration, where multiple student models of different capacities are simultaneously distilled from a single teacher model. The students improve each other through information sharing during distillation by a C-Net module. The method outperforms compared distillation baselines.

### Strengths
1) The proposed method is evaluated on a wide range of student and teacher architectures, as well as model sizes.
2) The paper is well-written and effectively communicates the key ideas, methodology, and experimental results. The organization of the paper is logical.
3) The paper provides detailed implementation details and code, which is easy to reproduce.

### Weaknesses
1) The novelty is limited in my view. This work follows the widely used online distillation framework, except that the proposed C-NET part is trained with meta-learning. There are no clear improvements to the framework. The core idea of using a meta-learned network to dynamically adjust distillation weights based on input instances is not entirely novel, and the paper doesn't sufficiently highlight the specific advantages of their approach over existing methods that use similar dynamic weighting strategies. The improvement over standard online distillation seems marginal, and the specific contribution of meta-learning in this context needs further clarification.
2) The experiments are only conducted on small datasets (CIFAR100, TinyImageNet). The author is encouraged to evaluate your method on a large dataset like ImageNet-1K. This limits the generalizability of the findings. The performance on small datasets might not translate to larger, more complex datasets where the relationships between teacher and student models could be different. The lack of evaluation on ImageNet-1K, a standard benchmark, makes it difficult to assess the practical impact of the proposed method.
3) Limited evaluation and ablation studies on modern high-performance CNN architectures such as ConvNext[1], VAN[2], and RepLKNet[3]. The paper should include experiments with these architectures to demonstrate the robustness of the approach. The current evaluation is limited to relatively older architectures, and it's unclear how the proposed method would perform with more recent and powerful models. The absence of ablation studies on the C-Net architecture and its meta-learning process also makes it difficult to understand the contribution of each component.
4) Can you provide further theoretical analysis or insights into how the meta-collaboration process influences the learning patterns of the student models?

### Questions
Please refer to weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to adopt multiple students with different model architectures and a single pre-trained teacher. \
To fully utilize the multiple students, they devise C-net and consensus regularization.

### Strengths
1. The motivation is sound.
- models with different architecture learn different knowledge, and therefore, could be beneficial for KD.

2. The proposed C-Net and its training process are novel.
- meta-learning with bilevel optimization is straightforward.

### Weaknesses
1. Critical missing related work on bidirectional knowledge distillation with multiple models. 
[A]  Deep mutual learning. CVPR'18 
[B]  Dual learning for machine translation. NeurIPS'16 
[C]  Bidirectional Distillation for Top-K Recommender System, WWW'21 
and on consensus learning with heterogeneous models.  
[D] Consensus Learning from Heterogeneous Objectives for One-Class Collaborative Filtering, WWW'22

These existing works, especially [A] and [C] should be compared theoretically and empirically in the manuscript.

2. In Eq.7, in my opinion, the optimization of $\phi$ should be the outer loop, since Eq.7 is the optimization for C-Net

### Questions
1. Please refer to Weaknesses

2. In Eq.7, in my opinion, the optimization of $\phi$ should be the outer loop, since Eq.7 is the optimization for C-Net

### Soundness
3 good

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
This paper proposes a new method for training multiple student models simultaneously, called meta-collaboration, which improves student accuracy for all students and beats state-of-the-art distillation baselines. The method allows for flexible management of inference costs at test time and can be applied to various datasets and model architectures. The authors demonstrate the effectiveness of their approach on CIFAR100 and TinyImageNet datasets and show that it outperforms other distillation methods.

### Strengths
1. This paper presents a relatively comprehensive experiment, including multiple datasets and many teacher-student pairs.

2. This paper is well-written and easy to understand, with clear explanations of the proposed method and experimental results.

### Weaknesses
While the idea of meta-learning for multi-teacher KD has potential, the claims require more empirical and analytical support. Broader experimentation, justification of design choices, and engagement with relevant studies would help validate the work's novelty and significance.

1. Lack of novelty:

While multi-teacher distillation is not a new idea, the paper claims to introduce a meta-learning approach to optimize the weights of different teachers. Direct comparisons to related work like AEKD (NeurIPS2020)  that uses optimization methods are missing. More discussion is needed to justify the claims of novelty. Also, meta-optimization is very difficult to implement and not very effective. Currently meta-optimized distillation is generally ineffective or difficult to reproduce

2. Lack of thorough evaluation:

The evaluation on small datasets is insufficient. Following KD work norms, it should test on large-scale datasets like ImageNet and report downstream transfer learning results. The choice of teacher-student pairs could be better motivated by discussing alternatives like lightweight networks.

3. Lack of discussion on relevant studies:

To properly situate this work in the rapidly advancing KD literature, it needs to discuss closely related recent papers [1,2,3,4,5,6] like those pointed out. These address self-supervised KD, representation matching, offline-online transfer, architecture search for distillation, and automated KD - all highly pertinent topics the paper does not engage with. A more comprehensive literature review would strengthen the paper.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
