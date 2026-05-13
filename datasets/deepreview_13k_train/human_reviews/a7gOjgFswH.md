# G4Seg: Generation for Online Segmentation Refinement with Diffusion Models

- Decision: Reject
- Scores: 5, 6, 6, 5, 5

## Abstract
This paper considers the problem of utilizing a large-scale text-to-image diffusion model to tackle the challenging Inexact Segmentation (IS) task. Unlike traditional approaches that rely heavily on discriminative-model-based paradigm or dense visual representations derived from internal attention mechanisms, our method focuses on the intrinsic generative priors in Stable Diffusion~(SD). Specifically, we exploit the pattern discrepancies between original images and mask-conditional generated images to facilitate a coarse-to-fine segmentation refinement by establishing a semantic correspondence alignment and updating the foreground probability. Comprehensive quantitative and qualitative experiments validate the effectiveness and superiority of our plug-and-play design, underscoring the potential of leveraging generation discrepancies to model dense representations and encouraging further exploration of generative approaches for solving discriminative tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an image segmentation method using a pretrained text-to-image diffusion model, specifically Stable Diffusion 2.1. Given a text prompt with a class label, which conditions the image generation in UNet layers, it computes a semantic difference between the original image and a mask-conditional generated image after a one-step denoising step. This discrepancy, which is computed by Hausdorff distance, is employed to update the foreground probability of each pixel. Initial coarse segmentation follows the settings in the selected baselines.

### Strengths
This paper provides a training-free method for open vocabulary single-class segmentation.

### Weaknesses
I carefully reviewed the paper. Rather than an extensive list of less critical and debatable issues, I will concentrate on the most significant concerns that influence my rating. My focus will be on the following three limitations:

1) The reliance on a specific class label in the text prompt limits this method to only a single category for a given image. It is not clear how this method extends multiple classes. Running the proposed method multiple times with multiple yet separate class labels would face the problem of post-consolidating, most likely handling contrasting segmentation results outside the diffusion steps, which seems non-optimal.  

2) The main idea is that, given an imperfect segmentation mask, the generated image will have a discrepancy from the original image. This drives the intuition given in the paper that with a more accurate segmentation mask, the probability of generating the original image is more likely to be maximized. How this is implemented is described in 3.2.2 and Appendix E. Some explanation is given 317-323; however, the explanation also highlights the reliance on a good initial segmentation mask. The ablation study does not present how sensitive the proposed method is to the initial segmentation accuracy.    

3) The segmentation mIoU improvement is marginal. Besides, the comparisons with stronger SOTA are missing OVAM (CVPR 2024) and CoDe (CVPR 2024). DeOP (ICCV 2023), which could be another interesting baseline.

### Questions
How could this method extend to other UNet-based text-to-image diffusion models beyond SD2.1 (such as Wurstchen, SSD-1B, SDXL, SD1.5, etc.) and their distilled versions (such as single or reduced step variants, LCM versions)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents G4Seg, a novel approach leveraging large-scale pretrained diffusion models for refining inexact segmentation without additional training. The method capitalizes on discrepancies between an original image and its generated counterpart conditioned on a coarse segmentation mask to refine segmentation results. By applying a semantic correspondence alignment and employing pixel-wise probability updates, G4Seg proposes a training-free, plug-and-play solution applicable to weakly supervised and text-supervised semantic segmentation tasks.

### Strengths
1. The proposal to use generative discrepancies from diffusion models for segmentation refinement is unique and well-explored, emphasizing the potential of generative models in traditionally discriminative tasks.

2. The method’s independence from training requirements is noteworthy, making it resource-efficient and broadly adaptable.

3. Comprehensive evaluation across standard datasets (PASCAL VOC12, PASCAL Context, MS COCO) demonstrates consistent performance improvements, achieving state-of-the-art results in certain scenarios.

### Weaknesses
1.  While results are promising, deeper comparisons with similar methods (e.g., training-free segmentation approaches) could be emphasized to highlight advantages and potential trade-offs more explicitly. Specifically, the paper should delve into the nuances of how G4Seg's approach to leveraging generative discrepancies differs from other training-free methods that might employ attention mechanisms or feature prototypes derived from diffusion models. A more thorough comparison should discuss the specific architectural choices and algorithmic differences that lead to the observed performance gains or losses.

2. Although tested on popular benchmarks, it is not entirely clear how G4Seg would scale to other datasets. The paper lacks a discussion on the potential impact of domain shift or variations in image complexity on the performance of G4Seg. It would be beneficial to see an analysis of how the method performs on datasets with different characteristics, such as those with significantly different object scales, lighting conditions, or levels of image clutter. Furthermore, the paper should explore the limitations of the method when applied to datasets with a large number of categories, as the semantic correspondence alignment might become more challenging with increased semantic diversity.

3. While computational cost is discussed, there is limited exploration of scenarios where G4Seg may not perform optimally (e.g., highly cluttered or ambiguous images). The paper should include a more detailed analysis of failure cases, specifically focusing on situations where the initial segmentation is poor or where the generative process struggles to produce a clear correspondence with the original image. It would be valuable to understand how the method behaves when faced with ambiguous object boundaries or when the initial mask is significantly misaligned with the actual object.

### Questions
Please see weaknesses

### Soundness
3

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
This paper presents an innovative diffusion-based approach to address the Inexact Segmentation (IS) task by leveraging the intrinsic generative priors inherent in Stable Diffusion. The authors propose a coarse-to-fine segmentation refinement strategy that exploits pattern discrepancies between original images and mask-conditional generated images. This is achieved through the establishment of semantic correspondence alignment and iterative updating of foreground probabilities. A key contribution of this work is the introduction of a semantic correspondence alignment methodology, which employs the pixel-wise Hausdorff distance as a discrepancy metric. The efficacy of the proposed method is demonstrated through extensive experimentation in both open-vocabulary and weakly supervised segmentation tasks. Notably, the approach consistently outperforms current state-of-the-art methods, showcasing substantial performance gains across various benchmarks.

