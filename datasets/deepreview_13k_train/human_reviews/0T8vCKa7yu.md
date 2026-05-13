# LLM Compression with Convex Optimization—Part 1: Weight Quantization

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
In recent years, compression of large language models (LLMs) has emerged as an important problem to enable language model deployment on resource-constrained devices, reduce computational costs, and mitigate the environmental footprint of large-scale AI infrastructure. In this paper, we lay down the foundation for LLM quantization from a convex optimization perspective and propose a quantization technique that builds on this foundation for optimum quantization outcomes. Our quantization framework, CVXQ, scales to models containing hundreds of billions of weight parameters and provides users with the flexibility to compress models to any specified model size, post-training. A reference implementation of CVXQ can be obtained from.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method called CVXQ for mixed precision weight-only quantization of large language models (LLMs) using convex optimization techniques. CVXQ allows for user-specific quantization bit depths by defining the average bit depth and then seeking to minimize quantization error within this constraint. The method introduces row-wise and column-wise clustering to achieve this goal, where each cluster can be assigned different bit depths. To assign these bit depths, the problem is formulated in a Lagrangian form and solved using convex optimization. The effectiveness of CVXQ is demonstrated by achieving superior performance on the WikiText perplexity (PPL) metric compared to methods such as GPTQ, AWQ, and OWQ across various sizes of OPT models.

### Strengths
* Demonstrates that companded quantization can reduce the mean square error of weights before and after quantization more effectively than uniform quantization.
* Introduces a novel approach to weight-only quantization by employing various partitioning methods, specifically row and column clustering.
* Proposes a method to minimize the degradation in performance due to quantization within a constrained average bit depth by finding the optimal bit assignment combination. This is achieved by defining the quantization objective function in a Lagrangian form and solving it using convex optimization.
* Shows that the proposed partitioning methods can result in greater bit depth savings compared to non-partitioned methods.

### Weaknesses
 * Lacks comparison with existing LLM quantization methods such as FlexRound[1] and QuIP[2]. The absence of a direct comparison with these methods makes it difficult to assess the relative advantages and disadvantages of the proposed CVXQ method. Specifically, it is unclear how CVXQ performs in terms of accuracy and compression rate compared to these state-of-the-art techniques.
* Primarily evaluates LLM performance using perplexity, with insufficient comparison across other metrics like MMLU and AlpacaEval. While perplexity is a useful metric for evaluating language models, it does not fully capture the performance on downstream tasks. A more comprehensive evaluation should include metrics that assess the model's ability to perform tasks such as question answering, common sense reasoning, and instruction following.
* Insufficient discussion and comparative analysis on how the proposed CVXQ method can be accelerated on existing hardware such as GPUs. One of the key goals of compression methods like quantization is to achieve actual acceleration. Although the paper mentions that this will be addressed in Part 2, it is crucial to include a discussion on how to accelerate the proposed quantization format. The lack of information on kernel implementation details and expected speedups makes it difficult to assess the practical benefits of the method.
* Tables 1 and 2 lack information on the average bit depth achieved by CVXQ. Since the proposed method assigns bit depths through a convex optimization process, it may not exactly match the user-specific quantization bit depth, leading to potentially different compression rates in practice. The absence of this information makes it difficult to evaluate the actual compression achieved by the proposed method.
* The quantization process described in the paper suggests that the time required for quantization might exponentially increase with the number of iterations, as shown in Figure 5. This could be a significant limitation for large models, making the method less practical for real-world applications.

### Questions
* What do the terms "row" and "column" mean in the context of row and column partitioning in Figure 3?
* What units were used for clustering in Tables 1 and 2?
* The Massive Activation paper[3] demonstrated significant performance degradation when clipping massive activations from activation distributions. Papers like LLM.int8, SmoothQuant, and AWQ have shown the importance of considering activation distributions to mitigate the impact of outliers. Can the proposed CVXQ method be extended to apply to activation distribution?
* How does the size of the calibration set affect the performance of CVXQ?

[3] Massive Activations in Large Language Models, https://arxiv.org/abs/2402.17762

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce a quantization framework called CVXQ, which first optimizes bit depth assignment and then refines step sizes and biases using convex optimization techniques. To further improve the quantization scheme, the framework incorporates matrix partitioning, dividing the matrix into a set of row or column sub-matrices, each with its own bit depth and step size. The experiments are conducted on Meta's LLaMA and OPT models, using PPL and GSM8K as evaluation metrics.

