- Decision: Accept
- Scores: 6, 6, 6, 8

## Merged Review

### Summary
The paper proposes SaLoRA, a method to preserve safety alignment during low-rank adaptation of LLMs by combining a fixed safety module (computed from harmful prompts) with task-specific initialization of trainable parameters. Experiments demonstrate that SaLoRA retains safety better than existing adapter-based methods while maintaining downstream task performance. One reviewer (score 8) was particularly positive, praising the careful experimental design and root-cause analysis, while the other three (score 6) found the work good but noted several limitations regarding evaluation breadth, theoretical depth, and missing analysis details.

### Strengths
- Well-motivated and addresses a critical, practical issue in PEFT (safety alignment degradation) (R1, R3, R4).
- The novel use of a fixed safety module combined with task-specific initialization is a clean, effective solution (R1, R2, R3).
- Empirical results are comprehensive and convincing across diverse LLMs (Llama-2-chat, Llama-3.1-Instruct, Mistral) and safety benchmarks (AdvBench, jailbreak attacks), with consistent safety improvement without sacrificing task performance (R1, R2, R3). Reviewer 4 notes the experimental design is carefully chosen and supports the theoretical argumentation well.
- The paper is clear, well-structured, and accessible, with helpful architecture diagrams (R2, R3, R4).
- Provides insights into potential root causes for increased sensitivity of low-rank adapters to toxic language (R4).
- Significant for safe deployment of LLMs in specialized applications (R2).

### Weaknesses
- **Limited hyperparameter and ablation analysis**: No systematic study of how the size and quality of the harmful prompts dataset affect SaLoRA’s performance (R1). No comparison of the proposed task-specific initialization against alternative standard initialization strategies (R1). The correlation between harmful rate and PEFT rank or model size is not analyzed; e.g., why does Llama-3.1-Instruct-8B have a higher baseline harmful rate (14%) than Llama-2-chat, yet SaLoRA reduces it more dramatically? (R2). Performance degradation with increasing/decreasing fine-tuning dataset size is not explored (R3).
- **Insufficient theoretical justification**: The theoretical analysis is presented but the derivations and assumptions are sometimes implicit; a clearer explanation of *why* SaLoRA outperforms existing approaches is needed (R1, R3). The claim of “feature difference” measurement (L.193) lacks details on how it is computed and what empirical results look like; the significant accuracy changes in Figure 3 require explanation (e.g., is the base model already aligned causing this?) (R4).
- **Narrow evaluation scope**: Mainly tested on AdvBench and jailbreak attacks; missing comparisons on broader safety benchmarks such as RealToxicityPrompts, factual accuracy, adversarial Q/A, and hate/abuse/profanity (HAP) filters (e.g., Granite Guardian) (R1, R4). No analysis of specific types of harmful responses (e.g., hate speech, misinformation) produced by LoRA-fine-tuned models, only a single “harmful case” in Figure 1 (R2). It is unclear whether SaLoRA is effective across all prompt/task types or has limitations in certain scenarios (R3).
- **Missing implementation and methodological details**: The Linear Probing Accuracy calculation is not explained – how the linear probe is trained (features used, loss function, optimization algorithm, whether trained on the same data as fine-tuning) (R2). The paper does not provide open-source code (R2).
- **Computational overhead comparison is brief**: A more detailed analysis of SaLoRA’s computational efficiency (e.g., training time, memory, inference cost) compared to other safety alignment approaches is needed, especially when scaling to larger models or datasets (R3).
- **Lack of ablation on evaluation metric**: The harmful rate relies solely on Llama-Guard-3-8B; an ablation using other classifiers (e.g., perplexity-based or human evaluation) would strengthen the results (R2).
- **Missing discussion of limitations**: The paper should explicitly discuss scenarios where SaLoRA may be less effective (R3).