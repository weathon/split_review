# Evaluating and Improving Large Language Models on Graph Computation

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
The ``arms race'' of Large Language Models (LLMs) demands new benchmarks to examine their progresses. In this paper, we introduce GraphArena, a benchmarking tool designed to evaluate LLMs on real-world graph computational problems. It offers a suite of four polynomial-time tasks (e.g., Shortest Distance) and six NP-complete challenges (e.g., Traveling Salesman Problem). GraphArena features a rigorous evaluation framework that classifies LLM outputs as correct, suboptimal (feasible but not optimal), hallucinatory (properly formatted but infeasible), or missing. Evaluation of over 10 LLMs reveals that even top-performing LLMs struggle with larger, more complex graph problems and exhibit hallucination issues. We further explore four potential solutions to address this issue and improve LLMs on graph computation, including chain-of-thought prompting, instruction tuning, code writing, and scaling test-time compute, each demonstrating unique strengths and limitations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces GraphArena, a benchmarking tool designed to evaluate LLMs on graph computation tasks.
It includes ten LLMs with polynomial-time and NP-complete graph problems. The authors claim to go beyond existing benchmarks by including real-world graph structures, introducing path-based evaluation criteria, and testing various improving-performance methods.

### Strengths
1. It includes a diverse set of graph tasks, ranging from simple to complex. It provides a useful evaluation tool for understanding the reasoning capabilities of LLMs on graph problems.
2. It also includes real-world graphs, which can help evaluate the models' performance on practical applications.
3. The paper compares LLMs with traditional graph algorithms, providing insights into the strengths and weaknesses of LLMs in graph computation tasks.

### Weaknesses
1. The analysis is surface-level and lacks in-depth insights into the models' reasoning capabilities. I also have questions about the selected tasks, such as why these specific tasks are chosen and how they represent real-world applications.
2. While the authors position GraphArena as an improvement over previous benchmarks, the degree of novelty in terms of task design and dataset is somewhat unclear. Could the authors provide a more detailed comparison with existing benchmarks?
3. The definition of small/large graphs are different across tasks, which might introduce inconsistencies in the evaluation. It would be helpful to standardize the graph sizes for a fair comparison across tasks.
4. For the evaluation metrics (Feasibility, Hallucination...), there is no clear explanation of how these metrics are calculated. 
5. The authors introduce System 1 and System 2 thinking to describe task complexity, but the connection is weak and lacks follow-through. This framing feels more like an afterthought without a clear motivation and in-depth analysis in the later sections.

### Questions
1. Could you elaborate on how the categories (correct, suboptimal, hallucinatory, missing) are determined in a more complex, multi-step task like the Traveling Salesman Problem? How does the evaluation framework ensure consistent scoring across models?
2. How are the polynomial-time and NP-complete tasks chosen, and do they represent a balanced challenge across diverse graph properties (e.g., density, connectivity)?
3. When using code generation to solve graph problems, how is the correctness of the generated code verified?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
- The paper introduces GraphArena, a LLM benchmark for measuring graph reasoning. 
    - GraphArena is based on real world graphs, including knowledge graphs, social networks, and molecular structures
    - The tasks constructed on these graphs capture a spectrum of different reasoning skills
    - The authors introduce a path-specific evaluation methodology which allows for finegrained measurement of LLM responses
- In addition to describing GraphArea, the paper compares the performance of different LLMs to a broad range of graph-based methods. 
- Finally, the authors explore a range of strategies to improve performance on GraphArea (finetuning, prompting, scaling test time compute).

### Strengths
- I think the benchmark is extremely well constructed. 
    - It is based on realistic data
    - It has a spectrum of difficulty, so different researchers may focus on different subsets of samples/tasks based on the types of models they are studying
    - Similarly, the evaluation protocol applied make sense, and section 2.3 does a good job of motivating it.
- The experiments are rigorous and comprehensive. I think the exploration of methods for improving performance is well-done and rounds out the paper nicely.

