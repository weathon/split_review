# Test-Time RAG: Enhancing Long Context Understanding in LLMs with Retrieval-Augmented Mechanisms

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Large Language Models (LLMs) are becoming increasingly pivotal in applications that depend on extensive personalized context, such as conversational agents and specialized task-oriented systems. In these scenarios, effective long-context handling is essential to support agentic tasks and enhance in-context learning capabilities. To address this challenge, we propose a novel integration of Retrieval Augmented Generation (RAG) techniques with LLMs, designed to enhance their ability to effectively manage and utilize large contextual information only available at test time. Our methodology, Test-Time RAG (TTRAG), enriches LLMs by dynamically generating novel conditional embeddings coupled with query rewriting and utilizing semantic search to retrieve the most relevant document chunks at test time. This process preserves the context’s meaning and enhances the model’s responsiveness and accuracy in knowledge-intensive Question Answering (QA) tasks. Our evaluations demonstrate our system’s ability synthesize and retrieve information across extensive texts: HotpotQA (+17.29%), QASPER (+4.39%), and Natural Questions (+8.73%), demonstrating the effectiveness of TTRAG across varied context lengths from 1 million to 9.6 million tokens.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose an iterative query rewriting approach that sequentially and conditionally embed the query with retrieved documents to improve long context understanding.

### Strengths
The authors propose to iteratively rewrite the query to improve search results for extensive personalized context, which is a timely problem of interest, with a significant body of literature.

### Weaknesses
Overall confused by the claims of the objective of the work and the actual paper body, it is not clear how the work relates to “long context understanding”, “personalised context”, or “specialised task-oriented systems”.  The authors proposed a rewriting query scheme with iterative embedding, with substantial details missing (and therefore, conclusiveness), see below.

- There is a substantial amount of work on query rewriting and agentic RAG which is not mentioned at all. There is no comprehensive literature review, with the “motivation” section being almost unrelated. Not able to compare to other related papers like “Query Rewriting for Retrieval-Augmented Large Language Models”, among many others.
- “Test-time” term is misleading. Similarly, the authors didn’t clearly show benefits of the approach specifically for “long context”, as claimed. The examples do not illustrate long context, only short context.
- Benchmarks do not seem well suited for the specific problem(s) claimed by the authors. Also, BM25 is not an embedding model.
- Motivation for the conditional compute not clear, context with long context understanding missing. Seems ad-hoc and not reproducible.
- A significant number of question arise, which is caused partially by the lack of reference to state of the art methodologies: how does this work compare to reranking methodologies? What is the latency of the pipeline? When does it stop the iteration loop (what are the stop criterion)? What is the effect of these stop criterion? How significant are the small increments in performance claimed by the authors? 
- Lack of overall reproducibility for different datasets

### Questions
/

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper looks at the problem of long-context RAG and provides 3 steps to solve it. Their overall approach, Test-Time RAG considers a custom embedding approach called Conditional Embeddings, uses query rewriting and then use conditional compute. They evaluate their results on a few different datasets showing consistent improvement in results over baseline.

### Strengths
The paper handles an important problem around long-context RAG. Their approach of using a conditional compute is important and shows the versatility of tasks in a question answering system and how a LLM prompt may not be the best way to do all queries. Query rewriting based on iterative search is an interesting idea too. The problem has practical implications in both research and industry.

### Weaknesses
The paper presents an interesting new perspective on long context retrieval. However the work has some limitations worth considering

1.  Section 3.1 introduces conditional embeddings however the authors do not state they are using pretrained embeddings for the same in this section. It reads like this is a custom embedding. Much later, in Table 1 we understand that the authors have used GPT3.5 embeddings and llama embeddings for the same. This makes reading section 3.1 hard without forward referencing
2. It is not clear why an average across the unmasked tokens in CE embeddings is better than taking a  weighted average (with learned weights)
3. Scalability of solution - how does this solution scale with respect to large datasets of documents ?
4. I do not understand on how you prevent Algorithm 1 to create irrelevant questions if the retrieval is of poor quality. The approach runs the risk of run away poor results on questions which do not have good answers in the database
5. Lack of clarity in what is CE and what is "CE (Filtering only)" in Table 1.
6. Lack of clarify that the model is a LLM model used only for question answering
7. How is F1 score computed? Over how many documents i.e. what is your retrieved k?
8. Whilst I appreciate the principle behind the conditional compute, it's relevance to the rest of the paper is relatively weak. Also how is the LLM leverage For example for count-based queries the map-reduce paradigm that has been recommended, does it mean the LLM generates the code for map-reduce? if not how will this be implemented?
9. The example in Figure 6 is a good example of my earlier comment on Conditional Rewrite. If the "Call me Manana" is not present in the document repository the query rewrite may tag it to some random group (based on what is retrieved) in the way the algorithm is designed/presented. it is not clear how this run-away is prevented to attach it to something random in what has been retrieved. Similar comment on fig 7/8

Overall, while interesting the paper has many unanswered questions. First, it is not clear on the cost vs. benefit analysis for the CE approach. Second, the conditional rewrite has a risk of runaway poor results which need to be addressed. Finally conditional compute is explained but how are some of it implemented is vague. In view of this, this paper in the current form leaves many questions unanswered on its applicability. More clarity on writing is preferable as there is a need to read further to understand the methodology.

