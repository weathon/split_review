# TesseraQ: Ultra Low-Bit LLM Post-Training Quantization with Block Reconstruction

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 5, 3

## Abstract
Large language models (LLMs) have revolutionized natural language processing, albeit at the cost of immense memory and computation requirements. Post-training quantization (PTQ) is becoming the \emph{de facto} method to reduce the memory footprint and improve the inference throughput of LLMs.
In this work, we aim to push the upper limit of LLM PTQ by optimizing the weight rounding parameters with the block reconstruction technique, a predominant method in previous vision models.
We propose TesseraQ, a new state-of-the-art PTQ technique, to quantize the weights of LLMs to ultra-low bits.
To effectively optimize the rounding in LLMs and stabilize the reconstruction process, we introduce progressive adaptive rounding. This approach iteratively transits the soft rounding variables to hard variables during the reconstruction process. Additionally, we optimize the dequantization scale parameters to fully leverage the block reconstruction technique.
We demonstrate that TesseraQ can be seamlessly integrated with existing scaling or clipping-based PTQ algorithms such as AWQ and OmniQuant, significantly enhancing their performance and establishing a new state-of-the-art.
For instance, when compared to AWQ, TesseraQ improves the wikitext2 perplexity from 14.65 to 6.82 and average downstream accuracy from 50.52 to 59.27 with 2-bit weight-only quantization of LLaMA-2-7B. 
{Across a range of quantization schemes, including W2A16, W3A16, W3A3, and W4A4, TesseraQ consistently exhibits superior performance.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a PTQ method，aTesseraQ, for LLM.  The author propose optimize weight rounding through a progressive
approach based on block reconstruction. Besides, the author also propose dequantization scale tuning to mitigate the reconstruction error.
The experiments on LLaMa models shows good performance, and this training-based PTQ method could be implemented with other PTQ methods.

### Strengths
1. The idea of optimizing the weight rounding error in LLM is interesting, while most previous methods focus on the weight clipping or distribution transmation.
2. The author proposes Progressive Adaptive Rounding strategy by deviding all rounding variables into harden and soften.
3. The performance in W2A16 setting is good and TesseraQ is orthogonal to other post-training quantization (PTQ) methods for LLM.

### Weaknesses
1. unclear writing: The writing in Section 3.2 of the paper is not sufficiently clear, making it somewhat difficult to read and understand. Moreover, this section constitutes the core content of the methodology and pertains to the detailed description of the method itself. Specifically, the progressive adaptive rounding (PAR) algorithm lacks a clear explanation of how the 'harden' and 'soften' variables are determined and updated during the optimization process. The criteria for transitioning variables from 'soften' to 'harden' are not explicitly defined, making it hard to grasp the practical implementation of this core component.
2. Outdated Comparison: The comparison methods in Table 1 appear to be somewhat outdated. The authors should compare with more advanced weight-only methods to demonstrate its superiority. The absence of recent and competitive baselines, such as more advanced rounding techniques or other state-of-the-art PTQ methods, makes it difficult to assess the true performance gains of the proposed method. The current comparisons do not sufficiently establish the novelty and advantage of TesseraQ.
3. Besides, other tables comparison seems inadequate. The authos should also report the comparison results with other Rounding method, such as Adaround and signRound. The lack of direct comparisons with established rounding methods like AdaRound and SignRound makes it difficult to isolate the specific contribution of the proposed progressive adaptive rounding strategy. Without these comparisons, it remains unclear whether the performance gains are due to the block-wise reconstruction or the specific rounding optimization method itself.
4. The author should discuss the method's limitation. The paper lacks a thorough discussion of the limitations of the proposed method. Aspects such as the computational cost of the progressive adaptive rounding, its sensitivity to hyperparameter settings, and its applicability to different model architectures should be addressed. A discussion of the method's limitations is crucial for a balanced assessment of its practical value.

### Questions
1. Why the author didn't compare with Adaround and signRound in Table1 and other experiments?
2. Compared with the traditional Layer-wise Rounding method Adaround, what is the superiority of the proposed TesserQ, is the block-wise reconstruction granulity or the Harden and Soften design? Why? The author should add more related discussion and results to analysis it.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces TesseraQ, a post-training quantization method for LLMs that focuses on optimizing weight rounding parameters using block reconstruction techniques. The key design is a Progressive Adaptive Rounding approach that iteratively converts soft rounding variables to hard variables, along with dequantization scale tuning.
﻿
The method is designed to work with existing quantization approaches like AWQ and OmniQuant, significantly improving their performance particularly for ultra-low bit scenarios (2-4 bits). Results show major improvements in both perplexity metrics and downstream task accuracy across different LLaMA models and quantization schemes.
﻿
The main contribution is enabling better ultra-low bit quantization of LLMs through tuning of quantization rounding while maintaining model performance, demonstrated through comprehensive empirical results.

### Strengths
1. The paper presents a clear motivation for ultra-low bit LLM quantization, with a well-justified technical solution. The authors effectively demonstrate how current methods struggle with low-bit quantization and explain why optimizing the entire weight tensor is necessary. The progressive adaptive rounding approach is sound to handle the problem.

2. The writing quality is exceptionally clear and professional. Complex technical concepts are explained systematically, from basic quantization principles to advanced optimization techniques. The figures and algorithms are informative and well-designed, particularly Figure 1 which clearly illustrates the workflow.

3. The experimental results show substantial improvements over strong baselines. For example, improving WikiText2 perplexity from 37.37 to 8.05 on LLaMA-2-7B with W2A16 quantization is a significant achievement. The ablation studies effectively isolate the contributions of PAR and DST.

4. The practical utility is demonstrated through real-world evaluations. The authors test different hardware configurations, measure actual throughput, and analyze memory consumption.

### Weaknesses
1. The paper lacks detailed technical comparisons with similar methods. While mentioning prior approaches like AdaRound and AdaQuant,  it doesn't experimentally demonstrate why the proposed methods are superior to the these methods. The rationale behind several design choices (sigmoid reparameterization; harden score metric in Eq 6; avoiding scale optimization in the quantization step) isn't fully justified through comparative experiments. Specifically, the paper does not provide sufficient evidence to support the claim that the proposed progressive adaptive rounding (PAR) approach is superior to directly optimizing the rounding of all weights simultaneously. The choice of using a sigmoid for reparameterization, while common, lacks a comparative analysis against other relaxation techniques. The Harden Score (HS) metric is introduced without a clear justification of its effectiveness over alternative methods for selecting which rounding variables to harden. Furthermore, the decision to avoid scale optimization during the quantization step is not thoroughly explained with empirical evidence, leaving open the question of whether this choice limits the optimization potential.

2. The evaluation demonstration has problems.
- The inconsistency in model selection between Tables 1, 2 and 3 makes it difficult to draw comprehensive conclusions. 
- Runtime and GPU memory analysis is limited to the 7B model.  As the runtime and memory consumption are important metircs, the authour should provide comprehensive efficiency metrics across different model sizes.
- The paper would be stronger with complete results for newer models like LLaMA-3 across all experiments.

3. The technical novelty is relatively incremental. Both block reconstruction and scale tuning are well-established in PTQ literature. While the paper makes useful improvements, it builds primarily on existing techniques rather than introducing fundamentally new concepts. The paper does not clearly articulate how the combination of these existing techniques leads to a novel contribution beyond the sum of its parts. The progressive adaptive rounding approach, while effective, is not presented as a fundamentally new optimization technique, but rather as a specific application of existing concepts.

### Questions
1. The choice to restrict rounding to ±1 steps seems limiting. Why not allow multiple step sizes as in AdaQuant? This decision could impact optimization flexibility, especially for ultra-low bit quantization where precision is crucial. Has this design choice been empirically validated against alternatives?

2. The effectiveness with weight transformation techniques is unclear. Specifically, would TesseraQ maintain its benefits when applied after Hadamard matrix transformations (as in QuaRot)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel method to compress large language models (LLMs) into ultra-low-bit formats while maintaining high performance. It introduces Progressive Adaptive Rounding (PAR), which gradually decides rounding schedules for groups of parameters within LLMs while retaining the training flexibility via Sigmoid-based soft-hard transition, improving quantization stability. By integrating with block-wise reconstruction instead of layer-wise optimization, TesseraQ captures inter-layer dependencies more effectively, and de-quantization scale tuning further reduces reconstruction errors. The method integrates seamlessly with existing quantization approaches like AWQ and OmniQuant, significantly improving perplexity and accuracy across benchmarks. TesseraQ achieves state-of-the-art results, offering a practical solution for deploying LLMs efficiently in memory-constrained environments.

### Strengths
The paper offers an interesting and effective add-on for block-wise reconstruction for LLM quantization with optimized rounding policy. Especially for Ultra-low bit scenarios, such combination advances the such field where prior quantization methods struggle to maintain performance for various tasks.

The methodology is well-designed, with clear theoretical motivation for each component, including PAR and dequantization scale tuning. The experimental results are robust, demonstrating TesseraQ’s superiority across multiple benchmarks such as WikiText2 and downstream reasoning tasks. The paper carefully evaluates TesseraQ’s effectiveness by comparing it to several existing methods, providing quantitative evidence that supports the proposed contributions.

In terms of the overall writing quality, the paper is generally well-organized and explains technical concepts like rounding optimization and block reconstruction in a clear and structured manner.  

The significance of the paper lies in its potential impact on LLM deployment, particularly for memory-constrained environments such as consumer devices and edge processors. TesseraQ pushes the boundaries of ultra-low-bit quantization, a growing need as LLMs become larger and more ubiquitous.

### Weaknesses
1. The paper proposes PAR instead of the common STE implementation. There is a lack of justification why direct utilization of STE for the rounding policy estimation would result in worse performance so that PAR is significant in the overall design. Specifically, the paper does not explore the potential instability or convergence issues that might arise from directly applying STE to the rounding policy, nor does it provide a comparative analysis demonstrating the benefits of PAR over a well-tuned STE approach. The absence of this comparison makes it difficult to assess the necessity of the progressive adaptive rounding strategy.

2. The paper purposes an effective rounding optimization add-on for enhancing the block-wise quantization for LLM, but there is a lack of theoretical analysis of the different between: A) BLOCK-WISE & Normal Rounding (round to the nearest) and  B) the proposed BLOCK-WISE & Rounding Optimization. If A) is well trained and fully converged, would it theoretically have the similar mathematical foundations as B)? The paper does not delve into the theoretical underpinnings of why optimizing the rounding policy within a block-wise framework leads to superior performance compared to simply using standard rounding within the same block-wise setup. It is unclear whether the gains are due to a more effective exploration of the loss landscape or simply a better fit to the training data.

