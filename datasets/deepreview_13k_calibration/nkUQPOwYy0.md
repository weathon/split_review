# Fast Multipole Attention: A Divide-and-Conquer Attention Mechanism for Long Sequences

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Transformer-based machine learning models have achieved state-of-the-art performance in many areas. However, the quadratic complexity of the self-attention mechanism in Transformer models with respect to the input length hinders the applicability of Transformer-based models to long sequences.
To address this, we present Fast Multipole Attention (FMA), a new attention mechanism that uses a divide-and-conquer strategy to reduce the time and memory complexity of attention for sequences of length $n$ from $\mathcal{O}(n^2)$ to 
$\mathcal{O}(n \log n)$ or $\mathcal{O}(n)$, while retaining a global receptive field. The hierarchical approach groups queries, keys, and values into $\mathcal{O}( \log n)$ levels of resolution, where groups at greater distances are increasingly larger in size and the weights to compute group quantities are learned. As such, the interaction between tokens far from each other is considered in lower resolution in an efficient hierarchical manner. 
A key aspect of our approach is that we \emph{learn} the basis functions that compute group quantities.
The overall complexity of FMA is $\mathcal{O}(n)$ or $\mathcal{O}(n \log n)$, depending on whether the queries are down-sampled or not. This multi-level divide-and-conquer strategy is inspired by fast summation methods from $n$-body physics and the Fast Multipole Method. 
We perform evaluation on autoregressive and bidirectional language modeling tasks and compare our FMA model with other efficient attention variants on medium-size datasets.
We find empirically that the Fast Multipole Transformer performs much better than other efficient transformers in terms of memory size and accuracy. The FMA mechanism has the potential to empower large language models with much greater sequence lengths, taking the full context into account in an efficient, naturally hierarchical manner during training and when generating long sequences.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an attention mechanism with $O(N\log(N))$ complexity where N is the sequence length. In particular, the paper proposes that each query attends to a local neighborhood in full resolution and to points further in the sequence at exponentially lower resolutions. The low resolution tokens are computed using strided convolution. The experiments in the paper compare the described method on autoregressive language modeling on enwik8 and masked language modeling on Wikitext-103, where it outperforms several other efficient attention methods.

### Strengths
The proposed method is conceptually simple and intuitive. In addition, the authors perform controlled testing, namely same exact model with different attention implementations, on real world tasks, autoregressive and masked language modeling. Finally,  the paper is well written with a sufficiently comprehensive review of the related works.

### Weaknesses
The major issue with the paper has to do with the experimental evaluation. Although I appreciate using real world language modeling tasks, there is a major baseline lacking, namely the vanilla transformer. This becomes even more important given that the setup is unusually small with a 6 layer transformer only. For instance, Reformer reports results with 12 layers on enwik8 which are significantly better at 1.19 bits per dimension. How would vanilla transformer and FMA compare at those sizes?

Another quite significant omission is the lack of any ablations. The method has several hyper parameters that change from experiment to experiment. There is absolutely no ablation study to provide some insight on the effect of group size m and the number of levels to the performance as well as the FLOPS and memory required.



### Questions
- How does vanilla transformer perform in the provided experiments?
- How does memory compressed transformer perform in the same experiments? Dividing the computational and memory cost by 3 would be quite enough for the tested sequence lengths.
- Minor, but why would the causal linear attention require more memory than the non-causal version? This seems like a bug in the implementation.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an efficient self-attention, Fast Multipole Attention, by exploring the hierarchial structure of the input to
reduce the complexity of standard self-attention.

Fast Multiple Attention shows comparable performance to efficient Transformer variants on enwik-8 and wikitext-103 with reduced
time and memory complexity.

### Strengths
The motivation to propose efficient attention for reducing memory/computation cost is reasonable and the fast multipole attention scheme is interesting.

Ablation study is conducted to support the efficiency of Fast Multipole Attention.

### Weaknesses
One important baseline is missing, [1], which almost has the same idea that takes the multi-resolution approximation.
I would like to know what is the major difference between fast multipole attention and [1].

Since the idea is so close to [1], I would like to see how it compares with [2] on enwik-8/wikitext-103/GLUE benchmark/Long Range Arena/WikiHop. 

The efficiency comparison with [1] is also needed to show the advantage of fast multipole attention. 

The theoretical analysis is not as sound as [1]. What is the approximation error of fast multipole attention (see Proposition 4.5 in [1].

### Questions
The idea is very similar to [1]. I would like to see a detailed comparison with [1]. Please see the weaknesses above. I will update my score based on the rebuttal.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new efficient self-attention mechanism to reduce the $O(n^2)$ cost to $O(n)$ or $O(n \log n)$ while maintaining a global receptive filed (unlike sparse attention variants). The proposed attention uses a multi-resolution approach. It uses high resolution to approximate the  query’s attention to nearby tokens, low resolution to approximate the attention to distant tokens, and even lower resolution for even farther tokens. The authors evaluated the method on autoregressive and bidirectional language models and found better accuracy and better efficiency compared to some efficient attention baselines.

### Strengths
1. This method built on multi-resolution analysis, which is a powerful but less explored tool for approximation. 

2. Unlike sparse attention variants, due to the use of multiple resolutions, the proposed attention provides a global receptive field to the entire sequence as well as efficiency benefits. 

3. This efficient self-attention supports causal attentions. This is most useful for the recently popular large language models (LLM) since most of them are auto-regressive models.

### Weaknesses
1. Discussion on other efficient attentions that also uses multi-resolutions is limited. For example, MRA attention [1] also provides a multi-resolution approximation of self-attention. Also, since the proposed method is an approximation to the full self-attention matrix, it would be better to compare the approximation quality of the proposed method with other approximation baselines, such as low-rank approximations or methods based on kernel approximations. The current comparison is insufficient without considering these alternatives.

2. Error analysis in 3.6 only analyzes the error between $QK^\top$ and $Q\tilde{K}^\top$, which is too rudimentary. The analysis should quantify how this approximation error propagates through the softmax and value projection, ultimately impacting the final output of the self-attention layer. A more detailed analysis of the error introduced at each stage of the attention mechanism is needed to fully understand the impact of the approximation.

3. Experiments are only performed on 512, 1K, and 2K sequence lengths, which are not very long. Full self-attention also performs efficiently on these sequence lengths (based on my knowledge and the efficiency comparison on Figure 3). The efficiency benefits of efficient attentions are very limited on these sequence lengths. The authors should evaluate the methods on longer sequences, such as 4K, 8K, or 16K, to demonstrate the true advantage of the proposed method for long-range dependencies.

4. No performance comparison to full self-attention on Table 1 and Table 2. Fused full self-attention (such as Flash Attention [2]) is integrated to PyTorch 2. The authors should give a performance and efficiency comparison to the full self-attention, especially with optimized implementations like Flash Attention, to provide a realistic baseline comparison.

5. On efficiency comparison, the batch size is 1, so compute load is small. In this case, kernel launch latency and memory latency might account for a large portion of the overall latency. Custom CUDA kernels usually have some advantages on these latency due to fused operations. It would be more convincing to provide latency for large batch size, such as 32, 64, or 128, to demonstrate scalability and practical efficiency.

### Questions
1. To the best of my knowledge, Linformer, Nystromformer, H-Transformer do not support causal attention, how are auto-regressive language modeling experiments performed on these baselines? 

2. Does this method support KV cache during inference, and will it introduce more overhead? When profiling inference time for Figure 3, is KV cache used?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
