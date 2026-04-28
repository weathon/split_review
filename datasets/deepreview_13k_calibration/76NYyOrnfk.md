# FastAttention: Extend FlashAttention2 to NPUs and Low-resource GPUs for Efficient Inference

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
FlashAttention series has been widely applied in the inference of large language models (LLMs). However, FlashAttention series only supports the high-level GPU architectures, e.g., Ampere and Hopper. At present, FlashAttention series is not easily transferrable to NPUs and low-resource GPUs. Moreover, FlashAttention series is inefficient for multi- NPUs or GPUs inference scenarios.   
In this work, we propose FastAttention which pioneers the adaptation of FlashAttention series for NPUs and low-resource GPUs to boost LLM inference efficiency. Specifically, we take Ascend NPUs and Volta-based GPUs as representatives for designing our FastAttention. We migrate FlashAttention series to Ascend NPUs by proposing a novel two-level tiling strategy for runtime speedup, tiling-mask strategy for memory saving and the tiling-AllReduce strategy for reducing communication overhead, respectively. Besides, we adapt FlashAttention for Volta-based GPUs by redesigning the operands layout in shared memory and introducing a simple yet effective CPU-GPU cooperative strategy for efficient memory utilization. 
On Ascend NPUs, our FastAttention can achieve a 10.7$\times$ speedup compared to the standard attention implementation. Llama-7B within FastAttention reaches up to 5.16$\times$ higher throughput than within the standard attention. 
On Volta architecture GPUs, FastAttention yields 1.43$\times$ speedup compared to its equivalents in xformers. Pangu-38B within FastAttention brings 1.46$\times$ end-to-end speedup using FasterTransformer.
Coupled with the propose CPU-GPU cooperative strategy, FastAttention supports a maximal input length of 256K on 8 V100 GPUs. All the codes will be made available soon.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to refactor the FlashAttention (used only on high-end GPUs A/H-series because of the tensor core architecture) to NPUs and earlier generation Volta (V100) GPUs. The adaptation is poses some challenges due to the underlying hardware architectures (NPUs have AI core and Vector units whereas V100s don't have tensor cores), therefore, the proposed new two-level tiling strategy for memory and commute efficiencies. On Vota GPUs, there is a further enhancement in the form of CPU-GPU based cooperative strategy for better memory usage. The proposed refactorings show efficient improvments in speedup and throughput on the corresponding hardware chips when compared to the vanilla case.

### Strengths
- The paper is some what reasonably written, however was able to follow along and understand the presented concepts. 
- The strengths of the paper are in the new tiling strategies be it be memory efficiency or the all-reduce communication efficiencies.
- Given the shortage of GPUs and at the outset to better exploit the available resources, FastAttention kind of a technique is very much appreciated and in that sense this approach is highly valuable.

### Weaknesses
 - In section 4.1 there is a description on the how the attention operations work in the proposed tiling strategy. It is not fully clear from the description as to how they work. Please address the following questions on this.
  - Please represent the tiling mathematically with equations showing how the matrices are tiled along with their dimensions 
  - A step-by-step breakdown of operations on the tiles, especially in a two-level tiling strategy.
  - In 2-3 sentences, explain how FastAttention tiling strategies compare with that of the existing FlashAttention.
- In section 4.2, there is this new term `Linear calculation` is not defined earlier, nor is easy to decipher. On that note, Please define clearly what these operations are, very important to understand given that there is so much optimization on these operations.
  - Please define "Linear calculation" when it's first introduced and clarify how these calculations take place in the overall attention mechanism, especially when the two stage tiling is in effect.
- what does this sentence mean `Given the CuTe library typically focuses ... ` (around lines 298 and 299). Please provide clarification on this.
- In section 4.3, the data layout is changed with CuTe to support Volta-GPUs. Two questions on this are 
  1. Data layout adaption should be done for a new LLM architecture or is this architecture agnostic? There are some details in Appendix B but it is not clear whether the process is manual or can be reproduced by using an algorithm.
  2. Then, besides there are bank conflicts being resolved, is there a procedure that can be followed or is it pretty manual and should be handled with care for each model? Note that there are not many details on how this was achieved either in Appendix or in the main paper.
  - For both the questions, please provide procedural details that helped close the gap in porting the FlashAttention to these older generation GPUs.
- In section 4.4, the terms `L_{CPU}` and `L_{GPU}` are introduced, but never defined. Please add definitions to those terms. 
- In Figure 8, please add a comparison with huggingface transformers implementation. This can help show the improvements over the vanilla implementations, especially there is a significant user base.

### minor issues:
- `thread in a Wrap.` at line 287 should be `warp`

### Questions
- In section 4.1 there is a description on the how the attention operations work in the proposed tiling strategy. It is not fully clear from the description as to how they work. Please address the following questions on this.
  - Please represent the tiling mathematically with equations showing how the matrices are tiled along with their dimensions 
  - A step-by-step breakdown of operations on the tiles, especially in a two-level tiling strategy.
  - In 2-3 sentences, explain how FastAttention tiling strategies compare with that of the existing FlashAttention.
- In section 4.2, there is this new term `Linear calculation` is not defined earlier, nor is easy to decipher. On that note, Please define clearly what these operations are, very important to understand given that there is so much optimization on these operations.
  - Please define "Linear calculation" when it's first introduced and clarify how these calculations take place in the overall attention mechanism, especially when the two stage tiling is in effect.
- what does this sentence mean `Given the CuTe library typically focuses ... ` (around lines 298 and 299). Please provide clarification on this.
- In section 4.3, the data layout is changed with CuTe to support Volta-GPUs. Two questions on this are 
  1. Data layout adaption should be done for a new LLM architecture or is this architecture agnostic? There are some details in Appendix B but it is not clear whether the process is manual or can be reproduced by using an algorithm.
  2. Then, besides there are bank conflicts being resolved, is there a procedure that can be followed or is it pretty manual and should be handled with care for each model? Note that there are not many details on how this was achieved either in Appendix or in the main paper.
  - For both the questions, please provide procedural details that helped close the gap in porting the FlashAttention to these older generation GPUs.
- In section 4.4, the terms `L_{CPU}` and `L_{GPU}` are introduced, but never defined. Please add definitions to those terms. 
- In Figure 8, please add a comparison with huggingface transformers implementation. This can help show the improvements over the vanilla implementations, especially there is a significant user base.

### minor issues:
- `thread in a Wrap.` at line 287 should be `warp`

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
4

### Summary
This paper presents the FlashAttention (or memory-efficient Attention) on the NPU and implements it on the currently unsupported GPUs. It adapts the FlashAttention algorithm to NPU with a two-level tiling, presents the software pipeline of computation/communication on multi-NPUs, implements it on V100 GPU, and presents the solution of long context.

### Strengths
- Design/implement a critical Algorithm onto the new architecture. The pipeline and offloading method are not explored in the official FlashAttention.
- Achieve good speedup.

### Weaknesses
 - Even though it presents solid implementation, the research contributed could be highlighted more. For example, the fusion and tiling of the Attention does not show significant difference to FlashAttention and memory-efficient Attention.
- It lacks the credit to memory-efficient Attention (Self-attention Does Not Need O(n^2) Memory), which is a concurrent (or earlier) work of fusing Attention with the similar method with FlashAttention-2, and supports TPU.



### Questions
- It claims in the introduction that, the existing FlashAttention cannot run on non-CUDA architectures. However, the memory-efficient Attention has supported TPU ((Self-attention Does Not Need O(n^2) Memory)), and its paper is released on 2021 Dec. Besides, there is also AMD GPU suppported FlashAttention (https://rocm.blogs.amd.com/artificial-intelligence/flash-attention/README.html), which is also non-CUDA.
- Section 4.2 describes the two-level tiling, is it the same with the normal GEMM implement on the NPU? This is similar to the two-level tiling on the GPU: block level and warp/MMA level.  A comparison between the two-level tiling described in this paper and the GEMM implementation can be helpful to show the unique contribution of this design.
- The current description does not highlight the research challenge of supporting FlashAttention on the V100 besides the engineer problems. Highlighting the unique design difference can better make the reader understand the contribution. Besides, supporting newer architecture rather than older architecture is the common research trend. Some discussion of supporting the old architecture could be helpful for this paper.

### Soundness
2

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
Existing implementations of FlashAttention do not support older or low-resource GPUs, such as those with Volta architecture and earlier models, as well as NPUs. This paper introduces FastAttention, the first adaptation of FlashAttention designed for these types of accelerators. It outlines the challenges and opportunities associated with porting FlashAttention to NPUs and pre-Ampere NVIDIA GPUs. The authors propose an implementation that optimizes performance by leveraging the specific hardware features of the target NPU or pre-Ampere GPU. Additionally, the evaluation demonstrates the performance of FastAttention in both single and multi-accelerator scenarios.

### Strengths
- The ability to run the faster FlashAttention on a greater number of AI accelerators is an important contribution to the AI community.  
- A well-designed solution has been proposed to effectively utilize the Cube/Vector units and the memory hierarchy in NPUs.  
- There is a clear comparison of the use of the Matrix Multiply Accumulator (MMA) in the Volta architecture versus later architectures.  
- The evaluation is thorough and comprehensive.

### Weaknesses
 - The work appears to focus more on incremental implementation rather than addressing or solving a novel problem innovatively. To enhance this work, the author could investigate how the techniques used to adapt the flashattention kernels for NPUs and low-resource GPUs might be applicable to a broader range of kernels designed for Turing, Ampere, and Blackwell architectures. For instance, any kernels based on Matrix Multiply Accumulation (MMA) could also benefit from these adaptations. In this context, flashattention could serve as a significant practical example that is explored in detail within the paper.
- The contributions seem to be limited to a few specific architectures. For example, although the title mentions "low-resource GPUs," FastAttention appears to primarily support V100 GPUs. Does FastAttention support all NVIDIA Volta GPUs? What about Pascal or earlier architectures? Additionally, what is the support status for non-NVIDIA architectures? It would be helpful to clearly specify which hardware architectures are supported, even if some are not.
- The paper discusses only the inference scenario, but it is unclear whether FastAttention is designed solely for inference or if it also supports training. The authors should clarify this and, if training is supported, include a discussion in the paper. For example, what are the memory requirements during backpropagation and how do the proposed optimizations affect gradient computation?
- The prior work and background on the fusion of attention and linear calculations in Section 4.2 could be explained more clearly and supplemented with relevant citations.

### Questions
- Does FastAttention work with any type/version of NPUs, or is it limited to only certain models?
- Is FastAttention compatible with low-resource GPUs beyond the ones mentioned in V100 and those based on the Volta architecture?
- Could you provide more details about the implementation of FastAttention? Was the code built on existing libraries or repositories? Is there a plan to integrate it into existing open-source LLM frameworks?
- In section 4.1, you describe an optimization intended to reduce the memory requirement for the causal mask. However, since the causal masking is determined solely by the relative positions in the sequence for each attention score, why generate a causal matrix? Could this be achieved with a simple instruction in the kernel that sets the result to zero for items that should not be included? To enhance the paper, it would be beneficial to assess this option in the experiments.
- Could you enhance the figure captions so that all relevant details of the experiments can be understood simply by looking at the plots and their captions? At times, readers need to refer back to the main text to grasp the specifics of an experiment, such as whether it measures prefill versus decode latency or the parallelization strategy employed. Including key takeaways in the figure captions would also be beneficial.

### Soundness
3

### Presentation
2

### Contribution
3
