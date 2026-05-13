# Long Context Compression with Activation Beacon

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Long context compression is a critical research problem due to its significance in reducing the high computational and memory costs associated with LLMs. In this paper, we propose Activation Beacon, a plug-in module for transformer-based LLMs that targets effective, efficient, and flexible compression of long contexts. To achieve this, our method introduces the following technical designs. 
1) We directly compress the activations (i.e. keys and values at every layer), rather than leveraging soft prompts to relay information (which constitute a major bottleneck to encapsulate the complex information within long contexts).
2) We tailor the compression workflow, where each fine-grained input unit is progressively compressed, enabling high-quality compression and efficient computation during both training and inference. 
3) We train the model through compression-based auto-regression, making full use of plain texts and instructional data to optimize the model's compression performance.
4) During training, we randomly sample a compression ratio at each step, teaching the model to support a wide range of compression configurations. 
Extensive evaluations are conducted on various long-context tasks whose lengths (e.g., 128K) may far exceed the maximum training length (20K), such as document understanding, few-shot learning, and Needle-in-a-Haystack. 
Whilst existing methods struggle to handle these challenging tasks, Activation Beacon maintains a comparable performance to the uncompressed baseline across various scenarios, 
achieving a 2x acceleration in inference time and an 8x reduction of memory costs for KV cache.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces “Activation Beacon,” a plug-in module to conduct long-context compression for LLMs. The proposed approach progressively compresses the activations at each layer and can be trained in the conventional auto-regressive way of language modeling. The authors demonstrate the benefits of this approach through evaluations on various long-context tasks for compression quality and inference efficiency.

### Strengths
- Compressing by chunks at each layer avoids the need for recomputation and addresses gradient back-propagation challenges present in some prior baselines that rely on recursive dependencies from final-layer outputs. This design enhances both training and inference efficiency.
- The chunking approach and the interleaved insertion of beacon tokens are straightforward and intuitive.
- Evaluations on various benchmarks indicate that the proposed approach generally outperforms the KV cache compression and “soft-prompt” compression baselines, achieving notable reductions in both inference time and memory usage.
- Training with randomly sampled compression ratios enables flexible compression ratios during testing.

### Weaknesses
 - In addition to LongBench and NIAH, it is essential to evaluate the proposed approach on newer, more challenging benchmarks, such as RULER [1].
- Some recent context compression baselines, including CEPE [2] and LLoCO [3], are not discussed in the paper and should be included for a more comprehensive discussion or comparison.
- How are rotary embeddings managed for the beacon tokens? Although the LLM processes a fixed chunk at a time, the relative positions of the beacon tokens vary across chunks. How are positional embeddings applied in these cases?
- Additional parameters are added and fine-tuned for self-attention projections specific to the beacon tokens. What is the impact of these added parameters on VRAM usage and latency? If the cost is significant, could LoRA fine-tuning be effective for the proposed activation beacons approach?
- What portion of time is allocated to prefilling and decoding? While the proposed method reduces some recomputation, it may require customized attention masks or iterative context processing, which could lack efficient kernel implementation or result in extra kernel calls. Please provide a latency breakdown of prefilling and decoding for specific workloads (e.g., 32/128k context, 128 decoded tokens) and compare it with the flash attention full-context baseline.
- How does the proposed approach affect fine-tuning throughput? Please compare its performance with Full-FT.

### Questions
- How are rotary embeddings managed for the beacon tokens? Although the LLM processes a fixed chunk at a time, the relative positions of the beacon tokens vary across chunks. How are positional embeddings applied in these cases?
- Additional parameters are added and fine-tuned for self-attention projections specific to the beacon tokens. What is the impact of these added parameters on VRAM usage and latency? If the cost is significant, could LoRA fine-tuning be effective for the proposed activation beacons approach?
- What portion of time is allocated to prefilling and decoding? While the proposed method reduces some recomputation, it may require customized attention masks or iterative context processing, which could lack efficient kernel implementation or result in extra kernel calls. Please provide a latency breakdown of prefilling and decoding for specific workloads (e.g., 32/128k context, 128 decoded tokens) and compare it with the flash attention full-context baseline.
- How does the proposed approach affect fine-tuning throughput? Please compare its performance with Full-FT.

I am open to adjusting my ratings if all concerns and questions are adequately addressed.

### Soundness
2

### Presentation
2

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
The paper introduces "Activation Beacon", a compression method designed to enhance long-context processing efficiency in LLMs. The approach compresses the activations of keys and values in transformer layers, avoiding bottlenecks associated with traditional soft prompt methods. Additionally, a progressive compression workflow compresses each context unit in chunks, allowing the model to handle longer contexts than the original LLM's window. Experimental results show Activation Beacon achieves significant memory and computation savings, with minimal loss in performance.

### Strengths
1. Activation Beacon reduces inference time by 2x and KV cache memory costs by 8x compared to the uncompressed baseline.

2. The method supports adaptive compression ratios, allowing flexibility for different tasks and contexts.

3. The proposed model maintains short-context capabilities, preserving the performance of the original LLM.

### Weaknesses
1. The performance of this method may vary with model size. Current evaluations focus on medium-sized models, lacking validation on larger-scale models, leaving its effectiveness and applicability in very large models underexplored. Specifically, the paper does not address how the compression ratio and the size of the beacon tokens would scale with larger models, which might require different configurations to maintain performance. The current results might not generalize well to models with significantly different architectures or parameter counts.

