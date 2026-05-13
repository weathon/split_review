# Can Large Language Models Effectively Modify Graphs?

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Graphs are essential tools for modeling complex relationships. While prior research with earlier generations of large language models (LLMs) showed them to struggle with basic graph primitives, we find that the situation has changed with modern state-of-the-art (SOTA) LLMs, which excel at these tasks. Given these advances, we propose a more challenging evaluation problem: graph modification, a foundational, interpretable, and non-trivial problem in which an LLM must determine the outcome of adding or deleting a given sequence of nodes or edges, and potentially then compute on the resulting modified graph. We introduce GraphModQA, a novel benchmark dataset comprising graph modification question-answer pairs designed to rigorously test LLMs’ abilities in graph manipulation and dynamic reasoning. Our results show that while SOTA LLMs perform well on static graph property tasks, their accuracy degrades on graph modification tasks; their performance is particularly low as the number of modifications increases, and when the adjacency matrix is used to represent the graph --- an essential encoding not explored in previous work. We provide new techniques for improving performance on graph modification tasks, and we introduce Modify and Print (MAP) prompting, which asks models to output the intermediate adjacency matrices at each step, and which markedly improves the models' performance. Our findings highlight a critical gap in current LLM capabilities regarding dynamic graph reasoning tasks and underscore the potential of techniques like MAP prompting to mitigate these challenges.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper explores the capability of LLMs in handling graph modification tasks, which involve adding or deleting nodes or edges and computing properties on the modified graph. It introduces GraphModQA, a benchmark dataset with question-answer pairs aimed at testing LLMs’ skills in graph manipulation and dynamic reasoning. The authors find that while current state-of-the-art LLMs handle static graph tasks well, their performance drops significantly with graph modifications, especially when using adjacency matrix representations. To address this, the authors propose Modify and Print prompting, a method where models output intermediate adjacency matrices, leading to improved performance.

### Strengths
- Clear write-up, which is easy to follow and get the core idea for readers.
- The proposed GraphModQA may serve as one of the important benchmarks for LLMs solving graph problems.

### Weaknesses
 - Presentation. The experiment part in the main papers lacks clear tables to show how different LLMs perform on the GraphModQA benchmark. The authors put a lot of large figures here, but they are less informative and are consuming too much of the space. Especially, the presentation makes the experiment part very difficult to follow and grasp the key findings.
- Lack of detailed presentation and showcasing of the proposed benchmark. After reading the paper, I still have no idea how many questions are there in GraphModQA in total, and what the forms of these questions are.
- The motivation of leveraging LLMs for graph modification remains unclear and confusing. Generally the task is trivial and you can swiftly and smoothly add some nodes or edges to the graph, by simply accessing to tools like PyG or NetworkX. Even if we would like LLMs to acquire such skill, it is more reasonable that if we directly add such feature in a tool-use style, especially for a trivial task, which can be done by a single function call.
- The proposed MAP method centers around CoT prompting for the certain task, and is considered less novel.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

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
This paper presents an innovative investigation into LLMs' capabilities in graph modification tasks. The authors introduce GraphModQA, a novel benchmark dataset designed to evaluate LLMs' ability to manipulate graphs through operations like adding/removing nodes and edges. Through comprehensive experiments with modern LLMs including GPT-4o-mini, Llama 3.1 405B, Claude 3.5 Sonnet, and o1-mini, they demonstrate that while these models excel at static graph property tasks, they struggle with dynamic graph modifications, particularly when using adjacency matrix representations. The work introduces a new prompting technique called Modify and Print (MAP) prompting, which shows promising improvements in model performance by requiring explicit output of intermediate graph states.

### Strengths
This manuscript demonstrates several notable strengths that warrant recognition in the field of LLM research and graph manipulation. The introduction of GraphModQA represents a significant advancement in benchmarking LLM capabilities, particularly through its novel focus on dynamic graph modifications rather than merely static property assessment. The authors have thoughtfully designed their experimental framework, incorporating various graph encoding methods and paying special attention to the previously unexplored adjacency matrix representation. The proposed Modify and Print (MAP) prompting technique shows genuine innovation in addressing the challenges of graph modification tasks, with empirical results demonstrating measurable improvements across different model architectures. Furthermore, the comprehensive evaluation across multiple state-of-the-art models (GPT-4o-mini, Llama 3.1 405B, Claude 3.5 Sonnet, and o1-mini) provides valuable insights into the relative capabilities of different architectures in handling structured data modifications. The authors' systematic approach to testing different modification types (Add Edge, Remove Edge, Add Node, Remove Node, and Mix) offers a thorough exploration of model behaviors under various graph transformation scenarios, while their detailed analysis of performance degradation patterns provides actionable insights for future research directions in improving LLM capabilities for graph manipulation tasks.

