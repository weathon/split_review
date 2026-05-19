# Are Transformers with One Layer Self-Attention Using Low-Rank Weight Matrices Universal Approximators?

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Existing analyses of the expressive capacity of Transformer models have required excessively deep layers for data memorization, leading to a discrepancy with the Transformers actually used in practice. 
This is primarily due to the interpretation of the softmax function as an approximation of the hardmax function.
By clarifying the connection between the softmax function and the Boltzmann operator, we prove that a single layer of self-attention with low-rank weight matrices possesses the capability to perfectly capture the context of an entire input sequence.
As a consequence, we show that one-layer and single-head Transformers have a memorization capacity for finite samples, and that Transformers consisting of one self-attention layer with two feed-forward neural networks are universal approximators for continuous permutation equivariant functions on a compact domain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proves a new approximation results for Transformers with a single layer and attention head and dim-1 head size. The key result is that under suitable conditions on the input sequences, there exists a self-attention layer with softmax function and the settings as above such that the output tokens are bounded and separated from each other by a given distance. This allows a feedforward layer to be trained on top of it and associate to each output token a given label due to the memorization capacity of FFN layers. Hence, two theorems regarding the memorization capacity of such Transformers are proven. Further, exploiting this result, a novel universality result is proved for two-layer and single-head Transformers for permutation equivariant functions.

### Strengths
Very interesting paper! The discussion is surprisingly readable, although I had some issues with interpreting some keywords which are not properly introduced. The results are quite significant, since this is the first paper according to my knowledge that proves approximation results for Transformers with a single layer and attention head. It's interesting that a dimension-1 head can already produce a contextual mapping (bounded and separated output tokens), hence allowing to train an FFN on top to map each token to the required label. Detailed proofs are provided in the appendix, which I did not check completely, but from what I've checked they seem correct.

### Weaknesses
I guess one weakness (which does not deduct from the value of the theoretical results) is that the experiments section simply demonstrates that such a Transformer (single layer single head head dim-1 and tied weights between Q K and V) can already memorize a dataset. Maybe one thing I would be interested in is whether keeping the projection vector fixed and set to the value found using the technique in the proof of Theorem 2 using Lemma 3 can already perform well in practice? 

I also had some issues with a few keywords that were not introduced, for example, in the discussion of Theorem 2 I had no idea what a sequence id was, or how it is used to construct the context id (which if I understood correctly is the output of the attention map?).

Some interesting follow-up questions were left unanswered, for example, how should the size of the FFN layer scale theoretically given the separatedness of the output tokens, or how having multiple attention heads and/or with higher rank can improve the performance?

### Questions
I have a couple questions:
- What is a sequence id, similarly what is a $v$-dependent sequence id?
- Is there any implication regarding the value of $\delta$ in the contextual mapping? In particular, how are the following approximation results affected if $\delta$ decreases?
- How does the memorization capacity depend on the vocabulary size?
- As is mentioned above, can we value of the rank-$1$ projection be computed as implied by the theory and kept at that value in the experiments to see how well that performs?
- Is there any difficulty with extending Prop. 1 using positional encoding to consider functions that are not permutation equivariant?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper critically examines the expressive capacity of Transformer models, specifically addressing the discrepancy between theoretical analyses and practical implementations of Transformers. Existing analyses have often necessitated overly deep layers or numerous attention heads for data memorization, which doesn't align with the Transformers used in real-world applications. This misalignment is largely attributed to the interpretation of the softmax function as an approximation to the hardmax function.

### Strengths
1. The paper is well-organized and clearly written, which is easy to follow.
2. The problem studied in this paper is interesting and valuable.
3. The theoretical work of this paper is sufficient, which improves the value of the paper.

### Weaknesses
This paper delves into the theoretical underpinnings of one-layer Transformers. However, there are areas that could benefit from further exploration:
1. While the study provides insights into one-layer Transformers, it raises the question of whether these findings can be extended to two-layer or even deeper architectures. How scalable is the presented theory?
2. The role of the number of attention heads in determining the memorization capacity remains unclear. If it does have an impact, are there any quantitative metrics provided to elucidate its influence?

### Questions
Please see the Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proves that Transformers with one self-attention layer using low-rank weight matrices, plus two FFNs, are universal appoximators of sequence-to-sequence functions. It makes a connection between the softmax function and the Boltzmann operator, and argues that softmax attention can be more useful for universal approximation than hardmax which is commonly used in existing papers.

### Strengths
- I appreciate the connection between the softmax function and the Boltzmann operator.

- The negative result on hardmax attention looks interesting to me.

### Weaknesses
- **Significance of the result seems limited to me.** Some claims in the paper are weak or wrong.
   - The authors claim that existing results on the expressiveness of Transformers require excessively deep layers or a lot of attention heads. While this paper requires less parameters in the attention layer, its construction requires large FFNs. 
   - Moreover, there is no characterization on the total number of model parameters in the memorization capacity result. It's not surprising at all the Transformers can memorize. It is the upper/lower bound on the required number of parameters for memorization that makes the result interesting.
   - This paper is _not_ the first universal approximation theorem for two-layer Transformers with a self-attention of realistic size, and Section 4.2 _overclaims_ the contribution because of misinterpretation of [1]. The universal approximation result (Theorem 4.1) in [1] _is_ constructive and the construction is even simpler than this paper. The authors also claim that [1] make a particular assumption on the domain of functions. But those assumptions are only for the approximation rate result (Theorem 4.2), which is orthogonal to this paper.

- **Proof issues.** Equation 10 seems buggy. First, I think the authors should specify $\mathbf X^{(i)}\neq \mathbf X^{(j)}$ or $\mathcal V^{(i)}\neq \mathcal V^{(j)}$. Second, if it holds for some $i,j$ and $k,l$, then one can consider the same inequality for $j,i$ and $l,k$ and obtain a contradiction. So I don't see why the condition can be true.

- **Related works.** The year of [2] is marked as 2023 in the paper, but [2] was actually published in ICLR 2020. The authors should correct this to avoid misleading. In addition, I recommend the authors to also discuss [3,4,5].

- **Presentation issues.** There are many typos and minor errors in the paper, to name a few:

   - Page 3, "the Transformer block is represented as a combination of ..." $\to$ "the Transformer block is represented as a composition of ..."
   - Page 5, "this theorem indicates that one-layer Transformer does not have a memorization capacity": Please emphasize one-layer Transformer _with hardmax attention_.
   - Theorem 2, $\mathbf{W}^V$ $\to$ $\mathbf{W}^{(V)}$.
   - The appendix uses eq. $i$ and equation $i$ interchangeably. Please make it consistent.


[1] Approximation theory of transformer networks for sequence modeling.

[2] Are Transformers universal approximators of sequence-to-sequence functions?

[3] $O(n)$ Connections are Expressive Enough: Universal Approximability of Sparse Transformers.

[4] Universal Approximation Under Constraints is Possible with Transformers.

[5] Your Transformer May Not be as Powerful as You Expect.

### Questions
- What are the size of FFNs and the number of model parameters in the construction?

- Can you clarify the discussion on [1] in the paper?

- Can you clarify the proof issue mentioned in **weaknesses**?

[1] Approximation theory of transformer networks for sequence modeling.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
