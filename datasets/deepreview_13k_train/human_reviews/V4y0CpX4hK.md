# Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Although LLM-based agents, powered by Large Language Models (LLMs), can use external tools and memory mechanisms to solve complex real-world tasks, they may also introduce critical security vulnerabilities. However, the existing literature does not comprehensively evaluate attacks and defenses against LLM-based agents. To address this, we introduce Agent Security Bench (ASB), a comprehensive framework designed to formalize, benchmark, and evaluate the attacks and defenses of LLM-based agents, including 10 scenarios (e.g., e-commerce, autonomous driving, finance), 10 agents targeting the scenarios, over 400 tools, 23 different types of attack/defense methods, and 8 evaluation metrics. Based on ASB, we benchmark 10 prompt injection attacks, a memory poisoning attack, a novel Plan-of-Thought backdoor attack, a mixed attack, and 10 corresponding defenses across 13 LLM backbones with nearly 90,000 testing cases in total. Our benchmark results reveal critical vulnerabilities in different stages of agent operation, including system prompt, user prompt handling, tool usage, and memory retrieval, with the highest average attack success rate of 84.30\%, but limited effectiveness shown in current defenses, unveiling important works to be done in terms of agent security for the community.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a comprehensive framework for assessing the security vulnerabilities in agents powered by Large Language Models (LLMs). The ASB framework aims to systematically test and evaluate different adversarial attacks and defense mechanisms for LLM-based agents across various operational scenarios, including e-commerce, autonomous driving, and finance. It provides benchmarks for ten agents, over 400 tools, multiple attack methods (such as prompt injection, memory poisoning, and backdoor attacks), and eight security metrics to assess effectiveness.

### Strengths
- The ASB framework is comprehensive, covering diverse attack types (e.g., prompt injection, memory poisoning, backdoor) and multiple defense strategies. ASB includes ten distinct agent scenarios, each with tools and tasks tailored for real-world applications.
- It provides structured metrics, such as Attack Success Rate (ASR) and Refuse Rate (RR), to evaluate the effectiveness of both attacks and defenses.
- The results of Figure 2 is interesting. Larger Models Tend to be More Fragile.
- Extensive experimental validation highlights critical vulnerabilities and the limitations of existing defenses.
- The opensource code is easy to use

### Weaknesses
The article lacks a critical analysis of the new findings and fails to compare the results with those of previous similar studies. For instance, in the text"Larger Models Tend to be More Fragile," the author states, "We visualize the correlation between backbone LLM leaderboard quality (Analysis, 2024) and average ASR across various attacks in Fig. 2. Larger models usually have higher ASR because their stronger capabilities make them more likely to follow attacker instructions." If the conclusion is as simplistic as this, the article becomes somewhat meaningless, merely assessing the differences in LLM capabilities. Although there appear to be some results from no-attack scenarios in the appendix, the author should consider presenting them alongside the ASR results. Alternatively, ASR should only be considered after the LLM successfully executes a task in a no-attack scenario. I hope to see results that combine ASR with no-attack scenarios in the rebuttal, along with more in-depth analysis.

### Questions
check the weakness

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an evaluation suite for attacks against LLM-based agents, and corresponding defenses. The suite includes evaluations for direct prompt injection attacks, observation prompt injection attacks, memory (RAG) poisoning attacks, and "Plan-of-Thought" backdoor attacks, a new attack introduced in this paper where the adversary places a backdoor in the system prompt. After formalizing the different attack vectors, the paper evaluates the effectiveness several attacks in the different scenarios (including a scenario where multiple vectors are used at the same time), and evaluates the effectiveness of several defenses.

### Strengths
This paper examines an important and timely area investigating security vulnerabilities in LLM systems. The authors evaluate and analyze a comprehensive set of both attack vectors and relative defenses, providing extensive testing coverage. Additionally, the paper makes a valuable contribution by unifying different types of prompt injection and poisoning attacks under a single cohesive framework for analysis (including an attack which leverages the different attack vectors, which this works shows to be very effective).

