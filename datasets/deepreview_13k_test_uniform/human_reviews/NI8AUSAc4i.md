# LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
The Key-Value (KV) cache is a crucial component in serving transformer-based autoregressive large language models (LLMs), enabling faster inference by storing previously computed KV vectors. However, its memory consumption scales linearly with sequence length and batch size, posing a significant bottleneck in LLM deployment.
Existing approaches to mitigate this issue include: (1) efficient attention variants integrated in upcycling stages, which requires extensive parameter tuning thus unsuitable for pre-trained LLMs; (2) KV cache compression at test time, primarily through token eviction policies, which often overlook inter-layer dependencies and can be task-specific.

This paper introduces an orthogonal approach to KV cache compression. 
We propose a \textit{low-rank approximation} of  KV weight matrices, allowing for plug-in integration with existing transformer-based LLMs without model retraining.
To effectively compress KV cache at the weight level, we adjust for layerwise sensitivity and introduce a \textit{progressive compression} strategy, which is supported by our theoretical analysis on how compression errors accumulate in deep networks. Our method is designed to function without model tuning in upcycling stages or task-specific profiling in test stages.
Extensive experiments with LLaMA models ranging from 8B to 70B parameters across various tasks show that our approach significantly reduces the GPU memory footprint while maintaining performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a low-rank compression approach (LORC) for large language models (LLMs) to efficiently manage the Key-Value (KV) cache, crucial for faster inference but memory-intensive. Traditional KV compression strategies either require model retraining, limiting practical deployment. LORC tackles this with a low-rank approximation of KV matrices, integrating progressively across layers to minimize error propagation. Experiments demonstrate substantial memory savings with minimal performance loss, providing a scalable, plug-and-play solution adaptable to pre-trained models without needing task-specific tuning.

### Strengths
1. The process of calculating sensitivity and condition number for each layer in LoRC is novel.

2. Mathematically robust proofs support the proposed method.

3. Compared to a uniform compression rate, the proposed progressive compression strategy achieves higher accuracy at the same compression rate.

### Weaknesses
**1. Latency and Throughput Experiments**

   The primary purpose of reducing KV Cache size is to decrease memory usage during inference, which ideally should lower latency or increase throughput. However, the LoRC method may introduce additional computational overhead due to:

- The need to recover the compressed KV cache, which requires extra computations.
- Frequent reading and writing of the large restored KV cache per layer for attention calculations, potentially impacting latency or throughput.
- The time required to compute sensitivity and perform SVD.

Please provide experimental results showing LoRC’s latency and throughput, including the time required for sensitivity calculations and SVD processing.

**2. Comparison with Other KV Cache Compression Methods**
   - The paper would be strengthened by a comparative analysis with other existing KV cache compression methods, including:
      - KV Cache eviction [1]
      - KV Cache quantization [2]
      - SVD-LLM [3]

Please compare LoRC's accuracy and latency at the same compression rates against these methods to highlight its unique benefits and trade-offs.

**3. (minor) Different trends in sensitivity by compression between training and inference.**

 Section 6.6 analyzes that compression in earlier layers negatively impacts inference due to the amplification of input-induced errors through forward propagation. In contrast, it is known that during training, compression in later layers tends to negatively impact accuracy [4-6]. Although the results are opposite, I think the author’s argument is reasonable as input errors amplify forward during forward propagation while input gradient errors amplify backward during backpropagation. Reflecting this point in Section 6.6 or the appendix could further strengthen the argument of the paper.

[1] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models, Neurips, 2023.
[2] ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification, arxiv, 2024.
[3] SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression, arixv, 2024.
[4] GACT: Activation Compressed Training for Generic Network Architectures, ICML, 2022.
[5] ALAM: Averaged Low-Precision Activation for Memory-Efficient Training of Transformer Models, ICLR, 2024.
[6] DropBP: Accelerating Fine-Tuning of Large Language Models by Dropping Backward Propagation, Neurips, 2024.

### Questions
The primary concern is related to the weaknesses above. If these concerns are adequately answered, I am willing to consider increasing the score to 6.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This proposes a method to reduce the memory demands of large language models (LLMs) by compressing KV caches using low-rank matrix decomposition on weights. LoRC designs a progressive compression strategy that adjusts compression rates across layers based on sensitivity to error propagation, thus providing better preservation of model performance.

This paper effectively designs a method for determining specific compression rates for each layer. However, it lacks critical measurements regarding practical acceleration and potential overheads in deployment. Without this information, it’s challenging to assess its suitability for real-world applications.

### Strengths
The progressive compression strategy effectively minimizes accuracy segregation with clear proof to demonstrate the error propagation under certain assumptions.

