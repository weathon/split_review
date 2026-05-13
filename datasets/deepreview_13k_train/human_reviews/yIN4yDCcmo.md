# INS-MMBench: A Comprehensive Benchmark for Evaluating LVLMs' Performance in Insurance

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Large Vision-Language Models (LVLMs) have demonstrated outstanding performance in various general multimodal applications such as image recognition and visual reasoning, and have also shown promising potential in specialized domains. However, the application potential of LVLMs in the insurance domain—characterized by rich application scenarios and abundant multimodal data—has not been effectively explored. There is no systematic review of multimodal tasks in the insurance domain, nor a benchmark specifically designed to evaluate the capabilities of LVLMs in insurance. This gap hinders the development of LVLMs within the insurance domain. In this paper, we systematically review and distill multimodal tasks for four representative types of insurance: auto insurance, property insurance, health insurance, and agricultural insurance. We propose INS-MMBench, the first comprehensive LVLMs benchmark tailored for the insurance domain. INS-MMBench comprises a total of 2.2K thoroughly designed multiple-choice questions, covering 12 meta-tasks and 22 fundamental tasks. Furthermore, we evaluate multiple representative LVLMs, including closed-source models such as GPT-4o and open-source models like BLIP-2. This evaluation not only validates the effectiveness of our benchmark but also provides an in-depth performance analysis of current LVLMs on various multimodal tasks in the insurance domain. We hope that INS-MMBench will facilitate the further application of LVLMs in the insurance domain and inspire interdisciplinary development.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces INS-MMBench, a comprehensive benchmark designed to evaluate the performance of LVLMs in the insurance domain. It is the first initiative to systematically review multimodal tasks within the insurance sector and establish a specialized benchmark for it.

### Strengths
1. Comprehensive Benchmark: The paper presents INS-MMBench, which is the first comprehensive benchmark tailored for evaluating LVLMs in the insurance domain. This benchmark is extensive, covering 8,856 multiple-choice visual questions across 12 meta-tasks and 22 fundamental tasks, providing a robust framework for assessing LVLM capabilities in various insurance scenarios.

2. Systematic Framework: The authors have developed a systematic and hierarchical task definition that ensures the tasks are closely aligned with real-world applications in the insurance industry. This bottom-up approach to task construction enhances the benchmark's relevance and practicality, making it a valuable tool for both research and practical applications.

3. The paper also includes an extensive evaluation of multiple representative LVLMs, offering detailed performance analysis across different insurance types and meta-tasks. This analysis not only validates the effectiveness of the INS-MMBench benchmark but also provides actionable insights into the current capabilities and limitations of LVLMs in the insurance domain, guiding future research and development efforts.

### Weaknesses
1. Multi-Choice Format Limitations: This benchmark follows a similar style to MMBench and MME in the general multimodal domain, all of which formulate their questions into multiple-choice formats. While this is an effective method for evaluating model performance, it has limitations that prevent generalization to open-ended question answering, which is more representative of real-world applications. The constrained nature of multiple-choice questions may not fully capture the nuances of complex reasoning required in practical insurance scenarios. For instance, assessing damage severity often requires a nuanced description rather than a simple selection from predefined categories. This format might also encourage models to rely on superficial pattern matching rather than genuine understanding.

2. Static Benchmark and Data Leakage: The benchmark is static, which does not mitigate the data leakage problem. This will likely render the benchmark less effective in future developments. The lack of dynamic updates means that models can potentially overfit to the existing dataset, limiting their ability to generalize to new, unseen insurance scenarios. This is a critical concern, as the insurance domain is constantly evolving with new types of claims, policies, and regulations. The absence of a mechanism to refresh the benchmark with new data will reduce its long-term utility.

3. Focus on US Insurance Law and Potential Bias: The benchmark primarily focuses on insurance, specifically insurance laws from the United States. This focus may introduce bias into the evaluation process, posing a risk for models developed in different country contexts. The legal and regulatory frameworks governing insurance vary significantly across different countries. A benchmark heavily reliant on U.S.-specific laws may not accurately reflect the performance of models in other regions, thus limiting its global applicability. This bias could lead to misleading results when evaluating models trained or deployed in different legal contexts.

### Questions
Check Weaknesses.

### Soundness
3

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
The potential for Large Vision Language Models (LVLMs) to impact the insurance industry is substantial, yet largely unexplored. This study establishes a benchmark to evaluate LVLM capabilities within the domain, focusing on four main insurance types: auto, property, health, and agriculture. To create the benchmark, the authors gathered multimodal data for each insurance category from public sources and converted it into multiple-choice questions using GPT-4o. They then evaluated popular LVLMs on this benchmark to provide an initial assessment of LVLM performance and reveal current limitations in handling insurance-related content by an error analysis. Finally, the authors try to address gaps in insurance knowledge and reasoning skills by adding insurance-related information to the prompt.

