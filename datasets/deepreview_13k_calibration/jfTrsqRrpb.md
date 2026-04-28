# Open-world Instance Segmentation: Top-down Learning with Bottom-up Supervision

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Top-down instance segmentation architectures excel with predefined closed-world taxonomies but exhibit biases and performance degradation in open-world scenarios. In this work, we introduce bottom-\textbf{U}p and top-\textbf{D}own \textbf{O}pen-world \textbf{S}egmentation (\Ours{}), a novel approach that combines classical bottom-up segmentation methods within a top-down learning framework. \Ours{} leverages a top-down network trained with weak supervision derived from class-agnostic bottom-up segmentation to predict object parts. These part-masks undergo affinity-based grouping and refinement to generate precise instance-level segmentations. \Ours{} balances the efficiency of top-down architectures with the capacity to handle unseen categories through bottom-up supervision. We validate \Ours{} on challenging datasets (MS-COCO, LVIS, ADE20k, UVO, and OpenImages), achieving superior performance over state-of-the-art methods in cross-category and cross-dataset transfer tasks. Our code and models will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a top-down bottom-up approach for open-set instance segmentation. The bottom-up segmentation module is used to predict object parts, and then the authors use a clustering/group method to assemble parts into objects.  The main point that the authors try to argue is that, this bottom-up module somehow fits well in the open-world (open-set) instance segmentation scenario.

### Strengths
originality: The approach involves quite a few components. To me the authors build a quite complex system and it's unclear to me what the motivation and which component is the main reason which contributes to the good performance.

quality: borderline

clarity: The idea is clear and the paper is easy to follow

significance: The task per se is quite important. However I do not think the system presented in this paper is good enough to have an impact on open-world instance segmentation.

### Weaknesses
1) The bottom-up module is quite complex, involving a few components. I do see the authors did ablation experiments to justify some design choices, it is not clear why  part-segmentation and grouping work better than other baseline approaches.  Part-segmentation + grouping appeared in the literature long time ago and researchers abandoned this idea.  Current experiments in this paper do not convince me that this is actually a better idea for open-world segmentation.  A simple baseline will be to train a class-agnostic instance segmentation using, e.g. COCO annotations.  Papers already showed that a  class-agnostic model works better for open-world problems. The authors do not provide a clear explanation of why their specific combination of bottom-up part segmentation and grouping is superior, especially given the historical lack of success with similar approaches. The ablation studies, while present, do not sufficiently isolate the contribution of each component, making it difficult to ascertain the true source of any performance gains. It would be more convincing to compare against a class-agnostic model trained on a larger dataset with more diverse object categories, to truly assess the advantage of the proposed method. 

2) The compared methods are very old. For example, authors choose Mask RCNN and MCG as the baseline methods. These two methods are very old. The authors will need to consider recent methods. Even for top-down methods, Mask2former etc. will be a much better choice. I see that the authors might argue that the proposed method can use any other top-down method to replace Mask RCNN. But still why choose MaskRCNN in the first place. Using a more recent method will make the experiment results more convincing. The choice of Mask R-CNN as a baseline is particularly problematic given the rapid advancements in instance segmentation. Mask2Former, for example, leverages transformer-based architectures and demonstrates superior performance. By not benchmarking against such state-of-the-art methods, the paper fails to adequately contextualize the performance of the proposed approach. The argument that the framework can integrate other top-down methods does not justify the initial choice of an outdated baseline. It creates a significant gap in demonstrating the true potential of the method in comparison to contemporary techniques.

### Questions
See above

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed the UDOS for open-world instance segmentation that combines bottom-up unsupervised grouping with top-down learning. This model designed a grouping module and refinement method to achieve SOTA performance on multiple datasets.

### Strengths
The group-parts-to-whole strategy for segmentation is interesting. 
Experiments on multiples datasets verify the effectiveness of the proposed methods.
The paper writing and organization are good and clear.

