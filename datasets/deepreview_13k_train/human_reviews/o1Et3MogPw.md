# Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence

- Decision: Accept
- Scores: 6, 8, 6, 8, 8

## Abstract
The rapid advancement of large language models (LLMs) has paved the way for the development of highly capable autonomous agents. However, existing multi-agent frameworks often struggle with integrating diverse capable third-party agents due to reliance on agents defined within their own ecosystems. They also face challenges in simulating distributed environments, as most frameworks are limited to single-device setups. Furthermore, these frameworks often rely on hard-coded communication pipelines, limiting their adaptability to dynamic task requirements. Inspired by the concept of the Internet, we propose the Internet of Agents (IoA), a novel framework that addresses these limitations by providing a flexible and scalable platform for LLM-based multi-agent collaboration. \framework introduces an agent integration protocol, an instant-messaging-like architecture design, and dynamic mechanisms for agent teaming and conversation flow control. Through extensive experiments on general assistant tasks, embodied AI tasks, and retrieval-augmented generation benchmarks, we demonstrate that \framework consistently outperforms state-of-the-art baselines, showcasing its ability to facilitate effective collaboration among heterogeneous agents. \framework represents a step towards linking diverse agents in an Internet-like environment, where agents can seamlessly collaborate to achieve greater intelligence and capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the "Internet of Agents" (IoA) framework to facilitate enhanced collaboration among autonomous agents using large language models (LLMs). Inspired by the Internet’s structure, IoA aims to address the integration challenges seen in current multi-agent systems (MAS). This is achieved through three key innovations: a protocol for integrating diverse agents, a layered architecture resembling an instant-messaging framework, and mechanisms for dynamic team formation and conversation flow. Through a series of experiments, the paper claims that IoA enables more effective collaboration than existing MAS frameworks, particularly in domains like retrieval-augmented generation (RAG) and embodied AI tasks.

### Strengths
- Innovative Conceptual Framework: The IoA draws a compelling parallel between the functionality of MAS and the Internet, introducing layered architecture and team formation protocols that offer adaptability and scalability.

- Comprehensive Experiments: The paper provides a well-rounded experimental design, including benchmarks that demonstrate the system’s effectiveness across multiple task categories.

- Task-Specific Improvements: IoA demonstrates improved performance in benchmarks like the GAIA and RAG, highlighting its potential advantage over existing MAS in facilitating agent cooperation and integrating heterogeneous tools.

### Weaknesses
 - Lack of Detailed Evaluation on Real-World Applications: While the experimental benchmarks are extensive, the paper lacks real-world application scenarios that demonstrate the IoA’s effectiveness in real world environments that require distributed settings. It is not unclear why GAIA benchmarks would need agents over internet instead of a simple central multi-agent system.

- Scalability and Performance Analysis: The paper lacks analysis on IoA’s computational overhead and network latency issues, especially when scaled to large numbers of agents across different devices distributed settings. An understanding of these scalability and performance trade-offs is critical.

- Vagueness in Mechanisms for Conversation Flow Control: The conversation flow control relies on LLMs and a finite state machine (FSM) for transitions, but the scalability of this approach when coordinating many situations with many states is not well justified. It would be great to have some ablation studies.

- Limited Insight into Integration of Third-Party Agents: The implementation of heterogeneous agent integration is described conceptually, but details on handling diverse architectures and security considerations when integrating third-party agents are lacking.

- Limited Novel Research Contributions: The paper’s focus on architecture and engineering limits its contribution to ML research. While the framework offers novel infrastructure, the lack of new research methodologies or performance optimizations in agent interactions might reduce its appeal in ML-centric venues.

### Questions
- How does IoA handle latency and data synchronization when agents are distributed across devices in real time?

- How does the protocol for agent integration address security, especially for third-party agents that may have differing trust levels? Could the authors expand on IoA’s security measures, especially regarding agent registration and message routing?

- Can the FSM for conversation flow control be adapted or scaled effectively if used with a larger number of agents than tested in the experiments? How adaptable is the finite-state machine-based flow control to tasks requiring high real-time interaction or rapid state changes?

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
3

