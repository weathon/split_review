# Sparse Rewards Can Self-Train Dialogue Agents

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Recent advancements in state-of-the-art (SOTA) Large Language Model (LLM) agents, especially in multi-turn dialogue tasks, have been primarily driven by supervised fine-tuning and high-quality human feedback. However, as base LLM models continue to improve, acquiring meaningful human feedback has become increasingly challenging and costly. In certain domains, base LLM agents may eventually exceed human capabilities, making traditional feedback-driven methods impractical. In this paper, we introduce a novel self-improvement paradigm that empowers LLM agents to autonomously enhance their performance without external human feedback. Our method, Juxtaposed Outcomes for Simulation Harvesting (JOSH), is a self-alignment algorithm that leverages a sparse reward simulation environment to extract ideal behaviors and further train the LLM on its own outputs. We present ToolWOZ, a sparse reward tool-calling simulation environment derived from MultiWOZ. We demonstrate that models trained with JOSH, both small and frontier, significantly improve tool-based interactions while preserving general model capabilities across diverse benchmarks

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces JOSH (Juxtaposed Outcomes for Simulation Harvesting), a self-alignment framework for large language model (LLM) agents to enhance multi-turn dialogue capabilities without human feedback, addressing the impracticality of traditional feedback-driven methods. JOSH leverages sparse reward signals within simulated dialogues to allow the model to self-improve, specifically targeting multi-turn tool-calling skills in task-oriented dialogues. The authors also introduce ToolWOZ, a dataset and benchmark based on MultiWOZ 2.0, designed to evaluate tool-usage in dialogue settings. Experimental results demonstrate that a fine-tuned LLaMA-3B model exhibits a 74% increase in Success Rate, and gpt-4o also shows improvements following JOSH self-alignment. Additional experiments on other public benchmarks indicate that JOSH does not degrade the model’s general performance.

### Strengths
* This paper presents a novel approach to self-alignment in dialogue agents using sparse rewards, reducing reliance on costly human feedback.
* ToolWOZ fills a gap in existing evaluation frameworks by focusing on tool usage in multi-turn dialogue settings, adapting MultiWOZ to emphasize real-world API interactions.
* JOSH demonstrates significant improvements in success rates and tool-call accuracy, particularly for smaller models, validating its effectiveness.

### Weaknesses
 * The paper does not assess how well the user simulator aligns with real human interactions.
* The evaluation of API calls lacks depth, as it does not separate analyses of API names and parameters.
* The design of the average reward function is not thoroughly examined, missing a discussion of alternative reward structures and their potential effects on agent behavior.
* The related work section does not cover relevant advancements in language agents for multi-turn dialogues.

### Questions
* How does JOSH compare to other sparse reward-based alignment or self-improvement approaches?
* Could strategies like reflection, which are often beneficial for tree-search and multi-turn tasks, enhance JOSH’s effectiveness if integrated?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a self-alignment approach called Juxtaposed Outcomes for Simulation Harvesting (JOSH), designed to improve dialogue agents in multi-turn, tool-calling tasks by leveraging sparse rewards. The authors propose ToolWOZ, a new simulation environment derived from MultiWOZ, for training agents to make correct API calls based on sparse reward feedback. The JOSH method aims to allow models, including smaller LLMs, to improve autonomously without relying on extensive human feedback, which is increasingly challenging to obtain as models advance.

### Strengths
1. The JOSH approach is a new solution for self-training dialogue agents, effectively utilizing sparse rewards to build a self-improvement feedback loop without external human evaluation.
2. By adapting MultiWOZ into ToolWOZ with a sparse reward structure, the paper provides a valuable benchmark tailored for tool-using task-oriented dialogue systems, which can benefit further research.
3. Results indicate that JOSH significantly improves models across benchmarks, demonstrating its potential as a scalable solution for optimizing agent interactions in multi-turn dialogue settings.

