# CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
In tackling the challenges of large language model (LLM) performance for Text-to-SQL tasks, we introduce CHASE-SQL, a new framework that employs innovative strategies, using test-time compute in multi-agent modeling to improve candidate generation and selection. CHASE-SQL leverages LLMs' intrinsic knowledge to generate diverse and high-quality SQL candidates using different LLM generators with: %(1) a divide-and-conquer method for complex queries, where we decompose them into sub-queries in a single LLM call; (2) a query execution-plan based chain-of-thought reasoning, where we mirror the steps a database engine takes during query execution to enhance performance; and (3) a novel instance-aware synthetic example generation technique to provide test-question specific few-shots demonstrations . To choose the best candidate, we employ a selection agent robustly selects condidates by ranking the candidates through pairwise comparisons with a finetuned LLM. Our {\it generators-selector} framework enhances both the quality and diversity of candidate queries, demonstrating superior performance over traditional methods. 
(1) a divide-and-conquer method that decomposes complex queries into manageable sub-queries in a single LLM call; 
(2) chain-of-thought reasoning based on query execution plans, reflecting the steps a database engine takes during execution; and 
(3) a unique instance-aware synthetic example generation technique, which offers specific few-shot demonstrations tailored to test questions.
To identify the best candidate, a selection agent is employed to rank the candidates through pairwise comparisons with a fine-tuned binary-candidates selection LLM. This selection approach has been demonstrated to be more robust over alternatives. The proposed generators-selector framework not only enhances the quality and diversity of SQL queries but also outperforms previous methods. Overall, our proposed CHASE-SQL achieves the state-of-the-art execution accuracy of 73.0 \% and 73.01\% on the test set and development set of the notable BIRD Text-to-SQL dataset benchmark, rendering CHASE-SQL the top submission of the leaderboard (at the time of paper submission).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The article discusses the formation of a pipeline for text2sql, which includes the following main parts: combining multiple methods (including DC-CoT, Query Plan-CoT and OS-CoT) to generate a set of candidate sql, with each sql query running through a fixer to fix the query so that it can be run, and finally, comparing each pair of queries and ranking to choose the most suitable query. The pipeline is implemented on close-source LLMs and is carefully promoted and evaluated to come up with a good method when testing multi-agent LLM for the text2sql task. The method reaches an execution accuracy of 73.01% and 73.0% on the development set and test set of the challenging BIRD Text-to SQL dataset which outperforms all of the published and undisclosed methods on this benchmark by a large margin.
Contribution:
+ Experiment multi method (include few-shot, CoT) to generate candidate SQL query from natural language text.
+ Develop evaluator agent to score every candidate and ranking for choose the best candidate.
+ Experiment combination and ablation many method choose to the effective text2sql pipeline.
+ Adapt Multi-agent LLM approach.

### Strengths
+ Proposed a pipeline that provides high efficiency on text2sql data and has proven its efficiency and high results on difficult benchmarks such as Bird and Spider.
+ There is a thorough review and explanation, making it easy to combine and remove components throughout the system.
+ The paper is presented fully and in detail, with thorough explanations of mathematical formulas, complete conclusions and details in the evaluation and testing.

### Weaknesses
 + CoT, Few Shot or query fixer methods are quite classic in testing LLM, so they have not mentioned the highlights in generating this query.
+ Beside the method uses available closed source models such as claude, gemini pro mainly to perform prompting and connect agents together, it is not possible to verify whether it is good to fine-tune open source for the above methods. The article would be better if there was more in-depth research on fine-tuning these models, which could be a useful scientific research and could be more easily deployed in practice. Overall, I rate the article very well in terms of testing and conclusions drawn.

### Questions
+ How about experimenting with the above pipeline for an open-source LLM, is it possible?
+ Can you give some examples of selecting rows to match the schema and user query?
+ Why schema union is so effective in evaluating your query pairs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the CHASE-SQL framework, a novel approach for improving text-to-SQL task with LLMs. The framework proposes multi-path reasoning techniques that decompose complex queries and optimize candidate generation for SQL, which involves three main strategies: a divide-and-conquer approach for breaking down queries, a CoT reasoning based on query execution plans, and an instance-aware synthetic example generation to enhance LLM performance. To select the best SQL candidate, a fine-tuned selection agent ranks generated queries through pairwise comparisons, achieving high accuracy. Extensive experiments have validated the effectiveness of the proposed framework. CHASE-SQL demonstrates SOTA performance on the well-recognized BIRD benchmark, achieving an execution accuracy of 73%, making it the top place on the leaderboard.

