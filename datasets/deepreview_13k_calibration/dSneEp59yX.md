# Training Free Exponential Context Extension via Cascading KV Cache

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The transformer's context window is vital for tasks such as few-shot learning and conditional generation as it preserves previous tokens for active memory. However, as the context lengths increase, the computational costs grow quadratically, hindering the deployment of large language models (LLMs) in real-world, long sequence scenarios. Although some recent key-value caching (KV Cache) methods offer linear inference complexity, they naively manage the stored context, prematurely evicting tokens and losing valuable information. Moreover, they lack an optimized prefill/prompt stage strategy, resulting in higher latency than even quadratic attention for realistic context sizes. In response, we introduce a novel mechanism that leverages cascading sub-cache buffers to selectively retain the most relevant tokens, enabling the model to maintain longer context histories without increasing the cache size. Our approach outperforms linear caching baselines across key benchmarks, including streaming perplexity, question answering, book summarization, and passkey retrieval, where it retains better retrieval accuracy at 1M tokens after four doublings of the cache size of 65K. Additionally, our method reduces prefill stage latency by a factor of 6.8 when compared to flash attention on 1M tokens. These innovations not only enhance the computational efficiency of LLMs but also pave the way for their effective deployment in resource-constrained environments, enabling large-scale, real-time applications with significantly reduced latency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes an extension to attention sink by (1) blockwise prefilling to optimize the latency of this period, (2) cascading caching management. The resulting framework shows quality and latency improvement over StreamingLLM.

### Strengths
1. Prefilling observation is sound. It's good to bulk processing this stage, which StreamingLLM and H2O failed to do.
2. It's intuitionally beneficial to keep the middle context in addition to sliding window and attention sink, which the paper proves by passkey performance.

### Weaknesses
1. It's pretty tricky to manage memory in this cascading way. I would say it's challenging to manage small amount of memory, e.g., two bytes, at arbitrary locations. It's very likely to cause memory fragmentation and hurt the throughput as a result, which a practical serving system should avoid.
2. There are a few earlier and more comprehensive works (compared to StreamingLLM) that tackles the prefilling stage with sparsity, e.g., MInference[1], it would be compare against [1].
[1] MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention

### Questions
1. Related to weakness 1, is this method compatible with continuous batching? How well does the method perform compared to, or compatible with actual serving systems, e.g., vllm/sglang? 
2. Could you benchmark the latency and quality wrt to Minference? 
3. For FlashAttention, which version are you comparing to? FlashAttention-1, FlashAttention-2, or FlashAttention-3? Triton or cuda kernel?
4. What would be the memory overhead, and IO overhead for computing, storing and access the EMA for each token(and manipulate the resulting memory layout change)? Also, can this operation be fused into online softmax? It would be good to add a pseudo code section to illustrate how this part is done, e.g., based on FlashAttention logic.

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
4

### Summary
The transformer’s context window is crucial for tasks like few-shot learning, but longer contexts increase computational costs, limiting large language models (LLMs) in long-sequence tasks. Recent key-value caching methods lower complexity but often discard tokens too soon and have inefficient prefill stages, leading to high latency. To solve this, the author propose a cascading sub-cache buffer system that selectively retains relevant tokens, supporting longer context without added cache size. This method improves accuracy and reduces latency across tasks, enhancing LLM efficiency for real-time applications in resource-limited environments.

### Strengths
- The idea of cascade kv cache is simple and effective
- The design of this method carefully considered the implementation so as to get the actual speedup

### Weaknesses
The baseline may not be sufficient, most of the experiment are comparing with streamingLLM

### Questions
- How's your peformance compared with Minference?
- How's your performance compared with others on RULER task, which is a benchmark for evaluating context size

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new training-free approach which significantly extend the effective context length of LLM. The authors first introduce a strided prefill which reduces the prompt computing latency on 1M tokens by a factor of 6.8 compared to flash attention. Then illustrate their cascade KV cache maintaining mechanism. Given the same KV cache size, the cascade mechanism gains impressive improvements compared with the existing methods.

### Strengths
1. Although the idea is simple, the experiment results are very good.
2. The idea is well implemented with careful code optimization.

### Weaknesses
The experimental section would be better if the idea is evaluated on more data sets.

### Questions
I am wondering the perplexity results on more evaluation datasets.

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
4

### Summary
In order to enable LLMs to preserve a long context without increasing the KV cache size, this paper proposes a training-free KV cache eviction policy with a cascading sub-cache algorithm. The algorithm allows one sub-cache window to accept a subset of tokens evicted from the previous sub-cache. This paper also introduces a linear prefill strategy that avoids the restrictive quadratic prompt complexity during the prefill stage by processing fixed-sized chunks (strides) of the prompt.

### Strengths
1. The experiments and conclusions are sufficient, including the evaluation of latency and accuracy on different tasks and LLMs. Also, the display of the experimental figures are clear.
2. This work builds a new paradigm of KV cache with cascading sub-cache and effectively extends the context length without increasing complexity or requiring additional training. This work provides a promising solution for efficient edge-side LLM inference.

### Weaknesses
1. I understand the proposed method is a generalization (more flexible version) of sliding window attention, but the main problem is that this paper does not clearly explain why the proposed cascading sub-cache is effective for KV cache eviction (intuitively). It is better to explain more about the background of cascading structure and the key motivations/observations/insights for introducing cascading KV cache. Specifically, the paper should elaborate on why a cascading structure, as opposed to other eviction strategies, is beneficial for maintaining relevant context information. A more detailed discussion of the theoretical underpinnings of this approach would be valuable.
2. Although experiments are sufficient, the baselines are kind of weak. For example, when evaluating on LongBench, there are more recent dynamic KV cache method such as PyramidKV [1], PyramidInfer[2], InfLLM [3], Quest [4], and FastGen [5]. It will be better to compare with one/two more recent dynamic KV cache method to further support your conclusions. The current baselines do not fully capture the state-of-the-art in dynamic KV cache management, which makes it difficult to assess the true novelty and performance of the proposed method. A comparison with methods that also focus on long-context scenarios would be more appropriate.
3. In Section 3.1, it is not clear that why use trunks can achieve linear attention complexity during the prefill stage, and what is the key difference between the proposed method and FlashAttention which also uses tiling to save the memory. The paper needs to clarify how processing fixed-size chunks leads to linear complexity, and how this differs from the tiling approach used in FlashAttention. A more detailed explanation of the algorithmic differences and their impact on computational complexity is needed.
4. From Section 3.2, each sub-cache relies on the previous sub-cache. The sequential procedure seems to have an impact on the inference efficiency. How to avoid this problem and achieve much higer efficiency compared with StreamingLLM. The paper should address the potential bottleneck caused by the sequential nature of the cascading sub-caches. A discussion on how to mitigate this issue and achieve higher efficiency compared to methods like StreamingLLM is necessary. This could involve techniques like parallel processing or optimized data transfer between sub-caches.
5. Token selection algorithm leverages exponential moving average (EMA) to track the historical attention score. This method seems similar to directly using accumulated attention score proposed by H2O. Can I understand this process as considering the different importance degrees of current and historical attention score based on the method of H2O, which is controlled by the hyper-parameter gamma. The paper should provide a more in-depth analysis of the token selection algorithm, comparing it to alternative methods like H2O. A discussion of the advantages and disadvantages of using EMA versus a simple accumulation of attention scores would be beneficial.

### Questions
Please refer to the weakness part for questions.

### Soundness
3

### Presentation
2

### Contribution
2
