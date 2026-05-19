# SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation

- Decision: Reject
- Scores: 6, 8, 3, 5

## Abstract
Adaptive Retrieval-Augmented Generation (RAG) is an effective strategy to alleviate hallucination of large language models (LLMs).
It dynamically determines whether LLMs need external knowledge for generation and invokes retrieval accordingly. 
This paper introduces \textit{Self-aware Knowledge Retrieval} (\model), a novel adaptive RAG model that extracts self-aware uncertainty of LLMs from their internal states. 
\model activates retrieval when the LLMs present high self-aware uncertainty for generation. 
To effectively integrate retrieved knowledge snippets, \model re-ranks them based on LLM's self-aware uncertainty to preserve the snippet that reduces their uncertainty to the utmost. 
To facilitate solving complex tasks that require multiple retrievals, \model utilizes their self-aware uncertainty to choose among different reasoning strategies. 
Our experiments on both complex and simple Question Answering datasets show that \model outperforms existing adaptive RAG methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a self-aware knowledge retrieval approach for RAG. Instead of retrieving information for all queries, this technique triggers retrieval only when the language model is uncertain about its answer. The uncertainty is measured by the correlation (based on the Gram matrix) of the last token representations from multiple parallel samplings. The paper also proposes using the uncertainty score to rerank the retrieved documents and combines iterative COT reasoning with retrieval. Experiments on multiple datasets show that the proposed method consistently outperforms previous RAG methods.

### Strengths
- The proposed method is well-motivated and performs effectively on benchmarks.

- The new uncertainty measurement is interesting and empirically outperforms previous methods like Perplexity or energy-based approaches.

- This paper conducts extensive experiments, and the results are insightful and support its main claims.

### Weaknesses
- The proposed method includes using the consistency of parallel sampling (with a sample time of 20) to determine the uncertainty of the LLM. This is performed at each retrieval step, which may increase computational costs during inference. It would be beneficial to compare the inference latency of these methods or evaluate them under a similar inference budget.

- I suggest moving Section 3.4 to an earlier position in the paper, as it appears to be the key proposal and is referenced in Sections 3.1, 3.2, and 3.3. Additionally, the current Section 3.4 is somewhat vague and could benefit from more detail.

- The paper finds that more retrieval steps decreases model performance, as shown in Table 3. This may be due to the use of a weak retriever (BM25) and the recall of only a few documents (top-3). The paper should also compare against a stronger retriever and with a larger number of recalled documents, as is common in most RAG settings.

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces SEAKR, a novel approach for adaptive Retrieval-Augmented Generation (RAG) that utilizes self-awareness within large language models (LLMs) to optimize when and how to retrieve external knowledge. The primary objective of SEAKR is to mitigate hallucination in LLMs by dynamically determining the necessity of external retrieval based on self-aware uncertainty detected within the model’s internal states. SEAKR integrates retrieved information using self-aware re-ranking, which selects knowledge snippets that effectively reduce uncertainty, and self-aware reasoning, which iteratively refines the retrieval strategy to address complex queries. Experimental results on both complex and simple question-answering tasks demonstrate that SEAKR significantly outperforms existing adaptive RAG methods by adapting retrieval and integration strategies to the model’s self-identified knowledge gaps.

### Strengths
- The writing is easy to follow and the logic is clear.
- The authors provide extensive experimental results across both complex and simple question-answering tasks , validating the robustness and superiority of SEAKR over state-of-the-art approaches. 
- SEAKR is one of the first methods to use self-aware uncertainty within the internal states of LLMs to guide retrieval decisions. By utilizing the model’s internal consistency, SEAKR ensures that retrieval is only triggered when necessary, addressing the inefficiencies and potential conflicts caused by indiscriminate retrieval.

