# DataSciBench: An LLM Agent Benchmark for Data Science

- Decision: Reject
- Avg Score: 3.20
- Scores: 3, 3, 6, 3, 1

## Abstract
This paper presents DataSciBench, a comprehensive benchmark for evaluating Large Language Model (LLM) capabilities in data science.
Recent related benchmarks have primarily focused on single tasks, easily obtainable ground truth, and straightforward evaluation metrics, which limits the scope of tasks that can be evaluated. In contrast, DataSciBench is constructed based on a more comprehensive and curated collection of natural and challenging prompts. We develop a semi-automated pipeline for generating ground truth (GT) and validating evaluation metrics. This pipeline utilizes and implements an LLM-based self-consistency strategy to produce accurate GT by leveraging collected prompts, predefined task types, and aggregate metrics. Furthermore, it employs a careful approach to filter a high-quality Task - Function - Code (TFC) list and assess each code execution outcome within TFC based on precisely defined metrics and programmatic rules. Our experimental framework involves testing 6 API-based models, 8 open-source general models, and 9 open-source code generation models using the diverse set of prompts we have gathered. Through this approach, we aim to provide a more comprehensive and rigorous evaluation of LLMs in the domain of data science, shedding light on their strengths and weaknesses. Experimental results demonstrate that API-based models greatly outperform open-sourced models on all metrics except for VLM-as-a-judge and Deepseek-Coder-33b-instruct achieves the highest score among open-sourced models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces DataSciBench, a novel benchmark for evaluating the performance of large language models (LLMs) on data science tasks. The authors propose a semi-automated data collection pipeline, complemented by filtering and expert review for data quality. DataSciBench includes 222 data science tasks of 6 task types. Comprehensive evaluation over 6 API-based models and 17 open-sourced models show that DataSciBench is challenging to even the best LLMs.

### Strengths
1. This work presents a new benchmark dataset for evaluating LLMs on data science tasks, which is a meaningful contribution to the community.
2. The benchmark covers representative task types in data science, from data processing to data mining and report generation.
3. The evaluation setup includes popular open-sourced and proprietary LLMs.

### Weaknesses
While this work has the potential to contribute a valuable benchmark to the community, several key issues need to be addressed:
1. The semi-automated pipeline uses a self-consistency strategy to generate ground truth for a portion of the tasks. However, there lacks detail on further quality control. Also, I think the difficulty and authenticity of model generated tasks is questionable. **Specifically, the fact that ground truth programs are generated using self-consistency decoding implies that existing models are already capable of solving these tasks. This raises concerns about the novelty and challenge presented by DataSciBench, potentially limiting the insights that can be derived from evaluating models on it.**
2. DataSciBench employs instance-specific evaluation scripts that are both generated and verified by LLMs. The quality measure of evaluation functions needs more elaboration.
3. As the author noted in section 5.3, DataSciBench shows a high correlation with LiveCodeBench and BigCodeBench. I personally see this as a negative of the proposed benchmark. Why do we need a benchmark that correlates well with existing ones?
4. It is unclear to me what is the motivation for introducing the Task-Function-Code (TFC) list data structure and how is it a significant contribution. Is there a baseline method that TFC outperforms?
4. The writing of this paper is often hard to follow, lacking elaboration on a lot of key details:
    - Section 3.2, Question Filtering: what are all the keywords for principle (1)? What does "questions that align with human preferences and LLMs" (line 200) mean?
    - Section 3.2, Expert Review: stage 1, what does "easy to evaluate" (line 204) mean? In stage 2, what does "unified instructions" refer to?
    - Details on metrics lacks elaboration (see below)
    - Section 5.1, how is "performance variance" measured? What are the values for API-based and open-sourced models?
    - Section 5.2, how many tasks are there in each difficulty level? How do you define "consistent performance" (line 417-418)?
    - Section 5.3, how do you define if performance of two datasets "mismatch" (line 431)? Also, the scale of x and y axes of Figure 5 is not matched. Then, what is the dashed blue line? How does it help establish the insight?
    - Section 6.2, what are the "characteristics of data science tasks" (line 518-519)? What are the "relatively simple data analysis operations" (line 526-527)? Further elaboration is needed to distinguish DataSciBench from existing benchmarks.
