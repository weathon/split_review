# TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Current Retrieval-Augmented Generation (\textit{RAG}) systems concatenate and process numerous retrieved document chunks for prefill which requires a large volume of computation, therefore leading to significant latency in time-to-first-token (\textit{TTFT}). To reduce the computation overhead as well as TTFT, we introduce \textit{\turborag}, a novel RAG system that redesigns the inference paradigm of the current RAG system by first pre-computing and storing the key-value (\textit{KV}) caches of documents offline, and then directly retrieving the saved KV cache for prefill. Hence, online computation of KV caches is eliminated during inference. In addition, we provide a number of insights into the mask matrix and positional embedding mechanisms, plus fine-tune a pretrained language model to maintain model accuracy of \turborag. Our approach is applicable to most existing large language models and their applications without any requirement in modification of models and inference systems. Experimental results across a suite of RAG benchmarks demonstrate that \turborag reduces TTFT by up to 9.4x compared to the conventional RAG systems (on an average of 8.6x), but reserving comparable performance to the standard RAG systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a kv caching computational technique that would significantly speed up (during inference time) the conventional RAG system in terms of time to first token (which would reduce user's wait time), and significantly reduce inference-time TFLOPs. In order to implement this technique, one would need to precompute the kv caches for all documents in a database. The paper makes the assumption that cross-attention between different retrieved documents are unnecessary, setting them to zero, which makes this computation technique an attention-approximation method. The paper reorder positional ids for the precomputed kv caches of the retrieved documents from a database, and using a fine-tuned LLM, it is able to achieve overall comparable performance on the RGB Benchmark as a gpt-4o powered conventional RAG system with some performance degradation in high-noise setting.
This computational technique is applicable to the following resource-constrained setting: an organization that has large storage space to store all pre-computed kv caches, has the hardware to fine-tune large language models (>=7B), has a preference to use open-sourced LLM (that use relative positions as positional embeddings) as generator rather than commercially available ones such as GPT-4o, whose user query instances and documents in database satisfy the assumption that cross-attention between documents are unnecessary for answer user queries, and is concerned about optimizing inference time.

### Strengths
This paper introduces a new computational technique that would speed up the inference time of an open-sourced RAG system. The paper makes the observation and subsequently the assumption that cross-attention between documents during inference is unnecessary. To avoid doing so would reduce significantly computation during inference. Therefore, this computational technique can be viewed as an attention-approximation. This assumption seems to hold for current RAG benchmarks such as RGB and LongBench multi-doc QA. This paper is written with sufficient motivation , and is able to explain its proposed computational technique with clarity. This paper identifies two technical problems with naively concatenating pre-computed kv caches, i.e. misrepresentation of positional ids, and a pre-trained LLM would suffer from distributional shift with reordered positional ids. The paper then proceeds to solve these two problems by using either composite or reordered positional ids, and then fine-tune a pre-trained LLM. In the experiment section, the paper shows that on RGB benchmark, turboRAG is only slightly worse than gpt-4o based naive RAG, and is significantly better than Qwen-7B based naive RAG. On 4 datasets from LongBench, this paper shows that turboRAG achieves 9x speedup and significant inference-time resource saving over Qwen-7B based naive RAG.

### Weaknesses
1. insufficient related work discussion. TurboRAG essentially uses an attention-approximation technique that assumes no cross-attention between different documents, this falls in line with many other work that manipulate and attempt to utilize the sparsity in attention maps. But few work along this line is mentioned and compared with the computational trick in turboRAG to convince me that it is a novel approach. This paper also reorders positional ids in RoPE, there are also many similar works that manipulate positional ids to various gains, such as efficiency in long-context inferencing, no such work is mentioned and compared with the positional id reordering trick used in the paper to convince me that is is a novel approach. Therefore, I would say the novelty and originality of this work is moderately low.


2. I am concerned about the limitations TurboRAG imposes on the research direction of RAG. As I wrote in the summary section, TurboRAG requires model fine-tuning which rules out most commercial LLMs. TurboRAG also requires a significant amount of offline processing and storing all precomputed kv caches, this is generally not feasible with real-life database. This paper does not discuss storage cost and time for offline kv computation. Lastly, the assumption made in paper (cross-attention between documents are unnecessary) would limit future work that adapts this technique and prevent them to explore harder, more challenging and more meaningful RAG tasks where the user query requires a careful synthesis of information in different documents, such as scientific document summarization, meta analysis generation etc. In fact, while some current benchmarks (5 explored in this paper, 4 from long bench and RBG) do not require information synthesis between different retrieved documents, this limitation in benchmarking resources should not be the cause to make provincial and limiting assumptions that would negatively impact future research efforts in RAG. FYI no limitation section is included in this work even though there is almost one spare page. Because of these limitations, I would incline to reject this paper in its current version.


3. I have some questions on the experiment evaluation sections that I will reserve to the Questions Section.

### Questions
1. First of all, it is unfair to use GPT-4o for a non-English benchmark because GPT-4o is predominantly trained for the English language. Second, why is the TFLOP, TTFT not reported for the RGB English dataset?

