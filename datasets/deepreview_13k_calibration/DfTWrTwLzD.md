# Two Are Better than One: Context Window Extension with Multi-Grained Self-Injection

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5

## Abstract
The limited context window of contemporary large language models (LLMs) remains a huge barrier to their broader application across various domains. 
While continual pre-training on long-context data is a straightforward and effective solution, it incurs substantial costs in terms of data acquisition and computational resources.
To alleviate this issue, we propose~\modelname, a novel approach grounded in the design philosophy of multi-grained context compression and query-aware information retrieval. 
\modelname~is composed of two short-context LLMs such as LLaMA-2, termed upper model and lower model.  
The lower model functions as a compressor while the upper model acts as a decoder. 
The upper model receives compressed, multi-grained context information from the lower model and performs context-aware modeling on the running text.
Information transfer between the compressor and decoder occurs only at the lowest layers to refrain from long forward paths in the lower model and redundant cross-attention modules in the upper model.
Based on this architecture, we introduce a specialized tree-style data structure to efficiently encode, store and retrieve multi-grained contextual information for text chunks. This structure, combined with a search algorithm, enables rapid encoding and retrieval of relevant information from various levels of the tree based on the input query. 
This entire process, wherein the sender and receiver are derived from the same LLM layer, is referred to as~\textit{self-injection}.
In our evaluation on long-context modeling and understanding tasks, \modelname~achieves superior or comparable results to several strong baselines, striking an effective balance between efficiency and performance.
Meanwhile, with the aforementioned design choices,~\modelname~can greatly reduce memory consumption, and demonstrates substantial speed-ups over other advanced baselines ($2\times$ over streaming, $3\times$ over encoder-decoder architectures).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SharedLLM, a novel approach for extending the context window of large language models (LLMs) by using a hierarchical architecture that pairs two short-context LLMs. In SharedLLM, one model, called the lower model, acts as a compressor that processes past context into compact, multi-grained representations. The other, the upper model, serves as a decoder that integrates this compressed context with current text to predict future tokens in a context-aware manner. Information is passed from the compressor to the decoder through self-injection layers at specific levels, allowing efficient integration without extensive cross-attention.

### Strengths
1. Innovative Multi-Grained Context Extension: Introduces a unique approach to extend context windows using a compressor-decoder model architecture, which efficiently handles large context data.
2. Strong Experimental Results: Demonstrates superior performance on several long-context benchmarks, providing evidence of the model's robustness.
3. High Efficiency: Outperforms other methods in terms of speed and memory usage, making SharedLLM viable for large-scale applications.

### Weaknesses
1. The method is very complicated. I admit that "complicated" itself is not sometimes a weakness. However, simple and elegant design is usually working well in model architecture research. Complicated design brings engineering difficulty and optimization problem. SharedLLM uses the last output as the embedding of a chunk which is used for retrieval by the queries. It is highly questionable whether optimization is valid where sparse computation usually has difficulty on gradient estimation.

2. SharedLLM divides context into different chunks and adds downsampling module to compress KV cache. This may hurt performance on some long-context tasks. The experiment part is not strong enough to support SharedLLM's long-context capability. I will give some existed benchmarks and easy examples accordingly:
- Needle-in-a-haystack is now a compulsory evaluation to show long-context's retrieval ability, which is also included in InfiniteBench. However, the experiment only includes two subtasks. The other part is also essential to show model's long-context ability.
- If I query the model to repeat all the previous context, the sparse-divided and compress context may hurt the context information. Moreover, If my first query does not include some context information, and my second query needs that again. Then, SharedLLM will drop it in the first response and can not answer my second question.

3. The experiment also lacks important baselines of KV pruning methods. For example, StreamingLLM is an early baseline which directly drops all the global information while only maintaining the local KV cache. There are many sparse KV cache works, including H2O, SnapKV, FastGen. These works are efficient and memory-friendly, while maintaining parts of long-context capability.

### Questions
1. What criteria guided the choice of retrieval policy in the context tree, and how sensitive is SharedLLM’s performance to different retrieval policy settings?
2. How does SharedLLM perform with different compression ratios, tree depths, and injection layer settings?
3. Have you considered testing SharedLLM with alternative context extension methods, such as position interpolation or memory-augmented architectures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents SharedLLM, which uses two short-context LLMs (derived from the same model family like LLaMA-2) in a hierarchical structure to handle long contexts. My understanding is that this paper has made the following contribution:

- Integrating the concept of "Context Tree": A binary tree structure storing text at different granularities, with higher compression ratios at higher levels

- Architecture: A lower model compresses context into multi-grained representations, while an upper model performs language modeling using this compressed information

- Query-Aware Retrieval: For instruction-following tasks, uses similarity scoring to selectively expand relevant tree nodes

- Layer-wise Connection: Information transfer occurs only at lower layers to reduce computational overhead

Empirical results on language modeling tasks up to 128K tokens and various instruction-following benchmarks.

However, I am a bit concerned with the presentation and also the technical depth explanation.

### Strengths
- the basic empirical setup for evaluation in experimental studies is clean on standard benchmarks, from ppl to instruction-following tasks

- ablation studies demonstrate the effectiveness of the approach

### Weaknesses
1. In my personal opinon, this paper could benefit from the improving the presentation, specifically,

