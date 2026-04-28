# VisualAgentBench: Towards Large Multimodal Models as Visual Agents

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 8, 6

## Abstract
\vspace{-2mm}
  Large Multimodal Models (LMMs) have ushered in a new era in artificial intelligence, merging capabilities in both language and vision to form highly capable \textbf{Visual Foundation Agents}.
  These agents are postulated to excel across a myriad of tasks, potentially approaching general artificial intelligence. 
  However, existing benchmarks fail to sufficiently challenge or showcase the full potential of LMMs in complex, real-world environments. 
  To address this gap, we introduce VisualAgentBench (\sm), a comprehensive and pioneering benchmark specifically designed to train and evaluate LMMs as visual foundation agents across diverse scenarios, including Embodied, Graphical User Interface, and Visual Design, with tasks formulated to probe the depth of LMMs’ understanding and interaction capabilities. 
  Through rigorous testing across nine proprietary LMM APIs and eight open models, we demonstrate the considerable yet still developing agent capabilities of these models. 
  Additionally, \sm constructs a trajectory training set constructed through hybrid methods including Program-based Solvers, LMM Agent Bootstrapping, and Human Demonstrations, promoting substantial performance improvements in LMMs through behavior cloning. 
  Our work not only aims to benchmark existing models but also provides a solid foundation for future development into visual foundation agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces VisualAgentBench (VAB), a benchmark designed to evaluate and train LMMs as visual agents in diverse, realistic scenarios, including embodied, GUI, and visual design tasks. VAB provides a unified, standardized framework for assessing LMMs across multiple domains, synthesizes high-quality multimodal data using a mix of programmatic solvers, LMM bootstrapping, and human demonstrations, and benchmarks 18 LMMs, uncovering both strengths and limitations in real-world task performance. Key insights include challenges in visual grounding, planning, and error recovery, offering a valuable testbed to push LMMs toward more adaptable and practical visual agents.

### Strengths
- Comprehensiveness: The main strength of this paper is its comprehensiveness in benchmarking Large Multimodal Models (LMMs) as visual agents. The authors introduce VisualAgentBench (VAB), a benchmark that covers a wide range of real-world application scenarios by including five major task categories: embodied agents, GUI-based agents, web agents, gaming agents, and visual design agents. This breadth makes VAB a thorough evaluation tool, enabling a more holistic assessment of LMMs' capabilities across different domains rather than focusing on a single application area.

- Extensive Experiments: The paper demonstrates substantial experimental rigor by benchmarking 18 different LMMs, encompassing both proprietary and open-source models. This extensive testing provides a solid foundation for the insights presented, which shed light on various LMM challenges, such as visual grounding and error recovery. These experiments allow for more reliable comparisons between models, offering valuable insights into how different LMMs perform in complex, interactive tasks. The conclusion on ReAct framework is also interesting.

- Insightful Analysis: Through the VAB benchmark, the authors provide some useful observations on the current state of LMMs as visual agents. They highlight specific limitations in visual grounding, action planning, and error handling across various environments, which helps to pinpoint areas for future improvement in LMM design. While these insights are not groundbreaking, they add value by identifying practical challenges that developers and researchers may encounter when deploying LMMs in real-world applications.

### Weaknesses
 - Insufficient Explanation for VL Model Performance: Some vision-language models perform poorly without adequate explanation. For instance, the paper doesn’t explore why certain models achieved low scores, leaving questions about the benchmark’s application across models.
- Unclear Role of Visual Information in Certain Tasks: The paper lacks clarity on how specific tasks, such as those in Minecraft, leverage visual information effectively and whether VLM is genuinely necessary for all actions. For instance, Minecraft actions like "Teleport" don't inherently require visual information since they can execute without reference to the visual state, raising doubts about the added value of VL models in such contexts. Clarifying how the benchmark ensures each action necessitates visual input, as opposed to pure language model decision-making, would help demonstrate the benchmark’s relevance and justify the use of VL models over text-only approaches in specific environments.
- Ambiguities in Figure Interpretation and Process Flow: Figures like Figure 2 could benefit from clearer annotations or explanations. The figure includes multiple input and output connections but lacks a clear process flow or indication of sequential dependencies, making it challenging to follow the intended agent behavior across rounds.

