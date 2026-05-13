# OSTQuant: Refining Large Language Model Quantization with Orthogonal and Scaling Transformations for Better Distribution Fitting

- Decision: Accept
- Scores: 8, 6, 6, 6, 5

## Abstract
Post-training quantization (PTQ) has emerged as a widely adopted technique for compressing and accelerating Large Language Models (LLMs).
The major challenge in LLM quantization is that uneven and heavy-tailed data distributions can expand the quantization range, thereby reducing bit precision for most values.
Recent methods attempt to eliminate outliers and balance inter-channel differences by employing linear transformations; however, they remain  heuristic and are often overlook optimizing the data distribution across the entire quantization space.
In this paper, we introduce Quantization Space Utilization Rate (QSUR), a novel metric that effectively assesses the quantizability of transformed data by measuring the space utilization of the data in the quantization space. We complement QSUR with mathematical derivations that examine the effects and limitations of various transformations, guiding our development of Orthogonal and Scaling Transformation-based Quantization (OSTQuant). OSTQuant employs a learnable equivalent transformation, consisting of an orthogonal transformation and a scaling transformation, to optimize the distributions of weights and activations across the entire quantization space. Futhermore, we propose the KL-Top loss function, designed to mitigate noise during optimization while retaining richer semantic information within the limited calibration data imposed by PTQ.
OSTQuant outperforms existing work on various LLMs and benchmarks. In the W4-only setting, it retains 99.5\% of the floating-point accuracy. In the more challenging W4A4KV4 configuration, OSTQuant reduces the performance gap by 32\% on the LLaMA-3-8B model compared to state-of-the-art methods. Code will be available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes the OSTQuant approach for LLM post-training quantization (PTQ), which assigns learnable Orthogonal and Scaling Transformations to each fully connected (FC) layer in LLMs. It also introduces the Quantization Space Utilization Rate (QSUR) as a metric to evaluate the quantizability of transformed data. Additionally, the KL-Top loss function is introduced to address the small calibration set issue.

### Strengths
- The proposed QSUR provides a quantitative index to evaluate the effectiveness of the transformations. It motivates the OSTQuant method, and the results demonstrate its high effectiveness.

- The paper achieves significantly improved results for 4-bit activation, weight, and KV cache quantization.

- The paper is mostly well-written. I particularly like Figure 1 which provides a clear illustration of the concepts.

### Weaknesses
 - Since this is a PTQ method, it would be beneficial to demonstrate its effectiveness on larger models, such as a 70B parameter model. Additionally, showing a scaling curve with model size, memory cost, computation cost, and quantization bit would help users understand the overall Pareto frontier between cost and quality.

- Some parts of the paper could be clearer, particularly in detailing certain aspects. For example, while Figure 1 is helpful, it took some time to understand the meaning of the grey dots and ovals.  Similarly, Table 3 lacks details about the inference system and why only prefill speedup is mentioned. Providing more context and explanations would improve the paper’s readability and accessibility.

### Questions
- It would be good to see the speedup results on hardware with FP4 support, like Blackwell architecture, to fully show the potential.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposes a PTQ technique that reportedly achieves SOTA results on LLMs.  
The technique employs an equivalent transformation before quantizer which combines smoothing and rotation in recent work, together with optimization of a top-K KLD loss and a weight-statistics-cognizant initialization of rotation.  
A local heuristic metric QSUR is introduced to assess the efficiency of quantization.  
Experiments and ablation studies were carried out with popular LLMs.

### Strengths
+ Well-motivated idea.
+ Adequate presentation of background and recent related work.
+ Comprehensive experiments.

### Weaknesses
 - Certain ablation studies are still missing that are necessary to establish the contributions from different components of the proposed technique (see below).
- Quality of writing could use further improvement.  For example, there seems to be a mislabeling of $\Lambda$ as $A$ in equations (9) and (10); certain figure legends, such as Fig. 6, are too tiny to read.

### Questions
* One major question I have is on the relative contributions by the 3 new ingredients in the proposed method: the equivalence pair reparameterization, the top-K KL loss, and the initialization.  The authors did conduct ablation study on the special initialization, but there seems to be a lack of ablation on the loss.  In other words, it is not clear how much the differential results in Table 2 comparing against other methods are due to the combination of smoothing and rotation, and due to the top-K KLD loss--what would be the result if one applies SpinQuant but optimizing the top-K KLD?  
* Another major question that I have is the role of QSUR.  The authors provided theoretic results on the effect of linear transformation on this local metric assuming Gaussianity--this is good.  But in practice, QSUR is not an objective function for direct optimization in conducting OSTQuant, but rather, OSTQuant minimizes a global KLD loss.  This begs the question: how do the global loss align with local QSURs?  During the course of OSTQuant optimization, if one measure QSUR across various layers in the network, do they all monotonically grow as the global loss monotonically decreases?

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
4

