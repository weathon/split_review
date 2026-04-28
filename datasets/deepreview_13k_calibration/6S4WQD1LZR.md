# Transformers are Universal In-context Learners

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Transformers are deep architectures that define ``in-context mappings'' which enable predicting new tokens based on a given set of tokens (such as a prompt in NLP applications or a set of patches for a vision transformer). In this work, we study in particular the ability of these architectures to handle an arbitrarily large number of context tokens. To mathematically, uniformly address their expressivity, we consider the case that the mappings are conditioned on a context represented by a probability distribution of tokens which becomes discrete for a finite number of these. The relevant notion of smoothness then corresponds to continuity in terms of the Wasserstein distance between these contexts. We demonstrate that deep transformers are universal and can approximate continuous in-context mappings to arbitrary precision, uniformly over compact token domains. A key aspect of our results, compared to existing findings, is that for a fixed precision, a single transformer can operate on an arbitrary (even infinite) number of tokens. Additionally, it operates with a fixed embedding dimension of tokens (this dimension does not increase with precision) and a fixed number of heads (proportional to the dimension). The use of MLPs between multi-head attention layers is also explicitly controlled. We consider both unmasked attentions (as used for the vision transformer) and masked causal attentions (as used for NLP and time series applications). We tackle the causal setting leveraging a space-time lifting to analyze causal attention as a mapping over probability distributions of tokens.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proves that transformers can universally approximate context-dependent mappings, $G(\mathbf{x}; \mu)$. They do this by showing that one-dimensional attention functions are dense in the one-dimensional context-dependent mappings. Separate proofs are provided for masked and unmasked attention.

### Strengths
*Nice prior-work section, succinctly summarizes a very large literature. 

*The "in-context mapping" formulation is nice, not sure if it was used in prior theory but seems to apply to many IC learners like RNNs and SSMs and so on. 

*Feel like many of the techniques used could become useful theoretical constructions themselves (like the Laplace-like transform of Lemma 1)

### Weaknesses
Hard to think of any beyond those already acknowledged by the authors. If I were to reach for one, I feel like the result itself is maybe less interesting than the methods (which are very interesting), since being able to approximate any function often doesn't translate to being able to learn it (e.g. shallow networks, polynomial regression), and so it might be nice to spend some space in the intro or discussion highlighting what if any bearing this has on learning.

### Questions
Only what I mentioned above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper examines Transformer's (unmasked and masked) ability to handle an unlimited number of context tokens. Contexts are modeled as probability distributions of tokens, with smoothness defined by continuity in Wasserstein distance. This paper shows that transformers can universally approximate continuous in-context mappings with fixed embedding dimensions and a constant number of heads.

### Strengths
I believe this paper provides a solid theoretical foundation for how a Transformer can model an infinite number of tokens, which supports the development of long-context language models. I find it especially surprising that a Transformer can handle an infinite number of tokens with a fixed embedding dimension.

### Weaknesses
I'm not sure if people actually use the unmasked variant discussed in this paper. For instance, bidirectional models like BERT and ViT must apply positional embeddings to their input tokens, meaning Eq. (2) isn’t typically used in practice. Therefore, I’d say the main contribution of this paper lies in its analysis of Eq. (3), which introduces additional regularity constraints on the token distribution. However, even within the analysis of Eq. (3), the practical implications of the smoothness condition defined by the Wasserstein distance are not entirely clear. While the theoretical framework is elegant, it remains to be seen how this smoothness constraint translates into tangible benefits for real-world language models, especially when considering the discrete nature of token embeddings and the complexities of training dynamics. Furthermore, the paper does not explore the limitations of the fixed embedding dimension in practical scenarios. While the theory suggests it can handle an infinite number of tokens, the finite capacity of the embedding space might lead to information bottlenecks or interference when dealing with extremely long contexts.

### Questions
I don't have any specific question.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the ability of transformers to approximate arbitrary in-context mappings, namely, their ability to transform an input set of token embeddings into an output set of embeddings arbitrarily close to a given target set, where each input token is transformed based on the context of the other input tokens. The input set is not limited to be a discrete finite set, but can be infinite or even continuous: in general it can be represented by a probability measure over the embedding space. A single transformer is able to obtain a given approximation level (aka precision), independently of the cardinality of the input set, which can even be infinite. The authors consider two settings: unmasked (aka non-causal, often used in vision applications) and masked (aka causal, often used in NLP), the masked setting requiring an extension of the approach used in the unmasked setting.

### Strengths
The paper explores in depth an interesting theoretical question about the in-context mapping abilities of the transformer architecture, namely its approximation abilities in presence of a context of arbitrary (even continuously infinite) cardinality.

The depth and rigour of the mathematical derivations appear (from the best judgment of a non-specialist, see also below) to be of very high quality.

### Weaknesses
The paper is extremely technical, and would require a considerable amount of time and effort, even by a mathematically inclined reader, to be fully understood.

The paper, as it stands, appears to be oriented towards a small number of readers, already familiar with the technical literature relating to measure-theoretic views of the approximation properties of transformers. Its appeal could be made broader by: (1) motivating the approach by potential (even non-immediate) applications and (2) by providing graphical illustrations of some of the underlying mathematical concepts, to help intuition (the current version of the paper does not provide a single illustration).

As the authors acknowledge, their results "are not quantitative", meaning (if I understand correctly), that a number of important parameters of the transformer architecture, such as the number of layers, are not bounded in terms of the approximation precision $\epsilon$. As they admit, this is a serious obstacle relative to applications. However, on the positive side, their current results provide some welcome clarification of the theoretical landscape.

The title "Transformers are Universal In-Context Learners" could be misleading to many readers, as it may seem to address the well-known question about the "ICL (In-Context Learning)" abilities of transformers, for example, the abilities of *fixed* LLMs, when provided with a "few-shot prompt of examples", to appear to "learn" to reproduce the "intention" expressed by the examples. In the current paper, the goal appears to be of a rather different nature, having to do with *finding* a transformer architecture and its parameters to approximate a given target contextual embedding. It would be useful if the authors could clarify whether they see a connection between their work and the usual notion of ICL.

### Questions
1 (Question). Could you provide one or two concrete examples that would illustrate the potential applicability of the approach? Such examples would improve the accessibility of the paper to a wider audience.

2 (Question). It is not fully clear to me why putting a probability measure over the input tokens is a natural move in the context of transformers. For instance, when considering a standard input of $n$ tokens, the usual representation is in terms of a set of cardinality $n$, and I am not quite sure why putting different weights over these tokens is an appropriate representation for modeling in-context mappings.

3 (Remark). On line 289, you say "Since our results are not quantitative, this is not a strong restriction." I had some difficulty making sense of this statement, starting with the unclarity of the term "not quantitative", which I finally understood to mean that you do not state bounds relative to $\epsilon$, e.g. concerning the number of layers $L$ (which could be mentioned along with the number of MLP parameters).

### Soundness
4

### Presentation
2

### Contribution
2
