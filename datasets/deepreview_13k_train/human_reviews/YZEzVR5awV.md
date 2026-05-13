# ClusComp: A Simple Paradigm for Model Compression and Efficient Finetuning

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
As large language models (LLMs) continue to scale, model compression becomes increasingly important for enabling edge deployment and ensuring accessibility to users with limited resources. Weight-only quantization is a key technique for model compression, allowing for a substantial reduction in model size while preserving performance. However, as bit-width decreases, the performance of quantized LLMs tends to degrade significantly. Additionally, due to the non-differentiable operation in quantization, standard finetuning on quantized LLMs is unsupported, and alternative finetuning approaches often fail to match the effectiveness of full finetuning. In this paper, we introduce ClusComp, a novel and simple model compression paradigm. ClusComp first clusters the weight matrices to generate codebooks, and then tunes these codebooks block-by-block to reconstruct intermediate activations. Despite its simplicity, ClusComp (1) consistently achieves better performance in 2-4 bit precision; (2) pushes the compression limit to the 1-bit level, and outperforms existing ultra-low-bit methods with limited finetuning steps; (3) facilitates seamless and efficient finetuning, surpasses existing quantization-based or memory-efficient finetuning methods, and even rivals full finetuning of the FP16 model. Notably, these procedures can be executed on a single NVIDIA A6000-48GB GPU for LLMs with as many as 70B parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper tackles memory savings for LLMs by using clustering-based quantization. ClusComp clusters the weight matrices
to generate codebooks, tunes these codebooks block-by-block to reconstruct intermediate activations, and also conduct recovery training for high compression regimes. It shows promising results for language modeling and also multimodal models across various tasks and model size.

### Strengths
- The motivation and method is sound and clear. It is nice to see that they clarify no gains in speedup while highlighting the memory savings and limited accuracy loss. 
- Paper presentation and writing are readable and easy to understand. 
- Experimental results are promising with a wide range of models, tasks, and comparisons to other methods.

### Weaknesses
 - I'd like to see more comparison to recent works, including clustering-based quantization [1] and for uniform PTQ [2]. 
- Some analysis that explains how the codebooks are distributed to better capture salient weights would be helpful to understand why this method works. 



### Questions
1. Figure 1: L45, "Some results are divided by a factor for better visualization." -> what does divided by a factor mean? Also, it is unclear what the triangular marker means on the bottom left graph (everything else is a circular marker; what is the difference?).
2. Add to the Figure 2 description that it's showing the kurtosis of weights. Also, recent works [1,2,3] show that activation-awareness is important for identifying weight outliers, so simply taking the weight distribution to explain the quantization difficulty of recent LLMs may be insufficient.

[1] Lin, et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", MLSys 2024.\
[2] Heo, et al., "Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models", ICLR 2024\
[3] Sun, et al., "A Simple and Effective Pruning Approach for Large Language Models", ICLR 2024

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ClusComp, a clustering-based paradigm for compressing large language models (LLMs). It flattens and reshapes the weight matrix and clustering the segments to a set of centroids while not reduces the bits of weights. It claims significant advancements in compression efficiency without performance degradation, even reaching 1-bit precision with improved finetuning outcomes over existing method.

### Strengths
1. **Empirical Results**: ClusComp achieves superior performance at low-bit precisions, outperforming alternative methods across various LLMs and multimodal models. Its efficacy is well-supported by extensive experiments.

2. **Memory Efficiency**: ClusComp demonstrates significant memory savings, making it feasible to deploy large models on resource-constrained devices, which is crucial for practical deployment.

### Weaknesses
1. ClusComp does not reduce the parameter count through dimensional reduction or bit-width reduction, thus maintaining the same computational load during inference.

2. Some visualizations lack clarity:
    - _Figure 1_: The meaning of the marker colors is unclear.
    - _Figure 3_: The histogram appears unnecessary; a simple text explanation could suffice.

3. The block-wise error minimization introduced in section 3.2.3 is a standard practice in post-training quantization and lacks novelty in this context.

### Questions
1. _Line 253-254_: The authors state that the codebooks are not quantized. Could further quantization improve the efficiency of the model? Would combining ClusComp with conventional quantization lead to better results?

2. _Figure 4 and Table C.4_: Why does the 2.01-bit ClusComp version (53.6% accuracy) perform better than the 2.14-bit version (51.7%) on Llama3-8B?

3. Could additional ablation studies on hyperparameters, such as cluster count and codebook dimensionality, provide more insight into their impact on compression performance?

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
The paper proposes a simple clustering based framework to quantize LLMs and finetune them. The authors employ k-means clustering to find the clustering centroids (i.e., the codebook) over small sub-vectors of the weight matrix. For finetuning, the paper proposes to finetune the entire codebook as opposed to QLoRA [1] which only finetunes the LoRA parameters while keeping the backbone quantized LLM frozen. For weight-only quantization and parameter-efficient finetuning, the paper improves over most baselines.

