# SharedContextBench: How Lossy are Long-context Methods in KV Cache Reuse

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 3, 6, 6, 8, 8

## Abstract
Long-context Large Language Models (LLMs) have unlocked numerous possibilities for downstream applications, many of which involve multiple requests sharing the same input context. Recent inference frameworks like vLLM and SGLang, as well as LLMs providers such as OpenAI, Gemini and Claude, have employed prefix caching techniques to accelerate multi-requests with shared context. However, existing long-context methods are primarily evaluated on single query testing, failing to demonstrate their true capability in real-world applications that often require KV cache reuse for follow-up queries. To address this gap, we introduce SharedContextBench, a comprehensive long-context benchmark to reveal how lossy are long-context methods in KV cache reuse scenarios. Specifically, it encompasses 12 tasks with two shared context modes, covering four categories of long-context abilities: string retrieval, semantic retrieval, global information processing, and multi-task capabilities. Using our benchmark, we evaluated five categories of long-context solutions, including Gated Linear RNNs (Codestal-Mamba), MambaAttention hybrids (Jamba-1.5-Mini), and efficient methods like sparse attention, KV cache compression, and prompt compression, on six transformer-based longcontext LLMs: Llama-3.1-8B/70B, Qwen2.5-72B/32B, Llama-3-8B-262K, and GLM-4-9B. Our findings show that sub-O(n) memory methods often struggle to maintain accuracy in multi-turn scenarios, while sparse encoding methods with O(n) memory and sub-O(n 2 ) computation in prefilling generally perform well. Additionally, dynamic sparse patterns in prefilling often produce more expressive memory (KV cache) compared to static methods, and layer-level sparsity in hybrid architectures reduces memory usage while yielding promising results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a new (set of) dataset focusing on the multi-round capability of LLMs under a long context setting.

### Strengths
1. The proposed dataset fills a major gap in long context evaluation — where there is often only a single question after a long input, with the question being answerable by simply retaining a few pieces of information within the long context — this makes a lot of eviction-based methods seemingly able to achieve strong performance on many long context datasets, although they are not actually long context capable.

2. Aside of the contribution of collecting this new dataset, the author also conducted a decent benchmark of different methods on their dataset.

### Weaknesses
1. The author should consider highlight the source and origin of each dataset a bit better. Many of the featured datasets looks similar from InfiniteBench. I am not sure if they are direct adoptions or modified; in either case, this deserve a better noting.

2. While the proposed dataset focused on multi-round QA under a "shared context" scenario. It looks like few or none of its question demand information from a previous QA. The author should consider adding some datasets (or new setting of existing datasets) covering this gap, or at least highlight it in its limitation.

### Questions
Recently, there have been many newly proposed long context evaluations (HELMET, Michelangelo, etc.) I wonder if the author can provide a discussion regarding such works so that future users will have some guidance on what to adopt.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces SharedContextBench, a benchmark specifically designed to evaluate the efficacy of long-context methods in scenarios that utilize KV cache reuse. It features an array of 12 tasks that test four long-context abilities across two modes of shared context. Evaluations are performed on five different categories of long-context methods using eight leading LLMs, with a detailed analysis of the results to uncover insights into the management of KV caches.

### Strengths
- SharedContextBench represents a significant innovation in benchmarking by addressing the evaluation gap in shared long-context scenarios, providing a robust assessment tool for practical applications. 
- The benchmark comprises a wide array of tasks across various capabilities and domains, ensuring a comprehensive evaluation of long-context methods. 
- A diverse range of these methods are tested against multiple large language models, offering an extensive overview of their performance. The findings bring to light considerable variations in KV cache management, emphasizing the critical importance of multi-turn and shared-context scenarios in method development. 
- The paper also delves into detailed analyses concerning memory usage and the sparsity observed in encoding and decoding processes, yielding valuable insights for future research endeavors.

### Weaknesses
 - Certain methods, such as KV cache compression, demonstrate limited effectiveness in shared contexts, which may restrict their practical deployment. 
