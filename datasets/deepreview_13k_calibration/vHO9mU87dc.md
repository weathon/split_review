# ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5

## Abstract
With the widespread deployment of long-context large language models (LLMs), there has been a growing demand for efficient support of high-throughput inference. However, as the key-value (KV) cache expands with the sequence length, the increasing memory footprint and the need to access it for each token generation both result in low throughput when serving long-context LLMs. While various dynamic sparse attention methods have been proposed to speed up inference while maintaining generation quality, they either fail to sufficiently reduce GPU memory consumption or introduce significant decoding latency by offloading the KV cache to the CPU. We present \Sys, a high-throughput long-context LLM inference system that stores the low-rank key cache and offloads the value cache to reduce the memory footprint for larger batch sizes and longer sequences. To minimize decoding latency, \Sys employs an accurate KV selection strategy that reconstructs minimal sparse KV pairs on-the-fly. By evaluating \Sys on a broad range of benchmarks, including RULER, LongBench, and Needle In A Haystack, and models like Llama-3.1-8B, Llama-3-8B-1M, GLM-4-9B-1M, Yi-9B-200K, Phi-3-Mini-128K, and Qwen2-7B-128K, we demonstrate that it can support up to 6$\times$ larger batch sizes and boost throughput by up to 3.04$\times$ on an A100 GPU without sacrificing accuracy, even surpassing the performance achievable with infinite batch size under the assumption of infinite GPU memory.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a high throughput LLM inference system for long sentence length. It proposes a compression method to leverage the low rank property of key cache and improve the sparse attention method by accurate KV selection.

### Strengths
This paper is well-organized and clearly written. The proposed method is well-motivated, addressing relevant challenges, and is supported by thorough analysis. The evaluation is comprehensive and robust, effectively substantiating the claims and demonstrating thoughtful considerations. Overall, this is a strong submission for ICLR.

### Weaknesses
1. As shown in Fig. 8, some downstream tasks, such as 'Frequent Words Extraction,' perform significantly worse with sparse KV enabled. A brief analysis of why this approach underperforms for these types of tasks would be helpful, as well as any potential solutions to address these limitations.
2. The proposed solution is currently evaluated on an 8B model with a 128K sequence length. It would strengthen the paper to include an analysis of whether this approach scales effectively for larger models, such as a 70B model with an extremely long sequence length of 1M.

### Questions
As listed in the weakness part.

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
3

### Summary
The increasing KV-cache poses great challenges to long-context LLM inference. This work presents a long-context LLM inference system, SHADOWKV. It decreases the memory footprint by storing the low-rank key cache and offloading value cache to CPU, and reduces the decoding latency by reconstructing the sparse KV pairs on-the-fly. Evaluations show that SHADOWKV supports up to 6x larger batch sizes and improves throughput by up to 3X on A100 GPU while maintaining the accuracy.

### Strengths
+ This work presents a very interesting observation on the KV cache: pre-RoPE key cache is exceptionally low-rank compared to post-RoPE key cache, value cache and KV projection weights. Built on this observation, the proposed SHADOWKV significantly reduces the memory footprint of the Key cache.
+ The work also improves the previous sparse attention work including QUEST by introducing outlier KV cache.
+ This work also implements the inference system and shows actual throughput improvement on the real world A100 GPUs.

### Weaknesses
 - The proposed method is complex, including low-rank K cache, CPU offloaded V cache, outlier KV cache, and dynamic sparse attention. However,  the ablation study on each component is missing.
   - In terms of model accuracy: 
      - it is unclear how much accuracy improvement an extra outlier KV cache will bring.
      - previous work Quest uses Min-Max as landmark cache, ShadowKV adopts Mean as landmark cache. It is unclear how much accuracy improvement this change will bring.
   - In terms of efficiency:
      - Authors only show a rough prefiling latency breakdown in Figure 1(c). It is unclear unclear how long it takes for computing the outlier cache (i.e., reduce, cosine-similarity, top-k, gather) in the profiling stage, how long it takes for KV cache chunk selection (i.e, MatMul, Softmax, Max, TopK) in the decoding stage, how long it takes for recomputing the K cache from low-rank cache. These overheads seem to increase linearly with the context length. It would be better to see the efficiency breakdown on every part of the system under different context lengths (e.g., 128K, 256K, 512K).
      - it is unclear how SHADOWKV performs for extremely long context. For example, the authors evaluated on Llama-3-8B-1M but only with up to 128K context length.
     - this work lacks efficiency comparison against previous work LoKi, Quest and MInference.

