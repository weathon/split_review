# Exploring contextual modeling with linear complexity for point cloud segmentation

- Decision: Reject
- Avg Score: 6.20
- Scores: 8, 5, 6, 6, 6

## Abstract
Point cloud segmentation is an important topic in 3D understanding. Traditionally, this task has been tackled using either the CNN or Transformer. Recently, a newcomer, Mamba, has emerged as a promising alternative, offering efficient long-range contextual modeling capabilities without the quadratic complexity associated with the Transformer’s attention mechanisms. However, despite Mamba’s potential, early efforts have \textit{all failed} to achieve better performance than the best CNN-based and Transformer-based methods. Since each of these diverse architectures possesses unique strengths and weaknesses, it's difficult to determine the most suitable approach for this task. In this work, we address this challenge by identifying the key components of an effective and efficient point cloud segmentation architecture. Specifically, we show that: 1) \textit{Spatial locality} and \textit{robust contextual understanding} are critical for strong performance, and 2) Mamba features linear computational complexity, offering superior data and inference efficiency compared to Transformers, while still being capable of delivering strong contextual understanding. Additionally, we further enhance the standard Mamba specifically for point cloud segmentation by identifying its two key shortcomings. First, the enforced causality in the original Mamba is unsuitable for processing point clouds that have no such dependencies. Second, its unidirectional scanning strategy imposes a directional bias, hampering its ability to capture the full context of unordered point clouds in a single pass. To address these issues, we carefully remove the causal convolutions and introduce a novel \textit{Strided Bidirectional SSM} to enhance the model’s capability to capture spatial relationships. Our efforts culminate in the development of a novel architecture named \textsc{\methodname}, which effectively integrates the strengths of CNN and Mamba. \textsc{\methodname} surpasses the previous state-of-the-art method, PTv3, by up to \textbf{+0.8} mIoU on key benchmark datasets, including ScanNet, ScanNet200, S3DIS, and nuScenes, while being \textbf{42.1\%} faster and \textbf{5.53$\times$} more memory efficient. Our code and data will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focuses on a simple yet practical target in 3D understanding: how to enhance the accuracy of a Mamba-based framework while preserving its efficiency rooted in linear complexity. The paper seeks to achieve this through an in-depth analysis of the components that contribute to the strong performance of PTv3, summarized as contextual understanding and spatial locality. These findings lead to the two major design elements of this work: Causal-free Mamba and Bidirectional Strided SSM. Overall, it is encouraging to see the method achieve solid performance on major scene-level point cloud semantic segmentation benchmarks.

### Strengths
1. **[Analysis-driven Methodology]** First of all, I appreciate the paper's analysis-driven approach: rather than being experiment-driven, it presents insights based on previous work and derives its methodology from this understanding. This makes the paper easier to follow and the proposed method more convincing.

2. **[Strong performance]** The paper achieves strong performance on several major point cloud semantic segmentation benchmarks and appears to be efficient as well.

### Weaknesses
The insightful analysis, convincing approach, and solid performance demonstrate that this manuscript makes **a valuable empirical contribution**. However, the following weaknesses **limit its broader impact**:

1. **[Scaling up]**  
**(a)** Many observations and analyses (such as the ablation on PTv3 window size) are based on training from scratch on ScanNet (1,500 samples), which is relatively small in scale. However, many model properties may change significantly when scaled up with more data. For instance, using the PTv3 window size ablation as an example, attention mechanisms are inherently adaptive to kernel size, meaning accuracy should not be negatively impacted by the window size. The degradation observed when increasing the window size beyond 1024 is likely due to insufficient data to support this adaptive capacity. Specifically, the model might be overfitting to the limited training data when using larger window sizes, preventing it from generalizing well. This effect could be mitigated with larger datasets or regularization techniques.
**(b)** It is good to see the Mamba framework achieve both higher accuracy and efficiency compared to previous SOTA. However, the true value of superior scratch accuracy and efficiency lies in its capacity for further scaling. I am particularly curious about the model's accuracy and efficiency when scaling up training through multi-dataset joint training, as well as its performance when scaling up parameters with larger data volumes. The paper should explore the model's behavior when trained on a combination of datasets like ScanNet, S3DIS, and Semantic3D, which would provide a more robust evaluation of its generalization capabilities. Furthermore, the impact of increasing model parameters (e.g., number of layers, hidden dimensions) on both performance and efficiency should be investigated to demonstrate its scalability.

2. **[Go beyond semantic segmentation]**
Why do point cloud perception and representation learning prioritize semantic segmentation? This is because it is the simplest way to evaluate the quality of learned representations using a single linear layer. However, this does not mean that research on point cloud backbones should be limited to semantic segmentation alone. The claims of the paper would be stronger if more downstream tasks, such as instance segmentation and object detection, were included. It may not be necessary to achieve the highest performance; instead, demonstrating more properties of the proposed method could be more informative. For example, the paper could evaluate the quality of the learned features by using them for object detection tasks, even if the detection performance is not state-of-the-art. This would provide a more comprehensive understanding of the representation's utility.

