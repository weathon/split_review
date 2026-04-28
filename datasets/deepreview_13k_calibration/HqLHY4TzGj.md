# Union-over-Intersections: Object Detection beyond Winner-Takes-All

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
This paper revisits the problem of predicting box locations in object detection architectures. Typically, each box proposal or box query aims to directly maximize the intersection-over-union score with the ground truth, followed by a winner-takes-all non-maximum suppression where only the highest scoring box in each region is retained. We observe that both steps are sub-optimal: the first involves regressing proposals to the entire ground truth, which is a difficult task even with large receptive fields, and the second neglects valuable information from boxes other than the top candidate. Instead of regressing proposals to the whole ground truth, we propose a simpler approach—regress only to the area of intersection between the proposal and the ground truth. This avoids the need for proposals to extrapolate beyond their visual scope, improving localization accuracy. Rather than adopting a winner-takes-all strategy, we take the union over the regressed intersections of all boxes in a region to generate the final box outputs. Our plug-and-play method integrates seamlessly into proposal-based, grid-based, and query-based detection architectures with minimal modifications, consistently improving object localization and instance segmentation. We demonstrate its broad applicability and versatility across various detection and segmentation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper revisits the problem of predicting box locations in object detection architectures. Traditional approaches typically regress box proposals to maximize the intersection-over-union (IoU) score with the ground truth and then apply non-maximum suppression (NMS) to retain only the highest scoring box in each region. The authors argue that both steps are suboptimal: regressing proposals to the entire ground truth is a challenging task, and NMS ignores potentially useful information from other boxes. To address these issues, the authors propose a simpler method—regressing proposals only to the intersection area between the proposal and the ground truth, rather than the entire ground truth, thus avoiding the need for proposals to extrapolate beyond their visual scope and improving localization accuracy. Additionally, they suggest generating the final box outputs by taking the union of the regressed intersections from all boxes in a region, rather than using a winner-takes-all approach, thus preserving valuable information from other boxes. This plug-and-play method integrates seamlessly into any detection architecture with minimal modifications and significantly enhances object localization and instance segmentation. The experimental results demonstrate its broad applicability and impressive performance across a variety of detection and segmentation tasks.

### Strengths
The "UoI" strategy proposed in this paper is highly innovative and practical, as it can seamlessly integrate into existing two-stage object detection networks, significantly improving detection performance. The authors creatively introduce the idea of regressing proposals to the intersection area with the ground truth, rather than the entire ground truth, addressing the challenges of regressing to the full target region. This not only improves localization accuracy but also offers an elegant and practical solution that can be easily adopted within current detection architectures. The paper is clearly written, with a logical structure that makes the proposed UoI method easy to understand. The figures and pseudocode are well-presented, offering an intuitive explanation of the approach. Furthermore, the extensive ablation experiments validate the effectiveness of UoI across various detectors, further strengthening the paper’s contribution. Overall, the paper excels in originality, clarity, and practical applicability.

### Weaknesses
While the paper excels in terms of methodological innovation, clarity of writing, and the presentation of figures and pseudocode, there is room for improvement in the design of comparative and ablation experiments. Specifically, the validation of the proposed UoI strategy is limited to a few methods, which may constrain its generalizability. For example, Table 1 only compares Faster R-CNN and Def-DETR’s detection performance on the PASCAL VOC dataset, while Table 2 provides comparisons for five methods (Faster R-CNN, Mask R-CNN, Cascade R-CNN, YOLOv3, and Def-DETR) on the MS-COCO dataset. However, why are methods like Mask R-CNN, Cascade R-CNN, and YOLOv3 not included in the PASCAL VOC comparison? Including these methods would strengthen the results and provide a more comprehensive evaluation. Furthermore, the absence of a consistent evaluation protocol across different datasets makes it difficult to assess the true impact of the UoI method. The inconsistent inclusion of different methods in different tables raises questions about the robustness and general applicability of the proposed approach. For instance, the performance of UoI on single-stage detectors like YOLOv3 is only evaluated on MS-COCO, while two-stage detectors are evaluated on both datasets, making it hard to draw a fair comparison across different architectures.

