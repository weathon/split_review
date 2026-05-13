# AMSC: Adaptive Multi-Dimensional Structured Compression with Theoretical Guarantees

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Network pruning is a pivotal strategy for reducing complexity and accelerating inference. Most pruning methods focus on a single dimension (depth or width), leading to insufficient compression when multiple dimensions are redundant. Additionally, separating pruning from training disrupts established network correlations, causing performance degradation. In this paper, we propose a novel Adaptive Multi-dimensional Structured Compression (AMSC) method that simultaneously learns the minimal depth, the minimal width, and network parameters under the strategy that  prioritizes depth compression. Specifically, based on the regularization technique,  AMSC incorporates layer- and filter- specific information into the penalty in order to adaptively identify and  eliminate redundant depth and width in terms of the importance and size of each layer and filter. It  integrates compression and training processes together without pruning. Consequently, the proposed method enables adaptive structure reduction from the initial configuration to a structure necessary that minimizes  the generalization error. Rigorous theoretical evidence is provided in terms of  the consistency of AMSC in achieving minimal network depth and width. To the best of our knowledge, this is the first study that offers a theoretical  guarantees in structure selection. Extensive experiments on CIFAR-10/100 and ImageNet datasets demonstrate our  method not only achieves  state-of-the-art compression performance in terms of FLOPs and total parameters, but also preserves competitive classification accuracy. For example, AMSC enhances the accuracy of ResNet56 on CIFAR-10 from 93.37\% to 93.71\%, while simultaneously reducing calculations by 58.63\% and parameters by 44.71\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel Adaptive Multi-dimensional Structured Compression (AMSC) approach that simultaneously compresses the depth and width of neural networks while maintaining model performance. The method demonstrates a thoughtful balance between architectural efficiency and computational effectiveness. The key innovation is incorporating layer- and filter-specific information into penalty terms to adaptively identify redundant components, where Eq 3 is at the center of the paper, which introduces loss terms during training to compress the model by constraining both its depth and width. Experiments suggest the merits of the method vs other counterparts.

### Strengths
1. The proposed adaptive weighting scheme ($\lambda(l) = \sqrt{q_l}/||\hat\theta_l||_2$) provides a mathematically principled approach to network compression by automatically adjusting compression intensity based on both parameter counts and layer importance, addressing a fundamental limitation in existing methods that use uniform compression.

### Weaknesses
 * The method's strong dependency on hyperparameters $λ_0$ and $λ_1$ (as shown in Figure 2) raises concerns about its practical deployability. The paper does not provide a systematic strategy for determining these crucial hyperparameters across different architectures. Tuning these hyper-params needs domain knowledge in practice, which makes the method hard to use.

* The baseline performance of the proposed AMSC method is consistently lower than competing methods across different architectures (e.g., 92.86% vs. 93.03%-93.72% on ResNet56, 92.63% vs. 93.50%-93.97% on ResNet110). This discrepancy in baseline accuracy makes it challenging to fairly evaluate the actual effectiveness of the pruning method, as the reported accuracy improvements might be partially attributed to the lower starting point rather than the superiority of the proposed approach. A more rigorous comparison would require experiments with standardized baseline models.

* Lack of ablation studies to validate the individual contributions of depth and width regularization. Comparison between "depth-only", "width-only", and the full method would better justify the necessity of combining both regularization. It is suggested to conduct ablation studies comparing "depth-only", "width-only", and the full method across different architectures and datasets. 

* Tab. 2, SSL is a quite old method. I am not sure if the comparison with it can really show any advantage of the method.

* For pruning papers, Resnet50 on ImageNet is a standard benchmark. This comparison is missing. It is recommended to have it.

### Questions
NA

### Soundness
2

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
3

### Summary
This work studies the problem of jointly pruning a neural network along the width (filters in CNNs), and the depth (layers or blocks). The authors propose a multi-dimensional pruning algorithm (AMSC) based on a novel regularization based loss function to identify which elements of the network are to be discarded while training. The elements are then discarded after training. Post pruning, the network is fine-tuned again. The authors suggest novelty of the proposed regulatization term lies in how the authors penalize each filter and layer. The authors provide a theoretical result to show that under certain assumptions, an algorithm like AMSC could potentially obtain optimal width and depth.

### Strengths
S1. The problem setting is quite interesting and important.

S2. Writing was mostly easy to follow

S3. Empirical performance of AMSC is better than the baselines

S4. Under the validity of the assumptions, Theorem 1 is quite interesting.

### Weaknesses
W1. Writing often lacks precision. Please state terminology before using. Citing a few instances below
- Line 182 "$\hat{\theta}_l$ and $\hat{\theta}_{l,j}$ are estimators.." This statement is unclear. Specifically, what are these estimators estimating, and what data are they derived from? The lack of context makes it difficult to understand the subsequent analysis.
- Line 186. "DNNs are highly unidentifiable" - what does this mean? This statement requires a more precise definition. Does it refer to the non-convexity of the loss landscape, or the existence of multiple solutions with similar performance? The authors need to clarify this concept.
- Lines 202 - 213. Writing needs to be improved. Shouldn't $dep$ be a function of $w$ and $wid$ be a function of $l$ since those are constraints? The current description is confusing and lacks clarity on how depth and width are related in the optimization process. It's unclear if these are constraints or optimization variables.
- Line 239: What is pseudo dimension? This term is used without proper definition or context. A brief explanation or citation is needed for readers unfamiliar with this concept.