### Strengths
1. The motivation behind establishing an insurance benchmark is worthwhile.  Evaluating LVLMs' capabilities on core insurance stages like underwriting and claims processing is practical and meaningful.
2. The benchmark covers a reasonable range of core insurance types relevant to key areas in everyday insurance applications.
3. The study provides an insightful error analysis, highlighting the current limitations of LVLMs in interpreting insurance-specific visual content.

### Weaknesses
 1. **Misalignment between Intent and Implementation**: While the authors claim the benchmark includes 12 meta-tasks and 22 fundamental tasks across stages like underwriting and claims processing in the Introduction section, the tasks illustrated in the paper are only loosely related to these stages. For example, meta-tasks in auto insurance such as “vehicle information extraction” and “vehicle damage detection” focus heavily on general computer vision tasks rather than directly addressing insurance-specific stages. This makes the benchmark feel more like a vision task set than an insurance task set.    
2. **Limited Accessibility for Reproducibility**: Although the authors promise to release the code and dataset, the GitHub repository has not been updated in four months, containing only a readme and a few diagrams. This lack of resources limits my ability to further assess the benchmark’s true rationality and effectiveness.
3. **Limited Novelty**: Some conclusions, such as “performance of closed-source LVLMs varies by training data size and methods,” are too general and widely understood, offering little new insight. The paper would benefit from focusing on more specific findings directly related to the insurance domain.

### Questions
Regarding the first limitation, could you share your perspective on how the current selective tasks directly align with the actual stages in the insurance process? For example, specific insurance stages like underwriting or claims processing?

I would consider slightly increasing the score if convinced that the benchmark specifically addresses key insurance stages, rather than being a collection of VQA tasks merely related to the selected insurance categories(auto, property, health, and agriculture).

### Soundness
1

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
3

### Summary
The paper presents a benchmark in the systematic evaluation of LVLMs in this field by introducing INS-MMBench, a domain-specific benchmark designed to assess these models across various insurance-related tasks.

Key contributions:

(1) INS-MMBench is the first comprehensive benchmark tailored for the insurance domain. It covers four representative types of insurance: auto, property, health, and agricultural insurance, reflecting real-world insurance scenarios such as underwriting and claims processing.

(2) The authors used a bottom-up hierarchical task definition approach to identify and refine relevant tasks for each insurance type. They collected and processed datasets to create visual question-answer pairs, ensuring that the benchmark aligns with practical applications in the insurance industry.

(3) The paper evaluates different LVLMs using INS-MMBench. The results highlight the challenges these models face and give some insights.

### Strengths
(1) Originality: INS-MMBench is the first benchmark tailored to evaluate LVLMs in the insurance domain. The authors' approach to defining tasks using a bottom-up hierarchical methodology is innovative and ensures that the benchmark aligns with real-world insurance scenarios, making it a pioneering effort in applying LVLMs to this new domain.

(2) Quality: The authors systematically identify and organize multimodal tasks across four types of insurance, and their comprehensive evaluation of ten LVLMs provides some insights. The inclusion of detailed error analysis and the exploration of prompt engineering techniques to mitigate common issues further strengthen the paper, offering practical suggestions for improving model performance.

(3) Clarity: The authors explain each step of their methodology in detail. 

(4) Significance: The introduction of INS-MMBench contributes to the field, as it enables a more nuanced evaluation of LVLMs in a domain with substantial practical applications. The benchmark could lead to improved automation in insurance-related tasks, such as claims processing and fraud detection, thus enhancing efficiency and accuracy in the industry. Moreover, by highlighting the narrowing performance gap between open-source and closed-source LVLMs, the paper encourages further research and development, potentially driving advancements in accessible and effective AI solutions for the insurance sector.

### Weaknesses
1. Benchmark Definition Lacks Depth in Insurance Scenarios

While INS-MMBench introduces tasks related to insurance, many are more aligned with general, common-sense VQA rather than specialized, nuanced scenarios seen in real-world insurance applications. To better reflect practical needs, the benchmark should include more complex tasks, such as multi-step reasoning or risk assessment based on a mix of visual and contextual data. For example, assessing the severity of vehicle damage should not only involve identifying the damaged parts but also evaluating the implications for the vehicle's structural integrity and safety, which requires a deeper understanding of automotive engineering principles and insurance-specific risk factors.

