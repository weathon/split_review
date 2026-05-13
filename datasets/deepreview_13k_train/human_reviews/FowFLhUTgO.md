# V2M: Visual 2-Dimensional Mamba for Image Representation Learning

- Decision: Reject
- Scores: 6, 8, 3, 5

## Abstract
Mamba has garnered widespread attention due to its flexible design and efficient hardware performance to process 1D sequences based on the state space model (SSM).
Recent studies have attempted to apply Mamba to the visual domain by flattening 2D images into patches and then regarding them as a 1D sequence.
To compensate for the 2D structure information loss (e.g., local similarity) of the original image, most existing methods focus on designing different orders to sequentially process the tokens, which could only alleviate this issue to some extent. 
In this paper, we propose a Visual 2-Dimensional Mamba (V2M) model as a complete solution, which directly processes image tokens in the 2D space.
We first generalize SSM to the 2-dimensional space which generates the next state considering two adjacent states on both dimensions (e.g., columns and rows).
We then construct our V2M based on the 2-dimensional SSM formulation and incorporate Mamba to achieve hardware-efficient parallel processing.
The proposed V2M effectively incorporates the 2D locality prior yet inherits the efficiency and input-dependent scalability of Mamba.
Extensive experimental results on ImageNet classification and downstream visual tasks including object detection and instance segmentation on COCO and semantic segmentation on ADE20K demonstrate the effectiveness of our V2M compared with other visual backbones.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a 2D state-space model (SSM) for visual representation learning, named V2M. Unlike previous Mamba-based visual representation methods that perform 1D sequence learning, V2M operates in 2D space, with each hidden state conditioned on its top and left tokens. Baron et al. have presented a 2D SSM but neglect the input-dependent characteristic of SSM, which is crucial for boosting performance.

### Strengths
- Developing high-performance, high-dimensional state-space models is an important topic, and the paper is an interesting attempt in this direction.

- The results in the paper are generally good, demonstrating strong performance on ImageNet classification, COCO detection, and segmentation compared to strong baselines such as ViM, LocalMamba, and VMamba.

### Weaknesses
 - One of the essential advantages of Mamba is its high efficiency in processing long sequences. The paper does not show V2M's performance on long sequences.

- V2M's runtime is not reported. Given that hardware-efficient implementation is an important part of V2M, comparing its runtime with 1D Mamba is crucial.



### Questions
- Writing: Use "Eq.~\eqref{xxx}" for equation references. The background formulation part can be shortened, e.g., Eqs. (1-5), as these have been widely described in previous vision Mamba papers.

- V2M seems better at spatial information modeling compared to ViM. If the positional embedding in V2M is removed, how significant is the performance drop? The performance drop could be minimal, right?

- How is the classification head designed?

- It would be interesting to see the formulation and results of V3M for video modeling.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents Visual 2-Dimensional Mamba (V2M), a novel framework for image representation learning that adapts the state space model (SSM), specifically the Mamba model, to the two-dimensional structure of image data. This paper extends the 1d SSM to a 2d form to fundamentally accommodate the structure of image data. As a non-hierarchical vision mamba method, it achieves better results than its baseline Vim.

### Strengths
- The consideration of 2d spatial relationship in the visual domain is intuitive and sounds reasonable.
- Different from other hierarchical vision mamba methods, this paper handles the visual perception with a plain, non-hierarchical architecture, maintaining the ability in multimodality applications.
- Compared with the baseline method, this paper presents significant improvements in both classification and dense prediction tasks.
- This paper aims at a good question. Scanning strategy with SSM methods is a key problem because the 1d original scanning does not treat all tokens equally.

### Weaknesses
 - The character corners in Figure 1 require further explanation. Specifically, the meaning of the numerical superscripts and subscripts associated with the state variables is unclear. The relationship between these indices and the spatial dimensions of the image needs to be explicitly defined and justified. Without a clear explanation, the reader cannot fully grasp the core mechanism of the proposed 2D SSM.
- Note that function names in formulas are usually typeset properly in Roman font, e.g., `rot`, `concat`, `SSM`, `Linear`, `sum` in Eq. 13~15. This lack of proper typesetting makes the equations harder to read and understand, especially for those not deeply familiar with the notation. Consistency in mathematical notation is crucial for clarity.
- The paper references preprints and arXiv versions of significant works, such as Mamba (COLM), Vision Mamba (ICML), and VMamba (NeurIPS). Citing preprints can be problematic as the final published versions often contain important changes or clarifications. The authors should update these citations to their final published versions to reflect the current state of the literature.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes the Visual 2-Dimensional Mamba (V2M) framework, an innovative model for image representation learning. Unlike traditional Mamba models that process image data in a 1D sequence, V2M adapts a 2D state space model to retain spatial structure, preserving local relationships between pixels. This 2D adaptation allows V2M to process image patches as 2D entities directly, thereby enhancing locality and coherence in visual representation.

