# DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads

- Decision: Accept
- Scores: 8, 5, 5, 6, 8, 6

## Abstract
Deploying long-context large language models (LLMs) is essential but poses significant computational and memory challenges.
Caching all Key and Value (KV) states across all attention heads consumes substantial memory.
Existing KV cache pruning methods either damage the long-context capabilities of LLMs or offer only limited efficiency improvements.
In this paper, we identify that only a fraction of attention heads, a.k.a, \emph{Retrieval Heads}, are critical for processing long contexts and require full attention across all tokens.
In contrast, all other heads, which primarily focus on recent tokens and attention sinks--referred to as \emph{Streaming Heads}--do not require full attention.
Based on this insight, we introduce \method, a framework that only applies a full KV cache to retrieval heads while using a light-weight, constant-length KV cache for streaming heads, which reduces both LLM's decoding and pre-filling memory and latency without compromising its long-context abilities.
\method uses a lightweight, optimization-based algorithm with synthetic data to identify retrieval heads accurately.
Our method significantly reduces long-context inference memory by up to 2.55$\times$ for MHA and 1.67$\times$ for GQA models while speeding up decoding by up to 2.18$\times$ and 1.50$\times$ and accelerating pre-filling by up to 1.73$\times$ and 1.63$\times$ for MHA and GQA models, respectively, with minimal accuracy loss compared to full attention.
Notably, combined with quantization, \method enables Llama-3-8B decoding with 3.3 million context length on a single A100 GPU.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
DuoAttention leverages finding around retrieval heads. By allocating more KV budget to such heads and compressing the rests, the method claims to have excellent long context performance.

### Strengths
1. The proposed method is extremely performant. It is rare to see a prefilled compressible token dropping method capable of doing NIAH. 

2. The efficiency optimization is solid, and it is supported by a thorough efficiency evaluation.

3. The optimization-based head selection approach offers a different avenue for attention head pattern matching.

4. The paper is nicely written.

### Weaknesses
1. The method mainly involves retrieval head + token dropping (in this case, StreamingLLM), which is slim in novelty. I don't think it is much of an issue given the impressive performance boost achieved while remaining practical, but this is worth mentioning.

2. The featured compared methods — SteamingLLM, H2O, and TOVA — are very dated. I'd like to see how it stands off with more modern KV cache compassion/sparse inference methods, e.g., SnapKV and MInference.

3. The NIAH setting is unclear. What does the needle look like? What background is used? The author should better clarify this, as different settings can lead to very different results.

4. Following #3, it looks like LongBench is the only real long context test evaluated. I'd like to see more coverage on other long context datasets, e.g., $\infty$Bench and RULER.

5.  I honestly do not understand the decision to feature models like Llama-3-8B-Instruct-Gradient-1048k and Llama-2-7B-32K-Instruct — these are third-party finetuned models with limited adaptation in the community. They were reasonable choices before Llama 3.1 as there wasn't a long context-capable Llama, but with Llama 3.1 being available and widely tested, it should clearly be the base model to avoid reaching very third-party recipe-specific conclusions (especially when the authors are not doing much, if any, >128k evaluations).

6. While I appreciate the additional results in A.7, I am still not quite sure how Figure 20 is achieved even after careful reading. The authors stated they "utilize MInference kernels to prefill all retrieval heads" in contrast to "prefilling all heads with MInference." First, what budget does Figure 19 have, and is it aligned with Figure 6? More specifically, are the authors only applying MInference sparse patterns to the retrieval heads? What drives that decision, and what would happen if you let MInference determine the patterns of non-retrieval heads? Would there be any improvement compared to making them all StreamingLLM heads? Also, MInference seems to exhibit some degradation on short-context tasks — can this be alleviated through some combination design?

7. Regarding RazorAttention, did you consider the echo heads proposed by the authors?

8. What does "retrieval head ratio" mean? Is it the ratio of retrieval heads being preserved or the total compression ratio? This distinction might lead to different conclusions regarding your 25% vs. 30% comment on RazorAttention.

