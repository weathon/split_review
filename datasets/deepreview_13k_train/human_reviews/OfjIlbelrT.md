# FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Large language models (LLMs) encounter computational challenges during long-sequence inference, especially in the attention pre-filling phase, where the complexity grows quadratically with the prompt length. Previous efforts to mitigate these challenges have relied on fixed sparse attention patterns or identifying sparse attention patterns based on limited cases. However, these methods lacked the flexibility to efficiently adapt to varying input demands. In this paper, we introduce FlexPrefill, a Flexible sparse Pre-filling mechanism that dynamically adjusts sparse attention patterns and computational budget in real-time to meet the specific requirements of each input and attention head. The flexibility of our method is demonstrated through two key innovations: 1) Query-Aware Sparse Pattern Determination: By measuring Jensen-Shannon divergence, this component adaptively switches between query-specific diverse attention patterns and predefined attention patterns. 2) Cumulative-Attention Based Index Selection: This component dynamically selects query-key indexes to be computed based on different attention patterns, ensuring the sum of attention scores meets a predefined threshold.
FlexPrefill adaptively optimizes the sparse pattern and sparse ratio of each attention head based on the prompt, enhancing efficiency in long-sequence inference tasks. Experimental results show significant improvements in both speed and accuracy over prior methods, providing a more flexible and efficient solution for LLM inference.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a pre-filling mechanism for LLMs, FlexPrefill, which dynamically adjusts sparse attention patterns and computational budget with respect to different input examples. There are two key innovations:
- Question aware sparse pattern determination, which leverage Jensen-Shannon divergence to determine whether an attention head should apply the "question-aware" pattern with respect to the given query. If not, it will apply the "vertical-slash" pattern similar to MInference.
- Cumulative-attention based index selection, which selects the sparse index by ensuring the sum of the normalized attention scores meets a predefined cumulative attention threshold, rather than selecting the sparse index to meet a given budget.

Experimental results indicate that FlexPrefill achieves comparable results with previous SOTA methods with GLM and Yi, and outperforms previous SOTA methods with a large margin with Llama and Qwen.

### Strengths
- The key idea that the complexity of input data varies so we should dynamically adjust sparse attention patterns and computational budget with respect to different input examples is interesting and reasonable.
- Experimental results indicate that FlexPrefill achieves comparable results with previous SOTA methods with GLM and Yi, and outperforms previous SOTA methods with a large margin with Llama and Qwen.

### Weaknesses
1. Figure 8 indicates that only a small portion of attention heads use Query-Aware patterns, whereas the fallback Vertical/Slash pattern is also applied in the baseline method, MInference. Given this observation, further illustration of the original attention patterns and an analysis of why FlexPrefill demonstrates significant performance gains over MInference are necessary.


### Questions
(a) How is the subset of queries $\hat{Q}$ selected for representative query selection in Query-Aware sparse pattern determination and Vertical-Slash head index selection? Is it randomly sampled?

(b) How was Figure 8 generated? Was it based on a specific case study or aggregated over all examples from one of the benchmarks?

(c) In Algorithm 4, the sparse index is selected globally (indicated by the flatten operation). What if perform query-wise index selection?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces FlexPrefill, a novel sparse attention mechanism aimed at improving the efficiency of long-sequence inference for large language models (LLMs). The proposed approach addresses the computational challenges associated with long-sequence processing by dynamically adjusting sparse attention patterns and computational budgets based on input characteristics. FlexPrefill consists of two key components: Query-Aware Sparse Pattern Determination, which selects between diverse and structured attention patterns using Jensen-Shannon divergence, and Cumulative-Attention Based Index Selection, which ensures efficient attention computation by dynamically selecting query-key indices based on attention scores. Experimental results demonstrate  improvements in both speed and accuracy compared to existing methods, such as Streaming LLM and Minference.

### Strengths
1. Originality: The paper presents an adaptive and flexible approach to sparse attention that addresses the limitations of fixed sparse attention mechanisms. The real-time adjustment of sparse attention patterns is a notable advancement in handling varying input needs during long-sequence inference, contributing to the growing body of research focused on optimizing LLM efficiency.

2. Quality: The quality of the experimental setup is high, with comprehensive comparisons to baseline methods like Streaming LLM and Minference. The authors provide detailed analyses that demonstrate improvements in both speed and accuracy, supporting the efficacy of the proposed method. The ablation studies further strengthen the validity of the claims by examining the contributions of each component of the approach.