2. The added complexity of managing beacon tokens and compression ratios increases implementation overhead for end-users, particularly when adapting to different tasks. In addition to actual inference latency, specific memory usage data across implementations would help clarify practical resource requirements. The paper lacks a detailed analysis of the computational overhead associated with the compression and decompression steps, which could become a bottleneck for certain hardware configurations. Furthermore, the process of selecting optimal compression ratios for different tasks is not clearly defined, leaving it to the end-user to experiment and potentially leading to suboptimal performance.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper compresses activations (keys and values) rather than using soft prompts, facilitating a progressive, fine-grained compression process. Specifically, it first partition input into small chunks, interleaving special beacon tokens that accumulate contextual activations.

### Strengths
- The paper presents an efficient method to compress long contexts, reducing memory usage by up to 8x and speeding up inference by 2x.
- Its progressive, fine-grained compression approach maintains high compression quality, allowing the model to handle longer inputs than its built-in context window.
-It supports flexible compression ratios, preserving model performance across various long-context tasks without degrading short-context capabilities.

### Weaknesses
 - Lack of Comparison with KIVI: The paper does not provide a direct comparison with KIVI, a relevant compression method that could offer insights into the performance trade-offs. Specifically, the paper should analyze the performance differences given that KIVI focuses on numerical compression of KV cache while this paper focuses on sequence length compression. A comparison would highlight the strengths and weaknesses of each approach.
- GPU Time Omission: The paper does not report GPU training or inference time, leaving uncertainty around the practical computational cost and efficiency of the proposed method. While inference latency is mentioned, a more detailed breakdown of GPU time for both training and inference is needed to fully assess the method's practicality, including time spent on beacon token generation and compression.
- Scalability Concerns: The method requires 8 A800 GPUs to train a 7B parameter model, raising concerns about its scalability to larger models like 70B, where computational demands could become prohibitive. The paper should discuss the memory footprint and training time scaling with model size, providing a more comprehensive analysis of the method's feasibility for larger models.
- Limited Comparative Analysis: The paper would benefit from including more baseline methods, particularly compression-based approaches like KIVI, KV-layer shared compression methods such as CacheGen, and relative-position encoding strategies like LM-Infinite. A more thorough comparison with methods that compress along different dimensions of the KV cache (layer, head, channel, numerical) would provide a more complete understanding of the proposed method's advantages and limitations. Additional References Needed: Incorporating comparisons with relevant works, such as LM-Infinite [1] for dynamic context management, CacheGen [2] for efficient context loading, and KIVI [3] for asymmetric quantization of KV caches, would strengthen the evaluation and highlight the advantages and limitations of the proposed approach.

### Questions
overall, this paper is novel and idea is well presented. please add more techniques for comparison so that users can choose different method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a method called Activation Beacon for efficient long-context processing. The method adds learned "beacon" tokens at regular intervals in the input query. These tokens are expected to learn "summaries" of the text. At inference time, when processing long contexts, the beacon tokens are retained and the other context tokens are discarded. Thus, the beacon tokens essentially provide a summary of the context. The authors evaluate their method in comparison with a few other recent methods for efficient long context processing. Their method significantly improves results on LongBench and Multi-Needle-in-a-Haystack. The authors also provide ablations for various design choices.

### Strengths
- The paper focuses on an impactful area (long-context efficiency for LLMs).
- The paper provides a relatively simple idea that is well-explained. I view simplicity as a plus - if a simple idea can give strong accuracy improvements, it's far better than an unnecessarily complicated idea.
- The paper demonstrates strong results. Table 2 demonstrates strong accuracy at good latency on standard benchmarks for long context. Their method is competitive with full fine-tuning and better than baselines. Table 1 provides strong accuracy as well (though latency is missing).
- The figures do a good job of explaining what's going on. Figure 1 and Figure 2 give nice overviews of the method.
- The method is computationally efficient compared to fine-tuning. Their "pretraining" (starting from an already-pretrained model) only requires 1B tokens which is very few.
- The paper ablates design choices (Table 4).
- The paper is generally well written.

### Weaknesses
 - In Table 1, it's not obvious whether the latencies are comparable. The compression ratio isn't mentioned.
- line 368: why do you use adaptive compression for llama-2 and uniform compression for qwen?

My main perceived weaknesses are regarding differences with previous works, and understanding why this method is performing so well:
- line 135: "ICAE and AutoCompressor... segment the long context into chunks and compress each chunk. However, both of them compress the context into soft tokens" <- how are these soft tokens different than beacon tokens? (similarly, on line 373-374, you mention soft tokens being a drawback)
- line 137: "Their compression workflow also lacks fine-grained handling of the chunked inputs, resulting in inferior compression quality" <- it seems like all they would need to do to allow "fine-grained handling of the chunked inputs" is just choose a smaller chunk size, so that the soft tokens appear more frequently. Is that right?
- - If this is true, it seems like your main contribution is the insight that soft tokens should be distributed evenly through the context. Would doing this massively improve the accuracy of ICAE and AutoCompressor? It seems like this is the main discovery, but I'm left wondering if I'm missing some more fundamental difference.

[Minor]:
line 47: "it it" -> "it"
line 53: "alternamtive" -> alternative
line 371: "highligh" -> "highlight"
line 483: "scope" -> score
Table 2: give units of "latency"

### Questions
My main question is in the "regarding differences with previous works" above. I want to understand if the results are improved mainly from decreasing chunk size, or if there's another difference between soft tokens and beacon tokens that explains the difference.

Also, what window size do you use? From Table 1, your model has a context length of 32k. I'm guessing you use this window size, but I don't see it explicitly stated, and line 184 suggests that 1024 would be a common window size, so I'm not sure. Since LongBench has only a few examples above 32k, I'm guessing the window logic isn't really used much (unlike for Needle In a Haystack)

### Soundness
3

### Presentation
3

### Contribution
3