### Weaknesses
1) The authors claim that modern LLMs "excel at basic graph primitives" but don't provide sufficient empirical evidence comparing performance across model generations.
2) The motivation for choosing graph modification as a benchmark task lacks rigorous justification. While intuitively sensible, there's no formal analysis of why this specifically tests model capabilities better than existing benchmarks.
3) The modification sequence function m(M,k) needs stronger theoretical grounding. The selection of modification types appears arbitrary without formal justification of their completeness or representativeness.
4) The analysis of prompt consistency lacks statistical validation. The authors need to include confidence intervals and significance tests for their performance claims.
5) The experimental setup for comparing different prompting strategies has several problems: No ablation studies to isolate the impact of different components; Missing justification for the choice of 250 graphs; Lack of error analysis on failure cases.
6) The hyperparameter selection process for MAP prompting isn't documented. Critical details about implementation choices are missing.
7) The model selection criteria need better documentation, particularly regarding architecture choices.
8) its presentation suffers from severe readability issues that significantly undermine its potential impact. The visual presentation is particularly problematic - all figures suffer from inadequate formatting, with Figure 2's experimental results being especially difficult to interpret due to its cluttered layout, minuscule font sizes, and insufficient caption detail.

### Questions
1) Can you provide statistical significance tests for the performance improvements claimed with MAP prompting?
2) For Section 5.2: How does the choice of 250 test graphs impact result reliability? What power analysis was performed?
3) What ablation studies were conducted to verify the individual components' contributions to performance?
4) For Table 1: Why were these specific baselines chosen? How do they compare to other recent graph-focused LLM evaluations?

### Soundness
3

### Presentation
2

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
The paper proposes a graph modification benchmark. The authors set several subtasks for graph modification tasks and evaluated several LLMs. Based on this, the authors also propose a novel MAP algorithm.

### Strengths
The authors propose a new evaluation of graph modification evaluation.

### Weaknesses
The paper is not well organized. What are the input and output of the task? What is the answer format? Does the final answer a graph or some token indicating the added nodes or edges? If the output is the graph itself, how do you build the MAP prompt? Please give some illustrations of your prompt and answer examples.

The experiments lack analysis. For example, why is the remove node dropping while the number of modifications increases while the add node is increasing? Besides, the authors suggest that they imply a CoT prompt, but they have no idea how they do a CoT prompt.

The authors should illustrate how the modified graphs are important for real-world applications or have a connection with other tasks. Otherwise, while lots of LLMs can achieve a very high score, it is not clear what further work we can do on this topic. This part needs further experiments to enhance.

### Questions
See weakness

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new benchmark dataset for graph understanding of LLMs. It contains QA pairs that first ask LLMs to modify graphs (e.g., add nodes or edges and remove nodes or edges), and then ask LLM questions regarding the structural properties of the graph (e.g., number of nodes). The authors also examine the performance of popular LLMs on this benchmark.

### Strengths
1. Using LLM to modify graph structure is a very interesting topic.
2. The proposed dataset is clearly introduced.

### Weaknesses
1. The contribution of the proposed dataset seems incremental. It uses the same graph property questions as in previous datasets but just has an additional step to ask the LLM to add or remove nodes and edges. However, why do we need LLMs to do specific modifications on graphs? Anyone can easily revise the adjacency matrix of a graph to add/remove nodes and edges (usually less than 10 lines of code ). Is there any real-world use case for such "modify and then analyze" graph questions?

2. Given the weak motivation of the proposed datasets, I think they are insufficient to examine the graph understanding ability of LLMs. A very interesting graph modification task for LLMs involves asking them to adjust a graph to achieve specific target properties. For example, using the minimum modifications to let a graph be disconnected or has at least K connected components, or using the minimum modifications to let a graph be isomorphism with another graph. 

3. The authors mentioned many times "dynamic graph" in their paper, but it is still unclear to me which part of their datasets is related to understanding dynamic graphs. It seems the authors regard multi-step modification as a kind of "dynamic graph modification", but this is just related to modification rather than the "dynamic graph reasoning" claimed in the abstract.

4. Much important information is missing, such as the detailed analysis and statistics of the datasets, the prompt they used during experiments, and the hyper-parameter settings.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2
