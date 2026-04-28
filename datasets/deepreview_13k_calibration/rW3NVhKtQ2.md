# Test-Time Graph Rebirth: Serving GNN Generalization Under Distribution Shifts

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Distribution shifts between training and test graphs typically lead to the decreased performance of graph neural networks (GNNs) with suboptimal generalization in real-world applications. Despite advances in graph learning under distribution shifts through designing various model architecture development with customized training strategies, existing solutions can be challenging in practical GNN deployment because they often require significant modifications or retraining of the GNNs. To address such challenges, in this work, we propose a novel method, i.e., Test-Time Graph REBirth, dubbed TT-GREB, to effectively generalize the well-trained GNN models to the test-time graphs under distribution shifts by directly manipulating the test graph data. Concretely, we develop an overall framework designed by two principles, corresponding to two submodules: (1) prototype extractor for re-extracting the environment-invariant features of the test-time graph; and (2) environment refiner for re-fining the environment-varying features to explore the potential shifts. Furthermore, we propose a dual test-time graph contrastive learning objective with an effective iterative optimization strategy to obtain optimal prototype components and environmental components of the test graph. By reassembling these two components, we could obtain a newly reborn test graph, which is better suited for generalization on the well-trained GNN model with shifts in graph distribution. Extensive experiments on real-world graphs under diverse test-time distribution shifts could verify the effectiveness of the proposed method, showcasing its superior ability to manipulate test-time graphs for better GNN generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel data-centric approach called Test-Time Graph Rebirth (TT-GREB) to improve the generalization of GNNs under distribution shifts. The method manipulates test graph data directly and does not require modifications to the GNN architecture or retraining. To achieve this, the method decomposes the test graph into environment-invariant and environment-varying components, using a prototype extractor and environment refiner. This leads to the creation of a “reborn” test graph that better matches the training graph distribution, enhancing the GNN’s generalization without altering its original structure. The dual contrastive learning objective and iterative optimization are key to refining the test graph for improved node classification performance.

### Strengths
The paper introduces a practical and innovative solution to the problem of GNN generalization under test-time distribution shifts without requiring retraining or modifications to the GNN model itself. The dual contrastive learning framework is designed to refine test-time graphs by optimizing environment-invariant and environment-varying features. Experimental results on diverse real-world datasets demonstrate that TT-GREB outperforms existing methods.

### Weaknesses
1. The problem setup seems quite contrived. Particularly, it is mostly unclear why a graph could be explicitly decomposed into environment-invariant and environment-varying parts, where the environment-varying variables are upper bounded with a certain notion of discrepancy (which is also not formally defined). While the authors write this as a proposition, it seems more like an (unrealistic) assumption without any support or proof. The lack of a clear definition for the discrepancy metric used to bound environment-varying variables further weakens the theoretical foundation. It would be beneficial to see a more rigorous justification for this decomposition, potentially with empirical evidence or theoretical analysis demonstrating its validity in real-world graph data.

2. There is no guarantee that the proposed Test-time Graph Rebirth as in definition 3.1 can improve out-of-distribution generalization. The definition itself does not inherently imply any improvement in generalization performance. A more detailed explanation connecting the definition to the expected outcomes is needed, along with a theoretical analysis or empirical evidence demonstrating the effectiveness of the proposed transformation in improving generalization under distribution shifts.

3. The method only shows marginal improvement over another data-centric graph ood method. While the experimental results demonstrate some improvement, the gains over existing methods, particularly data-centric approaches, appear to be relatively small. This raises questions about the practical significance of the proposed method, especially considering its complexity. A more thorough comparison, potentially including a wider range of datasets or a more detailed analysis of the performance differences, would be necessary to establish the method's practical value.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a test-time data-centric approach, Test-Time Graph REBirth (TT-GREB), designed to improve the generalization abilities of pre-trained Graph Neural Networks (GNNs) under graph distribution shifts at test time. It presents a method for regenerating test-time graphs by separating environment-invariant features (which capture the core predictive patterns) from environment-varying features (which address distributional shifts).  TT-GREB leverages dual test-time graph contrastive learning objective with self-supervision signals, along with an effective iterative optimization strategy to obtain expressive prototype features and environmental features. Extensive evaluations demonstrate TT-GREB's superiority over state-of-the-art methods in enhancing GNN performance under test-time distribution shifts.

### Strengths
1. The approach seems novel to me. This paper presents an approach to test-time graph rebirth, which contrasts with existing methods by focusing on modifying architectures and training strategies to address distribution shifts. The motivation is also clear to me.
2. The idea to extract environment-invariant features and refine the environment-varying features is reasonable to me.
3. Experiments include various GNN backbones and baselines to compare the performance.

