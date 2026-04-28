# Spider 2.0: Can Language Models Resolve Real-World Enterprise Text-to-SQL Workflows?

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Real-world enterprise text-to-SQL workflows often involve complex cloud or local data across various database systems, multiple SQL queries in various dialects, and diverse operations from data transformation to analytics. 
We introduce \ours, an evaluation framework comprising $632$ real-world text-to-SQL workflow problems derived from enterprise-level database use cases. 
The databases in \ours are sourced from real data applications, often containing over 1,000 columns and stored in local or cloud database systems such as BigQuery and Snowflake.
We show that solving problems in \ours frequently requires understanding and searching through database metadata, dialect documentation, and even project-level codebases. 
This challenge calls for models to interact with complex SQL workflow environments, process extremely long contexts, perform intricate reasoning, and generate multiple SQL queries with diverse operations, often exceeding $100$ lines, which goes far beyond traditional text-to-SQL challenges.
Our evaluations indicate that based on o1-preview, our code agent framework successfully solves only 17.0\% of the tasks, compared with 91.2\% on Spider 1.0 and 73.0\% on \bird. 
Our results on \ours show that while language models have demonstrated remarkable performance in code generation --- especially in prior text-to-SQL benchmarks --- they require significant improvement in order to achieve adequate performance for real-world enterprise usage.
Progress on \ours represents crucial steps towards developing intelligent, autonomous, code agents for real-world enterprise settings.
Our code, baseline models, and data are available at \url{https://spider2-sql.io}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Spider 2.0, a new NL2SQL benchmark designed to address the challenges of real-world enterprise text-to-SQL workflows. Unlike previous benchmarks, Spider 2.0 focuses on 595 complex workflow problems derived from real-world enterprise use cases involving databases often exceeding 1,000 columns and stored across diverse systems like BigQuery and Snowflake. These problems require models to handle intricate SQL workflows, understand long contexts, explore database metadata, manage dialect variations, and interact with project-level codebases. The tasks frequently involve generating multi-step, nested SQL queries exceeding 100 lines, encompassing diverse operations from data transformation to analytics. Spider 2.0 thus pushes beyond traditional text-to-SQL challenges, demanding higher levels of reasoning and adaptability from language models.

The evaluations reveal significant gaps in existing language model capabilities, with the introduced code agent framework solving only 15.1% of Spider 2.0 tasks, compared to 91.2% on Spider 1.0 and 73.0% on BIRD. This highlights the difficulty of handling real-world enterprise scenarios, such as schema linking in large databases, navigating diverse SQL dialects, planning complex query sequences, and effectively leveraging external documentation. The insights from Spider 2.0 underscore the need for substantial advancements in autonomous code agents to meet enterprise requirements.

### Strengths
S1) Originality: Spide 12.0 significantly extends traditional text-to-SQL benchmarks by focusing on real-world enterprise scenarios.  It incorporates a broader and more complex range of challenges, such as handling extremely large databases, diverse SQL dialects, and intricate workflows. This originality lies in redefining the scope of text-to-SQL tasks to better align with practical, enterprise-level applications.

S2) Quality: the benchmark created and curated 595 real-world text-to-SQL workflow problems derived from enterprise use cases, ensuring relevance and rigor. The inclusion of diverse database systems like BigQuery and Snowflake, along with tasks involving database metadata, codebases, and nested SQL queries, reflects meticulous data collection and a comprehensive representation of real-world complexity.

S3) Clarity: the paper is very well organized and carefully written. The content is very rich and deep. By providing detailed analysis and explicit examples of schema linking, dialect handling, and multi-step query generation, it offers clear insights into the difficulties faced by language models in enterprise scenarios.

S4) Reproducibility: the paper provides source code.

### Weaknesses
I don't find any major weakness

### Questions
No questions

### Soundness
4

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
5

