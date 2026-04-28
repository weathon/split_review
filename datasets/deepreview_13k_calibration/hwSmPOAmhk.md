# Understanding Factual Recall in Transformers via Associative Memories

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Large language models have demonstrated an impressive ability to perform factual recall. Prior work has found that transformers trained on factual recall tasks can store information at a rate proportional to their parameter count. In our work, we show that shallow transformers can use a combination of associative memories to obtain such near optimal storage capacity. We begin by proving that the storage capacities of both linear and MLP associative memories scale linearly with parameter count. We next introduce a synthetic factual recall task, and prove that a transformer with a single layer of self-attention followed by an MLP can obtain 100\% accuracy on the task whenever either the total number of self-attention parameters or MLP parameters scales (up to log factors) linearly with the number of facts. In particular, the transformer can trade off between using the value matrices or the MLP as an associative memory to store the dataset of facts. We complement these expressivity results with an analysis of the gradient flow trajectory of a simplified linear attention model trained on our factual recall task, where we show that the model exhibits sequential learning behavior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper is a natural extension to Cabannes et al. (2024) in three ways:

1. It extends the theory to a learnable task with trainable weights, not just studying random patterns
2. It considers the MLP and attention as contributions to the Associative Memory properties of transformers
3. It considers the (single-layer) transformer as a gradient flow

The goals are the same: to study the "memorization capacity" a.k.a. "scaling laws" of a transformer from the perspective of Associative Memory. The authors study this memorization capacity on a synthetic recall task consisting of memorizing subject-relationship correlations.

### Strengths
(S1) **Possibly high impact**. If the analyses performed in this paper are shown to hold for deeper transformers (with shared or unshared weights) using softmax activations in the attention and bigger datasets, the paper has the possibility to be high impact -- it would solidify the benefit of viewing transformers as formal Associative Memories, uniting the LLM community and the more niche physics- and math- communities studying associative memories. 

(S2) **Good, formal definition of Hallucination**. In a passing statement, this paper defines hallucination as the stage where [L455-460]

> ...the model ignores all other tokens in the sequence $z_{1:T}$ – including the useful subject token $s$ – and predicts based only on the relation r... the model is outputting a plausible, yet ultimately incorrect, answer to the prompt. 

As the associative memory perspective of transformers continues to gain traction and the theory of this paper extends to practically sized transformers and real NLP datasets, I can see this formal description of hallucination (i.e., the difference in the Cross-entropy loss of relationships and subjects) as game changing for the study of hallucination in LLMs. Related works do not seem to agree on a definition for "hallucination" except that it encompasses "undesirable predictions" from an LLM.

### Weaknesses
 (W1) **Unclear application to real Transformers and datasets**. (dual to (S1)) The simplified Transformer architecture studied theoretically and empirically in this work is smaller than real Transformers, uses only a single update step for much of the analysis, only uses a synthetic dataset to validate the theory, and drops the softmax from the attention. It is unclear how the theory would generalize to unshared weights and real datasets where the task is to reproduce sequences of data. Furthermore, the analysis focuses on a single layer transformer, whereas real-world transformers have many layers with complex interactions. The theoretical results need to be extended to multi-layer architectures to be more relevant. The use of a single update step for analysis also limits the applicability of the theory to real-world training scenarios where multiple gradient updates are the norm. The synthetic dataset, while useful for controlled experiments, does not capture the complexities of real-world data, such as long-range dependencies and diverse token distributions. The removal of the softmax from the attention mechanism also significantly simplifies the model and may not reflect the behavior of standard transformers.

