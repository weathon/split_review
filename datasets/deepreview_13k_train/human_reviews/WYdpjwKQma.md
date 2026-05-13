# LAIA-SQL: Enhancing Natural Language to SQL Generation in Multi-Table QA via Task Decomposition and Keyword Extraction

- Decision: Reject
- Scores: 8, 3, 6, 3

## Abstract
Natural Language to SQL (NL2SQL) provides an effective solution for multi-table question answering (Table QA) to automate data retrieval by transforming simple user queries into SQL commands. It enhances data accessibility and decision-making processes across various industries. Large Language Model (LLM) based NL2SQL methods have been shown to outperform rule-based or neural network-based NL2SQL methods. However, existing LLM-based NL2SQL approaches face challenges like inaccurate interpretation of user questions, slow retrieval speeds, erroneous SQL generation, and high operational costs. As there is a lack of datasets specifically designed to evaluate natural language understanding (NLU) in NL2SQL tasks and no models optimized for user question understanding in Table QA, we introduce LAIA-NLU, a novel dataset that dissects NLU into task decomposition and keyword extraction. LAIA-NLU contains 1,500 high-quality QA pairs, created through manual review. Using this dataset, we developed LAIA-NLUer, which is capable of effectively interpreting user intent in table-based queries. To further enhance NL2SQL performance in terms of speed, cost, and accuracy, we also present LAIA-SQL, a retrieval-augmented based NL2SQL framework. Experimental results show that LAIA-SQL outperforms state-of-the-art models, achieving an accuracy improvement to 67.28% in BIRD dataset, a 52.4% reduction in runtime, and a 97% decrease in operational costs. These improvements demonstrate the potential of our approach to advance multi-table data retrieval and analysis. Our code, dataset, and model will be publicly available to encourage further research in this field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses challenges in transforming natural language questions into SQL commands for multi-table question answering (Table QA). The authors introduce LAIA-NLU, a dataset focused on understanding natural language in NL2SQL tasks through task decomposition and keyword extraction. This dataset contains 1,500 carefully curated QA pairs, enabling improved interpretation of user intent in table-based queries. Building on this, the authors developed LAIA-NLUer, a model that enhances user question understanding, and LAIA-SQL, a retrieval-augmented NL2SQL framework optimized for cost, speed, and accuracy.

### Strengths
- Paper is well written and easy to follow.
- Their method is novel, efficient and effective.

### Weaknesses
 - Would like to see some Human Evaluation done on the outputs.
- The authors mention this in the limitations as well but maybe the dataset could be expanded using data augmentation strategies.

### Questions
- I am curious to see some examples of the revision module correcting mistakes.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the problem of question answering from multiple tables by converting users’ natural language questions into executable SQL, a task at the intersection of TableQA and text-to-SQL. The paper focuses on retrieval-augmented text-to-SQL methods, where parts of the tables are retrieved to better form the final SQL query. It proposes to tackle this task in several steps:

1. Understanding the User Query (NLU): Extract keywords and break down the query into simpler steps.
2. Table Retrieval: Identify and extract the necessary data from the underlying tables.
3. SQL Writing Stage: Create the SQL query based on the retrieval output, and optionally revise it using feedback from SQL syntax error messages.

The authors propose a dataset for query decomposition and keyword extraction in the multi-table text-to-SQL task, called _LAIA-NLU_. This dataset is constructed using questions from the BIRD dataset, and human-verified GPT-4o labels. Furthermore, they introduce _LAIA-SQL_, a retrieval-augmented text-to-SQL system that implements these three stages.

The paper experiments with various configurations of LAIA-SQL, using:

- NLU Stage: Few-shot `GPT-4`, fine-tuned `GPT-4o-mini`, and fine-tuned `Mistral-7B`.
- Table Retrieval: BM25 and MinHASH combined with OpenAI’s `text-embedding-3`, `Stella-400M`.
- SQL Writing Stage: Few-shot `GPT-4`, `GPT-4o`, and fine-tuned `DeepSeek-Coder` models.

Experimental results on the BIRD and Spider datasets show that LAIA-SQL outperforms prior systems in terms of lower latency and cost, and higher execution accuracy.

