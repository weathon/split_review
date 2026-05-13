# CoTFormer: A Chain of Thought Driven Architecture with Budget-Adaptive Computation Cost at Inference

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Scaling language models to larger and deeper sizes has led to significant boosts in performance. Even though the size of these models limits their application in compute-constrained environments, the race to continually develop ever larger and deeper foundational models is underway. At the same time---regardless of the model size---task-specific techniques continue to play a pivotal role in achieving optimal downstream performance. One of these techniques, called Chain-of-Thought (CoT), is particularly interesting since, as we point out in this work, it resembles employing a deeper transformer through re-applying the model multiple times. However, a key subtlety in computing the attention of past tokens differentiates CoT from simply applying the model several times. Based on this insight, we propose CoTFormer, a novel architecture which closely mimics CoT at the token level, allowing us to obtain significantly improved accuracies close to much larger models. While applying CoT introduces additional computation costs, we compensate for it by leveraging CoTFormer's special compatibility with token-wise variable depth. 
Through a compute adaptive model---which automatically allocates the compute to tokens that need it most---we show that it is possible to reduce the computation cost significantly without any reduction in accuracy, and with further compute cost reductions possible while maintaining a competitive accuracy. %

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces CoTFormer, a novel transformer architecture that draws inspiration from chain-of-thought (CoT) reasoning. The key insight is recognizing that CoT differs from simple weight-tying in how attention operates across intermediary reasoning steps. The authors leverage this insight to develop an architecture that allows tokens to attend to representations from all previous "thought" steps, leading to improved performance compared to baseline approaches like Block Universal Transformers. Additionally, they propose an adaptive computation mechanism that allows dynamic allocation of computational resources at inference time.

### Strengths
*The application of deploying LLMs to storage-constrained devices like mobile phones is relevant and timely.
* The proposed CoTFormer architecture (Figure 1(c)) effectively translates the CoT principle into architectural design, showing clear improvements over baseline approaches while maintaining parameter efficiency through weight sharing (Section 3.1).
* The architectural tweaks introduced in Section 3.3, particularly reserved layers and layer normalization after each repeat (LN-CoTFormer), prove crucial for achieving state-of-the-art results.
* Addition of depth embedding (Section 4.2) shows notable improvements in the adaptive setting.
* While not outperforming a FLOP-matched non-repeated transformer, the authors improve upon existing parameter-matched weight sharing baselines.
* The proposed architecture and adaptive repetition method are described clearly.

### Weaknesses
 * While Section 3.2 provides empirical evidence, the theoretical understanding of why CoTFormer works better could be deeper. Through analysis of attention patterns, we observe that tokens in later repeats tend to focus heavily on earlier representations that capture key contextual information, suggesting the model learns to leverage complementary features detected at different processing stages. This selective attention to informative past representations may help explain why CoTFormer outperforms the baseline Block Universal Transformer, where such cross-repeat attention patterns are not possible.
* Could better connect to recent theoretical work on transformer expressivity discussed in Section 2. Specifically, the paper could benefit from a discussion of how the proposed architecture relates to the existing theoretical understanding of the expressive power of transformers, particularly in the context of depth vs. width tradeoffs. It is unclear how the repeated processing of tokens and the ability to attend to previous representations affects the model's ability to learn complex functions compared to standard transformers.
* The sequence lengths that are used for training (256) are quite short relative to the lengths that are used for training modern language models and are shorter relative to common LLM evals and typical chatbot conversations. This raises concerns about the generalizability of the findings to more realistic scenarios with longer input sequences. Additionally, the paper does not explore the performance of the proposed method on tasks that require long-range dependencies, which are known to be challenging for standard transformers.
* Performance gap between adaptive and fixed-depth CoTFormers under same compute budget (Section 5). The paper does not provide a clear explanation for why the adaptive version does not achieve the same performance as the fixed depth version given the same compute budget. This suggests that the training procedure for the adaptive model may not be optimal, or that there may be fundamental limitations to the adaptive approach.
* Training efficiency of deeper layers could be improved (e.g. increasing the gradient information during adaptive training), as shown by the analysis of router weights distribution (Figure 5). The paper could discuss potential methods for improving the training of deeper layers, such as using techniques like layer-wise learning rate adaptation or gradient boosting, to ensure that all layers are effectively utilized during training.

