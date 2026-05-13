# PB-LLM: Partially Binarized Large Language Models

- Decision: Accept
- Scores: 8, 5, 6, 8

## Abstract
This paper explores network binarization, a radical form of quantization, compressing model weights to a single bit, specifically for Large Language Models (LLMs) compression. 
Due to previous binarization methods collapsing LLMs, we propose a novel approach, Partially-Binarized LLM (\pbllm), which can achieve extreme low-bit quantization while maintaining the linguistic reasoning capacity of quantized LLMs. 
Specifically, our exploration first uncovers the ineffectiveness of naïve applications of existing binarization algorithms and highlights the imperative role of salient weights in achieving low-bit quantization. 
Thus, \pbllm~filters a small ratio of salient weights during binarization, allocating them to higher-bit storage, \ie partially-binarization. 
\pbllm~is extended to recover the capacities of quantized LMMs, by analyzing from the perspective of post-training quantization (PTQ) and quantization-aware training (QAT). 
Under PTQ, combining the concepts from GPTQ, we reconstruct the binarized weight matrix guided by the Hessian matrix and successfully recover the reasoning capacity of \pbllm~in low-bit. 
Under QAT, we freeze the salient weights during training, explore the derivation of optimal scaling factors crucial for minimizing the quantization error, and propose a scaling mechanism based on this derived scaling strategy for residual binarized weights. 
Those explorations and the developed methodologies significantly contribute to rejuvenating the performance of low-bit quantized LLMs and present substantial advancements in the field of network binarization for LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper examines the application of network binarization to compress Large Language Models (LLMs), an approach that reduces model weights to a single bit. The authors have developed methodologies that significantly improve the performance of binarized LLMs, thereby contributing valuable insights to the field of LLM compression through network binarization.

### Strengths
1. Compressing LLMs is an important question for today’s AI research, and the authors first introduce binarization into LLM compression pushing the quantized LLM into ultra-low bits. 
2. The authors present a thorough exploration of network binarization techniques. They effectively demonstrate the feasibility and potential of partially-binarized LLMs using post-training quantization and quantization-aware training methodologies.
3. The inclusion of source code with the submission is commendable, enabling reproducibility and verification of the reported results, which are impressive.

### Weaknesses
1. While the incorporation of Quantization-Aware Training (QAT) in LLM compression is an interesting proposal, its practicality is uncertain given the substantial costs associated with training LLMs. Could the authors elaborate on the overhead implications of QAT for LLMs, specifically detailing the computational resources (e.g., number of GPUs, training time) and energy consumption required for their approach compared to standard training or other quantization methods?

2. In regards to Table 2, it is unclear whether GPTQ-PB represents the method proposed by the authors. Could you clarify the distinction between GPTQ-PB and PB-LLM within the context of your study, detailing the specific algorithmic differences and implementation choices that differentiate these two approaches? A more detailed explanation of how each method is applied to the partially-binarized weight matrix would be beneficial.

3. The application of optimal scaling techniques appears to be confined to the specific case presented. Could these techniques be generalized to other bit configurations, and if so, how might this affect the compression performance? Specifically, how would the optimal scaling parameters be determined for different bit-widths, and what is the expected trade-off between compression ratio and model accuracy when varying the number of bits used for the salient weights?

### Questions
See weaknesses

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a methodology termed PB-LLM for the partially weight-only binary quantization for Large Language Models (LLMs). Particularly, it outlines the limitations encountered when applying previous BNN works to LLMs, while proposing new methods from Post Training Quantization (PTQ) and Quantization Aware Training (QAT) for LLM low-bit weight quantization. Within PTQ, the paper utilizes Hessian information to identify element-wise salient weights, upon which 8-bit quantization is applied to preserve reasoning capacity in a pre-trained LLM, while binary (1-bit) quantization is applied to the un-salient weights. After applying mixed-quantization, it employs GPTQ to un-salient weights for further optimization (termed as GPTQ-PB). In QAT, the paper applies QAT during the LLM fine-tuning stage, utilizing 1) optimal scaling factor and 2) salient weight freezing methodology to bring about an efficient yet higher-performing QAT methodology (termed as PB-LLM). The methodologies studied and proposed in this work provide insightful contributions to the field of LLM binarization, showcasing the potential for further advancements in LLM binarization.

