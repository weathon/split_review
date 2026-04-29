# LLM Agent Communication Protocol (LACP) Requires Urgent Standardization: A Telecom-Inspired Protocol is Necessary

- Decision: Reject
- Scores: 4, 4, 5

## Abstract
This position paper argues that the LLM agent field must urgently adopt a unified, telecom-inspired communication protocol, exemplified by our proposed LLM-Agent Communication Protocol (LACP), to overcome critical deficiencies in current ad-hoc approaches that threaten safety, interoperability, and scientific progress. The prevailing landscape of fragmented protocols, perilously echoing early networking's ``protocol wars'', severely curtails agent collaboration and reliability. Our analysis identifies fundamental flaws including crippling interoperability gaps  that lead to scientific stagnation, inherent insecurity due to security being an afterthought, and a lack of transactional integrity stemming from monolithic designs unsuited for critical operations.

Drawing direct inspiration from telecommunications' transformative standardization, which championed principles like layered abstraction, security by construction, minimal core with extensibility, and consensus-driven interoperability, we propose LACP. LACP is a principled, three-layer framework  designed to ensure agents communicate with clear semantic intent, engage in reliable, verifiable transactions, and benefit from inherent security. It embodies its core tenets—minimal core, layered design, security by default, and content agnosticism—to provide a robust and adaptable communication foundation. We urge the NeurIPS community to spearhead the adoption of such a principled approach before current fragmentation becomes an irreversible impediment to trustworthy AI, particularly in high-stakes domains. This strategic shift is vital for unlocking the full scientific and societal potential of collaborative AI.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper argues that the Agentic AI field is heading towards something similar to the protocol wars in the early days of computer networks and that protocol standardization for agent-to-agent communication is necessary. While drawing insights from the history of telecom standardization, the authors compare existing agent-to-agent communication frameworks and point out their limitations. Finally, the authors present LACP, a framework for LLM-Agent communication, which they argue should be adopted immediately to lay a strong foundation for the future of verifiable, secure, and scientifically reproducible multi-agent systems.

### Strengths
[S1] The paper discusses a timely and relevant topic.

[S2] The position statement is easy to understand and important for the field and to the NeurIPS community.

[S3] The paper draws parallels from the history of telecommunication, and I believe we can surely learn from it to build future systems for agentic AI.

### Weaknesses
While the position of the paper makes sense, the arguments in favor of the position are either not thorough enough or assume working knowledge of agentic communication infrastructure.

[W1] As a person working in agentic AI infrastructure, I understand the limitations presented in Section 2.2. However, the arguments are definitely not strong enough for a general audience, especially an ML audience not fully well-versed with system infrastructure. For example, what part of the ecosystem is fragmented? What incompatible formats and ad-hoc APIs are the authors talking about? Monolithic designs are not always bad. Therefore, what complexities are the authors talking about?

[W2] LACP architecture presented is quite shallow. There is not enough evidence to justify the components. For example, why did the authors choose to have PLAN, ACT, and OBSERVE as the message types? Similarly, there is little to no justification as to why transactional guarantees like 2PC need to be standardized. Or alternatively, why should we not just rely on the security provided by TLS?

[W3] Similar to W1, in Section 4.3, how LACP brings the advantages is not properly justified.

[W4] Figure 1 is unclear and not properly explained.

### Questions
- Table 1's caption says that the table presents how LACP addresses the limitations of the framework. How is the table showing the limitations being addressed?

- It was very unclear to me why each of the features described in Table 3 was really needed in the protocol itself. Can the authors please explain?

### Presentation
2

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This position paper emphasizes the need for immediate standardization for the communication protocols of LLM Agents, drawing parallels to the historical “protocol wars” of telecommunications. It reviews the existing protocols of agents (OpenAI Functions, LangChain Agent Protocol, MCP, ACP, ANP, Agora, Google A2A) outlining their systemic shortcomings of fragmentation, insufficient security, lack of transactional fidelity, and inadequate interoperability. The authors set forward the LLM-Agent Communication Protocol (LACP) which is composed of an architectural three-layer model (Semantic, Transactional, Transport) drawing from telecom standards of minimal core, layered construction, security by default, and extensibility. The main goal of LACP is secure, verifiable, and interoperable communication of agents, especially in domains where safety is critical. The paper also presents and defends counterarguments that LACP would stymie innovation by claiming that LACP would be more favorable towards scientific innovation, while also allowing for a strengthened agent network.

### Strengths
* This paper does an excellent job of explaining why there is a need for standard communication protocols for LLM agents and why it is urgent.

* The telecom standardization comparison (ITU/3GPP, layered abstractions, minimal core + extensibility) is very enlightening and serves its purpose.

* The LACP architecture explanation is complete for a three layer architecture with discrete types of messages, security features, and transaction guarantees.

### Weaknesses
1. There is no experimental demonstration showing LACP’s actual performance, interoperability gains, or security benefits. This makes it harder to assess feasibility and adoption cost.
2. Line 281-289: The “<5% overhead” projection lacks empirical support on representative multi-agent workloads,
3. The explanation of layering at the semantic/transactional/transport level is adequate, however, concrete examples of message schemas, handshakes, or other forms of integration would aid in actualizing the proposed vision.
4. While historically informative, the analogy risks oversimplifying differences between LLM agent ecosystems and telecom infrastructure (e.g., faster iteration cycles, looser regulatory environment).

### Questions
Have you implemented a prototype LACP stack and measured its performance and integration overhead with some existing frameworks?

### Presentation
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper draws inspirations from studies in telecommunication area and propose to develop a standard protocal for LLM agents to ensure secure and efficient communications. The authors propose four principles for the protocol design and also propose the LACP as an example for illustration. Finally, they also discuss the alternative views.

### Strengths
This paper is written well and easy to follow. The topic of developing communication protocols for multi-agents is timely and important.
I appreciate the idea of gaining inspiration from telecommunications and conduct a deep and comprehensive analysis. The proposed principles are important and well-strcutred.
The figures are clear and help understand.

### Weaknesses
1. While it is feasible to draw inspiration from telecommunication, this paper lacks discussions on the unique part of LLM-based agents. The computer networks are much more massive than multi-agents at the current stage. Therefore, there should be some difference between computer networking and LLM-MAS communications, and those should be reflected in the principles. The current principles look like a straightforward inheritage from computer networking.

2. There should be discussions on latency, feasibility of implementations and etc of the proposed protocols. This is because LLM-agents are designed to be fully automatic and powerde by models rather than people. Therefore, the techniques of signatures, flow control and others can be restricted by model capabilities, and require a second thought.

### Questions
Since existing agent systems are much simpler than the computer network, as it involves fewer agents and less diversity (human is much more complicated and diverse), I curious that if a complicated communication protocol is an overkill and what is the trade-off in here?

### Presentation
4
