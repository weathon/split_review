# I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models

- Decision: Reject
- Scores: 5, 5, 6, 6, 3

## Abstract
Post-training quantization (PTQ) serves as a potent technique to accelerate the inference of large language models (LLMs). Nonetheless, existing works still necessitate a considerable number of floating-point (FP) operations during inference, including additional quantization and de-quantization, as well as non-linear operators such as RMSNorm and Softmax. This limitation hinders the deployment of LLMs on the edge and cloud devices.  
In this paper, we identify the primary obstacle to integer-only quantization for LLMs lies in the large fluctuation of activations across channels and tokens in both linear and non-linear operations. To address this issue, we propose I-LLM, a novel integer-only fully-quantized PTQ framework tailored for LLMs. Specifically, (1) we develop Fully-Smooth Block-Reconstruction (FSBR) to aggressively smooth inter-channel variations of all activations and weights. (2) to alleviate degradation caused by inter-token variations, we introduce a novel approach called Dynamic Integer-only MatMul (DI-MatMul). This method enables dynamic quantization in full-integer matrix multiplication by dynamically quantizing the input and outputs with integer-only operations. (3) we design DI-ClippedSoftmax, DI-Exp, and DI-Normalization, which utilize bit shift to execute non-linear operators efficiently while maintaining accuracy.
The experiment shows that our I-LLM achieves comparable accuracy to the FP baseline and outperforms non-integer quantization methods. For example, I-LLM can operate at W4A4 with negligible loss of accuracy. To our knowledge, we are the first to bridge the gap between integer-only quantization and LLMs. We've published our code on \href{https://anonymous.4open.science/r/I-LLM-F242/}{anonymous.4open.science}, aiming to contribute to the advancement of this field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an integer-only post-training quantization (PTQ) framework to accelerate the inference of large language models, called I-LLM. The authors introduce three main techniques: Fully-Smooth Block Reconstruction (FSBR), which reduces inter-channel activation disparities; Dynamic Integer-only MatMul, enabling dynamic quantization and integer-only matrix multiplication; and integer-only non-linear operators such as DI-ClippedSoftmax and DI-Exp, which use bit-shifting for efficiency. Experimental results show that I-LLM achieves accuracy on par with floating-point baselines while delivering significant improvements in computational performance and memory efficiency.

### Strengths
1. This paper addresses the challenge of integer-only quantization, which is often overlooked by existing work as typical LLM quantization methods usually store intermediate results as floating-point values.

2. The paper introduces innovative integer-only operators, such as DI-Exp, DI-ClippedSoftmax, and DI-Norm, to replace computationally intensive floating-point operations.

3. The experimental section includes a thorough comparison across multiple model types and configurations, as well as an ablation study, demonstrating the framework’s efficiency.

### Weaknesses
1. The motivation for this work is not clearly explained, especially regarding why integer-only quantization is necessary. The trade-off between accuracy and inference performance needs more discussion. Additionally, the configuration of different quantization types for weights and activations (e.g., W8A8, W4A8, W4A4) is not discussed. The paper lacks a clear explanation of the specific hardware constraints or application scenarios that necessitate integer-only quantization, making it difficult to assess the practical relevance of the proposed method. Furthermore, the absence of a detailed analysis of the accuracy-performance trade-offs for various weight and activation quantization configurations leaves a gap in understanding the method's applicability under different resource constraints.

2. The experimental setup lacks clarity, and more results on inference performance are needed. See detailed comments 1-3. Specifically, the paper does not provide sufficient detail on the benchmarking environment, including the specific hardware used, software libraries, and compiler optimizations. The lack of clarity on whether Tensor Cores were utilized and the specific framework employed for latency measurements makes it difficult to reproduce the results and assess the true performance gains. Furthermore, the paper does not include a breakdown of the latency contributions from different components of the model, making it difficult to pinpoint the bottlenecks and evaluate the effectiveness of the proposed integer-only operators.

3. The innovation of the Fully-Smooth Block Reconstruction method is limited, as it closely resembles SmoothQuant. Additionally, the overhead of dynamic quantization should be demonstrated in the experimental results. The paper does not adequately differentiate FSBR from SmoothQuant, particularly regarding the specific smoothing techniques and their impact on quantization error. The paper also fails to provide a detailed analysis of the computational overhead of dynamic quantization, including the cost of computing and applying the dynamic scale factors and zero points, which is critical for evaluating the overall efficiency of the proposed method.

