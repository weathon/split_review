# EVOSCHEMA: TOWARDS TEXT-TO-SQL ROBUSTNESS AGAINST SCHEMA EVOLUTION

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Neural text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable performance. However, database schemas frequently evolve to meet new requirements. Such schema evolution often leads to performance degradation for models trained on static schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL or lacks a comprehensive and controllable way to investigate the model robustness issue
under the schema evolution. In this work, we approach this crucial problem by introducing a novel framework, EvoSchema, to systematically simulate diverse schema changes that occur in real-world scenarios. EvoSchema builds on our newly defined schema evolution taxonomy, which encompasses a comprehensive set of eight perturbation types, covering both column-level and table-level modifications. We utilize this framework to build an evaluation benchmark to assess the models’ robustness against different schema evolution types. Meanwhile, we propose a new training paradigm, which augments existing training data with diverse schema designs and forces the model to distinguish the schema difference for the same questions to avoid learning spurious patterns. Our experiments demonstrate that the existing models are more easily affected by table-level perturbations than column-level perturbations. In addition, the models trained under our paradigm exhibit significantly improved robustness, achieving up to 33 points improvement on the evaluation benchmark compared to models trained on unperturbed data. This work represents a significant step towards building more resilient text-to-SQL systems capable of handling the dynamic nature of database schemas.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper has made some notable contributions as follow:
1. Contributed a new training method using augmented data in column-level and table-level to help Text-to-SQL model keep performance in the context of rapid changing schema in the future.
2. The new training approach also showed good results as the column-level and table-level change scenario given in the paper.

### Strengths
For originality: Paper introduces new appoarch to enhance performance of Text-to-SQL model. Paper also defines in detail the types of structural transformations that help standardize test cases and studies the stability of the text-to-SQL model such as: adding, removing, renaming for column-level and adding, removing, renaming, splitting, merging for table-level, laying the foundation for further research.

For quality: Creating augmented data by combining heuristics and GPT models ensures that the transformed data is reasonable, diverse, and of high quality. Furthermore, experiment results are clearly presented and demonstrate that the method actually improves the model results.

For clarity: Paper is presented in a logical, easy to understand with a clear structure. The goals and methods are described in detail.

For significance: Paper demonstrates that this approach is worthy of further testing and developing in the future.

### Weaknesses
The paper has a major flaw in the benchmark datasets and experiments:
1. The method only performs benchmarking on the dataset prepared by the author himself, there is no other dataset used to benchmark the data augmentation task in the paper. We need more external benchmark datasets.

2. The paper does not explore further fine-tuning methods to improve model performance. In addition, comparisons with closed-source models such as GPT models are still limited. For example, prompting methods for GPT models such as few-shot should be tried to compare with the models in the paper.

### Questions
1. Have you considered testing EvoSchema on larger, real-world databases beyond BIRD and Spider?

2.  Can you provide insights about heuristics methods for creating robust dataset?

3. Closed-source models are currently very high performing for code generation tasks like this. Why not consider tweaking them to make the answers of the closed-source models better so that comparing them with the results of a more meaningful method makes sense?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses an important practical challenge in text-to-SQL systems: maintaining performance when database schemas evolve. A novel training paradigm was proposed to augment training data with diverse schema designs to improve model resilience. The experimental results reveal that table-level changes impact model performance more significantly than column-level changes, and their proposed training approach demonstrates substantial improvement over baseline models.

### Strengths
1. The introduction and related work sections are well organized. It clearly sketches the existing problem, the proposed argument, and related work for text-to-SQL.

2. The topic of this paper is interesting and practical since real-world databases are always evolving.

3. Intensive experiments have been conducted to verify the performance of the proposed model.

### Weaknesses
1. The method of dividing the training and testing sets is unclear in this paper. 

2. How to get the new training and testing data with evolved databases is not clear. Do all the training and testing data share the same schema structure after the database evolves? If so, how can data leakage be avoided? If not, does it mean that there is only one change of database schema for each instance, and different instances share different structures of database schema? 

3. Cost and Efficiency Analysis. This paper uses closed-source LLMs, like GPT-3.5 and GPT-4, to generate synthetic data. Is it expensive? How many budgets are needed to achieve a desirable performance?

4. Some experiment results are suspicious and meaningless. Table 1 presents comparative results between open-source LLMs and closed-source models (GPT-3.5 and GPT-4) under schema evolution scenarios. However, this comparison is fundamentally flawed since closed-source LLMs cannot be fine-tuned with evolved schemas. Without the ability to retrain or adapt these models, the performance comparison between scenarios with and without schema evolution lacks scientific validity. The authors should either remove these misleading comparisons or clearly explain their methodology for evaluating closed-source models in this context.

### Questions
See above.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper tackles the robustness issues of Text to SQL. Primarily, it focuses on how database schema influence the SQL generation by ML models/LLMs. The work called EVOSchema provides a in-depth study of how schema changes at each table level and column level affect the robustness of text to SQL. The study is performed by introducing an approach that augments training data with heuristic and LLM based schema perturbations and enabling the trained models to learn more effectively ignoring undesired patterns from the data. Experiments have been conducted using the most popular Text to SQL datasets SPIDER & BIRD to demonstrate the improvements with their approach. Overall, this is an important work that highlights the importance of robustness in SQL generation and also proposes a reasonable approach to tackle the database schema influence on the same.

