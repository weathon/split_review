# PBADet: A One-Stage Anchor-Free Approach for Part-Body Association

- Decision: Accept
- Scores: 6, 8, 6, 6, 6, 5

## Abstract
The detection of human parts (\eg, hands, face) and their correct association with individuals is an essential task, \eg, for ubiquitous human-machine interfaces and action recognition.
Traditional methods often employ multi-stage processes, rely on cumbersome anchor-based systems, or do not scale well to larger part sets.
This paper presents \textit{PBADet}, a novel one-stage, anchor-free approach for part-body association detection. Building upon the anchor-free object representation across multi-scale feature maps, we introduce a singular part-to-body center offset that effectively encapsulates the relationship between parts and their parent bodies. Our design is inherently versatile and capable of managing multiple parts-to-body associations without compromising on detection accuracy or robustness. 
Comprehensive experiments on various datasets underscore the efficacy of our approach, which not only outperforms existing state-of-the-art techniques but also offers a more streamlined and efficient solution to the part-body association challenge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
-	It would be better if more details about the association process could be given.
-	How to choose the value of the hyper-parameter K used in L_{assoc}? The experiments would be more comprehensive if the value of K could be analyzed in the ablation study.
-	The reviewer wonders whether the models are trained from scratch or the pretrained YOLO weights are used. It is not mentioned in the paper.

### Strengths
-	Compared to the body-to-part center offset used in the previous one-stage method BPJDet, the part-to-body center offset proposed in this paper has better scalability in terms of the number of parts and avoids degrading the overall object detection performance.
-	The PBADet method proposed in the paper achieves state-of-the-art performance on BodyHands, COCOHumanParts and CrowdHuman datasets.
-	This paper is well organized, clearly presented, and effectively clarifies the differences from previous methods.

### Weaknesses
-	The author states that the proposed part-to-body center offset guarantees a one-to-one correspondence between parts and bodies. However, the paper does not elaborate on how the situation is handled when the predicted center offsets of multiple parts with the same category point to the same body. How to define the order for associating multiple parts with the same category? These details are not described in Section 3.4.
-	In Figure 2, it seems that 'P3' and 'P5' in the 'Multi-scale features' are labeled incorrectly.
-	It would be better if more details about the association process could be given.
-	How to choose the value of the hyper-parameter K used in L_{assoc}? The experiments would be more comprehensive if the value of K could be analyzed in the ablation study.
-	The reviewer wonders whether the models are trained from scratch or the pretrained YOLO weights are used. It is not mentioned in the paper.

### Questions
-	It would be better if more details about the association process could be given.
-	How to choose the value of the hyper-parameter K used in L_{assoc}? The experiments would be more comprehensive if the value of K could be analyzed in the ablation study.
-	The reviewer wonders whether the models are trained from scratch or the pretrained YOLO weights are used. It is not mentioned in the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a one-stage anchor-free approach (PBADet) for part-body association detection via singular part-to-body center offset that captures the relationship between parts and their parent bodies. It is an extension to one-stage anchor-free object detection methods for part-body association to identify part-body relationships. The approach supports multiple parts-to-body associations without compromising the accuracy and robustness of the detection process. The approach is evaluated on BodyHands, COCOHumanParts, and CrowdHuman datasets and the performance is comparable to the state-of-the-art (SOTA).

### Strengths
The paper is written well and easy to follow. The idea is very good and is inspired by the recent task alignment learning to enhance interaction between the two tasks for high-quality predictions.  

The rationale behind the anchor-free prediction, and part-to-body associations using models like YOLOv5, YOLOv7, and YOLOV8 is justified. 

A thorough experimental evaluation using well-known benchmarked datasets. On each dataset, the performance of the proposed approach is compared to the state-of-the-art and explains the performance gain and its impact on the overall accuracy.

The importance of the individual module model is experimentally evaluated. 

Interesting visualization to show qualitative comparison and highlight the erroneous predictions.

### Weaknesses
The anchor-free object representation uses multi-scale feature maps. How many scales have been used?  Is this the same as the backbone (e.g., YOLOv7) feature representation?

The approach uses a singular part-to-body center offset. The body center is the bounding box center or something else. Also, how important is accuracy in detecting the body center influencing the overall performance?

It would be nice to have a section on model capacity and computational complexity (e.g. Params, GFLOPS, per-image inference time, etc) to further improve the article. This should be compared to the other SOTA models.

The multi-scale module has a significant impact on the performance improvement w.r.t. the baseline. What could be the reason?

The loss weights ($\lambda$ and NMS thresholds $\tau$ values) are optimal for a given dataset?

### Questions
Please refer to the "Weakness" section.

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of human body part detection and association. The authors present a one-stage, anchor-free method to tackle this problem. Specifically, they introduce a part-to-body center offset to capture the relationship between parts and their corresponding bodies. The authors conduct experiments on BodyHands, COCOHumanParts, and CrowdHuman datasets.

