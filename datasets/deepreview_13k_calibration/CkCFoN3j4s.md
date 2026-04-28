# Locret: Enhancing Eviction in Long-Context LLM Inference with Trained Retaining Heads

- Decision: Reject
- Avg Score: 5.80
- Scores: 8, 3, 5, 5, 8

## Abstract
Large language models (LLMs) have shown remarkable advances in supporting long-context comprehension and processing tasks. 
However, scaling the generation inference of LLMs to such long contexts incurs significant additional computation load, and demands a substantial GPU memory footprint to maintain the key-value (KV) cache of transformer-based LLMs. 
Existing KV cache compression methods, such as quantization, face memory bottlenecks as context length increases, while static-sized caches, such as selective eviction, suffer from inefficient policies. 
These limitations restrict deployment on consumer-grade devices like a single Nvidia 4090 GPU. 
To overcome this, we propose \name, an efficient framework for long-context LLM inference that introduces \textit{retaining heads} to evaluate the causal importance of KV cache units, allowing for more accurate eviction within a fixed cache size.
\name~is fine-tuned on top of the frozen backbone LLM using a minimal amount of data from standard long-context SFT datasets. 
During inference, we evict low-importance cache units along with a chunked prefill pattern, significantly reducing peak GPU memory usage.
We conduct an extensive empirical study to evaluate \name, where the experimental
results show that \name~outperforms the recent popular and competitive approaches, including \textsc{InfLLM}, Quantization, \textsc{SirLLM}, and \textsc{MInference}, in terms of memory efficiency and the quality of generated contents --- \name~achieves over a $20\times$ and $8\times$ KV cache compression ratio compared to the full KV cache for \texttt{Phi-3-mini-128K} and \texttt{Llama-3.1-8B-instruct}. 
Additionally, \name~can be combined with other efficient inference methods, such as quantization and token merging.
To the best of our knowledge, \name~is the first framework capable of deploying \texttt{Llama-3.1-8B} or similar models on a single Nvidia 4090 GPU, enabling 128K long-context inference without compromising generation quality, and requiring little additional system optimizations

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes LOCRET, an framework designed to enhance memory efficiency in long-context large language model (LLM) inference by using retaining heads to score and selectively retain key-value (KV) cache units. The primary challenge addressed is the high computational and memory demands posed by long-context LLM inference, which often limits deployment on consumer-grade devices. LOCRET introduces a trained retaining head mechanism that evaluates and prioritizes cache units based on their causal importance, offering a scalable and efficient approach that maintains inference quality on devices such as Nvidia 4090 GPUs. The paper conducts a comprehensive evaluation, comparing LOCRET with various memory-efficient inference baselines, demonstrating notable improvements in memory compression and inference quality without sacrificing speed.

### Strengths
1. The paper presents a framework combining trained retaining heads with chunked prefill, contributing a distinctive approach to KV cache management in long-context inference. Unlike previous methods, LOCRET’s retaining heads learn a heuristic for cache importance, adapting to specific model architectures and sequence types, which provides greater flexibility across transformer-based LLMs.
2. The empirical evaluation is rigorous, with comparisons across a diverse set of baselines, including INFLLM, Quantization, SIRLLM, and MINFERENCE. The experiments cover both long and shorter context scenarios, supporting the paper’s claims of LOCRET’s superiority in maintaining performance while reducing memory usage.
3. LOCRET offers a good solution for deploying long-context LLM inference on consumer-grade hardware by significantly reducing the KV cache size without compromising quality. This contribution is valuable given the rising importance of long-context LLM applications in various fields.
4. The paper is well-organized, providing a clear explanation of LOCRET's architecture, training process, and the underlying intuition behind retaining heads. Diagrams effectively illustrate the framework and its mechanisms, enhancing reader understanding of the complex process of cache unit scoring and selective eviction.

