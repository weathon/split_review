# Structure-Guided Large Language Models for Text-to-SQL Generation

- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 10, 8, 3

## Abstract
Generating accurate Structured Querying Language (SQL) is a long-standing problem, especially in matching users' semantic queries with structured databases and then generating structured SQL. Existing models typically input queries and database schemas into the LLM and rely on the LLM to perform semantic-structure matching and generate structured SQL. However, such solutions overlook the structural information within user queries and databases, which can be utilized to enhance the generation of structured SQL. This oversight can lead to inaccurate or unexecutable SQL generation. To fully exploit the structure, we propose a structure-to-SQL framework, which leverages the inherent structure information to improve the SQL generation of LLMs. Specifically, we introduce our \textbf{\underline{S}tructure \underline{Gu}ided SQL~(SGU-SQL)} generation model. SGU-SQL first links user queries and databases in a structure-enhanced manner. It then decomposes complicated linked structures with grammar trees to guide the LLM to generate the SQL step by step. Extensive experiments on two benchmark datasets illustrate that SGU-SQL can outperform sixteen SQL generation baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method SGU-SQL, which represents user queries and databases into unified and structured graphs and employs a tailored structure-learning model to establish a connection between the user queries and the databases. The linked structure is then decomposed into sub-syntax trees, guiding the LLMs to generate the SQL query incrementally

### Strengths
This paper provides interesting ideas for text-to-sql, such as graph representation of query & data schema, query schema linkage, syntax tree based decomposition with LLMs, etc.  Although these concepts are not brand new, it is interesting to see how authors leverage on them with graph + LLMs

### Weaknesses
 **1 Method writing should be clearer**

It is not very clear how does schema-linkage is used in SQL generation by decomposition (sec 3.1)

How is score eq21 used in your algorithm? 

minor: 

PRELIMINARIES has detailed equations, etc, however this section seems not help introduce the method, may confuse readers (training GNN? prompting?)


**2. Performance is not competitive on more complex dataset like BIRD** 
To measure the effectiveness of the method, we need to show competitive results on complex realistic dataset. 

Table 2 is BIRD performance (exe acc 61), which is lower than SOTA 74 https://bird-bench.github.io/
SGU-SQL focus on leveraging structure-aware links between queries and database schema, so to prove effectiveness of the method, the method need to be tested on more challenging database, like BIRD. 

Table 1 Spider.  Many of the baseline methods are not Text-to-SQL specific method, therefore performance is not competitive. 
additionally only show method is good on Spider is not enough.  

ideally test performance on test split by submitting to leaderboard for generation ability



**3. need convincing ablation study to show each component designs is helpful**

Need ablation study on effectiveness of graph representation of query (sec 3.1) i.e.say compared with standard natural language representation without graph representation

Need ablation study on effectiveness of graph representation of database, compared with code representation “CREATE TABLE (...)” or serialized representation: table1: c1,c2 .. | table 2: c1, c2 … 

Need convincing ablation qualitative and qualitative results on the effectiveness of  “structure-aware linking”: effectiveness of DUAL GRAPH ENCODING(i.e. linking the query to the appropriate tables and columns in the database ). Since link query and database structure is one of key contribution, there should be clear ablation study

Need convincing ablation study to show “syntax-based decomposition” is effective. what if we do not do the “DECOMPOSING QUERY WITH SYNTAX TREE” (3.2.1), only directly generation SQL out. 
Table 3 compares with other basic decomposition approach. relatively simple prompt decomposition method can get on par text-to-sql performance ​​https://arxiv.org/pdf/2312.11242 (86.75 vs 87.5)

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
+ Identify the limitations of LLM-based Text-to-SQL models and introduce SGU-SQL, which
leverages structural syntax information to improve SQL generation capabilities of LLMs.
+ SGU-SQL proposes graph-based structure construction to comprehend user query and database
structure and then link query and database structure with dual-graph encoding.
+ SGU-SQL introduces tailored structure-decomposed generation strategies to decompose queries with
syntax trees and then incrementally generate accurate SQL with LLM.
+ Experiments on two benchmarks verify that SGU-SQL outperforms state-of-the-art baselines, including 11 fine-tuning models, 7 structure learning models, and 11 in-context learning models

### Strengths
+ The article is quite neat and meticulous, from giving mathematical formulas and reasoning why to do so and also the evaluation steps, ablation study, the article has introduced a completely new method in text2sql which is syntax-based prompting, avoiding traditional classical methods such as FewShot and CoT.
+ The method of the author group is quite new and very well implemented, the evaluation of the method is also on both open-source and closed source to provide an objective view.
+ The novelty of the method lies in the ability to build a good enough graph structure to link from user queries and information in the database, thereby helping to reduce the input of LLM to some extent, the selected information is carefully filtered to help the generated query be of better quality.

### Weaknesses
Overall I found the article quite good and have no comments on weaknesses.

