# Recycled Attention: Efficient inference for long-context language models

- Decision: Reject
- Scores: 6, 5, 5, 5, 6

## Abstract
Processing long-context input imposes a heavy computational burden when deploying large language models. Recently proposed inference-time methods accelerate generation by attending only to local context. Despite its efficiency gains, this approach fails to capture all relevant information in the input, showing substantial performance drop in long-context benchmarks. We propose recycled attention, an efficient and effective method which alternates between full context attention and attention over a subset of input tokens. When performing partial attention, we leverage the attention pattern of a nearby token that has performed full attention and attend only to the top K most attended tokens. We evaluate our methods on RULER, a suite of tasks designed to comprehensively evaluate long-context abilities, and long-context language modeling tasks. Applying our inference method to off-the-shelf LLMs achieves comparable speedup to baselines which only consider local context while improving the performance by 2x. We further experiment with continued pre-training the model with recycled attention to improve the performance-efficiency trade-off.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tries to tackle the challenges in long context LLMs. Long context LLMs create lots of KV cache during inference, therefore requiring large memory space and high bandwidth requirements. A representative line of work to address this problem is aiming at reducing the number of KV cache stored during inference. However, the authors reported performance problems for these approaches. Therefore, they proposed recycled attention. Instead of completely getting rid of some KV caches, a full attention is performed periodically generation process and a partial attention (i.e. using fewer important KV cache) is performed for the rest of the time. Evidences show that recycled attention can effectively identify the important KV cache and achieves higher performance without sacrificing too much efficiency.

### Strengths
1. The authors have used recovery rate to justify the idea of recycled attention. I do think the idea itself presents a thinking of hierarchical attention subject to generation phase.
2. The presentation of this paper is clear and convincing.

### Weaknesses
1. It would be good to have theoretical reasoning on the effectiveness of the recycled attention idea. Specifically, while the recovery rate provides empirical justification, a more formal analysis of why periodically performing full attention and then switching to partial attention maintains performance would strengthen the paper. For example, it would be valuable to understand the conditions under which the partial attention mechanism can effectively approximate the full attention, and how the frequency of full attention impacts the approximation error. This could involve analyzing the spectral properties of the attention matrices or the information loss during the partial attention steps.
2. As mentioned in the Limitation section, it would improve the paper if the experiments can go deeper into more settings, like the different stride for different layers. These questions are likely to raised after reading the paper. It is worth to have these results and will be helpful to draw more comprehensive insights. Otherwise, the contribution of the idea seems pretty limited. For instance, the paper could explore how the optimal stride varies across different layers and model sizes. Furthermore, the impact of the stride on different types of tasks (e.g., summarization vs. question answering) should be investigated. Without these detailed explorations, the generalizability of the proposed method remains unclear.

### Questions
1. Why QWEN appears to get a similar performance for streaming LLM and recycled attention? This pattern is true for both Figure 4 and FIgure5. 
2.  Why the gain is minimal when the output length is small? I feel like if the output length is small, it is possible that only the first step attention is in full form, others should be fast in terms of generating the tokens.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new efficient LLM inference method called Recycled Attention. Observing that the top-k tokens based on attention scores at current step still hold a significant portion of the attention mass over the following steps, authors interleave full attention within sparse attention to more accurately select important tokens, balancing the advantages and disadvantages of full and sparse attention.

### Strengths
Previous efficient inference methods based on KV Cache compression typically do not reuse a token once it has been evicted. Recycled Attention addresses this issue by interleaving Full Attention.
Compared to Vanilla Attention, Recycled Attention significantly reduces inference latency.
Compared to StreamingLLM and H2O, Recycled Attention achieves substantial gains on the Ruler Benchmark with nearly comparable inference latency.

### Weaknesses
Recycled Attention increases the memory burden. Compared to StreamingLLM and H2O, Recycled Attention requires additional maintenance of a full KV Cache.
The benchmark is limited. Ruler uses synthetic examples for testing. Performance on real sample benchmarks, such as LongBench[1], should also be reported.
After continued pretraining, only PPL is tested. For long context text modeling, PPL is not an intuitive metric. Additional experiments on Ruler and LongBench are needed.
Stronger comparison methods are missing. For example, Quest[2], which has a similar motivation to this paper, should also be included for comparison.

### Questions
I am curious about how H2O would perform in the attention mass overlap test in Section 2.2.
Additionally, most tokens in the Full KV Cache also come from the Recycle Steps. As the generation length increases, will there be an accumulation of errors compared to Vanilla Attention, resulting in an increasing performance gap between Recycled Attention and Vanilla Attention?

### Soundness
3

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
5

### Summary
Recycle attention combines the vanilla full attention and H2O. For every generation steps, it performs one full attention step and otherwise uses H2O. The novelty is limited.

The authors did not discuss how they decide the value of $S$ for each task. As a result, the results are questionable. Further discussion is necessary during the rebuttal period.

### Strengths
The paper is well-written. Many tasks and baselines are tested.

### Weaknesses
1. The novelty is very limited. Recycle Attention is essentially a straightforward interpolation between vanilla full attention and H2O. For every $S$ generation steps, it performs one full attention step and otherwise uses H2O. Therefore, it is not surprising that Recycle Attention performs well on the NIAH task, benefiting from occasional full attention. However, as a trade-off for combining the strengths of both approaches, Recycle Attention inherits their respective drawbacks: it is not as efficient as H2O and not as effective as full attention.

While combining vanilla full attention and H2O with an adaptive $S$ could have been novel, Recycle Attention leaves this to future study.

2. The emprically set $S$ makes experiments questionable. If I missed something, please correct me, but I did not find a detailed discussion on how $S$ was set for each task. In the ablation of S (Table 5 and Line 396), you conclude that there is "a different trend for different tasks." It appears that you set a specific $S$ for each task, making Recycle have optimal performance. If this is the case, it is a test data leakage, making the experiments unreliable.

