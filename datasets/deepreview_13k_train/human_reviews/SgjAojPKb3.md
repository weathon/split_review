# OpenNeRF: Open Set 3D Neural Scene Segmentation with Pixel-Wise Features and Rendered Novel Views

- Decision: Accept
- Scores: 5, 8, 5, 6

## Abstract
Large visual-language models (VLMs), like CLIP, enable open-set image segmentation to segment arbitrary concepts from an image in a zero-shot manner.
This goes beyond the traditional closed-set assumption, \ie, where models can only segment  classes from a pre-defined training set.
More recently, first works on open-set segmentation in 3D scenes have appeared in the literature.
These methods are heavily influenced by closed-set 3D convolutional approaches that process point clouds or polygon meshes.
However, these 3D scene representations do not align well with the image-based nature of the visual-language models.
Indeed, point cloud and 3D meshes typically have a lower resolution than images and the reconstructed 3D scene geometry might not project well to the underlying 2D image sequences used to compute pixel-aligned CLIP features.
To address these challenges, we propose \name{} which naturally operates on posed images and directly encodes the VLM features within the NeRF. This is similar in spirit to LERF, however our work shows that using pixel-wise VLM features (instead of global CLIP features) results in an overall less complex architecture without the need for additional DINO regularization. 
Our \name{} further leverages NeRF's ability to render novel views and extract open-set VLM features from areas that are not well observed in the initial posed images.
For 3D point cloud segmentation on the Replica dataset, \name{} outperforms recent open-vocabulary methods such as LERF and OpenScene by at least $+4.9$ mIoU.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores a similar paradigm to LeRF (Language-embedded radiance fields). Rather than distilling CLIP features to NeRF, rather it uses a different backbone i.e. OpenSeg to distill OpenSeg features to the 3D using NeRFs. The idea of distilling similar open-set features to 3D has been shown by OpenScene which required 3D meshes as input 3D representation, however, the paper studies it in the setting of Neural Radiance Fields which requires posed 2D images as input. Qualitative open vocabulary segmentation comparisons are shown on the Replica dataset coupled with quantitative comparisons with baselines like LeRF and OpenScene

### Strengths
The approach discussed very relevant problems i.e. distilling open-set 2D features to the 3D domain and moving away from traditional pipelines that work with a known number of categories i.e. approaches like Semantic-NeRF and Panoptic NeRF etc. The main benefits/strengths of the approach are as follows:

1. Qualitative comparison with LeRF and Open-Scene clearly shows better segmentation results despite the fact that LeRF was not designed for segmentation (which should be clearly pointed out)

2. Clearly better quantitative results on all, head, common, and tail sets

3. A good measure of uncertainty to improve the open-set feature field distillation into 3D.

### Weaknesses
1.  Though the uncertainty measure is sound, I wonder if this improves LeRF and OpenScene's performance as well. A similar measure was introduced in Semantic-NeRF and the authors didn't highlight the difference between their formulation and Semantic NeRF's formulation. 

2. This looks like an incremental work that extends LeRF by using a different encoder backbone which is very straightforward to implement. Can the authors justify it with really good segmentation performance on long tail in-the-wild queries etc? I didn't see that comparison

3. Not many in-the-wild examples could be seen in the paper. Replica dataset is easier since we have perfect viewpoint annotations. I wonder if the performance stays steady or breaks for more in the wild examples where there are imperfect viewpoint annotations. 

4. Does uncertainty measure really help? What if the initial NeRFs are not that good? Features tend to break for those viewpoints/areas. Do the authors have improved results in those cases?

### Questions
Please see all the questions in the weakness section. Overall I would have liked to see a thorough comparison with LeRF and what technical improvement the work bring (in addition to changing the pre-trained backbone), a comparison with Semantic-NeRF's uncertainty formulation, more in the wild examples and examples where the quality of NeRF is not that good and do the semantic features break or does uncertainty help in those areas

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces OpenNeRF, an innovative approach for superior open-set 3D semantic scene understanding. OpenNeRF demonstrates its suitability for detecting small long-tail objects, surpassing mesh-based representations in performance. Additionally, OpenNeRF effectively represents interesting scene parts, leading to improved segmentation performance.

### Strengths
1. The proposed OpenNeRF approach significantly improves 3D semantic segmentation results compared to baseline methods such as LERF and OpenScene. It can also detect challenging long-tail classes ignored by other methods.
2. Confidence estimation and analysis of novel views bring new insights for improving the Open-set 3D scene understanding.
3. OpenNeRF can be queried for arbitrary concepts, including object properties (eg. reflective, soft) and material types (eg. wood, cotton), showcasing its versatility. It shows impressive results in the wild scene using a phone scanner.

