# P2Seg: Pointly-supervised Segmentation via Mutual Distillation

- Decision: Accept
- Scores: 6, 8, 6, 6, 3

## Abstract
Point-level Supervised Instance Segmentation (PSIS) aims to enhance the applicability and scalability of instance segmentation by utilizing low-cost yet instance-informative annotations. Existing PSIS methods usually rely on positional information to distinguish objects, but predicting precise boundaries remains challenging due to the lack of contour annotations. Nevertheless, weakly supervised semantic segmentation methods are proficient in utilizing intra-class feature consistency to capture the boundary contours of the same semantic regions.
In this paper, we design a \textbf{M}utual \textbf{D}istillation \textbf{M}odule (MDM) to leverage the complementary strengths of both instance position and semantic information and achieve accurate instance-level object perception. The MDM consists of \textbf{S}emantic to \textbf{I}nstance (S2I) and \textbf{I}nstance to \textbf{S}emantic (I2S). S2I is guided by the precise boundaries of semantic regions to learn the association between annotated points and instance contours. I2S leverages discriminative relationships between instances to facilitate the differentiation of various objects within the semantic map. 
Extensive experiments substantiate the efficacy of MDM in fostering the synergy between instance and semantic information, consequently improving the quality of instance-level object representations. Our method achieves 55.7 mAP$_{50}$ and 17.6 mAP on the PASCAL VOC and MS COCO datasets, significantly outperforming recent PSIS methods and several box-supervised instance segmentation competitors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses Point-level Supervised Instance Segmentation (PSIS). The authors argue that the existing PSIS methods usually suffer from the lack of contour annotations, and thereby precisely predicting boundaries is still challenging. As a remedy, this paper introduces the Mutual Distillation Module (MDM), leveraging the complementary benefits of semantic information and instance position. In MDM, Semantic to Instance (S2I) exploits the precise boundary information of semantic maps to enhance the instance contours. Meanwhile, Istance to Semantic (I2S) uses discriminative instances to differentiate the number of objects in the semantic map. Extensive experiments and comparisons are conducted on the PASCAL VOC and MS COCO datasets.

### Strengths
1. The idea is sounding.
2. The ablations studies are extensively conducted.

### Weaknesses
[Major]
1. Some important and recent WSSS methods are missing. Please refer to the following CVPR 2023 papers.
* Weakly Supervised Semantic Segmentation via Adversarial Learning of Classifier and Reconstructor
* Out-of-Candidate Rectification for Weakly Supervised Semantic Segmentation
* Boundary-Enhanced Co-Training for Weakly Supervised Semantic Segmentation
* Token Contrast for Weakly-Supervised Semantic Segmentation

2. The performance table is incomplete. First, please show the result of mAP25. Also, there have been several works using the transformer backbone, such as Point2Mask or AttentionShift. Please compare with them. In addition, where is BESTIE (with Res101)? Finally, please include the results of the COCO test set.

3. The segment-anything model (SAM) can be an excellent option for solving PSIS. Please compare the proposed method with the SAM, from the performance perspective.

[Minor]
The overall  writing should be enhanced.

### Questions
Please refer to weaknesses.

### Soundness
2 fair

### Presentation
1 poor

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
The paper proposed a novel approach “mutual distillation” for Point Supervised Instance Segmentation (PSIS). The method utilizes point-supervised semantic segmentation results as an initialization for guiding instance segmentation, and then use an affinity matrix that represents instance segmentation details to optimize the semantic information This process achieves mutual distillation between instance and semantic information to improve the final result of instance segmentation. They validated the effectiveness of the proposed method on the VOC and COCO datasets.

### Strengths
1.	The concept of "MUTUAL DISTILLATION" in point instance segmentation is both novel and interesting. In my experimental observations, BESTIE doesn't handle adjacent objects well, possibly because it relies solely on semantic segmentation results without fully utilizing point-represented instance information. The motivation behind this paper aligns with my observations, and therefore, the proposed concept of mutual information exchange between semantic and instance information seems sound to me.
2.	The paper's experimental section is comprehensive, using two datasets, different backbones, segmentation architectures, and conducting essential ablation studies.
3. It appears that the visualization is effectively presented.

### Weaknesses
1.	Observations from Figure 7 and Figure 8 suggest that the proposed mutual distillation method appears to perform well in segmenting adjacent objects and addressing missing object issues. It would greatly enhance the quality of this paper if the authors could provide a quantitative analysis of these cases.
2.	Minor issue
The writing of introduction should be improved somewhat.
-  "Instance segmentation is a critical task in computer vision and is equally important in semantic segmentation estimation and instance discrimination."
to 
"Instance segmentation is a critical task in computer vision, where semantic segmentation estimation and instance discrimination are equally important ."
- “and it aims not only to locate objects accurately but also estimate their boundaries to differentiate”
to
“and it aims not only to locate objects accurately but also to estimate their boundaries to differentiate”
I understand the description in 2nd paragraph of introduction. But the 术语 “semantic segmentation” and “instance segmentation” may not suitbale, it should be “semantic information“ and “instance information”