### Weaknesses
1. While the use of retaining heads to score and retain cache units is a valuable idea, the approach may benefit from further differentiation from existing token-dropping and quantization-based methods. Some parts of the scoring approach appear to overlap with traditional token importance estimation techniques (e.g., heavy-hitter approaches). A more comprehensive analysis highlighting LOCRET’s distinctions from similar heuristics in cache management would strengthen the contribution.
2. The results indicate promising efficiency gains but lack granular performance data on how LOCRET’s accuracy scales with different cache budgets across various architectures. Additionally, while the framework shows reduced memory requirements, further evidence on latency and computation trade-offs associated with retaining heads would be beneficial for practitioners evaluating deployment feasibility.
3. Although LOCRET is tested across two LLM architectures, the applicability of this approach to a broader set of LLMs with diverse attention mechanisms (e.g., sparse attention) is not explored in depth. Discussing potential limitations or adjustments required for alternative models would enhance the generalizability of the method.

### Questions
1. Could the authors clarify how LOCRET’s retaining heads would handle extremely high-context lengths (e.g., 10 million tokens)? Would additional constraints or modifications be required to manage the scoring of cache units in such contexts?
2. While SIRLLM performs poorly on memory-demanding tasks, it performs well on comprehension tasks. Could the authors comment on potential reasons LOCRET outperforms SIRLLM in these scenarios, particularly when both approaches manage memory through cache eviction?
3. Could the authors provide further insights or examples where the heuristic scoring might diverge significantly from the true causal importance? This would clarify the potential trade-offs in LOCRET's eviction policy.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
To address the substantial overhead of KV cache in long-context reasoning with large language models, this paper introduces a novel method named LOCERT for KV cache pruning. LOCERT utilizes a more precise pruning metric called the causal importance score (CIS) to preserve the most significant KV cache entries.

### Strengths
- The method proposes a lightweight training-based selective key-value cache eviction paradigm for long-context language model inference, with an offline training cost of less than 1 GPU hour.
- Extensive validation on various datasets confirms the superiority of our proposed method over the baselines discussed in the paper.
- An efficient inference system implementation is provided, integrating a retaining head mechanism into a segmented pre-filling inference framework. It maintains a fixed-size cache set by evicting cache units with low predicted importance, thereby controlling GPU memory usage.
- The paper discusses the inadequacies of existing methods such as KV quantization, which fail to address the overhead caused by linear growth in KV size. Our selection-based KV cache eviction method utilizes a static-sized KV cache and outperforms previous strategies in preserving important KV cache entries.

### Weaknesses
 - The proposed method requires additional training, and although the authors claim it only needs one hour, it also utilizes an eight-card A800 server, which is still resource-intensive.
- The novelty of the proposed method is modest. It is unclear why the training of heads to perform KV cache eviction, predicting each KV's importance, and using the causal importance score (CIS) for pruning, is superior to existing methods like H2O.
- The paper lacks a detailed analysis of the causal importance score (CIS) and needs a deeper discussion to explain why this metric effectively reflects the importance of KV cache.

### Questions
- Regarding the use of a static-sized KV cache in selection-based KV cache eviction methods, can you explain why "the weakening correlation between local and global importance as sequences grow exacerbates this issue"?
- During training, the first loss term merely learns the maximum value of each column in the attention score. How effective would it be to directly use the maximum value of each column as a metric during inference?
- The paper mentions that methods like H2O cannot be effectively combined with KV quantization approaches. What are the actual performances of these methods?
- There are many papers similar to H2O that use attention score statistics for pruning, such as SnapKV and PyramidKV [2]. How does the method proposed in this paper compare with these approaches?
- Is the Stabilizer used only for selecting recent tokens?
- Is the performance improvement in this paper due to the SFT? What would be the effect if SFT were directly applied to the model?
- Should the number of heads in a retaining head be the same as in Query, or should it match Key/Value? If it matches Query, in structures like Grouped-Query Attention where each head's Key/Value corresponds to multiple heads' Query, how did you train this setup?

