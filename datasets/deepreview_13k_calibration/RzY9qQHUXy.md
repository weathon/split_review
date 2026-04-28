# Kill Two Birds with One Stone: Rethinking Data Augmentation for Deep Long-tailed Learning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 6, 8

## Abstract
Real-world tasks are universally associated with training samples that exhibit a long-tailed class distribution, and traditional deep learning models are not suitable for fitting this distribution, thus resulting in a biased trained model. To surmount this dilemma, massive deep long-tailed learning studies have been proposed to achieve inter-class fairness models by designing sophisticated sampling strategies or improving existing model structures and loss functions. Habitually, these studies tend to apply data augmentation strategies to improve the generalization performance of their models. However, this augmentation strategy applied to balanced distributions may not be the best option for long-tailed distributions. For a profound understanding of data augmentation, we first theoretically analyze the gains of traditional augmentation strategies in long-tailed learning, and observe that augmentation methods cause the long-tailed distribution to be imbalanced again, resulting in an intertwined imbalance: inherent data-wise imbalance and extrinsic augmentation-wise imbalance, i.e., two 'birds' co-exist in long-tailed learning. Motivated by this observation, we propose an adaptive Dynamic Optional Data Augmentation (DODA) to address this intertwined imbalance, i.e., one 'stone' simultaneously 'kills' two 'birds', which allows each class to choose appropriate augmentation methods by maintaining a corresponding augmentation probability distribution for each class during training. Extensive experiments across mainstream long-tailed recognition benchmarks (e.g., CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018) prove the effectiveness and flexibility of the DODA in overcoming the intertwined imbalance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper makes a theoretical analysis of data augmentation strategies in long-tailed learning and points out that there may be a variety of potential interweaving imbalances in long-tailed learning, such as class and augmentation. The author further proposes a dynamic optional augmentation strategy to alleviate the above imbalance problem from a new perspective. The proposed method is tested on different main-stream long-tailed datasets, including dealing with imbalance problems and augmentation problems. The comparison with existing methods shows the superiority of the proposed method.

### Strengths
1. The motivation proposed in this paper on how to choose suitable data augmentation for different classes is practical, which innovates the traditional way of long-tailed learning.
2. The theoretical analysis is sufficient, and the author has analyzed the potential risks of data augmentation in long-tailed learning. The explanation that data augmentation may bring hypocritical performance improvements is interesting.
3. This paper conducted a large number of comparative experiments with methods of different tendencies on mainstream benchmarks, including analysis at different levels. The results can demonstrate the effectiveness of this method.
4. This paper is well written, and the dynamically optional method proposed is easy to understand. In particular, the visualization of the training process allows me to have a more intuitive understanding.

### Weaknesses
1. My main question or weakness is that although the author has conducted analysis and verification in the traditional long-tailed learning field, the long-tailed distribution may not only exist in the visual field, and some other fields (e.g., graph cls.) seem to have the same problem. This paper lacks a discussion on the scalability of the proposed method.
2. Section 4.3 mentions that 'DODA can avoid more classes being sacrificed', but it seems that this cannot be intuitively found based on Figure 4.

### Questions
1. It would be beneficial if the author could provide a brief explanation or discussion on the scalability of the proposed method, which could promote its application in other open scenarios.
2. Regarding Section 4.3, the authors mention that DODA can avoid more classes being sacrificed. However, it may not be intuitive to find this based on Figure 4. Therefore, it would be helpful if the author could provide a more detailed explanation of the model's effect, which would allow others to better understand the improvements brought about by this method.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the problem of imbalance in existing data augmentation techniques in long tailed learning. This paper proposes to improve this by introducing a dynamic augmentation strategy - DODA (Dynamic Optional Data Augmentation) to reinforce well-performing augmentation strategies and punish the inefficient ones during training. The authors claim that this method kills two ‘birds’ - inherent data imbalance and extrinsic augmentation wise imbalance with one ‘stone’.

### Strengths
The work addresses the problem of long tailed learning from a data augmentation perspective and shows potential for huge gains by simply using augmentations efficiently without much computational overhead.

The paper has a simple writing style and is easy to read and follow.

### Weaknesses
 **Proposed Method**

a) The proposed method for DODA is exclusively used where augmentations  are solely for one single class and do not encourage inter class interaction. Augmentation methods such as mixup and its improved version Remix (Chou et al. 2020) have proven to be efficient in data-imbalance settings. However, comparison of the proposed method with Remix + LTL methods is lacking. Specifically, the paper does not explore how DODA would perform when combined with inter-class augmentation strategies like Remix, which could potentially offer complementary benefits. The current implementation limits the scope of DODA by focusing solely on intra-class augmentations, missing opportunities for more comprehensive data augmentation strategies.

