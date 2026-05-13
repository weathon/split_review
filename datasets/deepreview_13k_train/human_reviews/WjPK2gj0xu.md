# Multi-modality Expansion and Retention for LLMs through Parameter Merging and Decoupling

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Extensive fine-tuning of the synthesis between multimodal encoders and Large Language Models (LLMs) on modality-specific data can expand the modalities that LLM can handle, leading to the formation of Multimodal Large Language Models (MLLMs).
However, this paradigm to expanding modalities heavily relies on initiating fine-tuning from scratch with new multimodal data, which is both resource-intensive and inflexible. 
In this paper, we propose $\textit{MMER (Multi-modality Expansion and Retention)}$, a novel $\textit{training-free}$ approach that reuses and composes existing MLLMs to facilitate effective multimodal expansion while retaining the original performance of each MLLM. 
In particular, MMER maintains the multimodal encoders of the MLLMs while merging their LLM parameters.
By comparing the original LLM parameters with the merged ones, MMER can create binary masks that enable an approximate separation of the LLM parameters for each modality.
This process allows the decoupled parameters to independently process modality-specific inputs, thereby reducing parameter conflicts and maintaining the fidelity of the original MLLMs.
Additionally, MMER integrates strategies to prevent catastrophic forgetting by employing a similar approach to separately decouple the parameters fine-tuned on new tasks from the original parameters. 
Experiments on three multimodal tasks and fourteen dual-modal tasks show significant improvements over recent baselines, demonstrating that MMER can effectively expand multimodal capabilities of LLMs while retaining 99.6\% of the original performance. 
Further experiments in both single-task and cross modalities multi-task scenarios reveal that MMER significantly mitigates catastrophic forgetting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a training-free parameter-merge framework, called MMER, for MLLMs. This method compresses key parameter differences between each MLLM and original LLM into a merged task vector and a multimodal mask. When addressing tasks involving multimodal expansion and retention, MMER restores the parameters specific to the required modality using the task vector and mask, making the merged model approximate the corresponding MLLM. Extensive experiments demonstrate MMER’s effectiveness across various benchmarks and its capability to mitigate catastrophic forgetting.

### Strengths
1. The paper offers several clear illustrations that is greatly helpful in understanding the mechanisms of parameter merging, expansion, and retention.
2. By decoupling the merged task vector and mask, the model can utilize parameters approximating to specific modality to process corresponding modality inputs, which sounds make sense.
3. This method merges the newly fine-tuned MLLM as an additional task vector, while maintaining performance on the original task.

### Weaknesses
For audio modality, the merged model only selects 2.2% parameters from merged task vector (Figure 4a), which indicates the majority of key parameters in the audio MLLM deviate from the direction of the original LLM according to the merging mechanism. However, the merged model (98% parameter from original LLM + 2% parameter from merged task vector activated by audio mask) achieves 1.5x improvement compared to original audio MLLMs, which is confused. 

The author attributes this result to the redundant parameters in the audio model, consistent with the observations in [1]. However, even in [1], as more parameters are dropped, performance declines rather than an exaggerated 1.5x improvement. Considering that 2% of the parameters are not from the original audio MLLM, I wonder if that 2% of the parameters overlap with other modalities (such as video), thus providing more prior knowledge?

### Questions
According to the merging mechanism, merged task vector retains the parameters of target MLLM that are consistent with those of original LLM in direction. As more modalities are merged, the merged task vector will also accumulate key parameters from other modalities. Will the parameters of a single modality correlate to the final merged task vector? Will this correlation weaken with the introduction of more MLLMs, leading to the failure of the merging mechanism? In the merged task vector, what is the parameter overlap like across different modalities?

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
3

### Summary
The paper proposes a training-free approach, MMER, to enhance the multimodal capabilities of LLMs without extensive fine-tuning. To process different modalities, MMER maintains the vision encoder and introduces binary masks on the LLM parameters for each modality, facilitating modality-specific input processing and reducing parameter conflicts. Additionally, MMER incorporates a similar method to mitigate catastrophic forgetting by decoupling parameters fine-tuned on new tasks from the original parameters. The experimental results on multimodal and dual-modal tasks indicate that MMER achieves notable improvements over recent baselines, demonstrating its potential effectiveness.

