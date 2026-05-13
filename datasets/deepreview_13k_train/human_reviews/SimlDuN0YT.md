# Logical Consistency of Large Language Models in Fact-Checking

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
In recent years, large language model (LLM) has demonstrated significant success in performing varied natural language tasks such as language translation, question-answering, summarising, fact-checking, etc. Despite LLM’s impressive ability to generate human-like texts, LLMs are infamous for their inconsistent responses – a meaning-preserving change in the input query results in an inconsistent response and attributes to vulnerabilities of LLMs such as hallucination, jail breaking, etc. Consequently, existing research focuses on simple paraphrasing-based consistency assessment of LLMs, and ignores complex queries that necessitates an even better understanding of logical reasoning by an LLM. Our work therefore addresses the logical inconsistency of LLMs under complex logical queries with primitive logical operators, e.g., negation, conjunction, and disjunction. As a test bed, we consider retrieval-augmented LLMs on a fact-checking task involving propositional logic queries from real-world knowledge graphs (KG). Our contributions are three-fold. Benchmark: We introduce three logical fact-checking datasets over KGs for community development towards logically consistent LLMs. Assessment: We propose consistency measures of LLMs on propositional logic queries as input and demonstrate that existing LLMs lack in logical consistency, specially on complex queries. Improvement: We employ supervised fine-tuning to improve the logical consistency of LLMs on the complex
fact-checking task with KG contexts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a method for bench marking LLMs for logical consistency and ways to improve the logical consistency of LLMs through a supervised fine tuning using the fine tuning data. Paper shows how LLMs perform on different logical consistency checks with triples given a context to answer some logical queries and show the effectiveness of improving them with SFT. They propose three benchmark datasets based on three different knowledge bases and show how SFT improves across benchmarks.

### Strengths
Overall benchmarks for checking logical consistency for a given triple context and logical query are good and can help in evaluating logical consistency of LLMs.
Empirical results showing zero shot/prompt and fine tuning results show the improvements across benchmarks.

### Weaknesses
Experiments are more on the benchmark created and not sure how well they translate to real world situations or places where queries are in textual nature and does he supervised model still be able to generalize to textual data as opposed to triple context?

### Questions
After SFT, the models still perform as good on the original language benchmarks as the original model?
Was the goal of the peper to produce a model that does logical consistency in KG RAG kind of setting or in general to improve the logical consistency of LLMs ? if its later I don't see any experiments around other evaluation to show that.

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
3

### Summary
This paper discusses the topic of the logical consistency of LLM when answering complex queries that can be expressed by propositional logic and knowledge extracted from the knowledge graph. The logical consistency is defined by whether the model can answer the logical equivalent query with the same answer. To this end, the author first showcases some examples of non-consistency in query answering of LLM and then uses finetuning instead of prompting to improve the logical consistency of LLM.

### Strengths
1.	The definition of logical consistency is strict and the paper constructs three new datasets for finetuning and evaluating the consistency of LLM.
2.	The construction of the LLMQUERY seems interesting and the author proposes many optimizations towards that.
3.	The experiments show that the logical consistency can be improved by finetuning but not prompting.

### Weaknesses
1. Though being logical consistent is a desirable attribute of LLM, we are also interested in whether it retrieve the correct answer. The logical consistency is only computed by whether the model gives the consistent answer with itself, but whether the answers are true or false are neglected in the experiment. This raises concerns about the practical utility of the proposed consistency metric, as a model could be consistently wrong. The paper does not adequately address the trade-off between consistency and accuracy, and it is unclear if improving consistency necessarily leads to more reliable results.
2. The writing of this paper can be further improved. For example, the Proposition 3 is trivial and kind of redundant. There are also some mistakes like in Line 346 ``more computationally cheaper’’. The paper would benefit from a more rigorous and precise presentation of its core ideas. The current formulation of Proposition 3, for instance, lacks the necessary depth and clarity to justify its inclusion. Furthermore, the presence of grammatical errors detracts from the overall quality of the work.

### Questions
Similar with weakness, I wonder whether the logical consistency helps with the reasoning ability of LLM?

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
This paper tackles the significant issue of logical consistency in responses generated by large language models (LLMs). It emphasizes a gap in current research, where consistency assessments focus primarily on simple paraphrasing rather than complex logical reasoning. The authors address this by examining how LLMs handle propositional logic (involving operators such as negation, conjunction, and disjunction) within a fact-checking framework supported by knowledge graphs (KGs).

