# ChaosEater: Fully Automating Chaos Engineering with Large Language Models

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 5, 5, 6

## Abstract
Chaos Engineering (CE) is an engineering technique aimed at improving the resiliency of distributed systems.
It involves artificially injecting specific failures into a distributed system and observing its behavior in response. 
Based on the observation, the system can be proactively improved to handle those failures.
Recent CE tools realize the automated execution of predefined CE experiments.
However, defining these experiments and reconfiguring the system after the experiments still remain manual.

To reduce the costs of the manual operations, we propose ChaosEater, a "system" for automating the entire CE operations with Large Language Models (LLMs).
It pre-defines the general flow according to the systematic CE cycle and assigns subdivided operations within the flow to LLMs.
We assume systems based on Infrastructure as Code (IaC), wherein the system configurations and artificial failures are managed through code.
Hence, the LLMs' operations in our "system" correspond to software engineering tasks, including requirement definition, code generation and debugging, and testing.

We validate our "system" through case studies on both small and large systems.
The results demonstrate that our "system" significantly reduces both time and monetary costs while completing a reasonable CE cycle.
Our code is available in the Supplementary Material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a framework for automated testing and improving Infrastructure-as-Code systems based on Kubernetes. It follows the Chaos Engineering (CE) approach, which observes how the system reacts to artificially injected deficiencies. Based on configuration files, manifests, etc., the framework automatically analyzes to identify the normal behavior, then modifies the configuration and checks whether the system behavior degrades significantly, and, if necessary, modifies the system configuration to make the system more resilient.

The approach essentially boils down to using scripts to connect existing CE tools and having LLMs figure out parameters and code modifications as required. I'm not an expert in CE, so I don't know how hard that is. I welcome that the authors did make an effort to insert verification and validation steps to ensure the soundness of the approach. All in all, this seems like a promising step in applying LLMs to an interesting problem in software engineering.

### Strengths
The approach essentially replaces a human CE engineer with a combination of scripts and LLM input to implement the required tests and modifications. The entire workflow is highly automated so that with enough computational resources, one could imagine the system finding and fixing a variety of problems all by itself. This might bring considerable cost reductions, at least under the assumption that compute costs will decline rapidly in the future (and LLM power will increase).

### Weaknesses
The paper says little about the exhaustiveness of the approach. Given infinite time, would the system be expected to find the majority of relevant faults? The case study seems relatively simple, and even in such an idealized case, two different solutions are proposed, and it does not seem clear which one is preferable. I can imagine that this problem of choosing between alternatives is much worse in more complex systems. The authors admit in the discussion that it is not trivial to scale this to challenging tasks, and I applaud their intellectual honesty. The paper also lacks a clear explanation of how the system handles situations where multiple potential solutions are identified, and how it decides which one to implement. The case study, while illustrative, does not provide sufficient evidence that the system can handle the complexities of real-world infrastructure-as-code deployments. The lack of a systematic approach to evaluating the coverage of the generated chaos experiments is also a concern. It is unclear how the system ensures that all critical failure modes are explored, rather than just a subset of easily detectable issues. Furthermore, the paper does not discuss the potential for the LLM to introduce unintended side effects through its modifications, and how such risks are mitigated.

### Questions
- How are thresholds calculated from the inspected values (margin for natural fluctuations…)?
- Why is the temperature of the LLM set to zero? Doesn't this limit the creativity (or exhaustiveness, depending on the time budget) in devising chaos experiments?
- How can you be sure that VaC scripts work as intended (e.g., rather than just always giving positive results)? For example, you could voluntarily use thresholds that are too low to check that they give negative results when necessary.
- In the case study, the analysis phase presented two solutions: changing the restart policy or using a Deployment resource. Why was the latter solution chosen in the improvement phase? What are the perceived upsides/downsides? How about the actual upsides/downsides of this solution? E.g., does introducing three replicas increase the overall cost of operating the system?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a framework for automating Chaos Engineering (CE) workflows using LLMs. The system, ChaosEater uses multi-step, multi-agent workflow to generate hypotheses, inject failures, run experiments, analyze output, suggest improvements and repeat until Validation as Code passes. Chaos Eater may automate CE in Kubernetes (K8s) environments managed with Infrastructure as Code (IaC).

