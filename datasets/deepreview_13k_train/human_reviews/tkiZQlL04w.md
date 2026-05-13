# RazorAttention: Efficient KV Cache Compression Through Retrieval Heads

- Decision: Accept
- Scores: 8, 5, 6, 6, 5, 5, 5

## Abstract
The memory and computational demands of Key-Value (KV) cache present significant challenges for deploying long-context language models. Previous approaches attempt to mitigate this issue by selectively dropping tokens, which irreversibly erases critical information that might be needed for future queries. In this paper,  we propose a novel compression technique for KV cache that preserves all token information. Our investigation reveals that: i) Most attention heads primarily focus on the local context; ii) Only a few heads, denoted as retrieval heads, can essentially pay attention to all input tokens. These key observations motivate us to use separate caching strategy for attention heads. Therefore, we propose \blg, a training-free KV cache compression algorithm, which maintains a full cache for these crucial retrieval heads and discards the remote tokens in non-retrieval heads. Furthermore, we introduce a novel mechanism involving a ``compensation token'' to  further recover the information in the dropped tokens.  Extensive evaluations across a diverse set of large language models (LLMs) demonstrate that \alg achieves a reduction in KV cache size by over 70\% without noticeable impacts on performance. Additionally, \alg is compatible with FlashAttention, rendering it an efficient and plug-and-play solution that enhances LLM inference efficiency without overhead or retraining of the original model.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposed a method advocating keeping a full KV cache for retrieval/induction heads while adopting a StreamingLLM-like cache pattern for the rests. The proposed method claims to have strong long context performance and many efficiency perks.

### Strengths
1. The proposed method demonstrates decent performance, providing a significant improvement over many token dropping-based baselines.
2. The evaluation is thorough in terms of model coverages.
3. As recognized by many recent arts, being FlashAttention compatible is a prerequisite of being a pratical long context serving method, and this work fulfills this prerequisite.

### Weaknesses
1. The baseline methods (H2O and StreamingLLM) are dated and do not reflect the current SOTA of KV cache compression advancement. I understand if the authors do not intend to feature methods like KIVI or TOVA — as they are with different schools of approaches — but compare with sparse inference techniques like SnapKV or MInference are necessary.

The authors' discussion around L358 regarding SnapKV is faithful, as it corresponds to the findings of SharedContextBench (also submitted to ICLR here). However, SnapKV — and, in essence, methods like LoCoCo and LESS — are still worth featuring since we can almost always find weaknesses in any method. The authors should consider adding some quantifiable evaluations to reflect the weakness of SnapKV-like methods, if they intend to highlight the superiority of RazerAttention in this regard.

