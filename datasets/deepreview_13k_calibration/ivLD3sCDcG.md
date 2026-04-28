# Line2Rbox: Line-supervised Oriented Object Detection

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 6, 5

## Abstract
Oriented object detection is crucial for complex scenes such as aerial images and industrial inspection, providing precise delineation by minimizing background interference. Recently, the weakly-supervised oriented object detection has gaining attention due to its cost-effectiveness. However, the majority of existing weakly-supervised methods are either point-supervised or HBox-supervised, which presents a challenge in achieving an optimal balance between annotation cost and detection performance. In response, we introduce a novel form of line annotation, which is intermediate between point-level and plane-level annotation. Based on this, we present L2RBox, an end-to-end anchor-free detector that is the first line-supervised method for oriented object detection. The fundamental objective of the L2RBox is to utilise line labels for the completion of label assignment and the calculation of loss.  In particular, the line is mapped to the corresponding circle domain, which is then used to select training samples and calculate the center-ness target by the minimum circumscribed rectangle of the circle in the direction of the line.  The regression loss that we propose is designed to support the line as an optimisation target. It comprises four components, namely scale loss $L_s$, height loss $L_h$, position loss $L_p$ and angle loss $L_a$.
Extensive experimentation on DOTA-v1.0 and DIOR-R has demonstrated that our L2RBox significantly outperforms point-supervised methods, while requiring only a slight increase in labeling costs.  It is also noteworthy that the proposed approach also demonstrates a slight performance advantage over the fully-supervised FCOS in certain categories.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of balancing annotation cost and detection accuracy in weakly-supervised oriented object detection. The authors propose a novel method called L2RBox, which is the first line-supervised detector for oriented object detection. The method utilizes line annotations as a form of supervision, which is an intermediate level between point-level and plane-level annotations, aiming to reduce the annotation burden while maintaining high detection performance.

### Strengths
1. L2RBox introduces a new line annotation format for oriented object detection, which is a unique approach that sits between point and box annotations, offering a potential middle ground in terms of cost and accuracy.
2. The method presents an end-to-end anchor-free detector that uses line labels for label assignment and loss calculation, which is innovative in the context of weakly-supervised object detection.
3. The proposed regression loss is composed of four components (scale loss, height loss, position loss, and angle loss), which support line annotations as an optimization target, a novel approach in the field.
Advantages:
4. The method achieves comparable or even superior performance to fully-supervised detectors in certain categories, demonstrating its effectiveness.

### Weaknesses
1. The method involves complex label assignment and loss calculation mechanisms, which might be more challenging to implement compared to simpler point-supervised methods. Specifically, the paper does not provide sufficient detail on the exact algorithmic steps for label assignment, making it difficult to reproduce. The four-component loss function, while novel, also adds to the implementation complexity, requiring careful tuning of each component's weight and potentially leading to instability during training.
2.  While the method shows promising results on DOTA-v1.0 and DIOR-R datasets, its generalization capability to other datasets with different characteristics is not fully explored in the paper. The datasets used are primarily aerial images, and it is unclear how the method would perform on datasets with different object densities, viewpoints, or imaging modalities. For example, the performance on datasets with ground-level images or medical images is not discussed, which limits the understanding of the method's robustness.
3. Although the paper mentions that L2RBox does not increase computational cost significantly, the actual resource requirements for training and inference in real-world applications could be a concern for some users. The paper lacks a detailed analysis of the computational complexity, such as FLOPs or parameter counts, and does not provide a clear comparison with other methods in terms of training time and memory consumption. This makes it difficult to assess the practical feasibility of the method for resource-constrained environments.
4. Obtaining precise line annotations can be exceedingly demanding in terms of annotation costs, and in some scenarios, it may even surpass the difficulty of acquiring accurate bounding box annotations. The paper does not adequately address the practical challenges of line annotation, such as the need for specialized annotation tools and the potential for human error. The claim that line annotation is less costly than bounding box annotation is not sufficiently substantiated with empirical evidence or a detailed cost analysis.

### Questions
see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work aims to introduce a line-supervised oriented object detection method, representing a new form of weak supervision compared to previous point-level and hbox-level formats. To this end, this paper  present a novel line-supervised framework called L2RBOX, which is based on an anchor-free FOCS design. The primary technical contributions include label assignment and loss calculation utilizing line supervision, along with corresponding solutions. Experimental results demonstrate the effectiveness of the proposed method on the DOTA-1.0 and DIOR-R datasets.

### Strengths
1. This work proposes a new line supervision format and provides a comprehensive analysis in comparison to previous supervision formats.
2. The introduction of the effective framework L2RBOX includes detailed module designs, with experimental results on DOTA-1.0 and DIOR-R showcasing the superiority of the proposed method.
3. The paper is well-presented overall.

### Weaknesses
1. The line supervision format is based on the central axis annotation of objects. While this may simply the problem, a more randomized line representation would enhance its applicability. Specifically, the current approach limits the model's ability to generalize to objects where the central axis is not easily defined or where the object's shape deviates significantly from a simple elongated form. This reliance on a central axis could also introduce bias, as the model might learn to prioritize features aligned with this axis over other potentially relevant features. Given that this is the first work utilizing line supervision, this limitation is understandable.