### Strengths
1. Focused on a critical problem with LLMs and overall tackled it well.
2. This is a comprehensive framework for studying and improving robustness of Text to SQL against schema updates/changes.
3. Proposed metrics are robust and can serve as benchmark/baseline for further improvements in this specific area.
4. Training paradigm is diverse and well designed to assess the perturbations correctly.
5. Well articulated paper overall and easy to read.
6. Defined metrics are intuitive and appropriate for understanding the robustness.

### Weaknesses
1. First of all, the scope of the work is narrow i.e. it only focuses on one type of robustness challenge in Text to SQL.
2. The paper doesn't offer any novelty, originality or focuses on any strong theoretical foundations behind robustness issues in LLMs or any ML models.
3. There are several other works that tackle robustness and specific papers like ADVETA which tackle the robustness of SQL generation from schema changes. This work neither compares with them nor goes into detail about why this is one of the critical ways to tackle robustness in SQL.
4. Text to SQL systems don't necessarily use fine-tuned models. In such cases, this work is not relevant. Considering the generalizable nature of LLMs, it might be more effective in using such robustness strategies for post-training cases.

### Questions
There is just one big reason why this is not a sufficient contribution. The work is very narrowly scoped and offers very less novelty. These two can be improved well to make it a valuable contribution.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Database schemas evolve as end-user information needs change. However, most models are trained on static data and do not account for robustness under schema evolution. This paper addresses this challenge by (1) creating a taxonomy of common schema perturbation types, (2) developing a benchmark that simulates these schema changes, and (3) fine-tuning existing models on training data augmented with these perturbation types.

The paper shows that fine-tuning models on the perturbation-augmented data enhances their robustness to database schema changes.

### Strengths
1. This paper addresses a critical problem: enhancing model robustness in the face of data evolution. In the context of Text-to-SQL, data evolution specifically refers to schema changes.
2. The paper develops a taxonomy for schema evolution, mapping each type of perturbation to a real-world scenario. 
3. The paper presents a thorough evaluation across a wide range of open-source models as well as state-of-the-art commercial models.

### Weaknesses
1. The benchmark generation section is too brief and lacks critical details, which weakens the validity of the paper's results. My main question here is: how do you ensure that adding tables or columns does not create alternative correct SQL answers? Adding a table can introduce alternative join paths or semantically similar columns, which could also be used to answer the NLQ accurately. For example, in Figure 2, when adding an "appointment" table, if this table contains fields such as the patient who makes the appointment, the doctor assigned, and the laboratory records associated with the appointment, it could be used to join "patient" and "laboratory," forming another valid SQL query to answer the question. The paper mentions “applying heuristics to choose suitable synthesized tables or columns, which are not duplicated with existing ones.” However, this is too vague. What are the specific "heuristics"? What defines “suitable”? Is "duplicate" assessed in terms of syntactic similarity or semantic similarity? Please provide a more detailed explanation of the validation process for ensuring the uniqueness of correct answers after schema perturbations.

2. While the evaluation section is detailed, some results are counterintuitive, and the paper does not provide thorough explanations:

    a) In Table 1, why does "adding tables" cause the most significant drop in table match F1? How many tables were added? This seems counterintuitive, as "splitting tables" also increases the number of tables, yet its F1 score is much higher than "adding tables" (without perturbation).

    b) In Table 1, for "adding tables (w/o)," why is the column match F1 higher than the table match F1? This is counterintuitive, as correctly selecting columns typically requires selecting the correct table. The only plausible explanation is that columns are unevenly distributed across tables, and the model may accurately identify many columns in certain tables but fails to do so consistently across other tables.

    c) GPT-4 is used to generate the gold query for split and merge table cases. However, in Table 1, its performance is lower than that of models fine-tuned on augmented data for "split/merge tables." This is surprising, as GPT-4 should know the gold query for these scenarios.

Could you provide a more detailed explanation on these counterintuitive results?

3. My questions are listed in the second point of weaknesses.

Besides, I have doubts about the explanation in Section 4.2. It states that “during training without perturbations, the model only sees relevant table schemas, causing it to learn spurious patterns that always attempt to join all input tables.” I don’t believe this is accurate, as in BIRD, most gold SQL queries use only 2-3 tables from the database schema and there are many SQLs that only use a single table. It’s unclear to me why the model would learn that joining all tables is a beneficial pattern. An analysis comparing the distribution of table usage in the training data with the table usage distribution in the model-predicted SQLs would be helpful.

### Questions
My questions are listed in the second point of weaknesses.

Besides, I have doubts about the explanation in Section 4.2. It states that “during training without perturbations, the model only sees relevant table schemas, causing it to learn spurious patterns that always attempt to join all input tables.” I don’t believe this is accurate, as in BIRD, most gold SQL queries use only 2-3 tables from the database schema and there are many SQLs that only use a single table. It’s unclear to me why the model would learn that joining all tables is a beneficial pattern. An analysis comparing the distribution of table usage in the training data with the table usage distribution in the model-predicted SQLs would be helpful.

### Soundness
2

### Presentation
2

### Contribution
3
