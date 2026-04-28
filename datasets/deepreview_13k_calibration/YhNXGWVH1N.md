# LeanFlex-GKP: Advancing Hassle-Free Structured Pruning with Simple Flexible Group Count

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Densely structured pruning methods — which generate pruned models in a fully dense format, allowing immediate compression benefits without additional demands — are evolving owing to their practical significance. Traditional techniques in this domain mainly revolve around coarser granularities, such as filter pruning, thereby limiting their performance due to restricted pruning freedom.

Recent advancements in *Grouped Kernel Pruning (GKP)* have enabled the utilization of finer granularity while maintaining the densely structured format. We observed that existing GKP methods often introduce dynamic operations to different aspects of their procedures, where many were done so at the cost of adding complications and/or imposing limitations — e.g., requiring an expensive mixture of clustering schemes; or having dynamic pruning rates and sizes among groups, which lead to reliance on custom architecture support for its pruned models.

In this work, we argue the best practice to introduce such dynamic operation to GKP is to make `Conv2d(groups)` (a.k.a. group count) flexible under an integral optimization, leveraging its ideal alignment with the infrastructure support of *Grouped Convolution*. Pursuing such direction, we present a one-shot, post-train, data-agnostic GKP method that is more performant, adaptive, and efficient than its predecessors; while simultaneously being a lot more user-friendly with little-to-no hyper-parameter tuning or handcrafted criteria required.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a fine-grained pruning approach, which exploits grouped kernel pruning (GKP) with self-designed clustering and pruning methods, corresponding to high performance and general efficient inference speed. The authors identify that the existing methods correspond to coarse-grained pruning with inferior accuracy performance. In addition, they propose a grouping method to enable exploiting general infrastructure with the pruned model. Then, they propose a L-2 geometric method-based grouped kernel pruning method to perform the pruning operation. Furthermore, they exploit a post-pruning group count evaluation to evaluate the pruned model. They conducted experimental comparison with 5 baseline approaches, which demonstrates the advantages of the proposed approach.

### Strengths
1. The authors propose a find-grained pruning method that can have higher accuracy performance.
2. The introduction section is detailed with the presentation of the background explanation.
3. The experimental results seems promising.

### Weaknesses
1. The structure of the paper can be improved. Sections 1 and 2 are too detailed that Section 3 corresponds to only a small part, which is not enough to explain the major contribution.
2. 5 baseline approaches are compared while some lossless approaches or other baselines can be added as baseline approaches.
3. It is not clear whether the proposed method can achieve lossless pruning. Some theoretical analysis may be beneficial to the paper.
4. Many grammar errors, e.g., an higher ***, they can be run, with in, is determine by, with lowest etc.
5. Dependable experience may be independable experience.

### Questions
1. I wonder if "dependable experience" should be independable experience. 
2. I wonder if the proposed approach is lossless. In addition, I wonder if the proposed approach can be applied to other structures.
3. I wonder if the authors can compare the proposed approach with lossless pruning methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes that the best practice to introduce the dynamic operations to GKP is to make Conv2d flexible under an integral optimization, and proposes a one-shot, post-train, data-agnostic GKP method.

### Strengths
1. The writing is clear.
2. The background about Different Structured Pruning Granularities, Grouped Kernel Pruning, and Dynamic Structure Pruning is clearly introduced.
3. The idea of making Conv2d flexible under an integral optimization is interesting.

### Weaknesses
1. The evaluation lacks comprehensiveness.

- Baselines are restricted. A lot of related works about iterative structured pruning [1-10] and one-shot pruning [11-15] are not compared.

- Most of the evaluation focuses on the ResNet and VGG architectures. It will be better if more model architectures are evaluated, especially small models like MobileNet, EfficientNet, and ShuffleNet.

- In Section 4, it will be better if some insights can be provided, not only listing numbers.

2. The Ablation Study is missing.

3. The structure can be improved. The Introduction occupies too much space. The first 3.5 pages are all about the Introduction. 

4. The discussion about the related works is insufficient, such as iterative structured pruning [1-10], one-shot pruning [11-14], Grouped Kernel Pruning [15], and automatic pruning (with little-to-no hyper-parameter tuning) [2, 3].

### Questions
1. Can authors compare the proposed method with more related pruning works [1-14] (See above)?

2. Can some ablation study be provided?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes LeanFlex-GKP, a new structured pruning method that builds on recent work in grouped kernel pruning (GKP). This method is a one-shot, post-train, and data-agnostic. The key idea is to make the number of groups flexible across layers rather than having dynamic operations during filter grouping or pruning stages.

### Strengths
- The paper clearly identifies limitations of existing GKP methods in terms of complexity from dynamic operations and proposes a sensible alternative via flexible group counts.
- The method delivers empirical results across a wide range of model architectures and datasets.
- As a one-shot, post-train, data-agnostic technique with minimal hyperparameters, LeanFlex-GKP is far easier to use out-of-the-box compared to many existing methods.

### Weaknesses
 - The contribution of this paper is limited. This paper seems an incremental work of TMI-GKP, and the main difference between this work and TMI-GKP is the group count evaluation.
- It would be better if the authors can provide the experimental settings, such as hyperparameters they used for different models.
- From my understanding, LeanFlex-GKP also includes dynamic choices of clustering schemes in each of its convolutional layers as TMI-GKP. I would appreciate it if the author can give results of the performance of LeanFlex-GKP and TMI-GKP. I can only get limited information from Table 1 to Table 5.

### Questions
- Could the benefits of dynamic group counts extend to other structured pruning granularities like filter or channel pruning?
- Is there an optimal strategy for setting group counts or do they need to be exhaustively evaluated?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