### Questions
I have few questions and comments as below: 

1. In Table 1, the results for SmoothQuant under the W4A4 setting (e.g., 1.8e4 for the OPT family) are unusually high, especially compared to LLaMA models. This discrepancy should be explained.

2. The experimental setup is unclear, especially regarding Table 4, where latency and speedup for traditional W4A4 are reported. What framework was used, and was Tensor Core applied?

3. To better understand the efficiency of integer-only quantization, comparisons with other quantization works like QServe [1] and Atom [2] should be included.

4. In the quantization algorithms, how are the scale factor and zero-point stored? If they are stored as integers, does this significantly impact accuracy? A discussion on this trade-off is needed.


[1].QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving
[2].Atom: Low-bit quantization for efficient and accurate llm serving

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
The paper proposes I-LLM, an integer-only post-training quantization (PTQ) framework for large language models (LLMs), aiming to improve inference efficiency on hardware lacking floating-point support. The key contributions include the Fully-Smooth Block-Reconstruction (FSBR) to smooth inter-channel variations in activation and dynamic quantization methods (Dynamic Integer-only MatMul and others). Experiments on several LLMs, such as LLaMA and OPT, demonstrate improved modest speed and memory usage under W4A4 settings, with minimal accuracy loss compared to floating-point (FP) models. Despite these claims, the methodology largely extends known techniques, showing limited novelty, and lacks sufficient evaluation against state-of-the-art (SOTA) approaches on challenging quantization settings.

### Strengths
- The integer-only quantization of non-linear operations offers potential efficiency improvements for hardware without FP support.
- Demonstrates notable performance in W4A4 quantization settings, showing significant reductions in latency and memory usage on specific LLMs.

### Weaknesses
 - The proposed techniques, such as FSBR, heavily build on prior works like OmniQuant for quantization-parameter tuning and I-VIT for dynamic quantization, limiting originality.
- The absence of comprehensive SOTA comparison limits the rigor of performance claims, particularly missing comparisons with rotation-based methods (e.g., SpinQuant (Liu et al., 2024)) and LUT-based approximations (e.g., NN-LUT(Yu et al., 2022)).
- FSBR and DI-MatMul introduce computational overhead with on-the-fly operations like 8-bit scalar multiplication/division, yet no detailed ablation study quantifies the latency impact per Transformer component.
- The evaluation datasets and tasks are limited, and broader testing across more diverse and challenging benchmarks is required to substantiate the generalization of results.
- The description of FSBR is unclear. Could the authors provide a more explicit breakdown of its application across different computing units beyond MatMul?
- The authors also emphasize the outliers across the token (which sounds new), but Fig. 3 shows that the token-wise distribution looks much flatter than the channel-wise distribution, which is well known.

### Questions
- What framework and baseline setup were used for W4A4 quantization, and can more detail be provided about the experimental environment?
- The description of FSBR is unclear. Could the authors provide a more explicit breakdown of its application across different computing units beyond MatMul?
- The authors also emphasize the outliers across the token (which sounds new), but Fig. 3 shows that the token-wise distribution looks much flatter than the channel-wise distribution, which is well known.

### Soundness
2

### Presentation
2

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
The paper present an end-to-end quantization method that is applied to all the inference sub-steps in LLMs, including non-linear operations and all attention calculations. The technique presented leverages block and dynamic quantization concepts. Specific integer approximation for non-linearities are presented to avoid moving o fp when computing them, End-to-end results are presented, and an implementation of the method on GPU is also presented, showing significant speedups.

### Strengths
First method that covers all the steps of integer inference.
Presents implementation results, showing significant speedup even in non-adhoc designed hardware
end-to-end results in inference are presented, not only sub-steps

### Weaknesses
It seems the method is not post-training (the smoothing coefficients are learned), hence it is not applicable for the largest LLMs for which training is not really easy to repeat. 
Notation is hard to follow and could be simplified to get better intuition on the methods applied. 
Approximation proposed for non-linear functions are not really well justified
Similar ideas are present in I-BERT, I-ViT, BRECQ. Thus, the contribution of this paper seems to be incremental (see BRECQ: Pushing the Limit of Post-Training Quantization by Block Reconstruction)

### Questions
Detail more in depth the steps needed in training.

