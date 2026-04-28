# PolySketchFormer: Fast Transformers via Sketches for Polynomial Kernels

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 5, 8

## Abstract
The quadratic complexity of attention in transformer architectures remains a big bottleneck in scaling up large foundation models for long context. In fact, recent theoretical results show the hardness of approximating the output of softmax attention mechanism in sub-quadratic time assuming Strong Exponential Time Hypothesis. In this paper, we  show how to break this theoretical barrier by replacing softmax with a polynomial function and polynomial sketching. In particular we show that sketches for Polynomial Kernel from the randomized numerical linear algebra literature can be used to approximate the polynomial attention  which leads to a significantly faster attention mechanism without assuming any sparse structure for the attention matrix that has been done in many previous works. 

  In addition, we propose an efficient block-based algorithm that lets us apply the causal mask to the attention matrix without explicitly realizing the $n \times n$ attention matrix and compute the output of the polynomial attention mechanism in time linear in the context length. The block-based algorithm gives significant speedups over the *cumulative sum* algorithm used by Performer to apply the causal mask to the attention matrix. These observations help us design *PolySketchFormer*, a practical linear-time transformer architecture for language modeling with provable guarantees.

  We validate our design empirically by training language models with long context lengths. We first show that the eval perplexities of our models are comparable to that of models trained with softmax attention. We then show that for large context lengths our training times are significantly faster than FlashAttention.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach to attention computation in transformer networks that scales linearly rather than quadratically in the context length, and thus allows scaling to much larger context lengths.

The key idea is to replace the softmax non-linearity typically used in attention with a very simple polynomial non-linearity — in fact just f(x) = x^4. With this non-linearity, one can compute the attention matrix using a simple tensoring approach in O(n h^5) time, where n is the context length and h is the dimension of the token embeddings. This is linear in n, but the large dependence on h is bad in practice. To avoid this, the paper further sketches the tensored up query/key matrices using known techniques for sketching polynomial kernel matrices — in particular TensorSketch. This maintains linear in n scaling but improves the dependence on h to also linear, at the cost of some approximation and a quadratic dependence on a sketch size parameter that controls accuracy. 

The paper also introduces a blocked variant of an existing ‘cumulative sum’ algorithm for applying a lower triangular to the approximate attention matrix. This blocked variant trades off parallelizability (i.e. efficiency on GPUS) for memory usage/runtime.

Overall, the idea of this paper is nice and simple, and it is well explained. None of the ideas are particularly novel — TensorSketch for example has been used frequently in the past to approximate matrices under polynomial/entrywise non-linearitiess, like in the attention setting. The blocked cumulative sum algorithm is a simple optimization of an existing approach. 

The finding that replacing an exponential non-linearity with a much easier to compute/approximate polynomial is nice. Although I would have liked to see this discussed/analyzed more. Intuitively, f(x) = x^4 behaves very differently from f(x) = exp(x) since as x -> -infty, x^4 -> infty while exp(x) -> 0. That is, tokens with very different (opposite) embeddings in this new approach have large attention matrix values, rather than small ones. Why does this change not effect performance/cause issues with the new approach?

Given that the theoretical/algorithmic contributions are somewhat limited, I would have liked to see more of an empirical evaluation. This is beyond my area of expertise, however, the empirical evaluation seems to focus only on perplexity scores, which are a very limited metric, and as discussed in the paper itself, cannot necessarily distinguish methods that effectively implement long range attention from those that don’t. This seems to be a major draw back, especially given that the goal of the paper is to scale transformers to have longer context windows, and thus presumably longer range attention. From what I can tell there isn’t really any evidence in the empirical evaluation that the paper achieves/makes progress towards this goal.

The paper is fairly well written but has lots of typos and grammatical errors. It would need significant proofing before final publication.

### Strengths
See full review.

### Weaknesses
This paper proposes a new approach to attention computation in transformer networks that scales linearly rather than quadratically in the context length, and thus allows scaling to much larger context lengths.

The key idea is to replace the softmax non-linearity typically used in attention with a very simple polynomial non-linearity — in fact just f(x) = x^4. With this non-linearity, one can compute the attention matrix using a simple tensoring approach in O(n h^5) time, where n is the context length and h is the dimension of the token embeddings. This is linear in n, but the large dependence on h is bad in practice. To avoid this, the paper further sketches the tensored up query/key matrices using known techniques for sketching polynomial kernel matrices — in particular TensorSketch. This maintains linear in n scaling but improves the dependence on h to also linear, at the cost of some approximation and a quadratic dependence on a sketch size parameter that controls accuracy. 

