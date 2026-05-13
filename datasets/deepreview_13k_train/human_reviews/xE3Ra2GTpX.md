# Multi-Grained Knowledge for Retrieval-Augmented Question Answering on Hyper-long Contexts

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
In the task of hyper-long context question answering (QA), a key challenge is extracting accurate answers from vast and dispersed information, much like finding a needle in a haystack. Existing approaches face major limitations, particularly the input-length constraints of Large Language Models (LLMs), which hinder their ability to understand hyper-long contexts. Furthermore, Retrieval-Augmented Generation (RAG) methods, which heavily rely on semantic representations, often experience semantic loss and retrieval errors when answers are spread across different parts of the text.
Therefore, there is a pressing need to develop more effective strategies to optimize information extraction and reasoning. 
In this paper, we propose a multi-grained entity graph-based QA method that constructs an entity graph and dynamically combines both local and global contexts. Our approach captures information across three granularity levels (i.e., micro-level, feature-level, and macro-level), and incorporates iterative retrieval and reasoning mechanisms to generate accurate answers for hyper-long contexts.
Specifically, we first utilize EntiGraph to extract entities, attributes, relationships, and events from hyper-long contexts, and aggregate them to generate multi-granularity QA pairs. Then, we retrieve the most relevant QA pairs according to the query. Additionally, we introduce LoopAgent, an iterative retrieval mechanism that dynamically refines queries across multiple retrieval rounds, combining reasoning mechanisms to enhance the accuracy and effectiveness of answering complex questions.
We evaluated our method on various datasets from LongBench and InfiniteBench, and the experimental results demonstrate the effectiveness of our approach, significantly outperforming existing methods in both the accuracy and granularity of the extracted answers. Furthermore, it has been successfully deployed in online novel-based applications, showing significant improvements in handling long-tail queries and answering detail-oriented questions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a multi-grained entity graph-based QA method that constructs an entity graph and dynamically combines both local and global contexts, capturing information across three granularity levels: micro, feature, and macro levels, and incorporates iterative retrieval and reasoning mechanisms to generate accurate answers for hyper-long contexts. Evaluation results on LongBench and InfiniteBench demonstrate the effectiveness of the approach, significantly outperforming existing methods in both the accuracy and granularity of the extracted answers, and it can be deployed in online novel-based applications.

### Strengths
1. This paper proposes MKRAG (Multi-grained Knowledge Retrieval-Augmented Generation) for hyper-long context question answering. By integrating multi-grained entity graphs with an iterative retrieval and reasoning process, MKRAG addresses the limitations of traditional models constrained by context window size.
2. This paper introduces LoopAgent, an iterative retrieval framework that progressively refines queries across multiple retrieval cycles. By incorporating advanced reasoning capabilities, LoopAgent improves both retrieval and answering accuracy and mitigates information loss in traditional single-pass retrieval methods, particularly in complex multiple-entity scenarios.

### Weaknesses
1. The entities and their associated attributes, relationships, and events are extracted by LLMs. However, as noted in previous work, LLMs may fall short in information extraction (IE) tasks, such as entity extraction, relation extraction, and event extraction. If LLMs cannot handle IE well, errors could propagate through the system, leading to random, unpredictable, and non-generalizable outcomes. It could be better if the authors provide evaluation on the reliability of the IE process.
2. While the model of experiments is based on ERNIE, there lack a comparison with the other ERNIE variants capable of handling longer inputs, such as ERNIE-Turbo-128K. Including a comparison with models from the same series would strengthen the paper by better demonstrating the effectiveness of the proposed approach.

### Questions
See "Weaknesses".

### Soundness
2

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
To address the challenges of hyper-long context QA, particularly the limitations of context windows and retrieval errors in retrieval-augmented generation (RAG) due to inadequate semantic representation, this paper proposes Multi-grained Knowledge RAG Method (MKRAG). MKRAG involves extracting entities from context with EntiGraph chunk-by-chunk, generating multi-grained QA pairs, and iteratively retrieve related information by refining queries to get the final answer.

Results show that the proposed method achieve on par or slightly better performance compared with SOTA models/methods, and achieves high performance gain in the online test.

### Strengths
1. The EntiGraph module effectively enhances the representation and may have the potential to extract most necessary information from the document.
2. The multi-grained knowledge generation from entity graph helps capture possible QA from different granularity.

