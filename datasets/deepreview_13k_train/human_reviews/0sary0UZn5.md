# On the Limitation and Redundancy of Transformers: A Rank Perspective

- Decision: Reject
- Scores: 8, 3, 3, 8

## Abstract
Transformers have showcased superior performances across a variety of real-world applications, particularly leading to unparalleled successes of large “foundation” models. 
However, since these models are usually trained on web-scale datasets, the overall computation and memory loads are considerably increasing, calling for more *efficient* methods in machine learning. 
In this work, we step towards this direction by exploring the architectural limitation and redundancy of Transformers via investigating the ranks of attention score matrices. 
On one hand, extensive experiments are conducted on various model configurations (model dimensions, heads, layers, etc) and data distributions (both synthetic and real-world datasets with varied sequence lengths), uncovering two key properties: 
although the attention rank increases with the head dimension $d_h$, as expected, the rank is eventually upper bounded (limitation) and gets saturated (redundancy). We call them the *low-rank barrier* and *model-reduction effect*, respectively. 
On the other hand, we provide rigorous demonstrations for these observations through a fine-grained mathematical analysis, highlighting (i) a consistent theoretical upper bound ($\approx 0.63n$, $n$: the sequence length) of the attention rank regardless of the head dimension $d_h$, and (ii) a critical position of the rank saturation ($d_h=\Omega(\log n)$).
These results shed light on the inductive biases and internal dynamics of Transformers, contributing to the theoretical understanding and assessment of the model capacity and efficiency in practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work explores the architectural limitations and redundancy in Transformer models by analyzing the ranks of their attention score matrices. Through extensive experiments across diverse model configurations and data distributions, the authors uncover two key properties: the low-rank barrier and the model-reduction effect. These findings are rigorously supported by a fine-grained mathematical analysis, revealing (i) a consistent theoretical upper bound on the attention rank (0.63n) and (ii) a critical threshold for rank saturation where the hidden dimension h scales as Ω(log n). These results illuminate the inductive biases and internal dynamics of Transformers, deepening our theoretical understanding and enabling better assessment of model capacity and efficiency in practical applications. These insights are particularly valuable for Transformer architecture design and optimization.

### Strengths
This work studies a fundamental problem in Transformer model efficiency. In this paper, the authors present extensive empirical results and rigorous theoretical analysis, offering critical insights into the architectural limitations and redundancy in Transformer models. The findings are highly valuable for designing more efficient Transformer-based architectures.

### Weaknesses
While the paper presents extensive experiments on various model configurations and data distributions, the evaluation focuses on a few common computer vision datasets (CIFAR-10, CIFAR-100, and SVHN). This raises the question of whether the findings generalize to other domains, such as natural language processing or audio processing, where Transformer models are widely used. The analysis of attention rank, while thorough for vision tasks, may not directly translate to the sequential nature of language or the time-series characteristics of audio. For instance, the fixed input size of images contrasts with the variable-length sequences in NLP, potentially leading to different rank behaviors. The paper lacks a discussion on how the observed low-rank barrier might interact with the positional encodings and masking strategies commonly employed in NLP Transformers. Furthermore, the study does not explore the impact of different attention mechanisms, such as sparse attention, which could alter the rank properties of the attention matrices.

### Questions
The findings are rather interesting. Would they apply to other Transformer models, such as those used in NLP and audio processing tasks?

### Soundness
4

### Presentation
4

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
This paper focuses on the attention matrix in transformers, and studies the effect of the head dimension on the rank of this attention matrix. Under assumptions on the data and the transformer weights, the paper empirically and theoretically highlight that the rank of the $(n \times n)$ attention matrix for $n$-length input sequences is upper-bounded by a quantities close to $0.63n$, and that attention matrix rank grows with the head dimension $d_h$ but the gain in the attention matrix rank diminishes as the head dimension grows, demonstrating a "diminishing returns" behaviour. This behaviour is demonstrated with vision transformers where the ranks of the attention matrix of the first transformer block are reported as the head dimensions is varied.