The paper also introduces a blocked variant of an existing ‘cumulative sum’ algorithm for applying a lower triangular to the approximate attention matrix. This blocked variant trades off parallelizability (i.e. efficiency on GPUS) for memory usage/runtime.

Overall, the idea of this paper is nice and simple, and it is well explained. None of the ideas are particularly novel — TensorSketch for example has been used frequently in the past to approximate matrices under polynomial/entrywise non-linearitiess, like in the attention setting. The blocked cumulative sum algorithm is a simple optimization of an existing approach. 

The finding that replacing an exponential non-linearity with a much easier to compute/approximate polynomial is nice. Although I would have liked to see this discussed/analyzed more. Intuitively, f(x) = x^4 behaves very differently from f(x) = exp(x) since as x -> -infty, x^4 -> infty while exp(x) -> 0. That is, tokens with very different (opposite) embeddings in this new approach have large attention matrix values, rather than small ones. Why does this change not effect performance/cause issues with the new approach?

Given that the theoretical/algorithmic contributions are somewhat limited, I would have liked to see more of an empirical evaluation. This is beyond my area of expertise, however, the empirical evaluation seems to focus only on perplexity scores, which are a very limited metric, and as discussed in the paper itself, cannot necessarily distinguish methods that effectively implement long range attention from those that don’t. This seems to be a major draw back, especially given that the goal of the paper is to scale transformers to have longer context windows, and thus presumably longer range attention. From what I can tell there isn’t really any evidence in the empirical evaluation that the paper achieves/makes progress towards this goal.

The paper is fairly well written but has lots of typos and grammatical errors. It would need significant proofing before final publication.

### soundness:
 4 excellent

### presentation:
 3 good

### contribution:
 2 fair

### strengths:
 See full review.

### weaknesses:
 See full review.

### questions:
 I have asked various questions/made specific comments below. I starred ones that are more important/would be good to see addressed in the author response period.

