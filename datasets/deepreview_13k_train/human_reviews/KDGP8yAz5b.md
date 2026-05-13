# ReAttention: Training-Free Infinite Context with Finite Attention Scope

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
The long-context capability of the Large Language Models (LLM) has made significant breakthroughs, but the maximum supported context length remains a critical bottleneck limiting their practical applications. The constraint of context length in LLMs arises from the self-attention mechanism, which cannot effectively and efficiently capture the semantic relationships within infinitely long contexts via the limited pre-trained positional information and attention scope. In this work, we propose \textbf{ReAttention}, a training-free approach enabling LLM based on the self-attention mechanism to support an infinite context with a finite attention scope under sufficient memory resources. ReAttention performs the position-agnostic top-$k$ attention before the ordinary position-aware self-attention, freeing LLMs from the length extrapolation issue. We validate the performance of ReAttention on the LongBench, L-Eval, and InfiniteBench and demonstrate that it is on par with traditional methods. Furthermore, we also apply ReAttention on mainstream LLMs, including LLaMA3.1-8B and Mistral-v0.3-7B, enabling them to support context lengths of at least 1M and even expanding the context length of LLaMA3.2-3B-chat by 128$\times$ to 4M without any further training in Needle-In-A-Haystack tests. We also improve the efficiency of ReAttention with Triton and achieve an efficient extrapolation without additional overhead.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes ReAttention, a a training-free approach enabling LLM based on the self-attention mechanism to support an infinite context with a finite attention scope under sufficient memory resources. ReAttention splits the tokens into three parts: initial tokens, middle tokens, and local tokens. It maintains the initial and local tokens (their KV caches), select a subset of middle tokens, and re-concatenates them with positional index calibration, and then conduct attention operation.

### Strengths
1.	The method is intuitive. ReAttention maintains KV caches of tokens that are more frequently attended by the latest tokens, which reduces the memory overheads and remove redundant contextual segments from being attended. 
2.	The evaluation is comprehensive. Authors provide evaluation for many models and benchmarks. 
3.	The performance improvement is notable, compared to InfLLM and full attention.

### Weaknesses
1. The two-round attention operation introduces non-trivial overheads, which may result in latency similar to full attention. 
2. The efficiency in terms of latency and throughput can be the major drawbacks of this method. 
3. The method requires sufficient memory resources where full attention is also feasible. The advantage over full attention lies in evicting irrelevant tokens, similar to token-dropping methods, which improves performance. However, efficiency in long-sequence tasks remains a concern. When full attention isn't feasible, the two-round attention calculation might be costly, as the first round still requires full-attention calculations. 
4. In long-sequence generation, the query tokens can change dynamically. How does ReAttention handle middle-cache selection in this setting? Does it re-select middle caches periodically?

### Questions
1.	The idea appears similar to token eviction methods like H2O and FastGen. How does ReAttention compare with these methods in terms of accuracy and efficiency?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes ReAttention, a training-free approach to extend the context window of Large Language Models (LLMs) through a position-agnostic top-k attention mechanism. The key idea is to perform cache selection before regular self-attention, treating the extraction of critical context info as an additional attention process. The method enables models to handle theoretically infinite contexts with a finite attention scope. The authors validate their approach on multiple benchmarks and models, showing strong performance and efficiency gains through custom Triton kernel optimization.

### Strengths
- The problem is highly relevant and timely, as context length remains a critical bottleneck for LLMs. The paper clearly articulates three key conditions for infinite context extension (lines 040-046).
- The proposed method is simple and training-free. The two-stage attention approach (position-agnostic selection followed by regular attention) is intuitive and well-motivated. 
- The empirical results are impressive. They demonstrate: (1) Comparable or better performance vs full attention across multiple benchmarks (Fig 2); (2) Successful extension of LLaMA3.2-3B context by 128x to 4M tokens (Section 3.3); (3) Strong performance on challenging tasks like LongBench, L-Eval, and InfiniteBench.
- The experimental evaluation is comprehensive, including multiple model architectures (LLaMA, Mistral, Qwen series) and various benchmarks (LongBench, L-Eval, InfiniteBench). It also includes detailed ablation studies on hyperparameters (Table 2) and thorough efficiency analysis with Triton optimization in Section 3.4.