### Strengths
This paper considers an interesting topic of analysis, studying the rank of the attention matrix, and how it is limited from above, which puts a limitation on the expressivity of the attention mechanism.

### Weaknesses
 - (W1) In my opinion, the main weakness of this paper are the analysis tools and assumptions utilized for providing the rank upper bounds which is used make the main claim of this paper that the attention matrices are rank limited. Here are some specific issues:
  - (W1.1) There are many variations of multi-head where the value matrix $\mathbf{V}^{(i)} \in \mathbb{R}^{n \times d_h}$ has the head dimension $d_h$. But usually the key and query matrices do not need to have the same dimensionality as the value matrix. Furthermore, there are versions where $d_h \times h \not= d_{\text{model}}$, and $W_o$ projects $h \times d_h \to d_{\text{model}}$. For example $d_h = d_{\text{model}}$. How does the results studied here be affected by these different strategies? Furthermore, there are versions that just vary the value matrix dimension, but the query/key matrix dimensions are not affected by the number of heads. In that case, this analysis is not applicable. In fact, in the empirical evaluation of Figure 4b (which uses a different variation), we are able to go beyond the $0.63$ range with $d_h < 5$ and goes up to 0.68. Different variations of this could allow us to go to full rank (or close to it). In fact, it would seem that, with $h = 1$, we should be able to recover the full-rank. Can the authors please explicitly discuss how their analysis might change for these different variations? Alternately, can the authors please justify their choice of focusing on one particular formulation of multi-head attention as this would clarify the scope and limitations of the presented results?
  - (W1.2) It is not clear how much of this analysis is dependent on the normal distribution assumption on the weigthts and tokens? Consider a case where the $\mathbf{K} = \mathbf{Q} = \mathbf{X}$ with each $\|\|\mathbf{x}_i \|\|_2 = 1$ and the temperature is low enough that we are doing top-1 attention (which is also what is considered in this paper), then the matrix $\textbf{Attn}(\mathbf{X}) = I_n$ which is the $n\times n$ identity matrix, which is full-rank. So this clearly gives a case where the proposed bound is violated. Why is this an implausible case, or conversely, how does the presented analysis subsume this situation? While the identity attention matrix seems too special, one can think of a problem where each token needs to just attend to the token right before it (that is $\textbf{Attn}(\mathbf{X})[i, i-1] = 1, \forall i > 1$, leading to an off-diagonal almost full-rank attention matrix. Can the authors please address this specific counterexample and explain how it relates to their assumptions and results?
  - (W1.3) It is odd that while we are studying the effect of the head dimension on the rank of the attention matrix, Theorem 1 has no dependence on $d_h$. This makes the result somewhat odd. I think this is an artifact of the assumptions and analysis, which effectively reduces the attention matrix to the case where each row has 1 in one of the $n$ indices at random in a query independent way. This is equivalent to each token sampling uniformly at random with replacement a token out of the $n$ tokens. Thus the expected number of unique tokens attended to in the complete attention matrix (with only one non-zero per row) is equivalent to its rank. Using standard combinatorics arguments, this expected number of unique tokens attended (for sampling with replacement) to will come to $n(1 - (1 - 1/n)^n)$ which approaches the $\approx 0.63n$ bound. While the analysis in the paper is correct, this form of an attention matrix is not useful or interesting for real applications of transformers, and also the head dimension $d_h$ plays no role here, which is different from the motivation of this paper. Can the authors please explicitly discuss this apparent discrepancy and explain how it relates to their overall claims about the effect of head dimension on attention rank? Alternately, the authors can also share (or point to) a finer-grained analysis that directly tie this rank upper bound to the head dimension. 
  - (W1.4) It is not clear why line 363 "Recall that the rows of $\mathbf{X} \mathbf{W}_q \mathbf{W}_k^\top \mathbf{X}^\top = \mathbf{Q} \mathbf{K}^\top$ are independently and identically distributed as $\mathcal{N}(\mathbf{0}_n, \mathbf{K} \mathbf{K}^\top)$" is true. Why is this distribution independent of $\mathbf{Q}$? Similarly, equation (6) seems odd, highlighting that the rows for each query in the attention matrix are distributed identically. This query-independence is both odd and counter to the main motivation of transformers that usually have different attention patterns for different rows/queries.
- (W2) This is smaller weakness, but it is not clear what we can do with this rank-bounded-ness insight (assuming that this upper bound is useful and accurate). It is not clear what problems a transformer is unable to solve because of this rank-boundness, or what problems it would have been able to solve if it was able to have full-rank attention matrices. Can the authors please provide specific examples or hypothetical scenarios where this rank-boundedness might impact transformer performance or capabilities as this would help connect their theoretical results to practical applications.

Minor comments:
- (C1) It would be good to make the caption of Figure 1 self-sufficient (or point to the part of the text where the complete description is available). Otherwise, having such an introductory figure on page 2 seems a bit confusing.
- (C2) The "less than or around 0.01" comment in Table 2 caption makes that "log-dependence" argument a bit less convincing. One can alternately argue that for sequence length of 200, we needed more than a linear increase in $d_h$, implying a very different story.
- (C3) While the assumptions on the input are discussed in Remarks 2 and 3, note that the assumptions on the key/query projection matrices seem more restrictive to me, and require appropriate discussion.

### Questions
- (Q) Both KDEFormer [A] and Hyperattention [B] seems to also consider the rank of the attention matrix theoretically (among others). However, these references are missing. How is the setup of this current paper positioned against these references?
  - [A] Zandieh, Amir, et al. ["Kdeformer: Accelerating transformers via kernel density estimation."](https://proceedings.mlr.press/v202/zandieh23a.html) International Conference on Machine Learning. PMLR, 2023.
  - [B] Han, Insu, et al. ["HyperAttention: Long-context Attention in Near-Linear Time."](https://openreview.net/forum?id=Eh0Od2BJIM) The Twelfth International Conference on Learning Representations. 2024
- (Q) It is not clear how the rank of the attention matrix is tied to the expressivity of the attention mechanism. Are there existing results that make this connection?
- (Q) Given the use of softmax operation in the attention matrix, isn't it expected that the attention matrix will not be full rank? Part of the motivation for schemes like Performers [C], Scatterbrain [2] etc is this low rank structure. In fact, if we remove the softmax, this linear attention can probably have full rank if the head dimension is large enough but is not desired since the softmax operation is what makes attention work.
  - [C] Choromanski, Krzysztof Marcin, et al. ["Rethinking Attention with Performers."](https://openreview.net/forum?id=Ua6zuk0WRH) International Conference on Learning Representations. 2020.
- (Q) In Section 3.1, whose rank are we computing? The $\textbf{Attn}^{(i)}(\mathbf(X))$ matrices? How are the ranks aggregated across the multiple heads?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript investigates the relationship between head dimensions and the corresponding attention score matrix ranks. The authors identify two phenomena in Transformer attention ranks: (1) an upper bound on attention rank, referred to as the "low-rank barrier," and (2) the "model-reduction effect," which denotes the diminishing returns on attention rank when increasing head dimensions beyond a certain threshold. Experiments are provided to validate these findings.

### Strengths
1. The paper offers a new theoretical perspective on Transformer architecture, particularly in characterizing the limitations of attention ranks, which is insightful for understanding the underlying mechanics of model capacity.

2. The two phenomena in Transformer attention ranks: (1) an upper bound on attention rank, referred to as the "low-rank barrier," and (2) the "model-reduction effect," which denotes the diminishing returns on attention rank when increasing head dimensions beyond a certain threshold, are quite interesting and intriguing.

### Weaknesses
1. Lack of motivation: First of all, why should one care about the rank of the attention matrix? While it is interesting to note that the attention matrices display the low-rank barrier and model-reduction effects, it is unclear how these findings directly impact the design or usage of Transformer models in practical applications. The study would benefit from a more explicit motivation linking these theoretical insights to specific challenges in machine learning or computational limitations. In particular, attention ranks do not seem to have a clear relationship with the model performance or expressive power. Have you identified whether the low-rank barrier correlates with any performance metrics? Could the model-reduction effect be leveraged to improve model efficiency?

2. Assumptions in theoretical analysis: The theoretical analysis assumes orthonormal input sequences to attention, which may not fully reflect the reality. For example, there are other evidence in the literature suggesting that contexualized token embeddings tend to be anisotropic [Ethayarajh, 2019]. While the authors justify this orthogonal assumption by citing Tian et al. 2024, further discussion on the applicability of the theoretical results in varied real-world scenarios would enhance their robustness. In particular, the assumption of orthonormal inputs significantly simplifies the analysis, but it is unclear how the low-rank barrier and model-reduction effects would manifest with more realistic, potentially correlated, input embeddings. The analysis should address how deviations from orthonormality might affect the observed phenomena.

3. Limited exploration of practical applications: While the theoretical findings are interesting, the work could benefit from a more explicit discussion of how these insights translate into practice. For example, I would be interested to see if the findings on the model-reduction effect could lead to model compression techniques without significant performance loss. The paper should explore specific methods for leveraging the observed rank saturation to reduce model size or computational cost. For instance, could the saturation point be used to determine optimal head dimensions, or could it inform pruning strategies for attention heads?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the limitations of the rank of attention matrices, with a goal of gaining a better understanding of the expressive power of transformers. First, the paper provides experiments on randomly generated data from different distributions and show empirically a rank saturation at around 0.63n (n being the input dimension). Next, it is proved theoretically that transformers at initialization also exhibit this rank saturation. Finally, experiments are given on the CIFAR-10/100 and SVHN datasets showing a rank saturation phenomenon.

### Strengths
The phenomenon that is presented in the paper is interesting and sheds new light on the expressive power of attention matrices. The paper provides theoretical results and complementing empirical validation under different setting. The technical parts of the paper are clearly written and easy to follow.

### Weaknesses
I have some concerns with the presentation of the paper and the theoretical and empirical results:

1) The results of Sections 3 and 4 discuss transformers with random data, random weights, or both. It is difficult to generalize from that to general transformers trained on real data. In general, I believe it is OK to have a theoretical paper with restricted assumptions. However, the presentation of this work, and specifically the abstract and introduction, gives the impression that the low-rank phenomenon is general and not restricted to random settings. If the focus of the paper is random settings (i.e. random data and/or weights) this should be clearly stated. If the message of the paper is more general, then further evidence should be provided as I discuss later.

2) The theoretical result (Theorem 1) is nice, but limited and isn’t enough in itself for a theoretical paper. The biggest limitation is the assumption of the data. Although the authors justify assuming that the samples are almost orthogonal (e.g. drawn from a Gaussian or uniform on a sphere), the assumption is that they are exactly orthogonal. This allows only for n samples, instead of O(2^n) samples. It seems possible to prove this result for almost orthogonal data. The current proof only considers the case where the data vectors are strictly orthonormal, which is a very strong assumption that limits the practical relevance of the theorem. A more realistic scenario would involve data that is nearly orthogonal, where the dot product between any two data vectors is close to zero but not exactly zero. The theorem should be extended to this case, and the allowed deviation from orthogonality should be explicitly quantified.

3) The “real-world experiments” in section 5 are done on very small-scale image datasets, CIFAR-10/100 and SVHN. It would be more convincing to do experiments on larger datasets, and specifically text datasets where it is possible to change the embedding dimension, and thus experiment on the effects of changing n.

### Questions
- What would the effect of the rank in Theorem 1 be when having data that is almost orthogonal?

- Does the rank saturation phenomenon also happen in real datasets when the input dimension n varies?

### Soundness
4

### Presentation
3

### Contribution
3
