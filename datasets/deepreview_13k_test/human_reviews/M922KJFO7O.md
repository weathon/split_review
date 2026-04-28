# ClusterGen: Token Generation in Sublinear Time and Memory with Clustering KV Cache

- Decision: Reject
- Scores: 6, 5, 6, 8

## Abstract
Despite the significant success of large language models (LLMs), their extensive memory requirements pose challenges for deploying them in long-context token generation. The substantial memory footprint of LLM decoders arises from the necessity to store all previous tokens in the attention module, a requirement imposed by key-value (KV) caching. In this work, our focus is on developing an efficient compression technique for the KV cache. Empirical evidence indicates a significant clustering tendency within key embeddings in the attention module. Building on this key insight, we have devised a novel caching method with sublinear complexity, employing online clustering on key tokens and online 
 sampling on values. The result is a provably accurate and efficient attention decoding algorithm, termed ClusterGen. Not only does this algorithm ensure a sublinear memory footprint and sublinear time complexity, but we also establish a tight error bound for our approach. Empirical evaluations on long-context question-answering tasks demonstrate that ClusterGen significantly outperforms existing and state-of-the-art KV cache compression methods in terms of performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ClusterGen, a novel caching algorithm designed to generate tokens efficiently within large language models by optimizing memory usage. It addresses the critical challenge of linear memory growth in token generation by introducing a sublinear caching technique for key-value pairs in the attention mechanism. The method leverages clustering on key embeddings and online sampling for values, achieving sublinear complexity in both time and memory. ClusterGen ensures error bounds on approximation accuracy and is empirically validated against state-of-the-art KV cache compression techniques in long-context tasks, outperforming them in both memory efficiency and processing speed​.

### Strengths
1. The introduction of clustering for KV cache management in LLMs is novel and distinguishing from existing methods.
2. Theoretical analyses, including complexity and error bounds, are rigorously provided.
3. The proposed ''Clusterability'' assumption is validated on real LLMs.
4. Experiments are conducted to demonstrate ClusterGen's ability as a valuable tool for practical LLM applications.

### Weaknesses
1. While the evaluations are robust, it could be beneficial to explore ClusterGen’s performance on additional task beyond question-answering.
2. The Clusterability assumption may not hold universally across other LLMs.

### Questions
1. How does ClusterGen perform on tasks other than question-answering?
2. Have the authors considered methods to handle cases with low clusterability?

### Soundness
3

### Presentation
4

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
This paper considers the problem of reducing the "KV cache" (i.e. the cache needed to compute each entry of the Attention layer). Specifically, the paper observes experimentally that the keys in the existing systems that use Attention tend to be clustered. Then it proposes to utilize this insight into creating an approximation for the Attention layer by at a _very_ high level by only only remembering the "centers" of the said clusters. Doing this reduces both the space needed to store the KV cache as well as the time needed to compute the (clustered approximation) to the Attention layer.

The paper presents algorithms/data structures to both maintain the cluster and to compute the approximation to the Attention later. Assuming $(m,\delta)$-_clusterability_ (i.e. there are $m$ clusters and the max radius of each cluster is $\delta$), the paper proves that the proposed algorithms use sub-linear time and space (as opposed to the linear time and space for the vanilla Attention implementation) (under certain assumptions on the values of $m$ and $\delta$).

The paper also presents experimental results that shows that the proposed method performs better than two existing KV cache compression systems-- Sink and H20.

### Strengths
* The paper presents a nice clean theoretical modeling on how Attention keys cluster (and presents some experimental results to show that this is relevant in practice).

* The paper presents nice clean theoretical bounds on the performance of the proposed algorithms (that show that they improve upon the bounds of the plain vanilla Attention implementation).

* The experimental results show improvements over two existing systems-- Sink and H20.

### Weaknesses
There are two major weaknesses of the paper for me-- first, the paper analyzes the improvements in time and space in the RAM/CPU model but deep learning (DL) systems and specifically Transformer models today are run on GPUs (as is the case with the experiments in the paper) and it is not clear that the theoretical improvements in the paper would translate to the GPU model. The second (and related) weakness is that the paper does not do comparison with other architectures that aim to reduce the KV cache but do have implementations that are "GPU aware."

Theoretical Analysis is on the RAM model
----------------------------------------