### Strengths
- The paper provides a well-structured presentation of the preliminaries of binary quantization to the introduction of the proposed method, which made it easy to follow.

- Building on previous research such as AWQ and SparseGPT, this paper proposes a partial binarization technique through salient weight protection based on the hessian information and effectively demonstrates its efficacy in PTQ with ablation study (as shown in Table 1).

- The paper showcases empirical improvements in QAT optimization (higher accuracy with fewer training steps than LLM-QAT) across the CSQA tasks.

### Weaknesses
Major Concerns
- Lack of novelty: The authors propose the optimal scaling factor as their primary contribution, but the core idea itself seems to have already been proposed in the previous work. For example, [R1] proposed an optimal ternary function (eq. (3) of [R1]), but it can be trivially reduced to the binary function when the threshold is zero; then the equation seems to be identical to the equation (8) and (9) proposed in this paper.

[R1] Li te tal., Ternary Weight Networks


- Lack of Evaluation Task: This paper evaluates the reasoning capability of LLM only through the accuracy of the CSQA task. In the CSQA task, tasks such as OBQA and ARC challenge were used for OPT-1.3B, where the FP performance did not reach even the random baseline (25%). It raises questions about the suitability of these tasks for demonstrating the effectiveness of fine-tuning, and, hence, the superiority of PB-LLM. To show the effects of fine-tuning more clearly, it would be advisable to carefully select reasoning tasks that are appropriate for the model capacity. Reporting performance not just on CSQA, but also on multi-task accuracy like MMLU would be also beneficial for highlighting PB-LLM's efficacy.

- Inconsistent Salient Weight Methodology between PTQ and QAT: The absence of a consistent methodology for salient weight protection between PTQ and QAT is concerning. While the effectiveness of using Hessian criteria for identifying salient weights in PTQ is demonstrated through performance comparisons, the rationale for using magnitude criteria to identify salient weights in QAT seems to be missing. Understanding the disparity in the approach to salient weight protection across PTQ and QAT is crucial for a holistic appreciation of the proposed method.

- Insufficient evidence on PB-LLM efficiency: To claim that PB-LLM is more efficient in terms of training iteration number compared to LLM-QAT, a more thorough comparison seems necessary. Specifically, it needs to be clear whether the LLM-QAT, being compared with PB-LLM, has been fine-tuned on the same dataset as PB-LLM. Detailed experimental setup information regarding the LLM-QAT is required. Moreover, verification is needed on whether the results through PB-LLM QAT have fully enhanced the reasoning capacity of the pre-trained model. Essentially, it appears that the reasoning accuracy of the target model (OPT-1.3B) obtained through FP fine-tuning should be presented as the upper bound in Figure 7. Additionally, there seems to be a lack of information in Table 2 regarding whether FP LLaMA-7B performance is pre-trained or fine-tuned.


Minor Concerns
- Typo: Sec 3.3 bianrize -> binarize
- Consistent notation should be used in Sec 4.1 -> LLaMA, LLaMa -> LLaMA
- There may be an incorrect reference link in Sec 4.1, "showing its fast convergence property (refer to 3.2)" Should it possibly be corrected to "refer to 3.4?"
- There are spacing issues in the Figure 7 caption, "LLMin" should be "LLM in" and "PM-LLMtriumphs" should be "PB-LLM triumphs".

### Questions
1. What is the rationale behind utilizing a Hessian-based approach to identify salient weights in PTQ, while employing a magnitude-based approach to identify salient weights in QAT?

2. Is there a specific reason why only the PB methodology and GPTQ were applied in PTQ? I am curious about the performance of AWQ-PB in comparison.

3. Is there a plan to compare the task-specific fine-tuning in QAT with the 2-bit QAT-KD methodology (QuantGPT [R2], TSLD [R3])?

