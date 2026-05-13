# Needle Threading: Can LLMs Follow Threads Through Near-Million-Scale Haystacks?

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
As the context limits of Large Language Models (LLMs) increase, the range of possible applications and downstream functions broadens. In many real-world tasks, decisions depend on details scattered %
across collections of often disparate documents containing mostly irrelevant information. Long-context LLMs appear well-suited to this form of complex information retrieval and reasoning, which has traditionally proven costly and time-consuming.
However, although the development of longer context models has seen rapid gains in recent years, our understanding of how \textit{effectively} LLMs \textit{use their context} has not kept pace.
To address this, we conduct a set of retrieval experiments designed to evaluate the capabilities of 17 leading LLMs, such as their ability to follow threads of information through the context window.
Strikingly, we find that many models are remarkably \textit{thread-safe}: capable of simultaneously following multiple threads without significant loss in performance. 
Still, for many models, we find the \textit{effective context limit} is significantly shorter than the supported context length, with accuracy decreasing as the context window grows.
Our study also highlights the important point that token counts from different tokenizers should not be directly compared---they often correspond to substantially different numbers of written characters.
We release our code and long context experimental data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce simple single-needle retrieval, multiple-needle and conditional-needle retrieval and challenging needle threading and multithreading retrieval. Experiments on haystacks consisting of key-value pairs of UUIDs shows the retrieval precisions of 17 LLMs vary on different context lengths, multiple-needle and multiple threading conditions.

### Strengths
The paper focuses on an interesting problem: how effectively LLMs use their context. 
The observations from the experiments are inspiring, for example, many models are remarkably thread-safe: capable of simultaneously following multiple threads without significant loss.

### Weaknesses
Only one synthetic dataset is used for evaluation.

### Questions
What is the time complexity (running/response time) of each LLM that is used for evaluation in different experiment settings?

### Soundness
3

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
2

### Summary
The paper evaluates the performance of Large Language Models (LLMs) as their context limits increase, focusing on their ability to handle complex information retrieval across multiple documents. Through experiments with 17 leading LLMs, the study finds that while many models effectively manage multiple threads of information, their actual efficient context range is often shorter than their maximum allowed, leading to reduced performance as the context window expands. The research also highlights inconsistencies in token counts across different tokenizers. Results and methodologies are made available for further study.

### Strengths
Note: This is a review by an emergency reviewer. 

The paper addresses an intriguing and valuable research problem by exploring the utility of synthetic data for abstract tasks in the context of long-sequence processing.

Introducing multi-threading tasks as part of the experimental setup is particularly innovative. 

The findings of the paper offer practical insights that could inform both the academic and industry sectors about the design and tuning of language models for specific applications.

### Weaknesses
 Note: This is a review by an emergency reviewer. 

The major concern is that there's a gap between experimental design and real-world applications. The study employs highly abstract tasks using synthetic data with no natural language semantics, deviating considerably from the typical environments where large language models (LLMs) operate. The string-serialized JSON objects and UUIDs as key-value pairs fail to engage the models in natural language processing—core to their training and operational objectives. Consequently, the findings have limited applicability to real-world scenarios that demand comprehension, generation, and manipulation of actual linguistic content. This gap undermines the relevance of the research to practical applications of LLMs, which are primarily designed to interact with and generate coherent, contextually appropriate natural language.

The authors mention that they have released their code and experimental data for public use. However, the authors didn't upload supplemental materials to the open review nor include an anonymous link of their data and code. I would suggest sharing the code through an anonymous GitHub repository or similar platform. This would greatly aid other researchers and reviewers in replicating and understanding the research.

### Questions
Please refer to the previous section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the ability of Large Language Models (LLMs) to handle complex information retrieval and reasoning tasks across long contexts. The authors conduct a series of retrieval experiments with 17 leading LLMs to assess their capability to follow information threads within extensive context windows, revealing that while many models can manage multiple threads without significant performance loss, their effective context limits are often shorter than their technical limits. The study also emphasizes the variability in token counts between different tokenizers, which affects model performance comparisons. A key contribution is the introduction of a task-specific effective context limit metric, which provides a more nuanced understanding of model capabilities in long-context scenarios.

### Strengths
1. This paper provides an extensive evaluation of 17 leading LLMs across various long-context retrieval tasks, offering a thorough analysis of their performance in handling complex information retrieval and reasoning.

2. Through innovative needle threading and multi-threading experiments, the study creates scenarios where LLMs must follow chains of information across different parts of the context, effectively testing their limits in long-context understanding.

3. Analysis reveals significant differences in tokenization between models, crucial for understanding the discrepancies in reported context lengths and making accurate comparisons between LLMs.

4. The authors propose a task-specific and configurable metric independent of tokenization, enabling more precise assessment of models' reasoning capabilities over context.

### Weaknesses
1. The study's exclusive use of synthetic data (UUID key-value pairs) may not accurately reflect performance on natural language tasks or domain-specific applications. The reliance on UUIDs, while useful for controlled experiments, does not capture the nuances of semantic relationships, syntactic structures, and contextual dependencies present in real-world text. This could lead to an overestimation of the models' true long-context capabilities when applied to more complex, natural language scenarios.

2. The paper may be limited in techinical contribution. While the experiments are thorough and the analysis is insightful, the core methodology largely involves applying existing LLMs to a novel evaluation task. The introduction of the task-specific effective context limit metric is a valuable contribution, but the overall technical novelty of the approach might be considered incremental rather than transformative. The study does not introduce new architectural components or training techniques for LLMs, which could limit its impact on the field.

### Questions
1. Have you considered conducting smaller-scale validation experiments with natural language data to verify if the findings generalize?

2. For the branched threading task, why was it only evaluated on a subset of models and smaller context sizes?

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
This paper executed a set of experiments to evaluate the capabilities of 17 LLMs to perform retrieval tasks with long contexts. It introduces challenging multi-step threading and multi-threading retrieval tasks to test the models' ability to track information through extended contexts. The results show that increased context length reduces retrieval performance, with accuracy generally decreasing as the context window grows. The authors also demonstrate that many leading LLMs are thread-safe. Additionally, they highlight significant differences in token counts across different tokenizers.

### Strengths
(1) This paper studies an important aspect of LLMs -- their ability to manage long contexts -- which hasn't been fully explored yet.

(2) The paper is well-written.

(3) The task designs are comprehensive and insightful, especially the comparison between forward and backward threading.

(4) The experiments are extensive, and the results provide valuable insights into LLM performance with long contexts.

### Weaknesses
 (1) Code and data are not currently shared.

(2) The experiments in the paper rely on abstract retrieval tasks using synthetic data. These tasks can not reflect the complexity found in real-world, domain-specific applications. In practice, data often includes ambiguous language, diverse formats, and contextually relevant nuances. Moreover, the experiment design cannot test the model's ability to understand semantics.

### Questions
Given that the experiments rely on synthetic, abstract tasks, how do you anticipate the performance trends observed in your study would translate to real-world, domain-specific applications with more complex and noisy data?

### Soundness
3

### Presentation
4

### Contribution
3
