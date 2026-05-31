## Human Reviewer 1

### Summary
The authors present QUOKA, a training-free sparse attention algorithm for efficient LLM prefill. The method prioritizes queries with low cosine similarity to the mean to subselect keys. This achieves a 3-7x speedup and an 88% reduction in key-value pairs, while maintaining near-baseline accuracy.

### Strengths
-  The paper introduces a heuristic for query selection based on the hypothesis that queries with greater angular distance from the mean are more informative. This provides a geometric perspective on the multi-query attention problem that is distinct from conventional approaches focused on representativeness.
- The algorithm is designed to be training-free and hardware-agnostic by avoiding the use of custom kernels. This design allows for its potential integration into various inference systems without requiring model retraining or fine-tuning.
- The paper's experiments report reductions in Time-to-First-Token and attention latency across multiple hardware platforms. The results also show that these efficiency improvements are achieved while task accuracy is maintained close to that of the dense attention baseline.

### Weaknesses
- The paper does not include a comparison to alternative query selection strategies, such as selecting representative queries via clustering (e.g., K-Means centroids). Without this comparison, it is difficult to fully assess the performance of the proposed "outlier query" heuristic relative to more established methods for summarization.
- The evaluation of the method's applicability to generation tasks appears less developed. Since the core query subselection component is bypassed in the single-query decoding scenario, a comparison against baselines specifically designed for decoding-phase KV management would be necessary to fully substantiate the method's competitiveness in this setting.
- The potential impact of quantization on the method's performance is not discussed. The algorithm's reliance on precise geometric relationships (via cosine similarity) means its robustness in low-bit precision environments, which are common on its target hardware, remains an important but unevaluated factor.

### Questions
- Could you provide a more direct comparison or discussion against a "central representativeness" approach, such as selecting K-Means query centroids? This would help to empirically situate the performance of your proposed heuristic.
- The assumptions in Theorem 1 are central to the method's motivation. How consistently do these geometric conditions hold empirically across different models and layers? Supporting statistics or visualizations would be valuable.
- For the Math500 experiments where query subselection is not applied, could you please clarify the exact mechanism of QUOKA? Specifically, how are keys selected for the single active query during the generation phase?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 2

### Summary
Due to the quadratic nature of attention, long-context prefill remains a major challenge for large language models (LLMs). However, each query only needs to attend to a subset of key–value (KV) pairs to achieve reasonable performance. Existing sparse attention methods either rely on fixed attention patterns or are optimized primarily for the generation phase.  
This paper presents **QUOKA**, which identifies representative queries from each chunk based on the smallest cosine similarity to the mean query vector, then uses these representative queries to locate important KV pairs. The model finally performs full query–subset KV attention. QUOKA achieves strong performance on long-context benchmarks and is efficient to implement.

### Strengths
- The evaluation is comprehensive and the reported results are impressive.  
- The proposed method is clearly described, and the paper is easy to follow.

### Weaknesses
- Hardware efficiency may degrade due to the small chunk size and discontinuous KV selection.

### Questions
Thanks for submitting to ICLR 2026. This paper introduces an interesting idea of filtering query vectors using cosine similarity, inspired by DiffKV’s approach to KV cache filtering. However, I still have some concerns about the motivation and the efficiency claims.  

## 1. Intuition behind the “critical” query vectors
The intuition for using “critical” query vectors is not fully convincing. It is true that such queries are closer to the key vector space and may attend to a wider range of keys or exhibit higher variance in attention scores. However, since the softmax operation is applied independently to each query, the proposed approach only ensures that these selected queries have smaller attention errors. It does not necessarily guarantee that other queries in the same group will also exhibit small errors. Intuitively, it is unclear why these tokens should be more important for overall generation accuracy.  

## 2. Limited benefit in the generation phase
It is unclear how this method can lead to meaningful speedups during the generation phase. QUOKA estimates the similarity between each query and all keys, but since generation involves only one query vector, this step effectively performs half of the full attention computation. Even after selecting top-k keys and multiplying by the corresponding values, the overall computational reduction—and thus the speedup—appears minimal.  

