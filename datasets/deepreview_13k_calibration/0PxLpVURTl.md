# MIM-Refiner: A Contrastive Learning Boost from Intermediate Pre-Trained Masked Image Modeling Representations

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
We introduce MIM (Masked Image Modeling)-Refiner, a contrastive learning boost for pre-trained MIM models. MIM-Refiner is motivated by the insight that strong representations within MIM models generally reside in intermediate layers. Accordingly, MIM-Refiner leverages multiple instance discrimination (ID) heads that are connected to different intermediate layers. In each head, a nearest neighbor ID objective constructs clusters that capture semantic information which improves performance on downstream tasks, including off-the-shelf and fine-tuning settings.

The refinement process is short and simple -  yet highly effective. Within a few epochs, we refine the features of MIM models from subpar to state-of-the-art, off-the-shelf features. Refining a ViT-H, pre-trained with data2vec 2.0 on ImageNet-1K, sets a new state-of-the-art in linear probing (84.7\%) and low-shot classification among models that are pre-trained on ImageNet-1K. MIM-Refiner efficiently combines the advantages of MIM and ID objectives, enabling scaling ID objectives to billion parameter models using relatively little compute. MIM-Refiner compares favorably against previous state-of-the-art SSL models on various benchmarks such as low-shot classification, long-tailed classification and semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on bridging the gap between large MIM pre-trained models and SOTA methods. The paper first discovers that  MIM models have different types of blocks: those that mainly improve the pre-training objective and others that are responsible for abstraction. Then, the paper proposes a method MIM-Refiner, which adds Instance Discriminator heads on pre-trained MIM models for refinement. The ID heads exploit the intermediate representations to consistently improve the performance of MIM pretrained models. While the performance gains on large dataset full-finetuning are small, the proposed methods show remarkable gains on few-shot settings.

### Strengths
1. The paper first points out the influence of the lightweight decoder on the feature learning of the encoder in MIM methods.
2. The analyzing part is well-written.

### Weaknesses
1. The description of the method and experimental setup needs to be clarified. (a) Which blocks need to be fine-tuned during refinement, or do all blocks need to be fine-tuned? (b) How many epochs are needed to refine different models? (c) What is the structure of the ID head? Answers to all these questions should be contained in the manuscript.
2. Unfair comparison. The paper misses an important baseline - train the original model with 0 heads with the same epochs to demonstrate the importance of refinement (instead of just training more epochs).
3. Some typos. L267-269, see Table 1 instead of Figure 3b.

### Questions
Please refer to the weakness. I believe a clear description of the method and experimental setup is one of the most important things when writing a paper (weakness 1).

Additional question: what does the “relative” in Figure 3(d) mean? Does the value calculated by the performance of ( the i+1 th layer - the i-th layer)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a contrastive learning boosting method called MIM-Refiner to refine the features of pre-trained MIM models. MIM-Refiner leverages multiple instance discrimination heads (ID) which are connected to different immediate layers. Each ID head contains a contrastive loss that captures semantic information to improve the quality of learned representations. By training a few epochs, the features of MIM-Refiner surpass the current MIM models on multiple experiments: on ViT-H with data2vec 2.0 on ImageNet-1K, the accuracy of the proposed method reaches state-of-the-art performance on linear probing and low-shot classification.

### Strengths
1. This paper proposes a detailed analysis of the blocks of MIM models in which different blocks extract features with a specific focus and the most efficient features learned by MIM are from the middle blocks.

2. A contrastive learning-based method called MIM-Refiner is proposed to refine the representation of current MIM models by attaching the middle layers with ID objective. 

3. Experimental results show the effectiveness and generalization ability of MIM-Refiner on downstream tasks.

### Weaknesses
1. As the discussion of end-to-end training, the proposed method MIM-Refiner seems to be a two-step training method, with first step training MIM models and fine-tuning the updated models by incorporating ID heads to middle layers. Practically, this might increase the complexity of the training paradigm and deployment. Is it possible to improve the proposed method with end-to-end training on MIM and ID? If not, what are the potential bottlenecks to circumvent this goal?

2. There is no overview diagram that shows the detailed architecture of MIM-Refiner or how the training diagram goes. The diagram in Figure 4 provides partial information but does not clearly illustrate these points.

### Questions
Please refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
---

## **Summary**

