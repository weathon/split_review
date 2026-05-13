# ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Recent advancements in integrating large language models (LLMs) with application programming interfaces (APIs) have gained significant interest in both academia and industry. These API-based agents, leveraging the strong autonomy and planning capabilities of LLMs, can efficiently solve problems requiring multi-step actions. However, their ability to handle multi-dimensional difficulty levels, diverse task types, and real-world demands through APIs remains unknown. 
In this paper, we introduce \textsc{ShortcutsBench}, a large-scale benchmark for the comprehensive evaluation of API-based agents in solving tasks with varying levels of difficulty, diverse task types, and real-world demands. \textsc{ShortcutsBench} includes a wealth of real APIs from Apple Inc.'s operating systems, refined user queries from shortcuts, human-annotated 
high-quality action sequences from shortcut developers, and accurate parameter filling values about primitive parameter types, enum parameter types, outputs from previous actions, and parameters that need to request necessary information from the system or user.
Our extensive evaluation of agents built with $5$ leading open-source (size >= 57B) and $4$ closed-source LLMs (e.g. Gemini-1.5-Pro and GPT-3.5) reveals significant limitations in handling complex queries related to API selection, parameter filling, and requesting necessary information from systems and users. These findings highlight the challenges that API-based agents face in effectively fulfilling real and complex user queries.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a comprehensive, large-scale benchmark designed to evaluate API-based agents in real-world scenarios. It addresses the shortcomings of existing benchmarks and datasets, which often lack the richness and complexity needed to thoroughly assess different LLM-based agent models. To overcome these limitations, the authors have developed a high-quality benchmark encompassing 88 applications, 1,400 APIs, and an average of 21 actions per API, each covering various aspects of real-world deployments.

In the evaluation, the authors tested 10 LLMs on several key tasks: API selection, parameter filling, and the models' ability to recognize when to request additional input from either the system or the user. The experimental results show interesting insights, such as the challenges these models face with multi-step reasoning and understanding when external input is necessary.

### Strengths
This paper makes a notable contribution by creating a comprehensive benchmark for API-based agents, utilizing data extracted from Shortcuts. Compared to other API-based benchmarks, it offers several benefits, including a focus on the agents' ability to request necessary input from either the assistant or user and diverse difficulty of tasks. It covers a range of tasks, from simple ones to those involving complex APIs, queries, and action sequences. Additionally, the paper ensures quality by involving human verification, with shortcut developers serving as annotators.

The evaluations demonstrate insightful findings, especially regarding the challenges agent models face in reasoning and planning capabilities as indicated by API selection, as well as the difficulties weaker LLMs encounter in API parameter filling. These insights are valuable for the development of more advanced agent models.

### Weaknesses
1. Although the paper emphasizes that the benchmark includes high-quality human-annotated action sequences from shortcut developers and queries derived from real user demands, it only mentions the shortcut developers are our annotators. Further details in this area would be beneficial.

2. In section 3.2, the paper describes using GPT-4o to simulate user queries. However, it would be helpful to include the steps taken to verify the correctness and ensure the diversity of these user queries.

