# Structured Graph Reduction for Efficient GNN

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Scalability remains a prominent challenge for Graph Neural Networks (GNNs) when dealing with large-scale graph data. Graph coarsening is a technique that reduces a large graph to a smaller tractable graph. A good quality graph representation with specific properties is needed to achieve good performance with downstream applications.
However, existing coarsening methods could not coarsen graphs with desirable properties, such as sparsity, scale-free characteristics, bipartite structure, or multi-component structure. This work introduces a unified optimization framework for learning coarsened graphs with desirable structures and properties. The proposed frameworks are solved efficiently by leveraging block majorization-minimization, 
 $\log$ determinant, structured regularization, and spectral regularization frameworks. Extensive experiments with real benchmark datasets elucidate the proposed framework’s efficacy in preserving the structure in coarsened graphs. Empirically, when there is no prior knowledge available regarding the graph's structure, constructing a multicomponent coarsened graph consistently demonstrates superior performance compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on graph coarsening to reduce a large graph to a smaller tractable graph effectively. A unified optimization framework is introduced in the paper for learning coarsened graphs with desirable structures and properties. The approaches to efficiently solving the proposed framework are further presented in the paper. Extensive experiments are also conducted on various real benchmark datasets to validate the effectiveness of the proposed framework.

### Strengths
S1. Graph coarsening is an important problem in reducing a large graph to a smaller tractable graph effectively. 

S2. The paper proposes a unified optimization framework for learning coarsened graphs with desirable structures and properties, including sparse graphs, scale-free graphs, multi-component graphs, and bipartite graphs. 

S3. Experimental results show that the proposed method outperforms the state-of-the-art graph coarsening methods in terms of node classification accuracy.

### Weaknesses
W1. The benchmark datasets are all relatively small. Considering that the primary aim of graph coarsening techniques is to downsize large-scale graphs, validating the model's performance on larger datasets would lend more credibility to the results.

W2. Some experimental results require further clarification. For instance:

- In Table 7, the time required for coarsening and node classification using the proposed methods is not significantly less than that needed for node classification using the original graph. In the worst case (e.g., the BI-GC model on the CORA dataset), the time cost for the former even exceeds the latter. However, graph coarsening techniques are designed to reduce large-scale original graphs and enhance the scalability of existing GNN models. These empirical results seem to contradict the core motivations behind graph coarsening, necessitating further clarification.

- In Tables 1, 2, and 3 provided in the supplementary material, it would be beneficial to include node classification results using the original graph for comparison.

W3. The paper's presentation needs improvements. The literature review part is too short and not very informative. Moreover, the manuscript contains some sentences that are unclear and could lead to ambiguity. For instance:

- The last paragraph of Section 1 is somewhat vague and needs further clarification. While the authors emphasize the significance of adopting the multiple-component method in graph coarsening, the main contribution of this paper is the introduction of a generalized optimization framework that supports four kinds of graph structures simultaneously. The reasons for focusing on the other three structures – sparse graphs, scale-free graphs, and bipartite graphs – merit further explanation.

- Page 2: $C^T$ -> $C^\top$

- Page 3: Where $gdet(\Theta_c)$ denotes -> where $gdet(\Theta_c)$ denotes

- Table 3: Wh.da. -> Whole dataset

### Questions
Q1. It is noteworthy that most scale-free graphs also fall into the category of sparse graphs. Could the authors elaborate on the rationale behind discussing these two types of graphs separately?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a unified optimization-based framework for graph coarsening, addressing the computational challenges of processing large-scale graph data. Previous methods cannot coarsen graphs while preserving desired properties like sparsity, scale-free, bipartite, and multi-component structures. This submission introduces a unified solution leveraging block majorization-minimization and spectral regularization to enforce these structures during the coarsening process efficiently. The proposed method is validated through experiments on some graph benchmark datasets, demonstrating its effectiveness in preserving structural integrity in coarsened graphs. This approach also reveals a robustness that can simplify graph analysis and uncover meaningful insights, highlighting its potential for real-world applications.

### Strengths
1. The paper introduces a unified optimization-based framework for graph coarsening that efficiently preserves desirable properties such as sparsity, scale-free, bipartite, and multi-component structures. This approach is based on a previous study but applies to a broader setting.

2. The framework overcomes the limitations of existing methods, which often fail to maintain these properties during coarsening, potentially enhancing the performance of downstream graph-based machine learning tasks.

3. The framework's effectiveness is empirically validated through extensive experiments on real-world benchmark datasets. It demonstrates improved accuracy and efficiency in node classification tasks across various Graph Neural Network (GNN) architectures, setting a new standard for graph coarsening techniques.

### Weaknesses
There are several crucial issues:

1. The authors have delineated their contributions within the domain of graph coarsening; however, there's a need for greater specificity and clarity, particularly concerning the distinction from prior works like those of Manoj Kumar (JMLR, 2023) and Sandeep Kumar (JMLR, 2020). The authors need to explain what unique aspects of their framework set it apart from these previous studies. Further elaboration is required in Section 2 to clarify how this work advances the field beyond the current state-of-the-art. This clarification will not only strengthen the paper but also assist readers in understanding the novel contributions made by the authors.

