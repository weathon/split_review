# Prompt Injection Benchmark for Foundation Model Integrated Systems

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Foundation Models (FMs) are increasingly integrated with external data sources and tools to handle complex tasks, forming FM-integrated systems with different modalities. However, such integration introduces new security vulnerabilities, especially when FMs interact dynamically with the system environments. One of the most critical threats is the prompt injection attack, where adversaries inject malicious instructions into the input environment, causing the model to deviate from user-intended behaviors. To advance the study of prompt injection vulnerabilities in FM-integrated systems, a comprehensive benchmark is essential. However, existing benchmarks fall short in two key areas: 1) they primarily focus on text-based modalities, lacking thorough analysis of diverse threats and attacks across more integrated modalities such as code, web pages, and vision; and 2) they rely on static test suites, failing to capture the dynamic, adversarial interplay between evolving attacks and defenses, as well as the interactive nature of agent-based environments. To bridge this gap, we propose the Prompt Injection Benchmark for FM-integrated Systems (FSPIB), which offers comprehensive coverage across various dimensions, including task modalities, threat categories, various attack and defense algorithms. Furthermore, FSPIB is interactive and dynamic, with evaluations conducted in interactive environments, and features a user-friendly front end that supports extensible attacks and defenses for ongoing research. By analyzing the performance of baseline prompt injection attacks and defenses, our benchmark highlights the prevalence of security vulnerabilities in FM-integrated systems and reveals the limited effectiveness of existing defense strategies, underscoring the urgent need for further research into prompt injection mitigation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces FSPIB, a benchmark designed to evaluate foundational models when integrated with various modalities regarding prompt injection vulnerabilities. While prompt injection research has primarily focused on text-based models, this work explores how such attacks impact other modalities, such as documents, web pages, code, and images. The paper categorizes prompt injection threats and defenses into two levels: 1) Information level (e.g., information leakage, goal hijacking, response refusal) and 2) Action level (e.g., adversarial actions, parameter manipulation). Overall, the work seeks to provide a unified analysis of prompt injection vulnerabilities across diverse modalities, applications, and agents.

### Strengths
1. The paper advances current benchmarks by addressing vision, code, and web-based threats in addition to text-based modalities, and provides a structured analysis of both information-level and action-level threats.
2. The paper presents a comprehensive benchmark and analysis for prompt injection threats, covering a wide range of real-world applications, attacks, and defenses.
3. The interactive systems in a multi-turn evaluation add depth to the analysis, though specific details on the multi-turn evaluation are not fully elaborated.

### Weaknesses
Weaknesses:

- Lack of evaluation on real-world FM systems as mentioned in the limitations of the manuscript.

- Lack of design of attacks or defenses.

- The information provided in the manuscript is difficult to reproduce the proposed evaluation benchmark.

### Questions
1.	Please clarify the experimental settings in multi-turn evaluation.
2.	What are the major findings in the experimental results? Which applications or agents are more vulnerable? 
3.	Is any specific integration with foundation models more vulnerable?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new benchmark for prompt injection attacks on LLMs.
Compared to existing works, the proposed benchmark is interactive and dynamic
and it has larger coverage on differerent modalities and tasks.

### Strengths
1. The studied problem is interesting.

2. The proposed benchmark in this paper has large coverage on differerent
modalities and diverse tasks.

### Weaknesses
1. The diversity of the models involved in the experiments could be improved.
Only three models are involved in the experiments, i.e., GPT-4o mini, LLaMA 3
and Qwen-VL, which may not provide sufficient coverage for a comprehensive
benchmark study. Expanding the experiment to include a broader range of models
is recommended. Additionally, specifying which particular models were used
within the LLaMA 3 and Qwen-VL families would improve clarity.

2. It is suggested to provide a more in-depth analysis of the benchmark results to
extract key observations and conclusions. For example, this could include
investigating the underlying causes of variations in attack success rates across
different modalities, models, and attack types.

3. The novelty of this paper might be incremental. A key contribution it highlights
is a dynamic framework with interactive environments. However, as recognized
in this paper, the existing work AgentDojo already provides similar
functionality. While this paper argues that AgentDojo lacks comprehensive
coverage of task modalities and unified analysis across different systems, these
limitations might be relatively minor given the technical contributions.
Expanding coverage to include more modalities and tasks may also be seen as an
incremental enhancement.

