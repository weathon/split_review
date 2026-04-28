# B-MoCA: Benchmarking Mobile Device Control Agents across Diverse Configurations

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
Mobile device control agents can largely enhance user interactions and productivity by automating daily tasks. 
However, despite growing interest in developing practical agents, 
the absence of a commonly adopted benchmark in this area makes it challenging to quantify scientific progress.
In this work, we introduce \metabbr: a novel benchmark with interactive environments for evaluating and developing mobile device control agents.
To create a realistic benchmark, we develop \metabbr based on the Android operating system and define \tasknum common daily tasks.
Importantly, we incorporate a randomization feature that changes the configurations of mobile devices, including user interface layouts and language settings, to assess generalization performance. 
We benchmark diverse agents, including agents employing large language models (LLMs) or multi-modal LLMs as well as agents trained with imitation learning using human expert demonstrations. 
While these agents demonstrate proficiency in executing straightforward tasks, their poor performance on complex tasks highlights significant opportunities for future research to improve effectiveness. 
Our source code is publicly available at \href{https://b-moca.io}{https://b-moca.io}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces B-MoCA, a benchmark designed to evaluate mobile device control agents. It includes 131 common daily tasks and incorporates a randomization feature to test agents’ generalization across diverse device configurations, such as icon placements, wallpapers, languages, and device types. The benchmark evaluates various agents, including closed/open-source (M)LLMs and custom models trained from scratch. The paper shows agents' proficiency in straightforward tasks, but they struggle with complex tasks requiring multiple interactions. The paper provides a unified platform for comparing different methods, identifies limitations in current approaches, and offers open-source resources for reproducibility.

### Strengths
The benchmark includes a wide range of device configurations, providing a novel and important testing environment for the generalization capabilities of mobile device agents. Grounded in real-world applications, the benchmark is highly relevant for practical use. Its scope includes agents from a diverse set of models.

### Weaknesses
The range of tasks and mobile apps tested is somewhat narrow, which may not fully represent the potential capabilities of mobile device control agents. The paper lacks a compelling conclusion and fails to present inspiring findings that could significantly advance the field of research. This paper does not study the latest research and SoTA methods in mobile device agents, particularly those featuring more complex designs such as multi-agent systems and advanced UI understanding modules.

### Questions
The benchmark could be expanded to include more diverse and complex tasks that reflect real-world scenarios more accurately. Incorporating a study of SoTA methods and agents would provide more impactful findings. This would not only enhance the benchmark’s comprehensiveness but also offer deeper insights into the capabilities and limitations of current mobile device control agents.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a commendable and promising benchmark, B-MoCA, designed to evaluate mobile device control agents across a variety of device configurations. The task design is somewhat aligned with real-world scenarios, encompassing a broad spectrum of everyday activities. Additionally, the incorporation of environment randomization enhances the diversity of testing conditions. Overall, the presentation of the paper is clear, and the figures effectively support the data and findings.

### Strengths
B-MoCA defines 131 common daily tasks, such as opening applications, conducting web searches, and adjusting device settings. These tasks are grounded in realistic scenarios, making the benchmark more reflective of actual user needs than previous benchmarks that focused on simpler tasks. The authors emphasize the environment randomization feature, which introduces variations in device configurations (e.g., icon locations, languages, device types). This setup broadens the testing scope for agents, helping to prevent scenarios where agents merely "memorize" operations in fixed environments. Such variability facilitates the assessment of agent adaptability across different configurations, contributing to a more robust evaluation of agent generalization.

### Weaknesses
1. **Comparison with Existing Benchmarks:**

   While B-MoCA increases the task count and introduces environment randomization, it does not fundamentally differ in its core framework or testing methodology from existing benchmarks like WebShop and Mobile-Env. For instance, Mobile-Env provides a platform for training and evaluating mobile agents with a focus on GUI interaction, supporting both visual-based and text-based agents. [GitHub](https://github.com/X-LANCE/Mobile-Env) Similarly, WebShop offers a scalable environment for web-based interactions, emphasizing language grounding and decision-making. [Webshop Pnlp](https://webshop-pnlp.github.io/) B-MoCA appears to serve as an extension of these benchmarks rather than introducing a novel evaluation paradigm.  Could the authors provide a more detailed comparison between B-MoCA and existing benchmarks like WebShop and Mobile-Env, highlighting specific novel aspects or improvements in B-MoCA's methodology or evaluation framework?

2. **Multimodal Model Challenges:**

   Although B-MoCA accommodates multimodal models (such as those with image-based inputs), the paper does not thoroughly explore the specific challenges and limitations of these models in visual comprehension. For instance, the inclusion of multimodal inputs heightens model computational complexity, potentially resulting in latency issues, which are particularly critical in mobile device contexts. Recent studies have highlighted the importance of optimizing multimodal models for mobile devices to address these challenges. [ArXiv](https://arxiv.org/abs/2405.12107)    Could the authors discuss how B-MoCA addresses the computational complexity and potential latency issues associated with multimodal models, particularly in the context of mobile devices? Are there specific metrics or evaluations in B-MoCA designed to assess these aspects?

3. **Evaluation Scope:**

   The evaluation focuses solely on the capabilities of large language models (LLMs), while many open-source GUI agents, such as [1,2,3,4], remain unassessed by this benchmark. This limitation complicates the evaluation of future works utilizing B-MoCA. Including these could provide a more comprehensive comparison and facilitate easier adoption of B-MoCA for future research.

[1] AutoDroid，
[2] You Only Look at Screens，
[3] CoCo-Agent
[4] AppAgent

### Questions
Please refer to the weaknesses section above for specific points requiring clarification or further detail.

### Soundness
3

### Presentation
3

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
This paper introduces the B-MoCA benchmark with interactive environments for evaluating and developing mobile device control agents. Then several baseline agents for mobile device control are evaluated, identifying their limitations, such as their poor generalization in UI elements understanding and manipulation.

### Strengths
1. B-MoCA introduces a well-structured benchmark for evaluating mobile control agents.
2. B-MoCA contains 131 common daily tasks, from simple tasks to complex multi-step interactions to assess essential skills for mobile device management.
3. The benchmark tests agents based on various models and environment randomization.

### Weaknesses
1.  This paper lacks contribution and novelty, primarily presenting a benchmark for evaluating mobile device control agents. The conclusions drawn from the experiments lack depth, making it challenging to derive valuable insights for further improvement.
2. The paper lacks a qualitative comparison with other benchmarks for decision-making agents. Demonstrating that the proposed benchmark is more effective or of higher quality than existing alternatives is crucial to establishing its value.

### Questions
no

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel benchmark for evaluating and developing mobile device control agents. Based on the Android operating system, B-MoCA defines 131 common daily tasks and incorporates a randomization feature to alter mobile device configurations to assess the generalization performance of agents. The evaluation is quite comprehensive.

### Strengths
Strengths
1. The proposed method is based on Android, ensuring authentic evaluation environments.
2. It includes 131 daily tasks grounded in realistic scenarios, covering a range of applications.
3. By changing various elements, it assesses the agents' generalization capabilities across various device configurations.
4. Open-source.
5. Comprehensive evaluation.

### Weaknesses
1. It is better to train a new model based on a training dataset collected in the same way. The collected dataset contains various environments, and it is natural to explore whether the agent could gain better generalization abilities when trained in such a dataset. However, the existing benchmark only evaluates existing models, and I think the contribution is not enough. 
2. The conclusions are already well-known. The conclusion that I care about most is this one "such as their poor generalization in UI elements understanding and manipulation". This should be already well known at least in AppAgent, which serves as one of the code bases of this paper. In AppAgent, the authors utilize lots of tricks to improve the VLM's understanding abilities even using GPT-4V, such as generating documents and XML for references. Also, in GitHub, the author tested the best open-source VLM named Qwen-VL and reported a decrease in performance. All these could reflect the fact that VLM's limitations in understanding, and also prove that open-source VLMs are weaker than close-source ones.
3. Could you elaborate on the reasons for evaluating open-source VLMs alongside closed-source models, considering that there is a well-known performance gap between them?

### Questions
see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents B-MoCA, a benchmark for evaluating mobile device control agents (LLMs) on diverse configurations. Built around the Android OS, with ADB support. B-MoCA encompasses 131 daily tasks with environment randomization features, such as varied icon placements, language settings, and device types. These tasks and configurations test agents' generalization abilities by benchmarking large language models (LLMs) and custom agents.

### Strengths
1. An open-source project is proposed to evaluate all the popular LLMs we have today.
2. B-MoCA addresses an important gap by focusing on environmental diversity, making it a useful resource for researchers aiming to improve agent robustness.

### Weaknesses
1. Since the work has already been proposed in an ICLR 2024 workshop, it lacks the fresh innovation expected of a full ICLR 2025 conference submission. This may restrict its perceived value in the community.
2. Lack of novelty, I know it is bad to just say this, but I truly can't get any insights from this paper. It's a well-built open-source project to evaluate LLMs indeed, but I did not find any conclusion here interesting.
3. Although several LLMs and MLLMs were benchmarked, the paper does not explore adaptive fine-tuning or other strategies to mitigate performance declines in randomized environments.

### Questions
Have any additional measures been tested to mitigate performance declines due to randomization?

### Soundness
3

### Presentation
3

### Contribution
1
