# LLM Agents Should Employ Security Principles

- Decision: Reject
- Scores: 9, 7, 8

## Abstract
Large Language Model (LLM) agents show considerable promise for automating complex tasks using contextual reasoning; however, interactions involving multiple agents and the system's susceptibility to prompt injection and other forms of context manipulation introduce new vulnerabilities related to privacy leakage and system exploitation. **This position paper argues that the well-established design principles in information security, which are commonly referred to as *security principles*, should be employed when deploying LLM agents at scale**. Design principles such as *defense-in-depth, least privilege, complete mediation, and psychological acceptability* have helped guide the design of mechanisms for securing information systems over the last five decades, and we argue that their explicit and conscientious adoption will help secure agentic systems. To illustrate this approach, we introduce AgentSandbox, a conceptual framework embedding these security principles to provide safeguards throughout an agent’s life‑cycle. We evaluate with state-of-the-art LLMs along three dimensions: benign utility, attack utility, and attack success rate. AgentSandbox maintains high utility for its intended functions under both benign and adversarial evaluations while substantially mitigating privacy risks. By embedding secure design principles as foundational elements within emerging LLM agent protocols, we aim to promote trustworthy agent ecosystems aligned with user privacy expectations and evolving regulatory requirements.

## Human Reviews

## Human Reviewer 1

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
This position paper highlights that current LLM agents face serious, unresolved security and privacy risks, especially in multi-agent scenarios and under prompt injection attacks. The authors argue for explicitly adopting established security principles—defense-in-depth, least privilege, complete mediation, and psychological acceptability—rather than relying on ad hoc defenses. They propose AgentSandbox, a framework that systematically incorporates these principles through component isolation, context-aware access control, and adaptive policy management. Empirical results on the AgentDojo benchmark show that AgentSandbox offers a better balance of security and utility than existing methods. The paper calls on the NeurIPS community to make such foundational security principles standard practice for LLM agents.

### Strengths
1. Clear, actionable agenda: Provides a practical security agenda for agentic AI, bridging decades of security engineering wisdom and modern LLM challenges.

2. Novel system architecture: The AgentSandbox design (with persistent/ephemeral agents, I/O firewalls, etc.) is original, modular, and extensible.

3. Empirical grounding: Evaluations are performed on AgentDojo with multiple LLMs, using multiple baselines, supporting the position with real data.

### Weaknesses
1. Conceptual/prototype level: While AgentSandbox is well-motivated, it remains a conceptual framework; some implementation details are high-level or left for future work.

2. Evaluation scope: Empirical evaluation, though strong, is mostly on synthetic benchmarks (AgentDojo); further deployment in real-world, long-running agent settings would strengthen claims.

3. Adaptability and overhead: Some discussion of computational/resource overhead or usability trade-offs in complex multi-agent environments would be valuable.

### Questions
1. How does AgentSandbox perform when scaled to real-world, persistent multi-agent systems with dynamic, evolving tasks and long-term memory?

2. What are the expected computational and operational overheads of maintaining ephemeral agents and continuous mediation in production?

3. Can the reward modeling policy engine adapt to new, unseen attack vectors without explicit rule updates, or is continual retraining required?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper propose a position: the well-established design principles in information security should be employed when deploying LLM agents at scale. To justify the position, the authors propose a security framework called AgentSandbox that applies these security principles into the agents. They further provide illustrative examples and evaluations to show the resistence of AgentSandbox againts privacy and security problems.

### Strengths
The security of LLM agents is a very important topic and this work is very timely.
The proposed position is very reasonable, especially the idea of incorporating well-established secutiry principles from studies of  information security. 
The proposed framework is well described and shows a lot of potential. While this work only shows a basic impelmentation of these principles, the framework indeed brings many inspirations for future development of more robust and trustworthy agents.

### Weaknesses
I only have a minor concern. Since this work already proposes a security framework, what other aspects should future agent builder and deployer be care of?

### Questions
While I am not an expert in information security, I am curious that except for the 4 principles discussed by this work, what about other principles, since the authors mention that '... introduced eight design principles for secure systems...'?

The proposd framework is described in a general way, then are there any specific challenges when applying it to different domains, like medical, finance etc? I am curious in more details.

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
"LLM Agents Should Employ Security Principles" argues that LLM agent applications should adopt a general framework that ensures cybersecurity by design, drawing inspiration from traditional security principles. The authors propose a specific design pattern representing their own interpretation of how those traditional principles should be translated into the novel domain of LLM agents. While the overall goal of cybersecure agents is not a controversial position, there is not yet a level of consensus on the appropriate design patterns as there is in more established domains of cybersecurity. Discussing what a good design pattern would look like is an excellent and timely topic. 

The authors advocate for a separation of permanent and ephemeral AI agents to compartmentalize the application, thereby creating barriers around potential penetration vectors. They also envision a firewall for external traffic and an additional layer of protection between the user data and the ephemeral agent. In doing so, they incorporate traditional principles such as least-privilege data access, complete mediation on every agent action, defense-in-depth, while also following psychological acceptability by minimizing user intercession.

### Strengths
While anyone would typically agree that LLM agent applications should be cybersecure, it is not clear exactly what design patterns should become the industry-standards the way developers have such standards for other domains, such as internet protocols, and OAuth. Determining what these design patterns would be is a major undertaking, but a timely one as agentic applications come to market and new cybersecurity threats emerge. Security should be a concern to all developers and researchers of LLMs, and a venue like NeurPS is an excellent one to discuss these principles. 
The article does not simply state that agentic applications should be secure, but goes further by introducing their own proposed design pattern complete with demonstration on a benchmark. Demonstrations with measurable outcomes like this are a very fruitful way to commence a discussion: no one work will arrive at a completely full-proof principle, but attempts like this are sure to stimulate the kinds of discussions that can lead us there.

### Weaknesses
The core position that agentic LLMs should use security principles is hard to disagree with as a high-level idea and so I think the more fruitful area of discussion is what colleagues think of the particular design pattern proposed with a view to constructively addressing weaknesses and agreeing on strengths.

### Questions
This paper provides a great applied example with the AgentDojo benchmark. This is sufficient for the paper's goal of a proof of concept, however surely more comprehensive testing is warranted before trusting such an application in the real world. My question is: do the authors have any insight into how, in the future, developers could comprehensively test a design like that of AgentSandbox against enough possible threats as to make it production ready?

### Presentation
4
