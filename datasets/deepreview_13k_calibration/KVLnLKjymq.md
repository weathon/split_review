# Star Attention: Efficient LLM Inference over Long Sequences

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Inference with Transformer-based Large Language Models (LLMs) on long sequences is both costly and slow due to the quadratic complexity of the self-attention mechanism. We introduce Star Attention, a two-phase block-sparse approximation that improves computational efficiency by sharding attention across multiple hosts while minimizing communication overhead. In the first phase, the context is processed using blockwise-local attention across hosts, in parallel. In the second phase, query and response tokens attend to all prior cached tokens through sequence-global attention. Star Attention integrates seamlessly with most Transformer-based LLMs trained with global attention, reducing memory requirements and inference time by up to 11x while preserving 95-100\% of accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces star attention, a two-phase inference techniques to handle long sequences efficiently.

The author find that pure blockwise context encoding can bring attention spike in the attention scores , and propose "anchor blocks" to address this issue in stage 1, by attach the first block (the "anchor block") to the begining of each sub-block and conduct the encoding, which shift the attention spike to the "anchor block", and only use the encoded sub-block part for inference. In stage 2, the author combine the online softmax technique to make full use of query and previous encoded sequence for token generation.

The author conduct experiment on long-context benchmarks like RULER-NIAH using Llama family models, and do the abliation study on anchor blocks, learn effect of its position, content and size.

### Strengths
- This paper propose a interesting solution "anchor block" for breaking the dependencey of long-sequence to enable process in parallel.
- The ablation study is sufficient and present details effect of "anchor block" from different dimision.

### Weaknesses
 - Given the technical depth of the proposed method, the experiment result is not strong enough. In Table 1,  the improvement that the star attention can bring is marginal. While In Table 2, the propsoed method is hard able to achieve significant speed up without sacrifiing a huge amount of performance, especially on super long sequence.
- The experimental result may not solid. Combine Table1 and Table2, I notice that Llama-3.1-70B shows clear poor performence comparing to Llama-3.1-8B on both base and instruct version. This observation makes me questionable on the experiment set up and impelmentation.
- There presentation is not complete. For example, Figure 3 left is missing the data point on 32K lenght block, which make it inconsistent to the Figure 3 right. This may due to the seq-lenght limitation of 64K, the author should switch the setting from 64K to 256K to make the figure full-fill. also,Figure 3 type error "instruct global att".

### Questions
Follwing the discussion of the weakness part, I have following questions:
1. Why llama3-8B perform much better than llama3-70B on RULER-NIAH in both base and instruct version?
2. How to measure the "speed up"? it is unclear about the which time is used for comparsion, the time to generate the first token or the time to finish the response.
3. Why the star attention clearly outperform the global one in BABLONG and clearly underperform in RULER-NIAH at the same time?

### Soundness
2

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
4

### Summary
The paper presents Star Attention, a two stage approach to reduce the inference time of long context Transformers. It achieves 11x speed up with 95%-100% the performance.

### Strengths
1. The paper method is simple and clear.
2. The experiments are well motivated and provide decent ablations.

### Weaknesses
The main experiment is conducted mainly to RingAttention, an exact attention mechanism. In the reviewer opinion, the  experiments should also cover the following dimensions:

(1) Other sparse attention methods, e.g. H2o.
(2) exact attention system: there are other systems than RingAttention that is faster, e.g. DistFlashAttn.

### Questions
Please address the weakness section. Thanks!

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes star attention, which is based on an assumption "global attention is not necessary during context processing". It breaks the long context into multiple segments, prepend the first block with all other blocks, doing local attention. Then it replicates the queries and compute attention between query and each block. Finally, it sums up all block-wise attention to generate outputs. The method is evaluated with one synthetic benchmark and compare with only one baseline Ring Attention.

### Strengths
1. The proposed method is easy to understand.

2. The long-text LLM is an important research problem nowadays.

### Weaknesses
1. Lack of baselines and related work. Transformer for long context is an active area. But this paper does not have a related work section to discuss many related work in this area. Can authors justify why the baseline only includes Ring Attention, any many other related methods (e.g., StreamingLLM, Longformer, Reformer, Unlimiformer, are not included in the baselines or discussed in the paper? The papers i list here might already be out-dated, but there definitely are a lot more papers in the last two years. 

2. Only one synthetic benchmark is used in the experiment. I think Ruler is a good benchmark, but it is fully synthetic. The proposed method is based on that "global attention is not necessary in context processing", so I think it is important to evaluate the proposed method on real-world data (e.g., InfiniteBench and Bamboo).

3. The accuracy reported in Table 1 and Table 2 seem to be contradictory. In Table 1, the conclusion is the proposed method can maintain 95-100% accuracy. However in Table 2, the delta could be more than 10%. What is the delta in Table 2? If delta is the relative error, then ithe accuracy of Table 2 seems to be a lot worse than the accuracy in Table 1. (e.g., 95 * 90% =85.5).

4. The proposed method cannot be applied to cases where the LLM needs to generate a lot of  tokens (e.g., writing a paper). Though it is not a serious issue, it limits the application and contribution of the proposed method.

### Questions
See weakness above.

### Soundness
2

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
The paper introduces Star Attention, an approach designed to enhance the efficiency of large language models (LLMs) in processing extremely long input sequences. This method mitigates the high computational costs associated with traditional global self-attention by optimizing the prefill stage of inference: it employs a local attention mechanism with "anchor" blocks to capture core context across segmented portions of the input. Experimental results show that Star Attention improves inference efficiency while maintaining accuracy levels similar to those of full attention. Further, the paper conducts comprehensive evaluations to validate the rationale and underlying principles of the proposed method.

### Strengths
1. This paper provides an in-depth analysis of the "attention sink", presenting a new perspective on it and exploring the underlying causes of this effect.
2. This paper presents a concise and effective approach to accelerate long-sequence processing in LLMs, improving operational efficiency with limited accuracy degradation.
3. This paper provides ablation studies to validate the rationale and potential principles underlying the proposed method.
4. This paper is well-written and well-organized.

### Weaknesses
1.  The evaluation section of this paper includes only a few baseline methods. Aside from the global attention used in Ring Attention, no comparisons on accuracy and efficiency were made with other relevant parallel global context computation or attention approximation methods, such as Flash Attention, sliding window attention, or sparse attention. The lack of these comparisons makes it difficult to assess the true performance gains of Star Attention relative to the broader landscape of existing techniques. Specifically, the paper does not explore how Star Attention performs against methods that also aim to reduce computational costs of long sequence processing, which is a crucial aspect for evaluating its practical utility.
2.  In Table 2, for the Gradient-AI Llama3-8B-Instruct-1024K at sequence lengths of 512K and 1024K, and the Meta Llama-3.1-70B-Instruct at a sequence length of 128K, an accuracy drop of over 10% can be observed. The paper lacks a more detailed experimental analysis of these scenarios. It is unclear if this accuracy drop is due to the specific model architecture, sequence length, or some other factor. The paper should provide a more thorough investigation into the causes of this significant performance degradation, including analysis of the attention patterns and how they change with increasing sequence length.

### Questions
1. I suggest the authors considered compare Star Attention's accuracy and efficiency with other related works. Such comparisons could provide a more comprehensive understanding of Star Attention’s performance relative to existing methods.
2. In cases with longer sequences or larger models, accuracy degradation becomes more pronounced. Have you tried any approaches to mitigate this issue, such as increasing the block size directly? Or is it acceptable?

### Soundness
3

### Presentation
3

### Contribution
3