Moreover, Tables 4-7 and Figure 3 mainly show results for Faster R-CNN, without testing the UoI strategy on other classic detection architectures. To further validate the effectiveness of UoI, it would be beneficial to conduct experiments on additional well-established methods, demonstrating its applicability and advantages across a broader range of architectures. This would enhance the paper’s persuasiveness and provide stronger evidence for the practical utility of the proposed approach. The exclusive focus on Faster R-CNN for detailed ablation studies limits the understanding of how UoI interacts with different architectural choices and hyperparameters. For example, the optimal group size of 5 for Faster R-CNN might not be optimal for other architectures, and this needs to be explored. The lack of ablation studies on other architectures makes it difficult to generalize the findings and understand the true potential of the UoI method.

### Questions
1.	To enhance the overall aesthetic consistency of the paper's layout, a few minor formatting adjustments are recommended:

1）	Some bolded paragraph titles (e.g., the bold text followed by a period, such as "Problem Statement." in line 150) are set on a new line rather than immediately followed by the paragraph content. This may be intentional due to title length, or it might be a formatting issue. It is suggested to align these paragraph titles directly with the content following them. For example, "Intersection-based Grouping." in line 203 and "Regressing to intersections is simply an easier task." in line 448 should follow this format.

2）	The title "Inference cost" in line 267 lacks a period and should be updated to "Inference Cost." Additionally, the caption of Figure 4 ("Qualitative results…") is not bolded like the caption in Figure 5; please consider ensuring consistency with Figure 5's formatting.

3）	The paragraph titles throughout the paper vary between Title Case and Sentence Case. Although I will not list each instance here, please consider standardizing these for consistency.

2.	To ensure accuracy and clarity, a few content-related questions have also arisen:

1）	In line 220, the text states, "The regression function r : B → R maps each combined box to a final target box." Here, does R refer to the set of all ground truths? Previous sections define G or T as representing all ground truths, so it is unclear why R is used here instead of G or T. Could this be clarified?

2）	To guarantee the precision of the pseudocode in the Post-Processing Stage on the right side of Figure 2, could you confirm if it would be necessary to include "P ← P \ p_i" in the conditional statement within the red dashed box to ensure the "while P ≠ empty do" loop functions correctly (assuming the pseudocode within the green solid box is disregarded)?

3.	Could you clarify why the conditional statement in the pseudocode within the green solid box on the right side of Figure 2 uses "iou(H, pi) ≥ k" rather than "iou(M, bi) ≥ k" as in the red dashed box? Has there been any experimentation to validate the effectiveness of "iou(H, pi) ≥ k" over "iou(M, bi) ≥ k"? If not, please consider including such justification.

4.	In Table 3, there is a Comparison of instance segmentation on MS-COCO data, showing considerable improvements in AP for various object sizes (i.e., small, medium, and large objects as defined by COCO). The COCO definition of "small objects" encompasses those with an area under 32×32 pixels. Compared with small-object detection tasks in infrared imaging (where small objects typically occupy less than 10×10 pixels and may even be as small as a few pixels), COCO's small objects are relatively large. Could the authors clarify whether their proposed UoI method would also be effective for these considerably smaller targets?

5.	Figure 3(c) demonstrates that on the MS-COCO dataset, Faster R-CNN achieves optimal performance with the UoI strategy when the intermediate group size is 5. Have the authors considered studying the effect of varying the IoU threshold k in the UoI strategy (i.e., the IoU threshold used in the conditional statement in the pseudocode within the green solid box on the right side of Figure 2)?

6.	Figures 4 and 5 highlight certain limitations of the proposed UoI approach, specifically in handling crowded scenes. Could the authors specify if these crowded scenes refer to instances of multiple objects or instances of the same class, or do they also include multiple instances of different classes? Additionally, might the size of objects or instances in these crowded scenes significantly restrict UoI’s performance? Please provide a detailed discussion on these aspects.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper propose Union-over-Intersections method for object detection, which predict intersection box between proposal box and ground truth box and combine overlapped boxes into the final instance.

