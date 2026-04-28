# Don’t Discard, but Keep It Small: Context-Preserving KV Cache Compression with Importance-Aware Adaptive Precision

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 5, 6

## Abstract
As the length of input sequences in Large Language Models (LLMs) continues to grow, efficient key-value (KV) cache management has become essential for improving inference speed and throughput of autoregressive decoding.
Although several approaches have been proposed to reduce memory usage by selectively retaining only the important KV pairs and discarding the rest, these eviction-based methods can lead to unintended consequences during the generation process.
In this paper, we investigate the adverse effects of cache eviction methods and reveal that discarding KV pairs potentially introduces risks such as safety prompt breaches, hallucinations, and loss of critical contextual information.
Interestingly, we find that preserving even a fraction of the information from evicted KV pairs through reduced precision quantization significantly mitigates these issues.
On the other hand, we also observe that important KV pairs need to be maintained at higher precision to preserve generation quality.
Based on these findings, we propose Mixed-precision KV cache (MiKV), a robust plug-and-play cache compression method that balances performance and memory efficiency.
MiKV preserves lost contextual information by storing evicted KV pairs in low precision, while maintaining the essential KV pairs in higher precision to ensure generation quality. 
Experimental results across multiple benchmarks and LLM architectures demonstrate that our method achieves a state-of-the-art balance between compression ratio and model performance, outperforming existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents an efficient KV cache compression approach, which adopts adaptive quantization, assigning different elements in the KV cache bits according to their importance. This work also analyzes how missing information in the KV cache could harm the generation quality, leading to more hallucinations.

### Strengths
The idea is well-motivated and clear. The advantage of adaptive quantization has been widely studied in weight or activation quantization, such as AWQ. Applying a similar idea to KV cache is straightforward.

### Weaknesses
The novelty of this work is limited since the proposed method is more like an extension of KIVI by taking KV cache importance policies like H20 and SnapKV. One reason existing works don't use the adaptive KV cache compression is the engineering effort of implementing different quantizations with irregular shapes. 

One contribution of this work could be the engineering effort or the design choice of balancing performance and efficiency. However, the implementation details are insufficient. L464 said the implementation relies on the existing kernel of KIVI. It's better to have more details or to open-source the code. Do we need triton or CUDA kernels to enable adaptive quantization?

### Questions
Table 3 reports the RULER benchmark, but the details of the experiments are missing. For example, the RULER has a different context length from 4K to 128K. Which length is used for the testing? Since this work said it uses Longchat, I guess the context length is only 4K, based on the result of the full KV cache setting with the RULER leaderboard.

For the latency benchmark, I am confused with the testing setting. L1409 said this work uses the Huggingface transformers library to measure the wall-clock latency, but the following content said it adopts CUDA and triton kernel for testing other models. My understanding is that the proposed method is tested with kernels but not with vLLM, sglang, or other LLM inference engines. Besides, reporting throughputs is also very helpful for testing the KV cache compression method since the size of the KV cache largely influences the parallelism of the decoding samples in a batch.

### Soundness
2

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
This paper investigates the drawbacks of KV cache compression methods based on eviction and quantization. It introduces the MiKV method, which applies importance-based mixed-precision compression to the KV cache, preserving less critical KV pairs in lower precision while maintaining important pairs at higher precision.

### Strengths
1. Proposes a mixed-precision KV cache compression approach that can be seamlessly integrated with existing importance policies.

2. Reduces quantization loss by constructing a channel balancer.

### Weaknesses
1. Lack of baseline comparisons: Quantization methods like KIVI are not tested on the RULER benchmark.

2. The tested context length is not specify on the  RULER benchmark, and should include additional lengths (e.g., 8k, 16k, 32k), as KV cache compression is especially beneficial at larger context lengths.

3. RULER consists mainly of synthetic tasks; it would be valuable to test on real-world tasks such as InfiniteBench or LongBench.

### Questions
How does MiKV handle exceptionally long contexts? Unlike methods like H2O, which can keep the KV cache size fixed, MiKV’s KV cache size will inevitably increase as the context grows.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new KV cache compression method, called MiKV. MiKV quantizes unimportant KV cache into lower bit presentation while maintaining more important KV cache in higher bit presentation. The paper claims superior performance against existing baselines.

### Strengths
- The proposed channel balancer to avoid per-channel outliers is effective.

