# Agent-Oriented Planning in Multi-Agent Systems

- Decision: Accept
- Scores: 6, 3, 5, 6, 8

## Abstract
Through the collaboration of multiple agents possessing diverse expertise and tools, multi-agent systems achieve impressive progress in solving real-world problems. Given the user queries, the meta-agents, serving as the brain within these systems, are required to decompose the queries into multiple sub-tasks that can be allocated to suitable agents capable of solving them, so-called agent-oriented planning. In this study, we identify three critical design principles of agent-oriented planning, including solvability, completeness, and non-redundancy, to ensure that each sub-task is effectively resolved, leading to satisfactory responses to the original queries. These principles further inspire us to propose a novel framework for agent-oriented planning in multi-agent systems, leveraging a fast task decomposition and allocation process followed by an effective and efficient evaluation via a reward model. During the planning process, the meta-agent is also responsible for evaluating the performance of the expert agents, making timely adjustments to the sub-tasks and scheduling as necessary. Besides, we integrate a feedback loop into the proposed framework to further enhance the effectiveness and robustness of such a problem-solving process. Extensive experiments demonstrate the advancement of the proposed framework in solving real-world problems compared to both single-agent systems and existing planning strategies for multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper describes a method for solving queries using a multi-agent system, with multiple agents which are experts in at different sub-tasks. A meta-agent is then required to decompose the queries into multiple sub-tasks that are then allocated to suitable agents for solving them. The authors identified three critical principles for task completion:

That is Solvability - Each sub-task should be solvable by at least one of the available agents. 

Completeness - The set of sub-tasks should include all necessary information from the original query. That is the aggregation of the sub-tasks should have a comprehensive answer to the original query.

Non-redundancy – The set of sub-tasks should not include duplicate or unnecessary elements.

For each of these requirements, should it fail any, the meta-agent is required to revisit the task decomposition and/or task allocation.

To determine if a sub-task is completely resolved you would need to check if any of the agents can solve a sub-task, but due to the overhead required, they create a training dataset for a reward model using the fast decomposition process and a scorer, which evaluates agent response. This reward model is used to reduce the overhead of agent calls. It is used to approximate whether a sub-task is resolved by an agent by check if its score is sufficiently high (above a certain threshold). In cases where this score is not high enough for any agent, the sub-task is deemed to not fit the solvability criteria and the meta-agent replans.

They then explore when sub-tasks are lacking information/ambiguous or are too complex, and use a similarity calculation over the embeddings of the subtasks. If it is too high, there are tasks similar to it and it should be re-described according to the similar representative  sub-task. If it does not meet a threshold then the sub-task is considered too complex and is modified.
A detector is added to check that all key elements of the original query exist in all the sub-tasks, and that no two sub-tasks resolve the same key elements. If either is failed a recommendation based on that key element is made to help remove overlapping subtasks or supplement missing details.
This is evaluated vs a number of baselines and experiments are done based on a numerical reasoning dataset. It is shown to outperform the baselines.

Ablations are done to show that each component adds meaningfully to the model.

The related work is only listed after all the results.

### Strengths
The work shows three components which improve the ability of multi-agent LLM systems to improve the results of general LLM queries as compared to current methods.

All three components are shown to meaningfully add to the overall model, and directly tackle the presented critical principles for design.

### Weaknesses
The work is difficult to follow at times, I believe it can be made much clearer, especially with regards to Figure 2. It is difficult to understand this diagram without enough direct context. There is no clear direction that it takes. The detector does not seem to lead to a replan as described.

The ordering of the sections, particularly the related work, and how it reads in context at the end, does not make sense, was this just compiled in the wrong place accidentally?

The results only have one dataset to my understanding. Can this be extended to more datasets?

I have concerns that the rewards model does not generalize outside of this dataset? Or would that simply require more training on bigger datasets?

I believe this work is good and novel, however it could be improved upon with clearer writing.

### Questions
The results only have one dataset to my understanding. Can this be extended to more datasets?

I have concerns that the rewards model does not generalize outside of this dataset? Or would that simply require more training on bigger datasets?