### Weaknesses
I don't think the paper has any significant weaknesses. My only quibble is that while the graphs are drawn from the real-world, the questions themselves are not. But I think this is pretty minor, and shouldn't affect what ultimately seems like an interesting paper with a meaningful contribution. If the goal is to measure graph reasoning skills, then I think relying on artificial problems is perfectly acceptable.

### Questions
Are there any performance trends across different graph domains (e.g., DBPedia vs PubChemQC)? I wonder if differences in how graphs are tokenized by the model influence performance.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces GraphArena, a benchmark designed to evaluate large language models (LLMs) on a range of classical polynomial-time and NP-complete graph algorithms. GraphArena consists of four polynomial-time tasks and six NP-complete problems set on real-world graphs sampled from various domains.
GraphArena categorizes LLM responses as correct, suboptimal, hallucinatory, or missing, and ranks overall model performance using mean reciprocal rank (MRR), top-1, and top-3 probability. The authors evaluate over ten LLMs on GraphArena and show that current SOTA models display significant limitations on the included graph reasoning tasks, especially on larger graphs. The study further examines four strategies to improve LLMs' graph reasoning abilities: chain-of-thought prompting, instruction tuning, code generation, and scaling test-time compute. Each approach yields improvements; fine-tuning models yields particularly significant improvements in accuracy, feasibility, and reducing hallucinations on both P and NP tasks for both small and large graphs.
This benchmark highlights the gap between current LLM capabilities and the demands of complex graph reasoning tasks, and contributes insight into the current understanding of LLMs' limitations and potential in graph-based reasoning.

### Strengths
The paper provides several NP-Complete algorithmic reasoning tasks: MCP, MIS, MVC, MCS, GED, and TSP, which are a novel inclusion in the space of benchmarking LLM performance on graph reasoning. The selected P and NP tasks offer a representative sample of graph reasoning operations. The paper does a great job of providing clear experimental results and thorough evaluation of the models on the included tasks. While the study is not the first to evaluate LLMs on real-world graph datasets, there is novelty in evaluating LLMs on complex reasoning tasks on real world graphs, especially with additional textual features.

When considering the lack of breadth available in the peer-reviewed literature of benchmarks evaluating LLM performance on graphs published before July, this work provides novel insights into the SOTA algorithmic reasoning performance.

### Weaknesses
The paper’s main contributions are the inclusion of real-world graphs in its dataset and textual features in both the input and desired output. However, the paper does not clearly justify evaluating LLMs on these particular tasks over those in prior benchmarks exploring LLM graph reasoning. This paper would also benefit from justifying the exclusion of neural algorithmic reasoning literature (both GNN and LLM-based), particularly the recent papers, “Benchmarking ChatGPT on Algorithmic Reasoning” (McLeish et al. 2024) and “The CLRS-Text Algorithmic Reasoning Language Benchmark” (Markeeva et al. 2024).

Claim 3: The tasks in this benchmark seem to be structured as Input-Output (IO) problems. There is limited novelty in showing that fine-tuning improves reasoning improves performance on IO tasks, as shown in “Specializing smaller language models towards multistep reasoning” (Fu et al. 2023) and other prior works. The claim of “improving graph problem-solving” should be reduced unless the authors plan to provide additional experiments with other open-source LLMs that showcase novel findings, or can provide adequate justification for this claim.

Rigorous Path-based Evaluation: The authors mention they contribute a “rigorous, path-based evaluation”, but appear to be performing exact match accuracy and then a partial accuracy metric and integrated error analysis (Missing and Hallucination). These methods are used in “Can Language Models Solve Graph Problems in Natural Language?” (Wang et al. 2023). Multiple prior methods have required models to output a listing or mapping of node IDs as a response to a query, namely “Evaluating Large Language Models on Graphs: Performance Insights and Comparative Analysis” (Liu and Wu 2023), "Can Graph Descriptive Order Affect Solving Graph Problems with LLMs?" (Ge et al. 2024), and Wang et al. 2023 on shortest path queries.

I would be willing to raise my score if the above issues are addressed.