### Strengths
- The authors provide a thorough explanation of the methodology, making it easy to understand. 
- The authors present a novel insight and have correctly implemented the methodology, achieving promising results.
- The experimental content is comprehensive, covering key results across popular detection algorithms and both detection and segmentation tasks. The ablation study effectively discusses the strengths of the approach and includes an analysis of its limitations.

### Weaknesses
 - While this paper attempts to challenge the conventional box refinement paradigm (predict box directly and Winner-Takes-All for post-processing) in object detection models, it does not sufficiently demonstrate its viability as a true alternative to the original paradigm. (NOTE that although I mention this as a weakness, I still consider the approach to be novel and appreciate their effort to explore new insights. However, from an intuitive standpoint, the method does not strongly compel me to adopt it.)

 - Intuitively, this method seems more beneficial for detecting larger objects, as the "combine box" approach tends to union the box when merging bounding boxes within a group, potentially biasing towards larger boxes. Is combining multiple predictions still an ideal detection strategy for small objects? The smaller targets are often adequately covered by a single proposal, which means the approach sometimes defaults to the standard paradigm. Although the main experimental results indicate an improvement in mAP across object sizes, I would encourage the authors to further analyze how this paradigm performs for targets of different sizes.

- It seems that the target of the regression stage is dynamic. I would encourage the authors to further analyze about the concerned instability.

- The confidence scores of the combined boxes are not introduced in method descriptions. It is important because score is essential for mAP. (good score also benifits mAP)

- Isn't the combined boxes the new boxes? Why the number of predictions remain? Does the mAP evaluator obtain more predictions than baseline?
> By design, our method yields the same number of predictions as current detectors and is compatible with any NMS variant.

- Is regression function r a learnable regression head? Why an additional regression refinement module is required? Isn't the combined boxes the prediction boxes? (We nevel refine NMS outputs with an additional regression module. The baseline method seems lack one refinement module)

- How does the detectors with other types of proposal (e.g. DETR with non-two-stage-initialized object queries, FCOS with point based dense head) be integrated seamlessly by UoI? It seems that this method can only be a box refinement module for these non-box-proposal methods.
> Our plug-and-play method integrates seamlessly into any detection architecture with minimal modifications

### Questions
- Intuitively, this method seems more beneficial for detecting larger objects, as the "combine box" approach tends to union the box when merging bounding boxes within a group, potentially biasing towards larger boxes. Is combining multiple predictions still an ideal detection strategy for small objects? The smaller targets are often adequately covered by a single proposal, which means the approach sometimes defaults to the standard paradigm. Although the main experimental results indicate an improvement in mAP across object sizes, I would encourage the authors to further analyze how this paradigm performs for targets of different sizes.

- It seems that the target of the regression stage is dynamic. I would encourage the authors to further analyze about the concerned instability.

- The confidence scores of the combined boxes are not introduced in method descriptions. It is important because score is essential for mAP. (good score also benifits mAP)

- Isn't the combined boxes the new boxes? Why the number of predictions remain? Does the mAP evaluator obtain more predictions than baseline?
> By design, our method yields the same number of predictions as current detectors and is compatible with any NMS variant.

- Is regression function r a learnable regression head? Why an additional regression refinement module is required? Isn't the combined boxes the prediction boxes? (We nevel refine NMS outputs with an additional regression module. The baseline method seems lack one refinement module)

- How does the detectors with other types of proposal (e.g. DETR with non-two-stage-initialized object queries, FCOS with point based dense head) be integrated seamlessly by UoI? It seems that this method can only be a box refinement module for these non-box-proposal methods.
> Our plug-and-play method integrates seamlessly into any detection architecture with minimal modifications

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose the Union-over-Intersections (UoI) method, which modifies the object detection pipeline in two key ways:

