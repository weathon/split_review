# Perceptual Piercing: Human Visual Cue-Based Object Detection in Low Visibility Conditions

- Decision: Reject
- Scores: 3, 1, 3

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose a deep learning framework for foggy scenes object detection inspired by atmospheric scattering and human visual cortex mechanisms. A lightweight object-detection model is applied first, followed by a spatial attention-based dehazing model, and finally a larger object-detection model. A AOD-NetX module is proposed in region-based dehazing step based on AOD-Net. The authors show some experiment results on Foggy Cityscapes and RESIDE-β dataset using YOLOv5 and YOLOv8.

### Strengths
Good idea to apply human visual cues to object detection in foggy scenes.

Clear figures to show the proposed overall architecture of Perceptual Piercing and the AOD-NetX modules, making it easier for readers to understand, which improves the quality of the presentation.

### Weaknesses
This paper appears more like a course project rather than a conference paper. The presentation of experimental results looks like ablation studies, lacking extensive comparison with other state-of-the-art methods.

In addition, it lacks comprehensive ablation studies on pre-trained models, module design details, or other hyperparameters.

Shifting from a one-stage to a multi-stage approach, along with heavy reliance on YOLO and AOD-Net, limits the originality of this paper.

### Questions
Why does Foggy Cityscapes have 1525 images in test set? I didn't find the number in the original paper (Sakaridis et al., 2017). In addition, it's better to explain why the train+val+test is much less than 20,550 images, and why train+val+test is larger than 4332 images in RESIDE-β.

Can you explain why YOLOv8 has better performance in other Foggy Conditions but has worse performance in AOD-NetX Architecture and Clear Conditions than YOLOv5 in Table 2? Just need more explanation to Table 2 and Table 3.

Is there a comparison with other state-of-the-art methods to enhance the generalizability and significance of this paper?

Is there a runtime comparison, particularly with one-stage methods and the model size/runtime comparison between your proposed AOD-NetX and standard AOD-Net?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
It feels more like an assignment than a research paper, as it simply combines a dehazing network with the YOLO object detector to identify objects in foggy scenarios.
The dehaze method and the object detector are both out-of-date works.

### Strengths
No strengths.

### Weaknesses
Is it a homework?
- This paper feels more like an assignment than a research contribution, as much of the content consists of summarizing existing works like Foggy-Cityscapes, AOD-Net, and YOLO.
- Despite the title's claim to address vision tasks in low visibility conditions, the paper only focuses on fog, neglecting other relevant scenarios.
- The approach merely combines a dehazing technique with an object detection method, offering little innovation.
- The paper lacks clear motivation and meaningful contributions, and the overall writing quality is very poor.

### Questions
Very bad paper. Meaningless.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel pipeline to generate de-hazed, and detect objects within hazy or foggy images. Predominantly towards airport operations, the authors identify the need for improved computer vision practices within low visibility environments, with a particular focus on minimizing end-to-end computation resources. Named AOD-NetX, the authors propose a two-stage pipeline where the outputs of a lightweight object detection model are used as inputs to a pre-existing AOD-Net architecture to constrain de-hazing to target selected regions, thus reducing computation resource costs. An object detection model is then applied to the selectively de-hazed image. The authors train their models on the cityscape training dataset, and evaluate it on both in-distribution cityscape test dataset, and out-of-distribution RESIDE-ß test datasets, arguing that AOD-NetX outperforms state-of-the-art models.

### Strengths
In general this paper is very well written. The writing style is very clear, with few grammatical mistakes. It was easy to understand the points being made, and the methodology was reasonably well presented.

The motivations of the paper were well expressed, highlighting a clear need for improved object detection capability within low-visibility scenarios, while minimizing end-to-end computation costs.

The literature review was reasonably comprehensive, considered multiple different approaches and challenges within low-visibility environments, and sufficiently identified gaps within the existing literature.

### Weaknesses
## Main Concerns
---
My main concern is the interpretation of the results. From the provided quantitative results, it is not clear to me that the proposed AOD-NetX architecture provides a sufficient improvement in terms of either accuracy or computation resource reduction for this paper to be accepted. The introduction, literature review, and discussion sections highlight the need for computational efficiency in applications that might use de-hazing. One of the strengths of the paper is the focus towards end-to-end inference time, given the selection of the nano yolo models, and AOD-Net which is one order of magnitude quicker than its predecessors for de-hazed image generation. It is strange to me then that there is no quantitative analysis of inference time, at least in table 1-3, to show that the end-to-end speed is hardly slower than the baseline nano model. 

