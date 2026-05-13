# LSH Tells You What To Discard: An Adaptive Locality-Sensitive Strategy for KV Cache Compression

- Decision: Reject
- Scores: 5, 3, 5, 1, 3, 6

## Abstract
Transformer-based large language models (LLMs) use the key-value (KV) cache to significantly accelerate inference by storing the key and value embeddings of past tokens. However, this cache consumes significant GPU memory. In this work, we introduce LSH-E, an algorithm that uses locality-sensitive hashing (LSH) to compress the KV cache. LSH-E quickly locates tokens in the cache that are cosine dissimilar to the current query token. This is achieved by computing the Hamming distance between binarized Gaussian projections of the current token query and cached token keys, with a projection length much smaller than the embedding dimension. We maintain a lightweight binary structure in GPU memory to facilitate these calculations. Unlike existing compression strategies that compute attention to determine token retention, LSH-E makes these decisions pre-attention, thereby reducing computational costs. Additionally, LSH-E is dynamic -- at every decoding step, the key and value of the current token replace the embeddings of a token expected to produce the lowest attention score. We demonstrate that LSH-E can compress the KV cache by 30\%-70\% while maintaining high performance across reasoning, multiple-choice, long-context retrieval and summarization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
LLMs utilize KV cache to accelerate inference but take up significant GPU memory. LSH-E is an algorithm that uses LSH to compress the KV cache by evicting tokens that are cosine dissimilar. The token eviction happens pre-attention, thus making this method computationally affordable.

### Strengths
1. The small size of the KV cache allows it to be stored in GPU memory, eliminating latency from moving data between CPU and GPU.
2. KV cache eviction happens before attention computation, cutting down on unnecessary and expensive attention computations.
3. The greedy eviction approach makes it computationally very affordable.

### Weaknesses
1. It would be helpful to have an ablation study of LSH-E's performance with different numbers of first and recent tokens cached.
2. The benchmarks seem limited; there are only two datasets per task and the improvement over the baseline is not very significant in Needle-in-a-Haystack, Common Words, and MedQA Multiple Choice.
3. Evaluation does not include end-to-end speedup numbers, making it more difficult to see the ultimate impact of the contribution.
4. The greedy eviction algorithm assumes that the attention score between a particular key vector and the current query vector is representative of the attention score with subsequent query vectors. While there is ample empirical exploration on the correlation between attention and inverted LSH hamming distance, I could not find provable theoretical guarantees about the quality of the KV cache under this greedy eviction strategy or empirical observations about the consistency of attention scores across query vectors that suggest the soundness of this assumption. This is in contrast to other greedy approaches such as H2O that uses *accumulated* attention to be more robust to variations between individual query tokens.

### Questions
1. Under "Configuration and Setup", it is mentioned that you "keep the most recent 10 tokens and the first 4 tokens of the prompt always in the KV cache." Is the L2 eviction baseline also configured this way?
2. How well does LSH-E perform without keeping the most recent 10 tokens and the first 4 tokens?
3. Is it possible to perform more evaluations on LongBench tasks?
4. Do you have empirical results that show that the attention score for the current token is a reasonable proxy for attention scores for subsequent token, or that a low attention score for a current query token implies that the key token will not be critical to subsequent query tokens?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The idea is to reduce KV Cache by evicting and permanently dropping tokens at each position in the query. The heuristic used is to evict the lowest attention scored keys ( which is essentially similar to H2O / Scissorhands which preserve top attention scored keys). The difference is to use LSH to do a approximate score ranking to avoid SoftMax for exact computation.

### Strengths
Uses LSH to approximate attention computation for eviction (if you compare to h2o / scissorhands)

### Weaknesses
 - Novelty: The novelty is limited.
- H2O / Scissorhands are known to not perform well on longbenchmark. Can we see some results on longbenchmark like passage retrieval datasets ?
- Missing baselines --only baseline used is L2 norm. 
- Limited evaluation. can we get more results on longbenchmark at different budgets with standard baselines.