### Strengths
There are three main contributions of this paper.
1) Novel Dataset and Benchmarking: Three logical fact-checking datasets FreebaseLFC, NELLLFC, and WikiLFC, derived from knowledge graphs.
2) Evaluating LLMs on these new fact-checking datasets. The paper includes a variety of experimental setups, including comparisons of zero-shot instruction prompting and supervised fine-tuning, adding depth to the evaluation of LLMs' logical consistency. Results show that existing LLMs are not consistent when considering
logical equivalents or variants of these facts.
3) Improving the consistency of LLMs via supervised fine-tuning

### Weaknesses
1)  While the paper presents methods for extracting relevant KG context through BFS and embedding-based retrieval, it is unclear how effective these methods are in dynamically varying real-world contexts. Expanding this section could strengthen the applicability of the approach. Specifically, the paper lacks a thorough analysis of how the BFS-based context retrieval would perform when the underlying knowledge graph undergoes frequent updates, which is common in real-world scenarios. The embedding-based retrieval, while potentially more robust to changes, also needs a more detailed discussion on how its performance is affected by the evolution of the KG and the computational cost of re-computing embeddings. For example, what is the impact on retrieval accuracy if new entities and relations are added to the KG, and how often would the embeddings need to be updated to maintain acceptable performance?
2) The paper suggests fine-tuning as a solution to improve logical consistency but does not deeply discuss the associated computational overheads and limitations, which may impact the scalability of this approach for large datasets or diverse domains. The paper should provide a more detailed analysis of the computational resources required for fine-tuning, including the time and memory requirements, especially when dealing with large language models and extensive datasets. Furthermore, the paper should discuss the potential limitations of fine-tuning, such as overfitting to the training data and the difficulty of generalizing to new domains or types of logical reasoning. For instance, how does the fine-tuned model perform when presented with logical structures that were not present in the training data? 
3) The paper mainly focuses on binary responses, which may limit the generalizability of the method in complex domains. Exploring extensions to multi-class logic and non-binary answer consistency could open avenues for broader applications. Note that a fact might not be binary, e.g., Crimean is a part of Russian. The answer is nether yes or no, but depends on who claims it. The current approach does not address scenarios where the truth value of a statement is not absolute but rather depends on context, perspective, or the source of information. This limitation restricts the applicability of the method in real-world situations where facts are often nuanced and require more than a simple binary classification.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the logical consistency of LLMs in fact-checking using KGs. The authors first formalize the definition of logical consistency for LLMs and concentrate on retrieval-augmented LLMs within a fact-checking task. They propose three benchmarks, FreebaseLFC, NELLLFC, and WikiLFC to demonstrate that several existing LLMs lack logical consistency when handling complex queries, and employ supervised fine-tuning to enhance the logical consistency of these models.

### Strengths
1. This paper is well-written and easy to follow.

2. The logical consistency evaluation of LLMs is rational and interesting.

3. The employed supervised fine-tuning method on LLMs has enhanced the logical consistency performance.

### Weaknesses
1. The authors may want to provide more results across various scales of LLMs (including both smaller models such as Vicuna-68M and larger models like LLaMA2-70B) to comprehensively evaluate the logical consistency issue.

2. The authors may want to include more results from existing fact-checking methods using KGs, such as MiniCheck [1] or RefChecker [2], on the proposed benchmarks.

[1] Minicheck: Efficient fact-checking of llms on grounding documents. EMNLP, 2024.


[2] Refchecker: Reference-based fine-grained hallucination checker and benchmark for large language models. 2024.

3. The third contribution, "Improvement of Logical Consistency," appears somewhat underwhelming. In Table 1, Vanilla LLaMA-2-13B already achieved strong results before fine-tuning, which leads me to wonder whether models like GPT-4o, GPT-o1 exhibit lower levels of logical inconsistency which may be hardly noticeable.

4. The authors may want to discuss and summarize more LLMs with KG contexts methods in related work including [3] to provide a more comprehensive insight.

[3] Coarse-to-Fine Highlighting: Reducing Knowledge Hallucination in Large Language Models. ICML2024.

### Questions
1. Have the authors considered more complex logical expressions or some higher-order Horn rules?

2. The tables in the paper are not formatted as three-line tables, which appears somewhat unusual.

### Soundness
3

### Presentation
3

### Contribution
3
