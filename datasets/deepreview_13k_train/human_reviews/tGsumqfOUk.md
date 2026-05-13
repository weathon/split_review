# Learning Parameter Sharing with Tensor Decompositions and Sparsity

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Large neural networks achieve remarkable performance, but their size hinders deployment on resource-constrained devices. While various compression techniques exist, parameter sharing remains relatively unexplored. This paper introduces \gls{fips}, a novel algorithm that leverages the relationship between parameter sharing, tensor decomposition, and sparsity to efficiently compress large vision transformer models.  \Gls{fips} employs a shared base and sparse factors to represent shared neurons across multi-layer perception (MLP) modules. Shared parameterization is initialized via Singular Value Decomposition (SVD) and optimized by minimizing block-wise reconstruction error. Experiments demonstrate that \gls{fips} compresses DeiT-B and Swin-L MLPs to 25--40\%  of their original parameter count while maintaining accuracy within 1 percentage point of the original models.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces SParS (Sparsity-enabled Parameter Sharing) to efficiently compress large vision transformer models through parameter sharing, tensor decomposition, and sparsity. SParS employs a shared base and sparse factors to represent shared neurons in multi-layer perceptrons (MLPs). Experimental results demonstrate that SParS can compress MLPs of DeiT-B and Swin-L to 25%-40% of their original parameter count while maintaining less than 1% accuracy loss.

### Strengths
1. This paper is well organized and is easy to follow.

2. By decomposing the MLP params into sharing basis and sparse projection matrix, SparS shows the ability to achieve high compression rates with acceptable accuracy losses.

3. Experimental results show that SparS could outperform other vision transformer compression methods with similar compression rates.

### Weaknesses
1. This paper seems to be incremental in technical contributions. The method of sharing basis matrix is similar to HydraLoRA [4] in principle.

2. The differences and innovations of the proposed SparS compared to existing data compression methods [3,4] are not addressed.

3. This paper only shows compression rate and performance on the DeiT-B and Swin-L. Evaluations on models like Swin-B or ViT-L[1,2] are  missing. This limits the potential generalization ability of this paper.

4. Experiments on the language model as in the baseline [5] are missing.

5. Yu and Wu (2023) mentioned that the activation rather than weight matrix is of low rank. I recommend to further clarify this problem considering that they focus on tensor decomposition on the weight matrix.

### Questions
Is the redundancy and interplay among different blocks mentioned in the article limited to MLP? Will the attention layer also have the same phenomenon?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors provided a simple parameter-sharing method to compress the current models, which is easy to understand. The method can be divided into two parts: 1) use a Shared Initialization to decompose the weights of MLP layers to unified U matrics and individual V matrics, realizing a low-rank reconstruction; 2) use a Local Error Minimization with a small calibrated dataset to fine-tune the new models, maintaining the original performance.

### Strengths
1. The method is straightforward to understand.

2. The content is very rich, including analysis, figures, an algorithm, and experiments.

3. The analysis of Section 2 reveals the motivations of the method, which is interesting.

### Weaknesses
However, some aspects obstruct understanding.

Writing:
* The layout is not easy to read and appears chaotic, especially in Section 3.

* The summary of the contributions is too casual and the high-level meanings of the modules are not well mentioned.

* Some Figures are hard to understand without reading the text in different parts, lacking sufficient explanation in the caption.

* Please check some typos, including repetitive abbreviations (FC, Lines 103 and 107) and main reference (Line 583).

Method:

*  The parameter sharing is only conducted in the MLP layers. Could the linear layers of QKV also use parameter sharing?

* Did the local error minimization constrain the performance of the new compressed models?

* Although simplicity is good, the method is too simple without sufficient verification.

Experiments:

* The method mentioned focuses on large neural networks that DeiT-B and Swin-L could be recognized as large when compared to modern large models, such as LLM.

* Although this method focuses on parameter sharing, comparing it with other optimization methods, such as Distillation, and NAS, is helpful for better understanding this method.

* Apart from the Param budget, what is the computational budget or inference time for Table 1 and Table 2?

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Sparsity enabled Parameter Sharing (SParS) to compress large vision transformer models, which is an algorithm based on existing algorithms such as parameter sharing, tensor decomposition, and sparsity.

