# Data Interpreter: An LLM Agent For Data Science

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Large Language Model (LLM)-based agents have shown effectiveness across many applications. However, their use in data science scenarios requiring solving long-term interconnected tasks, dynamic data adjustments and domain expertise remains challenging. 
Previous approaches primarily focus on individual tasks, making it difficult to assess the complete data science workflow. Moreover, they struggle to handle real-time changes in intermediate data and fail to adapt dynamically to evolving task dependencies inherent to data science problems.
In this paper, we present \textbf{Data Interpreter}, an LLM-based agent designed to automatically solve various data science problems end-to-end. 
Our \model{} incorporates two key modules: 1) \textit{Hierarchical Graph Modeling}, which breaks down complex problems into manageable subproblems, enabling dynamic node generation and graph optimization; and 2) \textit{Programmable Node Generation}, a technique that refines and verifies each subproblem to iteratively improve code generation results and robustness.
Extensive experiments consistently demonstrate the superiority of \model{}. 
On InfiAgent-DABench, it achieves a $25\%$ performance boost, raising accuracy from $75.9\%$ to $94.9\%$. For machine learning and open-ended tasks, it improves performance from $88\%$ to $95\%$, and from $60\%$ to $97\%$, respectively.
Moreover, on the MATH dataset, \model{} achieves remarkable performance with a $26\%$ improvement compared to  state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Data Interpreter, a solution for constructing and executing data analytical pipelines on a given dataset (to be analyzed) and task specification. The solution is based on a hierarchical graph modeling of complex task decompositions, from task graph generator, action graph generator, to graph executor. The abilities of LLMs, including reasoning, planning, and code generation, are utilized in different phases and composed as an end-to-end solution. Data Interpreter is evaluated on various benchmarks and datasets.

### Strengths
S1. A system with strong motivations and real use cases is built and presented.

S2. The paradigm of task deposition is reasonable and likely to utilize LLM's abilities in an effective way.

S3. The solution works for various types of tasks and shows good performance in experiments.

### Weaknesses
W1. Overall, the presentation of the overview and some details of the solution is clear. Better if there is a real and complete example in the paper to help explain intuitions and more details of the solution.

W2. Overhead of the solution (e.g., resource, time, and cost for each task) is not analyzed and reported.

### Questions
Q1. Better if there is an end-to-end example in Section 3, which help explain how different components work in Data Interpreter in more details and intuitions. For example, how a task graph is generated step by step, what happens if there is an execution failure, and so on.

Q2. Analyze and/or report the overhead of the solution (e.g., resource, time, and cost for each task) as well as different components.

Q3. Reproducibility of the experimental results need to be commented (how to ensure the reproducibility?)

### Soundness
3

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
3

### Summary
This paper introduces a multi-agent framework for the automated resolution of data science problems. Specifically, a hierarchical graph modeling module is designed to decompose complex problems into interconnected sub-problems, followed by a programmable node generation technique that addresses each sub-task through iterative code generation and refinement. Their approach (named Data Interpreter) achieves better results when compared with other SOTA models on three different evaluation datasets.

### Strengths
1. This work establishs a novel data science scaffold that interprets tasks as graph, iteratively refining both sub-task construction and execution. They test the effectiveness of this method and achieved better performance given some baselines, additionally, ablation studies also confirm the effectiveness of the proposed module.
2. This paper is well-structured and presents a clear workflow of their proposed method, and show some interesting demonstrations to validate their advancedness of this scaffold.

### Weaknesses
From my perspective, the incremental contribution of this paper appears modest and limited, for the following reasons:
1. Like other LM-based agents[1], this method also relies on prompting techniques and without introducing interesting or advanced reasoning capabilities. Thus, the incremental contribution may not align with the standards expected at such a top conference.
2. Although the experiments display substantial performance improvements, the tasks appear carefully curated and too easy, potentially making them less convincing as evidence of the method’s advancedness.
3. The paper lacks comparisons with recent benchmark results within the same domain, as seen in [1][3], which could have strengthened the empirical evaluation.