### Questions
The paper is generally clear and well-written, the algorithm has been fully presented. While according to my perspective in the weakness section, I have the following question:

1. Why does the paper adopt Progressive Adaptive Rounding (PAR) instead of the more common Straight-Through Estimator (STE) for rounding policy estimation? What specific limitations or performance issues with STE justify the need for PAR in the overall design? If STE is applied, whether such progressive-stage training is still required?

2. Could the authors justify the theoretical basis for the improvement achieved by rounding optimization over the baseline?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Large language models (LLMs) has recently gained widespread attention，but face challenges in memory and computation requirements.  Post-training quantization (PTQ) is a common approach to address these issues. This work mainly proposes some optimization methods for PTQ targeting LLM.The proposed TesseraQ, a novel PTQ technique, can quantize LLMs to ultra-low bits. It introduces progressive adaptive rounding to iteratively transition soft rounding variables to hard ones during reconstruction and optimizes the dequantization scale parameters. TesseraQ can be integrated with existing PTQ algorithms like AWQ and OmniQuant. Experiments show that TesseraQ significantly improves performance.

### Strengths
The paper proposes a new rounding optimization design called TesseraQ， it can be combined with other PTQ methods to achieve new performance levels, establishing a new technological level for quantifying LLM in terms of confusion, downstream accuracy, and hardware performance.

