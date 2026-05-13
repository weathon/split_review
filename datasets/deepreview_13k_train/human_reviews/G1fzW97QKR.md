# Boosting Long-Context LLM Inference Efficiency with Intra-Layer Attention Similarity

- Decision: Reject
- Scores: 5, 8, 3, 3

## Abstract
The increasing context window size in Large Language Models (LLMs), such as the GPT and LLaMA series, has improved their ability to tackle complex, long-text tasks, but at the cost of inference efficiency, particularly regarding memory and computational complexity. Existing methods, including selective token retention and window-based attention, improve efficiency but risk discarding important tokens needed for future text generation. In this paper, we propose an approach that enhances LLM efficiency without token loss by reducing the memory and computational load of less important tokens, rather than discarding them. 
    We address two challenges: 1) investigating the distribution of important tokens in the context, discovering recent tokens are more important than distant tokens in context, and 2) optimizing resources for distant tokens by sharing attention scores across layers. The experiments show that our method saves $35$% KV cache without compromising the performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes POD, a method to improve LLM inference efficiency by differentiating between proximal tokens (recent and initial tokens) and distant tokens. Instead of discarding tokens like previous approaches, POD shares attention scores across layers for distant tokens while keeping full computation for proximal tokens. The authors show their method can save 35% KV cache without significant performance degradation on tasks like LongBench and LEval.

### Strengths
- The work studies an important problem in LLM deployment, as handling long contexts efficiently is becoming increasingly crucial. 
- The method is relatively straightforward to implement and requires minimal adaptation of existing models. As shown in Section 2.2, it mainly involves grouping similar layers and modifying the attention computation, without needing extensive finetuning or architectural changes.

### Weaknesses
 - The paper misses comparison with some important recent baselines, particularly SnapKV [1] and PyramidKV [2], which also address KV cache optimization. While the related work section mentions them briefly, not including them in the experimental comparison makes it difficult to assess the relative advantages of POD.
- The evaluation seems limited in scope given the current state of the field. The authors only test on LLaMA3-8B with 32K context, while recent models routinely handle 128K tokens, e.g., Llama 3.1 and 3.2, Mistral Nemo, Phi 3.5, and so on. This raises questions about how POD would scale to longer contexts and whether the benefits would hold at larger scales.
- Also, the methods were only evaluated on LLaMA3-8B. It is unknown whether the method only works for this specific model or whether the method can be generally applied to most LLMs.
- The implementation details raise concerns about compatibility with modern attention optimizations. The head-wise different grouping of layers (shown in Figure 2) suggests that each attention head would need different attention patterns, which may make it incompatible with efficient implementations like FlashAttention. Have you explored the compatibility of POD with FlashAttention or similar optimized attention implementations?
- The memory savings claims could be better substantiated. While the paper reports 35% KV cache savings, Table 2 shows somewhat inconsistent practical gains across different batch sizes, and there's limited analysis of the overhead introduced by maintaining separate attention patterns per head. Could you clarify the computational overhead of maintaining different attention patterns for each head?

### Questions
See the Weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method to reduce the size of KV cache to improve memory efficiency for long-context LLM. The proposed method involves sharing KV cache for “distant” tokens across layers, and continued pre-training the LM to adapt to this inference paradigm. Experiments are conducted with an extended LLaMA-3-8B model and evaluated on NIAH and two downstream tasks (LongBench and L-Eval). Results show that the proposed method saves 35% of KV cache while retaining performance, compared to previously proposed KV cache eviction method (H2O and StreamingLLM).

### Strengths
* This paper aims to improve efficiency for long-context language models, which is a practical and important problem.
* The paper is written clearly, with comprehensive analysis and experiments.

### Weaknesses
 * **Baseline set-up**: The proposed method involves continuing pre-training the model to adapt to the paradigm of KV cache sharing across layers, yet all of the baselines (StreamingLLM, H2O) except for the “window attention”, are inference-time methods, making the comparison a bit unfair. It would be good to show what is the performance of adopting the proposed method as an inference-time method.
* **Experiment results**: The paper reported performance for all methods in Table 1 but only reported memory footprint of the proposed method (PoD) in table 2. What is the memory footprint saving for the baseline methods (StreamingLLM, etc.), and what is the performance-efficiency trade-off for different methods?