### Weaknesses
1. This paper claims that the EntiGraph module enables accessing nearly all the necessary information. However, the performance of EntiGraph is not discussed, particularly in terms of precision and recall of entity extraction, which is crucial for the overall method's effectiveness.
2. In the Entity Pruning section, how the threshold $\tau$ is selected is not explained. There are also pre-defined thresholds in (10). The selection of thresholds are not justified by detailed analysis of module performance, and the impact of different threshold values on the final results is not explored.
3. By turning the document into entity graphs and generating knowledge accordingly, the model risks missing information during these processes, and the agent may be unable to answer the question given the insufficient information. The paper does not provide a clear analysis of the potential information loss during the conversion to entity graphs.
4. In the ablation study section, “Chuck Retrieval + Baseline” setting uses a chunk size of 500 tokens/chunk while the context window limit is 4k. It is not clear what is the chunk size used in MKRAG and if the small chunk size in the previous setting limits its performance. The paper lacks a discussion on the optimal chunk size and its impact on retrieval performance.
5. This paper claims that the proposed method demonstrating high accuracy in Online Test and high user satisfaction rate. However, details of the tests are not provided and the results are not compared against other SOTA models/methods. The lack of detailed experimental setup and comparative results makes it difficult to assess the true performance of the proposed method.

### Questions
1.	How is "importance weight" defined in equation (6)? More explanation of this part would be helpful.
2.	What is the module performance in each subtask? e.g., the recall rate of entities, accuracy of entity aggregation, effectiveness of entity pruning, effectiveness of thresholds in equation (10), and more?
3.	What is the average number of rewrites for each question (line 401)? How is the computation cost for the LoopAgent?
4.	The hyter-long context QA benchmark, InfiniteBench, has an average output of 6.3 tokens, which should be only a few words. Does these questions really need query-decomposition described in line 383?

### Soundness
1

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
In this paper, a model called MKRAG is proposed to deal with hyper-long context QA tasks. Through multi-grained knowledge generation and iterative retrieval agent, MKRAG model can effectively extract and integrate information,  and thus improves the accuracy of question answering. The experimental results show that the MKRAG model achieves excellent performance on multiple benchmark datasets, and shows a strong ability of long text understanding and multi-domain question answering.

### Strengths
1.The MKRAG model captures the local and global information in the text by constructing multi-grained entity graphs (including micro, feature and macro levels), and can generate more accurate answers than traditional RAG methods.
2. Overall well written and easy to understand.
3.Iterative retrieval agent, MKRAG model uses LoopAgent iterative retrieval mechanism to refine the query through multiple rounds of retrieval to alleviate the problem of information fragmentation encountered by traditional methods in dealing with ultra-long text.
4.In this paper, based on the hyper-long context question and answer field, the experiments not only aim at the long text, but also verify that the proposed model is also applicable in the short text.

### Weaknesses
1.Authors have not clearly stated the key innovations of this paper.  Authors to explicitly state their key innovations and provide a clear comparison to existing methods, highlighting specific novel aspects of their approach, e.g., a specific new method or a new framework of well incorporating existing techniques.
2. The multi-grained entity graph and iterative retrieval, while effective, could be computationally intensive, limiting scalability in resource-constrained environments. Therefore, authors should conduct time and space complexity analyses, as well as perform corresponding experiments for verification, such as the Inference Time and  the Time per Iteration.
3.Some experimental details are missing, such as hardware specifications, number of iterations, the stopping condition for iterative retrieval, and the convergence criteria for all models.
4.  About " we employ context aggregation algorithms to integrate both local and global contexts of the same entity, and utilize an LLM, EntiGraph, to generate multi-grained QA pairs (i.e., micro-level, feature-level, and macro-level). This multi-level strategy not only ensures that the model produces highly accurate answers for complex queries, but also mitigates the fragmentation of information that often hampers traditional methods",  1) the "EntiGraph" is a LLM model? 2) why generate multi-grained QA pairs from micro-level, feature-level, and macro-level, and what are the insights about these? 3) why this multi-level strategy can ensure high accurate answers? 4) does this strategy lead to much noise?
5. The model is relatively complex, and the paper fails to clearly present the training and optimization process of the model. 1）How to perform joint optimization among multiple modules, i.e., ITERATIVE RETRIEVAL AGENT, MULTI-GRAINED REPRESENTATION, ENTITY EXTRACTION? How is the training data for each module constructed?  For each entity, how to construct the embeddings of its attributes, relationships, events and temporal information?

