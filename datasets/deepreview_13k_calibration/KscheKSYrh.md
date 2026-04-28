# FreqKV: Frequency Domain Key-Value Compression for Efficient Context Window Extension

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 5, 5, 8, 6

## Abstract
Extending the context window in large language models (LLMs) is essential for applications involving long-form content generation. However, the quadratic complexity of self-attention and the linear increase in key-value (KV) cache memory requirements with respect to sequence length present significant challenges during fine-tuning and inference. Although LongLoRA achieves efficient fine-tuning by employing shifted sparse attention, inference remains inefficient due to the requirement for dense global attention.
In this work, we introduce a novel context extension method that optimizes both fine-tuning and inference efficiency. Our method exploits a key observation: in the frequency domain, the energy distribution of the KV cache is primarily concentrated in low-frequency components. By filtering out the high-frequency components, the KV cache can be effectively compressed with minimal information loss. Building on this insight, we propose an efficient compression technique, FreqKV, that iteratively reduces the increasing KV cache to a fixed size in the frequency domain, applicable to both fine-tuning and inference. With minimal fine-tuning, LLMs can learn to leverage the limited cache that is compressed in the frequency domain and extend the context window efficiently.
FreqKV introduces no additional parameters or architectural modifications, ensuring compatibility with the original full attention post-training.
Experiments on long context language modeling and understanding demonstrate the efficiency and efficacy of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents FreqKV, a method to extend the context window for large language models (LLMs) by compressing key-value (KV) caches in the frequency domain. The core premise is that the energy distribution of the KV cache concentrates primarily on low-frequency components, allowing high-frequency elements to be discarded without significant information loss. This iterative compression method, applied when the cache reaches a predefined limit, aims to maintain efficient inference without introducing new parameters or modifying the LLM's architecture. The authors claim that FreqKV offers improved memory and computational efficiency in long context tasks.

### Strengths
- Novel Approach: The use of frequency domain compression for KV cache management in LLMs is an innovative concept, particularly given the need for extended context handling in generative models.
- Parameter Efficiency: FreqKV avoids adding parameters or modifying the model architecture, making it potentially applicable to existing LLMs without extensive retraining.
- Empirical Validation: Results show comparable perplexity with full KV cache methods, suggesting that FreqKV achieves reasonable performance with reduced memory and computational overhead.
- Benchmark Evaluation: Extensive testing on long context language modeling and understanding tasks provides a solid empirical basis for evaluating FreqKV’s effectiveness.

### Weaknesses
 - Unclear Decompression Process: The method relies on iterative decompression via the inverse discrete cosine transform (IDCT) to restore KV states for attention computation. This raises concerns about the increased memory and computation needed to reconstitute the full KV tokens, potentially nullifying the benefits of compression. The paper lacks a detailed explanation of how the compressed KV cache is utilized during the attention mechanism. Specifically, it's unclear whether the full KV cache is reconstructed before each attention calculation or if a compressed representation is used directly, and if so, how this impacts the attention computation itself. The absence of a clear description of this process makes it difficult to assess the true computational cost and memory savings.
- Inadequate Justification of Training Requirement: Despite the focus on compression, the paper does not provide clear reasoning for additional training. If FreqKV merely discards high-frequency components, the rationale behind training to learn this transformation remains ambiguous. The paper does not explain why the model would need to be trained to handle the compressed KV states, especially if the compression is a simple frequency-based truncation. The lack of a clear explanation for the training requirement raises questions about the necessity of this step and its potential impact on the model's generalization capabilities.
- Lack of Discussion on Compression Overhead: The authors overlook a discussion on compression/decompression overheads, which could be significant if IDCT operations occur during inference. The efficiency claims are therefore weakened by the omission of such an analysis. The paper does not provide a detailed analysis of the computational cost associated with the DCT and IDCT operations, which are essential components of the compression and decompression process. The absence of this analysis makes it difficult to evaluate the overall efficiency of the proposed method, particularly when considering the potential overhead introduced by these transformations.
- Ambiguous Memory Savings: In Figure 3, the reported savings from FreqKV are challenging to interpret, given that the KV cache still requires reconstruction for each attention computation. The lack of explicit comparisons with non-compression methods or details on the computational trade-offs reduces the clarity of the benefits. The paper does not clearly articulate how the compressed KV cache translates to actual memory savings during inference. The need to reconstruct the full KV cache for attention calculation raises questions about the practical memory benefits, especially when compared to methods that do not involve compression and decompression.

