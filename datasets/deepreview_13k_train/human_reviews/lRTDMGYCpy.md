# Identify Critical KV Cache in LLM Inference from an Output Perturbation Perspective

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Large language models have driven numerous paradigm shifts in the field of natural language processing, achieving remarkable success in various real-world applications through scaling model size and leveraging long-sequence context reasoning.
However, the transformer architecture, which relies on self-attention, incurs substantial storage and runtime costs when handling long-sequence inference, particularly due to the generation of extensive Key-Value (KV) cache.
Recent studies aim to mitigate storage and latency issues while maintaining output quality by reducing the KV cache size, through the elimination of less critical entries, yet they rely on a basic empirical intuition of identifying critical cache entries based solely on top attention weights.
In this paper, we present the first formal investigation into the problem of identifying critical KV cache entries from the perspective of attention output perturbation.
By analyzing the output perturbation caused when only critical KV cache entries are used instead of the entire cache, we reveal that, in addition to the commonly used attention weights, the value states within KV entries and the pretrained parameters matrix are also important. Based on this finding, we propose a novel perturbation-constrained selection algorithm to identify critical cache entries by optimizing the worst-case output perturbation.
Extensive evaluations on 16 datasets from Longbench, along with detailed empirical analysis, have comprehensively confirmed the effectiveness of constraining output perturbation perspective in identifying critical KV cache. When combined with state-of-the-art cache eviction methods, it can achieve up to an additional 34\% cache memory savings while maintaining the same generation quality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper optimizes the critical KV selection for existing KV eviction methods during LLM inference. To identify critical KV, this paper uses L1 distance to measure the perturbation of attention outputs w./w.o. KV eviction under certain budgets, and draws the conclusion that both attention weights and value states projected through parameter matrix are important for reducing the output perturbation. It then proposes a perturbation-constrained selection algorithm which adopts top-k sampling to select two sets of KV: one for high attention weights and the other for both the norm of the projected value states and attention weights, respectively. Experimental results show that when integrating this selection algorithm into existing KV eviction methods like SnapKV, AdaKV, the output quality can be improved.

### Strengths
1.	Well-motivated: this paper points out that current KV eviction methods relying solely on attention weights, which is not a proper metric for identifying critical KV. 
2.	Sufficient theoretical analysis: the conclusion aligns with the motivation. 
3.	Good writing: easy to follow.

### Weaknesses
In general, the contributions are incremental, many claims lack supports and the experiments are not sufficient enough. 

1.	Many claims lack further explanation or theoretical supports. For example, why a subset of KV is sufficient for LLM inference? Instead of claiming that it is a commonly accepted assumption from empirical studies, more insights from theoretical perspective are expected since this paper emphasizes its theoretical contributions. 
(1) Why L1 distance is a good metric for measuring the output perturbation? L1 distance is well-known for its sparsity-sensitivity, but the attention outputs are dense. Any further explanation or theoretical supports for this metric? 
(2) What’s the relationship between output perturbation and the generation quality? Perturbation measures the deviation from the original output, but does this deviation have a significant impact on determining the output token? 
(3) Why set alpha to 0.25? The attention weights obey the power-law distribution, but why setting a fixed hyper-parameter is reasonable for any models and input distributions? Deriving this parameter directly from the attention weight distribution seems to be more reasonable.  

2.	The comparison is far from sufficiency, omitting many important baselines. For example, StreamingLLM [1] should be considered since it is an important empirical work. This paper needs this comparison to verify the gains from theorical analysis. Besides, the naïve attention mechanism (without any KV dropping) should also be included. The authors should demonstrate the generation quality gap between eviction methods and the ground-truth.  



### Questions
Justify claims. Add more experiments comparing with baselines.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This research examines KV cache compression by analyzing its impact on output perturbation. The study identifies critical KV cache elements by evaluating their maximum potential effect on output disruption, taking into account both value vector norms and attention score matrices. Through extensive testing across 16 datasets, the proposed methodology demonstrates consistent performance improvements.

### Strengths
1. KV cache compression represents a critical and increasingly relevant challenge in recent literature.
2. The study evaluates three distinct KV cache eviction strategies, each yielding comparable performance improvements.
3. Both the analytical framework and the implemented algorithm are reasonable.

### Weaknesses
This study can be further enhaned by enriching its experiments and empirical analyses (see suggestions & questions for more details).

