# STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
In this paper, we present the first structural binarization method for LLM compression to less than 1-bit precision. Although LLMs have achieved remarkable performance, their memory-bound nature during the inference stage hinders the adoption of resource-constrained devices. Reducing weights to 1-bit precision through binarization substantially enhances computational efficiency. We observe that some weights in binarized LLMs can be randomly flipped without significant performance degradation, suggesting the potential for further compression. To exploit this, our STBLLM employs an N:M sparsity technique to achieve structural binarization of the weights. Specifically, we introduce a novel Standardized Importance (SI) metric, which considers weight magnitude and input feature norm to more accurately assess weight significance. Then, we propose a layer-wise approach, allowing different layers of the LLM to be sparsified with varying N:M ratios, thereby balancing compression and accuracy. Furthermore, we implement a fine-grained grouping strategy for less important weights, applying distinct quantization schemes to sparse, intermediate, and dense regions. Finally, we design a specialized CUDA kernel to support structural binarization. We conduct extensive experiments on LLaMA-1/2/3, OPT family, and Mistral to evaluate the effectiveness of STBLLM. The results demonstrate that our approach performs better than other compressed binarization LLM methods while significantly reducing memory requirements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a structural binarization method for LLMs by combining N:M sparsity, residual approximation, and block-wise error compensation. Extensive experiments on LLaMA-1/2/3, OPT, and Mistral are conducted to evaluate the effectiveness of STBLLM. In addition, a specialized CUDA kernel is designed to support structural binarization.

### Strengths
* The analysis on flipping non-salient binarized weights is intriguing. I am wondering what would happen if we increase the ratio from 0.15 to 0.5?
* The proposed method achieves the lowest perplexity among all compared methods in the sub-1-bit regime.
* A specialized CUDA kernel for structural binarization, leveraging NVIDIA's Ampere GPU sparse tensor cores, achieves a 17.85x speedup over ABQ-LLM's 2-bit implementation.

### Weaknesses
 * The proposed method is a combination of several existing techniques including N:M sparsity, residual approximation, block-wise error compensation, and Trisection search (for the non-salient part). This raises some novelty concerns. I suggest the authors to 1) highlight the main novelty and contribution of the current submission; 2) provide ablation studies on a. how important the residual approximation is, b. the impact of Trisection search for grouping and why there are two groups. In addition, which techniques contribute the most to efficiency and which method contributes the most to the accuracy?
* The benchmark results are based on various N:M configurations. However, NVIDIA GPUs mainly support 2:4. The authors may discuss how practical the proposed method is on NVIDIA GPUs.
* The analysis on flipping non-salient binarized weights is intriguing. I am wondering what would happen if we increase the ratio from 0.15 to 0.5?
*  It is still unclear how the trisection search specifically improves the performance compared to a standard binary search, and what the exact innovation is. The authors should clarify which parts of the trisection search are novel and which are adapted from existing methods.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
This paper proposes a structured binary quantization method to accelerate LLM inference. It combines n:m pruning and binary quantization, compressing the model weights to an average of less than 1 bit. In n:m pruning, the authors introduce an SI method for indentifying significant weights, and a layer-wise dynamic n:m allocation method. In binary quantization, the authors partition the weights into salient and non-salient parts for separate processing and further apply a group-wise quantization method to the non-salient part. Experimental results demonstrate that STBLLM outperforms BiLLM under the same bit budget. In addition, significant performance improvement (17x) is achieved with customized CUDA kernels.

### Strengths
+ 1-bit weight quantization is important for accelerating LLM inference.
+ Dedicated CUDA implementations for the proposed method.

### Weaknesses
 + incremental novelty

While the proposed method is interesting and performs better than BiLLM, its novelty is limited: 1) The proposed SI method is very similar to Wanda, with the main difference being the introduction of additional data normalization. 2) The binary quantization method is quite similar to BiLLM, where the hessian matrix is used to divide weights into salient and non-salient parts, and residual approximation is employed to handle the salient part. The only difference is that STBLLM processes the non-salient weights into three parts instead of two as in BiLLM.

