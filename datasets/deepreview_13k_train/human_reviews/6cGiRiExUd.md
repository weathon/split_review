# Efficient Point Cloud Matching for 3D Geometric Shape Assembly

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Learning to assemble geometric shapes into a larger target structure is a fundamental task with various high-level visual applications. In this work, we frame this problem as geometric registration with extremely low overlap. Our goal is to establish accurate correspondences on the mating surface of the shape fragments to predict their relative rigid transformations for assembly. To this end, we introduce Proxy Match Transform (PMT), an approximate high-order feature transform layer that enables reliable correspondences between dense point clouds of shape fragments, while incurring low costs in memory and compute. In our experiments, we demonstrate that Proxy Match Transform surpasses existing state-of-the-art baselines on a popular geometric shape assembly dataset, while exhibiting higher efficiency than other high-order feature transform methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Proxy Match transform a low complexity feature transform that can be used in extracting correspondences for shape assembly. This approach tries to solve the quadratic complexity issue of high-order convolution by substituting it with a convolution with a common small-support proxy tensor that captures the local similarities among the shape.

### Strengths
Strong experimental results. This paper does not offer a lot of theoretical insight, but if the results are reproducible it will prove useful to a lot of practitioners

### Weaknesses
 - Lack of motivation: The role and derivation of the both the proxy tensor P and the learnable weight w should be better detailed. Specifically, the paper does not clearly articulate why a proxy tensor is a suitable substitution for high-order convolutions, nor does it explain the specific properties of the proxy that allow it to capture the necessary local similarities. The connection between the proxy and the underlying geometric structure of the shapes is not sufficiently explored. The paper also lacks a clear explanation of how the learnable weight 'w' interacts with the proxy tensor to achieve the desired feature transformation. It is not clear why a single learnable weight is sufficient for this purpose, or how it is optimized during training.
- Limited theoretical insight: the paper feel a bit ad hoc, in the sense of "I have done this and it works." It is not clear how the architecture was derived. The paper lacks a rigorous mathematical justification for the proposed method. There is no analysis of the approximation error introduced by using the proxy tensor, nor is there a discussion of the conditions under which the proxy match transform is guaranteed to perform well. The paper would benefit from a more in-depth theoretical analysis of the proposed approach, including a discussion of its limitations and potential failure modes.

### Questions
See points above

### Soundness
3 good

### Presentation
3 good

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
This paper proposes a new technique for efficiently aligning surfaces of fractured objects for re-assembly. Its principal insight is that a convolution on a bipartite graph formed from samples on the two object parts (with $N$ and $M$ points respectively) can be simplified (in terms of time/compute resources) by routing the messages that aggregate samples through a proxy transform layer. If the number of heads in this layer is $O(H)$ for some constant $H$, then the presence of the proxy layer changes the quadratic ($N \times M$) complexity of the convolution to $O(H) \times \max{N, M}$ (correct?)

### Strengths
The core of the method is a new technique to compute convolutions over the feature sets of the two fragments. The method is theoretically compelling and the authors do a good job of justifying it theoretically and practically. The experimental section seems thorough and validates the method vs several baselines.

### Weaknesses
The paper is written in a way that is rather difficult to follow -- I would suggest doing another pass (maybe with feedback from some external readers) to make the language more simple and streamlined.

I am also not entirely sure of the magnitude of the contribution. The proxy match transform is a clever trick that significantly enhances efficiency and accuracy in real-world training scenarios. But it sits inside a large pipeline that draws heavily upon previous work, and it is difficult to gauge its conceptual contribution. Is it a small tweak to make a big system better, or something so critical its impact goes beyond said big system?

For me, the second point puts the paper on the borderline, and the first point pushes it slightly below the threshold. I am open to revising the score based on the rebuttal and other reviewers' comments.

### Questions
Exposition:

- Since "shape assembly" is more commonly used to refer to assembling shapes from parts (e.g. a chair from seat, back and legs), it might be clearer to use "shape re-assembly" instead, or even "fractured shape re-assembly".

- "... two sets of features, $\mathcal{F}_P$ and $\mathcal{F}_Q$, associated with each point cloud" --> this reads as: each point cloud has two sets of features. You might want to rephrase as "... two sets of features $\mathcal{F}_P$ and $\mathcal{F}_Q$ associated with the two point clouds respectively" or something like that.

- Please don't use $P$, $\mathbf{P}$ and $\mathcal{P}$ to denote totally different things (near Eq. 3). It's super-confusing.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
High order feature transforms are used to lift features to a high dimensional space to simplify the correlation interpretation. However, this is a computational expensive process. This paper proposes a proxy feature transform(PMT) which transforms the high dimensional feature into an embedding of much smaller dimension while maintaining the feature correlation. As an application, this transform is applied to shape assembly problem in 3D using a coarse-to-fine registration strategy. Experiments show a significant improvement in the performance from existing methods.

### Strengths
Strengths:
the paper is well-formalised. It proves the existence of a smaller space orthonormal embedding in the theorem 1, which preserves the convolution of high dimensional features. This can be seen as the PCA for dimension reduction.
The ablation study justifies the various components of the algorithm and the orthonormality condition.
Experimental evaluation seems adequate and clearly indicates the strength of the algorithm.

