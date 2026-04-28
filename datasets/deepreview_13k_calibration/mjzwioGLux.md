# ROBUST SPARSE AND DENSE MATCHING

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Finding corresponding pixels within a pair of images is a fundamental computer vision task with various applications. Due to the specific requirements of different tasks like optical flow estimation and local feature matching, previous works are primarily categorized into dense matching and sparse feature matching focusing on specialized architectures along with task-specific datasets, which may somewhat hinder the generalization performance of specialized models. In this paper, we propose RSDM, a robust network for sparse and dense matching. A cascaded GRU module is elaborately designed for refinement to explore the geometric similarity iteratively at multiple scales following an independent uncertainty estimation module for sparsification. To narrow the gap between synthetic samples and real-world scenarios, we organize a new dataset with sparse correspondence ground truth by generating optical flow supervision with greater intervals. In due course, we are able to mix up various dense and sparse matching datasets significantly improving the training diversity. The generalization capacity of our proposed RSDM is greatly enhanced by learning the matching and uncertainty estimation in a two-stage manner on the mixed data. Superior performance is achieved for zero-shot matching as well as downstream geometry estimation across multiple datasets, outperforming the previous methods by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed the robust network suitable for both sparse and dense matching tasks called RSDM. In this work, simlarity matrix/cost volume of three scales are generated with feature level refinement and GRU based correlation volume level refinement. Context level information is also used to guide the GRU refinemnet block for the first scale.  For sparsification, warp error based on predicted dense matching results are used to estimate the uncertainty while balanced sampling strategy are use. This work also generate a dataset based on TartanAir with optical flows generated. Experiments are hold based on several banchmarks outperforming the previous methods by a large margin however several experimental results have to be provided.

### Strengths
1) Using flow to achieve cross-scale transfer of matching relationships is an efficient solution.
2) The ability to scale to diverse downstream tasks makes this approach attractive.

### Weaknesses
1. The problem statement of  "robust for sparse and dense matching":

   What are the main differences between the RSDM and the methods only fit for sparse or dense matching task? The RSDM seems designed based on original dense metching pipelines such as GMFlow with uncertainty estimation(from DKM) for sparsifiy the dense matching result. Can this setting be used in other dense matching works to make it suitable for sparse matching tasks?

2. The effectiveness of multi-scale design:

   The method used the FPN and  generate simlarity matrix in three scales. However, in the following three GRU Refinement Blocks only one  matrix seemes to be used. How about the matrixes in other two scales. Besides, further ablations on the multi-scale design should be provided.

3. The design of dataset:

   The proposed dataset seems like a subset of TartanAir dataset with a improved optical flow rendering method. What is the main problem solved by building this data set? What are the advantages over previous datasets besides better optical flow supervision? More experimental results based on this dataset need to be given.

4. Several results in ablation study is not clear:

   The data in the experimental table cannot clearly reflect the effectiveness of each module. For example, Table 1, what is the setting of RSDM? Is it the last row?

### Questions
See the Weakness part

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a robust sparse and dense matching network termed RSDM which can generalize well to unseen scenarios with our proposed cascaded GRU refinement for dense correspondence estimation and an uncertainty estimation module for sparsification.  The authors explore the effectiveness of scaling up the training data by mixing up multiple datasets. A comprehensive analysis is conducted to explore a more reasonable training strategy for enhanced robustness. The RSDM achieves state-of-the-art generalization performance in zero-shot evaluations for both matching and geometry estimation across multiple datasets, outperforming previous generalist and specialized models by an obvious margin

### Strengths
This paper propose a robust sparse and dense matching network termed RSDM incorporating the proposed cascaded GRU refinement module along with an uncertainty estimation module for sparsification. The decoupled training mechanism as well as the increasing diversity of the numerous training data contributes to the superior generalization performance in zero-shot evaluations for both matching and pose estimation.
The strengths are as follows:
1. The proposed RSDM can deal with both  sparse and dense matching task 
2. The proposed method mix up various dense and sparse matching datasets which significantly improves the training diversity.
3. Superior performance is achieved for zero-shot matching as well as downstream geometry estimation across multiple datasets, outperforming the previous methods by a large margin

### Weaknesses
The weakness are as follows:
1. The proposed model use high-weight parameters, swin-transformer, RAFT. It doesn't present the comparison with other methods.
2. The "Warping Error Map" is not detailed in paper, but it's important 
3. How to use "Uncertainty Map" in ransac filter, it should be given in detail.
4. In the experiments, the proposed method achieves good performance on zero-shot matching evaluations. but for Downstream pose estimation, it works not very well. Compared with DKM, its result is not very good. but the authors has no explanation.
5. There is no model size and runtime cost comparison with other methods.

### Questions
No questions

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a generalized dense matching network, capable of tackling both the optical flow and feature matching tasks simultaneously.  To do this, the authors propose a new model architecture that decouples the uncertainty estimation and investigate how to jointly train on a diverse set of flow and matching datasets.

### Strengths
* The authors provide a sound approach to matching, overcoming issues with confidence masks having different interpretations depending on the task by completely decoupling the certainty estimation as a posthoc step. The decoupling is also done in previous work (see PDCNet for example), but they do not detach gradients. What would have perhaps been even more interesting to see would be decoupling of the flow depending on the task. For example, small baseline tasks imply different priors on the types of flow that are likely. There is future potential in this type of approach.

* The paper, except for some minor mistakes, is easy to follow and well written. 

* The task is important and a method unifying small and large baseline matching would be of great interest to the community. (See UniMatch)

### Weaknesses
 * The model architecture is not well motivated. It seems similar to previous optical flow and dense feature matching works. It is not clear why the authors do not start from an established baseline like, e.g., PDCNet or GMFlow.

* The performance on pose estimation is significantly below previous work. The MegaDepth benchmark, which is commonly used, is only shown briefly in the ablation, but no state of the art comparison is provided. The performance is about 5% lower than DKM. On ScanNet the performance is about 3% lower. Also on optical flow the relation to state of the art methods is not documented.

* The ablation on the data is inconclusive. Adding optical flow datasets seem to lower results on pose estimation (Table 1). In the data ablation (Table 2) those results are no longer shown, why? Since those results are not shown, it must be assumed that adding more optical flow datasets further degrade performance.

* Overall message. The manuscript fails in convincing that, with the currently available datasets, unifying wide and small baseline stereo is a good idea. The authors make a good attempt, and their model performs well at both tasks, but worse than the specialized counterparts. Showing that it is possible to do both tasks has been previously shown (GLUnet), so what remains to be shown is that the joint paradigm is superior.

### Questions
1. What is the motivation of the architecture choice (see first weakness)?

2. Why does adding optical flow datasets reduce performance (see third weakness)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