### Questions
please refer to Weaknesses

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
4

### Summary
This paper introduces FSPIB, a comprehensive benchmark for evaluating prompt injection vulnerabilities in FM-integrated systems. FSPIB addresses gaps in current benchmarks by covering diverse modalities beyond text, including code, web, and vision, and by providing a dynamic, interactive testing environment. It evaluates attacks and defenses in agent-based systems, enabling ongoing adaptation to evolving adversarial strategies. Through baseline analysis, FSPIB demonstrates the prevalence of security vulnerabilities in FM-integrated systems and the limited efficacy of current defenses, highlighting the need for further research in prompt injection mitigation.

### Strengths
Strengths:
+ This work offers FSPIB, a comprehensive benchmark for evaluating prompt injection vulnerabilities in FM-integrated systems.
+ Comprehensive and thorough assessment.
+ Revealed the prompt injection security risk of the LLM agent framework.

### Weaknesses
Weaknesses:

- Lack of evaluation on real-world FM systems as mentioned in the limitations of the manuscript.
- Lack of design of attacks or defenses.
- The information provided in the manuscript is difficult to reproduce the proposed evaluation benchmark.

### Questions
Questions:

- Q1: Regarding the evaluation metrics, the attack success rate defined in this paper seems a bit vague. It would be better if the authors could provide more practical examples.

- Q2: As for the examples of successful attacks, the article seems to lack the demonstration of these cases. It would be better if the authors could show more examples of attacks.

- Q3: The concepts of "application" and "agent" in this article require further clarification. For instance, in the context of a web application, it is unclear whether the application performs a series of web-related operations or is solely intended for web retrieval. To enhance reader understanding of the practical implications of the attack scenarios and the interpretation of attack success rates, the authors should provide a more detailed explanation of the application scenarios and purposes for each application in the appendix.

- Q4: In addition to the baseline attacks and defenses, have the authors considered proposing any new attack and defense mechanisms? Given that ICLR is a top venue for cutting-edge research and technical innovation, the inclusion of novel technical designs would enhance the paper's impact and align with the high standards expected at such a conference.

- Q5: Could the authors provide detailed code and datasets to enable readers to reproduce the results? Based on the current information in the manuscript, it appears challenging for readers to replicate the experimental outcomes, which may hinder effective academic communication. Sharing reproducible resources would greatly enhance transparency and facilitate further research in this area.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper present a new framework for benchmarking systems that integrate a foundation model (FM). The framework considers both FM-integrated applications and FM-integrated agents; it spans multiple modalities, including code and vision, and multiple tasks, including web- and code-agent tasks. Attacks are evaluated in terms of information- and task-level threats, such as information leakage and adversarial actions. The paper uses the framework to evaluate three models (GPT-4o mini, Llama 3 as LLM, and Qwen-VL as VLM) against a number of prompt-injection variants (e.g., direct attack, boundary-confusion attack) and defenses (e.g., sandwich prevention, data isolation), showing that prompt-injection attacks may still pose a significant threat.

### Strengths
* More comprehensive benchmark than existing ones in terms of modality, types of threats, and evaluation pipeline.
* Benchmarking results on some state-of-the-art models as well as on baseline attacks and defenses.
* Prompt injection is an important problem.

### Weaknesses
* The implementation of the framework does not seem to be available.
* The evaluation of usability is not rigorous, i.e., paper claims that the framework is "user-friendly" but this is not evaluated (e.g., using user study).
* It would be better if the attacks and defenses listed in Section 3.3.2 were accompanied by references.

### Questions
* Would it make sense to frame the three information-level threats (leakage, goal hijacking, and refusal) in terms of the traditional CIA (confidentiality, integrity, and availability) triad? Also, is the terminology of "threat levels" common in the literature? The usage of the word "threat" in Section 3.2 seems unconventional.
* "despite the claims of strong safety alignment in the Llama 3 model, it still exhibits vulnerabilities to prompt injection"
Is safety alignment supposed to prevent prompt injection?

### Soundness
3

### Presentation
3

### Contribution
2
