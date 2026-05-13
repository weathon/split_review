# Tool-Planner: Task Planning with Clusters across Multiple Tools

- Decision: Accept
- Scores: 5, 8, 5, 6

## Abstract
Large language models (LLMs) have demonstrated exceptional reasoning capabilities, enabling them to solve various complex problems. Recently, this ability has been applied to the paradigm of tool learning. Tool learning involves providing examples of tool usage and their corresponding functions, allowing LLMs to formulate plans and demonstrate the process of invoking and executing each tool. LLMs can address tasks that they cannot complete independently, thereby enhancing their potential across different tasks. However, this approach faces two key challenges. First, redundant error correction leads to unstable planning and long execution time. Additionally, designing a correct plan among multiple tools is also a challenge in tool learning. To address these issues, we propose Tool-Planner, a task-processing framework based on toolkits. Tool-Planner groups tools based on the API functions with the same function into a toolkit and allows LLMs to implement planning across the various toolkits. When a tool error occurs, the language model can reselect and adjust tools based on the toolkit. Experiments show that our approach demonstrates a high pass and win rate across different datasets and optimizes the planning scheme for tool learning in models such as GPT-4 and Claude 3, showcasing the potential of our method

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes clustering similar tool APIs via LLMs and embeddings to enhance LLM planning efficiency in tool use. The ToolPlanner framework effectively addresses tool planning and invocation tasks using toolkits. Empirical results demonstrate the framework's superiority in performance and efficiency compared to multiple baselines, while ablations confirm the effectiveness of tool clustering.

### Strengths
1. The paper is well-written and easy to follow.
2. Comprehensive ablation studies on the core component, the toolkit.
3. Detailed appendix with experimental specifics and case studies.
4. Insightful error analysis.

### Weaknesses
1. The paper could include more comparisons with tree-based inference methods in LLMs, e.g., [1][2] in related work.
2. Consider comparing with ToolChain*[3].
3. The novelty is somewhat limited, as noted in Line 375, where the method is derived from DFSDT by replacing API nodes with toolkits. The authors could elaborate more in Sec 3.3 and include task replanning experiments to better distinguish this framework from DFSDT. While on the other hand, extensive results and ablations strengthen confidence in the framework's efficiency and effectiveness

### Questions
1. I suggest a name change for the framework to better reflect its toolkit-based planning, e.g., ToolkitPlanner.
2. Beyond Figure 4, what is the computation cost/wall time for clustering these APIs?
3. Line 217: How is another available API t′ selected within the same toolkit?
4. Line 259: Which LLM is used to assess Win Rate?
5. Line 262: Could the authors provide more details on detecting and measuring hallucinations?
6. The novelty is somewhat limited, as noted in Line 375, where the method is derived from DFSDT by replacing API nodes with toolkits. The authors could elaborate more in Sec 3.3 and include task replanning experiments to better distinguish this framework from DFSDT. While on the other hand, extensive results and ablations strengthen confidence in the framework's efficiency and effectiveness

 [1] Zhou, Andy, et al. "Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models." Forty-first International Conference on Machine Learning.

 [2] Feng, Xidong, et al. "Alphazero-like tree-search can guide large language model decoding and training." arXiv preprint arXiv:2309.17179 (2023).

 [3] Zhuang, Yuchen, et al. "ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search." The Twelfth International Conference on Learning Representations.

### Soundness
3

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
This paper introduces a new framework, Tool-Planner, which formulates LLM planning with API tools as a tree-search over clusters of tools, or 'toolkits', generated using SimCSE. Experiments and ablations show the soundness of this approach over its closest relative, DFSDT, which does a tree-search over single tools.

### Strengths
$Originality:$ This paper builds upon DFSDT and introduces a toolkit which provides better performance.

$Quality$: The experiments cover domains with many APIs, relevant baselines, and ablations which showcase the importance of the design choices.

$Clarity$: The paper is presented very clearly, especially methodology. My only nitpick is Figure 2 - my first  impression was that this was another Toolchain [1] paper because the search seems to be over single APIs rather than a selection over toolkits and then the most relevant API in the toolkit.

$Significance$: LLM abilities are empowered as they gain access to new tools but they also perform poorly in reasoning tasks with large action spaces. This paper provides a clever trick to cluster tools together, reducing the LLM decision space and simplifying the planning task. This will ensure that LLM performance in domains with tools remains relatively high regardless of the future introduction of many new tools.

[1] ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search (Zhuang et al. 2023)

### Weaknesses
- Table 1's feature categories are vague (what is Tool Integration?) and don't make it obvious how your work  clearly contrasts from DFSDT. "Tool Clustering" distinguishes this work more from DFSDT.
- Figure 2 looks like DFSDT or ToolChain from a glance; it is not obvious that the nodes were chosen from toolkits. Adding more emphasis / text on the toolkits could make things clearer.
- Toolchain is compared against in Table 1 but missing from the experiments

