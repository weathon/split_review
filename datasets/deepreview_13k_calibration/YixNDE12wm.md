# GuardAgent: Safeguard LLM Agent by a Guard Agent via Knowledge-Enabled Reasoning

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
The rapid advancement of large language models (LLMs) has catalyzed the deployment of LLM-powered agents across numerous applications, raising new concerns regarding their safety and trustworthiness.
In addition, existing methods for enhancing the safety of LLMs are not directly transferable to LLM-powered agents due to their diverse objectives and output modalities.
In this paper, we propose \namenospace, the first LLM agent as a guardrail to other LLM agents.
Specifically, \name oversees a target LLM agent by checking whether its inputs/outputs satisfy a set of given \textit{guard requests} (e.g., safety rules or privacy policies) defined by the users.
\name comprises two steps: 1) creating a task plan by analyzing the provided guard requests, and 2) generating guardrail code based on the task plan and executing the code by calling APIs or using external engines.
In both steps, an LLM is utilized as the core reasoning component, supplemented by in-context demonstrations retrieved from a memory module.
Such knowledge-enabled reasoning allows \name to understand various textual guard requests and accurately ``translate'' them into executable code that provides reliable guardrails.
Furthermore, \name is equipped with an extendable toolbox containing functions and APIs and requires no additional LLM training, which underscores its generalization capabilities and low operational overhead.
In addition to \name, we propose two novel benchmarks: an EICU-AC benchmark for assessing privacy-related access control for healthcare agents and a Mind2Web-SC benchmark for safety evaluation for web agents.
We show the effectiveness of \name on these two benchmarks with 98.7\% and 90.0\% guarding accuracy in moderating invalid inputs and outputs for the two types of agents, respectively.
We also show that \name is able to define novel functions in adaption to emergent LLM agents and guard requests, which underscores its strong generalization capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes GuardAgent, the first LLM agent designed to safeguard other LLM agents. GuardAgent utilizes the reasoning capabilities of LLMs to generate a task plan and translate it into guardrail code. It stands out for its flexibility in handling diverse guardrail requests by retrieving relevant demonstrations from a memory module, its reliability through code-based guardrails, and its low computational overhead, requiring no additional LLM training.

### Strengths
• The paper is well-structured, with a clear logical flow that facilitates understanding. The experimental design is concise, and the results are presented in an easily interpretable manner, enhancing the clarity of the study.

• The paper effectively underscores the necessity of the proposed "agent guarding agent" approach, particularly highlighting GuardAgent's importance in accommodating dynamic and complex guardrail requests. This emphasis supports the relevance and timeliness of the guardrail framework in addressing complex safety and privacy challenges.

### Weaknesses
• Lack of experimental comparison with existing works on Guardrail methods. While the related work section discusses existing many guardrail approaches, the study conducts only a brief comparison with “model guarding agent” approach. Expanding the scope of comparison with a broader range of guardrail techniques would strengthen the evaluation of GuardAgent’s effectiveness.

• In the ablation studies, the authors mention “the trend of code-based guardrails” as a rationale for the code-generation design of GuardAgent, but this observation has only been briefly mentioned. This aspect appears intriguing, and further experimental analysis and a more detailed discussion would enhance the understanding of this design choice.

• As the first work to explore “agent guarding agents”, this paper is positioned to serve as a key reference for future research in this domain. However, to support subsequent studies, it would benefit from an analysis of the GuardAgent limitations or potential threats to validity associated with current version of paper, as well as a discussion of possible future directions on “agent guarding agent”  to further advance the development of robust guardrail frameworks.

• Some typos are found.
- Section 4.1: In the second step 4.3),-> In the second step (Sec. 4.3)
- Why all metrics in all Tables has upwards arrow?
- Section 5.3: Tab. 2-> Table 2, Fig. 3-> Figure 3
- Please give a formal(short) caption for all Figures and Tables

### Questions
1. Could you clarify which specific work is being referred to as "agent guarding models" approach？
2. Additionally, it appears that related work on "model guarding agents" approaches has not been cited, right?
3. Could you discuss more about current limitations/challenges and future direction of “agent guarding agent” approach?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents GuardAgent, a protective guardrail framework that functions as a third-party safeguard for other LLM agents. GuardAgent initially utilizes an LLM to develop an action plan derived from guard requests as well as the inputs and outputs of the target agent. The LLM then transforms this plan into guardrail code, which is subsequently executed by an external engine. The authors also introduce two benchmarks specifically aimed at evaluating LLM safety: EICU-AC, designed to test access control for LLM agents in healthcare, and Mind2Web-SC, a dataset intended to assess safety mechanisms for web agents powered by LLMs. Experimental validation on these datasets shows that GuardAgent performs better than the "model-guard-agent" baseline, which uses hard-coded task instructions.