### Weaknesses
- Why do the authors introduce the concept of "Observation Prompt Injections" when there is already the term "Indirect Prompt Injection" which is commonly used in the literature?
-The motivation of PoT Attacks is unclear: what's an example of an adversary who controls the system prompt but not API? If the adversary is the API provider, there is nothing the user can do as the adversary can just make the API output arbitrary actions based on the inputs.
- The evaluation is not necessarily the most realistic as the authors don't use the official APIs but rather the ReAct framework.
- The paper does not provide a clear explanation of how the ASR and the performance not under attack (PNA) are computed. Do you check the actions taken by the agent? Do you observe changes in the state?
- What is the difference between PNA and BP in the metrics? In general, the authors introduce a lot of metrics, but barely show results with them.
- The utility of the defenses and of the models is unclear. This is only shown in the appendix, but should be highlighted in the main text. Moreover, how is it possible that some models have very low "PNA" (e.g., Gemma2-9B)
- The direct prompt injection attack scenario is unrealistic as the adversary is assumed to control the full user prompt, which is an inherently under-defined and unsolvable problem. There is no way to distinguish between the user's instructions and the adversary's instructions when the adversary has full control of the user prompt. This makes the attack trivial and uninteresting.
- The benchmark does not check for the correctness of the tool call arguments, which is important to evaluate the actual utility of the models. The benchmark only checks if a tool has been called, not if it has been called with the expected arguments. This makes the evaluation less realistic and less useful.
- The benchmark does not provide a realistic challenge for attacks, as the attacks are too easy to solve. The adversary only needs to get the model to call a tool, not to call it with specific arguments. This explains why some attacks have such high ASR.

### Questions
- What's your intuition for the fact that many models have higher ASR than performace without attacks?
- What do you mean by "Additionally, to simplify the tool-calling process, we did not set parameters for the tools, as we believe the ability of a model to set parameters, e.g., generating JSON format data, falls within the model’s capabilities, rather than its security framework." in the appendix? How do you parse the model outputs and transform them in actions?
- The appendix mentions "simulating tool calls". What do you mean by that?

See weaknesses for other questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Agent Security Bench (ASB), a benchmark for evaluating security vulnerabilities in LLM-based agents. ASB considers four main types of attacks: Direct Prompt Injection (DPI), Observation Prompt Injection (OPI), Memory Poisoning, and a novel Plan-of-Thought (PoT) Backdoor attack. The benchmark includes varying scenarios, agents and tools, and evaluates 23 different attack/defense methods across various LLMs. The experimental results show that LLM-based agents are vulnerable to various malicious manipulations at different stages.

### Strengths
+ The paper presents a comprehensive evaluation framework covering a range of attacks, metrics, models, and scenarios.
+ It systemizes various attacks at different stages of LLM-based agents.
+ The evaluation considers nearly 90,000 test cases, quantifying the vulnerabilities of existing LLM-based agents.

### Weaknesses
 + The new insights provided by the evaluation are limited. The main conclusion that LLM-based agents are vulnerable to various malicious manipulations at different stages is not new. It has been validated in previous studies. I expect to see that developing a comprehensive evaluation platform can provide new insights, which are impossible otherwise. For example, through a comparative study of different attacks/defenses, it may highlight their strengths/limitations and outline their design spectrums.

+ While the paper examines individual attack vectors at different stages of agent operation, it could benefit from a deeper exploration of attack interplay. Although the paper briefly discusses "Mixed Attacks," a more systematic investigation of attack combinations could reveal important vulnerabilities. For instance, simultaneous deployment of prompt injection and memory poisoning attacks might create compound effects that more accurately reflect real-world threat scenarios.

+ The experimental evaluation contains design choices that warrant further justification. For example, the simulated tool calls rather than real-world APIs might not fully capture real-world vulnerabilities. The choice of the 20-line threshold for determining attack success seems somewhat arbitrary. Please justify these design choices in more detail.

