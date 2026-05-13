# Running Huge Context Windows On Tiny GPUs

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
There is growing demand for large language models that can process hundreds of thousands or even millions of input tokens. Inference at this extreme scale demands significant computational resources and costs. To address the inference time costs associated with running self-attention based transformer language models on long contexts, we propose a tunable mechanism that reduces the cost of the forward pass by attending to only the most relevant tokens at every generation step using a top-k selection mechanism. We showcase the efficiency gains afforded by our method by performing inference on context windows up to 1M tokens using approximately 16GB of GPU RAM. Our experiments reveal that models are capable of handling the sparsity induced by the reduced number of keys and values. 
By attending to less than 1% of input tokens, we achieve over 95% of model performance on common long context benchmarks (LM-Eval, AlpacaEval, and RULER).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a top-k attention mechanism aimed at reducing GPU memory usage to enable processing at the million-token scale on a single GPU. The authors highlight the sparsity of the attention matrix, where only a small subset of vectors meaningfully contribute to the attention scores, making much of the computation redundant. To address this, they propose a method that retrieves only the keys with the highest attention scores, leveraging a vector database in CPU memory. This allows attention computation to focus on the top contributors, while the retrieval is optimized using approximate k-nearest neighbor search, achieving sublinear complexity. This approach enables efficient long-context inference by offloading memory requirements to CPU without the overhead of full attention computation. Experiments show that the method achieves over 95% accuracy on common benchmarks, even with a relatively small top-k value.

### Strengths
The paper is well-written, with thoughtfully designed figures and diagrams that effectively illustrate the authors' top-k-based attention mechanism. The benchmarks clearly demonstrate performance variations with different top-k selections, and the design is well-motivated by the sparsity present in each layer of the attention scores—Figures 1, 2, and 3 showcase the feasibility of the proposed method convincingly.

While this approach shares similarities with RAG, it specifically focuses on top-k retrieval in the KV cache, preserving the model's zero-shot and reasoning capabilities. The method shows strong adaptability across transformer-based models and offers promising potential for extending supported context lengths, which could have a substantial impact across the field.

### Weaknesses
The idea of exploiting sparsity in the attention mechanism is not entirely novel, as this work primarily focuses on reducing the number of tokens attended to. However, a significant challenge remains in ensuring that the method achieves reasonable inference speed while reducing GPU memory consumption.

While the authors propose leveraging plentiful and affordable CPU memory with a vector database for k-nearest neighbor retrieval, there is no benchmarking or analysis to demonstrate the impact of this design on inference speed, raising concerns about the practical adaptability of the proposed approach. Specifically, the overhead of transferring data between CPU and GPU for each attention layer could introduce significant latency, especially with larger context lengths, which is not addressed in the paper.

Another limitation is the lack of empirical benchmarks on GPU memory consumption after applying the method. Additional results in this area would greatly enhance the paper. It would be beneficial to see a comparison of memory usage with and without the method, across different context lengths and model sizes. This would provide a clearer picture of the actual memory savings achieved.

**Minor issue:**  In Algorithm 2, the formatting for the Softmax and attention score  `S`  sections is inconsistent, which could lead to confusion. Highlighting the modifications would help readers identify the primary changes. Additionally, clarifying the relationships between  `K_cache`  and  `K_cache_gen`, as well as  `V_cache`  and  `V_cache_gen`, could improve comprehension.

### Questions
1. What is the GPU memory consumption after applying this method? Can we quantify the reduction based on the provided parameters?
2. How does the CPU memory vector database handle efficient searching? Are there any benchmark results available for inference speed?
3. What is the expected maximum context length for a given model with this method? Can we estimate it based on GPU memory constraints and model parameters?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a KV cache compression method designed to enable longer context generation for large language models (LLMs) on memory-constrained GPUs. It maintains a comprehensive KV cache database on CPU memory and selectively transfers a top-k subset to GPU memory for efficient attention calculation. The method is evaluated through attention score analysis, a hyper-parameter 
𝑘
k ablation study, and tests on huge context generation. 

The results show over 95% accuracy on standard benchmarks while utilizing only 1% of the total context length, demonstrating significant memory efficiency.