### Strengths
1.The proposed G4SEG introduces an innovative training-free framework for inexact segmentation refinement using generative models. This approach represents a significant departure from previous discriminative-based and diffusion model (DM)-based training methods, offering a novel perspective in the field.

2. The concept of explicit mask projection and semantic correspondence alignment is particularly noteworthy. By ingeniously decoupling the mask refinement process from target image reconstruction, the authors present a unique solution to the segmentation refinement problem.

3. The method demonstrates consistent performance gains when incorporated with current state-of-the-art approaches in both open-vocabulary and weakly supervised segmentation tasks. This broad applicability underscores the effectiveness and versatility of the proposed technique.

### Weaknesses
1. The reliance on Stable Diffusion may potentially limit the model's efficiency compared to baseline methods, raising concerns about computational requirements and processing speed. Specifically, the iterative refinement process, involving multiple forward passes through the diffusion model, could introduce significant latency, making it less practical for real-time applications or large-scale datasets. The computational overhead of generating mask-conditional images and calculating pixel-wise Hausdorff distances needs to be carefully considered, especially when compared to simpler, non-generative refinement techniques.

2. The improvements are most pronounced when applied to less accurate segmentation models, such as GroupVit, which is trained solely with text labels. When used with stronger base segmentation models (e.g., SCLIP and DiffSegmenter), the performance gains appear to be less substantial, potentially limiting the method's applicability across a broader range of models. This suggests that the proposed method might be most effective as a post-processing step for relatively weak initial segmentations, rather than as a general-purpose refinement tool for all segmentation models. It raises questions about the method's ability to address subtle but critical errors in high-quality segmentations.

### Questions
1. How does the proposed method handle cases where the initial segmentation is significantly inaccurate or contains multiple errors? Is there a threshold of initial accuracy below which the refinement process becomes less effective or unreliable?

2. Given that the method leverages generative priors from Stable Diffusion, how sensitive is it to domain shifts or out-of-distribution images? Have the authors explored its performance on datasets or image types that differ significantly from those used in training Stable Diffusion?

3. Could this approach be extended or adapted to those fully-supervised methods that can already achieve accurate segmentation results, such as SegFormer and Mask2Former?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an effective method G4Seg based on Stable Diffusion to tackle the Inexact Segmentation task. This method utilizes the difference between the generated and original image to help refine the mask. By establishing a semantic correspondence alignment, the foreground probability of the confusion area can be effectively updated. Experiments on various benchmarks validate the effectiveness and superiority of this training-free approach.

### Strengths
(1) The idea that using the difference between the generated and original image to help refine the mask is interesting.

(2) This paper is generally well-written and easy to follow.

(3) The introduction of G4Seg is comprehensive and detailed.

(4) G4Seg is training-free and easy-to-use.

(5) The framework is tested across multiple benchmarks, including TSSS and WSSS, showcasing its versatility and effectiveness under different settings.

### Weaknesses
(1) G4Seg is based on Stable Diffusion and suffers from heavy time costs, resulting in poor practicality especially when inference at scale.  It would be better to report the specific inference cost for each dataset, not be confined to VOC but the complex COCO.

(2) As shown in the figures, the refinement of confusion areas is limited and imperfect. There are still a certain amount of pixels that G4Seg can not correct. What is the inherent reason for this phenomenon? The struggles to select confusion areas or failures in semantic correspondence alignment? Meanwhile, G4Seg should be compared to other mask refinement techniques such as training-free dense CRF and training-based CascadePSP [1], SegRefiner[2]. It seems that dense CRF is superior and more efficient than G4Seg. For training-based methods, I understand that these works may use additional pixel-level annotations for training, but the comparison can help readers understand the gap between G4Seg and SOTA mask refinement techniques.

(3) The feature maps in Stable Diffusion are heavily downsampled (e.g., 64x64). Does G4Seg work for small objects?

(4) VOC is not an ideal dataset to validate the boundary accuracy because areas near the boundary are labeled as “void” in GT masks. Datasets with more boundary-accurate annotations, like re-labeled VOC and BIG used in CascadePSP [1], are more appropriate.

(5) Detailed parameter sensitivity analyses for the injection weight $\alpha$ and mixing coefficient $\beta$ are lost, which is important to assess the robustness of G4Seg.

### Questions
In Table 6, how to inject boxes, points and scribbles into Stable Diffusion?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors  exploits the discrepancies between original images and coarse mask-conditional generated images to improve mask quality. The proposed method has performance gain on both open-vocabulary and weakly-supervised task.

### Strengths
(1) The motivation of reducing discrepancies between original images and coarse mask-conditional generated images is easy for understanding.

(2) The proposed method can improve the segmentation quality of existing open-vocabulary and weakly-supervised methods.

### Weaknesses
 (1) The contribution of this paper is limited, and the idea of reducing discrepancies is relatively incremental.

(2) The proposed method focuses on discrepancies. For irregular objects, it is difficult to give an accurate generation. Does the proposed method have negative results on these situations.

(3) The proposed method has limited improvement by performing a forward diffusion denoising process. 

(4) The proposed method is a refinement processing, which lacks of comparison with existing mask refinement method, such as CRF.

(5) It lacks the analysis about the hyper-parameters like injection weight and mixing coefficient. For implementation details, the settings on different tasks are different.

(6) The proposed method seems increasing the computational cost during inference according to Table 5.

### Questions
(1) The contribution and novelty could be improved

(2) More discussions about the discrepancies, and more experimental comparison

### Soundness
3

### Presentation
2

### Contribution
2