### Summary
The paper introduces a new benchmark, Spider 2.0, which consists of 595 real-world text-to-SQL workflow tasks over ~1000 columns. The  text-to-SQL tasks are significant more challenging compared to the commonly used Spider and Bird benchmarks. The authors evaluate multiple LLMs using Spider 2.0 and present a set of interesting findings.

### Strengths
S1. The new benchmark dataset is publicly available and critical for the community and enterprises that develop LLM-based text-to-SQL solutions.

S2. The dataset creation is solid and clearly presented in the paper. The SQL complexity including functions and dialects is closer to the real-life enterprise setting.

S3. The analysis provides some interesting findings, especially the error analysis of SQL generation.

### Weaknesses
W1. The agent aspect of the benchmark should be emphasized more as it largely separates Spider 2 from the other benchmarks. It is reasonable to use execution results as the metric for evaluation. However, the other important aspect is the ideal multi-turn process for each task. For example, what is the typical number of turns and the sequence to complete the task. The current evaluation lacks a clear definition of an ideal interaction sequence, making it difficult to assess the efficiency and reasoning capabilities of different agents in a standardized manner. This includes not only the number of turns but also the types of actions taken at each step, and the overall strategy employed by the agent.

W2. The difficult level in Sec. 3.1 is acceptable but not comprehensive. The SQL complexity reflects one aspect of the task difficulty. The other aspects include the data complexity (e.g., whether the task requires access to nested schema, any question/data ambiguity, etc.). If these are not as straightforward as the number of tokens, associating some tags to each task would help one to understand the specific challenges associated with the tasks. For instance, tasks involving complex joins across multiple tables, or those requiring reasoning over nested column structures, should be explicitly identified. Furthermore, the presence of ambiguous natural language queries, or the need for external knowledge to resolve the query, should also be considered as factors that contribute to the overall task difficulty. A more granular classification of difficulty, beyond just SQL length, is needed to fully characterize the benchmark.

W3. It seems that SQL is the only "code" allowed to execute the task. However, certain tasks such as data transformation might be easier to be executed through script languages (e.g., Python). IMO, a more realistic setting should allow LLMs to decide the best way to execute a (sub-)task. This will enable the LLMs, such as GPT-4o, to better leverage their strength in code generation. The current restriction to SQL might limit the potential of the benchmark to evaluate the full capabilities of advanced LLMs in complex data manipulation scenarios. For example, tasks that involve data cleaning, aggregation, or pivoting could be more efficiently handled using Python's Pandas library, and the benchmark should allow for such flexibility.

### Questions
Q1. Is CodeS-15B fine-tuned on Spider 2, or the fine-tuned model from the repo was directly used for evaluations?

Q2. Among dialect function usage errors, what is the ratio between simple syntax errors (i.e., LLMs not knowing the specific syntax) and completely incorrect chosen function?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Spider 2.0, a benchmark aimed at assessing the capabilities of large language models (LLMs) in handling complex text-to-SQL tasks within enterprise environments. Unlike previous datasets, Spider 2.0 involves real-world databases containing thousands of columns and diverse SQL dialects, with tasks that require interaction with database metadata, project-level codebases, and external documentation. The benchmark emphasizes challenges such as processing extensive schemas, using advanced SQL functions, and generating multi-step SQL queries.

Key findings highlight that current LLMs, even state-of-the-art models like GPT-4, struggle with Spider 2.0, achieving a success rate of only 15.1%. This reveals significant gaps in their ability to handle industrial-grade SQL workflows, which involve complex data transformations and analytical tasks. Spider 2.0 aims to push the development of more capable models for practical enterprise applications by providing a realistic and challenging benchmark.

### Strengths
S1. It is important to have Spider 2.0 for real enterprise Text-to-SQL. Spider 1.0 and BIRD focuses on multi-table tasks, while WikiSQL and GeoQuery only focus on single table tasks. These datasets are popular, but they still represent a very small part of the whole data analytics/science workflow. The emerge of Spider 2.0 tries to fill this gap.

S2. The collection of Spider 2.0 complies the data manipulation workflow in real enterprise scenarios. Detailed types of queries and error analysis are shown in detail, which indicates the future direction of improvement.

