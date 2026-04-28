# MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Multimodal foundation models (MMFMs) play a crucial role in various applications, including autonomous driving, healthcare, and virtual assistants. However, several studies have revealed vulnerabilities in these models, such as generating unsafe content by text-to-image models. Existing benchmarks on multimodal models either predominantly assess the helpfulness of these models, or only focus on limited perspectives such as fairness and privacy. In this paper, we present the first unified platform, MMDT (Multimodal DecodingTrust), designed to provide a comprehensive safety and trustworthiness evaluation for MMFMs. Our platform assesses models from multiple perspectives, including safety, hallucination, fairness/bias, privacy, adversarial robustness, and out-of-distribution (OOD) generalization. We have designed various evaluation scenarios and red teaming algorithms under different tasks for each perspective to generate challenging data, forming a high-quality benchmark. We evaluate a range of multimodal models using MMDT, and our findings reveal a series of vulnerabilities and areas for improvement across these perspectives. This work introduces the first comprehensive and unique safety and trustworthiness evaluation platform for MMFMs, paving the way for developing safer and more reliable MMFMs and systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MMDT (Multimodal DecodingTrust), the first unified platform for comprehensive safety and trustworthiness evaluation of multimodal foundation models (MMFMs). Unlike existing benchmarks that primarily assess helpfulness or focus on limited aspects such as fairness and privacy, MMDT evaluates MMFMs across multiple dimensions: safety, hallucination, fairness/bias, privacy, adversarial robustness, and out-of-distribution generalization. The platform includes diverse evaluation scenarios and red teaming algorithms to create a challenging benchmark. Through testing various multimodal models, MMDT identifies vulnerabilities and areas for improvement, contributing to the development of safer and more reliable MMFMs and systems.

### Strengths
1. MMDT provides a thorough evaluation across multiple dimensions of trustworthiness—safety, hallucination, fairness, privacy, adversarial robustness, and out-of-distribution (OOD) generalization. This comprehensive approach is unique and valuable for identifying vulnerabilities in multimodal foundation models (MMFMs).'
2. The study includes a range of scenarios tailored to different tasks, such as object recognition, counting, spatial reasoning, and attribute recognition. The use of red teaming algorithms for generating challenging data is innovative and enhances the robustness of the benchmark​.
3. By testing MMFMs in applications like autonomous driving and healthcare, the paper addresses real-world scenarios where safety and reliability are critical. This relevance adds practical value to the findings.
4. I like the very detailed appendix, which provide comprehensive information about the trustworthiness of MMFMs.

### Weaknesses
1. Although the paper identifies vulnerabilities and areas for improvement, it lacks a detailed discussion or guidance on specific mitigation techniques for enhancing model trustworthiness. Including concrete strategies for addressing the identified issues could improve the paper’s utility.
2. While MMDT identifies vulnerabilities across multiple dimensions, it may lack sufficient guidance on interpreting and addressing these vulnerabilities for practitioners, particularly those unfamiliar with the nuances of each trustworthiness perspective.
3. The study highlights general issues with MMFMs, but not propose in-depth comparisons between models and answer what make specific model has  strength and weaknesse.

### Questions
Thank you for submitting your work to ICLR! Overall, I like to read this paper as it produces very comprehensive evaluation in terms of the trustworthiness of the MMFMs. While reading this work, I have the following questions and I wish the author can resolve them:

1. In Table 1, as jailbreaking harmful instructions are optimizing adversarial prompts to help bypass safety filters, why the jailbreaking has lower HGR compared with the some of Vanilla case? I thought the jailbreaking is optimizing adversarial prompts, so that it should achieve higher success rate with higher HGR and BR, but it seems that the HGR is not optimized. Can the author explain why they end with this result, and why not optimizing HGR when crafting the adversarial prompts?

2. It seems like GPT-4v achieves best performance in defending against generating harmful text output with different image manipulation, can the author discuss the possible reason behind this?

3. You extend beyond social stereotypes to include decision-making and “overkill fairness.” Could you clarify the criteria used to define and measure overkill fairness? For example, how do you balance fairness goals with historical accuracy, and do you find certain models more prone to overkill fairness in specific contexts?

4. In your OOD evaluation, you find that DALL·E 3 and GPT-4o outperform other models, especially in tasks involving spatial reasoning and attribute recognition. Could you specify the types of OOD transformations that most challenge MMFMs, and whether these models employ specific techniques that enhance their resilience to such transformations?

5. The privacy benchmark assesses object-level memorization, focusing on CLIP embedding similarity to detect privacy leaks. Given this method, could you discuss any limitations or potential improvements? For instance, could certain model fine-tuning approaches mitigate memorization without significantly impacting performance?

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
4

### Summary
This paper presents MMDT (Multimodal DecodingTrust), the first unified platform dedicated to comprehensively evaluating the safety and trustworthiness of multimodal foundation models (MMFMs). MMDT provides a thorough assessment of both text-to-image (T2I) and image-to-text (I2T) models across key dimensions, including safety, hallucination, fairness, privacy, adversarial robustness, and out-of-distribution generalization. Through diverse evaluation scenarios and red teaming algorithms, MMDT establishes a high-quality benchmark that uncovers significant vulnerabilities within MMFMs.

