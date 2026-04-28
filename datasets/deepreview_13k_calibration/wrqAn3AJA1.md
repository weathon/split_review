# Everybody Needs a Little HELP: Explaining Graphs via Hierarchical Concepts

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Graph neural networks (GNNs) have led to major breakthroughs in a variety of domains such as drug discovery, social network analysis, and travel time estimation. However, they lack interpretability which hinders human trust and thereby deployment to settings with high-stakes decisions. %
A line of interpretable methods approach this by discovering a small set of relevant \textit{concepts} as subgraphs in the last GNN layer that together explain the prediction. This can yield oversimplified explanations, failing to explain the interaction between GNN layers. To address this oversight, we provide HELP (\textbf{H}ierarchical \textbf{E}xplainable \textbf{L}atent \textbf{P}ooling), a novel, inherently interpretable graph pooling approach that reveals how concepts from different GNN layers compose to new ones in later steps.
HELP is more than 1-WL expressive and is the first non-spectral, end-to-end-learnable, hierarchical graph pooling method that can learn to pool a variable number of arbitrary connected components.
We empirically demonstrate that it performs on-par with standard GCNs and popular pooling methods in terms of accuracy while yielding explanations that are aligned with expert knowledge in the domains of chemistry and social networks.
In addition to a qualitative analysis, we employ concept completeness scores as well as concept \textit{conformity}, a novel metric to measure the noise in discovered concepts, quantitatively verifying that the discovered concepts are significantly easier to fully understand than those from previous work.
Our work represents a first step towards an understanding of graph neural networks that goes beyond a set of concepts from the final layer and instead explains the complex interplay of concepts on different levels

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces HELP (Hierarchical Explainable Latent Pooling), a new graph pooling method that enhances the interpretability of Graph Neural Networks (GNNs) by elucidating how concepts across different GNN layers combine to form complex representations. HELP is the first non-spectral, end-to-end learnable hierarchical graph pooling method that can handle a variable number of connected components and demonstrates competitive accuracy with standard GNNs. The method's efficacy is quantitatively validated using novel metrics like concept completeness and conformity and qualitatively through expert-aligned explanations in domains such as chemistry and social networks, marking a significant advancement in making GNNs more interpretable.

### Strengths
1. Addressing the Challenge of Explainability in Graph Neural Networks:
The paper tackles a pressing and highly relevant issue in the field of graph learning – the need for explainability. Explainability is crucial in deploying GNNs for real-world applications where understanding the model's decision-making process is as important as the accuracy of its predictions.

2. Innovative Approach to Learning Hierarchical Structures:
The introduction of a hierarchical structure to improve explainability is a novel and compelling approach. Hierarchical interpretations of data are more aligned with human cognitive processes, making them a natural fit for explainability purposes.

### Weaknesses
1. Inadequate Methodological Detail:
The paper falls short in providing essential details in the method section, notably omitting some crucial symbols and function definitions (See Question 1). This lack of clarity impedes the reader's ability to fully comprehend the proposed interpretative framework for graph neural networks.

2. Insufficient Coverage of Related Works:
Although the paper mentions the DiffPool method, it neglects to discuss other works in the domain of learnable pooling in GNNs. Specifically, the paper [1] also proposed a learnable clustering approach which is highly relevant to the context of the presented work.

[1] Brain Network Transformer, NeurIPS 2022

3. Over-simplification of Synthetic Datasets:
The nearly perfect classification accuracy on synthetic datasets raises concerns about the complexity and applicability of the test environment. Such high performance suggests that the synthetic dataset may be too simplistic to effectively challenge and evaluate the proposed model.

4. Lack of Explicit Demonstration of Explainability Improvement:
The paper posits that high concept conformity leads to improved explainability but fails to demonstrate this relationship concretely. To substantiate such claims, the authors should provide empirical evidence or case studies that illustrate how explainability is enhanced as a direct result of increased concept conformity (See Question 3).

### Questions
1. In the Algorithm Section, please provide detailed definitions of used symbols and functions, for example, n_{blocks}, C, CONCOMP().
2. Please enlarge the font size in Figure 2, and can you explain the X and Y axes in detail?
3. Can you provide a case study to show which benefit the high Concept conformity can bring?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a hierarchical pooling procedure. At each step, the model processes multiple GNN layers at each step, performs clustering on representation, and merges connected components within the same cluster. By analyzing the relevant node mergers, we can gain insights into the model's decision-making process. In addition, this paper proposes a novel metric concept conformity to measure the noise level in the discovered concepts.

### Strengths
1) The proposed method takes into account the interactions between GNN layers, capturing the model's reasoning process from a hierarchical perspective, which refines the interpretability. In Section 3.1, the mentioned global clustering and merging clusters can enhance the effectiveness of clustering.

2) The paper is well written and easy to understand.

3) The paper studies an interesting problem that helps explain graphs.

### Weaknesses
1) In the experimental section, a synthetic hierarchical dataset is used instead of the commonly used BA-Shapes and BA-Community datasets. Since conventional datasets do not exhibit a hierarchical structure, does this mean that the proposed method cannot be applied to these datasets and real-world datasets, and therefore has limitations? In Table 1, for the real-world dataset, HELP does not perform very well.

