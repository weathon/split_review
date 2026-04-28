# SEA: Sparse Linear Attention with Estimated Attention Mask

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
The transformer architecture has driven breakthroughs in recent years on tasks which require modeling pairwise relationships between sequential elements, as is the case in natural language understanding. 
However, long seqeuences pose a problem due to the quadratic complexity of the attention operation. Previous research has aimed to lower the complexity by sparsifying or linearly approximating the attention matrix. Yet, these approaches cannot straightforwardly distill knowledge from a teacher's attention matrix, and often require complete retraining from scratch. Furthermore, previous sparse and linear approaches lose interpretability if they cannot produce full attention matrices.
To address these challenges, we propose \textbf{SEA}: \textbf{S}parse linear attention with an \textbf{E}stimated \textbf{A}ttention mask.
SEA estimates the attention matrix with linear complexity via kernel-based linear attention, then subsequently creates a sparse attention matrix with a top-$\hat{k}$ selection to perform a sparse attention operation. 
For language modeling tasks (Wikitext2), previous linear and sparse attention methods show roughly two-fold worse perplexity scores over the quadratic OPT-1.3B baseline, while SEA achieves better perplexity than OPT-1.3B, using roughly half the memory of OPT-1.3B, providing interpretable attention matrix. We believe that our work will have a large practical impact, as it opens the possibility of running large transformers on resource-limited devices with less memory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces SEA, a novel method to approximate the full dot-product attention at inference time. It uses two mechanisms: (i) it relies on a linearization to build a compressed attention representation and then (ii) generates a full-scale sparse attention mask from this representation. They show their method outperforms other linear and sparse attention methods in language modeling tasks, specifically on GLUE and Wikitext2, while being competitive in terms of memory usage and latency. SEA introduces additional model parameters which are trained on top of a pretrained model using knowledge distillation. Unlike some of its competitors, the method remains interpretable.

### Strengths
Enabling faster processing of long sequences is an important research direction, and the proposed method is well-motivated. I appreciate the effort made in presenting the method, which, despite its complexity, can still be understood. The idea of combining kernel-based linear attention and sparsification is novel. On GLUE tasks, experiments show how SEA approximates full attention better than other methods while remaining competitive in terms of memory footprint. Moreover, unlike other approaches, SEA can successfully approximate the full-attention of pretrained OPT models.

### Weaknesses
- Comparison with FlashAttention [1]: It would be fair to add FlashAttention among the baselines. Especially, FlashAttention would also be competitive in terms of memory.
- The method is still quite complex, making it hard to deploy. 
- The latency results do not show a clear advantage of the method over baselines, often being significantly slower.
- The justification of the method for autoregressive language modeling is unclear. As most causal models are used for sequence generation, sampling one token at a time, the need to sparsify the attention matrix at inference time is reduced.

References:
[1] FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

### Questions
- How would SEA compare to FlashAttention?
- How difficult is it to tune the weights given to the different loss terms? 
- Wikitext is a relatively narrow dataset, how would the approximation handle more diverse datasets such as openwebtext?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to improve the quadratic dependency of the attention mechanism on the token length to linear, addressing a critical issue in computational complexity.





------------------------------------------------------------------------------------
post rebuttal update:
I'd like to thank the authors for answering my questions. I raise my score.

### Strengths
The computational complexity of the attention mechanism is a serious bottleneck and improving this to linear is very useful. The strength of the paper is that it tackles an important problem.

### Weaknesses
The paper's clarity and explanation of the algorithm's functionality are lacking, making it challenging to determine its applicability, particularly with regard to pre-trained models.

### Questions
- Can your algorithm be applied to pre-trained models for faster inference without requiring fine-tuning? Can one apply your algorithm for faster inference with no fine-tuning whatsoever?

- Could you provide a detailed explanation of Figure 2? I'm having difficulty understanding this diagram. Is the decoder (MLP CNN) trained from scratch, or can it be extracted from pre-trained models?

- In general, do you train all components depicted in Figure 2, or do you incorporate some parts from pre-trained models while keeping them fixed?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new test-time sparse linear attention method that 1) estimates the quadratic attention in compressed size, in the style of Performer; 2) performs a top-k selection on the approximated attention to obtain a mask, and 3) interpolates top-k selection to obtain a full sparse attention matrix and then perform sparse attention. They show that their method achieves better perplexity on accuracies on WikiText2 and GLUE tasks respectively.

The authors also contribute a new Triton kernel for performing efficient sparse attention.

### Strengths
S1. I like the approach of a "test-time" sparse linear attention. 

S2. I appreciate the thorough description of the author's contributions.

S3: I appreciate the contribution of a new Triton kernel for sparse operations.

### Weaknesses
W1. One of the motivations of the paper is that other linear attentions cannot distill the learned attention patterns, and hence need to train from scratch. However, the authors in the paper still need to train their Performer and Decoder from scratch. I haven't seen any discussion about the inherent cost of doing that. Intuitively, it should be cheaper than training from scratch, but can you point me to the text (or elaborate in a new discussion) about how expensive it is to do this training?

W2. This is my subjective view, but the paper is extremely dense and hard to follow. I'd recommend reducing the notation significantly and moving most of the details to the appendix. I appreciate the figures, but overwhelming them with notation does aid my understanding of your method in the current version of the paper.

I recommend: 1) simpler figures with less notation that can clearly explain your method conceptually; 2) moving a lot of the notation in the text for the appendix.

W3. It seems to me that some of the results are a bit underwhelming. For example, in Figure 4, panel (a), right figure, what is the motivation to use your method, since I could use a Vanilla transformer and achieve an on-par accuracy with much less latency?

### Questions
Please, see W1-3 above. It would be great to revise your paper based on my comments and questions. Thanks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