### Questions
Please see the detailed information in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Mutual Distillation Module (MDM) to leverage the complementary strengths of both instance position and semantic information and achieve accurate instance-level object perception. It consists of Semantic to Instance (S2I) and Instance to Semantic (I2S) sepcifically.

### Strengths
This method is novel and new. Training in a multi-stage way, combining the advantages of both semantic segmentation and instance segmentation looks reasonable. The experimental improvement also looks good.

### Weaknesses
1. Training in a multi-stage way, I feel concerned about the efficiency of the method. The author should provide comparisons about efficiency, like GFLOPS, FPS, inference time and so on, with existing methods, to demonstrate that the improvement does not come from extra computational budget. In addition, will multi-stage training derive into more training iteration numbers? If so, the author should also provide fair comparison with the same iteration numbers.
2. The ablation study is conducted on VOC, where S2I looks like a 0.4% improvement. The effect of S2I is thus quite limited. I am also curious about the ablation study on the COCO dataset. Will the improvement becomes less? If se, I feel that S2I is unnessary and extra.
3. What's about the performance of the method on the COCO dataset with ResNet?

### Questions
Please refer to the weakness part. I will adjust my rating based on the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problems of local response and seprated semantic and instance learning on the pointly-supervised instance segmentation task. To solve the problems, the authors propose the Mutual Distillation Module, which achieves the conversion and cooperation between semantic and instance segmentation by predicting class, offset, and affinity, thus leveraging the complementary strengths of instance and semantic. Various experiments demonstrate the effective of the proposed method.

### Strengths
** The analysis of the complementarity of instance segmentation and semantic segmentation is reasonable for the pointly-supervised instance segmentation task, and the designed method corresponds to the analysis.

** The core S2I method is unique and more accurate than BESTIE.

** Experiments demonstrate that both the Semantic to Instance (S2I) and Istance to Semantic (I2S) module is effective and the overall method outperforms previous works.

### Weaknesses
 **  Writing and presentation need improvement. For example, there are some confusing descriptions that are not explained (e.g., Dim-align in Fig. 3, instance adaptive grouping in Sec. 3.1, the green arrow from S2I loss to the mask in Fig. 3).

**  Some key technical details are missing. In Fig. 3, there are multiple MDM stages, but the required number of stages are not specified or experimented. the additional training cost should be discussed.

** The ablation about β in Sec. 3.2 are missing, so the effect on “smoothening the distribution to attain the optimal semantic segmentation map” is not clear.

** According to Sec. 3.1, the pseudo labels used in the first stage are obtained by SAM, but SAM is contrary to the setting of weak supervision. Moreover, in Tab. 1 and 2 the authors mark the proposed method as “no extra data”. But in my opinion, the used off-the-shelf segmentation map should be considered as extra data.

**  Will the proposed S2I method be sensitive to the position of the points? Could the author provide some qualitative or quantitative analysis to further illustrate the robustness of the method?

### Questions
**  Could the author explain the details described in Weaknesses 1?

**  What impact do the hyperparameter β and the number of MDM stages have on performance?

**  Does the use of SAM destroy fair comparisons, and would other pseudo-label generators be useful?

**   Will the proposed S2I method be sensitive to the position of the points?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach to Point Level Supervised Instance Segmentation based on mutual learning and knowledge distillation. The proposed algorithm, P2seg, introduces mutual distillation to recover instance segmentation based on points supervision. Comparison with the state-of-the-art methods is done using Pascal Voc-2012 and COCO-2017.

