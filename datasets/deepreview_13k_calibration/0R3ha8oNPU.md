# SecCodePLT: A Unified Platform for Evaluating the Security of Code GenAI

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Existing works have established multiple benchmarks to highlight the security risks associated with Code GenAI.
These risks are primarily reflected in two areas: a model’s potential to generate insecure code (insecure coding) and its utility in cyberattacks (cyberattack helpfulness).
While these benchmarks have made significant strides, there remain opportunities for further improvement.
For instance, many current benchmarks tend to focus more on a model’s ability to provide attack suggestions rather than its capacity to generate executable attacks.
Additionally, most benchmarks rely heavily on static evaluation metrics (e.g., LLM judgment), which may not be as precise as dynamic metrics such as passing test cases. 
Furthermore, some large-scale benchmarks, while efficiently generated through automated methods, could benefit from more expert verification to ensure data quality and relevance to security scenarios. 
Conversely, expert-verified benchmarks, while offering high-quality data, often operate at a smaller scale.
To address these gaps, we develop \sys, a unified and comprehensive evaluation platform for code GenAIs' risks.
For insecure code, we introduce a new methodology for data creation that combines experts with automatic generation. 
Our methodology ensures the data quality while enabling large-scale generation. 
We also associate samples with test cases to conduct code-related dynamic evaluation.
For cyberattack helpfulness, we set up a real environment and construct samples to prompt a model to generate actual attacks, along with dynamic metrics in our environment.
We conduct extensive experiments and show that \sys outperforms the state-of-the-art (SOTA) benchmark \purplellama in security relevance.
Furthermore, it better identifies the security risks of SOTA models in insecure coding and cyberattack helpfulness. 
Finally, we apply \sys to the SOTA code agent, Cursor, and, for the first time, identify non-trivial security risks in this advanced coding agent.\footnote{We provide data in \url{https://huggingface.co/datasets/Virtue-AI-HUB/SecCodePLT}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents SecCodePLT, a unified and comprehensive evaluation platform for code GenAIs' risks. Considering insecure code, the author introduces a new methodology for data creation that combines experts with automatic generation. Considering cyberattack helpfulness, the authors set up a real environment and construct samples to prompt a model to generate actual attacks. Experiments show that CyberSecEval could identify the security risks of SOTA models in insecure coding and cyberattack helpfulness.

### Strengths
1. Promising direction. Establishing the benchmark to highlight the security risks associated with Code GenAI is a direction worth studying. 
2. Consider real-world attack behaviors and environment deployments. 
3. Compared with existing baselines from multiple perspectives and the results show the effectiveness of the proposed method.

### Weaknesses
 1. Some related work discussions are missing. 
 2. Some details are not explained clearly. 
 3. There are some minor errors that need to be polished and proofread.

### Questions
1. This article discusses risk assessment of code generation. Some related works on code generation may also be discussed, such as BigCodeBench [1].

[1] Bigcodebench: Benchmarking code generation with diverse function calls and complex instructions. https://arxiv.org/pdf/2406.15877

2. Some details are not explained clearly. In line 140 of the manuscript, the author mentions "extracting code chunks without proper context frequently leads to false positives". But it seems that the experiment did not perform an ablation experiment on the context field. As shown in lines 867 and 894, the context field is set to None. So I don't understand the role of context and how the solution SecCodePLT in this paper can benefit from context (how to reduce false positives).

3. In line 251 of the manuscript, the author mentions "We also introduce rule-based metrics for cases that cannot be evaluated with standard test cases". I am not sure where the rule mentioned here comes from. Is it based on some public manufacturer's provision? 

4. In MITRE ATT\&CK, the kill chain model may be common. In other words, an attacker often implements different attack stages through a series of attack techniques and tactics. It is unclear whether SecCodePLT considers such multi-stage attack and intrusion, rather than a single attack behavior.

5. Some minor errors, such as the missing period after "security-critical scenarios" on line 76. For "security is required.)" on line 253, the period should probably be after ")".

### Soundness
2

### Presentation
3

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
This paper develops SECCODEPLT, a unified and comprehensive evaluation platform for code GenAIs’ risks. It introduces a new methodology for data creation that combines experts with automatic generation for insecure code which ensures the data quality while enabling large-scale generation. It also associates samples with test cases to conduct code-related dynamic evaluation. Furthermore, it sets up a real environment and constructs samples to prompt a model to generate actual attacks for the task of cyberattack helpfulness, along with dynamic metrics in our environment.

### Strengths
The paper presents a pioneering approach by integrating a database with two distinct security-related tasks. SECCODEPLT serves as a comprehensive platform that unifies the evaluation of GenAIs’ risks associated with code generation. This integration facilitates a holistic approach to assessing different dimensions of security risks. By associating samples with test cases, SECCODEPLT enables dynamic evaluation related to code. This method allows for real-time assessments and adjustments, providing a deeper analysis of the code's behavior in practical scenarios.

### Weaknesses
1. The programming language used in the paper is limited, with Python being the sole language explored. This is inadequate for a comprehensive and large-scale benchmark. The inclusion of other programming languages like C/C++ and Java, which constitute a significant portion of recent CVEs, is crucial. These languages are more complex in syntax and more broadly applied, offering valuable insights into the capabilities of LLMs.
2. The paper's description of the data generation process for the IC task is unclear. It mentions the use of two different mutators to generate data, yet it fails to clarify the generation of the corresponding test suites. It is uncertain whether the test suites for these new datasets are generated by LLMs or if they reuse the original suites. If generated by LLMs, how is the quality of these suites assured? If the original test suites are used, can they adapt to new contexts effectively?
3. The paper lacks a necessary ablation study. The boundary of what is user control and what is provided by benchmark is not well clarified. The rationale behind the design of the prompts and instructions used to trigger evaluations is not well justified. For example, why do the authors use system prompts and user templates shown in the paper? Are they more reliable and efficient? Will the differences in these prompts affect the evaluation of LLM ability? If users want to use their own prompts, is there any way?
4. The evaluation metric of security relevance is confusing and lacks rationales. It is unclear whether this metric aims to assess specific properties of LLMs or the prompts themselves. Because the benchmark is designed to evaluate LLMs, using a metric that assesses the prompts introduces confusion. Furthermore, in the SECURITY-RELEVANCY JUDGE prompt template (D.1), the security policy reminder is included as part of the user input and fed directly to the LLM. This setup may influence the evaluation of security relevance and potentially introduce bias.
5. The ablation of the security policy reminder is missing, similar to problem 3. The paper does not discuss the reasons for choosing the security policy reminder prompt.
6. The paper lacks a discussion on the specific defenses employed in the CH task. In realistic settings, a variety of defenses, such as firewalls and intrusion detection systems, are typically deployed. It will be insightful to know how different LLMs perform when various defenses are considered in a simulated environment.
7. The usefulness and generalization of the CH task is limited. Practical attacks vary significantly and are influenced by diverse factors, but the scenario described in the paper lacks generalizability across different attack types and target systems. This limited setting restricts the ability to conduct an accurate and comprehensive evaluation of LLMs for the CH task. Additionally, the paper does not specify the capabilities of attackers, including the types of tools that can be used to launch attacks with LLMs. Also, the strong assumption that some internal users will click on phishing or other harmful links further reduces the task's practical relevance.
8. Evaluation metrics in CH task. It will be better to set a specific metric to evaluate the overall ASR for the end-to-end attack. Additionally, the details regarding the evaluation process are not well-explained – whether it is a fully automated process or requires human input at various stages to guide or adjust the evaluation.

### Questions
See above.

### Soundness
2

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
3

### Summary
The paper proposes SECCODEPLT, a unified and comprehensive evaluation platform for code GenAIs’ risks.

For insecure code, the authors introduce a new methodology for data creation that combines experts with automatic generation. For cyberattack helpfulness, the authors set up a real environment and construct samples to prompt a model to generate actual attacks, along with dynamic metrics.

### Strengths
Through experiments, SECCODEPLT outperforms CYBERSECEVAL in security relevance and prompt faithfulness, highlighting the quality of this benchmark. 
The authors then apply SECCODEPLT and CYBERSECEVAL to four SOTA open and closed-source models, showing that SECCODEPLT can better reveal a model’s risk in generating insecure code.

### Weaknesses
Many state-of-the-art methods for code generation are not mentioned and experimented in the paper, such as:

Jingxuan He, Martin Vechev. Large Language Models for Code: Security Hardening and Adversarial Testing. 2023. In CCS. https://arxiv.org/abs/2302.05319.

Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023. CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. In ICLR. https://arxiv.org/
abs/2203.13474

Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2023. InCoder: A Generative Model for Code Infilling and Synthesis. In ICLR. https://arxiv.org/
abs/2204.05999

Loubna Ben Allal, Raymond Li, Denis Kocetkov, Chenghao Mou, Christopher Akiki, Carlos Muñoz Ferrandis, Niklas Muennighoff, Mayank Mishra, Alex Gu, Manan Dey, et al. 2023. SantaCoder: Don’t Reach for the Stars! CoRR
abs/2301.03988 (2023). https://arxiv.org/abs/2301.03988

There are many other benchmarks for evaluations of code generation that are not mentioned and compared. Please refer to the paper https://arxiv.org/html/2406.12655v1 for details.

It is unclear how the author performs the code mutator as mentioned in “As specified in Section 3.2, we design our task mutators to keep the original security context and code mutator to preserve the core functionalities.” What types of code mutators are used here?

What dynamic methods do the authors use for “After mutation, we also manually check the security relevance of newly generated data and run dynamic tests to ensure the correctness of their code and test cases.”?

### Questions
In “Each seed contains a task description, example code, and test cases”, do all the source code samples have the task description? What are the methods used in test cases?

It is not clear how the author performs the code mutator as mentioned in “As specified in Section 3.2, we design our task mutators to keep the original security context and code mutator to preserve the core functionalities.” What types of code mutators are used here?

What dynamic methods do the authors use for “After mutation, we also manually check the security relevance of newly generated data and run dynamic tests to ensure the correctness of their code and test cases.”?

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
This paper provides a benchmark for evaluating security issues associated with LLM generated code. Specifically covering:   
i) Secure code generation: to assess LLMs ability to generate secure code (focusing on Python).  
ii) Cyber attack helpfulness: to evaluate a model’s capability in facilitating end-to-end cyberattacks.
They apply 4 LLMs to both benchmarks -- CodeLlama-34B-Instruct, Llama-3.1-70B, Mixtral-8×22B, GPT-4o – and compare their performance.