9. The core ingredient of the proposed method is leveraging the existence of induction/retrieval heads, where the importance of such heads has been well-studied in prior work. DuoAttention is not the first to explore assigning full cache to retrieval heads (though other works may be considered concurrent), and its gate-based optimization approach is heavily rooted in gating network studies from the MoE and pruning realms. For example, [3] — a widely regarded classic on MoE — also employs trainable gate values to determine the activation of different experts. Similarly, DuoAttention employs trainable gate values to determine head categorization, where the resemblance is strong. Various pruning methods also assign trainable importance scores to guide component dropping.

### Questions
One of the concurrent works, RazorAttention, also utilizes a very similar recipe. The authors compared it in Figure 13(1), but I find the reading to be very different from RazorAttention's own reporting. Any insight of why?

---

## Post-rebuttal update

The latest response from the authors is satisfactory for the most part: 

* It is a reasonable choice to feature Llama-2-7B-32K-Instruct if the goal is to include a long context-capable MHA model.
* The added Llama 3.1 results demonstrate that DuoAttention remains performant on one of the most mainstream long context models.
* I appreciate the authors for recognizing the connection between their optimization-based approach and prior gating network studies.
* The budget discussion regarding RazorAttention and NIAH is sound. However, I must note that if the authors did not explore echo heads — a key element of RazorAttention — in the ablation studies on "attention profiling," this omission should be explicitly noted.
* Similarly, if Figure 19 is not done with an aligned budget, it is not fair to directly compare Duo's NIAH performance with MInference by citing Figure 19. That said, using it as a baseline for Figure 20 is reasonable. I also have some reservations about claiming that the "sandwich in a SF park" needle is harder than the magic city/passkey retrieval-like needle, as the former is known to be very prompt-sensitive. However, this is a minor distinction, and as long as the setting is explicitly noted, both can be considered solid needle setups.


I am improving my rating to 8 if the authors can supply full $\infty$Bench report in their revision.

(In addition, I also add that I don't believe DuoAttention's incomptability with MQA models is a big deal. Yes, this limitation should be clearly noted; but it is rare to find powerful MQA models, and the community adopts GQA as a middle ground between MQA and MHA for good measures.)

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
This paper introduces a lightweight, optimization-based method DuoAttention that only applies a full KV cache to retrieval heads while using a constant-length KV cache for streaming heads. The proposed method achieves good performance in both MHA and GQA.

### Strengths
1.	It saves the GPU memory and enhances the inference efficiency for both MHA and GQA.

### Weaknesses
1.	There are some related works identifying the different patterns of retrieval and non-retrieval heads, such as RazorAttention, Retrieval Head Mechanistically Explains Long-Context Factuality, MInference, etc. It would be better to clarify the novelty of the proposed method.
2.	It can only be applied to multiple KV cache scenarios. For only single KV cache model structure, such as YOCO, it cannot be applied.
3.	The baselines are not comprehensive. It would be beneficial if the authors could compare their results with more advanced baselines.
4.	It seems the proposed method cannot achieve the best performance in all the benchmarks in Figure 7. It would be beneficial to give detailed analysis on the worse cases.

### Questions
Please address the questions in the weaknesses.

### Soundness
3

### Presentation
2

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
This work presents methods to reduce memory footprint and computational demands of Large Language Model's (LLM) attention layers to enhance inference speed and to accommodate longer context lengths. The authors build upon the observation that only a few attention heads within an LLM, also known as retrieval heads, have considerable impact on long-context performance. They propose a novel, optimization-based approach to identify these less critical heads, unlike previous methods that relied on heuristic techniques. This optimization process utilizes synthetic data designed specifically to evaluate long-context capabilities. Their results indicate superior model performance compared to current state-of-the-art retrieval head allocation techniques and certain KV sparsification methods, while maintaining comparable KV cache budget.

