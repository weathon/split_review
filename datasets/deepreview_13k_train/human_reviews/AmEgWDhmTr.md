# From Sparse Dependence to Sparse Attention: Unveiling How Chain-of-Thought Enhances Transformer Sample Efficiency

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Chain-of-thought (CoT)  significantly enhances the reasoning performance of large language models (LLM). While current theoretical studies often attribute this improvement to increased expressiveness and computational capacity, we argue that expressiveness is not the primary limitation in the LLM regime, as current large models will fail on simple tasks. Using a parity-learning setup, we demonstrate that CoT can substantially improve sample efficiency even when the representation power is sufficient. Specifically, with CoT, a transformer can learn the function within polynomial samples, whereas without CoT, the required sample size is exponential. Additionally, we show that CoT simplifies the learning process by introducing sparse sequential dependencies among input tokens, and leads to a sparse and interpretable attention. We validate our theoretical analysis with both synthetic and real-world experiments, confirming that sparsity in attention layers is a key factor of the improvement induced by CoT.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies how Transformers may or may not solve k-sparse parity problems. Without chain of thought, the authors provide a lower bound for one-pass algorithms with bounded memory, showing that exponential in k samples are needed, even though small transformers exist that solve the task. Then, the authors show positive results for learning with a CoT prompt using minibatch SGD, where order n samples are sufficient (where n is dimension, and up to log factors). The theory is complemented with extensive numerical experiments.

### Strengths
The results are interesting and novel, tackling the important question of training dynamics of transformers and the role of chain-of-thought prompting.

### Weaknesses
A couple of minor weaknesses (see also questions below):

* the lower bound is claimed to be about sample complexity, though it feels more like a computational lower bound. Perhaps this should be clarified.

* the initialization seems a bit non-standard, particularly W_{r,1:d}. Some more justification would be helpful.



### Questions
* could you comment on how the lower bound compares to other known computational lower bounds for parities, e.g. based on statistical queries, or in the spirit of Abbe-Sandon?

* could you clarify why the initialization on W_{r,1:d} in Assumption 1 is helpful, and whether it is needed? Is this what leads to "stronger correlation with the embedding ..." (L273) ? The phase 1 proof sketch would benefit from more clarity.

* note that O(n) learning of parities with fully-connected networks (thus with no sparse attention) is also possible when the staircase property holds (e.g. Abbe et al 2023, 2024). Is there a link between the CoT structure you consider and the staircase property?

* the proposed CoT prompt seems one of many possible choices, e.g. one could also have a length-n sequence that incrementally computes sparse parities up to each number. In a way, your way of encoding the problem almost requires that the user knows the secret set of locations, which seems pretty close to just giving the set as an input, which is a lot of information... Could you comment on any other possible choices, and why you chose this one?

minor typos: L247, "for any i" should be for any i, j and b vector?

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
This work aims to understand how Chain-of-Thought (CoT) improves sample complexity for transformers. In a setup of parity learning, it provides theoretical results of exponential sample complexity without CoT while the complexity of CoT is linear. Meanwhile, the training procedure with CoT induces sparse sequential patterns in attention, the rising of which is then empirically observed to be strongly correlated with perfect predicting in both settings of with and without CoT. The sparse attention patterns are also observed in finetuning on real-world data with CoT.

### Strengths
1. The motivation is good: understanding CoT is a significant direction to understand pre-training and finetuning LLMs, especially for reasoning tasks.
2. The theoretical setup is natural: parity learning is a popular setup for understanding neural networks and gradient methods, where some previous works were focusing on sampling complexity for staircase property in parity learning. Meanwhile, the sparse property of parity learning naturally brings the sparsity in learned attention.
3. Both theory and experiments clearly provide a exponential gap between the sample complexity with and without CoT.
4. The observation of sparsity in Qwen models on GSM8K is interesting, especially the math model finetuned with CoT.

### Weaknesses
1. In definition 2, the augmented sequence is with any permutation $S$. Is this permutation random or fixed during training? If it is random, it seems impossible to achieve perfect accuracy for next-token prediction in Theorem 3, and the monotone pattern in Figure 3(b) might also be questionable. If it is fixed, some clarification is helpful.
2. It would be better to include discussion regarding a recent related work [1].


### Questions
Please see the above concerns.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper theoretically studies the training dynamics of one-layer Transformers learning sparse parity problems using zero-shot CoT. The authors especially compare the sample complexity with or without CoT, which is interesting and verified by the experiments. The experiments and discussion on multi-pass training are also interesting.

### Strengths
The paper is well-written and easy to follow.
The experiments are overall solid to support the theory.
It is novel to study parity problems using Transformers. The theoretical analysis is novel. The comparison between CoT and without CoT is quite impressive and significant in future research.