### Weaknesses
Question: 
1. Is there any time-consuming experiments on the cluster in the grouping module? Because the similarity is calculated two-by-two.
2. I am interested in the AP performance if adding the classification head in cross-datasets and cross-category setting. I know the task is category-free and different from open-vocabulary segmentation task, but I wander the segmentation performance with higher recall.
3. As we know, the segment anything (SAM[1]) has high generalizability in category-free segmentation task. It is a foundation model pretrained in many data, but its zero-shot ability is strong without fine-tune in specific datasets in category-free segmentation task, so I think the comparison is necessary. Can this have higher recall that SAM? If not, please discuss on the contribution.
4. Why exclude part masks from U that overlap with any ground truth mask in S with an IoU greater than 0.9? Please discuss on it with experiments.
5. How about the grouping result on these situations: two same-category instances are close (or overlap), two instance with similar color, two hierarchical categories (e.g. clothes and person).
[1] Segment Anything, ICCV2023.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes bottom-Up and top-Down Open-world Segmentation (UDOS), a novel approach that combines classical bottom-up segmentation methods within a top-down learning framework.

### Strengths
This method is reasonable and novel. Combining bottom-up and top-down is an interesting idea.

### Weaknesses
1. This paper generate candidate object regions through unsupervised segmentation methods. However, it cannot be guaranteed that these unsupervised methods can generate object regions that cover all regions. Especially when the number of categories increases, I question the performance of the unsupervised segmentation methods. The author should provide :1) the specific performance of the unsupervised segmentation methods, 2) experimental comparison with existing methods when categories are more, like COCO to LVIS. The concern is that relying solely on unsupervised methods for region proposals might lead to a bottleneck, especially in complex scenes with numerous object categories, as these methods may not capture all instances effectively. 
2. The author should provide more result metrics with previous methods. For example, LDET also provides AP, AR10. The author should provide related performance comparisons to provide more comprehensive results. The lack of AP and AR10 metrics makes it difficult to compare this method with other open-world detection methods that use these metrics, hindering a thorough evaluation of its performance.
3. [A] also proproses a CLN (region proposal generation algorithm). What's about performance comparision with this work.
4. What's about the details about Refinement module? I feel that this is all about previous methods, no matter the objectness ranking and inference. The refinement module seems to be a standard implementation of existing methods, and the paper does not provide enough details on how it is adapted to this specific approach. It is unclear how the refinement module contributes to the overall performance of the proposed method beyond what is already established in previous works.

### Questions
Please refer to the weakness part. I will adjust the rating based on the author's feedback.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the limitations of top-down instance segmentation architectures in open-world scenarios, where predefined closed-world taxonomies may not be sufficient. To overcome this challenge, the authors propose a novel approach called Bottom-Up and Top-Down Open-world Segmentation (UDOS).

UDOS combines classical bottom-up segmentation methods within a top-down learning framework. It utilizes a top-down network trained with weak supervision derived from class-agnostic bottom-up segmentation to predict object parts. These part-masks are then refined through affinity-based grouping to generate precise instance-level segmentations.

The key advantage of UDOS is its ability to balance the efficiency of top-down architectures with the capacity to handle unseen categories by leveraging bottom-up supervision. By incorporating both approaches, UDOS achieves superior performance over state-of-the-art methods in cross-category and cross-dataset transfer tasks. The authors validate their approach on challenging datasets such as MS-COCO, LVIS, ADE20k, UVO, and OpenImages.

### Strengths
+ The paper demonstrates a high level of originality in several aspects. Firstly, it introduces the concept of combining classical bottom-up segmentation methods with a top-down learning framework to address the limitations of predefined taxonomies in open-world scenarios.

+ The use of weak supervision derived from class-agnostic bottom-up segmentation to predict object parts contributes to the originality of the proposed method.

### Weaknesses
- While the Multiscale Combinatorial Grouping (MCG) approach was proposed in 2016, it might be beneficial to consider the use of more recent methods, such as the Segmentation Attention Module (SAM), to enhance the generation of higher-quality masks for this problem. The integration of SAM into the existing framework could potentially improve the performance and accuracy of mask generation.

- In order to provide a comprehensive evaluation of the proposed approach, it would be valuable to compare it with relevant open-world panoptic segmentation techniques, such as ODISE (Open-vocabulary DIffusion-based panoptic SEgmentation). The inclusion of a comparative analysis with ODISE would enable a thorough assessment of the strengths and weaknesses of the proposed method and offer insights into its effectiveness in handling open-world scenarios.

### Questions
Please refer to paper Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