### Questions
Please provide a detailed discussion on how you choose S for each task; this is crucial for evaluating the soundness of your paper. Without this information, I can only give the lowest soundness score, but I am open to revising it once you provide clear guidelines for decising the value of S. 

I am also open to raising the overall rating if the authors can demonstrate that their experiments are reliable and fair.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work aims to improve the inference speed of long-context large language models. The motivation is clear: restricting certain tokens to attend only to a subset of tokens during decoding, reduces computation and thus accelerates the decoding speed. The method is verified on a popular synthetic benchmark (RULER) and several language modeling datasets to evaluate long-context large language models.

### Strengths
1. The motivation and paper writing are clear. Exploring inference acceleration for long-context large language models is highly meaningful. The writing in this paper is very clear, and I can easily understand the work.
2. The method is somewhat innovative. Compared to previous similar works ([1, 2, 3]), this work considers accelerating the decoding stage.

[1] Li, Yuhong, et al. "Snapkv: Llm knows what you are looking for before generation." arXiv preprint arXiv:2404.14469 (2024).

[2] Zhang, Yichi, et al. "PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling." arXiv preprint arXiv:2406.02069 (2024).

[3] Jiang, Huiqiang, et al. "Minference 1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention." arXiv preprint arXiv:2407.02490 (2024).

### Weaknesses
1. The benchmarks are limited. The authors validated the method on RULER and several datasets for language modeling evaluation. However, there are two vital problems:
 * RULER is just a synthetic benchmark; more evaluations on real-world tasks, such as the commonly used LongBench [1], are necessary. In addition, the widely used "needle in a haystack" [2] task for evaluating long-context LLMs is necessary.
 * The authors have validated the language modeling capability of their model through extensive experiments. However, recent works [3, 4] have pointed out that this metric (perplexity) is not an indicative measure.
2. The baselines are limited. The authors considered two important baselines: StreamingLLM and H2O. This is reasonable because both models apply attention only to tokens within a subset of the context during decoding. However, there are many other similar works that this paper does not address, such as SnapKV [5], PyramidKV [6], MInference 1.0 [7], etc.
3. The performance loss caused by this method is too severe. From Table 2, we can see that RecycledAttention shows a significant performance drop compared to the standard model, with a decrease of 33 points on Llama 3.1 and 32 points on QWEN-2. This level of performance loss is unacceptable in practical applications. When accelerating inference speed, we should prioritize maintaining the model's performance; simply speeding up while sacrificing performance is meaningless.

### Questions
The paper is written very clearly, and I have no questions.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on accelerating generation speed when dealing with long-context inputs using Large Language Models. Though prior methods have achieved inference speedup by different KV cache eviction policies, the eliminated tokens cannot be recovered in future generation process, thereby leading to performance decline on tasks requiring aggregating long-context information. To address this issue, the authors propose Recycled Attention, which keeps full kv cache in memory and realizes speedup by alternating between a sparse full-attention mode and a consecutive recycled attention mode. The latter only performs attention over a small subset of kv pairs identified using the attention weights produced by the full attention mode. Experiments are conducted on language modeling(Arxiv, Book, and PG19) and synthetic long-context tasks(RULER). Results demonstrate that Recycled Attention deliver higher task accuracy compared to baselines while achieving similar speedup gain.

### Strengths
1. The idea of utilizing attention pattern similarity between adjacent tokens to speed up inference makes intuitive sense.
2. The attention mass analysis and empirical results on downstream tasks demonstrate the effectiveness of Recylced Attention.
3. The experiment section is comprehensive, which includes two LLMs, two types of downstream tasks and different long-context configurations.

### Weaknesses
1. Details about the methods: Are there any discussion on the choice of using the first query head's results for each kv heads in a group? Why not the average of all query heads? The paper lacks a clear justification for this specific aggregation method, and it's unclear how this choice impacts performance, especially given that different attention heads often learn different patterns. A more thorough analysis of this design choice is needed, including ablation studies or comparisons with other aggregation techniques such as averaging or using a learned weighted sum.
2. Benchmarks: The paper perform experiments on RULER, which is mostly a synthetic long-context benchmark and the reported results exhibit a notable margin compared to vanilla full attention. It would be more convincing to incorporate more realistic long-context benchmarks, e.g., LongBench. The reliance on a synthetic benchmark, while useful for controlled experiments, limits the generalizability of the findings. The performance gains on RULER may not translate to real-world scenarios where the data distribution and task requirements are different. The absence of results on more established long-context benchmarks makes it difficult to assess the practical impact of the proposed method.
3. Baselines: For KV cache eviction baselines, the mainly compared methods in this paper are H2O and StreamLLM, which are both query-agnostic KV cache eviction methods. The experiment lacks comparisons with more accurate query-aware KV cache eviction methods such as SnapKV, NACL, PyramidInfer, and etc, for further validation. The lack of comparison against state-of-the-art query-aware eviction methods makes it difficult to ascertain the true advantage of the proposed approach. These methods often achieve better performance by selectively evicting less important tokens, and a comparison against them is crucial to demonstrate the superiority of Recycled Attention.
4. Experimental setting: The paper only focus on the decoding phase of LLM inference on short answer long-context tasks. From my understanding, a large fraction of major latency comes from the prefilling phase(Time-To-First-Token). The authors should include latency for prefilling stage to justify that the decoding speedup worth the sacrificed task accuracy. Moreover, for S=50 on RULER, it is equivalent  to prefilling-time eviction methods(such as SnapKV, NACL), of which the comparison is absent in the paper.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
2
