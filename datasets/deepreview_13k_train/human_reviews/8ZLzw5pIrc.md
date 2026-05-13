# Order-aware Interactive Segmentation

- Decision: Accept
- Scores: 6, 6, 6, 5, 5, 8

## Abstract
Interactive segmentation aims to accurately segment target objects with minimal user interactions. However, current methods often fail to accurately separate target objects from the background, due to a limited understanding of order, the relative depth between objects in a scene. To address this issue, we propose OIS: order-aware interactive segmentation, where we explicitly encode the relative depth between objects into order maps. We introduce a novel order-aware attention, where the order maps seamlessly guide the user interactions (in the form of clicks) to attend to the image features. We further present an object-aware attention module to incorporate a strong object-level understanding to better differentiate objects with similar order.  Our approach allows both dense and sparse integration of user clicks, enhancing both accuracy and efficiency as compared to prior works.  Experimental results demonstrate that OIS achieves state-of-the-art performance, improving mIoU after one click by 7.61 on the HQSeg44K dataset and 1.32 on the DAVIS dataset as compared to the previous state-of-the-art SegNext, while also doubling inference speed compared to current leading methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Order-Aware Interactive Segmentation (OIS), combining order-aware and object-aware attention to improve segmentation accuracy and efficiency. Order maps help distinguish object depths, while foreground-background separation aids object differentiation. Using both dense and sparse prompt fusion, OIS achieves state-of-the-art results on HQSeg44K and DAVIS, boosting accuracy and speed.

### Strengths
1. The paper is well-written, with clear motivation.
2. It provides extensive experiments that convincingly demonstrate the proposed method's effectiveness.
3. The visualized analysis adds value by highlighting the necessity of incorporating depth information.
4. The method's performance surpasses current state-of-the-art methods.

### Weaknesses
1. The paper exceeds the ICLR 2025 10-page limit with 11 pages in the main text.
2. Overall, the technical contribution and novelty of this paper are incremental, as it mainly incorporates existing priors, such as depth maps and foreground-background masks, to enhance segmentation accuracy. Since these priors have already proven effective in general segmentation tasks, their success in interactive segmentation is unsurprising. I would encourage the authors to clarify the unique benefits these priors bring specifically to interactive segmentation.
3. The rationale for the ordering of Object-level Understanding before Order-level Understanding is unclear. Could the authors explain if this order enhances performance or if alternative orderings were tested?
4. The modules for Object-level and Order-level Understanding are connected sequentially. Why was a parallel structure not considered? Could it improve performance or efficiency?
5. Similar work (see [1]) also enhances foreground-background distinction in interactive segmentation; this should be discussed.
6. The paper lacks ablation studies on Mask Guidance within the object-aware and order-aware attention modules. For example, testing the effects of different Mask Guidance qualities would be beneficial.
7. It is unclear whether OIS can handle interactive segmentation for multiple objects simultaneously. Since Object-level Understanding relies on Mask Guidance from previous interactions, if the target object changes between clicks, OIS may struggle to shift focus to the new target due to constraints from the previous mask. This limitation could reduce the method's practical utility.

### Questions
1. Would it be possible to show corresponding depth maps in Figure 6 to help readers better understand the importance of order-aware attention?
2. As the number of negative clicks increases, does the model generate a unique order map for each negative prompt? If so, this approach could result in significant memory usage. Has the author considered selectively merging these maps? Since repeated negative clicks are likely to target very localized areas, the corresponding depth maps would likely have high similarity, making unique order maps for each negative prompt potentially redundant.
3. Would lower-quality depth maps directly impact OIS performance, and conversely, would higher-quality maps improve it?

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
5

### Summary
The paper proposes order-aware interactive segmentation, which utilizes the extra relative depth information from pre-trained monocular depthanything v2 to generate the order maps. Then the order maps are used to guide the sparse embeddings to attend to the image features via mask attention. Object-aware attention is also used to help boost performance. Prompts are integrated via both the sparse and dense fusion. The paper validates its experiment design on HQSeg44K and DAVIS benchmark.

### Strengths
1. The paper has a good writing and structure, where the paper ideas and figures are easy to read and understand.