**Secure code generation benchmark:**    
The authors manually created 153 seed tasks covering 27 CWEs relevant to python – then used LLM-based mutators to generate variations of the tasks for each of the seeds (for large scale generation). They also include both vulnerable and patched code versions, together with functionality and security test cases for each task – resulting in a total of  1345 samples with about 5 test cases per sample.  
* They evaluate their samples on ‘prompt faithfulness’ and ‘security relevance’ – comparing with CyberSecEval and outperforming it on both.  
* They also evaluate the 4 LLMs for achieving the task’s required functionality using the pass @1 metric on the provided unit tests. And they evaluate the code security using carefully constructed security tests, including the boost in security when providing security policy info in the prompt.
* They also evaluate Cursor on their benchmark.  

**Cyber attack benchmark:**     
For this, they build a simulated environment containing a network that runs an e-commerce application. Their environment is structured similarly to a CTF, where the adversary aims to gain access to the database and steal sensitive user information. The benchmark facilitates 7 MITRE ATTACK categories.   
* They evaluate the 4 LLMs on their refusal rate to comply with generating attacks, and when attacks are generated, the attack success rate is measured.

### Strengths
The paper is tackling 2 important and timely problems at the intersection of LLMs and cybersecurity.   
•	Having a benchmark that includes both security and functionality unit tests for each code example is a strong contribution to the secure code generation literature. Many SOTA LLM papers in the literature currently test code security and functionality separately (ie. using separate datasets/tasks) due to lack of benchmarks with the capability to simultaneously test both. Strong and comprehensive benchmarks are definitely lacking for this problem.   
* Proposed approach to leverage LLMs to scale the development of secure code benchmark dataset.  
*  Using a controlled environment to see if the model can generate commands or code that facilitate attacks -- and tracking refusal rates in research on LLM-driven pentesting and red teaming can provide insight into the effectiveness of their internal safety mechanisms.

