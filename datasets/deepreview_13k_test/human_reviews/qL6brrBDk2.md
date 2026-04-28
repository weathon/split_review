# SAFLEX: Self-Adaptive Augmentation via Feature Label Extrapolation

- Decision: Accept
- Scores: 8, 5, 8, 8

## Abstract
Data augmentation, a cornerstone technique in deep learning, is crucial in enhancing model performance, especially with scarce labeled data.
While traditional methods, such as hand-crafted augmentations, are effective but limited in scope, modern, adaptable techniques often come at the cost of computational complexity and are hard to fit into existing processes.
In this work, we unveil an efficient approach that universally enhances existing data augmentation techniques by enabling their adaptation and refinement, thereby providing a significant and comprehensive improvement across all existing methods.
We present \textbf{\SAFLEX} (\textbf{S}elf-Adaptive \textbf{A}ugmentation via \textbf{F}eature \textbf{L}abel \textbf{EX}trapolation), an approach that utilizes an efficient bilevel optimization to learn the \textit{sample weights} and \textit{soft labels} of augmented samples. This is applicable to augmentations from any source, seamlessly integrating with existing upstream augmentation pipelines.
Remarkably, \SAFLEX effectively reduces the noise and label errors of the upstream augmentation pipeline with a marginal computational cost.
As a versatile module, \SAFLEX excels across diverse datasets, including natural, medical images, and tabular data, showcasing its prowess in few-shot learning and out-of-distribution generalization.
\SAFLEX seamlessly integrates with common augmentation strategies like RandAug and CutMix, as well as augmentations from large pre-trained generative models like stable diffusion. It is also compatible with contrastive learning frameworks, such as fine-tuning CLIP.
Our findings highlight the potential to adapt existing augmentation pipelines for new data types and tasks, signaling a move towards more adaptable and resilient training frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a principled method for data augmentation. To this end, the paper presents a bilevel optimization framework for weighing and soft-labelling the augmented data in order to compensate for the adverse generalization effects of weak, strong and sometimes meaningless augmented examples. Although the impact of data augmentation for generalization, in particular deep learning frameworks, has been substantial, there is still a lack of principled ways of doing data augmentation. This paper has identified this gap and convincingly addressed the problem.

### Strengths
The paper is well-written and easy to understand. 

The diagrams and the equations are easy to follow.

The experiments are performed on diverse datasets with various tasks, including medical imaging and tabular data.

The results are highly encouraging.

### Weaknesses
A few important previous works on sampling and purifying GAN synthetic data are relevant to this paper.  It is important to acknowledge and discuss their contributions in the paper. 

Caramalau, Razvan, Binod Bhattarai, and Tae-Kyun Kim. "Sequential graph convolutional network for active learning." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.
Bhattarai, Binod, et al. "Sampling strategies for gan synthetic data." ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020.

### Questions
I like the paper. Please see a few comments above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper argues that data augmentations can suffer with two main issues - 1. The augmented samples can become out of distribution to the training distribution and 2) the augmented samples can belong to a different class than the original sample. To tackle the first issue, the authors propose to add sample weights (w_i) to the augmented samples. Samples which are farther from the training distribution can be assigned a smaller weight. To tackle the second issue, the authors propose to make the one-hot label as soft-label to capture the uncertainties. 
To learn the sample weights and the soft-label the authors pose a bi-level optimization problem where in the inner loop, the model parameters are optimized over the training and augmented samples and in the outer loop the optimal augmentation parameters are optimized for. 

The authors conduct experiments across three settings - 1. medical datasets, 2. tabular datasets and 3. for contrastive learning approaches. Across all the experiments the authors show improved performance on top of standard augmentations such as RandAug, Mixup and CutMix.

### Strengths
1. The motivation in the paper about identifying the two issues with standard augmentation and then solving it by learning sample weights and soft-labels is really clear.

### Weaknesses
1. The main issue is a lack of proper baselines. Papers such as [1] have already explored using soft labels for augmentations where the softness is derived on the basis of augmentation strength. This paper's novelty thus gets limited. There is no comparison with [1] in any of the experiments. The authors should do a proper comparison with [1] and justify how their approach is better than it. 