### Strengths
Relevance: The paper addresses the critical and timely challenge of enabling long context generation in large language models under resource constraints, an essential topic for efficient LLM inference.

Effectiveness and Simplicity: The proposed method offers a simple yet effective approach to offloading KV caches, making it practical for implementation while delivering significant memory efficiency.

### Weaknesses
1. Lack of Comparative Analysis: The paper does not provide a comparison with related or concurrent works on KV cache sparsity, such as H2O and "Model Tells You What to Discard," missing an opportunity to contextualize its contributions within the broader research landscape. Additionally, there is an absence of detailed system-level performance metrics, such as latency, throughput, and supported context length, which are crucial for understanding the practical efficiency of the method.

2. Latency Concerns: The use of PCIe for data transfer between CPU and GPU may introduce significant latency overhead, which is not addressed in the paper.

3. Limited Dataset Scope: The evaluation does not include reasoning datasets (e.g., GSM8K, MATH), potentially overlooking the method’s impact on tasks that require strong reasoning capabilities.

4. Limited Acceleration Capability: The method can only accelerate the decoding stage but not the prefill stage. This limitation means that running the model on a single GPU with long context lengths is infeasible unless the prefill stage is computed using more powerful machines or other algorithms.

### Questions
1. Comparison with Other KV Cache Sparsity Works: The reviewer questions how this method compares with existing KV cache sparsity approaches. While the paper claims that extracting less than 1% of tokens still yields a high accuracy, other methods like Attention Sink, H2O, and "Model Tells You What to Discard" experience significant accuracy drops when reducing the KV cache to less than 30%. The reviewer seeks clarity on what makes this approach more effective.

2. Lack of Latency/Throughput Justification: The reviewer points out that the paper does not provide latency or throughput measurements. They emphasize the importance of system-level performance analysis, as highlighted in the weaknesses section.

3. Performance on Reasoning and Math Datasets: The reviewer asks about the method’s performance on challenging datasets, such as reasoning tasks (e.g., GSM8K) and math datasets (e.g., MATH), to evaluate how well the approach generalizes to tasks requiring strong reasoning capabilities.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a way of reducing the computational requirements of attention blocks during inference in an existing pretrained LLM without requiring modifications to the neural architecture or additional training, and does so with a minimal degradation of it's capabilities. While the proposed algorithm is an approximation of the full attention, it's soundness is backed with observations and empirical evidence.
Furthermore, the implications of using efficient kv-caching during inference is also fully explored, which allows this method to be used as a drop-in addition to the attention algorithm used in most transformer LLMs.

### Strengths
- The problem is well motivated and very important. Runtime drop-in efficiency improvements to LLMs is preferable, especially without requiring additional training because pretraining is expensive and a single architecture might not fit all use cases. Some might prefer the accuracy of full attention while others require the speed of approximate attention. In both cases, the same pretrained model can be used, massively reducing pre-training compute requirements.
- Describes the implementation of a top-k kv-cache. This method can be easily adapted for use within a kv-cache accelerated inference framework.
- Solid and sound evals using AlpacaEval, Open LLM Leaderboard and RULER datasets. Testing both short and long context capabilities of top-k attention.

### Weaknesses
 - Top-k attention as it stands by itself is not a novel algorithm, many papers have proposed it in the past, but not in the context of transformer LLM inference with kv-caching.
- A lack of comparison with other approximate attention algorithms with regards to benchmark scores and speed. (Why should we use this method rather than other more proven methods?)
- No table or numbers showing the compute and memory improvements. A paper focusing on inference efficiency should at least provide a few numbers in a table or graph showcasing the potential compute/memory savings.

### Questions
- How does this method scale to bigger models? If I understand correctly, the memory and compute savings should be larger and larger given that bigger transformer LLMs have more attention layers in general?
- In the paper, the author(s) notes a similarity to RAG, but why is there no comparison in the benchmarks? RAG is currently much more proven and highly efficient. It is currently unclear in the paper whether a naive top-k attention is really superior to it in practice without actual benchmarks.

### Soundness
3

### Presentation
3

### Contribution
2
