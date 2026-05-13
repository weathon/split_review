# Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We present chain-of-knowledge (CoK)
, a novel framework that augments large language models (LLMs) by dynamically incorporating grounding information from heterogeneous sources. It results in more factual rationales and reduced hallucination in generation. 
Specifically, CoK consists of three stages: reasoning preparation, dynamic knowledge adapting, and answer consolidation. 
Given a knowledge-intensive question, CoK first prepares several preliminary rationales and answers while identifying the relevant knowledge domains.
If there is no majority consensus among the answers from samples, CoK corrects the rationales step by step by adapting knowledge from the identified domains.
These corrected rationales can plausibly serve as a better foundation for the final answer consolidation.
Unlike prior studies that primarily use unstructured data, CoK also leverages structured knowledge sources such as Wikidata and tables that provide more reliable factual information.
To access both unstructured and structured knowledge sources in the dynamic knowledge adapting stage, we propose an adaptive query generator that allows the generation of queries for various types of query languages, including SPARQL, SQL, and natural sentences. Moreover, to minimize error propagation between rationales, CoK corrects the rationales progressively using preceding corrected rationales to generate and correct subsequent rationales. %  dynamically grounds each rationale, \ie iteratively 
Extensive experiments show that CoK consistently improves the performance of LLMs on knowledge-intensive tasks across different domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is a very interesting paper on Chain of Knowledge and integrating the question answering from LLM with traditional source of knowledge such as KG to improve the overall accuracy of question answering in domain-specific text.
Main contributions:
1. Chain of Knowledge for factual correctness
2. Adaptive query generator for identifying knowledge source and converting queries in respective form
3. Progressive correction of rationale using CoK
4. Following domains have been chose for the work factual, medical, physical, and biological.

### Strengths
The paper is very well written.
The authors have considered good number of scenarios for knowledge, and carefully selected wikidata as the knowledge source, provided the limitation on retrieval of knowledge in general.
I enjoyed reading this paper.

### Weaknesses
Please see the questions section for more.

* For the given SPARQL query SELECT ?answer WHERE { wd:/Souleymane Sane/ wdt:/child/ ?answer . ´ }, do you use some library to convert the entities/relation in their specific identifier form (entity linking), how do you know which is the correct identifier, in specific cases where similar natural language entities have two identifiers.
* Did you try domain specific questions with ChatGPT? Upon trying the example given in Figure 1 on ChatGPT, I could see the result as George Gamow. Maybe you should come up with an example where ChatGPT would hallucinate. Or if the idea here is to show open source LLM, then this example makes complete sense. Although it should be mentioned in this case which model is used (Llama2-7b-chat? or instruction tuned by yourself)
* It is possible that the knowledge injected through Wikidata doesn't answer the question asked, what would be done to answer the question in that case?
* Can you please explain how do you find specific relation for querying with an entity? There is a possibility of multiple entity attached with one relation. It is also possible that multiple relations connected with multiple entities, and it may be difficult to identify the relation depending on the question. What would be done in that case?

### Questions
* For the given SPARQL query SELECT ?answer WHERE { wd:/Souleymane Sane/ wdt:/child/ ?answer . ´ }, do you use some library to convert the entities/relation in their specific identifier form (entity linking), how do you know which is the correct identifier, in specific cases where similar natural language entities have two identifiers.
* Did you try domain specific questions with ChatGPT? Upon trying the example given in Figure 1 on ChatGPT, I could see the result as George Gamow. Maybe you should come up with an example where ChatGPT would hallucinate. Or if the idea here is to show open source LLM, then this example makes complete sense. Although it should be mentioned in this case which model is used (Llama2-7b-chat? or instruction tuned by yourself)
* It is possible that the knowledge injected through Wikidata doesn't answer the question asked, what would be done to answer the question in that case?
* Can you please explain how do you find specific relation for querying with an entity? There is a possibility of multiple entity attached with one relation. It is also possible that multiple relations connected with multiple entities, and it may be difficult to identify the relation depending on the question. What would be done in that case?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a chain-of-knowledge framework to augmenting LLM in question answering by dynamically retrieving the grounding information from multiple sources. The proposed method first gives the rationale in steps. Then the search query is generated by determining the domain involved in each rationale and the final query. Eventually, the rationale is corrected by the information obtained from the query to give a more plausible answer. The authors conducted experiments on multiple datasets and defeated the compared few-shot methods.

### Strengths
1. This article proposes a novel idea to reduce the hallucination of LLM by correcting each rationale in the chain of thought.
2. The proposed method considers structured and unstructured queries for heterogeneous data sources.
3. The authors conducted detailed experiments and analysis on multiple datasets from different domains.

### Weaknesses
1. The general outline of the suggested approach is somewhat understandable, but the crucial stages lack the necessary level of specificity. In my opinion, a key point in the effectiveness of the proposed method is how to construct accurate queries to retrieve grounding information, but the description in section 3 is still not clear enough. For example, the paper does not detail the process of creating a high-quality question-SPARQL dataset, which is crucial for training the adaptive query generator. While the prompt used with the training loss function is provided in the appendix by the authors, I believe it is important for the main body of the paper to be self-contained, and critical steps like this should not solely rely on the information provided in the appendix.
2. How does the author determine the table or tables used when generating a SQL query for a rationale, and how can they ensure that the query generated by ChatGPT is valid and answerable if table schema information is not provided. Ditto for SPARQL. Specifically, for SQL, how does the system handle complex table joins or nested queries, and how is the generated query validated against the table schema before execution? For SPARQL, how does the system ensure that the generated query aligns with the ontology and avoids syntax errors or non-existent properties and classes?
3. Baseline performance on the hotpotQA dataset seems too poor. Existing work [1] has achieved an accuracy of 0.37 when reviewing ChatGPT.