### Summary
This paper introduces the Internet of Agents (IoA), a novel framework for LLM-based multi-agent collaboration, inspired by the concept of the Internet. The framework aims to facilitate collaboration among autonomous agents by addressing the limitations of existing multi-agent frameworks, including ecosystem isolation, single-device simulation, and rigid communication and coordination. IoA consists of two core components: the server and the client. The server acts as a central hub controller, while the client serves as a wrapper for individual agents, enabling the necessary communications and protocols. The IoA architecture has three layers, i.e., interaction, data, and foundation layers, they collectively accelerate agent collaboration through the network. Experiments conducted in various settings demonstrate the effectiveness and versatility of IoA in facilitating efficient collaboration among heterogeneous agents.

### Strengths
The paper is well-written and organized, with the key components of IoA clearly illustrated and easy to follow.

The experiments are comprehensive, assessing IoA's capability to integrate agents with heterogeneous tools on the GAIA benchmark. It introduces a robust benchmark comprising 153 open-ended instructions spanning four diverse categories. The results illustrate IoA's effectiveness in integrating, orchestrating, and enabling independently developed agents with heterogeneous architectures. Further experiments with RoCoBench highlight IoA's ability to enhance the communication and collaboration capabilities of embodied agents. 
Moreover, in the RAG question-answering domain, IoA also surpasses existing methods.

### Weaknesses
In Section 3.2, while the paper constructs 153 open-ended instructions spanning four categories—search & report, coding, math, and life assistant—there is a lack of sufficient or list of examples (only one figure) to illustrate whether the questions are complex and require multi-step reasoning, or if they can be directly solved.  Therefore, the authors could include an appendix with a representative sample of tasks & solutions from each category, or provide a link to the full benchmark.

Additionally, the paper primarily employs GPT-4 as an impartial judge of response quality, but IoA might require more steps than competitors such as AutoGen.

### Questions
It would be beneficial to provide additional examples related to the constructed benchmark and to illustrate the specific steps undertaken by IoA.

GPT-4 might occasionally give higher evaluation scores or exhibit overconfidence. Could you discuss any potential biases or limitations associated with using this evaluation method in your benchmarks and whether you considered alternative evaluation approaches.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Internet of Agents framework for multi-agent collaboration, where agents from different developers communicate via an instant-messaging-like architecture and work in teams.
Communication is implemented by abstracting several conversational states, and implementing a finite-state machine to support state transition for agents.
The set of states includes 5 states, representing discussion, synchronous task assignment, asynchronous task assignment, pause & trigger, and conclusion, so and most of the "work" happens in the discussion state (this was not very clear to me).   Each agent has a LLM-based component which determines state transitions and selects the subsequent speaker.
The framework is evaluated using experiments with three types of tasks where teams of agents communicating using Internet of Agents framework are compared to existing multi-agent systems.

### Strengths
Inventing a "language" that can enable information transfer between different versions of AI agents is an exciting research question. It is certainly a useful idea, as proliferation of AI agents comes with a proliferation of agent versions and brands. At this stage, the question is still rhetorical rather than practical, as it took decades to build countless networking protocols for wireless routers and phones, like SIP, H323, TCP, UDP,.... In the current work the authors touch upon a novel question of introducing such as language, and take a step toward considering what would this language look like.

### Weaknesses
I feel like the authors miss the opportunity to focus the argument as a rhetorical/philosophical consideration to build an analogy with internet communication protocols.
Given the novelty of the issue, the system is still a toy and the experimental evaluation does not look as convincing as the conceptual notion of the potential that such a framework could be. 

Part of this general presentation issue, I find the Figure 1 to be much too cluttered. Maybe one way to approach this is to use an open source diagram creation tool, like draw.io, to make a clean arrows and boxes diagram with minimal text, showing how the various components interact. 

The paper could benefit from a few task workflow examples.

Overall all these comments are referring to one common point, which is lack of focus and clarity. My impression from this paper is that this is a worthy subject, but it is difficult to assess (rather than infer) what was done.

### Questions
How where these three specific benchmarks chosen?

The workflow of the conversational state machine is unclear to me. How are the tasks broken down into components? 

Each agent has a LLM component that manages state transitions, and which other components must agents have, to be part of this framework? 

Are only LLM-based agents able to participate in the framework?

Is it possible to present results (e.g. Table 3) as a bar plots with confidence intervals? If not, why?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Internet of Agents (IoA), a framework for enabling distributed collaboration among heterogeneous LLM-based agents. The key innovations include: 
(1) a protocol for distributed agent collaboration: a multi-layered architecture that enables agents to operate across different devices and locations, where each agent maintains its own "WebSocket" connection to a central server that handles message routing and coordination.

