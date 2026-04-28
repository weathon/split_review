# ViT-UWA: Vision Transformer Underwater-Adapter for Dense Predictions Beneath the Water Surface

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Vision Transformer (ViT) and its variants have witnessed a significant success in computer vision. However, they do not perform well in underwater dense prediction tasks due to challenges like complex underwater environments, quality degradation, and light scattering in underwater images. To solve this problem, we propose the  Vision Transformer Underwater-Adapter (ViT-UWA), the first detail-focused and adapted ViT backbone for underwater dense prediction tasks, without requiring task-specific pretraining. In ViT-UWA, we first introduce High-frequency Components Prior (HFCP) to add high-frequency information of underwater images to the plain ViT, which can help recover and capture lost high-frequency information of underwater images. Then, we propose an Detail Aware Module (DAM) to obtain a detail-focused multi-scale convolutional feature pyramid, which can be used in kinds of dense prediction tasks. Through the ViT-CNN Interaction Module (VCIM), we achieve bidirectional feature fusion between ViT and CNN. We evaluate ViT-UWA on multiple underwater dense prediction tasks, including semantic segmentation, instance segmentation, and object detection. Notably, with only ImageNet-22K pretraining, our ViT-UWA-B yields state-of-the-art 46.4 box AP and 44.2 mask AP on USIS10K dataset. We hope ViT-UWA could provide a new backbone for future research on underwater dense prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes adapted backbone for the Vision Transformer (ViT) architecture termed as Vision Transformer Underwater Adapter (ViT-UWA) specifically designed for dense prediction tasks in images acquired underwater. The two salient features of the proposed ViT-UWA are (a)  its ability to recover and capture high-frequency information in underwater images via the introduction of a high-frequency components prior (HFCP) and (b) it ability to capture features at multiple scales of detail for dense prediction tasks via a detail aware module (DAM) that is based on a multi-scale detail-focused convolutional feature pyramid.

### Strengths
The paper proposes a useful enhancement of the standard ViT architecture. The experimental results are encouraging when compared to other state-of-the-art (SOTA) methods for dense prediction in underwater imagery.

### Weaknesses
The high frequency signal attenuation observed in underwater imagery is very dependent on the environmental conditions. The proposed method should have incorporated underwater image signal correction that is based on the physics of light scattering under water such as the Sea-Thru algorithm [1]. The current approach does not explicitly model the wavelength-dependent attenuation and scattering effects that are inherent to underwater environments. This omission could limit the generalizability of the method across diverse underwater conditions, such as varying water turbidity, depth, and lighting. Furthermore, the method does not account for the potential color shifts and reduced contrast that are common in underwater images, which could impact the performance of the high-frequency component prior (HFCP) and detail aware module (DAM).

### Questions
The authors should clarify how they have addressed or would address the underlying physics of underwater signal correction.

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
In this paper, a novel underwater dense prediction backbone by combining the plain ViT. Besides, the high-frequency components prior and the detail aware module are proposed. The proposed method was trained and tested on multiple datasets and achieved comparable results. Finally, multiple ablation experiments illustrate the effectiveness of high-frequency components prior and the detail aware module in this method.

### Strengths
1. In this paper, multiple experiments were conducted on different datasets and compared quantitatively and qualitatively with multiple methods.
2. This paper is generally smooth, and the paper is easy to understand.
3. The visualization results of the method proposed in the paper look better than other compared methods.

### Weaknesses
1.	In ablation experiments, only indicators show whether the high-frequency module is useful or not, but there is a lack of visuals to show that the module can capture high-frequency information.
2.	In the ablation experiment, only the DAM was removed, but other simple CNN structures or Transformer structures were not considered to replace the DAM, which did not well illustrate the uniqueness and effectiveness of the module

### Questions
1. Can you show some visuals to illustrate that HFCP can capture high-frequency information?
2. Can you replace DAM with other simple structures to illustrate the uniqueness and effectiveness of your DAM?

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
This paper introduces a new backbone, ViT-UWA, specifically designed for underwater vision tasks. ViT-UWA consists of two branches: a ViT branch and a convolutional branch, which leverage the ViT-CNN Interaction Module (VCIM) to facilitate information sharing between them. Moreover, the ViT branch incorporates high-frequency components as additional input, while the CNN branch utilizes High-frequency Detail Convolution (HFDConv) to focus details. The model has achieved good results in several underwater tasks, such as object detection and instance segmentation.

### Strengths
1. The paper is well written, and the methods are introduced very clearly.
2. The paper conducted experiments on many tasks, demonstrating the performance advantages of ViT-UWA.

### Weaknesses
1. The biggest drawback of this paper is the lack of originality; the proposed ViT-UWA is composed of existing module combinations, such as the adaptive DC in HFDConv and the Deform Attention in VCIM. The so-called HFCP is merely the concatenation of the high-pass filtered result of the original image with the original image input to the model. Therefore, I believe the contribution of this paper to the community is insufficient.
2. Although ViT-UWA is specifically designed for underwater tasks, some unique designs, such as high-frequency components and detail information, are important in any scenario. However, ViT-UWA performs mediocrely on the Coco dataset in Table 10, while it performs well in underwater scenes. The authors' motivation for the model design does not convince me, and the reason for ViT-UWA's better performance in underwater scenarios remains unclear.

### Questions
1. Should the phrase "... improve by 2.3 and 0.6 AP" in line 504 be changed to "decrease by 2.3 and 0.6 AP"?
2. What would happen if HFCP were directly removed from Table 7 instead of being replaced by USUIR? Additionally, have any better supervised underwater image enhancement methods been tried instead of the unsupervised USUIR method, which often performs worse than supervised methods in many scenarios?
3. Why does VCIM use Deform Attention instead of ordinary cross attention?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the dense prediction tasks (semantic segmentation, instance segmentation and object detection) from underwater images via an adapted Vision Transformer (ViT) model. The work (named ViT-UWA) adds the High-Frequency Component Prior (HFCP) into the tokens for the plain ViT, and designs two modules of Detail Aware Module (DAM) and ViT-CNN Interaction Module (VCIM), where DAM is devised to extract detail-focused multi-scale features for VCIM and VCIM interacts with the plain ViT to fuse and refine the features for dense predictions. The experiments were conducted on three underwater image datasets, covering semantic segmentation, instance segmentation and object detection, compared with existing general ViT adapters and underwater dense prediction methods.

### Strengths
1. The effectiveness and efficiency of the proposed method seems good compared to the related works (Figure 2).
2. The proposed method ViT-UWA has advantages to adapt the underwater images with specific degradation on the details (Figure 3).

### Weaknesses
1. While the proposed method achieves good performance, it seems that the claimed contributions, i.e., HFCP, DAM and VCIM, are designed by considering some related works, thus it is somewhat questionable about the novelty of the design.
2. For efficiency evaluation, it's better to consider the aspects of Parameters, FLOPs, as well as training and inference time, especially the FLOPs and inference time for real-word applications.
3. The design seems to only consider the detail loss (HFCB and DAM) on underwater images, while the other degradations caused by the light absorption and scattering on underwater images are not considered, so how does the model learn these different degradations for dense prediction tasks.

### Questions
1. What are the specific differences on each contribution compared to existing similar works?
2. Please consider to evaluate the efficiency towards real-world applications.
3. How does the proposed model learn different degradations on underwater images for dense prediction tasks?
4. Please provide the discussion about the SAM 2 and proposed ViT-UWA.

### Soundness
3

### Presentation
3

### Contribution
3