### Questions
# Writing
On the proposed kv cache eviction algorithm, it would be better to discuss the connection and difference with FastGen [1] and MInference [2] in more details, given the similarity of the resulting algorithm. Also, as to the output perturbation, I feel it would be helpful to discuss the  existing success of this concept's adaptation in other deep learning algorithms (e.g., [3] and [4])

# Analyses
Additional theoretical analysis could strengthen the output perturbation perspective. A key area for investigation is the correlation between worst-case output perturbation predictions and actual perturbation measurements in real-world applications. 

# Experiments
Intuitively, the proposed algorithm applies not only to long-context tasks, but to all generation tasks. However, in the evaluation, only long-context tasks are used for evaluation. I highly suggest the author to evaluate the proposed algorithm in other popular LLM benchmarks (e.g.,  AlpacaEval). This is necessary to understand the performance of the proposed algorithm on a wider spectrum of scenarios. 

1. Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs
2. MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention
3. Understanding the Difficulty of Training Transformers
4. Catformer: Designing Stable Transformers via Sensitivity Analysis

### Soundness
3

### Presentation
3

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
This paper proposes a novel method to identify essential KV cache values based on a perturbation-constrained selection algorithm. Empirical results highlight this approach's performance in small KV budgets against other KV-cache eviction methods.

### Strengths
This paper introduces a novel perturbation-constrained selection algorithm. The criteria underlying the approach are well-motivated and rooted in mathematical principles with proof and derivation. The algorithm’s design is intuitive and straightforward, facilitating easy integration into existing frameworks.

### Weaknesses
While the overall paper is relatively sound, there are some writing and formatting issues I would like to see addressed:

* Section 3.2: In my opinion, this section needs to be reformatted and partially rewritten to be more concise with clearer structure. As the most essential part of the paper, it is currently challenging to read, with many notations introduced ambiguously and references placed somewhat haphazardly.
* Equation Alias: The author should create an alias for $\frac{N \cdot A}{\sum_n N_i A_i}$ to simplify and streamline the equations that reference this expression.
* Assumption 1 and Theorem 3: I believe these should form their own subsection, as they represent the core approach, while the other sections primarily provide proofs and background information.

Additionally, there are several points I still find unclear, and I would appreciate clarification from the authors:

* Assumption 1 Interpretation: I am having difficulty reconciling the assumptions made in Assumption 1 with several statements in the paper:
 
> Lines 17–19: "Yet they rely... attention weights"  

> Lines 60–63: "Although the term... higher attention weights"
 
> Lines 128–129: "However... critical entries"

These statements critique the empirical reliance on attention weights as indicators of importance. Could the authors clarify how they reconcile these criticisms with their own assumption about using attention scores to represent the importance of key-value entries?

* Arbitrary Choice of $\alpha$: I also find that Appendix A does not sufficiently address the arbitrary selection of $\alpha$. Does the model’s performance change with varying $\alpha$, and would such variation impact the conclusions drawn?

* Performance and Budget Constraints: Finally, I feel that the average improvement achieved is often marginal. Moreover, the performance degradation at budget $b$ appears too severe to be practical in real-world settings. Could the authors provide insight on the specific budget value 1024 < $b < 6711$ perhaps (2048, 4096) at which both their approach and other key-value eviction strategies yield comparable performance to the baseline? Additionally, is there a discernible advantage to the proposed method under these conditions?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel method to identify critical KVs in the KVCache for effective KV eviction. Unlike previous methods that solely rely on the attention score, the paper focuses on the attention output perturbation instead. It comes up with a theoretical upper bound for the attention output $L_1$ perturbation to optimize upon. More specifically, the paper proposes to include a small faction of KVs in the critical KVCache to capture the attention score while the rest to capture the derived upper bound term $\sum_{i=1}^n N_i A_i \Vert V_{i, :}\Vert_1$. Empirically, the paper shows that combined with this critical KV identification algorithm, they can consistently outperform the base version of SnapKV, Pyramid, and AdaKV on LongBench and over LLaMA-3.1-8B and Mistral-7B.

### Strengths
1. The KVCache compression problem is indeed well-motivated under the long-context scenario. Conventional approaches usually identify critical KVs based on the heuristic that tokens with a higher attention score are more important. In contrast, this work proposes a novel term derived from the attention output perturbation to capture the importance of different KVs with theoretical guarantees. 

2. The proposed method can be easily integrated into scenarios requiring critical KV identification, such as KV Compression or sparse-attention serving systems. 

