# Oversmoothing as Loss of Sign: Towards Structural Balance in Graph Neural Networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Oversmoothing is a common phenomenon in a wide range of graph neural networks (GNNs), where node representation becomes homogeneous and thus model performance worsens as the number of layers increases. Various strategies have been proposed to combat oversmoothing, but they are based on different heuristics and lack a unified understanding of their inherent mechanisms. In this paper, we revisit the concept of signed graphs and show that a wide class of anti-oversmoothing techniques can be viewed as the propagation on corresponding signed graphs with both positive and negative edges. Leveraging the classic theory of signed graphs, we characterize the asymptotic behaviors of existing methods and reveal that they deviate from the ideal state of structural balance that provably prevents oversmoothing and improves node classification performance. Driven by this unified analysis and theoretical insights, we propose Structural Balanced Propagation  (SBP) where we explicitly enhance the structural balance of the signed graph with the help of label and feature information. We theoretically and empirically prove that SBP can improve the structural balance to alleviate oversmoothing under certain conditions. Experiments on synthetic and real-world datasets demonstrate the effectiveness of our methods, highlighting the value of our signed graph framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores the phenomenon of oversmoothing that is prevalent in GNNs, where the node representations become homogenized as the number of network layers increases, leading to a degradation of model performance. Many strategies have been proposed to address this problem, but they are based on different heuristics and lack a unified understanding. By revisiting the concept of signed graphs, this paper shows that a wide range of anti-oversmoothing methods can be considered as propagation over the corresponding signed graphs containing positive and negative edges. Using structural balance theory, the authors describe the asymptotic behavior of existing methods and reveal that they deviate from the ideal structural balance graph that effectively prevents oversmoothing and improves node classification performance. Driven by this unified analysis and theoretical insights, the authors propose structural balance propagation (SBP), which explicitly designs the addition of negative edges to improve the structural balance of the graph and thus prevents undesirable oversmoothing across different classes. Experimental results on synthetic and real-world datasets confirm the effectiveness of the proposed method.

### Strengths
Originality: this paper shows how existing anti-oversmoothing methods can be understood from the perspective of signed graphs and introduces a new propagation method SBP. This not only provides a novel perspective on existing methods, but also proposes a new solution to the oversmoothing problem, which has a nice originality.

Quality: the article systematically analyzes a variety of anti-oversmoothing methods and also provides theoretical and empirical validation of the proposed SBP method to demonstrate its effectiveness. The experimental part uses both synthetic and real-world datasets to demonstrate the effectiveness of the methods. The overall quality is good.

Clarity: the paper performs well on clarity. The proposed theorems are all proved clearly, and the background and previous proposed methods are discussed comprehensively.

Significance: this paper not only provides a new approach to understanding and solving the oversmoothing problem, but also provides a unifying framework for existing anti-oversmoothing methods and promotes a deeper understanding of the mechanisms behind the oversmoothing phenomenon in GNNs. The significance of this work lies in the fact that it not only improves our understanding of existing techniques, but also proposes promising new tools to deal with practical problems.

### Weaknesses
Although the experiments show the superior performance of the SBP method on a wide range of datasets, an in-depth analysis of some specific cases is missing, e.g., why the Cornell as a heterogeneous dataset decreases rapidly as the K grows does not provide an explanation. Further analysis could help understand the behavioral patterns of SBP under different conditions and how to optimize its performance. The paper proposes the SID as a measure of the degree of structural balance, but it does not specifically show how to utilize the SID in practice to guide the design or adjustment of SBPs. If some examples can be provided to show how to optimize SBPs according to SID, the combination of theory and practical application will be closer.

In lines 361 and 362, the A_f is defined as -XX^T, which means A_f is a negative matrix. This means that all nodes are attracting each other rather than repelling, with the level of attraction depending on the similarity between node features. This seems quite different from the Label-enhanced SBP. Could you explain it in more detail? Additionally, it seems to me that the feature-enhanced SBP essentially uses an attention mechanism to strengthen connections between nodes with similar features. Wouldn’t using GAT yield good results in this case? In the experiments, only GCN-related methods were compared.

In line 394, the dimension of H^T H is d×d, which is different from A ̂ (dimension is n×n) in Equation (7). How do you solve this dimension gap?

In Figure 3 (a) Cornell, the Acc decreases rapidly as the K grows. Could you explain the reason?