2. The needle setting is unclear. It is often very easy to do the "eating sandwich in a park" needle with the "grass sky sun" repetition background. But it is hard with the "magic city number" needle with a noisy background (e.g., Paul Graham's essay). The authors should clarify this setting and consider adding more standardized needle evaluations, like the RULER.

3. Similar to #2, the LongBench truncation settings of Table 3 can also use some clarifications.

4. RazorAttention is proposed as an efficiency work. However, the efficiency evaluation is very limited. I'd like to see latency and throughput evaluation under different context length/batch size workloads.

5. The core design of the work heavily relies on the findings of Induction Heads and Retrieval Heads, making its novelty limited. While I don't think this is much of an issue due to the practical performance gain the proposed method achieved, the relationship of such works deserves much better highlight. The mere mentioning around L167 is not enough.

6. I'd like to see more dataset coverage beyond LongBench — as it is no longer very long w.r.t. models like Llama 3.1. Evaluation of Llama 3.1 on $\infty$Bench would fill this gap.

### Questions
DuoAttention and Not All Heads Matter are two concurrent works of RazerAttention. I'd appreciate it if the author could discuss their similarities and differences. In particular, I am interested in Figure 13(1) of DuoAttention — which supposedly features RazorAttention — but the needle performance is very different from your own reporting. I wonder why?

### Soundness
3

### Presentation
2

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
The paper proposed a novel KV cache mechanism basing on retrieval heads. To be more specific, the paper presents the observation of some retrieval heads that is essential for handling long context workload, then proposed a token-dropping based method to compress the to KV cache of the non-retrieval heads with compensation tokens, while keeping the retrieval head integrated, leading to substantial accuracy improvement compare to previous proposed method.

### Strengths
The paper observes the phenomenon of "retrieval heads" aligning with observations from other works.

Basing on the retrieval heads, the paper presents a straightforward token dropping based KV compression mechanism.

Experiments results show improvement compare with the previous token dropping based baselines.

### Weaknesses
Lack of experimental results on compression ratio:
The paper compares against StreamLLM and H2O. However, StreamLLM has a very limited compression ratio, and the performance of different compression ratio in H2O also will be different. The current manuscript lack the study of how different compression ratio in RazorAttention will affect the performance.

Lack of overhead evaluation on efficiency
The paper claims that RazorAttention can enhance LLM inference efficiency without overhead. However, there is no efficiency evaluation (both peak memory usage as well as the inference latency analysis). It is essential to have such real efficiency gain evaluation.

The novelty of "retrieval heads"
Previous paper [1] has demonstrated the existence of "retrieval heads" and its importance in serving long context. Do the authors aware of this and is there a difference between the two "retrieval heads" proposed in the two paper?

Miss of clarification:
"Retrieve and Process" in line 84: The manuscript claims that some heads are used for retrieval while some are used for process. However, lacks the analysis of "process"
"Protect" in line 234: what is the specific protection mechanism? 

Potential typos:
115 as follows:

[1] Retrieval Head Mechanistically Explains Long-Context Factuality

### Questions
See the weakness

### Soundness
3

### Presentation
2

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
The paper has made an observation: induction and echo heads are retrieval heads and others are local processing heads. They then keep complete KV Cache for retrieval heads and drop non-local KV for local processing heads. Following their hyper parameters, this leads to 70% asymptotic KV Compression.

### Strengths
1. The observation is neat.  And experiments support the hypothesis quite well. 
2. The recipe to identify the heads is very lightweight (although is this a contribution or is it previously known from anthropic paper?)

### Weaknesses
 1. Experiments

     A. why are some datasets from longbench missing like passage_retrieval etc

     B. Can you perform experiments on infinity benchmark for comparison.

     C. what is the exact KV compression in the longbench datasets? The 70% number is misleading since longbench generally has small context lengths and authors have used a context thold of 4000.  Please add exact KV Cache compression numbers for all the methods to the table. 

2. Novelty: Can you please elaborate on the novelty of defining / identifying the echo and induction heads. what is already known and what is figured out?

3. Writing errors: Please revise the manuscript for text/language errors. e.g. : 
    
     A. "There are been plenty ..." (page 1)  
    
     B. " and proved that accuracy .." ( page 2) {you showed it empirically .. and also 70% is not what you show in the experiments.}.

     C. C_0 in equation 2. Do you mean L_h ?

### Questions
Please address the weaknesses above.

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
The paper introduces RazorAttention, a training-free algorithm for compressing KV cach in LLMs. This method selectively retains information in specific “retrieval heads” of the multi-head attention mechanism while discarding remote tokens in other heads. A notable aspect of RazorAttention is using a "compensation token" to summarize discarded information, minimizing data loss. RazorAttention shows a 70% reduction in KV cache size with minimal performance impact, supporting compatibility with FlashAttention for efficient large-context inference without modifying the base model.

### Strengths
- RazorAttention’s head-specific strategy, distinguishing retrieval heads from non-retrieval heads, is a novel approach to KV cache compression that aligns with the attention heads’ different roles.
- This method is compatible with FlashAttention and offers practical efficiency gains without training or model alterations.
- RazorAttention is tested across various architectures, including ALiBi and RoPE models, proving effective on different LLM types, with compression ratios of up to 70%.

### Weaknesses
 - The paper lacks detailed efficiency reports, particularly on latency and throughput improvements. A breakdown of the actual performance gains would give better insight into its practical benefits.
- RazorAttention introduces operations like compensation token creation and slicing, yet the associated computational overhead is not profiled and discussed. A detailed overhead analysis and implementation would help.
- RazorAttention’s comparison is primarily with StreamingLLM and H2O, omitting comparison and discussion of other types of KV cache compression methods. (like what are others’ performances under similar compression rates? can this method be combined with others?)
- The results focus on one compression rate without experiments on varying compression ratios compared with others.

### Questions
- What are the latency and throughput improvements, both absolute and relative to the baseline?
- What are the comparative performances at different KV cache compression ratios?
- Has RazorAttention been tested on other models like Mistral-7B-Instruct-v0.2 or longchat-7b-v1.5-32k?
- Can you provide a breakdown or approximation of the distribution between retrieval and non-retrieval heads?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce a KV cache compression algorithm in LLMs that only maintains a full cache for retrieval heads and reduces all the remote tokens in non-retrieval heads to single compensation token per head. The proposed method can achieve 3X KV cache compression ratio without noticeable impacts on performance.

### Strengths
1.	It is pluggable solution that enhances the inference efficiency of a diverse set of large language models without noticeable impacts on performance.

### Weaknesses
1.	There are some related works identifying the different patterns of retrieval and non-retrieval heads, such as DuoAttention, Retrieval Head Mechanistically Explains Long-Context Factuality, MInference, etc. It would be better to clarify the novelty of the proposed method.
2.	It can only be applied to multiple KV cache scenarios. For only single KV cache model structure, such as YOCO, it cannot be applied.
3.	The baselines are not comprehensive. It would be beneficial if the authors could compare their results with more advanced baselines.
4.	It seems the proposed method cannot achieve the best performance in all the benchmarks. It would be beneficial to give detailed analysis of the worse cases.

### Questions
1.	What is the compression ratio for GQA in Llama3-8B-Instruct model? What is the compression ratio for 1024K sequence length?
2.	How to decide the 1% echo heads and 14% induction heads configuration? Have the authors tried different combination, e.g. more echo heads and less induction heads?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces RAZORATTENTION, motivated by the goal of reducing the size of the key-value cache as much as possible without losing semantic information. The rationale behind this approach is the retrieval heads in LLMs. For these retrieval heads, RAZORATTENTION retains the KV cache in its original state; for the other heads, it only caches recent tokens and attention sinks. Additionally, the paper designs a compensation strategy for compensating the information loss. Experiments indicate that RazorAttention can compress up to 70% of the KV cache without causing a noticeable decline in performance.

### Strengths
1. The research problem addressed in this paper is significant. Reducing the key-value  cache in large language models is a hot topic, and improvements in this area can have a substantial impact on the real-world deployment of LLMs.
2. Based on the phenomenon of retrieval heads present in large language models and in conjunction with the token dropping method, this paper explores an training-free way to reduce the key-value cache. The results from downstream tasks and NIH tests have both demonstrated the effectiveness of this approach.
3. The writing of this article is easy for readers to understand.

### Weaknesses
1. I agree that this work is the first training-free token reduction algorithm based on retrieval heads. However, to my knowledge, the phenomenon of retrieval heads being prevalent in LLMs was first articulated in [1]. [1] provides a detailed discussion on the properties of retrieval heads, which diminishes the novelty of this paper. Although the paper provides a theoretical analysis of AliBi-based models, which is commendable, it does not cover Rope-based models. The analysis should be extended to cover the more widely used RoPE positional embeddings, as the behavior of attention heads can be significantly different with different positional encodings. For example, the locality of attention might be affected, which could impact the effectiveness of the proposed method.
2. A recent work [2] is also motivated by the presence of retrieval heads. The main idea of [2] is to combine streaming heads with retrieval heads, which is very similar to the approach taken in this paper. But [2] is not training-free. It would be beneficial to elaborate on the advantages of this paper over [2]. The comparison should go beyond just the training-free aspect and delve into the practical implications of each approach. For instance, how do the computational costs compare during inference? Does one method introduce more latency than the other? Furthermore, a discussion on the trade-offs between training-free and training-based methods in terms of adaptability to different model architectures would be valuable.

### Questions
1. As mentioned in the weaknesses, it is beneficial to compare with DuoAttention in terms of effectiveness.
2. As a training-free method, a potential issue is that different models may have different optimal hyperparameters. For example, how can we quickly determine the suitable proportion of Induction Heads and Echo Heads for different models?
3. If a general theoretical analysis can be found explaining why retrieval heads are widely present in various models, that would be highly significant.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the attention mechanisms within transformer models, observing that most attention heads primarily focus on local context while only a few, termed "retrieval heads," are capable of attending to all input tokens. To optimize memory and computational efficiency, the authors propose maintaining a full key-value (kv) cache for retrieval heads and only keeping a recent kv cache for other attention heads. The identification of these retrieval heads is based on observed patterns known as the "Echo head" and "Induction head."

### Strengths
The paper is well-written and straightforward to follow.

### Weaknesses
1. The authors identify retrieval heads as echo heads and induction heads, demonstrated through an example using a synthetic repeated sequence. However, this example appears specifically designed to highlight these two types of heads. It raises the question of whether this pattern holds in more generalized query settings. Intuitively, it does not seem that in every type of query, the most crucial information is located solely in echo or induction tokens. Would these patterns still be dominant in more diverse and complex input data? Specifically, the paper lacks a rigorous analysis demonstrating that these heads consistently capture the most relevant information across a broad spectrum of queries, beyond the contrived example provided. The reliance on echo and induction heads as the sole indicators of retrieval capability seems overly simplistic and potentially limiting.

2. The authors state that they did not compare their method with SnapKV because SnapKV relies on the query for selecting the kv cache. However, this reasoning is weak, as SnapKV is a well-known and accepted method in the field. A comparison would provide more comprehensive insights. The argument that SnapKV's query-dependency makes it unsuitable for comparison is not sufficiently justified. Many real-world applications involve known query patterns or can benefit from query-aware optimizations, making a comparison with SnapKV highly relevant. The lack of such a comparison leaves a gap in the evaluation of the proposed method's practical utility.

3. I'm confusing that whether the selection of retrieval heads is model-based or  also query-specific. Are these retrieval heads consistent across different queries, or do different heads have different functions across different queries?

4. The authors note that reducing the kv cache for all non-retrieval heads introduces a notable accuracy gap and that compensation tokens can mitigate this gap. However, it is unclear whether the observed improvement comes purely from the use of compensation tokens or from the strategic allocation of the kv cache itself. An experiment comparing the combination of compensation tokens with other baseline models could clarify the extent of the improvement attributable to each factor. The paper does not fully disentangle the effects of the compensation tokens from the effects of the reduced KV cache, making it difficult to assess the true contribution of each component. A more controlled experiment is needed to isolate the impact of the compensation tokens.

### Questions
The paper lacks detailed experimental setup descriptions. When comparing with baseline methods, was the total kv budget (i.e., the combined kv cache size for all heads) kept constant?

### Soundness
2

### Presentation
3

### Contribution
2