### Weaknesses
1. The technical novelty of the paper is limited. In my opinion, there is little to no technical novelty presented in the paper. The proposed method is simply a combination of KV cache dropping method + quantization, which is in plain sight to notice given the orthogonality of KV cache dropping and quantization. Moreover, the proposed combination does not offer any substantial gain in term of performance, compared with quantization-only baselines in the experiments section, e.g. KIVI.
2. The empirical study on the detrimental effect of kv cache dropping offers little insights. Most of the claims are easy to notice given the nature of kv cache dropping methods. Moreover, the claims in section 3 are not supported by any experiment results.
3. KV cache dropping baselines are not enough. For example, H20 is considered to be old now given the fast pace development in this field, as well as a weak baseline [1]. There are more recent KV cache dropping baselines that are strong on long-context tasks [2] [3].

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the **MiKV** (Mixed-precision KV cache) strategy, an adaptive compression method for KV caching in LLMs to optimize memory usage without compromising performance. Unlike traditional eviction methods that discard less important KV pairs, potentially degrading context retention, **MiKV** preserves evicted pairs at lower precision and keeps crucial pairs at high precision, balancing memory efficiency with context integrity. The study identifies that cache eviction often leads to context loss, risking issues like safety breaches, hallucinations, and incoherent outputs. By introducing an outlier-aware quantization and importance-based precision control, **MiKV** maintains the generation quality across multiple benchmarks, achieving higher compression ratios and comparable performance to full-cache models. Experimental results indicate **MiKV**’s robustness in handling long contexts and minimizing memory footprint on GPUs.

### Strengths
1. **MiKV** effectively mitigates the risk of context loss by preserving all KV pairs in varying precisions, which prevents common issues like hallucinations and prompt breaches seen in eviction-based methods. This approach maintains generation quality even with high compression ratios.

2. The **MiKV** experiments are relatively thorough, covering diverse benchmarks like GSM8k, HumanEval, Line Retrieval, and MMLU to demonstrate effectiveness across tasks. 

3. The plug-and-play design of **MiKV** enhances its applicability, making it a versatile tool for LLM deployment in memory-constrained environments and bringing reasonable performance improvements

### Weaknesses
1. The paper mentioned that **MiKV** can be used off-the-shelf integrated with other important token selection policies such as H2O but didn't clearly state what eviction policies were used in experiments, especially Table 1, Table 3, and Figure 6. The experiments on larger models are limited. 

2. The improvement of **MiKV** on SnapKV is quite limited, showing that the mixed-quantization approach may not be universally effective on different important-token-selection policies, which shows that the most crucial component is the choice of selection policy of important tokens but not the mixed-precision strategy. 

3. In the latency analysis, the paper didn't measure the end-to-end latency of quantization method RTN, which achieves comparable performance in several settings in Figure 6.

### Questions
1. How does the **MiKV** perform GSM8k, HumanEval, Line Retrieval, and MMLU in tasks on larger models? What's the change of generation latency costed by larger models applied with **MiKV** compared to other approaches?

2. What's the implication behind the limited improvement of **MiKV** applied on SnapKV?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the issue that token eviction-based KV cache compression strategies can lead to the loss of critical context details, resulting in unintended generation outputs. The authors propose a mixed-precision KV cache (MiKV), which compresses KV pairs using a mixed precision approach rather than discarding them. The method preserves more important KV pairs in higher precision and stores others in lower precision. Experiments show that MiKV outperforms token eviction methods (e.g., H2O, SnapKV) and quantization approaches (e.g., KIVI) on selected benchmarks.

### Strengths
1. KV cache compression is a crucial research topic for large language models.
2. The idea of MiKV is simple and easy to implement.
3. Experimental results indicate that MiKV effectively retains critical details compared to eviction-based methods.

### Weaknesses
1. The novelty is somewhat limited. While the method is effective, the concept of identifying important tokens in the KV cache is not new, and mixed-precision quantization is a widely used technique in LLM quantization.
2. The paper would be clearer if it provided more detail on how important tokens are selected, rather than simply referencing prior research. This would make the paper more self-contained.

### Questions
1. I found Figure 1 a bit confusing. Does the quantization scheme for a token change as generation progresses? For instance, can a token in the cache shift from INT4 to INT2 during later stages of generation?
2. In Section 5, MiKV is compared with another KV cache quantization approach, KIVI. KIVI uses per-channel quantization for keys and per-token quantization for values, as outlined in the original paper. Was this setting preserved in your experiments? If not, the comparison might not be fair.

### Soundness
3

### Presentation
2

### Contribution
3
