# BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval

- Decision: Accept
- Scores: 6, 8, 6, 6, 10

## Abstract
Existing retrieval benchmarks primarily consist of information-seeking queries (e.g., aggregated questions from search engines) where keyword or semantic-based retrieval is usually sufficient.
However, many complex real-world queries require in-depth reasoning to identify relevant documents that go beyond surface form matching.
For example, finding documentation for a coding question requires understanding the logic and syntax of the functions involved.
To better benchmark retrieval on such challenging queries, we introduce \ours, the first text retrieval benchmark that requires \textit{intensive reasoning} to retrieve relevant documents. Our dataset consists of \totalexamples real-world queries spanning diverse domains, such as economics, psychology, mathematics, and coding.
These queries are drawn from naturally occurring and carefully curated human data.
Extensive evaluation reveals that even state-of-the-art retrieval models perform poorly on \ours. 
The leading model on the MTEB leaderboard~\citep{muennighoff2022mteb}, which achieves a score of 59.0 nDCG@10,\footnote{Retrieved from the \href{https://hf.co/spaces/mteb/leaderboard?task=retrieval}{MTEB leaderboard} on 2024-05-28.} produces a score of nDCG@10 of 18.3 on \ours. We show that incorporating explicit reasoning about the query improves retrieval performance by up to 12.2 points. 
Moreover, incorporating retrieved documents from the top-performing retriever boosts question-answering performance by over 6.6 points.
We believe that \ours paves the way for future research on retrieval systems in more realistic and challenging settings.\footnote{Our code and data are available at \url{https://brightbenchmark.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose Bright, an information retrieval benchmark that focuses on questions that require 'reasoning-intensive' retrieval to provide relevant content. Whereas most existing benchmarks focus on factoid questions where there is significant semantic overlap between the query and the retrieved content (or some 'translation', but not 'reasoning'). Specifically, Bright is actually 12 datasets including 7 datasets from StackExchange covering {Biology, Earth Science, Economics, Psychology, Robotics, Stack Overflow, Sustainable Living}, 2 coding data settings from {LeetCode (python), Pony}, and 3 math reasoning datasets {TheoremQA-Question Retrieval, TheoremQA-Theorem Retrieval, Art of Problem Solving}. Details are provided regarding the procedures to collect each dataset. In short, for StackExchange, human annotators browse recent posts and select a post with at least 5 upvotes and contain at least one URL link -- which are human validated to produce questions, answers, and relevant documents. Negative documents are collecting via identifying semantically similar but irrelevant documents (i.e., negatives) via a Google search powered method. These are human validated for unanimity. Pony coding adapts a code generation dataset to retrieving pages from manuals to cover syntax and LeetCode via a fairly straightforward crawling procedure. Math reasoning adapts TheoremQA to retrieve math queries that either use the same theorem as the query's solution (question retrieval), theorems from ProofWiki (theorem retrieval), or Math Olympiad problems (Art of Problem Solving) matching other problems that use the same theorems. Experiments are conducted based on 13 different retrieval engines including sparse retrieval, open-source dense retrieval, and proprietary models. The important findings is that nDCG@10 has variance amongst different systems (i.e., improvements can be made) while being relatively low as compared to other benchmarks (i.e., it is difficult). Additional experiments show that querying with LLM reasoning (i.e., chain-of-thought) improves performance (i.e., reasoning is needed for retrieval, irrespective of underlying retrieval method), retrieval improves RAG-based results (i.e., retrieval is an important problem). They also demonstrate that reranking with increasingly powerful LLMs improves retrieval performance, Bright appears robust with respect to data leakage in pre-training (i.e., pre-training doesn't cover reasoning requirements as much as most tasks), and that long-content retrieval (e.g., legal, medical) is more difficult.

### Strengths
A strong benchmark paper should satisfy some of the following dimensions (along with some commentary): 
- the task is useful
Difficult document retrieval is a long- and widely-studied problem. It is both more important in the era of LLMs due to increased reasoning capabilities, but potentially less important as more information is encoded in the parameters (modulo time-sensitive, etc.). Thus, additional motivation could help justify the significance of the work. 

- the dataset is large enough and non-trivial to construct
This is also mixed; the dataset isn't particularly large and is ostensibly of varying quality between Stack Exchange, Coding, and Math. That being said, it is clearly more complex than many existing benchmarks for at least a subset of the questions. For some questions, the quality is seemingly higher (i.e., more human validation) than existing datasets.

- there are sufficient details regarding the construction of the benchmark
Including the appendices, there are a lot of details -- to the point where I am confident I could replicate most of the results. However, the amount and clarity of the procedure for different data sets (Stack Exchange, Coding, and Math) isn't as detailed for all cases. Also, it isn't clear in general what the human annotation guidelines were, how annotators were recruited, and how they were compensated (unless it is just the authors and volunteers). However, the details are solid overall.

- the tools provided reduce friction for new people to work on this
Code is provided and was used to run several experiments. I didn't dig through the code and thus do not know how easily it is to conduct experiments. However, I am reasonable confident it is sufficient.

- the baseline models tested on the benchmark are non-trivial
The authors conduct several experiments over several different retrieval engines including state-of-the-art systems on related datasets.

- the benchmark answers new questions or enables new solutions
The authors did conduct experiments beyond just IR performance and were able to address some of these questions using this dataset. The discussion in these sections could be strengthened, but it is solid in this regard overall.

Evaluating the paper with respect to the stated dimensions,
Originality: There are multiple 'hard QA/IR' datasets, but the emphasis here is on IR for reasoning-heavy scenarios -- which is timely and a useful contribution. Many have likely considered such datasets, but the execution here is better than a first attempt.
Quality: Overall, the work is well-motivated, well-executed, and sufficiently rigorous. My primary concern in this regard is variance in quality between different benchmark types (QA, Math, Coding) and that this is a relatively small dataset.
Clarity: Overall, the paper is easy to understand and has sufficient details, especially when considering the appendices. The figures are helpful. My two suggestions in this regard are a Table comparing Bright to the most related datasets and more discussion regarding the empirical results including specific references to cells in the tables (i.e., I didn't always know which cells I was looking at when validating quantification claims).
Significance: I am fairly certain that at least part of this benchmark will be used, but not sure if all parts will be used. Additionally, it would have more potential impact if it was a larger dataset (or there was clear evidence that it covers some expected 'production' distribution)

### Weaknesses
On the other hand, below are some of my concerns regarding this paper (some previously mentioned):
- I would like to see a statistics-level comparison between Bright and competing datasets in a table ("Benchmarking retrieval" (line 104) and "Benchmarking reasoning" (line131) in Related Work section)
- I would like clarification regarding the annotation guidelines, recruiting experts, compensation for lines 248-253.
- To get the details for coding and math, one pretty much has to read the appendices and from what I can tell, the significance and quality of the Stack Exchange questions is the strongest aspects of the paper.
- The appendices are more detailed (to the point where they actually seem different from the text). However, still no details regarding annotation guidelines, recruiting experts, and compensation (unless the authors did all of this)
- The dataset seems relatively small; if I am incorrect, I would recommend a table contrasting this with other datasets (along with other aspects).
- For reasoning steps, a bit more from the appendix (e.g., StackExchange vs. coding vs. math stratification) would be helpful in the main text with discussion.
- In general, it isn't clear that ordering matters for RAG settings, so NDCG-based results may not be that useful as in IR settings. I also would recommend rank-biased precision and recall (i.e., evaluations similar to 'needle-in-a-haystack' settings.
- As implied in other areas, there are a lot of results, so more specific interpretation would be helpful (but I am aware of the page limit).
- While the authors claim that there are not licensing issues, I wasn't able to verify this. Obviously, if there are licensing issues (for academic research within commercial organizations?).

### Questions
The only two clarification issues I had are:
- Details regarding human annotator guidelines, annotator recruitment, and compensation. This would help in better understanding the reliability of the human annotations.
- More specifics regarding licensing (i.e., a table with licensing terms for each dataset being used).

### Soundness
4

### Presentation
3

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
The paper presents **BRIGHT**, a benchmark for evaluating retrievers on reasoning intensive tasks. **BRIGHT** contains 1,398 realistic tasks over 12 domains, including Biology, Psychology, Coding, and Math. By experimenting with 13 retrievers, the paper shows that **BRIGHT** is challenging for current systems - the best model reaches an nDCG@10 score of 22.1. Moreover, enhancing queries with reasoning traces improves retrieval performance, retrieval-augmentation with current retrievers improves QA accuracy, re-ranking with LLMs can increase retrieval accuracy, and pre-training on documents in **BRIGHT** does not further increase performance.

### Strengths
- The data collection pipeline is thorough and includes verification by two domain-expert PhD students. 
- Lots has been done to ensure diversity by focusing on several different StackExchange domains, two coding tasks, and an additional effort for including theorem-based questions.
- The experiments are extensive and cover 13 different retrievers, in addition to two re-rankers.
- The paper is well-written and easy to follow.

### Weaknesses
 - It could have been helpful to add a quantitative analysis in the analysis section. For example, an analysis that examines when models err could be useful for future research (see the Questions section for further discussion and some suggestions).

- There are a few details in the appendix that are not referenced from the main paper (e.g., the Limitations section), and I found the appendix a bit hard to follow. Consider verifying all main sections are referenced, or alternatively adding a small Table of Contents in the beginning of the Appendix.

### Questions
### Questions 
Perhaps I missed something, but do you think any of the following analysis will be helpful for future works - 
- A quantitative analysis that shows the rank of the gold document for the best retriever (QWEN).
- A qualitative analysis that examines why strong LLMs (e.g., GPT-4 in Table 3) fail to correctly rank relevant documents. The gold document can be added as an oracle to when it was not retrieved. If not, do you think that a different analysis regarding model errors can be helpful? 
- The ratio of evaluator failures described in lines 454-458 (although this is minor).

Again, maybe I am missing something, but did you also experiment with the StackExchange answers as positive passages?

### Suggestions 
- The abstract mentions that “The leading model on the MTEB leaderboard which achieves a score of 59.0 nDCG@10,1 produces a score of nDCG@10 of 18.0 on **BRIGHT**”. Consider adding which model this is, because the MTEB leaderboard is changing constantly.

- The example for “Level 1: Keyword-based Retrieval” only states that the part of highway 401 is *one of the widest*, while the question asks for the widest highway. I understand this is from the NQ dataset, but a positive passage that directly answers the query might be simpler for the reader.

- The appendix is sometimes referenced as Appendix (e.g., Appendix C) and sometimes as § (e.g., §B.3). Consider using one for consistency (this is of course very minor).

- The subsets of **BRIGHT** are relatively small, with the smallest including only 78 examples. Adding error bars or variance for the results, either in the paper or in a leaderboard, could help future researchers focusing on a specific subset.

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
The paper presents BRIGHT, a challenging retrieval benchmark designed to require deep, beyond-surface-form matching between queries and documents. Human annotators constructed a dataset of 1,398 instances spanning diverse domains. Current retrieval models perform poorly on this benchmark, highlighting its difficulty. The authors also propose several techniques aimed at improving retrieval performance.

### Strengths
- The benchmark is challenging and has the potential to drive future research toward developing retrievers that handle difficult queries more effectively.
- The dataset is human-collected, ensuring authenticity rather than relying on artificially generated data. 
- I liked the comprehensive appendix, which provided valuable insights into the annotation process and the dataset's structure.

### Weaknesses
 - Detailed analysis of results is lacking and some (RAG, reranking) are not surprising.
- In line 413, how can LLM-reasoning queries enhance the reasoning capabilities of retrievers? If the primary effect is an increase in lexical similarity (BM25's strong performance), should models be specifically trained to leverage this feature to perform well on BRIGHT? Additionally, the results for Coding and Theorem-based datasets (Table 38) appear inconsistent.
- In line 428, regarding retrieval-augmented generation, the QA performance seems to be already quite high when paired with current retrievers that are reported to perform poorly.

### Questions
- Have you tried finetuning retrievers on this benchmark?
- In figure 1, level 2 queries (NQ, MSMARCO) are outdated. It would be better to compare BRIGHT’s “intensive” reasoning to recent retrieval benchmarks, such as RAR-b or subset of BeIR and MTEB that goes beyond semantic matching.

### Soundness
3

### Presentation
4

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
This paper argues that for retrieval tasks, many real-world queries require in-depth reasoning to identify relevant documents, which goes beyond traditional keyword or semantic-based matching focused by existing benchmarks.
To benchmark retrievers on such reasoning-intensive queries, this paper created a new dataset, Bright, which consists of 1398 queries spanning diverse domains. 
The benchmarking on this new dataset demonstrated that state-of-the-art retrieval models perform poorly on this dataset.

### Strengths
1. This paper focuses on creating a new dataset to benchmark reasoning-intensive queries, which is a very important type of queries for RAG systems and search engines, and there does not exist such a benchmarking dataset so far.

2. The dataset covers a variety of domains, including economics, psychology, mathematics and coding, which is quite comprehensive.

3. The retrieval process in the experiments incorporated explicit reasoning about the query and achieved an up to 12.2 points improvement, which demonstrated that reasoning is indeed a bottleneck for such types of queries, which aligns very well with the motivation of the datasets.

### Weaknesses
1. There is no unified definition of either relevance or required reasoning across data from different domains in this dataset. Though the author wrote different "relevance" in different subsections, they are actually not definition of relevance but how the corpus is created.
It is acceptable as a dataset, however, there is a lack of deep scientific understanding about what exact (reasoning) ability is required for a retriever model to success on this dataset. Instead what we can learn from this dataset is that the retriever model may need to overfit some ad-hoc collection process.

2. Due to a lack of unified relevance definition, the dataset is more like a collection of different benchmarking applications where different relevant (can be either closely or loosely) information to the query can be helpful. Therefore, rather than using it as a retrieval benchmark to evaluate retrievers, it is more suitable to use it to evaluate the application. For these applications, the retrieval results are just intermediate results and can be difficult to judge whether they can actually help the final results.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
## Summary
The paper presents a challenging and novel retrieval benchmark which requires reasoning to answer queries

## Contributions
1. The first benchmark to focus solely on reasoning intensive retrieval. The benchmark is constructed from diverse domains and carefully curated to remove possible noise
2. Thorough experiments are done with respect to a variety of retrieval models -- sparse, open source small models, open source large models and even proprietary models
3. The authors list the data creation and curation process in detail. This would further help in creating similar such benchmarks

### Strengths
1. A high quality, relevant and challenging benchmark for information retrieval tasks
2. Comprehensive evaluation on a wide variety of models
3. Love the section on how chain of thought reasoning helps improve the models -- especially BM25!
4. Downstream task evaluation is also very helpful -- confirms the documents are relevant

### Weaknesses
1. (Lines 248-253): Why not use all three annotators independently? It seems you biased the expert annotators with annotations performed by a non-expert
2. Section 5.2 claims that continued pre-training does not help. However, you mention in Appendix A.3 that the average number went to 21.0! Why was 20.4 picked as the final number in Table 5. It is possible that continued pre-training in this fashion (only showing new documents from Stack Exchange) is making the model lose its generalization abilities. There are two options to do this ablation study -- train a model with a replay buffer, which samples data from the original training data along with stack exchange. Train a model where all data is used together (original training data and stack exchange)
3. How does an LLM (such as GPT-4o) work on the downstream task. That is give it a question, and evaluate its performance on answer quality (without giving any document)

### Questions
1. (Lines 248-253): Why not use all three annotators independently? It seems you biased the expert annotators with annotations performed by a non-expert
2. Section 5.2 claims that continued pre-training does not help. However, you mention in Appendix A.3 that the average number went to 21.0! Why was 20.4 picked as the final number in Table 5. It is possible that continued pre-training in this fashion (only showing new documents from Stack Exchange) is making the model lose its generalization abilities. There are two options to do this ablation study -- train a model with a replay buffer, which samples data from the original training data along with stack exchange. Train a model where all data is used together (original training data and stack exchange)
3. How does an LLM (such as GPT-4o) work on the downstream task. That is give it a question, and evaluate its performance on answer quality (without giving any document)

### Soundness
4

### Presentation
4

### Contribution
4