### Weaknesses
1. The experimental results are comparable to the data-centric baseline GTRANS. The improvement is not very evident. Specifically, while the authors claim a notable improvement on the Elliptic dataset, the overall trend across other datasets shows only marginal gains, raising concerns about the general effectiveness of the proposed method. The reported 5.5% and 7.1% F1 score increases on Elliptic with GPR and SAGE models, respectively, are not consistently observed across other datasets, suggesting the method's performance is highly dependent on specific dataset characteristics.
2. The proposed method appears less effective on large-scale datasets, such as the arXiv dataset. For even larger-scale datasets, will the performance be even worse and will the iterative optimization strategy be computationally intensive when the graph sizes are very large? The method's reliance on reweighting edges, which scales quadratically with the number of nodes, is a potential bottleneck for large graphs. The iterative nature of the optimization, involving multiple forward and backward passes through the GNN, further exacerbates the computational burden, making it unclear if the method can scale to graphs with millions of nodes. The memory requirements for storing the reweighting matrices also pose a practical limitation.
3. The captions and ticks in figures are too small for readers to read.
4. Some figures have inconsistent font sizes in their captions (e.g., Figure 4), detracting from the professional presentation.

### Questions
1. Can the method extend to other model architectures like Graph Transformers?
2. In terms of runtime comparison, could the authors provide more detailed comparisons of training and inference times?
3. How well does TT-GREB generalize to larger-scale datasets beyond those used in the paper? Will it hurt the performance or lead to huge time complexity? Could the authors clarify the scalability of the iterative optimization strategy, especially when applied to very large graph datasets?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a data-centric approach called TT-GREB to address the distribution shift in graph learning at test time. Specifically, TT-GREB employs 1. a prototype-extractor module to extract distribution-invariant subgraph, and 2. an environment-refiner module to extract spurious subgraph. The distribution-invariant subgraph, spurious subgraph, and the new graph of the previous two construct a triplet to supervise the graph neural network at test time to mitigate the distribution shift. The prototype-extractor module, environment-refiner module, and the graph neural network are optimized iteratively together. Empirical studies on several datasets show that the proposed TT-GREB can improve the out-of-distribution generalization performance of graph neural network.

### Strengths
Improving graph neural networks (GNNs)' out-of-distribution (OOD) performance is important to their real-world deployment since different distribution shifts may occur in the real world. Although some distribution-invariant GNN architectures have been designed, it is still unrealistic to wish these models to generalize to arbitrary unseen distributions. Adapting GNNs at test time is more realistic and general as it can employ some hints from testing data to guide network generalization. This paper follows the test-time adaptation approach and the proposed method can work well on several datasets.

### Weaknesses
Yet, the reviewer is concerned about some technical details as follows:

1. Why use two modules to extract the distribution-invariant and spurious subgraphs respectively? According to Proposition 1, the distribution-invariant subgraph and spurious subgraph are fully complementary. Thus, using one module to extract any one of the two subgraphs is sufficient to obtain both distribution-invariant and spurious subgraphs. Instead, this paper introduces two modules to extract these two subgraphs. The paper does not provide a clear explanation of why a single module cannot effectively disentangle these subgraphs, especially given their theoretical complementarity. The practical challenges of extracting one from the other, particularly in the context of complex graph structures and non-linear feature spaces, are not adequately addressed.

2. Based on 1, why is G_{te}^{'} different from G_{te}? As G_{te}^{'} is constructed by the distribution-invariant and spurious subgraphs from G_{te},  G_{te}^{'} should be the same as G_{te} according to 1. The construction of G_{te}^{'} is not clearly defined. If it is simply a combination of the extracted subgraphs, it should be identical to the original graph. The paper needs to clarify how G_{te}^{'} is modified or enhanced beyond a simple recombination of the subgraphs.

3. As G_{te}^{'} has a spurious subgraph, why push its embedding closer to the embedding of the distribution-invariant subgraph? The rationale behind aligning the embedding of the modified graph with the distribution-invariant subgraph is unclear, especially if the modified graph contains a spurious component. The paper should clarify why this alignment is beneficial for OOD generalization, given that the modified graph is supposed to contain both invariant and spurious information.

4. EERM is designed to improve the OOD generalization ability of GNNs, why does it underperform most baselines in Table 1?

### Questions
The authors are encouraged to address the concerns in the Weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper,  the authors introduce a novel graph data-centric paradigm for enhancing the ability of well-trained GNNs to real-world graphs experiencing distribution shifts at test time. The uniqueness of this paper lies in the re-operation of the test data to model the invariant features, which are then fed into the trained GNN for prediction. Empirically, experiments are conducted on five datasets and four benchmark networks to verify the effectiveness of the model.

### Strengths
1. The research question is critical
2. It is interesting to design a separate model to capture invariant representations on test data
3. Experimental verification was performed on multiple backbone networks

### Weaknesses
 1. This method can be seen as the process of designing an unsupervised model to extract invariant features during the test phase. However, it is often difficult to perform decoupled learning under unsupervised conditions.
2. This is misleading in Figure 1(a). In the general graph OOD generalization setting, the test graph is not seen during training. The figure may be a problem setting of domain adaptation.
3. This approach does not seem to be limited to graph data. What are the unique challenges for graph data?
4. In the experiment, the comparison method is not new enough, the latest one comes from ICLR2023. At the same time, Figure 5 is a bit difficult to observe, and its readability can be further improved. If new comparative experiments can be provided here, I will consider improving my score.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