5. The fine-grained metrics in Section 4.2 need further justification:
    - VLM-as-a-judge: Which VLM is used for judgement? What is the "predefined criteria" (line 319-320)? A reasonable evaluation or reference is needed to justify this metric.
    - Plot Validity: why checking the shape of the matrix can evaluate the quality of plot?
    - Data Accuracy: how exactly is mean square error measured? Is the output of corresponding tasks normalized to a specific format?
    - Visualization completeness: What does "checking their existence" mean? If it refers to checking the existence of the output file, I am afraid it is merely a necessary condition for task success and can not measure the quality of the output plot.
    - Model Accuracy: When is boolean output or decimal used? Why and how can they be unified into a single metric?
    - Relatedly, in Table 2, what is the "Score" column? Is it an aggregation of all fine-grained metrics (of different type)? How is it calculated?

### Questions
My main question have been listed in weaknesses.

### Soundness
1

### Presentation
1

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
This paper presents a novel benchmark named DataSciBench for evaluating LLMs to assess LLMs data science capabilities on complex tasks. It highlights the main drawbacks of previous works: a lack of task diversity, easily obtainable ground truths, and simplistic evaluation metrics. To address these issues, this new benchmark introduces a semi-automated LLM-based pipeline called Task - Function - Code (TFC), which generates ground truths and evaluation metrics for each subtask. They evaluated six APIs, eight open generation models, and nine open-source code generation models.

### Strengths
•	This paper is timely, as there have been considerable discussions about current evaluations becoming overly simplistic for modern LLMs.

•	The study is fairly comprehensive, featuring a large evaluation body over various data science tasks, testing across six APIs, eight open generation models, and nine open-source code generation models.

•	A new benchmark is appreciated, especially when well-motivated. Some readers may find the new insights from Section 5.1/5.4 valuable. It is indeed rather surprising that StarCoder2/ CodeLlama performed so poorly.

### Weaknesses
•	The primary motivation behind this paper is the observation that existing research often relies on easily obtainable ground truths and straightforward evaluation metrics on LLM’s data science capabilities. The authors surmise that existing benchmarks are lacking as they focus on “narrower tasks” and “with easy to obtain ground truth and straightforward evaluation metrics” (line 045-051). But the examples given, eg MLAgentBench and SWE-Bench does not seems to be particularly “narrow”. Also, easy to obtain ground truth and straightforward evaluation metrics may not always be a bad thing as sometimes they specifically measure a more direct performance of the models. 

•	The broad, complex data science concepts that this paper is trying to address are neither easy to define nor quantify.  It is unclear if this paper (as presented in its current form) has addressed the issues appropriately.  The underlying requirements of the benchmark, as set out by the authors in Lines 067-070, about “naturalness”, “challenging”, “multi-hop reasoning”, and “diversity of result types”, were not specifically addressed in the subsequent design of the benchmark and its metrics.  The various fine-grained metrics seemed to still be rather narrow and “straightforward”, and it was not explained how these metrics were calculated for complex data science tasks that this study aims to benchmark.  

•	It was unclear if their proposed benchmark is indeed be more sophisticated and trustable/higher-quality than previous works, as there were no comparisons with the related works on data science benchmarking. I was hoping for an in-depth discussion/establishment of the motivation of this benchmark. What sets this benchmark aside from the existing code benchmarks precisely? What exactly are the limitations of the existing code benchmarks that is covered by the DataSciBench?

•	Extensive experiments results on both open and closed source models on the proposed benchmark were provided.  While the insights may also be useful, they are not particularly surprising, as they mainly reinforce the idea that larger, closed-source models generally perform better compared to the evaluated open-source models. The insight from StarCoder2/CodeLlama mentioned in Section 5.1/5.4 is useful but the reasoning behind why it performs badly lacks empirical evidence to support it.

•	In terms of presentation, the missing/vague definitions of key components have made the paper hard to follow, which also raises doubts on the rigor and soundness of the study. For example, “data science” is a broad term, and the main paper did not provide and define the list of data science capabilities that it is aiming to benchmark, and how they can be quantified.  The main algorithm, Task-Function-Code (TFC) list, was presented abruptly.  What is “Function” with respect to “Task”?  Since “Code” a key component, then shouldn’t we also consider the coding ability of LLMs?  What do “Data Interpreter”, “Aggregate Function”, and “Programmatic Rules” in Figure 1 represent?  The six typical data science tasks were key to the study but they were “defined” in a very broad and subjective manner.  Similar issues for task integration, question filtering, and expert review.  Who are the experts?  How did they actually review the questions? These key concepts should be defined and explained clearly in the main body of the paper instead of relying on the readers to try to figure out by the examples in the Appendix later.   Moreover, the ablation study on tasks with different difficulty levels is not well-motivated or clearly defined. Although the authors categorize tasks as easy, medium, or hard, they do not adequately explain the criteria for these classifications or who is responsible for making these decisions.