### Questions
- Does decompression occur on-the-fly during inference? If so, the authors should clarify the associated computational and memory overhead of IDCT operations.
- Why is training required for FreqKV? Given that the method primarily involves discarding high-frequency components, it remains unclear why additional training would be necessary.
- How is memory efficiency maintained when reconstructing the full KV tokens? The need to reconstitute compressed contexts for attention suggests a potential bottleneck that could negate the claimed memory savings.
- What is the impact of different retaining ratios on inference time and accuracy? Further insight into how varying the retaining ratio affects both performance and efficiency would improve the comprehensiveness of the evaluation.

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
The authors introduce "FreqKV: Frequency Domain Key-Value Compression for Efficient Context Window Extension," a novel approach aimed at reducing the computational and memory demands associated with the KV-cache in large language models (LLMs) during both training and inference. This method uses a frequency-domain compression technique that retains only the low-frequency components of the KV cache, with the goal of optimizing memory usage and computational complexity for extended context windows.

### Strengths
1) Problem importance: FreqKV addresses the critical problem of context window extension in LLMs, specifically targeting issues of performance degradation, high computational complexity, and excessive memory consumption as context length increases which is an important challenge for enabling LLMs to handle long-form content efficiently in real-world applications.

2) Novelty of the approach: FreqKV introduces a novel approach by using frequency-based compression for the first time in context extension, compressing the information of all tokens instead of fully discarding some, as many other methods do.

3) Training and inference efficiency: FreqKV achieves efficient training and inference without introducing architectural changes or extra parameters. In both training and inference, memory usage is limited by a fixed cache size, and computational complexity grows linearly compared to the quadratic growth in original LLMs. This significantly improves latency and reduces memory consumption, especially for handling longer context windows.

4) Results: FreqKV outperforms the different KV compression techniques on LongBech in three tasks of Single Doc QA, Multi Doc QA, and Summarization.

### Weaknesses
1) Performance degradation in training: According to Table 1 of the paper, FreqKV shows higher perplexity compared to LongLoRA, particularly for context lengths of 4096 tokens or more on both test sets. This indicates that FreqKV may underperform slightly in language modeling accuracy at extended context lengths.

2) Results on higher context length: Table 1 reports results for context lengths up to 32K tokens, with no further results on longer contexts such as 128K. This leaves the method’s performance on very large context lengths untested and unclear.

3) Resource usage: While FreqKV does not introduce additional parameters or architectural changes, it still requires extra computational resources for the compression process. The computational complexity and latency overhead are negligible, as compression only occurs when the cache is filled. However, the specific overhead of the frequency-domain transformation and inverse transformation, which are core to the method, is not clearly quantified, making it difficult to assess the true cost of the approach.

4) Results of the other models: The results were reported only on the LLaMA-2-7b model (both base and chat versions), leaving FreqKV's performance on other LLMs unclear. This raises concerns about the generalizability of the findings, as different architectures and pre-training procedures can lead to varying sensitivity to compression techniques.

5) Generalizability:  In the paper, the optimal retaining ratio for FreqKV is determined through an ablation study. Applying this approach to other large language models could be time-consuming, as the best retaining ratio may vary from one model to another. The lack of a systematic method for determining this ratio limits the practical applicability of the method across diverse models.

6) Unifrom across layers: A limitation of FreqKV is its use of a uniform retaining ratio and cache size across all layers. Previous works (such as [1, 2, 3]) have shown that middle layers are particularly important for retrieval and reasoning tasks, suggesting that the importance of each layer's KV cache can vary depending on the task and model. Hence, some layers may contain more important information and would benefit from fewer rounds of compression. This uniform approach may lead to suboptimal performance by over-compressing critical layers and under-compressing less important ones.

