# AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments

- Decision: Reject
- Avg Score: 7.20
- Scores: 6, 8, 8, 8, 6

## Abstract
Evaluating large language models~(LLM) in clinical scenarios is crucial to assessing their potential clinical utility. Existing benchmarks rely heavily on static question-answering, which does not accurately depict the complex, sequential nature of clinical decision-making. Here, we introduce AgentClinic, a multimodal agent benchmark for evaluating LLMs in simulated clinical environments that include patient interactions, multimodal data collection under incomplete information, and the usage of various tools, resulting in an in-depth evaluation across nine medical specialties and seven languages.
We find that solving MedQA problems in the sequential decision-making format of AgentClinic is considerably more challenging, resulting in diagnostic accuracies that can drop to below a tenth of the original accuracy. Overall, we observe that agents sourced from Claude-3.5 outperform other LLM backbones in most settings. Nevertheless, we see stark differences in the LLMs’ ability to make use of tools, such as experiential learning, adaptive retrieval, and reflection cycles. Strikingly, Llama-3 shows up to 92\% relative improvements with the notebook tool that allows for writing and editing notes that persist across cases. To further scrutinize our clinical simulations, we leverage real-world electronic health records, perform a clinical reader study, perturb agents with biases, and explore novel patient-centric metrics that this interactive environment firstly enables.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents AgentClinic, a multimodal agent benchmark for evaluating large language models (LLMs) in simulated clinical environments. It challenges the traditional static question-answering evaluations by introducing interactive, dialogue-driven, sequential decision-making scenarios. The benchmark includes patient interactions, multimodal data collection, and tool usage, covering nine medical specialties and seven languages.

### Strengths
The paper presents an approach to evaluating LLMs in clinical environments by introducing AgentClinic, a multimodal agent benchmark. This is a departure from the traditional static question-answering evaluations and provides a more realistic and comprehensive assessment of LLMs' capabilities in medical diagnosis. The incorporation of biases into the benchmark is an original contribution, as it allows for the study of how biases can affect the performance of LLMs and patient perception.

The paper is well-written and easy to follow, with clear explanations of the benchmark design, agent roles, and evaluation metrics. The figures and tables are also well-designed and help to illustrate the key findings.

The work may has implications for the development and evaluation of medical AI systems. The study of biases in clinical environments is also of great importance, as it can help to improve the fairness and reliability of medical AI systems.

### Weaknesses
The study does not consider the impact of longitudinal data on the performance of LLMs, which is an important aspect of clinical decision-making.

While the paper introduces several novel evaluation metrics, such as patient compliance and consultation ratings, these metrics may be subjective and difficult to measure accurately.

One of my main concerns is that the core framework of this article seems to have a large overlap with AI Hospital (which also uses a multi-agent framework to evaluate the ability of doctor agents in multi-round medical interactions), but this article does not mention AI Hospital at all.

Ref: AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator

### Questions
1. How do you plan to address the issue of potential bias in the training data of proprietary models like GPT-4 and Claude 3.5? Can you provide more details on the steps you have taken to mitigate this bias?
2. The simulated clinical environment in AgentClinic seems to be relatively simple compared to real-world clinical settings. How do you plan to expand and improve the benchmark to better capture the complexity of actual clinical practice?
3. The evaluation metrics used in the paper, such as patient compliance and consultation ratings, are subjective. How do you plan to validate and improve the reliability of these metrics?
4. From the perspective of AI Hospital, some of the core contributions claimed by this paper will be greatly weakened, and I wonder if the authors can explain why AI Hospital is not cited. Alternatively, can you explain the similarities and differences between this article's framework and the AI ​​Hospital framework?

### Soundness
3

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
3

### Summary
Recognizing that existing static QA benchmarks often fail to reflect the complexities of clinical decision-making tasks, the authors propose AgentClinic, an open-source multimodal agent benchmark for simulating clinical environments. The framework introduces patient agents (informed by real clinical cases), doctor agents, a measurement agent, and a moderator, with agents exhibiting 24 different biases. The patient cases represent nine medical specialities across seven multilingual environments. The study reveals significant performance differences across models, highlighting the impact of biases and tool integration, with models like Claude-3.5 and Llama-3 demonstrating notable improvements with tools like adaptive retrieval and note-taking.

### Strengths
Dataset: This is a novel and comprehensive benchmark that closely mimics physician-patient interactions. Its inclusion of diverse medical scenarios ensures a comprehensive assessment of model capabilities, providing a challenging benchmark for evaluating model accuracy and generalization.

Approach: The authors use a robust benchmarking approach that includes multiple state-of-the-art models (e.g., Claude 3.5, GPT-4, Mixtral-8x7B, Llama 3, etc.) evaluated on the same task, and quantify uncertainty in performance. This methodology ensures a fair and statistically rigorous comparison of the models, enhancing the reliability and transparency of the results.

Experiment: The human evaluation ratings provided by physicians adds a layer of real-world applicability of this benchmark.

### Weaknesses
Stigmatizing language in medical records can influence not only how physicians perceive patients, but also how treatment decisions are made. Physicians have been found to prescribe pain medication less often when patient notes contain stigmatizing versus neutral language (P Goddu et al., 2018; Kelly et al., 2010). This dynamic can influence treatment outcomes and the overall patient-provider relationship. The clinical cases in the paper could benefit from more nuanced language that reflects these concerns, particularly in how bias is conveyed through medical documentation. Additionally, the paper’s "Bias and Patient Agent Perception" section could be expanded to explore patient trust in the healthcare system.

### Questions
1. What is the rationale behind an N of 20 for the interaction time when assessing the diagnostic accuracy of AgentClinic-MedQA? I’m surprised at the meaningful drop in diagnostic accuracy from 52% to 25%. 

