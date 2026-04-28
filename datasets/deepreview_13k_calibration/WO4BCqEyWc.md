# Augmentation-aware Self-Supervised Learning with Conditioned Projector

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
\vspace{-0.25cm}
Self-supervised learning (SSL) is a powerful technique for learning 
from unlabeled data. By learning to remain invariant to applied data augmentations, methods such as SimCLR and MoCo can reach quality on par with supervised approaches. 
{However, this invariance may be detrimental for solving downstream tasks that depend on traits affected by augmentations used during pretraining, such as color.}
In this paper, we propose to foster sensitivity to such characteristics in the representation space by modifying the projector network, a common component of self-supervised architectures. Specifically, we supplement the projector with information about augmentations applied to images. For the projector to take advantage of this auxiliary conditioning when solving the SSL task, the feature extractor learns to preserve the augmentation information in its representations. Our approach, coined \textbf{C}onditional \textbf{A}ugmentation-aware \textbf{S}elf-\textbf{s}upervised \textbf{Le}arning (\our{}), is directly applicable to typical joint-embedding SSL methods regardless of their objective functions. Moreover, it does not require major changes in the network architecture or prior knowledge of downstream tasks. In addition to an analysis of sensitivity towards different data augmentations, we conduct a series of experiments, which show that \our{} improves over various SSL methods, reaching state-of-the-art performance in multiple downstream tasks.\footnote{\href{https://sslneurips23.io/paper_pdfs/paper_6.pdf}{A short version of this paper} appeared at the \href{https://sslneurips23.io}{NeurIPS 2023 Workshop: Self-Supervised Learning - Theory and Practice}. \href{https://www.sciencedirect.}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Many self-supervised learning methods aim to learn augmentation-invariant representations. Such an approach could be harmful when a downstream task is sensitive to augmentation-aware information. To overcome this limitation of existing SSL methods, this paper proposes a simple yet effective approach that injects augmentation information (i.e., augmentation parameters) into the projection MLP used in the SSL framework. The approach shows superior performance over existing augmentation-aware information learning methods on ImageNet-100 experiments.

### Strengths
- This paper is generally well-written. It is easy to understand.
- The idea is simple, intuitive, and seems to be widely applicable.
- The proposed method, CASSLE, outperforms baselines (LooC, AugSelf, and AI) that also learn augmentation-aware information.

### Weaknesses
 **(1) Lack of comparison with recent augmentation-free SSL methods.** 
Recently, there have been proposed many augmentation-free self-supervised learning methods, including data2vec [1-2], I-JEPA [3], and Masked Image Modeling (MIM) [4-5]. The augmentation-free SSL methods do not use augmentation, in other words, they aim to learn full information about original images, rather than learning augmentation-invariant representations. Also, since they are often better than MoCo-v2 and SimCLR in various benchmarks (e.g., linear evaluation, fine-tuning, scalability), the authors should compare the proposed method with the methods. The lack of comparison with these methods makes it difficult to assess the true contribution of the proposed method in the broader landscape of self-supervised learning. It is crucial to understand if the proposed approach offers any advantages over methods that do not rely on augmentations at all, especially given the recent successes of these augmentation-free techniques.

[1] Baevski et al., data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language, ICML 2022 
[2] Baevski et al., Efficient Self-supervised Learning with Contextualized Target Representations for Vision, Speech and Language, 2022 
[3] Assran et al., Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture, ICCV 2023 
[4] He et al., Masked Autoencoders Are Scalable Vision Learners, CVPR 2022 
[5] Xie et al., SimMIM: a Simple Framework for Masked Image Modeling, CVPR 2022

**(2) Experimental results are not convincing.** 
The performance improvement of CASSLE over AugSelf is marginal. The reported improvements, while present, do not demonstrate a substantial leap in performance, raising questions about the practical significance of the proposed approach. The gains seem inconsistent across different experimental settings, further weakening the claim of its superiority. A more thorough analysis of the trade-offs and limitations is necessary to justify the proposed method.

**(3) Lack of novelty.** 
I feel that the proposed method is neither novel nor interesting. First, the goal of this paper has been widely studied via augmentation-aware objectives (e.g., AugSelf) and augmentation-free SSL methods (e.g., I-JEPA). Also, it is hard to find a strong advantage of the proposed idea compared to AugSelf. In my opinion, the choice between injection and prediction cannot make meaningful novelty. The core idea of incorporating augmentation information into the learning process is not new, and the specific way it is implemented in this work does not seem to offer a significant conceptual advancement over existing methods. The marginal performance gains further underscore the lack of substantial innovation.

### Questions
Can the proposed method be applied to generative modeling like GAN training? It is worth noting that the main baseline, AugSelf, can be utilized for efficient GAN training [1].

[1] Hou et al., Augmentation-Aware Self-Supervision for Data-Efficient GAN Training, NeurIPS 2023

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
State-of-the-art approaches to self-supervised representation learning (SSL) optimize invariance-inducing objectives of representations to augmented views of an input observation, while preventing their collapse to a trivial solution. Effective optimization of these objectives reasonably results to information loss about the features excited by the augmentations in the representation space. These features, however, could be useful to maintain for some downstream prediction (potentially transfer learning) tasks. While the projector network is a common feature of these methods which mitigates this effect, the invariance still persists. The authors propose a simple intervention to typical SSL pipelines in order to further mitigate this effect: ***they suggest to condition the projector network with information about the particular augmentation used to derive a view of an observation***. Experiments on downstream transfer learning tasks with pretrained networks demonstrate an improvement in performance compared to baseline methods, targeted at the same issue. Analysis of representations and the projector demonstrate that augmentation information is indeed used and the method leads to more sensitivity to the variations induced by augmentations in earlier activations of the pretrained network. They also provide with ablation analyses of various implementation design choices.

### Strengths
1. The identified problem is known and significant for representation learning. The authors discuss fairly well the related literature and approaches to its solution.
2. The idea is fairly novel, there have been some similar approaches that essentially “condition the projector network”. Please, refer to Question 1.
3. Nonetheless, their results generally convince that the detail is in the implementation level, rather than the conceptual.
4. The paper is well-written and well-argumented.

Overall, the paper convinces that conditioning the projector with augmentation information is a good direction towards creating more potent and transferable representations.

### Weaknesses
1. Experiments remain relatively small-scale in dataset and model size. Especially, it would have been interesting to examine the effect of conditioning as pretraining data becomes abundant.
2. CASSLE performs better (compared to AugSelf) for contrastive methods and BarlowTwins than others, i.e. BYOL and SimSiam. A discussion on why this happens can be interesting.
3. Semi-supervised (few-shot classification) results are competitive, but weaker.
4. Experiments on object detection task demonstrate a marginal improvement.

5. The paper does not report confidence intervals of their results.
6. Citation and bibliography style needs serious editing. Sometimes “et al.” is retained in bibliography, journals/conferences/proceedings are frequently missing and style is generally inconsistent.

### Questions
1. Missing relevant approach to CASSLE is [1]. They provide with a method which can be perceived as a kind of conditioning to augmentation information.
2. In *Related Work*, contrastive learning objectives usually refer to methods which prevent representational collapse by contrasting against negative pairs. Please clarify this distinction.
3. In *Section 4.2*, an analysis of activation invariance is presented based on the InfoNCE loss. Which similarity function was used to compare earlier representations?
4. In *Table 3*, how is the rank computed exactly?

[1] Bhardwaj, Sangnie, et al. "Steerable equivariant representation learning." arXiv preprint arXiv:2302.11349 (2023).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Self-supervised methods are known to learn representations invariant to augmentations applied during training. This can be problematic when features of such augmentations are important for downstream tasks. This work considers the important task of performing self-supervised learning without losing important semantic features in the data. To achieve this, CASSLE is proposed, a method which conditions the learned projection head on the augmentations of each view. The work demonstrates that this results in features which are still augmentation-aware.

### Strengths
* The manuscript is well written and experiments are well picked to test the purported claims regarding sensitivity of learned features to augmentations applied during training.
* CASSLE is simple and has demonstrated efficacy when training augmentation-based contrastive models. When compared to other methods that condition on augmentations applied during training, table 1 shows that CASSLE has superior performance across many datasets.

### Weaknesses
 * Based on Table 7, the proposed method seems to less effective for SimSiam and BYOL compared to InfoNCE based methods. The manuscript currently claims that CASSLE is applicable to all joint-embedding architectures, but the current experimental results do not demonstrate this.
* The experiments in 4.2 use the InfoNCE to evaluate augmentation-awareness, which is sensitive to the negative examples that are used. Instead of this, why not perform linear probing to predict the specific augmentation applied to an image? This would be a more direct measure of the augmentation-awareness.
* The work does not address the large body of work surrounding “feature suppression”, an important issue of contrastive models becoming invariant to features important for downstream tasks. I believe the work can be strengthened by including comparisons to methods proposed to address feature suppression [2], as well as evaluation on some feature suppression benchmarks [1].
* Current experiments do not demonstrate the effectiveness of CASSLE with augmentation-free approaches to self-supervised learning. This limits the modalities in which it can be applied to those where augmentations can be selected a priori. 

Minor:
* For Table 1, and other similar tables, could the authors add a column denoting mean improvement, taken over datasets, over the vanilla baseline to more easily compare each of the methods to CASSLE? It does not have to specifically be an additional column, but it would be nice to have an aggregate metric of performance in comparison to the baseline. 
* Some of the citations should be updated to include the full Author name (E.g., MoCo and SimSiam citations)

### Questions
* How does CASSLE relate to feature suppression [1] and shortcut solutions [2] in contrastive learning?
* Table 4 indicates that many of the methods were trained with a batch size of 256. Can the authors clarify why this was set so low? In the SimCLR paper it is shown that contrastive methods perform much worse when trained with a smaller batch size. Does CASSLE scale to larger batch sizes? Does CASSLE still perform well with a large batch size?
* Can CASSLE be applied to masked self-supervision? There seems to be a connection between CASSLE and the MAE, where the latter conditions on mask tokens to reconstruct masked patches.
* Have the authors tried performing feature inversion like in [3]? It would be interesting to see if CASSLE results in inverted features that are more reconstructive of attributes like color compared to vanilla contrastive features.


[1] "Intriguing Properties of Contrastive Losses,” Chen et al., 2021

[2] “Can contrastive learning avoid shortcut solutions?,” Robinson et al., 2021.

[3] “What makes instance discrimination good for transfer learning?,” Zhao et al., 2021.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of recent self-supervised learning methods that they learn to be invariant to data augmentations, which may be harmful for some downstream tasks. To tackle this problem, this paper proposes to modify the projector by feeding the information about data augmentations together with the encoder outputs. Experimental results show the effectiveness of the proposed method in transfer learning on image datasets.

### Strengths
- Learning augmentation-aware representations is a timely topic.

- The proposed idea is simple and ablation studies show how the design choices are made well.

### Weaknesses
- The work by [Garrido et al.] is a significant recent contribution to the field of self-supervised learning, particularly in learning equivariant representations. However, it is not discussed in this paper. This omission is noteworthy as it represents one of the most recent advancements among prior works.

- The proposed method introduces additional information about augmentations alongside the encoder outputs. However, the mechanism by which this helps "preserve more information about augmentations" in representations remains unclear. The observation in Figure 3, where injecting information of random augmentations leads to reduced cosine similarities, suggests that the projector's reliance on this additional information is not directly linked to changes in the learned representations (encoder outputs). In other words, the learned representations might not necessarily change regardless of whether the projector uses the additional augmentation information. A more rigorous theoretical justification or empirical evidence demonstrating the effect of the proposed method on the learned representations themselves would significantly strengthen the paper.

- While the proposed method aims to improve downstream task performance, the gains are generally marginal and often fall short of those achieved by previous methods. This raises questions about the practical significance of the proposed approach.

- In Table 1, the MoCo-v2 results only include one performance metric for LooC, which provides limited information. A more comprehensive comparison across multiple metrics would be beneficial.

- The performance of "AI by [Chavhan et al.]" on MoCo-v3 is missing in Table 1, despite being reported in the original paper. Including this result would provide a more complete picture of the comparative performance.

- The reference section requires careful revision. There are numerous instances of incomplete or inaccurate references. For example, the work by [Lee et al.], a close prior work, is cited with its arXiv version instead of the NeurIPS'21 publication. Many other references also lack the name of the published venue. This lack of attention to detail detracts from the overall quality of the paper.

- The paper only evaluates the proposed method on ResNet-50. While the authors mention that they focus on convolutional architectures, the lack of experiments with other architectures, such as ViT, raises concerns about the scalability and generalizability of the proposed method. ViT has become increasingly prevalent in recent years, and experiments with this architecture would help demonstrate the broader applicability of the proposed method.

### Questions
Please address concerns in Weaknesses.

> **post rebuttal**

As some of my concerns remain after discussion with authors, I keep my original rating unchanged with more confidence.

- I think your experiments can only be used to "indirectly" justify if the encoder preserves the information about augmentations. As I suggested, any theoretical analysis or a more direct experiment that checks if the proposed method better retains the augmentation information compared to the baseline would be helpful.

- Only ResNet-50 is used throughout experiments, so my concern on the scalability still remains. Note that ViT is just one option to resolve this concern; you can use different number of layers or other types of CNN architectures. Generally speaking, ViT becomes prevalent in the last ~ 2 years, so experiments with this type of architecture would strengthen your contribution.

- The reference section is still not proofread after being pointed out twice; at this point, I am not sure if authors are willing to show proper respect for previous works. MoCo v2 is an arXiv preprint and MoCo v3 is published in ICCV'21, but both miss their venues.

Xinlei Chen, Haoqi Fan, Ross Girshick, and Kaiming He. Improved baselines with momentum
contrastive learning, 2020b.

Xinlei Chen, Saining Xie, and Kaiming He. An empirical study of training self-supervised vision
transformers, October 2021b.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