### Strengths
1. The performance of the proposed CHASE-SQL framework is highly promising. It achieves SOTA accuracy on the well-recognized BIRD benchmark, outperforming both published and undisclosed methods, thereby demonstrating its effectiveness in complex text-to-SQL tasks.

2. The experiment of the paper is sufficient, and the error analysis section is detailed and highly informative. The authors provide comprehensive analyses, including performance across different databases, error analysis, and selection agent errors, offering clear insights into the model's strengths and areas for improvement. Notably, the error analysis section is outstanding and is garnering increasing attention within the text-to-SQL community, as it helps readers understand not only how the framework works but also why it works.

3. The overall framework is novel, and the paper is well-organized and easy to understand. The structure effectively presents the methodology, experiments, and results, making it accessible for readers to comprehend the contributions and significance of the proposed approach.

### Weaknesses
1. The paper does not include the cost of the proposed framework. Prompting proprietary LLMs for SQL generation has become a mainstream approach in text-to-SQL research. When the performance of various methods shows no significant differences, the method with lower API costs is typically preferred. Previous work has focused more on models released by OpenAI (e.g., ChatGPT, GPT-4) [1]. Since the Gemini series is also an outstanding proprietary LLM, this paper presents a good opportunity to introduce the series to the community by comparing its performance and API costs. Specifically, the paper lacks a detailed breakdown of the API calls made during the multi-path reasoning process, including the number of tokens used for each prompt and the associated costs. This information is critical for assessing the practical feasibility of the proposed method, especially when compared to other LLM-based approaches.

2. The model ablation study is lacking in the paper, and the selection of open-source models has not been discussed. The paper would benefit from verifying the proposed framework on a broader range of models, including GPT series models (e.g., ChatGPT, GPT-4) and open-source models (e.g., LLaMA-3.1, Qwen-2.5). Recently, well-designed frameworks for open-source models have achieved promising progress [2][3], demonstrating particular effectiveness for local deployment and real-world applications. Therefore, experiments on open-source models in this paper could further advance this development. The absence of experiments on open-source models limits the generalizability of the findings and their applicability in resource-constrained environments. Furthermore, the paper does not explore the impact of different model sizes and architectures on the performance of the proposed framework.

3. The description of the Query Fixer module is relatively brief. The authors could consider adding a detailed algorithm for correcting incorrect SQL in Section 3.4. Additionally, I suggest including a separate limitations section to discuss the potential challenges for application, such as the framework's complexity, generalization and extension capabilities [4], and the potential limitations in handling ambiguous questions [5][6]. The paper should delve deeper into the specific mechanisms used by the Query Fixer, including the types of errors it can handle and the strategies it employs for correction. A more detailed explanation would enhance the transparency and reproducibility of the proposed method.

### Questions
1. As a reviewer, I highly appreciate the detailed error analysis in this paper. However, I suggest that the authors include some parts of the error analysis in the main content instead of the Appendix, as it is gaining increasing attention from the text-to-SQL community.

2. As shown in Appendix A.3, why is the number of correct samples for some databases zero across various methods? Could this result be combined with the difficulty level of the corresponding questions for further analysis?

3. For the prompt used in the Query Fixer module, there are few-shot examples provided, as shown in Appendix A.7. What type of execution results do the examples represent? How does the performance of this module vary across different types of execution results (errors)? As an assumption, could including a diverse range of few-shot examples that cover as many types of execution errors (e.g., Column Not Found, Data Type Mismatch) enhance the correcting capability of the Query Fixer module?

4. The authors could consider using a different abbreviation instead of "CHASE" since there is a related work in the text-to-SQL community with a similar name [7].

[7] Jiaqi Guo, et al. "Chase: A Large-Scale and Pragmatic Chinese Dataset for Cross-Database Context-Dependent Text-to-SQL" In Proceedings of ACL, 2021.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces CHASE-SQL, a state-of-the-art Text-to-SQL approach that achieved top performance on the BIRD benchmark at the time of submission. It employs three prompting strategies — Divide-and-Conquer, Query Plan, and Few-Shot prompting with synthetic example generation — to first generate a diverse set of SQL candidates. These candidates are then evaluated by a selector, which is fine-tuned on BIRD to select the correct SQL from two SQLs. The selector does pair-wise comparison over the pool of candidates and outputs the one having the highest score.

