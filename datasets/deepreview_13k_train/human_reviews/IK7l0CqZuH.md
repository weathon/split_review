# Heavy Labels Out! Dataset Distillation with Label Space Lightening

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Dataset distillation or condensation aims to condense a large-scale training dataset into a much smaller synthetic one such that the training performance of distilled and original sets on neural networks are similar. Although the number of training samples can be reduced substantially, current state-of-the-art methods heavily rely on enormous soft labels to achieve satisfactory performance. As a result, the required storage can be comparable even to original datasets, especially for large-scale ones. 
To solve this problem, instead of storing these heavy labels, we propose a novel label-lightening framework termed \textbf{HeLlO} aiming at effective image-to-label projectors, with which synthetic labels can be directly generated online from synthetic images. 
Specifically, to construct such projectors, we leverage prior knowledge in open-source foundation models, \textit{e.g.}, CLIP, and introduce a LoRA-like fine-tuning strategy to mitigate the gap between pre-trained and target distributions, so that original models for soft-label generation can be distilled into a group of low-rank matrices. 
Moreover, an effective image optimization method is proposed to further mitigate the potential error between the original and distilled label generators. 
Extensive experiments demonstrate that with only about 0.003\% of the original storage required for a complete set of soft labels, we achieve comparable performance to current state-of-the-art dataset distillation methods on large-scale datasets. 
Our code will be available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the high storage cost of soft labels in dataset distillation that generates synthetic labels directly from images. It leverages open-source models like CLIP and a LoRA-like fine-tuning strategy to extract the labels, bridging the gap between pre-trained and target distributions.

### Strengths
1. The motivation of this paper is clear and easy to understand.
2. The proposed method is simple and effective.

### Weaknesses
I am convinced of the motivation of this paper, but there are significant concerns on using CLIP to generate labels from images:

1. Why not use stronger supervised models or self-supervised models? If we can use another stronger model like CLIP to generate labels from images, why not use it directly for the target task, or replace CLIP (weakly-supervised) with other models like supervised ViT or self-supervised DINOv2? Authors finetune CLIP vision encoder with LoRA, and text embeddings to adapt the specific dataset, which can be seen as a kind of supervised trained model. If we change it to supervised ResNet, ViT, or self-supervised DINOv2 (versus the performance reported with R18 from scratch), the performance may be better. Similarly, why not finetune the foundation models (CLIP or DINOv2) with LoRA on the distilled datasets if we have already used a foundation model?

2. The effectiveness of the proposed method. The storage of classifier weights is not important compared to labels, only 0.7MB in Table 3. In addition, the improvements of Text-Embedding-Based Init and Image Update are quite marginal (0.1 in accuracy). Most improvements come from LoRA-Like Knowledge Transfer, that is to say, adapting the supervised information of the dataset to CLIP vision encoder. 'M' is a bit confusing, please change 'M' to 'MB' in the paper.

### Questions
Why there is no 'Size of Labels' for L Yin et al. (2024) and Sun et al. (2024)

### Soundness
3

### Presentation
3

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
This work introduces HeLlO (Heavy Labels Out), a framework designed to address the challenge of high storage requirements for soft labels in large-scale dataset distillation. Instead of storing the entire soft label, an off-the-shelf pre-trained feature extractor is employed to generate labels in an online fashion during downstream network training. This approach significantly reduces the storage burden, especially when dealing with extensive datasets that necessitate numerous soft labels. Moreover, to mitigate the distribution gap between the target label space and the label space inherent to the pre-trained model, a LoRA-like fine-tuning strategy is applied.

### Strengths
The work effectively tackles the critical issue of high storage requirements for soft labels.

### Weaknesses
 - The comparison presented in Table 1 appears unfair. Unlike the baseline methods, the proposed method requires storing a teacher model (or its low rank version), which complicates a direct comparison. It is unclear why the storage size of the teacher model is relevant here. Please provide a more comprehensive comparison that includes the storage requirements for both the teacher model and the labels across all methods.
- Table 1 contains numerous missing values, which hinders a comprehensive comparison. The reviewer encourages the authors to provide complete results. At a minimum, please include the IPC 50 results for SRe2L and G-VBSM on the Places365-Standard dataset, as the proposed method performs lower than the baseline in this setting.
- Poor writing, there are many typos and ambiguous notations in the proof of Proposition 1, e.g. both $r_i$ and $r^{(i)}$ represent the text description for class $i$. Detailed feedback on these issues is provided in the questions part.

### Questions
- Ambiguous notations
    1. In line 198, $r_i$ is described as the text description for class $i$. What is $r^{(i)}$ in Equation (2)?
    2. In line 199, $v_T$ is used for the text description of the $i$-th class. What is the meaning of $v_T^{(i)}$ in Equation (3)?
    3. In line 201, $W$ is defined as a matrix of size $d_f \times C$, yet the authors also write $W = \textbraceleft w^{(i)} \textbraceright_{i=0}^{C-1}$, which suggests $W$ is a set. Could the authors clarify this discrepancy?