### Weaknesses
- Sensitivity to Uncertainty Thresholds: SEAKR’s reliance on a carefully chosen uncertainty threshold for retrieval introduces challenges in generalizability. Determining the optimal threshold can be difficult, and miscalibration may lead to over-retrieval or under-retrieval. This sensitivity could be problematic if SEAKR were applied across different domains with varying uncertainty levels in LLMs, potentially requiring frequent recalibration.
- Challenges in Numerical and Logical Reasoning: The paper notes that SEAKR’s improvement on datasets requiring numerical reasoning (e.g., IIRC) is limited. This suggests that while SEAKR can handle general knowledge queries well, it may not perform as effectively on questions that involve mathematical calculations, precise date comparisons, or logical deductions. Future iterations might need specialized handling of these reasoning types.

### Questions
- Why self-aware uncertainty from the internal state of LLMs can more accurately determines the knowledge demand compared with the output?
- What strategies could be introduced to better handle tasks that require numerical or logical reasoning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an adaptive RAG model that uses a multi-step reasoning strategy and dynamically decides whether to retrieve external knowledge based on an uncertainty estimator. The experiments show significant improvement over selected baselines. However, there are some flaws in paper writing, model design, and experiments. More details can be found in the weaknesses.

### Strengths
1. Using hidden states of the last token and the corresponding Gram matrix by sampling multiple generations to measure the generation uncertainty is novel compared to previous probability-based uncertainty measurements.
2. Experiments show significant improvement over selected baselines.

### Weaknesses
1. The organization and writing of the methodology introduction are a little bit confusing.
The first paragraph of Section 3 notes that the self-aware uncertainty estimator is the most important module. However, this paragraph only uses a symbol $U(c)$ to represent it without some clear introduction about its input/output and target. Then, in Sections 3.1, 3.2, and 3.3, the paper directly uses this symbol and only detailedly introduces $U(c)$ in Section 3,4. This writing style may lead to some confusion when reading the paper. I recommend first introducing your most important module, especially when it will be frequently utilized in other modules.

2. Lack of demonstrations of model design details.
In Section 3.1, what is the difference between "the pseudo-generated rationale" and "generated rationale"? How a query is generated specifically? More function, detailed introduction, and the corresponding motivation of model designs need to be provided to clarify your method process.

3. The calculation details of the "Gram matrix" can be provided to enrich the technique details of the paper.

4. The calculation of the "Gram matrix" relies on the multi-generation of LLMs. For each generation, the "<EOS>"'s hidden state still relies on the previously generated tokens. Does this process still be influenced by token sampling probabilities?

5. Since most of the modules are prompt-based, the stability of the proposed method is difficult to guarantee.

6. The selected search engine, BM25, is too old. A more advanced dense retriever or hybrid retriever could be utilized.

### Questions
1. Why the Section 3.1 is called "Self-aware retrieval"? It doesn't demonstrates more about retrieval process, but focuses on the generation of the next rationale and the next query.
2. For the "Query Generation" in Section 3.1, what does the symbol "r" refer to? Should it be "r_s"? 
3. Why "Gram matrix" can reliably measure the uncertainty of LLM on its generation? Are there some related analyses or theoretical proven?
4. Why evaluations are conducted on sampled test instances? It leads to different model performance values in Tables 1, 2, and 3, which is very confusing.

### Soundness
2

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
4

### Summary
The paper introduces SEAKR, a novel adaptive RAG model designed to improve the performance of LLMs by reducing hallucinations. SEAKR enhances RAG by dynamically invoking knowledge retrieval based on LLMs' internal self-aware uncertainty. When the LLMs experience high uncertainty during generation, SEAKR retrieves external knowledge, re-ranks retrieved snippets to reduce uncertainty, and integrates the most relevant information. This model also adapts reasoning strategies for complex tasks requiring multiple retrievals.

### Strengths
The paper proposes using the internal self-awareness of LLMs to enhance the effectiveness of adaptive RAG. Experimental results show that the proposed method significantly improves the accuracy of LLMs on multiple QA datasets, outperforming existing methods. The structure of the paper is very clear and easy to understand.

