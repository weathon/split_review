# Improving Planning with Large Language Models: A Modular Agentic Architecture

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Large language models (LLMs) demonstrate impressive performance on a wide variety of tasks, but they often struggle with tasks that require multi-step reasoning or goal-directed planning. Both cognitive neuroscience and reinforcement learning (RL) have proposed a number of interacting functional components that together implement search and evaluation in multi-step decision making. These components include conflict monitoring, state prediction, state evaluation, task decomposition, and orchestration. To improve planning with LLMs, we propose an agentic architecture, the Modular Agentic Planner (MAP), in which planning is accomplished via the recurrent interaction of the specialized modules mentioned above, each implemented using an LLM. MAP improves planning through the interaction of specialized modules that break down a larger problem into multiple brief automated calls to the LLM. We evaluate MAP on three challenging planning tasks -- graph traversal, Tower of Hanoi, and the PlanBench benchmark -- as well as an NLP task requiring multi-step reasoning (strategyQA). We find that MAP yields significant improvements over both standard LLM methods (zero-shot prompting, in-context learning) and competitive baselines (chain-of-thought, multi-agent debate, and tree-of-thought), can be effectively combined with smaller and more cost-efficient LLMs (Llama3-70B), and displays superior transfer across tasks. These results suggest the benefit of a modular and multi-agent approach to planning with LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Modular Agentic Planner (MAP), a modular architecture designed to improve the planning capabilities of large language models (LLMs). MAP integrates several specialized modules—such as action proposal, state evaluation, task decomposition, and error monitoring—each fulfilled by an LLM instance to enhance multi-step reasoning and decision-making. These modules work interactively, decomposing complex tasks into subgoals, validating actions, predicting outcomes, and assessing states, which allows the system to adapt and refine its plans dynamically.

### Strengths
1. Reasonable Modular Design: The proposed MAP employs a modular architecture that enhances the planning capabilities of large language models through the coordination of dedicated modules for task decomposition, state evaluation, and error monitoring. The design approach is reasonable and systematically structured.
2. Validation Across Multiple Tasks: The authors evaluated MAP on several representative tasks, including graph traversal, Tower of Hanoi, PlanBench, and the multi-step reasoning NLP task StrategyQA, providing a relatively comprehensive demonstration of the method’s applicability.
3. Demonstrated Transfer Performance: MAP shows a certain level of task transferability, suggesting that the approach can adapt to task variations in some cases, offering a reference for applying modular methods to complex tasks.

### Weaknesses
1. Lack of Novelty in Agent Design: Numerous studies have already explored agent system design using role-playing, multi-module coordination, or multi-agent frameworks, such as DEPS, JARVIS-1, Voyager, and CAMEL. These approaches have been validated on more complex, open-world benchmarks. For instance, DEPS includes Descriptor, Explainer, Planner, and Selector modules. Compared to these works, what are the specific advantages and unique contributions of this paper? The modular design, while reasonable, appears to be an incremental step rather than a significant leap, especially considering the existing body of work in modular agent architectures.

2. Predictor Module Challenges: The paper introduces a Predictor module, aiming to forecast the next state, which is inherently challenging, particularly in complex and stochastic real-world environments. This essentially functions as a world model, a field still underdeveloped in research. The paper does not adequately address the limitations of this module, especially in scenarios where the environment is not fully observable or deterministic. The reliance on a predictor without a robust mechanism for handling uncertainty raises concerns about the generalizability of the approach.

3. Evaluation on Standardized but Limited Tasks: The paper’s evaluation is primarily on two tasks—Graph Traversal and Tower of Hanoi—both of which are well-established problems in graph theory and search, with mature solutions already available. These tasks are not widely recognized as agent benchmarks, and the community may not find the experiments on these tasks compelling. The lack of evaluation on more complex, open-ended tasks limits the assessment of the proposed method's real-world applicability. While PlanBench and StrategyQA are mentioned, the core evaluation still relies heavily on these simpler tasks.