- In figure 1, it is hard for me to capture whether this is a encoder-decoder model or decoder-only model. The role of cross attention is not very clear. I would recommend authors to haven an overview of the model, and then dive into details, and use another figure to explain the context tree to avoid readers getting distracted. At least, you can mark which part is an encoder, and which part is a decoder.

- I really find it hard to understand what is "Tree Cross-attention" in Figure 1.

- The paper emphasizes on "self-injection" but this concept is nowhere in this central figure. 

- there are notations of compression ratio but I am not so sure that they are well explained.

- Authors were arguing "information preservation" but I am not so sure what does this mean?could you elaborate on this and connect this with related work?

2. Experimental setup and results

- There are many hyperparameter setup of the trees constructed, but the intuitive why those hyperparameters were used/set are not well discussed.  See Q1

- What do you handle the drift or variable length during training and inference? See Q2

- Different values of M were set, what's the intuition and what's the best practice? See Q3

### Questions
Q1. How do you setup the values of hyperparameters of context tree? for example, their depth? are they sensitive to the inference tasks?

Q2. How do you take care of variable length during training and inference? The dynamic NTK and Yarn used the inference-time ratio on this, but I am not so sure about this in your method, thank you in advance as I am out of curiosity. 

Q3. Robustness of different M values. M is an important model architecture base value, but I am not sure the robustness and meaning of setting different M values, and what is the best practice for this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes ShardLLM to reduce heavy training and inference cost in long-context LLMs. Specifically, this method insight is on the multi-grained context compression and query-aware information retrieval. SharedLLM uses  two short-context LLMs, where  the lower model functions as a compressor while the upper model acts as a decoder. The lower model divides the sequence into non-overlapping chunks and makes split-and-search procedure to choose relevant chunks. The selected chunks are then downsampled to reduce KV cache cost. The upper model encodes these keys and values via cross attention with chunk level positional embedding. 

The paper makes experiments on language modeling and supervised fine-tuning to verify the effectiveness of SharedLLM. In language modeling, SharedLLM outperforms other efficient long-context baselines. In supervised fine-tuning, SharedLLM also achieves strong performance in LongBench and InfiniteBench. The efficient experiments show that SharedLLM is cheap and easy to deploy. Finally, the ablation studies discuss the design choice.

### Strengths
1. The paper focuses on an important research area, where LLMs are struggling to achieve effective and efficient long-context training and inference. SharedLLM integrates the compression and retrieval idea, which is a promising research direction in this field.

2. The paper is well written. Although the proposed method includes a long procedure, the method section is organized well to help readers get the core idea. The experiment section includes all the necessary part, including performance, efficiency, and ablation studies.

### Weaknesses
1. The method is very complicated. I admit that "complicated" itself is not sometimes a weakness. However, simple and elegant design is usually working well in model architecture research. Complicated design brings engineering difficulty and optimization problem. SharedLLM uses the last output as the embedding of a chunk which is used for retrieval by the queries. It is highly questionable whether optimization is valid where sparse computation usually has difficulty on gradient estimation.

2. SharedLLM divides context into different chunks and adds downsampling module to compress KV cache. This may hurt performance on some long-context tasks. The experiment part is not strong enough to support SharedLLM's long-context capability. I will give some existed benchmarks and easy examples accordingly:
- Needle-in-a-haystack is now a compulsory evaluation to show long-context's retrieval ability, which is also included in InfiniteBench. However, the experiment only includes two subtasks. The other part is also essential to show model's long-context ability.
- If I query the model to repeat all the previous context, the sparse-divided and compress context may hurt the context information. Moreover, If my first query does not include some context information, and my second query needs that again. Then, SharedLLM will drop it in the first response and can not answer my second question.

3. The experiment also lacks important baselines of KV pruning methods. For example, StreamingLLM is an early baseline which directly drops all the global information while only maintaining the local KV cache. There are many sparse KV cache works, including H2O, SnapKV, FastGen. These works are efficient and memory-friendly, while maintaining parts of long-context capability.

### Questions
1. I'm curious about the result in Table 1 and Table 2. CEPE in line 349 is a re-produced result. Does it mean that the other results are all from the public checkpoint of the according paper? If so, I think the perplexity comparison is meaningless due to different experiment setting. If not so, the perplexity in short context (4k) is highly different, which is also weird.

2. On Infinibench evaluation, why you are only interested in two subtasks? There is not a rationale for that. After all, if you use a bench for evaluation, you usually use the whole subtasks.

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
3

### Summary
The paper introduces SharedLLM, an innovative approach designed to extend the context window of LLMs without incurring the substantial costs associated with continual pre-training on long-context data. The authors claim that SharedLLM achieves comparable or superior results on long-context tasks while significantly reducing memory consumption and increasing processing speed compared to existing methods.

### Strengths
1. The SharedLLM introduces an original dual-model architecture with a "context tree" data structure, enhancing the efficiency of context compression and retrieval for large language models.
2. Despite the complexity of the concepts introduced, the paper communicates the workings of the SharedLLM and its underlying mechanisms

### Weaknesses
1. The evaluation only uses the LLaMA-2 model, with no justification for not including more recent or varied models like LLaMA-3.
2. The method proposed in this paper does not seem to outperform other models in Longbench.

### Questions
See Weakness section

### Soundness
3

### Presentation
2

### Contribution
3