- The paper points out that many of the long-context methods tested are essentially extensions of existing models adapted for multi-turn dialogues, such as StreamingLLM. 
- The tasks within the benchmark may not capture all possible real-world application scenarios, possibly overlooking specific needs within certain domains. 
- Moreover, while the performance of these methods is thoroughly evaluated, the paper does not explore the deeper internal mechanisms of the models, such as the dynamics of information propagation in sparse attention mechanisms.

### Questions
- How were the real-world use cases that influenced the design of the benchmark tasks selected, and what impact did they have on the weighting of the evaluation criteria? 
- What improvements could be implemented in sub-linear memory methods to enhance their applicability and efficiency in multi-turn interactions?

### Soundness
3

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
This paper introduces a new benchmark designed to evaluate model performance on tasks at the intersection of long-context and shared-context settings. The authors argue that existing benchmarks inadequately address this domain, which is critical because long-context methodologies facilitate applications with substantial context reuse. Using this benchmark, the authors assess state-of-the-art open-source transformer models, their adaptations for long-context processing—such as sparse attention, KV caching, and prompt compression techniques—as well as gated linear RNN models. Additionally, the paper contributes a new static sparse attention mechanism that performs better than existing sparse attention methods. Finally, they analyze the effectiveness of various long-context strategies.

### Strengths
*Originality*
This benchmark measures the performance of long context language models in settings that are currently unaddressed by existing benchmarks.

*Quality*
The benchmark covers a wide range of tasks that vary in reasoning complexity and memorization difficulty. All tasks are performed in two shared context modes that are commonly used in real applications. Additionally, the paper demonstrates that the benchmark can be used to draw novel insights about the effectiveness of different long context approaches by evaluating state-of-the-art language models with a wide range of long context methods.

*Clarity*
The goal and contribution of the paper are very clear. Experimental results are clearly visualized.

*Significance*
Many applications enabled by long context models involve context sharing. Thus, this benchmark enables other researchers to make more informed decisions when building long context language models that are effective in real use cases.

### Weaknesses
1. The authors listed prefix caching methods in the related works section but they were missing from the experiments.
2. The paper does not explicitly highlight the unique insights that they were able to obtain with this benchmark that do not surface with other benchmarks. For example, it does not specify whether the relative performances of these methods consistent when they are measured with other benchmarks.
3. There does not seem to be a discussion on how well the synthesized data reflects real use cases. In particular, the retrieval use cases artificially vary the positions of the target strings to ensure long context utilization. There is no discussion on its importance in real life use cases, where queries may obey a power law distribution.
4. It is unclear how the proposed benchmark offered insights that led to the creation of the proposed Tri-shape sparse attention mechanism or how the benchmark uniquely highlights the benefits of this new mechanism, especially since it only significantly outperforms A-shape sparse attention in the first turn.

### Questions
1. Why do the experiments exclude prefix caching methods?
2. What unique insights did the proposed benchmark offer that guided the design of the proposed Tri-shape sparse attention mechanism?
3. Are there inconsistencies between the results obtained with the proposed benchmark and existing long-context or multi-turn benchmarks that can demonstrate the unique insights that this benchmark can provide?

### Soundness
3

### Presentation
4

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
This paper introduces a long-context benchmark SharedContextBench, to reveal how lossy are long-context methods in KV cache reuse scenarios. SharedContextBench includes 12 tasks with two shared context modes, covering four categories of long-context abilities: string retrieval, semantic retrieval, global information processing, and multi-task capabilities. The proposed benchmark is evaluated with several long-context methods and six LLMs.

### Strengths
1.	The paper introduces the long-context benchmark SharedContextBench, to reveal how lossy are long-context methods in KV cache reuse scenarios. The proposed benchmark includes 12 tasks with two shared context modes.
2.	The proposed benchmark is evaluated with several long-context methods and six LLMs. The experimental evaluation is comprehensive.
3.	The paper is easy to follow.