**Architecture**: The system consists of five primary phases:
   - **Pre-processing**: Processes configuration dependencies.
   - **Hypothesis Definition**: Defines system resilience criteria (steady states) and specifies failure scenarios for testing.
   - **Experimentation**: Conducts chaos experiments by injecting pre-defined failures while validating steady states in real-time.
   - **Analysis**: Reviews the experiment results to assess whether the system meets the resilience hypothesis.
   - **Improvement**: If the hypothesis is not satisfied, reconfigures the system accordingly and repeats the experimentation phase.

### Strengths
1. **CE Automation**: ChaosEater attempts full automation of Chaos Engineering, covering hypothesis generation, fault injection, and iterative system improvement using LLMs and agentic architecture.
2. **Well Defined Architecture**: Authors clearly define the architecture of the system and LLMs/agents that work in each of the parts.
3. **Demonstrated Case Study**: System is demonstrated on a case study with a Kubernetes-managed Nginx server system.
4. **Cost and Time Efficiency**: The system would significantly reduce the time and costs associated with manual CE processes.
5. **Validation as Code (VaC)**: Provides a transparent and consistent method for validating system resilience.

### Weaknesses
### Weaknesses
1. **Demonstrated on Toy System Only**: System has been demonstrated on a toy system with a very simple failure. It is not known if system will work well on actual large systems. Could you show results of experiments on a benchmark set or on larger systems? Also see weakness 2.
2. **Challenge in Vulnerability Discovery**: The system may not be able to identify issues in already resilient systems, where fault discovery requires deeper analysis.
3. **Limited to Development Environments**: Currently operates only in development environments. Additionally, CHAOSEATER struggles to uncover vulnerabilities in systems that are already resilient.
4. **Limited to Configuration Improvements**: If I understand correctly, only K8s configuration scripts can be changed in the system improvement step. In other words, the system does not automatically change the tested system code. This is a significant limitation, although I understand that currently LLMs may not be able to automatically change the tested system code to improve resiliency.

### Questions
Figure 7 is unreadable while taking a whole page – please replace with something that serves better in presenting the system.

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
4

### Summary
The paper proposes a system, called CHAOSEATER, that automates the entire Chaos Engineering (CE) cycle using LLMs to enhance the resilience of distributed systems. It defines a structured CE process with five phases: hypothesis setting, chaos experimentation, analysis, improvement, and final review. CHAOSEATER using Infrastructure as Code (IaC) to manage system configurations. The paper show the proposed system help in reducing the time and cost compared to manual CE

### Strengths
1- The paper demonstrates how LLMs contribute to reducing time and costs in Chaos Engineering (CE).

2- The paper is well-written and includes clear figures and visualizations.

### Weaknesses
1- Clearly differentiate your fully automated technique for Chaos Engineering (CE) using LLMs from existing approaches like self-refinement and self-debugging. Provide specific details on what sets your method apart and its unique contributions.

2- Include accuracy metrics in Table 1 to present success and failure rates alongside time and cost. This will offer a more comprehensive view of the technique's effectiveness.

3- To position this work as a foundational effort in automating system resilience improvement, construct a larger dataset, establish robust evaluation metrics for correctness, and include baseline comparisons with prior automated approaches using LLMs.

4- Add a qualitative analysis and human evaluation component to assess the effectiveness of LLMs in Chaos Engineering tasks. This will strengthen the paper by showing how well LLMs perform in real-world scenarios.

### Questions
If the paper proposes an automated system for Chaos Engineering (CE), consider constructing a benchmark to evaluate multiple LLMs and compare different automated approaches. This could provide a more comprehensive assessment of the system's effectiveness and highlight its unique contributions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The author proposes a system called ChaosEater, primarily designed to automate the Chaos Engineering (CE) workflow using LLMs. It provides an efficient and low-cost solution for maintaining system resilience, offering potential for automated resilience testing and fault remediation in future complex distributed systems.

