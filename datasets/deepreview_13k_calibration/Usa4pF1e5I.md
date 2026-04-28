# SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Large Language Models (LLMs) have revolutionized natural language understanding and generation tasks but suffer from high memory consumption and slow inference times due to their large parameter sizes. Traditional model compression techniques, such as quantization and pruning, mitigate these issues but often require retraining to maintain accuracy, which is computationally expensive. This paper introduces \ours, a novel approach for compressing LLMs using a one-shot Quantized Sparse Plus Low-rank Approximation. \ours eliminates the need for costly retraining by combining a symmetric quantization method (\quantization) with a saliency-based low-rank approximation. Our method reduces quantization error while leveraging sparse representations compatible with accelerated hardware architectures. Additionally, we propose a parameter-efficient fine-tuning recipe that significantly reduces overhead compared to conventional quantization-aware training. \ours achieves up to a 5.4\% improvement in model accuracy for sparsity patterns like 2:4, and the fine-tuning step further enhances accuracy by up to 5.8\%, demonstrating state-of-the-art performance. This work provides a pathway for efficiently deploying large models in memory-constrained environments without compromising accuracy

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The manuscript proposes an LLM compression method that combines quantization, sparsity, and low-rank approximation. This approach applies low-rank approximation guided by a significance-driven optimization function, followed by fine-tuning of LoRA blocks, ultimately achieving advanced improvements in compression accuracy.

### Strengths
1. Previous algorithms aimed at compression during inference generally do not retain LoRA. This manuscript innovatively retains it, and demonstrates its feasibility in terms of time efficiency through inference efficiency analysis.

2. The idea of using saliency to guide the optimization of LoRA is highly novel.

### Weaknesses
1. The motivation for introducing Equation 8 is unclear. For instance, the authors claim that deriving LR from E_Q and E_S is intended to “cancel the compression errors”, yet introduce a significance function F that does not seem directly related to these compression errors.

2. Prior to Equation 10, the significance calculation method from Wanda is introduced without clear motivation. To my knowledge, there are alternative methods for measuring significance, such as AWQ[1] and SparseGPT[2], yet the authors appear not to consider them.

3. In Section 3.2, the manuscript claims that previous error minimization methods did not consider "the importance of different weights", though methods like OBS[3] clearly address the importance of weights (see its explanation of L_q).

4. The manuscript does not explain the pruning approach used and lacks relevant formula descriptions for E_S.

5. There is a lack of comparison with advanced joint strategies for sparse quantization, such as JSQ[4].

6. The manuscript lacks statistics on model size, which may lead to unfair comparisons. Since SLIM introduces additional LoRA layers with a substantial rank (r=0.1), describing the extra parameter overhead is necessary. Similarly, theoretical computations for the number of OPs are also not provided.

### Questions
1. Significance is usually used to guide pruning decisions, so why is the significance calculation method proposed in Wanda used as the optimization target for quantization and sparsification? Why does optimizing the significance metric result in better low-rank adapters?

2. Why does not pruning weights in LQ-LORA lead to a significantly higher error rate?

3. Why does the discussion on Inference Speedup not consider the impact of quantization?

### Soundness
2

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
4

### Summary
In this paper, the authors propose to combine quantization and pruning to compress LLMs. A new quantization method called SLiM-Quant is proposed to reduce the quantization error. To develop the new method, the mean squared error used in the literature was converted to a probabilistic formulation, which is solved by numerical integration over the weight histogram. Then a pruning method (structured or unstructured pruning) is applied. To compensate for the accuracy loss due to pruning and quantization, a new low-rank adapter is proposed, which is based on the assumption of an additive invertible saliency function. Finally, the low-rank adapters are quantized in a manner of 16x16 tiles, which is finally merged into the quantized sparse weight.

### Strengths
1. Experimental results show that the proposed method leads to improved model accuracy under the same pruning and quantization scheme.

2. A novel low-rank adapter is proposed in this paper.

### Weaknesses
1. But why is the proposed low-rank adapter not compared with the previous low-rank adapter? Without such a comparison, it's hard to tell the advantage of the proposed method.

2. The combination of quantization and pruning seems to be a straightforward method. In this paper, the two methods seems to be loosely coupled. As mentioned in Questions, the joint optimization has some unanswered questions.

3. Actually acceleration performance is not reported in this paper.

### Questions
1. When merging the quantized sparse weight and low-rank adapters, there might be overflow due to addition. The non-zero values from the low-rank adapters might also be added to originally the pruned weights, which disturbs the pruning mechanism (in particular the 2:4 structured pruning). How should those potential problems during weight merging be solved?

2. What is the evaluation metric used in Table 1-3?

3. Does the quantization method proposed in this paper lead to zero values?

4. The paper did not propose a new pruning method. But in Table, SLiM works better than other methods under a pruning-only scheme.

5. The additive invertible saliency function comes from nowhere. The property is not explained in the supplementary either.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces SLIM, a method for compressing Large Language Models (LLMs) using a one-shot approach that combines quantization, sparsity, and low-rank approximation. It reduces memory usage and inference time without retraining, while maintaining high accuracy. SLIM also includes an efficient fine-tuning process, achieving up to 5.8% accuracy improvement over existing compression techniques, making it ideal for deploying large models on resource-constrained hardware.

### Strengths
1. The proposed symmetric quantization minimizes quantization error without altering the weights, resulting in reduced computational and memory overhead.
2. SLIM introduces a saliency-based method to reconstruct weights based on their importance, targeting weights with the highest impact on model output, which helps retain model accuracy. 
3. SLIM improves model accuracy by up to 5.4% over state-of-the-art pruning and quantization methods for 2:4 sparsity patterns. With fine-tuning, the accuracy gain can increase to 5.8%.
4. The fine-tuning recipe for sparse, quantized models significantly reduces the time and resources needed for fine-tuning. For example, a 13B parameter model that typically takes 36 days to fine-tune is reduced to just 14 hours on an H100 GPU.

### Weaknesses
1. The specific method for determining the quantization scale in L199-L202 should be described in more detail to clarify the contribution. Some background information (e.g., symmetric quantization, description of quantization errors, etc.) could be shortened or moved to the supplementary material to reduce the length.
2. Some more advanced quantization methods [1-5] significantly outperform GPTQ. Would combining these methods further enhance compression performance?
3. The combination of these different compression methods (sparsity, quantization) should result in a higher compression rate. However, related experiments on the memory footprint of the compressed model and the analysis of inference efficiency are not included in the paper.
4. The theoretical justification for modeling the impact of weight matrix quantization and pruning as additive noise in L205-206 is weak. It is not clear why the errors would simply add, and there is no experimental or theoretical support for this claim. The interaction of these errors could easily lead to non-additive effects, potentially amplifying the overall error rather than simply summing them.

### Questions
1. The issues mentioned in the weaknesses should be addressed.
2. In L205-206, why can the impact of weight matrix quantization and pruning be modeled as additive noise? Is there any experimental or theoretical support for this claim? Why wouldn’t the combination of the two errors introduce larger errors? Intuitively, if $W^Q= W+ E_Q$ and $W^S =W+ E_S $, why would $W^Q+W^S=W_C$?

### Soundness
2

### Presentation
2

### Contribution
1