### Questions
The proposed method involves using the attention scores to set the gate for combining the attention output for the distant and proximal tokens. However, FlashAttention does not explicitly write out attention scores during the attention computation. I am curious how this is handled on the implementation side?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes the POD (Proximal over Distant) approach to improve inference efficiency in large language models (LLMs) by optimizing memory and computational resources for distant tokens instead of discarding them. It introduces a strategy of sharing attention scores across layers for distant tokens, based on the observation that proximal tokens (recent and initial tokens) are more crucial. By selectively reusing attention scores in deeper layers for distant tokens, POD achieves a 35% reduction in KV cache without significant performance loss. Extensive experiments demonstrate that POD maintains performance while enhancing efficiency across benchmarks.

### Strengths
The model demonstrates no performance drop with POD, and its speed is improved compared to dense methods.

### Weaknesses
1. The baseline methods for comparison are insufficient. Although the authors mention other acceleration methods in the Related Work section, these were not included in the experimental comparisons.
2. Compared to other training-free acceleration methods, this approach requires a continued training phase, adding computational cost.
3. Although not essential, it remains unclear how this method performs with longer context lengths, such as the 128k length achieved by LLaMA 3.1.

I do not agree with the assumption that middle tokens are less important than edge tokens. This contradicts our prior knowledge, as the model may need to use information from any position during prediction. LM-Infinite and similar works have highlighted this issue, yet this is a limitation of the model rather than an optimization direction. Additionally, many papers achieve full accuracy in "needle-in-a-haystack" experiments, indicating that well-trained long-text models can overcome the "lost in the middle" issue.

### Questions
I do not agree with the assumption that middle tokens are less important than edge tokens. This contradicts our prior knowledge, as the model may need to use information from any position during prediction. LM-Infinite and similar works have highlighted this issue, yet this is a limitation of the model rather than an optimization direction. Additionally, many papers achieve full accuracy in "needle-in-a-haystack" experiments, indicating that well-trained long-text models can overcome the "lost in the middle" issue.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces **POD** (Proximal Over Distant), a method to boost the efficiency of LLM inference with long contexts. 

It addresses the memory and computation bottlenecks of the decoding by leveraging two insights: (1) Proximal Tokens Importance, where initial and recent tokens are more critical than distant tokens, allowing prioritized computation for these tokens; and (2) Intra-Layer Attention Similarity, where attention patterns between consecutive layers are similar, enabling shared attention scores for distant tokens across layers. POD optimizes inference by grouping layers based on this similarity, using shared attention for distant tokens, and minimizing memory usage in KV caching. Experiments show that POD can reduce KV cache memory by 35% while maintaining comparable accuracy to baseline models, effectively optimizing long-context LLMs without compromising on essential token information.

### Strengths
1. The paper creatively combines layer-similarity and post-trianing and proposes a novel approach **POD**, which improves inference efficiency by reducing memory requirements for less important distant tokens through inter-layer attention sharing, achieving a 35% reduction in KV cache while retaining all tokens for performance stability.

2. It provides evaluations across multiple long-context benchmarks and relevant ablation studies. **POD** outperforms baselines in most cases on provided experiments. In addition, the authors described the pipeline and details of **PoD** in a clear way.

### Weaknesses
1. The paper didn't explain the motivation in a reasonable way.

For example, (1) the observation 1 from Figure 1(a) is NOT really valid given the algorithm of StreamingLLM is to evict the tokens except for sink tokens (i.e. initial tokens) and most recent ones. In this case, "A equals B" inserted in the middle will be evicted and thus not used by StreamingLLM, which reasonably fails to return correct answer in the input. (2) The trend of similar attention scores shown in Figure 1(d) might not be immediately obvious to readers.

2. The setup of empirical results of the paper is relatively limited.

For example, (1) the paper only used LLaMA-3-8B model in experiment section, it would be better to how this approach performs when the LLM scales up; (2) the paper should also include some other SOTA token-selection-based approaches such as Quest: https://arxiv.org/abs/2406.10774

3. The training stage of **PoD** may add more computational costs the application of the approach.

### Questions
1. How does the approach apply to larger-scaled and up-to-date models such LLaMA-3-70B and LLaMA-3.1 models? 

2. Does the approach outperform other token-selection-based sparse attention mechanisms other than pure eviction-based baselines?

3. Can authors justify the weakness 1. and elaborate the observation from Figure 1(a)?

### Soundness
2

### Presentation
3

### Contribution
2