4. The optimal scaling factor and salient weight freezing seem to primarily aim at reducing harsh quantization errors before QAT. Is there insight into how these methods improve the QAT training process as depicted in Figure 5?

[R2] Tao et al, " Compression of Generative Pre-trained Language Models via Quantization" ACL 2022.  
[R3] Kim et al, "Token-scaled logit distillation for ternary weight generative language models" NeurIPS 2023

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Partially-Binarized LLM (PB-LLM), which leverages a PB mechanism to binarize LLMs for more efficient GPU memory usage. The main motivation behind PB is the recognition that a fraction of 'salient weights' exists within the LLM weights, which are essential and restrict full binarization. PB-LLM preserves the precision of these salient weights while focusing on binarizing the non-salient weights. The paper also investigates the integration of PB-LLM with post-training quantization and quantization-aware training schemes and establishes a connection between PB-LLM and GPTQ. Experimental results are presented to demonstrate the effectiveness of PB-LLM.

### Strengths
- The paper is well-written and well-motivated.
- The proposed PB-LLM scheme is easy to follow and straightforward to understand.
- Exploring to improve the memory and/or storage efficiency using quantization (and algorithmic approximation in general) of LLMs is a promising research direction.

### Weaknesses
 - Only Llama 7B is studied as the LLM for PB-LLM and all other baselines. Thus, it's not clear how the PB-LLM method performs on larger-scale models. Specifically, the paper lacks an analysis of how the percentage of salient weights impacts performance across different model sizes. It's possible that the optimal percentage of salient weights varies significantly with model scale, and this needs to be investigated to establish the generalizability of the approach.
- Only pre-trained base models are experimented with those models, however, are usually not deployed directly as applications. The paper does not evaluate the performance of PB-LLM on fine-tuned models, which are more commonly used in practical applications. This limits the practical relevance of the study, as the binarization scheme's impact on fine-tuned models could be different from that on pre-trained models.
- The LLM quantization scheme is motivated using an angle of GPU memory efficiency. However, the actual GPU memory usage before and after binarization/quantization is not studied in this paper. The paper does not provide concrete data on the actual memory savings achieved by the proposed method, which is crucial for justifying the approach's practical utility. The absence of such data makes it difficult to assess the real-world impact of PB-LLM on GPU memory efficiency.

### Questions
- How does PB-LLM's performance vary among various sizes of Llama models, e.g., 7B-65B?
- How does PB-LLM perform for aligned/instruction fine-tuned models, e.g., Alpaca and/or Vicuna? To what extent will the binarization scheme affect the model's performance say on the Hugging Face leaderboard [1]?
- What is the actual GPU memory saving look like for PB-LLM and all considered baselines?

[1] https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces PB-LLM, an extreme quantization method that partially binarizes model parameters based on their relevance to linguistic reasoning tasks. PB-LLM selectively identifies and designates a small fraction of salient weights for binarization, assigning them to higher-bit storage, and essentially implementing partial binarization. PB-LLM is extended to recover quantized LMMs' capabilities through post-training quantization (PTQ) and quantization-aware training (QAT). In PTQ, the Hessian matrix guides the reconstruction of binarized weights to restore reasoning capacity at low bits. In QAT, we freeze salient weights during training, derive optimal scaling factors to minimize quantization errors and propose a scaling mechanism for enhanced residual binarized weights. The result shows that PB-LLM achieves competitive results without losing performance gain.

### Strengths
+ Presents a practical approach that analytically identifies non-salient weights and applies binarization selectively for large models.
+ Achieves LLM binarization without sacrificing performance gains.

### Weaknesses
 - The proposed approach section is comprehensive, but its complexity makes it challenging to navigate and comprehend throughout the entire section.
- The analysis of evaluation is limited to a single task. It would be valuable to explore the potential limitations of PB-LLM in achieving comparable performance across various tasks.

### Questions
1. The readability of the paper can be improved by including a flowchart or block diagram of the proposed method by illustrating different stages of transforming a PB-LLM model. 
2. The paper reports primarily the accuracy to evaluate the proposed approach. The addition of the final model size after partial binarization can further solidify the claim.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
