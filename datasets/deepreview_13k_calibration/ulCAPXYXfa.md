# OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
During the inference phase of Large Language Models (LLMs) with long context, a substantial portion of GPU memory is allocated to the KV cache, with memory usage increasing as the sequence length grows. To mitigate the GPU memory footprint associate with KV cache, some previous studies have discarded less important tokens based on the sparsity identified in attention scores in long context scenarios. However, we argue that attention scores cannot indicate the future importance of tokens in subsequent generation iterations, because attention scores are calculated based on current hidden states. Therefore, we propose OmniKV, a token-dropping-free and training-free inference method, which achieves a 1.68x speedup without any loss in performance. It is well-suited for offloading, significantly reducing KV cache memory usage by up to 75% with it. The core innovative insight of OmniKV is: Within a single generation iteration, there is a high degree of similarity in the important tokens identified across consecutive layers. Extensive experiments demonstrate that OmniKV achieves state-of-the-art performance across multiple benchmarks, with particularly advantages in chain-of-thoughts scenarios. OmniKV extends the maximum context length supported by a single A100 for Llama-3-8B from 128K to 450K.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The inference of large language models (LLM) is memory intensive. This paper proposes a new method for reducing the GPU memory usage when doing LLM inference on GPUs. The main insight of this paper is the similarity of attention score matrix between different consecutive layers. By leveraging this insight, the author proposes a new method to reduce the GPU memory usage of the KV cache  by over 75% via offloading to CPU memory, while not significantly affect the accuracy.

### Strengths
* The author aims at a timely problem of reducing memory usage of KV cache for LLM inference.
* The proposed method is effect yet simple to implement.
* The author demonstrate real performance gain and capability to run LLM inference with longer sequence length with real workloads.

### Weaknesses
 * There is no mathematical guarentee that the propose method is universally applicable to all LLMs.

### Questions
Thanks for submitting the marvelous paper to ICLR. In general, I believe the paper is trying to solve a timely and important problem. While I appreciate the nice results the proposed methods can achieve, my major concern of this paper is that it introduces some hyper-parameters that could be non-trivial to tune. So, I am wondering how would you tune the filter layers in your designed algorithm?

Besides, since the author does not provide any intuition or mathematical guarantee in the paper, I would be concerned about the generalizability to bigger LLMs such as Llama 3.1 405B. So I am wondering if you have some intuition to explain why attention score matrix could be similar across different layers? While I understand it could be expensive to run experiments with larger LLMs, do you have any intuition that the proposed method will work even with larger LLMs?

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
This paper introduces a KV cache selection algorithm based on cross-layer similarity and shows reasonable downstream performance and wall clock speedups.

### Strengths
This paper explains the cross-layer KV cache selection similarity well and designs a real-world system based on this. The evaluations include the 70B-level model's results, and the decoding speed is also very impressive.

### Weaknesses
 1 Inference-time pipeline parallelism, especially in the same node, is uncommon.   "which is 1.87 times faster than the original model running on three A100 GPUs in pipeline" does not make sense to me.  A tensor parallelism baseline is expected in this case, even if I can understand it is very hard to beat.      
2 This paper uses cross-layer KV cache selection similarity. However, this idea was introduced by InfiniGen in a previous paper. No proper discussion is seen in this paper. If this is solved, I will raise my score.     
3 The baselines shown in this paper are not proper. Only InfLLM is a dynamic KV selection method, but it is mainly used for extending context windows. I will ask for comparisons with Quest or Loki, as they are also dynamic KV selection methods. Static KV selection methods like H2O can not only save inference time but also save total memory without CPU offloading. If this is solved, I will raise my score.

### Questions
As stated in weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes an inference optimization framework which leverage inter-layer attention similarity to offload most of the KV into CPU and select relevant context dynamically to alleviate the memory bound on GPU while maintaining the integrity of contexts.

### Strengths
1. The method can keep full context, which was reflected in the needle and LongBench tasks. 
2. The method can achieve preserve better model quality while having more speed-up over other methods in this class.

### Weaknesses
1. The memory manipulation doesn't seem to be compatible with fundamental serving mechanisms like continuous batching and prefix caching. It's questionable how such algorithm can work in real world.
2. It will be quite challenging to make the proposed method work with tensor parallel,pipeline parallel, and context parallel, which are also essential in production.

### Questions
1. Related to weakness 1, how does this method compare to vLLM/SGLang with FlashInfern/FlashAttention backend, in terms of throughput and latency? If slower, is OmniKV compatible with practical serving framework like vLLM? 
2. Related to weakness 2, can you benchmark TP=4,8 for <10b scale mdoels? Also, tp=8, pp=4, for any 70B models? I'd like to see (1) latency and throughput for prompt length of 128k, 256k, 512k(probably need ctx parallel) and output length of 512, (2) quality test on needle-in-a-haystack on 128k, 256k, 512k ctx.
3. Could you benchmark against [1], for both speed and quality preserving?

[1] MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention

### Soundness
3

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
4

### Summary
The paper presents OmniKV to reduce GPU memory usage when serving Large Language Models (LLMs) with long contexts. OmniKV is based on the observation that the importance of history tokens cannot be determined by the current stage attention score. Thus, permanently discarding some of past KV tokens may incur accuracy loss. OmniKV is a token-dropping-free and training-free inference method that reduces KV cache GPU memory usage by over 75% without performance degradation, which also accelerates  inference efficiency in long-text scenarios. The key insight of OmniKV is that important tokens are very similar across consecutive LLM layers. So that the KV Cache, which is offloaded to CPU, can be loaded to GPU in the meantime for different layers. Results demonstrate that OmniKV can handle a 450K context with a decoding latency of 7.52 tokens/s, which is 1.87 times faster than the original model running on three A100 GPUs in pipeline mode.

### Strengths
1) This paper focuses on a timely and important problem: Reducing the KV Cache memory usage of long-context LLMs. 

2) OminKV greatly reduces the GPU memory consumption when serving long-context LLM through offloading. It reduces the LLM inference latency by only loading important history tokens to GPU for attention computation. OmniKV well preserves model’s performance on long-context benchmarks such as LongBench and InfiniteBench.

3) OmniKV notices that the important tokens for consecutive layers are similar, merging the CPU-GPU memory loading procedure for multiple layers to reduce memory transaction and important token identification overheads.

### Weaknesses
1) The optimization techniques proposed in this paper cannot accelerate the prefilling speed of LLM. 

2) In Figure 4, it seems that OmniKV (w/ offload) is slower than the dense baseline until the sequence length reaches 128K. For OmniKV w/o offload, the speed also lags behind the dense baseline when sequence length < 32K.

3) The dense baseline (Full) seems not to be strong enough. For Llama-3-8B model on A100, TensorRT-LLM and vLLM take less than 20ms to decode a token (sequence length = 128K, batch size = 1) . However, the dense baseline takes ~80ms,  according to Figure 4.

### Questions
1) What is the dense baseline implementation used for efficiency evaluation in Figure 4?
2) In the last sentence of abstract, the authors mention that “By using a single A100 and Llama-3-8B, OmniKV can handle a 450K context with a decoding latency of 7.52 tokens/s, which is 1.87 times faster than the original model running on three A100 GPUs in pipeline.” I would appreciate if the authors could elaborate i) what is the baseline setting for “original model running on three A100 GPUs in pipeline”; ii) what will be the latency for “original model” if the model is served with tensor parallelism rather than pipeline parallelism.

### Soundness
2

### Presentation
3

### Contribution
2