### Questions
My questions are listed in the weakness section.

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
This paper introduces SHADOWKV, a CPU-offloading-based system for long-context LLM inference. SHADOWKV addresses GPU memory constraints by leveraging the low-rank property of the key cache, storing a low-rank pre-ROPE key cache on the GPU while offloading the value cache to the CPU. Additionally, SHADOWKV stores landmarks—mean values of post-ROPE keys for adjacent tokens—along with low-rank pre-ROPE key cache in GPU memory. During decoding, SHADOWKV utilizes these landmark keys to identify significant tokens, selectively recovering their keys and retrieving their values from the CPU. Evaluations on long-context benchmarks demonstrate that SHADOWKV maintains high accuracy while significantly reducing GPU memory consumption and inference latency.

### Strengths
* In-depth analysis on low-rank nature of key cache in comparison to value cache as well as weights.
* Leveraging spatial locality of post-ROPE key cache for dynamic sparse attention appears both novel and effective.
* Empirical results are impressive.

### Weaknesses
 * Incomplete Descriptions

The term "sparse budget" is not clearly defined in the paper, which may lead to confusion. Additionally, while SHADOWKV claims to leverage the temporal locality of the KV cache to reduce computation and communication (by approximately 60%), it lacks any detailed explanations on what that feature is.

* Handling Newly Generated Tokens

While the paper says that it excludes the handling of newly generated tokens for simplicity, this issue is quite significant and should not be ignored. If not addressed, the KV cache for newly generated tokens could negate SHADOWKV’s key benefits of reduced GPU memory usage and lower inference latency, especially with long output sequences. Incorporating mechanisms to handle these tokens within SHADOWKV is essential, and the authors should evaluate and report on its impact on accuracy.

* Lack of Comparison with Infinigen

The paper does not sufficiently compare SHADOWKV with Infinigen [1], a closely related work that similarly stores low-rank key cache in GPU memory, offloads the value cache to the CPU, and selectively fetches important values based on approximate attention scores. Although the paper briefly discusses Infinigen, given the significant similarities, a more in-depth comparison with Infinigen should be made in order to highlight the main differentiator of SHADOWKV.

### Questions
* What exactly is the “sparse budget”?

* How does SHADOWKV leverage the temporal locality of the KV cache?

* What are the exact GPU memory savings of SHADOWKV? Including a quantitative discussion on GPU memory savings in the paper would be helpful.

* How can SHADOWKV handle the KV cache for newly generated tokens, and what would be the impact of this?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SHADOWKV, a novel system that improves inference throughput for long-context LLMs. The key challenge addressed is the increasing memory footprint of KV caches as sequence length increases, which slows down inference. SHADOWKV offers a solution by offloading the value cache to the CPU while keeping a low-rank key cache on the GPU, reducing memory consumption without sacrificing performance. By employing a method of KV selection for sparse attention, it boosts throughput and supports larger batch sizes, showing improvements of up to 3.04× throughput on the A100 GPU.

### Strengths
The paper tackles a significant problem in LLM inference by reducing GPU memory usage through a hybrid CPU-GPU cache system, enabling long-context LLMs to operate more efficiently without sacrificing accuracy.

The system shows impressive throughput gains, handling up to six times larger batch sizes compared to baseline methods, which could substantially impact real-world LLM deployment.

SHADOWKV is tested on multiple models and benchmarks (e.g., Llama, GLM) across various tasks, demonstrating consistent performance improvements across all settings.

### Weaknesses
The main issue is that, as far as I know, SVD is precision sensitive, but I didn't find any discussion about precision in the paper. My main question is what precision is used for ShadowKV and baselines. If you are using precision like FP16/FP32, my question is how does ShadowKV work on FP8/(FP8 & FP16) precision? If the precision is FP8, how does ShadowKV survive from precision-sensitive SVD?

For the speed evaluation, I only found the throughput (tokens/s), are there any experiments for the time of each operation separately?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
