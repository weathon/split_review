# Selective State-Space Modeling of Correlation Maps for Semantic Correspondence

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Establishing semantic correspondences between images is a fundamental yet challenging task in computer vision. Traditional feature-metric methods enhance visual features but may miss complex inter-image relationships, while recent correlation-metric approaches attempt to model these relationships but are hindered by high computational costs due to processing 4D correlation maps. We introduce MambaMatcher, a novel method that overcomes these limitations by efficiently modeling high-dimensional correlations using selective state-space models (SSMs), treating multi-level correlation scores as states. By implementing a similarity-aware selective scan mechanism adapted from Mamba’s linear-complexity algorithm, MambaMatcher refines the 4D correlation tensor effectively without compromising feature map resolution or receptive field. Experiments on standard semantic correspondence benchmarks demonstrate that MambaMatcher achieves state-of-the-art performance without relying on large input images or computationally expensive diffusion-based feature extractors, effectively capturing rich inter-image correlations while maintaining computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes MambaMatcher, a Mamba-based approach to establish semantic correspondences. MambaMatcher attempts to model inter-image correlations by treating multi-level correlation scores at each position in the correlation map as a state in a state-space model. Specifically, the multi-level features obtained by the frozen extractor are first enhanced through feature aggregation. The enhanced features are used to construct a multi-level correlation map. Then, the correlation map is refined with the proposed similarity-aware selective scan mechanism. Experimental results demonstrate that MambaMatcher achieves a good balance between accuracy and efficiency in establishing semantic correspondences.

### Strengths
1. Mamba is a potential architecture to balance the accuracy and efficiency of establishing semantic correspondences. It is meaningful to explore how to apply the Mamba structure in this task.
2. The organization and presentation of this paper are clear.

### Weaknesses
 **1. The core design of MambaMatcher, i.e., treating the correlation scores at each position in the correlation map as a state in a state-space model, seems to provide only a minor benefit.**

According to the results in Table 4 and Table 5, the combination of a DINOv2 feature extractor, a 2D-Conv_{k=5} feature aggregation and the existing correlation aggregation processes (based on 4D-Conv or FastFormer) provide a similar accuracy compared with the proposed MambaMatcher. This phenomenon indicates that the selection of feature extractors and the design of single-image feature aggregation may be more significant problems in establishing semantic correspondences. Replacing the existing 4D-Conv or FastFormer with the Mamba structure in the correlation aggregation process just gives a small improvement. Such a performance decreases the significance of the motivation and the core design in this paper.

**2. Some claims in this paper are not discussed clearly.**

2.1. In Line 48, the authors claim that one problem of the existing correlation-metric approaches is that they “severely limit the feature map resolution”. However, the proposed MambaMatcher only processes the 30x30 feature map. Could we consider the 30x30 size as a large resolution? Maybe more experiments are required to validate MambaMatcher’s superiority in handling larger feature maps.

2.2. In Line 69, the authors claim that “MambaMatcher seamlessly integrates feature-metric and correlation-metric approaches into a unified pipeline.” It indicates that some parts of MambaMatcher are feature-metric-based while some are correlation-metric-based. However, there is no discussion to clarify such a claim.

**3. The introduction of the proposed “similarity-aware selective scan mechanism” is not clear enough.**

The first reason of this problem is that Figure 2 is not cited in the main text. Besides, some equations may make the process of “similarity-aware selective scan mechanism” clearer.

### Questions
Please provide more discussions and experimental results to address the above weaknesses.

-------------After the Discussion Period---------------

Thank the authors for the clear and detailed responses to my questions. As mentioned in the strengths I concluded, I consider this work as a meaningful exploration. I also agree with the authors that MambaMatcher can complement some existing components. However, my concern in W1 is mainly about the significance of this work, which is not addressed well in the rebuttal. According to the responses, the core Mamba-based module provides only modest improvements compared with some other parts like feature extractors and single-image feature aggregations. These results indicate that the significance of this work is relatively small. Considering both such strengths and weaknesses, I prefer to maintain my initial score. Thanks.

Moreover, I can understand the responses for W2.1. However, in my opinion, the statements about “high resolution” in the manuscript are confusing because the authors did not clarify that the resolution is discussed for the 4D correlation map rather than the original 2D feature map.