### Strengths
- MMER’s training-free approach makes it practical and resource-efficient, avoiding the computational costs of extensive fine-tuning.
- The method effectively retains the original performance of merged models, mitigating catastrophic forgetting and preserving their capabilities.
- MMER demonstrates versatility, applicable to various modalities, and maintains performance across diverse multimodal tasks.
- The paper includes extensive experiments that show consistent performance improvements over baseline methods, validating MMER’s robustness.

### Weaknesses
 - The paper could better explain the advantages of MMER over existing modular approaches and provide a clearer justification for adopting this monolithic method.
- While the paper demonstrates effectiveness, it lacks comparisons with certain mainstream MLLMs and does not evaluate larger-scale models. Including these aspects would strengthen the argument for MMER’s superiority and provide insights into its performance at scale.

### Questions
Refer to the weakness.

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
- The paper proposes MMER (Multi-modality Expansion and Retention), a novel training-free approach that reuses and composes existing MLLMs to facilitate effective multimodal expansion while retaining the original performance of each MLL
- Extensive and rigorous experiments on various multimodal benchmarks have been conducted to validate the effectiveness and robustness of MMER.

### Strengths
- The paper proposes a training-free MMER approach that enables seamless multimodal expansion for LLMs through multimodal parameter merging and decoupling.
- The paper also leverages MMER for mitigating catastrophic forgetting in MLLMs, demonstrating its potential for continual learning applications.
- Extensive experiments have been performed to demonstrate the effectiveness of MMER on multi-modality expansion,  multi-modality retention and mitigating catastrophic forgetting.

### Weaknesses
 - In terms of mitigating catastrophic forgetting, although MMER demonstrates good performance, considering the amount of storage required for MMER, it is unclear how this improvement compares to simply tuning task-specific adapters for new tasks.
- The paper mentioned that the hyper-parameters, such as $\alpha$ and $\lambda$, are selected based on the validation set. However, the construction of this validation set is not well-detailed, making it hard to tell how well these hyper-parameters can generalize to different tasks.
- The paper does not provide sufficient theoretical grounding for the proposed method, lacking analysis or reference on key aspects such as the relationship between model parameter differences and corresponding performance differences, the measurement of modality interference, or positive transfer between difference modality-specific LLMs.

### Questions
- In Equation 2, what is the rationale for using the Manhattan distance to minimize the distance between the reconstructed model parameters and the original LLM parameters?
- What will be the suggested way to quantify the difference between the original MLLM and its approximate version reconstructed by MMER? Furthermore, is there a relationship between this measured difference and the performance discrepancy?

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
3

### Summary
This paper introduces a novel training-free approach called MMER (Multi-modality Expansion and Retention). The approach aims to expand the capabilities of Large Language Models (LLMs) to handle multimodal data while retaining their original performance on specific modalities.
MMER merges LLM parameters from multiple MLLMs while constructing binary masks to decouple modality-specific parameters. This allows for independent processing of modality-specific inputs and reduces interference.

### Strengths
The paper introduces a new parameter decoupling strategy that effectively separates modality-specific parameters, reducing interference and enhancing performance.

The authors have clearly articulated the problem, the proposed solution, and the advantages of MMER over existing methods. 

The paper is clear and well-organized, making it easy for readers to follow the authors' line of reasoning.

### Weaknesses
In general, cross-modal tasks exhibit diversity, and the paper reports performance on only one cross-modal task for each modality combination, such as MUSIC-AVQA and MCUB. This makes the validation of the proposed method's effectiveness insufficiently comprehensive.

Lack of the performance of the unimodal model on the tri-modality task for a fairer comparison.

The author decouples modalities using addition and subtraction; however, models are typically nonlinear, which confuses me. The paper also lacks sufficient proof for this approach. Additionally, the justification for using Manhattan distance when calculating the mask is not strong enough.

### Questions
Can the author clarify how many parameters are decoupled for each modality?

I hope the author can provide a more detailed explanation and proof of the proposed method. I will consider changing my perspective if the author's response is valuable.

### Soundness
3

### Presentation
3

### Contribution
2
