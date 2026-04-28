# S2-Attention: Hardware-Aware Context Sharding Among Attention Heads

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Sparse attention, which selectively attends to a subset of tokens in the context, has been an established approach to enhance the efficiency of Transformers. 
However, its theoretical reduction in FLOPs has rarely translated into wall-clock speed-up over its dense attention counterparts, mainly due to the lack of hardware-level optimizations like FlashAttention.
Meanwhile, it remains unclear wheter sparse attention can maintain the model's quality at a scale of today's large language models (LLMs), and how this can be achieved.
This paper presents Sparsely-Sharded(S2) Attention, a Triton library that provides kernel optimization for sparse attention customizable at both per-head and per-context-range levels.
S2-Attention enables the exploration of novel and high-performance sparse attention techniques, which we demonstrate through extensive ablations across a wide range of sparse attention deisngs at various model scales. 
From these insights, we present several basic guidelines to design sparse attention that can achieve not only practical efficiency improvements, but also strong performance on downstream tasks.
To achieve high parallelization and optimized memory IO, sparse attention should \textbf{shard the context heterogeneously across attention heads}, where each head attends to a different subset of tokens while \textbf{collectively covering the full context}. Meanwhile, we find hybrid architectures combining sparse and dense attention particularly beneficial in practice.
These design choices lead to a novel sparse attention architecture,
which we evaluate with 1.3B, 7B models.
It achieves wall-clock speedup of 8.79X, 15.87X, 25.3X compared to the strong FlashAttention-2 baseline with strong downstream performance on-par with full attention and perfect retrieval performance at a 128k context length. 
In inference, for 7B models, our model, with the help of our S2-Attention kernel, achieves 4.5x speed-up compared to dense counterparts. 
S2-Attention will be released with easy-to-customize APIs for direct usage in Megatron and vLLM. 
We hope they will help future research develop sparse attention algorithms to improve the efficiency of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a Triton-based GPU kernel library designed to enhance the efficiency of sparse attention training and inference. By merging query blocks and splitting along head dimensions, the library improves GPU warp utilization, particularly for fine-grained sparse attention patterns. With this library, the authors propose a KV-cache-efficient heterogeneous sparse attention method, showing the performance and efficiency benefits of the library.

### Strengths
1. Useful libarary. The paper implements a practical sparse attention GPU kernel library that supports both training and inference. The flexibility to support fine-grained sparse patterns can benefit future research towards more effective and efficient sparse pattern design.
2. High efficiency. With the optimized sparse attention kernel, the paper shows speedups of up to 25.3 and 4.5 times for training and inference over the dense FlashAttention baseline.

### Weaknesses
1. The main concern of the paper lies in the proposed sparse attention pattern design. The proposed KV-Cache design principle seems overly conclusive and conflicts with existing works.

    a. The principle itself is not novel; similar sparse pattern designs for KV-Cache optimization have been explored extensively in prior studies, such as [1, 2]. Furthermore, recent work on retrieval-based KV-Cache reduction [3] demonstrates high performance despite contradicting this principle. It would be beneficial for the authors to revise their claims to improve rigor and acknowledge alternative approaches. Specifically, the authors should provide quantitative comparisons, such as wall-clock speedups, against the performance of methods like those in [3] which have demonstrated significant speedups over optimized baselines like FlashInfer. The lack of such comparisons makes it difficult to assess the true novelty and contribution of the proposed approach.

    b. The deduction of the claim "the sparse patterns should be based on absolute positions rather than relative ones" is confusing. It is unclear why the "vertical line" sparse pattern leads to absolute positions, and why windowed attention is the only exception. The explanation lacks a clear, step-by-step logical argument. For instance, it's not clear how the vertical line pattern inherently enforces absolute positioning, or why other sparse patterns cannot be implemented with similar memory access patterns. The authors should provide a more detailed explanation of the relationship between the chosen sparse pattern and memory access efficiency.

