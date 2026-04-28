# Swift4D: Adaptive divide-and-conquer Gaussian Splatting for compact and efficient reconstruction of dynamic scene

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Novel view synthesis has long been a practical but challenging task, although the introduction of numerous methods to solve this problem, even combining advanced representations like 3D Gaussian Splatting, they still struggle to recover high-quality results and often consume too much storage memory and training time. 
In this paper we propose Swift4D, a divide-and-conquer 3D Gaussian Splatting method that can handle static and dynamic primitives separately, achieving a good trade-off between rendering quality and efficiency, motivated by the fact that most of the scene is the static primitive and does not require additional dynamic properties. Concretely, we focus on modeling dynamic transformations only for the dynamic primitives which benefits both efficiency and quality. We first employ a learnable decomposition strategy to separate the primitives, which relies on an additional parameter to classify primitives as static or dynamic. For the dynamic primitives, we employ a compact multi-resolution 4D Hash mapper to transform these primitives from canonical space into deformation space at each timestamp, and then mix the static and dynamic primitives to produce the final output. This divide-and-conquer method facilitates efficient training and reduces storage redundancy. Our method not only achieves state-of-the-art rendering quality while being 20× faster in training than previous SOTA methods with a minimum storage requirement of only 30MB on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The sources describe Swift4D, a novel method for reconstructing dynamic scenes by separating static and dynamic elements and using a 4D hash grids to model the temporal information of dynamic Gaussian points. The separation improves efficiency, reducing both storage requirements and training time, while achieving strong rendering quality in various dynamic scene scenarios. The authors test their method on  N3DV, MeetRoom and Basketball court datasets and compare to different recent works.

### Strengths
- The paper is overall well written and easy to understand. The authors provide detailed descriptions of the methodology and experiments.
- According to the quantitative evaluation, the method performs favourably to competing approaches in image quality as well as optimization time.
- The idea is relatively simple of static and dynamic decomposition, but appears to be effective in terms of speed.

### Weaknesses
 - A key component of this work is the dynamic and static decomposition. The method introduces a dynamic level parameter that is optimized for each gaussian. As explained in section 3.2, a 2D dynamic-static pixel Mask is computed from the training video by leveraging the temporal standard deviation of each pixel. However, since the video can have camera motion as well as dynamic elements that yield varying the pixel intensity it is unclear to me how the standard deviation can serve as good criterion to  differentiate dynamic scene elements from static ones. Does this criterion work well on videos with strong camera motion?
- The authors propose a temporal pruning strategy, it would be good to discuss at some point existing pruning strategies, e.g. LightGaussians (Fan et al. NeurIPS 2024), and the relation ship the proposed pruning method.
- In the supplementary material videos, there seem to be artifacts of vanishing dynamic elements. In 2_baskball2.mp4 some players vanishing from frame to frame and it appears to have temporal inconsistencies, that questions the effectiveness of the method. Is this a common issue?

### Questions
- Please comment on the  Weaknesses above.
- How can the model differentiate between specular reflections and dynamic elements?

### Soundness
2

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
4

### Summary
This paper proposes Swift4D, which extends 3DGStream with a static & dynamic decoupling strategy. Doing this significantly reduced the model size and improved the rendering quality. The authors also introduce other tricks like  spatio-temporal structure modeling and adjusted density control.

### Strengths
* The motivation and technique design for this paper is straightforward and reasonable. Decoupling static and dynamic contents is an intuitive approach when dealing with real dynamic scenes. Although the approach is questionable, it may help researchers to understand the problem better and leverage the explicit structure of 3DGS.
* The experiment results on different datasets show improvements in various aspects, like training time and PSNR, though the FPS is lower, and this is not an on-the-fly method.
* The writing and illustration of this paper is pretty clear to me.

### Weaknesses
 * One critical weakness is the implementation of decoupling static and dynamic parts. Specifically, they use 2D supervision to build the dynamic factor. However, the way they build 2D masks is just to calculate the temporal variance of each pixel, which should lead to problems when dynamic movements happen in textureless regions. These regions can easily be recognized as static parts. Such a phenomenon could be observed in the sear_steak_static result of the supplementary, where part of the cloth is classified as static. In addition, calculating the variance throughout the entire time could cause problems in long-sequence video. The temporal variance approach is inherently sensitive to the chosen time window; a short window may miss slow-moving dynamic elements, while a long window might incorrectly classify areas with illumination changes as dynamic. Furthermore, the method does not account for occlusions, which could lead to inaccurate dynamic masks, especially when dynamic objects move behind static ones.