2. Although Claude 3.5 is reported to have the highest accuracy on both AgentClinic-MIMIC-IV and AgentClinic-MedQA, its performance varies by as much as 13 percentage points. What factors contribute to this moderate variability? Does this suggest issues with model robustness or potential limitations in the dataset or experimental design?

3. Have the authors conducted a detailed error analysis to identify the types of questions/ cases the models struggle with the most? Are there specific failure modes common to all the models, or do different models exhibit distinct weaknesses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces AgentClinic, a multimodal benchmark that evaluates language models' medical diagnostic abilities through **interactive dialogue** and examinations rather than static questions. Using four agents and incorporating biases, tools, and real clinical cases across specialties and languages, it demonstrates Claude-3.5's superior performance while revealing varied capabilities among models in *tool usage* and *bias handling*.

### Strengths
Overall, the paper is well-written with clear logical flow and is easy to follow. The motivation is clearly presented and makes sense: "Existing diagnostic challenges are not static QAs, but are interactive, dialogue-driven, sequential decision-making environments that require data collection, ordering appropriate medical exams, and understanding medical images across patients with unique family histories, lifestyle habits, age categories, and diseases." This naturally addresses key limitations in previous medical LLM agents' static QA-oriented tasks. The human evaluations from experts make the presented experiments solid. The discussion is also impressive and comprehensive.

### Weaknesses
Weaknesses discussed in the Discussion section:
- The simulated clinical environments are currently simple; more methods could be benchmarked:
  1. Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate (https://arxiv.org/abs/2305.19118)
  2. MedAgents (https://aclanthology.org/2024.findings-acl.33/)
  3. ReConcile (https://arxiv.org/abs/2309.13007)
- Uncertainty issues

Suggestions for improvement:
- Include a statistics table for utilized/built datasets, covering sample size, dataset modalities included, task types/descriptions
- Address ethics issues with closed-source LLMs by replacing them with open-source LLMs running offline to prevent patient-sensitive data leakage
- Fix typography: use ``xxx'' in LaTeX for quotes
- Add more multi-agent collaboration/MDT baselines
- Evaluate sensitivity to various prompting strategies

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The article establishes a dynamic evaluation benchmark by simulating doctor-patient dialogues to assess model capabilities. Detailed experiments were conducted in scenarios involving bias, multilingualism, multiple departments, and multimodality, providing the community with a comprehensive evaluation framework.

### Strengths
- Built an evaluation framework for multiple agents to assess the performance of LLM models from various dimensions, including diagnostic performance and patient experience.
- Constructed a comprehensive test set to measure LLM's diagnostic capabilities in a simulated environment from multiple settings, including performance of different models in biased environments, multilingual, multi-department, and multi-modal scenarios.
- Tested several representative closed-source and open-source models and provided an objective evaluation.

### Weaknesses
 - The article's simulation of interactions between multiple agents is relatively simple, with the main interactions in the experiment limited to between the doctor agent and the patient agent. The lack of complexity in the agent interactions limits the assessment of the model's ability to handle more nuanced, real-world clinical scenarios, such as those involving multiple specialists or complex patient histories that unfold over time.
- The article does not conduct an in-depth analysis of the reasons for the model's performance differences on AgentClinic-MedQA and MedQA. The analysis should explore specific failure modes and information gaps that lead to the observed performance discrepancies, rather than just noting the difference. For example, are there specific types of questions or symptoms that the model struggles to elicit through dialogue, and how do these compare to the information provided directly in MedQA?
- Although the article introduces human scoring of the model's performance, it does not involve humans in the simulation experiments, making it difficult to measure the differences between the model's performance and human performance. The absence of a human baseline in the interactive simulation makes it challenging to contextualize the performance of the LLM agents and understand how they compare to expert clinicians in a similar interactive setting.

### Questions
- Why is a measurement agent needed, and how does its role differ from that of a tool? I hope the author can provide a deeper explanation.
- It seems that the doctor agent in AgentClinic-MedQA has the opportunity to gather more information through multiple rounds of interaction compared to the doctor agent in MedQA. However, in actual tests, the performance of the doctor agent in AgentClinic-MedQA may be inferior to that of the doctor agent in MedQA. There could be many reasons for this phenomenon. Can the author provide an intermediate metric, such as the amount of useful information obtained by the doctor agents in both AgentClinic-MedQA and MedQA, to further determine the causes of this phenomenon?
- Is it possible to have human doctors interact with simulated patients under the most basic settings and then compare the performance differences between human doctors and LLM doctors? This might provide a more intuitive comparison.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors introduce AgentClinic, a multimodal benchmark for evaluating LLMs within simulated clinical environments. The pipeline’s performance is assessed using the MedQA, MIMIC-IV, and NEJM datasets.

### Strengths
Some conclusions may hold clinical relevance

### Weaknesses
My primary comments are as follows:

1. The paper is challenging to follow, as many crucial details are buried in the lengthy appendix rather than presented in the main text. For instance, it is unclear what specific biases are explored in this work and how they are defined. Additionally, how agent tools are integrated within the pipeline, what specific data are extracted from the MIMIC-IV dataset, the nature of the NEJM case challenge dataset, and whether it includes QA pairs all need clarification. Furthermore, the difference between specialist case use reports and general QA tasks should be explained. I recommend providing brief explanations for any non-standard terms in the main text for improved clarity.

2. Although the paper claims to simulate a real-world clinical environment, several settings and use cases seem impractical. For example, what is the intended purpose of the measurement agent? Why can’t the complete records be provided directly, or why doesn’t the doctor agent extract values directly from the database? Additionally, evaluating a patient agent seems unrealistic within actual clinical workflows.

3. Since the study focuses on evaluating LLMs within clinical contexts, the benchmark appears to lack some medical LLMs.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
