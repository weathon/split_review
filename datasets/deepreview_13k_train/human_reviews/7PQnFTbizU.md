# Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
AI Agents are changing the way work gets done, both in consumer and enterprise domains. However, the design patterns and architectures to build highly capable agents or multi-agent systems are still developing, and the understanding of the implication of various design choices and algorithms is still evolving. Agent-E introduces numerous architectural improvements over prior state-of-the-art web agents such
as hierarchical architecture, flexible DOM distillation and denoising method, and the concept of \textit{change observation} to guide the agent towards more accurate performance.
We first present the results of an evaluation of Agent-E on WebVoyager benchmark dataset and show that Agent-E beats other SOTA text and multi-modal web agents on this benchmark in most categories by 10-30\%. We then synthesize our learnings from the development of Agent-E into general design principles for developing agentic systems. These include the use of domain-specific primitive skills, the importance of distillation and de-noising of environmental observations, the advantages of a hierarchical architecture, and the role of agentic self-improvement to enhance agent efficiency and efficacy as the agent gathers experience.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Agent-E, a web agent designed to perform complex web-based tasks more efficiently. Agent-E employs a novel hierarchical architecture comprising three LLM-powered components: a planner agent, a browser navigation agent, and a verification agent.

The planner agent is responsible for high-level task management, breaking down user instructions into a sequence of manageable subtasks. These are delegated to the browser navigation agent, which plans and executes the necessary lower-level actions to complete each subtask. To handle the complexity of DOMs and improve interpretability, the browser agent utilizes a flexible DOM distillation approach, selecting the most suitable DOM representation for each task to highlight key elements and avoid overwhelming the LLM with unnecessary information. Additionally, the agent employs a 'change observation' mechanism, inspired by the Reflexion paradigm, where it monitors state changes after each action and receives verbal feedback to enhance situational awareness and performance.
Agent-E also incorporates a verification agent that provides feedback on incomplete or failed tasks, enabling a self-correcting system through a self-refinement mechanism. Agent-E was tested in on the WebVoyager benchmark.

### Strengths
Originality
The paper demonstrates a nice degree of originality, primarily through the architectural approach in Agent-E. By introducing a hierarchical framework with distinct, specialized roles (planner agent, browser navigation agent, and validation agent), the authors effectively address several challenges in web automation. The flexible DOM distillation approach is another contribution, as it allows the browser navigation agent to dynamically tailor DOM representations to the specific needs of each task. This feature moves beyond static DOM handling methods seen in prior work, reducing cognitive load and enhancing accuracy. Furthermore, the self-refinement mechanism, inspired by a Reflexion-like paradigm, adds a unique layer of adaptability, allowing the agent to detect and correct failures in real-time. Together, these components present a good advancement over traditional web agents.

Quality
The paper is supported by an experimentation and evaluation on the WebVoyager benchmark. The authors provide a detailed comparison with both text-only and multimodal web agents, showing improvements over existing methods. 

Clarity
The paper is generally clear and well-organized, with each component of Agent-E’s architecture clearly described. The role and function of the planner agent, browser navigation agent, and validation agent are each explained in detail, providing readers with a solid understanding of how Agent-E manages complex tasks. The authors also do a nice job of explaining the novel DOM distillation and change observation mechanisms (assuming you are reading the appendix). 

Significance
Agent-E’s contribution looks significant in the field of autonomous web navigation, overcoming limitations in current web agents—particularly around handling complex, multi-step web tasks and interpreting lengthy and dynamic DOMs. The hierarchical architecture and the adaptive DOM distillation approach are likely to inspire future research on modular and adaptable agent architectures. The self-refinement mechanism also has broader implications, showcasing a feasible pathway for self-correcting agents that can enhance reliability in real-world applications. Given the increasing integration of LLM-powered agents in business and personal automation, Agent-E’s success rate and improved reliability on the WebVoyager benchmark underline its potential impact in advancing practical applications in web-based automation.

### Weaknesses
1. My main concern is regarding the limited benchmarking scope. While the paper presents results on the WebVoyager benchmark, the reliance on a single (one would say old) benchmark limits Agent-E’s effectiveness. Given the paper's goal to establish Agent-E as a state-of-the-art web agent, it must be evaluated on additional benchmarks: WorkArena, WebArena, ST-WebAgentBench.
This is a major weakness as I am not sure if the results will be the same on the SOTA benchmarks. I must admit that it is very hard for me to judge this agent based on the WebVoyager benchmark solely. 

2. Agent-E’s architecture, with separate planner, browser, and validation agents, potentially introduces increased complexity and computational overhead. The paper does not fully address how this architecture scales in terms of computation and memory requirements, particularly when applied to larger, real-world workflows. Including benchmarks of computational resources used by Agent-E compared to simpler, single-agent systems would provide valuable insights.

### Questions
1. Can you add an explanation of DOM distillation, with performance analysis under different conditions?
2. Can you provide an in-depth study on the self-refinement mechanism’s impact on various error types and discuss potential trade-offs?
3. Can you include computational efficiency metrics and discuss optimizations or scalability considerations?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel architecture for solving Web tasks, comprising a multi agent system with a planner agent, browser navigation agent and validation agent. Next to the agent architecture, the authors propose a novel preprocessing/action formulation, where the agent gets access to a hand-made API. The latter enables to get the DOM tree in different representation or additional fine-grained filtered information. 

The new agent system is evaluated on the WebVoyager benchmark, where it is compared with the provided baselines of the benchmark (using gpt4-turbo) itself plus a recent text only approach. The results show that the new agent system is on par or better for the different sub-tasks, where an additional improvement can be seen when activating the validation agent (using gpt4-o).