### Strengths
**S1**: A valuable contribution of this paper is providing the LLM community with the probably first safety benchmarks that explicitly model user profiles. In these two benchmarks, the actions that the LLM agent needs to perform are related to the user's identity and profile, requiring the agent to assess whether the user's actions may pose potential risks based on their identity. These datasets present a greater challenge for LLM agents, as they need to incorporate the user profile and assigned permissions into the context to complete tasks while minimizing risks. Such benchmarks closely align with real-world needs, specifically in providing different services based on varying user permissions. This approach offers the LLM community a new perspective and dimension, while also presenting new challenges.

**S2**: In tasks aimed at enhancing the alignment or safety capabilities of LLMs, safety and helpfulness are often in conflict, requiring a trade-off. Specifically, as the safety capabilities of LLMs increase, the likelihood of them generating refusal responses also increases, which in turn reduces the likelihood of providing helpful information to the user—a phenomenon known as the "safety tax." However, in this paper, experiments demonstrate that GuardAgent does not affect the task performance of the target agent while safeguarding against potential risks. This design represents a well-executed approach.

### Weaknesses
 **W1**: The work in this paper first designs two benchmarks, i.e., EICU-AC and Mind2Web-SC, and then develops the method based on these two tasks. However, the motivation for proposing these benchmarks has not been well justified. Why are database retrieval (EICU-AC) and web service calls (Mind2Web-SC) the two representative tasks for testing the safety of LLM agents? What makes these two tasks sufficiently representative to measure the safety capabilities of LLM agents in mitigating risks? Are there any similar tasks in previous research that have been used to validate the safety of LLM agents? Why introduce these new tasks instead of using existing benchmarks? In summary, there needs to be an explanation and justification for the motivation behind proposing these new benchmarks.

**W2**: At the beginning of this paper, one contribution is introduced as ``generate guardrail code based on the task plan." However, after reading the benchmark design section, we find that the so-called guardrail code generation is actually a task-oriented function, not a task-agnostic, universally applicable design. Since the EICU-AC task itself requires generating structured query code for database retrieval, GuardAgent needs to have code generation capabilities. This doesn’t mean that a unique code design was developed to enhance the safety of LLM agents. Here, if the downstream task doesn’t require code generation, such as in a complex Q&A task where responses are given in natural language, would code generation then be a redundant design for GuardAgent? 

**W3**: Additionally, the authors state that GuardAgent leverages the LLM's reasoning capabilities to "accurately ‘translate’ textual guard requests into executable code." However, this capability is task-dependent. When the task does not require code generation, wouldn’t this reasoning ability be unnecessary? Therefore, the contribution proposed in this paper—particularly the guardrail code generation—is determined by the characteristics of the downstream tasks. It is not inherently a design that can be applied to various tasks to enhance LLM agent safety, which weakens this work's generalizability and impact.

### Questions
**Q1**: It is better to briefly introduce the definition of ‘model-guard-agent’ baseline when it first appears in this paper. Otherwise, it will confuse the readers.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents GuardAgent, a framework designed to enhance the safety and robustness of LLMs against adversarial inputs and potential misuse. GuardAgent leverages a multi-agent architecture, incorporating safety-checking agents that detect unsafe responses, and employs prompt engineering to guide the LLM toward safer outputs. The framework integrates several defensive techniques, including uncertainty estimation, self-refinement prompts, and cross-agent validation, to achieve a high level of safety without compromising the model’s performance. In addition to GuardAgent, this paper also proposes two novel benchmarks: an EICU-AC benchmark for assessing privacy-related access control for healthcare agents and a Mind2Web-SC benchmark for assessing safety regulations for web agents.

### Strengths
1. GuardAgent is the first framework focused on providing guardrails to LLM agents, addressing a critical gap in AI agent safety and privacy.

2. The system's non-invasive approach and extendable toolbox make it adaptable to diverse LLM agents and new guard requests.

3. GuardAgent demonstrates superior accuracy and reliability compared to baseline models, particularly when using code-based guardrails.

### Weaknesses
1. **Dataset Scope**: The paper evaluates GuardAgent on two specific datasets, EICU-AC for privacy-related access control in healthcare and Mind2Web-SC for safety compliance in web agents. While these datasets represent different types of guard requests, the limited scope raises questions about GuardAgent's generalizability. As a defense mechanism, how effectively can GuardAgent adapt to other domains beyond healthcare and web safety, where guardrails may vary significantly?

2. **Performance Variability**: The paper evaluates GuardAgent using different core LLMs, such as Llama3-70B and GPT-4, but it does not fully clarify how this choice impacts GuardAgent’s overall effectiveness. Does GuardAgent’s performance, including its accuracy in identifying violations, speed in generating guardrail code, and flexibility in adapting to complex guard requests, vary significantly depending on the model used?

3. **Memory Dependency**: The ablation study shows that GuardAgent’s performance improves with more in-context demonstrations. How does the quality of these demonstrations, such as their relevance or diversity, impact accuracy? Is there an optimal number of demonstrations that balances accuracy and efficiency, and does this vary by task or application?