### Questions
+ Have the authors compared the current method with the traditional CoT or FewShot methods?
+ What Lora rank does the author team use for fine-tuning? Have they tested it on multiple ranks?
+ Nhóm tác giả có thể giải thích thêm về cách training GNN, các thử nghiệm và kết quả đánh giá với GNN của bạn?

### Soundness
4

### Presentation
4

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
The paper focuses on tackling the challenge of generating robust and reliable SQL for a given natural language question. The authors propose SGU-SQL which is a novel framework leveraging the structural relationship between entities in user questions and the database tables for solving Text to SQL tasks using LLMs. There are three main challenges that the authors focus on:
1. Ambiguous user intents which lead to LLM's making uninformed decisions about SQL generation
2. Complex database schemas which may lead the LLM to confuse between different columns or tables
3. Complexity of SQL - LLMs are trained mainly for text generation whereas SQL is complex like programming language where only well-defined syntax must be used.

The authors tackle these issues by creating this framework where entities in natural language questions and the database are represented using graphs. These entities from questions to database are linked using a structure-linking model forming connections. Then, finally a prompt based method decomposes the complex question into subquestions and tackle these subquestions separately while aggregating them later. This method has been experimented with GPT-4 and a comparison has been reported using several models including SOTA from the leaderboard. Overall, the framework is proved to be successful while also achieving SOTA results on

### Strengths
1. The paper focuses on one of the critical issues with LLMs for SQL generation which requires the LLMs to tackle them in a unique way where reliability and robustness are a strong focus.
2. The framework is novel, intuitive and well designed to bridge the gap between an LLM which is tuned effectively for text generation and the SQL generation task which requires a structured understanding where the user queries can be ambiguous and answers can be complex.
3. The paper demonstrates strong results on the most popular SQL datasets SPIDER and BIRD which certifies the potential of the approach.
4. Well articulated work and not complex to follow from beginning to end. Conducted experiments including ablation studies are designed with thorough understanding.
5. The real world applicability and potential of this framework can be very high and effective when tackling large production grade databases in industrial applications.

### Weaknesses
1. The framework is novel and intuitive but because of SPIDER not being the best representation of production grade SQL, it would also beneficial to probably test them using SPIDER-2. BIRD is somewhat closer to a real-world SQL but SPIDER-2 has large-scale and diverse databases which evaluates the proposal on a much better dataset revealing how the proposal works on large scale datasets.
2. There's not much information provided on the future direction of this work which might hurt the significance/potential of the work a little. I'm mainly looking for how can this work be extended as it can provides opportunities for other researchers trying to explore in the same direction.
3. Specific discussion on the model used for structure linking seem insufficient. Like what training methodology and architecture choices.
4. When we discuss about constructing graphs and linking nodes, it may be important to learn about the complexities at a high level.

### Questions
1. In a real world, the databases are changed very often and there may be challenges where the proposed framework might not work same as proposed. In such cases, what components of the framework can still be relevant and what components must be changed is particularly industrial practitioners care about. Atleast including it in future directions might suffice.
2. How does this framework vary for dialects other than SQL? Not a super important question to clarify for the purpose of this conference, but having information about this can be helpful for practitioners.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Recent text-to-SQL methods using LLMs encounter challenges in accurately interpreting user intent and navigating the complex structures of databases. Existing decomposition-based approaches to improve LLM performance on text-to-SQL tasks often struggle with SQL's declarative syntax and the intricate links between queries and database elements. This paper introduces Structure Guided text-to-SQL (SGU-SQL), a novel framework that integrates syntax-based prompting to enhance LLM-driven SQL generation. SGU-SQL incorporates structure-aware linking between user queries and database schemas and decomposes complex SQL generation tasks into manageable subtasks through syntax-based guidance.

### Strengths
1) The experiments provide a comprehensive comparison with most of the previous works, showcasing that their approach outperforms all included baselines, although some recent approaches were not covered.

2) The novel prompting strategy significantly enhanced model performance across different LLM families, achieving substantial improvements over naive few-shot prompting and chain-of-thought (CoT) methods.

3) The paper presents an effective strategy for linking the structural elements of user queries to the database schema, facilitating more accurate SQL generation.

### Weaknesses
The primary limitation of this approach lies in the experimental section, where some of the most recent state-of-the-art methods, such as CHESS, Distillery, and CHASE-SQL, are not included. This omission is significant, as approaches like Distillery suggest that LLMs already demonstrate strong performance in handling complex schemas without the need for schema linking or query decomposition, challenging the findings of this paper. Additionally, as shown by CHASE-SQL, LLMs can achieve approximately 80% performance (compared to the 62% reported in this paper on BIRD) through enhanced sampling strategies, indicating that the main challenge in the text-to-SQL domain now lies in verifying the outputs of LLMs.

Furthermore, crucial tables, such as Table 2 and Table 3, have been relegated to the appendix. These tables contain valuable data and should be included in the main body of the paper for better accessibility and understanding.

### Questions
NA.

### Soundness
2

### Presentation
2

### Contribution
2
