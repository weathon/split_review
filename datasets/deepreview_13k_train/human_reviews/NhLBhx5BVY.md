# Instance Segmentation with Supervoxel Based Topological Loss Function

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Reconstructing the intricate local morphology of neurons as well as their long-range projecting axons can address many connectivity related questions in neuroscience. While whole-brain imaging at single neuron resolution has recently become available with advances in light microscopy, segmenting multiple entangled neuronal arbors remains a challenging instance segmentation problem. Split and merge mistakes in automated tracings of neuronal branches can produce qualitatively different results and represent a bottleneck of reconstruction pipelines. Here, by extending the notion of simple points from digital topology to connected sets of voxels (i.e. supervoxels), we develop a topology-aware neural network based segmentation method with minimal overhead. We demonstrate the merit of our approach on a newly established public dataset that contains 3-d images of the mouse brain where multiple fluorescing neurons are visible as well as the DRIVE 2-d retinal fundus images benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Traditional segmentation methods focus on total voxel accuracy. While some critical voxel errors might change the topology, most would not. This paper proposes a method to find those critical voxels and add additional penalty terms to the loss function whenever these voxels are inaccurately predicted.

The contributions of this paper are as follows:
1. An algorithm is proposed to detect split and merge errors which disrupt the number of components relative to the ground truth.
2. The computational complexity of this algorithm scales linearly with the number of voxels under the assumption of a tree graph.
3. This approach can be easily integrated into available segmentation frameworks as it is built on top of common voxel-based loss functions.
4. The experiments conducted show the effectiveness of the proposal relative to competing methods on two datasets.

### Strengths
In addition to the contributions listed above I would highlight the following:

1. The authors provide a good mathematical notation to communicate their methodology.
2. The didactic images facilitate a better understanding of the approach.
3. Details of training are explicitly mentioned such as the continuation scheme.

### Weaknesses
1. The paper could improve in terms of clarity in several cases. Most importantly, Algorithm 2--a critical part of the paper--is very vague and the only explanation provided about it under Corollary 3 does little to make it clearer. The algorithm's reliance on multiple nested conditional statements without a clear high-level explanation makes it difficult to grasp the core logic. Specifically, the conditions under which the algorithm iterates and how it determines critical components are not sufficiently explained, making it hard to understand the practical implementation.
2. More emphasis needs to be placed that the O(n) guarantee is only valid if critical components affect both local and global topology, i.e. having a tree graph. The current presentation does not adequately highlight the restrictive nature of this assumption. The linear complexity claim is only valid under the assumption that the graph is a tree, and this should be stated as part of the theorem itself, not just in the surrounding text. The implications of this assumption for real-world data, which often deviates from perfect tree structures, should be discussed.
3. The method is only sensitive to the number of components, while topology is much broader e.g. bifurcations, loops. This limitation needs to be communicated. The current method focuses solely on detecting split and merge errors, which are related to the number of connected components. However, topological errors can also include changes in genus, such as the creation or destruction of loops or handles. The paper should explicitly acknowledge that the proposed method is not sensitive to these types of topological changes.
4. The approach comes with hyper-parameters which might be time consuming to set. The paper does not provide sufficient guidance on how to set the hyper-parameters, and the impact of these parameters on the overall performance is not thoroughly discussed. The lack of a systematic approach to hyperparameter tuning could limit the practical applicability of the method.

### Questions
1. The loss function is introduced in Definition 1, and then expanded again in Section 3.3. A better sense of direction would have been conveyed if the two were mixed and mentioned early on in Section 3 and stated that the rest of the Section focuses on finding N(y^) and P(y^) in Definition 4. Removing G(.) and H(.) and having double sums might improve readablility.

2. The definition originally provided for S(.) does not have a subscript and is clear, but the explanation provided for the case with a subscript is hard to grasp.

3. In Method Section before Definition 1, it is stated that y_i \in {0,1,...,m} and y^_i \in {0,1,...,l}. Shouldn't they both sets be the same (no need for l)? Also m, l(?), and n are given without definitions.

4. Positively critical components rely on computing S(y^⊖y^+), while Algorithm 2 only requries knowing S(y⊖y^-). Why?

5. Condition 1 and Condition 2 are not really defined as such.

