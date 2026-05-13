# Time, Space and Streaming Efficient Algorithm for Heavy Attentions

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
A central problem related to transformers can be stated as follows: given two $n \times d$ matrices $Q$ and $K$, and a non-negative function $f$, define the matrix $A$ as follows: (1) apply the function $f$ to each entry of the $n \times n$ matrix $Q K^T$, and then (2) normalize each of the row sums of $A$ to be equal to $1$. The matrix $A$ can be computed in $O(n^2 d)$ time assuming $f$ can be applied to a number in constant time, but the quadratic dependence on $n$ is prohibitive in applications where it corresponds to long context lengths. For a large class of functions $f$, we show how to find all the ``large attention scores", i.e., entries of $A$ which are at least a positive value $\varepsilon$, in time with linear dependence on $n$ (i.e., $n \cdot \textrm{poly}(d/\varepsilon)$) for a positive parameter $\varepsilon > 0$. Our class of functions include all functions $f$ of the form $f(x) = |x|^p$, as explored recently in transformer models. Using recently developed tools from randomized numerical linear algebra, we prove that for any $K$, there is a ``universal set" $U \subset [n]$ of size independent of $n$, such that for any $Q$ and any row $i$, the large attention scores $A_{i,j}$ in row $i$ of $A$ all have $j \in U$. We also find $U$ in $n \cdot \textrm{poly}(d/\varepsilon)$ time. Notably, we 
(1) make no assumptions on the data, (2) our workspace does not grow with $n$, and (3) our algorithms can be computed in streaming and parallel settings. We call the attention mechanism that uses only the subset of keys in the universal set as LevAttention since our algorithm to identify the universal set $U$ is based on leverage scores. We empirically show the benefits of our scheme for vision transformers, showing how to train new models that use our universal set while training as well, showing that our model is able to consistently select ``important keys'' during training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies efficient algorithms for attention computation in transformer models. In particular for query $Q$ and key $K$ matrices in $\mathbb{R}^{n\times d}$, and function $f$ applied to each entry of $QK^T$ (for eg. $f=x^p$ for some $p>0$), this paper studies efficient algorithms to approximately compute $f(QK^T)$ followed by a row-normalization. The main contribution of the paper is to show that for any $\epsilon>0$ there exist a subset $U\subset[n]$ of keys, that is the rows of the key matrix $K$, such that for any query $q$, that is a row of query matrix $Q$, if the attention score of $q$ with $k_i$ after normalization is greater than $\epsilon$ then $i\in U$. The size of this set $U$ is $(\sum_{i\in [n]}\sigma_i^f(K))/\epsilon$ where $\sigma_i^f$ is the $i^{th}$ $f$-sensitivity score of $K$. For eg. when $f=x^2$ these sensitivities are nothing but the $\ell_2$ leverage scores of $K$. The set $U$ is independent of $Q$ and thus can be used to compute attention scores with any $Q$ in the future for a fixed $K$. Moreover using fast algorithms developed in the literature for computing $f$-sensitivities for a broad class of functions $f$, the set $U$ can be computed efficiently. For eg for any constant $p$, for $x^p$ the set $U$ can be computed in time $nnz(K)+poly(d/\epsilon)$ using the input sparsity time algorithm of Cohen and Peng for computing $\ell_p$ leverage scores.

### Strengths
The main strength of the paper is to apply tools from randomized numerical linear algebra to naturally arrive to the conclusion that if the attention score of a query is more than $\epsilon$ with any particular key, then simply by definition it implies that the $f$-sensitivity (or leverage score for the special case when $f=x^2$) will also be more than $\epsilon$. This directly implies that capturing all the keys of $K$ with sensitvities higher than $\epsilon$ suffices to prove their result. Thus I think the main strength of this paper is develop this connection in more detail, and prove results in various computational settings such as streaming and distributed settings regarding how to efficiently compute this set of universal keys, which I think is a good contribution to the literature.

### Weaknesses
One aspect I would want to get more clarity on is in the experimental section. The authors do arrive at the conclusion that the mass of practical attention matrices for each query can be captured by a small set of universal keys plus a set of local tokens for that specific query. However if this is the case, then algorithms for computing the set of local tokens should also be considered on top of computing the set of universal keys. For eg. it may be the case that in natural language applications, there are sentences in which for each token, it has a high correlation with a few local tokens in a small window around it. In this case, the leverage scores/sensitivities of each key may be large resulting in a large universal set, and the attention matrix has a high rank. However, the attention matrix can still be efficiently approximated with a sparse matrix as it essentially amounts to computing, for each token, the small set of local tokens with whom it has a high correlation.

### Questions
The main question I have is around the weakness that I brought up regarding the experimental section - that is how would the case be handled when $K$ has high rank and every key has high sensitivity ? Morever in the experimental section have the authors considered evaluation with other methods which are popularly used in attention approximation such as flash attention ?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper develops efficient algorithms to identify significant attention scores in transformer architectures without computing the full attention matrix. The key theoretical contribution is proving the existence of a small "universal set" of keys, independent of sequence length, that captures all large attention scores for any query. The authors provide efficient algorithms to find this set and compute attention scores in streaming and distributed settings. The work provides both theoretical guarantees and practical benefits for improving transformer efficiency.

### Strengths
1. Rigorous mathematical proofs for existence and size of universal sets
2. Straightforward integration with existing transformer architectures
3. Strong empirical results on vision transformers