### Questions
1. Could you clarify the role of bounding boxes and object tags in Figure 7? Does this mean that objects and tags must be visible in the input images so that the simulator can recognize and interact with these objects by their tag names? In Section 5.1, the authors discuss the use of object labels in embodied environments. How exactly does the agent operate when no object label or tag is provided?

2. To ensure ease of use, what practice does VAB provide? unified API access or modular code structure across different task environments? More details on engineering side for easy usage could be beneficial.

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
5

### Summary
The authors propose to apply large multimodal models to visual agent tasks, which is mored grounded than existing VQA tasks.
The authors collected 5 datasets including 1 for robotics in simulation, 1 for game playing, 2 for GUI manipulation and 1 for web page design.
The authors design a function calling-based action space for each task.
The agent tasks are created by first generating a bunch of templates with placeholders and then instantiating these templates.
Action trajectories for each task are collected by 1) human-written scripts(for web GUI tasks) 2) prompting existing LMMs like GPT-4o 3) human demonstration.
The authors collected 746 test cases and 4482 training trajectories across 5 tasks and benchmarked 18 proprietary and open-source LMMs.

### Strengths
1. The proposed benchmark provides a unified “function-call” action space as well as diverse task domains for benchmarking the agent ability of LMMs
2. Experiments and ablation are solid. A wide range of both commercial and open-source LMMs are evaluated on the proposed benchmark. Ablations of input image prompting(labels, SoM), reflection(injecting error) and planner(ReAct w/ & w/o Thought) are conducted.

