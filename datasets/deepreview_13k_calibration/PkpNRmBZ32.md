# Let SSMs be ConvNets: State-space Modeling with Optimal Tensor Contractions

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
We introduce Centaurus, a class of networks composed of generalized state-space model (SSM) blocks, where the SSM operations can be treated as tensor contractions during training. The optimal order of tensor contractions can then be systematically determined for every SSM block to maximize training efficiency. This allows more flexibility in designing SSM blocks beyond the depthwise-separable configuration commonly implemented. The new design choices will take inspiration from classical convolutional blocks including group convolutions, full convolutions, and bottleneck blocks. We architect the Centaurus network with a mixture of these blocks, to balance between network size and performance, as well as memory and computational efficiency during both training and inference. We show that this heterogeneous network design outperforms its homogeneous counterparts in raw audio processing tasks including keyword spotting, speech denoising, and automatic speech recognition (ASR). For ASR, Centaurus is the first network with competitive performance that can be made fully state-space based, without using any nonlinear recurrence (LSTMs), explicit convolutions (CNNs), or (surrogate) attention mechanism.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a series of hybrid state-space models (SSMs), inspired by the design of convnets. It achieves this by generalizing 1D kernels to 2D and designing the depthwise, group, and full convolution counterparts for SSMs. Experiments on several sequence modeling tasks validate the effectiveness of the proposed method.

### Strengths
1. The concept of generalized SSM blocks, configurable with flexible connectivity structures, demonstrates good soundness and could complement existing SSM designs.

2. The proposed method is supported by both theoretical analysis and empirical experiments.

### Weaknesses
1. The major concern is that the real-device training/inference efficiency of the proposed generalized SSM blocks is not provided. It is unclear whether the flexibility of these building blocks comes at the cost of reduced real-device efficiency. Specifically, the paper lacks a detailed analysis of memory bandwidth requirements and computational throughput, which are crucial for practical deployment. The authors should provide a breakdown of the operations involved in their generalized SSM blocks and how these operations map onto hardware resources, such as GPU cores or specialized accelerators. Without this analysis, it is difficult to assess the practical viability of the proposed method.

2. Another major concern is that the position of the proposed method among the latest SOTA SSMs is unclear. For example, Mamba has introduced input adaptivity in their selective state design and employed an advanced macro-structure with gating mechanisms and FFNs to enhance channel mixing in addition to token mixing. These advancements also address the limited expressiveness of vanilla SSMs, which are mostly depthwise-separable. The authors are expected to demonstrate whether the proposed method is a better choice or is orthogonal and can be combined with these advanced designs. The paper should include a more thorough comparison with these state-of-the-art methods, including a discussion of the trade-offs between model complexity, computational cost, and performance.

3. The proposed method is evaluated on small-scale sequence modeling tasks. It would be highly desirable for it to be evaluated on language modeling and commonsense reasoning tasks. These tasks are more complex and require models to capture long-range dependencies, which would provide a more rigorous test of the proposed method's capabilities. The current evaluation is insufficient to demonstrate the general applicability of the proposed method.

4. The writing clarity could be improved by better explaining certain terms. For example, the concept of "depthwise-separable" in the context of SSMs is important to the logic of this paper and should be better clarified. A more detailed explanation of how depthwise-separability is implemented in the proposed SSM blocks, and how it differs from full SSM operations, is needed. The paper should also discuss the implications of this design choice on model expressiveness and computational efficiency.

### Questions
My concerns are listed in the weaknesses section. 

I have one additional question: For the generalized SSM blocks with group/full convolution patterns, can I understand that these blocks integrate both token-mixing and channel-mixing within a single block, making other channel-mixing blocks, such as FFNs, unnecessary?

### Soundness
3

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
3

### Summary
The authors present an approach to augment the number of features in the inputs, outputs and internal states of LTI systems, leveraging state space models, in order to facilitate architectural flexibility towards building abstractions that vary feature dimensions in neural models, such as those in CNNs. The authors present connections between tensor networks, which generalize low-rank decompositions in a way that can be applied to SSM einsums.

