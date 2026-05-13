# LoRA-FA: Memory-efficient Low-rank Adaptation for Large Language Models Fine-tuning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
The low-rank adaptation (LoRA) method can largely reduce the amount of trainable parameters for fine-tuning large language models (LLMs), however, it still requires expensive activation memory to update low-rank weights. Reducing the number of LoRA layers or using activation recomputation could harm the fine-tuning performance or increase the computational overhead. In this work, we present LoRA-FA, a memory-efficient fine-tuning method that reduces the activation memory without performance degradation and expensive recomputation. LoRA-FA chooses to freeze the projection-down weight of $A$ and update the projection-up weight of $B$ in each LoRA layer. It ensures the change of model weight reside in a low-rank space during LLMs fine-tuning, while eliminating the requirement to store full-rank input activations. We conduct extensive experiments across multiple model types (RoBERTa, T5, LLaMA) and model scales. Our results show that LoRA-FA can always achieve close fine-tuning accuracy across different tasks compared to full parameter fine-tuning and LoRA. Furthermore, LoRA-FA can reduce the overall memory cost by up to 1.4$\times$ compared to LoRA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents LoRA-FA, a new parameter-efficient fine-tuning (PEFT) approach for Large Language Models (LLMs). LoRA-FA is an extension of the LoRA method which minimizes memory usage by freezing the A matrix in LoRA layers. This approach alleviates the need to store the input activation of the LoRA layer, leading to a reduction in memory footprint during fine-tuning. The authors provide comprehensive experimental evidence showcasing the efficacy of LoRA-FA across various LLMs including RoBERTa, T5, and LLaMA. The results demonstrate LoRA-FA's memory savings without compromising on fine-tuning performance.

### Strengths
* The proposed LoRA-FA method cuts down GPU memory usage by reducing both the number of trainable parameters and the activation memory compared to traditional full fine-tuning.
* Comprehensive experimental results on diverse models, including RoBERTa, T5, and LLaMA, demonstrate that LoRA-FA maintains competitive accuracy relative to both full fine-tuning and the original LoRA.
* The paper lucidly presents the background of parameter-efficient fine-tuning and proposes an expanded method that inherits the advantages of the previous work, LoRA.

### Weaknesses
 * The proposed method, which involves freezing the LoRA weight A from the existing LoRA, appears incremental in terms of novelty.
* In the context of "reducing the number of trainable parameters", as mentioned in the LoRA paper, the previously proposed PEFT method significantly reduced the number of trainable parameters. This led to a drastic reduction in the memory usage of the optimizer state, bringing it down to megabytes. Thus, using fewer trainable parameters than LoRA does not yield a significant difference. The paper does not adequately address the optimizer state memory, which is a critical component of overall memory usage.
* Regarding "reducing the activation memory", while LLaMA uses a max sequence length of 2k, the LLaMA2 model employs a 4k length. It's evident that models are gravitating towards longer sequence lengths. As per Table 1, LoRA-FA utilizes '2bsr' of memory (compared to LoRA's '2bsd+2bsr'), but the advantage in memory savings during training becomes less pronounced as the model's sequence length increases relative to LoRA. The analysis fails to consider the scaling of memory savings with respect to sequence length, and the potential diminishing returns for longer sequences.
* The proposed methodology primarily targets the reduction of memory usage during training. In section 4.2, Table 5, the variance in memory peak between LoRA and LoRA-FA is minimal, especially for generative models like LLaMA-7B. This raises concerns about the practical significance of the memory savings, particularly for larger models where the absolute memory difference is small.
* As stated in the LoRA paper, amplifying the trainable parameters doesn't notably affect accuracy (refer to Figure 2). For a more precise evaluation, I suggest the following comparative experiments with LoRA:
    * Match LoRA and LoRA-FA at the same level of trainable parameters and then compare their accuracy and memory peaks. The paper does not explore the trade-offs between parameter count and performance.
    * Adjust both LoRA and LoRA-FA to similar peak memory levels and compare their MMLU accuracy. The paper lacks experiments that directly compare the performance of LoRA and LoRA-FA under similar memory constraints.
    * Examine the peak memory usage of both LoRA and LoRA-FA when using generative models larger than LLaMA-7B to determine if the gap increases as the model size grows. The paper does not provide sufficient evidence to demonstrate the scalability of LoRA-FA's memory savings to larger models.

### Questions
Covered in the weaknesses section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce to reduce for activation memory during fine-tuning, called LoRA-FA. LoRA-FA introduces a memory-efficient approach by freezing certain weights of LoRA layers, significantly reducing activation memory without compromising performance or incurring additional computational costs. Experiments across various model types and scales, including RoBERTa, T5, and LLaMA, demonstrate that LoRA-FA consistently maintains fine-tuning accuracy while reducing overall memory costs by up to 4x and 1.4x compared to full-parameter fine-tuning and LoRA, respectively. Additionally, LoRA-FA is compatible with advanced memory optimization methods like FlashAttention, QLoRA, and ZeRO.