### Summary
The paper introduces QSUR and proposes OSTQuant that improves quantization performance by globally optimizing multiple equivalent transformation pairs in LLMs with KL-Top loss. Each transformation consists of a scaling transformation and an orthogonal transformation.

### Strengths
This paper mathematically derives a new metric QSUR to quantify the utilization of the quantization space, which is experimentally found to be positively correlated with the accuracy of the quantized model. Based on QSUR, the authors define the optimal transform matrix, which inspires them to combine the scaling and orthogonal transformation to minimize the quantization space. By incorporating scaling transformation and KL-Top loss, OSTQuant achieves SOTA results across various quantization settings while maintaining a low calibration cost.

### Weaknesses
While having mathematically derived the form of an optimal transform matrix, OSTQuant only applies weight outlier minimization initialization to the orthogonal transformation while leaving scaling transformation behind, incurring a small gap between the theoretical analysis and the method. Besides, it would be helpful to show the improvements of applying weight outlier minimization initialization compared with Hadamard matrix. It would also be beneficial to include experiment results on larger models (e.g. 70B) and decoding speedup.

### Questions
1. Can the authors showcase the effect of initializing the transform matrix with the theoretically derived form?

2. The experiment results on larger models such as LLaMA-2-70B and LLaMA-3-70B are missed in the paper, can the authors provide more experiment results on these models?

3. The decoding speedup is also missed in the paper. It would be helpful to include latency analyses on the decoding latency.

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
3

### Summary
This paper presents a mathematical framework to evaluate the effectiveness of smooth and rotation transformations in the context of outlier suppression during LLM quantization. It introduces a metric, QSUR, to assess the efficacy of various transformations and derives a closed-form solution for the optimal transformation. Based on QSUR, the paper proposes OSTQuant, a method that optimizes the combination of smooth and orthogonal transformations globally and employs KL-Top loss to mitigate noise during PTQ optimization.

There are some concerns regarding the methodology and assumptions in the paper. 

(1). Quantization Assumption: The paper assumes the volume of the quantization space $V_{S_{X}}$ as that of a cube when dimension $d=3$, which implies per-tensor quantization. However, the standard practice is to use per-token quantization for activations and per-channel quantization for weights. The volume of per-channel quantization is typically a cuboid when dimension $d = 3$. The authors should clarify if their assumptions are based on these scenarios and how their methodology applies to these more common quantization schemes.

(2). Mean Vector Neglect: In line 231, the paper states," we neglect the mean vector $µ$, so $λ_{max} = λ_{min} = λ$". The causal relationship between neglecting the mean vector and the equality of the maximum and minimum eigenvalues is not evident and requires further explanation.

(3). Optimization of Transformations: The paper optimizes the pair of smooth and orthogonal transformations, with the transformation initialized by the closed-form optimal derivation. It is unclear why it is necessary to further optimize a transformation that is already designed to reach maximum QSUR. Additionally, the paper lacks an ablation study on the impact of different orthogonal initialization methods.

(4). Correlation of QSUR and Model Performance: Figure 3 shows a positive correlation between QSUR and the performance of the quantized model. However, it is not demonstrated whether a higher QSUR value consistently leads to higher performance in quantized models. The paper should provide a more rigorous validation to establish this relationship across various datasets and architectures.

(5). Hadamard Transformation: The paper uses online Hadamard transformation for query and key. It is unclear whether the Hadamard transformation can be optimized as suggested in Figure 5.

### Strengths
The paper provides a mathematical framework that attempts to understand the role of smooth and rotation transformations in quantization, which is a novel approach. The introduction of QSUR offers potential insights into the quantization process, and the closed-form solution for the optimal transformation could serve as a theoretical foundation for further research. The integration of orthogonal and scaling transformations within OSTQuant could address issues related to outliers in activations and weights, which is a significant contribution.

### Weaknesses
A major concern is that, despite deriving a closed-form solution for the optimal transformation based on QSUR, the paper opts to use learnable transformation parameters initialized by the optimal transformation instead of directly applying the theoretically derived optimal transformation. This choice should be justified.

While the paper establishes a positive correlation between QSUR and the performance of the quantized model, it is unclear whether a higher QSUR necessarily indicates a superior transformation. There is a lack of rigorous validation demonstrating that transformations with higher QSUR values consistently lead to better model performance across various datasets and architectures.

The hypervolume $V_{S_{X}}$ of the quantization space $S_{X}$ is calculated using per-tensor quantization, whereas common practice typically involves per-token quantization for activations and per-channel quantization for weights. The authors need to clarify how QSUR applies to these more conventional quantization schemes and validate their metric in these contexts. Without this clarification, the applicability and robustness of QSUR are questionable.