### Questions
The baseline tasks and methods selected for comparison seem outdated and relatively easy. Could you provide additional evaluations against more recent benchmarks (e.g., the tasks in [2][4]) to more assess the effectiveness of this method?  Are there particular reasoning techniques or capabilities you think would significantly advance the field if incorporated?\
\
\
\
[1] Dominik Schmidt, Zhengyao Jiang, and Yuxiang Wu. "Introducing Weco AIDE", URL: https://www.weco.ai/blog/technical-report, 2024.\
[2] Qian Huang, Jian Vora, Percy Liang etc.. "MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation", ICML24.\
[3] Liqiang Jing, Zhehui Huang etc.. "DSBench: How Far Are Data Science Agents to Becoming Data Science Experts?", 2024.\
[4] Jun Shern Chan and Neil Chowdhury etc. "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering", 2024.

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
4

### Summary
The paper introduces Data Interpreter, a LLM-based agent designed to automate complex data science workflows. The authors address the limitations of existing methods, which often struggle with long-term planning, dynamic data adjustments, and evolving task dependencies.

### Strengths
1. The combination of hierarchical graph modeling and programmable node generation not only effectively addresses task decomposition and code generation but also enhances system flexibility and adaptability through dynamic node generation and graph optimization.
2. The abstraction of tasks and actions into graph structures is rational, which allows for more granular control and flexibility in the execution process, making it easier to handle complex and interconnected tasks.
3. The experimental results show that Data Interpreter achieves significant performance improvements in these tasks.
4. How to use LLM agents to solve complex data science tasks has broad practical applications.

### Weaknesses
While the paper presents a compelling and innovative approach to solving data science tasks using a LLM agent, there are several areas where the work could be improved. Below is a detailed assessment of the weaknesses, with a specific focus on the experimental setup and the lack of token usage comparison.  
1. One significant weakness in the experimental setup is the lack of a detailed comparison of token usage. The paper does not provide information on how many tokens are required for different tasks and datasets, nor does it compare the token consumption of Data Interpreter with other methods or baselines.  
2. The authors should conduct a thorough analysis of token consumption for different tasks and methods.  Provide a comparative analysis of token usage between Data Interpreter and existing methods or baselines. This will help readers understand the efficiency and resource requirements of Data Interpreter relative to other solutions.
3. By addressing the lack of token usage comparison, the authors can provide a more comprehensive and insightful evaluation of Data Interpreter, making the paper more robust and valuable to the research community.

### Questions
Could you provide a detailed breakdown of the token consumption for different types of tasks and datasets, and compare it with existing methods or baselines? Understanding the token usage will help evaluate the efficiency and resource requirements of Data Interpreter, especially in resource-constrained environments.

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
The paper proposes Data Interpreter, an LLM agent agent designed to solve data science tasks in an end-to-end fashion. Compared to existing works on LLM agent, this work presents two innovative modules: (1) the Task Graph Generator, which employs Hierarchical Graph Modeling to break down tasks into smaller, more manageable components, and (2) the Action Graph Generator, which utilizes Programmable Node Generation to select or generate tools and code for execution. These enhancements result in a 19.01% improvement in accuracy over the naive GPT-4 model on the InfiAgent-DABench and demonstrate competitive performance across various benchmarks, surpassing existing approaches.

### Strengths
- The paper addresses an intriguing and timely problem, which is how human can utilize the ability of LLM to perform end-to-end tasks for users efficiently.
- The authors conduct an extensive series of experiments across various data science tasks, achieving strong benchmark performance, which highlights the potential and effectiveness of the proposed approach.

