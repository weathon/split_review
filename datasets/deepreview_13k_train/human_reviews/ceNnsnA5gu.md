# WL-Tree: a New Tool for Analyzing Graph Neural Networks

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
The 1-WL algorithm provides a clean algorithmic model for graph neural networks (GNNs) that run with a message-passing architecture. Previous work compares a GNN against the 1-WL algorithm to analyze its expressiveness, and develops new GNN variants under the guidance of the comparison. In this work, we propose WL-Trees, a new algorithmic model of GNNs. We compute WL-trees using Breadth-First-Searches on the input graph. We show that WL-trees are equivalent to colors computed from the 1-WL algorithm. Despite the equivalence, WL-trees deepen the understanding of a graph’s structural information encoded in node representations. They also serve as an algorithmic model for improved GNNs to analyze their expressiveness from a new angle.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new concept, WL-tree, as a new perspective for analyzing GNNs. It theoretically proves that WL-trees are bijective mapping with the colors given by the 1-WL algorithm. It claims that such a new perspective could bring new understandings of the encoded structural information in GNN node representations.

### Strengths
1. The motivation of analyzing what structural informative is encoded in node representations is important.

2. The formulations of the theorems in the paper are formal, which could be potentially useful for the community.

### Weaknesses
1. Although WL-tree seems to be a new concept, I did not quite get what perspective from which it is important compared to existing 1-WL algorithm results. It is known that message passing GNN, such as GIN, are capturing the rooted subtree around each node, which is exactly the structure captured by 1-WL, as shown in Figure 1 of [1]. As defined in Section 4, the WL-tree proposed in this paper is also such a rooted subtree. The only difference is that the rooted tree in this paper does not include the parent of a node as its child. It is not clear to me why this difference is important and how it brings significant differences compared to existing understanding. Specifically, the paper does not clearly articulate how excluding the parent node in the child list of the WL-tree provides a fundamentally different or advantageous perspective compared to the standard rooted subtrees captured by the 1-WL algorithm. The paper needs to provide a more compelling argument for the novelty and utility of this specific tree construction. 

2. Also, it is unclear what advantages or new understandings can be inspired by this new concept. The paper claims that the WL-tree provides a new analysis tool, but it does not provide concrete examples of how this tool can be used to gain new insights into GNN behavior or design. It is not clear how analyzing GNNs through the lens of WL-trees leads to different conclusions or understandings compared to analyzing them directly through the lens of the 1-WL algorithm. The paper needs to provide specific examples of how the WL-tree analysis can reveal previously unknown properties of GNNs or lead to new model designs. 

3. The experiments only show a simple analysis of two existing GNN models. What new model designs this new concept can lead to? This is not obvious from the reading. I think the experimental section can include deeper analyses or include a model inspired by the introduced WL-tree tool. The current experiments do not demonstrate the practical utility of the WL-tree concept. The analysis of existing models is not sufficient to justify the introduction of a new analysis tool. The paper needs to include experiments that demonstrate how the WL-tree concept can be used to design new and improved GNN models or provide new insights into the limitations of existing models.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the paper, the authors propose a new tree model for GNNs, which they call WL-trees. The key idea of constructing WL-trees is based on a variant of breadth first search that allows to revisit non-parent nodes. Then the authors show that WL trees are equivalent to the 1-WL algorithm in terms of node coloring. They also propose an algorithm to identify subgraphs anchored at nodes which have the same node representations corresponding to a given WL tree. The contributions claimed by the authors are that the proposed WL trees can provide a more intuitive understanding of graph structures learned by message-passing GNNs.

### Strengths
[1] The paper proposes a different perspective to analyse graph structures underlying message-passing graph neural networks. 

[2] The connections between their proposed WL trees and anchored graphs are discussed, along with an algorithm that can identify anchored subgraphs corresponding to a given WL tree.

[3] Two existing GNN models are considered and analyzed in the experiments.

### Weaknesses
 [W1] The proposed method is not well defined. Below are some specific comments:

 - Page 3: The formulations in Equations 3-5 are not consistent. In Equation 3, an anchored subgraph is defined in terms of a set of walks but Equation (5) defines an anchored subgraph as a set of pairs of nodes and walks. Further, the definition of $\dot{\cup}$ is not clearly presented. Also, why $dist(i,j)$ is only less than $\ell$ but $dist(i,k)$ is less than or equal to $\ell$? The inconsistency in the distance constraints for nodes j and k within the same edge set definition is unclear and needs further justification. Specifically, it is not clear why the distance from the anchor node *i* to node *j* must be strictly less than *l*, while the distance from *i* to node *k* can be equal to *l*. This asymmetry in the distance constraints is not explained and raises concerns about the precise definition of the anchored subgraph.

