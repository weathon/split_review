# Attention Is All You Need For Mixture-of-Depths Routing

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
Advancements in deep learning are driven by training models with increasingly larger numbers of parameters, which in turn heightens the computational demands. To address this issue, Mixture-of-Depths (MoD) models have been proposed to dynamically assign computations only to the most relevant parts of the inputs, thereby enabling the deployment of large-parameter models with high efficiency during inference and training. These MoD models utilize a routing mechanism to determine which tokens should be processed by a layer, or skipped. However, conventional MoD models employ additional network layers specifically for the routing which are difficult to train, and add complexity and deployment overhead to the model. In this paper, we introduce a novel attention-based routing mechanism *A-MoD* that leverages the existing attention map of the preceding layer for routing decisions within the current layer. Compared to standard routing, *A-MoD* allows for more efficient training as it introduces no additional trainable parameters and can be easily adapted from pretrained transformer models. Furthermore, it can increase the performance of the MoD model. For instance, we observe up to $2$\% higher accuracy on ImageNet compared to standard routing and isoFLOP ViT baselines. Furthermore,  *A-MoD* improves the MoD training convergence, leading to up to $2\times$ faster transfer learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a parameter-free routing method for mixture-of-depths (MoD) models. 
It uses attention maps to discover the importance of each token. 
The authors also tested the results on a series of DeiT/ViT models.

### Strengths
This paper explores the token importance evaluation through the existing attention maps and thus reduce the overhead of extra layers.

### Weaknesses
1. There is no comparison with the current SOTA models since DeiT/ViT are relatively old. 
2. The idea is quite similar to the following papers. It would be great to include the comparison (such as accuracy and latency) with these papers. 
DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification and 
Token Merging: Your ViT But Faster

### Questions
1. what's benefits of the proposed approach compared to traditional ConvNet? It would be great to include some comparison with ResNext etc
2. What's the advantage of the proposed approach against the transformer / convnet hybrid architecture such as LeViT: a Vision Transformer in ConvNet's Clothing for Faster Inference or FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a parameter-free routing method to improve the routing mechanism in the mixture-of-depths (MoD) method. The basic idea is to directly use the attention scores in Transformer.

### Strengths
- Using the transformer attention in the MoD routing makes sense.
- Extensive results do prove that the proposed A-MoD outperforms MoD.

### Weaknesses
 - The entire study is too narrow and limited. This paper is specifically targeted at MoD. However, MoD is just an arxiv paper. Does MoD represent the SoTA in terms of the Pareto frontier? All the experiments are mainly compared with MoD? What about other SoTA methods? BTW, MoD is not impressive in Table 1, where it is even inferior to a simple baseline, isoFLOP.

- Why is higher average attention in (4) corresponding to higher importance? What is the semantic meaning? If so, shouldn't the background tokens in Fig. 4 not be skipped since they have high attentions with many other background tokens? BTW, what are the different columns in Fig. 4 and Fig. 5?

### Questions
Please address the issues pointed out in the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the authors aims to deal with an interesting problem: How to reduce the token number need to be computed in a layer, and proposed A-MOD. A-MOD is simply based on attention score to select tokens need to be calculated, and the rest will be directly skiped. Experimental results show promising results.

Such a topic is always interesting and important, especially in the era of large models. However, almost none is applied to indutry because these methods are always only efficient in theory. I encourage more explorations in this topic. Regarding this work, I believe many experimental settings are not reasonable or not as expected.

### Strengths
1. The authors tackle an important issue in improving the efficiency of ViTs by proposing a method that dynamically selects the most relevant tokens for computation. This approach aligns with similar techniques in the field, such as A-ViT, which also prioritize token selection for efficiency gains.

2. Additionally, the experimental results show promising performance.

### Weaknesses
The main idea behind the proposed method makes sense to me, but I have several concerns, particularly regarding the experiments and their settings.

1) First, the authors mention in Line 234 that they continue training from a previous checkpoint for an additional 100 epochs. I’m curious whether this approach is justified. Why not simply start training from scratch?

2) I also find the transfer learning setup a bit confusing, especially since the authors do not use fixed pretrained weights. Why is transfer learning considered in a work that focuses on efficiency? How does it contribute to the overall goals of the work? Clarity on this point would be help.

3) Regarding the baseline, I expected to see a vanilla ViT for comparison, but instead,  the authors reduced the original ViT layers to match FLOPs directly. This choice makes no sense to me if the goal is to demonstrate that A-MOD improves effiency. Additionally, I noticed that A-MOD significantly lowers the original performance of ViT. For instance, the original ViT-Tiny achieves ~74% accuracy, whereas A-MOD only reaches 69.76% and 71.8%. 
The abstract is is also very misleading; I initially was thinking the method reduces the number of tokens while improving accuracy on ImageNet by 2% (a huge improvement on ImageNet).

4) Is the same selection ratio applied across all layers, from shallow to deep? we know that shallow layers typically do not generate meaningful attention maps.

5) At a high level, A-MOD aims to reduce token number for computation, which is similar to the approach taken in the TO-ME paper (“Token Merging: Your ViT but Faster,” ICLR 2023). However, I noticed that the performance of A-MOD is much worse, and there are no speed tests provided to show efficiency gains.

6) In Fig. 4,  the last image of the first row, it appears that MOD selects almost all unimportant boundary patches and parts of the bird's head. Does this make sense? If it does, I would like to know why.