1. **Intersection-Focused Regression** : Instead of regressing proposals to the entire ground truth, the method focuses on the intersection area, simplifying the regression task and improving localization accuracy.
2. **Union of Proposals** : In the post-processing stage, rather than using a winner-takes-all strategy, the UoI method combines information from all proposals by taking the union of their regressed intersections, enhancing the final detection output.

The paper demonstrates decent improvements in object localization and instance segmentation across various architectures, including Faster R-CNN and YOLOv3. The UoI method is adaptable and can be integrated into existing detection frameworks with minimal changes, making it a promising advancement in the field of object detection.

### Strengths
* The method is straightforward, requiring only modifications to the training objectives and post-processing steps, making it easy to implement within existing proposal-based detectors.
* Experimental results demonstrate a solid improvement in accuracy while introducing only a minimal additional computational overhead

### Weaknesses
My primary concern lies in the novelty and significance of the method. The paper emphasizes the use of intersections, but in my view, intersections are a subset of Intersection-over-Union (IoU). Learning IoU inherently involves understanding intersections, and there are already existing works focused on learning IoU, such as IoU loss. This diminishes the overall importance of the paper. Additionally, learning the complete ground truth bounding box implies the need to understand both intersections and unions. With proper tuning, I believe that incorporating more information would benefit neural network learning rather than focusing solely on a partial representation.

The concept of the Union of Proposals appears to function similarly to a voting mechanism. Box voting for accuracy improvement has already been extensively validated through test-time augmentation techniques in challenges like VOC and COCO. Moreover, learning the complete ground truth bounding box can naturally facilitate a voting process as well.

Lastly, there are concerns regarding generalizability. The method relies on proposals, which limits its applicability in proposal-free approaches, such as YOLO and FCOS. This reliance on a specific number of proposals necessitates tuning, making integration with proposal-free methods less convenient. Furthermore, the merging of proposals into a single result complicates any further voting efforts, which could potentially yield additional improvements.

### Questions
1. What would be the implications of applying the Union of Proposals to learn the complete ground truth bounding boxes without altering the learning objectives?
2. Please provide a rationale for the weaknesses summarized above.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes to predict a set of intersection boxes for one given ground-truth box and then take the union of them to form the final detection box. The method is simple yet effective and is verified on 5 classic detectors.

### Strengths
1. The proposed method is simple yet effective and easy to be re-produced.

2. The discussion of the problem is quite clear; the paper is well-written.

3. The experiments and analyses are sufficient to support the soundness of the proposed method over the vanilla regression method. The results also verify its good versatility for a variety of object detectors.

### Weaknesses
1. As a box regression method, the paper did not compare the proposed method with IoU-based loss functions, e.g., GIoU [r1], CIoU [r2], Alpha-IoU [r3], EIoU [r4], etc, making the superiority of the methods less convincing.

2. It is mentioned by line 216, the proposed Intersection-based Grouping is compatible with any NMS variant. In the experiment, only Soft-NMS is tested. I suggest the authors provide more ablation on this.

3. In Fig.3(c), it shows that the performance may be sensitive to the number of proposals on Faster R-CNN and MS COCO. This characteristic may limit its robustness in different scenarios, e.g., different detectors or different datasets.

4. Why the datasets of ablation studies switch frequently between COCO and VOC? Not consistent.

5. The font size of Fig.3 is too small.

6. There are still important ablations in Appendix that do not appear in the main paper. The Fig. 4 is too large. I suggest removing half of Fig. 4 to save more room for presenting those experiments. Fig.5 is showing something similar to Fig.4 and can be removed too. I argue that those ablation studies are inspiring that provide more insights of the method.

7. There are no related works of bbox regression in Sec.2. I suggest giving a comprehensive introduction to that.

8. All the algorithms engaging in comparison must be appears in Sec.2 Related Works. Please check them carefully.

### Questions
Does the difference between the middle group of Table 1 (Faster R-CNN) and Table 4 lie in whether Soft-NMS is applied or not?

### Soundness
3

### Presentation
3

### Contribution
3