I disagree with the interpretation of the results of Table 2. On line 351 the authors write: 'such as AOD-Net and AOD-NetX, consistently improves object detection performance in both clear and foggy conditions.' 
While, YOLOv5s+AOD-NetX+YOLOv5x/YOLOv8n+AOD-NetX+YOLOv8x yield the best performance for foggy conditions, they actually have the worst performance in clear conditions (0.4896 and 0.5150 mAP respectively). 

I disagree with the interpretation of results of Table 3. On line 402 the authors write: 'The addition of AOD-Net generally improved performance for YOLOv8 but had a diminishing effect on YOLOv5.' Inclusion of AOD-Net in fact leads to a reduction of performance from 0.7125 to 0.6458 on OTS and 0.6978 to 0.6125 on RTTS. This statement further contradicts with what the authors said previously on line 376 'that the YOLOv8x architecture achieved the highest mAP scores under foggy conditions, with 0.7125 on OTS and 0.6978 on RTTS' (i.e. that actually the baseline YOLOv8x architecture performed the best, outperforming the addition of AOD-Net).

Given these results, I do not find the conclusion to hold. On line 480 the authors write: 'Our proposed AODNetX architecture outperforms state-of-the-art models, excelling in both standard and out-of-distribution datasets.' We need more comparisons with state of the art models, such as those suggested in the literature review; Gao et al. (2023), Yang et al. (2023b), Zheng et al. (2023). Additionally, authors should consider evaluating existing SOTA methods for fog analysis for comparison with respect to both accuracy and computation cost, such as YOLOv5-s-Fog [1] which achieves better performance than AOD-NetX on RTTS dataset and claims real-time performance. Currently only AOD-Net is compared to, and it is not obvious from the results that AOD-NetX out-performs this approach. The results in table 3 suggest AOD-Net and the baseline model have higher mAP on out of distribution datasets compared to AOD-NetX.

My second concern is that the methodology of this paper is not sufficiently different from existing solutions. The provided solution is to combine the outputs of an existing AOD-Net model with an object detector model to yield an image with selectively de-hazed image regions. Inference is then run on the same object detector with the new selectively de-hazed image as input. Neither the object detection architecture nor the AOD-Net architecture are new.

---
## Other concerns:
---
It is odd that AOD-Net is not present in the literature review; given it is highly relevant to the task. Furthermore, Fig. 2 assumes a knowledge of transmission map K that is assumed from the AOD-Net paper. Given the critical role that the AOD-Net architecture plays in the construction of AOD-NetX, a more thorough explanation of its components is required. At the very least, K should be explicitly defined in the body of the paper (for example modify line 258 to '... utilizes the transmission map K, created...').

Domain adaptation is a large field of study that is often used within foggy scenes, but is entirely ignored in the literature review. A brief description of de-hazing abilities of domain adaptation (e.g. [2-4]) would help contextualise the choice of AOD-Net better.

---
## Minor details I picked up that did not influence my decision:
---
- line 027, abstract: 'The code for perceptual piercing is available here.' - where? Or has this been removed for purposes of double blind review?
- Section 3.2 gives descriptions of biological motivations. Given the specific claims of this section, references are required here. The authors might consider feature integration theory [5] or other works within cognitive psychology [6], and early neural networks that use and reference biological inspiration [7]. Also Stone (2018) [8] investigates biological systems with respect to information theory. This book may contain references that are useful.
- Fig 1: Its caption separates the proposed solution into three components, a, b, and c. The figure should represent these divisions somehow i.e. there should be an explicit reference to parts a, b, and c in the figure itself.
- line 229 (fig 1 caption): Missing punctuation: '(a)Preliminary detection.'
- line 350: Missing a space: 'Table 2trained and tested'
- line 455: 'To address the issue of generalizability in single-dataset training, two potential approaches are proposed' - this is unclear to me. It suggests that the paper has already proposed two approaches to address the issue of generalizability. I would re-word this to something like 'we propose two potential directions for future work.'
- line 480: 'AODNetX'... Everywhere else it is referred to as AOD-NetX

### Questions
Why did the authors not provide any quantitative analysis of computation costs of the proposed AOD-NetX architecture compared to existing SOTA, such as inference time? Given the choice of object detector and de-hazing network, I would expect AOD-NetX to be very fast. It is a shame this is not quantified and highlighted.

### Soundness
1

### Presentation
3

### Contribution
1