3. Clarity: The paper is well-structured and clearly written, making it accessible to a broad audience. The authors provide a thorough explanation of the motivation, methodology, and experimental results.

### Weaknesses
1. Complexity of the Proposed Sparse Attention Mechanism: The multi-step decision-making process, involving both Query-Aware Sparse Pattern Determination and Cumulative-Attention Based Index Selection, introduces additional complexity to the attention mechanism. A detailed computational complexity analysis is missing, which raises questions about how the overhead introduced by this process is justified by the computational savings achieved through sparse attention. Specifically, the paper lacks a rigorous breakdown of the time complexity for each step, such as the Jensen-Shannon divergence calculation, sparse pattern selection, and index selection. Without this, it's difficult to assess the practical scalability of the method, especially for extremely long sequences.

2. Lack of Detailed Comparison of Computational Savings: The paper lacks a comprehensive comparison of how much computation is saved by using FlexPrefill compared to the baselines presented in Tables 1 and 2. While the paper mentions speedups, it does not provide a clear quantification of the reduction in floating-point operations (FLOPs) or the actual time taken for attention computation, making it difficult to assess the practical benefits of the proposed approach. A detailed breakdown of the computational costs, including memory access patterns, would be beneficial.

3. Limited Comparison with Recent Related Works: The paper does not include comparisons with other recent related works, such as Han et al. (2024) and Xiao et al. (2024a). Including these comparisons would help to better position the contributions of FlexPrefill within the context of current research. The absence of these comparisons makes it difficult to determine how FlexPrefill compares to the state-of-the-art in sparse attention mechanisms.

4. Mixed Performance Benefits: The reported performance benefits compared to the Full Attention model on long-context benchmarks are mixed, as shown in Tables 1 and 2. Additionally, the computational savings compared to the Full Attention model and other baselines are not adequately reported, which limits the understanding of the trade-offs involved. The paper should provide a more nuanced analysis of the performance-efficiency trade-offs, considering different sequence lengths and model architectures.

### Questions
1. Can you provide a detailed computational complexity analysis on the proposed sparse attention mechanism?

2. Given the complexity of the multi-step decision-making process, how feasible is it to integrate FlexPrefill into existing LLM frameworks without significant modifications?

3. In Figure 4, what is the average attention latency of the Full Attention model?

4. Can you include a comparison of how much computation is saved by using FlexPrefill compared to the baselines in Tables 1 and 2?

5. Have you considered including direct comparisons with other recent related works, such as Han et al. (2024) and Xiao et al. (2024a)? How does FlexPrefill compare to these methods?

6. How were the values of the thresholds (e.g., sparse pattern threshold and cumulative attention threshold) chosen? Were these values empirically determined, or based on specific criteria?

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
This paper addressed the flexibility of the sparse attention pattern to various input length and task currently applied in LLM. The authors split the attention heads into two types: the Query-Aware heads that capture variable sparse pattern upon query, and the Vertical-Slash heads that capture structured and invariant sparse patterns observed in pervious works. The authors decide the sparse pattern for each head by evaluating the discrepancy between the estimated and true attention distribution, and select the sparse pattern by summing up the largest attention scores to a threshold. The proposed method balances the computational efficiency with attention accuracy. The authors evaluate their approach on RULER and Infinite Bench and show that their method preserves high performance across multiple context length and tasks.

### Strengths
- The paper propose a more dynamic and flexible approach for sparse attention calculation. Their method performs sparse pattern search and sparse index selection both in a dynamic, query-aware manner. The flexibility and dynamism distinct it from MInference, and contribute to the performance improvement.
- The method is based on solid observations. 
- The paper gives a concrete and simple algorithm to construct these sparse attention patterns.
- The "Cumulative-Attention Based Index Selection" method is convincing with the details discussed in Appendix A. The authors derive the algorithm from the original  multi-objective optimization problem in details, providing the rationale in summing up the largest attention scores.

### Weaknesses
Methodology:

- **Insufficient Comparison with Baselines**: There are also other sparse attention method in recent works such as SampleAttention [1] and HiP-Attention [2]. The drawbacks of StreamingLLM in handling longer contexts is obvious in other papers, it would be better to compare to other more recent methods. The current baselines do not fully demonstrate the advantages of the proposed method, especially when considering the rapid advancements in sparse attention techniques. A more comprehensive comparison with state-of-the-art methods is needed to solidify the paper's contribution.
- **Insufficient evaluation of latency**: Although "Cumulative-Attention Based Index Selection" improves performance, it may result in unbalanced computation allocation between different attention heads. I think this could lead to an overall increase in latency, as MInference explicitly avoids this by setting a target FLOPs for each pattern. I think it is necessary to show to what extend the dynamic, head-distinctive computation allocation increases the end-to-end latency compared to the fixed budget setting within the same FLOPs. The paper should provide a detailed analysis of the latency overhead introduced by the dynamic allocation of computation, including a breakdown of the time spent on different parts of the attention mechanism.
- **Determination of attention patterns**: The algorithm select the vertical-slash pattern when the distribution of estimated and true attention is not that close. However, in my opinion, the distribution discrepancy only indicates that the result of block-wise sparse attention deviates the full attention, but doesn't lead to using the vertical-slash patterns. Is there any theoretical or empirical guarantee that vertical flash patterns are better than block-wise pattern in this scenario? The rationale for defaulting to vertical-slash patterns when the estimated and true attention distributions diverge is not sufficiently justified. The paper should provide a more rigorous explanation for this choice, including empirical evidence or theoretical analysis to support the claim that vertical-slash patterns are a better fallback in such cases.

Presentation:

- "eacct" -> "exact" in Line 1,043.
- The caption of Table 5 should be above the table.
- In Figure 4, it would be more clear to show the values of $\gamma$ for each point, which will be helpful to provide an empirical selection of $\gamma$. 
- The authors states "accelerating the computational process" in Line 357 but Table 1 does not include any result concerning efficiency. It would be better to give a reference to figure 4 here.

### Questions
- Q1: Figure4 shows the attention latency and performance on RULER. However, this figure is not comprehensive enough. Why there is only one point for MInference? Why not adjust the computation budget of MInference and plot a curve like "Ours"? A curve for "Fixed Budget Query-Aware" is also missing.
- Q2: In Algorithm 4, the attention map is normalized among all the attention scores, but Algorithm 3 only computes the mean values on each vertical and slash lines. The mean operation in Algorithm 3 can not assure the sum of $a_v$ and $a_s$ to be 1, thus the criterion of Algorithm 3 and 4 may be different even with the same $\gamma$. Could the authors explain why there is no normalization in Algorithm 3?
- Q3: in Appendix A, Step 7, the equivalent form of the dual objective is not that intuitive. How can we derive this from the equation in Step 6?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work investigates the LLM long sequence inference efficiency challenge and proposes a novel and flexible method FlexPrefill to solve it. The proposed FlexPrefill featured with two components: Query-Aware Sparse Pattern Determination and Cumulative-Attention Based Index Selection, of which the former one adaptively optimize the usage of the sparse attensions while the latter one ensures the quality of selected sparse attentions. Extensive experiments elaborate the effectiveness and superiority of FlexPrefill.

### Strengths
a) The proposed Query-Aware Sparse Pattern Determination strategy step further on existing work to provide flexibility to sparse attention usage.

b) Promising improvments on extensive experiment compared with SOTA.

### Weaknesses
a) Unclear costs analysis of pre-calculation on JS divergence.

b) The baseline selections are insufficient.



### Questions
a) Could the authors elaborate the intuition behind the usage of JS divergence? Would the W-Distence be more appropriate since W-Distence help measures the change costs of given two attentions? Also, how the JS divergence can help FlexPrefill to be effective and flexible, would it introduce addtional calculation costs?

b) Do the authors have a vision on how the model structure can impact on the performance of FlexPrefill?

c) For the baseline selections, concerns may arise since the FlexPrefill poses an automatic selection process which makes FlexPrefill more flexible while the baselines do have. It would be better to see the comparisons with methods equipped automatic selections such as Moa[1].

d) In formula (2), should the JS distance be the calculation on a||b and b||a given two distributions a, b. Can the authors elaborate the usage of a\hat{-}||m and a\hat{^}||m?


**Reference**

[1] Moa: Mixture of sparse attention for automatic large language model compression.

### Soundness
3

### Presentation
3

### Contribution
3