### Soundness
3

### Presentation
4

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
The paper introduces MambaMatcher for high-dimensional correlation modeling using selective state-space models, uniquely treating multi-level correlation scores as states to capture inter-image correlations. A key feature is the similarity-aware selective scan mechanism, enabling efficient, high-resolution correlation extraction. MambaMatcher combines feature-metric and correlation-metric approaches in a unified pipeline without compromising feature map resolution or receptive field. Extensive experiments show state-of-the-art performance on semantic correspondence benchmarks, outperforming diffusion-based methods with lower computational cost, making MambaMatcher an effective and efficient solution.

### Strengths
1. The paper is well-written and easy to understand.
2. The paper presents extensive experiments, demonstrating state-of-the-art performance on benchmark datasets.
3. The paper provides a thorough comparison of different feature aggregation and correlation aggregation structures, offering valuable insights into how these configurations affect model performance.

### Weaknesses
1. The motivation is unclear. While the authors claim that their method addresses the challenge of capturing inter-image correlations, they do not clearly define what constitutes an inter-image correlation problem or why it is important. A more detailed motivation and definition would help clarify the significance of this aspect for the reader. Specifically, the paper lacks a clear explanation of why feature-metric methods alone are insufficient for semantic correspondence tasks, and how explicitly modeling inter-image relationships overcomes this limitation. The paper should elaborate on the specific ambiguities that arise when matching features across images, such as repeated patterns or homogeneous regions, and why these ambiguities are not adequately addressed by intra-image feature analysis.
2. The novelty of the approach appears limited, as the correlation structure used in this method closely resembles that of CAT++, raising concerns about its originality. The paper needs to more clearly articulate the differences in how the correlation maps are processed and utilized, beyond simply stating that they are not concatenated with projected features. A detailed comparison of the computational steps and the specific operations performed on the correlation maps in both methods would be beneficial. The paper should also clarify how the proposed method's approach to modeling correlations as 'states' in a state-space model differs conceptually and practically from existing methods that also use correlation maps.
3. The visualizations in Figure 5 and Figure 3 are not easy to understand and could benefit from clearer explanations. For Figure 3, the purpose of showing the pre- and post-aggregation correlation maps is not immediately clear, and the paper should explicitly state what each stage represents and how it contributes to the final prediction. For Figure 5, the meaning of the red and green points is not clearly defined, and the paper should provide a legend or explanation that clarifies the visualization of correct and incorrect predictions.

### Questions
1. Time and Space complexity should be analyzed for the proposed algorithms, and also the key psuedo-code should be presented in this paper.
2. In the context of the paper, could you clarify what is meant by 'inter-image relationships'? Specifically, how does this differ from identifying semantic similarities across local pixels within an image, and why is it particularly challenging for feature-metric methods to capture these relationships?
3. The results in Table 1 have inconsistent resolutions, making it necessary to compare them at the same resolution to fully demonstrate the effectiveness of the proposed method.
4. Figure 5 is somewhat difficult to interpret, as it’s unclear what the red and green points represent. Providing a clearer legend or explanation for these colors would enhance the reader’s understanding of the figure’s purpose and improve overall clarity.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
MambaMatcher combines efficient high-dimensional correlation modeling with a selective scan mechanism, achieving superior performance on semantic correspondence benchmarks with lower computational costs.

While traditional feature-metric methods often fail to capture complex relationships between images, newer correlation-metric approaches address this but are hindered by the high computational cost of processing 4D correlation maps. MambaMatcher overcomes these issues by modeling high-dimensional correlations efficiently through selective state-space models (SSMs). Using a similarity-aware selective scan mechanism inspired by Mamba’s linear-complexity algorithm, MambaMatcher refines the 4D correlation tensor without compromising feature map resolution or receptive field. Experiments on standard semantic correspondence benchmarks demonstrate that MambaMatcher achieves state-of-the-art performance, capturing rich inter-image correlations while avoiding large input images and costly diffusion-based features.

### Strengths
1. Efficient Modeling of High-Dimensional Correlations: By using selective state-space models (SSMs), MambaMatcher models complex inter-image relationships effectively while avoiding the high computational cost typically associated with 4D correlation maps.

