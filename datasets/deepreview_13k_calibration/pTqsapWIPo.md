# $\textit{RwR}$: A Reason-while-Retrieve framework for Reasoning on Scene Graphs with LLMs

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Large Language Models (LLMs) have demonstrated impressive reasoning and planning capacities, yet grounding these abilities to a specific environment remains challenging. Recently, there has been a growing interest in representing environments as scene graphs for LLMs, due to their serializable format, scalability to large environments, and flexibility in incorporating diverse semantic and spatial information for various downstream tasks. 
Despite the success of prompting graphs as text, existing methods suffer from hallucinations with large graph inputs and limitation in solving complex spatial problems, restricting their application beyond simple object search tasks.
  In this work, we explore grounding LLM reasoning in the environment through the $\textit{scene graph schema}$.  
We propose $\textit{SG-RwR}$, an iterative reason-while-retrieve scene graph reasoning framework involving two cooperative schema-guided code-writing LLMs: a (1) $\textit{Reasoner}$ for task planning and information querying, and a (2) $\textit{Retriever}$ for extracting graph information based on these queries. 
  This cooperation facilitates focused attention on task-relevant graph information and enables sequential reasoning on the graph essential for complex tasks.
  Additionally, the code-writing design allows for the use of tools to solve problems beyond the capacity of LLMs, which further enhance its reasoning ability on scene graphs. 
  We also demonstrate that our framework can benefit from task-level few-shot examples, even in the absence of agent-level demonstrations,
  thereby enabling in-context learning without data collection overhead.
  Through experiments in multiple simulation environments, we show that $\textit{RwR}$ surpasses existing LLM-based approaches in numerical Q\&A and planning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes the RwR (reason while retrieve) framework which equips LLM with scene graph schema and provides a code interface for the LLM to interact with the graph. This is in contrast with some prior works that input the whole graph into the LLM's context. The Reason part is an LLM capable of reasoning over the environment and asks the retriever queries to complete. The retriever executes queries on the underlying scene graph and responds to the reasoning system. The authors show that this strategy is effective by testing this on three tasks showing superior performance compared to methods such as chain-of-thought

### Strengths
* The paper is well-written and easy to follow.
* Some prompt design choices are interesting (such as preventing the model from assuming things by detecting the word "assumption" in the response).
* The method shows superior performance compared to CoT and other intrinsic reasoning baselines.

### Weaknesses
 * The main weakness is the lack of novelty of this work: The introduced method seems to be a ReAct-style system + Tool-integrated reasoning (over graphs). As the authors mention in the related work section, incorporating knowledge retrieval from graphs has also appeared in prior works. The main novelty of this work seems to be the design of a Python interface for interacting with scene graphs + prompt designs.

* The method relies on the availability of a scene graph, which may not be available (e.g., a partially observable environment), or easily extractable.

[1] Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models, ICLR 2023

### Questions
* Can the method be extended to partially observable environments? For instance by providing the retriever an API to also modify the scene graph?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the issue of LLMs lacking the ability to handle large graph inputs and solve complex spatial tasks, this work proposes $\textit{RwR}$, a framework for reasoning on scene graphs with LLMs. $\textit{RwR}$ adopts a Reason-while-Retrieve style. The reasoner decomposes the task into small subtasks. Based on the output of the reasoner, the retriever extracts relevant graph information. Instead of feeding the entire graph into LLMs, this pipeline enables $\textit{RwR}$ to process task-related subgraph information, reducing the hallucinations and window size limitations of LLMs. Additionally, $\textit{RwR}$ has access to external tools, which further improve the reasoning ability of LLMs on scene graphs. Experiments in multiple simulation environments prove that $\textit{RwR}$ exhibits impressive performance.

### Strengths
1. This work represents the first effort in reasoning with scene graphs using LLMs, which facilitates the study of scene graphs.
2. Instead of simply using graphs-as-text as input to LLMs, this work proposes the Reason-while-Retrieve framework, which combines the reasoning and retrieval phases together, addressing the problem that LLMs cannot handle large input graphs.
3. $RwR$ utilizes schema-based grounding and code-writing for graph information, reducing hallucinations and improving reasoning ability, which can be applied in other graph-LLM-related domains.

### Weaknesses
1. $RwR$ retrieves and reasons multiple times, which increases the reasoning time.
2. The graph schemas and reasoning tools are also manually designed for specific tasks, causing issues when transferring to new tasks.
3. You conducted a few-shot experiment; however, you should conduct various few-shot experiments.

### Questions
1. I would like to see analysis about the increased time caused by retrieving more than once, compared to Retrieve-then-Reason method.
2. I was also wondering if $RwR$ can be used with other commonly used GraphRAG datasets, such as ExplaGraphs, SceneGraphs, and WebQSP. If so, please conduct experiments to prove its applicability or provide analysis. If not, please state the reasons why.
3. Why you do not contain retrieve-then-reason method in your baseline?

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
4

