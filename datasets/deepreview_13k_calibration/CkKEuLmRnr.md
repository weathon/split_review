# How Do Large Language Models Understand Graph Patterns? A Benchmark for Graph Pattern Comprehension

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Benchmarking the capabilities and limitations of large language models (LLMs) in graph-related tasks is becoming an increasingly popular and crucial area of research. Recent studies have shown that LLMs exhibit a preliminary ability to understand graph structures and node features.
However, the potential of LLMs in graph pattern mining remains largely unexplored. This is a key component in fields such as computational chemistry, biology, and social network analysis. To bridge this gap, this work introduces a comprehensive benchmark to assess LLMs' capabilities in graph pattern tasks. We have developed a benchmark that evaluates whether LLMs can understand graph patterns based on either terminological or topological descriptions. Additionally, our benchmark tests the LLMs' capacity to autonomously discover graph patterns from data. The benchmark encompasses both synthetic and real datasets, and a variety of models, with a total of 11 tasks and 7 models. Our experimental framework is designed for easy expansion to accommodate new models and datasets. Our findings reveal that: (1) LLMs have preliminary abilities to understand graph patterns, with O1-mini outperforming in the majority of tasks; (2) Formatting input data to align with the knowledge acquired during pretraining can enhance performance; (3) The strategies employed by LLMs may differ from those used in conventional algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a benchmark that evaluates SOTA LLM graph pattern understanding and whether any graph reasoning is gleaned from pretraining in graph-based tasks. The authors describe three distinct settings for evaluating graph pattern understanding: terminology-based, topology-based, and data-driven. 

The terminology-based evaluation explores whether LLMs can comprehend and reproduce graph patterns from the terminology found in pretraining data. Models are tested by examining their alignment with human understanding of a given pattern and assessing whether LLMs can follow human instructions for pattern-detection.

The topology-based evaluation assesses if LLMs are consistent in their ability to recognize identical patterns in different permutations. Models are evaluated on their ability to perform pattern mapping through isomorphic identification, graph editing, and extracting topology-based patterns.

The last evaluation strategy evaluates LLMs’ ability to independently identify and mine graph patterns within real-world datasets.
The paper evaluates 7 SOTA LLMs on their ability to understand 5 undirected graph patterns and 4 directed graph patterns. The results also include model performances on prompts using adjacency lists and edge lists, which are both popular formats for representing graph in LLM-Graph reasoning.

### Strengths
While the novelty of the overall goal is limited, this work offers the LLM-Graph reasoning community valuable, and seemingly reliable insight into how LLMs are able to manipulate and understand graph patterns. The paper also stands out because of its clear experimental design and extensive set of experimental results, which would yield insight into the growing research community focusing on LLMs applied to graph reasoning.

### Weaknesses
While the paper is generally well-organized and well-written, the paper suffers from a lack of space. It becomes difficult to parse, given the breadth of experimental results, some of which are not followed by fully satisfactory analyses. There are a total of 9 tasks, each with their own table or figure. Furthermore, several tables include both adjacency list and edge list results, which makes tables very difficult to read. I would suggest splitting the results into separate tables or even moving the lesser results to the appendix, as the impact prompt format is not a central result. 

The analysis of each set of experiments is often quite short and focuses mainly on the performance of o1 or generalizes to all LLMs. While it is important to discuss the best performing model, the paper offers little insights into the types of mistakes being made by underperforming models. For instance, section 4.2 simply states that the decreased average performance (as compared to the terminology-based results discussed in 3.2) were “likely due to increased hallucinations”. Is this backed by the experimental results? 

Section 4.1 provides an example of the type of analysis the other results analysis sections would benefit from. I also think the paper would benefit from providing a bird’s-eye view of how each model performs across all tasks. This would provide insight into the relative strengths and weaknesses of each model, which are currently difficult to glean.

Minor Issues:
- The paper mentions that LLMs tend to add extra edges to patterns such as T-triangle and V-S, leading to unintended structures. It would be helpful to clarify whether these extra edges result in completely disconnected structures or simply unintended modifications.

- The paper asserts that the adjacency list format is better suited for LLMs, which does seem to be the case for o1; however, the results for other models (e.g., pattern isomorphic mapping) do not seem to be as conclusive. A short analysis of these results would be helpful to the community when deciding which format to use for a given model in future experiments.

- The exclusion of 'large' graph sizes results in many figures limits the reliability of those figures.

