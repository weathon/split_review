# EDU-RAG: A RAG Benchmark with Web-enhanced Content in Education Domain. Can RAG Help AI Tutor?

- Decision: Reject
- Scores: 1, 3, 3

## Abstract
Hallucination has been a persistent challenge when using Large Language Models (LLMs). Retrieval-Augmented Generation (RAG) has emerged as a popular approach to mitigate this issue by maintaining context and coherence in generated outputs, as well as incorporating customized knowledge. In this paper, we propose a benchmark dataset for evaluating LLM performance in the domain of middle-school science question answering, using textbook questions augmented with real-world web search results. We assess the performance of various LLMs, including GPT-4o, Llama2-7b, and Llama3-8b, with and without the application of RAG. Our goal is to determine whether RAG can reduce hallucinations stemming from the inherent biases of pre-trained LLMs or from the retrieval of irrelevant knowledge, even when relevant information is accessible. The dataset and methodology introduced here provide a robust foundation for advancing the evaluation and development of RAG techniques in mitigating hallucinations across diverse LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a benchmark dataset for evaluating LLMs in the education domain. Further authors experiment with RAG based approach to reduce hallucinations in LLMs in the context of education.

### Strengths
1. The motivation behind the research in the education domain is relevant and apt.
2. Authors create a new dataset of MCQA for middle school level science. The dataset is augmented with information obtained via web-searches.

### Weaknesses
1. The paper lacks novelty as authors are implementing the standard RAG architecture for the QA task. 
2. The newly created dataset is mainly an extension of an existing TQA dataset augmented with content from the web, so there is very limited innovation.  
3. The paper doesn't report any new findings; the authors show that RAG helps to mitigate hallucinations to some extent but this is already known and established by previous research. 
4. The paper is poorly written with grammar mistakes, typos, poor formatting. A figure (Figure 2) is also missing from the paper, in place of that a blank box appears.

### Questions
Suggestions:
1. Authors should improve the formatting of the paper. For example, references are not in parenthesis (e.g., line 33, 35, etc.). Similarly, there are several grammatical mistakes in the paper that authors should fix.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an RAG benchmark in the education domain. The benchmark builds on top of AI2's TQA dataset, augmented with web search results for each question. The paper evaluates a few LLMs on performance on this benchmark where the metric is answer correctness (note that the author defined "hallucination" in terms of answer correctness). The author finds that RAG improves performance of LLMs in answering these questions. The author claims this benchmark will be useful for "advancing the evaluation and development of RAG techniques in mitigating hallucinations across diverse LLMs."

### Strengths
I like the direction that this paper attempts to go: evaluating and benchmarking RAG systems and LLMs and checking whether they hallucinate is very important. Doing all of these in the context of education is also important. I'm excited to see more work along this direction.

### Weaknesses
The paper seems to be poorly presented/written. Contributions seem insufficient and unclear.

In terms of presentation:
- Missing figure (figure 2)
- Table 1 and 2 are repeated 
- Not sure what the example question means in Fig 1 (the question is used multiple times in subsequent results and illustrations)

In terms of contribution:
- It is unclear to me what the *fundamental* differences or advancements that the proposed benchmark has compared to prior work. For example, I'm not sure how this benchmark is different from Yang 2024's. Expanding their dataset to a new domain doesn't seem super novel to me unless there are some fundamental differences or challenges which requires innovations in either constructing the benchmark or evaluating on the data, neither of which I find novel in this paper. This is my main concern.
- The research questions seem to be studying well-known conclusions. For example, RQ2 is, roughly speaking "can RAG help improve LLM performance"? I think the answer is YES by now and it is widely known. When reading the abstract, I thought the authors would evaluate how LLMs would perform in the presence of irrelevant information (line 22 ~ 23), which I think would be a deeper and more interesting analysis than RQ2, but unfortunately the authors did not present such analyses or findings. In general, I find the conclusions and analyses in this paper either already known or shallow.
- Some of the suggested future work is already done a few years ago. For example, SFT on retrieved content is explored in this paper back in 2022: https://arxiv.org/pdf/2201.08239 

Given that the paper appears not ready for presentation and the contributions are unclear and not particularly novel (see above for details), I would not recommend acceptance of this paper.

### Questions
What are the fundamental differences between this benchmark and previous ones? Or more specifically, what are the fundamental differences in the education domain versus finance etc in Yang 2024?

The prompt says "You must choose a letter even if you are unsure." How would one expect the LLM to output "I don’t know” if they are not instructed to do so? 

What motivates the authors to define hallucination as answer correctness? The way the authors defined hallucination seems more like model's problem solving or reasoning capabilities rather than hallucination.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces EDU-RAG, a benchmark dataset designed to evaluate the performance of Retrieval-Augmented Generation (RAG) techniques in the context of middle-school science question answering. The dataset combines textbook questions with relevant web search results, addressing the challenge of hallucination in Large Language Models (LLMs) like GPT-4o and Llama2-7b.

### Strengths
Originality: The paper presents a new benchmark dataset, EDU-RAG, specifically tailored for evaluating RAG techniques in the domain of middle-school science question answering. 
Quality: The methodology for constructing the benchmark dataset is explained, including the selection of questions, retrieval of web content, and processing of the data.
Clarity: The authors also provide a comprehensive overview of related work, placing their contributions within the broader context of RAG research.
Significance: The EDU-RAG benchmark has the potential to significantly advance the evaluation and development of RAG techniques for educational applications.

### Weaknesses
- The paper only evaluates a basic RAG algorithm design, consisting of a retriever, reranker, and generator. While this serves as a useful baseline, it does not explore the effectiveness of more advanced RAG techniques, such as modular RAG or advanced reranking methods.
- The paper acknowledges that RAG can reduce hallucination in some cases but also highlights instances where it may worsen the issue. However, the analysis of this phenomenon is limited, and the paper does not delve into the underlying reasons of it.
- Typo: The title of section References appears twice.
- Missing figure: The figure 2 is missing.

### Questions
- Have you considered expanding the scope of evaluation to include more complex question answering scenarios, such as open-ended questions or multi-hop reasoning tasks for educational applications?
- How did you address the potential bias in the web content retrieved using Google Search?
- How did you assess the quality and relevance of the web content retrieved for each question?

### Soundness
2

### Presentation
1

### Contribution
1