In line 469, different K range should be used for different datasets. I think this is a spelling mistake and please correct it.

### Questions
In lines 361 and 362, the A_f is defined as -XX^T, which means A_f is a negative matrix. This means that all nodes are attracting each other rather than repelling, with the level of attraction depending on the similarity between node features. This seems quite different from the Label-enhanced SBP. Could you explain it in more detail? Additionally, it seems to me that the feature-enhanced SBP essentially uses an attention mechanism to strengthen connections between nodes with similar features. Wouldn’t using GAT yield good results in this case? In the experiments, only GCN-related methods were compared.

In line 394, the dimension of H^T H is d×d, which is different from A ̂ (dimension is n×n) in Equation (7). How do you solve this dimension gap?

In Figure 3 (a) Cornell, the Acc decreases rapidly as the K grows. Could you explain the reason?

In line 469, different K range should be used for different datasets. I think this is a spelling mistake and please correct it.

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
The paper presents a unified viewpoint of previously proposed methods that mitigate the oversmoothing problem in graph representation learning through the lens of message passing on signed graphs. The authors then state that structurally balanced graphs are a sound solution to oversmoothing, and proposed two algorithms that edit the input graph to be more structurally balanced. Synthetic experiments suggest that the proposed methods indeed increases the overall structural balance (measured in the SID metric). On real-world datasets, the proposed algorithms are illustrated to perform competitively.

### Strengths
- The paper presents a unified treatment of existing solutions to oversmoothing
- The paper proposes structural balance as a way to compare different existing solutions
- The proposed method is empirically effective

### Weaknesses
 - While this might be an unavoidable problem, the analysis in this paper requires the linear GNN assumption, see my questions below. 
- In line 299-300 the authors state that structural balanced graphs can **completely** alleviate oversmoothing. Is this somewhat overclaimed? If my understandings are correct, theorem 4.3 essentially states that the graph representations mix over blocks in the graph, provided that inter-block connections are negative edges. I am not much convinced about whether this implies a valid solution to oversmoothing. As for example, theorem 1 in [1] shows that GCN representations mix over connected components, which is different from theorem 4.3 in that they require a perfect block structure of the input graph. Therefore, it might help to state formally what is a valid definition of oversmoothing, and why structurally balanced graphs indeed solve the problem.


### Questions
- As I mentioned in the weakness section, the paper relies heavily on linear GNNs. I understand that theoretically showing results over non-linear GNNs are hard. But I think there shall be empirical evidences suggest that the analysis of this paper indeed sheds light on nonlinear GNNs. 
- The proposed SBP methods edit the input graph to have smaller SID. I am curious about a more primary question: How is SID related to empirical performance? Are algorithms with lower SIDs, say, over Cora, more performant than others?
- I am confused by the "scalability of SBP" section: What does it mean to *reorder matrix multiplications ... to preserve the distinctiveness of node representations across feature dimension?*


[1]. Oono, Kenta, and Taiji Suzuki. "Graph neural networks exponentially lose expressive power for node classification." arXiv preprint arXiv:1905.10947 (2019).

### Soundness
2

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
2

### Summary
This paper presents a novel perspective on the oversmoothing problem in Graph Neural Networks (GNNs) through the lens of signed graphs. The authors make three main contributions: They unify existing anti-oversmoothing techniques by showing they implicitly add negative edges to the original graph. Introduce structural balance theory to characterize ideal propagation behavior that prevents oversmoothing. Propose two new methods (Label-SBP and Feature-SBP) that explicitly design negative edges to improve structural balance and prevent oversmoothing
The work provides both theoretical analysis and empirical validation on synthetic and real-world datasets, demonstrating superior performance compared to existing approaches.

### Strengths
1. Theoretical Innovation:
- Novel theoretical framework connecting oversmoothing to signed graphs
- Rigorous mathematical analysis of structural balance properties
- Clear theoretical justification for why existing methods may fail and how the proposed solutions work

2. Unification of Existing Work:
- Comprehensive analysis showing how various existing anti-oversmoothing techniques can be viewed through the lens of signed graphs
- Insightful table comparing different methods' implicit positive and negative graph components
- This unification provides valuable intuition for understanding existing approaches

3. Practical Solutions:
- Two concrete, parameter-free methods (Label-SBP and Feature-SBP) that are simple to implement
- Solutions work for both homophilic and heterophilic settings
- Empirical validation on 9 different datasets shows consistent improvements

