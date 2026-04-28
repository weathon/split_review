# KV-Dict: Sparse KV Cache Compression with Universal Dictionaries

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Transformer has become the de facto architecture for Large Language Models (LLMs), yet its substantial memory required for long contexts make it costly to deploy. Managing the memory usage of the key-value (KV) cache during inference has become a pressing challenge, as the cache grows with both model size and input length, consuming significant GPU memory.

We introduce a novel post-training KV cache compression method using KV-Dict, a universal dictionary that can accurately decompose and reconstruct key-value states. Unlike traditional quantization methods, KV-dict leverages sparse dictionary learning, allowing for flexible memory usage with minimal performance loss through fine-grained controls of sparsity levels. Moreoever, we retain competitive performance in the low memory regimes that 2-bit compression struggles to offer.

KV-Dict is remarkably universal, as it uses a small, input-agnostic dictionary that is shared across tasks and batches without scaling memory. This universality, combined with the ability to control sparsity for different memory requirements, offers a flexible and efficient solution to the KV cache bottleneck, maintaining strong performance on complex reasoning tasks, such as LongBench and GSM8k.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is on the challenge of deploying large language models (LLMs) – the memory consumption required to manage the key-value (KV) cache during inference. The paper proposes a method, KV-Dict, which uses a sparse dictionary-based approach for post-training KV cache compression.

### Strengths
The paper introduces sparse dictionary learning as a method to approximate KV cache compression, which seems to be a new contribution.
The KV-Dict method demonstrates comparable performance vs. a recent study KIVI.

### Weaknesses
 - The study primarily compares KV-Dict with KIVI, which, while valuable, may not provide a comprehensive view of its effectiveness relative to other potential KV cache compression techniques. Additional comparisons with more methods would strengthen the validity of the approach and its claims.
- Although KV-Dict is claimed to be universal across different inputs, the paper could benefit from a more detailed explanation and empirical studies of this claim. Demonstrating the effectiveness across a broader range of tasks and input distributions would help substantiate this claim.
- While the approach is technically sound, it may not introduce significantly new dimensions to the KV cache compression problem beyond the use of sparse dictionary learning. Highlighting new aspects of KV cache compression could enhance the paper’s contribution.

### Questions
- What was the primary motivation behind designing KV-Dict as a universal dictionary rather than task-specific dictionaries? Is this approach primarily for memory savings, or are there anticipated advantages in model generalizability?
- For a model such as Llama-3-8B, could the authors detail the procedure for model serving with KV-Dict? The paper mentions that dictionary learning was performed using WikiText-103. Is this same dictionary applied directly during prefilling and decoding stages, or would additional fine-tuning be necessary?
- Could the authors clarify the mechanism for obtaining compressed Key and Value states at model serving time? Is the dictionary pre-computed and directly used, or is there a dynamic adaptation of the dictionary as new inputs are processed?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces KV-Dict, a method for compressing the key-value (KV) cache in Transformer-based Large Language Models (LLMs) to address the significant memory demands during inference caused by the KV cache growing proportionally with model size and input context length. KV-Dict leverages a small, universal dictionary as an overcomplete basis to sparsely decompose and accurately reconstruct KV states using sparse dictionary learning techniques, specifically Orthogonal Matching Pursuit (OMP). This approach captures low-dimensional structures within the KV cache, allowing for significant compression (3-8×) with minimal reconstruction error. By providing fine-grained control over sparsity levels, KV-Dict enables users to balance memory savings against performance loss, achieving near-lossless performance even in low-memory regimes where traditional quantization methods struggle. The method is universal and input-agnostic, simplifying deployment across different tasks and batches without retraining or scaling memory. KV-Dict maintains strong performance on complex reasoning tasks like LongBench and GSM8K, offering an efficient, off-the-shelf solution for pre-trained LLMs to alleviate the KV cache bottleneck by exploiting redundancy and low-dimensional structures in KV states.

### Strengths
- There is a comprehensive set of experiments and ablations to validate the hypothesis and methods presented in this work.
- The problem is relevant and very practical. KV-Cache compression is a key bottleneck for LLM development.
- Speed and performance is competitive across a wide suite of benchmarks

