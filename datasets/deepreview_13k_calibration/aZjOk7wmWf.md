# Exploring and Unleashing the Power of Message Passing on Heterophilous Graphs

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Graph Neural Networks (GNNs) have demonstrated strong performance in graph mining tasks due to their message-passing mechanism, which is aligned with the homophily assumption that adjacent nodes exhibit similar behaviors. However, in many real-world graphs, connected nodes may display contrasting behaviors, termed as heterophilous patterns, which has attracted increased interest in heterophilous GNNs (HTGNN).
Although the message-passing mechanism seems unsuitable for heterophilous graphs due to the propagation of class-irrelevant information, it is still widely used in many existing HTGNNs and consistently achieves notable success. 
This raises the question: why does message passing remain effective on heterophilous graphs?
To answer this question, in this paper, we revisit the message-passing mechanisms in heterophilous graph neural networks and reformulate them into a unified heterophilious message-passing (HTMP) mechanism.
Based on HTMP and empirical analysis, we reveal that the success of message passing in existing HTGNNs is attributed to implicitly enhancing the compatibility matrix among classes.
Moreover, we argue that the full potential of the compatibility matrix is not completely achieved due to the existence of incomplete and noisy semantic neighborhoods in real-world heterophilous graphs.
To bridge this gap, we introduce a new approach named CMGNN, which operates within the HTMP mechanism to explicitly leverage and improve the compatibility matrix.
A thorough evaluation involving 10 benchmark datasets and comparative analysis against 17 well-established baselines highlights the superior performance of the HTMP mechanism and CMGNN method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a compatibility matrix-enhanced method to improve the expressiveness of graph neural networks on heterophilous graph data, and verifies its validity on 10 benchmark datsets.

### Strengths
Extensive experiments have been conducted, including empirical studies on compatibility matrices for various models. 

The experiments may be convincing based on the demonstration of the details.

### Weaknesses
1. The claim that success of HTGNN is due to "enhancing the compability matrix" is problematical. The compability matrix depicts the relations between classes whose instances are linked together, so naturally better representation (thus better prediction) definitely results in more desirable compability matrix. It seems that compability matrix should be the effect, not the cause.  It would be good to provide more evidence or analysis demonstrating that enhancing the compatibility matrix directly leads to improved representations, rather than being a consequence of them.
2. The theorems and lemmas (e.g., theorem 1) are overlay simple. Most of the results are obvious, without meaningful insights.
3. The motivation of "supplementary neighborhood construction" is not explained in Methodology.
4. No time and space complexity analysis of the proposed method.
5. The claim on "New datasets" introduced by this paper is inappropriate. It should precisely describe what is new about the dataset usage compared to previous work (unified data splitting cannot be the "new"), such as modifications to existing datasets, new combinations, or different preprocessing steps that the authors consider novel. that performs well on both homophilous and heterophilious graphs,
6. why some popular SOTAs like graphSAGE and recently developed methods such as Ref. [1-2]  are not included in comparison? The former performs well on both homophilous and heterophilious graphs, the latter two are also oriented towards heterophily issue.
7. The writing needs improvement. There are some  vague sentences and  non-standard writings,  eg. 232-234, 'it's', 'nodes' neighborhood'.

### Questions
1. Line 59-60, why increasing distinctiveness between rows of compability matrix will enhance node representation? It should be justified. Throughout the paper, I can only see the emphasis on the distinction between diagonal and non-diagonals of compability matrix.
2. Why design weights in the form of Eq. 7? no any intuitions behind.
3. Despite of the supplementary neighborhood construction (which can be viewed as additional label propagation) and the compability matrix optimization component, the performance improvement is still marginal, compared to the baselines in the paper.
4. what does it mean by "k neighborhoods"? how to count the number of neighborhoods for a node in question?

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
This paper examines the effectiveness of message-passing mechanisms in heterophilous graph neural networks (HTGNNs), where connected nodes often display contrasting behaviors. This paper propose a unified heterophilous message-passing (HTMP) mechanism and introduce CMGNN, which enhances the compatibility matrix to address incomplete and noisy semantic neighborhoods.

### Strengths
1. Building a unified codebase for heterophily benchmarks/baselines would greatly benefit community research.