(W2) **No comparison to the empirical scaling laws of modern LLMs**. Like (W1), this paper could be improved if the theoretical results are compared to the empirical results of e.g., the [Chinchilla scaling laws](https://arxiv.org/abs/2203.15556). Specifically, the paper should discuss how the derived scaling laws for the associative memory capacity relate to the observed scaling laws in large language models. For example, the Chinchilla scaling laws suggest a specific relationship between model size, dataset size, and performance. The paper should investigate whether the theoretical framework can reproduce such relationships or provide insights into why they might differ. The lack of such a comparison makes it difficult to assess the practical relevance of the theoretical findings.

(W3) **Associative memories are single-step updates**. One limitation of this work is that the associative memories are not energy-based models where the memories are encoded as fixed points of energy descent dynamics. Indeed, the memory capacity of the linear associative memory model would not scale linearly if formulated as an energy-minimization problem. It would be nice to see memory capacity studied in the recurrent setting. The current formulation of associative memories as single-step updates does not capture the iterative refinement of memories that occurs in energy-based models. This difference is significant because energy-based models can exhibit more robust memory retrieval and error correction capabilities. The paper should explore how the memory capacity of the proposed model changes when formulated as an energy-minimization problem and how this relates to the recurrent setting.

### Questions
(Q1) Standard Transformers typically output a probability distribution over all output tokens. The theory of Eq. (7) only considers the most-likely token (equivalent to setting the sampling temperature of LLMs -> close to 0). Indeed, there is a large debate in the community over the relationship between memorization and generalization. How could the memorization study of this work be scaled to study the *generalization* abilities of Transformers? I feel this theoretical framework could be used to tackle this problem.

(Q2) The paper only studies the causal-language modelling (i.e., GPT-style) objective. How would the theory extend to transformers trained on masked-token (i.e., BERT-style) tasks?

(Q3) Is $\sigma$ in Eq. (2) defined, or just an arbitrary non-linearity? The theory of [Dense Associative Memory](https://arxiv.org/abs/1606.01164) says that the choice of this non-linearity is critical to increasing the memory capacity of Associative Memories

(Q4) The experimental details around Fig 1 are incomplete -- I do not think I could replicate that experiment with the information included in the paper. Additionally, Fig 1 could be improved with error bars and notable "failure cases" e.g., the task of storing one-hot vectors [L130] or under different choices of $\sigma$ in the MLP (see (Q4)).

### Soundness
3

### Presentation
3

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
This papers show shallow transformers can use a combination of associative memories to obtain near optimal storage capacity. The verify this on a synthetic factual recall test.

### Strengths
1. The theoretical contributions are solid

### Weaknesses
1. The theoretical toy model is rather simple (MLP and one-layer transformer). It is unclear how it generalizes to multi-layer transformer. Specifically, the analysis focuses on a single attention layer, and it's not obvious how the associative memory mechanism would scale or behave with multiple stacked attention layers, which are a key component of modern transformer architectures. The interactions between different layers and their respective associative memories are not explored, and this limits the practical applicability of the theoretical findings.
2. If I understand correctly, the synthetic setting relies on the fact that noise tokens and subject tokens are disjoint. In reality, usually the last token (not eos in practice) should be somewhat relevant for token selection (for example, “in” as the last token would look for locations). It doesn’t make too much sense to let model do next token prediction after some random tokens. This disjointness assumption is a strong simplification that does not reflect real-world language modeling scenarios. In practice, the last token in a sequence often carries crucial contextual information that influences the prediction of the subsequent token. The model's performance in this simplified setting may not translate to more realistic scenarios where tokens are not independent and carry semantic relationships.

### Questions
1. How did you get the plot for Figure 5 (left)? It seems a bit too smooth. Also, why didn’t the first 2000 GD change the loss? It seems counter-intuitive. 
2. Could you give an intuitive explanation for why the model, in theorem 6, learns conditional distribution of relations as opposed to conditional distribution of subject?

### Soundness
3

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
4

### Summary
This paper examines factual recall in shallow Transformers, proposing that transformers can leverage associative memories for near-optimal storage of factual information. The authors demonstrate that linear and multi-layer perceptron (MLP) associative memories achieve storage capacity that scales linearly with the parameter count. They design a synthetic factual recall task to show that a single-layer Transformer can reliably store and retrieve facts using self-attention with or without an MLP. Additionally, their gradient dynamics analysis in a simplified linear attention model reveals a "hallucination" stage, where the model’s loss plateaus and predictions rely solely on relation information.

### Strengths
- This work offers a theoretical understanding of how shallow Transformers handle factual recall, specifically revealing linear and MLP associative memory capacity in managing storage.
- The gradient flow analysis, particularly the identification of an intermediate "hallucination" phase, adds depth to the understanding of transformer training dynamics.
- The paper demonstrates mathematical rigor in its proofs regarding associative memory storage capacity

### Weaknesses
 - The findings may be somewhat narrow, given the reliance on synthetic tasks. While the theoretical insights are valuable, it remains uncertain how well these translate to complex, real-world scenarios involving non-random and interdependent factual associations. Specifically, the synthetic task does not capture the nuances of real-world data, where facts are often interconnected and exhibit complex dependencies, potentially limiting the generalizability of the conclusions.
- The study is centered on shallow models, raising questions about the applicability of these findings to deeper, large-scale transformers commonly used in research and industry. The behavior of attention mechanisms and associative memory in deeper networks, with their increased capacity and complexity, may differ significantly from the shallow models analyzed in this paper. This discrepancy warrants further investigation to bridge the gap between theoretical results and practical applications.
- Certain sections, particularly those describing empirical setups for synthetic tasks, could benefit from added detail. Greater specificity on initialization, parameter tuning, and model configuration across trials would improve clarity and reproducibility. For example, the specific distributions used for initializing weights, the learning rate schedules, and the batch sizes used in training are not clearly stated, making it difficult to replicate the experiments.
- More discussion on related work exploring neural networks and attention mechanisms as associative memories [1,2] would strengthen the paper and highlight the novelty of the insight. The current discussion does not fully contextualize the work within the broader literature on associative memory in neural networks, potentially overlooking relevant prior findings and limiting the assessment of the paper's unique contributions.

### Questions
- The statement on line 117—that the number of associations scales linearly with the number of parameters (up to log factors)—is somewhat unclear. Without injective assumption, it looks like the number of tokens, not associations, scales linearly. Please elaborate on that point. 
- Section 4.2 appears to omit LayerNorm, which is part of the original Transformer layer. Would the theoretical results still hold if LayerNorm were considered?

### Soundness
3

### Presentation
2

### Contribution
3