2. In the related work section, for completeness of article, the discussion on point supervision should include references to the Point-Mask-RBox methodology, which has been discussed in previous point-supervised methods such as PointOBB and Point2Box. The absence of a discussion on how this work compares to Point-Mask-RBox leaves a gap in the analysis of point-based methods, particularly since Point-Mask-RBox also aims to generate oriented bounding boxes from point supervision, making it a relevant comparison.

3. Figure 5, which presents a comparison of trade-offs, would benefit from the inclusion of additional point and RBox-supervised methods. The current figure only shows a limited set of methods, making it difficult to fully assess the relative performance of the proposed line-supervised method. Specifically, including more diverse point-based methods and a wider range of RBox-supervised methods would provide a more comprehensive understanding of the trade-offs between annotation effort and detection performance.

### Questions
I lean towards a positive assessment of this work and offer two suggestions:

1. I recommend that the authors further explore the use of random line supervision rather than relying solely on a central line for practical applications in future research.

2. I encourage the authors to release the complete source code to benefit the advancement of this field.

### Soundness
3

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
5

### Summary
This paper innovatively proposes a new task for oriented object detection: Line-supervised Oriented Object Detection. It leverages existing RBox labels to generate precise central axes and designs an end-to-end anchor-free method based on FCOS. L2RBox uses the length information from line annotations and the feature map stride for sample assignment and designs losses to constrain the learning of target regression in terms of scale, height, position, and angle, achieving better performance than existing point-supervised methods in most categories. However, the writing of the paper needs improvement in several areas. For instance, the explanation of the sample assignment process lacks a clear description of how negative samples are assigned. Additionally, some details are unclear, such as the detailed generation method of line annotations and the discussion of their errors.

### Strengths
1. Good originality. This paper introduces a new task setting and provides a detailed analysis of the characteristics of various annotations in Oriented Object Detection. It designs a trade-off metric for evaluating existing weakly-supervised annotations (HBox, Point, and Line), thereby demonstrating that the proposed Line annotation can balance accuracy and efficiency.
2. This paper models the Line-supervised oriented object detection problem as a circle-based optimization problem and provides extensive visualizations and mathematical proofs to support this approach.

### Weaknesses
1. Issues about the proposed Line-supervised setting. 
- The paper lacks a detailed description of the process for generating Line annotations. In PointOBB and Point2RBox, it is mentioned that random sampling within a certain circular range is employed to simulate the error in manual annotations. However, Line2RBox lacks a discussion of this aspect, specifically how the line's length and orientation are affected by simulated annotation errors. The paper should clarify whether the simulated errors only involve rotation around the center or if they also include translation and scaling of the line, as these would have different implications for the model's robustness.
2. Limited generalization capability.
- According to the method description of Line2RBox, it lacks consideration for categories with extreme aspect ratios. Based on quantitative and visual results, Line2RBox performs poorly in BR and LV in DOTA-v1.0, and some categories in DIOR-R like APO and BR. Therefore, Line2RBox may be limited to detecting nearly square-shaped objects, overlooking variations in aspect ratios commonly found in remote sensing targets. This limitation is significant because many real-world oriented object detection scenarios involve objects with highly variable aspect ratios, and the method's inability to handle these cases reduces its practical applicability. The paper should provide a more detailed analysis of the failure cases and discuss potential solutions for handling extreme aspect ratios.
3. Unclear writing.
- Additionally, I would like to understand the meaning of taking the union of circles $C_g$ and $C_c$ when selecting training samples, considering that lines 254-256 indicate that a center radius exceeding the circular region is unfavorable. The rationale behind using the union of these two circles is not clearly explained, and it's unclear why the model wouldn't simply use the smaller circle. The paper needs to provide a more precise explanation of the sample selection process.
- In line 248, the specific value and discussion of the sampling ratio seem to be missing. The paper should provide the specific value used for the sampling ratio and justify this choice with experimental results or theoretical analysis. Without this information, it is difficult to assess the impact of this parameter on the model's performance.
- It seems that the term corresponding to the L-LA assignment method shown in Figure 2 does not appear in the main text, which may cause confusion. The paper should clearly define and explain the L-LA assignment method in the main text to ensure that the reader can easily understand the method.

### Questions
1. Lines 80-82: Is the annotation speed based on different labeling methods from the website https://www.makesense.ai/ measured by the authors? If so, how was it specifically carried out?
2. In practical manual annotation, can the angle and long edge achieve sufficient accuracy? What is the approximate error margin in manual annotations? The authors are supposed to provide further explanation in relation to "allowing for some margin of error" mentioned in Line 53.
3. How are negative samples selected? In the original FCOS, an ignore region is defined, where samples in the central area are positive and those in the outer region are negative. However, there appears to be no discussion of negative samples in L2RBox.
4. Does the designed scale loss produce similar effects for all categories? I believe targets with different aspect ratios may present varying levels of difficulty in such a loss optimization. For instance, the performance on the LV (large vehicle) category in DOTA-v1.0 is even lower than that achieved by point-supervised methods.
5. Lines 257-260: When facing densely arranged objects, is it appropriate to select the ground truth line with the shortest length as the target? What if a feature point is closer to a longer line in the feature map?