2. The advantages of the proposed heterogeneous context sharding pattern over existing designs are not clearly shown. Additionally, it is unclear how this pattern adapts to varying input lengths, as the ranges of context shards appear pre-defined and fixed. The paper does not clearly articulate how the sharding strategy dynamically adjusts to different input lengths, or how the pre-defined shard ranges are determined. A more detailed explanation of the adaptive mechanism and its performance across various input lengths is needed.

3. The performance comparison with other sparse attention kernels is not shown. Beyond dense attention methods, it would be valuable to assess the proposed kernel’s performance against other sparse attention methods with GPU kernels, such as those optimize prefill [4] and decode [5]. The paper should include a comparison against other sparse attention kernels, including those that optimize prefill and decode stages, to demonstrate the proposed kernel's performance relative to the state-of-the-art in sparse attention.

4. Minor writing issues: 

    a. Gramma and typo: Spelling mistake in section 3.1: imrpvoes -> improves; in section 5.1: th -> the

    b. Clarity: In the abstract, it should be specified that the “8-25x speedup” refers to training time.

### Questions
1. How does the efficiency of the proposed sparse attention kernel compare to that of other sparse attention methods?
2. In what ways does the proposed sparse attention pattern adapt to varying input lengths, and what is its performance across different lengths?
3. Given that the kernel dedicatedly optimized for fine-grained sparse patterns, how does the fine-grained sparse pattern impact model accuracy? What are the performance-efficiency trade-offs at different granularities for the proposed kernel compared to others?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces S2-Attention, a Triton-based library designed to optimize sparse attention in large language models (LLMs). Traditional sparse attention methods reduce FLOPs but fail to deliver real-world speedups due to memory access inefficiencies. S2-Attention addresses this with customized kernel optimizations, enabling flexible and efficient sparse attention patterns at per-head and per-context levels. 

Key contributions include:
1. S2-Attention uses a novel method of context sharding across attention heads, maximizing parallelization and improving memory access efficiency.
2. By combining sparse and dense layers, S2-Attention achieves performance on par with dense attention models while accelerating training and inference.
3. The library achieves up to 25.3x speedup over FlashAttention-2 in 7B models and provides substantial efficiency gains across different model sizes and context lengths.

### Strengths
1. The paper presents a novel approach to improving the real-world efficiency of sparse attention mechanisms in LLMs through S2-Attention, a customizable, hardware-optimized library. Unlike prior sparse attention methods that often fail to deliver actual speedups, S2-Attention effectively addresses the GPU memory access bottleneck. Additionally, the hybrid architecture combining sparse and dense layers is an innovative solution to balance efficiency and model performance.
2. The paper demonstrates high-quality research with extensive benchmarking and thorough evaluations that underscore S2-Attention's performance benefits. The experiments cover a range of model sizes (e.g., 1.3B and 7B models) and contexts, showing both training and inference gains across different configurations. The authors also offer a clear implementation path in Triton, indicating that the work is robustly engineered for real-world applications.
3. By achieving up to 25.3x speedup over FlashAttention-2 and providing easy-to-use APIs for integration into frameworks like Megatron and vLLM, S2-Attention has the potential to become a standard tool for optimizing sparse attention in LLMs.