### Questions
- How were the "Explainable Planning" and "Tool Integration" categorizations decided?
- What does "Tool Integration" refer to?
- How often do you observe failures where prioritizing APIs within the same toolkit leads to unnecessary expansions (due to the appropriate API being in another toolkit)?
- Why is ToolChain compared against in Table 1 but not in the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Tool-Planner method, a toolkit-based task planning framework designed to enhance the task planning and execution efficiency of LLMs in the context of tool learning. Tool-Planner achieves this by clustering APIs with similar or identical functionalities into toolkits, enabling LLMs to plan across these toolkits. This approach facilitates rapid adjustments and optimization of planning pathways when encountering tool-related errors, thereby improving overall performance.

### Strengths
- The proposed method is both intuitive and effective, as it enhances the accuracy and efficiency of LLMs in tool invocation through the clustering of tools and planning at the toolkit level.
- Experimental results on the ToolBench and APIBench datasets substantiate the efficacy of Tool-Planner in improving both success rates and competitive performance.

### Weaknesses
 - Certain aspects of the methodology require further clarification. For instance, in Section 3.2, the statement "In solving problems for specific states, the model will choose any API within the toolkit for invocation" raises concerns regarding its potential oversimplification. Additionally, since each API necessitates a specific parameter structure for input, how does the model determine the corresponding parameters for an arbitrarily selected API? This is especially concerning given that the API selection process within a toolkit seems to lack a clear decision-making process beyond random choice, which could lead to suboptimal API usage.
- The performance of Tool-Planner is significantly contingent upon the accuracy of the clustering process. Inadequate clustering may hinder the model's ability to identify suitable tools, thereby affecting task completion. Careful tuning of the clustering parameter is essential to achieve optimal performance, which may necessitate additional experimentation and adjustments. The paper does not sufficiently explore the sensitivity of the method to different clustering parameters or provide clear guidelines for selecting optimal values, which is a critical oversight.
- In the section on "Planning Exploration on Solution Space," it is important to quantify the number of tasks that progress to the "Task Replanning Across Toolkits" stage. Furthermore, what are the corresponding token consumption and computational time for these tasks? Without this data, it is difficult to assess the efficiency gains or losses associated with the replanning mechanism. The paper should also detail the criteria that trigger the need for cross-toolkit replanning.
- The ablation study requires further elaboration on the actual configuration of the baseline with Toolkit Integration. Specifically, how is the integration achieved, and what criteria are used to select the toolkit before invoking a specific API? Additionally, an adaptive adjustment method for the number of clusters should be described, along with experimental results validating the use of clustering methods such as DBSCAN for adaptive clustering. The current description lacks the necessary detail to understand the baseline's implementation and the adaptive clustering process.
- In the "Efficiency Evaluation" section, it is noted that the runtime of Tool-Planner is significantly higher than that of other algorithms outside of DFSDT. I would like to see a comprehensive analysis of the number of LLM invocations and token usage statistics associated with different methods. This would provide a more thorough assessment of method efficiency. Furthermore, analyzing the impact of cluster quantity selection on execution efficiency would be a valuable addition to the discussion. The paper needs a more granular analysis of the computational overhead associated with Tool-Planner, particularly in relation to the number of clusters used.

### Questions
Please refer to the Weaknesses section for details. I’m open to discussion and increasing my score if my comments are addressed satisfactorily.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Tool-Planner, a framework for task planning that uses clustered toolkits as nodes in tree search.

### Strengths
1. The idea of using toolkits as nodes in tree-search is novel and intuitive, providing a more structured approach to handling API failures.
2. The experimental results are comprehensive, covering multiple datasets and comparing against various strong baselines.

### Weaknesses
1. The method's performance heavily depends on the quality of the clustering algorithm and model. While Table 5 shows end-to-end performance comparisons of different clustering models, there's a lack of intermediate metrics to evaluate clustering quality.

2. The selection of the optimal k value for k-means clustering remains challenging. As is shown in Figure 3, determining an appropriate k value requires exploration and this is actually impractical when facing new datasets.  

3. The fundamental contribution of Tool-Planner can be viewed as introducing a prior into conventional tree-search-based methods - specifically, the assumption that when an API fails, the model should first attempt similar APIs. While this intuition is reasonable and the experimental results are promising, the paper has two key limitations in this aspect:

    **a.** Lacking theoretical analysis or justification for why clustering tools into toolkits leads to better performance. While empirically effective, understanding the theoretical underpinnings could provide insights into when and why this approach works better than alternatives.

    **b.** The paper doesn't explore whether similar benefits could be achieved through simpler means. Notably, the same prior (trying similar APIs first when one fails) could potentially be incorporated directly into LLM prompting. It remains unclear whether the additional complexity of explicit clustering and toolkit-based search is necessary, or if similar performance gains could be achieved by simply instructing the LLM to prefer similar APIs when handling failures.

### Questions
See weaknesses. Further:

1. Have the authors considered using more sophisticated clustering methods that don't require pre-specifying the number of clusters?
2. How does Tool-Planner perform when the available APIs change frequently? Is reclustering needed, and if so, how often?

I would consider revising my rating based on the authors' responses to these questions.

### Soundness
3

### Presentation
3

### Contribution
3