### Weaknesses
 - The paper has several writing issues and typos that should be addressed: e.g., Llama vs LLaMA and the wrong quotation in line 067.
- The related work section omits several relevant recent papers on efficient attention and KV-cache optimization, such as:
SnapKV [1] for efficient cache management, PyramidKV [2,3] for hierarchical cache structures, GemFilter [4] for attention-filtering, and many so on. These works tackle similar challenges and a comparison would strengthen the paper. It would be good to discuss them. Specifically, the paper should discuss how ReAttention compares to methods that perform explicit token eviction or selection from the KV cache. For example, techniques that use attention scores or other metrics to determine which tokens to keep or discard could provide valuable context for understanding the novelty of ReAttention.

[1] Li, Yuhong, Yingbing Huang, Bowen Yang, Bharat Venkitesh, Acyr Locatelli, Hanchen Ye, Tianle Cai, Patrick Lewis, and Deming Chen. "Snapkv: Llm knows what you are looking for before generation." arXiv preprint arXiv:2404.14469 (2024).

[2] Zhang, Yichi, Bofei Gao, Tianyu Liu, Keming Lu, Wayne Xiong, Yue Dong, Baobao Chang, Junjie Hu, and Wen Xiao. "PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling." arXiv preprint arXiv:2406.02069 (2024).

[3] Yang, Dongjie, XiaoDong Han, Yan Gao, Yao Hu, Shilin Zhang, and Hai Zhao. "PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference." arXiv preprint arXiv:2405.12532 (2024).

[4] Shi, Zhenmei, Yifei Ming, Xuan-Phi Nguyen, Yingyu Liang, and Shafiq Joty. "Discovering the gems in early layers: Accelerating long-context llms with 1000x input token reduction." arXiv preprint arXiv:2409.17422 (2024).

### Questions
How does ReAttention perform on more structured tasks that require precise positional understanding (e.g., code completion, mathematical reasoning)?

### Soundness
3

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
This paper proposes a training-free method (ReAttention) for improving the ability of pre-trained language models to process long context lengths. The method is motivated by the insight that attention scores without positional embeddings are still useful for identifying salient tokens.  

The main claims of the paper are that:

1. ReAttention matches or outperforms the performance of traditional self-attention in long-context scenarios. 
2. ReAttention matches or outperforms the performance of other training-free methods long-context methods (*e.g.* InfLLM). 
3. ReAttention extends the context length of existing LLMs (*e.g.* 8B and 3B llama) “to at least 1 million tokens”. 
4. ReAttention adds no computational overhead and less memory usage than regular self-attention.

### Strengths
*The method is motivated by an interesting observation.* “*We also find that the third condition can be satisfied through the attention score without positional embedding.” This insight that attention scores without positional embeddings can effectively identify salient tokens is quite interesting and, to my knowledge, novel.  

*Method works on pre-trained models.* Unlike approaches like Mamba which require training models from scratch with new architectures, ReAttention can be applied directly to existing pre-trained models. This makes it much more practical for immediate deployment and use with current state-of-the-art models.

*Claim 1 seems to be well-supported by the results.*   The empirical evaluation in Figure 2 and Table 1  across multiple benchmarks (LongBench and InfiniteBench) and model architectures shows that ReAttention matches or outperforms regular attention.
- Note: in the weaknesses, I highlight some missing baselines.

### Weaknesses
*Baselines in the long context evals are missing (Claim 2). W*hy is StreamingLLM included in the LongBench results but not the InfiniteBench results? And why is InfLLM included in the InffiniteBench results but not the LongBench results? The absence of consistent baselines across different benchmarks makes it difficult to assess the true performance of ReAttention relative to existing methods. Specifically, the paper should include StreamingLLM in the InfiniteBench experiments and InfLLM in the LongBench experiments to allow for a more direct comparison.

*Baselines in million-scale context seem to be missing. (Claim 3)* For the needle in a haystack experiments supporting Claim 3, the paper should compare against other methods capable of handling very long contexts like InfLLM and other recent approaches. Without these comparisons, it's hard to assess the relative advantages of ReAttention at extreme context lengths. The paper should include results for other long-context methods on the needle-in-a-haystack task, particularly at context lengths exceeding 100k tokens, to provide a more comprehensive evaluation.

