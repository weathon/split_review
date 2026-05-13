# Multi-Label Node Classification with Label Influence Propagation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Graphs are a complex and versatile data structure used across various domains, with possibly multi-label nodes playing a particularly crucial role. 
Examples include proteins in PPI networks with multiple functions and users in social or e-commerce networks exhibiting diverse interests. 
Tackling multi-label node classification (MLNC) on graphs has led to the development of various approaches. Some methods leverage graph neural networks (GNNs) to exploit label co-occurrence correlations, while others incorporate label embeddings to capture label proximity. However, these approaches fail to account for the intricate influences between labels in non-Euclidean graph data.
To address this issue, we decompose the message passing process in GNNs into two operations: propagation and transformation. 
We then conduct a comprehensive analysis and quantification of the influence correlations between labels in each operation. 
Building on these insights, we propose a novel model, Label Influence Propagation (LIP). 
Specifically, we construct a label influence graph based on the integrated label correlations. 
Then, we propagate high-order influences through this graph, dynamically adjusting the learning process by amplifying labels with positive contributions and mitigating those with negative influence.
Finally, our framework is evaluated on comprehensive benchmark datasets, consistently outperforming SOTA methods across various settings, demonstrating its effectiveness on MLNC tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Label Influence Propagation (LIP), a novel approach for multi-label node classification (MLNC) on graphs. The key innovation is analyzing and leveraging the mutual influences between different labels, rather than just label correlations. The authors decompose the message passing process into propagation and transformation operations to quantify label influences, construct a label influence graph, and dynamically adjust the learning process based on positive and negative label interactions.

### Strengths
1. The paper introduces a new way to analyze label relationships by examining their mutual influences rather than just correlations, supported by empirical observations shown in Figure 1.

2. The work provides a theoretical analysis of how label influences emerge during both propagation and transformation operations in graph neural networks.

3. The proposed LIP framework is plug-and-play compatible with various GNN architectures and shows consistent performance improvements across different datasets and settings.

### Weaknesses
The paper doesn't thoroughly discuss how the method scales with increasing numbers of labels or larger graphs.

### Questions
1. What are the limitations of decomposing message passing into propagation and transformation operations? Are there cases where this decomposition might not hold?

2. How sensitive is the method to the initial construction of the label influence graph?

### Soundness
3

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
3

### Summary
The paper proposes a label influence propagation framework for the multi-label node classification task. Specifically, the paper constructs a label influence graph based on the integrated label correlations. Then, the paper propagates high-order influences through this graph and dynamically adjusts the learning process by amplifying labels with positive contributions and mitigating those with negative influence.

### Strengths
Pros:
1. The paper considers the positive and negative influence of different labels and encourages or suppresses labels that bring positive or negative influences, respectively.
2. The proposed model is a plug-and-play approach, which can be applied to various GNN backbones. 
3. The paper offers a label correlation analysis by dissecting the pipeline into a forward and backward propagation segment.

### Weaknesses
Cons:
1. What is the difference between the label propagation methods? (GMNN: Graph Markov Neural Networks, Combining Graph Convolutional Neural Networks and Label Propagation, Resurrecting Label Propagation for Graphs with Heterophily and Label Noise). The paper should cite and compare with them, and highlight the improvement of the model.
2. Some hyperparameters are important to the model. It is better to give some hyperparameter analysis about the model, such as \alpha, \beta. It is suggested to plot the results showing how performance varies with these parameters and report the chosen values.
3. How does the number of label categories k affect the model? It is recommended to study the effect of the performance.
4. It is highly recommended to give some examples, i.e., the visualization of the positive and negative influence of different labels in the case studies, showing how certain labels positively or negatively influence others and how this affects the model's predictions.
5. It is recommended to give other backbones, such as the most commonly used GIN, to show the effectiveness of the model.
6. It is better to check the label of the axis in the figure. i.e., fig 4c. The label of the x-axis is missing.

### Questions
Please see the above weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper develops a new method LIP that leverages the propagation strategy to obtain high-order label information in the graph for multi-label node classification . The authors provide the theoretical analysis for the motivation and the proposed method. The extensive experimental results show the effectiveness of LIP on multi-label node classification.

### Strengths
1.  This paper is well-written and easy to follow.
2.  The authors provide the theoretical guarantee for the proposed method.
3.  LIP shows promising performance on various datasets.