### Questions
1. How does the author ensure that LLM can give faithful answers (query) when performing knowledge adaptation?
2. The proposed method leaves the decomposition of the question (i.e., the generation of each rationale) to ChatGPT. I am interested in whether this method is only applicable to chain-style question? For more complex questions, where the corresponding SPARQL contains more than one inference path, can the proposed method handle it?
3. When generating SQL (SPARQL) queries, how do the authors guarantee that the produced queries are valid?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the chain-of-knowledge (CoK) framework designed to augment the performance of LLMs by reducing instances of information hallucination and improving factual correctness. The CoK operates in three stages: reasoning preparation, dynamic knowledge adaptation, and answer consolidation. A distinctive feature of CoK is its ability to dynamically tap into diverse knowledge sources, including structured databases like Wikidata, using an adaptive query generator (AQG) capable of generating varied query languages, such as SPARQL, SQL, and natural language queries. The framework emphasizes progressive correction of the generated rationales, minimizing the risk of error propagation across reasoning steps. Experimental evaluations indicate that CoK enhances the performance of LLMs on knowledge-intensive tasks across different domains, surpassing the chain-of-thought (CoT) baseline by an average of 4.3%.

### Strengths
- CoK addresses the inherent limitations of existing methods by leveraging diverse knowledge sources, both structured and unstructured, improving the accuracy and factual correctness of LLM outputs.
- The adaptive query generator (AQG) showcases versatility, enabling seamless transition between specialized models and generic LLMs, allowing effective querying across different knowledge source formats.
- Progressive rationale correction reduces the risk of error propagation, ensuring more reliable generation of answers.
- Comprehensive experiments covering various knowledge domains, demonstrating a consistent performance boost over the CoT baseline.

### Weaknesses
 - While the paper emphasizes the use of diverse knowledge sources, it might benefit from a more explicit discussion on the scalability and efficiency of the framework as the volume and variety of sources grow. Specifically, the paper lacks a detailed analysis of how the system's performance would degrade with an increasing number of knowledge sources, and how the retrieval time would be affected. This is crucial for real-world applications where the number of sources can be very large.
- The framework's dependence on the AQG's capability to generate effective queries for all types of knowledge sources might be a potential bottleneck, especially for highly specialized domains. The paper does not provide a thorough analysis of the AQG's performance across various query languages and knowledge sources, and it's unclear how the system would handle cases where the AQG fails to generate an effective query. This is a critical point that needs further investigation, including performance analysis of AQG on specialized domains with less common query languages.
- Although the paper mentions improvement over the CoT baseline, deeper insights into the limitations and areas where CoK might not perform optimally would be beneficial. Except for the limitations of “Knowledge Sources” and “Knowledge Retrieval” discussed in Appendix G. The paper would benefit from a more detailed error analysis, exploring the types of questions where CoK fails, and why it fails. This would provide a more comprehensive understanding of the framework's capabilities and limitations.

### Questions
- How does the CoK framework handle situations where knowledge sources provide conflicting information? How are you going to solve it?
- What are the computational overheads introduced by the AQG and the dynamic knowledge adaptation process, especially when querying multiple heterogeneous sources?
- Have there been considerations or plans to extend the CoK framework to accommodate real-time or streaming knowledge sources?
- Can you provide insights into the training and fine-tuning process of the AQG, especially its adaptability across different query languages and knowledge sources?

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
This paper proposed chain-of-knowledge (CoK), a novel framework that augments LLMs by dynamically incorporating grounding information from heterogeneous sources. The CoK framework consists of three stages, reasoning preparation, dynamic knowledge adapting, and answer consolidation. This paper provided rich experiments and analysis.

### Strengths
S1. This paper proposed chain-of-knowledge (CoK), a novel framework to enhance the factual correctness of LLMs with heterogeneous knowledge sources. CoK can dynamically select one or multiple knowledge sources based on the types of questions.

S2. Cok participates in Cot which modifies incorrect answers in each reasoning step by introducing external knowledge, thereby generating the correct answer.

S3. This paper performs extensive experiments on knowledge-intensive tasks spanning a range of domains, including factual, medical, physical, and biological.

### Weaknesses
This paper bears a high resemblance to VE with the main distinction being the inclusion of multiple knowledge sources, which might be considered a relatively ordinary contribution. The AQG retrieves relevant knowledge from multiple knowledge sources by converting questions into SPARQL, SQL, and natural language queries. The SPARQL query generator is fine-tuned based on question-SPARQL pairs. I think this training process may make it challenging for AQG to generate SPARQL queries for complex and compositional questions. Because it cannot guarantee that the sub-questions derived from the CoT decomposition are all simple.

### Questions
Q1. The authors specifically evaluated the proposed framework in experiments, with a focus on the biology, medical, and physics domains, showing better results compared to the VE method. The knowledge sources used by the author include Wikidata, medical Flashcard, UpToDate, ScienceQA Physics, and ScienceQA Biology. I'm wondering if the authors also incorporated these knowledge sources into the VE method. If not, I believe such a comparison would be unfair.

Q2. LLMs generate multiple results based on self-consistency, if the consistency falls below a threshold, the proposed method is initiated to correct the answer. I'm curious about how often such a process needs to be introduced in practical experiments. Which of the three extraction methods (natural language, SPARQL, and SQL) do the authors consider to be more reliable for LLMs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