### Weaknesses
 1. **Motivation**: The HTMP framework proposed in this paper does not appear to specifically address the heterophily problem, as the mentioned components like FUSE and COMBINE are generally applicable (for instance, they are used in many works focusing on over-smoothing or over-squashing). Fundamentally, they are not exclusive to the heterophily issue and resemble more a general extension of the message-passing mechanism.

 2. **Experiments**: The experiments in this paper are conducted only on datasets with a relatively small node scale (with a maximum of just over 20,000 nodes), which does not demonstrate the scalability of the proposed method.

 3. **Methodology**

   - The paper's proposed CMGNN does not clarify the specific reasons for selecting components in AGG, COMBINE, and FUSE, namely how your chosen designs can help the proposed HTMP better estimate the compatibility matrix.
   
   - Moreover, the design of these components appears overly manual (e.g., why combine from only the three proposed types of neighbors in COMBINE? Why use concatenation in FUSE but weighted summation in COMBINE?), seeming like a patchwork of existing methods.
   
   - Finally, regarding using the rows of the adjacency matrix as additional node features, I believe this could lead to the model being unscalable (as the number of model parameters increases with the number of nodes) and seems to disrupt the permutation invariance of GNN models.

### Questions
1. Authors mentioned that during training, for efficiency, they only update the compatibility matrix when evaluation performance improves. How much difference in computation time is there between epochs when the CM is updated and when it is not?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper titled addresses the challenge of using GNNs on heterophilous graphs, where connected nodes often belong to different classes, defying traditional GNNs' homophily-based assumptions. It proposes the HTMP mechanism, a unified framework that improves message passing for such graphs by enhancing the compatibility matrix between classes. Additionally, the paper introduces CMGNN, a new GNN model under HTMP that explicitly leverages and refines the compatibility matrix to overcome issues related to noisy and incomplete semantic neighborhoods. Extensive benchmarking across various datasets and comparisons with different baselines validate CMGNN's effectiveness and the benefits of the HTMP approach in heterophilous settings.

### Strengths
1. **Unified Framework**: HTMP provides a cohesive structure for message passing in heterophilous GNNs, enabling flexibility and adaptability across different graph structures.

2. **Compatibility Matrix Enhancement**: CMGNN explicitly optimizes the compatibility matrix, effectively improving message relevance and class separability on heterophilous graphs.

3. **Comprehensive Benchmarking**: Extensive evaluations on 10 diverse datasets against 17 baselines validate CMGNN’s superior performance, demonstrating robustness in real-world heterophilous scenarios.

### Weaknesses
1. My primary concern with this paper is the Compatibility Matrix (CM). While the CM captures the likelihood of connections between classes in a graph, aiding message-passing in heterophilous GNNs, it closely resembles the attention mechanism by determining importance between different classes, rather than nodes. Additionally, the concept is not novel, as it has been employed in prior work, such as CPGNN [1]. Could the authors clarify the key differences introduced in this paper?

2. Although this paper focuses on message-passing GNNs, recent advances in spectral GNNs have shown competitive performance on heterophilous graphs. Were comparisons with spectral baselines like BernNet [2] and ChebNetII [3] considered? If spectral GNNs demonstrate superior performance, what is the rationale for focusing on message-passing GNNs?

3. In Table 3, “CMGNN” achieves identical performance to “W/O DL” on three datasets, including identical standard deviations, which seems unlikely given the exclusion of the “DL” component. Could the authors provide insights into this outcome?

4. Figure 8 is not in PDF format, making it appear blurred when zoomed in. A PDF version would enhance clarity.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies message passing on heterophilic graphs and claims that the compatibility matrix is the key to the message-passing mechanism. Based on the compatibility matrix, the authors propose a new framework (i.e., CMGNN). The experiments show that CMGNN is superior.

### Strengths
- The experiments in this paper show the superiority of the proposed method.

### Weaknesses
 - The paper lacks explanations in many key places, such as why A^{sup} and B^{sup} can supplement effective neighbor information. And some operations are wrong, such as the A^{sup} and B^{sup} \in R^{N*K}, while the Z is  R^{N*dr}, which can not conduct the inner-product operation in Eq. (9).
- Why A^{sup} is set to all 1? The authors need to explain.
- This paper is hard to read. Symbols are confusing, and symbols that appear for the first time are not explained. For example, what is H in Eq.(5)? what is \wave_{C} in Eq.(6)?

Overall, this paper is not solid, the motivation lacks verification, and the method is not clearly described. I tend to reject this paper.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
