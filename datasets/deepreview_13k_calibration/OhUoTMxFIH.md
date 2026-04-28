# Robotouille: An Asynchronous Planning Benchmark for LLM Agents

- Decision: Accept
- Avg Score: 5.67
- Scores: 3, 8, 6

## Abstract
Effective asynchronous planning, or the ability to efficiently reason and plan over states and actions that must happen in parallel or sequentially, is essential for agents that must account for time delays, reason over diverse long-horizon tasks, and collaborate with other agents. While large language model (LLM) agents show promise in high-level task planning, current benchmarks focus primarily on short-horizon tasks and do not evaluate such asynchronous planning capabilities. We introduce Robotouille, a challenging benchmark environment designed to test LLM agents' ability to handle asynchronous, long-horizon, and multi-agent scenarios. These datasets capture increasingly complex planning challenges that go beyond existing benchmarks, particularly in their requirement for agents to manage overlapping tasks, interruptions, and collaboration. Our results show that ReAct (gpt-4o) achieves 47% on synchronous tasks but only 11% on asynchronous tasks, highlighting significant room for improvement. We further analyze failure modes, demonstrating the need for LLM agents to better incorporate long-horizon feedback and self-audit their reasoning during task execution.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a benchmark to evaluate LLMs’ planning ability, focusing in particular on their asynchronous planning capabilities. Here asynchronous means that the optimal solution is not to complete sub-tasks in a sequential manner. Rather, while “waiting for” some subtasks to complete, the agent should directly focus on other tasks. The benchmark contains 30 tasks, where existing LLMs suffer to perform well even with techniques such as chain-of-thought.

### Strengths
- The paper proposes a benchmark for asynchronous planning based on an environment similar to overcooked.
- The paper demonstrates that many existing LLMs fail short at planning problems that requires to consider time delays of sub-tasks.

### Weaknesses
 - While this paper proposes a new benchmark for certain types of LLM reasoning tasks, it does not include sufficient experimental evaluation and analysis to highlight its main challenges. Specifically, while there are many LLMs as well as LLM-based planning algorithms to tackle planning problems, the paper only experimented with one LLM and two planning algorithms (CoT and ReAct). More baselines are needed to better illustrate the challenges posed by the proposed benchmark.

- It is unclear from the paper which components of asynchronous planning make it much harder than synchronous planning. In the failure mode analysis, it is unclear to me what does it mean to attribute failure in terms of uncertainty over the MDP. Additionally, this categorization seems to be irrelevant to the key ingredient of the benchmark: *asynchronous* planning. A detailed analysis of why “asynchronous” planning is harder is needed to understand in what ways do this benchmark challenges the methods.

- While the paper highlights that the benchmark requires long-horizon planning, the horizon counted by the paper is the number of required “atomic steps”, while the agent is performing high-level actions such as move an object to a place. This size of the graphs (e.g., in Figure 11) seems to be a better measure of the “planning depth”. Given this, it seems unclear what are the additionally challenges in this benchmarks compared to for example the AsyncHow dataset mentioned in the paper.

### Questions
Which components of asynchronous planning make it much harder than synchronous planning?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ROBOTOUILLE, a challenging benchmark environment designed to evaluate the capabilities of large language model (LLM) agents in handling asynchronous, long-horizon, and multi-agent scenarios. Specifically, ROBOTOUILLE serves as a simulator for cooking various recipes, aiming to stress-test LLM agents. It utilizes domain and problem JSONs to define the Markov Decision Process (MDP) and the language description of the environment and tasks. By testing models such as gpt-4-o in both synchronous and asynchronous datasets, the authors demonstrate that agents face greater challenges in completing assigned tasks under asynchronous conditions. Additionally, the paper provides a thorough analysis of failure modes towards the end.

### Strengths
1. There is a notable gap in benchmarks for planning and decision-making tasks that involve asynchronous, long-horizon scenarios. The authors effectively compare their work to relevant literature, underscoring the significance of ROBOTOUILLE. Moreover, the cooking aspect of the tasks makes them relatable and easy to understand.

2. By conducting experiments across two different settings, the authors identify key reasons for failure modes in the asynchronous decision-making context, such as the ineffectiveness of failure recovery strategies. This provides valuable directions for future research in asynchronous planning.

3. The models used in the experiments represent the latest advancements in the field, showcasing the highest capabilities of current LLMs. Despite this, the agents still struggle to consistently complete asynchronous tasks, highlighting the relevance of the research direction proposed in the paper.

4. The authors supply essential code and detailed implementation explanations, demonstrating that the experimental results are reproducible and persuasive.

### Weaknesses
1. The paper lacks a discussion on prompt design. The performance differences between the synchronous and asynchronous datasets may stem from variations in prompts, which often determine the practical limits of an agent's capabilities.

2. Additionally, the tasks in the synchronous and asynchronous datasets differ, making it inappropriate to directly compare results from both settings during the analysis. The lack of task parity makes it difficult to isolate the impact of asynchrony on agent performance. It is unclear if the observed performance differences are due to the asynchronous nature of the tasks or simply the inherent difficulty of the tasks themselves.

3. If possible, I suggest including experimental results from some open-source models in the model list. While these results may not surpass those of proprietary models, they could encourage the open-source community to pay more attention to this research area.

### Questions
1. The paper states that ROBOTOUILLE supports multi-agent environments by simply adding more players to the problem JSON. However, I did not see any related attempts or studies mentioned. Is this intended as a future research direction?

2. Some results in the experiments struck me as peculiar. For instance, in Table 2, the Gemini model performs significantly better than ReAct using the I/O CoT method. What accounts for this discrepancy?

3. Furthermore, in Table 3, Task 5 under synchronous conditions is more complex than Task 4, yet ReAct has a higher success rate. A similar situation occurs in the asynchronous setting. The paper does not provide a clear explanation for this phenomenon. What might be the underlying reasons?

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
4

### Summary
This paper introduces Robotouille, a benchmark designed to evaluate the planning capabilities of LLMs in asynchronous, long-horizon, and multi-agent environments. Authors highlight a significant performance gap for SOTA approaches (e.g., GPT-4o+ReAct), showing success rates of 47% in synchronous tasks and only 11% in asynchronous ones. The benchmark includes datasets with varying levels of complexity, along with a thorough failure analysis, offering key insights into where and why current approaches fall short.

### Strengths
+ Well-written with clear illustrations of domain complexities.
+ Rigorous experimental design, featuring carefully curated datasets across multiple complexity levels and a detailed failure analysis.

### Weaknesses
 * The paper can be split into two main sections: 1) introducing and baselining the benchmark and 2) analyzing results. While the first part is strong, insights in the second part are somewhat obscured. For instance, in Q6, the majority of both successful (72.7%) and failed (52.8%) trajectories prioritized subtask completion. Does this indicate that subtask prioritization may not be a critical area for improvement in planning? I encourage authors to capitalize more on their analysis.

* The absence of stochastic elements in the environment and experimentation is notable. One of the significant challenges for LLM architectures lie in adapting to stochastic domains [1].

* Although the paper initially emphasizes the multi-agent aspect of the environment, this is not reflected in the empirical results.

### Questions
* Line 366: Could you clarify why (0.5, 1.0] implies minimal progress? Wouldn’t a score of 0.5 indicate the solution is halfway there?

* Line 520: I was surprised not to see value propagation and temporal difference learning listed under Feedback Incorporation techniques.

### Soundness
3

### Presentation
4

### Contribution
2