### Strengths
1. The paper is well-written and provide a lot of details and insights for readers to learn about. The evaluation is solid with comprehensive comparison, lower/upper bound analysis and ablation studies. The design of all components within CHASE-SQL are well-justified.

2. Although the pipeline of generating a candidate pool and then selecting from it is not new, CHASE-SQL introduces novel strategies for candidate generation and fine-tunes the selector in a unique way, focusing on simple tasks, i.e., pairwise selection, rather than relying on reranking or selecting from a large pool. I particularly appreciate the approach used to construct the few-shot examples. Instead of tailoring examples to specific SQL types, it includes examples for both the full database and the specific database relevant to the question. Moreover, it aims to cover a broad range of SQL features rather than only complex examples, which significantly reduces the risk of the model overfitting to the provided examples.

3. By using examples generated on BIRD and fine-tuning the selector solely on BIRD, CHASE-SQL also achieves competitive performance on the Spider benchmark, demonstrating its generalizability.

### Weaknesses
The main concern is the cost and latency of CHASE-SQL. Assuming each generator produces 7 candidates, this results in 21 LLM calls. The prompt length for each call is also substantial, especially with the few-shot prompting strategy, which includes examples for both the full database and the specific database, aiming to cover a wide range of SQL features. For the selector, CHASE-SQL employs a pairwise comparison strategy, leading to O(n^2) LLM calls, where n is the total number of generated candidates. It would be helpful if the authors reported the total number of tokens processed by CHASE-SQL to generate SQL for a user query and provided the end-to-end latency. Given these factors, I am uncertain whether CHASE-SQL can achieve interactive Text-to-SQL. The token cost analysis provided for the Chase-SQL Generator seems inconsistent with my calculations. The paper states that for the financial database, the total number of input tokens for the Chase-SQL Generator is approximately 0.16 million across 106 questions, averaging about 1,510 tokens per question. However, my analysis of the generator input tokens, which includes the lengths of the Divide-and-Conquer Prompt, Query Plan Prompt, and Few-Shot Prompt, suggests a much higher token count. Specifically, I calculated the database description string for the financial database to be 1,204 tokens. When integrated into the provided prompts, the token lengths are: Divide-and-Conquer Prompt: 2,055 tokens; Query Plan Prompt: 1,814 tokens; and Few-Shot Prompt: at least 9,450 tokens, assuming 75 examples with 126 tokens each. This results in a total token count per question exceeding 13,319 tokens, which is significantly larger than the reported 1,510 tokens per question. This discrepancy raises concerns about the accuracy of the reported token usage.

### Questions
1. How many examples are included in the few-shot prompting (online synthetic example generation)?
2. What is the total number of tokens processed if I use CHASE-SQL to generate the SQL for a single question?
3, What is the end-to-end latency of CHASE-SQL?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Chase-SQL, which combines SQL queries generated by various LLM strategies to enhance query quality for natural language questions. It utilizes diverse approaches, including divide-and-conquer, few-shot learning with demonstration synthesis, and self-debugging. Leveraging Gemini Pro 1.5, Chase-SQL sets a new state-of-the-art performance on two prominent benchmarks, BIRD and Spider.

### Strengths
The main strength of the paper is its robust framework, which effectively integrates multiple LLM strategies to optimize SQL query generation, leading to state-of-the-art results. This framework not only demonstrates the versatility of techniques such as divide-and-conquer and self-debugging but also highlights the potential for real-world applications in natural language processing. It achieves superior performance on well-established benchmarks like BIRD and Spider.

### Weaknesses
The main weaknesses of the paper stem from the limited novelty of the framework and its individual techniques. A recent comprehensive survey on NL2SQL, available at https://arxiv.org/pdf/2408.05109, addresses many of the technical innovations discussed here, encompassing a wide range of recent studies that leverage LLMs. This suggests that the contributions may not be as groundbreaking as implied, as they largely reiterate established concepts in the field. 

First, let’s discuss the individual algorithms.