### Strengths
Evaluating latency and cost of text-to-SQL systems is of value but is often ignored in research. It is great that this paper is paying attention to this.

### Weaknesses
## 1. The connection between this paper and prior work should be improved.
The paper revisits concepts that have been extensively studied in the field. Question decomposition has been thoroughly explored in TableQA, knowledge base QA [1], and more general agentic search systems [4][5]. Additionally, similar research [2] [3] investigates prompting LLMs for query decomposition in text-to-SQL. Table retrieval for text-to-SQL is studied in [7]. These references are not included in the problem definition, prior work section, and experiments, and it would be beneficial to address this.

Other areas where the connection could be improved include:
- The paper assumes that query decomposition and keyword extraction are the primary methods for solving multi-table QA (L048, among others), which is inaccurate.
- Section 2.2 seems to conflate the NLU and TableQA literatures.
- L078 states, "There is a lack of quantitative evaluation metrics for assessing NLU performance across different LLMs within the TableQA domain," which is not substantiated. More broadly, what is the need for a question decomposition dataset, beyond the likes of [1]?
- The reference to TA-SQL (Line 082) should be corrected to [6].
- L121 mentions GraphRag, but that does not experiment with tables.

I recommend conducting a more comprehensive literature review, including papers published prior to 2024, and revising the claims and experiments accordingly.

## 2. The comparison of experimental results with prior work is potentially misleading.

Importantly, the comparison of experimental results with prior work is not apples-to-apples. For instance, the comparison against CHESS uses the evaluation result from that paper. However, CHESS uses `GPT-4-Turbo`, which is slower and more expensive than `GPT-4o` used in this paper. This undermines the claim that this paper outperforms prior work on cost and latency. Additionally, latency and cost (reported in Table 2) are not measured in the same end-to-end setting as Table 1.

## 3. Experiments could benefit from additional clarity and details.
The paper presents several ablation results, but the purpose of the ablation studies and the conclusions that can be drawn from them are unclearer. For example, it would be helpful to understand whether the reported accuracy and latency/cost benefits are due to better decomposition of the task compared to agentic approaches, better/shorter prompts, or higher quality of the models that are used and fine-tuned.

Some details that need further elaboration on include:
- In Section 4.2, it would be helpful to explain how tables are encoded into vectors and what preprocessing is done, considering that tables can be quite large.
- In the results reported in Tables 1 and 2, it should be specified which embedding model and reranker are used.
- In Tables 3 and 4, why do systems alternate between GPT-4 and GPT-4o? Keeping all but one of the components the same would help make better sense of the ablation results.

### Questions
1. What is the "Accuracy" metric in Table 2? How does it differ from dev EX in Table 1?
1. In Figure 1, a comparison is shown between GPT-4o and the "ours" method for task decomposition and keyword extraction. However, from what I understand, "ours" also uses GPT-4o. What is the main difference?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to enhance NL2SQL by improving the natural language understanding capabilities of LLMs via fine-tuning on a new NLU dataset. The authors motivate this approach with LLMs' weakness to decompose tasks and extract informative keywords correctly. They then curated a new NLU dataset specific to the NL2SQL scenario, LAIA-NLU, derived from BIRD and consisting of 1500 samples. The dataset was generated by first prompting GPT-4o and then revising manually by annotators. The authors then finetune LLMs on this dataset and integrate the fine-tuned LLM as a specialized NLU module into a retrieval-based NL2SQL framework. Experiments showed significant improvement over baseline models and marginally outperformed concurrent models on the BIRD leaderboard. The authors also claimed improvement in practical utility metrics including Time, Accuracy, and Cost, but the evaluation process for the practical utility metrics is not very clear.

### Strengths
## **1. The dataset seems reasonably useful**

The dataset is well motivated with an obvious pain point of LLM-based NL2SQL approaches, that is they do not always decompose tasks and locate key entities correctly. I can see the dataset serving as an auxiliary task for future modulized or end-to-end NL2SQL systems.

## **2. Experiment results show the effectiveness of fine-tuning LLMs on the dataset**

The ablation study (Table 3) shows adding the NLU module leads to significant improvement against the baselines (7.6% execution accuracy improvement on BIRD). The LAIA-SQL framework as a whole is also reported to outperform baselines on BIRD and Spider, although I have some concerns about the baseline choices, which I will elaborate on in the weakness and question sections.

