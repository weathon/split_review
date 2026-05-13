# A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
In modern large language models (LLMs), increasing the context length is crucial for improving comprehension and coherence in long-context, multi-modal, and retrieval-augmented language generation. 
While many recent transformer models attempt to extend their context length over a million tokens, they remain impractical due to the quadratic time and space complexities.
Although recent works on linear and sparse attention mechanisms can achieve this goal, their real-world applicability is often limited by the need to re-train from scratch and significantly worse performance. In response, we propose a novel approach, Hierarchically Pruned Attention (HiP), which reduces the time complexity of the attention mechanism to $O(T \log T)$ and the space complexity to $O(T)$, where $T$ is the sequence length. 
We notice a pattern in the attention scores of pretrained LLMs where tokens close together tend to have similar scores, which we call "attention locality". Based on this observation, we utilize a novel tree-search-like algorithm that estimates the top-$k$ key tokens for a given query on the fly, which is mathematically guaranteed to have better performance than random attention pruning. In addition to improving the time complexity of the attention mechanism, we further optimize GPU memory usage by implementing KV cache offloading, which stores only $O(\log T)$ tokens on the GPU while maintaining similar decoding throughput. Experiments on benchmarks show that HiP, with its training-free nature, significantly reduces both prefill and decoding latencies, as well as memory usage, while maintaining high-quality generation with minimal degradation.
HiP enables pretrained LLMs to scale up to millions of tokens on commodity GPUs, potentially unlocking long-context LLM applications previously deemed infeasible.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Hierarchically Pruned Attention (HiP) to reduce the time complexity of attention to O(T logT) and space complexity to O(T) where T is the sequence length. By exploiting the continuity of token sequence (tokens close together tend to have similar scores), for each query, the HiP use a tree-search like algorithm to approximately search the top k key tokens that yield large attention weights. Further, the author developed a KV cache offloading scheme to offload KV cache to host memory and reduce the GPU memory usage.

### Strengths
1. The proposed method uses iterative refinement to dynamically and approximately locate top k tokens, which is interesting. 
2. HiP shows promising efficiency improvement with only small performance drop. 
3. The appendix provides a lot of ablation study to study the behavior of the proposed method. 
4. The method is training free.

### Weaknesses
1. It would be easier to understand to have a figure illustration showing the tree search (or improve figure 2, the figure 2 step 1 is a bit confusing) for section 3.1. 
2. The algorithm divides the sequence into k segments, and one token will be selected in each segment. Is it correct? If so, then the top k tokens must be distributed in the sequence, and cannot be concentrated on certain regions. Why do you make this design choice? 
3. I am aware of some literatures that also use iterative refinement to dynamically calculate attention for efficiency. Have the authors tried to compare to these literatures?

### Questions
1. It would be easier to understand to have a figure illustration showing the tree search (or improve figure 2, the figure 2 step 1 is a bit confusing) for section 3.1. 
2. The algorithm divides the sequence into k segments, and one token will be selected in each segment. Is it correct? If so, then the top k tokens must be distributed in the sequence, and cannot be concentrated on certain regions. Why do you make this design choice? 
3. I am aware of some literatures that also use iterative refinement to dynamically calculate attention for efficiency. Have the authors tried to compare to these literatures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Hierarchically Pruned Attention (HiP) which reduces time and space complexity of the attention mechanism. HiP exploits "attention locality" to estimate top-k key tokens (w/ theoretical justifications as insights) for a given query and does so in a hardware aware way. Moreover, the paper introduces a further KV cache offloading steps which reduces space complexity further.

### Strengths
* The method being training-free means it can be used as a drop-in to already trained models.
* The paper does careful complexity analysis of its claims but strikes a balance on introducing information in a way to aid presentation (thinking of the informal theorem) while still being rigorous later. 
* It is extremely valuable to have code examples and implementation released.
* The paper is extremely comprehensive when understanding its metrics across different hardware and comparing with the many version of flash attention.

### Weaknesses
 * It would be great to have the long context benchmarks also for different models -- gemma and mistral are both open source and around similar sizes.

 * It would be beneficial to see a more comprehensive evaluation of the method across a broader range of tasks beyond MMLU, particularly those that are more sensitive to long-range dependencies and reasoning. While MMLU is a good benchmark for general knowledge, it may not fully capture the nuances of performance in tasks requiring complex contextual understanding.

### Questions
* Gemma 2 uses this mix between sliding window and normal attention. it would be great to understand if there are any degradation on non-llama architectures.
* The method does show that MMLU is not degraded when using this method. It would be interesting to see this for a broader set of metrics if possible.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel, training-free attention mechanism called Hierarchically Pruned Attention (HiP) to accelerate the serving of pre-trained Transformer-based large language models (LLMs) for long-context tasks. HiP addresses the computational challenges posed by the quadratic time and space complexity of standard attention mechanisms in handling long sequences.