W1. Divide-and-Conquer: This concept has been widely utilized in various NL2SQL studies, including DTS-SQL, TKK, and DEA-SQL, as illustrated in Figure 6 of the NL2SQL survey under the "Decomposition" branch. The papers of all the referred methods can be found in the survey. In order to highlight the technical contributions, it would be helpful to clarify how the proposed divide-and-conquer approach differs from or improves upon these existing methods. Specifically, the paper needs to articulate how its decomposition strategy avoids the error propagation issues inherent in multi-stage pipelines, and how it differs from methods that decompose the SQL generation task itself, such as TKK.

W2. Chain-of-Thought: The Chain-of-Thought (CoT) approach has also been extensively applied in NL2SQL research, with examples such as CHESS, ACT-SQL, and COE-SQL, which can be found in Figure 6 of the NL2SQL survey under the "Chain-of-Thought" branch. While the paper demonstrates improved performance using its CoT approach, it does not sufficiently justify the novelty of its specific implementation. The paper needs to clarify how the reasoning steps and implementation of the 'chain of thought' in their approach are fundamentally distinct from existing methods, rather than just a variation of prompt engineering.

W3. Instance-Aware Synthetic Example Generation: The authors assert that they introduce a "unique instance-aware synthetic example generation." However, the use of few-shot examples has already been explored in DIN-SQL and CodeS. Additionally, rather than synthesizing examples, it is often more straightforward to select existing examples from the training data. This raises the question: what advantages does synthesis offer over selection? Please provide empirical evidence or theoretical justification for why the proposed synthetic example generation approach outperforms or differs from simply selecting examples from training data. The paper should also clarify how its approach differs from existing methods that use training data for in-context learning, and why generating examples on-the-fly is superior to retrieving relevant examples based on question similarity.

- DIN-SQL: https://arxiv.org/abs/2304.11015
- CodeS: https://arxiv.org/abs/2402.16347

Next, let’s explore weaknesses from other aspects.

W4. Method Ensemble: The paper claims that ensembling multiple generated SQL paths is beneficial. However, it raises the question of why not include even more methods by incorporating readily available off-the-shelf solutions. The paper needs to justify the selection of the specific methods used and explain why adding more generators would not further improve performance, especially given the potential for diverse error patterns across different methods.

W5. Method Ensemble vs. Module Combination: In the reference titled "The Dawn of Natural Language to SQL: Are We Fully Ready?", a method for NL2SQL automated architecture search is discussed, which explores a predefined design space of NL2SQL solutions. This prompts a consideration of the pros and cons of coarse-grained method ensembles compared to fine-grained module ensembles. The paper should discuss the trade-offs between ensembling entire methods versus combining individual components of different methods, and why the chosen approach is more effective.

W6. Self-Consistency and Self-Reflection Methods: The authors propose self-consistency and self-reflection methods, yet both approaches have been extensively studied in the context of NL2SQL. Similarly, value retrieval and candidate generation techniques have been addressed in previous research, as noted in Table I of the aforementioned survey. The paper needs to clarify that these techniques are not novel contributions and focus on the unique aspects of their approach, such as the pairwise selector model.

W7. Algorithm 3 Execution Comparison: In Algorithm 3, the need to "compare both (ci, cj) and (cj, ci)" raises questions. Why is it necessary to evaluate execution results in both directions? Please provide a specific example or explanation of how comparing in both directions impacts the results or addresses potential biases in the selection process. The paper should elaborate on how this two-way comparison mitigates order bias in LLM selection.

W8. Experiments: The experimental results lack clarity regarding whether they stem from the capabilities of Gemini or the proposed framework. (1) If the benefits arise from the framework, the experiments should involve substituting Gemini with various LLMs to assess whether the framework enhances performance across different models. (2) The impact of ensembling different methods remains uncertain. (3) It is unclear how the proposed techniques individually compare to existing methods in areas such as value retrieval, candidate generation, and query fixing. Hence, the following experiments are important to enhance the experimental section:

- Conduct ablation studies comparing their framework with different LLMs.
- Provide a detailed analysis of the impact of ensembling different methods.
- Include comparisons of individual components (value retrieval, candidate generation, query fixing) against existing state-of-the-art methods for each task.

### Questions
Q1: The paper's novelty requires clarification, particularly in light of the concerns raised regarding the originality of its individual algorithms (see weaknesses W1, W2, and W3).

Q2: The technical contributions and key innovations compared to existing studies need to be clearly justified (refer to weaknesses W4 through W6).

Q3: The experimental design needs to be improved to more effectively verify the authors' claims (see weakness W8).

### Soundness
3

### Presentation
3

### Contribution
2