### Questions
- Has analysis of the errors of each model been done? If so, is it possible to include these analyses in the appendix?
- Could you clarify whether the extra edges added by LLMs in the T-triangle and V-S patterns result in completely disconnected structures or merely unintended modifications?
- What was the reasoning behind not analyzing the impact of parameter size on model performance? This information could provide valuable insights, especially given that certain models outperformed others.
- Could you expand on the analysis of the input prompt formats?
- Can you separate the EL and AL results into separate tables in the final version of the paper? If space constraints prevent both from being included in the main text, I suggest moving the weaker result to the appendix with the results from the above question.
- Was the exclusion of 'large' graphs in many figures done for the purpose of interpretability? If so, please include versions with the full or just the large results in the appendix.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper uses 11 experiments to evaluate the abilities of 7 state-of-the-art (SOTA) LLMs to understand graph patterns from synthetic and real data, as well as their abilities to discover these patterns from data. The authors vary the description of these patterns (terminology-based vs topology-based) in order to observe the impact on performance. The authors claim that models may employ strategies different to strategies found in traditional algorithms to solve tasks, and that models tend to perform better when the input description of the pattern follows a terminology-based description rather than a topological-based description.

### Strengths
- The paper is well motivated relative to prior work. This work introduces several key graph pattern tasks, and effectively highlights the potential applications of these tasks.
- The experimentation done in the paper are very comprehensive. The authors evaluate a large set of SOTA LLMs on a large breadth of experiments, including both synthetic and real datasets. This breadth in experimentation effectively showcase the current abilities of SOTA LLMs on graph pattern understanding and discovery.

### Weaknesses
=== Lack of In-Context Learning === 
- All experiments in the paper are done in a zero-shot setting. Demonstrating the impact of in-context learning, such as CoT prompting, on a subset of the experiments would improve the contribution of the paper.

=== Lack of Clarity in Writing ===
- Section 3.3 lacks clarity on the underlying data. The authors mention that in this task, the LLM takes in an input graph, and is instructed to “detect specific primitive graph patterns” within the input graph. Does every input graph have a graph pattern inside it, or do some input graphs have no graph pattern?
- Following from the above point, in Section 4.1 the authors “reuse the graph datasets in the terminology-based pattern detection task” in order to test the models’ abilities to map between isomorphic graphs. If some of these graphs do not have a graph pattern, then isn’t this experiment testing graph isomorphic mapping and not pattern isomorphic mapping? What is the explicit relevance of this section with respect to graph patterns?
- Sections 5.2, 5.3, and 7.2 are poorly written. In Section 5.2, it is unclear what the accuracies in Table 7 represent and how they differ from the accuracies in Figure 5. It is unclear as to what either are reporting. In Section 5.3, the structure of the experiment is difficult to follow. For both Section 5.2’s and 5.3’s experiment, including an algorithmic description or pseudocode for the experiment would also greatly improve clarity. In Section 7.2 where the authors first discuss the strategies LLMs use, for each task, it would be effective to state what strategies traditional algorithms actually use, and then compare these to the strategies used by LLMs. Also, the second point in this first paragraph states that “the adjacency list is often better than the edge list in experiments”, but it is unclear as to what relevance this has on the central claim of this paragraph. When the authors discuss the impact of input format on performance, they mention that “terminology-based graph pattern detection is usually better than topology-based ones”, but then soon afterwards repeat themselves by mentioning that the “terminology-based description is often better than topology-based”. It is also unclear what this point, as well as the later point that “the adjacency list input is better than the edge list input”, have to do with the pretrained knowledge of the LLMs.

=== Unsubstantiated Claims===
- In Section 3.2, the author state that “the scale of the input graphs generally doesn’t have a major impact...because LLMs generally prioritize high-degree nodes and their neighbors to form the pattern. In larger graphs, LLMs tend to identify more regions for potential edits.” It would be helpful for the authors to empirically validate that the LLMs are in fact prioritizing high-degree nodes when forming the pattern, as this would provide evidence to substantiate this claim.

### Questions
- In Section 3.1, how can DIV be more than 0 if the temperature of all models is set to 0?
- In Section 3.3, does every input graph have a graph pattern inside it, or do some input graphs have no graph pattern?
- In Section 6, how does the “Both” description look like? How do the “alkane groups and fluoride groups” target patterns look like?

### Soundness
3