### Weaknesses
 - Section 3 introduces the two primary contributions of the paper—Hierarchical Graph Modeling and Programmable Node Generation. However, some descriptions are way too vague and redundant, and should be streamlined and clarified. The current form leaves readers with many questions. For example:

  - Line 200-201: The nature of the relationship $r$ between processes lacks clarity. Is $r$ determined by predefined constraints that guide the LLM in constructing the **Directed Acyclic** Graph (DAG)? For example, does it ensure that steps like data visualization precede model training? Although introduced as a challenge, it’s later stated (line 214-215) that subprocesses exchange intermediate results and parameters, also represented by $r$. However, this raises questions: Wouldn’t exchanging information between processes that occur sequentially lead to cyclic dependencies in a DAG? How could a process that is supposed to appear later in a DAG exchange information with some other process that has already been executed? More importantly, under such a formulation, isn't the previously stated challenge easily solved, since every subprocess is defined to have a relationship with each other?
  
  - Equation 2 incurs more confusion. The presented equation only states the objective is to select the graph that maximizes the expected performance. It leaves unclear how the system generates potential graphs and evaluates their expected performance without prior execution. Is the system generating all possible graphs at once? Does the evaluation happen after the execution of the graph? Elaboration on these points would help clarify the approach.

  - The paper mentions "refining relationships between subprocesses" on line 216, but the actual refinement process is unclear. The only thing that's close to it is "Task Graph Refinement" on line 266, it appears to focus on editing task nodes rather than relationships. Further clarification on whether “subprocess” and “task” refer to the same entities, and on the refinement process, would enhance reader understanding.

  - The Algorithm 1 as presented, includes a variety of functions that are not well defined, which can make it difficult to interpret the intended functionality. From a reader’s perspective, it appears as a general nested-loop structure. More explicit descriptions of key functions would improve clarity.

  - How is the task graph generator on line 256 implemented?

  - What is the episodic memory defined on line 312? The episodic memory concept appears to leverage existing technology rather than representing an innovation within this work. 

  - Implementation Details in the appendix also only contains a single figure (Fig.6) that dives into the detail. However, several elements in this figure, such as "think", "act" and "combinations" lack clear definitions, which may hinder comprehension. Expanding these descriptions would provide us with some understanding of the methodology.

  - The *lack of reproducibility* of this work (see below) further exacerbates this problem.

- Continuous monitoring and iterative update seems less innovative, as it resembles functionality already present in major LLM-serving platforms, like ChatGPT, which also support updates following unsatisfactory results. Lines 262-264 suggest that this work automates this process by notifying the LLM when code execution encounters issues, which, while functional, is trivial.


- On line 533, the author states that "Our framework continuously monitors data changes and adapts to dynamic environments through iterative task refinement and graph optimization". However, it is unclear how "data change" is defined or detected. For example, how does the system recognize modifications in the underlying data (such as a file update at a previously specified path)? Additional explanation on this would be beneficial.

- No code nor any reproducibility statement has been provided by the authors. Given that the LLM backends used in this work (e.g. gpt-4, gpt-4o) as well as the datasets utilized in this work are publicly available, offering a reproducible example or allow readers to conduct experiments on their own would be extremely valuable in showcasing the agent's capabilities. Due to the missing of the code, I am unable to independently verify the results.

As it stands, the paper comes across more as a vague, high-level technical report rather than a fully detailed academic submission, as it primarily outlines the design without delving into the implementation specifics or the rationale behind certain design choices. Consequently, the work fall short of the rigor expected for ICLR.

Other minor problems in writing:

- Line 228: missing spaces before data exploration

- Line 244: At a more granular level -> At finer granularity

- Appendix A: Diversity and complexity insufficient -> Insufficient diversity and complexity.

- Figure 6: Recomendation -> Recommendation

### Questions
See weaknesses for a plethora of major questions.

Other questions include:
- Line 419-427 and Table 1 suggest that the proposed approach may underperform when using GPT-4, which the authors attribute to limitations in handling long contexts, proposing that this could be addressed with LLM backends that support extended context lengths like GPT-4o. This raises a few questions: Would similar performance improvements be observed with other LLMs (e.g., GPT-4-Turbo with 128k context or Qwen-72B with 32k context), several of which have already been tested in the ablation studies? Additionally, it would be valuable to know the primary failure cases of GPT-4 on InfiAgent-DABench and understand how Data Interpreter effectively mitigates these challenges.

### Soundness
3

### Presentation
2

### Contribution
2