### Weaknesses
1. No clear advantage over existing benchmarks. There are plenty of existing benchmarks for both high-level planning for robot manipulation in simulation like RoboVQA as well as for GUI agent tasks like Webshop-V and VisualWebArena. The proposed visual agent benchmark is surely more grounded than VQA benchmarks like MMMU, but I don’t see what’s the real contribution is if compared with domain-specific benchmarks. 
2. Low quality training trajectories. Take the GUI agent for instance, the proposed VAB-WebArene-Lite uses code script-based trajectory collection, which is well-known for its limited diversity compared with real-world human web browsing action trajectories. 
3. The function calling action space biases toward LMMs with a strong coding ability so that some LMMs unfairly got low scores(like Qwen-VL-Max and Gemini-1.0-Pro, which both do a good job for pure VQA benchmarks.
4. I still don't get the rationale behind why these tasks are chosen. The robotics, Minecraft, UI and webpage design are good domains but are not the only domains that matter. Why not include driving, drone and flat design, etc as well? Since VAB is not an exhaustive benchmark, how to choose each task is crucial. Also I don't know what does a comprehensive benchmark mean by the authors in the rebuttal.
5. Neither human-annotated nor LMM-bootstrapped ensures a high diversity. Only the careful task space design could achieve that goal. Maybe the authors could elaborate more about how the task lists are carefully crafted to maximize the diversity for each domain?
6. I don't understand why a model without function calling ability could not be a good VLM agentic model across different environments. I think Qwen-VL 1 is quite solid a VLM and could do well in many driving, robotics and UI tasks when fine-tuned as a VLA model without any function calling ability.
7. This is simply wrong, most robot arms like UR5 or franka have a workspace of 700mm-1000mm, if you allow the VLM to grasp objects within 1.2m there will be tons of failures. This makes me wonder if the VAB-OmniGibson really executed the action of VLM.
8. VAB-OmniGibson violates the golden design rule by simplifying real grasping trials into a rule-based text environment instead(if the robot has hand and is within 1.2m then grasp is success).

### Questions
1. Does the physical dimension of robot arm given in Gibson? As shown in Figure 1 Round 3, I don't think the grasp banana is feasible given its lying on the far end of the countertop

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a multimodal benchmark VisualAgentBench to evaluate LMMs as agents performing interactive tasks. The benchmark includes three scenarios based on five datasets/environments: Embodied (VAB-OmniGibson, VAB-Minecraft), Graphical User Interface (VAB-AndroidLab, VAB-WebArena-lite), and Visual Design (VAB-CSS). Besides benchmark data, the authors also provide additional task trajectories for training. All the task instances in the training and testing data are constructed by prototyping and instantiation. This paper applies a mix of three strategies to collect training trajectories according to the characteristics of different datasets. Experiment results show that the proposed benchmark is challenging for current LMMs and further SFT could improve the performance. The paper also conducts an analysis of visual grounding and planning to provide insights for the future development of LMM agents.

### Strengths
1. The proposed benchmark is a good complement to current multimodal and agent benchmarks to evaluate LMMs in challenging interactive scenarios.
2. The proposed benchmark has standardized environments with good consistency and reproducibility.
3. The paper also provides training trajectories for SFT.
4. The experiments are comprehensive, revealing problems of current models, and the analysis provides good insights.

### Weaknesses
1. The number of training data is still very limited. The paper does not show whether it is possible to scale up training data in the proposed environments in an efficient way.
2. There is no analysis and experiments to verify whether the proposed environments could be effectively used for RL training. Specifically, the paper lacks discussion on the reward structure and its impact on the learning process within these environments.
3. It would be helpful to train some non-LLM specialist models in each environment using RL/IL and report their performance as a reference. This would establish a performance baseline and help assess the difficulty of the tasks.
4. After fine-tuning LMMs with the collected training data, authors should also evaluate their general multimodal abilities on other multimodal benchmarks. Also, the authors should explore whether it is possible to maintain the original abilities while improving the performance on the proposed benchmark after SFT. The paper does not address the potential for catastrophic forgetting of general multimodal skills.
5. The authors should provide some trajectories of models tested for better illustration. It would be beneficial to see both successful and unsuccessful examples to understand the challenges.

### Questions
1. When training open LMMs, the paper says that they only use the vision input of the latest turn. Does this mean each turn in the training trajectory is treated as an independent sample (with previous turns provided in context) instead of training as a multi-turn conversation sample?
2. For evaluating LMM APIs, what do you mean by "Vision Input image won’t be kept in the dialog"? Wouldn't the images that appear in the previous turns in one conversation automatically be kept?

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
4

### Summary
The authors propose a benchmark for evaluating LMMs across a wide range of task: including proposing (1) standardized interfaces, prompting, and data formats, (2) a strategy for creating valid test sets, (3) multitask multi-environment trajectory train sets, (4) benchmarking of 18 open-sourced and closed-sourced LMMs, (4) analyses of LMMs' abilities for grounding and planning.

### Strengths
I appreciate the diversity of tasks explored, from embodied agents to visual design. I believe that general-purpose LMMs that can perform well on a wide range of tasks are essential, and such benchmarks are necessary. Interaction through text/vision-based environment feedback is an important aspect of the paper. I also appreciate the scale of evaluation in the paper, and the finetuning of open LMMs.

### Weaknesses
1. Can you elaborate on how the task description, action spaces, few-shot demonstrations, and notices for each environment are formatted as prompts? How are visual outputs of the environment passed in as text in the interaction rounds for embodied and GUI agents? Could you elaborate on how error recovering works in planning? Interested in seeing experiments on error recovery behavior across all models, or in general, some evaluation on the interaction rounds instead of final success rate only (e.g., average number of steps to recover from an error).
2. I’m also interested in seeing more detailed analyses on the tasks that these models fail on. For example, which “prototypes” lead to failure? Does each model fail in a way that is consistent with one another (e.g., is there correlation between the accuracy on each prototype/subtask?) Does finetuning an open LMM help on the grounding aspect more, or the planning aspect more?
3. On a high-level, it would be great to have a quantitative metric established in this benchmark that systematically measures performance on grounding vs reasoning, instead of as an analysis only. Also, related to the first point, quantitative evaluation on interaction behavior (perhaps some proxy metric on progress to the goal).

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
