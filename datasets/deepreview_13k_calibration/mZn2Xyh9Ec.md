# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 1, 8, 5

## Abstract
Scaling Transformers to longer sequence lengths has been a major problem in the
last several years, promising to improve performance in language modeling and
high-resolution image understanding, as well as to unlock new applications in
code, audio, and video generation.
The attention layer is the main bottleneck in scaling to longer sequences, as
its runtime and memory increase quadratically in the sequence length.
\sysnameone~\citep{dao2022flashattention} exploits the asymmetric GPU memory
hierarchy to bring significant memory saving (linear instead of quadratic) and
runtime speedup (2-4$\times$ compared to optimized baselines), with no approximation.
However, \sysnameone is still not nearly as fast as optimized matrix-multiply
(GEMM) operations, reaching only 25-40\% of the theoretical maximum FLOPs/s.
We observe that the inefficiency is due to suboptimal work partitioning between
different thread blocks and warps on the GPU, causing either low-occupancy or
unnecessary shared memory reads/writes.
We propose \sysname, with better work partitioning to address these issues.
In particular, we (1) tweak the algorithm to reduce the number of non-matmul
FLOPs (2) parallelize the attention computation, even for a single head, across
different thread blocks to increase occupancy, and (3) within each thread block,
distribute the work between warps to reduce communication through shared memory.
These yield around 2$\times$ speedup compared to \sysnameone, reaching 50-73\% of the
theoretical maximum FLOPs/s on A100 and getting close to the efficiency of GEMM
operations.
We empirically validate that when used end-to-end to train GPT-style models,
\sysname reaches training speed of up to 225 TFLOPs/s per A100 GPU (72\% model
FLOPs utilization)

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Scaling Transformers for longer sequences holds the promise of enhancing language modeling and understanding complex inputs, but is hindered by the attention layer's quadratic scaling in memory and runtime. FlashAttention has mitigated this by bringing linear memory usage and considerable runtime speedup, yet it still lags behind the efficiency of optimized matrix multiplication operations. To address this, FlashAttention-2 is introduced with improved work partitioning, yielding a significant speedup and reaching closer to the efficiency of matrix multiply (GEMM) operations. Empirical validation shows that FlashAttention-2 significantly increases the training speed of GPT-style models on both A100 and H100 GPUs.

### Strengths
* The proposed platform-specific optimizations are clever and sound.
* The resulting software artifacts are useful and have has the potential to benefit both researchers and practitioners.

### Weaknesses
* The work is mostly engineering-focused, with several "tweaks" made to FlashAttention. While these optimizations are valuable, the paper could benefit from a more in-depth analysis of the theoretical implications of these changes. For instance, how do these modifications affect the fundamental properties of the attention mechanism? Are there any trade-offs in terms of model expressiveness or convergence behavior introduced by these optimizations?
* The performance gains are relatively marginal, especially when compared to those of the original FlashAttention over the baseline. The paper would be stronger if it provided a more compelling justification for the significance of these gains in practical scenarios. While a 2x speedup is mentioned, the real-world impact needs further elaboration. For example, how does this translate to training time reduction for large language models? What are the cost savings in terms of computational resources?
* The absence of an ablation study makes it difficult to pinpoint the exact sources of efficiency. This is a crucial omission. Without a detailed breakdown of the performance contribution of each optimization, it is hard to assess their individual merits. For example, what is the specific speedup achieved by just modifying the work partitioning scheme compared to the baseline FlashAttention? How much does the improved parallelism contribute independently? Such an analysis would greatly enhance the scientific rigor of the paper.

### Questions
Thank you for submitting to ICLR 2024. FlashAttention-2 is a very useful artifact that has the potential to benefit both researchers and practitioners, and the proposed optimization techniques appear sound.