## 3. Hardware inefficiency due to small chunks
In the evaluation, the block size is set to 128. However, this configuration is inefficient on modern hardware, as each GEMM or attention operation on such small blocks yields low arithmetic intensity and thus lower TFLOPs. This effect is particularly noticeable on H100 and B200. In your latency test, do you also use block size 128 for the full attention baseline? A fairer comparison would allow full attention to use larger block sizes (e.g., 1024 or 2048), which are more hardware-efficient.  

## 4. Constraints on KV selection
Are there any constraints imposed on the selected KV pairs? If the selected KVs are discontinuous, how is self-attention computed efficiently using existing kernels? Discontinuous memory access patterns can severely hinder performance unless carefully optimized.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors propose a better chunked prefill technique which only uses a small subset of KV cache for each chunked prefill. The algorithm goes like this -- choose a subset of queries to select KV cache, compute scores for these queries and aggregate across heads and queries, choose topk scoring KV for chunked prefill. They show that their method outperforms a bunch of baselines at same sparsity.

### Strengths
Strengths
1. Great experimental breadth and strong performance compared to baselines. The experiments cover multiple benchmarks and baselines. 
2. Easy to understand algorithm.

### Weaknesses
1. The approach is not very principled. While it is true that queries with high similarity with K will have low similarity with Mean(Q) due to OOD nature of query and key distributions (this is what theorem says), the converse is not true (this is what you want for efficiency) . It is especially not true in high dimensions -- where it is highly likely that queries with low similarity with Mean(Q) would also have low similarity with K. 

So this being a critical component of algorithm is unsettling. I would assume that most queriers chosen are actually even worse than Mean(Q) w.r.t similarity with K.  Can we have distribution plots of cosine similarities of chosen queries vs. all the queries. 

Having said that their experimental section strongly supports their method.

2. some latest baselines are missing -- duoattention, xattention, spargeattention, might be good to add discussion / results for these.

### Questions
1. Can we have plots for cosine similarities (K, q) for chosen queries and all the queries.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a novel sparse attention method for improving the efficiency of transformer models during the prefill stage with chunked prefill. The idea is to select a subset of important queries by divergence to the mean query and only compute attention for those important queries and important key-value pairs. The method is evaluated on SOTA open-source LLMs against other sparse attention baselines and shows better efficiency and performance frontier.

### Strengths
- The proposed method is well-motivated with insight experiments
- The pseudo-code is extremely helpful in understanding the method
- The experiment is solid

### Weaknesses
- Some explanations of the claims are confusing

### Questions
Thank you for your submission. I like the paper overall and think the method is well motivated. I particulary enjoy the insight experiments in Figure 2 and 3, which make the motivation very clear. However, some claims and descriptions in the paper are poorly explained and a bit vague to me. I would appreciate it if the authors can clarify the following questions:
- What is the relationship with chunked prefill? The proposed method seems to be highly dependent on chunked prefill, but the relationship is not very clear to me. I can understand that some previous sparse attention methods can be inefficient under prefill with multiple queries due to aggregated sparsity. But why is chunked prefill specifically needed for the proposed method? Is it possible to use the proposed method without chunked prefill?
- "however, due to dynamic compute graph and KV cache memory bandwidth overhead under chunked prefill, their benefits are limited." Can you please elaborate more on this point? Why dynamic compute graph and KV cache memory bandwidth overhead limit the benefits?
- "During prefill, when relevant KVs are selected for many queries at once, this can result in significant performance degradations. Under chunked prefill, where important KVs are repeatedly subselected for multiple queries, these degradations become more pronounced." These two sentences are particulary confusing to me. Why chunked prefill makes the performance degradation more pronounced?
- The gather operator in algorithm 1 has inconsistent notations (at line 4 and line 12).
- “As discussed in Section 2, existing sparse attention methods face limitations in prefill efficiency and portability.” What do you mean by portability here?
- I don't fully understand the query selection process. Many of the previous sparse attention methods also reduce among the KV dimension, so the attention socres are approximated with partial KV, however, we still get the full attention scores for all queries. In this paper, it seems that you only select a subset of queries, does this means some of the queries are pruned? Does this means it is somehow similar to the previous work on token pruning?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
8

### Confidence
4