2. Overemphasis on Basic Tasks

Some tasks, like license plate recognition, are too basic and can be handled by smaller, specialized models. Evaluating LVLMs on these tasks does not showcase their strengths. Instead, the benchmark should focus on tasks requiring more advanced reasoning, such as verifying claims by cross-referencing multiple data points, including images, repair estimates, and policy details, to highlight the real capabilities of LVLMs. For instance, a more complex task could involve verifying the consistency of damage reports with photographic evidence and repair invoices, which would require the model to understand the relationships between different types of data and detect potential discrepancies.

3. Limited Emphasis on Reasoning and Higher-Order Tasks

The benchmark lacks tasks that test higher-order reasoning, which is crucial for insurance scenarios. Tasks involving contextual understanding, complex decision-making, and multi-modal integration would better evaluate how well LVLMs can handle real insurance industry challenges. For example, the benchmark could include tasks that require the model to evaluate the credibility of a claim based on the claimant's history, the circumstances of the incident, and the provided evidence, which would require the model to integrate information from multiple sources and make a judgment based on a complex set of factors.

4. Lack of Focus on Interpretability

Insurance applications require transparency, yet INS-MMBench primarily uses multiple-choice questions, limiting the ability to assess whether models can explain their decisions. Future benchmarks should include tasks that require LVLMs to provide rationale, enabling evaluation of their interpretability, which is critical for building trust in automated systems. For example, instead of just selecting the correct damage severity level, the model should be required to explain its reasoning by citing specific visual features and their implications, which would allow for a more detailed evaluation of the model's understanding and decision-making process.

5. Clarification Needed on Table 1
It appears there might be an error in the labeling of the last two rows in Table 1. Currently, "OmniMedVQA" is described as domain-specific for math, and "Mathvista" as domain-specific for medical. Given the names and typical use cases, it seems like these two may have been accidentally switched.

### Questions
1. Can you provide more details on how the benchmark tasks were selected?

It would be helpful to understand the criteria used to determine which tasks were included in INS-MMBench. Specifically, how did you ensure that the tasks accurately reflect real-world insurance challenges and not just general visual recognition problems?

2. Have you considered including more complex, multi-step reasoning tasks?

Given the importance of decision-making in insurance, would it be possible to expand the benchmark to include tasks that require multi-modal integration and reasoning (e.g., verifying a claim using images, text descriptions, and numerical data)? This could better showcase the strengths and weaknesses of LVLMs in handling real-world scenarios.

3. How do you envision improving the interpretability of model evaluations?

Since explainability is critical in insurance, have you considered adding tasks that require LVLMs to provide justifications or rationales for their answers? This could allow for a deeper evaluation of how well models understand and explain their decisions, which is crucial for real-world applications.

4. Do you have insights on the performance gap between open-source and closed-source models?

The results indicate a narrowing gap between open and closed-source models. Can you elaborate on specific factors contributing to this trend, and how future benchmarks might encourage more competitive open-source solutions?

### Soundness
3

### Presentation
3

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
This work introduces INS-MMBench, the first comprehensive benchmark designed to evaluate LVLMs in the insurance domain. INS-MMBench includes four insurance types: auto, property, health, and agriculture, and includes 8856 multiple-choice questions across 12 meta-tasks and 22 fundamental tasks. It is designed to evaluate LVLMs in practical insurance tasks, such as vehicle damage detection and health risk monitoring, combining real-world visual information with insurance-specific questions. Through the experiments, the authors show the current limitations of LVLMs in insurance domain and suggests targeted data and domain knowledge for improving the performance.

### Strengths
- The paper is well-written and well-organized. 
- This is the first systematic benchmark specifically designed for the LVLMs evaluation in the insurance domain and fills a gap in the current benchmark that often overlooks domain-specific applications.
- The experiments are comprehensive, and thorough error analysis categorizing different types of model failures is provided in the paper.

### Weaknesses
 - The human baseline experiments only involve 3 graduate students specialized in insurance, which is a small sample size.  This might not accurately represent the range of expertise and variability in the real-world insurance evaluations. I would suggest bringing in more experts from the industry to help perform the human evaluation. 
- This work does not discuss potential biases in the data sources or methods for mitigating them, which means that there is a risk that the benchmark may favor certain model behaviors or fail to generalize to different insurance scenarios.

### Questions
- How do LVLMs perform on insurance tasks that related to temporal reasoning for example analyzing claim patterns over time? The work evaluates static image understanding, but many insurance tasks require understanding temporal relationships and changes over time, and it seems that those samples are missing from the current benchmark.

### Soundness
3

### Presentation
3

### Contribution
3
