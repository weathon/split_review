# Pursuing Better Decision Boundaries for Long-Tailed Object Detection via Category Information Amount

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
In object detection, the number of instances is commonly used to determine whether a dataset follows a long-tailed distribution, implicitly assuming that the model will perform poorly on categories with fewer instances. This assumption has led to extensive research on category bias in datasets with imbalanced instance distributions. However, even in datasets with relatively balanced instance counts, models still exhibit bias toward certain categories, indicating that instance count alone cannot explain this phenomenon. In this work, we first introduce the concept and measurement of category informativeness. We observe a significant negative correlation between a category’s informativeness and its accuracy, suggesting that informativeness more accurately reflects the learning difficulty of a category. Based on this observation, we propose the Informativeness-Guided Angular Margin Loss (IGAM Loss), which dynamically adjusts the decision space of categories according to their informativeness, thereby mitigating category bias in long-tailed datasets. IGAM Loss not only achieves superior performance on long-tailed benchmark datasets such as LVIS v1.0 and COCO-LT but also demonstrates significant improvements for underrepresented categories in non-long-tailed datasets like Pascal VOC. Extensive experiments confirm the potential of category informativeness as a tool and the generalizability of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The proposed manuscript highlights the presence of category bias even in relatively balanced datasets and introduces the Information Amount-Guided Angular Margin (IGAM) to address this issue. IGAM is designed to dynamically adjust the decision space of each category based on its information amount, thereby mitigating category bias in long-tailed datasets. Additionally, the effectiveness of the proposed method was demonstrated on the LVIS v1.0, COCO-LT, and PASCAL VOC datasets.

### Strengths
__1.__ Overall, this paper was easy to understand.

__2.__ The performance presented in Tables 1 to 5 demonstrates the effectiveness of the proposed method, although comparisons with more recent approaches are lacking.

__3.__ The discussion in Section 4.7 of the paper is persuasive.

### Weaknesses
__1.__ The authors raised the problem in the introduction based on observations from the PASCAL VOC dataset, but their main results include LVIS and COCO-LT datasets. Thus, the authors need to conduct experiments across datasets such as LVIS and COCO-LT to verify that the results are consistent with the observations made from PASCAL VOC.

__2.__ The proposed method was evaluated on established CNN-based models (e.g., Faster R-CNN, Cascade Mask R-CNN). However, with the emergence of various ViT-based object detection networks (e.g., DETR, H-DETR), it is crucial to assess whether the observed effects are specific to the tested models or if they generalize across different architectures.

__3.__ More importantly, the authors did not compare their method with recent long-tailed object detection approaches. Notably, [Ref_1] includes experiments on both CNN- and ViT-based models and appears to outperform the proposed method. A comprehensive comparison and analysis distinguishing this work from such methods are necessary.

__4.__ The same issue applies to [Ref_2]. Although the proposed method may seem reasonable at first glance, the experimental validation is not sufficiently convincing. A logical comparison and thorough analysis with recent approaches, including those presented in [Ref_1] and [Ref_2], are essential to substantiate the contributions and effectiveness of the proposed method.

__5.__ Could the category bias in balanced datasets be influenced by factors such as object scale or degree of occlusion?

### Questions
Overall, the validation of the experiments is insufficient, and the authors need to analyze external factors contributing to category bias, such as scale and occlusion, which are important metrics in the COCO dataset.

### Soundness
3

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
This paper proposed a new measurement to learn the information of different categories and then proposed the corresponding Information Amount-Guided Angular Margin (IGAM) Loss to optimize the decision space of the object detection networks.

### Strengths
1. The paper reasonably introduces the current problems of long-tail distribution target detection.
2. The author uses a new category information measurement method to optimize the network and fully verifies its effectiveness through extensive experiments

### Weaknesses
The paper's observations on the problem are reasonable. However, I do not feel that the method proposed by the paper is strongly related to the proposed scenarios: long-tail distribution and object detection. Here are the corresponding reasons:
1. In the introduction stage, if the author simply wanted to propose the concept of category information, then there is no need to compare in the long-tailed scenario, and it is more direct to show the performance with information in the general scenario. If the author wants to explain it in the long-tailed scenario in Figure 1, then the performance compared with the category information can be in the previous long-tailed dataset. So I think there is no alignment here.
2. In the first paragraph of Section 3.1, the authors mention that ‘the amount of information should be extracted from the classification module’. So why not address this issue directly in the classification process, but instead put it in the object detection scenario, and emphasize that this work is the first to directly report on the widespread bias present in object detection models in object detection? How about classification?
3. In the experimental part, the three methods compared in Table 5 are all long-tailed methods. And they are all between 2021 and 2022. Should they be compared with newer methods? In addition, as mentioned in 1, if the author's intention in Figure 1 holds true, should this method be equally effective in the case of networks such as Faster R-CNN on relatively balanced Pascal VOC datasets?

### Questions
1. Figure 2 only shows information about two attributes. How is the class-wise average precision reflected?
2. In formula 6, how does the operation of loss affect the compression and expansion of the decision space? For example, if i is the least informative, then the m_ij of other components j are all negative. Intuitively, it increases the second term in the denominator and thus increases the loss L, but why does this operation compress i's decision space?
3. In the previous formulas 1 and 2, the author used variance to represent the amount of information. If m_ij is negative, it means that the amount of information (variance) of i is already relatively small, so why do we need to continue to compress its decision space?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to solve the longtail problem in object detection. The authors find that the instance amount cannot be a good metric to balance the training. They introduce the category information amount and design a new loss function with it to solve the problem.

### Strengths
I like this paper. The motivation is clear and the introduction delivers the idea very well. The novelty of this paper is good. The finding and solution are interesting, and straightforward but effective. The experiments can support their method. If all the content is original, then it deserves to be published.

### Weaknesses
Some suggestions:
1. Fig.1 please align the class names and the axis ticks.
2. Fig.2 is good to show the correlation between CIA and ACC, but it would be better to show the CIA figure here, or in the ablation study section. 
3. explain the symbol $m$ in the Line 170, $p$ in the Line 176.

### Questions
1. Do you have any reference to support Line 164-169?
2. Do you maintain several individual queues for different categories, or a single queue for all categories?

### Soundness
3

### Presentation
4

### Contribution
4