### Strengths
- The paper is well-written and easy to follow.
- The proposed single-part-body center offset is efficient and can accommodate a large number of body parts without increasing the number of offsets as the number of parts grows. This makes the proposed method more efficient compared to previous methods.
- The paper presents good experimental evaluations and comparisons with previous methods.
- The paper also presents experimental evidence to study the benefits of each proposed component in ablation studies.

### Weaknesses
 -Table 2 doesn't mention AP for small objects. The proposed method performs better than previous methods on medium and large objects. How does this compare to small objects?

-How do the ablation studies change on the COCOHumanParts dataset? I am curious about the performance of different components of the proposed method on different object sizes: small, medium, and large.

### Questions
Please see the Weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents PBADet, a one-stage, anchor-free object detection model that efficiently identifies and associates object parts, such as human body parts, to their main body. Utilizing multi-scale feature maps and a unique part-to-body center offset, PBADet offers improved accuracy and robustness over existing models. It addresses inefficiencies through a task-aligned learning strategy and a simplified decoding process for part-to-body associations, making it a streamlined and effective solution in object detection.

### Strengths
1. The framework is adaptable for various part-to-body association challenges beyond human body parts.
2. The model adopts an anchor-free paradigm, potentially improving detection performance for objects of varying sizes.
3. Incorporation of a task-alignment learning strategy for bounding box, class predictions, and part-body association.

### Weaknesses
1. The paper doesn't explicitly address how the model deals with occluded parts.
2. The dense, per-pixel prediction approach might lead to increased computational demands.
3. The performance might be highly sensitive to the tuning of loss function hyper-parameters.
4. There's a lack of in-depth comparative analysis with traditional anchor-based models.
5. The model's efficiency in handling images with multiple overlapping objects is unclear.

### Questions
1. How does PBADet address the challenge of occluded parts in the detection process?
2. How does the model perform in scenarios with multiple overlapping or closely situated objects?
3. Have you tested the model’s scalability and performance across various domains other than human part-to-body associations?
4. Could you provide more comparative performance of PBADet against traditional anchor-based detection models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This article presents a method for correlating part to body relationships in a single multi-person RGB image. The method is a single-stage approach that adopts the popular center-based detection architecture. To correlate a subject and multiple detected body parts, a common approach is to estimate center offsets from each body center to the underlying body part. But this may be ineffective since in case of occlusion/close interaction multiple body centers may point to the same body part. Therefore, this paper proposes to simultaneously estimate the offset of the body part position from the detected body part toward the center of the subject. This means that instead of estimating center-to-part offsets, estimating part-to-center offsets for each detected body part will avoid ambiguities in close interaction situations. The proposed method greatly improves the performance of hand association in BodyHands.

### Strengths
1. BodyHands performance improvements are impressive with simple associative design changes. Changing from center-to-part to part-to-center offset greatly alleviates the ambiguity of hand associations in training.

2. Interesting insights. The proposed method can achieve significant performance improvements in hand association on BodyHands. This demonstrates the interesting insight that the position of the hand is more ambiguous than the position of the center of the body. Because more occlusion/interaction occurs in the hand area.

### Weaknesses
1. Writings. It is important to clearly present ideas and implementation. The current presentation is very vague and difficult to understand. It is beneficial to emphasize conceptual-level differences in the introduction. But before that, the paper should at least introduce the method/idea clearly. Additionally, in the Methods and related work section, consider clearly presenting differences compared to previous methods.

2. In Figure 2, please highlight the parts where the proposed approach makes design changes. In Fig. 1, the direction of arrows are not very obvious. Besides, differences in qualitative results are difficult to distinguish. Please consider emphasizing it further.

### Questions
1. Will the proposed method be open-sourced? It seems hard to re-implement the results with limited details.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose an association method for part-body detection. Their framework is based on YOLO, which is anchor-free.  In experiments, they show PBADet's good performance.

### Strengths
1. This paper is easy to read.  
2. Association for body and parts is  worth studying.  
3. The method is evaluated in several datasets.

### Weaknesses
1.The main problem of this paper is that part-to-body offsets have been proposed in previous works [1]. Furthermore，in [1], they also try local center offsets to improve the performance. Hence, considering the not new idea and no other designs, the technical learning of this paper is limitted.  
[1] Jin L, Wang XJ. Grouping by Center: Predicting Centripetal Offsets for the Bottom-up Human Pose Estimation. TMM, 2022.  
2. "Single-stage" is controverial. This method is bottom-up but still need two-stage processing, i.e., detection and grouping. And single-stage method has been studied in several reaseraches [2]. There are  obvious differences between single-stage methods and this paper.  
[2] Single-Stage Multi-Person Pose Machines, ICCV, 2019.  
3. To verify the association efficiency, author should compare your association method with other grouping methods, such as associative embeddings and methods in [1], under the same part detection accuracy.    
[3] Associative Embedding: End-to-End Learning for Joint Detection and Grouping.  
4. The focus of this paper is association, but the evaluation metric is AP. More metrics on association quality should be discussed.

### Questions
Refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
