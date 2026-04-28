# Tree-of-Table: Unleashing the Power of LLMs for Enhanced Large-Scale Table Understanding

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
The ubiquity and value of tables as semi-structured data across various domains necessitate advanced methods for understanding their complexity and vast amounts of information. Despite the impressive capabilities of large language models (LLMs) in advancing the natural language understanding frontier, their application to large-scale tabular data presents significant challenges, specifically regarding table size and complex intricate relationships. Existing works have shown promise with small-scale tables but often flounder when tasked with the complex reasoning required by larger, interconnected tables found in real-world scenarios. To address this gap, we introduce "Tree-of-Table", a novel approach designed to enhance LLMs' reasoning capabilities over large and complex tables. Our method employs Table Condensation and Decomposition to distill and reorganize relevant data into a manageable format, followed by the construction of a hierarchical Table-Tree that facilitates tree-structured reasoning. Through a meticulous Table-Tree Execution process, we systematically unravel the tree-structured reasoning chain to derive the solutions. Experiments across diverse datasets, including WikiTQ, TableFact, FeTaQA, and BIRD, demonstrate that Tree-of-Table sets a new benchmark with superior performance, showcasing remarkable efficiency and generalization capabilities in large-scale table reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a tree-of-table method, which generates the tree thoughts to improve the LLMs' reasoning ability on large-size tables. The experiments are conducted on multiple datasets such as WikiTQ, TableFact, FeTaQA and BIRD and show the better performance than baselines.

### Strengths
1. The experimental results show the proposed tree-of-table method leads to better performance than baselines.
2. The experiments are conducted on multiple table-based datasets and show the effectiveness of the proposed method.

### Weaknesses
1. Deriving such a huge tree for table QA can raise the efficiency concern. 
2. It would be better to show some cases in which tree-of-table can handle better than chain-of-table.

### Questions
1. What types of queries and tables can mainly benefit from tree-of-table rather than chain-of-table?
2. How easy will it go into a dead loop during the derivation of the trees?

### Soundness
3

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
4

### Summary
This paper introduces "Tree-of-Table" to enhance LLMs' ability to understand and reason with large-scale tabular data. Key contributions include a framework with table condensation that distills relevant information from large tables, table-tree construction, which organizes reasoning steps into a hierarchical tree structure, and then table-tree execution which systematically processes the tree through DFS. The structure breaks down complex table understanding tasks into manageable sub-problems to allow more efficient processing compared to linear chain approaches. Their experiments demonstrated enhanced performance over existing methods on large-scale tables across multiple datasets including wikiTQ, TableFact, FeTaQA, and BIRD.

### Strengths
This paper introduced a tree structure for handling tabular data which is different from the traditional linear chain-of-thought and more recent chain-of-table methods. What I like in particular is how they combined table condensation with tree decomposition - the authors seem to have thought carefully about how humans break down complex problems, and they've used the insights and built this into their approach. The experimental work is solid. They tested their method on several different datasets (WikiTQ, TableFact, FeTaQA, and BIRD), which gives us confidence in the results. The numbers are impressive - they're getting better performance than existing methods, especially on BIRD which has those really large tables that are typically hard to handle. I was particularly convinced by their ablation studies.

The paper is easy to follow. The figures really help explain what's going on - Figure 1 does a great job showing how their approach differs from previous methods. They've managed to explain some pretty complex technical stuff without making it too dense. That said, they could have made some of the implementation details clearer. In terms of impact, this work matters because large-scale table understanding is a real problem that comes up all the time in practical applications. Their method shows promise for handling tables in finance, healthcare, and other fields where you often deal with complex tabular data. The performance improvements they're showing are consistent across different LLMs, and across various table understanding datasets. What stands out most to me is that they've taken a practical problem (with demonstrated efficiency improvement against other methods) that lots of people struggle with and come up with a solution that actually works better than what we had before. The evidence is there in their results, and they've explained their approach well enough that others could build on it.