The authors introduce a weighting for basis kernels which can be adapted to a recurrent system. Convolutions, in this way, are shown as sums of various real and complex combinations of Fourier modes. The authors use this idea to present Centaurus, a configuration of tensor networks that allows retains SSM blocks but projects internal state to different sizes, making it possible to mimic various CNN abstractions such as depthwise, grouped, and bottleneck convolutions.

The authors construct each of these layers and present implementation details, i.e. a tradeoff between optimization of einsum expressions (for which we have few compiler tools at the moment) versus GPU kernel customization.
 The authors present experiments on three tasks within sequence modeling/speech: keyword spotting, raw speech denoising, and speech transcription, showing strong results in each area with small models with good computational scaling properties.

### Strengths
- The presentation of methodology is convincing and strongly tied to first principle sin SSMs.
- The application of tensor networks to solve the problem of projecting kernel matrices to and from frequency spaces of different dimensions is novel and elegant.
- The presentation of implementation and computational considerations shows care was given to scaling tradeoffs, i.e. memory-boundedness of this regime of compute regime, opportunities (or lack thereof) for operator fusion, and operation/contraction ordering per kernel construction.
- Results are compelling — in particular, efficiency of the proposed models is impressive given performance.
- Attention to detail with the model name is nice.

### Weaknesses
 - Baselines could be much stronger, in that there are no other SSM model baselines. Ablations are mostly within the architectural innovations present with Centaurus.
- The constraint that some projection matrices from basis kernels must be real constrains the expressiveness of the model, although it’s likely that such generalizations in future work might enable this.
- A more comprehensive architectural ablation would make the paper stronger.  While there are explanations of architectures in appendix E, there is no study or comparison of components to CNNs. Do architectural ideas useful in building CNNs apply to building Centaurus models?