### Weaknesses
No major weakness.

Few comments
Paper is too compact. More details are required in the proof of theorem 1.
MLP and HDC in table 4 are never mentioned before.
The  transform is learnt on high amount of data. How does it perform with unseen data?

### Questions
Few comments
Paper is too compact. More details are required in the proof of theorem 1.
MLP and HDC in table 4 are never mentioned before.
The  transform is learnt on high amount of data. How does it perform with unseen data?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Proxy Match Transform (PMT), which is a low-complexity high-order feature transform layer that reduces the computational complexity and memory occupancy. The proposed PMT, combined with a GeoTransformer (CVPR 2022) framework, is used in the task of object assembly, where its effectiveness has been proved by experiments.

### Strengths
1. The proposed PMT, at least from the theoretical analysis, could effectively reduce the computational complexity. I personally consider this design similar to KPConv (ICCV 2019), where they use several anchor points to compute their correlations to spatial points that represent the local geometry. This design is reasonable, intuitive, and valuable.

2. The proposed method achieves the state-of-the-art in the benchmark for object assembly, although it is only a synthetic one and there lacks experiments on real data.

3. The Theoretical analysis in the Appendix provides a better understanding of the advantages of the proposed module, which I really appreciate, although it is overly complex to understand throughly.

### Weaknesses
1. The whole pipeline is developed upon GeoTransformer (CVPR 2022) and uses a majority of the previous design. The differences are the use of PMT to replace the Self- and Cross-Attention mechanisms in the coare level, as well as the use of PMT after each stage in decoder. I think this weakens the contribution and novelty of this paper. The core architecture heavily relies on the existing GeoTransformer framework, with the primary modification being the substitution of attention mechanisms with the proposed PMT module. This incremental change, while potentially beneficial, does not represent a substantial departure from the existing state-of-the-art, thus limiting the overall novelty. The paper needs to clearly articulate the specific novel aspects of the PMT module that go beyond a simple replacement of attention layers.

2. The methodology part is overly complex, and I do not this it is organized well and easy to follow. 

    2.1 For example, in Eq. (2) and the following equations, the calculation of attention matrix $\mathbf{A}$ is unclear; The description of how the attention matrix $\mathbf{A}$ is computed is insufficient. The paper does not clearly specify the exact mechanism used to derive the attention scores, making it difficult to understand the core of the PMT module. The lack of clarity in this fundamental aspect hinders the reproducibility and understanding of the proposed method. It is necessary to provide a detailed explanation of the attention calculation, including the specific operations and parameters involved.

    2.2 Moreover, it is also misleading that the proposed PMT is used to replace the attention mechanisms used in GeoTransformer, while in Fig.1 it is compared to the convolutions. And also in many other places concolutions are introduced, but all the computation of PMT seems like attention-based; The paper presents a confusing narrative by comparing PMT to convolutions in Figure 1 while describing it as a replacement for attention mechanisms. This inconsistency creates ambiguity about the true nature of the PMT module. The paper needs to clarify whether PMT is intended to be a form of attention or a novel type of convolution, and provide a consistent explanation throughout the manuscript. The current presentation makes it difficult to understand the underlying computation of PMT.

    2.3 In Eq. (2), it seems the output of PMT is the enhaced features, while in Eq. (4), the output is some correlation scores. Do I make a mistake in understanding this? The distinction between the outputs of PMT in equations (2) and (4) is unclear. It appears that equation (2) produces enhanced features, while equation (4) yields correlation scores. This inconsistency raises questions about the actual function of the PMT module and how these different outputs are used within the overall framework. The paper needs to clearly define the purpose of each output and how they contribute to the matching process. The current explanation is confusing and requires further clarification.

3. The experiments are only conducted on synthetic dataset, which makes me doubt its value in real applications. Therefore, it is better to include some real data. If there is no real data in this task, as this method is strongly based on GeoTransformer, simply running on GeoTransformer's benchmark also makes sense. The lack of experiments on real-world datasets significantly limits the practical relevance of the proposed method. The paper needs to demonstrate the performance of PMT on real data to validate its effectiveness in practical scenarios. The current reliance on synthetic data raises concerns about the generalizability of the method. If real-world data for object assembly is not available, the paper should at least evaluate the method on the benchmarks used by GeoTransformer to provide a more comprehensive evaluation.

4. As this paper mainly focuses on cutting the memory burden and reducing the complexity. Except for the theoretical analysis, it is also necessary to conduct experiments in terms of the memory occupancy and the running speed, to make comparisons to the state-of-the-art. The paper lacks empirical evidence to support the claims of reduced memory occupancy and computational complexity. While the theoretical analysis is appreciated, it is crucial to provide experimental results that demonstrate the actual memory usage and running speed of PMT compared to other state-of-the-art methods. Without these comparisons, the practical benefits of the proposed method remain unproven.

### Questions
See weaknesses for the questions. I strongly suggest the authors to re-organize their methodology part and simplify their symbols. Fig. 1 does not help understand the main contributions. Also the real-data experiments as well as the comparisons in terms of memory occupancy and running speed are highly encouraged.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
