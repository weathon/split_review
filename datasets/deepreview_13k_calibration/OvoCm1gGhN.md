# Differential Transformer

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Transformer tends to overallocate attention to irrelevant context. In this work, we introduce Diff Transformer, which amplifies attention to the relevant context while canceling noise. Specifically, the differential attention mechanism calculates attention scores as the difference between two separate softmax attention maps. The subtraction cancels noise, promoting the emergence of sparse attention patterns. Experimental results on language modeling show that Diff Transformer outperforms Transformer in various settings of scaling up model size and training tokens. More intriguingly, it offers notable advantages in practical applications, such as long-context modeling, key information retrieval, hallucination mitigation, in-context learning, and reduction of activation outliers. By being less distracted by irrelevant context, Diff Transformer can mitigate hallucination in question answering and text summarization. For in-context learning, Diff Transformer not only enhances accuracy but is also more robust to order permutation, which was considered as a chronic robustness issue. The results position Diff Transformer as a highly effective and promising architecture for large language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper aims to mitigate the problem in standard softmax attention to over-allocate attention weights to irrelevant context. The proposed Diff Transformer uses the difference between two separate softmax attention scores to cancel noise assigned to irrelevant contextual tokens. Concretely, Diff Transformer first partition the query and key vectors into two groups to compute separate softmax attention scores. The final attention score is the subtraction of the two groups. One learnable parameter $\lambda$ is introduced to balance the two groups of attention scores.

Experiments were conducted on a 3B-parameter model trained on 350B data tokens. Diff Transformer outperforms Transformer on training loss and downstream benchmarks. Ablation studies investigate the importance of the RMSNorm on each attention head.

### Strengths
1. The proposed modification of attention in Diff Transformer is well-motivated

2. The experimental results are strong, with large-scale experiments up to 3B-parameter models and 350B data tokens. 

3. The pre-trained model was evaluated on multiple benchmarks, and also on long-context evaluation, retrieval-oriented tasks, many-shot in-context learning and hallucination evaluation.

4. The paper is well-written, easy to follow.

### Weaknesses
Some design motivation in the model is still not clear:

1. Why the learnable $\lambda$ is re-parameterized in Eq (2)? The current explanation lacks a clear justification for the specific exponential form and the subtraction of two exponential terms. It's not immediately obvious why this parameterization is superior to a simpler, direct parameterization of $\lambda$.

