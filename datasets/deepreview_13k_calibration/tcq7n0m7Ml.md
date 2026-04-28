# EMS: Adaptive Evict-then-Merge Strategy for Head-wise KV Cache Compression Based on Global-Local Importance

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 3, 5, 5

## Abstract
As large language models (LLMs) continue to advance, the demand for higher quality and faster processing of long contexts across various applications is growing. 
KV cache is widely adopted as it stores previously generated key and value tokens, effectively reducing redundant computations during inference. 
However, as memory overhead becomes a significant concern, efficient compression of KV cache has gained increasing attention. 
Most existing methods perform compression from two perspectives: identifying important tokens and designing compression strategies. 
However, these approaches often produce biased distributions of important tokens due to the influence of accumulated attention scores or positional encoding. 
Furthermore, they overlook the sparsity and redundancy across different heads, which leads to difficulties in preserving the most effective information at the head level. 
To this end, we propose EMS to overcome these limitations, while achieving better KV cache compression under extreme compression ratios. 
Specifically, we introduce a Global-Local score that combines accumulated attention scores from both global and local KV tokens to better identify the token importance. 
For the compression strategy, we design an adaptive and unified Evict-then-Merge framework that accounts for the sparsity and redundancy of KV tokens across different heads. 
Additionally, we implement the head-wise parallel compression through a zero-class mechanism to enhance efficiency. 
Extensive experiments demonstrate our SOTA performance even under extreme compression ratios. 
EMS consistently achieves the lowest perplexity, improves scores by over 1.28 points across four LLMs on LongBench under a 256 cache budget, and preserves 95\% retrieval accuracy with a cache budget less than 2\% of the context length in the Needle-in-a-Haystack task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an adaptive Evict-Then-Merge Strategy (EMS) for efficient key-value (KV) cache compression. EMS utilizes a combined global-local scoring mechanism that tracks attention accumulation both across the entire model (global) and within individual layers (local) to rank and identify essential tokens. To meet the target compression budget, EMS first evicts tokens deemed irrelevant based on these criteria. It then merges the remaining tokens based on similarity; if tokens are too dissimilar, they are merged with a zero token. Empirical results with a budget of 256 demonstrate EMS’s superior performance in LongBench compared to other state-of-the-art (SoTA) methods.

### Strengths
The paper proposed EMS, which incorporates global and local attention to determine the token's importance for the KV cache, is a good idea. The strategy used to evict and merge tokens is unique, and under the proposed budget of 256 tokens, EMS performs well in LongBench.

### Weaknesses
I have several comments and questions that I hope the authors can clarify:

1. Memory Management: Could the authors confirm my understanding? It appears that EMS operates on a per-head basis, with each head tracking its own $s_{GLo}$ and $s_{Loc}$ statistics. If this is correct, then values such as $N_{tbm}$, $N_{irr}$, and $N_{imp}$ are non-uniform across all heads, meaning the KV cache would need to exceed the target budget to support this irregular pattern and maintain data contiguity. How was this challenge addressed?

2. Throughput: Due to the irregular pattern, EMS employs “shared entry expansion” to enable matrix vectorization. However, there is a non-zero probability that shared entries could expand to the full context length, yet this potential has not been discussed. Could the authors elaborate on how they handle or mitigate this? Furthermore, the overhead of managing these shared entries, including the look-up tables and expansion logic, could introduce significant latency, which needs to be quantified.

3. Efficiency Analysis: Given that EMS is dynamic, there’s a non-zero probability of memory spikes due to irregular patterns, particularly in scenarios where few tokens overlap across heads. This variability could impact efficiency, making the analysis in Section 5.4 potentially misleading. The analysis should include a detailed breakdown of memory usage across different heads and layers, including the overhead of the scoring mechanism and expansion process. Could the authors clarify how they accounted for this in their analysis?

4. Budget Restriction: I am curious about the decision to restrict the budget to 256 in LongBench. How was this value determined? Typically, we set the budget to the minimum level that maintains performance parity with a full cache, yet I didn’t find a discussion on the rationale behind this choice. It would be beneficial to see a more comprehensive analysis of performance across different budget levels to understand the trade-offs and limitations of EMS.

### Questions
see weaknesses

### Soundness
3

### Presentation
2

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
The paper explores efficient KV cache compression for large language models (LLMs) to handle long sequences. It introduces EMS, an Evict-then-Merge Strategy, which uses a Global-Local score to select important tokens, balancing global and local importance. This approach addresses biases from attention weights and positional encoding. EMS compresses the KV cache by first evicting irrelevant tokens, then merging less important ones into class centers. This head-wise method adapts the compression ratio per head, enhancing storage density while preserving model performance.

### Strengths
1) A balanced Global-Local score for token selection, reducing bias.
2) A head-wise Evict-then-Merge strategy based on sparsity and redundancy.
3) Efficient parallel compression using a zero-class center for merging.