### Questions
1. In Figure 1(b), PTv3 consumes even more memory compared to PTv2, which seems unusual since window-based attention should be significantly more memory-efficient than neighborhood attention. The only reason I can imagine is that FlashAttention may be disabled while using a large kernel, resulting in larger matrix multiplications. Could you provide a more detailed explanation of this setup?

2. Maybe a shorter, more impactful title could make it easier for readers to remember? The current version is too lengthy.

3. Maybe the table arrangement could be improved? I don’t recommend using resizebox, as it can lead to uneven text sizes. You might consider referring to the LaTeX source code from the PTv3 paper for tips on adjusting table formatting.

4. It might be better to reduce the use of bold text? For instance, consider changing `\textbf{Proposed Solution:}` to` \textit{Proposed solution:}`, and avoid bolding certain numbers in the main text.

(Minor suggestions for reference only)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the 3D point cloud segmentation task. It first compares the performance of three types of blocks: CNN, Transformer, and Mamba, and then improves the existing Mamba architecture. The authors provide extensive visualization results and ablation experiments.

### Strengths
[S1] It is meaningful to compare the performance of the three types of blocks—CNN, Transformer, and Mamba—on the same task, point cloud segmentation.
[S2] The paper is detailed and easy to read.
[S3] The paper conducts detailed ablation experiments on the newly proposed module.
[S4] The paper achieves state-of-the-art results on multiple datasets.

### Weaknesses
[W1] The comparison of CNN, Transformer, and Mamba blocks lacks strong evidence. I believe that concluding "CNN is more effective for local modeling and Transformer is better at handling contextual information" based on just one example for each is insufficient. The analysis is limited to a single instance per block type, failing to account for variations in hyperparameter settings, network depth, or architectural nuances that could significantly impact performance. A more rigorous comparison would involve a systematic exploration across a range of configurations and datasets to validate these claims.
[W2] The proposed method is more like a small fix to Mamba-based method. 
[W3] The two solutions proposed in this paper: 1) the casual-free block is described in very little detail and lacks a clear explanation; 2) bidirectional SSM seems to have already been introduced in VisionMamba (Zhu 2024), and this paper's work only adds n-stride.

### Questions
[Q1] Could the authors provide more detailed explanations of W1, such as whether there is theoretical evidence to support it or if there are sufficiently extensive experiments across multiple datasets?
[Q2] Is the Bidirectional SSM mentioned by the authors consistent with VisionMamba (Zhu 2024)? I do not see a bidirectional structure in Fig(6b), only the Strided SSM.
[Q2.5] If the answer of Q2 is yes, the result you reported in the second line of Tab(7d) shows that this structure can only bring 0.1% increasement, which seems inconsistent with the effects reported in VisionMamba (Zhu 2024) regarding this structure. From an efficiency perspective, is the introduction of the indirection necessary if it only brings a 0.1% improvement?
[Q3] The casual-free conv block is not clearly explained. If this is something new you are proposing, it would be helpful to include a more detailed explanation or illustration.
[Q4] Standardize the notation for SSM. In the abstract and introduction, it is referred to as "Strided Bidirectional SSM," while later it is called "Bidirectional Strided SSM."
[Q5] There’s something wrong of your hyperlink in 3.3. It should be Fig 5 but yours is Fig 4.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel architecture named MEEPO, designed for point cloud segmentation with a focus on efficient contextual modeling. It introduces Mamba, a state-space model (SSM) that achieves linear complexity compared to traditional Transformers, which have quadratic complexity. The authors identify Mamba's limitations, such as enforced causality and directional bias, and propose solutions through causal-free convolutions and bidirectional strided state-space modeling. MEEPO outperforms previous models, like PTv3, in accuracy, latency, and memory efficiency across several benchmark datasets (e.g., ScanNet, S3DIS, nuScenes).

### Strengths
1.	MEEPO introduces a new method by integrating CNN and Mamba components, achieving good contextual modeling with reduced computational costs.
2.	The paper thoroughly explores the limitations of existing architectures (CNN, Transformer, and SSM) and provides comprehensive ablations and comparisons to validate its design choices.
3.	The introduction of causal-free convolutions and bidirectional strided SSM in Mamba addresses some original limitations in Mamba for this task,.