Questions/Comments:
- **In Fig. 1 I don’t understand how the vanilla softmax attention runs out of memory at context length of 4k. Shouldn’t the memory footprint just be roughly (4k)^2 doubles, or roughly 32 MBs? This is extremely small. I can compute a 4k x 4k attention matrix in a few seconds on my laptop.
- “because of an RNN-style sequential dependence of linear transformers which essentially renders the linear attention implementation to be memory-bandwidth bound” — I don’t understand what this means. Sequential dependence of what on what? Does this not depends on the algorithm used?
- The work of Han, Avron, Shin on approximating entrywise transformed lower rank matrices with tensor sketch seems very related but is not cited. See: https://proceedings.mlr.press/v119/han20a.html
- The parameter m in Theorem 2.2 (in the runtime) seems to be undefined. Is this meant to be r?
- **I didn’t follow the explanation at the bottom of page 5. If we break out exactly what this is doing it is computing:
[AD_1 H P_1 D_2 H P_2 * AD_3 H P_3 D_4 H P_4]
where D_1,P_1 and D_3,P_3 are the random matrices chosen for SRHT_1(A) and SRHT_2(A) respectively. And D_2,P_2 and D_4,P_4 are chosen by TensorSRHT_1. This doesn’t look right to me. What is the purpose of applying the ‘double sketch’ D_1 H P_1 D_2 H P_2. If one looks at the Ahl et al. paper (https://arxiv.org/pdf/1909.01410.pdf), the base sketch is applied already to the first level of tensor products, not to the original input. I.e. the base sketch sketches from h^2 to r dimensions. Not h to r dimensions. In particular, Def 15 of that paper defines TensorSHRT which matches Def 2.4 of this paper, and should be directly used for sketching A^{tensor 2}. 
- In Theorem 2.5, the relevant JL moment properties are never defined or explained.
- I think as stated Theorem 3.1 is meaningless, as it doesn’t mention the memory tradeoff or even the algorithm used. So the theorem follows vacuously from noting that O(nr(b+d) >= O(nrd) and by Choromanski et al. we can comput mask(AB^T) C in O(nrb) time.
- ** In the end the tensor sketch is only actually applied for a degree 2 polynomial. Is it really the best option there? Why not explicitly compute Q^{tensor 2}, K^{tensor 2}. SVD them to get lower dimensional approximations tilde Q and tilde K and then compute tilde Q^{tensor 2} and tilde K^{tensor 2}. You are already explicitly tensoring up once in your last step anyways. 
- Related to the above, what is the final runtime complexity of your algorithm? The naive tensoring method is O(n h^5). Your’s is what in terms of n, h, and the sketch size r? Roughly O(n(h+r^2))?

### Questions
I have asked various questions/made specific comments below. I starred ones that are more important/would be good to see addressed in the author response period.

Questions/Comments:
- **In Fig. 1 I don’t understand how the vanilla softmax attention runs out of memory at context length of 4k. Shouldn’t the memory footprint just be roughly (4k)^2 doubles, or roughly 32 MBs? This is extremely small. I can compute a 4k x 4k attention matrix in a few seconds on my laptop.
- “because of an RNN-style sequential dependence of linear transformers which essentially renders the linear attention implementation to be memory-bandwidth bound” — I don’t understand what this means. Sequential dependence of what on what? Does this not depends on the algorithm used?
- The work of Han, Avron, Shin on approximating entrywise transformed lower rank matrices with tensor sketch seems very related but is not cited. See: https://proceedings.mlr.press/v119/han20a.html
- The parameter m in Theorem 2.2 (in the runtime) seems to be undefined. Is this meant to be r?
- **I didn’t follow the explanation at the bottom of page 5. If we break out exactly what this is doing it is computing:
[AD_1 H P_1 D_2 H P_2 * AD_3 H P_3 D_4 H P_4]
where D_1,P_1 and D_3,P_3 are the random matrices chosen for SRHT_1(A) and SRHT_2(A) respectively. And D_2,P_2 and D_4,P_4 are chosen by TensorSRHT_1. This doesn’t look right to me. What is the purpose of applying the ‘double sketch’ D_1 H P_1 D_2 H P_2. If one looks at the Ahl et al. paper (https://arxiv.org/pdf/1909.01410.pdf), the base sketch is applied already to the first level of tensor products, not to the original input. I.e. the base sketch sketches from h^2 to r dimensions. Not h to r dimensions. In particular, Def 15 of that paper defines TensorSHRT which matches Def 2.4 of this paper, and should be directly used for sketching A^{tensor 2}. 
- In Theorem 2.5, the relevant JL moment properties are never defined or explained.
- I think as stated Theorem 3.1 is meaningless, as it doesn’t mention the memory tradeoff or even the algorithm used. So the theorem follows vacuously from noting that O(nr(b+d) >= O(nrd) and by Choromanski et al. we can comput mask(AB^T) C in O(nrb) time.
- ** In the end the tensor sketch is only actually applied for a degree 2 polynomial. Is it really the best option there? Why not explicitly compute Q^{tensor 2}, K^{tensor 2}. SVD them to get lower dimensional approximations tilde Q and tilde K and then compute tilde Q^{tensor 2} and tilde K^{tensor 2}. You are already explicitly tensoring up once in your last step anyways. 
- Related to the above, what is the final runtime complexity of your algorithm? The naive tensoring method is O(n h^5). Your’s is what in terms of n, h, and the sketch size r? Roughly O(n(h+r^2))?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new architecture that attempts to be close to the original attention, but without the quadratic computational cost. The first observation relies on the cost of computing the attention matrix and performing the softmax on this matrix. The idea in this work is to replace the softmax with a polynomial of degree-k (where k is even). The second observation lies on approximating the polynomial computation with sketches. Then, to preserve the nonegativity, a squaring step after the computation of the first sketch is used. Lastly, various small architecture-optimization steps are completed to ensure that the implementation is fast, including the step of fast lower triangular computation of the causal attention matrix or the block-based variant inspired by FlashAttention.

### Strengths
The quadratic cost of the transformer is indeed a major bottleneck in the literature recently, and this is further evident in the context lengths used in practical models. In that sense, reducing this cost to linear is a relevant topic in the literature. In addition, I have not noticed any similar approach in the literature so far using the sketches to approximate the polynomial that approximates the attention matrix in turn.

### Weaknesses
- Even though the paper proposes a way to avoid the nonnegativity, another property of the softmax is that it upper-bounds a value to at most 1, while it’s less clear how the proposed model deals with this or whether this is even an issue. 

- The paper mentions in the introduction that in practice most sota papers use the vanilla transformer in practice (i.e. large-scale experiments), but then there are no sota papers and large-scale experiments conducted in the experimental section. In addition, there are few to no ablations on the choices made in this work. 

- There are some related works in the direction of polynomial and efficient attention that might be worth comparing with: “Hydra Attention: Efficient Attention with Many Heads” (10/2022) and “Linear Complexity Self-Attention with 3rd Order Polynomials” (3/2023).

- What is the performance of the proposed model in actual NLP-related tasks, such as translation etc? The paper mentions that this method is not only applicable on generation, but also conditional generation, but I do not see any related results here.



### Questions
- What is the perplexity of the model and why is this a good metric?

- Why is a degree 4 polynomial used?

- Why are all experiments up until the 16k context window only? What’s the core limitation for extending it further? 

- Why is a single-degree k polynomial (even more that it is restricted to be even) approximating the softmax? Are there any guarantees or insights on that?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new transformer architecture called PolySketchFormer that uses polynomial sketching techniques to approximate the softmax attention mechanism efficiently.  To be concrete, the authors approximate the dot products among tensorized queries and keys efficiently by first lowering their dimensions through randomized sketching matrices. Then, the authors ensure non-negativity of the approximated attention scores by a  "tensoring trick". Additionally, the authors propose a block-based algorithm for multiplication with lower-triangular causal masks, which is faster, though using more operations, than Performer (Choromanski et al., 2020).  Experiments are conducted to verify PolySketchFormer's effectiveness, speed, and ability to handle long-range context.

### Strengths
- S1. Using randomized sketch to reduce the  $O(nh^{p+1})$  complexity is insightful.
- S2. The proposed procedure for computing $\mathrm{It}(\tilde{Q}\tilde{K}^{T})V$ is contributive, especially to other other linear Transformers as well.
- S3. PolySketchFormer's effectiveness, speed, and ability to handle long-range context is verified by experiments.

### Weaknesses
 - W1. According to Definition 2.4,  PolySketchFormer can only express/approximate the polynomial $f(s)=s^p$ ($s:= \langle q,k \rangle$), where $p$ is **a power of 2**. This severely limits the flexibility of the attention mechanism, as it cannot directly approximate the softmax function, which is a more general and widely used attention mechanism. The restriction to powers of 2 means that the model cannot leverage intermediate polynomial degrees, potentially hindering its ability to capture complex relationships between queries and keys. This limitation should be more thoroughly discussed in the paper.
- W2. The input and output of the SRHT and TensorSRHT are not clearly illustrated, making it difficult to understand how these transformations affect the data. Specifically, the dimensions of the input and output tensors at each stage of the sketching process should be explicitly stated. A more detailed explanation with concrete examples would greatly improve clarity. It is unclear how the tensorization of the sketching matrices interacts with the original query and key dimensions.
- W3. A typo: On Page 3, the second to last line, it should be $q\in \mathbb{R}^h$, right?
- W4. In experiments, PolySketchFormer is compared only with Performer and FlashAttention. While these are relevant baselines, the evaluation would be more comprehensive if other efficient Transformer architectures, such as Linformer or Nyströmformer, were also included. This would provide a better understanding of PolySketchFormer's relative performance and limitations.

### Questions
- Q1. Please check W1. 
- Q2. In Table 1, what is exactly the Softmax model? Is it FlashAttention?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the issue of quadratic complexity for transformers. The authors propose the use of polynomial kernels and sketching to replace the softmax function to achieve linear complexity. For the theoretical part, they show that there are guarantees on the approximation error of the sketch. For the empirical part, they show the speed of the proposed method is faster than the compared methods for longer contexts.

### Strengths
1. The proposed method seems to be simple and reasonable.
2. The authors provide guarantees on the approximation of sketching.

### Weaknesses
1. The empirical result is weak. It seems that the proposed method with 8k, 16k context is slower than the other method with 2k, 4k context and has higher perplexity. Doesn’t this mean the proposed method is not better?
2. Need to elaborate more on the data leak of Performer, so the reviewers can verify the statement.
3. The authors need to elaborate on why some newer methods that perform better on the long range arena does not need to be compared. For example, ChordMixer or LongFormer.
4. The speedup does not seem to be large. Thus, it feels important to have more experiments to verify the perplexity/perform drop is generally within the acceptable range.

### Questions
1. Can you elaborate more on the data leak of Performer? Is this your discovery or it has been pointed out by others? It is better to give the reviewers some ways to validate this statement. Some reference/link to the issue will help.
2. Is rematerialization also used in the other methods? It is a bit unclear from the writing.
3. Can you briefly explain why Performer is slower than the softmax baseline in the experiments? This does not seem to be the case in the original paper. Is this because of bad implementation?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Transformers have an inherent quadratic complexity in context length due to self-attention computation with softmax function. Softmax self-attention can be approximated using polynomial functions. This method has complexity linear in context length, but the vanilla application of polynomial approximation creates an exponential dependency on the degree $p$ of the polynomial.
This paper introduces a sketch-based approximation for polynomial kernel self-attention using the *oblivious sketching* methods for higher-order polynomial kernels described in *Ahle et al. (2020)*. This method can bypass the exponential dependency on degree $p$ while the approximation error of the polynomial kernel self-attention matrix is inversely correlated with sketch size. They validate their theoretical guarantees by comparing the perplexity metric of softmax, polynomial kernel, and the new algorithm.
Additionally, the authors provide a block-based algorithm for decoder-only transformer models. This circumvents the sequential nature of the cumulative-sum algorithm used in prior approaches such as *Performer*. 
Experiments show that combining these two methods shows decent speed-up gains in runtime compared to standard softmax self-attention, polynomial kernel self-attention as well as fast algorithms for self-attention such as Performer and Flash Attention.

### Strengths
**Originality**

The clever combination of oblivious sketching for polynomial kernels with polynomial kernel self-attention although both of these individual ideas have been known for quite a while shows the originality of this paper.

**Quality**

Solid theoretical results on approximation guarantees for polynomial kernel self-attention and the experiments demonstrate the gains obtained by algorithms.

**Significance**

Quadratic complexity in self-attention is a significant barrier in scaling transformer-based models in low-resource settings. Softmax self-attention has shown superior empirical accuracy over other types of self-attention, but approximating softmax self-attention is known to be hard in subquadratic time in context length. Polysketch self-attention performs comparably to softmax while using truly subquadratic time and I believe this is a significant contribution.

### Weaknesses
Presentation and clarity of polysketch self-attention can be improved.

Typically in matrix sketching, we take the product of $A^{\otimes p} \in \mathbb{R}^{n \times h^p}$ and $S \in \mathbb{R}^{h^p \times r}$ explicitly. However, the proposed algorithm does not perform this explicit multiplication and avoids the exponential runtime dependency on $p$.  I believe the algorithm described in *Ahle et al. (2020)* uses the Fast Fourier Transform to compute $A^{\otimes p} S$ efficiently with the tree-based algorithm. However, this paper does not have any indication of how this product is computed. I believe it is important to outline this process for the completeness of this paper. 
I am surprised that the authors do not emphasize this fact enough, since it is a significant component that enables the removal of exponential dependency on degree $p$.

Typos:
1. On page 12, proof of theorem 2.5, Definition A.1. "$x \in \mathbb{R}^m$ with $\lvert\lvert x \rvert\rvert_2$" $\rightarrow$ "$x \in \mathbb{R}^m$ with $\lvert\lvert x \rvert\rvert_2 = 1$"
2. On page 13, the paragraph after the proof of theorem 3.1 does not make sense. I believe it belongs earlier in the paper or is redundant.

### Questions
**Questions**

1. In theorem 2.2, how large can the constant $C$ be? If $C$ is large, $r$ may become too large for it to be practical.
2. In theorem 2.2, what is $m$?
3. Perhaps I am missing something but on page 12, in the proof of theorem 2.5, does the JL-moment property of $S$ imply that $\langle S^Tc_i, S^Td_j \rangle.\langle c_i, d_j \rangle \le \langle c_i, d_j \rangle^2$ ? I do not see how $(\langle S^Tc_i, S^Td_j \rangle - \langle c_i, d_j \rangle + 2 \langle c_i, d_j \rangle )^2 (\langle S^Tc_i, S^Td_j \rangle - \langle c_i, d_j \rangle)^2 \le (1+C) (\langle S^Tc_i, S^Td_j \rangle - \langle c_i, d_j \rangle)^4 + 4(1+1/C) \langle c_i, d_j \rangle^2 (\langle S^Tc_i, S^Td_j \rangle - \langle c_i, d_j \rangle)^2$ holds for any $C \ge 1$ otherwise.

**Additional remarks**

Perhaps the following remarks can be candidates for future work.

1. Even though the block-based method is targeted at decoder-only models, I believe the approximate algorithm for polynomial kernel self-attention can be applied in general to any transformer-based architecture. Have the authors explored any other architectures with this approximate self-attention algorithm?
2. In "On The Computational Complexity of Self-Attention [Feyza Duman Keles, Pruthuvi Mahesakya Wijewardena, Chinmay Hegde]" paper, a polynomial approximation to softmax self-attention is derived using the finite Taylor series which includes lower order terms as well. Technically, this should be able to get arbitrarily close to softmax self-attention as the order $p$ is increased. If we use Polysketch self-attention to approximate each term of the Taylor series approximation, and thereby approximate softmax self-attention, I am curious what would be the closest approximation one can get while still maintaining subquadratic complexity in context length and subexponential complexity in degree $p$.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
