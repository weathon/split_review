# Palu: KV-Cache Compression with Low-Rank Projection

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Post-training KV-Cache compression methods typically either sample a subset of effectual tokens or quantize the data into lower numerical bit width. However, these methods cannot exploit redundancy in the hidden dimension of the KV tenors. This paper presents a hidden dimension compression approach called Palu, a KV-Cache compression framework that utilizes low-rank projection to reduce inference-time LLM memory usage. Palu decomposes the linear layers into low-rank matrices, caches compressed intermediate states, and reconstructs the full keys and values on the fly. To improve accuracy, compression rate, and efficiency, Palu further encompasses (1) a medium-grained low-rank decomposition scheme, (2) an efficient rank search algorithm, (3) low-rank-aware quantization compatibility enhancements, and (4) an optimized GPU kernel with matrix fusion. Extensive experiments with popular LLMs show that Palu compresses KV-Cache by 50% while maintaining strong accuracy and delivering up to 1.89× speedup on the RoPE-based attention module. When combined with quantization, Palu’s
inherent quantization-friendly design yields small to negligible extra accuracy degradation while saving additional memory than quantization-only methods and achieving up to 2.91× speedup for the RoPE-based attention. Moreover, it maintains comparable or even better accuracy (up to 1.19 lower perplexity) compared to quantization-only methods. These results demonstrate Palu’s superior capability to effectively address the efficiency and memory challenges of LLM inference posed by KV-Cache.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the issue of high GPU memory consumption in KV Cache during LLM inference by proposing a novel approach that differs from traditional KV Cache compression methods (such as quantization and token-level compression). Specifically, it employs Singular Value Decomposition (SVD) to reduce the rank of the KV Cache matrix, thereby decreasing its memory usage. Building on this method, the paper further explores several enhancements, including: 1) merging multiple heads into a group for SVD to minimize precision loss; 2) adaptively adjusting the compression ratio based on the redundancy of information at different layers; and 3) integrating the Walsh-Hadamard transform to facilitate quantization of the compressed results.

### Strengths
1.	The approach proposed in this paper, which utilizes Fisher information to allocate compression ratios for each linear layer, is both effective and scalable. It offers valuable guidance for other KV Cache and model parameter compression efforts.
2.	This paper implements a CUDA kernel to maximize throughput efficiency.
3.	This paper proposes and experimentally validates the compatibility of its optimization methods with traditional techniques such as quantization and LoRA fine-tuning, ensuring their practical applicability in real-world environments.
4.	This paper conducts comprehensive ablation experiments to validate the effectiveness of each optimization module individually.

### Weaknesses
1.	The method proposed in this paper, which utilizes SVD for rank reduction of parameter matrices, is not novel, as it has been employed in various studies (e.g., Sharma et al., "The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction," 2023). The corresponding optimization of KV Cache storage is consequently straightforward given the rank reduction of the parameter matrices.
2.	The paper does not provide open-source code, which raises concerns about the authenticity and reproducibility of their experimental results.
3.	The paper compares a limited number of related works; aside from the baseline, it only includes quantization-based methods such as Atom and KVQuant. However, token-level compression methods are also a key focus in the KV Cache compression field, which this paper completely overlooks. The authors should at least conduct comparative experiments and method combination studies with one of the state-of-the-art approaches in this area, such as H2O (Zhang et al., "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models," 2024).

### Questions
1.	Suggestion: The authors might consider adding a mathematical derivation section to demonstrate that the SVD method has an upper bound on the accuracy error resulting from the rank reduction of parameter matrices. This would enhance the generalizability and applicability of the method across different models and datasets.

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
The paper introduces Palu, a novel framework designed to compress the KV-cache of large language models (LLMs) using low-rank projection. Unlike existing techniques, such as quantization or token eviction, which may overlook redundancies in hidden dimensions, Palu effectively captures these latent efficiencies. Notably, it provides a post-training compression solution, in contrast to low-rank methods like GQA and MLA that require training from scratch. This approach allows Palu to strike a balance between memory efficiency, accuracy, and inference speed.

### Strengths
1. **Post-Training Solution:** Unlike MLA, which requires retraining from scratch, Palu can be applied post-training. This versatility allows for the compression of existing models without additional, costly training cycles.
2. **Balanced Accuracy and Efficiency:** The group-head low-rank decomposition (G-LRD) balances accuracy and computational efficiency. It preserves essential information while reducing reconstruction overhead compared to per-head and joint-head decompositions.
3. **Automated Rank Allocation:** By using Fisher information to dynamically assign ranks to matrices based on their importance, Palu ensures compression without significant accuracy loss. This approach optimizes each layer's sensitivity to compression.
4. **Quantization-Friendly Design:** Palu addresses quantization-induced outliers with a Hadamard transformation, effectively supporting low-bit quantization. This further enhances compression without compromising accuracy, yielding competitive perplexity scores compared to quantization-only methods.

