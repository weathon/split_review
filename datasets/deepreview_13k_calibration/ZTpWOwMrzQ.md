# Radar: Fast Long-Context Decoding for Any Transformer

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 8, 6, 3, 8

## Abstract
Transformer models have demonstrated exceptional performance across a wide range of applications. Though forming the foundation of Transformer models, the dot-product attention does not scale well to long-context data since its time requirement grows quadratically with context length. In this work, we propose Radar, a training-free approach that accelerates inference by dynamically searching for the most important context tokens. For any pre-trained Transformer, Radar can reduce the decoding time complexity without training or heuristically evicting tokens. Moreover, we provide theoretical justification for our approach, demonstrating that Radar can reliably identify the most important tokens with high probability. We conduct extensive comparisons with the previous methods on a wide range of tasks. The results demonstrate that Radar achieves the state-of-the-art performance across different architectures with reduced time complexity, offering a practical solution for efficient long-context processing of Transformers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper describes a training-free approach to speed up attention computation over a long context, by essentially performing a hierarchical search for the 'closest' tokens in the attention dot-product. Tokens are grouped into segments, and attention is restricted to the closest segments --- which itself is found through dot product attention to a 'segment'-level averaged projected feature.

The paper provides theoretical analysis of this approximation, and experiments show speedups over vanilla attention without significant drop in quality.

### Strengths
- The paper is very well written and motivated.
- The hierarchical search approach is novel, as is the use of averaged random projection features to allow identifying segments without retraining.
- The theoretical analysis is a nice addition to the paper and is insightful in understanding why we expect the approach to work.
- The experimental results are solid, and the approach appears to achieve real speedups when run on GPUs (not just in theoretical flops).

### Weaknesses
 - There seems to be an assumption that segments should be made of contiguous tokens. This might be a safe assumption, but should be discussed. I can imagine an 'adversarial' setting where the ideal attention matrix would have been centered on a subset of tokens spaced far apart (i.e., each in a different segment). The theoretical analysis could perhaps have focused on this as well (how likely it is for the top-k segments to include the top-k tokens).

- It would have been nice to include some examples of the true and approximated attention maps (as heatmap figures, and perhaps also as text examples). We only see performance numbers at the final task, but not directly how well attention is being approximated.

### Questions
In addition to speaking to the weaknesses listed above, it would be good if the authors could discuss whether they think this kind of hierarchical approximation to attention might work even better if it were included during training, not just as a post-training step.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Transformer are the core of LLMs. This paper introduces a novel approach coined "Radar", which accelerates inference and is even training-free. Theoretical results are provided and the effectiveness is shown by numerical experiments.

### Strengths
* The new approach selects the most important tokens with high probability.
* It accelerates inferences for transformers.
* The method does not need to be trained.
* Theoretical results are provided.
* Also the numerical results are convincing.

### Weaknesses
no weaknesses

### Questions
no questions

### Soundness
4

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
This work introduces a novel training-free approach that accelerates inference by dynamically identifying the most important context tokens. The paper also provides proofs of algorithmic correctness and includes a time complexity analysis. The experimental results indicate competitive performance.

### Strengths
1. The problem addressed is significant and appealing, focusing on a crucial aspect of LLM performance.
2. The paper presents a novel approach for accelerating LLM inference by selecting the most important context tokens.
3. The authors provide detailed proofs of algorithmic correctness and analyze the time complexity.
4. The experimental results are competitive, highlighting the effectiveness of the proposed method.

### Weaknesses
1. The analysis of time complexity needs more detail, particularly regarding lines 8 to 11 of Algorithm 1. This dynamic restructuring step may take more time than $O(t)$. Based on my understanding, this section could have a total time complexity of $\sum_{c=1}^{\sqrt{t}} c^2 = O(t^{3/2})$. Thus, the time required for calculating the importance score of a single segment is not constant.

### Questions
See weakness. If I made mistakes, please tell me and I am glad to give a high score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new method to approximate the softmax attention mechanism in transfomer architecture. The method works by segmenting the key embeddings and then for each query picking a few segments which have highest attention scores on average and computing the attention scores for the keys in those segments exactly. The mehtod uses random features proposed in the Performer paper  to estimate the average attention score of each segment.

### Strengths
The paper proposes a practical and easily implementable algorithm that demonstrates strong performance compared to existing streaming attention and sliding window attention methods.

### Weaknesses
The paper lacks a comparison with several relevant works focused on attention acceleration. Notably, the following papers explore sparse, low-rank, and combinations of these approaches with near-linear runtimes for long context, and it remains unclear how the proposed method measures up against them:

- `Chen, Beidi, et al. "Scatterbrain: Unifying sparse and low-rank attention." Advances in Neural Information Processing Systems 34 (2021): 17413-17426.`
- `Zandieh, Amir, et al. "Kdeformer: Accelerating transformers via kernel density estimation." International Conference on Machine Learning. PMLR, 2023.`
- Han, Insu, et al. "Hyperattention: Long-context attention in near-linear time." arXiv preprint arXiv:2310.05869 (2023).
- `Zandieh, Amir, et al. "SubGen: Token Generation in Sublinear Time and Memory." arXiv preprint arXiv:2402.06082 (2024).`
- `Roy, Aurko, et al. "Efficient content-based sparse attention with routing transformers." Transactions of the Association for Computational Linguistics 9 (2021): 53-68.`

Additionally, this method does not tackle the memory concerns regarding storing key-value embeddings in the KV cache; it requires retaining all key and value embeddings in the cache during the generation phase.

### Questions
- How does your method compare against the aforementioned works in experimental evaluations?

- The paper does not clarify how tokens are segmented. Do you segment the stream of tokens into contiguous chunks, or do you employ a different ordering method?

Additionally, I would like to note: please try to address my concerns, and rest assured that I will consider raising my score if you provide sufficient experimental results during the rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an algorithm for accelerating LLM inference by efficiently selecting of important tokens. Its headline claim is a reduction from $\mathcal{O}(t^2)$ sequence length complexity to $\mathcal{O}(t^{3/2})$.

### Strengths
I am not an expert in efficient approximations to softmax attention, so I cannot confidently speak to the novelty of this algorithm relative to other methods. I will confine my comments to the results as presented. The proposed algorithm is simple, and the experiments demonstrate that it achieves a seemingly reasonable balance of accuracy and efficiency. Moreover, I found the paper to be reasonably clearly written.

### Weaknesses
In my mind, the paper would be stronger if there was a clearer link between Theorem 2 and the experiments. Namely, unless I've missed something, the authors don't actually measure whether their algorithm retrieves the correct top-k index set in their experiments. It would be useful to do so, and to comment on whether by those results the bound in Theorem 2 is practically useful or not. It would also be useful to know something about the distribution of attention scores, which would affect what value of $k$ is reasonable. More precise (and in some sense more mechanistic) quantifications could help the reader get a better sense of why your method works.

In particular, the lack of direct measurement of top-k retrieval accuracy makes it difficult to assess the practical relevance of the theoretical bound. The experiments focus on downstream task performance, which is an indirect measure of the approximation quality. It would be more convincing to see a direct evaluation of how well the algorithm identifies the true top-k attention scores. Furthermore, the paper lacks any analysis of the attention score distribution. This distribution is crucial because it determines the effectiveness of top-k selection. If the distribution is highly skewed, a small $k$ might capture most of the attention mass, whereas a more uniform distribution might require a larger $k$ for similar performance. Without this analysis, it's hard to know if the chosen $k$ values are appropriate or if the algorithm is robust to different attention distributions.

Do you have any intuition for why the H20 and SnapKV methods perform so poorly when applied to the Mistral PG19 model (Appendix C)? The difference is quite striking, so it would be useful to have at least a hypothesis for why these methods do not generalize across architectures. This could also provide useful context for why the proposed method successfully generalizes.

There appears to be a typo on Line 837, as the square brackets enclose the equality.

It might be useful to state Lemma 1 in terms of concentration to the expectation at large $n$, as that could give a bound on error in a practical setting.

Given that the claimed time-complexity improvement is in the exponent of a power law, it would be useful to use logarithmic scales for time in the figures, so that one can see how tight the bound is.

It could be semantically useful to use a different color scheme for Figure 4, to distinguish the fact that here different dimensions are being used rather than different algorithms.

### Questions
- Do you have any intuition for why the H20 and SnapKV methods perform so poorly when applied to the Mistral PG19 model (Appendix C)? The difference is quite striking, so it would be useful to have at least a hypothesis for why these methods do not generalize across architectures. This could also provide useful context for why the proposed method successfully generalizes. 

- There appears to be a typo on Line 837, as the square brackets enclose the equality. 

- It might be useful to state Lemma 1 in terms of concentration to the expectation at large $n$, as that could give a bound on error in a practical setting. 

- Given that the claimed time-complexity improvement is in the exponent of a power law, it would be useful to use logarithmic scales for time in the figures, so that one can see how tight the bound is. 

- It could be semantically useful to use a different color scheme for Figure 4, to distinguish the fact that here different dimensions are being used rather than different algorithms.

### Soundness
3

### Presentation
3

### Contribution
3