### Presentation
3

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
Summary:
The author proposed a new benchmark evaluates LLMs in graph pattern recognition. While LLMs show early abilities in understanding graph structures, their potential in pattern mining is under-explored. This benchmark, covering 11 tasks and 7 models, tests LLMs' capacity to recognize and discover patterns in synthetic and real data. Key findings show O1-mini outperforms in most tasks, aligning data formatting with pretrained knowledge enhances performance, and LLMs use unique strategies distinct from traditional algorithms.

### Strengths
Pros: 
- The paper provide benchmark for evaluating LLMs’ ability in understanding graph patterns.
- Analysis has been conducted based on the proposed benchmark. Multiple research questions have been studied.

### Weaknesses
Cons:
- It would be great if o1-preview result can also be included, if feasible.
- In molecular graphs, how is the molecule features being provided to the LLMs? I am curious about how the molecular graph is being converted to textual format and feed into the LLMs.  More details are encouraged to be included. If edge lists is utilized, then example of the edge list representing molecules are encouraged to be shown.
- For the question, Can LLMs automatically discover graph patterns in real-world applications? A work using LLMs to find patterns in molecular data is encourage to be mentioned. The work has tried to use LLMs to identify key functional groups in molecular data for diverse molecular property prediction tasks[1].


[1] Zheng, Y., Koh, H. Y., Ju, J., Nguyen, A. T., May, L. T., Webb, G. I., & Pan, S. (2023). Large language models for scientific synthesis, inference and explanation. arXiv preprint arXiv:2310.07984.

### Questions
Same as Cons

### Soundness
3

### Presentation
3

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
The paper avaluates large language models (LLMs) on graph pattern comprehension. It explores three types of descriptions: terminology-based, topology-based, and data-drive and evaluates model performance across synthetic and real-world datasets. The study highlights LLMs' limitations and potential for recognizing graph patterns, especially with the inclusion of recent models like O1-mini.

### Strengths
1. The paper includes O1, a very recent model specifically designed for reasoning, highlighting its capabilities and limitations for graph tasks and revealing that there is still room for improvement in how LLMs handle graphs.
2. The paper is well-written, with good clarity and well-organized explanations, making it accessible for readers. The consideration of multiple input formats serves as a useful starting point for anyone new to the field of graph tasks using LLMs.
3. The range of tasks, spanning both synthetic and real-world datasets, provides a comprehensive evaluation of LLM performance on graph-related tasks.

### Weaknesses
1. Lack of Novelty:
The paper’s findings align with existing research, notably with studies like [1], which already demonstrate that LLMs have limited graph understanding. Although the inclusion of O1 is new and valuable, most results are expected and reflect known limitations of other LLMs in graph comprehension. The paper does not sufficiently differentiate its contributions from established findings, particularly in the context of graph representation learning and reasoning.

2. Predictable Results:
The finding that “formatting input data to align with pretraining knowledge can enhance performance” is elementary and expected in LLM research. This does not offer a significant new insight and detracts from the paper's contribution. The paper fails to explore more nuanced aspects of how specific input formats interact with different LLM architectures and pre-training objectives, thus missing an opportunity for deeper analysis.

3. Limitations of Terminology-Based Approaches:
While terminology-based descriptions can be effective for small, simple graphs, they become impractical for larger, denser graphs with multiple cycles, squares, and complex structures. The approach lacks scalability, which is a significant drawback in the context of graph pattern tasks. The paper does not adequately address the limitations of terminology-based approaches in handling graphs with varying degrees of complexity, and lacks a clear strategy for transitioning to more scalable methods.

4. Overlap with Existing Work:
Prior studies, such as [2] have already evaluated multiple topology-based prompts across diverse tasks, revealing similar findings. This paper’s contribution is limited since it doesn’t introduce substantial new insights beyond these previous efforts. The paper does not provide a detailed comparison with existing work on topology-based prompts, failing to highlight unique aspects of its approach or findings.

### Questions
1. In Section 3.1, what is the temperature used for evaluating diversity? Would increasing the temperature lead to more diversity?
2. In Section 5.1, the paper mentions that “LLMs tend to make errors when node degrees are close to 3.” Could the authors clarify why this happens?
3. In Section 6, is the test set complete, or is only a subset used for testing? Section C.3 does not clearly clarify this.
4. In the data-driven approach, what is the input format? Are these images?
5. Would fine-tuning be a feasible strategy to improve accuracy for real-world graph tasks?

### Soundness
3

### Presentation
4

### Contribution
1
