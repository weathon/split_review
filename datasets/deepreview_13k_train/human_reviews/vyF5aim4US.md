# QFree-Det: Query-Free Detector with Transformer and Sequential Matching

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Transformer-based detectors, such as DETR and DINO, often struggle with a specific limitation: they can detect only a fixed number of objects based on the predefined number of queries set. This limitation leads to missed detections when the scene exceeds the model’s capacity and increases false positives when the scene contains fewer objects. In addition, existing approaches often combine one-to-one and one-to-many matching label assignment methods in the decoder for accelerating the model training and convergence. However, this operation can introduce a new detecting ambiguity issue, which is often overlooked by those methods. To address these challenges, we propose QFree-Det, a novel query-free detector capable of dynamically detecting a variable number of objects across different input images. In particular, we present an Adaptive Free Query Selection (AFQS) algorithm to dynamically select queries from the encoder tokens, which resolves the issue of fixed capacity. Then, we propose a sequential matching method that decouples the one-to-one and one-to-many processes into separating sequential steps, effectively addressing the issue of detecting ambiguity. To achieve the sequential matching, we design a new Location-Deduplication Decoder (LDD) by rethinking the role of cross-attention (CA) and self-attention (SA) within the decoder. LDD first regresses the location of multiple boxes with CA in a one-to-many manner and then performs object classification to recognize and eliminate duplicate boxes with SA in a one-to-one manner. Finally, to improve the detection ability on small objects, we design a unified PoCoo loss that leverages prior knowledge of box size to encourage the model to pay more attention to small objects. Extensive experiments on COCO2017 and WiderPerson datasets demonstrate the effectiveness of our QFreeDet. For instance, QFree-Det achieves consistent and remarkable improvements over DINO across five different backbones. Notably, QFree-Det obtains a new state-of-the-art of 54.4% AP and 38.8% APs on val2017 of COCO with the backbone of VMamba-T under 1× training schedule (12 epochs), higher than DINO-VMamba-T by +0.9% AP and +2.2% APs. The source codes will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a novel query-free detector, QFree-Det, aimed at addressing the limitation of a fixed number of object queries in Transformer-based detectors such as DETR and DINO. The authors propose an Adaptive Free Query Selection (AFQS) algorithm and a sequential matching method, which significantly enhance the model's capability to dynamically detect a variable number of objects across different input images. Additionally, a new loss function, PoCoo, is designed to improve detection capabilities. The experimental results demonstrate that QFree-Det achieves remarkable performance on multiple datasets and various backbone networks.

### Strengths
> 1. Motivation:

The paper introduces the QFree-Det model, addressing the variable number of instances in different images, which is a pertinent issue in object detection. The proposal for a dynamic query selection approach is innovative and could significantly enhance the flexibility and accuracy of detection models.

> 2. Performance Improvement:

The paper demonstrates some performance improvements on the WiderPerson dataset, particularly in detecting small objects, which is a challenging aspect of computer vision.

### Weaknesses
 > Comparison with DETA and DDQ-DETR:

The discussions in Section 3.1.3 regarding the role of Self-Attention (SA) bear similarities to the disscussions taken in "NMS Strikes Back" (DETA) [1] and "Dense Distinct Query for End-to-End Object Detection" (DDQ-DETR) [2]. Both papers explore the effectiveness of traditional non-maximum suppression (NMS) and the role of SA integrated with transformer-based detectors, which is a relevant area of comparison for QFree-Det. Specifically, the paper should more clearly differentiate its approach from the deduplication strategies employed by DETA, which uses NMS for both query selection and post-processing, and DDQ-DETR, which combines NMS-based filtering with Hungarian matching. The current discussion lacks a detailed analysis of how QFree-Det's method of handling duplicate detections differs from these established techniques, particularly given that these methods also address the issue of redundant bounding boxes.

> Comparative Experiments in Table 3:

While the paper provides comparisons with models like DINO, it lacks a comprehensive set of comparative experiments with other state-of-the-art Transformer detectors, such as Stable DINO and CO-DINO. Including these comparisons would provide a more holistic view of QFree-Det's performance relative to the current landscape of object detection models. The absence of these comparisons makes it difficult to assess the true novelty and effectiveness of QFree-Det against the most competitive baselines. Specifically, the paper should include a direct comparison with Stable DINO, which also employs a stable matching strategy, and CO-DINO, which utilizes collaborative hybrid assignments, to better contextualize the performance gains of QFree-Det.

> Performance Comparison with Fixed Detectors:

The paper compares the performance of QFree-Det (AP 50.5) with DINO (AP 49.0). However, it is noted that improved versions of DINO, utilizing focal loss, have achieved an AP of 50.0, as demonstrated in the MMDETECTION repository. This raises the question of whether other state-of-the-art fixed detectors, when combined with loss functions like PoCoo or IA-BCE, could potentially outperform QFree-Det. Further experimentation and comparison with these models would be beneficial to assert the superiority or uniqueness of QFree-Det's approach. The paper should explore whether the performance gains are primarily due to the novel architecture or the proposed loss function, and whether these gains are specific to the QFree-Det architecture or can be generalized to other fixed-query detectors.

### Questions
> The number of decoder layers.

It seems decoder only have one layer of CA and 6 layers of SA?

> Speed of inference.

How fast can the QFree-Det be for some sparse scenario, i.e., only a instance in a image.

> Performances in line 476

Is the same experiments (47.1) as that of line 248?

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
This paper proposes QFree-Det, a novel query-free detector based on transformers, aiming to address the limitations of fixed query numbers and detection ambiguity in existing transformer-based detectors. The main contributions include the Adaptive Free Query Selection (AFQS) algorithm and the Location-Deduplication Decoder (LDD) framework.

### Strengths
-The AFQS algorithm and LDD framework provide a novel solution to the challenges of fixed query limitations and detection ambiguities that are common in traditional transformer-based detectors like DETR and DINO.

-The model achieves state-of-the-art results on the COCO2017 and WiderPerson datasets, particularly excelling in small object detection. This demonstrates the effectiveness of the proposed method over existing leading techniques.

-By enabling  dynamic query selection, QFree-Det effectively adapts to varying scene complexities, providing a robust framework for diverse detection scenarios.

-The introduction of the PoCoo loss function significantly enhances the detection capabilities for small objects, addressing a common challenge in object detection.

### Weaknesses
 -The authors propose AFQS algorithms and LDD frameworks, but lack in-depth theoretical analysis.  There is no detailed explanation of why removing location queries (PQ) does not significantly affect model performance, nor is there a theoretical proof of how LDD can effectively solve the detection ambiguity problem. The interaction between the content and positional queries, and the specific mechanisms by which the LDD framework mitigates ambiguity, require more rigorous justification. The paper would benefit from a more detailed analysis of the roles of cross-attention and self-attention in the decoder, and how these interactions are impacted by the removal of positional queries and the introduction of the LDD framework.

-Insufficient comparison with state-of-the-art methods, In Table 3, the authors mainly compare with older methods such as DINO, but lack detailed comparisons with more recently published methods (e.g. DAC-DETR, Co-DETR, etc.). This makes it difficult to assess the position of QFree-Det in the current research frontier. The comparisons should include a wider range of contemporary methods, and the specific advantages of QFree-Det over these methods should be clearly articulated. The paper should also address the limitations of the compared methods and how QFree-Det overcomes them.


-The author mentions that AFQS can reduce redundant queries, but does not provide a detailed computational complexity analysis or efficiency comparison with other methods. Lack of specific inference time and memory usage data. The analysis should include a breakdown of the computational cost of each component of the model, and a comparison of the inference time and memory usage with other state-of-the-art methods. The paper should also discuss the trade-offs between accuracy and computational cost, and how the proposed method balances these trade-offs.

