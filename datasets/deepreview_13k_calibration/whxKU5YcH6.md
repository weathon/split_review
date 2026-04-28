# SGOOD: Substructure-enhanced Graph-Level Out-of-Distribution Detection

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Graph-level representation learning is important in a wide range of applications. Existing graph-level models are generally built on i.i.d. assumption for both training and testing graphs. However, in an open world,  models can encounter out-of-distribution (OOD) testing graphs that are from different distributions unknown during training. 
A trustworthy model should be able to detect OOD graphs to avoid unreliable predictions, while producing accurate in-distribution (ID) predictions.
To achieve this, we present \algo, a novel graph-level OOD detection framework. We find that substructure differences commonly exist between ID and OOD graphs, and  design \algo with a series of techniques to encode task-agnostic substructures for effective OOD detection.
Specifically, we build a super graph of substructures for every graph, and develop a two-level graph encoding pipeline that works on both original graphs and super graphs to obtain substructure-enhanced graph representations. 
We then devise substructure-preserving graph augmentation techniques to further capture more substructure semantics of ID graphs.
Extensive experiments against 11 competitors on numerous graph datasets demonstrate the superiority of \algo, often surpassing existing methods by a significant margin.  The code is available at \url{https://anonymous.4open.science/r/SGOOD-0958}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies out-of-distribution detection on graph data, which is an under-explored research area in GNNs. The authors propose to exploit the substructure information that is invariant between in-distribution and out-of-distribution to endow the model with the OOD detection capabilities. To this end, the authors resort to constructing a super graph of substructures, augmentation for graph data and contrastive loss designs. Experiments with comparison with several SOTA models verify the effectiveness of the model.

### Strengths
1. The proposed method seems novel and reasonable

2. The paper is well written and clearly presented

3. The experiment results are strong given the comparison with several SOTA methods

### Weaknesses
1. The proposed method seems incremental and redundant

2. Some of the claims are inproperly stated without justification

3. Theoretical contributions are weak

### Questions
1. How is the model sensitive to different substructures as prior information? And how does this impact different tasks and datasets?

2. How are the negative samples for contrastive loss constructed? How is the sensitivity of the model w.r.t. number of negative samples?

3. The authors mentioned that GNNSafe [1], which is the state-of-the-art model for out-of-distribution detection on graphs, cannot be directly compared, can it be stated more clear why GNNSafe is not comparable with the methods in the experiment?

4. The experimental datasets already used are small. How does the model perform on large datasets? What is the computation cost compared with others?

[1] Qitian Wu et al., Energy-based out-of-distribution detection for graph neural networks. International Conference on Learning Representations, 2023.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes novel graph-level OOD detection framework that generates substructure-enhanced representations and uses substructure-preserving graph augmentations for contrastive training.

### Strengths
1. The proposed SGOOD outperforms a number of existing baselines.
2. The design of substructure-enhanced representation learning and augmentation is interesting.
3. The paper is well-organized and clear.

### Weaknesses
1. The proposed substructure learning on graphs is related to identifying and learning causally invariant substructures, which has been studied in some previous works [1-3]. Specifically, while the authors claim task-agnostic substructures, the methods used to identify these substructures, such as motif finding or community detection, often implicitly encode biases related to graph structure, which can be correlated with task-specific information. This raises concerns about whether the identified substructures are truly task-agnostic or if they inadvertently capture task-related patterns, thus limiting the generalizability of the approach.
2. As for Substructure-Preserving Graph Augmentations, although it perserves substructures, it might change the semantics of graphs. The augmentation strategy, while preserving the identified substructures, could introduce noise or alter the overall graph semantics in ways that are not beneficial for OOD detection. For instance, adding or removing edges while maintaining substructures might disrupt higher-order relationships or global graph properties that are crucial for distinguishing between in-distribution and out-of-distribution samples. This could lead to models that are robust to substructure changes but sensitive to other types of semantic shifts.

### Questions
How can the proposed SGOOD ensure semantically meaningful substrctures extracted by predefined methods? Why not using other learning based techniques like hypergraph learning, graph pooling or causal learning to extract substructures?

### Soundness
3 good

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
Drawing upon the observation of prevalent substructure differences between in-distribution (ID) and out-of-distribution (OOD) graphs, this paper introduces SGOOD, a graph-level OOD detection framework. SGOOD enhances OOD graph detection by incorporating mpre substructure information into ID graph representations. It achieves this through the creation of super graphs of substructures, the implementation of a two-level graph encoding pipeline, and the utilization of three graph augmentation techniques for graph representation. Extensive experiments demonstrate the effectiveness of SGOOD in graph-level OOD detection tasks.

### Strengths
1.	The paper presents a well-structured writing.
2.	It incorporates state-of-the-art graph-level OOD detection algorithms in comparative experiments.
3.	The paper explores an intriguing and relatively unexplored research area, emphasizing the importance of graph-level OOD detection.

### Weaknesses
1. The motivation to improve graph-level OOD detection by encoding more substructure information into graph representations is unclear.
2. The notion that encoding more substructure information into graph representations will enhance graph-level OOD detection faces skepticism. In practice, theoretically more powerful GNNs often under-perform their 1-WL equivalent counterparts across various graph datasets [1]. This is due to the fact that, in cases where node attributes can function as supplements to structural information, nearly all graphs can be differentiated by 1-WL equivalent GNNs. Substructures do not exist in isolation, and are accompanied by a lot of attribute information. Furthermore, these concerns are verified by the results presented in Table 7. Specifically, more powerful GNNs like NGNN and GNN-AK+ fail to outperform 1-WL equivalent GNNs SAG, TopK, and DiffPool in the graph-level OOD detection task. 
3. This paper lacks a clear definition of the graph distribution, and it does not explore the factors contributing to the distribution differences between ID and OOD graphs. It places excessive emphasis on the influence of substructures in graph-level OOD detection while neglecting the discussion of node attributes. Two graphs with identical structures but distinct node features may exhibit entirely different distributions.
4. The paper does not explicitly delineate the specific contributions of the proposed method, SGOOD, to the graph-level OOD detection task. Given the existence of many  theoretically more powerful GNNs, it remains unclear why SGOOD better than those GNNs in the graph-level OOD detection task. SGOOD appears to resemble a new GNN with powerful expressiveness rather than a specialized GNN that can identify OOD graphs.
5. Author wrote: "For augmentations, intuitively, if more information about training ID data is preserved, it is easier to distinguish unseen OOD data. The substructure-preserving graph augmentations are designed to achieve this. " Please provide further explanation for “more information”. What we need to do is to embed all the information related to the substructure into the graph representation? In [2], authors proposed that encoding the task-agnostic (e.g., graph classification task-agnostic) information into representations can improve the OOD detection task.
6. The current version proposes encoding task-agnostic substructures in the ID graph to improve OOD graph detection—a concept absent in the initial manuscript. This introduction of new elements has given rise to fresh uncertainties for me. Specifically, I question the appropriateness of defining modularity-based substructures as "task-agnostic." The author asserts that these substructures are task-agnostic due to their independence from specific learning tasks, such as graph classification. The assertion may somewhat inaccurate, given that these structures are closely tied to community detection. For instance, graphs within the same class may exhibit highly similar community structures, especially in social networks. The relevance of modularity-based substructures to the graph classification task appears uncertain and contingent upon the specific dataset used.

### Questions
1. Table 1 lacks clarity, making it difficult for readers realize the ID and OOD graphs used in statistics, and these statistical findings rely on prior knowledge.
2. GNNsafe appears to be primarily designed for node-level OOD detection. How can it be implemented at the graph-level?
3. OCGIN, OCGTL, and GLocalKD are predominantly designed for graph anomaly detection, and their use as comparison algorithms may not be entirely appropriate for graph-level OOD detection.
4. Figure 1 does not effectively convey how SGOOD is specifically tailored for the graph-level OOD detection task.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
