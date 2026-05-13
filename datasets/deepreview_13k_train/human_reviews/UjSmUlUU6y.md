# SimLayerKV: A Simple Framework for Layer-Level KV Cache Reduction

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Recent advancements in large language models (LLMs) have extended their capabilities to handle long contexts. However, increasing the number of model layers and the length of input sequences significantly escalates the memory required to store key-value (KV) cache, posing challenges for efficient inference. To mitigate this issue, we present SimLayerKV, a simple yet effective method that reduces inter-layer KV cache redundancies by selectively dropping cache in identified lazy layers. Our approach is based on the observation that certain layers in long-context LLMs exhibit ``lazy'' behavior, contributing less to modeling long-range dependencies compared to non-lazy layers. By analyzing attention weight patterns, we find that the behavior of these lazy layers is consistent across tokens during generation for a given input. This insight motivates our SimLayerKV, which identifies lazy layers and reduces their KV cache accordingly. SimLayerKV is training-free, generalizable, and can be implemented with only seven lines of code. We conduct extensive experiments on three representative LLMs, e.g., LLaMA2-7B, LLaMA3-8B, and Mistral-7B across 16 tasks from the LongBench benchmark. The results demonstrate that SimLayerKV achieves a KV cache compression ratio of 5$\times$ with only a 1.2\% performance drop when combined with 4-bit quantization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
With the recent increase in context lengths of large language models (LLMs), the memory required to store key-value (KV) cache has grown significantly. This paper aims to reduce inter-layer KV cache redundancies by selectively dropping caches in identified "lazy" layers. The paper first observes that certain layers in long-context LLMs are "lazy," primarily focusing on semantically unimportant tokens (the initial few tokens and the most recent few tokens) when performing attention. Furthermore, lazy layers are less important than non-lazy layers in long-context generation. The paper also finds that the laziness behavior is consistent across tokens for a given input and is easily identifiable. Based on these observations, the paper proposes SimLayerKV, a simple strategy that identifies lazy layers at either the prefill or decode stage and trims the lazy layers to reduce inter-layer KV cache redundancy. To demonstrate SimLayerKV's effectiveness, the paper evaluates it on popular benchmarks like LongBench and Ruler, showing a maximum compression ratio of 5x with only a 1.2% drop in performance. Unlike existing works, this paper is distinct in leveraging inter-layer KV cache redundancies and requires no additional training.

### Strengths
- The paper is novel in its exploration of better inter-layer KV cache trimming without additional training.
- The paper is well written

### Weaknesses
 - It is not clear why SimLayerKV is orthogonal to existing KV cache trimming or compressing methods
- The compression ratio of 1.6x on average without 4 bit Quantization is not significant
- There is performance degradation on more complex tasks
- The proposed way of identifying lazy layers is not flexible enough

### Questions
- In Figure 2, the paper demonstrates the attention patterns during long-context generation in layers 0, 10, 20, and 30, thereby categorizing layers into two types: lazy and non-lazy. How do the insights gained regarding attention patterns in this paper compare to prior work, such as MInference1.0, which identifies three sparse patterns (A-shape, Vertical-Slash, and Block-Sparse)? Do these findings align?

- Could you clarify the lazy layer identification algorithm further? The paper suggests two methods for identifying lazy layers—during the prefill stage and the decode stage. Specifically, when is this identification executed during online inference? How frequently is it updated during benchmarking, and how often would it be updated in an online inference scenario? For multi-round conversations, where inputs from a single user may vary significantly between rounds, how does SimLayerKV address this in its design?

- In Section 2 on related work, the paper references prior research on KV cache trimming, compression, and selection. It includes comparisons with MiniCache, StreamingLLM, and SnapKV as baselines. Why does the paper not include comparisons with more intra-layer trimming methods? Can you provide examples illustrating why inter-layer methods are orthogonal to intra-layer methods? Additionally, have you conducted experiments to demonstrate that integrating these two approaches does not significantly degrade performance?

- In Table 1, the paper compares the performance of SimLayerKV and baseline methods. On the LongBench benchmarks, why does SimLayerKV+Q outperform SimLayerKV in many cases, especially in nearly half of the tests for the Mistral-7B-Instruct model?

- What configuration is used for the StreamingLLM baseline? In Table 6, StreamingLLM achieves a 6-8x higher compression ratio than SimLayerKV; could you provide additional comparison results where both methods achieve similar compression ratios?

- In Section 6.3 on Ruler experiments, SimLayerKV shows a performance drop (8.2% on average) on Multiple Queries NIAH and significant degradation in Common Words Extraction (from 75.1% to 48.6% for a 32k context length). The paper attributes this to the data-dependent nature of lazy layer identification, specifically a fixed selection of lazy layers across the entire benchmark task. Have you conducted experiments to verify this hypothesis? Additionally, have you considered dynamically updating the selected lazy layers during runtime? What are possible solutions to fix this issue?

- What is the overhead introduced by lazy layer identification in terms of latency, and how does it affect the system’s overall throughput? Have you conducted end-to-end serving experiments to demonstrate SimLayerKV's deployment potential?