### Questions
1) How would the results of FreqKV change if applied to context lengths greater than 32K tokens? Would any additional modifications be necessary in FreqKV to support such extended context lengths?

2) What are the results of FreqKV on other popular large language models, such as GPT models or Gemini? How would the results of FreqKV change when applied to retrieval or reasoning tasks(such as Need-in-a-Haystack)?

4) Is there an algorithmic or automatic method for determining the optimal retaining ratio for FreqKV rather than relying on manual selection through ablation studies? 

5) How would the model's performance change if non-uniform cache sizes and retention ratios were used across different layers? Would an experiment comparing uniform compression to a non-uniform approach (where compression rates vary by layer) show the benefits of a more flexible compression strategy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents FreqKV which uses the discrete cosine transform to compress the KV cache in the frequency domain by removing the long tail of high frequency components, then uses iDCT on the fly to decompress the KV cache and use it normally within the model. The first few tokens are not compressed, similar to prior work on Attention Sinks. Compression is performed iteratively, such that whenever a new set of KV tokens are produced, it is compressed together with the previously-compressed tokens. This results in a linear increase in decoding time instead of quadratic.

### Strengths
KV-cache compression is an important open problem and frequency-domain transform is an interesting method that could be effective. Freq domain is also an interesting space for compression because computation can be done in the frequency domain as was previously demonstrated with CNNs. This work does not take advantage of this feature though.

### Weaknesses
1- What is the overhead of DCT and iDCT on the fly in every iteration? This does not seem to be factored in the performance measurements that you performed in the paper. How do you perform these transforms?
2- The presented method is a composition of attention sinks and freq-domain compression, but the baseline attention sinks result is not shown.
3- More evaluation on long-context results would strengthen the case. Since this is a KV-cache compression method, I find ppl results somewhat irrelevant. Longbench results are good, but I suggest adding GSM8k, needle-in-haystack, and other purpose-built benchmarks.
4- I didn't fully get why you needed to extend llama2 context to 32k instead of using llama3, which is already longer context (128k)?

### Questions
see weaknesses - most of my questions are there.

### Soundness
2

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
5

### Summary
This work introduces a novel context extension training method that compresses key-value states in the frequency domain rather than in the time domain. By analyzing the KV Cache in each layer and head of the Llama-2 model in the frequency domain, they found that the energy is concentrated in the low-frequency components. Based on this observation, they retain only specific low-frequency signals from the expanded KV Cache during model fine-tuning and explore various compression strategies. The proposed method aims to balance runtime speedup with an improved trade-off between model performance and loss.

### Strengths
1. The work brings significant novelty by providing a detailed analysis of why frequency-domain compression is suitable, based on layer-by-layer observations in the Llama model. This analysis leads to the proposal that caching only low-frequency components of the KV states is sufficient. As the author points out, previous approaches that evict KV Cache lead to a permanent loss of information, especially when extending sequence length, whereas this method mitigates that issue.

2. The theoretical analysis is robust, particularly in sections 3.1, 3.2, and 4.1, providing a solid foundation for the proposed approach.

3. The method delivers strong performance in both accuracy and latency. The ablation studies, particularly on sink tokens and the choice of $L$, further reinforce the approach's effectiveness.

### Weaknesses
1. The study is somewhat limited in scope, as it focuses on a single model, making it difficult to generalize the approach as a universal method for all decoder-only generative LLMs.

2. The benchmarks for long-text sequences are relatively few, which may limit the comprehensive evaluation of the method's effectiveness in handling extended sequences.

### Questions
1. You've only tested on Llama-2-7B-(chat). I'm curious about how the proposed "cache low-frequency is enough" approach would perform on other models such as Mistral or Llama-3/3.1 (GQA). If it can demonstrate similar advantages on these models, it would be incredibly exciting and broaden the impact of the work.