### Strengths
The article leverages LLMs to automate various stages of chaos experiments, thereby reducing manual operations. This innovative application demonstrates the potential of LLMs in infrastructure-as-code and fault injection testing, showcasing a degree of novelty.

### Weaknesses
1.The current version of ChaosEater relies on LLMs to handle complex input and output, particularly in multi-stage and multi-dependency chaos experiments, which can be susceptible to context length limitations. Even with models like GPT-4, longer contexts may still lead to information truncation, affecting the accuracy and comprehensiveness of the experiments. Specifically, the system's ability to maintain a coherent understanding of the experiment's state across multiple stages and dependencies is questionable, as LLMs may struggle with long-term dependencies and complex relationships between injected faults and system responses. This could lead to inaccurate planning and execution of experiments, particularly in scenarios involving cascading failures or intricate fault injection sequences.
2.The types of failures and injection methods currently supported by ChaosEater may be too limited to cover all potential faults in distributed systems. For example, the system may lack support for specific failure injections related to storage systems, such as disk latency or database locking, as well as certain network issues like packet loss and jitter. Furthermore, the paper does not mention support for various complex and dynamic failure scenarios, such as cross-injection of multiple faults, cascading failures, or the failure of partially dependent components, all of which are quite common in complex systems. While the system may support basic fault injections, it does not appear to handle the more nuanced and realistic failure scenarios that are critical for thorough resilience testing. The system's reliance on K8s manifest changes for remediation also limits its ability to address failures that require application-level or other backend layer modifications.
3.Chaos experiments typically require real-time monitoring and response to system states to promptly terminate the experiment in the event of severe anomalies or catastrophic failures. However, the paper does not mention that ChaosEater has such real-time monitoring capabilities, which limits its ability to dynamically adjust strategies during the experiment. The lack of real-time monitoring and dynamic adjustment capabilities means that the system may not be able to react to unexpected system behaviors or severe anomalies, potentially leading to prolonged disruptions or even catastrophic failures during experiments. This limitation is particularly concerning in complex distributed systems where the impact of fault injections can be unpredictable.

### Questions
The main points and issues have been outlined in the "Weaknesses" section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes ChaosEater, an automatic framework for Chaos Engineering (CE) operators. In particular, each CE operator is automated using one or multiple LLM agents, equipped with carefully crafted system/user/AI prompts. The experimental results demonstrate that the proposed system significantly reduces both time and monetary costs within the CE cycle.

### Strengths
- The paper presents an intriguing application of LLM agents in improving distributed system resilience.
- The framework effectively automates the CE process, minimizing the need for manual intervention.
- The authors provide the implementation of the proposed methods, which could be beneficial to the research community.
- The paper is well-organized, with a clear and logical flow.

### Weaknesses
 - It is unclear to what extent ChaosEater reduces the reliance on human expertise. For example, steady-state selection still requires experts to define measurable states, with the agent only used for state selection.
- Both steady-state selection and failure injection are determined by LLM agents, whose inherent biases could hinder the discovery of new issues. 
- Figure 7 is difficult to comprehend; it could be better to include a summarized version in the main text and move the detailed figure to the Appendix.
- The experiments seem limited to a toy example, which may not fully demonstrate the effectiveness of ChaosEater.

### Questions
- Is the LLM primarily used in most phases to adjust parameters within predefined templates (e.g., fault scopes)? Could a smaller model be employed in the experiment instead?
- The prompts in ChaosEater appear to be carefully designed, resulting in well-structured LLM responses. I suggest providing some detailed prompts in the Appendix. 
- In addition, what is the cost of prompt tuning, and can the agent maintain robustness when using other LLM models or in different environments?

### Soundness
2

### Presentation
4

### Contribution
2
