# ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
The advancements of language language models (LLMs) have piqued growing interest in developing LLM-based language agents to automate scientific discovery end-to-end, which has sparked both excitement and skepticism about their true capabilities. % the true capabilities of such agents.
In this work, we call for rigorous assessment of agents on individual tasks in a scientific workflow before making bold claims on end-to-end automation.
To this end, we present \bench, a new benchmark for evaluating language agents for data-driven scientific discovery. 
To ensure the scientific authenticity and real-world relevance of our benchmark, we extract 102 tasks from 44 peer-reviewed publications in four disciplines and engage nine subject matter experts to validate them.
We unify the target output for every task to a self-contained Python program file and employ an array of evaluation metrics to examine the generated programs, execution results, and costs.
Each task goes through multiple rounds of manual validation by annotators and subject matter experts to ensure its annotation quality and scientific plausibility. 
We also propose two effective strategies to mitigate data contamination concerns.
Using our benchmark, we evaluate five open-weight and proprietary LLMs, each with three frameworks: direct prompting, OpenHands CodeAct, and self-debug. 
Given three attempts for each task, the best-performing agent can only solve 32.4\% of the tasks independently and 34.3\% with expert-provided knowledge.
In addition, we evaluate OpenAI o1 with direct prompting and self-debug, which demonstrates the effectiveness of increasing inference-time compute.
Still, our results underscore the limitations of current language agents in generating code for data-driven discovery, let alone end-to-end automation for scientific research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces ScienceAgentBench, a new benchmark designed to test how well language agents can handle tasks in data-driven scientific discovery. The authors collected 102 tasks from 44 peer-reviewed papers across four scientific fields: Bioinformatics, Computational Chemistry, Geographical Information Science, and Psychology & Cognitive Neuroscience. Each task asks the agents to write self-contained Python programs to perform specific scientific activities like data processing, model development, analysis, and visualization.

To ensure the tasks are authentic and to prevent issues with data contamination, the authors involved experts from the respective fields and modified datasets so agents couldn't rely on memorized code. They evaluated five large language models using three different frameworks: direct prompting, OpenHands, and self-debug. The results showed that the best-performing agent could complete only about one-third of the tasks. This highlights the current limitations of language agents in fully automating data-driven scientific discovery and suggests that more advancements are needed.

### Strengths
The paper introduces ScienceAgentBench, a novel benchmark for evaluating language agents in data-driven scientific discovery tasks. By incorporating tasks from four diverse scientific disciplines—Bioinformatics, Computational Chemistry, Geographical Information Science, and Psychology & Cognitive Neuroscience—it creatively applies language agents to new domains, filling a gap where existing benchmarks fall short.

The benchmark is rigorously developed with input from nine subject matter experts, ensuring tasks are authentic and challenging. The authors proactively mitigate data contamination by modifying datasets, enhancing the reliability of their evaluation. They use comprehensive evaluation metrics—including Valid Execution Rate (VER), Success Rate (SR), CodeBERTScore (CBS), and computational costs—to provide a holistic assessment of agent performance.

The paper is well-organized and written, utilizing figures and tables to enhance understanding. The authors provide insightful analyses of experimental results, highlighting why current language agents struggle with these tasks. By releasing all code and data, they promote open science and collaboration, significantly contributing to the advancement of AI in scientific research.

### Weaknesses
1. The paper evaluates agents using three frameworks but doesn't justify these choices or explore advanced architectures like ReAct or Toolformer. Without including state-of-the-art frameworks that offer advanced reasoning and tool-use capabilities, the study may not fully assess the agents' potential to handle complex scientific tasks. Incorporating such frameworks could provide deeper insights into their capabilities and limitations.
2. Human evaluators who also participated in data collection may introduce bias due to familiarity with the tasks, affecting the objectivity of the assessments. Additionally, the error analysis lacks depth, as specific failure modes are not thoroughly examined. Involving independent evaluators and conducting a detailed error analysis would improve objectivity and help identify areas where agents struggle.
3. The paper doesn't compare the agents' performance with traditional methods or domain-specific tools, making it difficult to assess their practical utility relative to existing solutions. Including such comparisons would provide valuable context to evaluate the agents' real-world usefulness and guide future improvements.
4. Providing expert domain knowledge doesn't consistently improve agent performance and sometimes even decreases it, suggesting agents struggle to integrate this information effectively. Exploring why agents fail to benefit from expert knowledge could lead to better integration strategies and enhance their overall performance.