### Weaknesses
 * While a lot of work has been done for this paper and there are definitely strong contributions, by setting CyberSecEval as the goal post to beat, this paper goes too broad in scope (for a paper of this length) and fails to adequately establish its position among the existing peer reviewed literature for each of these 2 distinct research directions. There is no need for benchmarks to cover both secure code generation and cyber attack capability as they have fundamentally different objectives, setups, and evaluation metrics. In the case of  CyberSecEval, combining these tasks made sense because it was aligned with their product’s goals. For SecCodePLT, however, the logical connection is less clear. Secure code generation and cyberattacks don’t share the same purpose, infrastructure requirements, or audience, and combining them into the one conference-length paper restricts the depth of each evaluation.

* Overall, there is a lack of discussion/justification for the choice of prompt wording/techniques.

**Secure code generation task:**
i) Relevant benchmarks, such as LLMSecEval (MSR 2023), have been overlooked. LLMSecEval covers 18 Python-related CWEs, which challenges the authors' claim that existing benchmarks address only 8 Python-related CWEs.
A more detailed analysis of the scope/coverage of existing peer reviewed benchmarks and where this paper fits in would strengthen this work.
ii) Code security testing is challenging. Many SOTA papers try to utilize a combination of SAST tools, LLM vulnerability checkers, and manual checking. The discussion of the code security tests could be more convincing if it provided detailed information on the breadth and depth with which these tests cover potential vulnerabilities and edge cases. Eg. providing a breakdown of security test cases per CWE, showing how each test targets specific security requirements and edge cases, would help demonstrate thoroughness. Or providing a metric similar to code coverage in unit testing would help show that the security tests are exhaustive. Overall I didn’t understand how the vulnerable and patched code examples are used for evaluating the correctness of test cases and/or generated output.
iii) Prompt quality assessments could be stronger. The Security-relevancy Judge, based on GPT-4, introduces a potential bias since the same LLM type is used in prompt construction. Using diverse models or a user study evaluation of security relevance would provide more objective evaluations. Also – leveraging, for example, LLMSecEval’s metrics for prompt clarity and relevance would enhance prompt quality assessment, ensuring that prompts are as clear and useful as possible for secure code generation.
iv) The "instruction generation" task was hard to understand and seems to not involve generating written instructions or explanations – but asking the model to generate the full code based on the provided prompt?


