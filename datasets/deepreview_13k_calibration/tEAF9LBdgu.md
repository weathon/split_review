# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
\libName\  agents are customizable, {\em conversable}, and can operate in various modes that employ combinations of LLMs, human inputs, and tools.
Using \libName, developers can also flexibly define agent interaction behaviors.
Both natural language and computer code can be used to program flexible conversation patterns for different applications. \libName serves as a generic framework for building diverse applications of various complexities and LLM capacities.
Empirical studies demonstrate the effectiveness of the framework in many example applications, with domains ranging from mathematics, coding,  question answering, operations research, online decision-making, entertainment, etc.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present an open-source framework to develop LLM applications using multiple agents that interact with each other to complete tasks. The agents presented are customizable, can converse with each other and can operate in various modes using LLM, human input or tools. Through experiments, they show the effectiveness of this framework for several tasks like  Math Problem Solving, Question-Answering task etc.

### Strengths
-	The approach defines a generic design for agents that can use LLMs, human inputs, certain tools or combination of them. LLM agents can use capabilities such as role playing, progress making from conversation history, proving feedback. Human involvement can be configured at different levels e.g. frequency and conditions for when to request human input. Tools agents can execute code/functions (suggested by LLMs). 
Combining these agents in different configurations can result in powerful agents with very different capabilities.

-	The another useful insight of this paper is to divide the main application workflow into small multi-agent conversations which they call Conversation programming. It consists of two components: computation which is the actions that the agents take to get their response, control-flow which defines the decisions on which agents to send messages to. These two components allow for control over the conversation flow in the application workflow.

### Weaknesses
None

### Questions
-	In Figure 4(c), the performance of ReAct on Best of 3 is better than AutoGen (2 agents). I am curious as to what do you think would the reason for that?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents AutoGen, an open-source framework for building LLM applications via multi-agent conversations. The paper introduces two key concepts: conversable agents and conversation programming. Conversable agents are entities that can communicate with each other and have different capabilities powered by LLMs, humans, or tools. Conversation programming is a paradigm that allows developers to define the interaction behavior between agents using a fusion of natural and programming languages. The paper demonstrates six applications of AutoGen that span various domains and complexities and shows that AutoGen can achieve better performance, reduce development effort, and enable novel LLM usage scenarios.

### Strengths
(1)	The proposed framework simplifies the overall complex LLM workflows and enables automation. By using conversable and customizable agents, it supports conversational modes for complex workflows. It provides a collection of working systems with different complexities. These systems cover a wide range of applications from various domains and complexities. 

(2)	The proposed method allows developers to use a fusion of natural and programming languages to define agent behaviors and conversation patterns.

(3)	The paper demonstrates the effectiveness and generality of the framework in various domains and tasks. It showcases novel and innovative applications that are enabled by the multi-agent conversation framework.

### Weaknesses
(1)	The paper does not address the issue of context length, which may become too long as the number of conversation turns increases. This could affect the performance and efficiency of the LLMs and the agents. Specifically, the framework needs to consider how to manage the growing conversation history, as LLMs have a limited context window. Without a mechanism to truncate or summarize past interactions, the performance of the agents may degrade over extended conversations, leading to less coherent and relevant responses. This is a critical practical consideration for real-world applications.


(2)	It would be better to consider the cost issue, which is important for practical applications. The experiments are conducted on GPT-4 and GPT-3.5, which are expensive and not widely accessible. How would the framework perform on open-source LLMs with lower capacity? The paper should include a discussion on the trade-offs between model capacity, cost, and performance. It is important to understand how the framework can be adapted to resource-constrained environments and whether the benefits of multi-agent conversations can be maintained with less powerful models.


(3)	In my opinion, AutoGen appears to be an extension of CAMEL, both supporting agent role-playing and agent conversations. The authors discuss the related work of CAMEL in the appendix, and highlight two distinct advantages of AutoGen: 1) its capability for tool usage and 2) dynamic conversation. However, it deserves to give an in-depth discussion about CAMEL and AutoGen about their differences in the introduction section. Actually, I do not think the tool-usage is a big challenge if using the GPT4. It is expected to discuss the challenge from static conversation (of CAMEL) to dynamic conversation (of AutoGen). The paper needs to clarify the specific technical challenges in moving from static, role-based conversations to dynamic, multi-agent interactions, and explain how AutoGen addresses these challenges.

