# Compressing Vision Foundation Models at ImageNet-level Costs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Vision foundation models are renowned for their generalization ability due to massive training data. 
Nevertheless, they demand tremendous training resources, and the training data is often inaccessible, e.g., CLIP, DINOv2, posing great challenges to developing derivatives that could advance research in this field. 
In this work, we offer a very simple and general solution, named \textit{Proteus}, to distill foundation models into smaller equivalents on ImageNet-1K without access to the original training data. 
Specifically, we remove the designs from conventional knowledge distillation settings that result in dataset bias and present three levels of training objectives, i.e., token, patch, and feature, to maximize the efficacy of knowledge transfer. 
In this manner, Proteus is trained at ImageNet-level costs with surprising ability, facilitating the accessibility of training foundation models for the broader research community.
Leveraging DINOv2-g/14 as the teacher, Proteus-L/14 matches the performance of the Oracle method DINOv2-L/14 (142M training data) across 15 benchmarks and outperforms other vision foundation models including CLIP-L/14 (400M), OpenCLIP-L/14 (400M/2B) and SynCLR-L/14 (600M).}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
While many Vision Foundation Model (VFM) checkpoints are available, their training datasets are inaccessible. This paper shows that distilling a vision foundation model using only the ImageNet dataset gives us a model that matches the performance of a similar size model trained with massive data, on several vision benchmark datasets from different domains. The paper uses the popular intermediate feature distillation strategy for KD. Experiments were conducted using several teacher-student combinations.

### Strengths
Presentation: 
The paper was written well and was easy to follow.

Experiments: 
Authors evaluated their models on a wide range of CV tasks (classification, segmentation, depth estimation) using several downstream datasets. Experimental results show that models distilled only on ImageNet using the proposed approach match/outperform same size models trained on significantly larger datasets without distillation. Experiments also show that the feature-based distillation performs better than logit-based distillation approach DeiT.

### Weaknesses
``The problem setting of the paper is not convincing`` 
While the original datasets used to train models such as DINOV2 are unavailable, there are numerous large scale image datasets (DataComp, LAION, etc.) that are available to the community these days. If the goal is to get a small model that performs well on a broad array of tasks, I do not understand why one should restrict themselves to distilling on ImageNet. They can use more diverse datasets, for example, diverse subsets of data taken from one of the large-scale public datasets. If the paper had compared different datasets in terms of their KD effectiveness or proposed methods to create better general purpose KD datasets, that would have been an interesting and useful contribution to the community.

The authors performed an experiment by using target task datasets for distillation and showed improved performance. This is an obvious/expected behavior, which also suggests that "we should go beyond ImageNet". If one has access to some data from target tasks, they can curate better distillation datasets as shown in a recent paper: "Knowledge Transfer from Vision Foundation Models for Efficient Training of Small Task-specific Models", ICML 2024.


``Limited technical contribution``
Feature distillation is a standard approach in ML community. There are numerous papers that proposed various distillation objectives based on intermediate features. See "Knowledge distillation: A survey", International Journal of Computer Vision, 2021.
The presented approach uses standard l2 distillation loss on classification and patch tokens. It leverages masking strategy which is also a commonly-used data augmentation approach when training vision models.


``Presentation - Redundant/Confusing terminology``
The terminology of token-level, feature-level and patch-level is a bit confusing/redundant. In a vision transformer setting each image patch becomes a token, so it is confusing to refer to "classification token-based loss" as "token-level" and "patch token-based loss" as "feature-level". Both losses are token-based losses (either CLS token or patch token). Alternatively, both losses can also be called feature-based losses (CLS token features or patch token features). Both feature-level and patch-level losses described here are based on patch-tokens. So, the terminology of "feature-level vs patch-level" is confusing since both are actually patch-level losses, one with masking and one without masking. 

Table 1 - What does "Hint" in Table.1 refer to?

### Questions
Suggestions:

Training small models with distillation for improved performance is a fairly standard practice, and there are numerous distillation loss functions proposed over the last decade. An important question worth looking into in the current "data-centric ML world" is ``What is the right dataset to use for distillation?``. While the paper is looking into this, focusing solely on ImageNet dataset makes the paper's contribution fairly limited, especially given that there are several large-scale public image datasets available now. 

You could avoid the redundant/confusing terminology used for the three loss terms in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper aims to compress pre-trained vision foundation models, such as CLIP and DINO-V2, using only publicly available, small-scale datasets like ImageNet-1k, as the original training data is inaccessible. 
To achieve this, this paper proposed _Proteus_, which perform knowledge distillation (KD) from the pre-trained model at token-level, patch-level, and feature-level. With extensive experiments, this paper demonstrate that the distilled model achieves comparable performance with the foundation model across multiple tasks.

### Strengths
1. This paper is well-motivated. With the development of foundation model trained with private data, it's difficult for the community to reproduce or compress the foundation model due to the inaccessible training data. Thus, how to use existing academic public datasets as a proxy to achieve comparable performance is an interesting question. 

2. The performance of the model is excellent, as it achieve comparable performance with the foundation model with much less training data. Besides, this paper conducts extensive experiments and ablation studies to demonstrate the generalization ability of Proteus. 