### Questions
1. Have you considered evaluating state-of-the-art frameworks like ReAct or Toolformer incorporating advanced reasoning and tool-use capabilities? Including these could offer deeper insights into the agents' performance on complex tasks.
2. Since evaluators were also involved in data collection, how did you mitigate potential assessment bias? Would involving independent evaluators improve objectivity?
3. Could you provide a more detailed analysis of the standard failure modes encountered by the agents? Understanding specific errors might help identify areas for improvement.
4. Have you compared the agents' performance with traditional methods or domain-specific tools? Including such comparisons could help assess their practical utility relative to existing solutions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The ScienceAgentBench framework is introduced in this paper to assess the data-driven scientific discovery capabilities of LLM models. The framework offers both end-to-end and fine-grained metrics in evaluations. Significant room for improvement in scientific tasks was confirmed by implementing the benchmark on various sota models. The benchmark has the potential to serve as a long-term progress indicator for LLM models on scientific reasoning capabilities.

### Strengths
The study involved extensive data curation and human annotation, demonstrating the authors' dedication and thoroughness. The inclusion of both end-to-end and fine-grained metrics allows for a comprehensive evaluation of models, particularly when the models can only partially solve a problem. Additionally, the exploration and discussion of various interaction methods with the local environment provides valuable insights.

### Weaknesses
Coding generation-related tasks may not be representative of some other scientific domains. While recent research has focused on such tasks, the authors could briefly acknowledge this limitations, especially since the benchmark's name suggests a more comprehensive evaluation of broader scientific capabilities.



### Questions
Why was VER chosen over CBS when ranking models? High VER but low CBS could still indicate good context understanding, though poor execution. Was it considered to use heuristics / weighted sum to combine all metrics in the final evaluation?

Will setting CBS to 1.0 when SR is 1 introduce bias into the metric? Some argue that this specific treatment can skew the metric's results. While CBS may not be ideal when the model employs a different approach than annotation but still arrives at the correct answer, setting it to 1.0 could lead to inconsistent score interpretations. Additionally, if the ranking is order-based, this specific treatment might not have a significant impact.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel benchmark, ScienceAgentBench, designed to assess language agents' performance in data-driven scientific exploration. It meticulously curates 102 diverse tasks sourced from 44 peer-reviewed publications spanning four disciplines (Bio, Chem, Information Sci, Psy & Cog Neuroscience), subsequently validated by nine subject matter experts. Employing a variety of evaluation metrics, the study examines the efficacy of generated programs, their execution outcomes, and associated costs. By evaluating five LLMs, including both open-weight and proprietary models, across three frameworks—direct prompting, OpenHands, and self-debug—the findings underscore the current limitations of language agents in generating code for data-driven discovery.

### Strengths
(1) Writing: The clarity of this paper make it well-written and easy to comprehend.

(2) Benchmark: This paper introduces ScienceAgentBench, a framework tailored for assessing language agents in the realm of data-driven scientific exploration. It emphasizes scientific authenticity through collaboration with subject matter experts, establishes rigorous evaluation criteria, and maintains meticulous control over multi-stage quality assurance.

(3) Experiments: The paper evaluates three open-source models and two API-based models, conducting detailed assessments and in-depth analyses to provide comprehensive insights.

### Weaknesses
 (1) It appears that the emphasis of this paper leans more towards Data Science or data-driven discovery rather than scientific discovery.

(2) Task Annotation in Section 2.2 seems labor-intensive and time-consuming due to the involvement of identifying code, preprocessing data, implementing code, and writing dataset information. Are there any automated annotation or data collection methods available?

(3) How is the ground truth for each task defined and generated? Are there any automated validation methods that could streamline this process instead of relying solely on multiple rounds of manual validation by annotators?

(4) Could you elaborate on how the evaluation criteria outlined in Table 1 were established?

(5) Regarding the validation of generated Python programs during inference and the utilization of CodeBERTScore to assess token-level embeddings, have you considered employing a self-consistency strategy to validate multiple outputs over time?

(6) How is the validity of outputs generated by GPT-4o for the four heterogeneous datasets depicted in Figure 1 verified?

(7) Given the focus on code generation for data science, have you considered evaluating or providing the performance of code generation models like Codellama and DeepSeek-Coder?

(8) There appears to be inconsistency in the citation format, as observed in instances such as line 249 and line 251. Would it be possible to ensure uniformity in citation formatting throughout the paper?

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