2. To solidify the experimental results the authors should also experiment with stronger architectures and datasets such as ResNet-101 over ImageNet as done in [1].

I am willing to update my ratings if my concerns are addressed. 

References - 

1. Soft Augmentation for Image Classification. Liu et al. https://arxiv.org/pdf/2211.04625.pdf

### Questions
I have already mentioned it in the weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article contributes a workflow named as SAFLEX as data augmentation. Here is a summry:

(1) Authors unveil a novel parametrization for learnable augmentation complemented by an adept bilevel
algorithm primed for online optimization.
(2) Author's SAFLEX method is distinguished by its universal compatibility, allowing it to be effortlessly
incorporated into a plethora of supervised learning processes and to collaborate seamlessly with an
extensive array of upstream augmentation procedures.
(3) The potency of authors' approach is corroborated by empirical tests on a diverse spectrum of datasets
and tasks, all underscoring SAFLEX’s efficiency and versatility, boosting performance by1.2% on
average over all experiments.

### Strengths
They have considered experiments of different data types and model training as downstream tasks, which demonstrate their workflow as a robust one.

### Weaknesses
From a model perspective, this is a good one as topic of adaptive learning, though a  little bit off the topic of this conference. 
From data augmentation perspective, it is better to demo some more experiments in downstream task involves with high dimensional data.

### Questions
Is there any empirical experiments that SAFLEX can contribute to some other applicable downstream task like model training?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the training of high-performance neural networks on small amounts of training data by optimizing data augmentation. Existing methods in this field optimize the transformation itself in the feature space, which limits the available data augmentation transformations and has high computational complexity. This paper differs from these existing approaches by optimizing the importance weights of the input features and the soft labels to be assigned to the augmented data, thereby meta-learning the data augmentation available in the existing data augmentation pipeline. Focusing on features and labels in data augmentation has not received much attention, and the idea is novel. Furthermore, the paper proposes a method to approximate the bi-level optimization of meta-learning with validation data to a single-level optimization by borrowing the idea of gradient matching and developing an efficient algorithm. Experiments verify the effectiveness of the proposed method on various datasets, tasks, and combinations of data augmentation methods. On the other hand, the paper does not provide an evaluation of the first-order approximation or the computation cost, and there is room for improvement in this aspect.

### Strengths
+ The paper proposes a novel data augmentation optimization strategy that optimizes the importance and labels of input features. The idea is very interesting and original.
+ The paper proposes a first-order approximation method to efficiently compute meta-learning that requires bi-level optimization.
+ The paper applies and evaluates the proposed method not only on image datasets but also on table datasets. This evaluation is important in supporting the paper's claim that the method can be applied to any data augmentation pipeline.
+ The paper provides experimental results on the recently widely used CLIP pre-trained models, effectively demonstrating the impact of the proposed method.

### Weaknesses
- Even though the paper proposes a first-order approximation method, it does not provide an evaluation of this method. In other words, the paper should provide a performance comparison with the usual bi-level optimization and a computation cost comparison with other data augmentation strategies such as Fast AutoAugment.
- The writing of the paper is not necessarily of high quality. For example, Theorem 1 is very difficult to read because it contains multiple claims that make up the entire solution. Theorems and corollaries should be split for each claim, or if the propositions are ambiguous, they should be replaced with detailed explanations for each component, rather than in the form of a theorem. In fact, the proofs provided by the Appendix are almost obvious and make little theoretical contribution.

### Questions
- Do you think the proposed method can be applied to consistency-based semi-supervised learning with data augmentation, e.g., FixMatch [a]? The study of estimating the importance of samples and labels is well studied in the field of semi-supervised learning rather than in the field of data augmentation (e.g., FreeMatch [b]). If it can be shown that the scheme of the proposed method can be implemented in semi-supervised learning, the impact of this paper on the community will be even greater.

[a] Sohn, Kihyuk, et al. "Fixmatch: Simplifying semi-supervised learning with consistency and confidence." NeurIPS 2020.

[b] Wang, Yidong, et al. "Freematch: Self-adaptive thresholding for semi-supervised learning." ICLR 2023.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
