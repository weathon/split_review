# Low Rank Quantization Adaptation for Large Language Model

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
As the parameters of Large Language Models (LLMs) increase, quantization has emerged as a potent strategy for model compression and acceleration. Concurrently, Low-Rank Adaptation (LoRA) has been recognized as an effective method for enhancing LLM performance. However, integrating LoRA with quantization presents significant challenges, particularly in preserving the quantization format after model optimization. In this paper, we introduce Low rank Quantization Adaptation (LoQA) for LLM, a novel approach that effectively fine-tunes holistic quantization parameters. Specifically, we first propose a new perspective of quantization operator, which is compatiable with LoRA and mathematically equivalent to the original operator. In this way, all the parameters (scale and zero point) are finetuned simultaneously, and thus yields notable improvements in model performance.Thanks to the expanded optimization landscape, LoQA is broadly applicabile to various Post-Training Quantization (PTQ) techniques, ensuring better generalizability in practical deployments. To maintain the stability of the optimization, we further propose a LoRA scaling strategy that leverages quantization data to adjust the norm of the low rank adaptation, regulating the speed of convergence in optimization and preventing inappropriate LoRA scaling, which could lead to overfitting or underfitting. Compared to existing methods, LoQA consistently achieves performance gains across a wide range of models, proving its effectiveness and adaptability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends the QA-LoRA method by introducing Low-Rank Quantization Adaptation (LoQA) to enhance the fine-tuning of large language models (LLMs) within a quantized framework. LoQA addresses the integration challenges between quantization and Low-Rank Adaptation (LoRA), proposing Holistic Quantization Low-Rank Adaptation (HQ-LoRA), a quantization-compatible adaptation technique that allows finetuning of all quantization parameters (including scale and zero points) resulting in improved model performance. Additionally, the paper introduces Quantized Bit-aware scaling (QBAS), which adjusts LoRA scaling to account for the impact of integer weights at varying bit-widths. Overall, LoQA extends the QA-LoRA paper by modifying not only the quantization zero points (as in QA-LoRA) but also the quantization scale.

### Strengths
Strengths:

-Considering the quantization scaling as well during finetuning gives much more representation power compared to earlier approaches like QA-LoRA, which focus only on quantization zero points. Also, as demonstrated by empirical results, it usually results in better generalization across diverse set of models and bit budgets.

-LoQA especially outperforms previous methods on low-bit budgets, which would make it useful for ultra resource-efficient settings.

-In the 4bit regime, LoQA seems to perform competitively to algorithms like IR-QLoRA that use a mix of 4/16 in their inference deployment

-Given that it doesn’t carry 16bit LoRA parameters to the inference phase (as opposed to methods like QLoRA), it would bring considerable inference efficiency compared to "4+16" type of methods.

### Weaknesses
In general, this method is interesting - however, in terms of novelty,  this work is indeed an incremental work on top of the QA-LoRA work. Moreover, this paper could benefit from improvements in the presentation and description of the experiments.

Weaknesses:

-The paper presentation could be improved, especially in the experiment section. Implementation details are underspecified in many parts. Given that this research effort is based on empirical results, this lack of experimental setting would make it hard to reproduce the results for the community.

-For experiments comparing LoQA with QA-LoRA (as well as other similar methods), the corresponding ranks of the methods are not reported in most cases, which makes the reader question if the improvement could be due to using more parameters by LoQA or not.

-There’s lot of focus on MMLU evaluation after finetuning on alpaca/Flan datasets, which might not be representative of how this algorithm would actually work for other type of tasks/datasets. The only exception, Table 5, focuses on commonsense reasoning, which the performance is very close to QA-LoRA, while it uses half of your training complexity by having a single set of LoRA parameters for zero points.

-Table captions in many cases are not "self contained" and often have a very general caption, which make it hard to go through different tables and understand the results.

