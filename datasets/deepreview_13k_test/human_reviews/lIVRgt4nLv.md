# Agent S: An Open Agentic Framework that Uses Computers Like a Human

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
We present Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI), aimed at transforming human-computer interaction by automating complex, multi-step tasks. Agent S aims to address three key challenges in automating computer tasks: acquiring domain-specific knowledge, planning over long task horizons, and handling dynamic, non-uniform interfaces. 
To this end, Agent S introduces experience-augmented hierarchical planning, which learns from external knowledge search and internal experience retrieval at multiple levels, facilitating efficient task planning and subtask execution. 
In addition, it employs an Agent-Computer Interface (ACI) to better elicit the reasoning and control capabilities of GUI agents based on Multimodal Large Language Models (MLLMs). 
Evaluation on the OSWorld benchmark shows that Agent S outperforms the baseline by 9.37\% on success rate (an 83.6\% relative improvement) and achieves a new state-of-the-art. 
Comprehensive analysis highlights the effectiveness of individual components and provides insights for future improvements. 
Furthermore, Agent S demonstrates broad generalizability to different operating systems on a newly-released WindowsAgentArena benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Agent S, a groundbreaking framework designed to automate complex, multi-step tasks on computers through Graphical User Interface (GUI) interaction for human usage. Agent S tackles the challenges of acquiring domain-specific knowledge, planning over long task horizons, and navigating dynamic interfaces by employing experience-augmented hierarchical planning, which leverages both external web knowledge and internal experience retrieval. It also utilizes an Agent-Computer Interface (ACI) to enhance the reasoning and control capabilities of GUI agents based on Multimodal Large Language Models (MLLMs). The framework demonstrated significant improvements in task success rates on the OSWorld benchmark and showed broad generalizability to different operating systems, setting a new state-of-the-art in autonomous GUI agent performance.

### Strengths
1. Agent S stands out for its task automation through experience-augmented hierarchical planning. This method harnesses external web knowledge and draws upon internal memories, enabling the agent to decompose complex tasks into executable subtasks.
2. The introduction of the Agent-Computer Interface (ACI) is a notable strength of Agent S. This interface serves as a critical abstraction layer that facilitates precise perception and action in GUI environments. By defining a bounded action space with language-based primitives and incorporating a dual-input strategy, ACI enhances the agent's ability to ground actions and receive immediate environmental feedback. This innovation allows Agent S to operate more effectively and efficiently, setting a new standard for MLLM-based GUI agents.

### Weaknesses
1. The paper does not address the scalability and efficiency of the framework when handling a large volume of tasks or more complex workflows. There is a need to evaluate how the agent performs under increased load and whether the hierarchical planning and memory update mechanisms can scale without compromising the speed and accuracy of task completion.
2. The framework's performance could potentially falter in scenarios where reliable web knowledge is scarce or when there are frequent, rapid changes in application interfaces that outpace the web's ability to update corresponding information.
3. The paper acknowledges a high rate of execution errors, indicating that Agent S may struggle with decision-making and behavior adjustment during task execution.

### Questions
1. Could you elaborate on how Agent S differentiates between when to retrieve external web knowledge versus when to leverage internal memories? How is this decision balanced?
2. How does Agent S handle the cold start problem, especially when it encounters a task that neither memories has prior experience with? Could you explain the strategies for quickly adapting to new tasks?
3. Your error analysis indicates a high rate of execution errors. Could you present a more detailed breakdown of the types of execution errors encountered and discuss potential improvements to the Action Generator to reduce these errors, especially in complex, long-horizon tasks?

### Soundness
3

### Presentation
3

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
The paper proposes Agent S, a computer agent framework which can directly interact with computers through GUI interface. The proposed framework mainly consists of three components, a manager to manage external and internal memory for subtasks planning, a worker to complete subtasks with an episodic memory trajectory reflector, and a self-evaluator to summarize task experiences. The authors also propose an agent-computer interface as an abstraction layer. The proposed framework is evaluated on OSWorld and seen an increase of 9.37% success rate.

### Strengths
1. The performance of the proposed framework on OSWorld benchmark is quite good.
2. The proposed framework is well-engineered and the evaluation is systematic.
3. The presentation and visualization of the paper is good.

### Weaknesses
1. It would be unfair to compare the framework only to the baseline from OSWorld, which is a benchmark paper, not a methodology paper.
2. The self-supervised exploration process is not realistic in actual deployments and I believe it will lead to overfitting.
3. The ACI proposed in this paper can only act on selected elements in the accessibility tree, which somewhat sacrifices flexibility for performance because you cannot click on every coordinate of the screen.
4. While the framework is well designed, it doesn’t introduce much new. For example, it’s quite obvious that doing some early exploration, using external resources, and OCR would help. In addition, these processes, as well as subtask planning and self-evaluation would significantly slow down the task, which is already quite slow, and would cost more OpenAI tokens.