4. **Computational Efficiency**: What are the computational costs associated with GuardAgent’s code generation and execution process?

5. **Error Handling**: GuardAgent includes a debugging mechanism that uses an LLM to analyze and address errors during code execution. Could you clarify how robust this mechanism is? Specifically, how well does it handle different error types (e.g., syntax errors, logical errors, unforeseen inputs), and are there limits to the errors it can reliably resolve? Additionally, has it been tested in scenarios with complex or ambiguous errors, and what are its typical failure modes, if any?

### Questions
See the Weaknesses above.

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
This paper focuses on guardrails for LLM agents, with the authors proposing GuardAgent, a LLM agent designed to safeguard other LLM agents based on specified guard requests from users. The paper has the following contributions: (1) development of an LLM agent framework to guard other target LLM agents based on user requirements and using a memory module that stores previous use cases; (2) creation of two benchmarks for healthcare and web agents to evaluate access control policies; (3) evaluation and ablation study evaluating GuardAgent vs. baseline models.

### Strengths
This paper presents an innovative framework for a LLM agent to safeguard other LLM agents. The design of the framework is noninvasive, generates guardrails using python code execution (not natural language) and does not require LLM training or retraining, which are all strengths. Using python code execution as opposed to some knowledge-specific languages as done in some other works (e.g., Kang, Li R^2-Guard) is a bonus, supporting adoption by a wider set of programmers/engineers. 

In addition, the integration of the memory module is a nice feature which allows the agent to document new cases it runs into and learn from previous examples which can help reduce the burden of a user needing to specify an exhaustive list of requirements, and may allow for adaption to new (unseen) scenarios. This is an innovation compared to previous work (Rebedea et al. NeMo Guardrails; Inan et al, Llama Guard; Ghosh et al. Aegis) which either require users to specify and provision every safety/privacy property or need some type of training guideline, such as classification labels. The paper evaluates the framework based on the curated benchmarks and compared to baselines for different LLM model types. The experiments make sense as they test precision, recall and two measures of accuracy for the labels about whether a policy is violated or not. The eval includes an ablation study which shows performance improvements for the inclusion of the memory module and toolbox (supporting framework architecture decisions), and provide evidence that the framework performs well with performance improvements compared to the baselines in almost all criteria.

Finally, this paper is presented very nicely- the structure, organization and language are very clear and the figures are unambiguous and helpful.

### Weaknesses
The LLM guardrail space is quite saturated with recent work, and the related work section is quite concise. It might be worth expanding this section to better motivate the need for this work. For example, the authors mention that model- and agent- guarding cannot be directly used to safeguard  LLM agents with diverse output modalities. Can the authors provide some contextual examples or explain why?

The access control policies used for the healthcare and web agent scenarios and evaluation (though relevant for these application areas) are pretty simplistic. In many real world use cases, more complicated policies may be required to accurately provision safety/privacy constraints. For example, fine-grained access controls based on user roles, or temporal constraints on data access are not considered. The policies used in the experiments are limited to simple keyword matching or presence/absence of certain data fields, which does not reflect the complexity of real-world access control scenarios.

The GuardAgent only returns binary (policy violated or not) responses, which may not be sufficient to represent all cases of safety and privacy policies. Many policies are not so strict, and may need to return risk-based or threshold based responses. For example, a policy might allow a certain number of violations before triggering an alert, or might need to quantify the severity of a violation based on the context. The current binary output does not allow for such nuanced policy enforcement.

A pro of the framework is the automatic code generation through use of the framework's toolbox. I am wondering about the reliability and generalizability of such a process as inexecutable generated code would render the framework useless. This is not directly evaluated in the experimental section (though the authors mention code is almost always executable and does not often use the debugging stopgap in Section 4.3). It is unclear how the framework handles cases where the generated code fails to execute, and what mechanisms are in place to ensure the robustness of the code generation process. It would be useful to see an analysis of the types of errors that occur during code generation, and how often the debugging stopgap is used in practice.

It would be great if the authors intended to release their framework and benchmarks (e.g., so that people could contribute to the toolbox functionalities or specifications).

### Questions
(1) Can the authors provide examples or comment on the ability of the framework to adapt to more complicated policies than the ones evaluated in the experimental section (such as more fine-grained access controls for different users)?

(2) Can the authors comment on the ability of GuardAgent to handle nonbinary requirements (e.g., safety requirements that work on a threshold, risk-based requirements, etc.)? 

(3) Can the authors comment on or provide evidence that the framework's code generation process is reliable and generalizable (i.e., generates low rates of inexecutable code even for new safety or privacy policies or application domains)? Under what scenarios or tasks might this change; do new policies that have limited to no occurrence in the memory module result in more inexecutables?

(4) Do the authors have an idea about why the recall LPR does better for GPT-4 baseline compared to GuardAgent (Table 2)?

### Soundness
4

### Presentation
4

### Contribution
3