3. The additional ablation studies further complement its empirical evaluations and the conclusions that the proposed method can reduce attention output perturbations compared to the heuristics-based approaches.

### Weaknesses
1. The notations and writing for the mathematical derivations are a bit confusing. Specifically, the transition between defining $L$ as the $L_1$ norm of the attention output deviation in Eq. (6) and its subsequent use in Eq. (12) - Eq. (15) is unclear. In these equations, $L$ appears to directly represent the derived upper bound, which seems inconsistent. It would be more accurate to use $L \leq$ or introduce a new variable, say $\theta$, to represent the upper bound, maintaining a clear distinction between the actual deviation and its bound. This affects the clarity of the theoretical foundation of the proposed method.

2. The empirical evaluations are primarily conducted on smaller models, around 7B parameters. While these results are valuable, extending the experiments to larger models, such as those with around 70B parameters, would significantly enhance the paper's impact. Additionally, incorporating needle-in-the-haystack-type tasks could provide a more direct evaluation of the proposed method's ability to identify critical KVs. This is particularly important because in complex, multi-turn reasoning tasks, the KVs evicted based on current criteria might be crucial for subsequent decoding steps, and the current evaluation might not fully capture this aspect.

### Questions
1. In Eq. (6), $L$ is defined to be the $L_1$ norm of the attention output deviation. However, in Eq. (12) - Eq. (15), $L$ directly equals the derived upper bound for the attention output deviation. This is a bit confusing and seems to be a typo to me as the author should either use $L \leq$ or $\theta =$ for the derived upper bounds instead of $L=$ for Eq. (12) - Eq. (15).

2. If I understand Theorem 3 correctly, the author is actually trying to claim $\arg\max_{N}\gamma = \arg\min_{N}\theta$ instead of $\max_{N}\gamma = \min_{N}\theta$, a simple counter-example is when $\sum_i^{n}N_i A_i = 1$ (the selected tokens can capture all the mass), in which case, $\min_{N}\theta=0$ and $\max_{N}\gamma>0$. 

3. The proof of Theorem 3 is not quite straightforward for me. Firstly, the proposed inequality $\sum_i^n N_i A_i > \sum \text{Top}_k (A, b') > 0.5$ is not guaranteed for an arbitrary set of $N_i$ even if we have assumption 1. As we can selectively choose $N_i$ to not include tokens from $\text{Top}_k (A, b')$, in which case this is not guaranteed. Secondly, even if $\sum_i^n N_i A_i > 0.5$ is guaranteed, the derivation of $\arg\max_N \gamma = \arg\min_N \theta$ is not quite straightforward. More specifically, the assumption that 
$(2-1/\sum_i^n N_i A_i)>0$  is not a sufficient condition to derive that $\arg\max_N\gamma = \arg\min_N\theta$. For instance, I can have two sets of $N_i$, the first set has $\sum_i N_i A_i = 0.51$ and the second set has $\sum_i N_i A_i = 0.99$, then I can adversarially set $\Vert V_i\Vert_1$ so that the $\gamma$ corresponds to the first set of $N_i$ is slightly higher than that of the second set of $N_i$. According to your claim, you would choose the first set of $N_i$, which gives you a slightly higher $\gamma$ but way smaller $2-1/\sum_i^n N_i A_i$ in which case $\arg\max_N \gamma \neq \arg\min_N \theta$.  Please correct me if I am wrong on this. 

Suggestions on 3: You might want to move your algorithm description before stating the theorem as I am guessing the proposed inequality $\sum_i^n N_i A_i > \sum \text{Top}_k (A, b') > 0.5$ is based on your algorithm rather than for arbitrary $N_i$. And for theorem 3, if you want to prove the same bound, I would suggest you modify your assumption 1 to be $>0.51$ rather than $>0.5$ then you can lower bound the $2-1/\sum_i^n N_i A_i$ term with $2-\frac{1}{0.51}$ and can further upper bound the current $\theta$ with $\hat{\theta}=C-(2-\frac{1}{0.51}) \gamma$ and reach to the conclusion that $\arg\max_N\gamma = \arg\min_N\hat{\theta}$. 

4. Empirical-wise, if time allows I would be happy to see some results for a larger LLM (e.g., 70B) as well as for some needle-in-the-haystack type of task.

In general, the problem is well-motivated, and the proposed idea with theoretical support is novel. I would be happy to raise the score if the authors can address my concerns during the rebuttal period.

### Soundness
2

### Presentation
2

### Contribution
3
