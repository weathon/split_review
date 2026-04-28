# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Software is one of the most powerful tools that we humans have at our disposal; it allows a skilled programmer to interact with the world in complex and profound ways.
At the same time, thanks to improvements in large language models (LLMs), there has also been a rapid development in AI agents that interact with and affect change in their surrounding environments.
In this paper, we introduce \projname (\emph{f.k.a.} OpenDevin), a platform for the development of powerful and flexible AI agents that interact with the world in similar ways to those of a human developer: by writing code, interacting with a command line, and browsing the web.
We describe how the platform allows for the implementation of new agents, safe interaction with sandboxed environments for code execution, coordination between multiple agents, and incorporation of evaluation benchmarks.
Based on our currently incorporated benchmarks, we perform an evaluation of agents over \numbenchmarks challenging tasks, including software engineering (\eg, \textsc{Swe-bench}) and web browsing (\eg, \textsc{WebArena}), among others.
Released under the permissive MIT license, \projname is a community project spanning academia and industry with more than 2.1K contributions from over 188 contributors.co/spaces/OpenHands/evaluation} \\
    \slack & \textbf{\small{Slack}} & \url{http://bit.ly/OpenHands-Slack}\\
\end{tabular}
\end{center}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces OpenHands, is a community-driven platform designed to advance the development of AI agents that interact with the world in terms of code writing, command-line interaction, and web browsing. OpenHands includes an evaluation framework for benchmarking agent performance on tasks like software engineering and web browsing. It supports various LLMs and sandboxed environments for running these AI agents and conducts extensive evaluation of different agents in various benchmarks.

### Strengths
- The motivation to build an open-sourced agent platform is good. 
- The agent interface, with capabilities for code execution and web browsing, is impressive.
- Evaluations conducted across various agents and benchmarks are thorough and extensive.

### Weaknesses
N/A

### Questions
This paper introduces an open platform with the event-driven architecture to advance the AI agent development, especially focusing on coding and web browsing. It also conducts extensive evaluations of heterogeneous agents on various benchmarks. This is a solid contribution to the LLM agent community. I have some questions about the implementation details. 
- The authors mention that event streaming enables human intervention in agent tasks, which I believe is a crucial step for calibrating agent outputs. I wonder whether human intervention is enabled during the evaluation of agents and is there a mechanism to determine whether human intervention is required?
- Regarding the multi-agent delegation feature, I’m unclear on how agents collaborate. Is there an orchestrator agent responsible for task delegation, or is this managed through event streaming? If it’s the latter, how are tasks assigned and dispatched, and where do agents deliver their outputs?

### Soundness
3

### Presentation
3

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
The paper presents OpenHands, an open-source platform designed to facilitate the development of AI agents that interact with the world through software interfaces such as code execution, command-line operations, and web browsing. A key feature of OpenHands is AgentHub, a platform where users can contribute their own agents (architecture) to the community, fostering collaborative development of agent architectures. The platform provides a simple agent abstraction, making it accessible for users to create and extend agents, and provides a modular architecture for agent interactions and task execution, including an event-driven state management system, multi-agent coordination, and an extensible agent skills library. OpenHands aims to enable agents to even create tools by themselves. The authors describe the architecture, implementation details, and evaluate the platform across multiple benchmarks, including software engineering tasks and web browsing scenarios. It's kind of a combination of AutoGen and BrowserGym.

### Strengths
Originality:
OpenHands uniquely consolidates multiple agent capabilities: coding, command-line interaction, web browsing, and multi-agent collaboration, within a single, open-source platform. The introduction of AgentHub allows users to contribute their own agents, promoting community collaboration and expanding the platform's versatility. This integration distinguishes OpenHands from existing frameworks, although IMO some of the main ones are absent from the comparison (see questions).

Quality: 
The methodological approach is solid, featuring a well-defined architecture that includes an event-driven state management system and a secure, sandboxed runtime environment. The use of an extensible agent skills library enhances flexibility, allowing agents to perform complex tasks and even create tools themselves. The agent abstraction is designed to be simple, enabling users to easily create and extend agents.

Clarity:
The paper is generally well-written and logically structured, making it accessible to both practitioners and researchers. Key components of the platform, such as the agent abstraction, runtime environment, and evaluation framework, are explained clearly. Figures and tables effectively illustrate concepts and results.

Significance:
By providing an open-source, MIT-licensed platform with contributions from a large community, OpenHands has the potential to significantly impact the development and evaluation of AI agents. It introduces a varied range of datasets for each general agent domain, although it could be expanded in the browser domain (see weaknesses). Evaluating multiple close-source LLMs on each task in addition to the average costs of evaluating benchmarks is a valuable addition that offers practical insights.

### Weaknesses
Limited Novelty in Certain Aspects: While OpenHands integrates various functionalities, much of the work appears to assemble existing components from the domain into one place. Some features, like code execution in a sandbox and web browsing agents, are present in other platforms. The paper could better articulate how OpenHands distinguishes itself from similar frameworks like LangChain, DSPy, or AutoGen.

Basic Implemented Agents: The currently implemented agents are relatively basic. For example, the Browsing Agent is based on WebArena's agent, which is very simple to implement and not competitive with current SOTA agents. There are more advanced multi-agent architectures available that could be implemented in AgentHub to better demonstrate the system's capabilities in facilitating the general agents' development.

Outdated Datasets: The evaluation includes MiniWoB++, which is an outdated dataset. There are newer datasets, such as WorkArena, WorkArena++, and ST-WebAgentBench, that are more relevant. The last test agents in more complex, restricted environments using policy hierarchies. Incorporating these in the framework would strengthen the evaluation.

Evaluation Depth: The evaluation, while broad, could benefit from deeper analysis. Incorporating an automated data collector to track agent success and failure would enhance insight into agent performance and make the framework more complete.

### Questions
Distinction from Existing Platforms: How does OpenHands fundamentally differ from other agent development platforms like LangGraph, CrewAI and DSPy for multi-agent collaboration or BrowserGym for benchmark evaluation? Could the authors elaborate on the unique features or advantages that OpenHands offers over these frameworks? Including these comparisons in Table 1 would provide a more comprehensive overview.

Agent Performance Analysis: Can the authors provide a more detailed explanation about the data collector in the framework? Specifically, what makes the framework the best solution to develop an agent when one approaches such a task?
Another question is: how will the platform address this in future iterations?

Handling of Observations: How does the platform treat observations and their full composition? Can the authors clarify how observations are managed and utilized by agents? Providing more details on the configuration and usage of the event stream would enhance understanding, especially for developers less familiar with event-driven systems.

Security Considerations: Given that the platform allows the execution of arbitrary code in a sandboxed environment, what security measures are in place to prevent potential exploits or breaches? Has the sandboxing been tested against known vulnerabilities? Discussing security protocols would demonstrate the platform's reliability.

Web Page Understanding Techniques: Regarding the web experiments, it is not clear which page understanding techniques are used to interpret interactable elements and web pages. Does the framework provide screen/page understanding capabilities, or should a new user implement their own methods? Clarifying this would help users understand the platform's capabilities in web interaction tasks.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
OpenHands is an open-source platform for the development of general AI agents. This paper details the motivation behind OpenHands, the architecture of the platform, how a user might implement an agent using OpenHands, description of some existing baseline agents, and comparison of some of the OpenHands agents against other open-source agents on software, web, and other assisting tasks. Selected results show that their agents perform reasonably well across a wide range of these tasks (generally underperform the specialized agents).

### Strengths
OpenHands is a valuable contribution to the research community. The OpenAgents platform will surely be used to develop many future agents, and be referred to as a baseline for other agent-developing research projects. Tables 3, 4, and 5 present thorough experimentation of their agent(s) compared to many other baselines on various tasks.

### Weaknesses
While the value of OpenHands is apparent, the research question of this paper is unclear. If it is that they can develop a general agent that performs better across a range of tasks than any existing agent does, it is my judgement that the results and analysis do not explore this sufficiently to warrant a research contribution. To do so, discussion and ablations should be included for the design decisions of OH Browsing Agent v*, OH CodeAgent v*, OH GPTSwarm v*, etc. To then isolate the effect of those decisions, the choice of backend model should be held consistent to those of the baselines against which the OH agents are compared. Error analysis of results comparing OH to baselines would be another welcome contribution that has been omitted from this paper.

### Questions
Can we further motivate why we want a generalist agent? If we have specialized agents for different tasks, can we just have a coordinator deploy specialized agents where they perform best?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper describes OpenHands, fka OpenDevin, a platform to develop LLM agents which can take meaningful actions using computers, such as browsing, coding, and interacting with a command line.

Section 2 describes the architecture of the platform, detailing the state and event streams, actions and observations, and an extensible library of tools. Agent delegation is also mentioned.

Section 3 mentions some notable agents implemented using their platform.

Section 4 presents results of many evaluatory benchmarks, showing the OpenHands has a broad and general level of competence across domains including coding and browsing.

### Strengths
OpenHands is an excellent and significant LLM-agent platform, seeing use e.g. as one of the reference agents in OpenAI's MLE-bench https://arxiv.org/abs/2410.07095 , and there is value in having this scaffold's architecture explained and benchmark performance reported in a peer-reviewed form.


- General competence across three different domains (SWE, browsing, and 'misc') is significant

- Solve rate of 26% on SWE-bench is competitive, as are many of the results suggested by the tables (though, see below, I have questions around like-for-like comparison)

- The paper provides a great many benchmark results

- OpenHands has many useful features, such as the API server being inside the docker container, the ability to delegate subtasks to other agents, and an extensible library of tools

### Weaknesses
The paper is an announcement of a software platform, more than it is a description of a contribution to a research area. Normally I'd expect a paper to look like a research question, with some motivation, experimental design, and results. This paper shows little, if any, scientific exploration, instead the paper gives a high-level overview of the architecture with little motivation, and then uncritically showcases performance on a broad range of existing benchmarks. I'm unsure whether this kind of project-announcement is a fit for the conference.

Some smaller points:

- Why do the (e.g.) GPQA results not compare like-for-like LLMs? I would want to see whether a CodeActAgent powered by a particular LLM was better or worse than the bare LLM, but the table compares (Llama 3 70b chat, GPT 3.5 turbo 16k, GPT 4) with (gpt-4o-mini-2024-07-18 , gpt-4o-2024-05-13 , claude-3-5-sonnet), so it's unclear how much of the difference is due to the scaffold and what is due to the choice of LLM. This is also true for many results in Tables 4 onwards, perhaps an unfortunate downside of comparing to results from the literature, but this limitation precluding rigorous comparison should at least be acknowledged in the text.

- A large fraction of the paper comprises short summaries of many different benchmarks used to evaluate the codebase. Since these summaries are not original work, I question whether so much of the paper should be dedicated to them. (As a minor point, I'd expect this exposition to be in a setup / methodology / problem-setting section, rather than in the results.) Instead, the authors could focus more on the creative decisions made during the creation of their platform.

- L305 - I'm uncertain what is meant by "we compare OpenHands to open-source reproducible baselines that do not perform manual prompt engineering specifically based on the benchmark content"

- It seems surprising that OH CodeActAgent w. GPT-3.5 would get 2% on ToolQA, while ReAct (perhaps the most minimal form of agent scaffolding) would get 36%. Do you have any idea what's behind this performance difference?

- Also surprising is that CodeActAgent delegating to BrowsingAgent does very slightly worse than straightforwardly using BA directly. Could you discuss this?

### Questions
L305 - I'm uncertain what is meant by "we compare OpenHands to open-source reproducible baselines that do not perform manual prompt engineering specifically based on the benchmark content"

It seems surprising that OH CodeActAgent w. GPT-3.5 would get 2% on ToolQA, while ReAct (perhaps the most minimal form of agent scaffolding) would get 36%. Do you have any idea what's behind this performance difference?

Also surprising is that CodeActAgent delegating to BrowsingAgent does very slightly worse than straightforwardly using BA directly. Could you discuss this?

### Soundness
2

### Presentation
3

### Contribution
3