* It seems that this work can't deal with single-view videos like DNeRF. This could be a general limitation as it's hard to deploy and compare with other methods that can deal with such cases (e.g., SCGS). In addition, it needs to be trained offline, making the comparison with 3DGSStream kind of unfair. The offline nature of the training also limits its applicability to real-time scenarios, where on-the-fly adaptation to new frames is crucial. The method's reliance on pre-computed variance masks also means that it cannot easily adapt to changes in the scene's dynamics after training.
* To me, the result in Fig.7 does actually demonstrate the sensitivity of the dynamic threshold, where it affects the PSNR a lot. I am worried about the generalizability of the method since it's tested on scenes with similar dynamic-static compositions. The lack of a principled way to determine the optimal threshold is a significant concern. The method's performance could degrade significantly if applied to scenes with different dynamic-static ratios or more complex dynamic patterns. The experiments should include a more diverse range of scenes to validate its robustness.

### Questions
As described in weakness, my questions mainly focus on the generalizability to texture-less regions, highly dynamic videos (with different static-dynamic compositions), and long-term videos.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a 4D Gaussian representation for dynamic scenes, utilizing a learned deformation field to model Gaussian dynamics. To reduce the redundancy in dynamic learning, the method employs a decomposition strategy to separate dynamic and static elements. For the dynamic components, 4D spatiotemporal coordinates query a 4D hash grid, retrieving features from multi-resolution grids. An MLP then predicts the residual values of Gaussian attributes to capture the dynamics. By isolating dynamic from static components, this streamlined model efficiently handles dynamic modeling while occupying less space.

### Strengths
1. Decomposing static and dynamic elements is beneficial, effectively reducing the model's learning burden and increasing inference speed, as shown in Table 3. Notably, this separation is also present in the concurrent work GauFRe (Liang et al.) and the published work SC-GS (Huang et al.). This concept is a major contribution to GauFRe and a detailed implementation in SC-GS. Citing these methods when discussing this idea is appropriate.

2. The pruning strategy in Section 3.4 is innovative. Gaussian Splatting and NeRF, based on Multi-View Stereo (MVS) principles, converge when multi-view images reach a photometric consensus. An isolated Gaussian point, recognized by only a few views, tends to become a floating artifact, causing overfitting. This insightful point is valuable and inspires the community.

The two points already make me inclined to accept the paper, but there are some concerns. Please refer to the weaknesses section.

### Weaknesses
The experimental results and citations are insufficient. The FPS of Swift4DLite (Ours) is missing in Table 1, with no explanation provided. Additionally, the rendering speed is relatively slow, similar to 4DGS (Yang et al.) and SpaceTimeGS, with comparable rendering quality. The training time for SpaceTimeGS reported in Table 1 is too long; it should be under an hour. The FPS of SpaceTimeGS is also lower than I expected (130+). Moreover, several closely related works are not compared or cited:

1. Huang, Yi-Hua, et al. "SC-GS: Sparse-controlled Gaussian splatting for editable dynamic scenes." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
2. Yang, Ziyi, et al. "Deformable 3D Gaussians for high-fidelity monocular dynamic scene reconstruction." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
3. Lin, Youtian, et al. "Gaussian-flow: 4D reconstruction with dynamic 3D Gaussian particles." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

I recommend at least including comparisons with [1] and [3], as these methods model Gaussian dynamics using spatially and frequency-compact bases, respectively. Additionally, SC-GS achieves high FPS in rendering images by inferring the motion of sparse control points, according to their Supp.

### Questions
I hope the author can respond to my concerns and suggestions mentioned in the weaknesses section. If there are any issues with the experimental results, recommended citations, or comparisons, I would appreciate an explanation.

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
4

### Summary
This paper presents a Gaussian-splatting-based approach for dynamic scene reconstruction. It first builds a canonical space and decomposes the scene into static and dynamic components. Swift4D leverages a compact hash grid to model the deformations within the dynamic components. The proposed method includes a mechanism for identifying dynamic Gaussians and controlling density. Experimental results demonstrate that this method outperforms others.

### Strengths
The authors present an innovative approach to decomposing scenes into static and dynamic components by introducing a novel Gaussian attribute combined with alpha blending. To the best of my knowledge, this is the first method to leverage Gaussian splatting for scene decomposition. The results demonstrate its effectiveness on the datasets used, achieving high-quality rendering.

### Weaknesses
The primary concern regarding this paper is the lack of sufficient comparisons. While the authors assert that their method is suitable for dynamic scenes, the datasets utilized predominantly feature forward-facing scenes with limited movements. Although the VRU dataset is a multi-view dataset that captures inward-looking scenes, the authors did not provide quantitative comparisons involving it. Additionally, there are other multi-view datasets [1, 2] on which Swift4D could be evaluated, particularly D-NeRF [1], which has been employed in various deformation-based dynamic neural rendering methods that could serve as points of comparison.

The authors mention other methods, Liang et al. (2023) and He et al. (2024), that are also doing static-dynamic decomposition. However, it would be more beneficial to compare their methodologies with the proposed method through quantitative experiments rather than relying solely on qualitative descriptions.

Furthermore, the video results from the VRU dataset exhibit noticeable abrupt scene changes, likely due to the segmentation processing of the video. The authors should address this phenomenon in the paper.

### Questions
This paper has some merits. However, the scope and limitations of the proposed method are not clearly defined.

### Soundness
4

### Presentation
3

### Contribution
2