Here are my questions I would like the authors to answer:
* Perhaps the most significant omission in this paper is the lack of an ablation study. This makes it challenging to discern the contributions of individual optimizations. Among the proposed optimizations, which one has the highest impact?
* In Section 3.1, is the technique of skipping blocks for "causal masking" also applied to FlashAttention? As the authors mention, this technique can be applied to both FlashAttention and FlashAttention-2, and I am curious about how the application of this technique would affect the performance gap between FlashAttention and FlashAttention-2 if it had not been applied to FlashAttention.
* In Section 3.3, what is the performance impact of "tuning block sizes"? Was the same level of parameter tuning effort applied to FlashAttention? My question concerns the extent to which the performance gains over FlashAttention can be attributed to algorithmic improvements versus additional tuning effort, with the latter being less significant.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents improvements to FlashAttention (Dao et al., 2022), a established method for efficiently computing attention through fused ops. These improvements are designed specifically for better parallelism and work partitioning in GPUs, resulting in the development of FlashAttention v2. Performance benchmarks have been conducted for both training and inference phases. Additionally, the authors provide comprehensive results from training end-to-end GPT-style models with 1.3 billion and 2.7 billion parameters and 2k and 8k context sizes.

### Strengths
There are many things to like in this paper, such as:

1. The paper is well-written
2. The improvements are well-explained and justified
3. The paper covers both training and inference time optimization
4. The results are encouraging

In summary, I expect widespread adoption of FlashAttention v2 within the community. Furthermore, the methods proposed and utilized in this paper could inspire the creation of more efficient components in machine learning.

### Weaknesses
FlashAttention v2 has a notable limitation: it relies on recent, specialized GPU architectures like the A100 (and H100). This dependence restricts its applicability to environments with older hardware, potentially hindering broader adoption in research and development settings that lack access to the latest GPUs. Additionally, the requirement for custom CUDA kernels adds a layer of complexity, making it more challenging to integrate into existing deep learning frameworks and requiring specialized expertise for implementation and debugging. This reliance on custom kernels also increases the maintenance burden, as these kernels need to be updated and optimized for new hardware and software releases. 

A small critique is that Figure 3 could benefit from a more descriptive caption. The current caption lacks sufficient detail to fully understand the figure's content and implications, making it harder for readers to grasp the nuances of the presented data.

### Questions
Which GPU architectures currently support FlashAttention v2?
What are the minimum requirements for its use?
What modifications are necessary to adapt FlashAttention v2 for use with relative positional encoding methods (e.g., RoPE and ALiBi)?
Does FlashAttention v2 offer compatibility with sparse block masks (as in v1)?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a new algorithm, FlashAttention-2, which builds in FlashAttention to improve the efficiency of the attention algorithm when executed on GPUs. The authors focus, in particular, on maximizing the amount of time spent in "matrix-multiply" FLOPs, that is, computation that is using matrix multiplication units, which are better lent to GPU hardware given particular division of work amongst warps and loose requirements around shared memory accesses.

These optimizations include:
1. Deferring scaling of values in the online softmax computation to further reduce HBM utilization
2. Save a logsumexp for online softmax backwards rather than max and sums to reduce the memory usage.
3. The bulk of the changes present in FlashAttention-2 are related to scheduling. Parallelization over the sequence dimension results in better warp occupancy in cases where there are few attention heads or a low batch size. Further, the authors change how the backward pass shares computation in the query derivative update, which also reduce HBM utilization. Splitting the KV cache amongst thread blocks also helps to saturate memory bandwidth. Better partitioning amongst warps, overall, drives better utilization.

### Strengths
- The proposed approach shows promising improvements in a performance-critical parts of end-to-end transformer computation.
- The approach is symmetrically applicable for both training and inference with broad applications in both research and production settings.
- It is important that engineering contributions such as FlashAttention-2 (which I will refer to FA-2) are part of conference literature, and the attention to detail therein is what drives the solid impact of this work rather than a special "algorithmic contribution" in a classical sense.
- The devil is in the details: careful analysis of scheduling and an intuitive approach to laying out computation drives the approach's strong results.
- The work builds on an already-strong baseline, FlashAttention.
- The paper is well-written and organized and clearly lays out the authors' contributions; in particular, the paper is quite accessible to those without a low-level background in machine learning computation or GPU programming.

