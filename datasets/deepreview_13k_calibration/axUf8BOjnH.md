# AgentStudio: A Toolkit for Building General Virtual Agents

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
General virtual agents need to handle multimodal observations, master complex action spaces, and self-improve in dynamic, open-domain environments. However, existing environments are often domain-specific and require complex setups, which limits agent development and evaluation in real-world settings. As a result, current evaluations lack in-depth analyses that decompose fundamental agent capabilities. We introduce \env, a trinity of environments, tools, and benchmarks to address these issues. \env provides a lightweight, interactive environment with highly generic observation and action spaces, e.g., video observations and GUI/API actions. It integrates tools for creating online benchmark tasks, annotating GUI elements, and labeling actions in videos. Based on our environment and tools, we curate an online task suite that benchmarks both GUI interactions and function calling with efficient auto-evaluation. We also reorganize existing datasets and collect new ones using our tools to establish three datasets: GroundUI, IDMBench, and CriticBench. These datasets evaluate fundamental agent abilities, including GUI grounding, learning from videos, and success detection, pointing to the desiderata for robust, general, and open-ended virtual agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces AgentStudio, a toolkit designed for building general virtual agents capable of handling multimodal observations and complex action spaces in dynamic, open-domain environments. It includes a set of environments, tools, and benchmarks that address the limitations of current domain-specific virtual agent evaluations. AgentStudio provides a lightweight, interactive environment with generic observation and action spaces, integrating tools for task creation, GUI element annotation, and video action labeling. The paper also presents three datasets—GroundUI, IDMBench, and CriticBench—that evaluate fundamental agent abilities such as GUI grounding, learning from videos, and success detection, aiming to advance the development of robust, general, and open-ended virtual agents.

### Strengths
-  This paper provides a lightweight, interactive environment with highly generic observation and action spaces, such as video observations and GUI/API actions, which expand the task space to a massively open domain and real-world tasks. AgentStudio comes with tools for creating and validating benchmark tasks, annotating GUI elements, and labeling actions in videos, which are essential for customizing and validating tasks in real-world settings.
-  The toolkit enables online interactions for learning through trial and error, providing language feedback on failure reasons, which is crucial for open-ended learning and self-improvement of LLM-based agents.
- The paper introduces three datasets—GroundUI, IDMBench, and CriticBench—that target UI grounding, action labeling from videos, and success detection, respectively, providing a structured approach to evaluating and improving fundamental agent capabilities.

### Weaknesses
 -  This paper provides a lightweight, interactive environment with highly generic observation and action spaces, such as video observations and GUI/API actions, which expand the task space to a massively open domain and real-world tasks. AgentStudio comes with tools for creating and validating benchmark tasks, annotating GUI elements, and labeling actions in videos, which are essential for customizing and validating tasks in real-world settings.
-  The toolkit enables online interactions for learning through trial and error, providing language feedback on failure reasons, which is crucial for open-ended learning and self-improvement of LLM-based agents.
- The paper introduces three datasets—GroundUI, IDMBench, and CriticBench—that target UI grounding, action labeling from videos, and success detection, respectively, providing a structured approach to evaluating and improving fundamental agent capabilities.

 -  Although the authors have made the code available in the supplementary materials, it would be beneficial to offer a more detailed guide to assist users in understanding and implementing the benchmark effectively. Specifically, the documentation should include step-by-step instructions for setting up the environment, running the provided examples, and customizing the tasks for new scenarios. The lack of detailed documentation will hinder the adoption and usability of the benchmark.
- The paper's claims are somewhat overstated. While AgentStudio's tasks primarily focus on interactions within 2D graphical user interfaces (GUIs), the capabilities of a general virtual agent extend beyond these to include interactions with 3D virtual environments, such as those found in the metaverse. To align the paper's title with its scope or to enhance its benchmark, it would be essential to incorporate additional 3D world scenarios, like 3D video games, which would provide a more comprehensive assessment of a virtual agent's capabilities. The current focus on 2D GUIs limits the generalizability of the findings and the applicability of the benchmark to more complex real-world scenarios.


### Questions
How does AgentStudio handle user interactions, and what mechanisms are in place for agents to learn from and adapt to user feedback? Is it feasible to conduct a human evaluation of user experience when using the agent?

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
In this paper, AgentStudio, a trinity of environments, tools, and benchmarks for building general virtual agents is proposed. The benchmark contains GroundUI that evaluates UI grounding capability, IDMBench that evaluates action labelling capability and CriticBench that evaluates success detection module. Overall experimental results show that the existing VLM is still far away from being able to fully solve these benchmarks. Compared w/ previous works, AgentStudio provides the better observation and action spaces, and therefore can help develop and evaluate agents in real-world settings.

### Strengths
1. The paper is well written, easy to follow. 
2. The dataset curation process makes sense to me.
3. The experiments are adequate. Compared to previous works, AgentStudio has many advantages including interactivity, supporting data/tasks/tools, supporting language feedback, etc.
4. AgentStudio shows the short coming of existing models. For example, existing models can do pretty well on single API tasks, but very poorly on compositional tasks.
5. Also the benchmark shows that specialized models can do better than general model. For example, SeeClick does better than Gemini, Claude, etc for GroundUI.

