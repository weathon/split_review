# From Complex to Atomic: Enhancing Augmented Generation via Knowledge-Aware Dual Rewriting and Reasoning

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Recent advancements in Retrieval-Augmented Generation (RAG) systems have significantly enhanced the capabilities of large language models (LLMs) by incorporating external knowledge retrieval. However, the sole reliance on retrieval is often inadequate for mining deep, domain-specific knowledge and for performing logical reasoning from specialized datasets. To tackle these challenges, we present an approach, which is designed to extract, comprehend, and utilize domain knowledge while constructing a coherent rationale. At the heart of our approach lie four pivotal components: a knowledge atomizer that extracts atomic questions from raw data, a query proposer that generates subsequent questions to facilitate the original inquiry, an atomic retriever that locates knowledge based on atomic knowledge alignments, and an atomic selector that determines which follow-up questions to pose guided by the retrieved information. Through this approach, we implement a knowledge-aware task decomposition strategy that adeptly extracts multifaceted knowledge from segmented data and iteratively builds the rationale in alignment with the initial query and the acquired knowledge. We conduct comprehensive experiments to demonstrate the efficacy of our approach across various benchmarks, particularly those requiring multihop reasoning steps. The results indicate a significant enhancement in performance, up to 12.6\% over the second-best method, underscoring the potential of the approach in complex, knowledge-intensive applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper describes an approach to enhance and use knowledge in RAG setting to improve the overall of reasoning performance of LLMs. Paper proposes atomiser, a question generation for a given query/chunk. It uses the questions generated from the query to generate questions using LLM and use it in retriever to retrieve the context chunks. These are further used to generate any missing context by iteratively decomposing queries to gather mode suitable context to answer the given query and the final answer is generated using this process.

### Strengths
Paper is easy to follow and authors have done good job in explaining the overall method with good examples. Method shows consistent improvements across all the chosen benchmarks which require reasoning. Another strong point I see is knowledge augmentation is happening with query decomposition and context gathering, rather than going through KG generation etc, which can be more involved and can introduce another place for injecting errors.

### Weaknesses
Authors have no talked about the overhead this method introduces in terms of generating the final answer in terms of response time/ cost of using LLM in the whole process.

### Questions
Do any of the existing query decomposition techniques be used as is without using LLM here ? For example for the of interest in example presented in Figure 2, main questions needed are who is the direct of the film and who is the mother or parent of person X . Can't this be done using other methods ?

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
This paper introduces KAR-RAG, a novel RAG framework that improves retrieval efficacy through knowledge rewriting. Specifically, for each document chunk, KAR-RAG generates a set of atomic questions to label the available knowledge contained in the chunk, and use these atomic questions as indices for document chunk retrieval.

### Strengths
1. The paper is well-organized, and main components of the method (knowledge atomizer, query proposer, atomic retriever, atomic selector) are explained smoothly. 
2. The paper proposes a novel rewrite-and-index approach to tackle retrieval-augmented generation.
3. Experiments conducted on both open-domain and domain-specific datasets demonstrate that KAR-RAG achieves state-of-the-art results.

### Weaknesses
1. The construction of KAR-RAG's atomic knowledge base can be highly cost-intensive, as generating atomic questions for each document chunk for a large text corpus leads to extensive LLM API consumption. The authors did not include a cost analysis to address this.
2. The paper’s motivation is a bit ambiguous. While the authors claim that the work focuses on enhancing “domain-specific knowledge mining” and “complex logical reasoning”, the paper lacks clear explanation on how KAR-RAG resolves these issues. Instead, it seems like KAR-RAG is a framework enhancing knowledge retrieval in general, showing no specific improvement over either “domain-specific knowledge mining” or “complex logical reasoning”. 
3. The paper does not compare more recent and well-performing RAG baselines such as SearChain, ProbTree, etc, which may yield better results than KAR-RAG.

### Questions
When discussing the paper’s motivation, the authors could consider to address the challenge of accurate retrieval in general, instead of claiming to improve domain-specific knowledge retrieval (which may lead to misunderstandings on the paper’s core motivation).
Refered to Weaknesses session.

### Soundness
2

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
This paper introduces a novel Retrieval-Augmented Generation (RAG) framework called KAR-RAG, which enhances retrieval efficacy by incorporating a knowledge-aware task decomposition strategy. KAR-RAG decomposes complex queries into atomic questions, enabling more effective retrieval and logical reasoning from specialized datasets. The framework consists of four key components: a knowledge atomizer, query proposer, atomic retriever, and atomic selector, which collaboratively extract and utilize domain-specific knowledge to construct coherent rationales, achieving up to a 12.6% performance improvement over existing methods in multihop reasoning tasks.

### Strengths
1. This paper propose to enhance the RAG system with atomized knowledge retrieving mechnism. In particular, this paper designs knowledge atomizer, query proposer, atomic retriever, and atomic selector to construct the pipeline.
2. Experiments on complex question answering datasets show that the proposed method is effective.
3. The presentation of this paper is clear and easy to follow.

### Weaknesses
1. The effectiveness of each individual components should be further explored. For example, what if the knowledge is mingled together, rather than presented in atomic simple questions.
2. Lack of related works and baselines. This paper should survey and compare with more powerful RAG methods that elaborates on question decomposition, for example:
    - https://arxiv.org/pdf/2404.14464
    - https://arxiv.org/pdf/2406.19215

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper points out that the semantic retrieval is inadequate for mining deep, domain-specific knowledge for performing logical reasoning. The authors propose a knowledge-aware task decomposition strategy that extracts, comprehends, and utilizes atomic domain knowledge while constructing a coherent rationale.

### Strengths
S1.  Supplementing semantic retrieval-based RAG with fine-grained and atomic knowledge is a novel and realistic practice.

S2. The proposed strategy is easy to understand and follow.

S3. The experimental results are explicitly competitive.

### Weaknesses
W1. Regardless of the novel motivation, the explanation of the motivation is poor. The authors claim that ‘Current RAG methods relying on semantic retrieval fall short in deep domain-specific reasoning’. However, they do not specify the main challenges in domain-specific reasoning and why current RAG methods fall short in this setting. It will make this paper clearer and more convincing to clarify the above points.

W2. The proposed strategy includes using GPT4 to atomize raw chunks into sub-queries, using GPT4 to decompose the incoming queries, and using GPT4 to select optimal contexts and judge the termination. It’s more like a pipeline. Please point out the main technical challenges through this pipeline and the main technical contributions to solve the challenges.

W3. The proposed strategy relies highly on calling LLMs, which costs much. The dependence on the capability of GPT4 makes the proposed strategy inefficient and cost-intensive. Is there any cost analysis comparing the proposed strategy to baselines?

### Questions
The proposed strategy is dependent on GPT-4, which is expensive. Do cheaper LLMs fit in the pipeline? Are there any experiments or analyses with less expensive models? How might the performance be expected to change with different LLMs?

### Soundness
2

### Presentation
2

### Contribution
2