The algorithm optimizes the augmentation strategy on 10 predefined augmentation functions with fixed strengths. The authors should discuss the optimality of the selection of these functions and provide ablation studies for the same. The choice of these 10 augmentations appears arbitrary without a clear justification for why these particular transformations were selected. Furthermore, the fixed strengths of these augmentations may not be optimal for all classes or datasets, and the paper lacks any exploration of how different augmentation strengths would impact the performance of DODA. An ablation study varying the number and type of augmentations, along with their strengths, is needed to validate the robustness of the proposed method.

**Missing Baselines **

The effectiveness of DODA on state-of-the-art long-tailed methods PaCo [R1], and NCL[R2] is not demonstrated in the paper. It would be great if the results are provided in the rebuttal. The lack of evaluation on these methods makes it difficult to assess the true potential of DODA in comparison to existing state-of-the-art approaches. The paper needs to demonstrate that DODA can provide improvements over these methods, not just on simpler baselines.

[R1] Cui, Jiequan et. al. “Parametric Contrastive Learning”, Proceedings of the IEEE/CVF international conference on computer vision, 2021. 

[R2] Li, Jun et. al. “Nested Collaborative Learning for Long-Tailed Visual Recognition”. Proceedings of the IEEE/CVF international conference on computer vision, 2022.

### Questions
For contrastive methods such as BCL, how is DODA being used to generate multiple views of the same image for different classes?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Data augmentation (DA) is one of the strategies employed to address the dataset imbalance issue in long-tailed classification. This paper proposes the DODA algorithm based on the premise that in situations handling long-tailed datasets, the effectiveness of DA may vary for each class. In a nutshell, the proposed algorithm includes setting up a set of DAs and adjusting the preferences for each augmentation individually for each class during the training process. The paper offers experimental findings for CIFAR-LT, ImageNet-LT, and iNaturalist-2018.

### Strengths
1. The provided problem regarding data augmentation in long-tailed classification has a well-established and clear motivation.
2. Comprehensive experimental outcomes are presented, encompassing a range of existing training approaches and data augmentation techniques for addressing long-tailed classification.

### Weaknesses
1. The straightforward yet most important baseline is missing. The central idea presented in this paper is that there are both positive and negative DA effects specific to each class when working with long-tailed datasets, and it is beneficial to adjust them during the training process through the proposed DODA algorithm. Consequently, keeping the per-class weight distribution $\mathfrak{Q}_c$ fixed as a uniform distribution in the proposed DODA algorithm would serve as an essential baseline, which highlights the efficacy of the proposed adjusting approach. One can interpret the performance improvement described in the paper as simply due to the incorporation of extra data augmentation.

2. While the main tables present average values, the standard deviations are missing; it would be better to provide complete results, including standard deviations, in the appendices.

### Questions
1. Could you provide some valuable insights regarding the decline in performance that we see in the RIDE column of Table 1?
2. UniformAugment (LingChen et al., 2020) is a suitable baseline for comparison because of its straightforward application of a set of augmentations at random. It would be nice to see the UniformAugment baseline results.
3. It seems that the proposed methodology could be effective even in scenarios handling balanced datasets. Have you experimentally verified this by any chance?
4. ’its’ in the caption of Figure 6; quotation mark issues in LaTeX :)

---
LingChen et al., 2020, UniformAugment: A Search-free Probabilistic Data Augmentation Approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study focus on data augmentation for long-tailed learning. First, the authors theoretically analyzes that the traditional data augmentation techniques cause  the long-tailed distribution to be imbalanced again. Specifically, the traditional data augmentation techniques cause inherent data-wise imbalance and extrinsic augmentation-wise imbalance, which are called as two birds in this paper. To kill the two birds, the authors propose an data augmentation technique termed DODA which make each class to choose appropriate augmentation methods. Experimental results on 4 benchmark datasets verify effectiveness of the DODA.

### Strengths
Code is submitted.

Many studies are reviewed in the Appendix.

The paper is easy to read.

Theoretical ground for the proposed algorithm.

Extensive experiments are conducted with 4 benchmark datasets.

Detailed analyses for the superiority of the proposed algorithm are provided.

The proposed algorithm can be orthogonally used with other long tailed learning algorithm such as LDAM and RIDE.

### Weaknesses
I cant find weakness of this paper.

### Questions
I have no question.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
