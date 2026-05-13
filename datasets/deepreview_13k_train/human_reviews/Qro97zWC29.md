# Near, far: Patch-ordering enhances vision foundation models' scene understanding

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
We introduce NeCo: Patch Neighbor Consistency, a novel self-supervised training loss that enforces patch-level nearest neighbor consistency across a student and teacher model. Compared to contrastive approaches that only yield binary learning signals, i.e. "attract" and "repel", this approach benefits from the more fine-grained learning signal of sorting spatially dense features relative to reference patches. Our method leverages differentiable sorting applied on top of pretrained representations, such as DINOv2-registers to bootstrap the learning signal and further improve upon them. This dense post-pretraining leads to superior performance across various models and datasets, despite requiring only 19 hours on a single GPU. This method generates high-quality dense feature encoders and establishes several new state-of-the-art results such as +5.5 % and +6% for non-parametric in-context semantic segmentation on ADE20k and Pascal VOC, +7.2% and +5.7% for linear segmentation evaluations on COCO-Things and -Stuff and improvements in the 3D understanding of multi-view consistency on SPair-71k, by more than 10%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to enforce consistency of the sorting relationship between the student model and the EMA teacher model as a post-training strategy for advanced vision foundations models, such as DINOv2. The model is post-trained on the COCO or Pascal dataset. Improvements are observed in downstream semantic segmentation tasks on Pascal and COCO, especially under the evaluation protocol of linear probing.

### Strengths
1. The paper is clearly written and easy to follow.
2. The motivation of further improving advanced vision foundation models is promising, especially by designing a lightweight post-training technique.
3. The results under frozen encoders are impressive, compared with the original encoders.
4. The method of applying sorting-based consistency regularization is new to the post-training field.

### Weaknesses
1. My main concern lies in the difference between sorting-based regularization and a much simpler soft cross-entropy loss. It means, if we directly compute the similarity between $F_s \in R^{N \times d}$ and $F_r  \in R^{N_r \times d}$ as well as the similarity between $F_t  \in R^{N \times d}$ and $F_r  \in R^{N_r \times d}$ (suppose the obtained two similarity maps are $S_s, S_t \in R^{N\times N_r}$), can we directly apply a soft cross-entropy loss between $S_s$ and $S_t$ along the $N_r$ dimension? Will this be a stricter optimization target than the plain sorting-based strategy? Because it not only requires the sorted order to be the same, but also their pair-wise similarities with the referenced patches to be the same.

2. It is good to achieve promising results on downstream Pascal, COCO, and ADE20K datasets, when applying the post-training strategy. But I am wondering whether the post-training stage, especially only conducted on a small-scale COCO dataset, will potentially ruin the original DINOv2's good representation in broader scenarios, such as sketch images or urban-scene images (Cityscapes). It will be good to know how the post-trained model trades off between generalization and scene specification.

3. The proposed method fails to achieve obvious improvements over the original pre-trained encoders when evaluated under the fully-fine-tuning protocols (Table 4). For example, although the model is explicitly fine-tuned on COCO, it is still inferior to the original DINOv2 on COCO-Stuff dataset (46.8 *vs.* 46.5). Are there any insights into these results?

### Questions
- Could the authors provide additional results of semantic segmentation on urban-scene datasets like Cityscapes and remote sensing datasets?
- Could the authors explain why the fully-fine-tuning results are not better than the original pre-trained encoders? Indeed, it can be expected that the post-trained encoder is good than pre-trained encoder when evaluated under a frozen state, as the feature relationships are explicitly strengthened by the proposed strategy.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new self-supervised training loss called Patch Neighbor Consistency (NeCo). The key benefit of the proposed method is that the loss yields richer/fine-grained supervision over contrastive approaches. The proposed training scheme is applied over DINOv2 pretrained backbones and shows further improvements on a wide range of downstream tasks.

### Strengths
1. The paper is well written, with a wide range of ablations substantiating most of the design choices introduced in the method.
2. The improvements obtained by the proposed method in linear probing and multiview feature consistency evaluations indicate the superior quality of the learned features. Overall the method shows good improvement in a wide range of downstream evaluations.

