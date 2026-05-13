# FTP: Efficient Prefilling for Long-Context LLM Inference via FFN Token Pruning

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable performance across various NLP tasks, and have extended their capability to long-context scenarios. However, the increasing context length leads to longer inference time in both the prefilling and decoding stages.
Existing token pruning methods primarily evict tokens to compress the KV cache, and only accelerate the decoding stage.
Recent studies have extended token pruning to both stages, but they either yield subtle speedup during the prefilling stage or defer a portion of computations to the decoding phase. Critically, these approaches prioritize the attention module, overlooking the significant computations in the Feed-Forward Network (FFN) module.

In this work, we focus on the prefilling stage and propose a novel token pruning method named FTP for long-context LLM inference.
Our approach is based on the observation that the FFN module accounts for over 60\% of the inference time. FTP reduces this by pruning non-critical tokens before the inference of FFN. The importance of each token, along with the quantity to be pruned, are dynamically determined by the attention scores in each layer.
Unlike previous token pruning methods, FTP preserves a substantial amount of information of the pruned tokens through the residual connection, thereby achieving a notable speedup with only a negligible decrease in performance.
Specifically, the Qwen2-7B-Instruct model with FTP achieves a speedup of 1.24$\times$ in the prefilling stage with only a 1.30\% performance drop compared to the baseline model. The speedup is further boosted to 1.39$\times$ on a Qwen1.5-32B-Chat model.
Extensive experiments on long-context datasets across various tasks demonstrate the potential and effectiveness of FTP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
1. The paper introduces a method called FFN Token Pruning (FTP) to optimize the inference phase of large language models (LLMs) or long-context processing by selectively pruning tokens during FFN computations.
2. FTP dynamically prunes tokens with low attention weights.
3. FTP achieves faster inference speeds, showing up to a 1.39x improvement on models like Qwen2-7B-Instruct.

### Strengths
1. The method is straightforward and easy to apply.
2. The experiments demonstrate strong performance results.
3. The experimental setup is well-explained and easy to understand.
4. The analysis of experimental results is detailed and thorough.

### Weaknesses
1. FTP involves a considerable computational cost in calculating the Sum Attention Score, but this issue is not discussed by the authors.
2. FTP applies KVCache Eviction (Compression) methods to FFN token pruning without justification or evidence that the Attention Score is also effective for FFN token pruning. Additionally, FTP lacks a specific design tailored to FFN computations.
3. In Figure 5, FTP appears to retain only the beginning and end tokens, discarding most intermediate information. However, previous studies have shown that losing intermediate information can lead to sampling bias and performance loss [1].
4.  Similar research that also performs FFN token pruning, such as MoD [2], is not discussed in the paper. The choice of comparison methods is limited; for example, LongBench compares only with LLMLingua2 and lacks comparison with methods like KVCache Eviction, such as H2O [3] and NACL [1]. When compared with PyramidInfer, the setup lacks fair consistency, as the FlashAttention setting was not standardized.

### Questions
1. Could you explain why the Attention Score is effective for FFN token pruning?
2. Could you discuss the differences between this work and other dynamic layer-skipping methods?
3. Please analyze the eviction effects of FTP and assess whether it may result in a loss of intermediate information.

### Soundness
2

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
4

### Summary
This paper proposes a token pruning method called FTP to accelerate the prefill stage inference of long-context LLMs. The authors first demonstrate the importance of accelerating the prefill stage, noting that it accounts for over 60% of the inference time (it should be noted that this is the case when the number of tokens to be decoded is around 10~20). They identify the FFN module as the most time-consuming component. Based on this, FTP selects non-critical tokens from the input sequence at each layer using attention scores and omits these tokens from the FFN computation. In the experimental section, the authors use results from Longbench to demonstrate that FTP can accelerate the prefill stage while maintaining a certain level of performance.

### Strengths
- The idea of accelerating the prefill stage by pruning tokens in the FFN layer is innovative.
- The paper provides a clear explanation of the motivation and methodology.

### Weaknesses
 - The experimental section is relatively weak: 1) The benchmarks tested are limited, with only Longbench included. It is recommended to add another benchmark, such as BigBench, ZeroScrolls, or L-Eval; 2) The baselines tested are limited, with only PyramidInfer and LLMLingua2 included. The authors should add more baselines or explain why only these two baselines were selected.
- Some parts are not clearly written. For example, in lines 232-236, it is unclear how conclusions 2 and 3 are derived from Figure 5.

### Questions
- Typo: line 267: "and the dataset" should be "dataset".
- If the authors can address the issues raised in the weaknesses section, I would consider increasing the score.

### Soundness
3

