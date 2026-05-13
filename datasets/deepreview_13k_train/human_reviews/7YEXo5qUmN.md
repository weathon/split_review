# Organ-DETR: 3D Organ Detection Transfomer with Multiscale Attention and Dense Query Matching

- Decision: Reject
- Scores: 3, 3, 8

## Abstract
Query-based Transformers have been yielding impressive results in object detection.  The potential of DETR-like methods for 3D data, especially in volumetric medical imaging, remains largely unexplored.  This study presents Organ-DETR that contains two novel modules, MultiScale Attention (MSA) and Dense Query Matching (DQM), for boosting the performance of DEtection TRansformers (DETRs) for 3D organ detection.  MSA introduces a novel top-down representation learning approach for efficient encoding of 3D visual data. 
MSA has a multiscale attention architecture that leverages dual self-attention and cross-attention mechanisms to provide the most relevant features for DETRs.  It aims to employ long- and short-range spatial interactions in the attention mechanism, leveraging the self-attention module.  Organ-DETR also introduces DQM, an approach for one-to-many matching that tackles the difficulties in detecting organs.
DQM increases positive queries for enhancing both recall scores and training efficiency without the need for additional learnable parameters. 
Extensive results on five 3D Computed Tomography (CT) datasets indicate that the proposed Organ-DETR outperforms comparable techniques by achieving a remarkable improvement of +10.6 mAP COCO and +10.2 mAR COCO. 
Code and pre-trained models are available at \url{https://---}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper implements a Detection Transformer for medical organ segmentation. The approach claims some technical novelties for query matching, while the evaluation is restricted to finding organs that are very likely present and does exclude comparison to recent self-configuring detection frameworks (nnDetection).

### Strengths
The concept in itself is a reasonable approach to 3D multi-object detection. The paper comprises a reasonable number of ablations within the selected scope of methods. The approach is evaluated on real 3D CT data. The method is fast.

### Weaknesses
The experimental evaluation has in my opinion some important flaws and nowadays with the availability of fast and accurate 3D segmentation models it has limited clinically practical use. The authors only consider the detection of organs, which occur always exactly once in each scan. Object detection in medical 3D volumes when focussed on (healthy) organs is different from natural images, where the presence/absence of objects or multi-instances is the real challenge. The counterpart in medical imaging would be lesion/nodule detection, which may or may not appear once or multiple times in one scan. As a toy example the organ/bone detection task is fine, but a more realistic setting e.g. including LUNA16 as described in https://github.com/MIC-DKFZ/nnDetection would have to be considered. Table 1 only comprises adaptations of natural image detection pipelines to 3D but avoids direct comparison to realistic medical detection pipelines such as nnDetection or multi-label segmentation e.g. nnUNet. For VerSe (detection of vertebrae that could be well identified by a centre point) many more landmark localisation tools should have been evaluated in terms of localisation error in mm. Even within the comparisons RetinaNet show similar accuracy for VerSe despite slight differences in false positives. I wonder whether at least a direct comparison to the Retina-UNet which was part of the discontinued Medical Detection Toolkit (https://github.com/MIC-DKFZ/medicaldetectiontoolkit) could have been included?

### Questions
I would recommend to completely overhaul the experimental validation to include clinically more relevant medical detection tasks, e.g. LUNA16 and also incorporate SOTA methods. To my opinion this would require at least 50% change in content as the current submission is not directly evaluating multiple instances or localisation errors etc.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces Organ-DETR that leverages the power of Detection Transformers (DETR) for 3D organ detection in volumetric medical imaging. The authors identify the underexplored potential of applying query-based Transformers to 3D data and present two new modules, MultiScale Attention (MSA) and Dense Query Matching (DQM), to enhance the performance of Organ-DETR. The authors extensively evaluate Organ-DETR on five 3D Computed Tomography (CT) datasets. The experimental results demonstrate the superiority of the proposed approach over comparable techniques, showcasing a remarkable improvement of +10.6 mAP COCO and +10.2 mAR COCO.

### Strengths
- Adequate experiment and dataset: The authors conduct thorough evaluations on five 3D CT datasets, providing substantial evidence of the effectiveness of Organ-DETR. 
- Extensive Evaluation: Author extensively analyze various parameters and conduct ablation studies, further enhancing the robustness of their experimental approach.

### Weaknesses
 - Limited Novelty: The adoption of multi-scale attention in this paper is not novel, as it has been extensively explored in both medical imaging [1] and general visual recognition [2] contexts.
[1] Multi-scale Hierarchical Vision Transformer with Cascaded Attention Decoding for Medical Image Segmentation
[2] MAFormer: A Transformer Network with Multi-scale Attention Fusion for Visual Recognition
- One-to-Many Label Assignment: In the organ detection scenario, the use of a one-to-many label assignment strategy is not reasonable, considering that there is typically only one instance of each organ (e.g., liver, pancreas, spleen) in the human body.

### Questions
See weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a detection model called organ-DETR for 3D organ detection. There are two major designs, one for the multi-scale learning mechanism and another for the dense matching strategy. Extensive experiments on five public datasets demonstrate that the proposed organ-DETR has achieved superior performance than several public methods for 3D organ detection. The performance gain is impressive and the claims are supported by corresponding experiments. Overall, this work is sound.

### Strengths
1. Impressive performance gains
2. Extensive experiments
3. Clear motivation and reasonable model designs
4. Good paper writing

### Weaknesses
[1] This method is mainly designed and described from the technical view. However, for 3D organ detection, the clinical motivation and meanings are not clear. In other words, why are the ~10% improvements significant for medical tasks? The authors are suggested to elaborate more on this part. Specifically, what are the downstream clinical tasks that benefit from this improvement, and what are the clinical implications of a 10% improvement in detection accuracy? Are there specific organs where this improvement is more critical, and why? This lack of clinical context makes it difficult to assess the true impact of the proposed method. 

[2] Top-down processing is a typical design for detection. The technical novelty should be clearly pointed out in this paper. It's not sufficient to simply claim a novel method; the specific aspects that differentiate it from existing top-down detection methods need to be highlighted. For example, how does the proposed multi-scale learning mechanism differ from existing feature pyramid networks or similar techniques? How does the dense matching strategy improve upon standard matching techniques in object detection? Another issue is that ICLR might not be the best place for this paper and more technical contributions can be emphasized.

### Questions
See the above weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