### Weaknesses
There are two major issues. 
1. The theoretical proof seems incomplete. I failed to find proof of Theorem 3. I can only find a proof sketch and some supportive lemmas. As a theoretical paper, this harms the soundness. The provided proof sketch lacks sufficient detail to verify the claim, particularly regarding the convergence rate and the specific conditions under which the three-phase training process guarantees the desired outcome. The lemmas, while supportive, do not fully bridge the gap to a complete proof of the theorem. The absence of a rigorous, step-by-step derivation makes it difficult to assess the validity of the theoretical result.
2. If my understanding is correct, during the training and evaluation, the location to compute the parity in every sequence is the same, e.g., we always use the location 1,2, and 5 to compute the parity. I think it is a stronger and more reasonable result to make the location not fixed. For example, let $k=3$, then I can learn the sparse parity with any three locations. Especially during the testing, I can compute parity on a certain tuple of three locations that never appear during the training. This can make your work a stronger CoT inference rather than more of a training analysis. The current setup, with fixed locations, limits the generalizability of the findings and does not fully capture the potential of CoT for flexible reasoning over different input structures. The analysis would be more compelling if it could demonstrate learning a general parity function applicable to arbitrary location sets.

### Questions
1. Can your analysis be extended to few-shot CoT?
2. In lemma 22, line 1834, is $W^{(3)}$ in the third phase of the training? If so, then there is only one step in each phase? Does it imply that the training process is too fast or simple? This seems unrealistic.
3. This work seems to remove positional encoding. Why? If I add positional encoding, can the sample complexity be reduced in both cases, i.e., with or without CoT?

### Soundness
2

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
This paper presents a theory to explain why Chain-of-Thought (CoT) helps Transformer models to learn complex tasks. The paper first shows that a Transformer architecture with one layer and one head is expressive enough to represent the parity learning task. However, exponentially many samples are needed to solve this task with a subquadratic memory. Then, the authors demonstrate that a reformulation of the task with CoT can be solved with only a linear number of samples.

### Strengths
This paper studies the learning dynamics of a Transformer layer (with non-linear attention and MLP sublayers), which is crucial in order to understand better the properties of this architecture, and a technically difficult problem due to the highly non-linear parameterization of the architecture. The analysis of CoT is original and compelling, in that it gives a provable mechanism by which CoT simplifies the learning problem.

### Weaknesses
While the ideas in the paper are nice, the paper would highly benefit from polishing to improve the clarity and presentation of the message. In particular, the proofs are written in a telegraphic style, which makes it particularly difficult to check correctness. It also makes it hard to get a sense of how general the approach is, where the specific initialization scheme comes into play, etc. I give below more specific examples of things that confused me and would benefit from cleaning up.

Besides, I am not convinced by the real-world experiments. The difference in terms of entropy of the attention layers does not seem very significant, so in my opinion it is difficult to reach any strong conclusion from the figures.

All in all, the rating reflects the fact that the ideas are interesting, but I believe polishing the paper would make it much better.

Examples of confusing statements in the main text and the beginning of the proofs (the only point for which I would like an answer during the rebuttal is the first one, others are less important):
- in Theorem 2, the condition on $d$, $m$, $n$ and $k$ is not satisfied for the dimensions taken in the proof of Theorem 1, so it is hard to relate both results.
- line 296: “which only applies to one-pass training”, but Theorem 2 applies to multipass training?
- line 831: why $m>100$?
- line 841: I agree that the results should follow from random matrix theory, but you should give a proper statement and proof/reference. The result depends on the relative value of $d$ and $k$, and the current statement $d = \tilde{\Omega}(k)$ is too hand-wavy to conclude that the specific numerical values given in the Lemma are verified.
- line 844: why $\delta/4$?
- lines 896: why $8$ instead of $10$?
- line 901: the $\mathcal{O}(1/n^7)$ needs to be explained.
- line 913: “by choosing $a_r$ and $b_r$ iteratively”: this needs to be explained.
- line 916: “the parameters can be encoded in $\mathcal{O}(\log n)$ precision”. Why?
- line 960: this is not a valid proof of the Lemma, the derivation of the inequalities is non-trivial from the Assumption.

Minor remarks (no impact on score):
- line 46: the specific example of the number of letters in a word is not very relevant, because perhaps this is precisely an example of a task which may not be representable by a Transformer model due to the tokenisation mechanism.
- line 77: $k$ is not introduced yet.
- line 191: the bounds of the sum should depend whether it is a CoT or non-CoT task.
- line 230: it should be $W_{r,1:m}$ instead of $W_{r,1:d}$.

### Questions
In Definition 3, is there any advantage to taking random embeddings vectors, instead of fixed orthogonal vectors? From a modelling perspective, I don’t think random embeddings add much, and taking them fixed would greatly simplify the proofs by cancelling many terms, which you currently have to bound using random matrix theory and concentration inequalities. This contributes to making the proofs difficult to follow.

### Soundness
3

### Presentation
3

### Contribution
4