### Presentation
2

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
This paper presents a simple and effective token pruning method for FFN called FTP, designed to improve the efficiency of large language models (LLMs) during the prefilling stage of long-context inference. FTP addresses this by dynamically pruning non-critical tokens before FFN inference, using attention scores in each layer to determine token importance and pruning quantity. Unlike previous KV-cache eviction methods focusing on improving the efficiency of the decoding phase, FTP achieves speedups in TTFT with minimal performance loss.

### Strengths
1. This paper well-positioned its focus on the TTFT optimization of long-context LLM inference with a clear presentation of the walltime proportion of the main modules in each decoder layer during prefilling to show its motivation.
2. The FTP is simple and technically sound. Experiments on the LongBench dataset showed its effectiveness in achieving speedups in TTFT with less performance loss than baselines.
3. In the ablation study, FTP is also evaluated on larger models, which could be more practical and adopted for broad use.

### Weaknesses
1. There is a major performance loss on Code Completion Tasks with LLama3 model compared to baselines in Table 2. How the authors explain this phenomenon? This may impact the broader use of FTP and its effectiveness on different models.
2. In Table 2, the average performance of PyramidInfer is higher than FTP. The reported high TTFT for Pyramidinfer is not fair due to the pytorch-implemented attention. In this way, it seems hard to tell the effectiveness and efficiency of FTP compared to Pyramidinfer.


### Questions
1. How do the authors obtain the attention score for token pruning in FTP based on FlashAttention op?
2. Since the number of tokens with high attention scores varies among different layers, how to determine the best reserved ratio for each layer's FFN? Do the increasing number of pivotal tokens in Attention reflect that we should also reserve more tokens for FFN?

### Soundness
3

### Presentation
3

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
The paper introduces a new token pruning techniques at the pre-filling stage (before the autoregressive generative inference starts) for the FFN layer. This is mainly done by looking at the attention scores associated to each token, and keeping top-k tokens. The k is dynamically determined. Some heuristics are also employed  - for example, forcibly keeping first few and last few tokens from the original input and starting pruning only after the first few layers are executed. Performance in terms of accuracy and time taken till first token generation is shown in longBench.

### Strengths
1. The method is straightforward and elegant.
2. Offers a reasonable speedup while mostly maintaining the original performance.

### Weaknesses
1. No discussion about memory impact. Does this method reduces memory or keeps them the same? If there is a reduction - then by how much? Many of the prior methods are also motivated in terms of memory reduction.

1. Weak literature review. There are many works on token pruning outside LLM ([1,2,3] - just to name a few, but this is still a very incomplete list. More can be found by browsing the citation network). I found some of the contrasting against prior works as unsatisfactory. Overall, presentation can be more polished.

1. The overall trade-off (accuracy loss vs speedup) feels a bit lukewarm. The speedup is only (~1.2x-1.4x depending on model size), and in most contexts it may not seem worth it for the accuracy loss - although that's a matter of specific use case. While accuracy loss is bearable in most contexts, sometimes it can be high like about 20% drop by Llama for code-completion.

1. I am not sure how fair the comparison between PyramidInfer vs author's methods given the former doesn't have flash-attention and the latter do. Is PyramidInfer simply not implemented with flash-attention officially or can it be not implemented in principle? If it can be implemented in principle, then the only reason it would be currently facing a disadvantage seems to be due to lacking the relevant implementation. In that case, could have been better to make a more apples-to-apples comparison even if that means using pytorch-attention for all (a separate table can be used for pytoch-attention based results).

1. More benchmarks could have been attempted besides just the LongBench suite but not the biggest issue.

### Questions
1. There is a lot of repeated information in the tables. It seems to me that Table 1,2,4 can be the same table with all the approaches . Just consistently show TTFT (ms), and put all the non-large models (< 70B) there (the larger models are fine on a different table). 

1. The random baseline is better framed as an ablation.

1. The graph in Figure 7 seems uninterpretable if I am not missing anything. According to the text, it is supposed to show how speedup and accuracy varies with the $\eta$; but nothing the graph tells us which dot is associated with what $\eta$  or compression rates  for the other model.

1. "Unlike previous token pruning methods (Xiao et al., 2024; Li et al., 2024; Zhang et al., 2023b; Yang
et al., 2024b) where tokens are directly pruned from the whole layer, FTP dynamically selects a
certain proportion of tokens with an attention-based strategy and prunes them before the inference
of FFN." - This distinction is not sharp enough. Dynamic selection of certain proportion of tokens before FFN layers, is also direct pruning (by dynamic selection) from the whole (FFN) layers. So it's not explicitly said what the difference is. Perhaps you want to say that previously works applied token pruning to both attention + FFN, or that they apply permanent pruning (pruned in one layer => pruned in all later layers) and so on. But you need to be more explicit and sharp. . 

Review Caveat: I am not as familiar with modern works on LLMs for token pruning and not entirely sure where this method stands and if the best baselines have been chosen.

### Soundness
3

### Presentation
2

### Contribution
3