## **3. The proposed framework improves significantly on practical utility metrics**

The authors also reported significant improvement in the practical utility metrics, including Time, Accuracy, and Cost. It is reported to achieve a 52.4% reduction in runtime, and a 97% decrease in operational costs. However, more clarification about the evaluation setup and experiment details is needed.

### Weaknesses
## **1. The effectiveness of the approach is not well supported by the current experiment**

There are a few aspects of approach effectiveness that the authors are demonstrating, namely
1. Finetuning LLMs on LAIA-NLU makes them better user intent interpreters.
2. With the user intent interpreters, LAIA-SQL outperforms SOTA models on BIRD and Spider.
3. The LAIA-SQL framework also excels in practical utility metrics.

The current experiment settings did not fully support 2 and 3. This could be partly due to inconsistencies in the paper writing, but fundamentally it is due to the choice of baselines and experiment configurations that can be improved.

### **1.1 For 2, below are my recommendations:**

**In Table 1, I recommend using the official test score of the BIRD bench, for the following reasons:** 
1) there can be performance gaps between the dev set and test set, as seen in other models on the current leaderboard (e.g., Distillery + GPT-4o has 67.21 on the dev set but 71.83 on the test set, while Insights AI has 72.16 on the dev set but 70.26 on the test set), and the official leaderboard uses test set metric as the main ranking metric. 
2) the current reported number only indicates marginal improvement on the dev set. It's hard to justify the superiority of the performance with statistical significance.

I understand the concern mentioned by the authors in the paper that
> due to the anonymity policy, we only report the execution accuracy on the development dataset

However, according to the official Author Guide of ICLR 2025, it is permitted to report such numbers: https://iclr.cc/Conferences/2025/AuthorGuide
> Q: Can you explain how to treat de-anonymization in the case where a submitted paper refers to a challenge they won which can identify the authors?  
> It is ok to report the results on the leaderboard of a challenge. The authors can include the ranking and the name of the challenge. The reviewers will be advised to not intentionally search the authors by examining the leaderboard.

**In Table 3, I recommend revising the ablation configurations or explaining clearly the rationales behind the choice**

I'm confused by the current configurations. By comparing L435-436 I understand that UQU is providing a positive performance gain, but what does L436 vs 437 mean? What is the generation backbone model if it is not GPT-4o? I would recommend keeping the backbone model consistent (e.g., always using GPT-4o) while ablating the modules. It is unclear how the different modules interact and contribute to the overall performance. For example, does the revision module operate on the output of the SQL generation module, or does it have its own independent input? The lack of clarity makes it difficult to assess the individual contributions of each component.

In addition, I think the configuration "revision + generation" might be worth adding since that is also a common approach. I do not think entity retrieval is always done in NL2SQL approaches.

**In writing, I recommend removing the statements that the proposed approach outperformed SOTA models on both datasets**

I think it is fair to claim that the proposed method outperformed comparable (criterion: open source or published paper) models, but it would be misleading to say it outperformed SOTA models, especially on the Spider dataset.

### **1.2 For 3, I'm mainly referring to Table 2 in the paper.**

The main issue is that the evaluation process of getting these metrics is not included in the paper. Excluding the context makes the numbers hard to interpret. What does accuracy = 0.8 mean? Likewise for Time (s) and Cost. The lack of detail on how these metrics were calculated makes it difficult to reproduce the results or compare them with other studies. For example, what hardware was used to measure the time? What is the cost model used? Are these averages over multiple runs? These details are crucial for understanding the practical implications of the proposed approach.


## **2. The presentation can be clearer**

**Table headers can map to sections**

The modules in Figure 4 align with Section 4 well. However, the granularity in Table 3 seems not uniform. Are "Revision" and "Generation(*)" both part of section 4.3? Consider splitting them into columns or color-coding them for better readability. 

Same thing with Table 4, which is not very straightforward how components in each row map to the framework anatomy and which rows to compare. The current table format makes it hard to understand the impact of different components on the overall performance. For example, it is not clear which rows should be compared to isolate the effect of a specific module.

**The paper has some inconsistencies/unclarities that should be addressed.**

