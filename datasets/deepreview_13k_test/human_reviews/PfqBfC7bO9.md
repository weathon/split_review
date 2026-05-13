# Causal Unsupervised Semantic Segmentation

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Unsupervised semantic segmentation aims to achieve high-quality semantic grouping without human-labeled annotations. With the advent of self-supervised pre-training, various frameworks utilize the pre-trained features to train prediction heads for unsupervised dense prediction. However, a significant challenge in this unsupervised setup is determining the appropriate level of clustering required for segmenting concepts. To address it, we propose a novel framework, CAusal Unsupervised Semantic sEgmentation (CAUSE), which leverages insights from causal inference. Specifically, we bridge intervention-oriented approach (\textit{i.e.,} frontdoor adjustment) to define suitable two-step tasks for unsupervised prediction. The first step involves constructing a concept clusterbook as a mediator, which represents possible concept prototypes at different levels of granularity in a discretized form. Then, the mediator establishes an explicit link to the subsequent concept-wise self-supervised learning for pixel-level grouping. Through extensive experiments and analyses on various datasets, we corroborate the effectiveness of CAUSE and achieve state-of-the-art performance in unsupervised semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article introduces an algorithm CAUSE to address unsupervised semantic segmentation. The algorithm interprets the problem from a causal inference perspective, and mainly consists of two steps, i.e., building concept prototypes by maximising modularity and semantic grouping via concept-wise self-supervised learning. The algorithm has been evaluated on a set of segmentation datasets, like COCO-Stuff, Cityscapes, and VOC.

### Strengths
The causal inference perspective to solve unsupervised semantic segmentation is interesting and novel to me. The algorithm design basically makes sense, and shows promising performance on standard datasets.

### Weaknesses
My major concern revolves around Sec. 3.3. Writing in this part is not good. It is hard to understand all implementation details. __First__, it is unclear how Eq. 4 is derived. Since this is probably the most important part of the algorithm, more explanations should be given. __Second__, I am confused about how "find patch feature points in $T$ satisfying $\mathcal{D}_M[id_q,:]>\phi^+$" is implemented in practice. As far as I understand, $\mathcal{D}_M$ only summarizes prototype-prototype similarities; then how to select features based on the aforementioned rule? __Third__, for the statement "we set tight negative relaxation ..., ... emphasizing that hard negative mining is crucial to advance self-supervised learning", does a tight negative relaxation indicate easier negative mining?

The concept prototype bears high similarity with the work [ref1]. I am wondering whether the sinkhorn-knopp algorithm used in [ref1] can be used here for prototype generation. 

From Fig. 4, it appears that the method works particularly well in object boundaries (very close to ground-truths for, e.g., persons). While this is impressive for unsupervised segmentation, I am curious how the algorithm improves over other methods in boundary predictions.

There lacks description of training details. 

[ref1] Rethinking Semantic Segmentation: A Prototype View. CVPR 2022.

=======

overall, I am slightly positive to the article. However, since I am not an expert in casual inference, I will see other reviewers' comments and make the final decision.

### Questions
see [weaknesses]

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an unsupervised semantic segmentation method based on theory of causal inference. It introduce a concept clusterbook to serve as mediator to decide the cluster granularity. The cluster gradularity is considered a challenge and the key that effects unsupervised semantic segmentation.

### Strengths
1. overall the paper is well written. 
2. The proposed pipeline of modularity clustering works well on benchmarks.

### Weaknesses
The link between proposed pipeline and causal inference is not clear, even though the authors  pays a lot of attention in explaining what's backdoor and frontdoor adjustments. In addition, some key details of the pipeline are not very clear, which requires further explainations.

### Questions
1. The link between the proposed method and the causal inference is not very clear. The authors do pay much attention on theory and formulation of frontdoor adjustment, however is there explicit link between it with the proposed pipeline? that is between equation 1 and the algorithm 1 and 2. 

2. Calculation of affinity matrix is time consuming? how many samples does it use while calculating the affinity matrix? Does the codebook update while training? or fixed based on pretrained DINO features? In addition, how to guarantee the the codebook spans different levels, how to decide the propoer granularity? 

3. STEGO has similar mechanism of contrastive learning. which module does the proposed method benefits more from?  The codebook or the ST learning? 

4. A minor issue is that the ALGORITHM 1 should be placed near sec. 3.2 to prevent confusing

### Soundness
3 good

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
This paper discusses the task of unsupervised semantic segmentation (USS). The author proposes a new method called CAUSE, integrating USS into a causal problem through two steps: learning discrete sub-segmented representation with Modularity theory and conducting do-calculus with self-supervised learning in the absence of annotations. CAUSE bridges causal inference into unsupervised segmentation and obtain semantically clustered groups with the support of pre-trained feature representation. Extensive experiments on various datasets corroborate the effectiveness of CAUSE and achieve state-of-the-art results.

### Strengths
** The authors innovatively treat the USS task as a causal problem to solve the problem of determining the appropriate cluster level. 

** The authors propose a discrete sub-segmented representation learning method using Modularity theory, which compensates for the lack of semantic understanding in traditional unsupervised segmentation methods.

** The authors introduce causal inference into the unsupervised segmentation task and enable semantic segmentation with self-supervised learning in the absence of annotations.

** The authors propose a concept drift detection method based on causal relationships, which can effectively detect the concept drift problem in unsupervised semantic segmentation.

### Weaknesses
** This paper lacks a detailed explanation of the specific methodologies used for constructing the concept clusterbook and conducting concept-wise self-supervised learning.

** The paper could benefit from a detailed explanation of the implementation details, such as the specific architectures used for the segmentation head and the pre-trained model.

** This paper does not discuss the limitations or potential drawbacks of the proposed framework, which would have been useful for readers to understand the scope and applicability of the approach.

** The comparison with recent and state-of-the-art methods in unsupervised semantic segmentation is missing, which could provide a comprehensive evaluation of the proposed framework.

### Questions
**  Please discuss the limitations or potential drawbacks of the proposed framework? It would be helpful for readers to understand the scope and applicability of the approach.

** Please provide more details on the implementation, such as the specific architectures used for the segmentation head and the pre-trained model?

**  Please discuss the computational complexity of the proposed framework? Please provide any insights or analysis on the computational efficiency of the approach?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on unsupervised semantic segmentation and proposes a framework based on causal inference. Specifically, the proposed framework employs two-step pipline to solve the task, which is claimed as intervention-oriented approach (i.e., frontdoor adjustment). The proposed method first constructs a concept clusterbook as a mediator and then adopts concept-wise self-supervised learning for pixel-level grouping. Extensive experiments are conducted on various datasets to demonstrate the proposed method.

### Strengths
- The proposed method achieves performance improvements on various datasets.
- The visualizations are rich and abundant.

### Weaknesses
- The causal diagram is not solid. Why the path $T \rightarrow Y$ could be omit?
- The specific explanation about $U$ is missing. It is not convincing to use question as definition.
- What are the specific representations of  $T,M,Y,U$? E.g., $T \in \mathbb{R}^{D\times H\times W}$.
- Is there any instance or example for explaining Figure 2?
- The authors claim that the main goal is to group semantic concepts that  meet the targeted level of granularity. How do the items in clusterbook correspond to various granularities?
- Is is feasible to direct evaulate the mIoU based on results of the concept with respect to the index on clusterBook?

### Questions
See Weaknesses*

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
