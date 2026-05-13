# Beyond Browsing: API-Based Web Agents

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Web browsers are a portal to the internet, where much of human activity is undertaken. Thus, there has been significant research work in AI agents that interact with the internet through web browsing.
However, there is also another interface designed specifically for machine interaction with online content: application programming interfaces (APIs).
In this paper we ask -- \emph{what if we were to take tasks traditionally tackled by browsing agents, and give AI agents access to APIs}?
To do so, we propose two varieties of agents: (1) an API-calling agent that attempts to perform online tasks through APIs only, similar to traditional coding agents, and (2) a Hybrid Agent that can interact with online data through both web browsing and APIs.
In experiments on WebArena, a widely-used and realistic benchmark for web navigation tasks, we find that API-based agents outperform web browsing agents.
Hybrid Agents out-perform both others nearly uniformly across tasks, resulting in a more than 20.0\% absolute improvement over web browsing alone, achieving a success rate of 35.8\%, achiving the SOTA performance among task-agnostic agents.
These results strongly suggest that when APIs are available, they present an attractive alternative to relying on web browsing alone.io/API-Based-Agent/}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a hybrid approach that involves use of web browsing and API calling in web agents. The rationale for this approach is that APIs are generally better suited for consumption for agents than the often noisy and expansive HTML DOM structure of webpages. 

The result of the experiment on web-arena indicate having good quality API support enables the agent to make use of the APIs to perform the tasks reasonably well by itself or in combination with web browsing.

### Strengths
Overall the notion of API + Web browsing shows lot of promise. The implication of this results also presents interesting questions in terms of development of new websites in the future or existing websites in terms of making themselves more agent friendly in terms of exposing capabilities and APIs for optimal consumption by agents.

### Weaknesses
In the limitations the authors point that "In our paper we only evaluate web agents on WebArena tasks. The number and diversity of tasks
might be limited. However, to the best of our knowledge, no other real-world web task benchmarks are available at the moment. The tasks we used are the only ones we could find a bemchmark with.". This is not true. There are multiple web benchmarks which are more real-world such as webvoyager, GAIA (a subset of it involves web tasks) and to a limited extend webshop. This is not to say that WebArena evaluation is not valid, i think it is a perfectly reasonable evaluation, however the statement "no other real-world web task benchmarks are available at the moment" is factually not true.
Also not the spelling error in "bemchmark"

Missing analysis: I would also like to see an analysis of the error modes for API and API+Browsing. How many of the tasks could be performed exclusively using APIs and what are the minial number of API calls required for each. How many of these could the agent perform, and for those that the agent could not, what were the common error modes. The authors does mention good quality APIs influence performance ,however this is pretty obvious and generic. A detailed analysis of the error modes would present valuable insights.

### Questions
Elaborate on the error modes.

### Soundness
2

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
The paper introduces an enhanced AI web agent that incorporates API interactions as an additional action space alongside traditional GUI-based interactions. Traditional web agents often rely on simulating human-like actions on graphical user interfaces, which can be inefficient due to the complexity of web pages and limitations in accurately understanding UIs. To address these challenges, the authors develop an API-based agent that interacts directly with web services through API calls, bypassing the need for GUI interaction.

Recognizing that API support varies among websites, the authors also propose a hybrid agent capable of seamlessly switching between API calls and web browsing based on the context. This hybrid approach allows the agent to utilize APIs when available and revert to GUI-based interactions when necessary. The agents are evaluated on the WebArena benchmark, leading to three key findings:
1) API-based agents consistently outperform browsing-based agents on web tasks, regardless of the extent of API support.
2) API-based agents achieve higher success rates on websites with comprehensive API support (e.g., GitLab) compared to those with limited support (e.g., Reddit).
3) Hybrid agents outperform both solely API-based and solely browsing-based agents

### Strengths
Originality
The paper introduces a novel approach by incorporating API interactions as an additional action space for AI web agents, which traditionally rely on GUI-based interactions like simulated clicks and typing. By proposing API-based agents and a hybrid model that seamlessly switches between API calls and web browsing, the authors creatively combine existing ideas to address the limitations of current web agents. This innovative problem formulation expands the capabilities of AI agents in interacting with web services and tackles an unstudied area in web task automation.

Quality
The authors provide a robust empirical evaluation of their proposed agents using the WebArena benchmark. The experiments are well-designed to assess the performance across websites with varying levels of API support. The key findings are clearly supported by the data, demonstrating that API-based and hybrid agents consistently outperform traditional GUI-based agents. The paper effectively analyzes the results, highlighting the conditions under which each agent excels, and offers insights into the importance of comprehensive API support.