The ordering of the sections, particularly the related work, and how it reads in context at the end, does not make sense, was this just compiled in the wrong place accidentally?

Are there cases where the scorers are human experts? It was a bit ambiguous as to whether this was in fact the case.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The proposed system uses a LLM to generate a decomposition of a problem into an array of sub tasks that are then allocated to different agents. Then a reward model is used to improve the plan as it is being executed.

### Strengths
* The problem of multi-agent planning is highly important with high potential impact.
* How to decompose problems into sub-tasks based on the capabilities of the individual agents is often the key problem.
* Learning the capabilities of other agents is a hard and important challenge.
* The paper is easy to follow.

### Weaknesses
 * The paper does not relate to the rich and long history of multi-agent planning. A starting point could be [1].
* The design principles seem a bit backwards. Normally, the set of problems that can be solved by a set of agents is defined as the union of the problems that each agent can solve, then you have to check whether the particular problem is within that set. Normally, it is a hard computational problem to determine what problems an agent can solve. If the set of sub-tasks contain redundancy it is either a problem with the planner or there is reason, such as a need to deal with non-deterministic outcomes of actions. To have it as a design principle seems strange.
* In the completeness principle it is mentioned "The array of sub-tasks [...] should include all necessary information" what does this mean? The first principled is defined in terms "resolvable" tasks. The second principle is defined in terms of "necessary information". What is the relation between "necessary information" and "resolvable"?
* It is well known that LLMs cannot generate plans in the sense used in the planning community as there are no guarantees that the plan is correct nor that it actually solves the problem. My impression is thus that the proposed solution is more about learning a model of different agents capabilities than on planning.

### Questions
* Why is it beneficial to use natural language over PDDL and other languages specifically designed for planning? There are papers on this already [2] so it would make sense to compare to such an approach.
* Similarly, why not represent the agent capabilities in terms of planning operators or some other well-defined formalism rather than (what I presume) is natural language descriptions?
* How do you formally verify that the generated plans are correct and solve the problem?

[2] Translating Natural Language to Planning Goals with Large-Language Models by Yaqi Xie et al.

### Soundness
2

### Presentation
3

### Contribution
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
The paper presents a multi-agent framework for problem-solving. In particular, the framework uses a meta-agent to decompose a task into subtasks and assign each subtask to downstream expert agents based on their expertise. Then, it uses a reward model to evaluate the performance of the expert agents and use the rewards as signals for re-planning. Additionally, the framework incorporates a feedback system to further improve the robustness and accuracy of problem-solving. Empirical analysis over a numerical reasoning dataset indicates how the proposed framework outperforms the benchmarks, such as direct query to GPT-4o and chain-of-thought. Additionally, a set of ablation studies necessitates each component, such as the plan detector and the reward model, within the framework.

### Strengths
The paper is well-organized, presenting a detailed and thorough explanation of the proposed framework. A particularly compelling aspect is the approach of breaking down tasks into smaller components and assigning them to specialized agents according to their areas of expertise. This decomposition allows each agent to handle tasks within its domain, enhancing overall efficiency and precision. Additionally, the integration of a feedback system significantly boosts the framework’s performance by refining the agents’ actions and ensuring adaptive learning.

### Weaknesses
There are several limitations of the work that the authors may consider to address:

1. Expert agents: the difference between each expert agent is their input prompts, but they are using the same underlying model (GPT-4o). It could be more interesting to replace each expert agent with the current state-of-the-art model in their domain. I believe there are plenty of works to fine-tune the language models for code generation, solving math problems, etc.

2. I don't see the significance of the commonsense agent. Feels like the meta agent is also doing some common sense reasoning (e.g., understanding and decomposing tasks). If possible, please provide some use cases where the commonsense agent is necessary.

3. The cost (time and number of tokens) is high compared to direct querying GPT-4o, given that over 5x cost for only a 10 percent improvement. This probably can be solved by optimizing the expert agents (see point 1).

### Questions
1. In Table 1, in my understanding, the prompt tokens and completion tokens refer to the AVERAGE NUMBER of tokens for EACH task, is it correct? Probably it's better to clarify this in the paper.

