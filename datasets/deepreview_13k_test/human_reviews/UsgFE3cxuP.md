# MaskCLIP++: A Mask-Based CLIP Fine-tuning Framework for Open-Vocabulary Image Segmentation

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Open-vocabulary image segmentation has been advanced through the synergy between mask generators and vision-language models like Contrastive Language-Image Pre-training (CLIP).
Previous approaches focus on generating masks while aligning mask features with text embeddings during training.
In this paper, we observe that relying on generated low-quality masks can weaken the alignment of vision and language in regional representations.
This motivates us to present a new fine-tuning framework, named MaskCLIP++, which uses ground-truth masks instead of generated masks to enhance the mask classification capability of CLIP.
Due to the limited diversity of image segmentation datasets with mask annotations, we propose incorporating a consistency alignment constraint during fine-tuning, which alleviates categorical bias toward the fine-tuning dataset.
After low-cost fine-tuning, combining with the mask generator in previous state-of-the-art mask-based open vocabulary segmentation methods, we achieve performance improvements of +1.7, +2.3, +2.1, +3.1, and +0.3 mIoU on the A-847, PC-459, A-150, PC-59, and PAS-20 datasets, respectively.
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses limitations in open-vocabulary image segmentation, particularly the reliance on low-quality masks that weaken vision-language alignment. The authors propose MaskCLIP++, a fine-tuning framework that transfers CLIP's image-level recognition to local regions using ground truth masks and labels, eliminating the need for a specific mask generator. They introduce a consistency alignment module during fine-tuning to enhance local image-text similarity and reduce overfitting. Empirical results show that MaskCLIP++ outperforms previous state-of-the-art mask-based segmentation methods, achieving improvements of +1.7, +2.3, +2.1, +3.1, and +0.3 mIoU on the A-847, PC-459, A-150, PC-59, and PAS-20 datasets, respectively, with lower training costs.

### Strengths
+ The paper provides a good analysis of the limitations of using generated masks in previous open-vocabulary segmentation works, highlighting the challenges in improving mask generation compared to mask classification.

+ The paper introduces a new fine-tuning framework that leverages ground truth masks and labels, eliminating the need for specific mask generators. This approach addresses the limitations of relying on low-quality masks, improving the alignment of vision and language in regional representations.

+ Based on experiments on several benchmarks, the proposed method demonstrates better perfomrances compared to existing state-of-the-art mask-based open vocabulary segmentation methods.

### Weaknesses
- While the use of ground truth masks improves performance, it may limit the applicability of MaskCLIP++ in scenarios where such masks are not readily available or are costly to obtain. This may result in limitations of scaling up with data and unfair comparisons with other methods. 

- It is not clear whether the insights and proposed method can be generalized/applied to other recent state-of-the-art methods rather than just MaskCLIP. Such experiments/studies could help justify generalization ability of the proposed method.

### Questions
Please refer to details of above "Weaknesses" sections. Specifically:

(1) Is that possible to discuss potential ways to address scenarios where ground truth masks may not be available? If there are any techniques you could propose to generate high-quality pseudo-masks when ground truth is unavailable, or if you have explored using a mix of ground truth and generated masks during training. 

(2) Ablation studies about applying the proposed method to 1-2 other recent SOTA open-vocabulary segmentation methods will be helpful. This would provide concrete evidence of the method's generalizability beyond just MaskCLIP.

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
4

### Summary
This paper propose MaskCLIP++ to transfer CLIP's image-level recognition to local regions via ground truth masks and labels. Based on the analysis of the sources of misalignment, this paper proposes a consistency alignment constraint to ensure that alignment optimization preserves CLIP’s original embedding space. The proposed MaskCLIP++ can be used with different mask generators to achieve open-vocabulary segmentation at the semantic- or instance-level and achieve superior performance.

### Strengths
(1) The proposed MaskCLIP++ is straightforward and easy to follow.

(2) The presentation of this paper is good, with outstanding writing style and clarity.

(3) The paper demonstrates obvious improvements compared to the original CLIP, and it performs well with various
baseline segmentation methods.

(4) Detailed ablation studies are performed to analyze the impact of each component.

### Weaknesses
**[About Methods]**