### Strengths
* The paper is well-structured and the claims are easy to follow.
* This work addresses a significant research problem in LLM inference - KV cache optimization. 
* The authors perform comprehensive ablation studies to motivate each aspect of their proposed approach. The advantage of their proposed novel retrieval head selection method over the existing methods is well-supported by empirical results.

### Weaknesses
 * While tensor parallelism has proven effective in reducing latency and memory usage per GPU, this paper omits any discussion on how its proposed methods could be adapted to such model-parallel settings. For example, in an 8-way tensor-parallel configuration, the retrieval heads might become the performance bottleneck, potentially negating the gains from this work. The proposed method's reliance on a specific number of retrieval heads per layer, without a clear strategy for balancing this across GPUs, raises concerns about its practical applicability in distributed training and inference scenarios. Furthermore, the paper does not address the potential overhead of managing different types of attention heads in a tensor-parallel environment, which could introduce additional communication costs.

* Some state-of-the-art KV sparsification methods are missing in the comparative analysis. For instance, SnapKV, PyramidKV, AdaKV are some notable omissions. It is unclear if the proposed method can achieve comparable compression ratios to these methods, particularly for very long context lengths. The lack of a direct comparison makes it difficult to assess the practical advantages of the proposed approach over existing techniques. Specifically, the paper does not discuss how the proposed method would perform under more aggressive compression ratios, which are often required in real-world applications. 
   1. Yuhong Li, Yingbing Huang, Bowen Yang, Bharat Venkitesh, Acyr Locatelli, Hanchen Ye, Tianle Cai, Patrick Lewis, and Deming Chen. Snapkv: Llm knows what you are looking for before generation, 2024d. *Arxiv /abs/2404.14469*
   2. Zefan Cai, Yichi Zhang, Bofei Gao, Yuliang Liu, Tianyu Liu, Keming Lu, Wayne Xiong, Yue Dong, Baobao Chang, Junjie Hu, and Wen Xiao. Pyramidkv: Dynamic kv cache compression based on pyramidal information funneling, 2024. *Arxiv /abs/2406.02069*
   3. Yuan Feng, Junlin Lv, Yukun Cao, Xike Xie, and S. Kevin Zhou. Ada-kv: Optimizing kv cache eviction by adaptive budget allocation for efficient llm inference, 2024. *Arxiv /abs/2407.11550*

### Questions
* How effective is this method for reasoning-based tasks? Do the retrieval heads remain the same for question-answering type tasks as well as reasoning type tasks?
* Rather than merely illustrating the distinction between retrieval and streaming heads through specific examples, it would be more compelling to present statistically significant evidence demonstrating how the identified retrieval heads generalize across various sequences and tasks.
* Is there any way to extend this method to multi-GPU setting?
* To what extent can the memory savings lead to increased throughput? (Just a suggestion)

### Soundness
3

### Presentation
4

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
To tackle KV Cache problem, the paper introduces a new approach called DuoAttention, which classifies attention heads in LLMs into two types: Retrieval Heads and Streaming Heads. Retrieval Heads are essential for processing long contexts and require full KV cache storage, while Streaming Heads focus on recent tokens and can operate with reduced KV caches. DuoAttention uses a lightweight optimization process to identify non-compressible Retrieval Heads, allowing for efficient memory usage and faster processing. This method integrates easily with existing optimization techniques and significantly reduces the memory footprint and decoding time. When combined with quantization, DuoAttention enables models like Llama-3-8B to handle up to 3.33 million tokens on a single GPU, achieving a 6.4× increase in capacity compared to standard deployments.

### Strengths
1) The paper is well written and well motivated.
2) DuoAttention is a plug-and-play solution compatible with FlashAttention.
3) DuoAttention can accelerate inference during both the prefill and decoding stages.

### Weaknesses
1) Lack the experiment with the accuracy results after combining DuoAttention and KV quantization.
2) Lack the comparisons with new KV Cache compression technologies such as Minference.
3) Using different compression rates for different heads may lead to uneven computation across cards during parallel inference, potentially affecting performance.