### Weaknesses
1.  3.2 Some expressions are not very clear, and some variables have not been explained
2.  The new rounding error optimization method proposed in the paper mentions that compared to previous methods ( https://arxiv.org/pdf/2004.10568 ) does not rely on regularization loss , but HS and sorting were introduced. It doesn't have a significant advantage.For example, computational complexity and convergence speed.
3.  The paper combines the proposed rounding error optimization method with other methods for experimentation and comparison with other quantization methods, but does not use other rounding error optimization methods for the same experiment, and does not demonstrate the superiority of this method.For example, the Adaround mentioned in the article.
4. When comparing quantitative indicators such as W4A4/W3A3 that include activation, the QuaRot initial method was used, but it was not compared with using the QuaRot method alone. The advantage of the proposed new rounding error optimization method in improving accuracy cannot be clearly demonstrated.Suggest to use QuaRot as a baseline separately to include the results.

### Questions
1. The new rounding error optimization method proposed in the paper mentions that compared to previous methods ( does not rely on regularization loss , but HS and sorting were introduced. Does it have advantages in training convergence speed and video memory usage?
2. The paper combines the proposed rounding error optimization method with other methods for experimentation and comparison with other quantization methods, but does not use other rounding error optimization methods for the same experiment, Can relevant experiments be supplemented ?
3.When comparing quantitative indicators such as W4A4/W3A3 that include activation, the QuaRot initial method was used, but it was not compared with using the QuaRot method,Can relevant experiments be supplemented?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
TesseraQ is a new PTQ method for ultra-low bit quantization of LLM weights. It features progressive adaptive rounding and optimized dequantization scale parameters, improving block reconstruction. Integrated with PTQ algorithms like AWQ and OmniQuant, TesseraQ significantly enhances performance.

### Strengths
The authors introduce two techniques to optimize more parameters under PTQ settings, enhancing the performance of quantized models through block-wise reconstruction. These approaches, combined with existing transformation-based methods, deliver improved model accuracy without adding inference overhead.

### Weaknesses
1. While the paper claims to establish a new state-of-the-art, SpinQuant, as discussed in the related work, appears to far outperform the proposed method. It would be beneficial if the authors could initialize their model from SpinQuant and then apply their method to demonstrate its effectiveness.
2. Line 141 mentions that GPTQ can cannot be used to improve other transformation-based methods. However, GPTQ can significantly enhance the performance of rotation-based transformation like SpinQuant and QuaRot.
3. The rationale for using progressive freezing instead of a dynamic regularization term (i.e., AdaRound) for optimizing rounding values is not clearly articulated, nor is it convincingly demonstrated why this method surpasses AdaRound. The explanations in Lines 075 to 077 lack substantial evidence.
4. The paper does not compare its progressive rounding approach with existing rounding methods such as AdaRound, AdaQuant, and FlexRound, missing an opportunity to justify the need for progressive rounding.
5. Lines 230 to 231 discuss the potential negative impacts of optimizing the scale parameter $s$ in quantization. However, experimental evidence is needed to substantiate that learning $s$ is detrimental, as the current argument does not conclusively link optimization of $s$ to performance degradation.
6. The paper optimizes significantly more parameters than previous methods using limited data, raising concerns about potential overfitting. A user study or chat test could provide essential validation.
7. Line 473 states a significantly larger value than AWQ/OmniQuant, but it's unclear what this comparison signifies as these methods do not optimize rounding to flip variables.
8. The necessity of the sigmoid function $\sigma(\cdot)$ in Equation (9) should be experimentally validated. Why not use $\mathbf{v} \times \mathbf{s} \times (\theta^{q}-\mathbf{z})$ with $\mathbf{v}$ initialized to $\mathbf{1}$?
9. Further evaluation is needed on the effect of larger $t$ values in the expression $\frac{1}{\exp(tx)}$ and other scheduling functions in the **PAR Schedule** to demonstrate the method's robustness to different schedules.
10. More comparisons with block-wise reconstruction or learning-based methods, e.g, DuQuant (https://arxiv.org/abs/2406.01721) and QLLM (https://arxiv.org/pdf/2310.08041) could help confirm its effectiveness.
11. The author does not provide results for the proposed method without using transformation-based initialization.

### Questions
Why didn't the authors compare their method with OmniQuant for weight-activation quantization?

### Soundness
2

### Presentation
3

### Contribution
2