### Soundness
4

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
This study introduces a novel quantization approach for large language models (LLMs), featuring custom-designed modules: DI-MatMul, DI-ClippedSoftmax, DI-Exp, and DI-Normalization. These modules collectively outperform state-of-the-art (SOTA) methods, offering enhanced performance in LLM applications.

### Strengths
The authors provide valuable insights into the quantization of large language models (LLMs), demonstrating how such models can maintain high accuracy despite the reduced precision.

### Weaknesses
Consider combining quantization with pruning to achieve enhanced model efficiency and reduced computational overhead.
Consider a hybrid quantization approach, where different layers utilize varied precision levels, such as W4A4 for certain layers and W8A8 for others, to balance efficiency and performance.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces I-LLM, a novel integer-based post-training quantization (PTQ) framework for large language models (LLMs). Traditional PTQ techniques involve a mix of integer and floating-point operations, which limits deployment on edge devices that lack floating-point capabilities. The authors propose three techniques: Full-Smooth Block Reconstruction (FSBR) to smooth activation variations across channels, Dynamic Integer Matrix Multiplication (DI-MatMul) to manage variations between tokens, and dynamic integer implementations for nonlinear operations. Experiments show that I-LLM achieves comparable post-compression performance with existing methods while significantly reducing computational overhead.

### Strengths
1. The proposed framework enables integer-only quantization for LLMs: by completely avoiding floating-point operations, I-LLM takes an important step toward making LLMs deployable on edge devices, achieving faster and more efficient inference on hardware without the need for floating-point support.

2. The authors conducted extensive experiments across various LLM architectures, model sizes, and datasets, with the table data from the manuscript demonstrating overall outstanding performance.

3. This paper introduces techniques like FSBR and DI-MatMul that optimize LLM quantization accuracy by addressing variations across channels and tokens. These techniques help maintain high precision during the inference process.

### Weaknesses
1. Section 3.2 of the paper proposes 'training a smoothing coefficient for all activations and weights to aid in restoring the model’s quantization accuracy.' However, the training and solving process of this coefficient is not discussed, which could lead to confusion and misunderstandings. If the reason for not detailing this part is that the method aligns with SmoothQuant or OmniQuant, it should be explicitly cited and clearly explained.

2. Equations (1) and (2) extend SmoothQuant by applying smoothing to 'NonLinear Act-Smooth.' However, the motivation of SmoothQuant is to reduce the difficulty of quantization by lowering the smoothness of activations through a smoothing coefficient. In Equations (1) and (2), the smoothing coefficient is counterbalanced between the Gate-layer and Up-layer using '*s' and '/s', respectively. The paper does not discuss the rationale behind this operation or why 'W' scale is 'times' while the 'V' is 'division'. 

3. The definition of $\sigma$ in Equation (2) is confusing. Based on Equation (2) and line 262, it follows that $\sigma'(x1) = \sigma(x1 / s)$, and $\sigma'(x1') = \sigma(x1' / s)$. So we can get $\sigma(x1' / s) = \sigma(x1 / s)$, i do believe this is not a right equation or hope the author can make a clarification on this.

4. The authors state in line 270 that 'SmoothQuant and OmniQuant are subsets of FSBR.' However, based on the description in this section, it appears that FSBR actually adopts the techniques of SmoothQuant and OmniQuant and extends them within 'NonLinear Act-Smooth.' Referring to them as subsets is inaccurate and could lead to misunderstandings.

5. I have carefully reviewed and evaluated the anonymous code repository provided by the authors. Regarding the DI-MatMul computation process mentioned in Section 3.3 (specifically in *quantize/quant_modules/QuantMatMul, quantize/quantizer), its implementation and definition of 'dynamic' is consistent with the OmniQuant codebase. If there are any omissions or misunderstandings, I would appreciate further clarification from the authors.

6. Since the quantizer used in the paper results in the same post-quantization weight bit-width and additional quantizer parameters (scaling factor, zero factor) as methods like OmniQuant, the specific factors behind the reduction in **Weight Memory** listed in Table 4 for I-LLM are not clearly discussed. It would be helpful if the authors could clarify which specific parameter compression or operation contributes to this memory efficiency advantage.

7. In table 5, 'OmniquantQuant'->'Omniquant', 'CLippedSoftamx'->'CLippedSoftmax'

### Questions
Please refer to Weaknesses

### Soundness
3

### Presentation
1

### Contribution
2