2. Is this framework capable of collaborating with multiple agents with the same expertise and improving efficiency? For example, using multiple math agents to solve a complex math problem, while these agents run in parallel.

3. In my understanding, the four agents in the experiment are GPT-4o with different input prompts, are there any additional fine-tuning to improve the expertise of each agent?

4. The paper talks about solvability, completeness, and non-redundancy at the beginning of the paper. Are there any quantitative results showing that the proposed framework addressed these challenges?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework for agent-oriented planning in multi-agent systems, where a central "meta-agent" decomposes complex user queries into sub-tasks, assigns these sub-tasks to specific agents, and evaluates their performance. The authors focus on three key principles, namely, solvability, completeness, and non-redundancy, to guide efficient task decomposition and assignment. The framework also includes a feedback loop, enabling the meta-agent to refine its planning over time.

The framework’s emphasis on structured decomposition and task dependencies is well-suited for complex queries that involve multiple agents with diverse capabilities. By ensuring each sub-task aligns with an agent’s expertise, the system promotes both efficiency and reliability.

I have a few questions:
- Task dependencies are identified during decomposition, but dependencies may also emerge during execution. How does the framework adapt when unforeseen dependencies between sub-tasks arise? Could this affect the overall solvability or efficiency of the task set?

- The framework depends on structured task decomposition, yet real-world environments are often unpredictable and dynamic. How does this approach handle unexpected changes in agent availability or evolving task requirements without needing a complete re-plan?

- Non-redundancy is a key focus, yet redundancy can be valuable for fault tolerance. How does the framework balance efficiency with the potential need for redundancy, particularly in scenarios where backup solutions could be essential?

- The scalability of the approach isn’t clear to me. As the number of agents and interdependent tasks increase, how does the meta-agent manage complexity? Are there limitations on the scale or number of agents?

- The meta-agent requires detailed knowledge of each agent's abilities for effective task allocation. But it isn’t immediately clear to me, how are these capabilities/descriptions in D represented? Can you provide more details?

- Related to the comment above, can you discuss what representation is best suited for agent descriptions? Are these representations task dependent?

- Another follow-up on the above comment, can you discuss about the process/requirements if these representations need to be verified or even updated through the process? How can the approach be adapted to handle such cases?

- While the feedback loop allows for ongoing improvements, how does it prevent instability or oscillations in planning strategies? How would you introduce safeguards into the system or meta-agent to avoid fluctuating between different planning approaches?

Overall, I'm happy with the contributions made in this paper and vote for a weak accept. I'd be happy to raise my score given mine and my fellow reviewers' comments are adequately addressed. Thanks!

### Strengths
-- See above

### Weaknesses
Task dependencies are identified during decomposition, but dependencies may also emerge during execution. How does the framework adapt when unforeseen dependencies between sub-tasks arise? Could this affect the overall solvability or efficiency of the task set?

The framework depends on structured task decomposition, yet real-world environments are often unpredictable and dynamic. How does this approach handle unexpected changes in agent availability or evolving task requirements without needing a complete re-plan?

Non-redundancy is a key focus, yet redundancy can be valuable for fault tolerance. How does the framework balance efficiency with the potential need for redundancy, particularly in scenarios where backup solutions could be essential?

The scalability of the approach isn’t clear to me. As the number of agents and interdependent tasks increase, how does the meta-agent manage complexity? Are there limitations on the scale or number of agents?

The meta-agent requires detailed knowledge of each agent's abilities for effective task allocation. But it isn’t immediately clear to me, how are these capabilities/descriptions in D represented? Can you provide more details?

Related to the comment above, can you discuss what representation is best suited for agent descriptions? Are these representations task dependent?

Another follow-up on the above comment, can you discuss about the process/requirements if these representations need to be verified or even updated through the process? How can the approach be adapted to handle such cases?

While the feedback loop allows for ongoing improvements, how does it prevent instability or oscillations in planning strategies? How would you introduce safeguards into the system or meta-agent to avoid fluctuating between different planning approaches?

