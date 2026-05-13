# ReAcTree: Hierarchical Task Planning with Dynamic Tree Expansion using LLM Agent Nodes

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
Recent advancements in task planning using large language models (LLMs) have made remarkable progress. However, most existing methods, such as ReAct, face limitations when handling complex, long-horizon tasks due to inefficiencies in processing entire tasks through a single sequential decision-making process. To address these challenges, we propose ReAcTree, a hierarchical task planning method that automatically decomposes complex tasks into manageable subgoals within a tree structure. This tree consists of control flow nodes, which manage the execution order of agent nodes, and agent nodes that reason, act, and expand nodes into subgoals to achieve their goals. To further enhance performance, we introduce memory systems: each agent node retrieves goal-specific, agent-level experiences from episodic memory to use as in-context examples, and all agent nodes share and recall information obtained during task execution via working memory. Experiments on the WAH-NL dataset demonstrate that ReAcTree consistently outperforms ReAct across various LLMs and model sizes. For example, when using Qwen2.5 72B, ReAcTree achieves a goal success rate of 63\%, significantly surpassing ReAct's 24\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an LLM-based task planning algorithm that decomposes tasks into sub-tasks following a tree structure. This paper is a tree-search-based extension of the ReAct algorithm, which jointly generates reasoning traces (through chain-of-thought) and action/sub-goal sequences to improve performance on planning tasks.

The proposed algorithm ReAcTree enhances ReAct by allowing the agent to generate multiple possible sub-tasks at a state. The candidate sub-tasks will be explored in subsequent steps. When exploring/solving each sub-task, the agent also leverages relevant experiences explored in the past by retrieving them according to a similarity metric (similar to retrieval augmented generation). ReAcTree is tested against ReAct on one dataset and demonstrated improved performance.

### Strengths
- Solving complex real-world planning tasks is very important and relevant to AI research.
- This paper incorporates the idea of tree search into the ReAct algorithm and achieves improved performance.

### Weaknesses
 - The idea of using tree search or graph search to augment LLMs’ reasoning/planning capabilities has been explored by prior work (e.g., [1,2]). It is hard to evaluate the contribution of this paper without a detailed comparison/discussion of these very related approaches. If applicable, it is highly recommended to also include these methods as baselines in the experiments.

- Although ReAcTree can improve upon ReAct as shown by the experiments, it is unclear the difference between their efficiency. For example, by increasing the “maximum decision length” (terminology borrowed from the paper), the performance of ReAcTree will very likely also increase. However, this will render the algorithm more inefficient. If ReAct is given such additional time/compute, it can at least rerun the same algorithm multiple times to increase the success rate. Therefore, I think it is better to compare different methods with both objectives (performance and efficiency) in mind.

- It would be nice to see how much does the tree search component alone contribute to the overall performance. That is, if no memory (episodic memory and working memory in the paper) is used, how does ReAcTree performs compared to ReAct.

### Questions
What's the runtime of the proposed algorithm and the baselines? How would they scale with longer runtime?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a hierarchical method for LLM-based task planning. Rather than using a single decision-making process as in ReAct, ReActTree decomposes a complex task into different subtasks at various levels using a tree structure. Additionally, to manage the complexity in context introduced by the tree structure, the paper proposes a memory module from which related experiences can be retrieved as context.

### Strengths
Decomposing a complex task into a tree structure makes a lot of sense to me. Humans tend to think recursively, and a tree structure can best represent that recursive nature. Retrieving related experiences is also very effective, as having too much unrelated context is not helpful.

### Weaknesses
Despite its usefulness, the proposed method can be overly complex.

### Questions
I am curious if the authors have studied the percentage of tasks that extend beyond three layers when expanding the tree. What are the statistics regarding tasks and the number of layers in their expanding trees?

### Soundness
3

### Presentation
3

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
This paper introduces ReAcTree, a hierarchical task planning framework designed to handle complex, long-horizon tasks by decomposing them into smaller subgoals within a dynamic tree structure. ReAcTree uses control flow nodes and agent nodes, where each agent node functions as a task planner capable of reasoning, acting, and expanding goals. The model includes two memory components: episodic memory to store agent-specific experiences and working memory to share observations across nodes, allowing for more contextually relevant task planning.

