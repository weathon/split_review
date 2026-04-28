# OpsEval: A Comprehensive Benchmark Suite for Evaluating Large Language Models’ Capability in IT Operations Domain

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 6, 8, 5

## Abstract
The past decades have witnessed the rapid development of Information Technology (IT) systems, such as cloud computing, 5G networks, and financial information systems. Ensuring the stability of these IT systems has become an important issue. Large language models (LLMs) that have exhibited remarkable capabilities in NLP-related tasks are showing great potential in AIOps, such as root cause analysis of failures, generation of operations and maintenance scripts, and summarizing of alert information. Unlike knowledge in general corpora, knowledge of Ops varies with the different IT systems, encompassing various private sub-domain knowledge, sensitive to prompt engineering due to various sub-domains, and containing numerous terminologies. Existing NLP-related benchmarks (e.g., C-Eval, MMLU) can not guide the selection of suitable LLMs for Ops (OpsLLM), and current metrics (e.g., BLEU, ROUGE) can not adequately reflect the question-answering (QA) effectiveness in the Ops domain. We propose a comprehensive benchmark suite, OpsEval, including an Ops-oriented evaluation dataset, an Ops evaluation benchmark, and a specially designed Ops QA evaluation method. Our dataset contains 7,334 multiple-choice questions and 1,736 QA questions. We have carefully selected and released 20% of the dataset written by domain experts in various sub-domains to assist current researchers in preliminary evaluations of OpsLLMs. We test over 24 latest LLMs under various settings such as self-consistency, chain-of-thought, and in-context learning, revealing findings when applying LLMs to Ops. We also propose an evaluation method for QA in Ops, which has a coefficient of 0.9185 with human experts and is improved by 0.4471 and 1.366 compared to BLEU and ROUGE, respectively. Over the past one year, our dataset and leaderboard have been continuously updated.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents the OpsEval benchmark for assessing LLMs in IT operations (Ops). Moreover, a new evaluation method for QA in Ops is also introduced. Over 24 LLMs are evaluated in the proposed benchmark.

### Strengths
1. Introduced a new benchmark containing 9070 questions to evaluate LLMs in IT operations. The proposed benchmark is also diverse as it covers 8 tasks and three abilities across various IT sub-domains. 

2. The proposed FAE-Score evaluation metrics that focused on fluency, accuracy, and evidence outperform other existing evaluation metrics in terms of alignment with humans.

3. Experiments were conducted over 24 LLMs to evaluate their capabilities and limitations in this benchmark with various prompting techniques, quantization, etc.

4. The authors also release a small subset of the OpsEval benchmark.

### Weaknesses
1. The open-source version is quite limited in size, which makes the contribution quite narrow in scope. 
2. The approach to select the 20% data is not discussed in the paper. 
3. The contribution in the paper is quite incremental. There are existing relevant benchmarks like NetOps and OWL. The authors claimed that their contribution in this paper in comparison to these existing benchmarks is the continuously updated leaderboard. This cannot be considered as a major contribution.
4. The data from real-world companies are also quite small in comparison to other domains like Wired network or 5g Communication. This makes the usefulness of the proposed benchmark for real-world practical scenarios quite limited. 
5. The technical contribution in the FAE metric is quite limited. It just seems a utilization/combination of various existing techniques. Also, the motivation behind using various techniques is not clearly demonstrated. For instance, why QWEN was selected to evaluate fluency in FAE?
6. The authors criticized ROUGE and BLEU in various sections of the paper, then why did they adopt a ROUGE based method in the FAE metric for evidence evaluation?
7. Moreover, there are also contextualized metrics like AlignScore or BERTScore. Therefore, why these metrics were not used as an alternative to ROUGE?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents OpsEval, where the authors extract questions related to IT operations from multiple sources, and after preprocessing, automated labeling, and expert review, they construct a dataset containing 9070 entries. During LLMs evaluation, the authors propose the FAE-Score to address the limitations of the rouge and bleu scores, demonstrating a high correlation with human evaluation. Additionally, the paper conducts extensive experiments to test the performance of various base LLMs across different prompt types, task categories, and languages, and analyzes the underlying reasons for the results.

### Strengths
- The paper introduces a novel dataset, filling the gap in benchmarks for the IT operations domain.
- This is a highly comprehensive piece of work. Each step, from dataset construction to LLMs evaluation, is thoroughly executed, including data labeling and experimental comparisons.
- The FAE-Score shows better results compared to existing evaluation metrics, with the potential to become a widely adopted metric.

### Weaknesses
 - There are some minor issues with the paper's writing. For example, the same figure appears twice on page 14.
- For one of the main innovations, the FAE score, the paper only provides a textual description, without a formal definition or concrete examples (e.g., keyword extraction and similarity search).