2) The proposed synthetic hierarchical dataset is worth discussing. The accuracy of the model may be so high that the prediction of the dataset may be easier.

3) Intuitively, as the number of layers in the model increases, the model will capture fine-grained information. However, the method proposed in this paper pools the input graph to a coarser representation, so does it ignore the fine-grained features of the nodes at high-level layer?

4) For the metric Concept Conformity, i don't understand the formula, from the interpretation of the formula conf(c) should always be 1. In addition, will there be a case where two noise clusters are larger than the threshold t after merging, and then what should be done with these noise clusters?

### Questions
Please see the questions given in the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper achieved such progress:
1) proposes a new non-spectral interpretable-by-design pooling method called “HELP” to demonstrate how concepts from different GNN layers interplay with each other and compose a new concept in later GNN layers. This method can give explanations to the model prediction in terms of concepts and the analysis of the hierarchical structure of graphs can be performed. 
2) proposes a novel metric called “concept conformity” which measures the purity of a given concept to check if the discovered concepts by HELP are meaningful. 
3) demonstrate a method of GNN explainability via an interpretable GNN architecture design approach.

### Strengths
1. The motivation of this paper is clear, that is to find a GNN explainability method through neural network design and the writing style of this paper is also clear enough for readers to follow.
2. This method offers some inspiration on how to deal with GNN explainability. By searching for high-level explainable concepts, this method can thus identify the relevant subgraphs in the model decision-making process.
3. HELP uses K-Means as part of the algorithm, which is intrinsically more interpretable. Therefore, it can generate a more interpretable explanation of the model prediction compared to other black-box explainers.

### Weaknesses
1. The paper lacks context in the introduction of the part 3.2 “gradient flow”, the readers find it hard to understand how this part is related to other parts in this paper. There is no background information about why it is necessary to introduce “gradient flow” in this part and how it relates to other parts of this paper.
2. The explanation and description of how HELP works is insufficient. For instance, In part 3, this paper gives a limited description of how to implement “pooling” in this method (what is the exact way to apply a series of pooling blocks to the input graph, and how they are applied to different GNN layers?). Similarly, the description of Algorithm 1 is limited and readers might be confused about the purpose of each step in this algorithm (e.g., What is CONCOMP and why should we use it in this method?).
3. Though focusing on explainability, the experiment result shows that HELP doesn’t outperform other approaches in model accuracy, so the quality of this method in practice is questioned. The author needs to give more persuasive experiment results to show the feasibility of HELP.
4. The metric concept conformity is not applicable for all methods, e.g., ASAP generates NA for this metric. This means that the applicability of concept conformity requires further exploration.
5. This paper still needs to use other commonly used and standard metrics to measure the quality of generated concepts, instead of solely using two metrics.

### Questions
1. Why the discovered concept-based explanations from HELP can give deeper insight compared to previous works? What makes these discovered concepts better compared to previous methods?
2. How to ensure the process of converting graph embedding into a concept explainable enough after multiple layers of GNN? The concepts are generated after many layers of neural networks, so it’s hard to demonstrate that the concepts are still interpretable enough to explain the model prediction.
3. This paper states that “our techniques preserve sparsity” in “paper’s contribution”,  but there is none of any further explanation about this point. How is this statement validated by experiments or theories?
4. The accuracy of HELP always lies in 1 standard deviation from the best approach. Does it necessarily mean that some implementation details in HELP can be further revised to make it perform better?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article introduces Hierarchical Explainable Latent Pooling (HELP), an innovative graph pooling method designed to enhance the interpretability of Graph Neural Networks (GNNs). HELP operates by continuously pooling nodes with similar embeddings in the graph, merging these embeddings through average pooling in a hierarchical manner across various levels by k-means. This method allows HELP to identify and elucidate concepts in the input graph pertinent to the model's predictions, with these concepts evolving and increasing in complexity at higher pooling levels. Moreover, this paper designs a new metric Concept Conformity to measure the quality of a concept which is demonstrated better than existing metric in three aspects. Experimental results indicate that HELP matches the performance of leading GNNs while uncovering concepts that are more consistent and in alignment with domain knowledge.

### Strengths
1.	designs a new metric Concept Conformity to measure the quality of a concept which is demonstrated better than existing metric in three aspects.
2.	discusses the benefits of using k-means clustering to identify concepts.

### Weaknesses
1.	The motivation is not strong enough: Why we need identify concept in hierarchical manner?
2.	The representation need to be improved.
	•	The algorithm is very unclear to know how to find concepts.
	•	Many typos and undefined symbols such as V_i, b, CONCOMP .
	•	Unclear description of the synthetic dataset.
3.	Insufficient baseline.  GLGExplainer (Global Logic-based GNN Explainer) [1] is a post-hoc concept-based explanation method as well.
4.	The experiments do not show the advantage of hierarchical pooling which is the main motivation of this article.

### Questions
1.	For the synthetic dataset, you state “The class label is therefore given by (house, {triangle, house, fully connected pentagon})”, could you explain it in detail? 
2.	For the synthetic dataset, what are intermediate nodes?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
