# $EFO_{k}$-CQA: Towards Knowledge Graph Complex Query Answering beyond Set Operation

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
To answer complex queries on knowledge graphs, logical reasoning over incomplete knowledge is required due to the open-world assumption. Learning-based methods are essential because they are capable of generalizing over unobserved knowledge. Therefore, an appropriate dataset is fundamental to both obtaining and evaluating such methods under this paradigm. In this paper, we propose a comprehensive framework for data generation, model training, and method evaluation that covers the combinatorial space of Existential First-order Queries with multiple variables ($\efok$). The combinatorial query space in our framework significantly extends those defined by set operations in the existing literature. Additionally, we construct a dataset, $\efok$-CQA, with 741  types of query for empirical evaluation, and our benchmark results provide new insights into how query hardness affects the results. Furthermore, we demonstrate that the existing dataset construction process is systematically biased that hinders the appropriate development of query-answering methods, highlighting the importance of our work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a comprehensive framework for generating data, training models, and evaluating methods for complex query answering on knowledge graphs. The authors introduce the EFO k-CQA dataset, which captures a significantly broader combinatorial space of existential first-order queries compared to previous datasets. They demonstrate the limitations of existing datasets and benchmarks, and present new evaluation metrics tailored to queries with multiple free variables. The experiments on six representative CQA models provide new insights into query hardness and model performance.

### Strengths
1. The authors formulate a new class of queries, EFO k, that extends previous definitions and captures more complex query structures. This expands the scope of complex query answering on knowledge graphs.
2. The proposed framework is rigorously defined, and the dataset generation process is carefully designed to ensure non-trivial queries. The code and data are made publicly available.

### Weaknesses
1. The paper is more appropriate for the audience of a database or database theory conference rather than for ICLR.
2. The dataset is entirely synthetically created and lacks application in the real world.
3. No clear trend or conclusion can be seen from Table 2. There is no clear relation between the number of existential variables and the evaluation types.
4. The basic KG is incomplete. It will propagate errors as the query structure becomes more complex. Moreover, there is no method to guarantee the quality of the generated training and testing sets.

### Questions
Why should we scale the dataset if there are no real-world use cases.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Existing benchmarks for complex query answering for KGs do only consider specific (tree-shaped) queries. This is not sufficient to evaluate methods thoroughly.
The current work suggests new datasets which have 1) multiple variables and 2) removal of many trivial query shapes.

### Strengths
* Tying this domain to CSP is helpful because that way we can reuse insights.
* Section 2.1 and 2.2 propose a good approach to reduce the number of query shapes to those that are non-trivial. This is an important consideration.
* A reasonable choice has been made on what to put in the appendix. For readers, parts might be considered essential for the understanding of the paper, though, especially what is in appendix D.1. and the explanation of the joint metric.

### Weaknesses
 * The main difference between this and the work by Yin 2024, appears to be that multiple variables are allowed. This is a small difference, and also pointed out in the cited survey by Hongyu et al (Neural Graph Reasoning), so not really new. that survey also has a more general notion of graph queries, also for different graph types.
* The authors do not provide any insights in the limitations of what they propose. 

Minor:

* There are some inconsistencies in the math notation and symbols used in the paper. 
* In section 1, there are some grammar mistakes, mainly concerning the use of articles and plurals which make the text hard to read.

### Questions
* Could you elaborate in assumption 13 and 14? Why are they necessary? 
* Assumption 16 is quite questionable. I am aware of the earlier work doing this, but also there it was not appropriately justified. Is there any foundational reason this assumption is needed?
* I am confused about the benefit of including the marginal metric. As you correctly indicate, it is flawed when dealing with multiple free variables. What is the benefit of still including it?
 * I wonder how a method like mpqe would work on your dataset. It naturally obtains representations for all variables of the query.
* For the results of CQD, did you use the calibrated version $CQD^A$, or the original one? The calibrated one should be much more robust when computing on different query shapes.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces $EFO_{k}-CQA$, a framework for generating datasets and evaluating models on complex query answering (CQA) tasks over knowledge graphs (KGs). Unlike previous datasets limited to set operations and tree-based structures, EFOk-CQA supports the broader family of Existential First-Order (EFO) queries, extending to multiple variables and complex graph structures. The authors propose an end-to-end pipeline to generate EFO queries, sample answers, train models, and evaluate performance. The dataset is shown to cover 741 query types, aiming to capture a wide combinatorial space of queries. Through extensive experiments, the paper highlights structural biases in existing datasets and evaluates six prominent CQA models, revealing the influence of query hardness and graph topology on model performance.