+ mismatch between motivation and methodology

The motivation of this paper lies in the observation that some weights in binary LLMs do not significantly affect accuracy and can be further compressed (Section 3.1 and fig 1). Under this narrative, a reasonable approach would be to perform pruning on the binarized model to achieve further compression. In contrast, the method proposed in this paper adopts a ‘’prune-then-quantize’’ approach, which does not align with the motivation. The paper does not explain why pruning should be performed first and does not discuss how changing the order of pruning and binarization might affect the results. 

The motivation behind using a trisection-based partition for non-salient weights is confusing. It seems the authors aim to balance bits and performance (Section 3.4). However, the evaluation results show that the improved compression ratio and performance are due to n:m pruning, rather than the processing of non-salient weights. So, why should we partition the non-salient weights into three parts? Why not four or five? What do the terms dense, intermediate, and sparse mean?

+  confusing evaluations

While the experimental results of STBLLM are promising, the source of the accuracy improvements remains unclear. The experimental settings in the ablation study are somewhat confusing. For instance, Table 5 examines the effectiveness of the SI method in n:m pruning, but the results seem to represent 4:8 pruning plus binarization. What binarization method is used in the baselines? Table 8 directly compares STBLLM with BiLLM to illustrate the effectiveness of trisection partitioning, yet the pruning methods used in STBLLM and BiLLM are not the same (SI vs. Wanda). A detailed, step-by-step breakdown analysis of each technique's effectiveness would be helpful. Moreover, where does the 17x performance improvement come from when reducing 2-bit weights to 1 bit?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an efficient framework for LLMs, combining pruning and binarization to compress large, post-trained models. By applying N:M sparsity, it achieves precision below 1-bit and identifies salient weights through a newly introduced Standardized Importance (SI) metric. This metric considers both weight and activation values, avoiding the costly second-order computations typically required. Additionally, during pruning and binarization, the method separates non-salient weights into three groups to preserve as much information as possible in these parts. Extensive experiments demonstrate that the proposed method significantly reduces computational costs, accelerates inference, and maintains strong performance.

### Strengths
+ The paper is well-organized and easy to follow, with a clearly stated problem.
+ It introduces a new metric to assess weight importance, avoiding expensive second-order gradient computations and mitigating the impact of extreme values.
+ It is interesting that separate binarization for non-salient weights retains crucial information in this segment, enhancing model performance.
+ The approach is logical and rigorous, discussing the method from various perspectives and fully validating its effectiveness through comprehensive experiments.

### Weaknesses
 - In the zero-shot experiment, the paper mentions seven zero-shot tasks. It would be helpful to include a brief description of each task to provide readers with a clearer understanding of the evaluation scope.

 - Regarding Figure 3, part (b), after structured pruning, the empty parts should have no values. Why are zeros assigned to these parts? Additionally, structured pruning usually doesn't achieve weight-wise pruning, so what does "structured" mean in this context?

### Questions
+ Regarding Figure 3, part (b), after structured pruning, the empty parts should have no values. Why are zeros assigned to these parts? Additionally, structured pruning usually doesn't achieve weight-wise pruning, so what does "structured" mean in this context?

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
2

### Summary
This paper presents a sparse and binarized compression method for large language models (LLMs), achieving an average bit count of less than one bit. Specifically, in terms of sparsity, a new metric matrix is proposed to represent the importance of different weights, along with a method for calculating the sparsity level for each layer based on this metric. This allows for effective sparsification of the model weights. For quantization, weights are grouped and binarized within each group, thereby reducing quantization error. Experiments on models such as LLaMA-1/2/3 demonstrate that this method achieves superior performance at higher compression ratios.