### Questions
see questions above,

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents new methods to accelerate inference of auto-regressive transformers used in most modern-day decoder-based LLM architectures. Indeed, the main drawback of existing systems is the size of the "KV  Cache" or Key-Value Cache which is used during the attention mechanism. To speed up the attention calculation, most systems have a cache which remembers the keys and values of commonly used tokens, to avoid recomputing it for each token decoding.  However ,such a cache, for it to be performant at inference time, must scale quadratically with the sequence length, and linear in number of layers and attention heads. 

(Authors: please explain why for the uninformed reader -- this is stated in the intro, but without explanation)

In this paper, the authors present an LSH based method to evict far-away key tokens. Indeed, suppose we have an LSH which gets a binary encoding of any vector using random hyperplane projection method (SIMHASH). 
Then, we can first pre-process and compute the hamming distance between query token and all key tokens, and evict the farthest one, as this is the one least likely to affect the overall attention soft-max operation.

They implement this simple scheme and provide a range of quality vs cache size metrics comparing with one other KV-cache called L2-Dropout Cache, which drops the keys based on their magnitudes.

### Strengths
Studies an important problem of much significance in todays LLM era. 

Presents a simple yet elegant approach

Does good evaluations on a range of use-cases

### Weaknesses
Why is there no timing experiment, since that will be one key benefit of caching.

Why only restrict to attention-free cache policies and specifically only compare with the L2-dropout baseline? It would be beneficial to see comparisons against other eviction strategies, particularly those that leverage attention scores, to understand the trade-offs more clearly. The current comparison limits the scope of the evaluation and the conclusions that can be drawn about the effectiveness of the proposed LSH-based method.

Conceptually, what is the key difference with Reformer? I have not read that paper but you mention in passing that it is using LSH and simhash also. Is which cells to evaluate vs what to evict the only difference between Reformer and your work? If so, worth comparing with Reformer also in plots? A more detailed explanation of how this work differs from Reformer, especially in terms of the application of LSH, is needed. It is unclear whether the LSH is used in a similar manner, and if not, what the specific distinctions are.

What is the rationale of the policy? Why can't a token just evicted become relevant again? I guess is there some language-based "locality of reference"? The paper does not adequately address the potential for evicted tokens to become relevant again later in the sequence. This raises questions about the long-term impact of the eviction policy on performance, especially in tasks where long-range dependencies are important.

Do ablation of the hardcoded bits, i.e., you mention you hard-cache the first few and last few tokens. What is the contribution of this to your overall success metrics? The paper mentions hard-caching the first and last few tokens, but does not provide any ablation studies to quantify the impact of this design choice. It is unclear how much of the performance gain is due to the LSH-based eviction strategy versus the hard-caching of specific tokens.

The eviction policy is not clearly understandable in how it aggregates the hamming distances over time steps. Is it only based on the most recent time step, or some more complex rule? The paper lacks clarity on how Hamming distances are aggregated over time. It is unclear whether the eviction decision is based solely on the most recent time step or if there is a more complex aggregation rule. This ambiguity makes it difficult to fully understand the eviction process.


### Questions
Line 52: "However, this L2 dropout strategy only performs well on
long-context retrieval tasks. It is specialized to retain only those tokens with the highest attention" -- be more specific. Why is this?

Line 57: "wide variety of tasks?" -- how do you define this?

Line 145: Formally for our setup, distd(x, y) cos θx,y, here it is more a measure of cosine similarity than distance. Misleading, perhaps?

Line 419: did you mean "LSH dimension does significantly impact performance" --> does not?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces LSH-E, an algorithm for compressing the key-value (KV) cache in large language models (LLMs) using locality-sensitive hashing (LSH). Despite the availability of prior work—including KDEformer, Hyperattention, SubGen, and QJL—that similarly utilizes LSH for efficient attention and memory management, these related efforts are not cited here. LSH-E leverages Hamming distance calculations in a binary space following a Quantized Johnson-Lindenstrauss (JL) transform (SimHash) to identify and evict tokens with low relevance to the current query, resulting in memory savings. This pre-attention approach provides a lightweight, GPU-efficient solution for long-context tasks, although its effectiveness ultimately depends on the algorithm’s CUDA implementation efficiency.

