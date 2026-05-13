# QSpec: Speculative Decoding with Complementary Quantization Schemes

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Quantization has been substantially adopted to accelerate inference and reduce memory consumption of large language models (LLMs).
While activation-weight joint quantization speeds up the inference process through low-precision kernels, we demonstrate that it suffers severe performance degradation on multi-step reasoning tasks, rendering it ineffective.
We propose a novel quantization paradigm called \sys{}, which seamlessly integrates two complementary quantization schemes for speculative decoding. 
Leveraging nearly cost-free execution switching, \sys{} drafts tokens with low-precision, fast activation-weight quantization, and verifies them with high-precision weight-only quantization, 
effectively combines the strengths of both quantization schemes.
Compared to high-precision quantization methods, \sys{} empirically boosts token generation throughput by up to $1.80\times$ without any quality compromise, distinguishing it from other low-precision quantization approaches. 
This enhancement is also consistent across various serving tasks, model sizes, quantization methods, and batch sizes.
Unlike existing speculative decoding techniques, our approach reuses weights and the KV cache, avoiding additional memory overhead. Furthermore, \sys{} offers a plug-and-play advantage without requiring any training.
We believe that \sys{} demonstrates unique strengths for future deployment of high-fidelity quantization schemes, particularly in memory-constrained scenarios (\textit{e.g.}, edge devices).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a new method called QSPEC, which seamlessly integrates two complementary quantization schemes for speculative decoding. QSPEC utilizes W4A4 quantized LLMs to draft tokens and verifies these drafted tokens with W4A16 quantized LLMs, achieving results comparable to those of W4A16 quantized LLMs in generation tasks.

### Strengths
1. The authors highlight that quantized models perform worse on generation tasks (e.g., code and math) compared to multiple-choice tasks, particularly when using 4-bit quantized activations. This is a significant issue that the community should address.

2. To my knowledge, this paper is the first to combine quantization and speculative decoding. The authors analyze their compatibility, focusing on token prediction similarity, acceptance rate, shared weights, and key-value caches.

### Weaknesses
1. The novelty of this paper is limited. While the combination of speculative decoding and quantization is an interesting topic, the authors do not introduce any new methods. The core idea of using a lower-precision model for drafting and a higher-precision model for verification is conceptually straightforward. The paper lacks a detailed exploration of how different quantization techniques impact the acceptance rate in the speculative decoding framework. For instance, the authors should investigate if techniques like Atom or QuaRot, which employ different quantization strategies, lead to varying acceptance rates or speedups within their QSPEC framework. This would provide a more nuanced understanding of the interaction between quantization and speculative decoding.

2. It is recommended to make more comparisons with previous speculative decoding methods in order to better demonstrate the benefits of integrating quantization into speculative decoding in Table 4. The current comparison is insufficient to highlight the advantages of QSPEC over existing methods. Specifically, the paper should include a more detailed analysis of the memory consumption, which could be a significant advantage due to the shared weights and key-value cache. Furthermore, the paper should compare the performance of QSPEC with other speculative decoding methods, such as Medusa and EAGLE, across a range of batch sizes to demonstrate its scalability and efficiency.

3. The speedup ratio compared with previous speculative decoding methods such as Medusa and EAGLE is weak. The paper does not adequately address the practical benefits of QSPEC in terms of wall-clock time reduction compared to existing speculative decoding techniques. The authors should provide a more in-depth analysis of the latency at both the generation and prefilling stages for W4A4 and W4A16 models, to better understand the performance bottlenecks and the actual speedup achieved by QSPEC.

### Questions
Why does the speedup ratio relative to W4A16 decline as the batch size increases, as depicted in Table 4? I'm intrigued by the overall inference latency difference between the W4A16 and W4A4 models. Could you provide the latency of W4A4 and W4A16 at both the generation and prefilling stages?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper brings an elegant idea to use faster 4b quantized activations for drafting, and use full 16b activations for decoding.

There are significant weaknesses in completeness of the analysis, specifically lack of comparison with other quantization methods in terms of speedup.

### Strengths
It is an elegant idea to use faster 4b quantized activations for drafting, and use full 16b activations for decoding - it saves the memory for weights and helps to align draft / target distributions.

### Weaknesses
1) The paper does not reported acceptance rates

2) The paper no comparison to other lossless speculative decoding methods, namely Eagle2, Medusa2 with top speedups, BiTA with negligible VRAM overhead.

3) table 1: WikiText-2 PPL # 8.70 7.87 (+9.20%) 8.58 (+1.15%) - why ppl is lower for W4 methods? 