### Weaknesses
The paper did not analyze other long-context benchmarks. It would be benefical, if related long-context benchmarks are summarized and compared in a table.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents **SharedContextBench**, a benchmark for evaluating long-context Large Language Models (LLMs) in realistic, multi-turn, shared-context scenarios requiring KV cache reuse. It includes 12 tasks across four abilities—string retrieval, semantic retrieval, global information processing, and multi-tasking—tested in multi-turn and multi-request modes. Evaluated across five categories of open-source LLMs, results show sub-O(n) memory methods struggle in multi-run scenario while sparse and full attention methods perform well.

### Strengths
1. SharedContextBench fills an important gap by providing tasks that reflect the performance of LLM in realistic, multi-turn interactions.
2. The benchmark includes diverse tasks that thoroughly test LLM's long-context processing abilities, such as retrieval and global information aggregation, which matches the needs in research community.
3. By testing five different long-context methods on a range of LLMs, the benchmark offers valuable comparative insights, making it a robust tool for LLM evaluation in shared-context scenarios. The visualization in the paper is also very intuitive and helpful.

### Weaknesses
1. It would be more convincing to include a table listing the source of the dataset of each task.

### Questions
1. The benchmark is primarily designed to evaluate the accuracy, but with some adjustment people may also use it for performance evaluation on multi-run scenario?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces SharedContextBench, a comprehensive benchmark designed to evaluate long-context Large Language Models (LLMs) in scenarios where multiple requests share the same input context. The benchmark covers 12 tasks across four categories of long-context abilities: string retrieval, semantic retrieval, global information processing, and multi-tasking. It includes two shared context modes: multi-turn and multi-request. The paper evaluates five categories of long-context methods on six transformer-based long-context LLMs, highlighting the impact of sparsity in encoding and decoding, task complexity, and more.

### Strengths
1. The benchmark includes tasks that reflect real-world applications, such as multi-turn conversations, self-play Chain-of-Thought reasoning, and repository-level code debugging.
2. The extended retrieval tasks of key-value retrieval, prefix-suffix retrieval, and multi-hop retrieval are interesting to benchmark the LLMs.
3. The paper provides a detailed analysis of various long-context methods, highlighting their strengths and weaknesses in different scenarios, which offers valuable insights for future research and practical applications.
4. The taxonomy of different long-context methods in Table 1 is comprehensive and help to illustrate their advantages and disadvantages.
5. The paper highlights the challenges faced by sub O(n) memory methods in maintaining accuracy in multi-turn scenarios, providing an important insight into the limitations of these methods.
6. The study shows that sparse encoding methods with O(n) memory and sub $(O(n^{2})$ computation in prefilling generally perform well, offering a practical solution for efficient long-context processing.
7. The paper finds that dynamic sparse patterns in prefilling often produce more expressive memory compared to static methods, suggesting a direction for future research in optimizing long-context methods.
8. The breakdown results (Table 8 and 9) help to show more fine-grained insights.

### Weaknesses
1. The paper provides configuration details for the long-context methods, but it lacks a detailed analysis of how hyperparameters were tuned or their impact on performance. Specifically, it's unclear how parameters like the sparsity level in sparse attention mechanisms, or the chunk size in sliding window attention, were selected. The absence of a sensitivity analysis makes it difficult to assess the robustness of the reported results. For instance, a small change in the sparsity parameter could lead to a significant performance drop, and this is not explored.
2. A more thorough analysis of hyperparameter sensitivity could provide insights into the robustness of the proposed methods. It would be beneficial to see how the performance of each method varies across a range of hyperparameter values, perhaps visualized with error bars or heatmaps. This would help to understand the stability of the methods and identify optimal operating points. For example, how does the performance of a given sparse attention method change as the sparsity ratio increases from 1/2 to 1/16? This kind of analysis is missing.
3. Table 4 is a little confusing. Why some highest scores are not bold? And what is the meaning of the underscore? The table lacks clear explanation of the bolding and underscore conventions. It is not clear whether the bolding indicates the best performance among all methods or only among the efficient methods, and the meaning of underscore is not specified.

### Questions
Could you provide the source codes for the community to verify other methods?

### Soundness
3

### Presentation
3

### Contribution
3