### Questions
-Regarding QBAS: the scaling that you proposed is then being multiplied by a hyperparameter. Are you using the same $alpha$ across different bits?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Low-Rank Quantization Adaptation, called LoQA, a new approach for fine-tuning large language models (LLMs) while preserving quantization. LoQA consists of two techniques: (1) Holistic Quantization Low-Rank Adaptation (HQ-LoRA): This approach fine-tunes all quantized parameters, enabling broader optimization without losing the quantized model structure. (2) Quantized Bit-Aware Scaling (QBAS): This technique dynamically adjusts scaling factors based on bit-widths, enhancing performance stability across various quantization levels. LoQA is tested against state-of-the-art quantization methods and is effective across different model sizes and bit configurations. It yields significant improvements, particularly under ultra-low bit-width scenarios.

### Strengths
+ LoQA introduces a novel quantization-aware fine-tuning method that can support quantized LLMs to effectively balance model compression with performance.
+ Experiments show that LoQA consistently outperforms previous methods in accuracy and efficiency, even in ultra-low bit-width configurations.
+ The method supports multiple bit-widths and integrates smoothly with existing post-training quantization methods, making it adaptable to a wide range of applications.
+ LoQA is evaluated using the MMLU and common sense QA tasks, with consistent results.

### Weaknesses
 - LoQA requires more training time and memory compared to some baseline methods, which may hinder its practicality in resource-constrained environments.
- The study did not use the latest datasets or the newest training paradigms, which might limit the generalizability of the results to other, more current LLMs.
- Implementing LoQA in production may involve significant effort due to the complexity of fine-tuning across various bit-widths, which could add deployment challenges.

### Questions
Would you please describe how LoQA could be implemented in production?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to enable efficient LLM fine-tuning by combining quantization with LoRA. Rather than keeping LoRA inference in FP/BF16 during the forward pass, it proposes a holistic quantized LoRA approach where LoRA is fused into the quantization set to enable fully quantized inference. Additionally, the paper introduces a method to determine the LoRA scaling factor based on the target bit precision.

The proposed method achieves higher fine-tuning performance and training efficiency compared to QLoRA and QA-LoRA at 4/3/2-bit precision.

### Strengths
- The related work and motivation are clearly presented, making the problem the paper addresses easy to understand.
- The holistic quantized LoRA approach follows a similar direction to QA-LoRA, aiming to achieve fully quantized inference by fusing LoRA. The paper introduces a way to learn both the scaling and zero-point parameters, which adds flexibility to the method.

### Weaknesses
 - The holistic quantization method formulation is somewhat difficult to follow. Figure 2 is overly simplified, and would benefit from revision to visually clarify the equations in Section 3.2.
- Experiments are limited to the LLaMA family, and there is a lack of results on LLaMA-3. If dataset is an issue, it may be preferable to use more recent open-source datasets (e.g., SlimPajama) instead of the relatively old and small sample Alpaca dataset. Alternatively, comparing performance on domain-specific fine-tuning tasks (e.g., GSM8K, OASST1) as done in LoftQ/LQ-LoRA could provide additional insights.
- The main contribution of this paper appears to be preserving the quantization set in inference. However, the proposed method lacks significant innovation compared to QA-LoRA, and there is no report on the actual efficiency gains achieved during fully quantized inference. Section 4.3 only briefly mentions the potential for kernel optimizations, which seems insufficient given that fullly quantized inference is the main focus of this paper.

In summary, while the proposed method consistently outperforms QA-LoRA and addresses an important problem, the limited experimental results and unclear explanations of key methods indicate room for improvement.



### Questions
- In Section 3.2, the proposed method is still not entirely clear. On Line 249, what exactly do you mean by “two LoRA variants”?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel quantization-aware, parameter-efficient tuning method for large language models (LLMs) based on QA-LoRA. The approach reparameterizes both scaling and zero factors to mitigate quantization errors. Experimental results demonstrate its effectiveness.

### Strengths
1. Deployment is a crucial consideration for large language models (LLMs), with quantization-aware training being one of the key challenges in their deployment.

2. The proposed method is simple yet promising, as indicated by the experimental results.