### Weaknesses
1) Please quantify the computation time for calculating global scores and local scores and runtime comparisons between your method and alternatives for different sequence lengths, and determine if you have explored any approximation techniques to reduce this overhead for ultra-long sequences
2) Please quantify the additional computational costs of real-time merging.
3) More experiments are needed: ablation studies varying the relative weights of global and local scores, and performance comparisons across different types of tasks or model sizes.

### Questions
1) What are the benefits of doing mean-alignment for sGlo and sLoc?
2) Line 369-371: what are the specific operations of using and not using position information?
3) It's not clearly explained how to distinguish the three categories of KV cache.

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
4

### Summary
The study proposes a new KV cache compression method, called EMS, in which there are 2 levels of compression. In the first stage, the proposed method evict unimportant tokens based on the proposed KV importance estimation method called Global-Local Score. The Global-Local Score is claimed to consider the importance of the token comprehensively, without biasing toward either previous or recent token, resulting in a more uniform selection of KV cache to retain. In the second stage, the proposed method perform Evict-the-Merge operation based on the measured sparsity and redundancy of KV cache among different heads.The conducted experiment shows the performance of the proposed method is better than other baselines, even under resource-intensive scenarios.

### Strengths
- The observation on KV similarity is interesting.

### Weaknesses
1. I'm not quite convinced with the redundancy estimation part, but maybe I misunderstood some parts here. What if both K & V of two tokens are highly dissimilar, i.e. cos_sim(K_x,K_y) = -1 and cos_sim(V_x,V_y) = -1, their product is now 1, which is deemed as redundancy by the proposed method. However, I believe this situation is not redundant at all since both K & V are highly dissimilar so we should keep both of them. Can the author clarify this to ease my concern?
2. The study only experimented on KV cache size = 256. However, I believe it would be more beneficial to see the proposed method's performance under different cache sizes. Can the authors provide more result regarding to this?
3. The "expansion" part in Evict-then-Merge plays an important role to implement the framework, but is not elaborated in the main text (or briefly in the appendix). Can the author elaborate on why and how we should do this expansion?
4. Can the authors make sure that the experiment pipeline is correct? For example, in [1] [2], the performance of Mistral full KV on MF-en, HotpotQA, 2Wiki, SAMSum are all around 49.34, 42.77, 27.35, 42.96 respective. However, in the submission's reported numbers, they are 29.62, 36.42, 21.77, 71.00 respectively, which are off by a large margin. I am doubting the experiment pipeline the authors used. 
5. There are many variations of NIAH tasks, e.g. haystack formed from repetitive sentences or haystack formed from a long corpus. Can the authors elaborate which setting used in the study?

### Questions
Please see weaknesses.

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
5

### Summary
The proposed EMS includes:
1. the Global-Local score is designed for important token selection;
2. Evict-then-Merge compression strategy is designed;
3. an efficient head-wise parallel compression is designed for the KV cache.

EMS achieves extreme compression, retaining 95% retrieval accuracy using under 2% of the context length in the Needle-in-a-Haystack task.

### Strengths
The combination of local and global method is used in EMS, which compress the KV cache with a high compression rate and preserve the major context information.

### Weaknesses
The EMS depends on the online calculation of attention score and dynamic sparsity, leading to a high cost for practical deployment. And some sub-methods are similar to streamingLLM and H2O.

### Questions
We should explore the essential mechanism of the combination of local and global attention.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a head-wise adaptive strategy with a similarity-based merge method and a global-local scoring mechanism to improve KV cache compression performance under extreme compression ratios.

### Strengths
The authors propose joint optimization strategies in three directions to improve cache compression.

### Weaknesses
1. Evaluation is conducted only under a budget of 256, which is insufficient to account for data fluctuations. The method should be evaluated across a range of budgets (e.g., 128, 256, 512) to provide robust conclusions. Results for varying budgets in Table 5 lack sufficient validity without baseline comparisons, as all cache compression methods approach the full cache baseline with increased budgets. Including comparisons with baselines under different budget conditions would be more convincing.
2. More details regarding how the baseline value of 31.43 was derived in ablation study should be provided, especially since this value is not referenced in Table 1. Additionally, more ablation results, such as comparisons under different budget settings and using varied models, should be provided to ensure a comprehensive evaluation.
3. Results deviate significantly from prior work under full cache conditions, which may indicate potential issues in the experimental setup or implementation. On the synthetic PRe dataset, all models score close to 0 in this paper, while prior works [1-2] reported scores of 86.98 and 89.3 for Mistral-7B, and both 30.5 for LongChat-7B. A thorough investigation into these discrepancies is recommended
4. The authors propose head-wise adaptivity, similarity based cache merging, and a refined attention score for enhancing cache compression. However, some works exist for each of these aspects[3-5]. The authors should clarify differences from existing research. 
5. Given FlashAttention has become a standard technique for long sequence inference, using a global score may not be practical due to the additional quadratic computation and storage overhead needed to recompute global attention weights. In contrast, the local score only reconstructs attention weights for recent tokens, avoiding this burden. Thus, a global score should only be used if it delivers significant benefits; otherwise, the local score is more practical.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1