### Weaknesses
The paper is innovative in its approach and thorough experimentation. However, there are several critical questions that I raised in the "Question" section, which I believe are essential for the clarity and robustness of the findings. I hope the authors can provide insights on these points, and I look forward to further discussion.

 1. I am also a researcher specializing in hardware optimizations for Transformers, and I recognize the importance of sparse attention. Due to the self-attention mechanism in Transformers, there is significant redundancy since token-to-token similarities vary in each head’s activation, and sparse attention can help reduce this. However, because operations across heads are independent in Transformers, applying different attention sparsity patterns to each head does not traditionally contribute much to overall model acceleration. Each head has a different computational overhead, leading to an imbalance. Ultimately, the runtime is dictated by the head with the highest computational complexity. In Figure 1, the 'S2-Attention' subfigure seems to illustrate this issue, but it doesn’t appear that the authors discuss this challenge in the library design. Could the authors clarify if this imbalance was considered and, if so, how it was addressed?

 2. In Section 3.2, the authors mention that "retaining or masking every 64 tokens" allows the dense portion of sparse attention to fill each block. However, in Section 3.1, they state that "each warp contains 32 threads." The values of 32 and 64 seem contradictory. Is there a relationship between the 64-token blocks and the 32-thread warps, or are these independent design choices?

 3. In Figure 2(b), the authors seem to indicate that with a 32K context length, the “depth perfect” remains at 100% regardless of the token limitation. How is “depth perfect” defined in this context? It doesn’t appear to be referenced or defined elsewhere in the paper. Could the authors clarify? The same question for Figure 6(c)(d).

 4. In Figure 3, what is the control logic for data movement in MergeQ? Does it follow a fixed pattern? What kind of memory control logic is used in the SRAM for this process? Are the authors implementing in-memory computation within the SRAM, and is the softmax operation also executed within SRAM? Could you please provide a more detailed explanation of the MergeQ process, perhaps with a step-by-step breakdown or a flowchart illustrating the control logic and data movement?

 5. Lastly, could the authors clarify how many hardware measurements were conducted to obtain the reported results? Given the inherent variability in hardware performance, multiple measurements are typically necessary to ensure stability and reliability. It would be helpful to understand the stability of the hardware results presented. Could you please provide details on the number of runs performed for each experiment, any measures taken to account for variability (e.g., averaging results, reporting standard deviations), and how you ensured the stability and reproducibility of your hardware measurements?

### Questions
1. I am also a researcher specializing in hardware optimizations for Transformers, and I recognize the importance of sparse attention. Due to the self-attention mechanism in Transformers, there is significant redundancy since token-to-token similarities vary in each head’s activation, and sparse attention can help reduce this. However, because operations across heads are independent in Transformers, applying different attention sparsity patterns to each head does not traditionally contribute much to overall model acceleration. Each head has a different computational overhead, leading to an imbalance. Ultimately, the runtime is dictated by the head with the highest computational complexity. In Figure 1, the 'S2-Attention' subfigure seems to illustrate this issue, but it doesn’t appear that the authors discuss this challenge in the library design. Could the authors clarify if this imbalance was considered and, if so, how it was addressed?
2. In Section 3.2, the authors mention that "retaining or masking every 64 tokens" allows the dense portion of sparse attention to fill each block. However, in Section 3.1, they state that "each warp contains 32 threads." The values of 32 and 64 seem contradictory. Is there a relationship between the 64-token blocks and the 32-thread warps, or are these independent design choices?
3. In Figure 2(b), the authors seem to indicate that with a 32K context length, the “depth perfect” remains at 100% regardless of the token limitation. How is “depth perfect” defined in this context? It doesn’t appear to be referenced or defined elsewhere in the paper. Could the authors clarify? The same question for Figure 6(c)(d).
4. In Figure 3, what is the control logic for data movement in MergeQ? Does it follow a fixed pattern? What kind of memory control logic is used in the SRAM for this process? Are the authors implementing in-memory computation within the SRAM, and is the softmax operation also executed within SRAM? Could you please provide a more detailed explanation of the MergeQ process, perhaps with a step-by-step breakdown or a flowchart illustrating the control logic and data movement?
5. Lastly, could the authors clarify how many hardware measurements were conducted to obtain the reported results? Given the inherent variability in hardware performance, multiple measurements are typically necessary to ensure stability and reliability. It would be helpful to understand the stability of the hardware results presented. Could you please provide details on the number of runs performed for each experiment, any measures taken to account for variability (e.g., averaging results, reporting standard deviations), and how you ensured the stability and reproducibility of your hardware measurements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper first introduces a Triton library that implements sparse attention customizable at both per-head and per-context-range levels, and then proposes Sparsely-Shardded (S2) Attention which shards the context heterogeneously across attention heads but collectively covers the full context. The evaluation show that the proposed S2-Attention can achieve 2.5X training speed-up and 4.5X inference speed-up for a 7B transformer architecture design.