The theoretical analysis presented in the paper is for the RAM model and presents a random sampling based algorithm to show improvement in the RAM/streaming model. However, modern day system pretty much all run on GPUs and TPUs where random sampling does not tend to work well. This is primarily because in modern hardware all operations happen at the level of blocks-- in other words, reading one entry from a block is the same as reading the entire block. So e.g. if the random sampling does not take this block structure into account (which the algorithms in the paper from what I can tell do _not_ do), then it is not clear if the theoretical gains will manifest in actual systems since it might still be reading all the blocks even if the actual number of entries read by random sampling is much lower. Specifically, it is not clear to me that the proposed implementation would be competitive against an implementation of Attention like FlashAttention (https://github.com/Dao-AILab/flash-attention), which is an _exact_ Attention implementation that is hardware aware. Further, modern GPUs/TPUs allow for block-block matrix-multiplication in $O(1)$ time and an algorithm that is created specifically to exploit such natively supported operations might have a higher number of FLOPs than the proposed algorithm but would still beat the proposed algorithm in wall clock speed.

In summary, the modern hardware systems have native support for specialized operations, which the proposed algorithm does not seem to exploit. This does not make me confident that the proposed algorithm would work better than these hardware aware implementations.

Insufficient comparison with prior related work
-----------------------------------------------

The paper's weakness with adequate comparison with prior work can in turn be divided into three parts:

1. Of course it is entirely possible that the proposed algorithms actually run faster hardware aware algorithms (like FlashAttention) but no such comparison is provided in the experimental section of the paper. It is possible that the "Exact" Attention implementation uses a FlashAttention implementation but it is not clear from the paper whether this is the case. It would be good to either get confirmation that the "Exact" Attention uses a FlashAttention implementation (if so, which version) or if not, then it would be good to see comparison performance numbers with FlashAttention.
2. Moving beyond hardware aware exact FlashAttention implementations, there are approximate Attention implementations that have good implementations on modern hardware. Two recent examples-- The Hedgehog & the Porcupine (https://arxiv.org/abs/2402.04347) and Based (https://arxiv.org/abs/2402.18668) utilize the fact that one can approximate the exp function with low degree polynomials and then noting that apply a low degree polynomial to each entry of a low rank matrix gives rise to low rank matrices allows one to use these Taylor series approximations to define a "kernel" and then to use linear Attention instead of softmax Attention to reduce the KV cache size. These recent papers have implementations suited to modern hardware and have accuracy that matches those of Transformers (but are much more efficient).
    * I would like to point out that the above idea of using Taylor series + linear attention/low rank matrices have been exploited before. E.g. see the paper of Alman and Song (https://arxiv.org/abs/2302.13214) and the earlier work of Chen et al. (https://arxiv.org/abs/2110.15343). The latter paper also proposed to compress the KV cache under the assumption of keys being clustered (though the clustering model in this paper is cleaner and more general). But in general, for the theoretical results, it would be good to compare the theoretical results in this paper and the results e.g. in the Alman and Song paper (for the case when they get $n^{1+o(1)}$ implementation of Attention.
    * In addition to the above body of work on approximating Attention there have been alternative Attention free models that have garnered a lot of Attention. Mamba (https://arxiv.org/abs/2312.00752, also see Mamba 2: https://arxiv.org/abs/2405.21060) is probably the model that has garnered most attention. These models have comparable accuracy to Transformer but are much faster and use much smaller cache sizes.
    * Overall the paper should present a comparison with the above body of work (for approximate Attention models this should be done in both Tables 2 and 3, while for Attention free models comparison should be made in Table 3).
3. Finally, one big downside of the results presented in this paper is that the _accuracy_ over the exact Attention implementation takes a big hit. The proposed new algorithms do get an improvement of up to $50$ percent in cache size but also take a similar hit in accuracy. By comparison, the related work mentioned in the above bullet get a much larger improvement in cache size while _essentially not losing in accuracy/perplexity at all_ when compared to exact Transformers. However, these works are not evaluated in Tables 2 and 3 in the paper.

### Questions
Please address the two high level weaknesses pointed out above. Specifically,

1. Please comment on why the presented improvements in the RAM model would translate into wall clock improvement in modern GPU/TPUs.
2. Please compare (both the theoretical and experimental) existing results (as pointed out above and are not compared in the paper to the proposed system) with the proposed (theoretical and experimental) results.

Post-rebuttal comments
----------------------------

The authors addressed most of my concerns so am upping my score to a 5.

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
4

### Summary
This paper gives a sublinear time and space algorithm for a streaming version of attention where query, key, and value tokens are given online and the attention needs to be approximately maintained. Some recent papers have studied using improved caching algorithms to efficiently solve this problem, and this paper aims to improve on them.

It makes a key new assumption, that the keys in the attention problem are clusterable, i.e., they can be grouped into a sublinear number of clusters which have small Euclidean radius. It verifies experimentally that RoPE-based open source models seem to satisfy this. It then gives a provably correct and efficient algorithm given this assumption. Finally, it shows via experiments that the new algorithm improves in accuracy while maintaining low memory on some tasks compared to prior work.

### Strengths
- The paper introduces a new clusterability assumption and backs it up with experimental evidence. I think it's particularly interesting that this assumption holds for better-performing open-source LLMs but not worse-performing ones. Focusing on this new assumption may help to guide future work in this area.
- The paper brings in the powerful toolbox of streaming clustering algorithms to give an improved attention algorithm. It's fantastic when algorithms that have been developed over decades in other contexts can be applied to modern machine learning like this.
- The new algorithm has clean, provable guarantees for accuracy, running time, and memory use.
- The paper is solving a fundamental problem for LLMs.
- The paper is generally written well.

### Weaknesses
- This general approach seems less effective for long-range prompts than in other settings (see table 3), but long-range prompts seem to be the main motivation for efficient token generation (see the first couple lines of section 1.1). 
- There are a few details skipped, especially in the experiments section, that I'm confused about. See the questions below. In particular, the idea of using a sliding window of tokens (similar to prior work) is introduced only in the experiments section 4 but not in the algorithm theory above, and I'm unsure how much of the experimental validation is due to this and not actually the clustering.

### Questions
- Theorem 2.4 says the algorithm result satisfies equation (1); should it say equation (3) or (4)?
- Have sampling-based approaches for attention been used previously (in practice or theory)? I'm confused about why operator norm guarantees (eq (2)) are being used here, since they don't seem to have been used much previously for LLMs. Can you give intuition for why operator norm is a reasonable choice?
- In section 4.1 / table 2, how does the window size l compare between the three caching algorithms? Is the increase in accuracy coming because ClusterGen is able to use a bigger l? How significantly does integrating the window approach improve your algorithm? The use of the sliding window should be mentioned earlier when describing the algorithm, and not just in the experiment section.
- Did you verify the clustering assumption (definition 2.1) in the section 4 experiments? Is there a relationship between how clusterable the data is and the accuracy of the model? Does this explain why ClusterGen is better at some tasks than others in table 3?
- How did you choose which of the algorithms described in the related work (section 1.1) to compare with in the experiments (section 4)?
- How do the running times of the different algorithms compare in experiments? It seems only the memory usage is being considered.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of streaming attention problem, where key-value-query pairs are streamed to the algorithm and one needs to output the approximate attention module given by the accumulated key-value pairs and the current query. The goal is to design a data structure that uses sublinear in $n$ space. This paper achieves this goal by observing that in practice, the encodings of keys are usually well-clustered, hence it assumes that the keys can be clustered into sublinear in $n$ clusters. The data structure then consists of two main components: a dynamic sampler that approximates the matrix-matrix product, where the sampling is cleverly performed on the accumulated value matrix hence avoiding the hassle of handling the matrix involving query and entrywise exponentiation. The other component handles the normalization factor defined as $\sum_{i\in [n]} \exp(\langle k_i, q_n\rangle)$, where here it crucially uses the fact that keys are clusterable hence one could maintain a sublinear number of clusters and some uniform samples of each cluster, and approximate the normalization factor using this small coreset. Experiments are performed showcasing the effectiveness of the proposed algorithm. In particular, it was empirically checked the query vector has $O(1)$ norm and keys are generally clusterable, this enables the proposed algorithm to outperform several currently popular KV cache algorithms.

### Strengths
This paper studies an interesting problem that holds great theoretical and practical importance, namely developing a KV cache algorithm with sublinear memory. In practice, even an algorithm that uses constant factor smaller memory than $n$ would be valuable. The assumption imposed by this paper is quite natural, as embeddings for keys are usually clusterable among other nice properties. The proposed algorithm is simple, which is a big advantage, as it enables practical implementation. Sampling, in general could be computed quickly. 

Overall, I like this paper as it studies a very practical problem from theoretical lens, obtaining good theoretical guarantees and simple algorithms, which in turn would lead to good practical solutions.

### Weaknesses
At least from experiments, it seems that the algorithm performs better when $n$ is smaller (5000, 7000 and 9000) compared to when $n$ is larger (20000). On the other hand, the main merit of this algorithm is when $n$ is very large as that is precisely the setting when $o(n)$ memory and update, query time is invaluable. I encourage authors to conduct more experiments on large $n$, though I do understand the difficulty as large $n$ requires more memory and compute, so this could be taken as a minor suggestion rather than a major complain.

### Questions
Typo:

Line 196: "probabilities proportional to $\\|k_i\\|_2^2$" should be $\\|v_i\\|_2^2$ as the importance sampling is performed on $V_n$.

Question:

Can you provide a practical guideline on how to choose the hyperparameters of the data structure?

Comment:

Throughout the paper, the use of k is quite inconsistent, sometimes it's used as k and sometimes $k$. It's better to make it consistent.

### Soundness
3

### Presentation
3

### Contribution
3