### Strengths
1. The evaluation dimensions in this paper are comprehensive, covering essential aspects of trustworthiness, such as safety, hallucination, fairness, privacy, adversarial robustness, and out-of-distribution robustness.
2. The paper provides a thorough evaluation of multimodal foundation models from both T2I (text-to-image) and I2T (image-to-text) perspectives, resulting in a more unified assessment.
3. The writing is well-structured and logically clear.

### Weaknesses
1. The formatting of the paper appears to have some issues—could it be too wide?
2. The paper lacks a description of the design of the evaluation platform. As a trustworthiness-focused evaluation platform, this section is essential to highlight its unique contributions. Specifically, details on the platform's architecture, modularity, and how it ensures rigorous and continuous evaluation are missing. This makes it difficult to assess the platform's scalability and extensibility.
3. Please provide more detail on the criteria used to select models for evaluation. Appendix A.2 offers only a brief overview, but I would like to understand the rationale behind these choices. Furthermore, the selection of evaluated models seems limited, particularly for I2T models, as classic models like the Claude series are notably missing. The absence of these models raises concerns about the generalizability of the findings.
4. We notice that some data in the dataset are generated using models like GPT-4, and that GPT-4o is also used as an evaluation model. Could this approach inherently favor the GPT-4 series in the evaluation? This raises concerns about potential biases in the evaluation process, particularly if the generated data reflects the specific strengths or weaknesses of the GPT-4 model.

### Questions
Please refer to the weakness. If questions are addressed, I will raise the rating.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MMDT, a unified platform for evaluating the safety and trustworthiness of MMFMs. Unlike existing benchmarks, MMDT assesses models across multiple dimensions, including safety, hallucination, fairness/bias, privacy, adversarial robustness, and OOD generalization. The platform includes diverse evaluation scenarios and red teaming algorithms to generate challenging data. Evaluations conducted using MMDT reveal key vulnerabilities and areas for improvement in multimodal models, establishing MMDT as a foundational tool for advancing safer and more reliable MMFMs.

### Strengths
Strengths:

+ This work offers MMDT, a unified platform for evaluating the safety and trustworthiness of MMFMs. 
+ Comprehensive and thorough assessment.
+ Revealed the security risk of the MMFMs.

### Weaknesses
Weaknesses:

- No obvious weaknesses.

### Questions
Questions:

I am pleased to see that the authors have provided a comprehensive and in-depth benchmark evaluation of MMFMs in terms of safety, hallucination, fairness, and privacy, particularly including mainstream commercial models such as GPT-4 in the evaluation. Additionally, the availability of detailed code, data, and case examples is valuable, allowing readers to conduct further research and extensions. However, I have a few additional questions I would like to discuss with the authors.


- Q1: Although the authors provide a comprehensive and rigorous assessment of MMFMs, especially through the design of red team models for each evaluation objective, it would be beneficial if the authors could also briefly discuss blue team design. Would the authors consider adding a discussion on future blue team approaches in the manuscript?

- Q2: Have the authors examined the security threats of multimodal inputs to MMFMs? For instance, [R1] presents a multimodal red team model for MMFMs; addressing this would expand the assessment's scope.

[R1] Liu Y, Cai C, Zhang X, et al. Arondight: Red Teaming Large Vision Language Models with Auto-generated Multi-modal Jailbreak Prompts[C]//Proceedings of the 32nd ACM International Conference on Multimedia. 2024: 3578-3586.

- Q3: Could the authors elaborate on the differences and connections between the red team model introduced in this paper and existing work? Highlighting these distinctions would improve clarity.

- Q4: For dynamically evolving MMFMs, how does the proposed red team model adapt to ongoing changes? It would be helpful if the authors could address whether this adaptability has been considered in the current model.

- Q5: Finally, have the authors accounted for the diversity of test cases? Given that diversity is a crucial indicator of a red team model's effectiveness, an overview of this aspect would strengthen the evaluation.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Multimodal DecodingTrust (MMDT) to provide a comprehensive evaluation of safety and trustworthiness across multiple dimensions: safety, hallucination, fairness, privacy, adversarial robustness, and out-of-distribution generalization. MMDT includes diverse evaluation scenarios and red teaming algorithms, creating challenging data for each evaluation task to rigorously assess these perspectives.

### Strengths
The paper provides a comprehensive evaluation framework to evaluate Multimodal Foundation Models (MMFMs).

The evaluation using MMDT reveals specific vulnerabilities and areas of improvement in multimodal models, providing actionable insights for researchers and developers.

### Weaknesses
As a benchmark paper, I did not find many unique issues of MMFM compared to the general LLM or foundation models. I appreciate the large workload for benchmarking, but this is more like an experimental report than a solid research paper. For example, there are limited analytical components or theoretical insights. The evaluation framework, while comprehensive, does not deeply explore the underlying mechanisms causing the observed vulnerabilities. For instance, the paper identifies issues like hallucination and adversarial robustness, but it lacks a detailed analysis of why these problems manifest differently in multimodal models compared to unimodal models. Furthermore, the paper does not provide a clear methodology for how the red teaming algorithms were selected or adapted for multimodal scenarios, which raises questions about the generalizability of the findings. The analysis of fairness also seems superficial, lacking a discussion of specific metrics tailored to multimodal data and the potential biases introduced by the data itself.

### Questions
Can you emphasize some unique discoveries from your evaluation process? For example, something that is not straightforward, or something happens in MMFM but not in pure LLM?

### Soundness
3

### Presentation
3

### Contribution
3