4. Lack of Comparison with Other Role-Playing Methods: The paper lacks comparisons with other role-playing-based approaches, limiting insight into its relative effectiveness. The absence of a direct comparison with methods that use similar role-playing or multi-agent interaction paradigms makes it difficult to assess the specific advantages of the proposed approach. This omission makes it hard to determine if the gains are due to the specific modular design or simply the use of multiple LLM agents.

### Questions
Refer to the weakness, please.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes MAP, a modular, agentic LLM program that uses specialized modules: task decomposer, actor, monitor, predictor, evaluator, and orchestrator, by prompting GPT-4 with in-context learning to perform complex planning tasks. Empirically, the paper shows strong results improving over baselines such as few-shot prompting, multi-agent debate, and tree-of-thought and also shows analysis supporting the need for each component in their pipeline.

### Strengths
* The paper is well-written and easy to follow
* The empirical results of the method are compelling, with good performance gains across several planning tasks, and is easy enough to implement from the description in the paper, so it should be readily reproducible and easy to implement

### Weaknesses
 * Background on planning tasks and assumptions: The authors seem to operate under a fully observable setting that governs how the monitor, predictor, and orchestrator modules are set up. This assumption should be explicitly stated in Section 2, and how it would change when planning in a partially observable setting should be discussed, as well as whether it is in the scope of this work.
