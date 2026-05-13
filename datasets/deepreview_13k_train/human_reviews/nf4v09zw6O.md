# Self-Supervised Learning of Intertwined Content and Positional Features for Object Detection

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
We present a novel self-supervised feature learning method using Vision Transformers (ViT) as the backbone, specifically designed for object detection and instance segmentation. Our approach addresses the challenge of extracting features that capture both class and positional information, which are crucial for these tasks. The method introduces two key components: (1) a positional encoding tied to the cropping process in contrastive learning, which utilizes a novel vector field representation for positional embeddings; and (2) masking and prediction, similar to conventional Masked Image Modeling (MIM), applied in parallel to both content and positional embeddings of image patches. These components enable the effective learning of intertwined content and positional features. We evaluate our method against state-of-the-art approaches, pre-training on ImageNet-1K and fine-tuning on downstream tasks. Our method outperforms the state-of-the-art SSL methods on the COCO object detection benchmark, achieving significant improvements with fewer pre-training epochs. These results suggest that better integration of positional information into self-supervised learning can improve performance on dense prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a self-supervised learning method using Vision Transformers (ViT) for object detection and instance segmentation. It addresses the challenge of extracting features with both class and positional information. The method has two main components: (1) a novel positional encoding tied to cropping in contrastive learning, using vector field-based positional embeddings; and (2) masking and prediction, akin to Masked Image Modeling (MIM), applied to both content and positional embeddings. This approach enables effective learning of intertwined content and positional features. Experiments show that it outperforms existing self-supervised methods on the COCO benchmark with fewer pre-training epochs, highlighting the importance of positional information in dense prediction tasks.

### Strengths
- The paper is clearly written and easy to follow.

- The motivation for the method makes sense; exploring the interplay of content and positional features is crucial for instance-level perception.

- Extensive ablation studies validate the effectiveness of each component and justify hyperparameter choices.

- Experimental results demonstrate superior performance on object detection and instance segmentation tasks, outperforming several general self-supervised methods.

### Weaknesses
The main issue with this paper is the adequacy of its experimental setup and comparison framework.

- All comparison methods used in the paper are general self-supervised methods that are not specifically designed for dense prediction tasks. Among them, LOCA is tailored for semantic segmentation, making it difficult to genuinely demonstrate the superiority of the proposed method in terms of object detection/segmentation.

- There are several missing references that would provide a more comprehensive comparison, including:

[1] Yang C, Wu Z, Zhou B, et al. Instance localization for self-supervised detection pretraining[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 3987-3996.

[2] Wang X, Zhang R, Shen C, et al. Dense contrastive learning for self-supervised visual pre-training[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021: 3024-3033.

[3] Li Y, Huang D, Qin D, et al. Improving object detection with selective self-supervised self-training[C]//European Conference on Computer Vision. Cham: Springer International Publishing, 2020: 589-607.

[4] Bar A, Wang X, Kantorov V, et al. Detreg: Unsupervised pretraining with region priors for object detection[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022: 14605-14615.

[5] Cao S, Joshi D, Gui L, et al. HASSOD: Hierarchical adaptive self-supervised object detection[J]. Advances in Neural Information Processing Systems, 2024, 36.

[6] Chen J, Hu M, Li B, et al. Efficient self-supervised vision pretraining with local masked reconstruction[J]. arXiv preprint arXiv:2206.00790, 2022.

Based on this issue, I cannot confirm the core contributions of the proposed method in terms of experimental effectiveness, even though I believe the method is simple yet straightforward.

### Questions
Please further discuss the missing references outlined in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to strengthen the content and positional features of objects in self-supervised learning. It improves the positional embeddings related to the cropping process in self-supervised feature learning methods and introduces masked image modeling (MIM) to handle position embeddings. The effectiveness of the proposed method is validated through experiments on the COCO object detection benchmark and the ADE20K semantic segmentation dataset. However, the organization and clarity of the writing in the paper need improvement.

### Strengths
1. This paper provides a relatively detailed summary of existing SSL (Self-Supervised Learning) methods and their interrelations.
2. By observing the correlation between position information and class features in object detection tasks, the paper proposes position encoding based on the cropping positions of cropped views. This approach incorporates the consideration of global information from the original image and can accelerate convergence.

### Weaknesses
1. Writing Needs Improvement.

  - a) The organization of some sections needs improvement. For example, the related work section introduces too many formulas. It is suggested to move these formulas to a preliminary section and only provide the formulas of the most relevant existing methods to the proposed method.

  - b) There is a lack of abstract summarization for the proposed method. As a result, the description of the operations on features and encodings (Lines 238-250) feels like a plain statement without explaining the underlying motivations and implications. Additionally, there is a lack of necessary summarization after describing the specific processes of the method.

2. The Sufficiency of Experiments Needs Improvement.
- a) According to Table 1, the proposed method achieves better performance with fewer training epochs. However, it is unclear whether it would perform better if more training epochs were used. Additionally, it is not known how other comparison methods perform when using the same number of epochs.