### Questions
1. Is there any plan to further explore and use Automated QA generation? This is a direction that holds significant potential for deeper exploration.
2. Regarding the fluency score, Figure 11 presents a total score of 12 points, but the expert rating is between 0-3. Is there a conversion process involved here?
3. How to prove that taking fluency and evidence into account is reasonable? For multiple-choice questions, answering correctly is the most important factor, but is it possible that the FAE-Score might give a higher score to a response that is very logical but incorrect?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper focuses on IT Operations (Ops) and proposes a comprehensive evaluation benchmark for operations-related large language models (OpsLLMs). The authors initiate a community, involving companies to address privacy challenges. They classify questions under this topic into well-defined categories, providing a dataset of 9,070 examples, with 20% made publicly available for research. Additionally, they introduce a new evaluation metric, FAE-Score, which demonstrates a higher correlation with scores given by human expert compared to traditional metrics like BLEU and ROUGE.

### Strengths
- The dataset includes a broad range of categories and question types, accommodating diverse testing setups such as chain of thought (CoT), self-consistency, and few-shot in-context learning.
- The questions and data are collected from the Ops community, reflecting real-world performance issues, making this dataset a valuable resource for researchers in AIOps.
- They propose the FAE-Score, which aligns more closely with human evaluations than BLEU or ROUGE.
- The paper has a clear structure, good writing skills and sufficient figures.

### Weaknesses
 - The evaluation could benefit more from an analysis of option bias, like testing whether altering the order of choices in questions impacts the results. This could provide insights into any unintended biases within the model and improve the robustness of the evaluation.

### Questions
N/A

### Soundness
3

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
3

### Summary
The paper introduces OpsEval, a comprehensive benchmark suite developed to evaluate the capabilities of large language models (LLMs) within the IT operations (Ops) domain. Addressing the need for domain-specific benchmarks, OpsEval encompasses a bilingual multi-task dataset containing 9,070 questions across eight tasks and three cognitive abilities. The benchmark features a novel QA metric, FAE-Score, which surpasses traditional metrics (e.g., BLEU, ROUGE) in alignment with expert evaluations. Results from evaluating over 24 LLMs reveal insights into their performance variability and highlight areas requiring targeted improvements for practical AIOps applications.

### Strengths
- **Novelty**: OpsEval is the first comprehensive, bilingual benchmark tailored to IT operations, filling a significant gap in LLM evaluation for this specialized domain.
- **Robust Evaluation Framework**: Introduction of the FAE-Score provides a more reliable assessment method for domain-specific QA, aligning closely with human expert evaluations.
- **Diverse Dataset**: The dataset covers a range of sub-domains and tasks, including multi-choice and QA questions that reflect real-world scenarios, enhancing its practical applicability.
- **Comprehensive Analysis**: The paper presents detailed insights into how different LLMs perform under varied prompting techniques and tasks, providing valuable information for future model improvements and fine-tuning.

### Weaknesses
 - **Generalizability Concerns**: While the dataset's scope is impressive, its applicability to other IT sub-domains or rapidly changing tech scenarios is not fully addressed. The benchmark's design, particularly the task definitions and evaluation metrics, may not adequately capture the nuances of specialized areas such as network security or cloud infrastructure management. Furthermore, the dataset's static nature raises concerns about its relevance in the face of evolving technologies and operational practices.
- **Real-time Adaptability**: The benchmark's utility for models operating in dynamic, real-time environments remains unexplored. The current evaluation framework focuses on static datasets and does not assess the models' ability to handle streaming data, adapt to changing conditions, or make decisions under time constraints, which are critical aspects of real-world IT operations.
- **Limited Focus on Advanced Reasoning**: Although analytical thinking is a category, the paper does not deeply explore how LLMs handle multi-step or complex reasoning tasks within the Ops context. The benchmark lacks tasks that require models to perform intricate problem-solving, such as diagnosing complex system failures or optimizing resource allocation based on multiple interdependent factors. The current tasks primarily assess surface-level understanding rather than deep analytical capabilities.
- **Dependence on Proprietary Data**: The inclusion of proprietary company data, although necessary, limits the benchmark's accessibility for broader research. The lack of transparency regarding the specific nature of this proprietary data and the anonymization process makes it difficult to assess the potential biases introduced and hinders the reproducibility of the results.

### Questions
1. How might OpsEval be adapted for use with real-time or continuously updated data sources?
2. Are there any plans to expand OpsEval to include tasks involving more intricate, multi-step reasoning?
3. What measures are taken to ensure that the benchmark’s results are not biased due to proprietary data contributions?
4. Could the authors provide further detail on the types of error analysis conducted for different models, particularly regarding common failure modes?

### Soundness
3

### Presentation
3

### Contribution
3