### Strengths
- A simple alternative to scalar quantization, especially in scenarios where the size of the LLM is a bigger bottleneck than its latency.
- An efficient strategy to finetuning entire LLMs.

### Weaknesses
 - The proposed approach doesn't give latency benefits. However, the authors acknowledge this point.
- Some works that use codebooks and non-uniform quantization are missing from the related works section: SqueezeLLM: Dense-and-Sparse Quantization [2], Any-Precision LLM: Low-Cost Deployment of Multiple, Different-Sized LLMs [3].

- Does finetuning the codebook affect the generalization performance of the model? In the case of QLoRA, since the backbone LLM is frozen, the generalization properties of the LLMs are preserved.

### Questions
- Does finetuning the codebook affect the generalization performance of the model? In the case of QLoRA, since the backbone LLM is frozen, the generalization properties of the LLMs are preserved.



[1] Dettmers, Tim et al. “QLoRA: Efficient Finetuning of Quantized LLMs.” NeurIPS 2023.

[2] Kim, Sehoon et al. “SqueezeLLM: Dense-and-Sparse Quantization.” ICML 2024.

[3] Park, Yeonhong et al. “Any-Precision LLM: Low-Cost Deployment of Multiple, Different-Sized LLMs.” ICML 2024.

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
5

### Summary
The paper presents ClusComp, a way to cluster vectors of values in weights. This post-training 'quantization' technique shows competitive quality, outperforming state-of-the-art quantization methods. The authors evaluate on pre-trained models, multimodal models, and fine-tuned models.

### Strengths
1. The paper is well-organized and well-presented. The problem, insight, and method are all clear from reading the abstract alone, and the vast majority of my questions are answered by just reading the paper in detail.
2. Figure 1 is very clear and convincing. We see the obligatory "our line is better than everyone else's", and the ~1 bit model performance, with just a modicum of calibration data, is especially impressive. Out of curiosity, how does SqueezeLLM/GPTQ/QuiP fare, if it was plotted on the same graph?
3. Related work is thorough, and the plots include relevant baselines for comparison -- both popularly-used models and popularly-used compression techniques. This paper includes all relevant baselines that are popularly-used.
4. Evaluation is thorough, with perplexity and zero-shot accuracy results for the pretrained model, as well as downstream multimodal evaluation. On top of that, the authors show lora-tuned results. The results are convincing and clearly presented.

### Weaknesses
One missing component is the lack of latency or power benchmarks. In short, this LUT is huge. Per C.1, n could be as large as 65500, which is *basically 2^16. g=5, so the LUT is now 16 * 5 * 2^16 > 2^22 bits or 2^19 bytes. That's 500 KB, which is too large for L1 (H100 has 256 KB of L1, but this needs to fit both the indices AND the LUT), meaning decoding every tile in a matmul could potentially result in many RAM accesses. As a result, I'm curious if a custom kernel for this method would actually be faster than its FP16 baseline, on modern GPUs.

However, future hardware will have increasingly larger and larger SRAMs -- and with it, larger L1s. Given the nature of research, I think this concern can be deprioritized as a result. We'll eventually get to a point where hardware makes this concern obsolete. So, in my opinion, the paper already makes a clear contribution: This is a technique that achieves high quality and would be worth optimizing hardware/kernel performance for. Granted, I don't think it's possible to do in the current form with modern hardware, but maybe its cousin could be made hardware friendly. Papers don't have to be picture perfect out of the gate, for production in the current state or day.

The problem right now is that at bitwidths of >= 3bpw you’re at similar accuracy but much lower throughput. So cluscomp is strictly worse at these bitwidths.

### Questions
- What does "time" mean in Figure 1's caption mean? Inference latency? Training time?
- What does $\leq$ mean in Table 2? I looked for mention of this in the main text and caption for Table 2 but couldn't find a mention.

Summary: I don't have much to say here, because the idea was simple, easy to understand, and thoroughly experimented with. Results are shown on pre-trained LLMs, multimiodal LLMs, and fine-tuned LLMs. My main concern is hardware friendliness above, meaning I don't believe latency would actually be reduced due to the size of the look-up-table. However, I still believe this is a paper worth publishing, as it sets a north star for further hardware friendly improvements. There's also a possibility that I'm wrong however. If you can show hardware friendliness for modern hardware, I would bump my rating up!

### Soundness
4

### Presentation
4

### Contribution
3