### Weaknesses
1. While I understand the core idea the author aims to convey, I believe the writing could be improved by providing a more general analysis of approaches to quantization-aware (QA) training or reparameterization of quantization parameters. This would be more important to the community and the contributions will be more important.
2. The contributions appear to be incremental.
3. Figure 2 could be enhanced: it currently labels the LoRA parameters 𝐴 and 𝐵 for QLoRA, but lacks annotations for QA-LoRA and the proposed method. Additionally, the concept of Holistic LoRA is not clearly conveyed.
4. This method seems have limitations which only support group-wise quantization.

### Questions
1. Any inference time results?
2. other questions please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Low Rank Quantization Adaptation (LoQA) for LLMs, a novel parameter-efficient fine-tuning method for quantized models. LoQA aims to reduce memory consumption across model weights, gradients, and optimizer parameters. It includes two core modules: **HQ-LoRA** (Holistic Quantization Low-Rank Adaptation) and **QBAS** (Quantized Bit-Aware Scaling), aligning quantization parameter granularity with LoRA parameters in group quantization.

### Strengths
- The proposed method is well-motivated and sounded.
- This approach is straightforward yet effective, especially in ultra-low bit-width scenarios.
- Code is provided for reproducibility.

### Weaknesses
 - **Limited novelty**: The method’s innovation is incremental, building on QA-LoRA and closely resembling group quantization applied to LoRA parameters. In Sec 3.2, LoQA uses two LoRA components, whereas QA-LoRA requires only one, which may lead to a higher parameter count.
- **Experimental limitations**:
  - LoQA does not demonstrate clear improvements on LLaMA 2, and for LLaMA 3, only training loss rather than performance results is presented. Providing promising results on more advanced models would strengthen the paper’s contribution. The lack of clear performance gains on LLaMA 2 is concerning, as it suggests the method may not be robust across different model architectures. Furthermore, presenting only training loss for LLaMA 3 is insufficient to validate the method's effectiveness; validation or test set performance is crucial to demonstrate generalization.
  - Important baselines, such as **IR-QLoRA** and **QLoRA**, are absent in Tables 5,7,9, affecting comparison fairness. The absence of these key baselines makes it difficult to assess the true performance of LoQA relative to existing state-of-the-art methods. A comprehensive comparison should include these baselines to ensure a fair evaluation.
  - While the authors claim broad applicability of LoQA across post-training quantization techniques, only **GPTQ** settings are evaluated. Evaluating only GPTQ limits the scope of the paper's claims. The method's performance should be demonstrated across a wider range of post-training quantization techniques to validate its broad applicability.
- **Poor presentation and writing**:
  - Figure 2 lacks clarity in distinguishing between QA-LoRA and LoQA. The visual differences between QA-LoRA and LoQA in Figure 2 are not sufficiently clear, making it difficult to understand the architectural nuances of the proposed method. The figure needs to be revised to provide a clearer distinction.
  - In Sec 3.3, the rationale for setting $maxq$ to $2^{N-1}$ is not sufficiently analyzed. The choice of setting $maxq$ to $2^{N-1}$ lacks sufficient justification. A more detailed analysis of the impact of this parameter on the quantization process is needed.
  - In some tables (e.g., Tables 4, 7, 8), entries are missing bold formatting to indicate the best results. The lack of consistent bold formatting for best results in tables makes it harder to quickly identify the superior performing methods.
  - The LoRA rank used in the compared methods is not clearly specified. The LoRA rank used in the compared methods should be explicitly stated to ensure reproducibility and fair comparison.
  - The "4+16 bit" setting is not formally defined. The "4+16 bit" setting is not clearly defined, leading to potential confusion about the precision of different components of the model.
  - "Llama-7b" and "Llama-7B" are inconsistently referenced throughout the paper. The inconsistent use of "Llama-7b" and "Llama-7B" throughout the paper introduces unnecessary ambiguity and should be standardized.
  - "Post-fine-tuning" in line 269 is incomplete. The phrase "Post-fine-tuning" in line 269 is incomplete and lacks the necessary context to understand the process being described.

### Questions
Please refer to the Weaknesses above for questions.

### Soundness
3

### Presentation
2

### Contribution
2