### Questions
•	What is the main difference between the coarse-grained metrics presented in this paper and the techniques in Hong et al. (2024) and Chen et al. (2021)? Are the authors applying the concepts from Hong et al. (2024) and Chen et al. (2021) in a different domain? The Success Rate (SR) introduced by Chen et al. (2021) is used to evaluate models for code generation. In line 514, the authors mention that data science evaluation is closely related to code generation. How does one evaluate an LLM’s data science capability instead of its coding ability?

o	(Chen et al. (2021)) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374, 2021.

o	(Hong et al. (2024)) Sirui Hong, Yizhang Lin, Bangbang Liu, Binhao Wu, Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang, Lingyao Zhang, Mingchen Zhuge, et al. Data interpreter: An llm agent for data science. arXiv preprint arXiv:2402.18679, 2024.

•	Could you explain the expert review process in detail?

•	A few more detailed questions:

o	Line191-192: what were the requirements used? 

o	Line 193: what were the few-shot example used? Where did you get the examples? Do you change the few-shot every time you prompt the LLM?

o	Line 240-241: What is the percentage of prompts you used from BigCodeBench? For self-consistency strategy, as it does not guarantee correctness but only improves it, do you use any post generation strategy to ensure that the code you obtain under this is accurate?

o	Table 2: Any insight on why does CodeLama-13b-Instruct outperforms the rest on VLM by a large margin but is poor in the other metrics?

### Soundness
1

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
The paper presents DataSciBench, a comprehensive benchmark for assessing large language models (LLMs) in data science applications. DataSciBench includes 6 task types: data cleaning and preprocessing, data exploration, data visualization, predictive modeling, data mining, and report generation. The authors also propose a semi-automated Task-Function-Code (TFC) framework, which assesses model performance from coarse-grained (e.g., completion and success rates) to fine-grained (e.g., data quality scores, visualization completeness) perspectives. The evaluations of 23 models show that API-based models (especially GPT-4o) consistently outperform open-source models. The benchmark sheds light on challenges for LLMs in handling complex, multi-step data science tasks and provides insights into their strengths and limitations in this domain.

### Strengths
1. This paper presents DataSciBench, a comprehensive benchmark for assessing large language models (LLMs) in data science applications. I looked at several questions in the attached zip file. The questions are indeed complex enough. Figure 5 / Table 3 provides evidence for data contamination risks and correlation with LiveCodeBench and BigCodeBench.

2. The authors propose a semi-automated Task-Function-Code (TFC) framework to generate ground truth and obtain evaluation metrics for each subtask and for both coarse-grained and fine-grained perspectives.

3. The authors did extensive experiments including 23 models, ranging from API-based (closed-source), open-sourced general, and open-sourced code generation models. GPT-4o still leads the leaderboard, which is not surprising. But it's good to see performance among various models on DataSciBench and the low performance of hard level examples, which can help recognize the challenges in complex multi-hop reasoning.

4. The paper is well-written and easy to follow.

### Weaknesses
1. It's good to see such a comprehensive benchmark for data science released, but it seems somewhat trivial to me for collecting existing prompts in BigCodeBench or LLM-synthesized instructions. Essentially, what's the biggest difference between DataSciBench and previous code benchmarks for data science?

2. The ground truths were generated by LLMs via self-consistency, which might contain false positive ground truths.

3. The experimental analysis part concludes the overall performance (closed-sourced > open-sourced), the difficulty ablation, and non-contaminated as well as correlations with other two code benchmarks. However, for the insights part, the paper dies not give many details about how models fail on such coding tasks, typical error cases, and how to potentially improve models to solve these issues?

### Questions
1. Sorry if I missed it, but seems the paper does not mention the total example numbers in DataSciBench?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces DataSciBench, a benchmark aimed at evaluating the capabilities of Large Language Models (LLMs) in data science tasks. It targets more comprehensive assessment by utilizing complex, more detailed, multi-faceted prompts that involve data cleaning, data analysis, visualization, pattern matching, etc. For evaluation, the authors introduce a semi-automated Task-Function-Code (TFC) pipeline for generating ground truth codes/outputs and evaluating agent performance using LLMs. The benchmark tests six API-based models, eight general open-source models, and nine open-source code generation models, with the key conclusion or insight being API-based models tend to outperform open-source ones.