### Strengths
The authors derive several mathematical formulations for the quantization scheme, making a few assumptions about weight distributions, such as Normal or Laplace. They use figures to illustrate whether the statistical data from the OPT models align with these assumed distributions.

### Weaknesses
The main concern with this manuscript is that it does not address practical hardware constraints. Specifically, the authors permit each weight to have a different bit depth assignment, a strategy that is rarely seen in existing literature. For instance, AWQ employs dedicated kernels and uniformly quantizes all weights to 4 bits, aligning with the availability of a 4-bit engine. However, the manuscript lacks discussion on hardware acceleration or performance degradation resulting from the proposed quantization scheme.

By neglecting hardware-related considerations, the comparisons with previous works may appear unfair. Well-established quantization methods like OWQ, AWQ, or RTN explicitly demonstrate how their quantized models achieve latency improvements on common GPUs. In contrast, this manuscript explores more complex ideas, such as pruning and matrix partitioning, without addressing the impact on parallelism or the hardware requirements these approaches would entail.

It is crucial to describe the limitations of the quantization scheme for practical hardware implementation. Without doing so, methods that account for hardware acceleration might seem inadequate, despite the practical challenges associated with mixed precision or varying bit depth assignments.

For example, the authors should clarify how different bit-depth assignments would affect matrix multiplication kernels as batch size increases, as this could have a significant impact on performance.

In summary, the major concerns are: 1) the lack of considerations for hardware acceleration; 2) the use of configurations, such as varying bit depths, that seem impractical and create unfair comparisons with prior work; and 3) the need for a reevaluation of experimental results, given that the proposed quantization schemes operate under fundamentally different assumptions.

### Questions
Please see weaknesses

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a framework for efficient handling of large language models (LLMs) by (1) determining mixed-precision quantization at layer or group levels to meet a target bitwidth and (2) proposing a novel method for deciding quantization step sizes.

### Strengths
The proposed techniques are well-grounded in theory, and each aspect of the framework appears logically sound and justifiable.

### Weaknesses
The paper introduces a mixed-precision approach, but comparisons are primarily made with uniform-precision quantization methods. A broader survey and comparison with other mixed-precision methods, addressing their strengths and weaknesses, would provide a stronger context for evaluating the proposed method.

An ablation study is needed. According to Z-Fold [1], step size determination methods like Min-Max, MMSE, and Hessian-based approaches are often used in quantization. A comparative analysis showing the effectiveness of the proposed method against these would strengthen the evaluation.

Separating the processes of bit-precision allocation and the quantization algorithm applied could provide clearer insights into each aspect of the method.

The proposed methodology is reasonable but lacks comparative analysis, which would underscore its relative advantages.


Testing on a wider range of models and benchmarks would further validate the generalizability of the proposed approach.

### Questions
The paper claims that the proposed algorithm completes the quantization quickly, yet a lack of experimental or theoretical analysis supports this assertion. Could the authors provide more evidence or discussion on this aspect?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the critical issue of large language model (LLM) compression, proposing a novel quantization technique, CVXQ, viewed from a convex optimization perspective. CVXQ, scalable to models with hundreds of billions of weight parameters, allows users to compress models to any specified size after training

### Strengths
The paper introduces a comprehensive quantization method for applying different bit allocation to groups within a large language model (LLM) matrix.

### Weaknesses
 - The paper's contribution isn't distinct. Although it proposes treating dynamic bit allocation as a convex optimization problem, this approach faces several issues:
  - Mixed-precision quantization is a well-researched field; the paper should highlight how its method differs from existing techniques and why it chose to compare solely with LLM quantization methods.
  - Group quantization is not a new concept but a long-standing basic strategy in the quantization field.
  - The convex optimization formulation proposed seems flawed. For instance, in equation three, f(X) is not convex, which questions the validity of the entire problem.
- The writing needs improvement. The definition of "part-1" in the title is unclear, and many descriptions in the text are ambiguous.
- The utility of mixed precision within a matrix is unclear. This approach would require complex, specific hardware design, limiting its broad application. Most mixed-precision quantizations occur between layers, not within a matrix.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