### Weaknesses
1. The concept of the "goal set" in sparse rewards is insufficiently defined, particularly how it influences the agent’s behavior and the implications of duplicating actions in a path. The description lacks detail on how the goal set is constructed, how it interacts with the agent's policy, and what mechanisms prevent the agent from repeatedly executing the same actions once a goal is achieved. The paper mentions that goals are removed from the set once achieved, but it does not explain how this removal is implemented or how it affects the agent's exploration strategy. Furthermore, the paper does not discuss the potential for the agent to exploit the reward structure by focusing on easily achievable goals while neglecting more complex ones.
2. The choice to branch at the turn level rather than the agent action level lacks a comprehensive rationale, leaving questions about its impact on computational efficiency and performance outcomes. In multiwoz dataset, the agent predicts dialogue act in each turn. The delexiclized response is then generated. The slots values are then filled in the delexiclized response to yield the final response. This process is clearly different from the one illustrated in Figure 2. The paper does not adequately justify why branching at the turn level is superior to branching at the action level, especially considering that each turn can involve multiple actions. The lack of a clear explanation raises concerns about the potential for suboptimal exploration and the computational cost of exploring a larger search space. The paper should provide a more detailed analysis of the trade-offs between turn-level and action-level branching, including a discussion of how each approach affects the agent's ability to learn effective policies.
3. While considerable effort is spent on detailing ToolWOZ, the sparse reward process and its precise mechanics within JOSH are not thoroughly elaborated, reducing clarity around its contribution to the results. The paper does not provide sufficient detail on how the sparse reward is calculated, how it is used to update the agent's policy, and how it interacts with the beam search. The lack of clarity makes it difficult to assess the effectiveness of the proposed method and to reproduce the results. The paper should provide a more detailed explanation of the reward function, including the specific criteria used to determine whether a goal has been achieved and the magnitude of the reward.
4. The baseline comparisons are primarily limited to supervised fine-tuning (SFT) and variants of the sparse reward approach itself. To better contextualize the efficacy of JOSH, comparisons with other RL-based methods, particularly those designed for dialogue or tool-calling tasks, would be beneficial. The paper does not compare the performance of JOSH with other state-of-the-art reinforcement learning algorithms, such as Proximal Policy Optimization (PPO) or Deep Q-Networks (DQN), which are commonly used in dialogue and tool-calling tasks. This lack of comparison makes it difficult to assess the relative strengths and weaknesses of JOSH and to determine whether it represents a significant advance over existing methods.

### Questions
As in weaknesses

### Soundness
2

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
2

### Summary
They propose both a benchmark and a method for training multi-turn tool use dialogue agents. Their method uses beam search to find successful trajectories and uses failed paths in the beam search as negative examples. They finetune an LM on these successful/unsuccessful pairs with KTO. The benchmark is called ToolWOZ, which re-purposes the popular dialogue systems benchmark MultiWOZ to a more native LM tool use format. They evaluate their method on both ToolWOZ and another standard benchmark tau-bench. They find that their method substantially improves LLaMA 3-8B's success rate on both benchmarks. They also conduct evaluations of the robustness of each benchmark by analyzing the standard deviation of the results, finding ToolWOZ with the goal simulator to give the lowest standard deviation. Finally, they conduct some error analysis of their approach on ToolWOZ.

### Strengths
* They propose both a novel method and a benchmark, but they also make sure to evaluate on an existing benchmark to enable more robust comparisons.
* They conduct good analysis to demonstrate the robustness and viability of their benchmark.
* Their method demonstrates good performance gains on the tasks they study.
* The paper is overall well written and easy to follow.

### Weaknesses
 * Their method feels a little ad-hoc. Yes, it makes sense to build off-policy preference pairs for training these models, but there are numerous ways this could be achieved and its unclear why the specific methodological decisions made in this paper are the correct ones.
* They compare to an SFT baseline, but not other RL-inspired approaches for finetuning agents, so it is unclear how well their approach compares against stronger baselines.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces JOSH, a self-training framework designed to enable agentic models to achieve self-alignment. The core component of JOSH is the data rollout pipeline, where an agent first interacts with a GPT-based simulator to generate multi-turn conversations that involve tool-calling responses. A critical aspect of this process is the use of beam search to create a tree-structured trajectory. From this trajectory tree, they extract SFT and preference data for subsequent fine-tuning. To evaluate JOSH, they have also curated a multi-turn tool-calling benchmark called ToolWOZ.

### Strengths
The proposed method is evaluated on different model backbones, even gpt-4o

The curated benchmark is useful to the community.

The presentation is mostly clear and easy to follow.

### Weaknesses
The primary weaknesses of this paper lie in its novelty and the experimental validation.

Novelty: The proposed framework is not particularly novel, as it builds upon concepts that have been extensively studied within the community. Techniques such as data rollouts, beam search, and supervised/preference fine-tuning have all been well-explored in prior works. The combination of these techniques, while potentially useful, does not present a significant conceptual leap. The paper lacks a clear articulation of how the specific integration of these components leads to a novel approach, especially in the context of self-training dialogue agents.

Experiments: This paper evaluates JOSH using only a single benchmark and does not provide comparisons with other robust baselines. There are numerous multi-turn tool-calling and agentic benchmarks available, such as WebLinx and MINT; conducting experiments on multiple benchmarks would significantly strengthen the validity of the results. Furthermore, there are several highly similar methods in this domain, such as Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents and V-STaR: Training Verifiers for Self-Taught Reasoners, which should be considered as baselines to effectively demonstrate the true performance of JOSH. The absence of these comparisons makes it difficult to assess the true contribution of the proposed method.

### Questions
How much does it cost to finetune 4o?

### Soundness
2

### Presentation
2

### Contribution
2