### Questions
* I’m confused by Figure 1(c): it seems to indicate that the earlier token representations (i.e. the red rectangles) are reprocessed by the model to make new token representations. But Section 3.1 seems to contradict this and instead describes that these earlier representations are only used as context in attention.
* It would be helpful to state the total parameter counts of the models used in each experiment, as well as the total number of training tokens in each experiment (either in a table or in the prose describing experimental setup).
* 471: It would be helpful if the authors provided more details on their “efficient implementation”, and specifically how the authors are using a non-causal FlashAttention kernel to implement their  proposed method.= 
* How do position embeddings work with the added interleaved tokens? Are the interleaved tokens given the same position id as the original tokens they came from, do the position ids change between repetitions, or something else?
* Do the authors have any intuitions as to how their method behaves as the width of the model changes? It appears to be held constant across all experiments.
* 402: what does it mean to “activate a prefix of repeats”? is this the fixed depth baseline that is referenced in Figure 4?
How does mixture of repeats work during, for example, batch size 1 transformer decoding, where there is only a single token being processed through the model?


Below are some thoughts that might be helpful but are not critical to give insight into ways that might improve the paper.
* Consider analyzing attention patterns and strengthening theoretical connections to transformer expressivity research (building on 3's architecture analysis).
* Explore sparse variants to improve scaling for longer sequences beyond 8192 (extending the computational analysis in 3.2).
* Focus on improving training efficiency, particularly for deeper layers and adaptive computation (addressing limitations discussed in 5).
* Develop specialized attention implementations for better computational performance (following the implementation discussion in 5).
* Expand evaluation to include longer sequences and broader comparisons with other adaptive approaches (extending the experimental work in 4.3).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes CoTFormer, a novel Transformer-based model architecture for generative language models.
Like Universal Transformers, a CoTFormer re-applies the same Transformer blocks for an adaptive number of times for generating each token.
The major difference is, after each repeat, the output tokens interleaved with input tokens are used as the new input for the next repeat;
this is inspired by chain-of-thought where each generated "thought token" can attend directly to all previous thought tokens.
Other details are handled, such as compatibility with KV cache and batch processing during inference.
Empirical results show that a CoTFormer achieves lower perplexity or higher scores in some common benchmarks 
than Block Universal Transformer with the same configuration, 
or a standard Transformer of the same size.

### Strengths
- This work proposes a novel Transformer-based model architecture, and draws an interesting link to chain-of-thought.
The proposed CoTFormer is compatible with KV cache and batch processing, which is not the case for many other adaptive-computation architectures tailored to autoregressive generation.

- Overall the writing is good, and things are mostly well explained.

- The source code is provided.

### Weaknesses
My major concern is that the empirical evidence for the efficacy of CoTFormer, or its advantages over the standard Transformer architecture, is insufficient.

- Generally speaking, the empirical results from the main text suggest that a CoTFormer with $n_{\text{repeat}} \ge 2$ slightly outperforms a standard Transformer of the same size in terms of perplexity, but underperforms a standard Transformer with twice as many layers, except in Table 2 where a CoTFormer with $n_{\text{repeat}}$ as large as 5 (and other tweaks) achieves a perplexity that is lower by only 0.06. 
The issue is that the inference cost (in terms of time or memory, or both) of a CoTFormer, with the total number of tokens growing linearly with $n_{\text{repeat}}$, can possibly be larger than that of a standard Transformer with twice as many layers. This raises the question of whether CoTFormer actually pushes forward the Pareto frontier of accuracy and cost; to support such a claim, it is necessary to compare CoTFormer's accuracy-cost curves with those of standard Transformers (not just Block Universal Transformer). Without clear evidence of its advantages over standard Transformers, the additional complexity overhead to code and infrastructure might further hinders the adoption of CoTFormer in future research or applications.

- The results of downstream performance in Appendix B have limited implications, as discussed by the authors in Line 725. 
    For example, all scores for MMLU are close to 25%, namely the accuracy of randomly picking option A/B/C/D.

- The current work only contains end-to-end performance (perplexity or scores) on some common datasets and benchmarks.
    There is no intermediate empirical result (except for Figure 5) or synthetic task, like those in the original paper of Universal Transformers (Dehghani et al., 2019), for truly understanding when, why and how CoTFormer works or fails.
The authors might consider visualizing the attention patterns of CoTFormer, or designing synthetic tasks that highlight CoTFormer's fundamental advantages over standard Transformers or Universal Transformers.

### Questions
- Typo in Line 114, "similar the" --> "similar to the"


- Is it possible to convert a standard pre-trained Transformer to a CoTFormer via a post-training or fine-tuning phase, which can be much more efficient than pre-training a CoTFormer from scratch?
I can't see an obvious way of doing this, since the behavior of a CoTFormer deviates significantly from that of a standard Transformer.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new model architecture called CoTFormer that improves the Block Universal Transformer by providing intermediary representations from previous repeats in the attention. Besides CoTFormer architecture, the paper also proposes a training approach called Mixture of Repeats that varies the number of model passes for individual tokens based on their difficulty. Results show that CoTFormer substantially improves accuracy and inference computation efficiency over Block Universal Transformer.

### Strengths
1. The CoTFormer architecture and Mixture-of-Repeats approach effectively improve the performance and efficiency of the Universal Transformer.
2. The evaluation of downstream tasks illustrates the CoTFormer's potential to surpass the standard Transformer.

### Weaknesses
1. Possible misuse of technical terms: Chain-of-thought is a prompting technique. The process illustrated by Figure 1 (a) is called auto-regressive, which is orthogonal to CoT. Could the authors clarify how the CoTFormer model architecture model relates to the CoT prompting? Could CoT prompt be applied to CoTFormer model?
2. The model architecture is not clearly explained. Specifically, the meaning of different colors in Figure 1 is vague. Why are there no yellow tokens in Figure 1 (b) and (c)? The figure can be more clear if the caption explains the reason for the absence of yellow tokens and the meaning of different numbers of tokens.
3. Figure 2 shows the inference FLOPs vs. Perplexity. However, it cannot suggest better "scaling properties of CoTFormers" (quote Line 257 of the paper) because scaling properties should be suggested by the training FLOPs vs Perplexity following Kaplan et al.[1]. Could you provide the training FLOPs vs. Perplexity plot for Figure 2?
4. Could you add the standard Transformer to Figure 2?
5. The paper claims that "The growth in computation cost is actually much less noticeable". Could you provide the real measurement of computation cost in terms of memory footprint (Figures 2 and 3 only show FLOPs)?

### Questions
1. Figure 2 shows the inference FLOPs vs. Perplexity. However, it cannot suggest better "scaling properties of CoTFormers" (quote Line 257 of the paper) because scaling properties should be suggested by the training FLOPs vs Perplexity following Kaplan et al.[1]. Could you provide the training FLOPs vs. Perplexity plot for Figure 2?
2. Could you add the standard Transformer to Figure 2?
3. The paper claims that "The growth in computation cost is actually much less noticeable". Could you provide the real measurement of computation cost in terms of memory footprint (Figures 2 and 3 only show FLOPs)? 

**After discussion period, questions were addressed by the authors:

Answer 1: Keep all the other factors constant, the scaling behavior with respect to the training FLOPs still holds.

Answer 2: The accuracy of the standard Transformer in Table 1 can indicate the distance between the CoTFormer and the standard Transformer. Therefore, it is necessary to add the standard Transformer to Figure 2.

Answer 3: Theoretically, the memory footprint is the same for CoTFormer and Block Universal.
 

[1] Kaplan, Jared, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. "Scaling laws for neural language models." *arXiv preprint arXiv:2001.08361* (2020).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents CoTFormer, a novel Transformer architecture that leverages the Chain-of-Thought mechanism to enhance model performance while allowing for budget-adaptive computation at inference. CoTFormer enables intermediate tokens to be accessible, improving accuracy without significantly increasing computational costs. The authors further propose an adaptive training method that dynamically allocates computational resources based on the needs of individual tokens. Empirical results demonstrate that CoTFormer outperforms existing models, such as the Block Universal Transformer, while maintaining a smaller model size.

(Note: Thank the authors for their clarification; that addressed some of my concerns. I've adjusted the score accordingly)

### Strengths
1. The architecture is novel and the authors made smart observations with respect to the CoT can access previous tokens.
2. The problem is very practical and of high interest to the community, especially with limited computation resources
3. The paper is overall well-written and organized.

### Weaknesses
1. The paper could have a more detailed discussion on the scalability of the architecture, with respect to larger models and higher sequence lengths, since the paper discusses that the attention computation is not the bottleneck. Specifically, the paper lacks an analysis of how the proposed CoT mechanism interacts with increased model depth and sequence length. It is unclear if the benefits of CoTFormer would persist or diminish with significantly larger models, and the paper should include experiments or a discussion on the potential challenges.
2. The paper studies the performance of CoTFormer on a particular dataset; would be interesting to see the performance on other datasets. While the chosen dataset is large and generic, it is still important to demonstrate the generalizability of the approach across different types of data. The paper should include experiments on datasets with different characteristics to assess the robustness of CoTFormer.
3. The paper could have benefited from a more thorough theoretical analysis of COTFormer, especially with the number of repeats compared to the block universal transformer. The paper lacks a formal analysis of the computational complexity and convergence properties of the proposed architecture, particularly regarding the number of repeats. A theoretical comparison with the Block Universal Transformer would provide a deeper understanding of the advantages and disadvantages of CoTFormer.

### Questions
1. Is the compute budget a hyperparameter to tune to achieve an optimal balance between accuracy and computation?

### Soundness
2

### Presentation
3

### Contribution
3
