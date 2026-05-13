# BlackDAN: A Black-Box Multi-Objective Approach to Effective and Contextual Jailbreaking of Language Models

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
While large language models (LLMs) exhibit remarkable capabilities across various tasks, they encounter potential security risks such as jailbreak attacks, which exploit vulnerabilities to bypass security measures and generate harmful outputs. Existing jailbreak strategies mainly focus on maximizing attack success rate (ASR), frequently neglecting other critical factors, including the relevance of the jailbreak response to the query and the level of stealthiness. This narrow focus on single objectives can result in ineffective attacks that either lack contextual relevance or are easily recognizable. In this work, we introduce BlackDAN, an innovative black-box attack framework with multi-objective optimization, aiming to generate high-quality prompts that effectively facilitate jailbreaking while maintaining contextual relevance and minimizing detectability. BlackDAN leverages Multiobjective Evolutionary Algorithms (MOEAs), specifically the NSGA-II algorithm, to optimize jailbreaks across multiple objectives including ASR, stealthiness, and semantic relevance. By integrating mechanisms like mutation, crossover, and Pareto-dominance, BlackDAN provides a transparent and interpretable process for generating jailbreaks. Furthermore, the framework allows customization based on user preferences, enabling the selection of prompts that balance harmfulness, relevance, and other factors. Experimental results demonstrate that BlackDAN outperforms traditional single-objective methods, yielding higher success rates and improved robustness across various LLMs and multimodal LLMs, while ensuring jailbreak responses are both relevant and less detectable.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The manuscript presents an investigation into jailbreaking attacks on large language models (LLMs) and introduces a novel approach aimed at enhancing the success rate of such attacks. The authors employ Multi-Objective Evolutionary Algorithms (MOEAs) to advance the field of black-box attacks on LLMs. The introduction offers some intriguing insights; however, the paper could benefit from a more accurate illustration of the methodology and a comprehensive discussion of related work. Additionally, the clarity of the experimental visualizations could be improved. While the paper is informative and presents interesting concepts, it may require further refinement before it meets the publication standards of a top-tier conference.

### Strengths
1. The paper provides numerous visualizations, which serve as a valuable supplement to the textual content.
2. The introduction of Multi-Objective concepts to enhance attack efficiency in this domain is innovative and represents a promising direction for future research.

### Weaknesses
1. There appears to be some redundancy between the second and third paragraphs of the introduction. Furthermore, the limitations identified in the study are not substantiated by references, which would lend credibility to these claims.
2. The issues highlighted in the introduction (Figure 1) as examples require more thorough exploration in the subsequent sections. The current version seems insufficient to fully address these concerns.
3. The paper makes broad assertions regarding its extensibility to various goals. While it demonstrates effectiveness for the goals discussed, the potential for broader applicability warrants additional investigation. Since the techniques used in many-objective optimization are not trivial, and no evidence can prove the author can extend the method to other goals, it is not convincing.
4. The literature review could be more focused, particularly in distinguishing between traditional adversarial machine learning and LLM-specific black-box attacks. The current version's black-box attack references encompass a wide range of traditional adversarial machine learning literature, which may not be directly relevant to LLM-specific attacks.
5. The methodology section would benefit from a clearer depiction of the proposed approach. While a figure is provided, a more detailed explanation would enhance reader comprehension.
6. In Section 3.2, the use of established algorithms such as NSGA-II should be framed as an application rather than a novel technical contribution. The delineation between preliminary concepts and the core technical contributions could be more precise.
7. The experimental setup should include a description of the computational resources used, as this context is essential for assessing the reported time consumption.
8. The paper employs the concept of Pareto ranks without adequate explanation. Given that this may not be familiar to all readers, a definition and context within the NSGA-II algorithm would be beneficial.
9. The visualizations presented would be more impactful if accompanied by in-depth interpretations that provide further insights.

### Questions
1. Could the authors clarify the overlap in the introduction and ensure that the limitations discussed are supported by relevant literature?
2. Would it be possible to expand on the examples introduced in the introduction throughout the subsequent sections? What is the connection of the two mentioned goals and later introduced fitness functions?
3. The authors are encouraged to substantiate the claim of extensibility with additional empirical evidence or theoretical discussion.
4. A more targeted literature review that focuses on LLM-specific black-box attacks would be valuable.
5. A detailed walkthrough of the methodology, possibly supplemented by a step-by-step figure or flowchart, would greatly aid in understanding the proposed approach.
6. Clarification on the use of established algorithms and their role in the research would help distinguish between the foundational and novel aspects of the work.
7. Providing details on the computational resources used in the experiments would lend context to the time consumption results.
8. An explanation of Pareto ranks and their relevance to the study would be beneficial for readers unfamiliar with the concept
9. Finally, the authors might consider enhancing the visualizations with more comprehensive explanations to better support the narrative of the paper.

### Soundness
3

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
The paper presents an interesting approach, leveraging both white-box and black-box attacks on LLMs, with a focus on semantic consistency in adversarial examples. However, there are several areas of concern that need to be addressed before the work can be considered for publication. Specifically, the novelty of the approach is limited, and there are significant gaps in the related work, justification of experimental choices, and analysis of the method's effectiveness.

Strengths:
* The use of LLMs in both white-box and black-box attacks is timely and relevant to current trends in adversarial research.
* The paper attempts to address semantic consistency in adversarial attacks, an important challenge for generating adversarial examples that remain meaningful to humans.

Weaknesses:

1. Related Work:
The related work section is notably underdeveloped. There is a significant omission of important prior work, particularly on black-box attacks that do not utilize LLMs. For example, well-known black-box attack methods like Jailbreaking Black Box Large Language Models in Twenty Queries, Open Sesame! Universal Black Box Jailbreaking of Large Language Models,  All in How You Ask for It: Simple Black-Box Method for Jailbreak Attacks, Tree of Attacks: Jailbreaking Black-Box LLMs Automatically, are absent from the discussion, despite their relevance. Furthermore, the concept of Semantic Consistency, which seems to be borrowed from Open Sesame! Universal Black Box Jailbreaking of Large Language Models has not been properly cited.

2. Use of Older LLMs:
The paper relies on relatively older LLMs, such as LLaMA-2, despite the fact that newer, more advanced models have been released recently. This weakens the relevance of the results, as it is unclear how the proposed attack method would perform on state-of-the-art models. Since LLMs are evolving rapidly, the use of older models may limit the paper’s impact.

3. Success Indicator:
The choice of using "5" as the success indicator using GP4-Judge is not well justified. It’s unclear why this specific number was chosen or what theoretical or empirical basis supports this decision. This arbitrary threshold weakens the rigor of the evaluation.

4. Computational Overhead:
The paper does not provide a detailed analysis of the computational overhead associated with the proposed attack. Since adversarial attacks can be resource-intensive, understanding the computational cost is crucial for assessing the practicality of the method.

5. Novelty:
The novelty of the work is limited. While the switch from a GA algorithm to NSGA is noted, this change does not represent a significant leap in innovation. Similar work already exists in the literature, and the proposed approach seems like an incremental improvement rather than a novel contribution.

6. Lack of Ablation Study:
There is no ablation study in the paper to understand the contribution of individual components of the method. Without such analysis, it is difficult to assess which parts of the approach are most important for its success.

7. Hyperparameter Selection:
The paper does not provide sufficient details on how the hyperparameters were chosen. This is critical in understanding the generalizability and robustness of the proposed method. Were these values selected based on empirical experimentation, or were they adopted from prior work?

Overall Recommendation:
Weak Reject

While the paper addresses a timely topic and proposes an approach that could be of interest, significant revisions are required. The lack of an ablation study, the absence of justification for hyperparameter choices, the underdeveloped related work section, and the limited novelty of the method collectively weaken the paper’s contribution. With substantial improvements in these areas, the paper could be a stronger contribution to the field.

### Strengths
* The use of LLMs in both white-box and black-box attacks is timely and relevant to current trends in adversarial research.
* The paper attempts to address semantic consistency in adversarial attacks, an important challenge for generating adversarial examples that remain meaningful to humans.

### Weaknesses
* Novelty: The novelty of the work is limited. While the switch from a GA algorithm to NSGA is noted, this change does not represent a significant leap in innovation. Similar work already exists in the literature, and the proposed approach seems like an incremental improvement rather than a novel contribution.

* Use of Older LLMs: The paper relies on relatively older LLMs, such as LLaMA-2, despite the fact that newer, more advanced models have been released recently. This weakens the relevance of the results, as it is unclear how the proposed attack method would perform on state-of-the-art models. Since LLMs are evolving rapidly, the use of older models may limit the paper’s impact.

* Computational Overhead and lack of ablation study:
The paper does not provide a detailed analysis of the computational overhead associated with the proposed attack. Since adversarial attacks can be resource-intensive, understanding the computational cost is crucial for assessing the practicality of the method. There is no ablation study in the paper to understand the contribution of individual components of the method. Without such analysis, it is difficult to assess which parts of the approach are most important for its success.

### Questions
* Ablation Study: Could you provide an ablation study to demonstrate the impact of individual components of your method on the overall performance of the attack? This would help in understanding which aspects of your approach contribute most significantly to its effectiveness.

* Hyperparameter Selection: Can you clarify how you selected the hyperparameters for your method? It would be helpful to know whether these values were chosen based on empirical experimentation or adopted from prior work. Additionally, could you discuss the sensitivity of your results to different hyperparameter settings to assess the robustness of your approach?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Apart from ASR, existing jailbreak attacks frequently neglect other critical factors, including the relevance of the jailbreak response to the query. This paper introduces BlackDAN, which leverages NSGA-II algorithm to jailbreak LLMs and achieves multi-objective optimization, including the effectiveness of attack and the semantic consistency. Authors have conducted comprehensive experiments to prove the effectiveness of BlackDAN.

### Strengths
1. The experimental part is comprehensive, and the authors have fully proved the ASR improvements.
2. The introduction of NSGA-II is reasonable, which allows the integration of other fitness functions.

### Weaknesses
1. More technical background about NSGA-II and the detailed description about Algorithm 1&2 are recommended to be provided.

2. As a common operation in the area of jailbreaking, considering only two genetic operations is not comprehensive enough [1]. This may be the reason why some results in Table 1 and Figure 3 are not satisfied enough. Additionally, this paper lacks the citation of some other jailbreak attacks which also leverages genetic algorithm [2, 3].

3. In line 24-26 of the abstract, authors claim that BlackDAN leverages MOEAs to optimize “stealthiness”, but this has not been proved in the experimental part and seems like an over-claim.

4. The experimental section lacks a standard metric (like ASR) to fully demonstrate the semantic consistency between the jailbreak prompt and outputs.

[1] GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts.
[2] Semantic Mirror Jailbreak: Genetic Algorithm Based Jailbreak Prompts Against Open-source LLMs.
[3] Open Sesame! Universal Black Box Jailbreaking of Large Language Models.

### Questions
1. See weakness 2. Why the authors do not leverage various genetic operations? Are there any contradictions between them and existing genetic operations?

2. See weakness 4. Are there any actual evidences to prove that BlackDAN enhances the readability/ usefulness of the jailbreaking outputs?

### Soundness
3

### Presentation
3

### Contribution
2
