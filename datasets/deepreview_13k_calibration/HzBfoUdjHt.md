# Dynamic Discriminative Operations for Efficient Generative Inference of LLMs

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 5, 6, 6, 6

## Abstract
Efficient generative inference in Large Language Models (LLMs) is impeded by the growing memory demands of Key-Value (KV) cache, especially for longer sequences. Traditional KV Cache eviction strategies, which discard less critical KV-pairs based on attention scores, often degrade generation quality, leading to issues such as context loss or hallucinations. To address this, we introduce **D**ynamic **D**iscriminative **O**perations ($\mathbf{D_2 O}$), a novel method that optimizes KV cache size dynamically and discriminatively at two levels without fine-tuning, while preserving essential context. At **layer-level**, by observing the varying densities of attention weights between shallow and deep layers, we dynamically determine which layers should avoid excessive eviction via our proposed ***dynamic allocation strategy*** to minimize information loss. At **token-level**, for the eviction strategy in each layer, $\mathbf{D_2 O}$ innovatively incorporates a ***compensation mechanism*** that maintains a similarity threshold to re-discriminate the importance of currently discarded tokens, determining whether they should be recalled and merged with similar tokens. Extensive experiments on various benchmarks and LLM architectures have shown that $\mathbf{D_2 O}$ not only achieves significant memory savings and enhances inference throughput by more than 3$\times$ but also maintains high-quality long-text generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Dynamic Discriminative Operations D2O, an efficient generation method in large language models. D2O uses layer-level to dynamically adjust cache usage and token-level strategies to merge discarded tokens. D2O achieves significant memory savings and improves throughput without sacrificing generation quality, as demonstrated in various benchmarks and LLM architectures.

### Strengths
- D2O takes into account the phenomenon of varying attention score densities across different layers in LLMs, dynamically allocating KV cache budgets for each layer. Additionally, for important discarded tokens, D2O uses a weighted merging approach to retain their information, mitigating information loss during token eviction.
- Compared to various KV cache compression methods, D2O demonstrates consistent superiority across a wide range of benchmarks and different models. With a comparable improvement in throughput, D2O achieves significant performance gains in task execution.
- This paper provides extensive ablation analysis, validating the effectiveness of each component within D2O.

### Weaknesses
 - The Introduction states that "existing methods equally treat all the layers and indiscriminately evict KV pairs at each layer." However, some prior work has already considered allocating different KV cache budgets across layers, such as PyramidInfer[1] and PyramidKV[2]. The allocation method in D2O should be compared with those in previous works, specifically detailing how D2O's dynamic allocation strategy differs from the heuristic approaches used in these prior works, and under what conditions D2O's approach is superior.
- The use of mathematical symbols is confusing. For example, the F representing variance in line 207 is a scalar and should not be in bold, as well as u_ij in line 261. Additionally, the paper should clarify the exact meaning of each symbol when it is first introduced, to ensure clarity and avoid ambiguity.
- The experiment setup is not clear enough. For example, in Section 5.3, the maximum length setting for the LongBench test is mentioned. However, the specific length settings for each dataset within LongBench are not provided, making it difficult to assess the generalizability of the results. Furthermore, the paper should provide more details on the hardware and software configurations used for the experiments, to ensure reproducibility.

### Questions
- As the generation length increases, if a certain KV Cache budget is maintained, the effect of token merging is expected to weaken. Are there any experiments on this?
- The performance testing in the paper separates the benchmarks from the throughput tests. In the LongBench, the prompts are usually long while the outputs are short, so the methods presented in this paper may not save much time on such tasks. Are there more suitable benchmarks where the generated text is longer, allowing for simultaneous evaluation of generation speed and performance?

### Soundness
4

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
This paper proposes D2O, a method for efficient LLM inference through dynamic KV cache optimization. The key contributions include: (1) layer-wise cache allocation based on attention density patterns, and (2) a token-level strategy combining eviction with dynamic merging using EMA threshold. The method achieves 3x throughput improvement while maintaining generation quality across various tasks.

### Strengths
-The paper brings up a major snag in putting LLMs into action, especially the memory requirements of the KV cache during making inferences. This is a crucial issue for real-world applications.

-The authors have conducted extensive experiments across multiple LLM architectures  and tasks, providing a broad evaluation of the method's effectiveness.

 -D2O shows notable improvements in throughput and memory efficiency, achieving up to 3x higher throughput while preserving generation quality, which are important metrics for the deployment of LLMs.

### Weaknesses
-The core ideas (layer-wise allocation and token merging) are largely combinations of existing techniques. The EMA threshold mechanism is straightforward and lacks theoretical justification.The dynamic allocation strategy is similar to existing attention-based pruning methods

-There is insufficient analysis. There is no ablation study on the impact of different attention patterns across layers. There is also limited discussion on why the 3:1 ratio for N:M works best. 

-Regarding experimental concerns, the comparison with baselines is not entirely fair as some methods (like H2O) are designed for different scenarios. There is no discussion on the trade-off between computational overhead and memory savings.

### Questions
-How does the computational overhead of D2O scale with increasing sequence lengths and model sizes?