Clarity
The paper is fairly written. It provides a concise background on the limitations of existing web agents and the motivation for incorporating API interactions. The key contributions are explicitly stated, and the progression from problem statement to conclusion is logical and coherent.

Significance
This work is significant as it addresses a critical gap in the field of AI web agents by leveraging APIs, which are inherently designed for machine interaction. The findings have practical implications for the development of more efficient and accurate web agents capable of handling real-world tasks. By demonstrating that API-based and hybrid agents outperform traditional methods, the paper provides valuable insights that could influence future research and the design of web services. The emphasis on the importance of comprehensive API support underscores a strategic direction for both AI development and web infrastructure enhancement.

### Weaknesses
My main concern is the insufficient details on the hybrid agent decision Mechanism: The paper does not provide a detailed explanation of how the hybrid agent decides when to switch between API calls and GUI-based interactions. Clarifying the criteria or algorithms used for this decision-making process is crucial for understanding the agent's functionality and for others to replicate or build upon the work. I personally did not understand how it works in practice. In addition, the paper provides limited technical details on the implementation of the API-based and hybrid agents. For instance, information about the architecture, error handling, and integration with existing systems is sparse. Including more implementation specifics would improve the clarity and allow for better assessment of the work's feasibility and scalability.

Evaluation Scope and Generalizability: The experiments are conducted solely on the WebArena benchmark, which may not cover a sufficiently diverse set of websites and tasks to demonstrate the agent's general applicability. Expanding the evaluation to include a wider variety of websites with different levels of API support and varying complexities would provide stronger evidence of the agent's effectiveness and robustness (See WorkArena, WorkArena++, ST-WebAgentBench, WebCanvas).

Dependence on API Availability and Quality: The proposed approach relies heavily on the availability and comprehensiveness of APIs, which can vary widely across websites. The paper does not address how the agent handles incomplete, undocumented, or changing APIs. Discussing strategies to mitigate these issues, such as API discovery or adaptation mechanisms, would enhance the practicality of the approach.

Security and Ethical Considerations: Direct interaction with web service APIs raises potential security and privacy concerns, such as authentication management, rate limiting, and compliance with terms of service. The paper lacks a discussion of these challenges and does not propose solutions to ensure that the agent operates securely and ethically. Addressing these concerns is important for real-world deployment.

Performance Metrics and Statistical Analysis: The evaluation primarily reports success rates without sufficient analysis of other important performance metrics such as execution time, resource utilization, or learning efficiency. Additionally, the paper does not mention whether the results are statistically significant.

Adaptability to Web Changes: Websites frequently update their interfaces and APIs, which can break automation scripts. The paper does not discuss how the agent adapts to such changes over time. Exploring methods for the agent to detect and adjust to updates would improve its long-term usefulness.

### Questions
1. How does the hybrid agent decide when to switch between API calls and GUI-based interactions? 

2. How does your agent manage situations with incomplete, undocumented, or frequently changing APIs? Discussing strategies for API discovery, error handling, or adaptation would improve the practicality of your approach.

3. What measures are in place to address security and privacy concerns, such as authentication, rate limiting, and compliance with websites' terms of service? 

Can you share detailed information about the technical implementation of your agents, including architecture specifics, error-handling mechanisms, and integration with existing systems?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to use API-based agents to complement web-only browser based agents for completing web tasks. Using web-arena benchmark which is a simulated web environment, they evaluate how an API-calling agent would perform with focus on highlighting how it has complementary strengths and can outperform a baseline web browsing agent. Finally a hybrid agent is proposed that combines the two agents together to hopefully have the best performance of both the agents.

### Strengths
The biggest and (unfortunately) only strength of this paper is the novelty in proposing to use web and API-based agents to highlight the need to use API-based alternative when available and not ONLY rely on web browsing agents alone. This is great idea in practice since it allows for realistic use of the new wave of web agents.

### Weaknesses
There are three major weaknesses of the paper as mentioned below along with evidence.
1. Incomprehensive literature survey
- API Agents are not new as mentioned in line 51 on page 1; there has been a lot of work on it such as the ToolBench's ToolLlama, AnyTool's hierarchical agent, etc.
- Sec 9 in page 10 claims that there are no other real-world web task benchmarks available but there are several of them: WebVoyager, WebShop, WorkBench, to name a few.