### Weaknesses
 - The baselines benchmarked in the paper can be stronger.
  - For latency benchmarks in Figure 5, the only baselines are a FasterTransformer and PyTorch. The authors do not consider compilers
  - Do the PyTorch benchmarks in Figure 5 use CUDA Graphs? PyTorch has significant framework overhead, and CUDA Graphs can give an order of magnitude speedup for some workloads, especially latency-sensitive ones.
- The above applies more generally to the other evaluation in Section 4; FlashAttention-2 is compared to PyTorch, then implementations with Triton and Cutlass, but not with any other frameworks capable of code generation. For example: while XLA may not be memory-bandwidth-aware by default, it can still generate kernels with fused operators that significantly reduce total memory I/O.
- While not needing to resort to approximations is a significant advantage of FlashAttention-2, this could be highlighted much more in the manuscript. Section 1 discusses many alternative attention approximations -- even speculation about why these aren't used (i.e. they are riskier when researchers have limited resources and don't adapt as easily) would strengthen the exactness boon of the authors' approach.

Several improvements to writing might improve the paper:
- The constant and equation in general in Sections 4.1 (i.e. 4) is not adequately explained (why is the sequence length squared? why 4?). Clarifying these might help new readers.
- The usage of "major problem" in the first sentence of the abstract is unclear -- it's clear that scaling sequence lengths is difficult; are the authors suggesting the problem is difficult, significant, or both?
- Section 1: "However, context length increases" <-- is missing "**as** context length increases"
- Text in all of the provided diagrams can be made clearer, and the diagrams can be rendered more clearly. It is difficult to read them as is.
- Section 3.2 might more clearly explain "prefill" and "KV cache" to readers. While somewhat ubiquitously understood amongst people doing performance engineering for large-scale transformers, some clarification would help the paper flow and increase its accessibility.
- Figure 2 can be clearer with respect to rows and columns -- this is the attention matrix -- what is its size/can the axes be labeled?

### Questions
- Why are the gaps between FA/FA-2 different with Cutlass versus in Triton, if the authors were to speculate? Further, the comparison in section 4.1 can be clarified -- is the assertion that the performance of the vanilla CUDA implementation of FlashAttention and the Cutlass FlashAttention implementation in xformers are congruent?
- The authors might also consider mentioning in the manuscript what they think trends in changing GPU hardware will mean for FA-2's general direction. Given that HBM bandwidth is not improving as quickly as SM arithmetic latency and that the amount of vram available on GPUs is not increasing, how will the approaches used in FA-2 change in relevance over time?
- Do you think a compiler could realistically generate FA-2? What sort of cost models might be required?
- How does FA-2 function when there is no explicit sequence length dimensions? In many training setups, tokens are padded without sequence boundaries, and models learn end-of-sequence tokens implicitly. What is the default behavior in this regime?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes FlashAttention-2 which improves upon FlashAttention by introducing "tweaks" to improve performance on GPUs.   The paper claims the tweaks improve performance by increasing occupancy and use of matrix-multiply hardware (tensor cores).  The paper reports a bit under $1.3\times$ wall clock speedup versus FlashAttention.

### Strengths
Improving training speed of LLMs is of great interest to many.

### Weaknesses
Could do a better good job explaining how a given "tweak" helps achieve a given improvement (occupancy, use of tensor cores).

Regarding the equation at the top of Page 5, I am unclear "$\mbox{diag}(l^{(1})^{-1}$" is to the power -1.  Comparing to the prior equation seems like exponent of -1 should be 1.

I think it would help some readers (like me) understand the contribution a bit better if the paper briefly summarized the key changes in the six (unnumbered) equations on Page 5 that are described as the "online softmax trick" versus the six on Page 3.  

How do the "tweaks" in Section 4.1.1 help reduce non-matrixmul FLOPs?  I know a fair amount about tensor cores, but it wasn't obvious to me.

The paper claims occupancy is increased on Page 6 but it was unclear: (i) what definition of occupancy is being used (GPU resources could mean many things and occupancy often just refers to number of warps that can concurrently run versus max number supported by hardware ); and (ii) whether any measurement has been made to confirm the claimed improvement (e.g., using NVIDIA Parallel Nsight or similar approaches for collecting performance counters).

