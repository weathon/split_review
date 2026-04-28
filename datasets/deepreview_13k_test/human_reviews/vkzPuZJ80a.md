# Accelerating Retrieval-augmented Language Model Serving with Speculation

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Retrieval-augmented language models (RaLM) have demonstrated the potential to solve knowledge-intensive natural language processing (NLP) tasks by combining a non-parametric knowledge base with a parametric language model.
Instead of fine-tuning a fully parametric model, RaLM excels at its low-cost adaptation to the latest data and better source attribution mechanisms.
Among various RaLM approaches, iterative RaLM delivers a better generation quality due to a more frequent interaction between the retriever and the language model.
Despite the benefits, iterative RaLM usually encounters high overheads due to the frequent retrieval step.
To this end, we propose \Sys{}, a speculation-inspired framework that provides generic speed-up over iterative RaLM while preserving the same model outputs through {\em speculative retrieval} and {\em batched verification}.
By further incorporating prefetching, optimal speculation stride scheduler, and asynchronous verification, \Sys{} can automatically exploit the acceleration potential to the fullest. 
For naive iterative RaLM serving, extensive evaluations over three language models on four downstream QA datasets demonstrate that \Sys{} can achieve a speed-up ratio of $1.75$-$2.39\times$, $1.04$-$1.39\times$, and $1.31$-$1.77\times$ when the retriever is an exact dense retriever, approximate dense retriever, and sparse retriever respectively compared with the baseline.
For KNN-LM serving, \Sys{} can achieve a speed-up ratio up to $7.59\times$ and $2.45\times$ when the retriever is an exact dense retriever and approximate dense retriever, respectively, compared with the baseline.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a collection of methods aimed to accelerate the retrieval-augmented language model. In particular, RaLMSpec is proposed, which employs speculation-inspired framework that provides generic speed-up over iterative RaLM while preserving the same model outputs through speculative retrieval and batched verification. Additionally, prefetching, optimal speculation stride scheduler and synchronous verification are further proposed to improve the performance. Experimental evaluation show a speed-up ratio of around 2x compared to the baseline method.

### Strengths
1. It presents several techniques to speedup the retrieval-augmented language model serving.
2. It achieves speedup over the baseline approach and seems satisfactory.

### Weaknesses
1. The overall contribution of the paper is not quite enough to present in ICLR.
2. The novelty of the paper is limitted.

### Questions
1. The the speedup varies from different settings (e.g. hardware, data, model, etc)?
2. why the speed up for different retriever differ so significantly? It is better the show breakdown the the major time-consuming parts and perform insightful analysis.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a framekwork called RaLMSpec for accelerating iterative RaLM serving. It is inspired by speculative execution and speculative decoding and reduces the number of calls to retrieve from external corpora so that decreases its serving cost. The main idea sounds reaonable and the experiment results show moderate speedup.

### Strengths
The idea of speculative retrieval sounds interesting and may reduce the number of calls to the large external corpora. It can potentially save cost of serving an iterative RAG system.

### Weaknesses
I am primarily concerned about the significance of this work.

Firstly, I am unsure about the practicality of iterative RAG. From my understanding, current AI-powered search engines like Bing Chat do not operate iteratively. Instead, they perform retrieval all at once and then apply RAG. These systems typically have a cache system that stores the results of common queries, thereby saving the cost of performing retrieval for each query. The only difference between this paper and these common practices is the iterative RAG setting. However, I am still concerned about this iterative setting, as I am uncertain whether the benefits are significant enough, especially for LLMs.

Secondly, as far as I understand, the main cost of the RAG model lies in the generation aspect. For mature search engines, various optimizations of the retrieval part are already well-established, fast, and efficient. However, generation has always been the more costly part. Therefore, I am unsure whether the speedup improvement reported by the authors refers to the savings in the retrieval part or the end-to-end savings. If it is the latter, I would like to know how much improvement this technology could bring when applied to a mature search engine.

Some minor issues:

- A comparison between iterative RAG and conventional RAG should be presented to demonstrate the value of iterative RAG, as it may introduce more latency.

- The LLMs used in the experiments are small. This makes the retrieval speed improvement appear greater in the end-to-end latency improvement. However, when the LLM becomes larger, the end-to-end speed improvement will become very marginal.

- There are previous related studies (e.g., [1]) that explore the idea of speculation and cache in the RAG setting. The authors should include these as related work, while they focus more on the generation speedup.

References:

[1] Yang et al.: Inference with Reference: Lossless Acceleration of Large Language Models. https://arxiv.org/abs/2304.04487

### Questions
See the weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This author proposes a new framework called RaLMSpec that accelerates retrieval-augmented language model serving with speculation. RaLMSpec provides generic speed-up over iterative RaLM while preserving the same model outputs through speculative retrieval and batched verification.

The author empirically evaluated RaLMSpec on three language models on four downstream QA datasets, and the results show that RaLMSpec achieves a speed-up ratio of up to 2.39× compared to the iterative RaLM approach.

Key components include:

1. Caching-based speculative retrieval mechanism and prefetching: RaLMSpec leverages the temporal locality of retrieved documents to enable a request-level local cache for speculative retrieval.  RaLMSpec prefetches the cache to reduce the latency of the first retrieval.

2. Batched and asynchronous verification: RaLMSpec uses a batched verification step to guarantee correctness while reducing the retrieval overhead. This is done asynchronously to overlap the verification with the retrieval and further boost the speculation performance.

3. Optimal speculation stride scheduling: RaLMSpec schedules the speculation stride optimally to balance the trade-off between speed and accuracy.

### Strengths
1. Empirical results are impressive: RaLMSpec achieved better performance in terms of speed and accuracy. In the meantime, RaLMSpec achieved comparable or better accuracy than the baseline approach while providing a significant speed-up.

2. The presentation and the technique proposed are clear: batching, prefetching, asynchronicity, and scheduling. While none of this is new standalone, the authors combine them clearly and cleverly to boost the overall performance of augmented retrieval.

### Weaknesses
1. The ablation study does not shed light on which component contributes the most to the performance gain. It would be nice to have a breakdown on how much batching, prefetching, asynchronicity, and scheduling contributed to the overall performance improvement to give more insights about the characteristics of the workload.

### Questions
My main concern is regarding the ablation study listed above. I would be happy to raise my rating if the author can provide further analysis on how each component contribute to the overall performance gain and share more insights about the characteristics of the workload.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to accelerate retrieval-augmented language models (RaLM) by incorporating speculation over iterative RaLM. The proposed framework, RaLMSpec, leverages the temporal locality of the retrieved documents and uses a caching-based speculative retrieval mechanism with bached verification to reduce the latency in the retrieval phase. Based on this, three techniques are proposed to further speed up the process, i.e., top-k cache update, asynchronous verification, and optimal speculation stride scheduler. Experiments are conducted on various datasets, language models, and retrievers and RaLMSpec is proven to be effective.

### Strengths
- This paper targets an interesting and promising direction in the community, which is to make the inference faster so that the models could be more deployable in real-world scenarios.
- This is the first work to employ the idea of speculation in retrieval-augmented language models.
- The proposed framework is sound and the paper is overall well-written and organized. The figures demonstrated the method vividly. Almost everything is clear to me.
- The proposed methods are experimented with comprehensive settings, and the results are significant when using dense retrievers.

### Weaknesses
- The proposed framework, with three additional tricks stacked, is still not promising in all settings. For example, it does not bring much speedup with approximate dense retrievers on GPT and Llama-2.
- The related work section needs reorganization. The current version simply decomposes the framework into related parts and introduces the works one by one. It's hard to grasp the major contribution and position of this work correctly at first glance.

### Questions
1. How will the *speculation stride s* evolve during the process? Is there any experiments/analysis on how the initialization of *s* affect the performance?

2.  Any intuitions on why RaLMSpec brings more speedup on OPT2 than the other two models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