4. Clear Presentation:
- Well-structured paper with logical flow
- Helpful visualizations (especially Figure 1)
- Clear connection between theory and practice

### Weaknesses
 1. Limited Analysis of Computational Complexity:
- The paper lacks detailed discussion of computational overhead introduced by the proposed methods. Specifically, the analysis should include the time complexity of constructing the signed graph and the impact of negative edge propagation on overall runtime. No runtime comparisons with existing approaches are provided, particularly for the proposed Label-SBP and Feature-SBP methods.

2. Empirical Validation Gaps:
- While 9 datasets are used, most appear to be standard benchmark datasets. There is a lack of experiments on very large-scale graphs with millions of nodes and edges, or on graphs with specific structural properties that might challenge the proposed methods. Limited testing on industrial applications further restricts the generalizability of the findings. No ablation studies are provided that examine the individual contributions of the positive and negative graph components, or the impact of different negative edge construction strategies.

3. Theoretical Assumptions:
- Some theoretical results rely on specific conditions that may not hold in practice, such as the assumption of linear propagation and completely structurally balanced graphs. The paper does not adequately discuss the practical implications when these assumptions are violated, or how the performance of the proposed methods might degrade under non-ideal conditions. The metric SID (Structural Imbalance Degree) is introduced, but its practical utility and the sensitivity of the methods to variations in SID are not thoroughly explored.

### Questions
How does the computational complexity of SBP compare to existing methods, especially for large-scale graphs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the issue of oversmoothing in Graph Neural Networks.
The authors propose a unified approach to anti-oversmoothing techniques by utilizing the concept of signed graphs, where both positive and negative edges are considered. 
Through structural balance theory, they show that improving the balance of signed graphs can prevent oversmoothing and enhance node classification. 
They introduce Structural Balanced Propagation (SBP), which uses both label and feature information to improve graph structure. Theoretical and empirical results on various datasets demonstrate SBP’s effectiveness.

### Strengths
1. The idea of viewing over-smoothing from the perspective of the sign-graph is interesting. The results show that many over-smoothing methods can indeed be generalized under the same form, which is promising.

2. I like the cSBM experiments. They demonstrate the effectiveness of the proposed method well.

### Weaknesses
 **1. Incompleteness of Experiments:**  
The experimental evaluation lacks completeness, particularly in terms of benchmark comparisons. The baselines used are outdated, as more recent state-of-the-art methods like GCNII and $\omega$GCN [1] are not considered. In fact, from Table 2 in [1], it is evident that these methods achieve significantly higher results on datasets like Cora, CiteSeer, and PubMed. A more comprehensive table, similar to Table 2 from [1], should be provided for better comparison. Additionally, the results on heterophilic datasets are not convincing, as newer methods, such as those presented in [2], show superior performance.

**2. Over-smoothing Methods Coverage:**  
The selection of anti-oversmoothing methods in Section 3 is limited. While DropEdge is included, more recent methods like DropMessage [3] are ignored. Moreover, the paper overlooks the importance of residual connections, which are extensively explored in methods like GCNII and PDE-GCN, as discussed in [1]. Therefore, the paper does not cover a sufficient range of contemporary techniques aimed at addressing oversmoothing.

**3. Recent Challenges to Over-smoothing:**  
The very premise of oversmoothing has been questioned in recent works [4, 5], which argue that oversmoothing may not exist structurally. If the authors are positioning SBP as a solution to oversmoothing, they should engage with these discussions. Additionally, Table 7 shows that when GCN is combined with SBP, performance degradation is still severe, whereas methods like GCNII and $\omega$GCN do not exhibit such issues. This raises doubts about whether SBP truly mitigates oversmoothing effectively.

**4. Scalability Concerns:**  
The scalability of SBP is not fully explored. There is no complexity analysis or running time comparison provided. Furthermore, referring to the ogbn-arxiv dataset as "large" is misleading; it is not sufficient to demonstrate the scalability of the method. A more rigorous analysis of both space and time scalability is necessary.

### Questions
I'm not sure about the detailed implementation of the norm techniques used in the paper. Are the BatchNorm, contra-norm learnable? If so, will the learnable parameter affect the analysis in Theorem 3.1?

### Soundness
2

### Presentation
3

### Contribution
1
