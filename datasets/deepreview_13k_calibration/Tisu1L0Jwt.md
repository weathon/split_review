# State Space Model Meets Transformer: A New Paradigm for 3D Object Detection

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
DETR-based methods, which use multi-layer transformer decoders to refine object queries iteratively, have shown promising performance in 3D indoor object detection. However, the scene point features in the transformer decoder remain fixed, leading to minimal contributions from later decoder layers, thereby limiting performance improvement. Recently, State Space Models (SSM) have shown efficient context modeling ability with linear complexity through iterative interactions between system states and inputs. Inspired by SSMs, we propose a new 3D object DEtection paradigm with an interactive STate space model (DEST). In the interactive SSM, we design a novel state-dependent SSM parameterization method that enables system states to effectively serve as queries in 3D indoor detection tasks. In addition, we introduce four key designs tailored to the characteristics of point cloud and SSM: The serialization and bidirectional scanning strategies enable bidirectional feature interaction among scene points within the SSM. The inter-state attention mechanism models the relationships between state points, while the gated feed-forward network enhances inter-channel correlations. To the best of our knowledge, this is the first method to model queries as system states and scene points as system inputs, which can simultaneously update scene point features and query features with linear complexity. Extensive experiments on two challenging datasets demonstrate the effectiveness of our DEST-based method. Our method improves the GroupFree baseline in terms of $\text{AP}_{50}$ on ScanNet V2 (+5.3) and SUN RGB-D (+3.2) datasets. Based on the VDETR baseline, Our method sets a new state-of-the-art on the ScanNetV2 and SUN RGB-D datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel approach to 3D object detection, particularly for indoor environments, by integrating State Space Models (SSMs) with Transformer architectures. The key contributions of the paper are:

1. **Introduction of DEST (State Space Model-based 3D Object Detection)**: The paper proposes a new paradigm called DEST, which addresses the limitations of fixed scene point features during the query refinement process in existing methods. This is the first method to model queries as system states within an SSM framework.

2. **Design of an Interactive State Space Model (ISSM)**: The authors develop an ISSM that effectively functions as queries in complex 3D indoor detection tasks. The ISSM-based decoder is tailored to the characteristics of 3D point clouds, fully harnessing the potential of the ISSM for 3D object detection.

3. **Enhanced Performance**: Extensive experimental results demonstrate that the proposed SSM-based 3D object detection method consistently enhances the performance of baseline detectors on two challenging indoor datasets, ScanNet V2 and SUN RGB-D. Comprehensive ablation studies validate the effectiveness of each designed component.

4. **ISSM-based Decoder**: The paper introduces an ISSM-based decoder that replaces the transformer decoder in DETR-based methods, addressing the performance limitations caused by fixed scene point features. This decoder simultaneously updates both scene point and query point features.

5. **Comparison with State-of-the-Art Methods**: The DEST-based detector significantly outperforms previous 3D object detection methods on the ScanNet V2 and SUN RGB-D datasets, demonstrating substantial performance improvements.

Overall, the paper introduces a new state-space model-based approach to 3D object detection that overcomes the limitations of existing methods, particularly in handling complex indoor environments, and achieves state-of-the-art performance.

### Strengths
1. Writing: The writing is clear and effectively conveys the content of the paper, making it easy to understand.

2. Innovative SSM Integration: The paper creatively combines State Space Models with transformers, offering a unique approach to 3D object detection that reduces complexity while enhancing performance.

3. Performance Improvement: The model achieves substantial performance gains on benchmarks, specifically outperforming existing models on AP metrics for key datasets (ScanNet V2 and SUN RGB-D).

4. Detailed Experimentation: Extensive experiments, including ablation studies, provide strong evidence for the model’s effectiveness and validate each component’s contribution.

### Weaknesses
1. According to Table 5, the proposed method results in a noticeable increase in latency.
2. What is the motivation for introducing SSM in this paper? Why is SSM suitable for 3D detection tasks? I believe this is a critical point that requires detailed explanation from the authors.

### Questions
Please refer to section Weaknesses.

### Soundness
2

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
3

### Summary
The paper address an issue that the ﬁxed scene point features lead to suboptimal reﬁnement of query points in the later layers of transformer and then introduce a novel DEST-based method for 3D indoor object detection. The key design is ISSM, which models query points as system states and scene points as system inputs, allowing simultaneous updates with linear complexity. Experiments in ScanNetv2 and SUN RGB-D show its effectiveness.

### Strengths
1.	Meaningful topic：The paper starts from this problem that scene point features in the transformer decoder remain ﬁxed, leading to minimal contributions from later decoder layers, thereby limiting performance improvement for DETR-based methods.
2.	Convincing experiments: The paper tries its method on different baseline and datasets to verify its effectiveness. Ablation studies are also comprehensive.
3.	Creative design of method: The paper designs a novel state-dependent SSM parameterization method that enables system states to effectively serve as queries in 3D indoor detection tasks.