The paper identifies the representation degradation issue in Masked Image Modeling (MIM)-pretrained large foundation models. To address this, the authors propose a simple yet effective method to prevent degradation and further improve the representation quality of MIM methods by adding auxiliary contrastive losses to the last layers of Vision Transformers (ViTs) on top of the MIM objective. The paper provides improved performances with large margins over current state-of-the-art (SOTA) methods through extensive experiments and rigorous analysis, demonstrating the success of the proposed approach.

---

### Strengths
---

## **Strengths**

- The paper is well-written, with clear observations, a well-developed motivation, a straightforward idea, a clearly-stated method, extensive experiments, and comprehensive analysis.
  
- It effectively identifies the representational degradation phenomenon in large visual foundation models pre-trained with MIM self-supervised learning (SSL), providing evidence through multiple experiments.
  
- The proposed method offers a simple and effective solution to prevent this issue and improve the representation quality of MIM SSL.

- Rigorous experiments and analysis are conducted to show the success of the proposed method, with large improvements over current SOTA.

---

### Weaknesses
 
### **Limitations**

1. To prevent representation quality degradation in the last layers of ViTs, the authors experiment with contrastive loss, which requires constructing a queue/pool for positive and negative samples. I noticed the proposed method uses a top 20-NN approach to retrieve positive samples in the queue, which could contribute significantly to the increased training time per step. What's the queue size used? how much does it contribute to the increased training time per step?

2. Since the paper emphasizes preserving the richness of representations, evaluation on dense prediction tasks such as object detection and instance segmentation (OD/IS) would be valuable, in addition to the provided segmentation probing on ADE20K.

   - It would be meaningful to compare the performance of MIM-refiner-pretrained ViT-L on COCO object detection against MAE-pretrained ViT-L following the ViTDet framework [1].

   - [1] Li, Y., Mao, H., Girshick, R., & He, K. (2022, October). *Exploring plain vision transformer backbones for object detection.* In European Conference on Computer Vision (pp. 280-296). Cham: Springer Nature Switzerland.



### Questions
---
Since D2V2 is used as a baseline, does the representation degradation issue also appear in the audio and language domains?

---

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MIM-Refiner, which leverages contrastive learning to boost MIM models. The proposed method is simple and has demonstrated effectiveness in few-shot image classification tasks.

### Strengths
S1: This paper is well-written and easy to follow.

S2: This paper is not the first to point out that the encoder in MIM methods partially performs image encoding and representation learning. A similar conclusion is also discussed in [A], highlighting that MIM methods using a single ViT structure tend to face this issue. The reviewer previously conducted experiments on MAE-B, showing that introducing an additional decoder can effectively alleviate this problem. This paper demonstrates that, for methods like MAE that use an asymmetric encoder-decoder architecture， especially in larger models， a small decoder cannot fully decouple encoding and decoding, providing academic insights.

S3: This paper proposes a simple and effective MIM-Refiner method, refining the later blocks of MIM models to enhance MIM representations effectively.

[A] Context Autoencoder for Self-Supervised Representation Learning.

### Weaknesses
W1: Existing work [A] has shown that fine-tuning MIM models can enhance their representation capability (for image classification), but the improvement under full fine-tuning is minimal. Additionally, MAE has demonstrated significant transfer performance on dense prediction tasks [B] (object detection/instance segmentation). Fine-tuning MIM models with contrastive learning methods is unlikely to bring substantial improvement and may even negatively impact performance. Specifically, the contrastive loss may over-emphasize instance discrimination at the expense of the rich feature representations learned by MIM, which are beneficial for dense prediction tasks. The paper should provide a more thorough analysis of the trade-offs between contrastive learning and MIM objectives, especially in the context of full fine-tuning and dense prediction tasks.

W2: Current vision foundation models, such as DINOv2, exhibit strong patch-level representation learning capabilities and combine MIM and CL. Their learned representations have shown effectiveness in tasks like image classification, pixel classification, and depth estimation. Although this paper discusses the relationship between MIM-Refiner and these models, suggesting that MIM-Refiner can build on them for further improvement, I am concerned that MIM-Refiner may degrade pixel-level representation performance for tasks like semantic segmentation or depth estimation (especially when the backbone is fixed). The concern is that the contrastive learning objective used in MIM-Refiner might not be as effective as the combined MIM and CL approach used in models like DINOv2 for pixel-level tasks, potentially leading to a degradation in performance when the backbone is frozen. The paper needs to provide more evidence that MIM-Refiner does not negatively impact pixel-level representation quality, especially when compared to models that already combine MIM and CL.

### Questions
see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