*Missing token-throughput comparisons (Claim 3).* The paper only compares time to first token (*i.e.* the cost of prefill).  How does it fare against regular attention in terms of efficiency during the decoding phase? The paper should include a comparison of token throughput during decoding, not just prefill time, to fully evaluate the efficiency of the method.

*Apparent tradeoff in memory consumption (Claim 4).* The authors state that ReAttention uses less memory than self-attention. However, based on Figure 7, it appears that this is only true after ~100k in context length. The authors should highlight this tradeoff and provide a more detailed analysis of memory usage at different context lengths. The paper should clarify that ReAttention's memory benefits are not consistent across all context lengths and that there is a crossover point where it becomes more memory-efficient than standard attention.

*Method description lacks details.* It’s unclear exactly how the method works from the description in Section 2. For example, what does it mean that ReAttention “adopts chunked streaming input during the prefilling stage.” I recommend that the authors provide a detailed description of how prefill with ReAttention differs from decoding. It would be great if the authors included a pseudo-code description of both the prefill and decoding stages (either in the main paper or the appendix). The paper needs a more precise description of the chunking mechanism during prefill and how the recalled tokens are integrated into the attention mechanism during both prefill and decoding. A pseudocode description would significantly improve clarity.

*The "infinite" in the title is misleading.* It’s not clear from the experiments that ReAttention actually supports infinite context. Further, there are still practical limitations from memory constraints that would prevent the model from really achieving infinite context length. The paper should be more precise about what "infinite" means in this context and acknowledge the real-world constraints. The paper should clarify that the method enables very long context lengths but is still limited by available memory, and therefore, does not achieve true infinite context.

### Questions
- *What is the performance of the baselines in the needle-in-a-haystack experiments.*
- *In Figure 7, is the FullAttn* implementation FlashAttention?
- *How exactly does ReAttention differ from InfLLM? Is the only difference that position embeddings are not applied during the lookup step?* (I recommend the authors update the paper to make this comparison more clear.)
- *Minor improvements:*
    - In Figures 3 and 4, the axes and color bars are too small to be legible.

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
5

### Summary
The paper introduces ReAttention, a training-free approach for enabling large language models (LLMs) to handle infinite context lengths with a finite attention scope. The method involves a position-agnostic top-k attention mechanism, which precedes traditional self-attention, to select the most relevant context segments. This approach addresses the limitations of context length in LLMs without the need for additional training. The authors validate ReAttention across multiple benchmarks, demonstrating its effectiveness and efficiency compared to existing methods.

### Strengths
1. The use of Triton to optimize the attention mechanism reduces computational overhead and memory usage.
2. The method supports significant context length extensions, showcasing its potential for real-world applications.

### Weaknesses
1. The paper uses the top-K method to select KV, but this has been studied in H2O. It feels like the paper is a combination of StreamingLLM+H2O, and then rewrites Triton to make up for the calculation time of QK. I don't see any novelty. It would be helpful to provide more specific details on how ReAttention differs from or combines elements of StreamingLLM and H2O. The core idea of using a top-k selection over the KV cache is not new, and the paper needs to clearly articulate what distinguishes its approach from existing methods that employ similar selection mechanisms. Specifically, the paper should detail how the position-agnostic nature of the top-k selection interacts with the attention mechanism, and how this differs from the position-aware selection used in H2O, for example.

2. The rewrite of the Triton operator is indeed very effective, but it is more of an engineering contribution.

3. The paper is mainly an improvement on KV. There are so many optimizations on KV, but there are so few baselines added for comparison. It is recommended to select some baselines from SnapKV, PyramidKV, LongGen, InfiniPot, DuoAttention and other methods for comparison. The paper should include a more comprehensive set of baselines, particularly those that focus on KV cache optimization. This would help to better contextualize the performance gains of ReAttention and highlight its specific advantages over other methods. The lack of comparison with these methods makes it difficult to assess the true novelty and effectiveness of the proposed approach.

4. Many experiments in the paper show good results, but there is no intuitive or formal explanation for why this method can achieve such good results. For example, theoretical analysis, or visualizations that might help explain the performance gains. The paper needs to provide a more in-depth analysis of why ReAttention performs well, beyond just presenting empirical results. This could include a theoretical analysis of the method's properties, or visualizations that illustrate how the top-k selection mechanism interacts with the attention mechanism to achieve better results. Without this, it is difficult to understand the underlying reasons for the observed performance gains.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