2. Why is gpt-4o's baseline not reported for the LongBench multi-doc QA datasets? I think there are plenty of space left to include these results.

3. Can the authors address the potential data contamination from its fine-tuning dataset to the 5 datasets used in the evaluation section (4 from long bench and 1 from RGB). Musique, wikimqa and hotpotqa are primarily based on wikipedia articles, and many datasets used in Table 6 are also based on wikipedia articles. Also, HotpotQA is included in table 6, why is it also used for testing?

4. I think the paper would benefit if the authors show this turboRAG technique is applicable to other LLMs, such as the more recent state-of-the-art Llama3.1 8B and 70B.

5. Currently, there is no link to code, model checkpoints and fine-tuning data. This raises issue of reproducibility.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
1. This paper introduces TurboRAG, a novel approach to improve the performance of Retrieval-Augmented Generation (RAG) systems without sacrificing accuracy. 
2. A new pipeline that decomposes the prefill stage of conventional RAG systems into offline and online phases, significantly reducing the overhead of key-value (KV) cache computation.
3. Techniques to handle attention mask and position IDs to maintain model accuracy, including:


                    a.  Independent attention between document chunks. 
                    b.  Rearranged position IDs for concatenated KV caches


5. A fine-tuning approach to adapt language models to the new attention and position ID patterns.
6. Substantial improvement in time-to-first-token (TTFT) performance, achieving up to 9.4x speedup (8.6x on average) over state-of-the-art multi-document QA benchmarks without compromising accuracy.
7. The authors demonstrate that TurboRAG maintains comparable accuracy to conventional RAG systems on document QA tasks, even under high-noise conditions. They also show that the approach does not significantly impact the model's general capabilities across various tasks.
8. TurboRAG's key innovation lies in precomputing and storing KV caches for document chunks offline, then directly utilizing these caches during online inference. This approach significantly reduces computational overhead and improves inference efficiency, particularly for applications with strict latency requirements.
9. The paper provides experimental results on multiple benchmarks, including RGB and LongBench, to validate the effectiveness of TurboRAG in terms of accuracy and performance. The authors also discuss the impact on batch size scaling and overall system efficiency.

### Strengths
*Originality:*
1. Introduces TurboRAG, a novel approach to accelerate Retrieval-Augmented Generation (RAG) systems by precomputing key-value (KV) caches for document chunks offline.
2. Proposes innovative techniques to handle attention masks and position IDs to maintain model accuracy while using precomputed KV caches.
3. Redesigns the RAG inference paradigm by transforming the online computation of KV caches for retrieved documents into a hybrid offline-online process.

**Quality:**
1. Provides a comprehensive experimental evaluation across multiple benchmarks, including RGB and LongBench.
2. Demonstrates significant performance improvements, achieving up to 9.4x speedup in time-to-first-token (TTFT) compared to conventional RAG systems.
3. Conducts thorough regression tests to ensure the proposed modifications do not negatively impact the model's general capabilities.
4. Presents detailed ablation studies on different configurations (TurboRAG-composite and TurboRAG-reordered) and analyzes their performance under various noise ratios.

**Clarity:**
1. Well-structured paper with clear sections outlining the problem, methodology, and experimental results.
Includes informative figures (e.g., Figure 1 and Figure 2) that effectively illustrate the differences between standard RAG and TurboRAG approaches.
2. Provides clear explanations of technical concepts, such as the attention mask matrix and position ID rearrangement.
Significance:
3. Addresses a critical performance bottleneck in RAG systems, potentially enabling their application in latency-sensitive scenarios.
Achieves substantial improvements in TTFT without compromising accuracy, which could have broad implications for real-world RAG applications.
4. Proposes a method that is applicable to most existing large language models without requiring modifications to the models or inference systems.
5. Reduces computational resource utilization during online inference by 98.46% compared to standard RAG, significantly increasing the maximum supported batch size and enhancing throughput.

Overall, the paper presents a novel and significant contribution to the field of RAG systems, offering a well-executed and clearly explained approach to improve their performance while maintaining accuracy. The potential impact on real-world applications and the broader applicability of the proposed techniques add to the paper's significance in the field of natural language processing and information retrieval.

### Weaknesses
 **Limited exploration of trade-offs:**
The paper focuses primarily on the benefits of TurboRAG but does not thoroughly explore potential drawbacks or limitations. For instance: The authors do not discuss the storage requirements for precomputed KV caches, which could be substantial for large document collections. There's no analysis of how TurboRAG might impact memory usage during inference, especially for scenarios with many retrieved documents. A more balanced discussion of these trade-offs would provide a clearer picture of TurboRAG's applicability in different settings.

 **Limited comparison to other optimization techniques:** The paper primarily compares TurboRAG to a naive RAG implementation. However, it doesn't extensively compare against other recent optimization techniques for RAG systems or long-sequence processing, such as Efficient attention mechanisms (e.g., Performer, Reformer) and Other caching strategies or optimization approaches for RAG systems . A broader comparison to other RAG optimization approaches in addition to native RAG and also to other LLM architectures would help contextualize TurboRAG's contributions within the current state of the art.

 **Limited discussion of scalability:** The paper demonstrates impressive speedups, but doesn't extensively discuss how TurboRAG scales with increasing document collections at scale or query complexity. Additional experiments or analysis on scalability would strengthen the paper's claims about TurboRAG's broader applicability.



