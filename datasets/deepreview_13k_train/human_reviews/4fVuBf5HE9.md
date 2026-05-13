# Towards Analyzing Self-attention via Linear Neural Network

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Self-attention is a key component of the transformer architecture which has driven much of recent advances in AI. Theoretical analysis of self-attention has received significant attention and remains a work in progress. In this paper, we analyze gradient flow training of a simplified transformer model consisting of a single linear self-attention layer (thus it lacks softmax, MLP,  and layer-normalization) with a single head on a histogram-like problem: the input is a sequence of characters from an alphabet and the output is the vector of counts of each letter in the input sequence. Our analysis goes via a reduction to 2-layer linear neural networks in which the input layer matrix is a diagonal matrix. We provide a complete analysis of gradient flow on these networks. Our reduction to linear neural networks involves one assumption which we empirically verify. Our analysis extends to various extensions of the histogram problem.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper simplifies the training dynamics problem of a 1-layer linear self-attention layer into the joint optimization problem with two matrix variables that minimize loss like l_{df}(Q, v) = 0.5 * |Q*Diag(v) - M|_F^2. They show that this loss will decrease in exponential speed. They also try histogram tasks and show that the learned attention maps match their expectation.

### Strengths
1. The writing is clear, and the main result is easy to understand.
2. I think the construction of s for solving dynamics systems in theorem 2 is skillful.

### Weaknesses
1) The main setup studied in the paper is not well motivated. Why should one care about the histogram-like learning tasks? By construction, self-attention can easily model this task. But that alone does not justify the importance of such tasks. The paper does not provide any compelling argument for why analyzing this specific task is relevant to understanding the broader behavior of self-attention in more complex scenarios. It's unclear what insights gained from this simplified setting can be generalized to practical applications of self-attention.
2) The paper considers a very simplified setup, e.g., single-layer, no positional embeddings, and the size of the alphabet equal to the embedding dimension. How the findings of this paper affect the practice is not at all clear from the current version of the paper. The lack of positional embeddings, for example, significantly limits the applicability of the analysis to real-world sequence modeling tasks where position is crucial. Furthermore, the constraint of alphabet size equaling embedding dimension is highly artificial and does not reflect common usage of self-attention models.
3) While discussing the prior works, the paper states "...While insightful, these papers generally involve stylized assumptions and this makes it difficult to compare the results." However, this paper goes on to study a completely new problem (again with various assumptions); hence does not provide any comparison with prior art. The paper introduces a new set of assumptions without clearly articulating how this new framework relates to or improves upon existing work. The lack of comparison makes it difficult to assess the significance of the results.
4) There is significant scope for improvement in the presentation of the paper. For example, one can improve the flow of the paper by better organizing the key contributions and the discussion of prior work. Similarly, there is room for improvement in the presentation of the technical content. Section 4 repeatedly mentions Eq. (2) which is only introduced later in Section 5. Similarly, Theorem 2 is mentioned multiple times before being formally introduced or informally discussed. How do various points in Remark 1 constitute an as "extensions of theorem 2"?

### Questions
The same as weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to understand the training dynamics of self-attention networks. In particular, the paper focuses on a simplified single-layer self-attention network without softmax, MLP, layer normalization, and positional embeddings. It restricts itself to a specific class of learning tasks, namely histogram-like tasks. In its simplest form, given an $N$ length sequence, this task requires the network to produce an $N$ length output sequence where $i$th output element contains the frequency of the input element at the $i$th position in the input sequence. The paper reduces the problem of learning the simplified self-attention model to learning a two-layer linear network. Subsequently, the paper analyzes the gradient flow for learning the two-layer linear network.

### Strengths
1) The paper considers multiple variants of the histogram-like learning tasks for a single-layer self-attention model. 
2) The paper explores a connection between learning self-attention models and linear networks.
3) The paper exploits the structure of the underlying problem and breaks down the gradient flow analysis of learning linear networks to multiple one-dimensional problems.

### Weaknesses
1. The paper only deals with a very simple attention layer with only a single linear layer and lacks the components of the transformer model. This setting is not practical in real-world applications and thus limits the scope of the paper’s results. Specifically, the absence of multi-head attention, positional encodings, and feed-forward networks, which are crucial for the success of transformers in practice, makes the analysis less relevant to the broader understanding of transformer training dynamics. The simplified model, while mathematically tractable, may not capture the complex interactions and non-linearities that arise in full transformer architectures.

2. The paper only considers the histogram tasks, which is rather limited in the context of Transformers. This task does not reflect the sequence-to-sequence nature of many transformer applications, such as language modeling and machine translation, where the model needs to process and generate variable-length sequences. The histogram task, with its fixed-length input and output, does not fully explore the capabilities of the attention mechanism in handling sequential dependencies and long-range interactions.

3. The paper lacks experiment results to demonstrate the theoretical results. While the theoretical analysis is detailed, the absence of empirical validation makes it difficult to assess the practical relevance and applicability of the findings. Experiments should demonstrate the convergence behavior of the loss function and the impact of different initialization strategies, as well as the effect of the simplified attention mechanism on the training dynamics.

### Questions
See the comments under the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes the gradient flow training dynamics of a simplified linear transformer on the histogram task. The method reduces the training of a simplified transformer to that of a linear neural network with two layers where the first layer is a diagonal matrix. The theoretical results of the paper are based on one assumption, which is experimentally justified.

### Strengths
1. The proofs of the theorems and lemmas are provided and detailed.

2. Assumption 3.1 for the theoretical results seems reasonable and experimentally justified. 

3. The paper is well-motivated.

### Weaknesses
1. The paper only deals with a very simple attention layer with only a single linear layer and lacks the components of the transformer model. This setting is not practical in real-world applications and thus limits the scope of the paper’s results.

2. The paper only considers the histogram tasks, which is rather limited in the context of Transformers. 

3. The paper lacks experiment results to demonstrate the theoretical results.

### Questions
1. Can the results of the paper be extended to other common machine learning tasks where Transformers succeed such as language modeling or machine translation, rather than just the histogram tasks?

2. It would be helpful to show the decay behavior of the loss function $l$ in Theorem 1 under random initialization. Additionally, the authors should demonstrate the behavior of $l$ under bad initialization.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