### Strengths
None noted.

### Weaknesses
There are several major concerns for this work.

1. Lack of novelty. All the components of SParS are existing and well-known algorithms, such as low=rank decomposition for FC layers, sparse training and pruning g (Hoefler et al., 2021,Zhu & Gupta, 2017, Evci et al., 2021). As a result, SParS is a straightforward combination of such existing algorithms which clearly lack novelty.

2. Unjustified formulation. The low-rank decomposition described in lines 219-224 is not justified. Why all the individual weights share the same $U$ and the same singular values $\Sigma$ with different $V$? What is the approximation error of such heuristic? Empirical or theoretical studies are expected to explain such low-rank decomposition on the concatenation of the weights.

3. Limited experiments. The SParS is only evaluated for DeiT-B (with 12 blocks) and Swin-L, while there is a large family of vision transformers including various versions of Swin, ViT, etc and it is not clear how SParS performs on a broad range of these vision transformers. Moreover, image classification results along cannot justify the effectiveness of the propose method, and more experiments in segmentation/detection on standard benchmarks are expected.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Sparsity-enabled Parameter Sharing (SParS), a compression algorithm for neural network parameters. This method typically focuses on compressing MLP layers in vision transformers by using shared base and sparse factors across multiple layers. Authors provide visualization and analysis on stages of the algorithm and ablate different ways of truncating MLP parameters. The authors demonstrate that their approach can compress DeiT-B and Swin-L MLPs to 25-40% of their original size while maintaining accuracy within 1% of the original models. Experiments also show that SParS (+FT) outperforms baseline methods like GFM.

### Strengths
- **Novel approach**: In general, the method is new and it's a smart application of sparsity on modern neural networks
- **Clear presentation**: Authors present the motivation, methodology, experiments and analysis clearly. 
- **Empirical justification**: Authors use solid experiments to justify their choice of the design, i.e. on truncation strategy, number of grouped layers.
- **Strong results**: 25-40% parameter saving is in general a decent number in model compression related works.

### Weaknesses
 - **Limited comparison**: in the main results section, authors provide few comparison with other related parameter saving methods. The limited comparative analysis makes it difficult to fully assess the method's effectiveness relative to the current state-of-the-art approaches. Specifically, the paper lacks a comparison against methods that employ structured sparsity or low-rank approximations, which are common techniques for model compression. The absence of these comparisons makes it difficult to determine if SParS offers a significant advantage over existing techniques or if it simply achieves similar performance with a different approach.
- **Insufficient theoretical analysis**: while the empirical results are promising, the paper lacks sufficient theoretical analysis to explain why SParS outperforms baseline methods. A more detailed discussion of the underlying mechanisms and intuitive explanations would enhance the reader's understanding and make the technical contributions more accessible. For instance, the paper does not delve into the mathematical properties of the shared base and sparse factors, nor does it explain why this specific combination leads to effective compression. A theoretical analysis should also explore the conditions under which SParS is expected to perform well, and when it might fail.
- **Narrow application scope**: this work mainly focuses on vision transformers, whereas parameter-efficient methods are particularly crucial for large language models. The authors should consider extending their analysis to language models or discuss potential challenges and modifications needed for such applications. The current scope limits the impact of the work, as the techniques may not be directly applicable to other domains where model compression is highly needed.

### Questions
**Question**:
- Yu et al., 2023 explore weight-sharing in attention layers and find that it saves parameters in trade of small performance drop. I'm wondering if you can extend your methods to attention layer parameters. If not, what's the reason?
- Same as the weaknesses section. Why didn't you provide comparison with methods like MiniViT(Zhang et al., 2022)?


**Reference**:

Yu, Yaodong, Sam Buchanan, Druv Pai, Tianzhe Chu, Ziyang Wu, Shengbang Tong, Benjamin Haeffele, and Yi Ma. "White-box transformers via sparse rate reduction." Advances in Neural Information Processing Systems 36 (2023): 9422-9457.

Zhang, J., Peng, H., Wu, K., Liu, M., Xiao, B., Fu, J. and Yuan, L., 2022. Minivit: Compressing vision transformers with weight multiplexing. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 12145-12154).

### Soundness
3

### Presentation
3

### Contribution
3