- Page 4: For the function id(·) that maps a tree node to a node in an anchored graph, since a node in an anchored graph may appear multiple times in the tree, is it still a function? The concern here is that the mapping id(·) is not a function in the strict mathematical sense if multiple tree nodes map to the same graph node. This needs clarification to ensure the mapping is well-defined.

[W2] The proposed WL-trees differ from the computational tree structures of message-passing GNNs mainly in disallowing the revisit of the parent nodes. The authors claim that the proposed WL-trees are equivalent to the 1-WL algorithm in terms of node coloring. This does not seem correct. Consider a counter-example, where G is a graph consisting of two triangles and H is a cycle of length 6. These two graphs cannot be distinguished by 1-WL, but would have different WL-trees proposed in the paper. The claim of equivalence to 1-WL is problematic. The counterexample highlights that the proposed WL-trees can distinguish graphs that 1-WL cannot, indicating a fundamental difference in their expressive power. This discrepancy undermines the claim that WL-trees provide a faithful representation of the information captured by 1-WL.

[W3] The tree structures underlying message-passing GNNs and their connection to 1-WL have been well studied in the literature. It is unclear why the proposed WL-trees can provide a more fine-level analysis of the expressiveness of node representations learned by message-passing GNNs. In particular, the proposed WL-trees are not equivalent to 1-WL (see the above point [2]). The novelty and utility of the proposed WL-trees are not well-justified, especially given existing work on analyzing GNNs via computational trees and their relation to 1-WL. The lack of equivalence to 1-WL further weakens the argument for WL-trees providing a more fine-grained analysis.

[W4] In what kinds of scenarios will the proposed algorithm 1 be useful? The practical application of Algorithm 1 is unclear. The paper does not provide concrete examples or use cases where this algorithm would be beneficial. Without a clear understanding of its utility, the algorithm's contribution is questionable.

[W5] For the section 6, what are the justifications for selecting CLIP and Nested GNN? There are a large number of GNN models developed in the literature. I don't see why these two particular GNN models are selected for analysis. The choice of CLIP and Nested GNN for experimental analysis is not well-motivated. The paper needs to justify why these specific models were chosen over other GNN architectures. Without a clear rationale, the experimental results may not be generalizable or representative of GNNs as a whole.

[W6] Theorem 12 and Theorem 13 look confusing. Why is max used in Equation 8? Is the notation $G(j,h)$ defined? Also, the expressive power of Nested GNN goes beyond 1-WL, but the WL-trees proposed in the paper are claimed to be equivalent to 1-WL. So why does Theorem 13 state that there is a bijective mapping between WL-trees and their node embeddings calculated by Equation 10? The use of the max operation in Equation 8 is not explained. The notation $G(j,h)$ is undefined, making the theorem difficult to understand. Furthermore, the claim of a bijective mapping between WL-trees and node embeddings for Nested GNN is inconsistent with the fact that Nested GNN has expressive power beyond 1-WL, while WL-trees are claimed to be equivalent to 1-WL.

[W7] For the statement "A smaller count or conditional entropy means that the WL-tree can better identify a node’s surround structure", is any theoretical justification? Analysing GNN models using average counts of anchored subgraphs and the conditional entropy of anchored graphs look ad hoc. The connection between the proposed metrics (average counts and conditional entropy) and the ability of WL-trees to identify a node's surrounding structure lacks theoretical grounding. The analysis seems ad hoc without a clear justification for why these metrics are appropriate measures of a WL-tree's discriminative power.

### Questions
W1 - W7

### Soundness
1 poor

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents WL-tree, a tool for analyzing graphs based on the multiset of walks of a given length that leave a node. An algorithm that identifies whether a certain node satisfies a given WL tree is also presented. Finally, a working implementation of two graph neural networks (GNNs) that enhance the expressiveness of message-passing GNNs with node id representations.

### Strengths
The presentation is good.

### Weaknesses
The tool presented in the paper, WL tree, essentially corresponds to the well-notion of tree unravelling from a node in a graph. That this notion is equivalent with WL coloring is absolutely folklore and has been used in many papers for decades. As such, the paper does not bring any new conceptual contribution into the picture. Theoretically speaking, all results in the paper are simple exercises. 

The authors also show a poor understanding of the related literature. A concrete example is when they mention that WL has the same expressive power than *guarded* FO_2^\cnt. This is simply not true, and it is not what Cai et al have proved. They have shown that the distinguishing expressive power of WL is exactly the same as FO_2^\cnt (the guarded version is, in fact, weaker). The results by Barceló et al do not concern this notion of expressive power, but a different one. They show that each guarded FO_2^\cnt unary formula can be turned into an equivalent GNN over the set of all graphs. That is, the result by Barceló et al is *uniform*, while the one by Cai et al. is not (and neither is the result of Morris et al.)

### Questions
I have no concrete questions. The paper is below the bar in my view.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