### Weaknesses
1. The performance drop when rendering novel views from random positions suggests that the approach is sensitive to the quality and meaningful context of the additional views. This sensitivity could be problematic in scenarios where obtaining high-quality, contextually relevant novel views is challenging or expensive. The reliance on specific view characteristics might limit the method's applicability in more unconstrained environments.


### Questions
1. Could you provide more details on the evaluation protocol used to compare explicit-based (mesh/point cloud) and implicit-based (NeRF) methods for open-set 3D semantic segmentation? What were the key findings of this evaluation?
2. Have you considered the scalability and computational efficiency of OpenNeRF? How does it perform in terms of runtime and memory requirements compared to other methods?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a NeRF-based scene representation for open-set 3D semantic scene understanding. The method extends previous work by leveraging pixel-aligned features and a mechanism to identify regions that require generating novel views. These additional views of the scene allow the proposed approach to extract more open-set features and improve the overall understanding of the 3D semantic scene. The results have been tested on the Replica dataset and have outperformed a mesh-based baseline and a NeRF-based baseline.

### Strengths
* The paper is well-written and justified. All the technical details are well-elaborated.
* The concept of using novel view synthesis capabilities to extract additional visual-language features for better scene understanding is interesting and straightforward.
* The qualitative results appear satisfactory and the quantitative results outperform OpenScene and LERF.

### Weaknesses
My main concern is regarding the evaluation:
* While the Replica dataset may be challenging for long-tailed settings, it would be great to evaluate on larger-scaled datasets and outdoor benchmarks such as Matterport3D, ScanNet, and nuScenes.
* One of the main contributions of this work is the use of novel view synthesis to extract additional visual-language features. To ensure the quality of the learned features, it seems necessary to evaluate the quality of the rendered views and their effect on scene understanding.
* To better evaluate the proposed method, it would be better to compare it with 2D methods such as LSeg, OV-Seg, and ODISE, as well as other 3D methods including Feature Field Distillation, Semantic-NeRF, and Panoptic Lifting (disregard whether these methods are open or closed-set).


Some questions regarding the confidence estimation and novel camera view selection:
* The uncertainty map in Figure 3 indicates that the door and cabinet are the most uncertain points, while the generated novel pose in Figure 2 seems to focus primarily on the table. Given high uncertainty points, how are the camera views sampled?
* Although there is a positive correlation between per-point uncertainty and per-point error, the heat maps appear to emphasize all areas other than the wall and floor. It is also intriguing that the peaks of uncertainties don't correspond to object boundaries, but rather the entire object. It would be better to demonstrate more samples to showcase these findings.

### Questions
Please see the weaknesses part for my concern and confusion.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to address the task of 3D open set detection by harassing implicit reconstruction methods, and specifically NeRF.
If I am not mistaken, the method boils down to adding supervision/prediction-head of per-pixel CLIP features in addition to the RGB/color head, while keeping the per-voxel density $\sigma$ prediction used in NeRF. 
The authors use depth supervision, when available, as done in previous works.

The devil lies, as always, in the details of the training regime, and the authors stress some details that are important to make the network converge to the presented results:
The authors use OpenSeg feature maps which are more localized and therefore do not supervise them in a multi-scale fashion.
Additionally, one should refrain from using such features near the image edge as they are less stable.
Finally, one of the main points in the training process, the authors claim that training on novel views (generated by a trained NeRF) makes as big difference. Specifically, novel views are selected to minimize the uncertainty of the OpenSeg features, measured as generalized variance on the in 3D. This help mitigate areas where open-set features "disagree" from multiple viewpoints.

The experimental section evaluates the method compared to the previous 3D open-set approaches, which are all explicit.
The authors divide the labels into 3 groups by frequency, which better emphasized the strength of the propose method on rare ones.

### Strengths
* The paper was rather easy to follow, for an experienced NeRF reader (which is reasonable these days :-) ).
* The base of the method is rather straight forward to understand (adding CLIP predictions)
* The authors indicate uncertainty estimation of the open-set head is  a strong signal to help the network converge, with help of NeRF novel views.
* The results show the advantage of implicit methods over explicit ones
* The ablation study helps to understand which part of the training regime made the difference.

### Weaknesses
Many of the details of the paper were presented in previous works (e.g. per-pixel feature supervision was presented in NeRF-SOS fo DINO). and a big part of the novelty here is in the details of applying them to 3D segmentation.
This alone does not prevent acceptance, IMHO.

### Questions
A question on the novel-view based training: 
Can you please comment on the seemingly bootstrapped nature of this approach?
In other words - a NeRF model has to be trained in the first place to generate novel views, and these novel views are then trained to predict open-set features?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