### Strengths
- This approach integrates sparsity with quantization, achieving a significantly higher compression ratio by reducing both the number of active weights and the bit precision required to represent them. The sparsity aspect not only reduces storage needs but also opens up additional acceleration opportunities, as sparse models can skip unnecessary computations, leading to more efficient inference.
- A dedicated CUDA kernel was developed to optimize the performance of the sparse and quantized model on GPU hardware. This kernel was specifically tailored to exploit the structure of the sparse and binarized weights, enabling efficient memory access patterns and computation. The actual runtime performance of the model was measured using this custom kernel, providing a practical assessment of speedup gains achieved through the combined compression and acceleration strategy.

### Weaknesses
 - While the proposed quantization methodology shows promise, the performance improvements over the baseline BiLLM implementation appear to be incremental. I would encourage the authors to further highlight the distinctive advantages of their approach and potentially explore additional optimization strategies to achieve more substantial gains.
- The manuscript would benefit from enhanced clarity in several sections. Of particular importance is the need for a more comprehensive explanation of the average bit count calculation methodology. I suggest:
  - Including a detailed step-by-step breakdown of the calculation process
  - Providing specific examples to illustrate the computational procedure at inference time
  - Clarifying how this calculation relates to the overall system performance on speedup or memory reduction

- Regarding the calculation of average bit count:
   - Could you clarify whether the overhead from indices associated with sparsity has been factored into the calculation?
   - It would be helpful if you could provide a concrete example illustrating the calculation methodology, including both the weight bits and any additional storage requirements.

- In Algorithm 1, there appears to be some ambiguity regarding the Semi-Structured function:
   - Is this function performing sparsification based on SI?
   - Neither the main text nor the appendix provides details about this function's implementation. Could you please elaborate on its mechanism?

- The term "OBC" in Algorithm 1 requires clarification:
   - While BiLLM mentions this as an abbreviation from another work, it would be beneficial to provide the full reference and explanation for completeness.

- Regarding computational requirements:
   - Could you provide an estimate for the computational time required for the 65B model, perhaps through theoretical scaling analysis?

- In Figure 3, there appears to be an overlap between Salient Weight and Non-salient Weight distributions:
   - Could you explain the underlying reasons for this overlap?
   - How does this overlap affect the overall performance of the method?

- Concerning Tables 5 and 7:
   - There seems to be redundancy as Table 5 appears to be a subset of Table 7's Wikitext2 results. Could you justify the inclusion of both tables?
   - The manuscript lacks discussion of Table 7's results, particularly regarding:
     * Why does SI perform worse than SparseGPT on PTB and C4 datasets?
     * What factors contribute to the different performance patterns across datasets?
     * Could you provide insights into these performance variations?

### Questions
- Regarding the calculation of average bit count:
   - Could you clarify whether the overhead from indices associated with sparsity has been factored into the calculation?
   - It would be helpful if you could provide a concrete example illustrating the calculation methodology, including both the weight bits and any additional storage requirements.

- In Algorithm 1, there appears to be some ambiguity regarding the Semi-Structured function:
   - Is this function performing sparsification based on SI?
   - Neither the main text nor the appendix provides details about this function's implementation. Could you please elaborate on its mechanism?

- The term "OBC" in Algorithm 1 requires clarification:
   - While BiLLM mentions this as an abbreviation from another work, it would be beneficial to provide the full reference and explanation for completeness.

- Regarding computational requirements:
   - Could you provide an estimate for the computational time required for the 65B model, perhaps through theoretical scaling analysis?

- In Figure 3, there appears to be an overlap between Salient Weight and Non-salient Weight distributions:
   - Could you explain the underlying reasons for this overlap?
   - How does this overlap affect the overall performance of the method?

- Concerning Tables 5 and 7:
   - There seems to be redundancy as Table 5 appears to be a subset of Table 7's Wikitext2 results. Could you justify the inclusion of both tables?
   - The manuscript lacks discussion of Table 7's results, particularly regarding:
     * Why does SI perform worse than SparseGPT on PTB and C4 datasets?
     * What factors contribute to the different performance patterns across datasets?
     * Could you provide insights into these performance variations?

### Soundness
3

### Presentation
3

### Contribution
2