2. Poorly written and shows that it was not proof-read and submitted in haste.
- Line 047, page 1: "Nonetheless, However, ..."
- Line 083, page 2: "that combining" -> "that combines"
- Line 134, page 3: "withe"?
- Line 157, page 3: "Fig 2" -> "Fig 1"
- Line 189, page 4: "see section ??"
- Table 2 caption, page 8: "Each row columns sums up to 1."-> "Each column sums up to 100"

3. The most important one: imperfect representation/description of the results, which doesn't allow us to be confident of the findings.
- Table 1 description in Sec 6.1 line 375 mentions that the API-based Agent achieves higher scores in all websites compared to the Browsing agent, which is NOT true as can be seen in the results of Shop-Admin and Multi Sites. 
- Lines 401-4-3, page 8 say that the browsing agent achieved its best scores on Gitlab and Map, which is not true again. While the sentiment is agreed that it performs poor, it is not represented correctly.
- Line 404, page 8: Hybrid agent did NOT outperform other agents in all categories. In fact, the SteP agent outperforms the hybrid agent in Shopping, Reddit and also on the average!
- Line 423, page 8, "Steps" results description of Table 4 states that "browsing agent consistently takes more steps to complete tasks compared to boath the API-based and hybrid agents". This is false as the table shows that Browsing agent takes least steps than the other two agents for Shopping, Shop-Admin and Multi-Sites.
- Lines 478-479, page 8: This is some leakage that needs to be addressed as adding new APIs are going to obviously help the API-based agents. Also, the numbers are claimed to improved from 9.43% to 14.15% for reddit, but none of the tables show a 9.43% for reddit for any agent.
- WebArena is arguable to be a "realistic" benchmark as WebVoyager is a more realistic one where it is not simulated.

### Questions
- A baseline web browsing agent is described in Sec 2.2. This is very little information. There is great amount of work on developing SOTA web browsing agent and full technical reports on that. One of those should be baseline or a description of such a baseline agent shouldn't be possible in 2 paragraphs. Can you please provide more information on the baseline agent OR why one of the SOTA ones is NOT used for the baseline results? Some known agents are WebArena agent, STeP agent, Agent-E, AgentOccam, to name a few.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a study on leveraging web APIs to improve the performance of web browsing agents. It compares the performance of three settings, web-browsing only, API only, and hybrid ones on WebArena, a recent benchmark for web-based tasks.

### Strengths
This paper explores the use of web APIs for web-browsing tasks and studies the performance and cost of different settings. 
This paper utilizes the current LLM tools such as ChatGPT, CodeAct, to minimize human interference.

### Weaknesses
The major issue of this paper is that it lacks research depth and novelty. Web APIs have been widely used to facilitate the access to online resources, especially data related resources. This paper follows the idea and makes a simple, straightforward attempt of using web APIs if they are available to collect information from websites. No research challenges are identified and the methods are not optimized.

The approach may work in a small-scoped and closed system with the assumption of prior knowledge of the API endpoints and their documentation formats. It is work-in-progress and yet to explore and address many practical problems of leveraging web APIs in an open-end environment. Those problems could be caused due to the lack of systematic supports on locating API endpoints, understanding the semantics of API description, decomposing a task into the invocations of multiple APIs, fixing potential quality issues of codes generated by CodeActAgent, fusing results from multiple APIs, etc.

### Questions
1. Invoking web APIs to collect data is a standard use of web APIs. Given this, what is the novelty of the paper? What are the research challenges of including the use of web APIs in a web browsing agent. 
2. The proposed two phase documentation retrieval seems to be straightforward and lacks intelligence on interacting with API endpoints. It is unclear how to provide the list of available API endpoints given the prompt of a task? What if there is no readme document or the document is not complete or accurate? Is the agent only designed for RESTful APIs? How about SOAP-based and GraphQL APIs?
3. How to deal with practical issues of using web APIs listed in the weaknesses section?
4. The paper deals with brief and incomplete API documentation by using GPT-4 to generate it. But how reliable the GPT-4  generation would be and what the benefits of using them are unclear. 
5. The paper should discuss more about the limitations of the work, in which scenarios human interference is unavoidable, and how to minimize it. 
6. The paper compares the proposed approach with StepP, AutoEval, AWM. The paper should describe each work a bit in terms of the methods they propose and why they are selected. The reference items of AutoEval and AWM do not have the journal/conference information so it is unclear whether/where they are published. The paper should also explain why the browsing agent works much less effectively than these three baselines.

### Soundness
2

### Presentation
2

### Contribution
2
