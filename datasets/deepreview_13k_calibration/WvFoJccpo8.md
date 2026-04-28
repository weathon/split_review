# QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Recently years have witnessed a rapid development of large language models (LLMs). Despite the strong ability in many language-understanding tasks, the heavy computational burden largely restricts the application of LLMs especially when one needs to deploy them onto edge devices. In this paper, we propose a quantization-aware low-rank adaptation (\textbf{QA-LoRA}) algorithm. The motivation lies in the imbalanced degrees of freedom of quantization and adaptation, and the solution is to use group-wise operators which increase the degree of freedom of quantization meanwhile decreasing that of adaptation. QA-LoRA is easily implemented with a few lines of code, and it equips the original LoRA with two-fold abilities: (i) during fine-tuning, the LLM's weights are quantized (\textit{e.g.}, into \textsf{INT4}) to reduce time and memory usage; (ii) after fine-tuning, the LLM and auxiliary weights are naturally integrated into a quantized model without loss of accuracy. We apply QA-LoRA to the LLaMA and LLaMA2 model families and validate its effectiveness in different fine-tuning datasets and downstream scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a modification to the QLoRA method, designed to facilitate the training of large language models with limited computational resources. QLoRA initially quantizes neural network weights to NF4 format and subsequently optimizes LoRA matrix weights in FP16. This process increases inference latency, as everything is converted to FP16 during inference. The proposed alternative method outlined in this paper ensures the appropriate quantization of LoRA weights without necessitating a reversion to FP16 during inference. This enhancement involves just a few lines of code, offering a more efficient solution. While the paper lacks specific results and comprehensive explanations, it presents a promising direction for optimizing large language model training within constrained computational budgets.

### Strengths
**Addresses a Significant Issue** - QLoRA's potential is realized through its ability to quantize LoRA weights, effectively resolving the disparities observed between fine-tuning and inference in QLoRA.

**Streamlined Implementation** - The authors highlight the method's simplicity, emphasizing that it necessitates a mere two lines of code modification to yield impressive enhancements.

**Thorough Assessment** - The evaluation is meticulous, with the authors examining a spectrum of competitive methods and diverse model architectures to demonstrate the method's advantages comprehensively.

### Weaknesses
Reasoning behind the method - Wy should all the c_ij as defined in the paper be equal is not clear — which is the main motivation for the group-wise quantisation. I would be willing to improve the scores with better explanation on the explanation of the method (See the questions)

In Algorithm 1, the function `merge_with_quantization` is defined but never used.

What is the degree of freedom of quantisation and adaptation - These seem to be new terms that are added in this paper and not used in the literature. These have to be defined, before claiming that they are increased or managed by the proposed method

Page 6 is just results - Page 6 is just results without much to interpret. These are a bunch of numbers. Please consider presenting this table in a better manner. Can this be presented as a graph for readers? Just numbers are hard to read

In Table 2, you indicate that the number of parameters in the method are lesser than QLoRA — almost by 2x. Why is this the case? This seems like a unfair comparison to QLoRA. What is the time taken in hours for fine-tuning with similar number of parameters.

Section 3.3 explains the method and the reasoning behind on why the rank degenerates to 1. But the explanation is not comprehensive.

### Questions
1. In Algorithm 1, the function `merge_with_quantization` is defined but never used. 
2. What is the degree of freedom of quantisation and adaptation - These seem to be new terms that are added in this paper and not used in the literature. These have to be defined, before claiming that they are increased or managed by the proposed method
3. Page 6 is just results - Page 6 is just results without much to interpret. These are a bunch of numbers. Please consider presenting this table in a better manner. Can this be presented as a graph for readers? Just numbers are hard to read
4. In Table 2, you indicate that the number of parameters in the method are lesser than QLoRA — almost by 2x. Why is this the case? This seems like a unfair comparison to QLoRA. What is the time taken in hours for fine-tuning with similar number of parameters.
5. Section 3.3 explains the method and the reasoning behind on why the rank degenerates to 1. But the explanation is not comprehensive.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a Quantization-Aware Low-Rank Adaptation (QA-LoRA) for efficient fine-tuning of LLM. This work comes improves Q-LORA algorithm by introducing group-wise operators which lift the need for post-training quantization. QA-LoRA implementation is simple and generic. It benefits from a balance between the number of parameters required for adaption and quantization. The experiments show that fine-tuning and inference stages are computationally efficient thanks to the use of INT4. The memory footprint of QA-LoRA is lower than QLoRA. In terms task accuracy, QA-LoRA is better than Q-LoRA with post-training quantization (GPTQ).

### Strengths
- This work solves a limitation of previous parameter-efficient tuning of LLMs by eliminating the need for a separate post-training quantization which drops model accuracy
- QA-LoRA further enhances memory efficiency of SOTA while preserving accuracy
- The experiments are convincing as they cover a wide range of scenarios

### Weaknesses
QA-LoRA introduce a hyper-parameter (L: Group size). This requires additional optimization and It is unclear if it can be selected without tuning.

### Questions
- I wonder if larger model where the need of this technique is crucial, e.g., 30B-60B, could be discussed.
- Figure 3 legend should have QA-LoRA instead of A-LoRA

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes QA-LoRA, a LoRA based parameter efficient LLM finetuning scheme with quantization. QA-LoRA extends QLoRA to be able to add low-rank matrices with pre-trained weights in low-bit tensors directly, without the need to PTQ on low-rank matrices. To guarantee that the summation of low-rank matrices and pre-trained weights are still within the same quantization range, the authors relax the requirement of each row being the same into groups, through group-wise quantization. This improves the accuracy and efficiency during inference. During evaluation, the authors experimented with a series of LLaMA and LLaMA2 models with different sizes. Results showed that the proposed models can achieve superior performance than LoRA and QLoRA.

### Strengths
* The paper organization, presentation, and references are good.
* The proposed method has enough novelty.

### Weaknesses
 * Parameter offset in experiments: The proposed method incorporates group-wise/sub-channel qunatization, which includes an additional number of parameters for scales. Also, the proposed QA-LoRA reduces the size of low-rank matrices. However, these parameter offsets are not reflected in the results, which could be misleading to the audiences. It would be more informative to add the actual model size (or estimated) in MB/GB for each of the models. Specifically, the size of the scaling factors introduced by group-wise quantization should be explicitly stated, as these are not negligible and contribute to the overall memory footprint. Furthermore, the reduction in the low-rank matrix size should be quantified in terms of the number of parameters, not just qualitatively. The current presentation makes it difficult to assess the true memory savings and computational overhead of the proposed method.
* In the ablation study, only group size is examined. It would be worthwhile to experiment with the D_int as well, as it is also part of the tradeoff between model size and accuracy. It would be interesting to see what is the lowest D_int in this setup, compared to vanilla LoRA. The impact of varying D_int on both model size and performance should be thoroughly investigated. A smaller D_int might lead to a more compact model but could also result in a significant drop in accuracy. It's crucial to understand this trade-off to determine the optimal configuration for different use cases. The current ablation study is incomplete without this analysis.

### Questions
See those in weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