[1] LLM Knows What You are Looking for Before Generation
[2] Dynamic KV Cache Compression based on Pyramidal Information Funneling

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a training-based KV cache compression framework LOCRET for long-context LLM inference. The framework introduces retaining heads to evaluate the causal importance of KV cache units, allowing for more accurate eviction within a fixed cache size. The proposed framework is evaluated with two LLMs on Nvidia 4090 GPU.

### Strengths
1.	This paper proposes a training-based KV cache compression framework LOCRET for selective KV cache eviction for long-context LLM inference. The proposed framework on two LLMs outperforms related methods on two LLMs and two benchmarks.
2.	The paper is easy to follow.

### Weaknesses
1.	The paper claimed “LOCRET is also applicable to all transformer-based LLMs and various hardware”. However, the proposed method is only evaluated with two LLMs (Phi-3-mini-128K and Llam-3.1-8B-instruct) and one hardware platform (Nvidia 4090 GPU).
2.	The proposed framework is validated with ∞Bench and L-Eval. How is the performance on other long-context benchmarks, such as longBench, et al. ?

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes LOCRET, a novel framework for long-context LLM inference aimed at reducing GPU memory usage through trained retaining heads. Unlike existing static cache eviction methods, LOCRET uses lightweight training to estimate the causal importance of KV units, achieving more accurate cache eviction. The experimental results demonstrate memory efficiency and competitive generation quality with models like Llama-3.1-8B to perform 128K token inference on a single RTX 4090 GPU.

### Strengths
The motivation of the paper is well-articulated, and the experiments are thoughtfully designed. Specifically:

- The claims are strongly supported by comprehensive experimental results. The framework addresses the core issue of KV cache growth through the use of retaining heads, with detailed benchmarks comparing LOCRET against several existing methods.
- The selective eviction strategy, guided by the use of CIS, is convincingly motivated. The experiments are well-structured, thoroughly exploring various datasets, models, and baselines, providing strong evidence of LOCRET’s effectiveness.
- The empirical evaluations comprehensively assess memory usage, inference speed, and performance across a diverse set of tasks. The results are consistently underpinned by sound theoretical analysis. Additionally, LOCRET facilitates long-context inference on GPUs like the Nvidia 4090, significantly enhancing the accessibility of advanced LLMs on consumer-grade hardware.

### Weaknesses
The core idea of this paper is to develop an effective eviction policy through training retaining heads. However, several weaknesses need to be addressed:

- SirLLM is not an appropriate baseline for evaluating token eviction strategies. SirLLM is designed primarily for multi-turn conversations and is not tested on benchmarks like InfiniteBench or L-Eval. A more suitable baseline for eviction-based methods would be SnapKV [1]. Although chunk prefilling may not align perfectly with SnapKV, the authors could still avoid OOM errors and reduce GPU peak memory usage by employing layer-by-layer token dropping during prefilling. The use of chunk prefilling with SnapKV is not a fair comparison, as SnapKV is not designed for this. A more appropriate evaluation would compare SnapKV without chunk prefilling on tasks where memory is not a limiting factor, such as shorter sequences on InfiniteBench or RULER, to accurately assess the effectiveness of the proposed eviction strategy.

- The benchmark suite lacks depth, particularly for information retrieval tasks. The retrieval task within InfiniteBench is overly simplistic, comprising repeated sentences that can be trivially discarded. I recommend that the authors incorporate experiments on RULER [2], following the MInference settings, to provide a more meaningful evaluation of retrieval performance. The current RULER evaluation shows significant performance degradation on complex tasks, even when trained on RULER-specific datasets, indicating a lack of generalizability. The method struggles with tasks involving multiple key-value pairs, suggesting a limitation in its ability to handle complex retrieval scenarios.