### Weaknesses
1.	In Section 4.2, the authors claim that they propose a 'Bidirectional Strided SSM' method, however, Bidirectional SSMs have already been proposed in works like [1][2] to address the issue of forgetting unidirectional sequences. I believe that not referencing these articles while claiming authorship is not rigorous. Additionally, what baffles me is that in Table 7, a comparison is made for strides ranging from 2 to 16, showing a decreasing trend in performance. So, why not similarly compare and discuss the results for a stride of 1? The lack of this comparison makes it difficult to fully assess the impact of the striding mechanism, and whether it is truly beneficial compared to a non-strided bidirectional approach.
2.	The manuscript presents in Fig. 4 the mIoU performance of the Transformer-based PTv3 under different range windows. The advantage of the Mamba model lies in its better memory capabilities for long sequences. The authors emphasize this advantage in line 240, but they do not provide specific data to demonstrate the validation of this conclusion in point cloud data  (the author can show a similar format figure as Fig.4). Without a direct comparison of Mamba's performance with varying input lengths, the claim about its superior handling of long sequences remains unsubstantiated. It is crucial to see how Mamba's performance scales with increasing point cloud size, similar to the analysis done for PTv3.
3.	Table 7 in the article indicates that the parameter volume of CNN+Mamba is smaller than that of pure Mamba. However, based on the author's description, compared to pure Mamba, the author has added a CNN module to Mamba and employed a bidirectional mechanism for computation. Why the parameter count is lower than pure Mamba needs further clarification from the author. The explanation should address the specific architectural choices that lead to this counter-intuitive result, such as the channel sizes and kernel sizes used in the CNN and Mamba components, and how these choices affect the overall parameter count.
4.	In line 251, the referred figure is not Fig.4, it should be Fig. 5.

### Questions
please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes several popular neural network architectures, including CNN-based and Transformer-based designs, as well as the recently introduced Mamba model. It proposes a new point cloud segmentation architecture, MEEPO, which combines the strengths of CNNs and Mamba, surpassing previous state-of-the-art methods like PTv3 on multiple key benchmark datasets.

### Strengths
1. The model is highly efficient and achieves accuracy that exceeds prior state-of-the-art methods.
2. The design of the Strided Bidirectional SSM effectively enhances the model's understanding of spatial relationships.

### Weaknesses
1. The proposed hyper-structure is based on the analysis of existing architectures, which makes the technical innovation somewhat limited.


### Questions
I am unsure whether the authors of this paper are aware of *Point Cobra*. I would like the authors to address the numerous similarities between the two papers and provide an explanation.

1. While the new model structure aligns with the previous version (NIPS2024), there are differences in latency and memory usage. I am interested in understanding the source of these improvements.

2. This paper introduces an additional CNN module to capture the local features of the point cloud. Could the Causal-Free Conv1D in the Mamba block be removed, given that these two modules appear to serve the same role in the model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Point cloud segmentation is crucial for 3D understanding, traditionally tackled using CNNs or Transformers. Recently, Mamba has emerged as an efficient solution for contextual modeling, though it has struggled to outperform leading CNN and Transformer methods. This work identifies key requirements for effective segmentation: strong spatial locality and robust contextual understanding. Enhancing Mamba, the authors remove causality and introduce a Strided Bidirectional SSM to address directional biases in unordered point clouds. The resulting architecture, MEEPO, merges the strengths of CNNs and Mamba, achieving up to +0.8 mIoU over state-of-the-art methods on benchmarks like ScanNet and nuScenes, with notable gains in speed and memory efficiency.

### Strengths
1. The paper is well-structured with a clear analysis-driven approach.
2. The experimental results are impressive.

### Weaknesses
1. In lines 238-241, it's unclear why Mamba is considered effective for local processing, given its design goal of modeling long sequences with linear complexity. The reference to a "locally-biased forget gate" needs further explanation and detailed analysis or statistical data beyond visualization. It's not immediately obvious how the forget gate, which controls information flow over time, inherently promotes local processing in the context of point clouds, where the notion of 'time' is not explicitly present. A more rigorous justification, perhaps involving analysis of the gate's behavior with respect to spatial proximity of points, is needed.

2. In lines 300-302, the statement that long-range attention is unnecessary may only partially reflect the issue. The core reason might be the sparsity of 3D point clouds. Transformers generally require extensive data and prolonged training to surpass CNNs, so it might be more accurate to say that insufficient data limits the full potential of Transformers rather than implying long-range attention is irrelevant. The argument that long-range attention is not needed should be supported by more concrete evidence, such as experiments with varying amounts of training data or different transformer architectures that are more suitable for sparse data. Simply stating that it is unnecessary without such evidence is not convincing.

3. The innovations appear somewhat limited, with minimal structural changes. The modifications, such as Causal-Free Mamba and Bidirectional Strided SSM, feel more like tricks. While these modifications show performance gains, the fundamental architecture remains largely unchanged. A more in-depth exploration of alternative architectural designs or a more substantial modification to the core Mamba mechanism would be more impactful. The current modifications, while effective, lack a certain level of novelty from an architectural perspective.

4. Presenting results on downstream perception tasks like segmentation and detection would add further value. While segmentation results are provided, demonstrating the method's effectiveness on other tasks, such as object detection, would strengthen the paper's claims of general applicability. This would also provide a more comprehensive evaluation of the proposed method's capabilities.

### Questions
see above weakness

### Soundness
2

### Presentation
3

### Contribution
2