W2. Arguments for Assumption 4.1 and Contribution 1 are not quite convincing for the following reasons
- For figures 2 and 5, why is it that accuracy is pegged to depth / width of the network? That seems unconvincing. Would this hold for different random initialisations of the network? The relationship between accuracy and network dimensions needs more rigorous justification. The observed trends could be due to specific initializations or training procedures, and the authors need to demonstrate the robustness of this relationship.
- Lines 355 - 357: "In contrast..." This argument isn't convincing to ensure validity of Assumption 4.1. Had that been the case, this would have been a lemma/theorem. Figure 1 should be plot for various values of (depth, width). For instance, Fig. 1a is has a fixed width, I suppose. Can this be plot for various widths? Also, how does this plot vary for different random initializations? The argument for Assumption 4.1 is weak and lacks empirical support. The authors should provide more comprehensive experiments to validate this assumption, including varying both depth and width and using different random initializations.

W3. Please refer to the questions

Typos:
Line 83-84: The sentence "This phenomenon emphasizes..." seems incomplete

Line 218: Demonstrate~s~

Line 224 & 763: $M_b < \infty$?

Table 1: Tayl~a~(o)r

Line 315: shown

### Questions
Q1. Can the authors contrast or position this work to the body of literature in Neural Architecture Search as a part of related works?

Q2. Why do the authors call AMSC a depth-first strategy? There is no indication in algorithm 1 of this.

Q3. How close are the obtained depth and widths upon using AMSC to the optimal depths and widths for each network?

### Soundness
3

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
4

### Summary
This paper proposes an adaptive multi-dimensional structured pruning method to compress DNNs by incorporating the penalty terms related to filters and layers into the loss function. Additionally, the adaptive weights are leveraged to modulate the influence of the penalty for each filter in each individual layer. Experiments on classification tasks and theoretical evidence demonstrate that the proposed method seems to be effective.

### Strengths
1. Code is released.
2. The paper is generally well-written, and the theoretical analysis is comprehensive.
3. The experiments are extensive, with various datasets and models.

### Weaknesses
1. In Table 1, the baselines in this paper are significantly lower than those in previous methods. For example, for ResNet-110, the baselines of other methods are all above 93.5%, while the baseline in this paper is 92.63% (a reduction of >0.87%). The authors should compare the results among different methods under similar baselines. This discrepancy raises concerns about the reliability of the reported improvements, as a lower baseline can artificially inflate the perceived effectiveness of the pruning method. It is crucial to establish a fair comparison by using consistent baseline implementations or clearly justifying any differences.
2. The authors should report the results of VGG-16 on CIFAR-10 and ResNet-50 on ImageNet, as numerous methods conduct experiments on these architectures, such as [1, 2, 3, 4, 5]. Reporting these results would facilitate comparisons with other approaches. The absence of these standard benchmarks makes it difficult to assess the method's performance relative to the broader literature. Specifically, these architectures are widely used in pruning research, and their inclusion would provide a more comprehensive evaluation.
[1] M. Lin, R. Ji, Y. Wang, et al. Hrank: Filter pruning using high-rank feature map. CVPR 2020.
[2] H. Zhang, L. Liu, H. Zhou, et al. Akecp: Adaptive knowledge extraction from feature maps for fast and efficient channel pruning. ACMMM 2021.
[3] H. Wang, C. Qin, Y. Zhang, et al. Neural pruning via growing regularization. ICLR 2021.
[4] G. Fang, X. Ma, M. Song, et al. Depgraph: Towards any structural pruning. CVPR 2023.
[5] L. Liu, S. Zhang, Z. Kuang, et al. Group fisher pruning for practical network compression. ICML 2021.
3. To demonstrate the effectiveness of Equation 4, more experiments should be conducted in Section 5.3.3, including: 
(a) Keep $ \lambda _0 $, $ \lambda _1 $  unchanged, compare the results of proposed method with those obtained when setting $\lambda (l) = 1$, $\lambda (l,j) = 1$. This is important to isolate the impact of the adaptive weighting scheme. Without this comparison, it is unclear whether the performance gains are due to the adaptive weights or simply the overall regularization strength. (b) Compare the results with those obtained using reverse weighting, i.e., when $\frac{{\sqrt {q _ l  } }}{{\lVert {\hat \theta _ l  } \lVert_2 }}$ is larger, the corresponding weight $\lambda (l)$ should be smaller. Similarly, when $ \frac{{\sqrt {q _ {l,j} } }}{{\lVert {\hat \theta _ {l,j} } \lVert_2 }} $ is larger, the corresponding weight $\lambda (l,j)$ should be smaller. This would rigorously test the proposed weighting scheme's design. (c) Analyze the influence of $\lambda (l)$ and $\lambda (l,j)$ on accuracy individually, as well as their influence when investigating $\lambda (l)$ and $\lambda (l,j)$ simultaneously. This analysis is necessary to understand the contribution of each component to the overall performance and to identify potential interactions between them.
4. Do the authors validate the effectiveness of the proposed method on other tasks, such as object detection?

Minor issues:
1. Several symbol errors. For example, $ \lVert {\theta _ l } \lVert \propto \sqrt {q _ l } $ and $\lVert \theta _ {l,j} \lVert \propto \sqrt{q _ {l,j}}$ seem to lack rigor. Also, there is an error in the equation on page 5, Line 209.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2