### Questions
1. What is the average time cost to complete a task using OpenAI API-based models and self-hosted models?
2. Does the continued memory growth consume more LLM input context tokens? What is the average context length?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents Agent S, a novel framework for GUI-based operating system control that integrates three key strategies: experience-augmented hierarchical planning, continual memory update, and an Agent-Computer Interface (ACI). The framework introduces an effective memory mechanism with initialization and continuous update algorithms, demonstrating state-of-the-art performance on computer use benchmarks like OSWorld. A notable contribution is the carefully designed ACI that addresses the unique challenges of MLLM agents interacting with desktop environments.

### Strengths
1. **Novel and Effective Memory Mechanism**: Introduces a well-designed memory system with both narrative and episodic components
Provides clear algorithms for both initial memory construction and continuous updates
Demonstrates a complete closed-loop system with practical effectiveness


2. **Insightful Analysis of Agent-Computer Interaction**: Deep analysis of fundamental challenges in MLLM-based computer control
Identifies key issues like discrete time response, lack of internal coordinate systems, and inefficient feedback processing
Addresses the limitations of traditional API/script-based automation approaches


3. **Innovative ACI Design**: Proposes a dual-input strategy combining visual and accessibility tree information
Implements bounded action space with concurrent feedback
Successfully bridges the gap between MLLM agents and GUI control requirements


4. **Strong Empirical Results**: Achieves SOTA performance on established benchmarks
Provides comprehensive experimental validation

### Weaknesses
1. **Limited Problem Definition**: The paper could benefit from a more detailed introduction to computer automation tasks
Key concepts like planning, execution, and grounding could be better explained for readers new to the field


2. **Presentation Issues**: Some overlap between Figures 3 and 4 that could be consolidated or better differentiated
Technical details of the ACI implementation could be more thoroughly described

### Questions
1. **Citation Format Issues**: References to OSWorld (Xie et al., 2024) and WindowsAgentArena (Bonatti et al., 2024) need clarification as they appear to be forward citations


2. **Figure Organization**: Have the authors considered combining Figures 3 and 4 for better presentation, or focusing Figure 4 more specifically on memory aspects?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new multimodal large language model agent for GUI control, called Agent S. Its main feature is the ability to complete various tasks in a GUI interface through direct keyboard and mouse control. Comparing with other agents, Agent S incorporates an experience-augmented hierarchical planning method, which enhances the agent's ability to decompose tasks based on trajectories stored in memory. Experiments demonstrate that this framework is versatile, capable of executing various GUI-oriented tasks across different systems(Ubuntu and Windows).

### Strengths
The advantages of this paper are that it has a clear line of thought, smooth transitions, and is easy to follow. The main architecture diagram of the agent is concise and clear, allowing for a straightforward understanding of the information flow. The selection of experimental environments is well-considered, taking into account both Ubuntu and Windows systems, which proves the effectiveness and generalization of the framework.

### Weaknesses
However, the experiments in this paper are not sufficiently comprehensive. First, the baselines used are not enough, and in the comparison results of the main experiments, MLLMs are used simply instead of MLLM agents. The experimental results based on single MLLMs that only input images and accessibility trees are not convincing enough. Existing agents such as Cradle and Claude 3 perform well using only keyboard and mouse inputs without requiring additional accessibility trees. As a result, the third contribution of this paper also limits the applicability of Agent S and raises doubts about whether all GUIs provide accessibility tree inputs and whether such inputs are necessary. Thus, the contributions of this paper may seem insufficiently innovative. 

reference：
[1]Tan W, Zhang W, Xu X, et al. Cradle: Empowering Foundation Agents towards General Computer Control[C]//NeurIPS 2024 Workshop on Open-World Agents.

### Questions
First, I have some doubts about the generalizability of accessibility trees. Do all GUIs have accessibility trees, and do systems like Ubuntu and Windows have similar forms of accessibility trees? I hope the article can clarify these points. Secondly, I would like the article to compare Agent S with different agents, evaluating whether Agent S demonstrates better experimental results compared to existing GUI agents. Lastly, the ablation study does not adequately cover all points of contribution. An experiment should clarify the performance of Agent S when solely relying on image input without ACI.

### Soundness
3

### Presentation
2

### Contribution
2