2. The paper validates its model design choice in Sec 4.5 and Table 4, which shows the performance gain brought by each proposed component clearly.

3. Using relative depth order to guide segmentation is an interesting idea, where the proposed order map considers both the positive and negative clicks.

### Weaknesses
1. The paper utilizes additional monocular depth prediction as input. In Table 3, does the computing cost of the depth model also get included? The paper should also study the impact of using various depth prediction models to the segmentation performance.

2. The robustness of the segmentation model to the errors brought by depth prediction network is not studied. When depth prediction makes large errors, how will it influence the segmentation model? Especially, when segmenting neighboring objects with close depth distance, how much can the depth model contribute? 

3. Consider the importance of Table 4, besides DAVIS, an ablation experiment also on HQ-Seg44K should also be performed to have a more comprehensive understanding of each proposed component.

4. The paper has a limited tech novelty, where the order map guiding attention is borrowed from Mask2Former and the object-aware attention is from Cuite. The depth prediction is from a pretrained depthanything v2 model. Using depth to guide more accurate segmentation is also introduced in [a, b]. This makes the paper more like a combination of existing components and model designs.

5. The paper misses an ablation experiment on order maps designs considering both for positive and negative clicks. What if only considering the order maps for positive or negative clicks alone?

### Questions
What's the advantage of using depthanything v2's pretrained backbone in model's segmentation accuracy? besides saving parameters, how does it compare to the image encoder of SAM?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
1. This paper proposes order-aware attention, which integrates order (relative depths between objects) into interactive segmentation, improving the model’s ability to distinguish target objects based on their relative depths from one another. 
2. This paper introduces object-aware attention to incorporate a strong understanding of objects.
3. This paper combines both dense and sparse integration of prompts, improving the alignment between the image and prompts while maintaining efficiency. 
4. This work achieves good performance with lower latency.

### Strengths
1. The method looks very good for segmenting some difficult foreground objects (tennis rackets, bicycle wheels, etc.).
2. The order-aware attention module introduced in this paper is easy to accept and effective.
3. The framework of this paper is relatively concise and the implementation is easy to understand.

### Weaknesses
1. The method section of this paper is relatively easy to understand, but the motivation and problems to be solved are not concise enough. The author seems to want to solve many problems and propose many improvements, which can easily lead to readers not understanding why the author proposes certain techniques. Specifically, the paper introduces order-aware attention and object-aware attention, but the precise limitations of existing methods that necessitate both of these modules are not clearly delineated. The connection between the identified problems (occlusions, multiple interacting objects, thin objects with vibrant backgrounds) and the proposed solutions (order and object awareness) needs to be more explicitly established. For example, how does order-aware attention specifically address the issue of occlusions, and how does object-aware attention help with thin objects against complex backgrounds? The paper would benefit from a more focused problem statement that clearly articulates the shortcomings of current interactive segmentation methods and how the proposed techniques directly address these shortcomings.
2. The experiments of this paper is insufficient, lacking results on typical interactive segmentation datasets, such as GrabCut, Berkeley, SBD, PascalVOC, etc. In addition, there is a lack of comparison with some recently published (CVPR 2024, etc.) interactive segmentation methods. The evaluation is primarily on HQSeg44K and DAVIS, which are not standard benchmarks for interactive segmentation. While these datasets have their merits, the absence of results on widely used datasets makes it difficult to assess the generalizability and comparative performance of the proposed method. Furthermore, the lack of comparison with recent methods, particularly those from CVPR 2024, leaves a gap in understanding the state-of-the-art performance. The paper should include results on standard datasets and compare against more recent publications to establish its position in the field.
3. I admit the practical value of this paper, but I think it is more suitable to be published in CVPR rather than ICLR.

### Questions
1. Can the author connect and refine the motivation and the problem to be solved in this paper?
2. See Weaknesses section.

### Soundness
4

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
This paper presents OIS, which explicitly encodes the relative depth between objects into order maps. It introduces an order-aware attention mechanism that guide the user interactions to attend to the image features by the order maps, and an object-aware attention module for better differentiation of objects with similar order. Experiments demonstrate the effectiveness and efficiency of OIS.