In line 231, the paper states," we neglect the mean vector $µ$, so $λ_{max} = λ_{min} = λ$". The causal relationship between neglecting the mean vector and the equality of the maximum and minimum eigenvalues is not evident and requires further explanation.

The paper optimizes the pair of smooth and orthogonal transformations, with the transformation initialized by the closed-form optimal derivation. It is unclear why it is necessary to further optimize a transformation that is already designed to reach maximum QSUR. Additionally, the paper lacks an ablation study on the impact of different orthogonal initialization methods.

The paper uses online Hadamard transformation for query and key. It is unclear whether the Hadamard transformation can be optimized as suggested in Figure 5.

### Questions
(1). Why is the closed-form optimal transformation derived from QSUR not directly applied in the model?

(2). Does a higher QSUR value guarantee a better transformation in terms of model performance?

(3). Which of the transformation matrices mentioned in the paper are Hadamard matrices and which are unit orthogonal matrices, and are Hadamard matrices trainable as well?

(4). Should softmax be applied before or after the top-k selection, and what is the rationale behind this choice?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the Quantization Space Utilization Rate (QSUR) to assess data quantizability and guides the development of Orthogonal and Scaling Transformation-based Quantization (OSTQuant). OSTQuant optimizes weight and activation distributions in the quantization space and includes a KL-Top loss function to enhance semantic retention in post-training quantization. It outperforms state-of-the-art methods, maintaining 99.5% accuracy in simple configurations and significantly reducing performance gaps in more complex settings.

### Strengths
1. The paper introduces a new metric, QSUR, that links distribution characteristics with quantization space utilization, providing insight into the impact of transformation-based quantization approaches.
2. The proposed method for improving QSUR surpasses previous state-of-the-art techniques in performance.

### Weaknesses
1. Line 087 incorrectly identifies the two methods as block-wise reconstruction methods, which they are not.
2. In Equation (21), the direction of the inequality sign is incorrect. This error affects the subsequent proof, which also requires modification.
3. In Equation (4), the terms $\lambda_{min}$ and $\mathbf{q}_{min}$ should be replaced with $\lambda_{max}$ and $\mathbf{q}_{max}$ respectively, in order to correctly derive $\mathbf{\mathit{v}}_{min}^{org}$ for use in Equation (5). Please refer to the simple example shown in Figure 1(a). Corresponding changes are needed in the related sections of the paper.
4. The paper assumes that weights and activations are normally distributed. This assumption limits the generalizability of the results. The Laplace distribution, commonly used to model tensors, especially for outliers, is not considered. For further reference, see [this link](https://mobiusml.github.io/hqq_blog/).
5. Equation (29) appears to contain a clerical error. If this is not the case, a detailed explanation from the author would be beneficial.
6. The derivation in Section A.2.3 does not convincingly ensure that $|\mathbf{q}_{max}|=d^{-\frac{1}{2}}$, which is necessary to obtain Equation (33).
7. Line 335 mentions "Figure X," which should be corrected to "Figure 5".
8. The use of the scaling vector $\mathbf{S}^i_{u|g}$ in Figure 5 under non-linear activation functions is not equivalent, and it is not employed in current studies. The author should explain the rationale behind using this vector.
9. The notations for vectors and matrices throughout the paper are inconsistent. For example, $S_{updown}$ in Table 4 versus $\mathbf{S}_{u|d}^i$ in Figure 5. The paper should clarify the relationships among $\mathbf{S}_{ffn}^i$, $\mathbf{S}_{attn}^i$, and $\mathbf{S}^i$.
10. In Figure 5, $\mathbf{S}_{qk}^i$ and $\mathbf{S}_{ov}^i$ appear non-trainable. The paper does not provide an explanation for this choice.
11. Table 1 is not illustrated anywhere in the paper.
12. The paper does not include performance comparisons using larger Language Models, such as the 70B LLaMA-3, or investigate other model families and architectures, such as Mistral or Mixtal (MoE). Such comparisons could provide a broader evaluation of the proposed methods.

### Questions
1. Could the authors provide the speedup achieved during the decoding stage after implementing their proposed methods?
2. The paper should describe the initialization process for the scaling vectors used in the transformations. 
3.  How does the model perform if only the initial matrix and vectors are employed to transform the model followed by naive quantization without training?
4. The performance improvement when compared with SpinQuant using a 4-4-4 quantization scheme appears to be less obvious in most cases than when using a 4-4-16 scheme. Can the authors explain why there is a disparity in performance improvements between these two configurations?
5. Regarding the activation distributions post-transformation, is there a noticeable difference among OSTQuant, SpinQuant, and QuaRot? It would be beneficial if the authors could include visualizations for both SpinQuant and QuaRot.

### Soundness
2

### Presentation
1

### Contribution
3