Much of Algorithm 1 seems similar to the original FlashAttention.  It may help summarizing which lines are different.  It would also help the reader if there was a summary of which lines lead to the reduction in non-matrixmul FLOPs and improved occupancy.

"Only at the every end of the" - typo.

For the backward pass (Section 3.1.2): It was unclear what the relevance of the paragraph on MQA and GQA is to the changes in FlashAttention-2 versus FlashAttention.  

In Figure 2, does an uncolored square mean no computation?  Does the backward pass for a given worker start right away or do workers need to synchronize between forward and backward pass?  Do you not need to compute the combined result for the forward pass before you can start the backward pass?    If you do need to wait, then how can one achieve greater than 50% use of peak performance if roughly half the compute cycles are spent waiting for the longest running forward/backward pass thread block to complete?   If you don't need to wait, why not?

I'm not sure how to relate Figure 3 to Algorithm 1 (i.e., which lines it is meant to illustrate).  From the two paragraphs above Figure 3 I get it there are two potential sources of reduced execution time: fewer shared memory accesses and fewer synchronizations (__syncthreads, I assume).  Unclear which of those matters most and why given that shared memory accesses proceed about as fast as register file accesses and synchronization with a thread block is low overhead.  

Why is FlashAttention (version 1) missing in Figure 5?

As someone who knows GPUs well, I would have liked to see more performance counter data to backup the claims of the sources of performance improvements.   I understand space is limited in the main text, but in checking the supplemental material, while it is great to see all the code, there appeared to be no PDF providing additional data or details.  Including one might have helped.

### Questions
Regarding the equation at the top of Page 5, I am unclear "$\mbox{diag}(l^{(1})^{-1}$" is to the power -1.  Comparing to the prior equation seems like exponent of -1 should be 1.

I think it would help some readers (like me) understand the contribution a bit better if the paper briefly summarized the key changes in the six (unnumbered) equations on Page 5 that are described as the "online softmax trick" versus the six on Page 3.  

How do the "tweaks" in Section 4.1.1 help reduce non-matrixmul FLOPs?  I know a fair amount about tensor cores, but it wasn't obvious to me.

The paper claims occupancy is increased on Page 6 but it was unclear: (i) what definition of occupancy is being used (GPU resources could mean many things and occupancy often just refers to number of warps that can concurrently run versus max number supported by hardware ); and (ii) whether any measurement has been made to confirm the claimed improvement (e.g., using NVIDIA Parallel Nsight or similar approaches for collecting performance counters).

Much of Algorithm 1 seems similar to the original FlashAttention.  It may help summarizing which lines are different.  It would also help the reader if there was a summary of which lines lead to the reduction in non-matrixmul FLOPs and improved occupancy.

"Only at the every end of the" - typo.

For the backward pass (Section 3.1.2): It was unclear what the relevance of the paragraph on MQA and GQA is to the changes in FlashAttention-2 versus FlashAttention.  

In Figure 2, does an uncolored square mean no computation?  Does the backward pass for a given worker start right away or do workers need to synchronize between forward and backward pass?  Do you not need to compute the combined result for the forward pass before you can start the backward pass?    If you do need to wait, then how can one achieve greater than 50% use of peak performance if roughly half the compute cycles are spent waiting for the longest running forward/backward pass thread block to complete?   If you don't need to wait, why not?

I'm not sure how to relate Figure 3 to Algorithm 1 (i.e., which lines it is meant to illustrate).  From the two paragraphs above Figure 3 I get it there are two potential sources of reduced execution time: fewer shared memory accesses and fewer synchronizations (__syncthreads, I assume).  Unclear which of those matters most and why given that shared memory accesses proceed about as fast as register file accesses and synchronization with a thread block is low overhead.  

Why is FlashAttention (version 1) missing in Figure 5?

As someone who knows GPUs well, I would have liked to see more performance counter data to backup the claims of the sources of performance improvements.   I understand space is limited in the main text, but in checking the supplemental material, while it is great to see all the code, there appeared to be no PDF providing additional data or details.  Including one might have helped.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