### Weaknesses
1. Some statements regarding the contributions in this paper are flawed. For example, the paper claims that existing adaptive RAG methods determine whether retrieval is needed solely based on the model’s output, which is clearly incorrect. Papers like Self-RAG[1] use the model’s in-context learning ability to judge whether additional knowledge retrieval is necessary, and during this process, the model naturally considers input prompts, including questions and retrieved knowledge. Additionally, many adaptive RAG methods re-rank retrieved knowledge during the integration process. For example, Self-RAG labels knowledge as "is_supportive," "is_related," and "is_useful." Similar work includes RankRAG[2], RagVL[3]. Therefore, the paper's claim that existing methods "neglecting to re-rank multiple retrieved knowledge and optimize the reasoning paths" is biased.

2. The method proposed in this paper mainly consists of three processes: retrieval, re-ranking, and reasoning. The overall pipeline design is not novel, and the innovation of this paper lies primarily in using the model's self-aware uncertainty to evaluate the output of each process to decide when to retrieve, how to re-rank the retrieved knowledge, and whether to use the model's generated rationale or the retrieved information during reasoning. However, based on the experimental results in Table 3, using the proposed Self-aware Uncertainty Estimator does not provide a particularly significant improvement compared to using LN-Entropy, perplexity, or prompt to determine the LLM's uncertainty. Therefore, the innovation of this paper is limited, and the improvements in experiments may be more attributable to the effectiveness of the pipeline itself, while the innovation in the pipeline design is trivial.

3. Computing self-aware uncertainty seems to be a very time-consuming and computationally expensive process, yet the paper does not discuss the time and computational cost of the entire reasoning process. On the other hand, although this method is tuning-free, it can only be applied to local models. For closed-source LLMs, since their hidden layers are inaccessible, this method is not applicable, which weakens the advantage of this method in being tuning-free and affects its practical value.

4. The experiment uses the F1 measure as an evaluation method, but in practice, when calculating F1, the model's output is matched word-by-word against the ground truth in an N-to-N fashion. This is not the standard F1 score evaluation method and does not reflect the method's retrieval performance. Moreover, this aspect was not clarified in the experimental design.

[1] Asai, Akari, et al. "Self-rag: Learning to retrieve, generate, and critique through self-reflection." arXiv preprint arXiv:2310.11511 (2023).
[2] Yu, Yue, et al. "RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs." arXiv preprint arXiv:2407.02485 (2024).
[3] Chen, Zhanpeng, et al. "MLLM Is a Strong Reranker: Advancing Multimodal Retrieval-augmented Generation via Knowledge-enhanced Reranking and Noise-injected Training." arXiv preprint arXiv:2407.21439 (2024).

### Questions
1. How long is the inference time required for the entire pipeline? Compared to the Prompt method, how much additional computation is needed when using the self-aware uncertainty estimator proposed in this paper? Is it applicable to larger LLMs?

2. Since the proposed self-aware uncertainty estimator can only be applied to local models, could the LLM be fine-tuned with an additonal adapter to better calculate uncertainty?

3. When determining whether retrieval is necessary, could a simpler and more effective approach be used, like Chain of Knowledge[4], where self-consistency is employed to assess the need for retrieval? When the model shows strong output consistency through self-consistency, retrieval may not be needed. Would this method be simpler and more effective than calculating self-aware uncertainty?

4. From Table 3, it seems that just using the LLM-generated rationale can achieve results close to those that require external retrieval. Does this imply that the knowledge retrieval in this method is not particularly effective, and the retrieved knowledge does not provide sufficient performance gains for the reasoning results?

5. Even if the LLM-generated rationale has low uncertainty, it may still represent a strong hallucination. How can this issue be avoided to better filter and re-rank the LLM-generated rationales?

[4] Li, Xingxuan, et al. "Chain-of-knowledge: Grounding large language models via dynamic knowledge adapting over heterogeneous sources." arXiv preprint arXiv:2305.13269 (2023).

### Soundness
2

### Presentation
3

### Contribution
2