### Questions
1.Authors have not clearly stated the key innovations of this paper.  Authors to explicitly state their key innovations and provide a clear comparison to existing methods, highlighting specific novel aspects of their approach, e.g., a specific new method or a new framework of well incorporating existing techniques.
2. The multi-grained entity graph and iterative retrieval, while effective, could be computationally intensive, limiting scalability in resource-constrained environments. Therefore, authors should conduct time and space complexity analyses, as well as perform corresponding experiments for verification, such as the Inference Time and  the Time per Iteration.
3.Some experimental details are missing, such as hardware specifications, number of iterations, the stopping condition for iterative retrieval, and the convergence criteria for all models.
4.  About " we employ context aggregation algorithms to integrate both local and global contexts of the same entity, and utilize an LLM, EntiGraph, to generate multi-grained QA pairs (i.e., micro-level, feature-level, and macro-level). This multi-level strategy not only ensures that the model produces highly accurate answers for complex queries, but also mitigates the fragmentation of information that often hampers traditional methods",  1) the "EntiGraph" is a LLM model? 2) why generate multi-grained QA pairs from micro-level, feature-level, and macro-level, and what are the insights about these? 3) why this multi-level strategy can ensure high accurate answers? 4) does this strategy lead to much noise?
5. The model is relatively complex, and the paper fails to clearly present the training and optimization process of the model. 1）How to perform joint optimization among multiple modules, i.e., ITERATIVE RETRIEVAL AGENT, MULTI-GRAINED REPRESENTATION, ENTITY EXTRACTION? How is the training data for each module constructed?  For each entity, how to construct the embeddings for its attributes, relationships, events and temporal information?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses a challenge in hyper-long context QA, where retrieving precise answers from extensive and dispersed content poses substantial obstacles. Current approaches often suffer from limitations, such as input-length constraints in LLMs and semantic loss in RAG systems. The authors propose a multi-grained entity graph-based QA framework, termed MKRAG, that operates across three granularity levels—micro, feature, and macro—to improve information extraction and reasoning across hyper-long texts. Their framework also introduces an iterative retrieval mechanism, LoopAgent, designed to refine retrievals and improve accuracy through multiple rounds. The evaluations across datasets show that MKRAG achieves state-of-the-art results, particularly excelling in scenarios with high granularity requirements, such as long-tail or detail-oriented queries.

### Strengths
1. The multi-grained QA method integrates a graph-based representation of entities and iterative retrieval, allowing the model to retain contextual coherence and retrieve relevant answers from hyper-long contexts.
2. The inclusion of LoopAgent, an iterative retrieval mechanism, improves QA accuracy by refining the search process across multiple rounds, which is particularly beneficial for complex and nuanced queries.
3. The model shows state-of-the-art performance on both hyper-long and moderately long datasets, outperforming baseline models like GPT-4 and other RAG-based approaches on LongBench and InfiniteBench.
4. The model has been effectively deployed in real-world applications, such as online novel-based platforms, and demonstrates enhanced scalability and practical utility in handling real-time queries.

### Weaknesses
1. Although the model circumvents some LLM limitations, the use of a multi-granularity framework and iterative retrieval adds complexity and computational demands, which may be prohibitive for broader real-time applications. How to evaluate the efficiency of the proposed method?
2. The approach heavily relies on accurate entity extraction and structured graph relationships. In cases where entity relationships are sparse or ambiguous, the model's performance may degrade. Do the authors test other entity extraction methods other than EntiGraph?
3. The paper should further discuss trade-offs between different granular levels and how the system decides the optimal level of granularity in real time, especially in cases with sparse information.
4. There are many prompt/context compressing methods that should be included as baselines:
4.1. Jiang, Huiqiang, et al. "Llmlingua: Compressing prompts for accelerated inference of large language models." arXiv preprint arXiv:2310.05736 (2023).
4.2. Jiang, Huiqiang, et al. "Longllmlingua: Accelerating and enhancing llms in long context scenarios via prompt compression." arXiv preprint arXiv:2310.06839 (2023).
4.3. Pan, Zhuoshi, et al. "Llmlingua-2: Data distillation for efficient and faithful task-agnostic prompt compression." arXiv preprint arXiv:2403.12968 (2024).
4.4. Li, Yucheng, et al. "Compressing context to enhance inference efficiency of large language models." arXiv preprint arXiv:2310.06201 (2023).

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2