+ The paper could better address how its findings translate to real-world deployment scenarios. While the paper identifies the ineffectiveness of current defenses, it doesn't propose substantial new defense mechanisms. Further, the analysis of why current defenses fail could be more detailed. It's suggested to discuss potential paths forward for developing more effective defenses.

### Questions
Please see the detailed comments above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Agent Security Bench (ASB), a comprehensive framework for evaluating LLM-based agents’ security vulnerabilities and defense mechanisms. ASB covers ten real-world scenarios (e.g., e-commerce, finance), ten corresponding agents, over 400 tools, and various attack methods (e.g., prompt injections, memory poisoning). The framework benchmarks attacks and defenses across 13 LLMs with nearly 90,000 testing cases, and the results reveal critical security vulnerabilities, such as a high average attack success rate of 84.30%. The study formalizes attack and defense strategies (such as Direct Prompt Injections and Memory Poisoning). Overall, the study constitutes a solid contribution to shed more light on the security of LLM-based agent systems.

### Strengths
- The ASB framework is extensive and includes many tasks, tools, and agent types. It introduces a broad attack/defense evaluation scheme relevant to the growing field of LLM-based agents.
- The paper introduces a Plan-of-Thought (PoT) Backdoor Attack, which is novel in targeting the hidden system prompt. This introduces a unique avenue of attack compared to the more commonly known Direct Prompt Injection (DPI) and Observation Prompt Injection (OPI). The new attack vector highlights an important vulnerability and contributes to the community.
- The large-scale testing (90,000 cases) across multiple model versions and providers, including different scenarios, provides good evidence of the study’s validity. It’s great that the benchmark tests cover multiple model types and versions.
- The formalization of various attacks (e.g., Direct Prompt Injection, Memory Poisoning, Plan-of-Thought Backdoor) provides a clear, mathematical framework for understanding how the vulnerabilities manifest in LLM-based agents. This level of precision enables reproducibility and creates a foundation for further exploration of attack vectors in future research. 
- The defense mechanisms, particularly paraphrasing and PPL detection for prompt injections, are interesting and seem worthy of discussion of securing LLM agents.

### Weaknesses
 - The included metrics (ASR, RR, etc.) are valuable, but the heavy reliance on quantitative results can obscure the qualitative insights. More qualitative analysis of specific attack case studies or real-world applicability would deepen the understanding of how these vulnerabilities manifest in practice. Specifically, how and why certain attacks are successful in specific scenarios. For instance, in practical settings, the factors leading to a high ASR might vary based on agent behavior or task context, which is not easily explained through raw numbers alone. A case study focusing on one scenario in detail (e.g., e-commerce agents) could show how vulnerabilities are exploited and why defenses like paraphrasing might succeed or fail in that context.
- Related to the above remark, in real-world applications, security vulnerabilities often arise due to specific conditions—such as interaction with third-party tools or nuanced prompt handling mechanisms—that may not be fully captured by numerical metrics. For example, ASR might indicate high vulnerability to memory poisoning, but it does not explain the operational context in which memory poisoning is particularly damaging or stealthy. Highlighting qualitative aspects, such as the role of human oversight in detecting poisoned memory or how task context influences tool usage, would give the reader a deeper understanding of the agent's security posture.
- The paper mentions existing benchmarks like InjecAgent and AgentDojo, but it could elaborate on the comparison between them and further explain the prior benchmarks’ limitations versus the advances made by ASB. 
- The evaluation results indicate limited effectiveness in preventing attacks. In particular, the Plan-of-Thought backdoor defense strategy seems underexplored to mitigate attacks. Stronger practical suggestions for defenses would increase the paper’s net positive impact on the defensive community.

### Questions
- Have you considered more advanced defense mechanisms, such as dynamic prompt rewriting or context-aware anomaly detection? What challenges do you foresee in implementing stronger defenses, particularly in balancing effectiveness and maintaining agent performance?
- Can you elaborate on how the vulnerabilities identified in the benchmark manifest in real-world applications? For example, how would a memory poisoning or mixed attack affect a specific real-world use case, such as financial services or autonomous driving?

### Soundness
4

### Presentation
3

### Contribution
3