### Weaknesses
1. Not sure # of tasks is enough. I would love to see the # of tasks can continue to grow.
2. Currently, the software seems to be randomly selected. One potential improvement is that maybe the author can get some statistics of most used software and include the top ones into the Benchmark. For example, I would imagine Photoshop could be an interesting case to add to the evaluation suite.

### Questions
1. Will AgentStudio be open sourced?
2. I did not quite get "For example, we can create a failure trajectory by extracting the first few steps of a successful one" How exactly is failure example being created?

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
5

### Summary
This paper presents AgentStudio, a toolkit for building and evaluating general virtual agents that can interact with software through GUI and API interfaces. The main contributions are: (1) An interactive environment supporting multimodal observations and actions, (2) Tools for creating benchmark tasks and annotating data, (3) A benchmark suite of 205 tasks and three datasets (GroundUI, IDMBench, CriticBench) for evaluating fundamental agent capabilities.

### Strengths
1. The interactive environment design allowing both GUI and API interactions is valuable

2. It introduces an online task-completion benchmark and three datasets to evaluate fundamental agent abilities in real-world settings. The benchmark suite consists of 205 real-world tasks across various applications such as VS Code, Google Workspace,
and Office suites

3. Evaluating current LLM-based agents (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Qwen-VL-Chat) on real-world software interaction tasks, it provides good analysis of failure modes and limitations of existing models.

### Weaknesses
1. Limited technical novelty - the environment appears to be largely an integration of existing components without significant new technical contributions.

2. The three datasets created for fine-grained evaluation are quite small in scale: IDMBench, criticBench has only 345, 350 trajectories respectively.

3. Insufficient technical details about the implementation: 
Only cursory mention of using VNC and Docker
No discussion of performance, latency, scalability, reliability considerations

### Questions
Can AgentStudio enable large scale data collection, and agent evaluation? Will it support multi-threading that can be integrated to online RL training of agents? 

What are the key technical differences between AgentStudio and existing environments like VisualWebArena?

Why are the evaluation datasets so small? Are there plans to scale them up?

In IDM-Multiple, accuracy is calculated based on the exact match of the action sequences. Is this too restrictive? Would there be multiple optimal action sequences? Even suboptimal, but successful sequences demonstrate agent capabilities. 

The paper presents an interesting system but falls short in terms of technical novelty and scale of evaluation. The main contribution appears to be integration of existing components rather than fundamental technical advances. The small scale of the evaluation datasets also limits the impact. While the direction is promising, the current work would benefit from more technical depth and larger-scale evaluation.

Post rebuttal:
There are still further questions on how useful AgentStudio is as many components are very basic, e.g. annotation tool as characterized "minimalism". Furthermore, it is not clear college students are typical users and whether there are any quality control processes, the 51% calls into questions to the labeling process.

I still feel the paper is borderline. Nonetheless, I am happy to update my score.

### Soundness
2

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
2

### Summary
This paper presents a comprehensive toolkit that includes an environment, tools, benchmarks, and datasets designed to evaluate virtual agents’ capabilities across diverse software tasks. The authors focus on enabling realistic evaluations of agents in real-world settings, providing tools to easily construct these environments within a POMDP framework. They conduct extensive experiments on their benchmark, covering various GUI and API-related tasks, to assess the overall performance of current agents and their effectiveness in three specific tasks. Additionally, they introduce three datasets that address fundamental challenges, highlighting limitations in current models.

### Strengths
1. AgentStudio provides a holistic toolkit, including environments, tools, and benchmarks, addressing the need for flexible agent training across varied virtual scenarios​. It also supports diverse input modalities (text, images, videos) and action types (GUI, APIs), making it versatile for training agents to handle real-world tasks and improving generalizability.
2. The creation of GroundUI, IDMBench, and CriticBench highlights an effort to evaluate core agent skills such as GUI grounding and success detection, advancing the field with nuanced benchmarks​.
3. AgentStudio's lightweight design and compatibility with various operating systems (including Docker environments) improve accessibility and ease of use for a wider research audience​.

### Weaknesses
1. Although AgentStudio emphasizes versatility and real-world applicability, the benchmarks and tasks are still simulated in controlled environments, which may not fully capture the complexities of real-world application. The challenges faced by agents in uncontrolled, dynamic environments are difficult to replicate, which could limit the generalizability of the findings to actual user settings. Specifically, the simulation environment may not adequately model the variability in user interfaces, network latency, or unexpected system errors that agents would encounter in real-world scenarios. The reliance on a controlled setting could lead to an overestimation of agent performance, as agents might be optimized for the specific simulation parameters rather than generalizable problem-solving.
2. Success rates and accuracy are used as primary metrics, which may not fully capture an agent's capabilities, particularly in scenarios requiring complex decision-making or nuanced interaction. For example, success rates don’t account for partial progress in multi-step tasks, which may lead to an incomplete assessment of an agent’s performance and fail to identify areas where improvement is needed. Furthermore, these metrics do not capture the efficiency of the agent's actions; an agent might achieve a task but do so in a suboptimal manner, which is not reflected in a simple success/failure metric. The lack of metrics that assess the quality of the agent's interaction, such as the number of steps taken or the resource consumption, limits the evaluation's comprehensiveness.

### Questions
See above Weakness

### Soundness
4

### Presentation
3

### Contribution
3