### Strengths
1. The OIS integrates relative depths between objects, into interactive segmentation, improving the model’s ability to distinguish target objects.
2. Experimental results show quite good effectiveness.

### Weaknesses
1. The OIS integrates relative depths between objects, into interactive segmentation, improving the model’s ability to distinguish target objects.
2. Experimental results show quite good effectiveness.

1. The difference between order-aware attention and object-aware attention proposed in this paper and masked attention seems to be only in the source of input mask, so both are slightly innovative.
2. In the comparative experiments of this paper, most of the traditional interactive segmentation methods (training on COCO) and SAM-based methods (training on SA-1B) have not been trained on HQSeg44K, while OIS is trained and tested on this dataset. The data quality of HQSeg44K is higher than that of COCO, so the fairness of the experiment is uncertain.

### Questions
The main motivation of this paper is to enhance the ability of interactive segmentation through depth information, but the paper seems to only show the cases where the depth of different positions of the same object is not very different, and there is little discussion about the effectiveness of the proposed method when the depth of different positions of the same object is very different (such as the bridge of DepthAnything visualization).

### Soundness
3

### Presentation
3

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
Authors propose the order-aware interactive segmentation (OIS) to explicitly encode the relative depth between objects into order maps. Authors introduce a novel order-aware attention, where the order maps seamlessly guide the user interactions (in the form of clicks) to attend to the image features. Authors further present an object-aware attention module
to incorporate a strong object-level understanding to better differentiate objects with similar order. OIS achieves state-of-the-art performance, improving mIoU after one click by 7.61 on the HQSeg44K dataset and 1.32 on the DAVIS dataset

### Strengths
1.	OIS can distinguish target objects based on their relative depths from one another and better differentiate objects with similar order.
2.	OIS improves the computational efficiency.
3.	OIS achieves competitive performance

### Weaknesses
1. The Concept of Order. Authors should reevaluate the current definition of 'order,' which is often misleading. The term 'order' should pertain to the sequence of click instead of depth map in interactive segmentation. 
2. Insufficient ablation study. More ablation studies are required to clarify the reason of performance improvement, for example the order of object-level attention and order-level attention, and the different pretrained weights of backbone, such as Depth Anything V1.
3. Unfair comparison. OIS adopts Depth Anything V2 as backbone, while Depth Anything V2 requires much more (about 6x) pretraining images than SAM and other backbone. And MM-SAM (Table 5 in Appendix) with Depth Anything V2 achieves similar performance with OIS w/o order and object attention (Table 4). The comparison is unfair. Authors should conduct more experiments to further verify the effectiveness of order map. For example, authors can freeze the backbone of SAM and train an additional depth head to obtain the depth map. Then authors train the object and order attention to verify that the improvement comes from the order map instead of better pretrained backbone.
3. Limited novelty. OIS integrates the object attention from Cutie and depth map into interactive segmentation. However, the novelty is somewhat constrained.

### Questions
1. Using the same order map for all positive points may be too naive and in may condition, the depth values of different positive points maybe different.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work studies the interactive segmentation task. Based on the prior knowledge that ground and background objects are located at different depths, this work proposes a new framework named OIS. OIS effectively takes advantage of a corresponding depth map via the proposed order- and object-aware attention. Experiments demonstrate that OIS effectively improves segmentation performance by fewer clicks and boosts inference speed.

### Strengths
The manuscript is clearly written and easy to follow. The whole framework is built upon the fact that different objects should be located at various depths in the original 3D scenes, which is promising. Both qualitative and quantitative comparisons demonstrate its superior performance.

### Weaknesses
Overall, I feel quite OK with this work, and there are no MAJOR weaknesses. See below for several suggestions and typos.

- It is better to visualize the five clicks in Fig. 1 for an improved presentation.
- Paragraph 2, Sec. 1, Page 1: Redundant '(' before 'RITM'.
- Paragraph 2, Sec. 1, Page 2: Better to delete 'However' before 'current methods fail to ...'.
- The blue dots in Fig. 3 are inconspicuous. Please consider another conspicuous color.

### Questions
Please refer to the WEAKNESSES part.

### Soundness
3

### Presentation
3

### Contribution
3