2. If possible, I’d like to see how this method performs on benchmarks like **Ruler** (https://github.com/zhang677/RULER) and **Needle In A Haystack** (https://github.com/gkamradt/LLMTest_NeedleInAHaystack/). These could provide a more diverse and challenging evaluation of the approach.

3. If these points can be addressed, I will reconsider the score.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method for compressing the KV cache into a fixed length, by filtering out high-frequency components. This compression can be applied iteratively, so that a small fixed memory budget is enough for processing long contexts. This approach reduces both memory and computational requirements, applicable during both training and inference. The authors demonstrate that this method yields minimal perplexity reduction when compared to full attention (without compression) and compared to other compression methods. They also demonstrate its effectiveness on long context downstream tasks via the LongBench benchmark.

### Strengths
**Originality**: The paper presents a novel idea that allows processing longer contexts by making uses of the observation that the information in the KV cache is mostly in the low frequency components. While this observation is not new, using it to compress the KV cache has not been done before, to the best of my knowledge.

**Significance**: As LLMs become stronger and more prevalent, it also becomes more and more important to make them applicable for longer contexts. Therefore, methods like FreqKV that allow processing longer contexts with minimal effect to quality might become invaluable.

**Clarity**: The method is simple, and presented clearly and elegantly.

### Weaknesses
 **Results:**
* Hard to interpret the strength of the results in table 1 without a comparison to a simple baseline like local attention. While table 1 shows that the higher perplexity is not as bad as in the other compression method (LoCoCo), it would be nice to also show a comparison to local attention. In many cases the difference in perplexity between full attention and local attention might not be very large (e.g., see Xiong et al., 2022, “Simple Local Attentions Remain Competitive for Long-Context Tasks”), so it would be helpful to see if this method of compressing the full context to max size 4k works substantially better than the trivial method of only keeping the latest 4k elements in the KV cache. The absence of this comparison makes it difficult to assess the true benefit of the proposed frequency-based compression, as a simple truncation might yield comparable results, especially given the relatively small perplexity differences observed.
* Method’s performance does not strongly exceed competing compression methods such as SnapKV and PyramidKV (table2 shows slightly higher avg for FreqKV but it’s not clear how significant this difference is). The reported average improvements are marginal, and without a clear statistical significance analysis, it's hard to determine if these differences are meaningful. Furthermore, the lack of a direct comparison on identical tasks and context lengths makes it difficult to ascertain the true advantages of FreqKV over these existing methods.

**Interpretation:** while the paper shows that the method works in practice, it does not explain the reasoning behind the observation. Specifically, is there a plausible explanation for why the information in the KV cache is concentrated around low frequency components? And how is the transformer adapting to work with semi-compressed KV cache during fine tuning? While these questions are not crucial for presenting a practical method, discussing them would make the paper stronger.

### Questions
* Why is there no overlap between the methods listed in table 3 and table 4? Specifically, why not test the perplexity of SnapKV etc. on PG-19? And why not test LoCoCo on LongBench? Is there any reason why these do not apply?
* As stated in weaknesses - I think it would make the results of table 2 stronger if you include a comparison with a simple baseline like local attention.
* As stated in weaknesses - I think some discussion of the advantages / disadvantages of FreqKV compared to other compression methods (such as SnapKV and PyramidKV) would be helpful. Currently, table 2 shows that these methods seem to be on-par so it’s difficult to understand the advantages of FreqKV without this discussion.

**Small suggestions:**
* Introduction has a typo (“shifted spare attention” --> “shifted sparse attention”)
* In section 4.2 (“KV Compression in the Frequency Domain”), the notation for $\tilde{K}_{0:L-1}^{0:N-1}$ is IMO confusing. Because of the superscript, it took me a while to understand that the shape of $\tilde{K}$ is (L, d) and not (N, d). I think it would be helpful to explain this in the text explicitly.
* Currently both PyramidKV and LoCoCo use the reference “Cai. et al., 2024”.

### Soundness
3

### Presentation
3

### Contribution
4
