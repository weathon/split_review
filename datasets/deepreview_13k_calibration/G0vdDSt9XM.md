# CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Large language models (LLMs) are often augmented with tools to solve complex tasks. By generating code snippets and executing them through task-specific Application Programming Interfaces (APIs), they can offload certain functions to dedicated external modules, such as image encoding and performing calculations. However, most existing approaches to augment LLMs with tools are constrained by general-purpose APIs and lack the flexibility for tailoring them to specific tasks. In this work, we present \textbf{\framework}, a general tool creation and retrieval framework for LLMs. It creates toolsets specifically curated for the tasks and equips LLMs with a component that retrieves tools from these sets to enhance their capability to solve complex tasks. For each task, we collect specific code solutions by prompting GPT-4 to solve the training examples. Following a validation step ensuring the correctness, these solutions are abstracted into code snippets to enhance reusability, and deduplicated for higher quality. At inference time, the language model retrieves snippets from the toolsets and then executes them or generates the output conditioning on the retrieved snippets. Our method is designed to be flexible and offers a plug-and-play approach to adapt off-the-shelf LLMs to unseen domains and modalities, without any finetuning. Experiments on vision-language, tabular processing, and mathematical reasoning tasks show that our approach achieves substantial improvements compared to strong baselines. In addition, our in-depth analysis reveals that: (1) consistent performance improvement can be achieved by scaling up the number of tools and the capability of the backbone models; (2) each component of our approach contributes to the performance gains; (3) the created tools are well-structured and reliable with low complexity and atomicity.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces CRAFT, a novel framework for augmenting Large Language Models (LLMs) with specialized tools to tackle complex tasks. CRAFT generates task-specific toolsets and provides a retrieval component, enabling LLMs to offload functions to external modules through code snippets and APIs. This approach overcomes the limitations of general-purpose APIs, offering tailored solutions and improved flexibility. The framework ensures the quality and reusability of tools through validation, abstraction, and deduplication processes. Experiments across various domains, including vision-language, tabular processing, and mathematical reasoning, demonstrate substantial improvements over strong baselines. The paper's in-depth analysis confirms the scalability of CRAFT, the significance of each component, and the reliability and simplicity of the created tools. Ultimately, CRAFT presents a plug-and-play solution, enhancing the adaptability and problem-solving capabilities of off-the-shelf LLMs without requiring finetuning.

### Strengths
1. CRAFT showcases originality by combining tool learning, code generation, and retrieval to enhance LLMs' capabilities, applying this novel approach across various tasks and domains.

2. The framework is rigorously validated across different tasks, demonstrating substantial improvements and ensuring tool correctness and reusability, reflecting the high quality of the work.

3. The paper is well-structured and clearly written, providing a comprehensive presentation of the CRAFT framework, its applications, and experimental results.

4. CRAFT addresses crucial challenges in augmenting LLMs, offering a significant advancement in the field and demonstrating practical applicability and effectiveness across diverse domains.

### Weaknesses
1. The paper could benefit from a more detailed exploration of scenarios where CRAFT might not perform as expected. Understanding the limitations and potential failure cases of the framework would provide a more balanced view and help guide future improvements. Specifically, the paper lacks a discussion on how the tool abstraction process might fail to generalize across different input formats or edge cases. For instance, if a tool is created based on a specific date format, it's unclear how the framework handles variations in date inputs or other similar format-sensitive scenarios. A more in-depth analysis of these failure modes is needed.

2. While the paper compares CRAFT to several strong baselines, expanding this comparison to include a wider range of existing tools and frameworks (e.g., SOTA methods in VQA) would strengthen the validity of the claimed improvements. This would also help in positioning CRAFT more clearly in the landscape of existing solutions. The current comparison, while showing improvements, does not fully contextualize CRAFT's performance relative to state-of-the-art methods in the specific tasks, particularly in areas like VQA where many specialized models exist.

3. The paper could provide a more in-depth analysis of the tool creation and retrieval components of CRAFT. Understanding how different types of tools contribute to performance improvements and how the retrieval mechanism interacts with various tasks would offer valuable insights. For example, the paper does not detail how the tool retrieval mechanism handles ambiguous queries or how it prioritizes tools when multiple options are available. A more granular analysis of the retrieval process and its impact on overall performance is needed.

4. While the paper mentions the scalability of CRAFT, providing empirical evidence and a more thorough discussion on how the framework scales with the number of tools and the complexity of tasks would be beneficial. The paper lacks a quantitative analysis of how the framework's performance changes as the toolset size increases or as the complexity of the tasks grows. This is crucial for understanding the practical limits of CRAFT.

5. The paper could explore and address potential biases in the tool creation process, especially considering the reliance on GPT-4 for generating code solutions. Ensuring fairness and mitigating biases is crucial for the applicability of CRAFT across diverse scenarios. The paper does not discuss potential biases that might be introduced through the use of GPT-4, which could lead to unfair or skewed results, especially when dealing with diverse datasets.