### Questions
- The authors should cite other work in speech that explores other convolutional architectures, such as ([Kirman et al.](https://ieeexplore.ieee.org/iel7/9040208/9052899/09053889.pdf), time-depthwise separable convolutions, [Hannun et al.](https://arxiv.org/pdf/1904.02619), or other extensive architectural ablations based on computational efficiency for training and inference: [Pratap et al.](https://arxiv.org/pdf/2001.0972))
- ASR baselines can examine other convolutional architectures such as those presented in [Synnaeve et al.](https://arxiv.org/pdf/1911.08460); these baselines are slightly better comparisons given that they are also end-to-end and also present results language-model based decoding.
- Experiments in Appendix E leverage samples from Libri-Vox — was they Libri-Light or samples of raw data?
- A brief discussion of future work/applications to other domains (outside of speech) for CNNs (such as computer vision tasks) might strengthen the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present Centaurus, an adaption of state-space models (SSMs) / linear RNNs (lRNNs) to audio modeling / processing, where they embed these layers of different dimenionalities into a deeper hybrid architecture, where they take inspiration from classical CNN networks that use different strides, kernel sizes and feature dimensions at different levels in the network. Their ablations show that the hybrid composition is superior to homogenous depth-wise, bottleneck and point-wise bottleneck architectures, and their models show strong performance while being superiorly FLOP-efficient compared to the current SOTA. Theoretically, they connect their hybrid architecture adaptions to tensor networks combined with Fourier operations and show the optimal tensor contraction strategy for their network.

### Strengths
Their hybrid architecture shows better results at lower FLOPs, while retaining a similar scaling behaviour compared to other homogeneous models across model sizes.

### Weaknesses
The proposed model is a combination of known primitives (SSMs and inhomogeneous scaling from CNN architectures).
The work does not cite and compare to other relevant, related work that potentially outperforms the trained models on the given datasets, e.g. Zhao et al. 2022: "Monaural speech enhancement with complex convolutional block attention module and joint time frequency losses." for the VB-DMD dataset.

The choice of baselines in Table 1 is not fully justified. The table implies that Centaurus beats all baselines in performance, while having lower computational demands and parameters. However, stronger baselines likely exist, albeit with larger computational demands, and these are not discussed or compared against in detail.

### Questions
Since both RNNs and State Space models are well-known, a detailed introduction of these architectures can be omitted, except for the parallelization / transformations to/from the Fourier domain.
Einsum notation is definitely superior for Tensor expressions, so also here the extensive introduction could be reduced.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an efficient deep state-space model, Centaurus. Inspired by traditional ConvNets, the authors explore a heterogeneous design using block variants similar to convolutional blocks. The model is framed through the perspective of Tensor Networks and optimized by ordering tensor contractions for efficiency. Experiments demonstrate that the model achieves competitive performance across multiple tasks, including keyword spotting, raw speech denoising, and ASR.

### Strengths
- The authors proposed a novel perspective by viewing state-space models (SSMs) as tensor networks, enabling efficiency optimizations through contraction order analysis. This tensor network approach is advantageous for visualization, allowing the authors to address efficiency as a congestion optimization problem on the base graph. The approaches demonstrated in the paper contributes a valuable exploration into efficient SSM models.
    - One of the optimizations involves applying FFT to transform the SSM into the frequency domain, allowing the optimal contraction order to be analyzed for improved efficiency. While FFT introduces a slight computational cost, which is not compute-bound, is minimal compared to the efficiency gains achieved through optimized contraction order.
    - The authors explore multiple variants of SSM operations and illustrate them in a figure, broadening the possibilities for combining heterogeneous blocks to enhance model performance. Earlier SSM models only used identical operations throughout.
    - The authors converted SSM into Frequency domain by FFT, which allows the optimization of determining the optimal “contraction order”. The paper also discussed the approach to evaluate the memory and computational requirements of an einsum contraction path involving FFT.
    - As an example, the author explained how they find the optimal contraction order of Bottleneck SSM Operation. The proof involved Lemma 1 that reveals the intermediate tensors have at most 3 dims, which restricted the potential optimization paths. This largely reduced the manual work of comparing different contraction orders.

- The proposed method demonstrates competitive performance with significantly enhanced efficiency. For keyword spotting, the model achieved the best accuracy with 100x fewer FLOPs. In raw speech denoising, the authors conducted an ablation study on different SSM variants and concluded that the hybrid Centaurus model achieved the highest PESQ score with the smallest parameter count and the fastest FLOPs/sec. For ASR, the model also showed competitive performance.

### Weaknesses
The paper includes a large amount of appendix material, likely due to page limitations. While the authors present key results in the main paper, leaving detailed proofs in the appendix, it would be beneficial to adjust the structure to highlight more of the original contributions and slightly condense other sections, such as the background. Although the background on SSM and einsum notation is important and well-explained, it occupies two full pages. For instance, a potential improvement could be briefly summarizing the proof of Lemma 1 and explaining how it restricts feasible patterns in the main paper. As it is an important detail of explaining how you explore the optimal order. It would reduce the need for readers to frequently switch between the appendix and the main text.

The expression of the depthwise SSM operation in Section 4.1, Figure 1, differs slightly from the expression in Section 4.2 (above Equation 9), particularly in the subindex. The expression in Section 4.2 includes a subindex “b” that is not present in the earlier section. Could you clarify the difference and explain the meaning of “b”? If it refers to the bit representation in quantization, it would be helpful to explicitly cover this detail in the paper.

The authors provided an example of the most complex case—the bottleneck block—but skipped examples of other operations. Are there any general theories or principles that could be further distilled from these examples?

### Questions
- The expression of the depthwise SSM operation in Section 4.1, Figure 1, differs slightly from the expression in Section 4.2 (above Equation 9), particularly in the subindex. The expression in Section 4.2 includes a subindex “b” that is not present in the earlier section. Could you clarify the difference and explain the meaning of “b”? If it refers to the bit representation in quantization, it would be helpful to explicitly cover this detail in the paper.

- The authors provided an example of the most complex case—the bottleneck block—but skipped examples of other operations. Are there any general theories or principles that could be further distilled from these examples?

### Soundness
4

### Presentation
3

### Contribution
3