### Strengths
The use of theoretical approaches such as SimHash, a highly efficient hashing method, is a valuable aspect of this work, contributing to both the effectiveness and scalability of the proposed method.

### Weaknesses
 - The term "novel" should not be used for LSH in this context, as it is not a new approach and has appeared in prior work. Specifically, the methods used in KDEformer, Hyperattention, QJL, and SubGen demonstrate significant overlap, yet these works are not cited here, despite their relevance.

- The experimental setup lacks comprehensiveness; comparisons with alternative methods like H2O, SubGen, and other established baselines should be included to provide a more robust evaluation.

- The datasets used in the experiments are not sufficiently large for evaluating performance in long-context scenarios. Given that these methods target long-sequence processing, experiments should ideally use token sizes over 50,000. LongBench or other large-scale datasets would be more appropriate for a thorough evaluation.

- Additionally, runtime metrics should be reported to assess the efficiency of token generation and to substantiate the computational benefits claimed in the paper.

### Questions
- Could you provide a plot showing the distortion error introduced by LSH compression across different levels of compression? Specifically, how does the approximation quality change as more tokens are evicted or as the quantization parameters are adjusted?

- Given that LSH-E’s efficiency largely depends on its CUDA implementation, can you elaborate on any specific optimizations made within the CUDA code?

- Could you clarify how LSH-E handles multi-head attention? Specifically, is each head processed separately with its own LSH compression, or is there a shared mechanism across heads?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method that uses LSH to perform kv cache eviction. The provided experiments show that the proposed method outperforms the baseline.

### Strengths
Strong Points
----
S1. The problem of the paper is well-motivated. 

S2. The proposed algorithm is simple and clear with illustrative example.

S3. The proposed method outperforms the baseline L2.

### Weaknesses
Weak Points
----
W1. Important related studies and baselines are missing:
Singhania, P., Singh, S., He, S., Feizi, S., & Bhatele, A. (2024). Loki: Low-Rank Keys for Efficient Sparse Attention. arXiv preprint arXiv:2406.02542.
Tang, J., Zhao, Y., Zhu, K., Xiao, G., Kasikci, B., & Han, S. (2024). Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference. arXiv preprint arXiv:2406.10774.

W2. The key measures of the targeted task should be have more accurate inference with lower memory footprint and latency. I do not agree with the methodology of not comparing with other "non attention-free" methods.

W3. The presentation of experiments need to be improved: Lack of discussions and intuitions in the experiment analysis. For example, why does LSH-E outperform Full in Figure 4a; why does LSH-E become worse than L2 after 50% cache budget in Figure 4b? We have many subsubsections in the experiments, but most contents in those are barely text illustration of the figure and result while no discussion of why we would have those results.

W4. The execution time of the proposed system is missing.

W5. The discussion of the error introduced by the LSH is not included. I wonder what if we use cosine similarity to evict the cache instead of LSH, how will be the accuracy, latency, and memory usage?

W6. In the supplementary materials, we see more experiments with more baselines that are better than L2. I wonder the reason why the authors do not include them.


Presentation
----
P1. Line 180 "heavy hitters' -> ``heavy hitters''
P2. The axis captions of the figures are too small to be seen.

### Questions
See weakness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a KV cache compression method based on LSH and shows that LSH-E can achieve good downstream performance on various downstream tasks with a 30%- 70% compression ratio.

### Strengths
This paper applies novel LSH methods to KV cache problems. The motivations and reasons why LSH can produce a good performance are well discussed. Besides this, a static compression rate of 30% - 70% is also helpful for many LLM serving systems, given the accuracy is preserved.

### Weaknesses
1. There is no comparison with other static KV compression baselines, including H2O, streamingLLM, and SnapKV. If this problem is solved, I will raise my score.
2. Only the memory compression ratio is shown. I will ask for the wall clock speedups (latency or throughput).

### Questions
Besides the problems mentioned in Weakness,
1 Does this method work well with quantization (KIVI, AWQ)?
2 How long does LSH-E increase first token latency?

These two questions can be left for future work.

### Soundness
2

### Presentation
3

### Contribution
3