### Soundness
3

### Presentation
2

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
In the light of line annotation offers a cost-effective approach with orientation data, this paper presents the L2RBOX network, which employs line annotation for oriented object detection. The detector's architecture is based on FCOS and leverages the minimum circumscribed circle and horizontal rectangles derived from the line annotation to supervise the prediction of size, angle, and position.

### Strengths
1) Line-supervised oriented object detection is a promising yet challenging task. Exploring how to balance annotation costs and detection performance through line annotations is also an intriguing area of research.

2) The proposed L2RBox demonstrates performance that is comparable to fully RBox-supervised methods in certain scenarios.

### Weaknesses
1) The line annotation provides orientation information but lacks some size details compared to the HBox annotation. The key issue is how to derive the missing size information from the line annotation, which only represents a single axis. This paper assumes that the major and minor axes of the object are equal. The proposed solution is to expand the line annotation into circle and square representations, which are not specifically designed to address the missing size information. The expansion to a circle, using the line as a diameter, inherently assumes a 1:1 aspect ratio, which is a strong and often unrealistic constraint for many real-world objects. This approach does not account for the variability in object shapes and proportions, potentially limiting the model's ability to accurately predict bounding boxes for objects with significant aspect ratio deviations.

2) The proposed speed-accuracy tradeoff is represented by the product of normalized accuracy and time efficiency. The author should review related literature and discuss the validity of this indicator. The use of a simple product of normalized accuracy and time efficiency as a trade-off metric is questionable. This metric does not account for the relative importance of accuracy versus speed, which can vary significantly depending on the application. A more robust approach would involve using a weighted sum or a Pareto front analysis to better capture the multi-objective nature of the problem. Furthermore, the normalization method used can significantly impact the results, and the paper lacks a detailed justification for the chosen normalization technique.

3) The network structure is heavily based on FCOS and lacks validation for generalizability across other detection paradigms, making it challenging to assess the effectiveness of the proposed methods. The reliance on FCOS limits the assessment of the core line-to-RBox conversion method. The paper does not explore how the proposed method would perform with other detection architectures, such as anchor-based methods like Faster R-CNN or single-stage detectors like RetinaNet. This lack of experimentation limits the generalizability of the findings and makes it difficult to determine if the observed performance is due to the proposed method or the specific characteristics of the FCOS architecture.

### Questions
1) Have you considered implementing a specific design to predict the minor axis length (i.e. width)? Using statistical priors for aspect ratios across different object classes or estimating the minor axis length based on contextual information could be effective approaches.

2) It would be helpful if the authors could present prediction accuracy for the major and minor axes separately and provide additional analysis.

3) The scaling ratio parameter "k" is introduced to represent the annotated object width for center-ness calculations. However, it appears that "k" does not contribute to performance. Could you clarify the purpose of this hyperparameter?

4) The author could enhance Fig. 5 by providing additional information. For instance, the trade-off balance could be more effectively illustrated by calculating the area under the accuracy-efficiency scatter curve for different classes or subsets, where applicable.

5) Is this Line-to-RBox method adaptable as a plug-and-play approach for other common detectors, such as RetinaNet or Faster-RCNN?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel annotation format for oriented object detection, line annotation, which is intermediate between point-level and box-level annotation. L2RBox is proposed as the first solution for the new proposed task setting, providing a baseline for future research.

### Strengths
The research topic is new and the overall writing quality is good. A new solution for weakly supervised oriented object detection based on line annotations is proposed. Experiments on DOTA and DIOR are reported, providing a baseline for future research. If the task setting can be proven useful, it can open up a new field for exploration.

### Weaknesses
My major concern is the evidence to prove the meaningness of line-supervision setting is not solid. The main evidence is the claim that the line annotation is faster than HBox (according to https://www.makesense.ai/), but I cannot find such information in the provided link.

Given that both lines and HBoxes are determined by two points, how come lines are much faster than HBoxes? Furthermore, the comparison of annotation times appears to be based on inconsistent levels of annotation accuracy. It seems that annotators are instructed to carefully fit HBoxes and RBoxes to the object, while line annotations are treated as a simple, coarse marking. This discrepancy in annotation instructions makes the time comparison unfair and potentially misleading. The authors should clarify whether RBoxes are annotated using three or four points, as this impacts the annotation time comparison. The theoretical moving distance argument is also problematic, as it assumes that annotators do not zoom in to improve accuracy, which is unrealistic. If annotators zoom in, the time required increases, making the comparison of annotation times without ensuring comparable accuracy meaningless. Finally, the authors claim that their method is robust to inaccurate line annotations, but they do not provide a comparison to HBox methods under similar conditions of inaccuracy. This makes it difficult to assess the true benefit of line annotations.

### Questions
1. Given that both lines and HBoxes are determined by two points, how come lines are much faster than HBoxes? 
2. Is the detector trained with line annotations more robust to the annotation inaccuracy than those trained with HBoxes?

### Soundness
3

### Presentation
3

### Contribution
3