7) Generally, attention maps in shallow layers do not reliably indicate importance. Given this, how should we interpret the results shown in Fig. 5? Were the specific attention heads or examples chosen selectively, or could you provide additional much more examples (besides the bird and car used throughtout the paper) to support the findings?

8) Finally, in Line 420, the authors state, “attention maps do not always learn semantically meaningful scores.” This leads me to two questions: How did you conclude that this issue is only limited to larger models? If this only happens in larger models, why does A-MOD work for ViT-Tiny?

### Questions
1. Are there any other reproducible results for MOD on ImageNet?

2. How are different heads within a single layer handled? Will different heads select different tokens for computation in a layer?

3. As indicated in the abstract, it’s unclear how this method improves training and inference efficiency on an ImageNet-scale dataset. Are these efficiency improvements achieved in practice (like in training and inference speed) or just in theory?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Mixture of Depth methods have recently been proposed as an alternative to Mixture of Expert methods. Instead of deciding to which expert to route a token, MoD takes a decision whether or not to skip the current expert. The main purpose shared by these methods is that of finding a better compute/performance tradeoff, which is currently of particular interest in the context of LLMs and large generative models. One of the main challenges for building such methods is the design of stable routing mechanisms. The authors propose A-MoD, a routing method which performs pruning of tokens traversing the current layer, based on the respective attention scores in the previous layer. The authors evaluate their method on classification tasks on a set of DeiT and DiT models of varying size.

### Strengths
- The method is simple and clearly explained throughout the paper. It seems possible to implement it easily for small models operating on short token sequences.
- The proposed method is simple and the idea of eliminating learnable routing, a major source of training instabilities, is an interesting research direction.
- Some performance improvements are shown under some settings of a classification task.

### Weaknesses
 - The method requires access to the attention matrices. Modern attention implementations (e.g. "FlashAttention") do not materialize attention matrices due to their large materialization cost. An implementation of A-MoD viable for an LLM or large generative model would require non-trivial implementation effort to match the performance of modern attention implementations.
- The chosen evaluation setting is composed only of classification tasks. Token pruning is particularly suited for this task, as all tokens with information not relevant to the depicted object can be safely discarded and the model output consists in only an aggregation of the tokens. A more significant evaluation would have taken segmentation, language modeling, or image/video generation problems into account. In these tasks token pruning can be problematic, as every token will be returned as an output. Pruned tokens are at risk of generating artifacts in such context. Lack of evaluation in these context is a significant limitation.
- The method presents a limitation in the maximum achievable speedup with respect to a corresponding dense architecture. In particular, as each A-MoD block bases its pruning on the previous block, it can only be applied at alternating blocks, posing a maximum achievable speedup to 2X over a corresponding non A-MoD model. In contrast, a learnable routing mechanism would allow application of MoD to each layer, allowing for higher theoretical speedups, making the pursuit of this paradigm more promising than A-MoD.
- Some recent MoE architectures (Snowflake Arctic LLM) show that it is beneficial to apply MoE at every layer. A-MoD can apply it only every other layer
- Table 1 proposed evaluation with an isoFLOP baseline. Under 3/8 configurations, the isoFLOP baseline has <90% of the flops of the A-MoD model. Such comparison does not appear fair
- Table 1 would benefit from being accompanied by a Pareto curve visualization of performance vs compute, which could highlight better the Pareto front for the C=12.5% case, where compute of the baseline and A-MoD method is mismatched.
- The paper does not take inference throughput into consideration. In this paper, FLOPs are an incomplete indicator of model cost in that they do not highlight performance losses caused by the need to materialize the attention matrix. It is likely that the isoFLOP baseline when implemented carefully with an efficient attention implementation would outperform A-MoD in terms of inference throughput and memory utilization, especially if evaluated in practically-relevant language modeling or generative tasks with large amounts of tokens.
- Discussion in 4.5 and Fig. 7 are not convincing. In Fig 7 (a) performance is aligned to the isoFLOP baseline, in Fig 7 (b) compute is too mismatched between baselines to draw conclusions.

In summary, the pursuit of A-MoD seems less promising than traditional MoD or MoE paradigms due to its limited theoretical maximum achievable speedup of 2X. Evaluation is performed on classification only, missing some important performance metrics (throughput/latency) and in some circumstances under unfair evaluation settings for the baseline. Evaluation does not comprise important dense prediction tasks such as language modeling or image/video generation. No discussion or remedy is presented for the need of materializing full attention matrices, limiting applicability of the method for large models operating on long sequences, which could benefit most from MoD/MoE.

For these reasons, I do not believe the method implementation and evaluation are solid enough for the paper to be accepted.

### Questions
- Can the authors provide an implementation of an efficient attention mechanism such as "Flash Attention" with support for A-MoD? If yes, how would the performance of this implementation compare to the original implementation?
- Can the authors show performance of the method on a task such as semantic segmentation, language modeling or image/video generation that involves producing an output token for each input token to confirm that token dropping would not affect output quality?
- Could the authors revise Table 1 to perform a fairer comparison with isoFLOP baselines and show results using a Pareto curve?
- Could the authors revise qualitative evaluations to include throughput measures rather than FLOPS only, ensuring baseline methods make use of efficient attention implementations?
- Could the authors revise quantitative evaluation to include a task involving large numbers of tokens (>=4k tokens) to show that the attention operation implementation can remain efficient as the input size grows?

### Soundness
2

### Presentation
3

### Contribution
2