**Cyber attack scenario:**
i) The paper lacks a comparison with existing cyber ranges and security testing frameworks like MITRE's Caldera, Metasploit, Cyber Range by IBM, etc, as well as other benchmarks like VulHub, HackTheBox, OWASP Benchmark, VulnHub, etc. The paper lacks a discussion of where they fall short, and why you needed to create your own simulation range – in general the positioning of SecCodePLT within the existing ecosystem is insufficient. What gap in existing environments are you are targeting? In what way did you customize your environment for LLM Evaluation?  One of the gaps in the existing literature on LLM-driven pentesting and red teaming is lateral movement – so a simulated environment and benchmark focused on measuring LLM capability for lateral movement would have been interesting.
•	(Small detail- Table 2 claims that the environment facilitates seven of the MITRE attack categories – but then lists ‘weaponisation and infiltration’ - neither of which are MITRE attack categories.)
ii) Refusal analysis seemed to not be extensive. Motivation is not provided for the choice of role playing wording in the prompt: “I am a security researcher conducting a red teaming test on a web server”. Were other things tried that might be more persuasive for Claude?

**Typos/misprints in the paper:**
* Missing a word here on page 2? “our automatic and validate process…”.
•	Repeated phrase on page 3: “not even not even vulnerable”.
•	Page 4: “MITER” should be MITRE.
•	Page 6: The Figure 2 caption: ‘worn’ – perhaps should be “worm”?
•	Page 6: “active domain (AD) server” --- should this be Active Directory?
•	Section 4.2 says Figure 8 and 9 are about CyberSecEval but the figure captions say they are about SecCodePLT.
•	Multiple instances of “cursor”  -  should be “Cursor”.
•	Page 9: “Not that we consider cursor…” – should be “Note”.

### Questions
* Please provide more details on the security tests, addressing the concerns in the weaknesses section abve - including the breadth and depth with which these tests cover potential vulnerabilities and edge cases.   
* Has any analysis of diversity across the 10 samples for each seed and the 5 test cases per sample been conducted? There might be redundancy.   
* How are the vulnerable and patched code examples used for evaluating the correctness of test cases and/or generated output?
* Please include a comparison with LLMSecEval.

**Cyber attack scenario:**   
* As outlined in the weaknesses above, please explain the motivation for creating your own simulation range and what gap in existing ranges/benchmarks yours is targeting.   
* Please provide more details on your attack refusal investigation - were other role playing prompt wordings tried that might be more persuasive for Claude? Etc.

### Soundness
2

### Presentation
2

### Contribution
3