### Weaknesses
1.	For VDETR, improvement is not big enough.

### Questions
1.	Are there other methods to solve “fixed scene point” from previous works? 
2.	Is is helpful to simultaneously update both scene point and query point features for most model, or just for DEST?
3.	State Space Models (SSM) has an efﬁcient context modeling ability with linear complexity through iterative interactions between system states and inputs. Is it possible to combine SSM and Transformers in 3D object detection?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors observe that the performance of DETR-based 3D object detection methods increases slowly in the last few Transformer decoder blocks. Based on the observation, this paper introduces state space models into 3D object detection and proposes an interactive state space model to update both 3D scene features and queries. Specifically, the authors design a state-dependent SSM parameterization to make each query interact with its respective scene features. Besides, the authors propose four key designs in an SSM-based decoder (*i.e.*, Hilbert-based serialization, inter-state attention, IBS module, and gated FFN). Experimental results show that the proposed method can be combined with multiple 3D detectors and further improve the detection accuracy on both Scannet V2 and SUN RGB-D datasets.

### Strengths
- The authors observe that the performance improves slowly in the last few blocks in the DETR-based 3D detector which is interesting.
- Experimental results show that the proposed methods can be combined with multiple DETR-based detectors and achieve SOTA performance.

### Weaknesses
 - Questions about the proposed method
  - The first question is about computational complexity, in the proposed **Extension of $\Delta$**, the authors expand $\Delta$ $K$ times which will largely increase the computational complexity. The author should provide some results about the computational cost such as FLOPs. Specifically, the expansion of $\Delta$ involves a learnable linear transformation, which, while not directly impacting the core SSM processing, does introduce additional parameters and computations that should be quantified. The authors need to clarify the exact operations involved in this extension and their computational implications, particularly in terms of memory access and potential bottlenecks.
  - Secondly, the design of **Spatial Correlation** Module, especially the relative offsets is similar to the 3D Vertex Relative Position Encoding used in VDETR. The authors should clarify the differences in how these relative offsets are utilized. While VDETR uses them to inject positional information into the attention map, the current paper uses them for generating SSM parameters. The authors need to elaborate on the specific advantages of using relative offsets in this manner, especially in the context of state space models, and why this approach is superior to directly incorporating positional information into the state representation.
  - Further, the ISSM-based decoder stacks lots of elements with few explanations. the authors should explain the importance of each component in the method section. Besides, more illustrations should be provided, for example, the structure of the inter-state attention module. Designs such as Hilbert serialization have been used in Point Transformer v3. The bidirectional scanning mechanism is also common in vision Mamba. The authors need to explain their rationale to avoid being mistaken for a simple stacking of modules. The novelty of combining these components needs to be justified, and the specific benefits of each component within the proposed architecture should be clearly articulated. The authors should provide ablation studies to demonstrate the contribution of each component to the overall performance.

- Questions about the experiments
  - In table 5, do the results in Param. represent the total parameters or the added parameters when using DEST?

### Questions
Lots of typos should be modified.
- Line 28, imporoves -> improves
- line 107, perpormance -> performance

Also, in line 84, 0.64 -> 6.4 according to figure 1.

The authors should carefully examine the article.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Based on the motivation that sharing same scene representations in different decoder layers limits the overall performance of DETR-based 3D detectors, the paper proposes a mamba-based decoder architecture for indoor 3D detection. To fit the mamba design to 3D detection, the paper treats queries as states and scene representations as inputs. Experiments show that the proposed method improves existing baseline models.

### Strengths
1. The idea of updating scene features and query point features simultaneously is well-motivated.

2. With sufficient and extensive evaluations and ablations, the authors validate that DEST surpasses previous baseline methods with reasonable computational cost.

### Weaknesses
1. As mentioned by the authors in line 87 - 89, it is possible to "update the scene feature throughout the decoder layers with transformers". Compared to the input point cloud, processing the encoded points (1024/4096 for GroupFree3D/V-DETR) with quadratic time complexity is somewhat acceptable. It is also possible to implement the attention layers with modern flash-attention approaches [R1] for efficiency. The authors are encouraged to present numerical comparisons to support the choice for SSMs.

2. Missing citations. The Hilbert-based point cloud serialization strategy is closely related to PTv3[R2]. The authors are encouraged to state the relation to [R2].

### Questions
1. As shown in Fig. 4 (a), the difference between the proposed method mainly replaces the cross-attention layers in the standard transformer decoder architecture with the proposed ISSM blocks. Is it possible to also replace the inter-state attention module with bi-directional mamba?

### Soundness
4

### Presentation
3

### Contribution
3