- Token eviction based methods may struggle in multi-turn conversation scenarios. For example, in key-value retrieval tasks, if the user queries a different key-value pair during a subsequent turn, the model’s accuracy could degrade significantly due to missing context or prematurely evicted tokens. The current multi-turn evaluation using the Rock-Paper-Scissors benchmark is not sufficiently challenging, as StreamingLLM, a known weak baseline, achieves reasonable performance. A more rigorous evaluation should include tasks where the model must retrieve different keys across multiple turns, such as the multi-key task in RULER, to better assess the method's ability to maintain context across turns. Additionally, the evaluation should include off-topic turns to assess the robustness of the method in realistic conversational settings.

### Questions
- Could you clarify why there is a significant difference in performance between SirLLM and LOCRET in Table 3? If both methods operate under the same KV budget, the latency bottleneck should primarily stem from the attention operation. What factors contribute to LOCRET’s superior performance despite this similarity?
- Why is it necessary to keep the last $n_s$ caches? Could the retaining head detect and manage these recent tokens effectively? Does this indicate that the retaining head’s predictions are not sufficiently accurate for recent tokens, and if so, what improvements could address this limitation?
- How does LOCRET handle noisy datasets, such as conversational data with inconsistent or off-topic turns? Are there cases where retaining incorrect KV pairs causes irreparable errors during generation, and if so, how does the method mitigate such risks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents LOCRET, a framework that enhances long-context large language model (LLM) inference on consumer GPUs. LOCRET introduces "retaining heads," lightweight components added to a frozen LLM backbone to estimate the importance of each key-value (KV) cache unit. LOCRET optimizes cache eviction and reduces GPU memory usage during inference by predicting which cache units are crucial. Combined with chunked prefill, it outperforms methods like InfLLM and SirLLM in memory efficiency and generation quality, enabling models like Llama-3.1-8B to run 128K context inference on a single Nvidia 4090 GPU without performance loss.

### Strengths
Novelty: The introduction of retaining heads for estimating causal importance is a novel approach to KV cache management.
Practical Impact: Enables deployment of large LLMs on consumer-grade GPUs without significant performance loss.
Comprehensive Evaluation: Extensive experiments across multiple datasets and models validate the effectiveness of LOCRET.
Compatibility: LOCRET can be integrated with other efficient inference methods like quantization and token merging.
Lightweight Training: Requires minimal additional training time and resources

### Weaknesses
Clarity of Presentation: The paper contains grammatical errors and unclear notations, hindering understanding.

Theoretical Depth: The theoretical underpinnings, particularly regarding the causal importance score and its properties, could be more thoroughly developed.

Hyperparameter Analysis: Limited discussion on the impact of key hyperparameters (e.g., cache budget, chunk size) on performance.

Limited Discussion of Limitations: The paper does not sufficiently explore potential drawbacks or scenarios where LOCRET may underperform.

Reproducibility: Some essential details for reproducing results are located in the appendix rather than the main text.

### Questions
1. Stabilizer Length: Could the authors provide more insight into how the stabilizer length ns affects performance across different models and datasets? Is there an optimal range for ns?
2. Theoretical Justification: Can the authors elaborate on the causal importance score's theoretical properties and explain how it ensures minimal approximation error during cache eviction?
3. Hyperparameter Sensitivity: Have the authors conducted ablation studies on the cache budget b and chunk size B? How do these parameters impact performance and memory usage?
4. Generalization: It might be out-of-scope, but how well does LOCRET generalize to other transformer architectures, such as encoder-decoder models or those with different attention mechanisms?
5. Limitations: Are there specific tasks or contexts where attention pool-based methods might outperform LOCRET? How does LOCRET handle scenarios with severe context discontinuity?
6. Quantization Methods: You mention KV cache quantization techniques, mentioning the computation overhead as their limitation. Could you compare these techniques, e.g., KVQuant, with sparse attention methods such as FastGen?
7. Combination: You mention the possibility of combining your approach with other efficient inference methods. Could you expand on this with results?

### Soundness
3

### Presentation
2

### Contribution
2