### Strengths
+ this work presents a flexible kernel implementation that supports finer-grained sparse attention. Previous work FlashAttention-2 requires the sparsity granularity to be same as the block size, while this work introduces Merge-Q technique to effectively decouple the granularity of sparsity pattern and attention computation while achieving the expected speedup.
+ this work provides a detailed accuracy comparison to demonstrate the effectiveness of heterogeneous context sharing and union completeness.

### Weaknesses
 - S2-Attention requires training models from scratch, raising concerns about its compatibility with pre-trained models. This limits its flexibility compared to other sparse attention methods  (e.g., QUEST, H2O) that support plug-and-play integration.
- the benefits of supporting finer-grained sparsity remain unclear; if existing block sparse attention methods suffice, the proposed library may be less practical.

### Questions
My questions are listed in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Sparsely-Sharded (S2) Attention, a Triton-based library that optimizes sparse attention mechanisms for large language models (LLMs) by selectively attending to subsets of tokens. It proposes sharding context heterogeneously across attention heads to achieve higher parallelism and memory efficiency while maintaining strong downstream performance. Additionally, the paper demonstrates that hybrid architectures combining sparse and dense attention are particularly effective. Extensive experiments showcase the proposed attention mechanism’s significant wall-clock speedups and accuracy comparable to dense attention methods.

### Strengths
**Significant Performance Gains**: S2-Attention achieves impressive wall-clock speedups (8.79x, 15.87x, and 25.3x), outperforming FlashAttention-2 and maintaining strong downstream performance.

**Memory and Computation Efficiency**: The method offers higher parallelization and optimized memory I/O, crucial for large-scale models, especially when handling high token lengths.

**Real-World Applicability**: The library is designed to integrate with popular LLM frameworks (e.g., Megatron, vLLM) and provides user-friendly APIs, enhancing its usability for practitioners.

### Weaknesses
 **Lack of Performance Comparison on Larger Models**: While the paper demonstrates hardware benefits on large-scale models, especially with high token lengths, it lacks the corresponding task performance comparisons. The experiments are limited to a 1.3B parameter model, which does not fully validate the effectiveness of the proposed method on larger models where the benefits of sparse attention are expected to be more pronounced. Specifically, the paper should include task performance results on models with 7B parameters or more, which are more representative of current large language models.

**Paper Organization and Writing Issues**: There are several grammatical issues and unclear figure descriptions, which hinder the readability and understanding of the paper. For example:
1. The caption of Figure 5 only explains Figure 5(a) and lacks descriptions for Figure 5(b).
2. The legends in Figure 8 are too small to read. Additionally, there is an issue with the label on the y-axis of Figure 8(b). These issues make it difficult to understand the results and replicate the experiments.


### Questions
1. Although this paper highlights its advantages for large-scale models, especially with high token lengths, it only provides task performance results on Llama2-1.3B with a maximum sequence length of 8192, which somewhat limits the validation of its overall effectiveness.

2. Table 1 lists various S2-Attention variants, each with different task performance. Could the authors clarify which S2-Attention variant was used to measure the speedup and throughput in the subsequent experiments?

3. The paper reports both backward latency and end-to-end training speedup, validating its effectiveness for a single step. However, I would like to know if the sparse models proposed here require the same number of training steps to converge as dense models, so that the benefits extend to the total training time as well.

4. Since memory reduction is another key advantage of sparsity, it would be helpful to include comparisons in terms of GPU memory reduction for the proposed S2-Attention.

### Soundness
2

### Presentation
2

### Contribution
3