### Strengths
1. The EFOk-CQA framework is a meaningful extension to existing CQA benchmarks, expanding beyond single-variable, set operation-based queries to include multiple-variable and complex query graphs. It also addresses a notable gap in CQA evaluation, offering a comprehensive benchmark that reflects real-world query complexity.
2.  The paper demonstrates a high degree of rigor in constructing the EFOk-CQA dataset. The authors establish well-defined assumptions to exclude trivial cases, implement a pipeline for end-to-end evaluation, and provide empirical results with various CQA models across a comprehensive range of query structures and complexities.
3. The paper is well-organized, with clear definitions and illustrations that help in understanding complex query structures. Concepts such as query graphs, grounding processes, and evaluation metrics are presented with detailed explanations and visual aids, facilitating comprehension.
4. The EFOk-CQA dataset and framework have implications for advancing CQA research. By covering a broader range of query types, the benchmark could lead to the development of more generalized and capable CQA models. The analysis of model performance based on query topology and difficulty also provides useful insights for future CQA model improvements.

### Weaknesses
1. In section 3.1, while the framework supports complex queries, the combinatorial space of queries could grow exponentially as query parameters increase. This might make it challenging to scale up the dataset generation process efficiently or to apply the framework to larger, more complex knowledge graphs. Specifically, the paper does not address the computational cost associated with generating queries with a higher number of existential variables or more complex graph structures, which could become a bottleneck in practical applications.
2.  The use of joint metrics to evaluate models with multiple free variables is valuable, but it is noted in the paper that joint rankings could lack reliability due to inherent difficulty. This limitation could affect the robustness of evaluation for complex queries, particularly when interpreting the rankings for CQA tasks. The paper does not provide a detailed analysis of why these joint rankings are unreliable, nor does it offer alternative evaluation strategies to mitigate this issue.


### Questions
1. Given the vast combinatorial space, how scalable is the framework for generating queries with more complex conditions or additional free variables? Are there specific trade-offs in terms of time or computational resources that become prohibitive?
2.  How often do the assumptions used to generate non-trivial query graphs (e.g., no decomposition) align with real-world query requirements? Would relaxing these assumptions reveal additional complexities or insights about query-answering models?
3.  Can the authors provide an error analysis highlighting specific failure modes of the evaluated models? For example, are there certain query types (e.g., cyclic vs. acyclic) where models consistently underperform? This information could clarify which specific capabilities of current SOTA works require improvement.

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
The paper proposes a benchmarking framework for complex query answering, specifically targeting existential first-order (EFO) queries with k independent variables. The paper proposes a new dataset, EFOk-CQA, comprising 741 diverse query graphs.

### Strengths
- The paper defines a new framework for CQA that extends existential first order logic with single variable (EFO1) to existential first order logic with k independent variable (EFOk).
- The paper defines three new metrics for evaluating EFOk queries.
- The paper constructs new datasets of query-answer pairs from 741 different abstract query graphs. The queries are based on FB15k-237, FB15k, and NELL.
- Overall, the originality, quality, clarity, and significance of the paper is good.

### Weaknesses
 - Unusual structure of the paper: no section with title "introduction", related work in appendix, main section of the paper (Section 3) only gives a rough overview with important details in the appendix.
- Presentation could be improved (some spelling and grammar issues)

Details
-------
- "KGs suffer from incompleteness during its construction" --> their construction (plural)
- Figure 1, typo: presdient --> president
- Figure 1, right: Born(y_1, x_1) appears twice. Should the second one be co-author?
- Appendix C: "projections(Definition" space before parenthesis missing
- Proposition 20: "it can not only" --> cannot
- Section G: Knowledge graph with attributes: Two recent works are missing: NRN and LitCQD

### Questions
- Can you strengthen the motivation for the new query types (EFOk)? For example, can you provide additional real-world examples? Or statistics of real-world query logs? The paper claims that fraud detection would benefit from the proposed approach (Appendix "society impact"). However, no references or concrete examples are given.
- What was the runtime to compute the results in Tables 1 and 2?

### Soundness
3

### Presentation
2

### Contribution
3