### Weaknesses
1. **Inefficiency with Positional Encoding**: Palu requires reconstructing the original key cache when calculating positional encodings, which may reduce computational efficiency. This reconstruction process introduces a computational overhead that could potentially negate some of the benefits gained from compressing the KV-cache. The need to revert to the original key states for positional encoding calculations suggests a fundamental limitation in the approach, especially for models where positional information is critical.
2. **Performance on Complex Tasks**: Palu-50% does not outperform lower-compression 2-bit quantized KV-Cache methods, particularly on complex tasks like Code and Synthetic. This limitation suggests that Palu’s effectiveness may decrease in more challenging scenarios, where high compression ratios can impact accuracy. The fact that a more aggressive compression rate (50%) fails to surpass a lower compression rate with quantization highlights a potential weakness in Palu's ability to preserve information when pushed to its limits, especially on tasks that require intricate reasoning or pattern recognition.

### Questions
Is it possible to compress position embedding by similar way to remove the key cache reconstruction in attention computing? Or do some better tricks in attention computing rather than reconstructing key states?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Palu, a KV-Cache compression framework that reduces memory usage in LLM inference by applying low-rank projection to the hidden dimension. Palu decomposes linear layers into low-rank matrices, caching compressed intermediate states and reconstructing KV values on the fly. Key features include medium-grained low-rank decomposition, automated rank search, quantization compatibility enhancements, and a GPU-optimized matrix fusion kernel. Experiments show that Palu compresses KV-Cache by 50% and boosts attention module speed by up to 1.87×.

### Strengths
S1: The method creatively combines SVD algorithms with KV-cache compression, optimizing speed and grouping different attention heads with varied compression rates, which is insightful.

S2: The experiments are comprehensive, measuring both the algorithm’s accuracy and speed.

S3: The figures and tables are clear, and the descriptions are precise.

### Weaknesses
W1: In Section 3.1, the statement "However, this approach poses significant computational challenges during runtime that make it impractical for deployments" lacks experimental results and theoretical support, even though this claim is foundational to the proposed method.

W2: There is no theoretical proof for the accuracy of the proposed algorithm, such as bounded error analysis.

W3: The time complexity of the algorithm is not analyzed.

W4: In Section 4, the relationship between "compression rate" and "Avg. Bits" is unclear. Additionally, definitions of metrics such as "compression rate" are not specified.

W5: The code is not open-sourced, making reproducibility uncertain.

### Questions
Q1: Corresponding to W1, provide theoretical or empirical evidence for the statement in Section 3.1 that " However, this approach poses significant computational challenges during runtime that make it impractical for deployments "

Q2: Corresponding to W2, add a theoretical derivation of the algorithm's error bounds.

Q3: Corresponding to W3, include an analysis of the algorithm's time complexity.

Q4: Corresponding to W4, clarify the relationship between "compression rate" and "Avg. Bits" in Section 4, along with definitions of related metrics.

Q5: It is recommended to open-source the code.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Palu is a new framework for compressing the key-value cache in large language models, reducing memory usage and improving inference speed. It uses low-rank projection, group-head low-rank decomposition, and automatic rank allocation to achieve up to 50% KV-cache compression with minimal accuracy loss. Palu also integrates quantization compatibility and optimized GPU kernels, resulting in significant speedups, especially for long-context scenarios. The framework outperforms state-of-the-art quantization methods and demonstrates effectiveness across various LLMs and benchmarks.

### Strengths
- Novelty: unlike common quantization and pruning approaches, Palu uses low rank decomposition to lower the size of KV caches, which is more mathematically sound and doesn't require hardware changes.
- Significant compression is claimed, and it is to be expected that KV caches can be significantly compressed. However, I do have some concerns about the achieved compression which I cover in the weaknesses.
- Extensive empirical results spanning accuracy studies and speed-up analyses are provided.

### Weaknesses
 - While caching latent keys and values makes sense from the memory efficiency angle, it introduces significant computational overheads during decoding. Indeed, while the prefill phase can allow for GEMMs to occur at every layer, the decoding phase is all about GEMVs. However, in the palu framework, a full GEMM is required for to rematerialize each key and value matrix to be used in the attention module. This adds a lot of complexity, particularly when decoding a large output sequence length.
- What the paper really is doing is not KV cache compression, but really it is compressing the QKV WxA layer preceding attention by applying SVD on two thirds of the weight matrix. 
- The experimental setup doesn't make a lot of sense. It is mentioned that FlashAttention is not used for apples-to-apples comparison. But FlashAttention anyway is there to speed-up the prefill phase where the KV cache doesn't exist yet. Why does it then matter? Why are you including prefill latency when your solution is supposed to be addressing KV cache compression, which is used in the decoding phase?

### Questions
- In Table 1, why does Llama2-7B have better perplexity and accuracy than Llama3-8B-Inst? There is definitely something wrong in the experimental setup.
- Rather than compressing weights, since KV cache compression is desired, can a method such as ESPACE [1] be used to project activations to a low rank directly?
[1] Sakr, Charbel, and Brucek Khailany. "ESPACE: Dimensionality Reduction of Activations for Model Compression." arXiv preprint arXiv:2410.05437 (2024).

### Soundness
2

### Presentation
3

### Contribution
1