### Strengths
* When comparing activation memory among various existing fine-tuning methodologies, it is evident that LoRA does not significantly reduce activation memory compared to full fine-tuning.
* In this paper, the authors propose a simple yet effective approach to reduce activation memory size during the fine-tuning phase by selectively freezing certain portions of the LoRA adaptation layer.
* The experimental findings demonstrate that the proposed LoRA-FA achieves performance comparable to LoRA across various large language models (LLMs), including LLaMA, T5, and RoBERTa, in downstream tasks.
* The study highlights the compatibility of LoRA-FA with advanced memory optimization techniques such as FlashAttention, QLoRA, and ZeRO.

### Weaknesses
 * The discussion on the benefits of reduced activation memory through LoRA-FA is lacking. In the finetuning phase, unlike the inference phase, both sequence length and batch size are longer, resulting in high GPU utilization. Therefore, it is not considered practically significant to make LoRA-FA more memory efficient than the existing LoRA.
* I think efficient finetuning becomes more crucial as the model size increases. Therefore, it is necessary to demonstrate that as the model size grows, it shows performance similar to LoRA. However, the models experimented in the paper were limited to sizes up to 7B, which is relatively small. The trends in models larger than 7B remain unknown.
* As I consider LoRA to be a comprehensive methodology that encompasses LoRA-FA, it is difficult to anticipate that LoRA-FA would exhibit better accuracy than LoRA.
* The cost required for inference after finetuning is completed is the same for both LoRA and LoRA-FA.
* While the paper demonstrates a reduction in activation memory, it does not adequately address the practical implications for training throughput. The fine-tuning phase typically involves larger batch sizes and sequence lengths, which often makes the process compute-bound rather than memory-bound. Therefore, the reduction in activation memory may not translate to a significant improvement in training speed or overall efficiency, especially if the computational cost remains similar to LoRA.

### Questions
* Is there any performance difference based on the initialization method for the LoRA adaptation layer A?
* When integrating the proposed LoRA-FA into QLoRA, how does it impact the performance of CSR or MMLU in models such as LLaMA, RoBERTa, and T5? While Section 4 of the experiment results demonstrates the approach of freezing adaption layer A in various LLMs' LoRA, including QLoRA, there seems to be a mention of potential application without concrete results on the performance after actual finetuning.
* When looking at Figure 4 in the Appendix, it appears that LoRA and LoRA-FA exhibit a similar trend in TFLOPS. What are the benefits gained during the Finetuning phase by actually reducing activation memory?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a minor but meaningful tweak to LoRA, by freezing the A matrix, which has notable benefits in improving training memory. The paper provides both theoretical and empirical justifications for why LoRA-FA achieves close to LoRA performance.

### Strengths
- The method is simple, well-explained, and well-justified
- The experiments are fairly comprehensive (though as detailed in weaknesses, still leave some crucial questions unanswered)

### Weaknesses
 - The writing of the paper at times leans towards over-claiming or making unsuitable comparisons to bolster their method. For example, in section 1 and in other spots, the memory of LoRA-FA is compared to full fine-tuning but not LoRA. Given that LoRA-FA is fundamentally a tweak of LoRA, the natural comparison should be to LoRA, not the full fine-tuning just to make the numbers look more impressive. To the authors: the benefits of LoRA-FA are moderate but clear; there is not need to oversell the method.
- The crux of the evaluation lies in whether LoRA-FA underperforms LoRA, or performs comparably with reduced memory consumption. While the evaluations in the paper are quite comprehensive (spanning 3 model families), I think the current experiment still fall short of resoundingly answering this crucial question, and I would like to see the authors run a set of experiments to address this. To put this more explicitly: to determine if LoRA-FA underperforms LoRA (or not), we need a setting where LoRA is "capacity-constrained", to determine if LoRA-FA has even less "capacity" than LoRA. To do this, we need a setting where LoRA meaningfully underperforms full fine-tuning. For both the RoBERTa and T5 experiments, this is not the case. The LLaMA-7B experiments on Alpaca/FLAN -> MMLU come the closest to this, but the margin is still too small to tell (and essentially no gap at all in the case of Alpaca) (more broadly, MMLU is not a fine measure of LM performance). I can recommend the authors run a set of experiments on something like Super-NaturalInstructions, where there is likely to be a bigger gap (since the evaluation is performed on generated sequences rather than simple multiple-choice knowledge questions).

### Questions
My questions are detailed in the weaknesses section above (testing exactly where/how much capacity is lost between LoRA and LoRA-FA). I am willing to update my score given more experiments addressing my question.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
