# CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 10, 6

## Abstract
Large language models (LLMs)' proficiency in handling long sequences boosts KV caching demand. Recent efforts to evict KV cache have alleviated the burden for inference, but they often fail to allocate resources rationally across layers with different attention patterns. In this paper, we introduce Cascading and Adaptive KV cache Eviction (CAKE), a method that significantly improves LLM inference efficiency by optimizing KV cache eviction through an adaptive cache allocation strategy implemented via a cascading cache management and an innovative eviction indicator. We approach KV cache eviction as a ``cake-slicing problem,'' assessing each layer's KV cache needs by considering attention dynamics in both spatial and temporal dimensions. During the prompt prefilling, CAKE allocates rational cache size for layers by analyzing layer-specific KV cache preferences and manages the memory budgets with the guidance of these preferences in a cascading manner. This approach allows for a global view of cache size allocation, distributing resources optimally based on the diverse attention mechanisms across layers. Also, we've designed a new eviction indicator that considers the shifting importance of tokens over time, addressing a limitation in existing methods that often overlook temporal dynamics. Our comprehensive experiments on the LongBench and NeedleBench datasets show that CAKE is capable of preserving the performance of models when retaining only 3.2\% KV cache and consistently outperforms current baselines across various models and memory constraints, especially in low-memory situations. Moreover, CAKE outperforms full cache with FlashAttention implementation, achieving 10$\times$ faster decoding for 128K-token sequences and maintaining consistent decoding speed across sequence lengths.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Cascading and Adaptive Key-value cache Eviction (CAKE) method for optimizing Key-Value cache evicting in large language models. Specifically, CAKE assesses each layer’s KV cache needs by considering attention dynamics in both spatial and temporal dimensions. During the prompt prefilling, CAKE allocates rational cache size for layers by analyzing layer-specific KV cache preferences and manages the memory budgets with the guidance of these preferences in a cascading manner. Besides, CAKE introduces a novel eviction indicator that accounts for both the long-term influence and temporal variability of token importance. Extensive experiments demonstrate CAKE’s superior performance across different models and memory constraints, especially in low-memory scenarios.

### Strengths
(1)	This paper provides a novel and practical key-value cache eviction approach to enhance LLM’s proficiency in handling long sequences, based on layer-specific KV cache preferences in a cascading manner.

(2)	The paper is well-organized, and the writing is clear. In particular, Figure 2 clearly points out the differences between the proposed CAKE and other existing models, and I find almost no typos in this paper.

(3)	The theoretical analysis (e.g. Theorem 2) rigorously demonstrates the equivalent KV cache eviction results of the proposed preference-guided cascading cache management to the vanilla preference-prioritized adaptive allocation strategy.

(4)	The extensive experiments on several open-source LLM benchmarks truly validate the effectiveness of the proposed algorithms.

(5)	Overall, the proposed algorithm CAKE model is novel, practical and efficient. The corresponding experimental results are extensive and sound.

### Weaknesses
(1)	The abbreviation “KV” in the title and abstract (e.g. line 12, or the second line of abstract) should be clearly written as “Key-value”, as this word appears for the first time in the whole paper.

(2)	In line 23, the abstract section says “this approach allows for a global view of cache size allocation, distributing resources OPTIMALLY”. The word “optimally” is somewhat controversial, until you can demonstrate rigorously from a theoretical point that the proposed resources distribution method is optimal (with respect to certain theoretical property). Therefore, I would suggest to use less controversial word, like “adaptively”.

(3)	Equation (4) is a little confusing for me. Since $A[i,:]$ is a row vector, $\log{A[i,:]}$ is also a row vector, then is $ A[i,:] \log{A[i,:]}$ the inner product of these two vectors? Should give more clear explanations.

(4)	I read the proofs line by line, and according to my experience, the proof is sound. However, since the proof of Theorem 1 is truly basic and short, I believe it will be better to describe “Theorem 1” as a proposition. Besides, in Theorem 1, “For layer $l \in [L]$”, does it mean for any (fixed) layer, or mean there exists a layer? More explanations should be clarified.

(5)	In Table 1 of the experimental results, the proposed CAKE obtains SOTA results in most benchmark datasets. But in some benchmarks, some existing models like TOVA and SnapKV can achieve better results. Could you give more analysis in which kind of benchmark datasets can CAKE obtain better experimental results than the existing baselines?