### Strengths
- Sensible research direction, as LLMs can be of great use in automatizing various Web tasks
- Superior empirical results on existing benchmark, which includes representative Web tasks
- Key learnings are extracted from the proposed method, including the implmeneted task-specific agent design

### Weaknesses
 - Unclear if added value comes from DOM API or multi-agent system. At this point, it would be of value to have ablations or a proper baseline with only one LLM which uses the API. 
- Unclear if choice of gpt4-o for the validation agent has an impact on the results.
- Related work does not concisely depict the delta to other works, but simply list other works.
- No usage of open-source models, which could additionally be fine-tuned

### Questions
- Have you empiricially evaluated the impact of using provided API and the agent design? The impact of the validation agent was evaluated separately, so one can extract the added value.
- Does the task-specific agent design might have limitations to Web tasks or would it generically work well for any browser-based Web task? 
- What is the motivation and influence of using gpt4-o as validation agent and not sticking to gpt4-turbo? Would the results be less competitive with a gpt4-turbo validation agent?
- Have you performaned fine-tuning experiments with open-source models?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Agent-E, an LLM-driven web agent designed to perform a range of web tasks including: page interaction, form filling, content summarisation, and analysis of DOM structures. Agent-E uses 3 LLM-powered agents to respectively perform high-level task planning, browser navigation to complete given tasks, and validation - in particular providing feedback on browser state when tasks are incomplete; allowing the agent to re-attempt the task and self-correct.

Further, the authors introduce 3 novel DOM Distillation strategies to pre-process the DOM that is presented to the LLM-powered agents. These are (1) text only - used in summarisation tasks (2) input fields - used in search or form-filling type interactions and (3) all fields - a complete JSON representation of all elements in the DOM. Additionally the authors provide change observations, such noting that popups appear when an LLM interacts with a button, to support the browser navigation agent in planning its next step.

### Strengths
- The paper tells a clear narrative, and does a good job of presenting the high level agent architecture, and capabilities of the agent.
 - Achieves SOTA performance on the WebVoyager benchmark, and justify use of this benchmark due to the diversity of pages available. The paper could be further strengthened by running their agent on the other benchmarks discussed in their paper.

**Originality**
The authors introduce several seemingly novel techniques that allow them to achieve SOTA performance on WebVoyager , including:
 - Use of distinct agents for high-level planning, browser navigation, and validation of success
 - Use of feedback from validation agent to re-attempt failed tasks
 - Use of DOM Distillation
 - Providing change actions to the browser navigation agent

**Quality**
The evaluation is thorough and displays the performance of different variations of the validation / refinement architecture across different websites in the benchmark.

**Clarity**
The paper clearly describes the high-level architecture of the agent, novel contributions and evaluation. However, it lacks various details that make it understand, e.g., the implementation of each agent (prompting and inputs) and does not have supplementary materials such as a codebase to facilitate this understanding.

**Significance**
The system achieves SOTA performance on the WebVoyager benchmark, beating previous models by over 16%.

### Weaknesses
 - The authors choose to not make their code available for review. This makes it difficult to assess the accuracy with which the paper describes their codebase. Please provide anonymised repo using something like https://anonymous.4open.science/, and describe more details of your agent architecture in the appendix (i.e. prompts used for each agent). Morever, this limits the *theoretical* contributions of the paper, as various contributions of the work, are not described in great detail in the work. Such contributions include:
    - Change observation: No explanation is given of what information is given to the LLM to generate the natural language change observation; is it the DOM before and after? a diff? or some more novel algorithm that is applied?
     - What is the architecture of the validation agent / what information is it given to identify whether a task has been completed or not and give feedback
 - There are several claims that are not well quantified by the authors, including:
	 - "We consider the primitive skills we enabled in Agent-E to be enough for the vast majority of general web automation tasks": Perhaps there are statistics you can provide such as the number of tasks in the WebVoyager benchmark which require skills that are not enabled; and elaborate more on why 
- The Agent Design Principles are based soley on the authors learnings and intuition, this section could be improved by drawing upon and referencing existing works that discuss architectures / design principles for (1) agentic software (2) LLM planning (3) LLM accuracy optimisation esp. when dealing with structured data. We also comment on some specific design principles:
	- "Routinely analyze, reflect": please use more precise language than "reflect"; it seems like you have (1) batch jobs that find common tasks and turn them into reproducible workflows that can be called (2) allow for tasks to be re-run with knowledge of outcomes from past tasks - much of this seems like optimisations for production settings, but not something that is particularly insightful from a scientific standpoint. I would have expected the word reflect to likely indicate fine tuning but that does not appear to be the case here.

### Questions
**Question**
 - Nitpick: Why did you choose the name verification agent, this confused me on the first read of the paper as I thought this agent would verify the *plan*, instead it seems that this agent is used to assess whether a task has succeeded after execution, and prompt re-attempt on failures. Perhaps something along the lines of "reviewer", "monitor" or "feedback" agent may be better.
 - "Hierarchical architecture excels in scenarios where tasks can be decomposed into sub-tasks that need to be handled at different levels of granularity"; realistically this just seems to be helping an LLM with Chain of Thought by getting it to decompose tasks at different levels of granularity giving it more time to "think". Have you run experiments to see if this hierarchical architecture still provides benefit when using models like o1-preview that are able to do this kind of chain-of-thought work out of the box.
 - Is DOM Distillation a term that the authors of this paper have coined, or is it used elsewhere?
 - What methodology, if any, was used to identify the 3 agent architecture - were there any other architectures that were tried before this?
 - Why was only the validation agent tested with vision modalities?

### Soundness
2

### Presentation
3

### Contribution
3