### Weaknesses
1. The theoretical foundation needs more work. While the tree-based approach shows good empirical results, there's limited analysis of why it works better than linear chains. 

2. Some key experimental details are missing or unclear: They don't specify how they chose parameters like MAXDegree and MAXDepth for the Table-Tree. These seem pretty important for the method's performance. Alsothe computational overhead of building and traversing the tree structure wasn't properly analyzed, for example - memory requirements for storing intermediate results at tree nodes and overall computational complexity compared to simpler approaches

3. The ablation studies could go deeper. There's no clear analysis of how the tree structure's depth affects accuracy. The comparison with Chain-of-Table focuses mainly on final accuracy, but doesn't explore cases where their method might perform worse

### Questions
1. The authors should explain the theoretical advantages of their hierarchical decomposition - when does it work better and why? This would help us understand the method's limitations and where it might fail.
2. There's no discussion of error propagation through the tree structure. In a tree structure, errors at higher levels will propagate down through all child nodes. For example, if the table condensation step (at the root) removes important information, or if an early operation in the tree is incorrect, how does this affect the final result? The paper shows good overall accuracy but doesn't analyze these failure cases.
3. Related to above, how sensitive is your method to the quality of the initial table condensation step? What happens if crucial information is accidentally filtered out?
4. What is the complete set of operations in the operation pool? How were these operations selected and validated?
5. Have you analyzed cases where Tree-of-Table performs worse than Chain-of-Table? This would be valuable for understanding the method's limitations.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the "Tree-of-Table" method, designed to improve the reasoning abilities of large language models (LLMs) when dealing with large and complex tabular data. The approach involves two main steps: Table Condensation and Decomposition, which simplifies and organizes the data, and Hierarchical Table-Tree Construction, creating a structured representation that benefits systematic reasoning. This method enhances the efficiency and generalization capabilities of LLMs, demonstrated through superior performance on datasets like WikiTQ, TableFact, FeTaQA, and BIRD. This study advances LLM methods for parsing and understanding extensive tabular datasets, setting new benchmarks in handling complex table-based information.

### Strengths
* The idea of using tree as a roadmap to guide the LLMs through table(s) is sound but seems like an adaptation from other work to table tasks. It's not very novel to consider increment LLMs using chain-of-thoughts to tree-of-thoughts, which have been already verified on other domains, like graphs.

### Weaknesses
W: I'm unclear about the logic in the introduction from lines 94 to 103, specifically why the Chain-of-table is limited to smaller tables. What does 'smaller' refer to exactly? Is it generally about the number of rows/columns or the total number of tokens across all cells?

W: The performance of the proposed tree-of-table is limited, especially compared with the chain-of-table referred to in Table 1 and 2. Additionally, it's not very easy to differentiate the contribution of tree-of-table and chain-of-table. The authors should consider providing a critical analysis about the difference in the introduction or method section, and show how this improvement can account for the performance enhancement.

Several relevant papers should be considered in references:

* Large Language Models are few(1)-shot Table Reasoners
* StructGPT: A General Framework for Large Language Model to Reason over Structured Data
* TAP4LLM: Table Provider on Sampling, Augmenting, and Packing Semi-structured Data for Large Language Model Reasoning
* Table Meets LLM: Can Large Language Models Understand Structured Table Data? A Benchmark and Empirical Study
* TableRAG: Million-Token Table Understanding with Language Models

### Questions
Q1: I'm unclear about the logic in the introduction from lines 94 to 103, specifically why the Chain-of-table is limited to smaller tables. What does 'smaller' refer to exactly? Is it generally about the number of rows/columns or the total number of tokens across all cells or like a database: the number of tables linked with keys?

Q2: what is the OP pool mentioned in Figure 1? I suggest the authors to rephrase the process of chain-of-table in case not all readers are familiar with this method. Additionally, the authors should also describe the difference between chain-of-table and proposed tree-of-table explicitly.

### Soundness
3

### Presentation
3

### Contribution
2