### Questions
-- See above

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a new framework for multi-agent systems where meta-agents decompose user queries into sub-tasks, allocate these tasks to appropriate agents, and evaluate the results based on three key design principles: solvability, completeness, and non-redundancy. The meta-agent also uses a reward model to assess agent performance and includes a feedback loop for continuous improvement. The proposed framework demonstrates noticeable advancements in solving complex real-world problems by efficiently coordinating agents compared to existing methods.

### Strengths
This paper proposes an interesting framework for agent-oriented planning in multi-agent systems, including an integrated feedback loop and reward model, which appear to be novel.

This paper is well-structured, with a clear methodology and comprehensive experimental analysis.

This paper is clearly written and well-organized, making the complex concepts of agent-oriented planning accessible.

This paper addresses a crucial challenge in multi-agent systems—optimizing task decomposition and agent coordination, which has substantial implications for practical applications in artificial intelligence.

### Weaknesses
While this paper explored a very important problem of agent-oriented planning, I do have a few questions/concerns regarding the reported research work:

1. The principles of solvability, completeness and non-redundancy appear to be very general in nature. They may not be entirely new to the field of multi-agent systems or task planning. The novelty may not lie in the principles themselves but in how they are implemented within the specific context of large language models (LLMs) and agent-oriented systems. While the paper integrates these principles into the implementation of a meta-agent, the principles alone may not represent a breakthrough. This paper could benefit from a more detailed discussion of how these principles are uniquely applied in the context of LLM based multi-agent systems.

2. There seems to be a clear lack of technical details regarding how each agent is constructed, operates, and integrates with the meta-agent. While the paper describes agents such as the “search agent,” “math agent,” and “commonsense agent,” I don't quite understand their underlying architectures and decision-making processes (e.g., the underlying models used for each agent and their training processes). Additionally, the descriptions of agent capabilities seem to be vague. This lack of technical depth makes it difficult to assess the robustness, scalability, and adaptability of the agents, as well as their performance in diverse real-world applications. Without these technical details, the framework’s effectiveness remains partially speculative, relying more on theoretical design principles than on concrete, replicable methods.

3. The reward model developed in this paper operates like a surrogate to predict the performance of using any specific task agent to tackle any given sub-task. The general idea of predicting agents' performance is not new. The concrete design of the network architecture and the training algorithm for the reward model may be new. However, the corresponding technical contribution was not clearly highlighted and justified. The same concern also applies to the feedback loop, which is commonly used to update the surrogate models in the literature. Its novelty under the newly proposed framework may need to be better elucidated. Potentially, this paper may benefit by providing a more detailed comparison with existing surrogate models or a clearer explanation of how their approach differs from standard feedback loops in the literature.

4. This paper introduces multiple algorithm/system parameters, such as reward model thresholds, agent selection criteria, and similarity measures, which may be challenging to fine-tune. This complexity makes it potentially difficult to adapt the proposed multi-agent system to new datasets or applications, as optimal tuning may require deep domain-specific knowledge and extensive experimentation, further affecting the system’s usability. In line with this concern, it might be helpful for the authors to provide some concrete guidelines or heuristics for parameter tuning, or to discuss potential strategies for automating or simplifying this process for new datasets or applications.

5. The experimental evaluation in the paper appears to be limited in scope, as it primarily focuses on a single numerical reasoning dataset. It remains questionable whether the newly developed multi-agent system can generalize well across diverse real-world tasks or more complex, domain-specific applications. Hence, the authors may need to discuss potential challenges in applying their system to more diverse or complex tasks.

### Questions
Could you elaborate on how the principles of solvability, completeness, and non-redundancy are uniquely adapted for LLM-based multi-agent systems in this framework?

Could you clarify the unique aspects of your reward model and feedback loop in this framework? How do they differ from traditional surrogate models, and what specific contributions do they offer to agent-oriented planning in LLM-based systems?

What strategies or guidelines do you suggest for fine-tuning the system’s parameters for new datasets or applications? Are there ways to simplify or automate this tuning process to improve usability?

### Soundness
3

### Presentation
3

### Contribution
2