(2) an instant-messaging-like architecture for agent discovery and teaming: agents can search for collaborators based on capability descriptions and form nested teams, implemented through a central registry that maintains agent capabilities and allows semantic matching for team formation

(3) dynamic mechanisms for conversation flow control: a finite state machine approach that manages conversation states (discussion, task assignment etc.,), where LLMs autonomously decide state transitions and next speakers to maintain structured dialogue

(4) a protocol for integrating third-party agents: a standardized interface that requires agents to implement a simple `run()` function accepting task descriptions and returning results, allowing agents built under different protocols (AutoGPT or OpenInterpreter) to be wrapped and integrated into the framework.

IoA (GPT3.5) is evaluated across GAIA benchmark, open-ended instructions, embodied AI tasks, and retrieval-augmented generation, and IoA consistently outperformed other baselines on GAIA, open-ended instruction benchmark and matches or exceeds GPT4 performance on IoA.

### Strengths
1. The architecture is novel and the design is well-motivated which address three key issues in typical multi-agent systems (MAS). 
2. The technical foundation is clear as there is rigorous formalization of key mechanisms and detailed ablation studies showing importance of each component
3. The evaluation is comprehensive as it include a variety of benchmarks testing different aspects of agent heterogeneity along with strong empirical results across all tasks. (GPT3.5-based IoA agents outperforming GPT4 baselines)

### Weaknesses
One major concern about this framework is the cost (compute/financial) as Table 6 showed IoA is much more expensive than other multi-agent frameworks like AutoGPT and Open Interpreterm which might limit deployment of this frame at scale.

### Questions
How does performance scale with increasing number of agents?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose the Internet of Agents (IoA), a novel framework for enabling collaboration between heterogeneous AI agents distributed across different devices. Drawing inspiration from the Internet's architecture, IoA introduces key mechanisms including agent registration/discovery, nested team formation, conversation flow control using finite state machines, and flexible task assignment. The framework addresses limitations of existing multi-agent systems like ecosystem isolation, single-device constraints, and rigid communication pipelines.

### Strengths
- The authors present a well-motivated and timely contribution given the rapid advancement of autonomous agents and the need for frameworks to orchestrate their collaboration
- The layered architecture design is elegant and comprehensive, with clear separation between interaction, data, and foundation layers for both server and client components
- The experimental evaluation is thorough, testing the framework across diverse scenarios including general assistance, embodied AI tasks, and retrieval-augmented generation
- The nested team formation mechanism is theoretically sound, with formal analysis showing reduced communication complexity compared to fully connected structures
- The finite state machine approach to conversation control is well-grounded in Speech Act Theory and provides a principled way to manage agent interactions

### Weaknesses
 - While the authors demonstrate strong empirical results, the theoretical analysis of the framework's properties (e.g., convergence guarantees, scalability limits) could be strengthened
- The evaluation focuses primarily on task performance metrics. Additional analysis of system properties like latency, resource usage, and communication overhead would be valuable (I do see some of this in Appendix E)
- The authors could expand on potential failure modes and mitigation strategies, particularly for scenarios with unreliable network connections or agent failures
- The security implications of allowing distributed agents to collaborate deserve deeper treatment, including potential vulnerabilities and safeguards. I appreciate that the authors included the Security Module in the schematic, but think having a bit more discussion of it (in the appendix) could be beneficial

### Questions
- Really cool that you drew inspiration from Speech Act Theory for this work. Have you considered what Rational Speech Act has to offer in this case? Would be neat to see it leveraged to deal with things like recursive reasoning (theory of mind), own uncertainty and uncertainty of other agents, etc.
- How does the system handle potential deadlocks in the conversation state machine? Are there specific examples of potential deadlock scenarios you've considered? Can you describe any mechanisms or safeguards implemented to prevent or resolve such deadlocks in the conversation flow?
- What mechanisms ensure fair resource allocation when multiple agent teams are operating simultaneously?
- How does the framework maintain consistency when agents have conflicting knowledge or goals?
- Could the authors elaborate on the scalability limits of the nested team formation approach?
- What strategies are employed to prevent malicious agents from disrupting team collaboration? Is that just offloaded to the Security Module?

### Soundness
3

### Presentation
4

### Contribution
4