### Questions
1) Is the proportion of Retrieval Heads the same for different models? Why choose 25% Retrieval Heads for MHA and 50% for GQA?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The DuoAttention uses the retrieval heads and local streaming heads, realizing the KV cache compression and acceleration:
1) the retrieval heads preserve the major information of the long-context, which can not be compressed;
2) the non-retrieval heads are compressed by locality, which is accelerated with StreamingLLM;
3) the retrieval heads are detected with importance learnable weights;
4) Finally, the prefill is accelerated by chunked prefilling, and the decoding is accelerated with compressed KV cache.

### Strengths
1. the experiments is enough and confident
2. the writing and clarity are clear
3. the concept of retrieval heads is significant for static KV cache compression

### Weaknesses
1. the detection of retrieval heads is based on the fine-tuning of importance weights, the usability should be enhanced
2. the compression ratio is limited, if the retrieval heads preserve the full context information

### Questions
1. the offline method to find the retrieval heads is more important for practical application
2. the compression ratio of KV cache should be improved

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Overall, this is an interesting and solid work. It categorizes all attention heads of LLMs into two types—Retrieval Heads and Streaming Heads—based on an offline analysis. By pruning the KV cache of Streaming Heads, this study achieves more efficient inference.

### Strengths
1. The paper is well-written and easy to follow, with a novel methodology.
2. The work is solid, having been evaluated on multiple benchmarks. It also combines the orthogonal technique of quantization, further enhancing its results.
3. The evaluations demonstrate promising results.

### Weaknesses
### strengths:
1. The paper is well-written and easy to follow, with a novel methodology.
2. The work is solid, having been evaluated on multiple benchmarks. It also combines the orthogonal technique of quantization, further enhancing its results.
3. The evaluations demonstrate promising results.

### weaknesses:
1. **Choice of Baseline**: DuoAttention is essentially a KV cache compression algorithm, and all the performance gains come from reducing the amount of KV cache that was previously stored, whether in the prefilling stage or the decoding stage. While the authors compare their method to H2O, TOVA, and StreamingLLM, these approaches are no longer state-of-the-art. For instance, SnapKV [1], which was published in April and is now widely regarded as a more powerful KV cache compression method, should have been considered. In the commonly used LongBench evaluation, SnapKV outperforms H2O with only one-quarter of the cache budget [1]. Additionally, in needle-in-a-haystack tasks, SnapKV benefits from its pooling operations and significantly improves accuracy compared to H2O. When compressing an 8K sequence to 128 tokens, SnapKV incurs minimal performance loss, outperforming H2O by a large margin, as shown in [2]. In the experimental section, the authors highlight a limitation of H2O: “Since the original designs of H2O and TOVA do not support long contexts, we modify their algorithms by replacing the pre-filling stage with FlashAttention and simulating decoding for the last 50 tokens of the input, following Tang et al. (2024b).” This limitation arises because H2O requires the accumulation of global attention weights, which is incompatible with FlashAttention. However, SnapKV and its successors only observe attention scores within a small observation window for compression, making them highly compatible with FlashAttention. This allows recalculating only a small portion of attention weights for compression when combined with chunked prefill. Therefore, SnapKV would be a more appropriate baseline for this paper.

2. **Inappropriate statements:**

a. _“Moreover, DuoAttention is **fully compatible** with important optimization techniques like GQA and quantization.” “Approximative attention methods, such as H2O (Zhang et al., 2023b), StreamingLLM (Xiao et al., 2023b), TOVA (Oren et al., 2024), and FastGen (Ge et al., 2024), often compromise accuracy in long-context applications and are **incompatible** with essential KV cache optimization techniques like GQA”_ 