### Weaknesses
1. No evaluation on (large) language models. Limited ablation studies on prediction quality

2. Limited ablation studies on prediction quality

### Questions
1. What are the trade-offs between exact and approximate computation of attention scores?

2. Can the approach be parallelized effectively across multiple GPUs (Tensor Parallel)?

3. What is the impact on training time and convergence?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The attention mechanism is a bottleneck for transformers in terms of efficiency. Standard method of attention mechanism takes quadratic time with respect to the input, where the main issue is to calculate the n by n attention matrix A. This paper studies a class of attention mechanism where we replace f(x) = exp(x) in the vanilla attention with f(x) = |x|^p for some p, and show that regardless of the input data, there exists a set of columns of A that include all the large entries. Moreover, one can find this set efficiently. As a result, one can hope to approximate A by retaining only these large entries efficiently. The paper then generalizes the results to streaming and parallel settings.

### Strengths
1. Speeding up/approximating the attention mechanism is an interesting topic to study. 
2. It is natural to think that as n (sequence length) grows larger, there will only be a subset of keys that are similar, i.e. have larger inner product, with the queries. This paper gives a theoretical analysis on how large such a subset can be and how we can find it. 
3. This paper is clearly written and the mathematical contents are interesting.

### Weaknesses
1. The paper mentions that the standard attention mechanism cannot be well-approximated unless SETH is false (Alman & Song 2023), so I guess the point is that we are hoping for a good/efficient approximation for other attention variants. Although f(x) = |x|^p has been proposed and used in previous work (PolySketchFormer, TensorSketch), I don’t think they are the “gold standard” for attention, and therefore the motivation of studying this polynomial attention is not so clear to me. 
2. Even if we can find all the columns containing all the large entries, does that imply a reasonable approximation after we multiply the attention matrix with the value matrix V? In addition, if we consider multiple self-attention layers, even though we can find the important columns of all attention matrices, it is not clear to me whether we can still have any kind of guarantee on the final output.

Overall I think the problem that this paper proposes is an interesting problem in numerical linear algebra, but I am not really convinced about its impact on transformer theory.

### Questions
The result in this paper, as the authors stated, applies to any Q. It seems like this is because of the way f-sensitivity is defined (by taking the sup over all y). In practice Q might be structured (I think there is a shared-QK transformer where Q and K are identical), and I wonder if we can say anything about it.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors study the attention computation problem: given the query, key, and value matrices $Q, K, V \in \mathbb{R}^{n \times d}$, the goal is to output $D^{-1} A V$, where $A = \exp(QK^\top/d) \in \mathbb{R}^{n \times n}$ and $D = \mathrm{diag}(A {\bf 1}_n) \in \mathbb{R}^{n \times n}$ is a diagonal matrix. Exactly computing the product of $D^{-1}$, $A$, and $V$ requires $O(n^2 d)$ time, which can become very large when the length of the input token $n$ is large, so in this work, the authors present a novel theoretical framework and algorithm for efficiently identifying the large attention scores (the entries of the attention matrix $A$), while maintaining the linear time complexity with respect to $n$. Additionally, this paper finds the large attention scores for a large class of function $f$ in $A = f(QK^\top/d) \in \mathbb{R}^{n \times n}$, which includes all $f(x) = |x|^p$.

### Strengths
1. This paper gives a very solid theoretical foundation showing the existence and properties of universal sets and finds all of the large attention scores with size independent of sequence length. It applies the techniques from randomized numerical linear algebra to study the attention problem. 

2. The theoretical results do not rely on any restrictive assumptions and are applicable to a wide variety of functions, including all $f(x) = |x|^p$. The algorithm can be computed in streaming and parallel settings.

3. The experimental results support the theoretical findings by considering a pre-trained ViT model. Moreover, the model quality has more than 90 percent of the accuracy of the full softmax attention when only selecting the top 32 keys.

### Weaknesses
1. This paper does not include an overview of the recent works, which might make it hard for readers outside this field to understand the importance of the contributions. Works like [ZGD+20] develop the sparse attention, reducing the computation complexity to $O(n)$, and other works like [SYZ23, GSWY23, ZHDK23] are more related to this work: applying the numerical linear algebra techniques, including tensor trick, preconditioner, and sketching to reduce the computational complexity.

2. The experiment only focuses on the pre-trained ViT model. This paper does not study any other language models. Therefore, it is hard to see whether or not the framework developed in this paper can be generalized to more language models.

[ZGD+20] Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham et al. "Big bird: Transformers for longer sequences." NeurIPS'20.

[SYZ23] Zhao Song, Junze Yin, and Lichen Zhang. "Solving attention kernel regression problem via pre-conditioner." AISTATS'24.

[GSWY23] Yeqi Gao, Zhao Song, Weixin Wang, and Junze Yin. "A fast optimization view: Reformulating single layer attention in llm based on tensor and svm trick, and solving it in matrix multiplication time." Preprint'23.

[ZHDK23] Amir Zandieh, Insu Han, Majid Daliri, and Amin Karbasi. "Kdeformer: Accelerating transformers via kernel density estimation." ICML'23.

### Questions
1. $\epsilon$ is used to determine the large attention scores. How can we decide the value of $\epsilon$?

### Soundness
4

### Presentation
4

### Contribution
3