6. Potential typos: Section 3.1.2 line 2: false negative mask -> false positive mask; Two lines above Corollary 1: lemma seems extra.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a "supervoxel based topological loss function" to solve the connectivity-related problems in segmentation tasks. The paper considered the key components of false positives and false negatives as key factors affecting the topology and uses loss functions to optimize them. Through algorithm design, the time complexity is reduced. The theoretical proof is rich, and the effectiveness of the model is verified on EXASPIM2 and DRIVE. The visualization effect shows that the loss function proposed in this paper can effectively improve the visualization effect.

### Strengths
1. The paper proposed novel ideas and methods that are simple and effective after being optimized by the proposed algorithm in this article.
2. The paper verified the effectiveness of the method in both 3D and 2D dimensions.

### Weaknesses
1. Lack of visual comparison with baseline in Figure 5.
2. Performance metrics should be described using formulas.
3. Lack of comparison with more loss functions that can supervise topology changes.

### Questions
Critical components should not include areas that do not affect the topology structure. In the visualization effect of Figure 4, why is the structure more slender compared to the baseline, and can the proposed loss function optimize the segmentation edge?

What are the values of α and β in the experiment?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors work on binary as well as instance segmentation of curvilinear structures. This segmentation task is prone to errors such as split and merge mistakes. The authors resolve such errors by extending the topological concept of simple points to superpixels (or supervoxels). While most topological-based methods are computationally expensive, the authors propose an algorithm to reduce the complexity of their method. The authors validate their method on 2 datasets and compare against several topology-aware baselines.

### Strengths
1) The authors extend the concept of simple points to supervoxels. In the false negative and false positive maps, they check if keeping or removing the connected component (CC) changes the topology or not. If it changes the topology, then they deem it critical and apply high weight to it in the loss function while training. The critical CCs correspond to the split/merge errors that one would like to resolve.
2) The authors develop an $O(n)$ solution where $n$ is the number of pixels/voxels using standard graph algorithms like BFS. This is much cheaper compared to existing topology-aware methods whose algorithms are atleast $O(n \log n)$ or $O(n^2)$.
3) The authors provide adequate proofs of their runtime in the supplementary.

### Weaknesses
1) In principle, the novelty of the contribution seems limited as an existing concept of simple points has been extended to superpixels (collection of pixels) instead. The core idea of extending simple points to superpixels, while seemingly straightforward, lacks a significant leap in conceptual innovation. The method essentially applies a known topological concept to a different granularity of image representation without introducing a fundamentally new theoretical framework or addressing a previously unconsidered challenge in topology-aware segmentation.
2) The authors should consider comparing against clDice [1] as a baseline since clDice has shown better performances among the topology-aware methods. The absence of a comparison against clDice, a state-of-the-art topology-preserving loss function, is a notable oversight. The authors should demonstrate how their method performs against clDice, especially given its reported superior performance in tubular structure segmentation. Without this comparison, it is difficult to assess the relative effectiveness of the proposed approach.
3) The authors do not provide any ablation study. Considering they have hyperparameters $\alpha$ and $\beta$ in their loss function, the authors would benefit from providing an ablation study of these loss weights and provide a discussion on how each hyperparameter affects the results. The lack of an ablation study for the hyperparameters $\alpha$ and $\beta$ is a significant weakness. The authors should systematically evaluate the impact of varying these parameters on the segmentation performance and provide insights into their sensitivity. This analysis is crucial for understanding the robustness and generalizability of the method.

### Questions
1) Please also see the weakness above.
2) As the authors claim that they are proposing a topology-aware neural network, they should also evaluate the result on topology-aware metrics like clDice [1], Betti Matching [2], and Betti Number [3].
3) Please mention if the numbers in bold are just numerically better, or, if t-test [4] has been conducted to check if the performance improvement is statistically significant or not.

**References**

[1] Shit, Suprosanna, et al. "clDice-a novel topology-preserving loss function for tubular structure segmentation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

[2] Stucki, Nico, et al. "Topologically faithful image segmentation via induced matching of persistence barcodes." International Conference on Machine Learning. PMLR, 2023

[3] Hu, Xiaoling, et al. "Topology-preserving deep image segmentation." Advances in neural information processing systems 32 (2019).

[4] Student, 1908. The probable error of a mean. Biometrika, pp.1–25.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