### Weaknesses
1. The main weakness of the proposed method is the baselines. Since the proposed method is introduced as post-training adaptation scheme. It would be fair to continually pretrain DINOv2 and other pretraining methods also by the same duration as NeCo. An ablation on matching training flops/epochs between all the pretraining methods and NeCo would be good to have in the paper.
2. The method has carefully crafted hyperparameters to ensure some overlap between teacher and student patches. Is it possible that the method can do away with ROIAlign by not performing any geometric transformations in data augmentation. At the moment it seems like ROIAlign is used to undo the geometric transformation applied to the image presented to the teacher model.

### Questions
It would be good to clarify the main weakness of proposed baselines. An understanding of how the method performs against baseline approaches, when their training flops/epochs are matched can bolster the claims made in the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces NeCo, a self-supervised training algorithm that enhances patch-level nearest neighbor consistency across student and teacher models, aiming at improving scene understanding in vision foundation models. NeCo leverages differentiable sorting on pretrained representations, such as DINOv2, to boost learning signals and performance across various models and datasets. The method requires minimal training time and establishes new state-of-the-art results in non-parametric in-context semantic segmentation and 3D understanding.

### Strengths
1.	The paper is well-written. 
2.	Experiments are extensive and convincing, providing rich results on various settings.
3.	The proposed method is simple, interesting, and effective, surpassing previous works by a large margin.

### Weaknesses
1.	The major contribution of NeCo seems to be introducing sorting consistency into visual representation pretraining. In pages 4-5, the description of differentiable swapping and sorting takes majority of space in Section Method, but these contents are proposed by previous works and simply pasted here. 
2.	The method requires a pretrained backbone (e.g. DINO) for visual representation learning, and outperforms previous methods. However, some previous learning methods (e.g. MAE) does not require a pretrained backbone, so the improvement may partially come from the additional information brought by the pretrained backbone DINO. Is it possible to use the sorting consistency between different views to learning representation without the pretrained backbone teacher?

### Questions
1.	Please give more details on sampling and collecting patch features with ROIAlign. How the box coordinates of patches are sampled? Also, how the different views of one single image are sampled? 
2.	How the sorting algorithm is implemented? Are O(nlogn) algorithms such as quick sorting (other than odd-even sorting mentioned in the manuscript) compatible with differentiable swapping?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces NeCo, a self-supervised training loss that enforces patch-level nearest neighbor consistency between a student and teacher model. Unlike binary contrastive methods, NeCo leverages fine-grained learning signals by sorting spatially dense features relative to reference patches. By applying differentiable sorting on top of pretrained representations like DINOv2, NeCo achieves superior results across various models and datasets with minimal GPU time.

### Strengths
1. It makes sense to perform self-supervised learning by bringing Neighbor Patch Consistency closer.

2. Although the overall method design is based on existing simple strategies, it shows significant performance improvements. The proposed method achieves SOTA on several downstream tasks.

3. Further self-supervised training based on existing pretrained models (e.g., DINOv2) can significantly reduce computational cost and GPU training time.

### Weaknesses
1.The comparative experiments in the paper are not comprehensive. If DINOv2 is used as a baseline, it is necessary to align with the downstream tasks validated in the DINOv2 paper as much as possible. Additionally, if the goal is to claim dense prediction capability, it is also important to validate the model’s representation abilities on more instance and dense recognition tasks, such as CityScapes, KITTI, and NYUd.

2.Regarding pairwise distance computation, if this method only calculates distances within a single batch, it results in a limited computational space and may not capture all potential patches that are near the selected patches. 

3.Obtaining patch features prior to distance computation heavily relies on the feature extraction capability of the pretrained foundation model. If the pretrained foundation model introduces noise in feature extraction (a common phenomenon), how does your method prevent the accumulation of such errors? 

4.The use of cosine similarity for distance calculation may not be the most accurate choice, as it lacks an ablation study.

5.Does the proposed Patch Neighbor Consistency self-supervised strategy have generalizability? For instance, can it be applied to more foundation models like CLIP, SIGLIP, SAM, etc.?  In other words, can the proposed method adapt to more pretrained models as in the experiment in Table 3?

6.Additionally, is this method suitable for transformer models trained from scratch, assuming it can use another foundation model to extract features for distance computation?

### Questions
Please refer to the weaknesses. I also have an additional empirical question: Would incorporating a 'repel' signal for distant patches (similar to contrastive loss) alongside the computation of near patch consistency enhance the performance of the proposed method?

### Soundness
3

### Presentation
3

### Contribution
3