6. Including a user study or examples of real-world applications of CRAFT could provide additional validation of the framework's practicality and effectiveness, offering a more comprehensive evaluation. The paper lacks real-world validation, which is critical to demonstrate the practical applicability of the framework beyond controlled experimental settings.

### Questions
1. Failure Cases: Can the authors provide specific examples or scenarios where CRAFT may not perform optimally? Insight into challenges or limitations faced by the framework would be valuable for a comprehensive understanding.

2. Baseline Comparison: Could the authors expand on the choice of baselines used for comparison? Including a broader range of existing tools and frameworks (existing SOTA methods) might help in better positioning CRAFT’s contributions.

3. Tool Creation and Retrieval Analysis: How do different types of tools contribute to the performance improvements observed with CRAFT? Additionally, how does the tool retrieval mechanism interact with various tasks?

4. Real-World Application: Are there examples of real-world applications where CRAFT has been applied? Including such examples or results from a user study could provide additional validation for the framework.

5. Tool Abstraction and Deduplication: Could the authors elaborate on the process of abstracting code solutions into reusable snippets and the criteria used for deduplication? Understanding this process in detail would provide clarity on the quality assurance of tools.

6. Handling of Descriptive Responses: The paper addresses potential issues with underestimated performance due to descriptive responses from LLMs. Could the authors provide more details on how this issue is handled or mitigated in CRAFT?

7. Scalability: The paper mentions the scalability of CRAFT. Could the authors provide empirical evidence or a more detailed discussion on how the framework scales with the number of tools and the complexity of tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces CRAFT, a novel framework designed to enhance large language models (LLMs) by creating and retrieving task-specific tools. CRAFT creates toolsets first and equips LLMs with a component that retrieves these tools to solve complex tasks. Experiments on vision-language, tabular processing, and mathematical reasoning tasks demonstrate the superiority of this approach over strong baselines. The analysis reveals that performance improvement is consistent when scaling the number of tools and the capability of backbone models, and that the created tools exhibit low complexity and atomicity.

### Strengths
1.	Traditional approaches to augment LLMs with tools lack flexibility, as they rely on general-purpose APIs. CRAFT addresses this problem by reusing task-related tools, which is more flexible.
2.	This method can adapt off-the-shelf LLMs to new domains and modalities without finetuning.
3.	Experiments show that the proposed framework can improve a lot compared to previous approaches.

### Weaknesses
1.	The setting of the experiments is a little bit limited. There are many agent benchmarks like MINT, AgentBench, and so on, which focus on the problem-solving capacity of LLMs as agents. The reviewer thinks the work needs to be further verified on broader benchmarks for agents.
2.	The comparison with LATM is a little bit unfair. The toolset created by CRAFT is the output of GPT-4, while the tool used by LATM is created by an inferior model if there is no misunderstood.
3.	The transferability of the toolset should be discussed as I noticed that the toolset for the VQA task and the toolset for the reasoning task are not the same. Maybe the authors can experiment to create a general tool set for all tasks and see what will happen.

### Questions
Please see the weakness.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents CRAFT, a framework for tool creation and retrieval to customize large language models (LLMs) for various tasks and domains. CRAFT creates a specialized toolset by prompting LLMs to generate and abstract code solutions for problems, and validates and deduplicates the tools. CRAFT retrieves relevant tools from the toolset by multi-view matching, and adds them to the prompt of LLMs for code generation. CRAFT improves performance on vision-language, tabular processing, and mathematical reasoning tasks.

### Strengths
1. This paper proposes a tool generation and tool-using framework for LLMs which is a good attempt to enhance LLMs' capability to solve reasoning tasks by generating programs.

2. Personally I think the idea of a "pseudocode library" proposed in future work is cool and meaningful.

3. The experiments on baselines and different LLMs are comprehensive and the result is promising. Basically, I agree with the authors that tool generation puts a high demand on the LLMs' coding ability.

4. The created toolsets are a particularly important contribution to the LLM community.

### Weaknesses
1. The authors mentioned that alternative backbone models like CodeLlama demonstrate near-random performance. Can the authors provide such results (the performance of different LLMs in creating and using tools) in the experiment?

2. I suggest that the author should make the distinction between more specific methods more prominently in the main text (though the difference has been discussed in the experimental setting), such as by creating a table to compare various tool-augmented language model methods, and so on. The current Figure 1 appears to be similar to previous work like LATM, making it difficult to showcase the uniqueness of this article.

### Questions
1. What does "bug-free" mean and how do the authors ensure that the generated tools are "bug-free"?

2. What is the result of tool generation with GPT-3.5-turbo and other LLMs?

3. Can CRAFT be adapted to programming tasks like HumanEval since it generates "APIs"?

4. Can the authors discuss more on the "pseudocode library" like can we use a natural language library and how is it different from in-context learning?

5. Can the authors analyze more on the created toolsets like where they might it can be applied/generalized?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