### Questions
In Table 1, CAKE could not outperform existing methods on some benchmarks. Could you give more analysis in which kind of benchmark datasets can CAKE obtain better experimental results than the existing baselines? Or in what situations, CAKE will fail to achieve good results?

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
2

### Summary
This paper introduces a method for optimizing KV cache eviction through a cache allocation strategy to enhance LLM inference efficiency. The proposed cache allocation adapts to layer preferences, adjusting KV cache injection to improve efficiency while maintaining satisfactory performance. Extensive experiments are conducted to demonstrate the method’s effectiveness.

### Strengths
The paper is well-written, with clear motivations for the proposed method and pipeline illustrations. Incorporating layer-wise preference modeling to guide KV caching strategies is intuitive, given the insights from attention dynamics analysis.

The proposed method is straightforward and compatible with existing KV caching strategies, making it easy to integrate while achieving decent efficiency. The authors provide ample experiments to substantiate this point.

Empirical analysis is comprehensive, covering 16 tasks with various LLMs of different specifications, offering a comprehensive evaluation.

### Weaknesses
Most empirical analyses focus on smaller LLMs with 7B-8B parameters, which may limit the generalizability of this approach for much larger LLMs. Specifically, it would be valuable to see how computational costs and performance are impacted across different LLM sizes.

The empirical improvements over existing baselines are relatively modest, which could suggest limited practical advantages in some cases.

### Questions
Please see weakness aspects above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
A novel technique that solves KV cache management to improve computational efficiency considering spatial and temporal attention dynamics. 10× faster decoding for extended sequences. Layer-wise memory budget allocation.

### Strengths
S1. Identified and visualized the attention dynamics in spatial and temporal axis

S2. Strong empirical analysis on multiple datasets

S3. Actual improvement in inference latency

S4. Excellent presentation (great paper flow and beautiful figures)

### Weaknesses
I do not identify any major weaknesses of the paper.

### Questions
Q1. I'm just curious how this technique could scale to larger models (no need to verify it empirically)

Q2. Could this technique potentially help transformers stay competitive against RNN-based models like Mamba?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces CAKE, a method for efficient KV cache management in LLMs that enhances inference by dynamically allocating cache based on each layer’s spatial and temporal attention demands. By framing cache eviction as a cake-slicing problem, CAKE optimally distributes resources across layers and incorporates a novel eviction indicator to account for the shifting importance of tokens over time. Extensive experiments show the potentials of CAKE.

### Strengths
- Pioneering Adaptive Memory Budgets: CAKE is the first work to consider adaptive memory budgets for different layers of LLMs. This innovative approach allows for more efficient memory utilization, improving model performance by allocating resources where they are most needed.

- Addressing KV Cache Compression: The paper tackles the timely problem of KV cache compression in LLMs, which is especially relevant for on-device applications. By focusing on this issue, the work makes LLMs more practical and accessible in resource-constrained environments.

- Clear Writing: The overall writing is clear, though the paper structure is a bit chaotic. This clarity facilitates comprehension, replication, and further research based on the paper's findings.

### Weaknesses
 - The motivation for using spatial dispersion and temporal shift in cache size allocation is unclear. Providing more insights or intuition would help clarify its benefits. Additionally, Table 2 shows that the adaptive allocation strategy provides minimal improvement, suggesting it may not be necessary.

- The adaptive KV compression method is incompatible with flash-attention. Given that flash-attention is widely adopted for efficient training and inference of LLMs, it’s unlikely that practitioners would choose CAKE over flash-attention in practice.

- Only two LLM backbones, Llama and Mistral, were evaluated, which may be insufficient. Consider adding another backbone, such as Phi, Qwen, or Gemma, to strengthen the analysis.

- The team has not open-sourced their code, which could raise concerns about the reproducibility of their work.

- The baseline methods used for comparison are not sufficiently strong. Consider including the following more robust methods (For KVQuant[1] and KIVI[2] should be jointly used with the flash-attention, and GEAR could remain the original settings):

[1] Hooper, Coleman, et al., "Kvquant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization." arXiv preprint arXiv:2401.18079 (2024).

[2] Liu, Zirui, et al., "KIVI: Plug-and-Play 2bit KV Cache Quantization with Streaming Asymmetric Quantization." (2024).

[3] GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
2

### Contribution
2
