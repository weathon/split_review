# Transformer-VQ: Linear-Time Transformers via Vector Quantization

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
We introduce Transformer-VQ, a decoder-only transformer computing softmax-based dense self-attention in linear time.  Transformer-VQ's efficient attention is enabled by vector-quantized keys and a novel caching mechanism. 
In our large-scale experiments, Transformer-VQ is shown highly competitive in quality, obtaining 0.99 bpb on Enwik8, 26.6 ppl on PG-19, and 3.16 bpb on ImageNet64. In addition, the optimized implementation of Transformer-VQ is over 3x faster than a comparable quadratic-time transformer at sequence length 8k, is over 12x faster at 32k, and can scale to 131k with similar throughput

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* The paper proposes a linear-time attention mechanism based on vector-quantization.
* This scheme is evaluated quantitatively and qualitatively on various datasets.

### Strengths
* The idea of using vector-quantization to achieve linear attention sounds reasonable.
* The paper includes a detailed discussion of various related works and how they differ from Transformer-VQ.
* Code is provided, aiding reproducability.
* The paper provides qualitative samples of the various trained models.

### Weaknesses
 * I think the presentation of the paper could be improved. I think some pseudocode or diagrams illustrating the main ideas would be useful, while some of the theorems could potentially be moved to the Appendix.
* It seems to me that Transformer-VQ only significantly outperforms prior work on ImageNet64 where it uses a 7x larger model than the second best model.
* It also not entirely clear to me what the real-world advantage of Transformer-VQ is, I assume that the attention mechanism is significantly faster for longer context due to being linear. If so, it would be useful to demonstrate this with some actual speedup experiments.
* The datasets Transformer-VQ is evaluated on are also not current mainstream LLM datasets (which is the main application of Transformers and attention at the moment); I think results for e.g. standard token-level language modeling on C4 or The Pile would be more convincing.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new attention mechanism that can be realized to be linear in time. The proposed method uses vector quantization (mapping with learnable smooth codebooks) in a way that has non-zero gradients following [van den Oord *et al.* (2017)). Showing that attention as expressed in Definition 3.1. can be realized in linear time is not trivial, so the authors show in Thm. 3.7 how this speed up can be implemented using "cache" variables.

### Strengths
* Practicality: Instructions on how to implement the architecture is very detailed, and it looks like the authors experimented quite a lot to design an architecture that works well with various architecture sizes (190M, 1.2B, 1.3B parameters)
* Large-scale experiments across various challenging tasks.

### Weaknesses
The authors experiment with various architecture sizes; how did the authors choose which parameters to scale up? Is there some "scaling laws" that the authors observed to be useful? For example, fixing the codebook size to 256 may restrict the model's expressiveness which can be extremely critical for generative models. Given that the authors are emphasizing a decoder model which is particularly useful for generative tasks, I believe this paper would benefit from analysis on this new parameter's effect in addition to Sec. 5.1.1. One type of experiment that could demonstrate this effect would be to see if the model's performance saturates at some parameter count, and see if performance saturation is caused by the codebook size by training the same model with a larger codebook size S. Sharing these would be useful to anyone who plans to use this architecture for custom tasks. 

Overall the paper is well written, but I think the paper could benefit if the authors provide intuition for the caching mechanisms and the implementation for efficient attention (Theorems 3.4-3.7). Further, the proofs are written just as a sequence of equations without any conceptual descriptions, so it's quite hard to understand what steps are being used in the proofs.

### Questions
* In Sec. 5.1.2 the authors say that the codebook size is 256 but Table 6 in the appendix shows S is 512. Is this a typo?
* What are the authors trying to show with ImageNet64? Is this part trying to show-case the model's applicability as a "vision transformer" type of model?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel attention mechanism with linear time complexity. The core idea is to apply vector quantization (VQ) on Keys, leading to the primary computing being (Query x Codebooks), where the number of codebooks is relatively small (256, 512, 1024) compared to the entire sequence length. The proposed method, termed Transformer-VQ, is applicable for both Transformer Encoder and Decoder models. Experimental results in long-context language modeling and image density estimation show that the proposed attention modification achieves performance comparable to prior works.