S3. Spider 2.0 is a valuable dataset for the future agent of data analytics, which will be an important future trend of the data science domain. This paper also provides Spider-Agent, which can be a new baseline of data analytics agent.

### Weaknesses
W1. There should be an opportunity to have an end-to-end benchmark for enterprise data analytics/ data science workflow with both SQL query and Python. Also, it would be better to also consider queries on Hadoop/Cassandra, which are also widely-used storages.

W2. In this paper, schema linking and table mapping results are shown. It would be better to open-source these two related datasets to extend the gap of LLM-based Text-to-SQL schema linking.

W3. It would be better to show the number of tokens of Codebase+DB Info+Documents, which should be an important parameter for picking up proper LLMs to construct agents.

### Questions
1. W3

2. May I ask where can I find the proper json file for Spider 2.0 and Spider 2.0 Light in your repo?

3. Please figure out the difference between your work and MLE-Bench made by OpenAI

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents Spider 2.0, a new benchmark for Text-to-SQL systems that introduces more complex and realistic SQL tasks compared to benchmarks like Spider 1.0 and BIRD. Spider 2.0 tasks require models to leverage project-level information, such as codebases and documentation, for generating accurate SQL queries. It also includes more SQL dialects such as DuckDB, Snowflake, and BigQuery, and utilizes advanced SQL functions such as ST_DISTANCE and CORR. 

The benchmark demonstrates its difficulty by showing that even state-of-the-art language models achieve a maximum accuracy of only 15.12%. This result highlights significant gaps in current Text-to-SQL approaches that perform well on enterprise-level SQL generation tasks. Spider 2.0 can potentially advance Text-to-SQL systems, bringing them closer to being practical for enterprise applications.

### Strengths
1. Spider 2.0 is the first Text-to-SQL benchmark to incorporate complex contexts — such as data pipeline code and SQL dialect documentation — into the SQL generation process, reflecting an essential aspect of real-world SQL writing in a data engineer’s workflow. This marks a significant advancement over BIRD, which only includes simple evidence (1-2 sentences) as external knowledge.
2. SQL queries in Spider 2.0 are derived from actual projects and tutorials, enhancing the benchmark's realism and quality. Each database instance is selected to ensure sufficient complexity, with a minimum of 200 columns per database.
3. The evaluation in this paper is highly insightful, offering readers a clear perspective on the current limitations of LLM-based text-to-SQL approaches.

### Weaknesses
The goal of this paper is to simulate real-world enterprise text-to-SQL workflows. While the authors have made substantial progress toward this aim, several important aspects of enterprise workflow characteristics remain unaddressed.

1. Context Complexity: The paper has included codebase and SQL docs as the context. However, in the enterprise setting, business context is also crucial. For example, different companies have different ways to compute daily active users or user retention rates. There can be a page-long documentation to explain how a metric should be calculated or even a page-long formula that defines a metric directly. This kind of context is missing from the benchmark. 
2. Schema Complexity: The paper says it selects databases where the number of columns is larger than 200. However, that does not guarantee that the schema is complex enough. For example, these 200 columns can be stored in one table. It is not clear how complicated the table relationship is. How many joins are involved in the SQL?
3. Question Complexity: The questions are generated by the authors based on the SQLs crawled from forums or tutorials, which might not reflect the nature of real-world BI questions, which often ask for trends or patterns. Including real data engineers to audit the benchmark or participate in the benchmark generation process can make it more convincing.

Despite these limitations, I recognize the authors' efforts in taking an important first step toward an enterprise setting.

### Questions
1. How many tables per database in Spider 2.0? The paper only reports the number of columns per database. 
2. The paper's abstract states that it can "generate multiple SQL queries with diverse operations, often exceeding 100 lines." However, the queries average 144 tokens, which seems unlikely to translate into over 100 lines. Am I misunderstanding something here?

### Soundness
3

### Presentation
4

### Contribution
4