- b) The Experiment section lacks sufficient analysis to explain why the cross-wise position masking strategy is better.

### Questions
1. As stated in Line 309, the proposed method can be adapted to other SSL methods. It is recommended to supplement with additional experiments that demonstrate the generalizability of the proposed method by applying it to other SSL methods.

2. It is suggested to provide more experiments on object detection and instance segmentation datasets, such as those used in DINOv2 and iBOT, to further validate the effectiveness of the proposed method.

### Soundness
3

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
5

### Summary
---

## **Summary**

The paper argues that the key to making self-supervised learning (SSL) effective for object detection (OD) and instance segmentation (IS) lies in capturing both positional and image content information in an intertwined manner. To address this, the authors propose an extension to existing Masked Image Modeling (MIM) approaches, such as iBOT and DINOv2, by predicting masked positional embeddings along with masked image content. Experimental results on the COCO and ADE20K benchmarks demonstrate significantly improved performance compared to general-purpose SSL methods. Ablation studies and detailed analyses further illuminate the effectiveness and characteristics of the method.

---

### Strengths
---

## **Strengths**

- The paper is straightforward and clearly written.
- The method’s design is well-motivated by observations of current approaches.
- The experiments demonstrate significantly improved performance with substantial margins.

---

### Weaknesses
 
### **1. Overstated Motivation**

The motivation behind the proposed method somewhat overstates the “unclear”-ness surrounding current SSL’s effectiveness in downstream tasks. The authors frequently use the term “unclear” when describing SSL’s mechanisms for enhancing performance across various downstream tasks. However, numerous studies have already explored this topic through lenses such as clustering and the information bottleneck theory. Notable examples include:

- [Shwartz-Ziv, R., & LeCun, Y. (2024). *To compress or not to compress—self-supervised learning and information theory: A review*. Entropy, 26(3), 252.](#)
- [Assran, M., et al. *The hidden uniform cluster prior in self-supervised learning.* Proceedings of the Eleventh International Conference on Learning Representations.](#)
- [Zhou, D., et al. (2022). *Understanding robustness in vision transformers.* In International Conference on Machine Learning, 27378–27394.](#)

It is widely recognized that SSL’s ability to capture semantically meaningful information reflecting both the global and local distribution of pretraining data is essential for generating transferable and generalizable representations.

---

### **2. Limited Novelty**

The proposed method is a straightforward extension of existing approaches, such as DINOv2, which itself builds upon iBOT. This method treats position embeddings (presented as a vector field in this paper) as content to be recovered alongside the masked image content.

---

### **3. Counter-Intuitive Positional Embedding (PE) Effectiveness**

The effectiveness of the proposed positional embedding (PE) approach is somewhat counter-intuitive. From my understanding, this proposed PE essentially introduces “absolute” positional information with respect to a larger virtual image, whereas existing methods typically inject “relative” positional information within a crop. However, absolute positional information is generally less desirable in current object detectors, which favor relative positional information. For instance, the bounding box head of Mask R-CNN in ViTDet regresses offsets and scales relative to each anchor rather than the absolute positions of bounding boxes within the image, as this approach generalizes better across different object scales and positions.

Although the paper provides an ablation study on the use of the proposed PE, further analysis is needed to clarify its success. For example, what specific type of positional embedding field is employed? It would also be valuable to compare results across different types of vector fields, such as sinusoidal position embedding fields and Rotary Position Embedding (RoPE) fields:

- [Su, J., et al. (2024). *Roformer: Enhanced transformer with rotary position embedding*. Neurocomputing, 568, 127063.](#)

---

### **4. Performance on Image-Level Tasks**

In the proposed framework, the ViT model extracts both image-level and patch-level representations. Consequently, the resulting model should generalize across both dense prediction tasks (such as object detection and instance segmentation) and image-level tasks. However, the paper presents results only for object detection and instance segmentation. To fully assess the overall quality of the learned representations, standard image-level evaluation protocols should also be included. This would provide a more comprehensive understanding of the model’s generalization capabilities across different types of tasks.

---

### **5. Comparison with Recent SSL Methods**

The paper does not discuss or compare with many recent SSL methods specifically designed for dense prediction tasks or employing multi-level strategies, which are directly relevant to the proposed framework. Notable methods include:

- [Li, C., et al. (2021). *Efficient self-supervised vision transformers for representation learning*. arXiv preprint arXiv:2106.09785.](#)
- [Yun, S., et al. (2022). *Patch-level representation learning for self-supervised vision transformers*. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 8354-8363).](#)
- [Zhou, P., et al. (2022). *Mugs: A multi-granular self-supervised learning framework*. arXiv preprint arXiv:2203.14415.](#)
- [Zhang, S., et al. (2023). *Patch-level contrasting without patch correspondence for accurate and dense contrastive representation learning*. arXiv preprint arXiv:2306.13337.](#)
- [Su, Q., et al. (2024). *FLSL: feature-level self-supervised Learning*. Advances in Neural Information Processing Systems, 36.](#)
- [Stegmüller, T., et al. (2023). *Croc: Cross-view online clustering for dense visual representation learning*. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 7000-7009).](#)
- [Lebailly, T., et al. (2023). *CrIBo: Self-Supervised Learning via Cross-Image Object-Level Bootstrapping*. arXiv preprint arXiv:2310.07855.](#)

These works are highly relevant and should be included in the Related Work section or incorporated into the experimental comparisons to better situate the proposed method within the current landscape of SSL techniques.

---

### **6. Classification of Techniques in Related Work**

The classification of techniques in the Related Work section could be improved. The methods categorized under “dense feature learning” are essentially patch-level or multi-level SSL approaches, incorporating both image-level and patch-level representations. In contrast, the methods in the “Patch-level feature learning” category are more accurately described as Masked Image Modeling (MIM) approaches, which align more closely with generative methods due to their focus on reconstructing masked content. Adjusting these classifications would provide clearer distinctions between different SSL paradigms.


### Questions
1. See weakness 3
2. What is the training duration compared to iBOT? What are the specifications of the devices being used? Please provide them in the paper.

### Soundness
3

### Presentation
3

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
The paper presents a new technique for masked image modelling. Instead of only masking the content, they also mask the positional encoding. Additional, the authors replace the traditional positional encoding with positional encoding that is encoded w.r.t. to the original image input grid (before taking crops). The empirical results confirm the usefulness of their method.

### Strengths
-The paper is mostly well writen and easy to follow.

-Table 2 is convincing, it provides empirical evidence for the usefulness of their method.

### Weaknesses
-I think the novelty of the novelty of the "positional encoding tied to the cropping process" is overstated. Other works have already used it for correspondence matching in dense-representation learning e.g. [1], [2], [3]. I would like to see a better comparison of these approaches in the related works section.

-The authors state:
352, 491: “Although semantic segmentation is not our primary focus” but also:
013: “We present a novel self-supervised feature learning method using Vision Transformers (ViT) as the backbone, specifically designed for object detection and instance segmentation”
         --> the claims should be reformulated in a coherent way.

-Footer 1 points to a section with a definition of "effective epoch". "effective epoch" is not found in that section. There is another footer in that section with the definition. This should be made easier for the reader.

-239: methods

-483: that learns pre-trained weights --> either they are learned, or pretrained

-There are too many footnotes e.g. 4,5,6, it makes it hard to read.

### Questions
-What you are trying to acheive is to have relative positional encoding from one crop, to the other. By resizing and shifting, you're essentially marginalizing over all scales and starting grid position. There should be a cleaner way to encode these relative encodings, what do you think?

-How is e[POSMASK] defined?

### Soundness
3

### Presentation
3

### Contribution
2
