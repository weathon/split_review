# MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
While large language models (LLMs) have made strides in understanding tabular data, current tabular evaluation benchmarks, such as WikiTableQuestions and WikiSQL, are focus on single-table scenarios, which cannot necessarily reflect the complexity of real-world applications. To bridge this gap, we present a \textbf{M}ulti-table and 
Multi-hop Question Answering (MMQA) dataset to assess LLMs' understanding and reasoning capabilities in handling multi-table tasks. The MMQA dataset demands that models perform multiple inferences by drawing evidence from various tables, which are designed to be connected with each other and require models to identify and utilize relationships such as foreign and primary keys. Then, we introduce a comprehensive evaluation framework that tailors to assess LLMs' capabilities in several aspects including Multi-Table Retrieval, Text-to-SQL Generation, Multi-Table QA, Primary Key Selection, and Foreign Key Selection. 
Finally, we propose a novel multi-table retrieval method that achieves state-of-the-art (SOTA) performance on the MMQA dataset compared to several strong baselines. 
Our experiment results reveal that, compared with human performance, both open-source and commercial LLMs leave significant performance room for improvements in multi-table understanding and reasoning tasks. We believe that the MMQA benchmark will enhance and facilitate LLMs' multi-table capabilities in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new benchmark for multi-table multi-hop reasoning using question answering. This benchmark evaluates models on 5 aspects: multi-table retrieval, text-to-sql generation, multi-table QA, Foreign Key selection, and Primary Key Selection. They also provide 2 splits: one for questions where reasoning is needed across 2 tables, and another one across 3 tables (and hence more challenging). This benchmark is novel because prior works focus on single-table QA, while the proposed one focuses on multi-table, which is also a more realistic setup since it is common to perform unions and joins across tables in real-world scenarios. They conduct evaluations on multiple proprietary LLMs and open-weights LLMs and compare them with human and baselines and multiple retrieval methods. The paper aims to answer the following questions:

How well are LLMs at solving multi-table QA tasks compared to humans? -> there is still a large gap to close
How well can LLMs solve structured reasoning tasks such as Primary/Foreign Key Selection? -> only o1 achieves an accuracy > 40, which shows LLMs struggle on this subtask, which is key for proper multi-table reasoning.
How does the performance of LLMs decrease when the table sizes increases? -> when the table is too long, performance rapidly decreases indicating there is a (length, #rows) threshold where LLMs cannot understand tables well.

### Strengths
* Very complete benchmark for evaluating table reasoning in LLMs.
* The benchmark includes different subsets for different difficulty levels, it also includes multiple subtasks, which can be useful to evaluate intermediate steps needed to solve multi-table QA.
* Analysis of multiple open-weights and close-weights LLMs.
* Includes short and longs tables, which can be useful for analysis of LLMs’ long-context understanding.
* More generally, this benchmark can be very useful for future research on table reasoning.

### Weaknesses
 * The paper uses a partial match evaluation that depends on GPT4 (which can be fine), but they don’t provide and evaluation of the quality of this metric.

### Questions
* How good is the partial match evaluation? Does this metric correlate to a human partial match evaluation?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the task of information retrieval and question answering from multiple tables, focusing on questions that require information from multiple tables and reasoning. For this task, the paper introduces the _Multi-table and Multi-hop Question Answering (MMQA) dataset_, along with several subtasks that multi-table QA systems might need to solve: Table retrieval, Table QA, Text-to-SQL, Primary key selection, and Foreign key selection.

This dataset is constructed by template-based synthesis of SQL queries from the tables in the Spider dataset, and converting them into natural language questions using GPT-4-Turbo, in addition to quality checks conducted by experts.

The paper also introduces _MTR_, a new method for the multi-table retrieval subtask. MTR uses question decomposition and both question-table relevance (using single-table retrievers from prior work) and table-table relevance, to tackle this subtask.

Finally, the paper benchmarks several open LLMs (TableLLaMA-7B and Mistral-7B) and proprietary LLMs (GPT-3.5, GPT-4, Gemini-pro, and O1) on the MMQA dataset and conducts ablation studies to understand the effects of table length on the performance of various systems. These experiments show that there is a significant gap between the performance of LLMs and human experts on this dataset and task.

### Strengths
This paper identifies a task where large language models (LLMs) are significantly behind humans, and open models lag behind closed commercial models (like O1). This is quite valuable for the research community to continue developing better LLMs.

MMQA has a comprehensive set of question categories, including "list/count all answers," which are often overlooked in TableQA datasets.

The experiments are thorough, and include a good mixture of open and closed LLMs. I imagine future research will be able to easily compare their systems against these baselines.

### Weaknesses
## 1. The MMQA Dataset is Synthetic
To construct MMQA, this paper generates SQL using templates and then converts them to natural language using an LLM. There are two potential downsides to this approach. One is that synthetic evaluation and test sets pose the risk of overestimating the performance of models [4]. This may occur due to the lower diversity of natural language questions or the fact that, since they are generated from SQL, they may be too close to SQL or otherwise "unnatural" compared to questions that users of such systems may ask. 

For example, the question in Figure 1, "What are the distinct creation years of the departments managed by a secretary born in state Alabama?" uses the terminology from the tables ("creation," "department," "state") and the SQL keyword "distinct." In a more realistic setting, a user might instead ask, "When were the departments managed by an Alabamian secretary established?". Given that the user is most likely not aware of column names in the database. Tackling this setting involves additional challenges like mapping the terms users use into column names and dealing with ambiguities.


## 2. Evaluation Metrics Need More Thought
Using ROUGE and BLEU for SQL is not really appropriate. To compare SQL queries directly, exact match is often used. Execution accuracy is another commonly used evaluation metric in the literature. It involves executing the resulting SQL against the database and comparing its answer against the answer from the gold SQL. Please note that the original Spider dataset paper uses these two metrics. 
Even more suitable metrics are discussed in [3] and [2]. For example, [2] proposes a generalization of execution accuracy, which could be useful for evaluating "list" and "count" questions in MMQA.

Using Exact Match and Partial Match for QA underestimates the performance of models. This is especially noticeable when evaluating LLMs (as this paper does). Also, I wonder how these metrics handle "list" answers, given that they are quite sensitive to order. Or if a system is off by one when answering a "count" question because it missed one of N rows, shouldn't it get a partial score? See [5] for an example of how using an LLM judge to compare a model's predictions against the gold answer can help alleviate this problem.

In addition, it might make sense to add a unified text-to-SQL and TableQA subtask. This means that a system proposed in future work can answer the question in any way it chooses, either by generating and executing an SQL query or by directly reading the tables, and the final answer is evaluated against the gold answer. This would have the additional benefit that text-to-SQL methods and TableQA methods can use this dataset and compare their work across the two lines of research.

## Other minor issues
- In Algorithm 1, it should also be specified that a single-table retriever is used, in the same way it mentions that GPT-4-Turbo is used. Additionally, “outputs” are not sub-questions but tables.

### Questions
1. In Table 1, what is the unit of "question length"? Is it measured in characters?

1. Line 199: How do you measure the number of reasoning steps?

1. What is the input for the Table QA, Text-to-SQL, "Primary Keys Selection," and "Foreign Key Selection" tasks? Are the gold tables used as input?

1. In Table 4, what is the difference between, for example, "TableLlama-7b" and "MTR (TableLlama-7b)"? Is it just the question decomposition part done by GPT-4-Turbo, or is their training data also different?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces MMQA, a novel multi-table multi-hop question-answering dataset. The authors randomly sampled from the Spider dataset and prompted LLMs to generate natural language questions. The synthesized dataset then went through human experts' manual verification. Compared to existing table question-answering datasets, MMQA features a more diverse task collection, longer reasoning chains, and evaluations on different granularities. Extensive experiments run on MMQA indicate that there is still a large performance gap between the current SOTA LLMs and humans. The authors also propose a strong baseline, MTR, for the multi-table retrieval task. Additional insights and analysis on the evaluation results are also provided.

### Strengths
## **1. The task is novel and important**

The task of multi-table question answering is novel and important because it is very common in real product environments to consider multiple tables together, yet previous table question answering datasets have mainly focused on single-table scenarios. MMQA is able to close this gap. From this perspective, I believe the paper is well motivated and the problem is realistic and important. 

## **2. The quality of the dataset is high**

The dataset contains 3,312 expert-verified tables with 7.61 average reasoning steps and a diversity of task types. The experiment results show a large gap where current SOTA LLMs such as OpenAI o1-preview only achieve around 50% success on MMQA evaluation metrics while humans achieved 80-90%. 

## **3. A strong baseline is proposed**

The authors also proposed a strong baseline, MTR, that significantly (around 10-15% better on retrieval metrics) outperformed existing LLMs on the multi-table retrieving task. This model can serve as a good reference for future models on MMQA.

## **4. The paper is in general well written**
The paper is in general clear and easy to follow. The logic flow is straightforward and clearly presented. The authors also submitted supplementary dataset samples that give a sense of what the dataset will look like, which is helpful.

### Weaknesses
## **1. Diversity and naturalness of queries in the dataset**

The dataset is constructed by sampling from 45 SQL templates in the Spider dataset and converting them into natural language using GPT-4-turbo. This approach inherently limits the diversity of query types. Additionally, due to the synthetic nature of the dataset, its distribution does not fully align with that of real-world user queries. The reliance on a limited set of SQL templates means that the dataset may not cover the full spectrum of complex multi-table reasoning patterns that could arise in real-world scenarios. For example, the dataset might underrepresent queries that require complex aggregations, nested subqueries, or specific types of joins beyond those present in the original Spider templates. Furthermore, the use of GPT-4-turbo for natural language generation, while efficient, may introduce biases or stylistic consistencies that are not representative of the variability found in human-generated questions. This could lead to models overfitting to the specific style of the generated questions rather than learning generalizable multi-table reasoning skills.

## **2. Baseline models tested are relatively weak**

The current baselines are mostly general-purpose LLMs except TableLlama, which is a smaller 7B model. I would recommend adding more recent LLM-based table question answering agentic systems as baselines, such as the ones on top of the Spider leaderboard: https://yale-lily.github.io/spider. The lack of comparison against state-of-the-art table question answering systems makes it difficult to assess the true difficulty and novelty of the MMQA dataset. Specifically, evaluating against systems that incorporate techniques like iterative query refinement, dynamic schema linking, and more sophisticated reasoning modules would provide a more comprehensive understanding of the challenges posed by the dataset. The current baselines, while demonstrating a performance gap, may not fully capture the potential of existing table QA technologies, thus potentially underestimating the difficulty of the task.

### Questions
## **1. What kinds of annotation disagreement occurred?**

In 3.1 the authors described the annotation quality verification process. I was wondering what kinds of disagreement patterns were observed. Were the annotators disagreeing with each other because they made mistakes themselves all the time? Was there any case that was due to query ambiguity or GPT-4-turbo's incorrect NL translation? How did you manage those situations, if any?

## **2. Did you notice any bias, information loss, or noises introduced by GPT-4-turbo as the query translator?**

One concern about GPT-4-turbo translating the template-based queries is that GPT-4-turbo might introduce bias (e.g., some wording patterns get overrepresented), information loss (e.g., the semantics in the SQL might not be fully faithfully translated into NL), or noises (e.g., hallucinated or ignored columns/entities/tables/etc). Did you observe any of such risks and how did you handle them? Would it make sense to also include the caveats and potential issues with the approach in e.g. appendix?

### Soundness
4

### Presentation
3

### Contribution
3