Minor Weaknesses:
- Inclusion of synthetic graph results for the top performing LLMs would strengthen the claim that prior benchmarks fail to adequately stress test LLMs with diverse graphs
- The paper should mention the strong likelihood of the real-world graph datasets being included in the pre-training datasets of many (if not all) of the models being evaluated.
- The paper would benefit from a comparison with other recent works in LLM algorithmic reasoning, for example, Ge et al. 2024, “Transformers meet Neural Algorithmic Reasoners” (Bounsi et al. 2024), “Are Large Language Models Graph Algorithmic Reasoners?” (Taylor et al. 2024), and other recent works in the NAR field in the camera-ready version, as these papers cover a significant breadth of graph algorithmic reasoning tasks and methods for improving LLM algorithmic reasoning.
- Table 2 has several misleading bold results:
  - Lines 439-440: Qwen2-7b should be bolded for feasibility in NP small graphs
  - Lines 441-442: GPT-4o-Coder should be bolded for Polynomial large graphs
  - Lines 443-444: DeepSeek-V2 base should have bold text for accuracy in NP small graphs and feasibility in NP large graphs
- Figure 6 reference links to figure 5 for some reason
- The paper would benefit from providing a centralized list of all models evaluated and their settings, including any hyperparameter tuning

### Questions
- In the appendix, several prompts are shown in which the size of the graph problem presented for CoT reasoning is larger than the query problem. How did you decide on the size of graph problem to use in CoT? Is it standard across all CoT prompts? If it was tuned, please describe the process
- Is there further analysis of the types of errors that LLMs are prone to on this benchmark?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents GraphArena, a benchmarking tool for evaluating LLMs on graph computational problems. GraphArena includes polynomial-time and NP-complete tasks and a detailed evaluation framework. The study tested over ten LLMs on 10,000 problems, finding that models often struggle with complex graphs and exhibit hallucination. It also explores some solutions: chain-of-thought prompting, instruction tuning, code writing, and scaling test-time compute.

### Strengths
S1: It's great to see that GraphArena includes diverse real-life datasets, addressing the limitation of benchmarks that only use synthesized graphs.

S2: The evaluation study is thorough, covering a broad spectrum of LLMs. The techniques proposed to enhance task performance are intriguing, and the results are valuable to the community.

S3: The paper is well-written and easy to read.

### Weaknesses
### Major weaknesses

W1: The discussion and motivation can be improved. This paper presents a useful and sound benchmark and conducts a comprehensive analysis, but the impact of these findings on practitioners and researchers is not clear. I recommend adding a discussion section in / after Section 3.2 to elaborate on the main takeaways of this paper. For example, are the findings in Section 3.2 surprising? How should we interpret the results from Section 3? What should researchers do in the future?

W2: Some experiments are not consistent. For example, SFT is only applied to Llama and Qwen, while coder is only applied to GPT and DeepSeek. Why not conducting all the proposed methods in Section 3.2 on all the models tested in Section 3.1?

W3: While I appreciate the use of real graphs in GraphArena, the connection between the tasks, findings, and these real graphs is weak. I recommend (1) including examples that demonstrate the tasks in GraphArena are relevant to real-world graph tasks and (2) providing a stronger rationale for using LLMs to solve these tasks over traditional graph algorithms.

### Minor weaknesses

M1: The many green boxes in the introduction makes this section hard to read. I recommend disabling the box highlighting or reducing citing redundant papers. For example "(Li et al., 2023c; Jin et al., 2023; Perozzi et al., 2024; Wang et al., 2023; Chen et al., 2024b)." => "(e.g., Li et al., 2023c; Jin et al., 2023; Perozzi et al., 2024)."

M2: Figure 6 comes before Figure 5.

M3: It is rather confusing to have SFT and coder in the same table, while COT and test-time compute in other different figures.

### Questions
Q1: It is unclear how testing LLMs on graph computational problems is a good way to assess reasoning capabilities (L48). How is reasoning capability defined?

Q2: What do "intuitive thinking" and "conscious thinking" mean for an LLM (L64)?

Q3: What are these templates? (L214) Are graphs always encoded as an edge list (figure 1)? Can one use adjacency list or adjacency matrix to represent a graph in text?

### Soundness
3

### Presentation
3

### Contribution
3