### Questions
(1)	Please refer to Weakness (2). How would the framework perform on open-source LLMs with lower capacity?

(2)	Please refer to Weakness (3). What is the technique challenge for introducing dynamic conversation compared with AutoGen? 

(3)	Can this method be applied in other complex tasks, such as automatically using professional tools (Oracle, MATLAB)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an open-source toolkit AutoGen, It introduces a tool to facilitate developing multi-agent LLM backed systems. The tool considers three different backend handlers for requests including LLM agent, human and some tools like code executor. It provides developers an opportunity to use both natural language or code for interaction. It covers 6 different use cases and shows promising results against default GPT benchmarks and some other tools.

### Strengths
+ Open-source multi-agent programming framework is definitely an interesting project.
+ Authors include some empirical results to showcase their performance of the tools.
+ Authors provide extensive documentation to explain different use cases.

### Weaknesses
- Not much takeaway in terms of scientific learning.
I don’t find as a reader what lessons or results we can get from the paper. The main message is that we have a tool that can help developing multi-agent conversation. In my personal opinion, developing it based on a mature LLM agent is neither time-consuming nor scientifically challenging.

- The results are not convincing.
I found the comparison of results is not rigorously evaluated and not convincing. For example, the paper shows that by repeating the question again to LLM may potentially get better results. But the results are not convincing due to few sample they use nor making a lot of sense.

- Too much brag about their system but little evidence is shown to support it.
For example, in the introduction, they aim to design a “capable, reusable, customizable, and effective” system. I didn’t see support towards it.

### Questions
Can you specify why the interactive retrival can lead to better results? I am curious about what the result will look like if I try different variations of questions? As with interactive, I can think of the improvement is due to more trials other than better problem understanding.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces AutoGen to enhance the development of LLM applications through the use of multiple conversational agents. These agents are customizable, capable of various modes of operation, and can interact with each other, human inputs, and tools to accomplish complex tasks. The framework supports programming interaction behaviors using both natural language and code, catering to a wide range of applications across different domains.
Contributions:
- The framework provides a generic and extensible design for agents, enabling them to engage in conversations and multi-turn interactions seamlessly.
- AutoGen introduces a conversation-centric programming paradigm, simplifying the development of complex LLM applications and providing adaptability to a wide range of needs.

### Strengths
- AutoGen’s conversation-centric programming paradigm can simplify and unify the development of complex LLM applications, showcasing originality in application workflow design.
- AutoGen provides robust support for developers, including the ability to program agent interactions using both natural language and code, catering to a diverse set of development preferences and needs.

### Weaknesses
While AutoGen presents a promising framework for multi-agent applications of LLMs, the paper tends to read more like a tech report rather than a traditional research paper, as it lacks a focused exploration of research-oriented problems. The novelty of the work seems constrained by this, as it primarily introduces and elaborates on the framework’s capabilities without diving deep into scientific inquiries or hypotheses testing. Although the practical utility of AutoGen is clear, the analysis provided in the paper regarding its positioning and performance relative to existing solutions is not sufficiently comprehensive, and the discussion on scalability, performance overheads, and real-world applications remains superficial. The agent customization, while a strong feature, could benefit from clearer guidelines, and the human-AI interaction aspect requires more elaboration. These areas of improvement highlight a need for a more detailed, research-focused approach, and suggest that the work may find a more fitting audience at a venue like the System Demonstration track at ACL, where applied tools and frameworks are showcased and appreciated.

### Questions
- Is there any scenarios in which the single agents outperform the multi-agent counterparts? For example, the Alfworld may be as easy as possible for a single agent to solve, maybe the assistant agent and executor agent can be the same one which generates the formatted [think + act] steps at the same time, which makes the multi-agent problem into a prompt template design problem.
- How did the grounding agent in the A3 of Figure 4 know the crucial commonsense knowledge, Did you design the specific prompts/few-shot examples to teach it?
- Why do only two methods have the whole dataset results in A1 of Figure 4?
- In the scenario of the A6 of Figure 3, multi-agent players are playing chess, how to make sure every agent strictly follows the chess rules?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