### Summary
The paper introduces Reason-while-Retrieve (RwR), a framework that grounds large language models (LLMs) in environments represented as scene graphs to enhance complex reasoning. RwR uses two cooperating LLM agents: a Reasoner for task planning and a Retriever for extracting relevant subgraphs, working in an interleaved manner to overcome information overload in the Reasoner. This framework also enables tool-assisted problem-solving through code-writing. Experiments demonstrate that RwR outperforms existing methods across several tasks.

### Strengths
1. The proposed Reason-while-Retrieve (RwR) framework introduces an interleaved approach, alternating between subtask planning and targeted subgraph extraction from scene graphs, enhancing reasoning performance.

2.  The schema-based grounding and code-writing enables precise information retrieval from graphs, minimizing hallucinations and strengthening LLM reasoning on complex tasks.

3. Experimental results indicate that RwR significantly improves performance across various tasks in distinct environments.

### Weaknesses
1. The novelty of the Reason-while-Retrieve (RwR) framework is somewhat limited, as it closely resembles the ReAct framework. ReAct also utilizes an interleaved approach where LLMs generate both reasoning traces and task-specific actions to address hallucination issues. In each iteration, ReAct first produces a reasoning "thought" and then generates an action to interface with and gather information from external environments.

2. The procedural details of RwR are not fully articulated. As shown in Figure 2, some iterations appear to exclude the query step, leaving it unclear how these missed queries are managed within the framework. Furthermore, the role of the code writing and execution within the analysis step is not clearly defined, especially given that the code execution outcome is not explicitly shown in Figure 2.



### Questions
1. What are the key differences between RwR and ReAct? Could the authors consider using ReAct as a baseline for comparison?

2. In Table 1, for the NumQ&A task, why does ZeroShot outperform CoT methods (both 0-CoT and Few-Shot CoT)?

3. Typos:
   - In the middle of Figure 2, there are two instances of *a_t*. 
   - In line 192, it’s unclear why the conversation history includes *(q_t, G_t)*, and the definition of *G_t* is missing.
   - In line 197, it states "query for the 'door IDs and attributes' that connect two rooms (a2) for solving the subtask," *a2* should be *q2* here.

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
3

### Summary
The paper introduces a cooperative graph reasoning framework called **Reason-while-Retrieve** (**RwR**) , designed to enhance the capabilities of large language models (LLMs) across two simulation environments, BabyAI and VirtualHome. Unlike previous approaches, RwR leverages the collaboration of two specialized agents—a Reasoner and a Retriever —which write code to process textual graph-based information, mitigating the effect of hallucinations. Furthermore, the proposed method achieves state-of-the-art performance on tasks in BabyAI, Numerical Q&A, and VirtualHome.

### Strengths
The topic of this paper, leveraging LLMs for reasoning with scene graphs, is both interesting and significant. The strengths of this work are as follows:

1. The figures are clearly presented, making it easy to follow and understand the message the authors are conveying.

2. The paper introduces code-writing and schema-based grounding techniques for graph reasoning, which effectively help mitigate hallucinations in LLM reasoning.

3. The proposed approach, RwR, significantly enhances the performance of LLMs in tasks like Numerical Q&A, 2D Traversal, and Household Task Planning. Notably, it achieves a perfect score (100%) in the VirtualHome environment.

### Weaknesses
The weaknesses are illustrated as below:

1.  **Lack of Novelty**: The core idea presented in the paper does not appear sufficiently novel. While the paper introduces an iterative reasoning process, the concepts of a "Retriever" and "Reasoner" are already well-established in the field of graph reasoning. Most importantly, the authors fail to provide detailed experimental results regarding how many rounds of iteration the RwR requires, which weakens the contribution of the proposed method. Furthermore, the specific implementation of the "Retriever" and "Reasoner" for scene graphs lacks a detailed justification for its design choices. The paper does not adequately explain why the chosen code-writing and schema-based grounding techniques are superior to other potential methods for processing graph-based information, especially given the existing literature on graph neural networks and symbolic reasoning.

2.  **Incomplete Experimental Results**: Some experiment results seem not complete, such as RwR-FS and RwR-A on the NumQ&A dataset in Table 1. The lack of these results makes it difficult to fully assess the method's performance across different settings. Additionally, the paper does not provide a clear analysis of the computational overhead introduced by the iterative reasoning process, particularly in terms of inference time and memory usage. This is a crucial aspect for practical applications and should be thoroughly investigated.

3.  **Lack of Evaluation on Hallucinations**: Given that one of the core motivations of the paper is to mitigate hallucinations in graph reasoning, it is essential to provide some relevant experimental results, like hallucination rates or detailed case studies. This would allow readers to better understand the effectiveness of the proposed method in addressing this issue. The paper should include a quantitative analysis of how often the model generates incorrect or inconsistent information when processing scene graphs, and compare it to baseline methods. Without this, the claim of mitigating hallucinations remains unsubstantiated.

### Questions
In addition to the weaknesses previously highlighted, could the authors consider providing results using an open-source LLM? This would offer greater clarity and accessibility for the research community.

### Soundness
3

### Presentation
2

### Contribution
3