### Strengths
* While the idea of adopting VQ into Transformers is not entirely new (ex: Clustered Attention), the paper’s innovation is in using VQ for Keys and demonstrating its effectiveness (especially for Decoder). This is a nice contribution.
* The paper provides a comprehensive review of related works, addressing various aspects. Furthermore, the equations and notations are presented clearly to help clarify the core idea.

### Weaknesses
 * Although this paper focuses on efficient computation, there is no direct comparison of FLOPs or actual inference latency on GPUs/TPUs with previous works. It would also be beneficial to include a comparison between models with and without VQ. The absence of these comparisons makes it difficult to assess the practical benefits of the proposed method in terms of computational speedup and resource utilization. Specifically, without FLOPs analysis, it's unclear how much the reduced key computation translates to overall efficiency gains, and the lack of latency benchmarks leaves the real-world performance impact uncertain. Furthermore, comparing against a non-VQ baseline would isolate the effect of the VQ mechanism.
* Only one model size (1.3B for PG-19, 1.2B for ImageNet64) is used for experiments. To demonstrate the effectiveness, it would be valuable to test with multiple (smaller) model sizes where the sequence length exceeds the hidden dimension of Transformers. I assume that the actual inference speedup would arise when the sequence length is sufficiently larger than the hidden dimension of Transformers – I’m not sure if the tested models are such a case. The current experiments do not fully explore the relationship between model size, sequence length, and the efficiency gains of the proposed method. It is crucial to evaluate the method's performance across different scales to understand its applicability in various settings. Specifically, the benefits of the linear time complexity may not be apparent when the sequence length is not significantly larger than the hidden dimension, and testing smaller models would clarify this.
* As the authors mentioned in Section 5.2.1, it seems that simple attention dropout is not applicable; is searching for the appropriate regularization setting a challenging job? In other words, is the model robust enough regarding regularization hyperparameters? The sensitivity of the model to regularization hyperparameters is a concern. The fact that standard attention dropout fails suggests that the model might be more susceptible to overfitting or require more careful tuning of regularization parameters. It is important to understand the robustness of the model with respect to these hyperparameters to ensure its reliable performance.
* The paper uses the GAU Transformer instead of a vanilla Transformer; Is there any reason why you used this variant? If the reason is that GAU employs single-headed attention, is Transformer-VQ applicable to a base (naïve) Transformer architecture?
* Linear-time Encoder is also explained in Section 3.2 but there are no corresponding experiments.
* The “truncation-free fixed-size cache” part is confusing. Does this refer to the limitation of the total stored Key size to “LK” (Section 3.4.2)? If so, then where does the ‘truncation-free’ part come?
* Suggestion: It would be beneficial to include a figure of the computation process (especially visualizing L, C, K, and V) for both the encoder and decoder. The current version only presents mathematical formulations, which can make it difficult to understand the core algorithm.
* (minor) In Section 3.1, maybe the “gated activation unit” is a typo of “gated attention unit”?
* (minor) Large “K” seems to be used in two different contexts (key and query block size); consider changing the latter to another letter.

### Questions
* As the authors mentioned in Section 5.2.1, it seems that simple attention dropout is not applicable; is searching for the appropriate regularization setting a challenging job? In other words, is the model robust enough regarding regularization hyperparameters?
* The paper uses the GAU Transformer instead of a vanilla Transformer; Is there any reason why you used this variant? If the reason is that GAU employs single-headed attention, is Transformer-VQ applicable to a base (naïve) Transformer architecture?
* Linear-time Encoder is also explained in Section 3.2 but there are no corresponding experiments.
* The “truncation-free fixed-size cache” part is confusing. Does this refer to the limitation of the total stored Key size to “LK” (Section 3.4.2)? If so, then where does the ‘truncation-free’ part come?
* Suggestion: It would be beneficial to include a figure of the computation process (especially visualizing L, C, K, and V) for both the encoder and decoder. The current version only presents mathematical formulations, which can make it difficult to understand the core algorithm.
* (minor) In Section 3.1, maybe the “gated activation unit” is a typo of “gated attention unit”?
* (minor) Large “K” seems to be used in two different contexts (key and query block size); consider changing the latter to another letter.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