One thing that confused me at the beginning was "LAIA-NLUer", which seems to only appear at the beginning and end of the paper. My assumption is it is later named the "UQU" module. I would recommend unifying that.

L407 mentioned Qwen-1.5-Coder, yet I don't think it is included.


**Typos and formatting**

L081-L083, among others: CHESS Talaei et al. (2024) -> CHESS (Talaei et al., 2024) 

L236: 'unsatisfactory' -> ``unsatisfactory''

L301: "SELECT" -> ``SELECT''

L375: Bird -> BIRD

L435: Generaton -> Generation

### Questions
Please refer to the Weakness section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the LAIA-SQL framework, which is oriented toward increasing performance in NL2SQL generation for TableQA. To improve its NLU, especially for NL2SQL so that it can generate more accurate SQL, it creates an LAIA-NLU dataset. Using this dataset, the authors have identified an appropriate model called LAIA-NLUer that improves user intent interpretation and quality in SQL generation. The LASQL framework optimizes understanding, retrieval, and generation modules for significantly improved accuracy and efficiency. This can be further manifested from the experimental results where LAIA-SQL outperforms the existing models in runtime reduction and cost saving. As a result, LAIA-SQL provides a much faster and less costly solution regarding NL2SQL and TableQA tasks.

### Strengths
1. The performance of LAIA-SQL is highly promising. Experimental results indicate that LAIA-SQL achieves superior accuracy compared to other state-of-the-art NL2SQL methods. Its performance on widely recognized BIRD and Spider benchmarks highlights its effectiveness and robustness.

2. The cost-effectiveness of the proposed method is impressive. LAIA-SQL not only improves accuracy but also reduces operational costs by up to 97% compared to competing methods. This cost efficiency, along with a 52.4% reduction in runtime, demonstrates that LAIA-SQL is well-suited for enabling large-scale NL2SQL solutions in real-world applications.

3. The introduction of a new dataset for NLU is a novel contribution. By creating the LAIA-NLU dataset, the authors address a critical gap in NL2SQL tasks. Designed with task decomposition and keyword extraction in mind, this dataset enhances model training and evaluation, providing a specialized resource that significantly advances NLU capabilities in SQL generation.

### Weaknesses
1. The paper would benefit from a more comprehensive review of existing work in the field. Section 2 should include an individual subsection that covers more related work on NL2SQL, such as [1][2][3][4][5].

2. The paper does not include an error analysis of the SQL generation task. Referring to advanced studies [6][7], an error analysis that categorizes the types of incorrect execution would provide significant insights into which types of SQL the proposed methods handle well and where they still struggle. Additionally, a comparison of execution errors with previous methods could clearly demonstrate the improvements brought by the proposed framework. Readers are often interested in understanding why it works as much as how it works.

3. Some of the contributions in the paper are not clearly verified. In L18-L20, the authors claim that current approaches in NL2SQL suffer from slow retrieval speeds, and in L27-L31 they claim to have achieved a speed-up. However, Table 2 presents only the total time cost without detailing the time cost of each component, particularly the entity retrieval module. The authors should present the retrieval performance of current approaches as a baseline and then show that their proposed framework is more effective in clearly verifying their contribution.

### Questions
1. How does the Revision module work? The authors claim that the incorrect SQL and execution feedback are combined to prompt LLMs to revise the original SQL. How many times is the revision conducted? Is there any criterion or threshold to prevent an infinite loop of revisions for extremely difficult questions? Additionally, how does this module relate to cost-effectiveness? Will the overall framework cost be influenced by the number of revisions?

2. Why is the proprietary model utilized in the module ablation study different? In Table 3, the comparison between "Entity Retrieval + Revision + Generation" and "Entity Retrieval + Generation" uses different models (GPT-4o and GPT-4), which is confusing. Did this setting lead to a correct conclusion in Section 5.3? Furthermore, how does the framework work with open-source models in each module?

3. Will the authors consider submitting the results of the paper to the public leaderboards BIRD and Spider to verify their performance on the test set? I believe making the LAIA-NLU dataset publicly available would enhance the contribution of the paper.

4. There are a few typos and formatting errors in the paper. The authors should carefully revise these aspects.

### Soundness
1

### Presentation
1

### Contribution
2
