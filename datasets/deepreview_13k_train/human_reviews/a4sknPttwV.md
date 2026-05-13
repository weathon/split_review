# DCA-Bench: A Benchmark for Dataset Curation Agents

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
The quality of datasets plays an increasingly crucial role in the research and development of modern artificial intelligence (AI). Despite the proliferation of open dataset platforms nowadays, data quality issues, such as insufficient documentation, inaccurate annotations, and ethical concerns, remain common in datasets widely used in AI. Furthermore, these issues are often subtle and difficult to be detected by rule-based scripts, requiring expensive manual identification and verification by dataset users or maintainers. With the increasing capability of large language models (LLMs), it is promising to streamline the curation of datasets with LLM agents. In this work, as the initial step towards this goal, we propose a dataset curation agent benchmark, DCA-Bench, to measure LLM agents' capability of detecting hidden dataset quality issues. Specifically, we collect diverse real-world dataset quality issues from eight open dataset platforms as a testbed. Additionally, to establish an automatic pipeline for evaluating the success of LLM agents, which requires a nuanced understanding of the agent outputs, we implement a dedicated Evaluator using another LLM agent. We demonstrate that the LLM-based Evaluator empirically aligns well with human evaluation, allowing reliable automatic evaluation on the proposed benchmark. We further conduct experiments on several baseline LLM agents on the proposed benchmark and demonstrate the complexity of the task, indicating that applying LLMs to real-world dataset curation still requires further in-depth exploration and innovation. Finally, the proposed benchmark can also serve as a testbed for measuring the capability of LLMs in problem discovery rather than just problem-solving.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to solve the detection of data quality issues such as data errors, documentation issues, file discrepancies, and legal/ethical risks. This study of this paper starts from curating 221 test cases from eight popular dataset publishing platforms (like HuggingFace, Kaggle) and propose an automatic evaluation framework using GPT-4. It is interesting to know that without any hints, a baseline GPT-4 Curator agent can only reveal 11% of the data quality issues in the 221 test cases. When given the most specific hint, 70% of the issues can be detected.  This is understandable because finding the hidden issues of data quality is a complex task, even for human experts like dataset users and platform maintainers.

### Strengths
S1: the exploration of data quality issues is an interesting and important problem. If LLMs are able to automate the detection of data quality issues, they will be helpful for automatic maintenance of data publishing platform.
S2:  The dataset collection process seems reasonable. Four different types of issues are annotated, representing the typical issues that may happen in public data platforms.
S3: The evaluation system leverages LLMs in multiple perspectives for implementing different evaluation strategies, using RAG, code interpreter to write and execute programs, etc.

### Weaknesses
W1: the Evaluator is designed to leverage LLMs as judges for assessing whether the detection results are correct or not. However, as authors mentioned:  the annotated test data for the Evaluator are collected after the prompt design for the Evaluator. This raises concerns that the test data may simply align with the designed prompts, potentially indicating that the Evaluator’s performance is optimized for this specific data. This brings into question  about how  the proposed prompt design of the Evaluator can generalize across different Curators and issues in the DCA-Bench.

W2: The performance of the system in identifying dataset quality issues appears to have been evaluated solely on datasets that are known to have issues. It is currently unclear how the system performs on high-quality datasets where no issues are present. This raises concerns about its ability to avoid false positives in scenarios where no data issues exist.

### Questions
Are high-quality datasets included in the evaluation process? How about false positives (i.e., incorrect identification of issues in clean datasets) if using the proposed detection models.

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
2

### Summary
The work introduces a benchmark aimed at evaluating the ability of large language model (LLM) agents to autonomously detect subtle data quality issues in large, real-world datasets.

The work addresses the ongoing challenges in maintaining data quality on open platforms, where issues like mislabeling, documentation gaps, and ethical concerns are prevalent.

DCA-Bench comprises 221 real-world test cases across eight major dataset platforms and employs an automatic evaluation framework using GPT-4 to assess the performance of LLMs as dataset curators.

### Strengths
- The work addresses a significant problem in AI, as dataset quality is critical for robust model performance and reliable research outcomes.
- The work provides a foundation for future research into fully autonomous dataset curation systems, which could save time and reduce errors in data management.
- The framework offers different hint levels to evaluate LLMs at multiple stages of problem discovery, providing nuanced insights into model capabilities.
- DCA-Bench constructs an automatic evaluation pipeline: leverages GPT-4 to automate evaluations, which aligns well with expert human assessments, making the process scalable and consistent.

### Weaknesses
 - There is a lack of a fully realistic testing environment. While comprehensive, the test cases may not fully represent the diversity of data quality issues encountered in real-world curation. The reliance on simplified scenarios might not capture the complexities and nuances of real-world datasets, potentially limiting the generalizability of the findings.