4) table 4: 7B W4A16 HumanEval seems too fast (300+ vs other methods)

5) the paper fails to notice that W4A4 is more memory efficient - need to compare using same memory budget

6) the abstract should mention average improvement, not peak

7) Since this is a lossless method, tests should mostly focus on speed, not on quality. So please add speedup comparisons vs other quantization methods, not just to W4A16 baseline.

8) Llama family should refer to L2 paper, not just L3

9) Table4 - add model names

### Questions
1) How would your method compare in speedup to other lossless speculative decoding methods, namely Eagle2, Medusa2 (with top speedups), BiTA (with negligible VRAM overhead).

2) How would your method performs with tree-based speculation?

3) Is the method good for batched generation? What is its performance vs batch size?

4) please report your observed acceptance rates

### Soundness
2

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
3

### Summary
The authors propose a weight-sharing speculative decoding framework for quantized models with varying activation precisions. The core insight of this work is that aggressive weight-activation quantization methods, such as W4A4, often result in performance degradation on complex multi-step reasoning tasks. To address this performance gap while retaining the efficiency of low bit-width models, the framework employs W4A4 to draft the output and W4A16 to verify it, sharing 4-bit weights but producing outputs at different precisions. The KV-cache is subsequently updated by the high-precision model, enhancing the framework with a high-quality KV-cache. Experiments demonstrate that the framework achieves comparable performance to full W4A16 models, while delivering higher throughput with W4A4-based drafting.

### Strengths
The paper presents an interesting observation that claims of "lossless" performance in many quantization studies are often skewed by limited evaluation benchmarks, which overlook the negative impacts of activation quantization. To address this issue, the authors propose a weight-sharing mixed-precision speculative decoding framework. Unlike conventional heterogeneous speculative decoding, which uses a small model for drafting and a significantly larger model for verification, the authors argue that homogeneous speculative decoding with weight-sharing is more suitable for edge scenarios. Although the framework may appear similar to conventional speculative decoding, experiments demonstrate its advantages in both accuracy and throughput.

### Weaknesses
While the observation and intuition behind this work are compelling, some experiments seem to be missing, which weakens the support for the authors' claims. For instance, Tables 1 and 3 lack comparisons with FP16 models. Demonstrating the performance differences between FP16 and W4A16 on complex multi-step reasoning tasks would help the community better understand the true performance gaps between FP16 models and their quantized counterparts. Additionally, Table 4 lacks throughput evaluations for W4A4. Including a latency and accuracy trade-off comparison between the framework and FP16, W4A16, and W4A4 models would provide valuable insights. The absence of these experiments may mislead readers and hinder a full assessment of the proposed framework. I am willing to raise my score if authors address aforementioned issues.

### Questions
- Could the authors provide the accuracy of the FP16 models in Tables 1 and 3?
- Could the authors provide the throughput of the FP16 and W4A4 models in Table 4 as well as in Figures 4 and 5?
- Could the authors include a figure illustrating the throughput and accuracy trade-offs for the proposed framework compared to all baselines?

### Soundness
2

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
3

### Summary
The authors investigate the impact of LLM quantization on multi-step reasoning tasks and find that current methods are insufficient in some cases. They introduce a system design for speculative decoding where activation quantization is disabled during the verification stage. They find that this can improve HW performance without degrading model quality.

### Strengths
Improving the HW performance of multi-step reasoning is a relevant and impactful problem. The authors provide a very insightful analysis into both the impact of quantization on multi-step reasoning and the impact of activation quantization on token prediction probabilities, both of which are novel insights to my knowledge.

### Weaknesses
While the results are promising, the benchmarking may be incomplete. As an alternative to this approach, one could just use a smaller draft model without weight sharing assuming memory is not a constraint. Often the significantly smaller draft model is tuned to the verification model to improve acceptance rates. There is no comparison against this dual-model architecture to establish a concrete baseline. As such, it is unclear which approach one should take. Furthermore, the authors present this work as a new quantization paradigm, but it is more accurately described as a novel inference pipeline leveraging existing quantization methods. The core contribution lies in the specific application of activation quantization within a speculative decoding framework, rather than introducing a new quantization technique itself. This distinction is crucial because it shifts the focus from fundamental advancements in quantization theory to a specific system-level optimization.

### Questions
Have you considered the scenario where a draft model is significantly smaller than the verification model and fine-tuned specifically to maximize acceptance rates? Are the memory benefits from weight sharing still large enough to warrant using QSpec over such an approach?

### Soundness
3

### Presentation
3

### Contribution
2