### Weaknesses
1.  The review of related work is not comprehensive.
2.  The ablation study is inadequate.
3.  The efficiency study is missing.

### Questions
My concerns are mainly from two parts: discussions of relation work and designs of experiments.

1.  Actually, decoupled GNNs\[1,2,3,4,5] have been studied in past a few years. Although the authors are inspired by the theoretical analysis to decouple the propagation module and feature transformation, the previous efforts in decoupled GNNs should be discussed. I have noticed the authors cite APPNP \[1], one of the representative decoupled GNNs, in Line 263. Here, I suggest the authors open a new subsection in Related Work to comprehensively review recent decoupled GNNs.
2.  As a plug-and-play, I suggest the authors try more advanced GNNs as backbones for ablation study, such as advanced decoupled GNNs\[1,3].
3.  Based on Figure 4(b), I suggest the authors conduct ablation on all other datasets to comprehensively validate the contribution of each module.
4.  The author claim the efficiency of the proposed method via the time complexity analysis. Maybe the authors can report the computational cost of each methods, including training time cost and GPU memory cost, to strength this contribution.



[1] Predict then propagate: Graph neural networks meet personalized pagerank, ICLR 2019

[2] On the equivalence of decoupled graph convolution network and label propagation, WWW 2021

[3] Adaptive universal generalized pagerank graph neural network, ICLR 2021

[4] Towards deeper graph neural networks, KDD 2020

[5] Neighborhood Convolutional Graph Neural Network, KBS 2024

### Soundness
3

### Presentation
3

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
This paper proposes the Label Influence Propagation (LIP) method for multi-label node classification on graph-structured data. The main idea is to model both positive and negative influences between labels by separating the message-passing process into distinct propagation and transformation operations. Additionally, LIP constructs a label influence graph to quantify label-wise importance scores.

### Strengths
- This paper is well-motivated, emphasizing the importance of multi-label node classification in various domains. The challenge of label correlations and their potential positive and negative influences in non-Euclidean data is clearly explained.
- The idea of constructing a label graph is interesting.
- Experimental results demonstrate that LIP achieves notable performance gains across datasets of diverse domains, regardless of the backbone GNNs, highlighting its versatility.

### Weaknesses
 **W1.** The writing needs more thorough proofreading. I noticed several grammatical issues, which detract from the overall quality of the paper.

Examples include:
- "Illustrate" should be changed to "Illustration of" in Fig. 3 caption.
- "contain" should be "containing" in line 300.
- "analysis" should be "analyze" in line 313.
- "which can be change" should be "which can be changed" in line 320.

Additionally, table captions should be placed *above* the tables.

Several critical errors related to definitions also needs to be revised:
- "negative influence" should be "positive influence" in line 301.
- The eq. 6 seems inconsistent with the textual explanation of positive influence.
- $\Omega_j$ may need to be revised to $\psi_j$ for consistency.

**W2.** The clarity of the paper needs to be improved. For instance:
- The theoretical justification in Section 4.2 and Appendix A needs more clarity. While the authors assert that the graph structure is a key driver of label influence during propagation, they do not fully clarify how the feature influence $I(i,j)$ and PPR are connected to the proposed label influence metric in the propagation operation. I can infer that positive and negative influences in PPR and feature influence metrics correspond to Equations 6 and 5, respectively, but this connection should be made explicit.
- Additionally, the augmented form of $\text{\textbf A}$ is not clearly defined. Is it a multi-hop adjacency matrix?

**W3.** What are the limitations of the proposed method? The authors didn't include a discussion on the potential limitations of the proposed method.

### Questions
**Q1.** Could you provide additional explanation of the performance enhancement on heterophilous graphs? It's interesting that LIP consistently enhances performance on these datasets, despite the method appearing to be built upon a homophily assumption.

**Q2.** How does the performance change when varying the $\beta$ in eq. 12?

**Q3.** Although the authors state that "multi-label classification on graph data is inherently transductive" in the Appendix, the inductive setting with partially accessible graph structure is more realistic in many real-world applications. While benchmark datasets are commonly used in a transductive manner, it would be straightforward to modify these datasets for the inductive setting by masking nodes and their corresponding edges in different splits. The authors should consider evaluating LIP under such conditions to verify the practical relevance.

### Soundness
3

### Presentation
2

### Contribution
3