### Strengths
1. **Comprehensive Experiments**: The design of DataSciBench is comprehensive, encompassing multiple facets of data science tasks with varied complexity levels and multiple open- and closed-source models. 
2. **Empirical Evaluation**: The semi-automated evaluation approach provides a unified and granular evaluation.

### Weaknesses
1. **Limited Significance**: While DataSciBench claims to assess data science abilities, the paper does not provide enough evidence that the chosen tasks reflect realistic data science challenges. Real-world data science often requires domain knowledge, iterative hypothesis testing, and adaptability to complex, often messy datasets. In contrast, the tasks presented here appear to lack such depth, instead focusing on simpler, predefined tasks that may not mirror the complexity of real data science workflows.
2. **Overly Detailed Task Prompts**: It seems that task prompts provide step-by-step instructions. This makes the setting simpler guiding the model through the steps rather than requiring it to reason through the steps on its own. This detailed prompt shifts the evaluation focus toward correct code generation rather than genuine reasoning and problem-solving, which undermines the goal of assessing data science capability in LLMs. An effective data science benchmark should evaluate a model’s ability to break down complex tasks independently.
3. **Insufficient Transparency in Task Selection**: The selection criteria for the included tasks and prompts are not well-defined. It’s difficult to assess how representative these tasks are of the real-world data science landscape. Some tasks seem too rudimentary, raising questions about the intended difficulty level and relevance for LLM agents. The paper would benefit from explicitly discussing how these tasks align with the challenges data scientists face in practice.
4. **Lack of Experiments with Larger Models**: The paper does not include experiments with larger models (e.g., 13B or 70B parameters), which limits the benchmark’s insights into how model size impacts performance on complex data science tasks. Larger models are typically more capable of handling nuanced reasoning, making them essential for assessing benchmark robustness. 
5. **Inadequate Novelty**:  This work relies heavily on straightforward prompt generation and LLM validation techniques, much like previous code generation benchmarks. The benchmark introduces no fundamentally new types of task paradigms or significant results/insights that would justify its focus as a new data science-specific benchmark. 
6. **Poor Quality Control**: The semi-automated ground truth generation process raises concerns about quality and reliability. Self-consistency verification without extensive human oversight risks introducing erroneous ground truths, especially for complex tasks.

### Questions
See weaknesses.

*Minor*:
1. Could you update Table 1 to add the domain and number of tasks for a more holistic comparison of this work w.r.t previous works?
2. In tasks where the prompt outlines the solution steps, how do you account for the model’s independent reasoning capability as part of its evaluation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces DataSciBench, a new benchmark designed to evaluate the capabilities of LLMs in data science tasks. It addresses limitations of existing benchmarks by focusing on complex, multi-task scenarios with challenging prompts. The authors develop a semi-automated pipeline for generating ground truth and validating evaluation metrics, called Task-Function-Code (TFC). The study tests 23 models, including API-based and open-source models, revealing that API-based models generally outperform open-source ones.

### Strengths
None.

### Weaknesses
1. The writing of this manuscript is not clear and extremely hard to follow. For example, it is unclear to me what the tasks are, how many samples are there in the benchmark, and how does the TFC work, etc. The authors may consider re-write the manuscript, and add some examples of the samples for better comprehension.
2. The benchmark seems not novel. There exist many "data science" or coding-related benchmarks for LLMs. The authors claim that previous studies "focusing on single tasks, simplistic evaluation metrics, and readily available ground truth", which lacks citations and discussion. The complexity and necessity of this new benchmark are not convincingly demonstrated.
3. Although the evaluation includes numerous models, it lacks depth in insights. A more detailed analysis, such as examining model performance across different question types, could reveal knowledge and reasoning disparities among models.

### Questions
1. How does the TFC work? Why is it necessary?
2. How do the authors ensure the correctness of the generated ground truth, even if the so-called test cases pass? If the ground truth can be easily obtained by just generation and rule-based verification, the tasks may be very easy and straightforward. Then, what is the value of this benchmark?

### Soundness
1

### Presentation
1

### Contribution
1