2. Novel Similarity-Aware Selective Scan Mechanism: The paper introduces a unique scan mechanism inspired by Mamba’s linear-complexity algorithm. This mechanism refines the 4D correlation tensor accurately, enabling high-resolution processing of inter-image correlations.

### Weaknesses
1. The content in Sec 4.2 MULTI-LEVEL CORRELATION COMPUTATION AND AGGREGATION is somewhat ambiguous. The overall process flow should be: Shape the correlation map from 4D to 1D -> order -> reorder -> reshape  the correlation map  from 1D to 4D. Is the sorting performed along the $H \times W \times H \times W$ dimension or along the $2L$ dimension? If it is along the $H \times W \times H \times W$ dimension, is the sorting directly based on similarity in descending order? How are the potential spatial relationships between correlation elements encoded?

2. Similarity-aware Selective Scanning: Mamba relies on its inherent order to capture the relative positional relationships between sequence tokens. When  correlation elements are sorted by similarity before scanning, does this mean  no longer need to consider the spatial locations of these elements?

3. Parameters of Feature Aggregation: Line 215 states that "The feature aggregators share the same weights across all levels to maintain efficiency." However, Lines 320-322 describe the feature aggregation layer as consisting of two layers of 2D convolution with a kernel size of 5, with output channel dimensions of 64 and 14, respectively, and a ReLU activation function in between. This implies that feature aggregation includes four 2D convolutional layers and two ReLU activations. However, in Table 6, feature aggregation is reported to have 42.5M parameters, which appears inconsistent. Please provide a more detailed explanation.

### Questions
1. Ambiguity in Feature and Correlation Aggregations. Section 4.1 introduces Multi-level Feature Aggregation using a lightweight 2D convolution network, while Section 4.2 proposes MULTI-LEVEL CORRELATION COMPUTATION AND AGGREGATION using Mamba. Both aggregation modules require training, but throughout the text, the authors often refer to “the aggregation” without specifying which aggregation they mean. This lack of clarity can easily lead to confusion, as in Lines 251-352: “We freeze the visual feature extractor during training to focus on learning the aggregation layers.” Here, does “the aggregation layers” refer to the feature aggregation in Section 4.1, the correlation aggregation in Section 4.2, or both?

2.Effects of selective scan order. Table 5 indicates that the relative order of correlation elements significantly impacts performance, with ascending order notably reducing effectiveness compared to descending order. This may be because, in causal inference, later tokens pass information to all preceding tokens. Placing high-similarity tokens at the beginning can help reduce interference from other correlation elements. The paper briefly claims that "Early processing of strong matches helps resolve ambiguities in these regions," in Sec. 4.2, but a more in-depth analysis is needed.

### Soundness
3

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
5

### Summary
This paper proposes a new method called MambaMatcher, which applies selective state space models (SSMs) to semantic matching tasks and combines Mamba's linear complexity algorithm to efficiently process 4D correlation tensors. Compared with existing methods, MambaMatcher has improved the accuracy of keypoint localization without sacrificing computational efficiency, demonstrating significant performance improvements.

### Strengths
1. This paper introduces the first use of selective state-space models (SSMs) to efficiently model high-dimensional inter-image correlations.
2. This paper proposes a similarity-aware selective scan mechanism improves accuracy and efficiency in refining high-resolution correlations.
3. MambaMatcher integrates feature-metric and correlation-metric methods, achieving state-of-the-art performance with lower computational costs.

### Weaknesses
1. The specific description of the Correlation Aggregation via Similarity aware Selective Scan section is not clear enough. 
2. There are some grammar errors in the paper ( e.g., Fig.4 Ground-truth correspondence and page 3, line 132).
3. Some formulas have commas or periods after them, while others do not. There is no uniformity in format ( e.g., Eq.10 and Eq.11).

### Questions
1. How does MambaMatcher balance the integration of feature-metric and correlation-metric methods? 
2. Are there scenarios where this integration could present limitations or potential drawbacks?
3. Is there a significant difference in performance when processing images with different levels of complexity or size?

### Soundness
3

### Presentation
2

### Contribution
3