- How might performance and compression ratios change if individual heads within a layer are considered? Have additional experiments been conducted on this aspect? Would controlling for smaller granularities potentially improve performance, or could it lead to worse outcomes?

### Soundness
3

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
5

### Summary
This paper aims to optimize the efficiency of the LLM inference by reducing the KV embeddings that are needed to be cached in the memory. Based on the observations of the attention weights of different layers, the authors propose an algorithm to identify the “lazy” layers, whose attentions weights of the initial tokens and recent tokens are predominately larger than those of other tokens, and then trim the KV cache of these lazy layers so as to reduce the memory cost. Some experiments on LLaMA2-7B, LLaMA-3-8B, and Mistral-7B show the effectiveness of the proposed method.

### Strengths
1. The research question is interesting and promising for the highly-efficient inference of LLM. Since the KV cache grows linearly with the number of layers, it’s natural to optimize this problem from the layer’s perspective. Recently, increasingly more studies are focused on this topic.
2. From what I understand, the proposed method might be able to save the memory cost not only for decoding, but also prefilling, which is useful for those case where the prompt is way longer than the generated response.
3. The paper has reasonable design of experiments.

### Weaknesses
1. The way to identify the lazy layers involves quite a few hyper-parameters, such as the length of $X_{last}$, $X_{initial}$, $X_{recent}$, and $\delta$. There is no systematic way to tune those hyper-parameters, which makes it too empirical.
2. Since there are two ways to identify the lazy layers, does it mean the lazy layers in prefilling and decoding are different? 
3. Can we identify the lazy layer on-the-fly during the inference? because in practice we usually do not have a small subset of data to identify the lazy layers first, then conduct the real inference.
4. A big missing part of this paper is the result of efficiency, like token throughput, latency or memory cost of the proposed method, since the goal of the algorithm is to optimize the efficiency. 
5. There are quite a few related works trying to identify the optimal KV cache strategies for different layers [1][2][3], it’s unclear what are the cons and pros of those methods compared with the proposed one.

### Questions
please refer to the Weaknesses

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
This paper proposes a simple and effective method, SimLayerKV, which reduces inter-layer KV cache redundancy by selectively discarding the cache of “lazy” layers. The authors found that, in long-context LLMs, certain layers contribute minimally to modeling long-distance dependencies, displaying “lazy” behavior. By analyzing attention weight patterns, they observed that these lazy layers consistently exhibit this behavior throughout the generation process for a given input. SimLayerKV identifies these lazy layers and reduces their KV cache accordingly without altering the cache of non-lazy layers or merging caches across layers. Extensive experiments on three representative LLMs demonstrate that SimLayerKV, combined with 4-bit quantization, achieves a 5x KV cache compression rate with only a 1.2% performance drop.

### Strengths
1. This paper addresses a good research topic: efficient LLM inference.
    
2. The paper is well-organized.
    
3. The proposed method is clearly presented.

### Weaknesses
1. The designed identification algorithm does not meets the observation. It will also treat the layer that attend all of the tokens, including the intial, the recent tokens, and other tokens in the sequence as the lazy layer.
    
2. Why only use the only one token rather than few tokens, as in prefilling stage, in decoding to detect the lazy layers?
    
3. It seems that there are a lot of parameters need to be manually set in this algorithm, including the X_intial, X_recent, and W_last, making the designed algorithm less practical. Moreover, these parameters are also not covered in the ablation study and the authors did not explain how they configure them in the experiments.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces SimLayerKV, a method aimed at addressing the increased memory requirements for storing key-value (KV) caches in large language models (LLMs) that handle long contexts. It identifies "non-lazy" layers in these LLMs that contribute significantly to modeling long-range dependencies. By implementing a novel KV cache eviction strategy that selectively drops caches in less critical layers based on attention weight patterns, SimLayerKV effectively reduces memory usage related to inter-layer KV cache redundancies.

### Strengths
- The study identifies non-lazy layers within large language models and introduces an innovative KV cache eviction method that significantly reduces the memory usage of KV caches.
- The proposed approach is training-free, generalizable, and can be implemented in just seven lines of code, demonstrating its ease of application.
- Experiments conducted on three representative LLMs across 16 tasks from the LongBench benchmark illustrate that SimLayerKV, when combined with 4-bit quantization, achieves high KV cache compression ratios with only a minimal drop in performance.

### Weaknesses
 - The paper notes that KV caches in non-lazy layers must be fully retained, which does not fundamentally solve the substantial overhead caused by KV caches. This could still result in high memory usage. Methods like H2O are able to drastically reduce the memory footprint of KV caches.
- There is a lack of comparison with existing advanced KV cache eviction methods, such as H2O, SnapKV, and PyramidKV.
- The method proposed by the paper appears trivial, and it is unclear whether non-lazy layers will still be present in larger models or how this phenomenon may relate to different datasets.

### Questions
- What is the underlying cause of non-lazy layers?
- Many papers have analyzed the relationships between cross-attention layers. How does this relate to the non-lazy layers identified in this paper?

### Soundness
3

### Presentation
3

### Contribution
2