### Strengths
This paper innovatively introduces a 2D state space to address the spatial coherence issues faced by SSM models in the visual domain, achieving promising results.

### Weaknesses
1.Novelty

The novelty is moderate, as there has already been substantial research, such as VMamba[1], exploring how sequence models can preserve 2D structural information in visual tasks. While the authors propose a 2D state space, the core idea of multi-directional scanning is not entirely new, and the specific implementation appears to be a variation of existing approaches.

2.Implementation

While this paper introduces a theory of 2D state space to address coherence issues in visual tasks,  its implementation relies on excessive simplification, lacking a detailed explanation of the rationale behind this approach and its potential implications. Specifically, the simplification of the 2D state space equations to leverage 1D SSM hardware optimizations, while practical, lacks a rigorous justification. The paper does not adequately explore the potential trade-offs or limitations introduced by this simplification, particularly regarding the loss of information from the horizontal direction when calculating $h^2_{i,j}$.

3.Performance

The performance demonstrated in this paper shows only minor gains over early baselines like Vim[2] and VMamba[1], without advantages over more recent models like EfficientVMamba[3]. The reported improvements are not substantial enough to justify the increased complexity and computational cost of the proposed method. Furthermore, the comparisons are made against reimplemented baselines, not the original reported results, which raises concerns about the validity of the performance gains.

4.Experiment

It is foreseeable that the proposed method will impact speed and memory usage; however, the paper lacks sufficient efficiency tests, memory usage tests, and ablation studies, resulting in limited experimental support. The absence of detailed analysis on the computational overhead, including FLOPs, throughput, and memory footprint, makes it difficult to assess the practical applicability of the method. The lack of ablation studies also limits the understanding of the contribution of each component of the proposed method.

5.Presentation

The expression of the formulas is somewhat confusing, such as the approach used to split Equation 7 into Equations 9 and 10, and the unclear logical progression from Equation 11 to Equation 12. The notation used in the equations could be improved for clarity, and the logical flow of the mathematical derivations needs to be more explicit.

### Questions
Could you add more efficiency experiments and ablation studies to this paper and provide a more thorough discussion based on those findings? 

Additionally, could you offer a more detailed analysis and explanation of the simplifications mentioned in Section 3.2?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The submission introduces a Visual 2-Dimensional Mamba (V2M) model, aimed at preserving the inherent prior of 2D image data. The V2M model incorporates a 2D State Space Model (SSM) that directly processes image tokens in 2D state space by considering two adjacent states in both dimensions. The authors convert the time-varying 2D SSM into a near-equivalent 1D Mamba format for efficient parallel computation. Experimental results show that V2M outperforms existing visual backbones on ImageNet classification and various downstream tasks.

### Strengths
1. The proposed time-varying 2D SSM is based on Roesser’s state space model, which intuitively depicts the spatial information of the image. 

2. This paper proposes a simplified computational process for Roesser’s state space model, resulting in two consecutive 1D SSM block, thus achieving hardware-efficient parallel processing.

3. The proposed V2M model adopts four scanning directions and compares three types of classification tokens: mean pooling, edge class token and middle class token.

### Weaknesses
1. Although the theoretical analysis of 2D SSM is based on Roesser’s state space model, it is simplified into two 1D SSM processes for parallelism. I am not sure whether this simplification retains the ability of Roesser’s SSM to capture the spatial dependencies within the image. Specifically, the simplification seems to reduce the influence of horizontal dependencies when calculating the vertical component, which could limit the model's ability to fully capture the 2D nature of the image data.

2. The performance improvement is tiny especially in the downstream tasks. It is not sure whether the improvement is brought by the proposed 2D SSM. From the ablation study in Table 4, modeling in four directions seems to offer greater benefits than the 2D SSM itself. Furthermore, the reported performance gains are marginal, and it's unclear if these small improvements justify the increased computational cost. The gains on ImageNet are also quite small, and the downstream task improvements are not compelling enough to demonstrate the effectiveness of the proposed 2D SSM.

3. The FLOP of V2M is much higher than that of baseline models, for example, 1.5G for Vim-T and 1.9G for V2M-T. Specific operating speeds, such as throughput, should be provided. Please gradually add each module to the baseline model, and give the corresponding number of parameters, FLOPs, throughput and performance. The significant increase in FLOPs without a substantial performance boost raises concerns about the practical applicability of the model. The lack of detailed analysis on the computational overhead makes it difficult to assess the trade-off between performance and efficiency.

### Questions
1. The method part (Sec. 3.2) is not clear enough. From equation 11 and 12, it seems that the horizontal component and the vertical component are the same after simplification, which contradicts formula 6. It is better if the authors can give a clearer and comprehensive explanation about the simplified computational process.
2. Please add the ablation study for 2D SSM block itself.

### Soundness
3

### Presentation
3

### Contribution
3
