# CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Language agents have shown some ability to interact with an external environment, e.g., a virtual
world such as ScienceWorld, to perform complex tasks, e.g.,  growing a plant, without the startup
costs of reinforcement learning. However, despite their zero-shot capabilities, these agents
to date do not continually improve over time, beyond performance refinement on a specific task.
 Here we present CLIN, the first language-based agent to achieve this,
so that it continually improves over multiple trials, including when both the
environment and task are varied, and without requiring parameter updates.
Our approach is to use a persistent, dynamic, textual memory,
centered on {\it causal abstractions} (rather than general ``helpful hints''),
that is regularly updated after each trial so that the agent gradually learns useful
knowledge for new trials. In the ScienceWorld benchmark, CLIN is able to continually improve on repeated trials on the same task and environment,
outperforming state-of-the-art reflective language agents like Reflexion by 23 absolute points.
CLIN can also transfer its learning to new environments (or new tasks), improving its zero-shot performance
by 4 points (13 for new tasks) and can further improve performance there through continual memory updates, enhancing
performance by an additional 17 points (7 for new tasks). 
This suggests a new architecture for agents built on frozen models that can still 
continually and rapidly improve over time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use a memory module to help LLM-based agents to do continual learning using interactions with the world. The memory module takes an novel form of causal abstractions to summarize the agent's interaction trace into knowledge that can be reused for future interaction.

### Strengths
Significance: While the idea of having a memory to store experiences is not new, the novelty of the work lies in using LLM to summarize the experience into some form of knowledge, here in causal abstractions. I think this work could open door to more advanced and systematic study of how LLM agents can learn, i.e. gain knowledge from raw information, based on online interactions with the world. 

For example, in a new gaming environment with different physics laws, the LLM-based agent needs to interact with the world to gain information on the actual physics in the new environment. There needs to be a process of learning and obtaining abstractions from these experiences to get generalizable laws. This can potentially help LLM gain new knowledge or domain-specific knowledge about unseen world and unseen domains. 

Experimental Results: the experimental results and comparison with baselines are convincing.

### Weaknesses
1. Technical Novelty: the idea of having a memory of past experiences and learned summary of knowledge is not very new; while this work proposes that the content in the memory is important, i.e., using causal abstractions helps agent's learning, the method is not that different in terms of the general idea.

I think the causal abstraction seems to be only a specific instantiation of imposing some prior structure of memory. The authors would need to give more evidence on why this is universally applicable.

2. The memory entirely depends on the agent's own exploration trace, so if the agent cannot explore enough and find some useful information, the agent cannot gain the corresponding knowledge.

3. I think usually for an agent to be "continually learning", it needs to adapt to many different tasks over time. However, this work focus on accumulating knowledge continually for one task, which is not really continual adaptation.

### Questions
1. When generating causal abstractions, how does the LLM resolves credit assignment problem? If the agent do several actions and results in several different results, how does it know what actions contribute (and not contribute) to what result?

2. Curious about whether the causal abstractions generation depends on LLM' known commonsense knowledge about the world, or depends on its own reasoning ability. What happens if the world follows some new logic, and does the causal abstraction generation still be correct?

3. If the environment dynamics changes and old causal relationships are wrong, does the agent know when to update and unlearn the original knowledge?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a continuously learning language agent called CLIN, which improves the language-based agents. Unlike previous models, CLIN improves its performance without the need for parameter updates. CLIN uses a system centered on causal abstractions and a dynamic textual memory that regularly updates after each trial, the agent gradually learns and applies new knowledge for future trials. This framework is evaluated in the ScienceWorld benchmark, demonstrating its ability to adapt across different tasks and environments.

### Strengths
- The underlying mechanism of using causal abstractions for memory storage demonstrates a novel learning methodology.
- The experiments conducted using the ScienceWorld benchmark are comprehensive and rigorous.
- The paper is well-structured, making it easy to understand.

### Weaknesses
 - The CLIN system is built on past experiences carrying forward context to new experiences. When there are potential issues such as misleading context, it will affect its performance.
- Although CLIN claims to have the ability of self-exploration, it primarily focuses on known information, which may affect its performance in new environments.
- Although CLIN presents some potential improvements over existing methods, it still does not have significant breakthroughs within the framework of current works.

### Questions
- CLIN's textual memory seems to depend heavily on causal abstractions. How does the system handle tasks where the relations are not causal or obscure?
- How robust is the system when facing incorrect or misleading information stored in its memory? Is there any mechanism in place to correct or override these inaccuracies?
- How does the system handle potential changes in state that are not immediately reacted to an action?
- Could you provide more insights on how the executor modifies an action when it doesn't align with valid actions? Specifically, how does it ensure that the modified action still aligns with the intended goal?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the continual learning abilities of LLM agents and proposes CLIN that maintains a memory of causal abstractions to help in future trials by reflecting on the last trial and current memory.

### Strengths
1. The paper is clearly written and easy to follow.
2. The experiments demonstrate a large improvement in multiple environments.
3. The illustrations in the paper are informative.

### Weaknesses
1. The novelty is somewhat limited. Specifically, the authors discussed the difference between their method and Reflexion. But it is not clear if the causal abstractions can be generalized in distinct environments with different goals. Even if they can, I assume that the summaries kept in memory are pretty high-level and abstract. Can these summaries still benefit the performance of individual tasks? The experiments in the ScienceWorld benchmark make sense as different tasks share common rules. More experiments would be good to support the method, such as the benchmarks used in Reflexion (e.g., ALFWorld that the authors used as examples), where common rules may be hard to find useful for individual tasks. It's unclear how the method would perform in environments where the relationships between objects and actions are less structured or more variable, such as interactive coding environments where the causal links are not as explicit as in physical manipulation tasks. The fixed format of the memory, such as "x may be necessary to y", also raises concerns about its adaptability to tasks with more complex relationships that cannot be easily expressed in this format.
2. More comparisons to related works can be added, such as [1, 2] which also improve iteratively via trials.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a memory architecture, CLIN, that generates causal abstractions as textual memory. A memory generator takes the execution results to update the memory. This enables language-based agents to improve their capability over iterations. The inclusion of meta-memory helps generalization to unseen tasks and environments. The experiments in the ScienceWorld benchmark show that CLIN outperforms the state-of-the-art reflective agent, Reflexion.

### Strengths
- CLIN shows that the language agent can continually update and improve its task performance even if they do not update weights.
- This paper shows that it is possible to use prompting to Identify the causal abstractions necessary for agents to change their behaviors or fix previous errors.
- The experiment shows that memory design helps generalization and can efficiently solve some tasks with a few trials.

### Weaknesses
 - The key component of CLIN is the memory abstraction. However, it is hard to understand the criteria of how to determine the necessary causal abstraction and how to assess the uncertainty of the relevant concepts. While the related prompts are provided in the appendix, it will be hard to extend them without understanding the design criteria or rationale for the memory generator. Also, the accuracy of the generated memory is not evaluated, it is unclear whether the performance improves because the LLM generates the correct memory or just provides more details to the task which may not be causal.
- A causal abstraction doesn’t necessarily need to be structured. The drop in ablation when using the free-form advice suggests the importance of the structured sentence format rather than the causal abstraction. This ablation still doesn’t show the usefulness of causal abstraction.

### Questions
The experiment results show that the longer tasks such as growing fruit in Fig 4 are harder for CLIN to adapt. But Fig 4c shows memory improves more episodes for the longer tasks, what are the improvements for long vs. short tasks? What kind of information is still missing for the long tasks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