-Although the improvement of the PoCoo loss function for small object detection is shown in Table 7, there is no in-depth analysis of why this loss function can be particularly effective in improving small object detection performance. The paper should provide a detailed explanation of how the PoCoo loss function addresses the challenges of small object detection, and how it differs from existing loss functions. The analysis should include a discussion of the gradient behavior of the loss function, and how it affects the training process.

### Questions
-How does QFree-Det perform on other challenging datasets beyond COCO and WiderPerson? Are there specific scenarios where QFree-Det might underperform?

-Can you provide a more detailed analysis of the trade-offs between performance and computational cost in QFree-Det?

-How does the AFQS algorithm scale with increasing image complexity and object density?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose QFree-Det, a query-free detector that select dynamic queries from encoders and decouples one-to-one and one-to-many matching in sequential way. It achieves remarkable improvements compared to the DINO baseline.

### Strengths
1. The paper analyze the ambiguity problem overlooked in current one-to-many detectors, and propose a new sequential matching method to tackle this problem, which is not explored before.
2. The paper is well-written and the experiments are comprehensive.

### Weaknesses
The dynamic query selection mechanism is similar to the distinct query selection process in DQS[1]. And the sequential matching process is similar to the hybrid layers in H-DETR[2] and MS-DETR[3]. It is better to add citation and discussion with them. The paper does not adequately address the novelty of the dynamic query selection mechanism, particularly in comparison to methods that also select a subset of queries from the encoder outputs. The sequential matching process, while presented as a novel contribution, bears a resemblance to existing approaches that use hybrid layers or sequential processing of object queries. The lack of a clear distinction from these methods weakens the claims of novelty. Specifically, the paper should clarify how its approach differs from the iterative refinement strategies used in other DETR-based models. The paper would benefit from a more rigorous analysis of the computational cost and efficiency of the proposed method compared to existing methods.

### Questions
See the weakness part

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
5

### Summary
Transformer-based detectors like DETR and DINO have a fixed capacity for detecting objects, leading to missed detections and false positives. To overcome these limitations, QFree-Det is proposed as a dynamic, query-free detector that adapts to varying object counts in input images. It features an Adaptive Free Query Selection (AFQS) algorithm for flexible query selection and a Location-Deduplication Decoder (LDD) that separates one-to-one and one-to-many detection processes to reduce ambiguities. Additionally, a unified PoCoo loss enhances small object detection.

### Strengths
1. The idea of producing a flexible number of queries to predict a flexible number of detections, is interesting.
2. The paper is easy to follow, and the presentation is good.
3. The performance of the proposed QFree-Det compared to SOTAs looks good.

### Weaknesses
1. The contribution of AFQS is not strong enough. The main idea of the proposed Adaptive Free Query Selection (AFQS) algorithm: The fixed content query (CQ) is replaced by the proposed flexible self-adaptive decoder query (SADQ), where SADQ is obtained by sorting the classification scores of all N encoder tokens and selecting the scores above a certain threshold as M SADQ. In short, the AFQS algorithm is a simple strategy to reduce N queries into M queries by sorting the classification scores. I don't think it is enough to be a main contribution.
2. The novelty of sequential matching is incremental, where sequential matching combines Box Locating Part (One-to-many matching), and Deduplication Part (One-to-one matching). One-to-many matching and One-to-one matching are the existing methods.
3. The framework of Box Locating Part (One-to-many matching) and Deduplication Part (One-to-one matching), looks complex. Deduplication Part (One-to-one matching) can be replaced by the parameter-free NMS. The Deduplication Part (One-to-one matching) looks more complex than NMS.
4. PoCoo loss is useful for small object detection. However, the connection between PoCoo loss and the motivation of designing a query-free detector, is very weak.
5. Dynamic query selection and the dual-step decoding process may require more computational resources, potentially impacting processing speed in real-time detection applications.
6. According to Table 5, free-query with AFQS only is worse than fixed-query.

### Questions
see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1