(1) The illustration of PSM is confusing and unclear. For example, in *Line 204-210*, the author analyzes the cause of misalignment and offers an unintuitive phenomenon. Since the similarity $r$ can be optimized to be close to the target, why the order of $m'^T_1t$ may deviate further from the target? It would be better if the author could explain this phenomenon using specific statistics or figures.

(2) In *Line 236-240*, the author argues that the simplest way to achieve consistency alignment is to update the similarity map in another dimension. If I understand right, it refers to $Linear<E_m, E_t>$ as shown in Table 1. However, the next paragraph directly demonstrates $<E_m, Norm(E_t+P_t)>$, which is incoherent and irrelevant to the above statement. Besides, the $<E_m, Norm(E_t+P_t)>$ used in this paper is very similar to the Content-Dependent Transfer module in [1], resulting in the limited contribution of this paper.

(3) I doubt the effectiveness of decoupling the joint training of the mask generator and classifier for open-vocabulary segmentation. It may be challenging to achieve "real open vocabulary" without training the mask generator. For example, if I want to perform part segmentation (e.g., segmenting person's hands rather than person), the off-the-shelf mask generator may struggle to generate these fine-grain masks if not training on the target dataset.

**[About Experiments]**

(1) As far as I understand, MaskCLIP++ is an enhancement of CLIP to align vision and language in regional representations. To validate the local classification ability, it should be compared to related counterparts like MaskCLIP [2], CLIP-Surgrey [3], SCLIP [4], CLIPSelf[ 5], SAM-CLIP [6], etc. A more valid usage is to perform pixel-level classification based on dense features like SCLIP (zero-shot segmentation), which avoids the impact of mask generators and only focuses on local representations.

(2) It also makes sense to combine MaskCLIP++ with existing open-vocabulary segmentation or mask generators to improve their classification performance as done in this paper. However, some comparative experiments should be conducted using counterpart methods mentioned above (e.g., FC-CLIP to generate mask and SAM-CLIP to classify). 

(3) The scenes and categories in ADE and COCO Panoptic are similar and relevant, which is not convincing to assess overfitting. More scenes like Street-View Datasets used in FC-CLIP should be adopted for better persuasiveness.

---

[1] Collaborative Vision-Text Representation Optimizing for Open-Vocabulary Segmentation.

[2] Extract Free Dense Labels From CLIP.

[3] CLIP Surgery for Better Explainability with Enhancement in Open-Vocabulary Tasks.

[4] SCLIP: Rethinking Self-Attention for Dense Vision-Language Inference.

[5] CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction.

[6] SAM-CLIP: Merging Vision Foundation Models towards Semantic and Spatial Understanding.

### Questions
(1) What is the detailed setting used in Figure 1b? How to determine the GT classification of a mask if it contains multiple categories?

(2) Why use the OpenAI model for ResNet architecture but EVA-CLIP for ViT architecture?

(3) Section 4.1 demonstrates that the model is fine-tuned on the COCO Panoptic training set, but in Table 5, the training set is COCO-Stuff. Why use different training sets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents MaskCLIP++, a masked-based CLIP fine-tuning framework designed for open-vocabulary semantic segmentation. It identifies a performance bottleneck in mask classification accuracy and proposes a consistency alignment module to improve local image-text alignment while mitigating overfitting issues. Experimental results on several benchmarks demonstrate that MaskCLIP++ outperforms existing methods in open-vocabulary semantic, panoptic and instance segmentation  tasks. Additionally, extensive ablation studies are conducted to validate the effectiveness of the proposed framework.

### Strengths
- **Motivation:** The motivation for this work is clearly articulated in the introduction, providing a solid foundation for the research.
- **Quality:** The techniques employed in this paper are sound and well-presented, although some visual illustrations would enhance clarity and understanding.
- **Experiment:** This work conducts extensive experiments to thoroughly validate all aspects of the proposed methods, demonstrating a robust evaluation process.

### Weaknesses
- **Originality:** The primary contribution of this work is the proposed PSM, which enhances local image-text alignment while mitigating overfitting issues. However, this consistency alignment is reminiscent of the cost volume aggregation used in CAT-Seg, which considerably diminishes the novelty of the approach.   

- **Presentation:** The presentation of this work requires improvement. For instance, Figure 3 illustrates the detailed framework of MaskCLIP++, but the clarity of this illustration is insufficient. There is no detailed depiction of the Neck module or the PSM module. Furthermore, while the PSM contains several learnable components, their representations are not adequately explained. Additional unclear aspects are provided in the Questions section.

- **significance:** The performance of MaskCLIP++ is not sufficiently impressive. As indicated in Table 5, it achieves competitive results in most cases. For example, when compared with CAT-Seg, which utilizes a large VLM, MaskCLIP++ does not demonstrate superior performance despite the introduction of a mask generator and various hyperparameters.

### Questions
- The authors assert that this framework eliminates the need for a specific mask generator. However, this claim is unsubstantiated, as MaskCLIP++ still requires a specific mask generator during inference, and the choice of mask generator can significantly influence the final performance.
- The claim that the consistency alignment module can substantially reduce overfitting issues is not well-supported by the experimental results. There is no evidence presented regarding overfitting, making it questionable to attribute overall performance improvements to overcoming these issues..
- While the motivation is effectively articulated in the introduction, additional experimental results are needed to demonstrate how well this work enhances mask classification compared to the original mask generator. Since this work aggregates both the class probabilities of the fine-tuned CLIP and the mask generator, direct comparison becomes challenging.
- In lines 207-210 on page 4, the authors claim that once &r& is optimized to align with the target, the original similarity relationships become disrupted, necessitating the consistency alignment. However, this observation may instead indicate that the original similarity relationships are noisy and require improvement. This perspective aligns with findings in CAT-Seg, where the original similarity was also deemed noisy, leading to the use of aggregation on the similarity matrix.

### Soundness
3

### Presentation
2

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
This paper proposes MaskCLIP++ which uses ground-truth masks during training and can adapt many off-the-shelf segmentation networks during inference. The proposed method significantly reduces the training time while achieving SOTA performances on standard OVSS and OVPS benchmarks.

### Strengths
1. The proposed method, MaskCLIP++, reaches SOTA performances on standard open-vocabulary benchmarks while requiring significantly less training cost and can adapt many off-the-shelf segmentation network (e.g. Mask2Former and FC-CLIP) during inference.
2. The ablation studies presented in this article are thorough and well-structured, offering valuable insights into the impact of each design choice.
3. The proposed module about consistency alignment which enables training with ground-truth masks and inferencing with off-the-shelf segmentor seems novel and interesting to me.

### Weaknesses
1. The experiment results, though SOTA, is only marginally higher than previous SOTA e.g. CAT-Seg and MAFT+. The improvement seems marginal when the number of categories is smaller (e.g. ADE20K150, PC59, PC20). Moreover, I failed to find the performances on closed-vocabulary setting i.e. mIoU/PQ on COCO-stuff/COCO-Panoptic, which the authors should consider reporting these results in supplementary materials.
2. Is the proposed method capable of adapting any class-agnostic mask generator for inference? a) a simple experiments may be to use ground-truth but class-agnostic masks which can serve an upper bound for class-agnostic mask generator; b) if yes, is it possible to extend this work by combining SAM?
3. What is the inference efficiency in terms of FLOPs in comparison to previous methods? 
4. CAT-Seg also benchmarks its approach on the MESS datasets [1], which include domain-specific data distinct from the training source. To further demonstrate the strengths of the proposed method, the authors might consider conducting experiments and providing comparative results with CAT-Seg on this benchmark.

[1] Benedikt et al. What a mess: Multi-domain evaluation of zero-shot semantic segmentation. NeurIPS 2023

### Questions
1. I would like to learn more about the detailed implementation of class inclusion/exclusion in Equation(4). For example, COCO makes a fine-grained distinction among wall-stone, wall-brick, etc but ADE20K considers the super-category wall. From Table 7 in Appendix, it seems that wall is considered as seen category. Is this classification manual or based on text overlapping of super-categories? What are potential impacts that super-categories appear in training source but fine-grained classification is needed in zero-shot datasets? Some qualitative comparisons would be helpful for understanding.
2. I am curious about the method's name "MaskCLIP++". Is there a relationship to MaskCLIP, which employs a pre-trained class-agnostic mask proposal network and uses predicted masks to refine attention masks?

The following are some typos that do not affect my ratings:
1. The paper *Learning to generate text-grounded mask for open-world semantic segmentation from only image-text pairs* appears twice in References.

### Soundness
4

### Presentation
3

### Contribution
3