I believe the compatibility of DuoAttention with GQA is not significantly different from other methods. DuoAttention forcedly classifies a group of attention heads under GQA into the same category through offline analysis, thus upporting GQA. However, other methods could achieve the same effect by accumulating weights for a group of kv cache during cache eviction. Therefore, GQA compatibility seems more like an implementation detail rather than a unique feature of the algorithm. In fact, StreamingLLM does not encounter any GQA compatibility issues. The lack of GQA compatibility in earlier works, in my opinion, stems from the fact that GQA was not widely adopted when those methods were initially proposed. Later methods, for the sake of comparison, maintained this approach without further integrating GQA, which could have been easily addressed at the code implementation level. A recent study [3] applying cache eviction in paged attention has demonstrated that this compatibility can be easily achieved in practice.

b._“Also, these methods (H2O, TOVA, StreamingLLM) cannot reduce the prefilling cost of long-context LLMs.”_

 Previous evaluations of cache compression often compress the KV cache after the prefilling stage to ensure comparability. Since the KV cache for each layer can be compressed immediately after the completion of that layer's prefilling computation, this already substantially reduces the peak memory usage during the prefilling process. If further reduction in computational cost during the prefilling stage or a more significant decrease in peak memory usage for very long input texts is desired, combining these methods with chunked prefilling can provide additional acceleration—a straightforward solution. This is particularly applicable to StreamingLLM, which is same with the same Streaming Head in this paper, and thus faces no obstacles in applying such methods. If one argues that the H2O method combined with chunked prefilling may require additional accumulation of global attention weights, the additional baseline SnapKV can effectively address this issue.

### questions:
1. The core of this paper focuses on prioritizing the retention of the KV cache in important attention heads while attempting to discard less important cache in other heads, based on offline detection results. Some follow-up works on SnapKV seems to align closely with this approach [3,4]. For example, [4] employs a similar strategy by identifying important attention heads through online analysis of "altering model outputs," subsequently allocating more budget to these key heads and reducing the budget for others. What do you think is the relationship between these budget allocation strategies and the detection of retrieval heads?

2. In Equation 2, why is the index i set to $L$? Shouldn't it be $N$ instead?

3. How do you control the cache budget to a specifical ratio like 50% in the experiments? It seems challenging to precisely manage the cache budget within this approach.

### Questions
1. The core of this paper focuses on prioritizing the retention of the KV cache in important attention heads while attempting to discard less important cache in other heads, based on offline detection results. Some follow-up works on SnapKV seems to align closely with this approach[3][4]. For example, [4] employs a similar strategy by identifying important attention heads through online analysis of "altering model outputs," subsequently allocating more budget to these key heads and reducing the budget for others. What do you think is the relationship between these budget allocation strategies and the detection of retrieval heads?

2. In Equation 2, why is the index i set to $L$? Shouldn't it be $N$ instead?

3. How do you control the cache budget to a specifical ratio like 50% in the experiments? It seems challenging to precisely manage the cache budget within this approach.

[1] Li, Y., Huang, Y., Yang, B., Venkitesh, B., Locatelli, A., Ye, H., ... & Chen, D. (2024). Snapkv: Llm knows what you are looking for before generation. arXiv preprint arXiv:2404.14469.

[2] Zhang, Y., Gao, B., Liu, T., Lu, K., Xiong, W., Dong, Y., ... & Xiao, W. (2024). PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling. arXiv preprint arXiv:2406.02069.

[3] Rehg, I. (2024). KV-Compress: Paged KV-Cache Compression with Variable Compression Rates per Attention Head. arXiv preprint arXiv:2410.00161.

[4] Feng, Y., Lv, J., Cao, Y., Xie, X., & Zhou, S.K. (2024). Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference. ArXiv, abs/2407.11550.

While this paper is engaging and provides extensive evaluations, several limitations hold me back from giving it a higher score.  If the authors can address these concerns during rebuttal phase, I believe it would greatly enhance the paper’s quality, and I’d be glad to reconsider my score.

### Soundness
3

### Presentation
3

### Contribution
3