- Performance is heavily dependent on hints. Without hints, the baseline LLM agent detected only 11% of issues, indicating a limited ability to autonomously identify dataset problems. This suggests that the LLM's capacity for independent reasoning and problem-solving in data quality assessment is quite constrained, raising questions about its practical utility in fully autonomous settings.
- The automatic evaluation pipeline, while effective, may introduce subtle biases that differ from nuanced human judgment. The use of GPT-4 for evaluation, while scalable, might not fully replicate the depth and context-awareness of human expert analysis, potentially leading to discrepancies in the assessment of data quality issues.

### Questions
The benchmark is primarily text-focused, will the benchmark be scalable to multimodal data (e.g., image or audio datasets)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a Dataset Curation Agents Benchmark to evaluate the ability of LLM agents to identify hidden data quality issues in community-contributed datasets. Focusing on the challenge of detecting undocumented issues rather than solving known problems, this benchmark uses 221 real-world test cases from popular dataset platforms and an automatic evaluation framework utilizing GPT-4, with alignment to expert evaluations. Initial results indicate a baseline GPT-4 Curator detects only a small percentage of issues, underscoring the complexity and need for further research in autonomous dataset curation.

### Strengths
1. Innovative Concept: The paper presents a novel approach by shifting focus from issue-solving to issue-discovery in dataset curation.
2. Comprehensive Coverage: DCA-Bench provides a broad testing ground with diverse curated test cases, representing real-world scenarios across different platforms.
3. Automatic Evaluation Framework: The use of GPT-4 for evaluation is a practical advancement, offering scalability where human annotation is not feasible.
4. Clear Practical Relevance: Tackling hidden data quality issues addresses a significant gap in dataset management, which is crucial for improving AI research outcomes.

### Weaknesses
1.	Limited Test Set Size: With only 221 samples, and limited instances in some categories (e.g., only 10 ethical instances), the test set might not sufficiently capture the complexity of real-world data quality issues. Increasing the dataset size and diversity could improve robustness.
2.	Missing Related Works: The paper does not adequately engage with existing literature regarding data system and LLM agents, such as [arXiv.2402.02643, LLM-Enhanced Data Management], [SIGMOD’24, Data-juicer: A one-stop data processing system for large language models], and [ICML'24, DS-Agent: Automated Data Science by Empowering Large Language Models with Case-Based Reasoning], which could provide valuable context and highlight the novelty of this work.
3.	Clarity Issues and minor writing suggestions: There are several presentation issues, such as missing references to Figure 1 in the text and unclear definitions in Table 1 for sample-level, type-level, and tag-level insights. Addressing these could enhance readability and comprehension. Beside, Line 104-105 lacks a “:” Line 213~214 lacks the references of “Kaggle、OpenML、TF-Dataset、Open-Data-Registry, Five-Thirty-Eight”.
4.	Applicability to different types of datasets: only eight open data set platforms have been mentioned, but there is a lack of analysis on whether different types of data sets (such as medical data, financial data, etc., have special properties) are equally applicable. It is recommended to add discussion or preliminary experimental results to demonstrate the versatility of DCA-Bench.

### Questions
None, plz see the weakness above

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel benchmark for assessing the capability of LM-based curator agents in identifying potential issues within datasets. The authors also streamline the evaluation process, enabling non-expert usage. Baseline evaluations conducted with GPT-4 demonstrate the system’s performance and highlight the potential value of their autonomous dataset curation approach.

### Strengths
1. This paper establishes a complete curation agent benchmark derived from real-world datasets, providing test cases ranging from easy to challenging, and potentially can be serve as an important foundation in this area.
2. The paper is well-organized, presenting a clear workflow of the proposed method alongside some demonstrations that effectively validate the robustness of the evaluation framework.

### Weaknesses
From my perspective, this paper presents the following limitations:
1. The benchmark appears to rely primarily on data sources from machine learning engineering, with a limited number of test cases. This raises questions about its generalizability to other domains, such as image datasets. Specifically, the current benchmark lacks diversity in data types and problem contexts, focusing mainly on tabular or text-based data common in ML engineering. The absence of image, audio, or time-series data limits the benchmark's applicability to a broader range of real-world scenarios. Furthermore, the limited number of test cases within the ML engineering domain itself may not fully capture the variety of issues that can arise in practice.
2. While the work presents a well-defined benchmark with a structured testing procedure, it largely resembles a series of experiments conducted with GPT-4 rather than a comprehensive agent-testing framework. The experiments on more agents are insufficiently thorough. The evaluation seems to be heavily reliant on a single LLM, GPT-4, without sufficient exploration of other agent architectures or methodologies. This raises concerns about the robustness of the findings and the potential for bias towards the specific capabilities of GPT-4. The paper lacks a systematic comparison across different types of agents, including those using different reasoning mechanisms or tool-use strategies. The experiments should include a more diverse set of agents to validate the generalizability of the benchmark.
3. The paper does not provide open-source code.

### Questions
Can your method be effectively applied to other domains, such as image datasets like ImageNet? Do you intend to make the benchmark publicly available?\
\
\
Additional: \
Pointing out an issue with your paper’s formatting: typically, one page contains around 53 lines of content, but your paper only has 46 lines, like page 1.

### Soundness
2

### Presentation
3

### Contribution
3