* Missing related work: The paper is missing a few relevant works in partially observable settings:
     * [Adapt](https://arxiv.org/abs/2311.05772): This paper also has recursive task decomposition using three modules (which is similar to some of the modules in MAP) for text games that can be argued have planning components in partially observable settings. 
     * [LATS](https://arxiv.org/abs/2310.04406): Similarly, this paper also uses several LLM components or modules and fuses them with tree search (MCTS) which is relevant to MAPS. A discussion of the similarities and distinctions between these works would place the work better in the broader context of the existing work.
* Lack of acknowledgment of and addressing computational overhead and cost tradeoff with performance: As noted in Appendix A.8, it can be argued that MAP uses a significantly higher token budget (which also translates into monetary cost) as compared to the baselines to get the performance gains it achieves. A fairer comparison would be to increase the computation budget of baselines such as depth and breadth of tree search and verify that the performance gains persist. Similar to the Adapt paper, the authors can increase the number of tokens generated or report the best of n trials to enable such a comparison.

### Questions
* The metrics for evaluating the planning tasks should be discussed explicitly in Sec 3.1
* The presentation of tables 1-3 can be improved by adding the column lines to clearly see the content boundaries and summarize the key takeaways and why you report different baselines for these tasks.
* In Sec 4, it will be helpful to state the numerical margins of improvements in the text for all the plots, since it is not discussed in the paper and is a bit hard to read from the plots.

### Soundness
3

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
This paper proposes the Modular Agentic Planner (MAP), a modular agentic architecture that improves the planning capabilities of LLMs. The architecture includes components for conflict monitoring, state prediction, state evaluation, task decomposition, and orchestration. Each module is implemented using an LLM and performs a specific function in the planning process. The authors evaluate MAP on four tasks: graph traversal, Tower of Hanoi, PlanBench, and StrategyQA, and showed improvement over baselines like CoT, ToT, ICL and Zero-shot. An ablation study is performed to highlight TreeSearch and TaskDecomposer's contribution to the MAP's performance.

### Strengths
1. The experiments and ablation analysis are thoroughly conducted with statistical significance.
2. Inspirations from cognitive neuroscience are interesting.
3. Writing is clear and easy to follow, and the method section is clear. 
4. Thorough ablation analysis on method's failure method
5. Solid results compared to the baselines provided (especially on challenging tasks like PlanBench).

### Weaknesses
1. Novelty and relation to prior work -- MAP seems to be a modular agentic framework with search, which is not the first time this high-level structure is introduced, and works with similar framework were not explicit discusses. See references below.
2. In relation to point 1, I find the baselines in the experiments all too weak. There are plenty of work on LLM agents that use explicit planning modules and/or MCTS. It would be more convincing if the MAP can still outperform those. If that's the case, an analysis on why MAP outperforms planning-based methods would be great to have as well. 
**Minor stuff**: tables contains odd spacing, and a lot of white spaces.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes MAP, a modular planning architecture designed to address the limitations of LLM-based planning methods. Each module has a specific role and operates collectively within the system. Each module is inspired by concepts from cognitive neuroscience and reinforcement learning (RL). The authors demonstrate performance improvements over baselines (GPT-4 Zero-shot, GPT-4 ICL, GPT-4 CoT, ToT, MAD) in tasks such as graph traversal, Tower of Hanoi, PlanBench, and StrategyQA.

### Strengths
- The concept of using multiple LLM-based modules, each with a specific role in planning, is well-conceived. Additionally, grounding each module in neuroscience and RL theories strengthens the approach.
- The tasks used in the experiments, such as graph traversal and PlanBench, effectively isolate and test the planning capabilities of LLMs, demonstrating the system’s potential to address planning challenges.

### Weaknesses
 - The primary limitation of MAP is its high computational cost, which does not seem fully justified by the observed performance gains. According to Section A.8, the number of input tokens used in MAP is 83 times higher than GPT-4 CoT. Even the efficient version of MAP is 36 times more costly.
- The explanation of MAP in the main text is insufficient, requiring reference to multiple sections in the appendix to fully understand certain modules. For example, understanding the Actor and Monitor modules requires consulting not only the main text but also Algorithm 2, Algorithm 3, and Sections A.7.2 and A.7.3 in the appendix. Additionally, inconsistencies remain in the descriptions. For instance, Algorithm 2 shows the Actor outputting an action sequence $A$, but in Section A.7.2, both action sequences and state information are included. It is unclear whether the Actor outputs only action sequences, both action and state, or relies on other modules for state information. Similarly, in Algorithm 2, the Monitor is described as taking the action sequence $A$ from the Actor and producing validity and feedback for the sequence. However, the in-context examples in Section A.7.3 show feedback and validity generated for each individual action, creating ambiguity about how the Monitor processes an entire action sequence to produce validity and feedback.
- Like many LLM-based planners, MAP relies heavily on selecting in-context examples. However, there is no detailed explanation for how these examples are chosen. The authors should clarify whether in-context examples are fixed or dynamically selected. If fixed, identifying effective examples for each module could be costly. If dynamically selected, an explanation is needed on how examples are constructed and selected.
- The Task Decomposer appears to lack a mechanism for recovering from errors in subgoal generation, meaning that an initial mistake in generating a subgoal could lead to failure regardless of subsequent steps. Additionally, MAP currently only generates single subgoals in experiments. Verification is needed to assess its effectiveness when multiple subgoals are required.
- The Predictor module seems likely to perform well only in deterministic environments. In complex or non-deterministic environments (e.g., Minecraft [1], ALFWorld [2], WebShop [3]), accurate prediction may become challenging, risking performance degradation.

### Questions
- Each module is inspired by neuroscience and RL. Is there a theoretical background that also covers interactions between these modules?
- How are in-context examples selected and constructed for each module? Are they fixed or dynamically selected according to task requirements?
- Is prompt design automated, or does it require manual configuration? Given MAP’s architecture, prompt design for all modules could be costly and time-consuming. The automatic insights collection approach used by ExpeL [4] could also serve as a useful reference.
- Why does the Task Decomposer currently generate only a single subgoal?
- The Actor’s in-context examples (A.7.2) lack feedback examples. Can the Actor effectively process feedback when it is provided by the Monitor?
- Is there a plan to test in more complex environments (e.g., Minecraft [1], ALFWorld [2], WebShop [3]), where prediction errors may occur more frequently?
- Even efficient version of MAP incurs significant computational costs. How do the authors plan to address this issue?

[4] Zhao, Andrew, et al. "Expel: Llm agents are experiential learners." *Proceedings of the AAAI Conference on Artificial Intelligence*. Vol. 38. No. 17. 2024.

### Soundness
2

### Presentation
2

### Contribution
3
