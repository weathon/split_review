# Holistic Reasoning with Long-Context LMs: A Benchmark for Database Operations on Massive Textual Data

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
The rapid increase in textual information means we need more efficient methods to sift through, organize, and understand it all. While retrieval-augmented generation (RAG) models excel in accessing information from large document collections, they struggle with complex tasks that require aggregation and reasoning over information spanning across multiple documents--what we call  \textit{holistic reasoning}. Long-context language models (LCLMs) have great potential for managing large-scale documents, but their holistic reasoning capabilities remain unclear.  In this work, we introduce HoloBench, a novel framework
that brings database reasoning operations into text-based contexts, making it easier to systematically evaluate how LCLMs handle holistic reasoning across large documents. Our approach adjusts key factors such as context length, information density, distribution of information, and query complexity to evaluate LCLMs comprehensively. 

Our experiments show that the amount of information in the context has a bigger influence on LCLM performance than the actual context length. Furthermore, the complexity of queries affects performance more than the amount of information, particularly for different types of queries. Interestingly, queries that involve finding maximum or minimum values are easier for LCLMs and are less affected by context length, even though they pose challenges for RAG systems. However, tasks requiring the aggregation of multiple pieces of information show a noticeable drop in accuracy as context length increases.  Additionally, we find that while grouping relevant information generally improves performance, the optimal positioning varies across models. Our findings surface both the advancements and the ongoing challenges in achieving a holistic understanding of long contexts. These can guide future developments in LCLMs and set the stage for creating more robust language models for real-world applications.co/datasets/megagonlabs/holobench} \\
\end{tabular}
\end{center}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents HoloBench, a benchmark designed to evaluate the holistic reasoning capabilities of Long-Context Language Models (LCLMs). While Retrieval-Augmented Generators (RAGs) effectively access information from large document collections, they struggle with complex tasks that require aggregation and reasoning across multiple documents. The authors refer to this as holistic reasoning, for which long-context language models have been developed. HoloBench aims to evaluate LCLMs against RAGs under various conditions.

Although similar datasets have been created in the past, this dataset is more comprehensive in terms of context length, information density, information distribution, and query complexity, and it includes automated evaluation methods.

### Strengths
The code has been released, and the data is reproducible. I believe the authors are providing a valuable service to the community.

### Weaknesses
From a technical standpoint, this method is relatively straightforward.

### Questions
How do you differentiate between long but simple questions and genuinely complex ones?

### Soundness
3

### Presentation
4

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
The authors propose a new comprehensive benchmark to test the reasoning capabilities of LCLM across multiple dimensions. The authors unveil a range of novel insights from this benchmark, by comparing the performance of recent LCLM on diverse scenario (position of the information, density of information, complexity of the query).

### Strengths
The authors :
- Proposed a new, original, comprehensive and timely benchmark dataset and framework based on text-to-sql for consistent long context LM benchmarking
- Important benchmark dataset and frameworks, showing novelty into aspects of LCLM seemingly not thoroughly explored yet
- Identified a range of novel and important insights about LCLM reasoning (lost in the middle comparison, model size, RAG comparison, query complexity effect, CoT importance)
- Tested recent LCLM (Llama 3.1, GPT4o, Claude 3.5, Gemini 1.5)
- Used LLM-based evaluation metrics, but which showed 93.8% agreement with human judgements
- Good paper layout to quickly identify important insights derived from the benchmark
- Good discussion points on RAG contribution

### Weaknesses
 1. Limited benchmark size:
According to Section 3.3, HoloBench consists of only 90 questions, which is significantly smaller in scale compared to other benchmarks like BABI Long and NOCHA. The small size of the benchmark makes it susceptible to randomness, compromising the reliability of the evaluation results.

2. Lack of diversity and practicality:
Since each database table stores data of a similar type, the data constructed by HoloBench tends to be highly homogeneous and confined to a single scenario dictated by the original database. Compared to other benchmarks that use richly varied books as a base corpus for long-context tasks, HoloBench, built from individual databases within a single text-to-SQL dataset, lacks diversity and richness, offering limited scenarios.