### Questions
1. Could the authors provide an analysis of the storage requirements for TurboRAG compared to conventional RAG systems? This information would help readers understand the trade-offs involved.

2. How does TurboRAG impact memory usage during inference, especially for scenarios with many retrieved documents? An analysis of memory consumption would provide a more complete picture of the system's efficiency.

3. How does TurboRAG compare to other recent optimization techniques for RAG systems or long-sequence processing, such as efficient attention mechanisms (e.g., Performer, Reformer) or other RAG caching and optimization strategies?

4. how does TurboRAG scale with increasing document collections or query complexity?

5. The paper focuses on a specific LLM architecture. Have the authors tested or considered how TurboRAG might apply to other popular LLM architectures? This information would be valuable for understanding the broader applicability of the approach.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors of this paper propose the TurboRAG framework, which allows documents to be encoded offline by an LLM and used later for any retrieval augmented generation task. Their main contribution is the idea that a model can be fine-tuned in order to enhance its robustness to missing sections of the KV-cache, since the retrieved document KV-caches will be independent of each other (retrieved documents will not be able to attend to each other directly). This allows for a 5 to 10 times speedup in terms of the "time-to-first-token" without any significant performance degradation in both RAG and standard generation tasks.

### Strengths
- The paper is well written and clear.
- Allowing LLMs to pre-compute the KV cache of a document for later use could significantly speed-up RAG applications and reduce their computational requirements.
- Their fine-tuning methodology is simple, intuitive and apparently quite effective in allowing models to leverage independently retrieved KV-cache information.
- Their approach leads to no performance degradation in tasks outside of RAG.

### Weaknesses
 - It is unclear whether the efficiency improvements are significant when the retrieved documents are short (efficiency improvements are only measured with 8-16k tokens. I believe that most RAG settings will be mostly working with shorter prompts than that. For example, the supporting passages in multi-hop QA datasets within LongBench are actually only around 200 tokens each.
- The metrics presented in the results sections are not well specified.
- The table column and row titles are, especially for Table 2 and 3, need to be properly capitalized and formatted.
- It's unclear if the reported speedups account for the overhead of transferring the pre-computed KV-cache from CPU to GPU memory, which could be non-negligible for shorter sequences. This overhead could potentially negate the benefits of pre-computation when dealing with smaller retrieved documents.
- The paper does not explore the potential of using the pre-computed KV-cache representations for retrieval itself, which could reduce the need for a separate encoding model. This is a missed opportunity to streamline the pipeline and reduce computational costs.
- The observation that the Naive RAG model underperforms the Turbo reordered RAG model in English LongBench QA tasks is peculiar and lacks sufficient explanation. It raises concerns about the robustness of the baseline and the experimental setup.
- The fact that HotpotQA and DuReader are part of the fine-tuning data to enable TurboRAG and also the main experimental setting is makes it harder to tell if the method can truly generalize. Are we at least fully certain that there is no data leakage?

### Questions
- As referred to in the weaknesses, how long must the retrieved prompt be in order to offset the latency created by moving the KV cache from the CPU to the GPU? It seems that it went from 10x to 4x with only a difference of around 4k tokens.
- Did you have any experiments on using the KV cache representations to enhance retrieval itself? It seems awkward to have to encode all documents with two models offline.
- Is there any reason why you would expect the Naive RAG model would underperform Turbo reordered RAG model in english LongBench QA tasks? This seems very strange to me.
- The fact that HotpotQA and DuReader are part of the fine-tuning data to enable TurboRAG and also the main experimental setting is makes it harder to tell if the method can truly generalize. Are we at least fully certain that there is no data leakage?

### Soundness
3

### Presentation
2

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
The paper proposes caching key-value (KV) pairs for all documents within a Retrieval-Augmented Generation (RAG) system to reduce the overhead of KV cache computation during inference. Additionally, it introduces simple techniques for reordering position embeddings to optimize performance.

### Strengths
1. The paper is well-written and easy to follow, making the proposed techniques accessible to readers.

2. The proposed pipeline for RAG demonstrates a significant decrease in time to first token (TTFT), showcasing practical improvements in efficiency.

### Weaknesses
1. While the idea of precomputing the KV cache to reduce TTFT is effective, it is not particularly novel. Prior work, such as  [1], has already explored precomputing KV caches to achieve similar objectives. Although this paper mentions RAGCache, it lacks a thorough discussion that differentiates the proposed methods from existing approaches. Including a detailed comparison with RAGCache in both methodology and experimental results would strengthen the paper’s contribution.

2.  While precomputing document KV caches can effectively reduce TTFT, it increases storage costs, as each document needs a separate set of KV caches for different models. It is important for the paper to mention this storage issue so that readers can understand the potential trade-offs involved.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