2. The time complexity of the proposed framework is quadratic to the size of the graph $O(n^2k)$ where $n$ is the number of nodes. It will be impractical if one wants to apply this technique to large-scale graphs.

3. The experiments were tested on all small graphs. It would be more interesting if very large graphs were used, such as graphs in OGB datasets.

### Questions
Some key questions are:
Here are the refined questions:

1. The reviewer notes that the submission lacks a clear exposition of its novel contributions, especially when contrasted with prior works such as those by Manoj Kumar (JMLR, 2023) and Sandeep Kumar (JMLR, 2020). Could the authors specifically articulate the unique and novel aspects of their approach that advance the state-of-the-art in graph coarsening?

2. While applying convex optimization methods to graph coarsening is theoretically appealing, concerns arise regarding scalability, as time complexity may increase quadratically with the number of nodes. This appears to conflict with the primary objective of graph coarsening, which is to reduce computational load. Can the authors address the apparent contradiction and clarify how their algorithms maintain or improve upon the time complexity compared to existing graph coarsening methods?

3. The datasets employed in validating the proposed technique are relatively small-scale. For a comprehensive evaluation of the proposed method's efficacy, would the authors consider applying their approach to larger-scale graphs where the benefits of coarsening could be more pronounced and the technique's scalability and effectiveness more rigorously assessed?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies graph reduction techniques to speedup GNN training. This paper proposes an optimization framework to get reduced graph, which preserves certain desired structural properties. The reduced graph is then used to train GNN parameters. On several benchmark datasets, the proposed method exhibiting improved performance compared to existing coarsening and condensation methods.

### Strengths
1. The motivation is cleared explained.
2. The experimental results show the advantages of the proposed method.

### Weaknesses
1. The novelty is limited. First, using a graph reduction techniques to speedup GNN training is not new. Second, all the components involved in the coarsening objectives are quite standard, which are widely used for controlling the structures of the solution. Third, the heuristics used to solve the optimization problems are also standard optimization techniques. 
2. The datasets used in the experiments are all small: the largest contains 30k nodes. These datasets can be easily trained using full-batch training. 
3. For the testing accuracy, there is a notable gap between the proposed methods and whole graph training. 
4. In the experiments, the proposed method is compared only against 2 reduction methods. There are numerous coarsening/sparsification/condensation methods, I suggest the authors add more baselines. 
5. There is no analyses on the correlation between downstream task performance and the coarsening objectives values, i.e., whether a better coarsening matrix (in terms of the coarsening objectives) results in better classification accuracy.

### Questions
1. What data splits are used in the experiments?
2. The authors present the sparsity of $\phi$ in the experiments. I am also interested in the sparsity of the results graph. The original graph is sparse and if the reduced graph is dense, then the training cost could be higher than training on the original (sparse) graph.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops an optimization-based framework for structured graph coarsening. The proposed approach coarsens the graph based on some desirable structural properties such as sparsity, scale-free, bipartite, and multi-component. Experiments have been conducted on different real-world data sets on the node classification task.

### Strengths
1) Scalability is an important challenge for GNNs.
2) The optimization procedures seem reasonable.
3) The proposed method is fast.

### Weaknesses
Overall, I think the paper solves an important problem, but is not well written enough for publishing. 
1) Claiming two baselines from 2021 are the recent state-of-art baselines to be compared with seems not convincing. The paper has mentioned a more recent work in Sec. 2.2, Kumar et al. 2023. It is not clear to me why Kumar et al. 2023 is not compared against in the experiments. 
2) Sec. 2 is not well-motivated and not intuitive enough.  For example, why should we use (1)? Why are structural properties such as multi-component and scale-free important in structured graph coarsening? The explanation of the mapping matrix C and its constraints is insufficient. The connection between the sparsity of the \phi matrix and the performance on downstream tasks is not clearly established with theoretical or empirical support. 
3) There are several proposed methods based on different desired coarsened graph properties, but it is not clear which is preferred in what scenarios. Also, why not impose all constraints? The paper lacks a clear discussion on the trade-offs between different structural constraints and their impact on the final performance. It is unclear why imposing all constraints simultaneously would be problematic, especially given the optimization-based nature of the framework. 
4) The experimental results are only between coarsening methods, but it would be better to also compare the performance with the original GNN model without coarsening and show the performance gap. This comparison is crucial to understand the cost of coarsening in terms of performance degradation. 
5) It is not clear what specific GNN is used in Sec. 5. The lack of specificity makes it difficult to reproduce the results or assess the generalizability of the approach. 
6) It is not explained why the baselines instead of the proposed methods are boldfaced in the header of Table 7. This formatting choice is confusing and misleading. 
7) Typos exist. For example,  the first minus sign after equation (11) should instead be an equal sign I guess?

### Questions
1) The paper has mentioned a more recent work in Sec. 2.2, Kumar et al. 2023. Why Kumar et al. 2023 is not compared against in the experiments?
2) In Sec. 2, why should we use (1)? Why are structural properties such as multi-component and scale-free important in structured graph coarsening?
3) Which structural property is preferred in what scenarios? Also, why not impose all constraints?
4) What is the performance gap between the proposed coarsened GNN and the original one?
5) What is the specific GNN used in Sec. 5?
6) Why should the baselines instead of the proposed methods be boldfaced in the header of Table 7?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