3. The evaluation primarily features selected proprietary models like GPT-4o and Gemini. For open-source LLMs, it mainly compares with general LLMs such as Qwen-2-70B and LLaMA-3-70B. Considering comparisons with more robust, specifically developed AI Agent models such as AgentLM (70B from https://github.com/THUDM/AgentTuning) and xLAM (8x7b or 8x22b from https://github.com/SalesforceAIResearch/xLAM) could provide more insights.

4. The source of the reported numbers in Table 1 could be more clearly specified. There is uncertainty regarding whether models like Qwen-2.5-7B and LLaMA-3-8B consistently achieve more than 90% on ToolBench and over 80% on ToolLLM. Furthermore, given that MetaTool (https://github.com/HowieHwong/MetaTool) does not provide comprehensive details or code for model evaluation and metrics, more information is necessary to verify the accuracy of the table data.

### Questions
Please refer comments in above fields.

### Soundness
4

### Presentation
4

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
This paper introduces a new benchmark ShortcutsBench, which evaluates agents' capabilities in solving tasks through API calling. They compare multiple API-based benchmarks, and showcase why ShortcutsBench contributes to the assessing agents' API calling abilities. The paper evaluates several API-based agents constructed based on the ReACT framework. The authors perform detailed analysis on the evaluation results.

### Strengths
- The authors introduce ShortcutsBench, which is a more holistic benchmark that contains real APIs, well-designed queries and actions. This could contribute to better evaluation of current agents's API calling capabilities in solving real-world tasks.
- The authors provide example instances from ShortcutsBench in the appendix, which helps understanding the types of tasks in this benchmark.
- The authors provide detailed analysis based on the evaluation results of several API-based agents.

### Weaknesses
 - Section 3 is not well-elaborated. readers will benefit from clearer description of this process. For example, for (2), the authors say 'after duplicating based on icloud link, ....', it is not very clear what is duplicated and why this step helps. It would be good if the authors could refine their descriptions on their methodology.
- The authors cite each work too many times in the paper, for example, a research paper is is cited five times in one paragraph in Section 2. Referencing previous works is good practice, but referencing too many times affects readability. It would be good if they could remove repetitive references.
- The paper does not make it very clear what is their most important finding in the abstract/intro/conclusion. It would be good if they could highlight their most important findings in the abstract/intro/conclusion. For example, they could discuss how open source models perform comparably to closed source models on simpler tasks but not harder tasks.

### Questions
- Why is all API-based agents the authors evaluate based on the ReACT framework, it would be good if they could provide additional evaluation/analysis on other frameworks, such as CodeAct.

### Soundness
3

### Presentation
2

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
This paper introduces ShortcutsBench, which mines real-world APIs/action sequences from iOS shortcut app. They then synthesize tasks with language model, and test a range of model's ability on it. Results show the task remains challenging to today's LMs.

### Strengths
- Interesting approach: mining APIs/existing action sequence from Shortcut Apps makes a lot of sense, which is a resource previous works haven't tapped into.
- Comprehensive evaluation: the authors evaluated a wide range of LMs across Open and close source models.

### Weaknesses
1. Limited evaluation: The paper primarily assesses the model’s ability to choose correct actions based on ground-truth sequences but doesn’t evaluate its end-to-end task success rate (as done in, for example, AppWorld [1]). Experiments linking these aspects are missing.
2. No human validation: Given the synthetic nature of the benchmark, it’s uncertain whether all tasks are truly solvable or what the benchmark’s upper bound is. Including human performance as a reference would add clarity.

### Questions
1. A notable feature of this benchmark seems to be scalability -- extracting real-world APIs and action sequences from Shortcut apps and sharing sites seems relatively easy. Providing quantitative details on dataset construction—such as time taken for each step and the actual extent of manual effort involved—would be nice.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces ShortcutsBench, a benchmark to assess LLMs’ ability to call external APIs and create structured text (ex: JSON). The dataset was collected from the Shortcuts tool available on Apple devices. The authors perform the analysis of performance of a number of open and closed-source LLMs against ShortcutsBench.

### Strengths
[1] Analysis results in 4.2 are insightful and confirm the ranking of closed- and open-source LLMs on traditional general knowledge and reasoning benchmarks like MMLU.

[2] The artifacts are provided and well-organized.

### Weaknesses
[1] It is a technical report that lacks a scientific component. It should go to a software engineering conference, for example, International Conference on Software Engineering (ICSE) or IEEE/ACM International Conference on Automated Software Engineering (ASE). The paper can also go to Datasets and Benchmarks tutorials at AI conferences. Whereas the work is technically impressive and valuable for the software engineering community, there is no scientific value in the assessment of how good LLMs are able to use APIs. The problem at hand is purely technical and as a clear indicator for this is that over two thirds of references are links to web pages rather than scientific studies.

[2] The analysis of the performance of GPT 4o with the structured output capability was not performed.
https://openai.com/index/introducing-structured-outputs-in-the-api/

[3] The used language appeals to emotions rather than states the scientific value (ex: “We made great efforts to evaluate…”).

[4] Several references are outdated, pointing to arxiv whereas the paper has been already published at a conference (ex: ToolLLM).

### Questions
I suggest to submit to a more relevant conference, rather than to ICLR, as mentioned above.

### Soundness
2

### Presentation
2

### Contribution
3