3. Limited challenge:
In HoloBench, rows from relevant and irrelevant tables are merged as relevant and irrelevant contexts, respectively. However, data stored in different tables of a database typically exhibit noticeable differences, allowing LLMs to potentially distinguish between relevant and irrelevant contexts with ease. This suggests that the tasks provided by HoloBench may not be sufficiently challenging.

4. Evaluation fairness and reliability:
HoloBench uses GPT-4-mini as its evaluation metric, which leads to potential uncontrollability and unfairness in evaluation. The human judgm

### Questions
/

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces HoloBench, a benchmark aimed at evaluating the holistic reasoning capabilities of Long-Context Language Models (LCLMs) when handling multi-document contexts. The framework aims to systematically assess LCLMs by controlling factors like context length, information density, distribution, and query complexity. The study uses a text-to-SQL dataset and corresponding databases to generate dataset for evaluating long-text language models. Based on proposed benchmark, the study shows that the quantity of information within the context more significantly impacts model performance than the pure length of the context. The findings provide insights into the strengths and limitations of LCLMs in processing large-scale text.

### Strengths
1.The paper offers a reasonable definition of the holistic reasoning capability of LLMs. The motivation of employing a text-to-SQL dataset to construct an evaluation framework for the holistic reasoning capabilities of Long-Context Language Models is reasonable.
2.The methodologies of benchmark construction are reasonable, for example, constructing data with varying difficulty levels and types based on the inherent difficulty classifications of the text-to-SQL dataset and the types of queries.
3.Given that the extractable information from databases can be freely controlled, the proposed Automated and Scalable Evaluation is practical.
4.The paper is written in a concise and coherent manner, offering illustrative figures that facilitate comprehension. The experiment results are clearly presented and easy to read.

### Weaknesses
1. The reality and the quality of the corpus/context is unclear. The author decided to generate the context by verbalizing data rows, which may lead to a set of unrealistic documents/passages with a simple description of attribute values in each row. Furthermore, there is no study in this paper that can show that the verbalization process is faithful to the original tables/rows.

2. The discussion about RAG and LCLMs are flawed. It does not make sense at all that limited RAG only retrieving 2k tokens and compared it with a language model that can be fed with 4k to 16k context.

### Questions
Please answer the concerns in the above weaknesses section and the questions below:

1. Selection of databases:
According to reference [1], Spider consists of 200 different databases, yet as stated in line 214 of the paper, HoloBench only employs five databases from it. What was the reason behind selecting these specific five databases? Would the findings apply consistently across other databases and other scenarios as well?
[1] Spider: A large-scale human-labeled dataset for complex and cross-domain semantic parsing and text-to-SQL task


2. Potential information leakage:
The benchmark is constructed based on a publicly released text-to-SQL dataset from 2018, which might have already been included in the pre-training corpus of existing large language models. This could lead to potential information leakage, where LLMs might arrive at correct answers simply due to prior exposure to the data. Could the authors address this concern?

3. Comparative analysis using long-context models:
In Section 4.3, the authors utilize a document retriever that handles only 2k tokens while experimenting with data ranging from 4k to 64k tokens. This undermines the reliability of the performance comparison between LCLM and RAG. The authors should employ a RAG model that supports long-context processing to conduct this experiment accurately.

### Soundness
2

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
This paper argues that existing RAG systems struggle with complex tasks that require aggregation and reasoning over information spanning across multiple documents, while Long-Context language models may have the potential to this task but there is no study clearly show that. This paper proposed a new framework called HoloBench, which used database operations to generate context to test whether LCLMs can answer the target type of questions. 
The experiments indicate that the amount of information in the context has a bigger influence on LCLM performance than the actual context length as well as the complexity of queries.

### Strengths
1. It is great to see a set of design principles in a paper that is to propose a benchmarking framework.

2. The paper did a comprehensive study of experiments and found interesting observations about factors, such as information amount, context length, information positions and query types and complexity to query performance.

### Weaknesses
1. The reality and the quality of the corpus/context is unclear. The author decided to generate the context by verbalizing data rows, which may lead to a set of unrealistic documents/passages with a simple description of attribute values in each row. Furthermore, there is no study in this paper that can show that the verbalization process is faithful to the original tables/rows.

2. The discussion about RAG and LCLMs are flawed. It does not make sense at all that limited RAG only retrieving 2k tokens and compared it with a language model that can be fed with 4k to 16k context.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