### Questions
1. What is the architecture used in the bidirectional encoder? How do the authors arrive at this architecture?
2. Please explain why average of unmasked tokens is better than a weighted sum of the unmasked tokens where the weights can be learned? either a theoretical explanation or an empirical study is preferred.
3. Clearly differentiate between CE vs CE Filtering only
4. What are the performance implications of Test-Time RAG? On the infrastructure which you are using (which is not specified?) how much time and GPU memory does CE introduce? Given the gains in Tables 1 and 2 are relatively less, is it worth the compute?
5. Can statistical tests (even a means test) be done on each of the groups of 3 in tables 1 and 3 highlighting which numbers are statistically better than the baseline and where is CE better than CE Filtering?
6. What are the time impacts on iterative query rewriting ? What is the distribution of the number of rewrites as per the algorithm? how long does the response take with rewrites vs. without on average?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Test-time RAG, a framework that integrates Retrieval-Augmented Generation (RAG) with dynamic query handling at test time. It aims to improve the long-context understanding of Large Language Models (LLMs) by addressing the limitations of static retrieval and pre-indexed document embeddings. The framework consists of three main components: Conditional Embeddings, Iterative Query Rewriting, and Conditional Compute, which work together to enhance context processing dynamically. The paper evaluates Test-time RAG on several benchmarks, showing improved performance in handling complex, long-context retrieval tasks such as knowledge-intensive question answering (QA).

### Strengths
The starting idea is insteresting: dealing with streaming and changing long context with tailored RAG.

### Weaknesses
1. **Poor Writing and Organization**: The presentation of the paper is confusing and difficult to follow due to ambiguous and hard-to-read sentences, poor organization, and unclear structuring of key arguments.

2. **Inconsistent Focus**: The introduction starts by discussing personalized and trustworthy AI, but the subsequent sections focus on long-context benchmarks without sufficiently connecting to the original arguments.

3. **Strange Motivation for Test-time Processing**: The rationale for processing context at test time appears weak, especially given that user history or dynamically changing contexts could be indexed incrementally.

4. **Lack of Component Integration**: The paper presents three distinct components (Conditional Embeddings, Iterative Query Rewriting, Conditional Compute) but does not adequately explain their interrelationship. The experiments are also conducted individually rather than for the overall method, which leaves the effectiveness of the integrated system unclear.

5. **Inefficient Indexing**: The experiments on Conditional Embedding involve incorporating the query into the document indexing process, which makes it impractical because the indexed embeddings cannot be reused efficiently.

6. **Weak Experimental Validation**: The experiments provided are not comprehensive or robust enough to fully validate the effectiveness of the proposed techniques.

7. **Lack of Discussion or Justification**: There is minimal discussion on why or how the proposed techniques improve the results, leaving the reader with questions about the validity and significance of the approach.

### Questions
1.	What is the specific connection between the initial focus on personalized and trustworthy AI and the later focus on long-context benchmarks? Could the authors clarify the relevance of these two aspects?
	2.	Why was the decision made to process context at test time when many changing contexts (e.g., user history) could be indexed incrementally? What benefits does test-time processing offer in these cases?
	3.	How are the three components (Conditional Embeddings, Iterative Query Rewriting, Conditional Compute) related to each other? Could the authors provide a clearer description of how these components work together within the overall system?
	4.	Why were most experiments focused on Conditional Embeddings rather than evaluating the full method? What impact do Iterative Query Rewriting and Conditional Compute have when used together with Conditional Embeddings?

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
4

### Summary
This paper propose test-time RAG, aiming at constructing more contextual text embeddings to improve the retrieval accuracy. This method consists of 3 technologies: conditional embedding, query rewriting and conditional computing. It conducts experiments on 3 RAG datasets with 2 different LLMs and 2 different embedding models, to demonstrate this method can improve models’ performance.

### Strengths
1. The author conducts experiments on 3 RAG datasets with 2 different LLMs and 2 different embedding models to demonstrate the advantage of test-time RAG.

### Weaknesses
1. Poor writing

The author’s presentation is hard to understand. I cannot understand the description of the methods even after reading 10 times, such as the sentence “utilize encoder-decoder variants which jointly condition context on text appearing before and after a given token in a sequence” (line 164).

2. Impracticable time consumption

“Conditional embedding” needs to encode each document in test-time, which will certainly take extremely much more time. Even though the author proposes “conditional computing” to reduce the latency, it can only function on a narrow range of task types such as counting or KV retrieval. But the author did not compare the time latency with that of standard RAG methods on more general problems. This casts doubt on the practical feasibility of this approach in real-world scenarios.


3. Query rewriting may introduce more issues

The author claims that query rewriting can leverage knowledge in LLM’s pretraining data. However, it can be affected by LLM’s hallucination, which is exactly what RAG technology wants to solve. Therefore, in most RAG scenarios, LLMs are allowed to only use knowledge in the retrieved documents instead of their inner knowledge.

4. The resolution of the figures is low. And the sizes and positions of them are also inapt.

### Questions
Can you test the time consumption of test-time RAG, compared with standard RAG methods, on these general problems?

### Soundness
2

### Presentation
1

### Contribution
1