-What are the trade-offs between the compression ratio and the quality of the generated output?

-How does D2O handle extreme cases, such as sequences longer than 100k tokens?

-Why is the exponential function chosen for the allocation strategy? Have other functions been considered?

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
3

### Summary
This paper focuses on token eviction for large language models and introduces a dynamic allocation strategy at the layer level and a compensation mechanism at the token level.

### Strengths
1. The proposed token eviction mechanisms at both the layer level and token level are well-reasoned and contribute to performance improvements in the models.
2. The effectiveness of the proposed methods is validated across multiple model backbones and long-context benchmarks.

### Weaknesses
1. The experimental comparisons are not comprehensive enough. The authors should compare their method with recent token eviction approaches, such as SnapKV and SirLLM. Additionally, comparisons with token compression techniques like LoCoco would be beneficial.
2. It is suggested that the authors evaluate the performance of their method on benchmarks with longer contexts, such as InfiniteBench and RULER, which consist of instances up to 128K tokens.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores methods for saving the KV cache during inference of large language models. Specifically, the authors investigate ignoring less important tokens in the context during decoding and find that, to prevent excessive performance degradation, the number of tokens discarded should vary across different layers. Additionally, they explore a token compensation mechanism to mitigate the information loss caused by discarding tokens. Experiments demonstrate that their approach accelerates the model while maintaining performance.

### Strengths
* The motivation is clear and saving the KV cache of LLMs during inference is significant.
* This paper deeply investigates the difference in token eviction across layers and explores a reasonable token compensation mechanism.
* The experiments are relatively extensive.

### Weaknesses
 * Some judgments are inaccurate. As noted in lines 181-182: "Employing a uniform eviction strategy such as the ones proposed in H2O...". However, to my knowledge, H2O also adopts a layer-wise token eviction strategy, as evidenced in its open-source code [1].
* The baselines are limited. Exploring the issue of token eviction ratios across different layers is highly meaningful. However, to my knowledge, some relatively classic works in this area, such as PyramidKV [2], were not considered by the authors.
* Some experimental results are quite unusual. In detail,
  * Logically, discarding some tokens would lead to information loss. However, some results in Figure 5 of the paper indicate that, after discarding certain tokens, the performance improves significantly compared to the original model (for instance, on the TruthfulQA task). Is this reasonable?
  * The evaluation results on Longbench differ significantly from those in some previous studies. For example, The results in line 423 of the paper differ by more than **10** points from those in Table 1 of PyramidKV [2] and SnapKV [3]. I believe the authors need to carefully review and revise their findings to provide more reliable results.

### Questions
* In formula (5), $S_\ell$ is the cache size for each layer. However, when calculating $\alpha_\ell$, the number of model layers $L$ is multiplied again. Is this a typographical error?
* In formula (6), I cannot understand the calculation of AttnScore during token generation.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Dynamic Discriminative Operations (D₂O), a method to optimize KV cache management in large language models. At the layer level, D₂O allocates cache sizes dynamically based on attention variance. At the token level, it merges similar tokens and prunes less important ones, preserving essential contextual information. This approach reduces memory usage while improving efficiency and accuracy in long-text generation and inference tasks, outperforming existing cache compression techniques.

### Strengths
1. The proposed method outperforms traditional eviction-based approaches, significantly reducing performance loss in sparse long-text inference.
2. Extensive experimental analysis on hyperparameter selection, various models, and datasets strongly validates the method's effectiveness.
3. The method demonstrates excellent generalizability, as it can be applied to a wide range of existed pretrained models without requiring additional post-training or fine-tuning.

### Weaknesses
The innovation and novelty of the proposed method are somewhat limited compared to existing sparse attention pre-trained models or eviction-based inference approaches. For instance, the concept of token merging has been discussed in several prior works, such as https://openreview.net/pdf?id=LCTmppB165 and https://arxiv.org/html/2407.08454v1. Additionally, the idea of dynamically allocating different computational loads to different layers has also been explored in other works, such as https://arxiv.org/pdf/2404.02258.



### Questions
1. For the Dynamic Allocation Strategy, could it result in a single layer's computational load exceeding that of processing all tokens in a layer? How would this be handled in such cases?
2. In the Dynamic Allocation Strategy, how do you ensure that the computational load is uniform across samples within a batch? Could there be scenarios where some samples in the same batch have significantly higher or lower computational loads, thus reducing inference efficiency? Can this strategy be integrated with existing inference acceleration methods like vLLM?
3. In the Dynamic Allocation Strategy, is there any physical rationale behind the decision to allocate fewer KV caches to layers with high attention score variance?
4. Could the method be compared to a smaller full-size model with similar inference time costs?
5. In Table 9 and Figure 5, D₂O performs better than the full model in some tasks. Could you explain and analyze the reasons for this outcome?
6. In Section A.4, could you provide results for the full model in the multi-turn dialogue examples for comparison?
What are the inference costs in Table 3 for identical batch sizes?
7. Missing citation: https://arxiv.org/pdf/2408.03675 . This paper also focuses on optimizing token eviction methods which introduces a random eviction strategy that retains more token information.

### Soundness
4

### Presentation
3

### Contribution
2
