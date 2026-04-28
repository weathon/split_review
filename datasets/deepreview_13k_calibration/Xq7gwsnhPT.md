# UNIP: Rethinking Pre-trained Attention Patterns for Semantic Segmentation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
Pre-training techniques significantly enhance the performance of semantic segmentation tasks with limited training data. However, the efficacy under a large domain gap between pre-training (e.g. RGB) and fine-tuning (e.g. infrared) remains underexplored. In this study, we first benchmark the infrared semantic segmentation performance of various pre-training methods and reveal several phenomena distinct from the RGB domain. Next, our layerwise analysis of pre-trained attention maps uncovers that: (1) There are three typical attention patterns (local, hybrid, and global); (2) Pre-training tasks notably influence pattern distribution across layers; (3) The hybrid pattern is crucial for semantic segmentation as it attends to both nearby and foreground elements; (4) The texture bias impedes model generalization in infrared tasks. Building on these insights, we propose UNIP, a UNified Infrared Pre-training framework, to enhance the pre-trained model performance. This framework uses the hybrid-attention distillation NMI-HAD as the pre-training target, a large-scale mixed dataset InfMix for pre-training, and a last-layer feature pyramid network LL-FPN for fine-tuning. Experimental results show that UNIP outperforms various pre-training methods by up to 13.5% in average mIoU on three infrared segmentation tasks, evaluated using fine-tuning and linear probing metrics. UNIP-S achieves performance on par with MAE-L while requiring only 1/10 of the computational cost. Furthermore, with fewer parameters, UNIP significantly surpasses state-of-the-art (SOTA) infrared or RGB segmentation methods and demonstrates the broad potential for application in other modalities, such as RGB and depth. Our code is available at https://anonymous.4open.science/r/UNIP-8DCC/.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the pre-trained attention patterns for semantic segmentation in the infrared domain. It first concludes from the performance of different pre-training methods in infrared segmentation that the pretraining task is the key factor. Then, it takes deeper research on the attention pattern and states the importance of the hybrid attention pattern. Based on this insight, this paper used NMI to indicate the attention pattern and proposed a new pre-training framework named NMI-HAD to distill the layers with hybrid attention patterns. It also proposes LL-FPN and has improved fine-tuning performance

### Strengths
1.	The writing is easy to follow.
2.	The ideas proposed by the author are well supported by the detailed experimental results.
3.	The pre-training method is important in semantic segmentation.

### Weaknesses
1. Although the analysis of attention patterns is persuasive, more comparison with the attention patterns in other RGB semantic segmentation datasets, for example, ADE20k, is necessary. Since the idea of enhancing the segmentation performance with the help of both local and global attention (e.g. Swin Transformer) is not new, it is hard to explain the reason why the difference in attention patterns is more important in infrared semantic segmentation. The difference on attention pattern and their impact between RGB dataset and infrared dataset needs to be clarified.
2. As it is mentioned in line 475 “Excessive constraints on features may intensify the distillation shift and hinder the generalization of distilled models“, an ablation for distillation that combines the features and attention is needed. The comparison between its performance against each method individually can support the claim about excessive constraints.

### Questions
Since the proposed NMI-HAD is layer-wise, I’m curious about the performance when the distillation is more fine-grained. For example, why not apply the distillation on different heads? I may suggest the author to conduct an experiment comparing the performance between layer-wise approach and head-wise approach, which can have deeper insight on the choice of distillation strategy.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper leverages strong pre-trained models to boost the performance of infrared semantic segmentation. The authors identify the best attention patterns and propose the hybrid-attention distillation to improve the performance and efficiency at the same time. A large-scale mixed dataset is also presented for pre-training. The proposed methods achieve the new state-of-the-art results.

### Strengths
1. The benchmark of vision foundation models on infrared segmentation datasets and the introduction of NMI to identity attention patterns for distillation contribute to the community. 
2. Extensive and comprehensive experiments are conducted and the proposed approach significantly surpasses state-of-the-art infrared or RGB segmentation methods.

### Weaknesses
1. The underlying motivation is not very clear. In my opinion, the authors sometimes aim to emphasize the performance in infrared semantic segmentation and sometimes aim to emphasize the versatility of the proposed method. However, on the one hand, the proposed approach is not specific to infrared semantic segmentation tasks. On the other hand, from the viewpoint of visual pre-training and downstream transfer learning, there is a lack of experiments on more general datasets and performance comparisons with related works. Compared to previous works in knowledge distillation, the biggest contribution may be to provide a method to choose which layer to distill. This is the main concern for me.

2. It is strange to distinguish between the last two attention patterns by calling them “local-global” and “global”. The “global” attention patterns are just attention collapse as the authors stated. Therefore, if only considering a single distillation target, the last layer may not be the best choice. I believe previous works have suggested this. If using multiple hierarchical features which is more common, the conclusion may be different.

### Questions
For NMI-HAD, is only the attention map of a single layer used for distillation?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a deep analysis on why RGB pre-trained models performs worse on thermal images. Based on the analysis, the authors present a NMI-guided distillation for improved segmentation. Experiments on different datasets are performed.

### Strengths
- This paper presents a deep analysis on benchmarking the infrared semantic segmentation performance of various pre-training models.
- The experimental results are extensive, and the writings are good.

### Weaknesses
 - The title of the paper is inappropriate as it misleadingly suggests a general semantic segmentation task. In fact, this paper mainly focuses on infrared segmentation of small models by adapting pre-trained models.
- According to the claims of the authors, the MIM (Masked Image Modeling) strategy focuses more on texture information and is not suitable for segmenting infrared images. Why using an MAE-based model as the teacher for distillation can achieve better results?
- This paper seems no comparison with existing distillation strategies used in domain-adaptive methods. If possible, I think it is better to give a comparison.
- More experiments on built datasets can be given to demonstrate the effectiveness of proposed method. For example, we first train on RGB images and then fine-tune on infrared image, or jointly train on both dataset.

### Questions
Please answer the title, claim, and experiment questions in weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work first deeply analyzes the transfer performance on infrared tasks of popular pre-training regimes, including supervised training, contrastive learning and masked image modeling. Based on three valuable observations, this work proposes a pre-training and finetuning framework for infrared image segmentation, dubbed UNIP—specifically, an NMI-HAD distillation algorithm, a mixed large-scale InfMix dataset, and an LL-FPN architecture. Complete experiments and analysis demonstrate the effectiveness of the proposed algorithm.

### Strengths
This work is well-motivated, clearly written and very convincing. All observations and hypotheses are proved by empirical or numerical evidence, which makes the whole work complete and sound.

### Weaknesses
Overall, I feel pretty OK with this work, and there are no **MAJOR** weaknesses. Some minor suggestions are as follows for the author's reference.

- As this work focuses only on infrared images, the word infrared should appear in the title to make it sound and avoid misunderstanding, *e.g.*, for infrared semantic segmentation.
- Some abbreviations should be given their corresponding specific names and appropriate citations if necessary when they first appear, *e.g.*, SSL (semi-supervised learning) in Sec. 2.1.
- Unalighed letters of ViT in Fig. 8.

### Questions
Please refer to the WEAKNESSES part.

### Soundness
4

### Presentation
4

### Contribution
3
