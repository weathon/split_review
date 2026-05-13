# Topology-Informed Graph Transformer

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Transformers have revolutionized performance in Natural Language Processing and Vision, paving the way for their integration with Graph Neural Networks (GNNs). One key challenge in enhancing graph transformers is strengthening the discriminative power of distinguishing isomorphisms of graphs, which plays a crucial role in boosting their predictive performances. To address this challenge, we introduce 'Topology-Informed Graph Transformer (TIGT)', a novel transformer enhancing both discriminative power in detecting graph isomorphisms and the overall performance of Graph Transformers. 
TIGT consists of four components: A topological positional embedding layer using non-isomorphic universal covers based on cyclic subgraphs of graphs to ensure unique graph representation: A dual-path message-passing layer to explicitly encode topological characteristics throughout the encoder layers: A global attention mechanism: And a graph information layer to recalibrate channel-wise graph features for better feature representation.
TIGT outperforms previous Graph Transformers in classifying synthetic dataset aimed at distinguishing isomorphism classes of graphs. Additionally, mathematical analysis and empirical evaluations highlight our model's competitive edge over state-of-the-art Graph Transformers across various benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have introduced an innovative Graph Transformer designed to enhance its discriminative capabilities. This paper demonstrates the ability of the proposed method to effectively distinguish graph isomorphisms through a novel dual-path message-passing layer. Both experimental and theoretical findings substantiate the authors' assertions. Moreover, the study delves into a novel positional embedding layer, aiming to harness topological information more efficiently within the Graph Transformer framework. Experimental evaluations further underscore the method's proficiency in graph-level benchmarks.

### Strengths
1. **Performance.** The introduced methodology exhibits outstanding performance, notably excelling on the CSL dataset and outperforming the expressive power of contemporary Graph Transformers.
2. **Theoretical Development.** Comprehensive theoretical exploration confirms that the proposed approach encompasses and advances beyond current graph transfomers.

### Weaknesses
1. **Novelty.** This work is merely a simple adoption of Cy2C-GNNs with multi-head attention to package that as a graph transformer. The authors present the same layer, except for edge features E^{l-1}, as two different layers in Section 3.1 and Section 3.2. They are called Topological positional embedding layer and Dual-path MPNNs, respectively. After getting node features, then some multi-head attention-based graph transformer.
2. **Scalability.** The authors discuss the scalability of the proposed method regarding the number of nodes, edges, and edges in cyclic subgraphs. The method has a quadratic complexity in terms of the number of nodes. This indicates that the method does not scale well, and it might be difficult to apply it to large-scale graphs.
3. **Applicability.** The authors showed the effectiveness of the proposed methods only on graph-level benchmarks. As the authors mentioned, the demonstration in other-level tasks, such as node classification/clustering, link prediction, and community detection, is needed to check the applicability.

### Questions
1. Provide more baselines, including GNNs. Especially the proposed method is very similar to Cy2c-GNN and the key module is from that paper, but the authors did not compare their method with Cy2-GNN in Table 1, where the proposed method show significant improvement against graph transformers. In Table 2 and 3, Cy2-GNNs are missing. 
2. Please provide more implementation details of Cy2-GNN-1 and compare its computational cost and model [parameters.Is](http://parameters.Is) it fair to compare between TIGT and Cy2-GNN-1.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Topology-Informed Graph Transformer (TIGT), a novel graph transformer architecture designed to improve the discriminative capability for detecting graph isomorphisms. The TIGT model consists of four key components: a topological positional embedding using cyclic subgraphs of graphs, a dual-path message-passing layer, a global attention mechanism, and a graph information layer. Experimental results on various graph classification tasks illustrate the effectiveness of the proposed method.

### Strengths
- The writing of this paper is easy to follow.
- The problem of strengthening the discriminative power of distinguishing isomorphisms of graphs is crucial.
- This paper conducts extensive experiments.

### Weaknesses
- Originality/Novelty: The main theoretical results (Theorem 3.1 and Theorem 3.2) are mainly based on previous work (Choi et al., 2023).
- The assumptions made in Theorem 3.3, which requires two graphs to have the same number of nodes and edges, and Theorem 3.4, which assumes that all graphs have the same number of nodes with degree $d$, may have limitations in practical applications. 
- It would be valuable if the authors could discuss the presence of cyclic structures in graph datasets and its impact on the proposed architecture's performance, whether it is missing or not.
- Ablation study: The authors have provided an ablation study for key components of the method. However, the topological positional embedding layer, the main contribution of this paper, appears to have a marginal effect.
- Although the authors have provided an analysis of the computational complexity for the proposed method, they have not provided empirical results regarding running time compared to baselines. I would suggest the authors also measure the running time of the method and other baselines.
- Baselines: Some baselines on graph transformer are either missing or not adequately discussed:
1. Kong, Kezhi, et al. "GOAT: A Global Transformer on Large-scale Graphs." ICML 2023.
2. Zhang, Zaixi, et al. "Hierarchical graph transformer with adaptive node sampling." NeurIPS 2022.

### Questions
See weaknesses above

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
Current graph transformers lack the ability to distinguish isomorphisms of graphs, thus affecting the predictive performance of the methods. To address this problem, this paper proposes Topology-Informed Graph Transformer (TIGT). TIGT contains four components: a topological positional embedding layer, a dual-path message-passing layer, a global attention mechanism, and a graph information layer. Also, a mathematical analysis of the discriminatory ability of TIGT is given in this paper.

### Strengths
1.This paper is well structured.
2.In this paper, experiments are conducted on several datasets and a rich theoretical proof is given.

### Weaknesses
1.Lack of review of related work and comparison of TIGT with other work.
2.A graph is vertex-biconnected if it is connected and does not have any cut vertex. The definition of vertex biconnected in this paper is wrong.
3.The case used in Appendix A.2 for the proof of Theorem 3.2 is too particularized, so that the generalization of the theory and the proof cannot be guaranteed.
4.Missing ablation of the component “global attention layer” in ablation study.
5.The performance improvement of TIGT is not significant and in many cases it is not as good as GRIT.

### Questions
1.Can you describe the main innovations of your method compared to previous graph transformer methods?
2.The theoretical proof of Theorem 3.1 in Appendix A.1 is highly similar to the reference[1], can you specify the innovation of the theory in this paper?
3.Are the values shown in Table 1 the F1 value? How are the results obtained for the TIGT achieve 100% with variance 0.0? How are the results obtained for GRIT+RRWP?

References:
[1]Yun Young Choi, Sun Woo Park, Youngho Woo, and U Jin Choi. Cycle to clique (cy2c) graph
neural network: A sight to see beyond neighborhood aggregation. In The Eleventh International
Conference on Learning Representations, 2023.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