2. Why in Eq (3) there is a term $(1 - \lambda_{init}$ for each head? The explanation provided for aligning gradients with the Transformer is not entirely convincing. While the derivation shows the gradient magnitude is normalized, it does not explain why this specific normalization is necessary or why it is better than other possible normalizations. It's unclear why the gradients of the Diff Transformer would be inherently misaligned without this term.

3. Why the RMSNorm for each head is so important for Diff Transformer stability? The explainable in section 3.8 is unconvincing to me. The explanation that it ensures each token has a moderate magnitude is vague. It does not explain why the differential attention mechanism would lead to such large variance in token magnitudes that require head-wise normalization. The argument about sparse attention is also not well-supported with concrete evidence or analysis.

### Questions
NA

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Differential Transformer, a novel architecture for LLMs that enhances attention to relevant context while canceling out noise. The core innovation is a differential attention mechanism that calculates attention scores as the difference between two softmax attention maps, promoting sparse attention patterns and reducing attention noise. The paper demonstrates through extensive experiments that the DIFF Transformer outperforms the standard Transformer in various aspects, including scaling model size, training tokens, long-context modeling, key information retrieval, hallucination mitigation, in-context learning, and reduction of activation outliers.

### Strengths
1. this is a solid and well-written paper. 
2. while the technique itself is not complex, as far as I know, this is the first work to propose a new architecture using differential attention. 3. the experiments and conclusions in this paper are thorough and insightful.

### Weaknesses
1. the authors mention "promoting the emergence of sparse attention patterns" multiple times on Lines 13, 160, and 539, but do not provide statistics and quantification of the sparsity of attention distribution between DIFF Transformer and the general Transformer. Specifically, the paper lacks a clear definition of what constitutes a 'sparse' attention pattern in this context, making it difficult to assess the claim's validity. The absence of metrics such as the percentage of attention weights below a certain threshold or the Gini coefficient of the attention distribution further weakens this claim.
2. The authors did not discuss or conduct experimental comparisons with work related to the sparse attention. 
For example: 
> Efficient Content-Based Sparse Attention with Routing Transformers
>
> Generating Long Sequences with Sparse Transformers.
It is crucial to contextualize the proposed method within the landscape of existing sparse attention techniques. Without this, it's hard to understand the novelty and advantages of the DIFF Transformer compared to other methods that also aim to reduce computational costs and improve efficiency through sparsity.
3. It would be even better if the effectiveness of the DIFF Transformer could be validated on image or speech modalities. The current evaluation is limited to text-based tasks, and it is unclear whether the benefits of differential attention would generalize to other data modalities with different statistical properties.
4. The absence of a *Related Work* section limits the paper's ability to contextualize its contributions within the broader field. This makes it difficult to assess the novelty of the approach and how it relates to existing attention mechanisms and sparse attention techniques.

### Questions
1. Do both attention calculations in differential attention use RoPE positional encoding?
2. Similar to multi-query attention, can $K_1$, $K_2$, or $Q_1$, $Q_2$ share parameters?
3. Is there a significant difference in sparsity between DiffAttn and regular attention? Does the first term of DiffAttn resemble the pattern of standard attention (implying that the second negative attention term serves to cancel out noise)?
4. What is the calculation formula for Table 3? (Specifically, what is the exact normalization operation?)
5. Please discuss the relationship between differential attention and sparse attention.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new model architecture called Differential Transformer (DIFF Transformer), which reduces noise and more accurately focuses on relevant context through a differential attention mechanism. In a series of language modeling experiments, DIFF Transformer outperforms the standard Transformer across various tasks and model sizes. The paper demonstrates the superiority of this method in long-context modeling, key information retrieval, hallucination mitigation, in-context learning, and reduction of activation outliers.

### Strengths
1.The proposed DIFF Transformer introduces an innovative differential attention mechanism that reduces attention noise through the difference between two independent softmax mappings. This approach performs exceptionally well in long-context processing, making a significant improvement for long-text tasks.
2.DIFF Transformer demonstrates strong performance in language modeling, in-context learning, and multi-needle retrieval tasks, particularly outperforming traditional Transformers in long-context scenarios. It greatly enhances the accuracy and robustness in practical applications like question answering and text summarization, showing broad potential for various use cases.
3.The paper provides extensive experimental validation, confirming DIFF Transformer’s stability across different tasks and model parameter settings. The hyperparameter tuning is thorough, ensuring both robust performance and reliable results.
4.The paper is well-organized, with clear illustrations and analogies that present the differential attention mechanism effectively. Detailed experimental steps make it easy to understand the innovative contributions.

### Weaknesses
While the differential attention mechanism brings notable performance improvements, it also adds computational complexity. Efficiency tests indicate that DIFF Transformer’s throughput, particularly with multi-head normalization and dual softmax calculations, is slightly lower than that of traditional Transformers (by about 5%-12%). Although this impact is relatively minor in the experiments, further exploration of computational efficiency would be valuable if scaling to large-scale applications. Specifically, the paper does not fully explore the trade-offs between the increased computational cost and the performance gains across different sequence lengths and model sizes. The reported 5-12% reduction in throughput could become a more significant bottleneck in very large models or when processing extremely long sequences, which are precisely the scenarios where DIFF Transformer is intended to excel. A more detailed analysis of the computational overhead, including memory usage and latency, would be beneficial.

### Questions
I don't have questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new Transformer variant, called Diff Transformer. The key idea is in the design of attention mechanism, where Diff Transformer uses two softmax attention functions to cancel out potential attention noises. Through a suite of empirical studies, Diff Transformer show promising performances compared to standard Transformer architecture.

### Strengths
- The paper introduces a simple architecture tweak to mitigate the observations that Transformer models tend to incorrectly allocate excessive attentions to irrelevant contexts.
- The paper demonstrates promising empirical results of the proposed architecture through a decent suite of evaluations, ranging from language modeling capability that fits well with scaling law, in-context learning, to improving long-context capability and mitigating contextual hallucination.
- I appreciate that the authors include a variety of downstream tasks to showcase how addressing attention noises in Transformer models can lead to performance improvements.

### Weaknesses
 - Related work can be discussed more thoroughly in the paper. For example, [1] discusses that Transformer models tend to mis-allocate attention to irrelevant contexts potentially biased by their position within the context [1], and [2] also shows LLMs can be easily distracted by irrelevant contexts.
- While the proposed Diff Transformer shows promising performances, they have to be trained from scratch which can be computationally expensive compared to post-training approaches that mitigate attention noises in standard Transformer models, such as the calibration technique used in [1], and improved decoding approaches used in [3] and [4]. Currently, vanilla Transformer is the only baseline considered in the paper. However, I would appreciate if the authors can show how Diff Transformer compares to other more lightweight techniques that fix Transformer's attention noises.
- Apart from pretraineing Diff Transformer, there is no further instruction tuning experiments included in the current paper. I would be interested in seeing whether instruction tuned Diff Transformer also shows better performances than standard instruction tuned Transformers.

### Questions
- Can the authors elaborate further on why we need a fixed multiplier $(1 − \lambda_{init}) $ in Diff Transformer (Eq. 3)?
- In section 3.7, Is absmax quantization the suitable approach to adopt in this context? Why not consider quantization approaches that are robust to activation outliers, such as LLM.int8()?

### Soundness
3

### Presentation
3

### Contribution
3