### Weaknesses
1. Limited Comparison with Related Work: The paper only compares LoRC to uniform compression, omitting relevant methods that leverage perplexity evaluation [1] or Hessian-based scoring [2] for deciding layer-wise compression rate for performing low-rank decomposition.
2. Lack of Measurements on Latency or Throughputs improvements: While LoRC demonstrates memory savings, it does not discuss potential gains in speed or latency—key metrics for assessing the real-world efficiency of compression methods.
3. Unclear Handling of Rotary Position Embedding (RoPE): The paper needs more clarity on the compatibility with RoPE. The author provides a brief section in Appendix C; the detailed workflow seems ambiguous, particularly on whether it must be reapplied at each step and what overhead this entails. Further explanation is crucial for models that rely on RoPE.

[1] ASVD: Activation-aware Singular Value Decomposition for Compressing Large Language Models
[2] Palu: Compressing KV-Cache with Low-Rank Projection

### Questions
1. How do you handle RoPE?
2. How much of this system is implemented and what speedups are you able to attain?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on compressing the KV cache in long-context large language models. It cleverly utilizes Singular Value Decomposition (SVD) to decompose the KV cache and employs the Q and O matrices to absorb the decomposition, thereby reducing the required cache. The writing is clear, the proposed method is highly innovative, and experiments demonstrate the effectiveness of compressing the KV cache.

### Strengths
1. The core idea of the paper is insightful, as it proposes compressing the KV cache by performing low-rank decomposition on the KV values and absorbing them into the Q and O matrices.

2. Theoretical analysis and proofs are sufficient, as the paper derives upper and lower bounds for the error through mathematical formulations.

3. The paper demonstrates effective compression results, achieving high compression ratios of the KV cache with minimal impact on performance.

4. The writing is clear, making the paper easy to understand.

### Weaknesses
1. The author directly performs SVD decomposition and reconstruction on the K and V matrices. However, in previous SVD for LLM compression work, this original method of decomposing the weight matrix without re-training it usually leads to a large performance loss (as mentioned in Pufferfish, ASVD). The paper does not clearly explain why the performance loss is small under the same approach.

2. The paper does not prove the superiority of the proposed Progressive Compression Strategy. The increase in compression ratio with layer depth does not align with findings in existing work on SVD for LLM compression (e.g., ASVD, SVD-LLM, FWSVD).

3. The rationale for using the cumulative condition number as a compression metric for each layer is not clearly demonstrated.

4. The experiments are insufficient, as the paper lacks comparisons with previous KV cache compression methods and does not evaluate models other than Llama.

### Questions
1. In the previous work on SVD for LLM compression, directly performing SVD on the weight matrix without updating the weight matrix results in a huge performance loss. Can the author explain why there is no performance loss in this work?

2. Could the authors explain why using the Cumulative Condition Number as a criterion for rank selection is reasonable?

3. The progressive compression across layers seems questionable. Previous works on automatic rank pruning (e.g., ASVD, FWSVD) do not indicate that rank should decrease with increasing layer depth. Moreover, the final layers of a model are often crucial and should not have their rank excessively reduced. While the paper presents single-layer analysis, it does not consider inter-layer dependencies. Could the authors compare the Progressive Compression Strategy with other automatic rank pruning approaches to establish its validity or superiority?

4. Could the authors conduct experiments on more models (beyond Llama) and compare with other KV cache compression methods?

### Soundness
4

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
4

### Summary
This paper introduces LoRC, a novel approach to KV cache compression that leverages the inherent low-rank properties of weight matrices. It employs a progressive layer-wise compression strategy to approximate the KV weight matrices without requiring model retraining. Experimental results demonstrate that LoRC significantly reduces GPU memory usage with minimal to no performance degradation.

### Strengths
1. The authors provide a theoretical analysis of error bounds for KV cache compression to examine a progressive compression strategy. The study indicates that compressing shallow layers less aggressively than deeper layers helps preserve model performance.

2. The authors propose a KV cache compression method using low-rank approximation of KV weight matrices for transformer-based (LLMs) without requiring model retraining.

3. The paper is well-organized and the motivation is clear.

### Weaknesses
1. By using low-rank approximation, the computational overhead should also be reduced compared to dense computation. In the experiments, I only found comparisons of compression ratio and performance. Could you provide details on your implementation for computing the attention layer? Did you use pure PyTorch? Additionally, have you tested the speedup compared to the full KV cache method?

2. The authors claims that the proposed methods enhances LLM performance in memory-constrained deployment scenarios. Are there any experiments to support it? For example, can this method be deployed on consumer GPUs with limited memory (24 GB or less) where the full KV cache model cannot fit? are there models that cannot be deployed on consumer GPUs but can be deployed using the proposed method?

### Questions
Please see the above.

### Soundness
3

### Presentation
3

### Contribution
2