### Strengths
1. ReAcTree’s approach to breaking down tasks into manageable subgoals enables it to handle complex, long-horizon tasks with greater efficiency than sequential approaches.

2. By incorporating episodic memory and working memory, ReAcTree improves the relevance of in-context examples and facilitates observation sharing across agent nodes, reducing task redundancy and improving task success rates.

### Weaknesses
1. The paper lacks a clear explanation of how memory (both episodic and working) is coupled with ReAcTree agents. The integration details are not shown in the algorithm, leaving critical explanations about memory interactions and their role in ReAcTree agents underdeveloped.

2. The paper would benefit from a substantial rewrite to improve clarity, particularly around key definitions, memory components, and the agent interaction mechanisms within ReAcTree.

3. The memory retrieval approach relies solely on cosine similarity without a discussion of its selection or adaptability as memory scales. Furthermore, it is unclear how the memory retrieval process integrates termination states and handles large datasets.

4. While the paper claims that shorter text trajectories improve retrieval efficiency, the ReAcTree framework targets complex, long-horizon tasks that likely produce lengthy trajectories, making this assertion unclear. Constraints or empirical evidence on trajectory length’s impact would add clarity.

### Questions
1. In L233-237, the authors introduce an **extended action space** for agent nodes, which appears to include a vast range of potential actions. Given this large action space, how does the approach address the **curse of dimensionality** in selecting and processing these actions efficiently?

2. In Algorithm 1, L11, the variable **$n_e$** is used, but it is not defined in the paper. Could you clarify what $n_e$ represents in this context?

3. Regarding the **episodic memory retrieval** mechanism:
   - How does the **cosine similarity** metric work in this context to retrieve relevant experiences? Why was this method chosen over alternative retrieval strategies?
   - How well does this method scale when the memory contains a **large number of stored experiences**?
   - What role does the **termination state $s$** play in memory retrieval? Specifically, does ReAcTree consider only successful trajectories, or are other outcomes (e.g., failures) also retrieved?

4. In L290-291, the authors mention that **shorter text trajectories** allow for more efficient context usage, facilitating a broader range of example retrieval. However:
   - Could you provide an **empirical study** or analysis supporting this claim?
   - Is there a **constraint** on the trajectory size for optimal efficiency in ReAcTree?
   - Given that ReAcTree aims to handle **complex, long-horizon tasks**, which often generate extensive text trajectories, how does the approach reconcile this apparent paradox between trajectory length and retrieval efficiency?

5. In L294-295, the paper describes **working memory** as part of the agent's skill set, $A_t^n$. This raises some clarity issues:
   - Could you clarify or redefine **skill set** to explain how working memory integrates within it?
   - Why is working memory modeled as an **action** in the task planning context, and how can it be "utilized as an action by agent nodes"?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ReAcTree, a novel hierarchical task planning framework that leverages Large Language Models (LLMs) to decompose complex tasks into manageable subgoals using a dynamic tree structure.

### Strengths
1. The dynamic tree expansion mechanism effectively combines the structure of behavior trees with the flexibility of LLM-based planning.
2. The experiments cover multiple LLM architectures and sizes, demonstrating the framework's robustness.
3. The framework addresses real-world constraints through partial observability in the experimental setup.
4. The improvement compared to ReAct is significant.

### Weaknesses
1. The paper seems to lack a comparison with other tree-based planning methods [1-3]. This makes it difficult to contextualize the contribution within the broader landscape of hierarchical planning approaches.
2. The abbreviation "WM" in Table 1 is not explicitly defined in the caption or text, reducing clarity.
3. The paper doesn't discuss the computational cost of maintaining and expanding the tree structure compared to sequential approaches.
4. There could be more discussion about when and why the system fails, which would help understand its limitations.

### Questions
See weaknesses. Further:

1. What is the impact of different memory retrieval strategies on the system's performance?
2. How does ReAcTree handle cycles or repetitive tasks that might require loop structures?
3. Given that the LLM needs to perform repeated planning at different nodes in the tree structure, is there a potential issue of error accumulation? When mistakes occur at higher levels of the tree, how do they propagate through the subsequent planning steps? It would be valuable to see an analysis of error propagation and any mechanisms in place to mitigate such cascading failures.

I would consider raising my score based on the authors' response

### Soundness
3

### Presentation
3

### Contribution
3