### Strengths
Originality. Point-supervised instance segmentation is not new in the weakly supervised literature, most approaches being more oriented to panoptic segmentation, ensuring a parsing of scenes better than instance segmentation. The novelty here is to use mutual learning between semantic segmentation and instance segmentation. The mutual information module is formed by a network S2I that transfers the semantic information to instances and a module I2S that uses the instance affinity matrices, class maps and offsets map predicted by an off-the-shelf segmentation network, namely HRNet (see e.g. \cite{ YuanCW19} and (https://github.com/HRNet/HRNet-Semantic-Segmentation) to refine results cyclically. 

Quality and clarity. The effort of explaining the architecture with a number of images and sketches is appreciable. 

Significance. The proposed mutual information-based method could, in principle, be lifted to large-scale datasets.

### Weaknesses
Novelty:
The paper is quite similar to BESTIE [Kim et Al., CVPR 2022], with the mutual distillation mimicking the semantic knowledge transfer defined in BESTIE. Many passages are pretty similar, though BESTIE provides algorithms and thorough explanations of the complex architecture, which are not given here.

Organization:
-No information is given on the instance affinity matrix and class map, as computed by HRNet (as stated in the last line of pg. 3, Overview of Method). HRNet is a semantic segmentation net [YuanCW19], which is never cited, and its practical role is not defined. The paper fails to specify how HRNet's output is transformed into instance-level information, which is crucial for the proposed method.

-No ablation is provided to understand the effect of each component. For example, it needs to be clarified if the semantic segmentation map is obtained by full supervision or by weak supervision. The mIoU of the obtained semantic segmentation is not provided.
-The number of points supplied at input, how they are collected, and the relation between them and the targets should be discussed. The paper does not clarify if these points are manually annotated or automatically generated. The spatial distribution of these points and their relation to object boundaries is also not addressed. The number of iterations used seems to be quite high.

In particular: 
A table showing scores, according to the number of points taken as input, was expected. Table 5, named “hard pixel ratio”, does not seem to be informative. 
A table showing the number of parameters for HRNet, MDM, and Mask-RCNN, used to retrain the MDM, was also expected, given the number of modules used.  
A table showing the impact of semantic segmentation was expected.

Ambiguities:
- The full loss L = \lambda_{I2S} L_{I2S} + \lambda_{S2I} L_{S2I} is such that L_{S2I} = L_{offset} + L_{segmentation}, though no weight for balancing L_{S2I} is added. 
However, on page 6, paragraph Training details, it is written that the weight of the segmentation loss is 1.0 and the weight of the offset loss is 0.01, which do not sum to 1 for L_{S2I}. The paper needs to clarify how these individual loss components are balanced within the overall loss function.
- As stated in Training details, Mask R-CNN is used for retraining MDM. Table 4 result is, in fact, the same as the result given in Table 1.
However, in Table 1, BESTIE (points) is given on PascalVOC-2012 a mAP_{50} score of 52.8, while on BESTIE paper is reported 56.0, higher than the 55.6 mAP_{50} of the paper under revision. Likewise, there is no value for BESTIE mAP_{70}, which instead is 36.5. On COCO-2017 BESTIE obtains 34.0, while the results displayed here, on Table 2, are 33.6, therefore less than BESTIE. The paper does not adequately explain the discrepancy in BESTIE's performance.
- In the two paragraphs “Results on Pascal VOC 2012” and “Results on MS COCO 2017”, it is written that the BESTIE algorithm is retrained to justify the lower scores reported, but it is not discussed why; while being the method almost similar an explanation is required. Therefore, apparently, the presented work does not improve on the SOTA. 
Furthermore, the works of [Kim_2023_CVPR] and [liao2023attentionshift] are not even reported, providing better results than those displayed in the paper under revision. The paper should provide a more comprehensive comparison with all relevant state-of-the-art methods.

- Possibly incorrectly reported values:
The difference between panoptic segmentation and instance segmentation is that instance segmentation does not consider ‘stuff’, and the metric mAP on ‘things’ allows confidence on overlapping objects. The difference implies (see [Kirillov_2019_CVPR]) that the metric PQ^{th}, that is panoptic quality on ‘things’, is like AP when from AP the non-overlapping predictions are subtracted, which means that AP benefits from predicting multiple overlapping hypotheses.
This paper, under revision, reports on Table 1 and 2 comparisons with Point2Mask [li2023point2mask]) quite inexactly. 
In fact, Point2Mask obtains on VOC 2012 results with PQ^{th}, namely panoptic quality on ‘things’, equal to 59.4 (with swin-transformer), and 53.0 with Resnet-101 while on Table 1 it is reported as mAP_{50} = 48.4 and mAP_{75} = 22.8. Similarly, on COCO-2017, no justification for these reported results is given.


Other comments:
1. Hadarmad should be Hadamard, which is repeated twice on pages 5 and 8.
2. Pg. 5: The concept of “instance ownership relation” is not introduced.
3. Pg. 5, eq. (5), it should be noted that A is assumed to be generated by the network HRNet, which is not referred to and it is a segmentation network. 
4. Pg 6: The description of COCO-2017 is wrong. It is written that COCO (i.e. COCO 2017) includes 110k images, but COCO 2017 includes 118k images. The test set is not reported. This is made of 40670 images, does this imply that no tests were made? Actually, there are no results on the test set.
5. Pg. 6 declares, “We assess the performance of object detection using two measures. We measure the performance using the standard protocol mean Average Precision(mAP). “Object detection”? The performance should be about instance segmentation unless it starts with HRNet object detection.

### Questions
Please explain:

    how the semantic segmentation is obtained.
    Why BESTIE is retrained, for both PascalVOC-2012 and COCO-2017.
    Why so many iterations are used, and what is included.
    Provide details about the number of points used and the relations points-targets.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