### Weaknesses
### Major
- Writing: The writing in this paper is hard to follow and at some points it is hard to understand the motivation for why things are being done. After reading the abstract for example, I am unable to tell wether this is a sparsity based method or quantization method or both. There are also a bunch of grammatical errors littered around the paper that make it hard to read e.g "such dictionary does not scale" line 095.
- Besides, performance on benchmarks it would be great to see some qualitative results with samples to see what the output from LLMs using KV-Dict look like compared to those from a few other methods or when using the full KV-cache without compression.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The KV cache of Large Language Models (LLMs) scales in proportion to both the model size and input sequence length, resulting in increased GPU memory usage. This poses significant constraints when deploying LLMs. To address this limitation, this paper proposes a novel method called KV-Dict, which compresses the KV cache efficiently. KV-Dict leverages sparse dictionary learning to reconstruct the KV cache in a near-lossless manner using a small calibration dataset. For creating sparse representations, it employs Orthogonal Matching Pursuit (OMP), and the dictionary is directly learned through gradient updates. The proposed method demonstrates higher accuracy compared to existing approaches and maintains satisfactory accuracy even at higher compression ratios than 2-bit quantization.

### Strengths
- The proposed method exhibits higher accuracy than existing KV cache compression methods at equivalent compression rates, demonstrating its superiority in preserving model performance under constrained memory settings.
- It achieves a higher compression rate than 2-bit quantization while maintaining robust and dependable accuracy, indicating its resilience even under significant compression.
- Despite performing compression using the Wikitext dataset, the method achieves commendable accuracy on the GSM8K dataset, illustrating its adaptability and generalization across different data types.

### Weaknesses
 - Absence of throughput measurements: Given that a primary motivation for KV cache compression is to reduce GPU memory consumption, thereby enabling an increase in batch size and improving throughput, the paper would benefit from comparative throughput results against methods such as KIVI. This would provide a clearer picture of the practical benefits of KV-Dict in real-world deployments.
- Increased latency: Although this method achieves impressive compression rates and accuracy, it does so at the cost of increased latency, which may impact the feasibility of its deployment in latency-sensitive applications. The paper lacks a thorough analysis of the latency overhead, especially in end-to-end scenarios, making it difficult to assess the practical implications of this trade-off.
- Limited experimental validation across varying model sizes: The majority of experiments have been conducted on models in the 7B/8B range. Additional validation on both larger and smaller models would strengthen the findings, particularly to assess whether the dictionary exhibits universal properties across diverse model sizes. Furthermore, the paper does not explore the sensitivity of the method to different model architectures, which could impact its general applicability.

### Questions
- What is the end-to-end latency? While the paper provides latency measurements for each component in Table 5 and notes that minor overhead is introduced due to parallel processing, an actual end-to-end latency measurement would be beneficial to understand the full extent of this overhead in practice.
- What batch size was used in the latency measurements?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the memory challenges of deploying Transformers in Large Language Models (LLMs), specifically focusing on the key-value (KV) cache, which grows with both model size and input length, consuming extensive GPU memory during inference. To tackle this, the authors introduce KV-Dict, a novel post-training compression technique for the KV cache. KV-Dict uses sparse dictionary learning to decompose and reconstruct key-value states, distinguishing itself from traditional quantization methods by providing flexible memory usage and fine-grained sparsity control with minimal performance loss.

### Strengths
1. This method uses a dictionary method for compression of KVCache, which is quite a less developed method in this topic

### Weaknesses
1. The problems stated in the introduction section are not well answered in the following sections. The paper stated two problems: “off the shelf” consideration and the problem of eviction strategies under long contexts. However, the experiments use KIVI, which is “off the shelf” (even more it doesn’t need training a dictionary) neither does it use eviction strategies.
2. The motivation is unclear. The introduction talked about the long context, but the abstract talked about reasoning tasks like GSM8k. Most questions+answers in GSM8k are below 800 characters, do we really need KVCache compression? how much gain can we get?
3. Generalizability issues: Based on Figure 2, it seems like 48 tokens contain 8 independent clusters, which requires at least 8 atoms. Then for N=4096, does it mean maybe it can only represent KVCache that are at most 24K long? Thus is this really Universal?
4. Value Cache issue: Still Figure 2, it actually gives a stronger implication than the author’s statements: the key cache is always similar to the key cache close to it, no matter what the content is. This is very strong, and does this also apply to the Value cache? If yes, this is counterintuitive, can you explain it? if not, is this method universal?

### Questions
The above questions as well as the following

1. For Table “top-k perceptron” what is “top” defined as? how do you select to make the autoencoder sparse? Since this seems weird that if the autoencoder converges why it cannot beat OMP which is a greedy method?

2. what about the Latency Comparison with KIVI?

3. For training, how do you initialize the dictionary? isn’t this important?
4. also for training, you didn’t specify clearly in the experiments section what is the training data for the dictionary, is it also wikitext as in Table 1? this is important to claim the generalizability of your method.

### Soundness
2

### Presentation
2

### Contribution
3