- What is the definition of weak teacher in line 237? Does is differ from the teacher defined in line 162?
- The reviewer is curious about the potential outcomes of using a model pre-trained on the original real dataset as the label projector. Could the authors provide more insights or results related to this scenario?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes an interesting alternative to label storage in the context of data distillation. By developing image-to-label projectors based on existing works in CLIP and LoRA, their proposed method, HeLlo can dramatically reduce the original storage requirements of the soft label set by generating them in an online fashion. Understandably with large datasets (i.e. large number of classes), the size of softlabels will scale linearly and can create storage bottlenecks for further downstream usage of the distilled data. Experimentally, we see that the proposed method can far surpass the performance of SoTA work RDED on the distillation benchmarks -- including a variety of different downstream architectures (both convolutional and transformer).

### Strengths
I do think this paper approaches a problem that isn't really being avidly researched in the field of data distillation. In particular, most works aim to reduce the costs associated with the number of images, or the learning paradigms for distillation. However, this work looks at an add on to existing distillation techniques in an effort to reduce the storage requirements of the labels. From a novelty perspective, I would agree that this paper incorporates new or innovative techniques into solving a unique problem. I believe there is value in the idea of an image-label-projector, particularly in distillation, and it is interesting to see how CLIP and LoRA have influenced the author's designs, showing a blend of recent developments in adjacent domains. The results are quite convincing, and the ablations studies appear throughout, including downstream applications, such as continual learning. I believe this contribution has strengths primarily in novelty and target scope. However, the latter is also a weakness I elaborate on below.

### Weaknesses
Despite the interesting approach taken in this paper, I find there to be a few crucial weaknesses that may overshadow the benefit of the approach. Data Distillation computational costs are often computed regarding the size/number of images as these often take up more storage space than the labels. Understandably at lower image/class ratios, this distribution may deviate (as soft labels would remain scaled at the number of classes, say 1K on ImageNet) -- however I am not convinced that the storage cost of soft labels is indeed that significant. In particular, the asses data distillation methods are on Image Classification, hence each image is associated with one vector of soft labels. Thus at a reduced number of images, 1 or even 50 images per class, the incurred cost of soft labels is actually quite small, (appears to be a couple GB's on ImageNet1K at 10 ipc). Finally, I think alternate methods of logit compression should be compared, such as simple quantization of the logits to a lower precision, as they may not indeed cause significant performance degradation, but will greatly reduce the storage costs. I think the primary weakness here is whether the contribution in this paper actually solves a problem that is being faced in data distillation. As currently I think the scope is not actually a commonly faced problem in the field.

Additionally, I think the professionalism/clarity of the figures can be improved, particularly Figure 1.0, where certain words are covered by symbols, etc.

### Questions
Some questions I think that could be helpful here:

1. Can we apply this to more complex tasks (like segmentation of vision language models)? This would widely increase the scope of the paper, and understandably storage requirements on these tasks would be significantly more prominent (i.e. segmentation would have softlabels for each pixel so the computational costs would be far larger).

2. How does the method compare with naive compressions such as quantization etc. 

I think the biggest things for the authors to focus on during the rebuttal/discussion phase should be comprehensive comparisons against existing storage compression techniques (particularly simple ones, such as quantization or even interpolation). Additionally, I would find this work's significance far more compelling as it has been applied to a task where the storage costs of soft labels are a clear bottleneck, like semantic segmentation.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Dataset distillation aims to condense large training datasets into smaller synthetic ones, but current methods still demand substantial storage for soft labels. The proposed method, HeLlO, tackles this issue by generating synthetic labels directly from images using foundation models like CLIP and fine-tuning with low-rank matrices, significantly cutting down storage requirements. This approach delivers performance on par with state-of-the-art methods while using just 0.003% of the original storage.

### Strengths
[S1] This paper tackles one of the key challenges in efficient training and dataset distillation (DD).

[S2] The writing is clear and easy to follow.

[S3] The results show comparable performance to some of the state-of-the-art methods on large-scale datasets, but the experiments could be more extensive, especially in terms of comparisons and generalizability.

### Weaknesses
[W1] There are concerns about the method's generalizability, especially regarding its applicability to high-resolution datasets and various model architectures. I suggest testing DRUPI on 256x256 ImageNet-1k, as well as practical datasets like clinical and aerial images, to better assess its versatility. Additionally, evaluating its performance on ViT models would help determine how well the method generalizes across different architectures.

[W2] An analysis of distillation costs is missing from the paper, which is crucial for assessing the efficiency of data-efficient training algorithms. A detailed comparison of the training costs for both the proposed method and state-of-the-art (SOTA) approaches, especially in terms of memory usage and training time, is necessary.

[W3] The paper lacks comparisons with key state-of-the-art methods such as DREAM, DataDAM, and SeqMatch in Table 2. Adding these comparisons would offer a more complete evaluation of DRUPI's effectiveness. If these methods were excluded for specific reasons, it would be helpful for the authors to explain their omission and clarify how DRUPI compares to these recent approaches.

### Questions
1. Does the method demonstrate cross-architecture generalization capability on ViT models?
2. Can HeLlO maintain strong performance at higher IPCs, such as 100 or 200?
3. How does the proposed framework perform on other downstream tasks like object detection or segmentation?

### Soundness
2

### Presentation
3

### Contribution
2