### Strengths
1. HiP's training-free nature eliminates the need for costly retraining of large LLMs, making it readily applicable to existing models.
2. HiP's hierarchical pruning significantly reduces the computational complexity of attention from quadratic to log-linear, enabling efficient handling of long sequences.
3. KV cache offloading effectively addresses the memory limitations of GPUs, allowing HiP to scale to much longer context lengths.
4. The paper provides thorough experimental results on diverse benchmarks, showcasing HiP's effectiveness in terms of speedup, performance preservation, and context length extension.
5. The paper includes a theoretical analysis of HiP's hierarchical pruning algorithm, providing insights into its superior performance compared to random key selection.

### Weaknesses
1. HiP's effectiveness relies on the assumption of attention locality. While this assumption generally holds, there might be cases where it's violated, potentially impacting performance. Specifically, the paper does not explore scenarios where long-range dependencies are critical, such as tasks requiring reasoning over distant parts of the input sequence. The method's performance in such cases is unclear and needs further investigation.

2. HiP enforces the same sparsity across all rows of the attention matrix. This static sparsity pattern might not be optimal for all input sequences. The paper should explore dynamic sparsity mechanisms that adapt the sparsity pattern based on the input, potentially leading to better performance and efficiency. For example, the sparsity could be made dependent on the magnitude of attention weights or the importance of tokens.

3. The implementation and optimization of HiP, particularly the KV cache offloading, are tailored for specific hardware platforms (e.g., RTX 4090). While the paper presents results on other hardware, the optimization process is not detailed enough to ensure portability and optimal performance across diverse hardware accelerators. The paper should provide more details on the optimization process and how it can be adapted to different architectures. It is unclear how the autotuning is implemented and how it will be available to other researchers.

4. The paper doesn't specifically address potential LLM alignment issues that might arise from applying HiP. The changes to the attention mechanism could potentially alter the model's behavior, leading to unintended consequences. Further investigation is needed to ensure HiP's safety and robustness in practical deployments, especially in sensitive applications.

### Questions
1. How does the choice of chunk sizes in HiP's hierarchical pruning affect the trade-off between accuracy and efficiency?
2. What strategies can be employed to further optimize KV cache offloading, such as using different memory tiers or compression techniques?
3. How well does HiP integrate with other efficiency techniques, such as quantization or model pruning, to further improve serving efficiency?
4. Can HiP be effectively applied to other Transformer architectures beyond the specific LLM model used in the paper?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents HiP (Hierarchically Pruned Attention), a novel approach aimed at reducing the time and space complexity of the attention mechanism in Large Language Models (LLMs). HiP leverages the observation that tokens close together tend to have similar attention scores to estimate the top-k key tokens for a given query on the fly. This results in sub-quadratic time complexity (O(T log T)) and linear space complexity (O(T)), where T is the sequence length.  Experimental results show that HiP significantly reduces both prefill and decoding latencies while maintaining high performance on benchmarks such as LongBench.

### Strengths
1. HiP does not require retraining, making it easy to apply to pre-trained models. In addition, by reducing the time complexity to O(T log T) and space complexity to O(T), HiP enables the use of longer context lengths without the associated quadratic cost.
2. Through KV-cache offloading, HiP optimizes GPU memory usage, which is especially beneficial for large models.
3. HiP can dynamically adjust to different sequence lengths, making it suitable for a variety of tasks that involve long contexts.

### Weaknesses
1. The effectiveness of HiP is contingent upon the presence of "attention localities," which might vary across different LLM architectures or tasks. The robustness of this operation deserves more discussions. Specifically, the paper should include a more detailed analysis of how the locality assumption holds across different model sizes, pre-training datasets, and downstream tasks. It is not sufficient to simply state that locality exists; the degree to which it exists and its impact on performance should be quantified and discussed.
2. While HiP reduces latency in the decoding phase, the iterative pruning process might introduce overhead in the initial stages. How does the proposed method balance these two parts. It would be beneficial to see a breakdown of the latency contributions from the pruning process versus the actual attention computation, especially during the initial prefill stage. This would help to understand the trade-offs involved and identify potential bottlenecks.
3. The authors have already shown improvements for certain sequence lengths, while it is expected to thoroughly explore how HiP scales to extremely long sequences or very large models. The current configuration on the sequence length (128k) and the model size (8B) are relatively small for a paper studies on the efficient decoding. Alternatively speaking, the scalability of this method deserves more experiments to support. The paper should include experiments with significantly larger models (e.g., 100B+ parameters) and longer sequence lengths (e.g., 1M+ tokens) to demonstrate the true scalability of HiP. Furthermore, the paper should discuss the memory and computational requirements of HiP as the model size and sequence length increase.

### Questions
See the weakness for details.

### Soundness
2

### Presentation
3

### Contribution
3