3. The empirically finding that conventional knowledge distillation with CE loss introduce dataset bias is interesting.

### Weaknesses
1. The novelty of this paper is limited. Although the results are promising, the loss at token, feature, and patch level has been widely explored in vision transformer distillation [1,2,3,4]. Besides, all of them can be considered as KD with intermediate features, which has been a common setting in KD. However, this paper does not cite and discuss any recent related works that perform KD with intermediate feature maps. Specifically, the paper does not address the nuances of applying these distillation techniques to large vision foundation models, where the scale and complexity of the models may introduce unique challenges not present in smaller models. The paper should also discuss how the proposed method compares to other distillation techniques that focus on preserving the generalization ability of the teacher model, rather than just mimicking its output on a specific dataset.

2. Although this paper presents experimental results to support that empirically removing CE loss can mitigate dataset bias, it would be better to provide some theoretical analysis to understand this question better. The current explanation lacks a formal justification for why removing the CE loss leads to better generalization. A more rigorous analysis, perhaps drawing from existing theories on domain adaptation or transfer learning, would greatly strengthen this claim. Furthermore, the paper should explore the potential trade-offs of removing the CE loss, such as the impact on convergence speed or the stability of the training process. It would also be beneficial to investigate whether other loss functions could achieve a similar effect without completely discarding the information from the training labels.

### Questions
The definition of "feature" is ambiguous. Currently, this paper just defines it as "intermediate feature _v_" (Line 171) without any additional information. This paper should specify which specific feature maps of vision transformers is used, like the output of the last transformer encoder layer of ViTs, the outputs of all 12 transformer encoder layers of ViTs, the attention maps, the Q/K/V within self-attention modules, etc.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple yet effective method for distilling the generalization ability of visual foundation models using only the ImageNet dataset. Specifically, compared to traditional knowledge distillation, it omits hard logits distillation, cross-entropy loss, and KL-divergence loss, while introducing MSE loss to align the intermediate results of the student network with those of the teacher network. The alignment of intermediate results involves three levels: token level, feature level, and patch level. Experiments show that the proposed method effectively distills the generalization ability of the teacher network.

### Strengths
1. This paper presents a simple yet effective method that utilizes the hidden layer features of the teacher network to successfully transfer its generalization ability to the student network.

2. The article provides extensive experimental validation of its claims on the ViT architecture, with datasets that include classification, segmentation, and depth estimation. The student network architecture encompasses various sizes, including ViT-small, ViT-base and ViT-large.

3. This paper is well-written.

### Weaknesses
1. This paper is less novelty. Previous works have also utilized intermediate layers for distillation on ImageNet-1K and achieved good performance on other datasets, such as MiniViT[1], and [2]. What are the differences between this work and those approaches. What are the comparative results of these methods with your work?

2. Figure 3 is not referenced in the main text, and it is unclear what issue Figure 3 is intended to illustrate.

3. When validating the generalization ability of the student network, how many epochs were fine-tuned for fine-grained classification, segmentation, and depth estimation? Compared to baseline methods like DeiT and IBOT, which used the same amount of data, was the computational load higher?

4. Why does Figure 7 show that more data leads to lower results on the ImageNet linear evaluation? For instance, sampling 50% of the data seems to yield better results than sampling 100% of the data.

5. How do the results of distillation when integrating hard logits distillation, the Cross-Entropy loss, the KL-divergence loss, and the MSE loss compare to the results obtained using only the proposed method? Would there be a decline in performance?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Proteus, a method for distilling large vision foundation models into smaller equivalents on ImageNet-1K without access to the original training data. By focusing on token, patch, and feature-level training objectives, Proteus achieves impressive results at ImageNet-level costs, enabling broader access to training foundation models. When compared to other models including DINOv2-L/14, CLIP-L/14, OpenCLIP-L/14, and SynCLR-L/14, Proteus demonstrates competitive performance across 15 benchmarks, matching the Oracle method in some cases.

### Strengths
1. Proteus offers a practical and accessible method for distilling foundation models, addressing the resource-intensive nature of training such models.
2. Proteus demonstrates appealing performance and efficacy in knowledge transfer, matching or outperforming models trained on significantly larger datasets.
3. The paper is well-structured and effectively communicates the proposed solution and its results.

### Weaknesses
1. What is the performance of Proteus-L/14 distilled from the DINOv2-L/14 teacher? This informs the extent of performance degradation when distillation using ImageNet-1K.
2. Validation on varying data scales: The paper lacks validation on different data scales, such as subsets of ImageNet-1K or larger datasets like ImageNet-21K, which could provide more comprehensive insights. Specifically, it is unclear how the performance of Proteus would be affected by reducing the number of training samples per class or by reducing the number of classes used for training. This is important to understand the data efficiency of the proposed method.
3. Validation on other models and domains: The authors are suggested  to validate the effectiveness of  Proteus on diverse models and domains, such as large-scale pre-trained LLMs or diffusion models, to validate generalizability. The current evaluation is limited to vision models, and it is not clear if the proposed distillation approach would be effective for other modalities or model architectures.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
